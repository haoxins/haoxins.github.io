#!/usr/bin/env python3

import os

rootdir = os.path.dirname(os.path.realpath(__file__))
file_infos = []
contents = []

dir = os.path.join(rootdir, 'articles')
for (dirpath, dirname, filenames) in os.walk(dir):
  for filename in filenames:
    p = os.path.join(dir, filename)
    info = os.stat(p)
    file_infos.append({'mtime': info.st_mtime, 'path': p, 'name': filename})


def takeMtime(info):
  return info["mtime"]


file_infos.sort(key=takeMtime, reverse=True)

for i in file_infos:
  with open(i['path'], 'r') as f:
    lines = f.readlines()
    title = lines[1].split(':').pop().strip()
    content = '* [' + title + '](articles/' + i['name'] + ')'
    contents.append(content)

with open(os.path.join(rootdir, 'index.md'), 'w') as f:
  f.write('\n'.join(contents))
