#!/usr/bin/env python3

from os import path, walk
import subprocess
from typing import List

root_dir = path.dirname(path.realpath(__file__))

index_contents = []


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
            .replace("–", "-", -1)
            .replace("′", "'")
            .replace(" ", "", -1)
            .replace("　", " ", -1)
            .replace("～", "~", -1)
        )

        f.seek(0)
        f.write(text)
        f.truncate()


def get_files_from_git() -> List[str]:
    subprocess.run(["git", "add", "--all"])
    output = subprocess.run(["git", "status", "-s"], capture_output=True)

    files = output.stdout.decode("utf-8").split("\n")
    files = filter(lambda s: s.endswith(".md") and (not s.startswith("D ")), files)
    files = map(
        lambda s: s.split("->").pop().strip() if s.startswith("R") else s[1:].strip(),
        files,
    )

    return files


# Format files
for file in get_files_from_git():
    fmt_md(file)


# Build index
def gen_index_contents(sub_path):
    file_infos = []
    article_dir = path.join(root_dir, sub_path)
    for _, _, filenames in walk(article_dir):
        for filename in filenames:
            if filename.startswith("quantum-0"):
                continue
            p = path.join(article_dir, filename)
            file_infos.append({"path": p, "name": filename})

    file_infos.sort(key=lambda info: info["name"])

    for i in file_infos:
        with open(i["path"], "r") as f:
            lines = f.readlines()
            title = lines[1].split(":").pop().strip()
            content = f'- [{title}]({sub_path}/{i["name"]})'
            index_contents.append(content)


years = ["2025"]


def write_index_file():
    for year in years:
        index_contents.append(f"### {year}\n")
        gen_index_contents(year)
        index_contents.append("")
    with open(path.join(root_dir, "index.md"), "a") as f:
        f.write("\n".join(index_contents))


# write_index_file()
