#!/usr/bin/env python

import sys

# Given a list of urls, print out the top 3 frequent filenames.
#
# ex.
#
# Given urls = [
#     "http://www.google.com/a.txt",
#     "http://www.google.com.tw/a.txt",
#     "http://www.google.com/download/c.jpg",
#     "http://www.google.co.jp/a.txt",
#     "http://www.google.com/b.txt",
#     "https://facebook.com/movie/b.txt",
#     "http://yahoo.com/123/000/c.jpg",
#     "http://gliacloud.com/haha.png",
# ]
#
# The program should print out
#
# a.txt 3
# b.txt 2
# c.jpg 2

# === Default urls
urls = \
[
  "http://www.google.com/a.txt"
, "http://www.google.com.tw/a.txt"
, "http://www.google.com/download/c.jpg"
, "http://www.google.co.jp/a.txt"
, "http://www.google.com/b.txt"
, "https://facebook.com/movie/b.txt"
, "http://yahoo.com/123/000/c.jpg"
, "http://gliacloud.com/haha.png"
]
#///

if len(sys.argv[1:]) > 0:

 urls = sys.argv

#
# Reduction per question statement
#

def reduce(urls):   # ===

 freq = {}

 for k in [ _.split('/')[-1] for _ in urls ]:

  if k not in freq: freq[k] = 0

  freq[k] += 1

 return freq.items()

# ///

result = reduce(urls)

#
# Hello world!
#

top = 3
 
result = sorted(result,key=lambda _ : _[1],reverse=True)

# PP
width = max([len(_[0]) for _ in result])

for file, rep in result[:top]:

 print(f'{file:>{width}s} {rep:3d}')

