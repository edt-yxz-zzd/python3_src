r'''
e ../../python3_src/seed/io/make_mode_ex4open.py
see:
    view ../../python3_src/seed/io/may_open.py
        open4w
        open4w_err
        open4r

xencoding = nonencoding | encoding
may_encoding = None | encoding

nonencoding = '' | None | False
encoding :: nonempty_str




from seed.io.make_mode_ex4open import is_binary_mode5xencoding, xencoding2may_encoding, mk_mode_ex4open4w, mk_mode_ex4open4r

from seed.io.may_open import open4w, open4w_err, open4r

#'''
__all__ = r'''
is_binary_mode5xencoding
    xencoding2may_encoding
    mk_mode_ex4open4w
    mk_mode_ex4open4r
'''.split()#'''




def is_binary_mode5xencoding(xencoding, /):
    if not (type(xencoding) is str or xencoding is None or xencoding is False): raise TypeError
    return not xencoding
    bt = 'b' if not xencoding else 't'
        # False, None, '' ==>> binary
        # '...' ==>> text
def xencoding2may_encoding(xencoding, /):
    is_b = is_binary_mode5xencoding(xencoding)
    may_encoding = None if is_b else xencoding
    return may_encoding
def mk_mode_ex4open4w(*, force, xencoding):
    '-> (mode, may_encoding)'
    may_encoding = xencoding2may_encoding(xencoding)
    is_b = may_encoding is None
    bt = 'b' if is_b else 't'
    xw = 'x' if not force else 'w'

    mode = f'{xw}{bt}'
    return (mode, may_encoding)
def mk_mode_ex4open4r(*, xencoding):
    may_encoding = xencoding2may_encoding(xencoding)
    is_b = may_encoding is None
    bt = 'b' if is_b else 't'
    mode = f'r{bt}'
    return (mode, may_encoding)


from seed.io.make_mode_ex4open import is_binary_mode5xencoding, xencoding2may_encoding, mk_mode_ex4open4w, mk_mode_ex4open4r
