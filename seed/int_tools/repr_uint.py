
r'''

seed.int_tools.repr_uint
py -m seed.int_tools.repr_uint
from seed.int_tools.repr_uint import uint2reprdigits, uint2iter_reprdigits_LE, iter_reprdigits2uint



reprdigits_BE
    first digit if any is not 0
reprdigits_LE
    last digit if any is not 0

reprdigits_XE = reprdigits_LE | reprdigits_BE
    reprdigits_XE is neither bidigits nor bijection_digits (which consider len and take leading 0s into count)
        see: nn_ns.Bijection.IntegerBJ.UInt2Digits




iter_repr_uint__little_endian = uint2iter_reprdigits_LE
repr_uint = uint2reprdigits
repr_uint_LE = uint2reprdigits_LE
repr_uint_BE = uint2reprdigits_BE

eval_iter_reprdigits = iter_reprdigits2uint
eval_iter_reprdigits_LE = iter_reprdigits_LE2uint
eval_iter_reprdigits_BE = iter_reprdigits_BE2uint


>>> uint2reprdigits(0, radix=2, big_endian=True)
()
>>> uint2reprdigits(1, radix=2, big_endian=True)
(1,)
>>> uint2reprdigits(2, radix=2, big_endian=True)
(1, 0)
>>> uint2reprdigits(3, radix=2, big_endian=True)
(1, 1)
>>> uint2reprdigits(4, radix=2, big_endian=True)
(1, 0, 0)
>>> uint2reprdigits(4, radix=2, big_endian=False)
(0, 0, 1)
>>> uint2reprdigits(3, radix=2, big_endian=False)
(1, 1)
>>> uint2reprdigits(2, radix=2, big_endian=False)
(0, 1)
>>> uint2reprdigits(1, radix=2, big_endian=False)
(1,)
>>> uint2reprdigits(0, radix=2, big_endian=False)
()


>>> iter_reprdigits2uint((), radix=2, big_endian=False)
0
>>> iter_reprdigits2uint((1,), radix=2, big_endian=False)
1
>>> iter_reprdigits2uint((0, 1), radix=2, big_endian=False)
2
>>> iter_reprdigits2uint((1, 1), radix=2, big_endian=False)
3
>>> iter_reprdigits2uint((0, 0, 1), radix=2, big_endian=False)
4
>>> iter_reprdigits2uint((1, 0, 0), radix=2, big_endian=True)
4
>>> iter_reprdigits2uint((1, 1), radix=2, big_endian=True)
3
>>> iter_reprdigits2uint((1, 0), radix=2, big_endian=True)
2
>>> iter_reprdigits2uint((1,), radix=2, big_endian=True)
1
>>> iter_reprdigits2uint((), radix=2, big_endian=True)
0


#'''

__all__ = '''
    uint2reprdigits
        repr_uint
        uint2iter_reprdigits_LE
            iter_repr_uint__little_endian
        uint2reprdigits_LE
            repr_uint_LE
        uint2reprdigits_BE
            repr_uint_BE
    iter_reprdigits2uint
        eval_iter_reprdigits
        iter_reprdigits_LE2uint
            eval_iter_reprdigits_LE
        iter_reprdigits_BE2uint
            eval_iter_reprdigits_BE
    '''.split()
#bit_length

def uint2iter_reprdigits_LE(u, /, *, radix):
#def iter_repr_uint__little_endian__plain(u, /, *, radix):
    r'uint -> radix{>=2} -> Iter<uint%radix> # reprdigits_LE(last digit if any is not 0), reprdigits_LE is not bidigits or bijection_digits'
    if type(radix) is not int: raise TypeError
    if not radix >= 2: raise ValueError
    if type(u) is not int: raise TypeError
    if not u >= 0: raise ValueError

    while u:
        u, r = divmod(u, radix)
        yield r

def uint2reprdigits(u, /, *, radix, big_endian:bool):
    r'uint -> radix{>=2} -> big_endian{::bool} -> tuple<uint%radix>'
    it = uint2iter_reprdigits_LE(u, radix=radix)
    reprdigits_LE = tuple(it)
    if big_endian:
        reprdigits_BE = tuple(reversed(reprdigits_LE))
        reprdigits_XE = reprdigits_BE
    else:
        reprdigits_XE = reprdigits_LE
    return reprdigits_XE

def uint2reprdigits_LE(u, /, *, radix):
    r'uint -> radix{>=2} -> tuple<uint%radix>'
    return uint2reprdigits(u, radix=radix, big_endian=False)
def uint2reprdigits_BE(u, /, *, radix):
    r'uint -> radix{>=2} -> tuple<uint%radix>'
    return uint2reprdigits(u, radix=radix, big_endian=True)


uint2iter_reprdigits_LE
uint2reprdigits
uint2reprdigits_LE
uint2reprdigits_BE
iter_repr_uint__little_endian = uint2iter_reprdigits_LE
repr_uint = uint2reprdigits
repr_uint_LE = uint2reprdigits_LE
repr_uint_BE = uint2reprdigits_BE


def iter_reprdigits2uint(iter_reprdigits_XE, /, *, radix, big_endian:bool):
    r'Iter<uint%radix> -> radix{>=2} -> big_endian{::bool} -> uint'
    f = iter_reprdigits_BE2uint if big_endian else iter_reprdigits_LE2uint
    return f(iter_reprdigits_XE, radix=radix)

def iter_reprdigits_LE2uint(iter_reprdigits_LE, /, *, radix):
    if type(radix) is not int: raise TypeError
    if not radix >= 2: raise ValueError
    weight = 1
    acc = 0
    for digit in iter_reprdigits_LE:
        if type(digit) is not int: raise TypeError
        if not 0 <= digit < radix: raise ValueError
        acc += digit*weight
        weight *= radix
    u = acc
    return u
def iter_reprdigits_BE2uint(iter_reprdigits_BE, /, *, radix):
    if type(radix) is not int: raise TypeError
    if not radix >= 2: raise ValueError

    acc = 0
    for digit in iter_reprdigits_BE:
        if type(digit) is not int: raise TypeError
        if not 0 <= digit < radix: raise ValueError
        acc *= radix
        acc += digit
    u = acc
    return u
eval_iter_reprdigits = iter_reprdigits2uint
eval_iter_reprdigits_LE = iter_reprdigits_LE2uint
eval_iter_reprdigits_BE = iter_reprdigits_BE2uint


def _t():
    radix = 10
    for u in range(1, 120):
        reprdigits_BE = (*map(int, repr(u)),)
        if reprdigits_BE[0]==0:
            reprdigits_BE = reprdigits_BE[1:]
            assert not reprdigits_BE
        else:
            assert reprdigits_BE[0]

        ##
        assert reprdigits_BE == uint2reprdigits_BE(u, radix=radix)

        reprdigits_LE = uint2reprdigits_LE(u, radix=radix)
        assert reprdigits_LE == tuple(reversed(reprdigits_BE))

        assert u == iter_reprdigits2uint(iter(reprdigits_BE), radix=radix, big_endian=True)
        assert u == iter_reprdigits2uint(iter(reprdigits_LE), radix=radix, big_endian=False)


        assert u == iter_reprdigits2uint((reprdigits_BE), radix=radix, big_endian=True)
        assert u == iter_reprdigits2uint((reprdigits_LE), radix=radix, big_endian=False)


if __name__ == "__main__":
    _t()
if __name__ == "__main__":
    import doctest
    doctest.testmod()


