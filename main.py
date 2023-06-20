import animes
from tools import words_processing, wordcloud_visualization

import importlib
import os
from PIL import Image
from pathlib import Path


def generate(submodule_name):
    module = importlib.import_module("animes." + submodule_name)
    module_path = Path(module.__path__[0])
    print("loading colormap")
    colormap = Image.open(module_path / Path("colormap.png"))
    print("loading mask")
    mask = Image.open(module_path / Path("mask.png"))
    print("loading words")
    words = module.get_words()
    print(f"{len(words)} words loaded")
    words = words_processing(words)
    print(f"{len(words)} words kept")
    print(words)
    wc = wordcloud_visualization(words, colormap, mask)
    wc.save(f"wordclouds/{submodule_name}.png")


if __name__ == '__main__':

    # for submodule in os.listdir("animes")[::-1]:
    #     if submodule[0] == "_":
    #         continue
    #     generate(submodule_name)

    generate("steins_gate")