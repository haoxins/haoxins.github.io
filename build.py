#!/usr/bin/env python3

import os
from os import path

root_dir = path.dirname(path.realpath(__file__))

file_infos = []
contents = []


def gen_contents(sub_path, reverse):
  article_dir = path.join(root_dir, sub_path)
  for (_, _, filenames) in os.walk(article_dir):
    for filename in filenames:
      p = path.join(article_dir, filename)
      info = os.stat(p)
      file_infos.append({'mtime': info.st_mtime, 'path': p, 'name': filename})

  file_infos.sort(key=lambda info: info["name"], reverse=reverse)

  for i in file_infos:
    with open(i['path'], 'r') as f:
      lines = f.readlines()
      title = lines[1].split(':').pop().strip()
      content = f'* [{title}]({sub_path}/{i["name"]})'
      contents.append(content)

  file_infos.clear()


# Generate the index page

gen_contents('articles', False)

contents.append('\n### Archived\n')

gen_contents('_archived', True)

with open(path.join(root_dir, 'index.md'), 'w') as f:
  f.write('\n'.join(contents))
