"Mirai Nikki"
import glob
import itertools
import nltk
from nltk.tokenize import TweetTokenizer
import re


def get_words():
    path = __path__[0] + "/subs/*.vtt"
    print(path)
    sub_files = glob.glob(path)
    tokenizer = TweetTokenizer()
    all_tokens = []
    for f in sub_files:
        print(f)
        text = read_file(f)
        tokens = tokenizer.tokenize(text)
        all_tokens.extend(tokens)
    return all_tokens


def read_file(file):
    lines = []
    for line in itertools.islice(open(file, "rb"), 1, None):
        line = line.decode("utf8")
        timestamp = "\d+:\d+\.\d+"
        pattern = f"{timestamp} --> {timestamp}"
        if re.match(pattern, line):
            continue
        line = re.sub("<.*?>", "", line)
        lines.append(line)

    return "\n".join(lines)


if __name__ == "__main__":
    print(get_words())