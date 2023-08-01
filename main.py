import animes
from tools import parse_vtt, tokenize, words_processing, wordcloud_visualization

from PIL import Image
from pprint import pprint
import glob
import numpy as np


def wordcloud_pipline(anime_name, words_kept, carving_color):
    anime_path = f"animes/{anime_name}"

    print("loading colormap")
    colormap = Image.open(f"{anime_path}/colormap.png")
    print("loading mask")
    mask = Image.open(f"{anime_path}/mask.png")

    print("loading subs")
    subs = glob.glob(anime_path + "/subs/*.vtt")
    print(f"{len(subs)} subs loaded")

    print("parsing subs")
    text = "\n".join([parse_vtt(f) for f in subs])
    print(f"{len(text)} characters loaded")

    print("tokenizing subs")
    words = tokenize(text)
    print(f"{len(words)} words loaded")

    print("processing words")
    words = words_processing(words, words_kept)
    pprint(words, sort_dicts=False)
    print(f"{len(words)} words kept")

    print("creating vizualisation")
    wc = wordcloud_visualization(words, colormap, mask, carving_color)
    wc.save(f"wordclouds/{anime_name}.png")


if __name__ == '__main__':
    blackish = np.array([22, 22, 22])
    greyish = np.array([180, 180, 180])
    whiteish = np.array([233, 233, 233])

    wordcloud_pipline("onepunch_man", 250, blackish)
