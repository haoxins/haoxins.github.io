#!/usr/bin/env python3
import subprocess
from os import path

root_dir = path.dirname(path.realpath(__file__))


def fmt_md(file: str):
    file = path.join(root_dir, file)
    with open(file, "r+") as f:
        text = f.read()
        text = (
            text.replace("\t", " ", -1)
            .replace("‘", "'", -1)
            .replace("’", "'", -1)
            .replace("“", '"', -1)
            .replace("”", '"', -1)
            .replace("（", " (", -1)
            .replace("）", ") ", -1)
            .replace("《", " <", -1)
            .replace("》", "> ", -1)
            .replace("【", " [", -1)
            .replace("】", "] ", -1)
            .replace("，", ", ", -1)
            .replace("、", ", ", -1)
            .replace("。", ". ", -1)
            .replace("；", "; ", -1)
            .replace("：", ": ", -1)
            .replace("！", "! ", -1)
            .replace("？", "? ", -1)
        )

        f.seek(0)
        f.write(text)
        f.truncate()


subprocess.run(["git", "add", "--all"])
output = subprocess.run(["git", "status", "-s"], capture_output=True)

files = output.stdout.decode("utf-8").split("\n")
files = filter(lambda s: s.endswith(".md"), files)


def get_filename(s: str) -> str:
    if s.startswith("R"):
        return s.split("->").pop().strip()
    else:
        return s[1:].strip()


files = map(get_filename, files)

for file in files:
    fmt_md(file)
