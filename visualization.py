import collections
import os
import re
import sys

import nltk
import numpy as np
from PIL import Image
import wordcloud


def wordcloud_visualization(module):
    words, colormap, mask = module.get_words(), module.colormap, module.mask
    # Keep only alpha-numerical characters
    words = [w.lower() for w in words if w.isalnum()]

    # Load the image and convert them to the right format
    colormap = np.asarray(Image.open(colormap).convert("RGB"))
    mask = np.asarray(Image.open(mask).convert("L"))

    # Create usefull masks from the mask image
    border_mask = mask == 255
    inner_mask = mask == 0

    # Remove stop words
    stop_words = nltk.corpus.stopwords.words("english")
    words = [w for w in words if w not in stop_words]

    # Count the top words
    counter = collections.Counter(words)
    top = dict(counter.most_common(250))
    print(top)

    # Mask for the word cloud
    wc_mask_in = np.array(mask)
    wc_mask_in[~inner_mask] = 255
    options = {
        "random_state": 0,
        "mask": wc_mask_in,
        "mode": "RGB",
        "background_color": "white",
        "color_func": lambda *arg, **kwarg: "black",
    }
    # Create the word cloud
    wc = wordcloud.WordCloud(**options)
    wc.fit_words(top)
    # Convert the array to a grey scale image
    wc_array = np.asarray(Image.fromarray(wc.to_array()).convert("L"))

    img = np.array(colormap)

    # Find the color background based on the mean color
    average_color = np.mean(colormap[inner_mask])
    whiteish = np.array([22, 22, 22])
    blackish = np.array([233, 233, 233])
    carving_color = whiteish if average_color > 255 / 2 else blackish

    # Create a normalized mask from the word cloud
    wc_normalized = np.expand_dims((255 - wc_array) / 255, -1)

    # Linear interpolation between the text and the backgroud color
    img = (1 - wc_normalized) * carving_color + wc_normalized * colormap
    # Convert the image back to int
    img = img.astype(np.uint8)

    # Add the border
    img[border_mask] = colormap[border_mask]

    Image.fromarray(img).save(f"wordclouds/{module.__name__}.png")


if __name__ == '__main__':
    nltk.download("stopwords")
    nltk.download("punkt")

    import nge
    import cb

    wordcloud_visualization(nge)
    wordcloud_visualization(cb)
