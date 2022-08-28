import glob
import subprocess
import json
from pprint import pprint
import re

files = glob.glob("subs/*.mkv")

kept_chapters = ["Part A", "Part B"]

for f in files:
    data = subprocess.run(f'ffprobe -i "{f}" -print_format json -show_chapters -loglevel error', capture_output=True)
    chapters = json.loads(data.stdout)["chapters"]

    chapters = [c for c in chapters if c["tags"]["title"] in kept_chapters]
    print(f, len(chapters))

    for i, c in enumerate(chapters):
        command = f'ffmpeg -loglevel info -i "{f}" -ss {c["start_time"]} -to {c["end_time"]} -map 0:s:1 "{f}_{i}.vtt"'
        data = subprocess.run(command, capture_output=True)
        # print(data.stderr.decode("utf-8"))
        # break

files = glob.glob("subs/*.vtt")

for f in files:
    data = open(f, "rb").read().decode("utf-8")
    data = re.sub("\n+(.*)", "\n\\1", data)
    data = re.sub("\n(\d+:\d+.\d+ --> \d+:\d+.\d+)\n", "\n\n\\1\n", data)
    open(f, "wb").write(data.encode("utf-8"))
