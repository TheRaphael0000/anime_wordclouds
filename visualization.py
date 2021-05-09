import re
import collections
import os
import sys

from PIL import Image
import numpy as np
import wordcloud
import nltk


def wordcloud_visualization(folder, get_words):
    os.chdir(folder)
    sys.path.append(folder)

    # Read images
    colormap = Image.open("colormap.png")
    border = Image.open("border.png")
    mask = Image.open("mask.png")

    words = get_words()
    words = [w.lower() for w in words if w.isalnum()]

    # Remove stop words
    stop_words = nltk.corpus.stopwords.words("english")
    words = [w for w in words if w not in stop_words]

    # Count the top words
    counter = collections.Counter(words)
    top = dict(counter.most_common(250))

    # Create the word cloud
    wc = wordcloud.WordCloud(
        mask=np.asarray(mask), mode="RGBA", background_color=None, color_func=lambda *args, **kwargs: "black")
    wc.fit_words(top)
    img = Image.fromarray(wc.to_array())

    # Color the wordcloud
    _, _, _, a = img.split()
    r, g, b, _ = colormap.split()
    img = Image.merge("RGBA", (r, g, b, a))

    # Add the border
    img = Image.alpha_composite(border, img)

    os.chdir("..")
    img.save(f"{folder}_wordcloud.png")


if __name__ == '__main__':
    nltk.download("stopwords")
    nltk.download("punkt")
    
    from nge import get_words as nge

    wordcloud_visualization("nge", nge)
