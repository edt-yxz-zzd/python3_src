#__all__:goto
r'''[[[
e ../../python3_src/seed/io/find__naive.py
see:
    seed.iters.find
        #search subseq
        #using failure_func
    nn_ns.bin.stream_search
        #search subseq
        #using polynomial hash
    seed.seq_tools.seq_index_if
        #search value
        #using predicator
    seed.text.StepDecoder
        #def&search "line"
        #using step_builder,step_predicator
    ----
    seed.io.find__naive
        #using str.find/bytes.find/seq.?find?
        #why naive? nn_ns.app.search_bytes_in_file using seed.iters.find too fancy too slow to search bytes in big file
    ----
    seed.seq_tools.find_all
        #search subseq
        #using str.find/bytes.find/seq.?find?, or seed.iters.find
    nn_ns.app.search_bytes_in_file
        #using seed.io.find__naive or seed.iters.find


[[search substr/subbytes
  hash? no! py is slow to mk call on per byte ==>> depend on C
  block
    W-whole_size
    B-block_size
    T-target_size
    O((W/B)*((B+T-1)*2+T) + init(T))
    =O((W/B)*(2*B+3*T+init(T)) + INIT(T))
    =O(W*(2*B/B+3*T/B+init(T)/B) + INIT(T))

    init(T) =?= k*T*log2(T)
    let B > 3*k*T*log2(T)
    let B := max(16K,16*T*log2(T))
]]



seed.io.find__naive
py -m nn_ns.app.debug_cmd   seed.io.find__naive -x
py -m nn_ns.app.doctest_cmd seed.io.find__naive:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.io.find__naive!
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.io.find__naive   @f
from seed.io.find__naive import iter_find_bytes__naive_, list_find_bytes__naive_





>>> from io import BytesIO
>>> min_block_size = 2
>>> bs = b'012abc6789abc'
>>> ibfile = BytesIO(bs)

>>> len(bs)
13
>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_(b'', ibfile)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_(b'abc', ibfile)
[3, 10]
>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size)
[3, 10]


>>> bs = b'x'*10000 + b'012abc6789abc'
>>> ibfile = BytesIO(bs)

>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_(b'abc', ibfile)
[10003, 10010]
>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size)
[10003, 10010]


#neednot:>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=10002)
[10003, 10010]
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=10003)
[10003, 10010]
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=10004)
[10010]
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=-9)
[10010]
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=-10)
[10003, 10010]

>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=10002, may_negativeable_end_location=-1)
[10003]
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=10002, may_negativeable_end_location=-7)
[10003]
>>> list_find_bytes__naive_(b'abc', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=10002, may_negativeable_end_location=-8)
[]



>>> bs = b'012aaa6789aaa'
>>> ibfile = BytesIO(bs)
>>> list_find_bytes__naive_(b'aa', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=0)
[3, 4, 10, 11]
>>> list_find_bytes__naive_(b'aa', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=0, overlap=False)
[3, 10]


>>> list_find_bytes__naive_(b'aa', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=0, _force_block_size=1)
Traceback (most recent call last):
    ...
ValueError: too small: _force_block_size==1 < 2==len(target_bytes)


#0%2
>>> list_find_bytes__naive_(b'aa', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=0, _force_block_size=2)
[3, 4, 10, 11]
>>> list_find_bytes__naive_(b'aa', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=0, _force_block_size=2, overlap=False)
[3, 10]


#1%2
>>> list_find_bytes__naive_(b'aa', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=1, _force_block_size=2)
[3, 4, 10, 11]
>>> list_find_bytes__naive_(b'aa', ibfile, min_block_size=min_block_size, may_negativeable_begin_location=1, _force_block_size=2, overlap=False)
[3, 10]







#target_is_bytess=True;re turnon
>>> bs = b'012aaa6789aaa'
>>> ibfile = BytesIO(bs)
>>> list_find_bytes__naive_([b'aa', b'aa6', b'2a'], ibfile, target_is_bytess=True)
Traceback (most recent call last):
    ...
NotImplementedError: overlap=True and target_is_bytess=True
>>> list_find_bytes__naive_([b'aa', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True)
[2, 4, 10]
>>> list_find_bytes__naive_([b'aa', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True, with_found_bytes=True)
[]
>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_([b'aa', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True, with_found_bytes=True)
[(2, b'2a'), (4, b'aa6'), (10, b'aa')]
>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_([b'aa', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True, with_target_idx=True, with_found_bytes=True)
[(2, 2, b'2a'), (4, 1, b'aa6'), (10, 0, b'aa')]
>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_([b'aa', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True, with_target_idx=True)
[(2, 2), (4, 1), (10, 0)]






# b"" and with_extra_output_ex
    'search b"" will not change ibfile.tell()result'
>>> bs = b'012aaa6789aaa'
>>> ibfile = BytesIO(bs)
>>> list_find_bytes__naive_([b'', b'aa', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True, with_found_bytes=True)
[(0, b''), (1, b''), (2, b'2a'), (3, b''), (4, b'aa6'), (5, b''), (6, b''), (7, b''), (8, b''), (9, b''), (10, b'aa'), (11, b''), (12, b''), (13, b'')]
>>> ibfile.tell()
13
>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_([b'', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True, with_found_bytes=True)
[(0, b''), (1, b''), (2, b'2a'), (3, b''), (4, b'aa6'), (5, b''), (6, b''), (7, b''), (8, b''), (9, b''), (10, b''), (11, b''), (12, b''), (13, b'')]
>>> ibfile.tell()
13
>>> __ = ibfile.seek(0)

>>> list_find_bytes__naive_([b'', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True, with_target_idx=True)
[(0, 0), (1, 0), (2, 2), (3, 0), (4, 1), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0)]
>>> ibfile.tell()
13
>>> __ = ibfile.seek(0)
>>> list_find_bytes__naive_([b'', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> ibfile.tell()
0
>>> list_find_bytes__naive_([b'', b'', b''], ibfile, overlap=False, target_is_bytess=True, with_target_idx=True, with_found_bytes=True)
[(0, 0, b''), (1, 0, b''), (2, 0, b''), (3, 0, b''), (4, 0, b''), (5, 0, b''), (6, 0, b''), (7, 0, b''), (8, 0, b''), (9, 0, b''), (10, 0, b''), (11, 0, b''), (12, 0, b''), (13, 0, b'')]
>>> ibfile.tell()
0
>>> list_find_bytes__naive_([b'', b'', b''], ibfile, overlap=False, target_is_bytess=True, with_target_idx=True, with_found_bytes=True, with_len_found_bytes=True)
[(0, 0, b'', 0), (1, 0, b'', 0), (2, 0, b'', 0), (3, 0, b'', 0), (4, 0, b'', 0), (5, 0, b'', 0), (6, 0, b'', 0), (7, 0, b'', 0), (8, 0, b'', 0), (9, 0, b'', 0), (10, 0, b'', 0), (11, 0, b'', 0), (12, 0, b'', 0), (13, 0, b'', 0)]
>>> ibfile.tell()
0
>>> list_find_bytes__naive_([b'', b'aa6', b'2a'], ibfile, overlap=False, target_is_bytess=True, with_len_found_bytes=True)
[(0, 0), (1, 0), (2, 2), (3, 0), (4, 3), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0)]
>>> ibfile.tell()
13


>>> from seed.mapping_tools.dict_op import mapping_symmetric_diff4patch__immutable__default, mapping_symmetric_patch4lhs__immutable__default, mapping_symmetric_patch4rhs__immutable__default


#_to_yield_locals_firstly=True
>>> bs = b'012abc6789abc'
>>> ibfile = BytesIO(bs)
>>> def eq(r, d, /):
...     rd, *ls = r
...     if not rd == d:
...         print(rd)
...         print(mapping_symmetric_diff4patch__immutable__default(rd,d))
...     return ls



# b''
>>> __ = ibfile.seek(0)
>>> eq(list_find_bytes__naive_(b'', ibfile, _to_yield_locals_firstly=True), {'declen_idc': (0,), 'ibfile': ibfile, 'min_block_size': 16384, 'begin_location': 0, 'end_location': 13, '_force_block_size': 0, 'with_target_idx': False, 'with_found_bytes': False, '_to_yield_locals_firstly': True, 'W': 13, 'new_idx4maxT': 0, 'reduced_declen_target_bytes_ls': (b'',), 'maxT': 0, 'b_single': True, 'b_pseudo_single': False, 'begin_location4null': 0, 'minT': 0, 'overlap': True, 'pseudo_reduced_declen_target_bytes_ls': (), 'reduced_declen_idc': (0,), 'target_bytes_ls': (b'',), 'with_extra_output': False, 'with_len_found_bytes': False, 'with_extra_output_ex': False})
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


    'search b"" will not change ibfile.tell()result'
>>> ibfile.tell()
0







# [b'',b'a']
>>> __ = ibfile.seek(0)
>>> eq(list_find_bytes__naive_([b'',b'a'], ibfile, _to_yield_locals_firstly=True, overlap=False, target_is_bytess=True), {'declen_idc': (1, 0), 'ibfile': ibfile, 'min_block_size': 16384, 'begin_location': 0, 'end_location': 13, '_force_block_size': 0, 'with_target_idx': False, 'with_found_bytes': False, '_to_yield_locals_firstly': True, 'W': 13, 'new_idx4maxT': 0, 'reduced_declen_target_bytes_ls': (b'a', b''), 'maxT': 1, 'b_single': False, 'b_pseudo_single': True, 'begin_location4null': 0, 'minT': 0, 'overlap': False, 'pseudo_reduced_declen_target_bytes_ls': (b'a',), 'reduced_declen_idc': (1, 0), 'target_bytes_ls': (b'', b'a'), 'with_extra_output': False, 'with_len_found_bytes': False, 'with_extra_output_ex': False})
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> ibfile.tell()
0





#b'a'
>>> __ = ibfile.seek(0)
>>> eq(list_find_bytes__naive_(b'a', ibfile, _to_yield_locals_firstly=True), {'declen_idc': (0,), 'ibfile': ibfile, 'min_block_size': 16384, 'begin_location': 0, 'end_location': 13, '_force_block_size': 0, 'with_target_idx': False, 'with_found_bytes': False, '_to_yield_locals_firstly': True, 'W': 13, 'new_idx4maxT': 0, 'reduced_declen_target_bytes_ls': (b'a',), 'maxT': 1, 'b_single': True, 'b_pseudo_single': True, 'minT1': 1, 'B': 16384, 'q': 0, 'r': 13, 'minT': 1, 'overlap': True, 'pseudo_reduced_declen_target_bytes_ls': (b'a',), 'reduced_declen_idc': (0,), 'target_bytes_ls': (b'a',), 'with_extra_output': False, 'with_len_found_bytes': False, 'with_extra_output_ex': False})
[3, 10]














# [b'a',b'b']
>>> __ = ibfile.seek(0)
>>> r = list_find_bytes__naive_([b'a',b'b'], ibfile, _to_yield_locals_firstly=True, overlap=False, target_is_bytess=True)
>>> eq(r, {'declen_idc': (0, 1), 'ibfile': ibfile, 'min_block_size': 16384, 'begin_location': 0, 'end_location': 13, '_force_block_size': 0, 'with_target_idx': False, 'with_found_bytes': False, '_to_yield_locals_firstly': True, 'W': 13, 'new_idx4maxT': 0, 'reduced_declen_target_bytes_ls': (b'a', b'b'), 'maxT': 1, 'b_single': False, 'b_pseudo_single': False, 'minT1': 1, 'B': 16384, 'q': 0, 'r': 13, 'pattern': b'(?:a|b)', 'minT': 1, 'overlap': False, 'pseudo_reduced_declen_target_bytes_ls': (b'a', b'b'), 'reduced_declen_idc': (0, 1), 'regex': re.compile(b'(?:a|b)'), 'target_bytes_ls': (b'a', b'b'), 'with_extra_output': False, 'with_len_found_bytes': False, 'with_extra_output_ex': False})
[3, 4, 10, 11]

>>> r[0]['regex']
re.compile(b'(?:a|b)')







# [b'a',b'b'], with_target_idx=True
    pattern,regex changed
>>> __ = ibfile.seek(0)
>>> r = list_find_bytes__naive_([b'a',b'b'], ibfile, _to_yield_locals_firstly=True, overlap=False, target_is_bytess=True, with_target_idx=True)
>>> eq(r, {'declen_idc': (0, 1), 'ibfile': ibfile, 'min_block_size': 16384, 'begin_location': 0, 'end_location': 13, '_force_block_size': 0, 'with_target_idx': True, 'with_found_bytes': False, '_to_yield_locals_firstly': True, 'W': 13, 'new_idx4maxT': 0, 'reduced_declen_target_bytes_ls': (b'a', b'b'), 'maxT': 1, 'b_single': False, 'b_pseudo_single': False, 'minT1': 1, 'B': 16384, 'q': 0, 'r': 13, 'pattern': b'(?:(a)|(b))', 'minT': 1, 'overlap': False, 'pseudo_reduced_declen_target_bytes_ls': (b'a', b'b'), 'reduced_declen_idc': (0, 1), 'regex': re.compile(b'(?:(a)|(b))'), 'target_bytes_ls': (b'a', b'b'), 'with_extra_output': True, 'with_len_found_bytes': False, 'with_extra_output_ex': True})
[(3, 0), (4, 1), (10, 0), (11, 1)]

>>> r[0]['regex']
re.compile(b'(?:(a)|(b))')
























################################
################################
################################
################################
#try re
>>> m=re.match('((?P<_1>a)|(?P<_2>b))', 'b')
>>> m.groupdict()
{'_1': None, '_2': 'b'}
>>> m.groups()
('b', None, 'b')
>>> m.lastindex
1
>>> m.lastgroup
>>> None
>>> m=re.match('((a)|(b))', 'b')
>>> m.lastindex
1
>>> m=re.match('a|b', 'b')
>>> m.lastindex
>>> None


#]]]'''
__all__ = r'''
    iter_find_bytes__naive_
        list_find_bytes__naive_
'''.split()#'''
__all__

import re
from seed.for_libs.for_re import iter_find_matchobjs_, iter_find_spans_, list_find_spans_
    #def iter_find_matchobjs_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, /, *, overlap:bool):
from seed.io.get_size_of_ibfile import get_size_of_ibfile, get_size_of_ibfile_ex, explain_may_negativeable_end_locations_of_ibfile_ex, explain_negativeable_location_of_ibfile_ex, explain_may_negativeable_location_rng_of_ibfile_ex#; #may have [len(ibfile) < end_location]

from seed.math.floor_ceil import floor_log2, ceil_log2
from seed.tiny import check_type_is, check_uint, mk_tuple
from itertools import repeat, chain, pairwise

#bufsize4zlib_decompress = 0x4000
min_block_size = 0x4000 #16K
#min_block_size = 16<<20 #16M
if 1:
    #deleted at eof
    overlap=True
    may_negativeable_begin_location=None
    may_negativeable_end_location=None
    _force_block_size=0
    target_is_bytess=False
    with_target_idx=False
    with_found_bytes=False
    with_len_found_bytes=False
    _to_yield_locals_firstly=False


def list_find_bytes__naive_(target_bytes, ibfile, /, *, overlap=overlap, min_block_size=min_block_size, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location, _force_block_size=_force_block_size, target_is_bytess=target_is_bytess, with_target_idx=with_target_idx, with_found_bytes=with_found_bytes, with_len_found_bytes=with_len_found_bytes, _to_yield_locals_firstly=_to_yield_locals_firstly):
    'search b"" will not change ibfile.tell()result'
    return [*iter_find_bytes__naive_(target_bytes, ibfile, overlap=overlap, min_block_size=min_block_size, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location, _force_block_size=_force_block_size, target_is_bytess=target_is_bytess, with_target_idx=with_target_idx, with_found_bytes=with_found_bytes, with_len_found_bytes=with_len_found_bytes, _to_yield_locals_firstly=_to_yield_locals_firstly)]


def iter_find_bytes__naive_(target_bytes, ibfile, /, *, overlap=overlap, min_block_size=min_block_size, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location, _force_block_size=_force_block_size, target_is_bytess=target_is_bytess, with_target_idx=with_target_idx, with_found_bytes=with_found_bytes, with_len_found_bytes=with_len_found_bytes, _to_yield_locals_firstly=_to_yield_locals_firstly):
    'search b"" will not change ibfile.tell()result'
    check_type_is(bool, overlap)
    check_uint(min_block_size)
    check_uint(_force_block_size)
    check_type_is(bool, _to_yield_locals_firstly)
    check_type_is(bool, with_target_idx)
    check_type_is(bool, with_found_bytes)
    check_type_is(bool, with_len_found_bytes)
    check_type_is(bool, target_is_bytess)
    if target_is_bytess:
        target_bytes_ls = target_bytes;del target_bytes
        #target_bytes_ls = sorted(target_bytes_ls, key=len, reverse=True)
        #target_bytes = target_bytes_ls[0] #with max len
    else:
        check_type_is(bytes, target_bytes)
        target_bytes_ls = [target_bytes]
    target_bytes_ls = mk_tuple(target_bytes_ls)

    if not target_bytes_ls: raise TypeError
    for target_bytes in target_bytes_ls:
        check_type_is(bytes, target_bytes)

    declen_idc = mk_tuple(sorted(range(len(target_bytes_ls)), key=lambda idx:len(target_bytes_ls[idx]), reverse=True))
    target_bytes = target_bytes_ls[declen_idc[0]] #with max len

    target_bytes_ls
    declen_idc
    target_bytes
    assert len(target_bytes) == max(map(len, target_bytes_ls))

    if not (_force_block_size == 0 or _force_block_size >= len(target_bytes)):raise ValueError(f'too small: _force_block_size=={_force_block_size} < {len(target_bytes)}==len(target_bytes)')
    the_curr_tell_location = ibfile.tell()
    (ibfile_or_sz, (begin_location, end_location)) = explain_may_negativeable_location_rng_of_ibfile_ex(ibfile, the_curr_tell_location, may_negativeable_begin_location, may_negativeable_end_location)
        #; #may have [len(ibfile) < end_location]

    #print(the_curr_tell_location, begin_location, end_location)

    check_uint(begin_location)
    check_uint(end_location)
    if not begin_location == the_curr_tell_location:
        ibfile.seek(begin_location)
    if len(target_bytes_ls)>=2 and overlap:raise NotImplementedError('overlap=True and target_is_bytess=True')
    assert target_bytes_ls
    assert target_bytes_ls[declen_idc[0]] is target_bytes
    return _iter_find_bytes__naive_(declen_idc, target_bytes_ls, ibfile, overlap, min_block_size, begin_location, end_location, _force_block_size, with_target_idx, with_found_bytes, with_len_found_bytes, _to_yield_locals_firstly)





def _find_maxT_le_W(target_bytes_ls, declen_idc, W, /):
    for new_idx, old_idx in enumerate(declen_idc):
        if not W < len(target_bytes_ls[old_idx]):
            return new_idx
    raise logic-err
def _mk_reduced_declen_target_bytes_ls_ex(target_bytes_ls, declen_idc, new_idx4maxT, /):
    ls = []
    s = set()
    reduced_declen_idc = []
    for old_idx in declen_idc[new_idx4maxT:]:
        target_bytes = target_bytes_ls[old_idx]
        s.add(target_bytes)
        if len(s)==len(ls):continue
        ls.append(target_bytes)
        reduced_declen_idc.append(old_idx)
        assert len(s)==len(ls)
    return mk_tuple(ls), mk_tuple(reduced_declen_idc)

def _iter_find_bytes__naive_(declen_idc, target_bytes_ls, ibfile, overlap, min_block_size, begin_location, end_location, _force_block_size, with_target_idx, with_found_bytes, with_len_found_bytes, _to_yield_locals_firstly:'.regex is exported to be used by nn_ns.bin.find_zlib_objs_in_file::iter_find_xxx_objs_in_file_', /):
    #now support:assert not (len(target_bytes_ls)>=2 and overlap), NotImplementedError('... overlap=True and len(target_bytes_ls)>=2 ...')
    #assert all(len(a)>=len(b) for a,b in pairwise(target_bytes_ls)), 'requires target_bytes_ls sorted by len <<== re.(|) choose first not longest'
    assert len(declen_idc) == len(target_bytes_ls)
    assert all(len(target_bytes_ls[a])>=len(target_bytes_ls[b]) for a,b in pairwise(declen_idc)), 'requires target_bytes_ls***declen_idc sorted by len <<== re.(|) choose first not longest'

    def locals_(locals, /, *nms):
        d = {**locals}
        #del d['find_iter']
        #del d['_iter_results4null']
        #del d['locals_']
        for nm in nms:
            del d[nm]
        return d
    excluded_nms = ['locals_', 'excluded_nms']
    if not ibfile.tell() == begin_location:
        #seeked but fail
        if _to_yield_locals_firstly:
            yield locals_(locals(), *excluded_nms)
            #yield locals_(locals())
            #yield {**locals()}
        return#main_return

    minT = len(target_bytes_ls[declen_idc[-1]])
    assert minT == min(map(len, target_bytes_ls))


    #avoid if possible:fsz = get_size_of_ibfile(ibfile)
    #   now only when minT==0
    if minT == 0:
        #may have [len(ibfile) < end_location]
        fsz = get_size_of_ibfile(ibfile)
        end_location = min(fsz, end_location);del fsz
        # [end_location <= len(ibfile)]
    # [minT == 0] -> [end_location <= len(ibfile)]
    #  when [minT > 0], since [len(ibfile) < end_location] read no bytes, has no result

    W = end_location -begin_location
    #old@b_single:
        #if W < T:
    if W < minT:
        #bad rng or too few bytes
        if _to_yield_locals_firstly:
            yield locals_(locals(), *excluded_nms)
        return#main_return
    assert W >= minT >= 0
    assert end_location  >= begin_location
    # [minT == 0] -> [end_location <= len(ibfile)]
    # [W >= minT >= 0]
    # [end_location  >= begin_location]
    new_idx4maxT = _find_maxT_le_W(target_bytes_ls, declen_idc, W)
    reduced_declen_target_bytes_ls, reduced_declen_idc = _mk_reduced_declen_target_bytes_ls_ex(target_bytes_ls, declen_idc, new_idx4maxT)


    #reduce
    # if len(target_bytes) > W, remove
    # recalc maxT, b_single
    maxT = len(reduced_declen_target_bytes_ls[0])
    #old@b_single:
        #T = len(target_bytes)
    assert maxT == max(map(len, reduced_declen_target_bytes_ls))
    assert minT <= maxT <= W
    # [minT <= maxT <= W]
    if 0:
        b_single = len(declen_idc)-new_idx4maxT==1 or maxT == 0 or (minT==maxT and all(x==y for x,y in pairwise(reduced_declen_target_bytes_ls)))
        if b_single:
            target_bytes_ls = (target_bytes_ls[0],)

    else:
        #now removed duplicates
        b_single = len(reduced_declen_idc)==1

    if minT==0:
        pseudo_reduced_declen_target_bytes_ls = reduced_declen_target_bytes_ls[:-1]
    else:
        pseudo_reduced_declen_target_bytes_ls = reduced_declen_target_bytes_ls
    #xxx assert pseudo_reduced_declen_target_bytes_ls
    assert all(pseudo_reduced_declen_target_bytes_ls)
    b_pseudo_single = len(pseudo_reduced_declen_target_bytes_ls)==1




    with_extra_output = with_target_idx or with_found_bytes
    with_extra_output_ex = with_extra_output or with_len_found_bytes
    if minT == 0 and with_extra_output_ex:
        extras4null = []
        old_idx4null = reduced_declen_idc[-1]
        null_bytes = target_bytes_ls[old_idx4null]
        assert null_bytes == b''
        if with_target_idx:
            #extras4null.append(0)
            extras4null.append(old_idx4null)
        if with_found_bytes:
            extras4null.append(null_bytes)
        if with_len_found_bytes:
            extras4null.append(0)


    if minT == 0:
        begin_location4null = begin_location
    def _iter_results4null(found_location, /, *, not_found=False):
        nonlocal begin_location4null
        #since [end_location <= file_size]@[minT == 0]
        #   found_location can be 1+end_location
        #
        # [minT == 0] -> [end_location <= len(ibfile)]
        if not minT == 0:
            return ''
        else:
            begin_location4null #check exists
            rng = range(begin_location4null, bool(not_found)+found_location)
            begin_location4null = 1+found_location
                #found_location was occupied by longer match; skip it
                #or not_found, yield already
            if with_extra_output_ex:
                extras4null #check exists
                return ((location4null, *extras4null) for location4null in rng)
            else:
                return rng
    #end-def _iter_results4null(found_location, /, *, not_found=False):
    excluded_nms.append('_iter_results4null')

    # [minT <= maxT <= W]
    if minT == 0 and (b_single or not with_extra_output_ex): #not with_extra_output
        # all position
        # [minT == 0] -> [end_location <= len(ibfile)]
        #
        #bug:yield from range(begin_location, end_location)
        if _to_yield_locals_firstly:
            yield locals_(locals(), *excluded_nms)
        yield from _iter_results4null(1+end_location)#begin_location4null
        return#main_return
    # [not (minT == 0 and b_single)]
    # [minT > 0 or not b_single]
    assert maxT > 0
    # [maxT > 0]
    assert pseudo_reduced_declen_target_bytes_ls


    #if minT == 0 and not (b_single or not with_extra_output): raise NotImplementedError('search b"" but ...too many options')
        #assert minT > 0

    #assert minT > 0 or not (b_single or not with_extra_output)
    assert minT > 0 or (not b_single and with_extra_output_ex)
    if minT > 0:
        minT1 = minT
    elif minT == 0 and not (b_single or not with_extra_output_ex):
        #minT1 = min(map(len, filter(bool, target_bytes_ls)))
        minT1 = len(reduced_declen_target_bytes_ls[-2])
    else:
        assert minT == 0 and (b_single or not with_extra_output_ex)
        #del minT1 = ???N/A
        raise logic-err

    assert minT >= 0
    assert (minT == 0 and (b_single or not with_extra_output_ex)) or minT1 > 0


    if minT==0:
        assert (not b_single and with_extra_output_ex)
        minT1 #check defined
    else:
        # [minT > 0]
        # [minT1 := minT]
        minT1 #check defined
    minT1 #check defined
    assert W >= maxT >= minT1 > 0
    # [minT==0] -> [[not b_single][with_extra_output_ex]]
    # [minT1 defined]
    # [0 < minT1 <= maxT <= W]



    #old@b_single:
        #B = max(min_block_size, 16*ceil_log2(T+2)*T)
    B = max(min_block_size, 16*ceil_log2(maxT+2)*maxT)
    if _force_block_size:
        B = _force_block_size
    #old@b_single:
        #if not B >= T: raise logic-err
    if not B >= maxT > 0: raise logic-err

    q,r = divmod(W,B)
    #print(q,r, W,B)
    #old@b_single:
        #sz4step = 1 if overlap else T
    #sz4step_ = lambda found_bs:1 if overlap else len(found_bs)
    #bug:assert q > 0
    #old@b_single:
        #assert W >= T > 0
    #now may [minT==0]:xxx assert W >= minT > 0
    #old@b_single:
        #assert B >= 16*T > 0 or _force_block_size
    assert B >= 16*maxT > 0 or _force_block_size
    #old@b_single:
        #assert sz4step > 0
    #assert sz4step_ ???
    #now may [minT==0]:xxx assert all(target_bytes_ls)
    assert all(pseudo_reduced_declen_target_bytes_ls)
    assert pseudo_reduced_declen_target_bytes_ls

    #if not b_single:
    if not b_pseudo_single:
        #using re
        #pattern = b'(?:' + b'|'.join(map(re.escape, target_bytes_ls)) + b')'
        #if with_found_bytes
        if with_target_idx:
            #pattern = b'(?:' + b'|'.join(b'(' +re.escape(target_bytes_ls[idx]) +b')' for idx in declen_idc) + b')'
            pattern = b'(?:' + b'|'.join(b'(' +re.escape(bs) +b')' for bs in pseudo_reduced_declen_target_bytes_ls) + b')'
                #catch subpattern
        else:
            #pattern = b'(?:' + b'|'.join(re.escape(target_bytes_ls[idx]) for idx in declen_idc) + b')'
            pattern = b'(?:' + b'|'.join(map(re.escape, pseudo_reduced_declen_target_bytes_ls)) + b')'
        #requires target_bytes_ls sorted by len here
        regex = re.compile(pattern)
        #if overlap:raise logic-err
        1;  regex.finditer # only nonoverlap
        if 1:
          1;iter_find_matchobjs_ # extend regex.finditer with `overlap`
            #def iter_find_matchobjs_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, /, *, overlap:bool):
          def find_iter(bs, max_i, /):
            '-> Iter (i@bs, may old target_idx, may found_bs, len_found_bs)'
            for m in iter_find_matchobjs_(regex, minT1, maxT, bs, None, max_i, None, overlap=overlap):
                (i, may_target_idx, may_found_bs, len_found_bs) = _m2o5re(m)
                assert i <= max_i
                yield (i, may_target_idx, may_found_bs, len_found_bs)
        elif overlap:
          def find_iter(bs, max_i, /):
            '-> Iter (i@bs, may old target_idx, may found_bs, len_found_bs)'
            i = 0
            while i <= max_i:
                m = regex.search(bs, i, max_i+maxT)
                if m is None:break
                i = m.start(0)
                if max_i < i:break
                (i, may_target_idx, may_found_bs, len_found_bs) = _m2o5re(m)
                yield (i, may_target_idx, may_found_bs, len_found_bs)
                i += 1
            return;yield

        else:
          assert not overlap
          def find_iter(bs, max_i, /):
            '-> Iter (i@bs, may old target_idx, may found_bs, len_found_bs)'
            for m in regex.finditer(bs):
                i = m.start(0)
                if max_i < i:break
                (i, may_target_idx, may_found_bs, len_found_bs) = _m2o5re(m)
                yield (i, may_target_idx, may_found_bs, len_found_bs)

                #_b,_e = m.span(0)
                #j = i+(_e-_b)
                #yield from _iter4overlap_that_begin_between__(bs, i, j)

        #end-def find_iter(bs, max_i, /):
        def may_target_idx5may_branch_idx_(may_branch_idx, /):
            if may_branch_idx is None:
                may_target_idx = None
            else:
                regex_branch_idx = may_branch_idx
                new_target_idx = regex_branch_idx-1
                assert new_target_idx >= 0
                #old_target_idx = declen_idc[new_target_idx]
                    #new idx -> old idx
                assert new_target_idx <= len(pseudo_reduced_declen_target_bytes_ls) <= len(reduced_declen_idc)
                old_target_idx = reduced_declen_idc[new_target_idx]
                    #reduced new idx -> old idx
                may_target_idx = old_target_idx
            return may_target_idx
        #end-def may_target_idx5may_branch_idx_(may_branch_idx, /):
        excluded_nms.append('may_target_idx5may_branch_idx_')
        def _m2o5re(m, /):
            '-> (i@bs, may old target_idx, may found_bs, len_found_bs)'
            #i = m.start(0)
            i,j = m.span(0)
            len_found_bs = (j-i)
            may_found_bs = m.group(0) if with_found_bytes else None
            may_branch_idx = m.lastindex
            may_target_idx = may_target_idx5may_branch_idx_(may_branch_idx)
            return i, may_target_idx, may_found_bs, len_found_bs
        excluded_nms.append('_m2o5re')
    else:
        #assert b_single
        assert b_pseudo_single
        def find_iter(bs, max_i, /):
            '-> Iter (i@bs, may target_idx, may found_bs, len_found_bs)'
            #assert len(bs) >= minT > 0
            assert len(bs) >= maxT == minT1 > 0
            assert minT in [0, minT1]
            #[target_bytes] = target_bytes_ls
            [target_bytes] = pseudo_reduced_declen_target_bytes_ls
            found_bs = target_bytes
            len_found_bs = len(found_bs)
            T = len(target_bytes)
            assert T==maxT
            assert max_i + T == len(bs)
            #target_idx = 0
            target_idx = reduced_declen_idc[0]
            sz4step = 1 if overlap else T
            assert 0 < sz4step <= T
            j = 0
            assert 0 <= j < len(bs)
            while True:
                i = bs.find(target_bytes, j)
                if i < 0:
                    break
                yield i, target_idx, found_bs, len_found_bs
                j = i+sz4step
                assert 0 < j <= len(bs) # <<== T >= sz4step > 0
            end4last_match_or_0 = j
        #end-def find_iter(bs, max_i, /):
    find_iter
    excluded_nms.append('find_iter')

    def search_loop():
      if 1:
        block_location = begin_location
        prev = b''
        #old@b_single:
            #assert len(prev) < T
        #now may [minT==0]:xxx assert len(prev) < minT #not maxT
        assert len(prev) < minT1 #not maxT,minT

      #for _ in range(q):
      for sz in chain(repeat(B,q), [r] if r else []):
        #print(sz)
        assert sz
        #old@b_single:
            #assert len(prev) < T
        assert len(prev) < maxT #not minT/minT1
        #bs = prev+ibfile.read(sz)
        _bs = ibfile.read(sz)
        bs = prev+_bs
        #eof = len(_bs) < sz or sz < B
        eof = len(_bs) < B
        #old@b_single:
            #if len(bs) < T:
        if len(bs) < minT1: #not maxT/minT
            assert eof
            #eof
            #   not searched
            #   but only null_bytes can match
            #may have [file.eof < end_location]
            break
        # [minT1 <= len(bs) <?> maxT]
        if 1:
            _max_i = len(bs)-minT1
            max_i = _max_i if eof else len(bs)-maxT
            assert 0 <= max_i <= _max_i
        if 1:
            #dumb value only for end4last_match_or_0
            #i = 0; found_bs = b''
            i = None
        for o5f in find_iter(bs, max_i):
            _i = o5f[0]
            assert 0 <= _i <= _max_i
            #if not eof and len(bs)-_i < maxT:break
            if max_i < _i:break
            (i, may_target_idx, may_found_bs, len_found_bs) = o5f
            found_location = block_location+i
            yield from _iter_results4null(found_location)#begin_location4null
            len_found_bs
            ts = [found_location]

            if with_target_idx:
                assert not may_target_idx is None
                target_idx = may_target_idx
                ts.append(target_idx)
            ts

            if with_found_bytes:
                found_bs = may_found_bs
                if with_target_idx:
                    target_idx
                    target_bytes = target_bytes_ls[target_idx]
                    assert target_bytes is found_bs or target_bytes == found_bs
                    found_bs = target_bytes
                ts.append(found_bs)
            ts

            if with_len_found_bytes:
                ts.append(len_found_bs)

            if len(ts)==1:
                [found_location] = ts
                yield found_location
            else:
                yield (*ts,)
            if i == max_i:break

        #end4last_match_or_0 = j
        (begin4last_match_or_0, end4last_match_or_0) = ((0,0) if i is None else (i,i+len_found_bs)); del i

        #old@b_single:
            #assert len(bs) >= T
            #sz4skip = len(bs)-T+1
            #assert 0 < sz4skip <= len(bs)
        # [minT1 <= len(bs) <?> maxT]
        if len(bs) < maxT: #not minT1/minT
            assert eof
            #eof
            #   has searched until eof
            #may have [file.eof < end_location]
            break
        # [maxT <= len(bs)]
        assert len(bs) >= maxT >= minT1 >= 1
        sz4skip = 1+max(len(bs)-maxT, begin4last_match_or_0)
        assert 0 < sz4skip <= len(bs)

        if not overlap:
            sz4skip = max(end4last_match_or_0, sz4skip)
        assert 0 < sz4skip <= len(bs)
        prev = bs[sz4skip:]
        block_location += sz4skip
            #block_location grow strictly
        yield from _iter_results4null(block_location-1, not_found=True)#begin_location4null
      #end-main-loop
      if 1:
        yield from _iter_results4null(1+end_location)#begin_location4null
        return
    #end-def search_loop():
    excluded_nms.append('search_loop')

    if _to_yield_locals_firstly:
        #after 『def find_iter()』to export `regex`
        yield locals_(locals(), *excluded_nms)
    yield from search_loop()
    return#main_return

if 1:
    #deleted at eof
    del overlap
    del may_negativeable_begin_location
    del may_negativeable_end_location
    del _force_block_size
    del target_is_bytess
    del with_target_idx
    del with_found_bytes
    del with_len_found_bytes
    del _to_yield_locals_firstly
from seed.io.find__naive import iter_find_bytes__naive_, list_find_bytes__naive_
from seed.io.find__naive import *
