
'''
unicodedata.category(char) in ('Ps', 'Pe', 'Pi', 'Pf')
or unicodedata.mirrored(char)
'''

__all__ = ['is_open_close_char']

from unicodedata import category, mirrored

categories = ('Ps', 'Pe', 'Pi', 'Pf')
def is_open_close_char(char):
    return mirrored(char) or category(char) in categories


