"Darling in the Franxx"
import glob
import itertools
import os

import nltk
import webvtt


p = os.path.dirname(__file__)
colormap = p + "/colormap.png"
mask = p + "/mask.png"


def get_words():
    "Get the words from the whole serie"
    sub_files = glob.glob(p + "/subs/*.vtt")
    file_words = [get_words_from_subtitles(f) for f in sub_files]
    words = list(itertools.chain(*file_words))
    return words


def get_words_from_subtitles(file):
    "Get the words from a subtitle file"
    file_words = []
    for caption in webvtt.read(file):
        file_words.extend(nltk.tokenize.word_tokenize(caption.text))
    return file_words
