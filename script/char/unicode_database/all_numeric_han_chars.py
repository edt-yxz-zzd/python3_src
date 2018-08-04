
from seed.io.RCXW import make_rcxw__text

ofname = 'all_numeric_han_chars.u8'
oencoding = 'utf8'

def _make():
    from han2ntype2number import all_numeric_han_chars
    return all_numeric_han_chars

all_numeric_han_chars = make_rcxw__text(_make
    , ofname, encoding=oencoding)()
assert 73 == len(all_numeric_han_chars)

