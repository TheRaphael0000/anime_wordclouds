"Death Note"
import glob
import itertools
import os

import nltk
from nltk.tokenize import TweetTokenizer
import webvtt


def get_words():
    sub_files = glob.glob(__path__[0] + "/subs/*.vtt")
    words = []
    for f in sub_files:
        words.extend(get_words_from_subtitles(f))
    return words


def get_words_from_subtitles(file, buffer_size=6):
    "Get the words from the whole serie"
    tknzr = TweetTokenizer()
    file_words = []
    previous = []
    for caption in webvtt.read(file):
        text = caption.text
        # weird "Delete"s in the subtitles
        text = text.replace("Delete", "")
        if text in previous:
            continue
        previous.append(text)
        if len(previous) > buffer_size + 1:
            del previous[0]
        file_words.extend(tknzr.tokenize(text))
    return file_words