
__all__ = '''
    iter_all_char_ords
    iter_all_chars
    '''.split()

from .constant import CHAR_ORD_UPPER
def iter_all_char_ords():
    return range(CHAR_ORD_UPPER)

def iter_all_chars():
    return map(chr, iter_all_char_ords())


