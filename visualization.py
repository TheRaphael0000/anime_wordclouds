import re
import collections
import os
import sys

from PIL import Image
import numpy as np
import wordcloud
import nltk


def wordcloud_visualization(module):
    words, colormap, mask = module.get_data()
    words = [w.lower() for w in words if w.isalnum()]

    colormap = np.asarray(Image.open(colormap).convert("RGB"))
    mask = np.asarray(Image.open(mask).convert("L"))

    mask = np.array(mask)
    colormap = np.array(colormap)

    border_mask = mask == 255
    inner_mask = mask == 0

    # Remove stop words
    stop_words = nltk.corpus.stopwords.words("english")
    words = [w for w in words if w not in stop_words]

    # Count the top words
    counter = collections.Counter(words)
    top = dict(counter.most_common(200))
    print(top)

    wc_mask_in = np.array(mask)
    wc_mask_in[~border_mask & ~inner_mask] = 255
    options = {
        "random_state": 0,
        "mask": wc_mask_in,
        "mode": "RGB",
        "background_color": "white",
        "color_func": lambda *args, **kwargs: "black"
    }
    wc = wordcloud.WordCloud(**options)
    wc.fit_words(top)

    wc_array = np.asarray(Image.fromarray(wc.to_array()).convert("L"))
    wc_mask = wc_array > 127

    carve = wc_mask & ~border_mask
    average_color = np.mean(colormap[inner_mask])
    whiteish = [22, 22, 22]
    blackish = [233, 233, 233]
    carving_color = whiteish if average_color > 127.5 else blackish
    colormap[carve] = carving_color

    Image.fromarray(colormap).save(f"{module.__name__}_wordcloud.png")


if __name__ == '__main__':
    nltk.download("stopwords")
    nltk.download("punkt")

    import nge
    wordcloud_visualization(nge)

    import cb
    wordcloud_visualization(cb)
