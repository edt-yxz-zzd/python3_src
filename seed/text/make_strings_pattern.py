
__all__ = '''
    make_chars_pattern
    make_strings_pattern
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


