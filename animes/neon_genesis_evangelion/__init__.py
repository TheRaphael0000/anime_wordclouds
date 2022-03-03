"Neon Genesis Evangelion"
import glob
import itertools
import os

import nltk
import webvtt


def get_words():
    sub_files = glob.glob(__path__[0] + "/subs/*")
    file_words = [get_words_from_subtitles(f) for f in sub_files]
    words = list(itertools.chain(*file_words))
    return words


def get_words_from_subtitles(file):
    "Get the words from the whole serie"
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
