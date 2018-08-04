


__all__ = '''
    repr_string_as_unicode
    repr_char_as_unicode
    repr_char_ord_as_unicode
    '''.split()

from itertools import chain

def repr_string_as_unicode(chars):
    # Iter char -> String
    return ''.join(chain('"'
            , map(repr_char_ord_as_unicode, map(ord, chars))
            , '"'))
    return ''.join(chain('"', map(repr_char_as_unicode, chars), '"'))
def repr_char_as_unicode(char):
    # except ""!!!!
    return repr_char_ord_as_unicode(ord(char))
def repr_char_ord_as_unicode(char_ord):
    return rf'\U{char_ord:0>8X}'

