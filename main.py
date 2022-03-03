import animes
from tools import words_processing, wordcloud_visualization

import importlib
import os
from PIL import Image
from pathlib import Path

if __name__ == '__main__':

    for submodule in os.listdir("animes")[::-1]:
        if submodule[0] == "_":
            continue
        print(submodule)
        module = importlib.import_module("animes." + submodule)
        module_path = Path(module.__path__[0])
        colormap = Image.open(module_path / Path("colormap.png"))
        mask = Image.open(module_path / Path("mask.png"))
        words = module.get_words()
        words = words_processing(words)
        wc = wordcloud_visualization(words, colormap, mask)
        wc.save(f"wordclouds/{submodule}.png")
