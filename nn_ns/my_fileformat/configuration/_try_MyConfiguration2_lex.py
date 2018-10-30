
__all__ = '''
    tokens
    source_string
    '''.split()

from . import MyConfiguration2_lex
from .MyConfiguration2_lex import (
    #parse_source_string as tokenize
    lex_postprocessor
    ,BigNewlineNoIndents
    ,BigNewlineIndents1
    ,t_ANY_BigNewlineNoIndents
    )
from pathlib import Path
import re

tokenize = lex_postprocessor.tokenize
'''
rough_pattern
rough_regex
precise_pattern
precise_regex

__doc__
fullmatch
match

'''
class Global:
    this_folder = Path(__file__).parent
    example_fname = this_folder / 'configuration file format - example.txt'
    example = example_fname.read_text(encoding='utf8')


source_string = '''\
>>> {}:
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
'''

source_string = Global.example
tokens = tokenize(source_string)

if __name__ == '__main__':
    print(tokens)
    for t in tokens:
        print(t)

