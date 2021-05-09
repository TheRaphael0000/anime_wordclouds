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
    lines = [l.text for l in webvtt.read(file)]
    file_words = [nltk.tokenize.word_tokenize(l) for l in lines]
    file_words = list(itertools.chain(*file_words))
    return file_words
