from tools import parse_vtt, tokenize, words_processing, wordcloud_visualization

import nltk
from PIL import Image
from pprint import pprint
import glob
import numpy as np
import argparse


def wordcloud_pipline(anime_name, stop_words, words_kept, carving_color):
    nltk.download("stopwords", quiet=True)
    nltk.download("punkt", quiet=True)

    anime_path = f"animes/{anime_name}"

    colormap = Image.open(f"{anime_path}/colormap.png")
    mask = Image.open(f"{anime_path}/mask.png")

    subs = glob.glob(anime_path + "/subs/*.vtt")
    print(f"{len(subs)} subs files loaded")

    text = "\n".join([parse_vtt(f) for f in subs])
    print(f"{len(text)} characters")

    words = tokenize(text)
    print(f"{len(words)} words")

    print("stop words")
    print(stop_words)

    words = words_processing(words, stop_words, words_kept)
    pprint(words, sort_dicts=False)
    print(f"{len(words)} words kept")

    wc = wordcloud_visualization(words, colormap, mask, carving_color)
    wc.save(f"wordclouds/{anime_name}.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Word Cloud Tool')

    colors = {
        "k": np.array([22, 22, 22]),
        "gray": np.array([180, 180, 180]),
        "w": np.array([233, 233, 233]),
    }

    parser.add_argument('folder')
    parser.add_argument('-w', '--words', default=250, type=int)
    parser.add_argument('-c', '--color', default="k", choices=colors.keys())

    args = parser.parse_args()

    stop_words = nltk.corpus.stopwords.words("english")

    wordcloud_pipline(args.folder, stop_words,
                      args.words, colors[args.color])
