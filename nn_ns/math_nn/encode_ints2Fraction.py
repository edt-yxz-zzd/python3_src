
r'''
used to encode version

encode_ints2Fraction
    frA, frB = map(~, [lsA, lsB])
    assert (frA < frB) == (lsA < lsB)


encode_ints2continued_fraction
    ints = [a0, a1,..., an]
    cf = [0; b0, c0, b1, c1, ..., bn, cn, +inf...]
    b[i] = 1 + max(0, -a[i])
    c[i] = 1 + max(0, +a[i])

dvfcf - dot version, finite continued fraction

'''

__all__ = '''
    encode_ints2continued_fraction
    encode_ints2Fraction

    decode_ints_from_finite_continued_fraction
    decode_ints_from_Fraction

    ints2dot_version
    dot_version2ints
    dvfcf_encode
    dvfcf_decode
'''.split()


from .continued_fraction.continued_fraction import \
     finite_continued_fraction2Fraction, continued_fraction_expand,\
     ND2Fraction, Fraction2ND


def ints2dot_version(ints):
    return '.'.join(map(repr, ints))
def dot_version2ints(dv):
    return map(int, dv.split('.') if dv else [])
def dvfcf_encode(dv):
    ints = dot_version2ints(dv)
    fr = encode_ints2Fraction(ints)
    N, D = Fraction2ND(fr)
    s = '{}/{}'.format(N, D)
    return s.encode('ascii')

def dvfcf_decode(fcf):
    s = fcf.decode('ascii')
    N, D = s.split('/')
    ND = map(int, [N,D])
    fr = ND2Fraction(ND)
    ints = decode_ints_from_Fraction(fr)
    return ints2dot_version(ints)

    

def encode_ints2continued_fraction(ints):
    yield 0
    for i in ints:
        yield 1+max(0, -i)
        yield 1+max(0, +i)
    return

def encode_ints2Fraction(ints):
    return finite_continued_fraction2Fraction(encode_ints2continued_fraction(ints))


def _test_encode_ints2Fraction():
    from itertools import product, chain
    bs = [-1, 0, 1]
    intss = chain.from_iterable(map(lambda i:product(bs, repeat=i), range(4)))
    intss = sorted(intss)
    #print(len(intss))
    #print(intss)
    *frs, = map(encode_ints2Fraction, intss)
    #print(frs)
    for a, b in zip(frs, frs[1:]):
        assert a < b


def decode_ints_from_Fraction(fr):
    cf = continued_fraction_expand(fr)
    return decode_ints_from_finite_continued_fraction(cf)
def decode_ints_from_finite_continued_fraction(cf):
    *cf, = cf
    
    if not cf:
        raise logic-error
    Error = ValueError('not invaild Fraction')
    if cf[0] != 0:
        raise Error
    if len(cf) % 2 != 1:
        if cf[-1] <= 1:
            raise Error
        cf[-1] -= 1
        cf.append(1)
    assert len(cf) % 2 == 1

    bs = cf[1::2]
    cs = cf[2::2]
    assert len(bs) == len(cs)
    for b, c in zip(bs, cs):
        if all(i != 1 for i in [b,c]):
            raise Error

    ls = []
    for b, c in zip(bs, cs):
        if b > 1:
            assert c == 1
            x = 1-b
        elif c > 1:
            assert b == 1
            x = c-1
        else:
            assert (b,c) == (1,1)
            x = 0
        ls.append(x)

    return ls


def _test_decode_ints_from_Fraction():
    from itertools import product, chain
    bs = [-1, 0, 1]
    intss = chain.from_iterable(map(lambda i:product(bs, repeat=i), range(4)))
    intss = sorted(intss)
    *frs, = map(encode_ints2Fraction, intss)
    try:
        for fr in frs:
            decode_ints_from_Fraction(fr)
    except:
        print(fr)
        i = frs.index(fr)
        print(intss[i])
        *cf, = continued_fraction_expand(fr)
        print(cf)
        raise
    _intss = map(decode_ints_from_Fraction, frs)
    *_intss, = map(tuple, _intss)
    assert _intss == intss

    

def _test_dvfcf():
    from itertools import product, chain
    bs = [-1, 0, 1]
    intss = chain.from_iterable(map(lambda i:product(bs, repeat=i), range(4)))
    intss = map(ints2dot_version, intss)

    for ints in intss:
        assert ints == dvfcf_decode(dvfcf_encode(ints))


if 0:
    _test_dvfcf()
    _test_encode_ints2Fraction()
    _test_decode_ints_from_Fraction()





