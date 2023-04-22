#__all__:goto
r'''[[[
e ../../python3_src/seed/text/decode_on_err_bytes_.py

used in:
    view script/欧路词典囗汉语大辞典.py
        看看有哪些直接存储的utf8字符串

seed.text.decode_on_err_bytes_
py -m nn_ns.app.debug_cmd   seed.text.decode_on_err_bytes_
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.text.decode_on_err_bytes_   @decode_on_err_bytes_
py -m nn_ns.app.doctest_cmd seed.text.decode_on_err_bytes_:__doc__ -v

from seed.text.decode_on_err_bytes_ import REPLACEMENT_CHARACTER, u8_bytes4REPLACEMENT_CHARACTER
from seed.text.decode_on_err_bytes_ import decode_on_err_bytes_, decode_on_err_bytes_ex_
    #def decode_on_err_bytes_(encoding, bs, /):
    #   :: encoding -> bytes -> (ok_strs/[str], bad_bss/[bytes]{.len=1+len(ok_strs)})
    #
    #def decode_on_err_bytes_ex_(encoding, bs, /):
    #   :: encoding -> bs/bytes -> triples/[(rng4bs/uint%(1+len(bs)), sub_bs/bytes, may ok_str/(str if idx4triples%2==1 else None))]{.len%2==1}
    #

>>> from seed.text.decode_on_err_bytes_ import decode_on_err_bytes_, decode_on_err_bytes_ex_
>>> from seed.text.decode_on_err_bytes_ import REPLACEMENT_CHARACTER, u8_bytes4REPLACEMENT_CHARACTER

>>> decode_on_err_bytes_('u8', b'')
([], [b''])

>>> decode_on_err_bytes_('u8', b'9')
(['9'], [b'', b''])
>>> decode_on_err_bytes_('u8', b'\x80')
([], [b'\x80'])

>>> decode_on_err_bytes_('u8', b'97')
(['97'], [b'', b''])
>>> decode_on_err_bytes_('u8', b'\x80\x81')
([], [b'\x80\x81'])

# [chooes_(2+2;2) == 4*3//2 == 6]
>>> decode_on_err_bytes_('u8', b'97\x80\x81')
(['97'], [b'', b'\x80\x81'])
>>> decode_on_err_bytes_('u8', b'\x8097\x81')
(['97'], [b'\x80', b'\x81'])
>>> decode_on_err_bytes_('u8', b'\x80\x8197')
(['97'], [b'\x80\x81', b''])

>>> decode_on_err_bytes_('u8', b'9\x807\x81')
(['9', '7'], [b'', b'\x80', b'\x81'])
>>> decode_on_err_bytes_('u8', b'\x809\x817')
(['9', '7'], [b'\x80', b'\x81', b''])

>>> decode_on_err_bytes_('u8', b'9\x80\x817')
(['9', '7'], [b'', b'\x80\x81', b''])


>>> decode_on_err_bytes_ex_('u8', b'\x809\x817')
[((0, 1), b'\x80', None), ((1, 2), b'9', '9'), ((2, 3), b'\x81', None), ((3, 4), b'7', '7'), ((4, 4), b'', None)]


#]]]'''
__all__ = r'''
    decode_on_err_bytes_ex_
        decode_on_err_bytes_

    REPLACEMENT_CHARACTER
        u8_bytes4REPLACEMENT_CHARACTER
    '''.split()#'''
    #mk_bytes
__all__



from itertools import pairwise #islice
#from seed.seq_tools.find_all import find_all_, iter_all_
#from seed.seq_tools.mk_nonsubseq_of import check_antisubseq_, mk_a_nonsub_uint_seq_of_uint_seq_, mk_a_nonsubseq_of_
#def mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq, /)->antisubseq:
#def mk_a_nonsubseq_of_(key_seq, /, *, is_key_ok, extra_keys)->antisubseq:

#from codecs import lookup_error, register_error

REPLACEMENT_CHARACTER = '\uFFFD'
u8_bytes4REPLACEMENT_CHARACTER = b'\xef\xbf\xbd'
assert ord('�') == 0xFFFD
assert REPLACEMENT_CHARACTER == '\uFFFD' == chr(0xFFFD) == '�' == u8_bytes4REPLACEMENT_CHARACTER.decode('u8') == b'\x80'.decode(encoding='ascii', errors='replace')
assert chr(0xFFFD).encode("u8") == b'\xef\xbf\xbd' == u8_bytes4REPLACEMENT_CHARACTER

def _():
    REPLACEMENT_CHARACTER
    extra_keys = '�\n'
    assert len(extra_keys)==2==len({*extra_keys})
    def is_key_ok(ch, /):
        return ch in extra_keys
    return extra_keys, is_key_ok
def _(bad_uint, /):
    extra_keys = ''.join(map(chr, range(bad_uint)))
    assert len(extra_keys)==bad_uint==len({*extra_keys})
    def is_key_ok(ch, /):
        return ord(ch) < len(extra_keys)
    return extra_keys, is_key_ok
if 0:
    class _Globals:
        bad_uint = 0x80
        extra_keys, is_key_ok = _(bad_uint)

assert b'' == REPLACEMENT_CHARACTER.encode(encoding='ascii', errors='ignore')

def mk_bytes(bs, /):
    if not type(bs) is bytes:
        bs = bytes(bs)
    assert type(bs) is bytes
    return bs

#def inexactly_decode_(encoding, bs, /):
def decode_on_err_bytes_(encoding, bs, /):
    r'''encoding -> bytes -> (ok_strs/[str], bad_bss/[bytes]{.len=1+len(ok_strs)})

    assert len(ok_strs)+1==len(bad_bss)
    assert all(ok_strs)
    assert all(bad_bss[1:-1])
    '''#'''
    triples = decode_on_err_bytes_ex_(encoding, bs)
    #ok_str__join__bad_bss = [*g(bs)]
    ok_str__join__bad_bss = [m if m else sub_bs for idx4triples,(_,sub_bs,m) in enumerate(triples)]
    assert len(ok_str__join__bad_bss)%2==1
    #return ok_str__join__bad_bss
    ok_strs = ok_str__join__bad_bss[1::2]
    bad_bss = ok_str__join__bad_bss[0::2]
    assert all(type(bad_bs) is bytes for bad_bs in bad_bss)
    assert all(type(ok_str) is str for ok_str in ok_strs)

    assert len(ok_strs)+1==len(bad_bss)
    assert all(ok_strs)
    assert all(bad_bss[1:-1])
    return (ok_strs, bad_bss)

def decode_on_err_bytes_ex_(encoding, bs, /):
    r'''encoding -> bs/bytes -> triples/[(rng4bs/uint%(1+len(bs)), sub_bs/bytes, may ok_str/(str if idx4triples%2==1 else None))]{.len%2==1}

    assert all(type(rng4bs) is tuple and len(rng4bs)==2 and all(type(i) is int for i in rng4bs) for (rng4bs,_,_) in triples)
    assert all(type(sub_bs) is bytes for (_,sub_bs,_) in triples)
    assert all(may_ok_str is None or type(may_ok_str) is str for (_,_,may_ok_str) in triples)

    assert all(j_==_i for ((i_,j_),_,_),((_i,_j),_,_) in pairwise(triples))
    assert all(i <= j for ((i,j),_,_) in triples)
    assert 0 == triples[0][0][0]
    assert len(bs) == triples[-1][0][1]
    assert all(mk_bytes(bs[i:j])==sub_bs for ((i,j),sub_bs,_) in triples)


    assert len(triples)%2 == 1
    assert all((m is None) is (idx4triples%2==0) for idx4triples,(_,_,m) in enumerate(triples))
    assert all(ok_bs and ok_str for (_,ok_bs,ok_str) in triples[1::2])
    assert all(bad_bs for (_,bad_bs,_) in triples[2:-1:2])
    '''#'''
    #find_all_
    #mk_a_nonsubseq_of_
    #mk_a_nonsubseq_of_(bs, is_key_ok=_Globals.is_key_ok, extra_keys=_Globals.extra_keys)
    #mk_a_nonsub_uint_seq_of_uint_seq_(0x80, bs.translate(... ch >= 0x80 -> 0x80 ...))
    #sep = u8_bytes4REPLACEMENT_CHARACTER
    #bs = memoryview(bs)
    memoryview(bs)
    saved_bs = bs

    sep = REPLACEMENT_CHARACTER.encode(encoding=encoding, errors='ignore')
        #sep may be b''
        # [encoding=='ascii'] ==>> [sep==b'']

    if 0:
        bs.find(sep)
        #AttributeError: 'memoryview' object has no attribute 'find'
        bs.split(sep)
        #AttributeError: 'memoryview' object has no attribute 'split'

    bss = [bs] if not sep else bs.split(sep)
    assert bss

    def f(bs, /):
        ls = bs.decode(encoding=encoding, errors='replace').split(REPLACEMENT_CHARACTER)
        return ls
    lss = [*map(f, bss)]
    assert lss
    assert all(lss)
    it = iter(lss)
    for xs in it:
        break
    ls = [*xs]
    b = REPLACEMENT_CHARACTER
    for xs in it:
        a = ls.pop()
        c = xs[0]
        L = len(ls)
        ls += xs
        ls[L] = f'{a}{b}{c}'
    ls = [*filter(bool, ls)]

    def g(bs, /):
        i = 0
        for ok_str in ls:
            assert ok_str
            ok_bs = ok_str.encode(encoding)
            assert ok_bs
            j = bs.index(ok_bs, i)
            bad_bs = bs[i:j]
            bad_bs = mk_bytes(bad_bs)
                # to avoid bytearray
            assert type(bad_bs) is bytes
            k = j+len(ok_bs)
            assert ok_bs == bs[j:k]
            if 0:
                yield bad_bs
                yield ok_str
            else:
                yield ((i,j), bad_bs, None)
                yield ((j,k), ok_bs, ok_str)
            i = k
        if 1:
            bad_bs = bs[i:]
            if 0:
                yield bad_bs
            else:
                j = len(bs)
                yield ((i,j), bad_bs, None)

    assert saved_bs is bs
    triples = [*g(bs)]

    assert all(type(rng4bs) is tuple and len(rng4bs)==2 and all(type(i) is int for i in rng4bs) for (rng4bs,_,_) in triples)
    assert all(type(sub_bs) is bytes for (_,sub_bs,_) in triples)
    assert all(may_ok_str is None or type(may_ok_str) is str for (_,_,may_ok_str) in triples)

    assert all(j_==_i for ((i_,j_),_,_),((_i,_j),_,_) in pairwise(triples))
    assert all(i <= j for ((i,j),_,_) in triples)
    assert 0 == triples[0][0][0]
    assert len(bs) == triples[-1][0][1]
    assert all(mk_bytes(bs[i:j])==sub_bs for ((i,j),sub_bs,_) in triples)


    assert len(triples)%2 == 1
    assert all((m is None) is (idx4triples%2==0) for idx4triples,(_,_,m) in enumerate(triples))
    assert all(ok_bs and ok_str for (_,ok_bs,ok_str) in triples[1::2])
    assert all(bad_bs for (_,bad_bs,_) in triples[2:-1:2])
    return triples
#end-def decode_on_err_bytes_ex_(encoding, bs, /):
#end-def decode_on_err_bytes_(encoding, bs, /):




from seed.text.decode_on_err_bytes_ import decode_on_err_bytes_, decode_on_err_bytes_ex_
    #def decode_on_err_bytes_(encoding, bs, /):
    #   :: encoding -> bytes -> (ok_strs/[str], bad_bss/[bytes]{.len=1+len(ok_strs)})
    #
    #def decode_on_err_bytes_ex_(encoding, bs, /):
    #   :: encoding -> bs/bytes -> triples/[(rng4bs/uint%(1+len(bs)), sub_bs/bytes, may ok_str/(str if idx4triples%2==1 else None))]{.len%2==1}
    #

from seed.text.decode_on_err_bytes_ import REPLACEMENT_CHARACTER, u8_bytes4REPLACEMENT_CHARACTER
