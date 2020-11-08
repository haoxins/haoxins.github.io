#!/usr/bin/env python3

from os import walk
from os import path

rootdir = path.dirname(path.realpath(__file__))
contents = []

dir = path.join(rootdir, 'articles')
for (dirpath, dirname, filenames) in walk(dir):
    for filename in filenames:
        p = path.join(dir, filename)
        file = open(p, 'r')
        lines = file.readlines()
        title = lines[1].split(':').pop().strip()
        content = '[' + title + '](articles/' + filename + ')'
        contents.append(content)
        file.close()

file = open(path.join(rootdir, 'index.md'), 'w')
file.write('\n'.join(contents))
file.close()
