import glob
import re
import collections
import itertools

import webvtt
from PIL import Image
import numpy as np
import wordcloud
import nltk


def main():
    # Read images
    colormap = Image.open("colormap.png")
    border = Image.open("border.png")
    mask = Image.open("mask.png")

    # Read subtitles
    sub_files = glob.glob("subs/*")
    words = [get_words_from_subtitles(f) for f in sub_files]
    every_words = list(itertools.chain(*words))

    # Remove stop words
    stop_words = nltk.corpus.stopwords.words("english")
    every_words = [w for w in every_words if w not in stop_words]

    # Count the top words
    counter = collections.Counter(every_words)
    top = dict(counter.most_common(250))
    print(top["stupid"])
    print(top["please"])

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

    background.save("nge_wordcloud.png")

def get_words_from_subtitles(file):
    file_words = []
    valid = False
    for caption in webvtt.read(file):
        # Ignore opening and ending
        if "Shounen yo shinwa ni nare" in caption.text:
            valid = True
            continue
        if "To Be Continued" in caption.text:
            break
        # Tokenize the caption line
        if valid:
            words = nltk.tokenize.word_tokenize(caption.text.lower())
            words = [w for w in words if w.isalnum()]
            file_words.extend(words)
    return file_words

if __name__ == '__main__':
    nltk.download("stopwords")
    nltk.download("punkt")
    main()
