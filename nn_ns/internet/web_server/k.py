#!py -2
# -*- coding: utf-8 -*-
#encoding = utf-8

import urllib

path = r'E:\my_data\program_source\python3_src\root\internet\download_comic\getComic-master\yhzp\将夜\第0012话-第六回 上\001.jpg'
url = urllib.pathname2url(path)

print(url, type(path))
