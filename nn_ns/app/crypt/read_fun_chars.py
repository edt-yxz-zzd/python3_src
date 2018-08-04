

__all__ = ['fun_chars']

import os.path
import io
from bs4 import BeautifulSoup

fun_chars_html_basename = 'total_fun_chars.html'
html_path = os.path.join(os.path.dirname(__file__), fun_chars_html_basename)
with open(html_path, encoding='utf8') as fin:
    #soup = BeautifulSoup(fin, 'html.parser')
    soup = BeautifulSoup(fin, 'lxml')
s = str(soup.body.pre.string); del soup
def good_line(line):
    line = line.strip()
    return line and line[0] != '#'
fun_chars = ''.join(line for line in s.split('\n') if good_line(line))
fun_chars = ''.join(fun_chars.split())
assert len(fun_chars) == 249







