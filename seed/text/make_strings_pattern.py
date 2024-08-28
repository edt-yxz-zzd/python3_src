
__all__ = '''
    make_strings_pattern
    make_chars_pattern
    '''.split()

from re import escape
from itertools import chain

def _escape_char(char):
    if len(char) != 1: raise TypeError
    return escape(char)
def make_chars_pattern(chars):
    # ['a', '1'] ==>> r"[a1]"
    patterns = map(_escape_char, chars)
    pattern = ''.join(chain('[', patterns, ']'))
    return pattern
assert make_chars_pattern(['a', '1']) == '[a1]'
assert (__:=make_chars_pattern([*r'^a-z\w[]'])) == r'[\^a\-z\\w\[\]]', __

def make_strings_pattern(strings):
    # ['ab', '12'] ==>> r"ab|12"

    #bug:
    #   patterns = map(re.escape, strings)
    #   pattern = '|'.join(patterns)
    # should sort pattern from longest to shortest

    strings = sorted(set(strings), key=len, reverse=True)
    patterns = map(escape, strings)
    pattern = '|'.join(patterns)
    return pattern

assert make_strings_pattern(['a', 'aa']) == 'aa|a'


from seed.text.make_strings_pattern import make_strings_pattern
from seed.text.make_strings_pattern import make_chars_pattern
from seed.text.make_strings_pattern import *
