r'''
e ../../python3_src/seed/text/mk_char_pt_ranges5predicator.py


assert printable_ascii_char_pt_ranges == alnum_ascii_char_pt_ranges | punctuation_ascii_char_pt_ranges | NonTouchRanges(((32, 33),))
    # [printable%95 == alnum%(10+26*2==62) | punctuation%32 | space%1]


py -m seed.text.mk_char_pt_ranges5predicator
py -m nn_ns.app.debug_cmd   seed.text.mk_char_pt_ranges5predicator

from seed.text.mk_char_pt_ranges5predicator import mk_char_pt_ranges5predicator, mk_ascii_char_pt_ranges5predicator
from seed.text.mk_char_pt_ranges5predicator import char_pt_ranges2char_set, char_pt_ranges2sorted_chars, char_pt_ranges2iter_sorted_chars

from seed.text.mk_char_pt_ranges5predicator import printable_ascii_char_pt_ranges, printable_ascii_sorted_chars
from seed.text.mk_char_pt_ranges5predicator import is_printable_ascii_char, is_printable_ascii_str


see:
    view ../../python3_src/seed/text/charset_filter.py
    view ../../python3_src/seed/text/mk_char_pt_ranges5predicator.py

used in:
    view ../../python3_src/seed/lang/claim/repr4str__using__isprintable__to_determine_chars_escaped_in_output.py

[[[


str.isprintable


#not py!!!
https://www.includehelp.com/c-programs/check-whether-a-character-is-a-printable-character-or-not-without-using-library-function.aspx
int isPrintable(char ch)
{
    if (isAlphaNumeric(ch) || isPunctuation(ch))
        return 1;
    return 0;
}


https://www.geeksforgeeks.org/python-string-isprintable-method/
(letters, symbols, digits, punctuation and whitespace)
The only whitespace character which is printable is space or ” “, otherwise every whitespace character is non-printable and the function returns “False”.

# U+3000, (U+FF00–U+FFEF)
Halfwidth and Fullwidth Forms: U+FF00–U+FFEF
>>> '\u3000'.isprintable()
False
>>> '　'
'\u3000'


difference char group regex [[:print:]] vs [[:graph:]]
https://www.petefreitag.com/cheatsheets/regex/character-classes/
[[[

Regular Expressions (Regex) Character Classes Cheat Sheet
POSIX Character Classes for Regular Expressions & their meanings
Character Class =[def]= Meaning
[:alpha:] =[def]= Any letter, [A-Za-z]
[:upper:] =[def]= Any uppercase letter, [A-Z]
[:lower:] =[def]= Any lowercase letter, [a-z]
[:digit:] =[def]= Any digit, [0-9]
[:alnum:] =[def]= Any alphanumeric character, [A-Za-z0-9]
[:xdigit:] =[def]= Any hexadecimal digit, [0-9A-Fa-f]
[:space:] =[def]= A tab, new line, vertical tab, form feed, carriage return, or space
[:blank:] =[def]= A space or a tab.
[:print:] =[def]= Any printable character
[:punct:] =[def]= Any punctuation character: ! ' # S % & ' ( ) * + , - . / : ; < = > ? @ [ / ] ^ _ { | } ~
[:graph:] =[def]= Any character defined as a printable character except those defined as part of the space character class
[:word:] =[def]= Continuous string of alphanumeric characters and underscores.
[:ascii:] =[def]= ASCII characters, in the range: 0-127
[:cntrl:] =[def]= Any character not part of the character classes: [:upper:], [:lower:], [:alpha:], [:digit:], [:punct:], [:graph:], [:print:], [:xdigit:]


See also: Regex Cheat Sheet

Copyright © 2008 Pete Freitag (http://www.petefreitag.com/), All Rights Reserved.
This document may be printed freely as long as this notice stays intact.
]]]

python str.__repr__() which characters as escaped Sequence?
    isprintable!!!
        see:
            view ../../python3_src/seed/lang/claim/repr4str__using__isprintable__to_determine_chars_escaped_in_output.py


]]]
#'''

__all__ = '''
    mk_char_pt_ranges5predicator
    mk_ascii_char_pt_ranges5predicator

    printable_ascii_char_pt_ranges
    printable_ascii_sorted_chars
    is_printable_ascii_char
    is_printable_ascii_str







    mk_char_pt_ranges5predicator
    mk_ascii_char_pt_ranges5predicator

    printable_ascii_char_pt_ranges
    lower_ascii_char_pt_ranges
    upper_ascii_char_pt_ranges
    alpha_ascii_char_pt_ranges
    alnum_ascii_char_pt_ranges
    numeric_ascii_char_pt_ranges
    digit_ascii_char_pt_ranges
    decimal_ascii_char_pt_ranges
    space_ascii_char_pt_ranges
    punctuation_ascii_char_pt_ranges

    char_pt_ranges2char_set
    char_pt_ranges2sorted_chars
    char_pt_ranges2iter_sorted_chars

    printable_ascii_sorted_chars
    alnum_ascii_sorted_chars
    punctuation_ascii_sorted_chars
    space_ascii_sorted_chars

    is_printable_ascii_char
    is_printable_ascii_str
    '''.split()



___begin_mark_of_excluded_global_names__0___ = ...
from seed.data_funcs.rngs import make_Ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet
from seed.data_funcs.rngs import NonTouchRanges
___end_mark_of_excluded_global_names__0___ = ...

try:
    chr(0x11_0000)
except ValueError as e:
    #ValueError: chr() arg not in range(0x110000)
    assert repr(e) == r"ValueError('chr() arg not in range(0x110000)')"
else:
    raise logic-err


def mk_char_pt_ranges5predicator(pred, /):
    return _mk_char_pt_ranges5predicator(0x11_0000, pred)
def mk_ascii_char_pt_ranges5predicator(pred, /):
    return _mk_char_pt_ranges5predicator(0x80, pred)
def _mk_char_pt_ranges5predicator(end_char_pt, pred, /):
    s = StackStyleSimpleIntSet()
    for i in range(end_char_pt):
        ch = chr(i)
        if pred(ch):
            s.add(i)
    return make_Ranges(s.rngs)

printable_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isprintable)
assert printable_ascii_char_pt_ranges == NonTouchRanges(((32, 127),))
assert printable_ascii_char_pt_ranges.len_ints() == 95

def _show(ranges, /):
    print(ranges)
    print(ranges.len_ints())
#_show(printable_ascii_char_pt_ranges)


#dir(str)
#..., 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', ...
#
printable_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isprintable)
lower_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.islower)
upper_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isupper)
alpha_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isalpha)
alnum_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isalnum)
numeric_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isnumeric)
digit_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isdigit)
decimal_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isdecimal)
space_ascii_char_pt_ranges = mk_ascii_char_pt_ranges5predicator(str.isspace)
punctuation_ascii_char_pt_ranges = printable_ascii_char_pt_ranges - alnum_ascii_char_pt_ranges - space_ascii_char_pt_ranges

def _show_all_ascii_char_pt_rangess():
    for nm, v in [*globals().items()]:
        if nm.endswith('_ascii_char_pt_ranges'):
            print(f'assert {nm} == {v}')
            print(f'assert {nm}.len_ints() == {v.len_ints()}')
if __name__ == "__main__":
    _show_all_ascii_char_pt_rangess()

assert printable_ascii_char_pt_ranges == NonTouchRanges(((32, 127),))
assert printable_ascii_char_pt_ranges.len_ints() == 95
assert lower_ascii_char_pt_ranges == NonTouchRanges(((97, 123),))
assert lower_ascii_char_pt_ranges.len_ints() == 26
assert upper_ascii_char_pt_ranges == NonTouchRanges(((65, 91),))
assert upper_ascii_char_pt_ranges.len_ints() == 26
assert alpha_ascii_char_pt_ranges == NonTouchRanges(((65, 91), (97, 123)))
assert alpha_ascii_char_pt_ranges.len_ints() == 52
assert alnum_ascii_char_pt_ranges == NonTouchRanges(((48, 58), (65, 91), (97, 123)))
assert alnum_ascii_char_pt_ranges.len_ints() == 62
assert numeric_ascii_char_pt_ranges == NonTouchRanges(((48, 58),))
assert numeric_ascii_char_pt_ranges.len_ints() == 10
assert digit_ascii_char_pt_ranges == NonTouchRanges(((48, 58),))
assert digit_ascii_char_pt_ranges.len_ints() == 10
assert decimal_ascii_char_pt_ranges == NonTouchRanges(((48, 58),))
assert decimal_ascii_char_pt_ranges.len_ints() == 10
assert space_ascii_char_pt_ranges == NonTouchRanges(((9, 14), (28, 33)))
assert space_ascii_char_pt_ranges.len_ints() == 10
assert punctuation_ascii_char_pt_ranges == NonTouchRanges(((33, 48), (58, 65), (91, 97), (123, 127)))
assert punctuation_ascii_char_pt_ranges.len_ints() == 32











assert decimal_ascii_char_pt_ranges == digit_ascii_char_pt_ranges == numeric_ascii_char_pt_ranges

assert alnum_ascii_char_pt_ranges == digit_ascii_char_pt_ranges | alpha_ascii_char_pt_ranges
assert alnum_ascii_char_pt_ranges.len_ints() == digit_ascii_char_pt_ranges.len_ints() + alpha_ascii_char_pt_ranges.len_ints()

assert alpha_ascii_char_pt_ranges == lower_ascii_char_pt_ranges | upper_ascii_char_pt_ranges
assert alpha_ascii_char_pt_ranges.len_ints() == lower_ascii_char_pt_ranges.len_ints() + upper_ascii_char_pt_ranges.len_ints()


assert printable_ascii_char_pt_ranges == alnum_ascii_char_pt_ranges | punctuation_ascii_char_pt_ranges | NonTouchRanges(((32, 33),))
    # [printable%95 == alnum%(10+26*2==62) | punctuation%32 | space%1]


def char_pt_ranges2char_set(char_pt_ranges, /):
    iter_sorted_chars = char_pt_ranges2iter_sorted_chars(char_pt_ranges)
    char_set = frozenset(iter_sorted_chars)
    return char_set
def char_pt_ranges2sorted_chars(char_pt_ranges, /):
    iter_sorted_chars = char_pt_ranges2iter_sorted_chars(char_pt_ranges)
    sorted_chars = ''.join(iter_sorted_chars)
    return sorted_chars
def char_pt_ranges2iter_sorted_chars(char_pt_ranges, /):
    iter_sorted_chars = (map(chr, char_pt_ranges.iter_ints()))
    return iter_sorted_chars


printable_ascii_sorted_chars = char_pt_ranges2sorted_chars(printable_ascii_char_pt_ranges)
alnum_ascii_sorted_chars = char_pt_ranges2sorted_chars(alnum_ascii_char_pt_ranges)
punctuation_ascii_sorted_chars = char_pt_ranges2sorted_chars(punctuation_ascii_char_pt_ranges)
space_ascii_sorted_chars = char_pt_ranges2sorted_chars(space_ascii_char_pt_ranges)
def _show_all_ascii_sorted_charss():
    for nm, v in [*globals().items()]:
        if nm.endswith('_ascii_sorted_chars'):
            print(f'assert {nm} == {v!r}')
if __name__ == "__main__":
    _show_all_ascii_sorted_charss()
assert printable_ascii_sorted_chars == ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
assert alnum_ascii_sorted_chars == '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
assert punctuation_ascii_sorted_chars == '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
assert space_ascii_sorted_chars == '\t\n\x0b\x0c\r\x1c\x1d\x1e\x1f '



def is_printable_ascii_char(ch, /):
    i = ord(ch)
    return i in printable_ascii_char_pt_ranges
def is_printable_ascii_str(s, /):
    return str.isprintable(s) and max(map(ord, s), default=0) < 0x80
assert is_printable_ascii_str('')
assert is_printable_ascii_str(' ')
assert is_printable_ascii_str('+')
assert is_printable_ascii_str('a')
assert is_printable_ascii_str('0')
assert not is_printable_ascii_str('\t')
assert not is_printable_ascii_str('\n')


from seed.text.mk_char_pt_ranges5predicator import printable_ascii_char_pt_ranges, printable_ascii_sorted_chars
from seed.text.mk_char_pt_ranges5predicator import punctuation_ascii_char_pt_ranges, punctuation_ascii_sorted_chars
from seed.text.mk_char_pt_ranges5predicator import *
