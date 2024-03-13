#__all__:goto
r'''[[[
e ../../python3_src/seed/types/PruneableArray.py
vs:
    view ../../python3_src/seed/types/CuttableStream.py


不太像正常数组，所以取消MutableSequence
    主要多了个prune_lt_()


[[
bug fixed!!
===
found bug@nn_ns.app.debug_cmd
    from:seed.types.PruneableArray
bug:cannot found unbound_name:『begin』
    -->from seed.pkg_tools.detect_all_unbound_names import DetectAllUnboundNames
    -->from ._forgot_import import symtable2forgots
    -->def _collect_forgots(table, may_context, /):
        patch...
class PruneableArray:
    @property
    def begin(sf, /):
        return sf._begin
    def __contains__(sf, v, /):
        j = sf.index(v, begin, end)
        ...
]]

seed.types.PruneableArray
py -m nn_ns.app.debug_cmd   seed.types.PruneableArray -x
py -m nn_ns.app.doctest_cmd seed.types.PruneableArray:__doc__ --ndiff -ff -v
py_adhoc_call   seed.types.PruneableArray   @f

>>> PruneableArray(0, [])
PruneableArray(0, [])
>>> PruneableArray(-1, [])
Traceback (most recent call last):
    ...
TypeError
>>> PruneableArray(-1, [], negative_offset_ok=True)
PruneableArray(-1, [], negative_offset_ok = True)


>>> ls = PruneableArray(0, [])
>>> ls.validate()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(0, [], _begin = 0, _sz4null = 0, negative_offset_ok = False)'
>>> ls.append(0)
>>> ls.extend(range(1,9))
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(0, [0, 1, 2, 3, 4, 5, 6, 7, 8], _begin = 0, _sz4null = 0, negative_offset_ok = False)'
>>> ls.prune_lt_(0)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(0, [0, 1, 2, 3, 4, 5, 6, 7, 8], _begin = 0, _sz4null = 0, negative_offset_ok = False)'
>>> ls.prune_lt_(1)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(0, [None, 1, 2, 3, 4, 5, 6, 7, 8], _begin = 1, _sz4null = 1, negative_offset_ok = False)'
>>> ls.prune_lt_(0) #skip:2
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(0, [None, 1, 2, 3, 4, 5, 6, 7, 8], _begin = 1, _sz4null = 1, negative_offset_ok = False)'
>>> ls.prune_lt_(3)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(0, [None, None, None, 3, 4, 5, 6, 7, 8], _begin = 3, _sz4null = 3, negative_offset_ok = False)'
>>> ls.prune_lt_(4)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(0, [None, None, None, None, 4, 5, 6, 7, 8], _begin = 4, _sz4null = 4, negative_offset_ok = False)'
>>> ls.prune_lt_(5)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(5, [5, 6, 7, 8], _begin = 5, _sz4null = 0, negative_offset_ok = False)'










>>> ls = PruneableArray(999, range(1, 9))
>>> ls.prune_lt_(999+4)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1003, [5, 6, 7, 8], _begin = 1003, _sz4null = 0, negative_offset_ok = False)'
>>> ls = PruneableArray(999, range(1, 9))
>>> ls.prune_lt_(999+3)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> save = ls._copy4debug_()
>>> save._dump4debug_(); save.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'

    __eq__
    __ne__
    __ge__
    __gt__
    __le__
    __lt__
>>> xs = ls._copy4debug_()
>>> ls == xs
True
>>> ls != xs
False
>>> ls <= xs
True
>>> ls >= xs
True
>>> ls < xs
False
>>> ls > xs
False
>>> xs = ls._copy4debug_()
>>> xs.pop()
8
>>> ls == xs
False
>>> ls != xs
True
>>> ls <= xs
False
>>> ls >= xs
True
>>> ls < xs
False
>>> ls > xs
True

>>> xs = ls._copy4debug_()
>>> xs.prune_lt_(xs.begin+1)
>>> ls == xs
False
>>> ls != xs
True
>>> ls <= xs
True
>>> ls >= xs
False
>>> ls < xs
True
>>> ls > xs
False




>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'

    __iter__
    __reversed__
>>> [*ls]
[4, 5, 6, 7, 8]
>>> [*reversed(ls)]
[8, 7, 6, 5, 4]

>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'

    __len__
    __getitem__
    __setitem__
    __delitem__
>>> len(ls)
5
>>> ls[1002]
4
>>> ls[1006]
8
>>> ls[1001]
Traceback (most recent call last):
    ...
IndexError: 1001
>>> ls[1007]
Traceback (most recent call last):
    ...
IndexError: 1007
>>> ls[1002] = 777
>>> ls[1006] = 777
>>> ls[1001] = 777
Traceback (most recent call last):
    ...
IndexError: 1001
>>> ls[1007] = 777
Traceback (most recent call last):
    ...
IndexError: 1007
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 777, 5, 6, 7, 777], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> del ls[1002]
Traceback (most recent call last):
    ...
IndexError: 1002
>>> del ls[1004]
Traceback (most recent call last):
    ...
IndexError: 1004
>>> del ls[:1004]
Traceback (most recent call last):
    ...
IndexError: slice(None, 1004, None)
>>> del ls[1006]
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 777, 5, 6, 7], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> del ls[1004:]
>>> del ls[1006]
Traceback (most recent call last):
    ...
IndexError: 1006
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [777, 5], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'


    clear
    pop
    append
    extend
    insert
    remove
>>> ls = save._copy4debug_()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> ls.clear()
>>> ls
PruneableArray(1002, [])
>>> ls.pop()
Traceback (most recent call last):
    ...
IndexError: pop empty
>>> ls = save._copy4debug_()
>>> ls.pop()
8
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> ls.pop()
7
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'
>>> ls.append(777)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 777], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'
>>> ls.extend([555, 333])
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 777, 555, 333], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'
>>> ls.remove(777)
>>> ls.insert(ls.begin, 111)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [111, 4, 5, 6, 555, 333], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'


    __add__
    __iadd__
    __imul__
    __mul__
    #__rmul__
>>> ls = save._copy4debug_()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> rs = ls + ls
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'
>>> rs._dump4debug_(); rs.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> rs = ls + ls._copy4debug_()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'
>>> rs._dump4debug_(); rs.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls += ls
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls += ls._copy4debug_()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'


>>> ls = save._copy4debug_()
>>> rs = ls * 3
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'
>>> rs._dump4debug_(); rs.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> rs = ls * 1
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'
>>> rs._dump4debug_(); rs.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> rs = ls * 0
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> rs._dump4debug_(); rs.validate()
'<PruneableArray._dump4debug_>(999, [], _begin = 999, _sz4null = 0, negative_offset_ok = False)'


>>> ls = save._copy4debug_()
>>> ls *= 3
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls *= 1
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls *= 0
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'




    __repr__
    #__str__
    #__reduce__
    #__reduce_ex__
>>> ls = save._copy4debug_()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> ls
PruneableArray(1002, [4, 5, 6, 7, 8])
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'


    __contains__
    count
    index
>>> ls = save._copy4debug_()
>>> 5 in ls
True
>>> 1 in ls
False
>>> ls.index(1)
Traceback (most recent call last):
    ...
ValueError: 1
>>> ls.index(5)
1003
>>> ls.count(1)
0
>>> ls.count(5)
1
>>> ls[-1] = 5
>>> ls.count(5)
2
>>> ls.count(5, None, -1)
1
>>> ls.count(5, 1)
2
>>> ls.count(5, 1003)
2
>>> ls.count(5, 1004)
1
>>> ls.count(5, 1006)
1
>>> ls.count(5, 1007)
0

    copy
    reverse
    sort
>>> ls = save._copy4debug_()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(999, [None, None, None, 4, 5, 6, 7, 8], _begin = 1002, _sz4null = 3, negative_offset_ok = False)'
>>> xs = ls.copy()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'
>>> xs._dump4debug_(); xs.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls.reverse()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [8, 7, 6, 5, 4], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls.sort()
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 5, 6, 7, 8], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls.sort(key=lambda x:x*7%9)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [4, 8, 7, 6, 5], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls.sort(key=int.__neg__)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [8, 7, 6, 5, 4], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'

>>> ls = save._copy4debug_()
>>> ls.sort(reverse=True)
>>> ls._dump4debug_(); ls.validate()
'<PruneableArray._dump4debug_>(1002, [8, 7, 6, 5, 4], _begin = 1002, _sz4null = 0, negative_offset_ok = False)'


#]]]'''
__all__ = r'''

PruneableArray

Error
    Error__iter
        Error__iter_after_prune_too_much
        Error__iter_after_pop_too_much

adjust_slice_
    adjust_until_le_
    adjust_until_ge_

'''.split()#'''
__all__

from seed.math.sign_of import sign_of
from seed.tiny import ifNone, echo, print_err
from seed.tiny import check_type_is
from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.helper.repr_input import repr_helper, repr_helper__str

#from seed.lang.calc_len_of_py_range_ import calc_len_of_py_range_

#from collections.abc import MutableSequence

def adjust_until_le_(upB, i, step, /):
    if not i <= upB:
        r = (upB -i) % abs(step)
        i = upB -r
    return i

def adjust_until_ge_(lowB, i, step, /):
    if not lowB <= i:
        r = (i -lowB) % abs(step)
        i = lowB + r
    return i
def adjust_slice_(rng, sl, /, *, easy_vs_hard, fix_None_only):
    r'''
    >>> range(100)[104::-60]
    range(99, -1, -60)

    '''#'''
    begin, end = rng
    start = sl.start
    stop = sl.stop
    step = sl.step
    step = ifNone(step, 1)

    if step > 0:
        ######################
        if start is None:
            start = begin
        elif fix_None_only:
            pass
        elif easy_vs_hard:
            start = adjust_until_ge_(begin, start, step)
        else:
            start = max(begin, start)
        ######################
        if stop is None:
            stop = end
        elif fix_None_only:
            pass
        else:
            stop = min(end, stop)
        ######################
    elif step < 0:
        ######################
        if start is None:
            start = end-1
        elif fix_None_only:
            pass
        elif easy_vs_hard:
            start = adjust_until_le_(end-1, start, step)
        else:
            start = min(end-1, start)
        ######################
        if stop is None:
            stop = begin-1
        elif fix_None_only:
            pass
        else:
            stop = max(begin-1, stop)
        ######################
    else:
        raise 000
    return slice(start, stop, step)

#class PruneableArray(MutableSequence):
class PruneableArray:
    r'''
    ???'no:append_left <<== __iter__+_offset as modified_detector'
    ===
    ===
    ijk:
        ===
        i - idx5usr
            [[not negative_offset_ok] -> [i<0] -> [wrap i as seq[-1]]]
        ===
        j - abs-idx
            [[j<0] -> [negative_offset_ok]]
            [[not negative_offset_ok] -> [j>=0]]
            [j == sf.explain_idx_(i)]
        ===
        k - rel-idx
            [0 <= sf._sz4null <= k < len(sf._ls)]
            [k == j -sf._offset]
        ===
    ===
    #assume null after end is -inf
    #assume null before begin is +inf
    ===
    ===
    '''#'''
    def __init__(sf, offset, iterable, /, *, negative_offset_ok=False):
        check_type_is(bool, negative_offset_ok)
        if negative_offset_ok:
            check_type_is(int, offset)
        else:
            check_int_ge(0, offset)
        sf._neg_ok = negative_offset_ok
        sf._offset = offset
            # [[not$negative_offset_ok] -> [_offset >= 0]]
            # _offset used in __iter__ as modified_detector
        sf._begin = offset
            # [0 <= _begin-_offset <= len(_ls)]
            # [0 <= _sz4null <= len(_ls)]
        sf._ls = [*iterable]
            # [_ls[:_begin-_offset] == [None]*(_begin-_offset)]
            # [_ls[:_begin-_offset] == [None]*_sz4null]
        sf._sz4null = 0
            # [_sz4null == _begin-_offset]
    def validate(sf, /):
        _offset = sf._offset
        _ls = sf._ls
        _neg_ok = sf._neg_ok
        _begin = sf._begin
        _sz4null = sf._sz4null
        assert _offset >= 0 or _neg_ok
        assert _sz4null == _begin-_offset
        assert 0 <= _sz4null <= len(_ls)
        assert _ls[:_sz4null] == [None]*_sz4null

    def __len__(sf, /):
        return len(sf._ls) -sf._sz4null
    @property
    def negative_offset_ok(sf, /):
        return sf._neg_ok
    @property
    def begin(sf, /):
        return sf._begin
    @property
    def end(sf, /):
        return sf._offset + len(sf._ls)
        return sf.begin + len(sf)
    @property
    def rng(sf, /):
        #rng9j
        begin = sf.begin
        end = sf.end
        return (begin, end)
        return (begin, begin + len(sf))
    _rng9j = rng
    @property
    def _rng9k(sf, /):
        #rng9k
        #bug:return (0, len(sf))
        return (0, len(sf._ls))
    def _get_rng__jk_(sf, /, *, j_vs_k):
        if not j_vs_k:
            rng9j = sf._rng9j
            return rng9j
        else:
            rng9k = sf._rng9k
            return rng9k
    @property
    def idx_range(sf, /):
        begin, end = sf.rng
        return range(begin, end)

    def explain_idx_(sf, i, /, *, strict):
        'strict -1|0|1|2'
        j = sf._explain_idx__j5i_(i, strict=strict)
        return j
    def _explain_idx__j5i_(sf, i, /, *, strict):
        'strict -1|0|1|2'
        j = sf._explain_idx__jk5i_(i, strict=strict, j_vs_k=False)
        return j
    def _explain_idx__k5i_(sf, i, /, *, strict):
        'strict -1|0|1|2'
        k = sf._explain_idx__jk5i_(i, strict=strict, j_vs_k=True)
        return k
    def _explain_idx__jk5i_(sf, i, /, *, strict, j_vs_k:bool):
        'strict -1|0|1|2'
        check_type_is(bool, j_vs_k)
        check_type_is(int, i)
        check_int_ge_le(-1, 2, strict)
        if not sf.negative_offset_ok and i < 0:
            # [MUST[offset >= 0]][[i<0]->[wrap]][i<0]
            j = i +sf.end
            #if j < 0: raise IndexError(i)
        else:
            # [MAYBE[offset < 0]][[i<0]->[nowrap]]or[i>=0]
            j = i
        j
        if j_vs_k is True or strict > 0:
            k = j -sf._offset
        ######################
        if strict == 0:
            pass
        elif strict == -1:
            if not sf.negative_offset_ok and j < 0: raise IndexError(i)
        elif strict == 1:
            #if not sf.begin <= j < sf.end: raise IndexError(i)
            if not sf._sz4null <= k < len(sf._ls): raise IndexError(i)
        elif strict == 2:
            #if not sf.begin <= j <= sf.end: raise IndexError(i)
            if not sf._sz4null <= k <= len(sf._ls): raise IndexError(i)
        else:
            raise 000
        if j_vs_k is True:
            return k
        return j
    #explain_idx_ = _explain_idx__j5i_

    def _prune_via_fill_(sf, sz4del, /):
        assert 1 <= sz4del < len(sf)
            # [_offset used as modified_detector] ==>> [min update _offset] ==>> [sz4del =!= 0]
        old__sz4null = sf._sz4null
        new__sz4null = old__sz4null + sz4del
        sf._ls[old__sz4null:new__sz4null] = [None]*sz4del

        sf._begin += sz4del
        sf._sz4null = new__sz4null
    def _prune_via_shift_(sf, sz4del, /):
        #vs:_drop_nulls_
        #vs:_prune_via_shift_
        assert 1 <= sz4del < len(sf)
            # [_offset used as modified_detector] ==>> [min update _offset] ==>> [sz4del =!= 0]
        sz4nulls_del = sf._sz4null + sz4del
        del sf._ls[:sz4nulls_del]
        sf._offset += sz4nulls_del
        sf._begin = sf._offset
        sf._sz4null = 0
    def _prune_all_(sf, new_end, /):
        #vs:clear
        #vs:_prune_all_
        assert new_end >= sf.end
        if new_end == sf._offset:
            return
        # [new_end =!= _offset]
            # [_offset used as modified_detector] ==>> [min update _offset] ==>> [new_end =!= _offset]
        sf._ls.clear()
        sf._offset = new_end
        sf._begin = new_end
        sf._sz4null = 0
    def prune_lt_(sf, i, /, *, beyond_end_ok=False):
        #vs:__delitem__
        #vs:prune_lt_
        j = sf.explain_idx_(i, strict=-1)
        if j <= sf.begin:
            return
        if j >= sf.end:
            if not (beyond_end_ok or j==sf.end): raise IndexError(i)
            sf._prune_all_(j)
            return
        old__sz = len(sf)
        sz4del = j -sf.begin
        new__sz = old__sz -sz4del
        new__sz4null = sf._sz4null+sz4del

        assert 1 <= sz4del < len(sf)
            # [_offset used as modified_detector] ==>> [min update _offset] ==>> [sz4del =!= 0]

        #if new__sz4null > new__sz and new__sz4null >= (new__sz<<1):
        if new__sz4null >= new__sz:
            sf._prune_via_shift_(sz4del)
            return
        sf._prune_via_fill_(sz4del)
        return
    def __iter__(sf, /):
        ls = sf._ls
        offset = sf._offset
            # modified_detector
        k = sf._sz4null
            #why not use 『i := sf.begin』directly?
            #   since: _offset may be huge!!!
        while 1:
            if not offset is sf._offset:
                if 0:
                    i = offset +k
                    offset = sf._offset
                    k = i -offset; i = None
                else:
                    k += offset -sf._offset
                    offset = sf._offset
                #if k < 0:raise Error__iter_after_prune_too_much
            if k < sf._sz4null:raise Error__iter_after_prune_too_much
                # 『<』 <<== maybe via .prune_lt_()
            if not k < len(ls):
                # 『>=』 <<== maybe via .pop()
                break
            yield ls[k]
            k += 1
        return
    def __reversed__(sf, /):
        ls = sf._ls
        offset = sf._offset
            # modified_detector
        k = len(ls)-1
        while 1:
            if not offset is sf._offset:
                k += offset -sf._offset
                offset = sf._offset
            if not k < len(ls):raise Error__iter_after_pop_too_much
                # 『>=』 <<== maybe via .pop()
            if k < sf._sz4null:
                # 『<』 <<== maybe via .prune_lt_()
                break
            yield ls[k]
            k -= 1
        return
    def _convert_slice__jk5i_(sf, sl9i, /, *, j_vs_k, to_adjust_slice, strict4slice):
        rng9j = sf.rng
        if to_adjust_slice:
            #ls = sf._ls
            rng9jk = sf._get_rng__jk_(j_vs_k=j_vs_k)

        sl9i = adjust_slice_(rng9j, sl9i, easy_vs_hard=False, fix_None_only=True)
        jk8start = sf._explain_idx__jk5i_(sl9i.start, j_vs_k=j_vs_k, strict=strict4slice)
        jk8stop = sf._explain_idx__jk5i_(sl9i.stop, j_vs_k=j_vs_k, strict=strict4slice)
        step = sl9i.step
        sl9jk = slice(jk8start, jk8stop, step)
        #if 0b0001:print_err(on_slice_, x, sl9i, sl9jk)
        if to_adjust_slice:
            sl9jk = adjust_slice_(rng9jk, sl9jk, easy_vs_hard=False, fix_None_only=False)
            assert step == sl9jk.step
            #if 0b0001:print_err(on_slice_, x, sl9i, sl9jk, rng9jk)
            #if 0b0001:print_err(sf._dump4debug_())
        return sl9jk
    def _explain_xidx__jk5i_(sf, x, /, *, on_int_, on_slice_, on_tuple_, j_vs_k, strict4idx, strict4slice, to_adjust_slice, easy_vs_hard):
        if 1:
            #取消tuple: 或许: 应该『sf[a,b:c]==[sf[a],*sf[b:c]]』
            #   see:__getitem__
            if type(x) is tuple:raise TypeError
        #if 0b0001:print_err(x)

        def f(x, /):
            if type(x) is int:
                i = x
                jk = sf._explain_idx__jk5i_(i, j_vs_k=j_vs_k, strict=strict4idx)
                return on_int_(jk)
            elif type(x) is slice:
                sl9i = x
                sl9jk = sf._convert_slice__jk5i_(sl9i, j_vs_k=j_vs_k, to_adjust_slice=to_adjust_slice, strict4slice=strict4slice)
                return on_slice_(sl9jk)
            elif type(x) is tuple:
                xs = x
                return on_tuple_(tuple(map(f, xs)))
            raise TypeError(type(x))
        return f(x)

    def __getitem__(sf, x, /):
        #取消tuple: 或许: 应该『sf[a,b:c]==[sf[a],*sf[b:c]]』
        #   see:_explain_xidx__jk5i_
        #
        get = sf._ls.__getitem__
        y = sf._explain_xidx__jk5i_(x, on_slice_=get, on_int_=get, on_tuple_=echo and None, j_vs_k=True, strict4idx=1, strict4slice=0, to_adjust_slice=True, easy_vs_hard=False)
            #... ???type(sf)(subseq)???
        return y
    def _del_tail_at_(sf, new_end9k, /):
        #vs:pop
        #vs:_del_tail_at_
        end9k = len(sf._ls)
        sz4null = sf._sz4null
        assert sz4null <= new_end9k < end9k
        new__sz = new_end9k -sz4null
        if new__sz == 0:
            sf.clear()
        else:
            del sf._ls[new_end9k:]
        sf._drop_nulls_(force=False)
    def _drop_nulls_(sf, /, *, force):
        #vs:_prune_via_shift_
        #vs:_drop_nulls_
        sz4null = sf._sz4null
        if sz4null:
            if force or sz4null >= len(sf):
                del sf._ls[:sz4null]
                sf._sz4null = 0
                sf._offset = sf._begin
    def clear(sf, /):
        #vs:_prune_all_
        #vs:clear
        ls = sf._ls
        if ls:
            ls.clear()
            sf._drop_nulls_(force=True)
                # [force:=True] to avoid call『len(sf)』since broken
    def __delitem__(sf, x, /):
        'not support 『del sf[:i]』to avoid misuse, use 『sf.prune_lt_(i)』instead'
        #vs:prune_lt_
        #vs:__delitem__
        if type(x) is tuple:
            raise TypeError(type(x))
        def on_slice_(sl, /):
            end9k = len(sf._ls)
            start = sl.start
            stop = sl.stop
            step = sl.step
            if step > 0:
                if start >= stop:
                    return
                if not stop==end9k: raise IndexError(x)
                new_end9k = start
            elif step < 0:
                if start <= stop:
                    return
                if not start+1==end9k: raise IndexError(x)
                new_end9k = stop+1
            else:
                raise 000
            if not abs(step) == 1: raise IndexError(x)
            new_end9k
            #if 0b0001:assert 0, new_end9k
            sf._del_tail_at_(new_end9k)
        def on_int_(k, /):
            end9k = len(sf._ls)
            if not k+1 == end9k: raise IndexError(x)
            new_end9k = k
            sf._del_tail_at_(new_end9k)
        sf._explain_xidx__jk5i_(x, on_slice_=on_slice_, on_int_=on_int_, on_tuple_=None, j_vs_k=True, strict4idx=1, strict4slice=0, to_adjust_slice=True, easy_vs_hard=False)
        return
    def __setitem__(sf, i, v, /):
        check_type_is(int, i)
        k = sf._explain_idx__k5i_(i, strict=1)
        sf._ls[k] = v
    def __iadd__(sf, ot, /):
        sf.extend(ot)
        return sf
    def __add__(sf, ot, /):
        sf = sf.copy()
        sf += ot
        return sf
    def __mul__(sf, n, /):
        check_type_is(int, n)
        if n <= 0:
            return type(sf)(sf._offset, '', negative_offset_ok=sf.negative_offset_ok)
        sf = sf.copy()
        sf *= n
        return sf
    def __imul__(sf, n, /):
        check_type_is(int, n)
        if not sf:
            return sf
        if n <= 0:
            sf.clear()
            return sf
        if n == 1:
            return sf
        sf._drop_nulls_(force=True)
        sf._ls *= n
        return sf
    def extend(sf, vs, /):
        if vs is sf:
            sf *= 2
            return
        sf._ls.extend(vs)
    def insert(sf, i, v, /):
        k = sf._explain_idx__k5i_(i, strict=2)
        sf._ls.insert(k, v)
    def append(sf, v, /):
        sf._ls.append(v)
    def pop(sf, /):
        #vs:_del_tail_at_
        #vs:pop
        if not sf:
            #raise Error__pop_empty
            raise IndexError('pop empty')
        v = sf._ls.pop()
        sf._drop_nulls_(force=False)
        return v
    def __contains__(sf, v, /):
        try:
            j = sf.index(v)
                # ^ValueError
        except ValueError:
            return False
        return True
    def remove(sf, v, begin=None, end=None, /):
        '-> None|^ValueError'
        j = sf.index(v, begin, end)
            # ^ValueError
        k = j -sf._offset
        del sf._ls[k]
        sf._drop_nulls_(force=False)
    def count(sf, v, begin=None, end=None, /):
        '-> num_eqvs|^ValueError'
        ks = sf._nonlazy_useonly__iter_find__k_(v, begin, end, j_vs_k=True)
        c = 0
        for c, k in enumerate(ks, 1):
            pass
        return c

    def index(sf, v, begin=None, end=None, /):
        '-> j|^ValueError'
        js = sf._nonlazy_useonly__iter_find__k_(v, begin, end, j_vs_k=False)
        for j in js:
            return j
        raise ValueError(v)
    def _nonlazy_useonly__iter_find__k_(sf, v, begin=None, end=None, /, *, j_vs_k):
        sl9i = slice(begin, end, 1)
        sl9k = sf._convert_slice__jk5i_(sl9i, j_vs_k=True, to_adjust_slice=True, strict4slice=0)
        begin9k = sl9k.start
        end9k = sl9k.stop
        ls = sf._ls
        if j_vs_k:
            jk5k_ = echo
        else:
            offset = sf._offset
            jk5k_ = offset.__add__
        for k in range(begin9k, end9k):
            try:
                b = ls[k] == v
            except Exception:
                pass
            else:
                if b:
                    jk = jk5k_(k)
                    yield jk
        return
    def _copy4debug_(sf, /):
        ot = type(sf)(sf._offset, sf._ls, negative_offset_ok=sf.negative_offset_ok)
        ot._begin = sf._begin
        ot._sz4null = sf._sz4null
        return ot
    def copy(sf, /):
        #vs:_copy4debug_
        #vs:copy
        sf._drop_nulls_(force=True)
        return type(sf)(sf._offset, sf._ls, negative_offset_ok=sf.negative_offset_ok)
    def reverse(sf, /):
        sf._drop_nulls_(force=True)
        sf._ls.reverse()
    def sort(sf, /, **kwds):
        sf._drop_nulls_(force=True)
        sf._ls.sort(**kwds)

    def _dump4debug_(sf, /):
        #vs:__repr__
        #vs:_dump4debug_
        #diff from: __repr__:
        #   no:『sf._drop_nulls_(force=True)』
        #
        return repr_helper__str('<PruneableArray._dump4debug_>', sf._offset, sf._ls, negative_offset_ok=sf._neg_ok, _sz4null=sf._sz4null, _begin=sf._begin)
    def __repr__(sf, /):
        #vs:_dump4debug_
        #vs:__repr__
        sf._drop_nulls_(force=True)
        args = (sf._offset, sf._ls)
        kwds = {}
        if sf.negative_offset_ok:
            kwds = dict(negative_offset_ok=True)
        else:
            kwds = {}
        return repr_helper(sf, *args, **kwds)

    def _cmp_(sf, ot, op4sign, op4ls, /):
        if not type(ot) is __class__:
            return NotImplemented
        sign = sign_of(sf._begin -ot._begin)
        if not sign == 0:
            return op4sign(sign)
        return op4ls(sf._ls, ot._ls)

    def __eq__(sf, ot, /):
        op4sign = lambda s: False
        op4ls = list.__eq__
        return sf._cmp_(ot, op4sign, op4ls)
    def __ne__(sf, ot, /):
        op4sign = lambda s: True
        op4ls = list.__ne__
        return sf._cmp_(ot, op4sign, op4ls)
    #assume null after end is -inf
    #assume null before begin is +inf
    def __lt__(sf, ot, /):
        op4sign = lambda s: s < 0
        op4ls = list.__lt__
        return sf._cmp_(ot, op4sign, op4ls)
    def __le__(sf, ot, /):
        op4sign = lambda s: s < 0
        op4ls = list.__le__
        return sf._cmp_(ot, op4sign, op4ls)
    def __gt__(sf, ot, /):
        op4sign = lambda s: s > 0
        op4ls = list.__gt__
        return sf._cmp_(ot, op4sign, op4ls)
    def __ge__(sf, ot, /):
        op4sign = lambda s: s > 0
        op4ls = list.__ge__
        return sf._cmp_(ot, op4sign, op4ls)

    ######################
    negative_offset_ok
    begin
    end
    rng
    _rng9j
    _rng9k
    idx_range
    validate
    explain_idx_
    ######################
    prune_lt_
    ######################
    __eq__
    __ne__
    __ge__
    __gt__
    __le__
    __lt__

    __iter__
    __reversed__

    __len__

    __getitem__
    __setitem__
    __delitem__
    clear
    pop
    append
    extend
    insert
    remove

    __add__
    __iadd__
    __imul__
    __mul__
    #__rmul__

    __repr__
    #__str__
    #__reduce__
    #__reduce_ex__


    __contains__
    count
    index

    copy
    reverse
    sort

#end-class PruneableArray:

class Error(Exception):pass
class Error__iter(Exception):pass
class Error__iter_after_prune_too_much(Error__iter):pass
class Error__iter_after_pop_too_much(Error__iter):pass
#class Error__pop_empty(Exception):pass



__all__


from seed.types.PruneableArray import PruneableArray
    #def prune_lt_(sf, i, /, *, beyond_end_ok=False):

from seed.types.PruneableArray import Error, Error__iter, Error__iter_after_prune_too_much, Error__iter_after_pop_too_much
from seed.types.PruneableArray import adjust_slice_, adjust_until_le_, adjust_until_ge_

from seed.types.PruneableArray import *
