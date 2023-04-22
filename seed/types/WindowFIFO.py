#__all__:goto
r'''[[[
e ../../python3_src/seed/types/WindowFIFO.py
see:
    from collections import deque
    view ../../python3_src/seed/types/Deque.py
    view ../../python3_src/seed/iters/PeekableIterator.py
    view ../../python3_src/seed/types/WindowFIFO.py


WindowQueueRILRO:
    '!!!init:O(1) without putL!!!'
WindowDeque:
    '!!!init:O(W) with putL!!!'

NOTE:
    copy,__repr__,_debug_repr:should update if __init__ api changes

seed.types.WindowFIFO
py -m nn_ns.app.debug_cmd   seed.types.WindowFIFO
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.types.WindowFIFO   @f
py -m nn_ns.app.doctest_cmd seed.types.WindowFIFO:__doc__ -v


from seed.types.WindowFIFO import WindowQueueRILRO, WindowDeque

from seed.types.WindowFIFO import BaseQueueError, QueueError__full, QueueError__null, QueueError__assignment__len_not_match




modify:clear,reverse,__setitem__,popL,popR,putR#may putL #__init__,to_raise_if_put_on_full
query:iter,reversed,len,bool,__getitem__
debug:_debug_repr,_2idx_rng,_iter_idx_rngs
>>> from seed.types.WindowFIFO import WindowQueueRILRO, WindowDeque

>>> from seed.types.WindowFIFO import BaseQueueError, QueueError__full, QueueError__null, QueueError__assignment__len_not_match

>>> q = WindowQueueRILRO(None)
>>> q
WindowQueueRILRO(None)
>>> bool(q)
False
>>> len(q)
0
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 0, _j = 0, _ls = [], _mw = None, _rfpf = False)>]'
>>> q.putR(111)
>>> q
WindowQueueRILRO(None, [111])
>>> bool(q)
True
>>> len(q)
1
>>> q.extendR([222,333,444,555,666,777,888,999])
>>> bool(q)
True
>>> len(q)
9
>>> q.popsL_(6)
[111, 222, 333, 444, 555, 666]
>>> q
WindowQueueRILRO(None, [777, 888, 999])
>>> bool(q)
True
>>> len(q)
3
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 6, _j = 9, _ls = [None, None, None, None, None, None, 777, 888, 999], _mw = None, _rfpf = False)>]'
>>> q.popL() #_post_pop:_std_shift() #[3N_ge_L]
777
>>> q
WindowQueueRILRO(None, [888, 999])
>>> bool(q)
True
>>> len(q)
2
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 0, _j = 2, _ls = [888, 999], _mw = None, _rfpf = False)>]'
>>> q.popR() #_post_pop:(remove tail None) #[no_dummy_tail]
999
>>> q
WindowQueueRILRO(None, [888])
>>> bool(q)
True
>>> len(q)
1
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 0, _j = 1, _ls = [888], _mw = None, _rfpf = False)>]'
>>> q.popL() #_post_pop:clear() #[no_dummy__if__i_eq_j]
888
>>> q
WindowQueueRILRO(None)
>>> bool(q)
False
>>> len(q)
0
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 0, _j = 0, _ls = [], _mw = None, _rfpf = False)>]'


>>> q = WindowQueueRILRO(6, [111, 222, 333, 444, 555, 666, 777, 888, 999])
>>> q
WindowQueueRILRO(6, [444, 555, 666, 777, 888, 999])
>>> bool(q)
True
>>> len(q)
6
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 3, _j = 3, _ls = [777, 888, 999, 444, 555, 666], _mw = 6, _rfpf = False)>]'
>>> q[0]
444
>>> q[-1]
999
>>> q[2]
666
>>> q[3]
777
>>> q[2:4]
[666, 777]
>>> q.popsR_(2)
[888, 999]
>>> q
WindowQueueRILRO(6, [444, 555, 666, 777])
>>> bool(q)
True
>>> len(q)
4
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 3, _j = 1, _ls = [777, None, None, 444, 555, 666], _mw = 6, _rfpf = False)>]'
>>> q.popR()
777
>>> q
WindowQueueRILRO(6, [444, 555, 666])
>>> bool(q)
True
>>> len(q)
3
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 3, _j = 6, _ls = [None, None, None, 444, 555, 666], _mw = 6, _rfpf = False)>]'
>>> q.popL()
444
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 4, _j = 6, _ls = [None, None, None, None, 555, 666], _mw = 6, _rfpf = False)>]'




>>> q = WindowQueueRILRO(6, [111, 222, 333, 444, 555, 666, 777, 888, 999])
>>> q.popsL_(2)
[444, 555]
>>> q
WindowQueueRILRO(6, [666, 777, 888, 999])
>>> bool(q)
True
>>> len(q)
4
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 5, _j = 3, _ls = [777, 888, 999, None, None, 666], _mw = 6, _rfpf = False)>]'
>>> q[0]
666
>>> q[-1]
999
>>> q[1]
777
>>> q[:2]
[666, 777]
>>> q.popL()
666
>>> q
WindowQueueRILRO(6, [777, 888, 999])
>>> bool(q)
True
>>> len(q)
3
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 0, _j = 3, _ls = [777, 888, 999], _mw = 6, _rfpf = False)>]'
>>> q.popR()
999
>>> q.popR()
888
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 0, _j = 1, _ls = [777], _mw = 6, _rfpf = False)>]'
>>> q.popR()
777
>>> q._debug_repr()
'[<WindowQueueRILRO(_i = 0, _j = 0, _ls = [], _mw = 6, _rfpf = False)>]'



#]]]'''
__all__ = r'''
WindowQueueRILRO
WindowDeque

BaseQueueError
    QueueError__full
    QueueError__null
    QueueError__assignment__len_not_match
'''.split()#'''
__all__

def _():
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper

from seed.tiny_.check import check_uint
from seed.helper.repr_input import repr_helper
from itertools import repeat
    #repeat(elem [,n]) --> elem, elem, elem, ... endlessly or up to n times

class BaseQueueError(Exception):pass
class QueueError__full(BaseQueueError):pass
class QueueError__null(BaseQueueError):pass
class QueueError__assignment__len_not_match(BaseQueueError):pass
class _WindowXXX:
    __slots__ = ()
    #def __init__(sf, may_len_window, iterable=None, /, *, reverse=False, to_raise_if_put_on_full=False):
    #def __init__(sf, len_window, iterable=None, /, *, reverse=False, to_raise_if_put_on_full=False):
    #may_len_window vs len_window
    def __repr__(sf, /):
        mw = sf.get_may_len_window()
        ls = [*sf]
        args = (ls,) if ls else ()
        kwds = dict(to_raise_if_put_on_full=True) if sf.to_raise_if_put_on_full else {}
        return repr_helper(sf, mw, *args, **kwds)
    def _debug_repr(sf, /):
        nms = type(sf).__slots__
        kwds = {nm:getattr(sf,nm) for nm in nms}
        s = repr_helper(sf, **kwds)
        return f'[<{s!s}>]'
    def copy(sf, /):
        cls = type(sf)
        return cls(sf.get_may_len_window(), sf, to_raise_if_put_on_full=sf.to_raise_if_put_on_full)
    @property
    def to_raise_if_put_on_full(sf, /):
        return sf._rfpf
    @to_raise_if_put_on_full.setter
    def to_raise_if_put_on_full(sf, to_raise_if_put_on_full, /):
        sf._rfpf = bool(to_raise_if_put_on_full)

    def get_may_len_window(sf, /):
        return (sf._mw)
    def is_null(sf, /):
        return not sf
    def is_full(sf, /):
        # [def__is_full]:goto
        return None is not sf.get_may_len_window()==len(sf)
    def iter_(sf, /, *, reverse):
        (i,j) = sf._2idx_rng()
        idc = range(i,j)
        if reverse:
            idc = reversed(idc)
        return map(sf._ls.__getitem__, idc)
    def __iter__(sf, /):
        return sf.iter_(reverse=False)
    def __reversed__(sf, /):
        return sf.iter_(reverse=True)

    def __getitem__(sf, k, /):
        (i,j) = sf._2idx_rng()
        x = range(i,j)[k]
        if type(k) is slice:
            idc = x
            return [*map(sf._ls.__getitem__, idc)]
        else:
            idx = x
            return sf._ls[idx]
    def __setitem__(sf, k, v, /):
        (i,j) = sf._2idx_rng()
        x = range(i,j)[k]
        if type(k) is slice:
            idc = x
            vs = iter(v); del v,x
            vs = [*vs]
            if not len(vs) == len(idc): raise QueueError__assignment__len_not_match
            for _ in map(sf._ls.__setitem__, idc, vs):pass
        else:
            idx = x
            sf._ls[idx] = v

    def putR(sf, v, /):
        if sf.is_full() and not sf.to_raise_if_put_on_full:
            sf.popL()
        sf._putR(v)
    def extendR(sf, vs, /):
        for _ in map(sf.putR, vs):pass
    def popsR_(sf, n, /):
        it = range(n)#check
        if len(sf) < n:raise QueueError__null
        vs = [sf.popR() for _ in it]
        vs.reverse()
        return vs
    def popsL_(sf, n, /):
        it = range(n)#check
        if len(sf) < n:raise QueueError__null
        vs = [sf.popL() for _ in it]
        #vs.reverse()
        return vs

    #__iadd__ = extend
    def __iadd__(sf, vs, /):
        sf.extendR(vs)
        return sf
    if 1:
        extend = extendR
        #append = putR
        def append(sf, v, /):
            sf.putR(v)
        #pop = popR
        #pop_left = popL
        def pop(sf, /):
            return sf.popR()
        def pop_left(sf, /):
            return sf.popL()
    r'''
    def __imul__(sf, n, /):
    def __eq__(sf, ot, /):
    def count(sf, v, /, begin, end):
    def indexL(sf, v, /, begin, end):
    def indexR(sf, v, /, begin, end):
    def findL(sf, v, /, begin, end):
    def findR(sf, v, /, begin, end):
    index
    find
. .TODO
    #'''
#class WindowFIFO(_WindowXXX):
class WindowQueueRILRO(_WindowXXX):
    r'''!!!init:O(1) without putL!!!
    #right-side-in-left-right-side-out
    #  vs: FILO,FIFO:first-in-last/first-out
    #

    N = len(sf)
    L = len(sf._ls)
    W = len_window | inf
    i = sf._i
    j = sf._j

    [[[约束:
    #除了_post_pop()，因为它就是用来规范数据以符合约束的
    #

    # j,i,0,L的关系:
    [0 <= i <= L]
    [[i==L] -> [j==i==0==L]]

    [0 <= j <= L]
    [[j==0] -> [j==i==0==L]]

    [[L==0] -> [j==i==0==L]]
        {j,i,0,L}两两相等
        上面出现3种等价退化情形:[L==0], [j==0], [i==L]
        [choose_(4;2)==4*3/2==6]
        只剩3种正常情况:[i==0], [j==L], [j==i]
    [[j==i==0==L]xor[[L>0][0 <= i < L][0 < j <= L]]]

    [[no_dummy_tail] =[def]= [[i<j] -> [j==L]]]
        #preserved by _post_pop(),reverse()
    [[j==i==0==L]or[0 <= i < j == L]or[[0 < j <= i < L]]]
    [[i<j] -> [j==L]]
    case (i,j):
        * [[0 <= i < j == L] -> [N==j-i>0]]
        * [[0 < j <= i < L] -> [N==j+(L-i)>0]]
        * [[j==i==0==L] -> [N==0]]
    [[L==0] <-> [j==i==0==L] <-> [N==0]]
    [[L==0] <-> [N==0]]
        # [def____bool__]



    bug: [[j==i] -> [j==i==0==L]]
        # [L>0] is fine, using whole sf._ls, i.e. [N==L]
    bug: [[j==i] -> [is_full sf]]
        # [N==L] but not is_full # [N==W]

    [[j==i] <-> [[j==i==0==L]or[0<j==i<L]]]

    bug: [[j==i] <-> [N==L]]
    [[N==L] <-> [[j==i==0==L]or[0<j==i<L]or[0==i<j==L]]]
    [[N==L] <-> [[j==i]or[0==i<j==L]]]

    [[no_dummy__if__i_eq_j] =[def]= [[j==i] -> [N==L]]]
        # pop may (dec j)/(inc i) to mk [i==j]
        # preserved by _post_pop():sf.clear()
    [[j==i] -> [N==L]]
    [may_dummy_range =[def]= if [0<i<j] then (0,i) elif [j<i] then (j,i) else None]
        !! [[i<j] -> [j==L]]


    [[is_full sf] =[def]= [N==W]]
        # [def__is_full]
    [N==W]:
        !! [N <= L <= W]
        [N==L]
        !! [[N==L] <-> [[j==i==0==L]or[0<j==i<L]or[0==i<j==L]]]
        [[j==i==0==L]or[0<j==i<L]or[0==i<j==L]]
    [[is_full sf] -> [[N==L==W][[j==i==0==L]or[0<j==i<L]or[0==i<j==L]]]]
    bug: [[is_full sf] -> [j==i]]




    # W,N,L的关系:
    [0 <= N <= L <= W]
    # [[L==0] <-> [N==0]]
        # [def____bool__]:goto

    [[3N_ge_L] =[def]= [L/3 <= N <= L]]
        #required by reverse() to achieve O(N)
        #preserved by _post_pop():_std_shift()
    [0 <= L/3 <= N <= L <= W]

    [N <- {j-i,j-i+L}]
        !! [[j==i] -> [j==i==0==L]]
        !! [0 <= N <= L]
        ==>> [上面两解要么相等，要么只有一个符合约束]
    bug: [N == (j-i)%L]
        [is_full sf]:
            * [L==0] ==>> [div 0 err]
            * [0==i<j==L] ==>> [rhs==0][lhs==L]
            * [0<j==i<L] ==>> [rhs==0][lhs==L]

    bug: [N == (j-i) if i <= j else (j-i+L)]
    [N == (j-i) if i < j else (j-i+L)]
        # [def__len]
        [j==i]:
            [N==j-i+L==L]
            * [j==i==0==L]
            * [0<j==i<L]
    ]]]
    '''#'''
    __slots__ = '_mw _rfpf _ls _i _j'.split()
    def __init__(sf, may_len_window, iterable=None, /, *, reverse=False, to_raise_if_put_on_full=False):
        if not may_len_window is None:
            len_window = may_len_window
            check_uint(len_window)
        if not iterable is None:
            iterable = iter(iterable)
        reverse = bool(reverse)
        to_raise_if_put_on_full = bool(to_raise_if_put_on_full)

        sf._mw = may_len_window
        #sf._rfpf = to_raise_if_put_on_full
        sf.to_raise_if_put_on_full = to_raise_if_put_on_full
        sf._ls = []
            #O(1)
            # max len(ls) == len_window
            # [bool(sf) == bool(sf._ls)] #clear when is_empty
        sf._j = 0
        sf._i = 0
            # begin = sf._i
            # end = sf._j
            # [begin==end] ==>> [is_empty][len(sf._ls)==0]or[is_full][len(sf._ls)==len_window]
            # [begin>end] ==>> [len(sf._ls)==len_window]
        if not iterable is None:
            sf.extendR(iterable)
        if reverse:
            sf.reverse()
    def reverse(sf, /):
        'O(len(sf))'
        #O(N)
        L = len(sf._ls)
        i, j = sf._i, sf._j
        i = L-i
        j = L-j
        i,j = j,i
        sf._ls.reverse()
            #O(L)
            #!! [L/3 <= N <= L] #see:_post_pop():_std_shift():[3N_ge_L]
            #==>>O(N)
        sf._i, sf._j = i, j

        # see:[may_dummy_range =[def]= if [0<i<j] then (0,i) elif [j<i] then (j,i) else None]
        #not: if i <= j:
        if i < j:
            assert i==0
            del sf._ls[j:]
            # [no_dummy_tail]:goto
        return
        sf._std_shift()
            #O(N)
        sf._ls.reverse()
            #O(N)
        return
        sf._ls = reversed(sf)
            #O(N)
        sf._i = 0
        sf._j = len(sf._ls)
        return
    def __len__(sf, /):
        # [def__len]:goto
        sz = (sf._j-sf._i)
        if not sz > 0:
            # [begin==end] ==>> [is_empty][len(sf._ls)==0]or[is_full][len(sf._ls)==len_window]
            # [begin>end] ==>> [len(sf._ls)==len_window]
            #xxx  sz += sf._w
            sz += len(sf._ls)
        assert sz >= 0
        return sz
    def __bool__(sf, /):
        # [def____bool__]:goto
        return bool(sf._ls)
        return bool(len(sf))
    def _iter_idx_rngs(sf, /):
        if not sf: return
        i = sf._i
        j = sf._j
        if not i < j:
            #yield (i, sf._w)
            yield (i, len(sf._ls))
            yield (0, j)
        else:
            yield (i, j)
    def _2idx_rng(sf, /):
        if not sf:
            return (0,0)
        i = sf._i
        j = sf._j
        if not i < j:
            #i -= sf._w
            i -= len(sf._ls)
        return (i,j)
        return range(i,j)
    def clear(sf, /):
        sf._ls.clear()
        sf._i = 0
        sf._j = 0
        return
    #xxx def putL(sf, v, /):
    #   ==>> O(N) to fill whole window
    #       popL/popR are ok
    def _putR(sf, v, /):
        if sf.is_full():raise QueueError__full
        j = sf._j
        if j == len(sf._ls):
            if j == sf._mw:
                j = 0
            else:
                sf._ls.append(None)
        else:
            pass
        assert not j == len(sf._ls)
        sf._ls[j] = v
        sf._j = j+1
    def _std_shift(sf, /):
        if not (sf._i == 0 and sf._j == len(sf._ls)):
            ls = [*sf]
            sf._ls = ls
            sf._i = 0
            sf._j = len(ls)
        assert sf._i == 0 and sf._j == len(sf._ls)
    def _post_pop(sf, /):
        i = sf._i
        j = sf._j
        if i == j:
            # after pop ==>> [0==N<L]
            # [no_dummy__if__i_eq_j] requires [L==N]
            # [[j==i] -> [N==L]]
            sf.clear()
            # [L==N==0]
        elif len(sf)*3 < len(sf._ls):
            # [0 <= N < L/3]
            sf._std_shift()
            # [3N_ge_L]
            # [L/3 <= N == L]
        elif i < j < len(sf._ls):
            del sf._ls[j:]
                #more than 1 when after popL, i become 0
            # [no_dummy_tail]:goto
        # [L/3 <= N <= L]
        assert not len(sf)*3 < len(sf._ls)
    def popL(sf, /):
        if not sf:raise QueueError__null
        i = sf._i
        v = sf._ls[i]
        sf._ls[i] = None
        #bug:sf._i = (i+1)%len(sf._ls)
        #   i = L-1 --> L --> 0
        #   j = L
        #   should be (L:L) now be (0:L)
        i += 1
        if sf._j < i == len(sf._ls):
            i = 0
        sf._i = i
        sf._post_pop()
        return v
    def popR(sf, /):
        if not sf:raise QueueError__null
        j = sf._j

        #bug:assert sf._ls[j] is None
        # * need: len(sf._ls)==len_window
        # * need: j := j%sf._w1
        #j -= 1 # may be j == -1

        #j = (j-1)%len(sf._ls)
        if j == 0:
            j = len(sf._ls)
        j -= 1
        v = sf._ls[j]
        sf._ls[j] = None

        if 0 == j < sf._i:
            j = len(sf._ls)
        sf._j = j
        sf._post_pop()
        return v


#class WindowQueue(_WindowXXX):
#class WindowQueueLRILRO(_WindowXXX):
class WindowDeque(_WindowXXX):
    '!!!init:O(W) with putL!!!'
    #double-end-queue
    #from collections import deque
    __slots__ = '_rfpf _ls _sz _i'.split()
    def __init__(sf, len_window, iterable=None, /, *, reverse=False, to_raise_if_put_on_full=False):
        check_uint(len_window)
        if not iterable is None:
            iterable = iter(iterable)
        reverse = bool(reverse)
        to_raise_if_put_on_full = bool(to_raise_if_put_on_full)

        #sf._mw = may_len_window
        #sf._w = len_window
        #sf._rfpf = to_raise_if_put_on_full
        sf.to_raise_if_put_on_full = to_raise_if_put_on_full

        sf._ls = [None]*(len_window+1)
            #O(W)

        sf._sz = 0
        #sf._j = 0
        sf._i = 0
            # begin = sf._i
            # end = (sf._i+sf._sz)%sf._w
        if not iterable is None:
            sf.extendR(iterable)
        if reverse:
            sf.reverse()
    def reverse(sf, /):
        'O(len(sf))'
        #O(N)
        L = len(sf._ls)
        if len(sf)*2 < L:
            #[0 <= N < W/2]
            #O(N)
            ls = [*reversed(sf)]
            sf.clear()
            sf.extendR(ls)
        else:
            #[W/2 <= N <= W]
            #O(W)==>>O(N)
            j = (sf._i+sf._sz)%sf._w1
            j = L-j
            i = j
            sf._ls.reverse()
                #O(W)
            sf._i = i
    def __len__(sf, /):
        return (sf._sz)
    def __bool__(sf, /):
        return bool(len(sf))
    def get_len_window(sf, /):
        return (sf._w)
    @property
    def _w(sf, /):
        return len(sf._ls)-1
    _mw = _w #for get_may_len_window
    @property
    def _w1(sf, /):
        return len(sf._ls)
    if 0:
        @property
        def _begin(sf, /):
            return (sf._i)
    @property
    def _end(sf, /):
        end = (sf._i+sf._sz)%sf._w1
        return end
    def _iter_idx_rngs(sf, /):
        if not sf: return
        i = sf._i
        j = i+len(sf)
        w1 = sf._w1
        if w1 < j:
            j -= w1
            yield (i, w1)
            yield (0, j)
        else:
            yield (i, j)
    def _2idx_rng(sf, /):
        i = sf._i
        j = i+len(sf)
        w1 = sf._w1
        if w1 < j:
            i -= w1
            j -= w1
        return (i,j)
        return range(i,j)
    def clear(sf, /):
        for (i,j) in sf._iter_idx_rngs():
            sf._ls[i:j] = repeat(None, j-i)
        sf._i = 0
        sf._sz = 0
        return
        (i,j) = sf._2idx_rng()
        idc = range(i,j)
        for k in idc:
            sf._ls[k] = None
        sf._i = 0
        sf._sz = 0
        return
    def putL(sf, v, /):
        if sf.is_full() and not sf.to_raise_if_put_on_full:
            sf.popR()
        sf._putL(v)
    def _putL(sf, v, /):
        if sf.is_full():raise QueueError__full
        i = sf._i = (sf._i-1)%sf._w1
        sf._ls[i] = v
        sf._sz += 1
    def _putR(sf, v, /):
        if sf.is_full():raise QueueError__full
        j = sf._end
        sf._ls[j] = v
        sf._sz += 1
    def popL(sf, /):
        if not sf:raise QueueError__null
        i = sf._i
        v = sf._ls[i]
        sf._ls[i] = None
        sf._i = (i+1)%sf._w1
        sf._sz -= 1
        return v
    def popR(sf, /):
        if not sf:raise QueueError__null
        j = sf._end
        assert sf._ls[j] is None
        #j -= 1 # j == -1
        j = (j-1)%sf._w1
        v = sf._ls[j]
        sf._ls[j] = None
        sf._sz -= 1
        return v
    #########
    def extendL__reversed(sf, vs, /):
        for _ in map(sf.putL, vs):pass
    if 1:
        extend_left__reversed = extendL__reversed
        #append_left = putL
        def append_left(sf, v, /):
            sf.putL(v)

from seed.types.WindowFIFO import WindowQueueRILRO, WindowDeque

from seed.types.WindowFIFO import BaseQueueError, QueueError__full, QueueError__null, QueueError__assignment__len_not_match
