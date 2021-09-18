#!/usr/bin/env python3

import re
import os
from os import path

root_dir = path.dirname(path.realpath(__file__))

file_infos = []
contents = []

last_year = None


def gen_contents(sub_path):
    article_dir = path.join(root_dir, sub_path)
    for (_, _, filenames) in os.walk(article_dir):
        for filename in filenames:
            p = path.join(article_dir, filename)

            year = filename.split("-")[0]
            if not re.match(r"[0-9]{4}$", year):
                year = None

            file_infos.append({"path": p, "name": filename, "year": year})

    file_infos.sort(key=lambda info: info["name"], reverse=True)

    for i in file_infos:
        with open(i["path"], "r") as f:
            lines = f.readlines()

            year = i["year"]
            global last_year
            if year != None and year != last_year:
                last_year = year
                contents.append(f"### {last_year}")

            title = lines[1].split(":").pop().strip()
            content = f'* [{title}]({sub_path}/{i["name"]})'
            contents.append(content)

    file_infos.clear()


# Generate the index page

gen_contents("articles")

gen_contents("archived")

with open(path.join(root_dir, "index.md"), "w") as f:
    f.write("\n".join(contents))
