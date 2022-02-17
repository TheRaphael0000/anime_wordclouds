"Cowboy Bebop"
import glob
import itertools
import os

import webvtt
import nltk


p = os.path.dirname(__file__)
colormap = p + "/colormap.png"
mask = p + "/mask.png"


def get_words():
    "Get the words from the whole serie"
    sub_files = glob.glob(p + "/subs/*")
    file_words = [get_words_from_subtitles(f) for f in sub_files]
    words = list(itertools.chain(*file_words))
    return words


def get_words_from_subtitles(file):
    "Get the words from a subtitle file"
    lines = [l.text for l in webvtt.read(file)]
    file_words = [nltk.tokenize.word_tokenize(l) for l in lines]
    file_words = list(itertools.chain(*file_words))
    return file_words
