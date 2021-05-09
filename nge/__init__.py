import glob
import itertools
import os

import webvtt
import nltk
import numpy as np
from PIL import Image


def get_data():
    p = os.path.dirname(__file__)
    print(p)

    sub_files = glob.glob(p + "/subs/*")
    file_words = [get_words_from_subtitles(f) for f in sub_files]
    words = list(itertools.chain(*file_words))

    colormap = p + "/colormap.png"
    mask = p + "/mask.png"

    return words, colormap, mask


def get_words_from_subtitles(file):
    file_words = []
    valid = False
    for caption in webvtt.read(file):
        # Ignore opening and ending
        if "Shounen yo shinwa ni nare" in caption.text:
            valid = True
            continue
        if "To Be Continued" in caption.text:
            break
        if valid:
            file_words.extend(nltk.tokenize.word_tokenize(caption.text))
    return file_words
