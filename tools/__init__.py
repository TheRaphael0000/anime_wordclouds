"Create a wordcloud visualization"

import collections

import nltk
import numpy as np
from PIL import Image
import wordcloud


nltk.download("stopwords")
nltk.download("punkt")


def wordcloud_visualization(words, colormap, mask):
    # Load the image and convert them to the right format
    colormap = np.asarray(colormap.convert("RGB"))
    mask = np.asarray(mask.convert("L"))

    # Create usefull masks from the mask image
    border_mask = mask == 255
    inner_mask = mask == 0

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
    word_cloud = wordcloud.WordCloud(**options)
    word_cloud.fit_words(words)
    # Convert the array to a grey scale image
    wc_array = np.asarray(Image.fromarray(word_cloud.to_array()).convert("L"))

    img = np.array(colormap)

    # Find the color background based on the mean color
    average_color = np.mean(colormap[inner_mask])
    whiteish, blackish = np.array([22, 22, 22]), np.array([233, 233, 233])
    carving_color = whiteish if average_color > 255 / 2 else blackish

    # Create a normalized mask from the word cloud
    wc_normalized = np.expand_dims((255 - wc_array) / 255, -1)

    # Linear interpolation between the text and the backgroud color
    img = (1 - wc_normalized) * carving_color + wc_normalized * colormap
    # Convert the image back to int
    img = img.astype(np.uint8)

    # Add the border
    img[border_mask] = colormap[border_mask]

    return Image.fromarray(img)


def words_processing(words):
    # Keep only alpha-numerical characters
    words = [w.lower() for w in words if w.isalnum()]

    # Remove stop words
    stop_words = nltk.corpus.stopwords.words("english")
    words = [w for w in words if w not in stop_words]

    # Count the top words
    counter = collections.Counter(words)
    words = dict(counter.most_common(250))
    return words
