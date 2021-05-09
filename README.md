# Information

Feel free to create pull requests, but do not commit subtitles !

To create a visualization :

1.  Extracts the subtitles using [FFMPEG](https://www.ffmpeg.org/) to the VTT format, due to obvious copyright problems, they can't be on the repository.
2.  Preprocess the image using [a graphical tool](https://www.gimp.org/) to create a mask.
3.  From this mask and the words obtained from the subtitles, the script uses [nltk](https://www.nltk.org/) to remove stop words, [wordcloud](https://pypi.org/project/wordcloud/) to create a visualization and a bit of [numpy](https://numpy.org/) image math's.

# Neon Genesis Evangelion

![https://preview.redd.it/zas5oikp8wc61.png?width=640&crop=smart&auto=webp&s=34cbab3f631bdf9df08cca1ffe2776f7432ce3c0](https://preview.redd.it/zas5oikp8wc61.png?width=640&crop=smart&auto=webp&s=34cbab3f631bdf9df08cca1ffe2776f7432ce3c0)

Data used:

-   English subtitles from the 1995 anime: [Neon Genesis Evangelion](https://en.wikipedia.org/wiki/Neon_Genesis_Evangelion)
-   [Original image](https://7themes.su/photo/hd_wallpapers/anime/neon_genesis_evangelion_minimal/57-0-11947)

Reddit : [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful/comments/l2ozn2/oc_neon_genesis_evangelion_word_cloud/) [r/evangelion](https://www.reddit.com/r/evangelion/comments/l2p3k3/neon_genesis_evangelion_word_cloud/)

# Cowboy Bebop

Data used:

-   English subtitles from the 1998 anime: [Cowboy Bebop
    ](https://en.wikipedia.org/wiki/Cowboy_Bebop)
-   [Original image](https://wallup.net/cowboy-bebop-spike-spiegel-monochrome-anime-minimalism/)
