#__all__:goto
r'''
not synchronized

impl:
    use list as underlying container
    instead of singly-linked-list or doubly-linked-list
    append_left/append_right:
        if full then double the size
    pop_left/pop_right:
        if not 1/4-full then half the size

stack - FILO/LIFO
queue - FIFO
deque
    double-ended queue


[[
reason:
    from collections import deque
    from seed.types.Deque import DequeII as deque
    #!!  collections.deque:not support slice:
    # dq[n:m]
    # TypeError: sequence index must be integer, not 'slice'

used in:
    seed.iters.PeekableIterator

]]

py -m seed.types.Deque
py -m nn_ns.app.debug_cmd   seed.types.Deque -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.Deque:__doc__  -ht # -ff -df

example:
>>> Deque()
Deque([])
>>> Deque([])
Deque([])
>>> Deque([1,2])
Deque([1, 2])

>>> d = Deque()
>>> len(d)
0
>>> d.append_right(1)
>>> d
Deque([1])
>>> d.append_right(2)
>>> d
Deque([1, 2])
>>> d.append_left(-1)
>>> d
Deque([-1, 1, 2])
>>> d.append_left(-2)
>>> d
Deque([-2, -1, 1, 2])
>>> d.pop_right()
2
>>> d
Deque([-2, -1, 1])
>>> d.pop_left()
-2
>>> d
Deque([-1, 1])
>>> len(d)
2
>>> d.pop_left()
-1
>>> d
Deque([1])
>>> d.pop_right()
1
>>> d
Deque([])


>>> d = Deque([1,2,3,4])
>>> len(d)
4
>>> d[1]
2
>>> d[-1]
4
>>> d[-4]
1
>>> d[4] #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
IndexError



>>> d = Deque([1,2,3,4])
>>> for k in range(-7, 9):
...     d = Deque([1,2,3,4])
...     d.rotate_right(k)
...     (k, d)
(-7, Deque([4, 1, 2, 3]))
(-6, Deque([3, 4, 1, 2]))
(-5, Deque([2, 3, 4, 1]))
(-4, Deque([1, 2, 3, 4]))
(-3, Deque([4, 1, 2, 3]))
(-2, Deque([3, 4, 1, 2]))
(-1, Deque([2, 3, 4, 1]))
(0, Deque([1, 2, 3, 4]))
(1, Deque([4, 1, 2, 3]))
(2, Deque([3, 4, 1, 2]))
(3, Deque([2, 3, 4, 1]))
(4, Deque([1, 2, 3, 4]))
(5, Deque([4, 1, 2, 3]))
(6, Deque([3, 4, 1, 2]))
(7, Deque([2, 3, 4, 1]))
(8, Deque([1, 2, 3, 4]))

>>> d = Deque([1,2,3,4])
>>> for k in range(-7, 9):
...     d.rotate_right(k)
...     (k, d)
(-7, Deque([4, 1, 2, 3]))
(-6, Deque([2, 3, 4, 1]))
(-5, Deque([3, 4, 1, 2]))
(-4, Deque([3, 4, 1, 2]))
(-3, Deque([2, 3, 4, 1]))
(-2, Deque([4, 1, 2, 3]))
(-1, Deque([1, 2, 3, 4]))
(0, Deque([1, 2, 3, 4]))
(1, Deque([4, 1, 2, 3]))
(2, Deque([2, 3, 4, 1]))
(3, Deque([3, 4, 1, 2]))
(4, Deque([3, 4, 1, 2]))
(5, Deque([2, 3, 4, 1]))
(6, Deque([4, 1, 2, 3]))
(7, Deque([1, 2, 3, 4]))
(8, Deque([1, 2, 3, 4]))




>>> d = Deque([1,2,3,4])
>>> for k in range(-7, 9):
...     d.rotate_left(k)
...     (k, d)
(-7, Deque([2, 3, 4, 1]))
(-6, Deque([4, 1, 2, 3]))
(-5, Deque([3, 4, 1, 2]))
(-4, Deque([3, 4, 1, 2]))
(-3, Deque([4, 1, 2, 3]))
(-2, Deque([2, 3, 4, 1]))
(-1, Deque([1, 2, 3, 4]))
(0, Deque([1, 2, 3, 4]))
(1, Deque([2, 3, 4, 1]))
(2, Deque([4, 1, 2, 3]))
(3, Deque([3, 4, 1, 2]))
(4, Deque([3, 4, 1, 2]))
(5, Deque([4, 1, 2, 3]))
(6, Deque([2, 3, 4, 1]))
(7, Deque([1, 2, 3, 4]))
(8, Deque([1, 2, 3, 4]))





>>> d = Deque([1,2,3,4])
>>> d[::2]
[1, 3]
>>> d[1::2]
[2, 4]
>>> d[1:3:1]
[2, 3]
>>> d[::-2]
[4, 2]
>>> d[1::-2]
[2]
>>> d[1:3:-1]
[]
>>> d[1:3:-2]
[]

>>> range(4)[::-2]
range(3, -1, -2)
>>> range(4)[::-2][::-1]
range(1, 5, 2)
>>> [*range(4)[::-2][::-1]]
[1, 3]

>>> slice(None, None, -2).indices(4)
(3, -1, -2)
>>> range(4)[3:-1:-2]  # ==>> bug__slice_X_range
range(3, 3, -2)
>>> [*range(4)[3:-1:-2]]
[]

>>> d.slice_(None,None,-2)
Deque([4, 2])
>>> d.slice8list_(None,None,-2)
[4, 2]






>>> d = Deque([1,2,3,4])
>>> d == Deque([1,2,3,4])
True
>>> [*iter(d)]
[1, 2, 3, 4]
>>> [*d.iter_slice_(None,None,-2)]
[4, 2]




##vivi:collections.deque API
    rotate
    append
    extend
    pop
    appendleft
    extendleft
    popleft
>>> d = Deque([1,2,3,4])
>>> d
Deque([1, 2, 3, 4])
>>> d.rotate()
>>> d
Deque([2, 3, 4, 1])
>>> d.appendleft(999)
>>> d
Deque([999, 2, 3, 4, 1])
>>> d.extendleft([66,77,88])  ### reversed extend!!!
>>> d
Deque([88, 77, 66, 999, 2, 3, 4, 1])
>>> d.append(666)
>>> d
Deque([88, 77, 66, 999, 2, 3, 4, 1, 666])
>>> d.extend([33,44,55])
>>> d
Deque([88, 77, 66, 999, 2, 3, 4, 1, 666, 33, 44, 55])
>>> d.popleft()
88
>>> d
Deque([77, 66, 999, 2, 3, 4, 1, 666, 33, 44, 55])
>>> d.pop()
55
>>> d
Deque([77, 66, 999, 2, 3, 4, 1, 666, 33, 44])





'''#'''

__all__ = '''
Deque
'''.split()#'''

#[mk_seq_rng__with_step__len_,mk_seq_rng__with_step__seq_] = lazy_import4funcs_('seed.seq_tools.mk_seq_rng__with_step', 'mk_seq_rng__with_step__len_,mk_seq_rng__with_step__seq_', __name__)
from seed.seq_tools.mk_seq_rng__with_step import mk_seq_rng__with_step__len_
from seed.tiny_.slice2triple import slice2triple
from seed.helper.repr_input import repr_helper
import operator # .index

class _Nothing:pass
class Deque:
    r'''
methods:
    __len__
    __getitem__ # idx only
    __repr__
    to_list

    extend_left
    extend_right
    append_left
    append_right
    pop_left
    pop_right

    clear
    xxx no:__iter__,__eq__

news:
    rotate_right
    rotate_left

    slice8list_
        slice_
        __getitem__ # ++slice{step:=1}

    iter_slice_
        __iter__
        __eq__

    ##vivi:collections.deque API
    rotate
    append
    extend
    pop
    appendleft
    extendleft
    popleft

'''#'''
    def __init__(self, iterable=None):
        # __begin == 0 or 0 < __begin < len(__ls)
        self.__ls = []
        self.__begin = 0
        self.__size = 0
        self.__ver = object()
            # timpstamp

        if iterable is not None:
            self.extend_right(iterable)
    def clear(self):
        self.__ls.clear()
        self.__begin = 0
        self.__size = 0
        self.__ver = object()
    def __len__(self):
        return self.__size
    def extend_left(self, iterable):
        for _ in map(self.append_left, iterable): pass
    def extend_right(self, iterable):
        for _ in map(self.append_right, iterable): pass

    def __getitem__(self, idx_or_slice):
        if type(idx_or_slice) is slice:
            sl = idx_or_slice
            return self.slice8list_(*slice2triple(sl))
            #bug:bug__slice_X_range:
            return self.slice8list_(*sl.indices(len(self)))
            # return __class__(...)
            raise NotImplementedError
        #elif isinstance(idx_or_slice, int):
        idx = idx_or_slice
        idx = operator.index(idx)
        sz = self.__size
        if not -sz <= idx < sz: raise IndexError('out-of-range')
        if idx < 0:
            idx += sz

        idx += self.__begin
        L = len(self.__ls)
        if idx > L:
            idx -= L
        return self.__ls[idx]

    def slice_(self, begin, end, /, step=1):
        '-> Deque # [step:=1]'
        T = type(self) #__class__
        ls = self.slice8list_(begin, end, step)
        return T(ls)
    def slice8list_(self, begin, end, /, step=1):
        '-> list # [step:=1]'
        return self.__slice_to_list(begin, end, step)
    def __iter__(self):
        return self.iter_slice_(0, len(self))
    def iter_slice_(self, begin, end, /, step=1):
        #????? what if modified while __iter__ ????
        # use to_list instead
        #   now:++timpstamp:self.__ver
        #see:__slice_to_list
        sz = len(self)
        (b_reversed, begin, end, step, length) = mk_seq_rng__with_step__len_(sz, begin, end, step)
        if not length:
            return

        timpstamp = self.__ver
        ls = self.__ls
        L = len(ls)
        idc4ls = range(L)

        offset = self.__begin
        i = offset + begin
        j = offset + end
        fst_part = idc4ls[i:j:step]
            # MAYBE:[len(ls) < i]
            # MAYBE:[len(ls) < j]
            #   => MAYBE:[len(fst_part) < length]

        snd_sz = length - len(fst_part)
        if snd_sz:
            _i = i + step*len(fst_part) - L
            _j = j - L
            snd_part = idc4ls[_i:_j:step]
            jss = [fst_part, snd_part]
        else:
            jss = [fst_part]
        assert sum(map(len, jss)) == length
        if b_reversed:
            jss = [js[::-1] for js in jss[::-1]]
        jss

        def __(jss, /):
            for js in jss:
                yield from js
        js = __(jss)

        for j in js:
            if not self.__ver is timpstamp:raise Exception('Deque modified while iter')
            yield ls[j]
        return
 
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, type(self)):
            return NotImplemented
        if not len(self) == len(other):
            return False
        return all(map(operator.eq, self, other))

    def to_list(self):
        return self.__to_list(0, len(self))
    def __slice_to_list(self, begin, end, step):
        sz = len(self)
        (b_reversed, begin, end, step, length) = mk_seq_rng__with_step__len_(sz, begin, end, step)
        if not length:
            return []
        #if length == 1: return [self[begin]]
        offset = self.__begin
        ls = self.__ls
        i = offset + begin
        j = offset + end
        fst_part = ls[i:j:step]
            # MAYBE:[len(ls) < i]
            # MAYBE:[len(ls) < j]
            #   => MAYBE:[len(fst_part) < length]

        snd_sz = length - len(fst_part)
        if snd_sz:
            _i = i + step*len(fst_part) - len(ls)
            _j = j - len(ls)
            snd_part = ls[_i:_j:step]
            r = fst_part + snd_part if fst_part else snd_part
        else:
            r = fst_part
        assert len(r) == length
        if b_reversed:
            r.reverse()
        return r
    def __to_list(self, begin, length):
        '[0 <= begin <= begin+length <= len(self)]'
        return self.__slice_to_list(begin, end:=begin+length, step:=1)
        #.ls = self.__ls
        #.i = begin + self.__begin
        #.length = length #self.__size
        #.j = i+length
        #.#xxx:if not 0 <= i <= j <= len(self):raise 000
        #.:if not 0 <= length <= len(self):raise 000
        #.fst_part = ls[i:j]
        #.    # MAYBE:[len(ls) < i]
        #.    # MAYBE:[len(ls) < j]
        #.    #   => MAYBE:[len(fst_part) < length]

        #.snd_sz = length - len(fst_part)
        #.if snd_sz:
        #.    snd_part = ls[:snd_sz]
        #.    r = fst_part + snd_part if fst_part else snd_part
        #.else:
        #.    r = fst_part
        #.assert len(r) == length
        #.return r

    def __repr__(self):
        return repr_helper(self, self.to_list())
    def __pre_append(self):
        # full ==>> double the size
        #
        # pre: __begin == 0 or 0 < __begin < len(__ls)
        # post: 0 <= __begin < len(__ls)
        #
        sz = self.__size
        ls = self.__ls
        if not sz == len(ls):
            # not full
            return
        # [sz == len(ls)]
        # full
        self.__ver = object()
        i = self.__begin
        if i == 0:
            if not sz:
                # sz: 0 --> 2
                ls.append(_Nothing)
                ls.append(_Nothing)
            else:
                # double the size
                assert sz > 0
                ls.extend(_Nothing for _ in range(sz))
                assert len(ls) == 2*sz
            return
        assert sz > 0
        assert i > 0
        assert sz
        # [sz > 0]
        if 2*i < sz:
            # ls == short ++ long
            short = ls[:i]
            ls[:i] = [_Nothing]*i
            ls += short
            ls += [_Nothing]*(sz-i)
        else:
            # ls == long ++ short
            # !! [sz > 0]
            # [0 <= self.__begin < sz == len(ls)]
            short = ls[i:]
            # [len(short) > 0]
            assert short
            ls[i:] = [_Nothing]*sz
            self.__begin = len(ls)
            ls += short
            # !! [len(short) > 0]
            # [0 <= self.__begin < len(ls)]
        assert len(ls) == 2*sz

    def __post_pop(self):
        # 1/4 full ==>> half the size
        sz = self.__size
        ls = self.__ls
        L = len(ls)
        if not sz:
            self.__ls.clear()
            assert self.__begin == 0
            self.__ver = object()
        elif sz < L >> 2:
            # sz < L//4
            assert sz
            sz_to_del = half_L = L >> 1
            assert sz_to_del

            i = self.__begin
            j = i + sz
            if j >= L:
                j -= L

            if j >= i:
                sz_at_tail = L - j
                assert sz_at_tail
                sz_to_del_at_tail = min(sz_to_del, sz_at_tail)
                del ls[-sz_to_del_at_tail:]
                sz_to_del -= sz_to_del_at_tail
                self.__ver = object()
            del j

            if sz_to_del:
                # to del before __begin
                sz_to_del_before_begin = sz_to_del
                del ls[i-sz_to_del_before_begin:i]
                self.__ver = object()
            assert len(ls) == half_L



    def append_left(self, x):
        #__begin == 0 or 0 < __begin < len(__ls)
        self.__pre_append()
        # 0 <= __begin < len(__ls)
        #assert len(__ls)

        i = self.__begin
        ls = self.__ls
        i -= 1
        if i < 0:
            #assert len(ls)
            i += len(ls)
        ls[i] = x
        self.__begin = i
        self.__size += 1
        self.__ver = object()

    def append_right(self, x):
        #__begin == 0 or 0 < __begin < len(__ls)
        self.__pre_append()
        # 0 <= __begin < len(__ls)
        #assert len(__ls)

        i = self.__begin + self.__size
        ls = self.__ls
        if i >= len(ls):
            #assert len(ls)
            i -= len(ls)
        ls[i] = x
        self.__size += 1
        self.__ver = object()


    def pop_left(self):
        if not self: raise IndexError
        i = self.__begin
        ls = self.__ls
        x = ls[i]
        ls[i] = _Nothing

        self.__size -= 1
        if not self:
            self.__begin = 0
        else:
            i += 1
            if i == len(ls):
                i = 0
            self.__begin = i
        self.__post_pop()
        self.__ver = object()
        return x
    def pop_right(self):
        if not self: raise IndexError
        ls = self.__ls
        i = self.__begin + self.__size - 1
        if i >= len(ls):
            i -= len(ls)

        x = ls[i]
        ls[i] = _Nothing

        if i == self.__begin:
            # ==>> old __size == 1
            # ==>> new __size == 0
            self.__begin = 0
        self.__size -= 1
        self.__post_pop()
        self.__ver = object()
        return x


    def _rotateR1_(self):
        'pop_right >>> append_left # [len(self) >= 2]'
        assert len(self) >= 2
        if 1:
            self.__ver = object()
            ls = self.__ls
            sz = self.__size
            i = self.__begin
                #first
            L = len(ls)
            _i = (i-1)%L
                #pre-first
            j = (i + sz - 1)%L
                #last
            last = ls[j]
            ls[j] = _Nothing
            ls[_i] = last
            self.__begin = _i
        else:
            x = self.pop_right()
            self.append_left(x)
    def _rotateL1_(self):
        'pop_left >>> append_right # [len(self) >= 2]'
        assert len(self) >= 2
        if 1:
            self.__ver = object()
            ls = self.__ls
            sz = self.__size
            i = self.__begin
                #first
            L = len(ls)
            j = (i + sz - 1)%L
                #last
            j1 = (j + 1)%L
                #post-last
            i1 = (i+1)%L
                #second
            first = ls[i]
            ls[i] = _Nothing
            ls[j1] = first
            self.__begin = i1
        else:
            x = self.pop_left()
            self.append_right(x)
    def rotate_right(self, n=1):
        'pop_right >>> append_left'
        return self.rotate(-n)
    def rotate_left(self, n=1):
        'pop_left >>> append_right'
        return self.rotate(n)
    def rotate(self, n=1):
        'Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.'
        #n = operator.index(n)
        sz = len(self)
        if sz < 2:
            return
        # [2 <= sz]
        if n==1:
            # [2 <= sz]
            self._rotateL1_()
            return
        if not n:
            return
        # [2 <= sz]
        n %= sz
        if not n:
            return
        # [1 <= n < sz]
        hsz = sz>>1
        # !! [2 <= sz]
        # [1 <= hsz < sz <= hsz*2+1]
        # [1 <= sz-hsz <= hsz+1]
        if n > hsz:
            # [1 <= hsz < n < sz <= hsz*2+1]
            n -= sz
            # [1-sz <= hsz-sz < n < 0 <= hsz*2+1-sz]
            m = -n
            # [sz-1 >= sz-hsz > m > 0]
            # [1 <= m < sz-hsz <= sz-1]
            # [1 <= m < sz-hsz <= min(hsz+1, sz-1)]
            assert 1 <= m <= hsz < sz
            # [1 <= m <= hsz < sz]
            f = self._rotateR1_
            k = m
            # [1 <= k <= hsz < sz]
        else:
            assert 1 <= n <= hsz < sz
            # [1 <= n <= hsz < sz]
            f = self._rotateL1_
            k = n
            # [1 <= k <= hsz < sz]
        # [1 <= k <= hsz < sz]
        f, k
        for _ in range(k):
            f()


    def popleft(self):
        return self.pop_left()
    def pop(self):
        return self.pop_right()
    def appendleft(self, x, /):
        return self.append_left(x)
    def append(self, x, /):
        return self.append_right(x)
    def extendleft(self, iterable):
        return self.extend_left(iterable)
    def extend(self, iterable):
        return self.extend_right(iterable)
if 0:
    from collections import deque
    dir(deque)
['__add__', '__contains__', '__copy__', '__delitem__', '__eq__', '__ge__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setitem__', '__str__', 'append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 'index', 'insert', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate']
#.maxlen
#.appendleft
#.extendleft
#.popleft
#.rotate
    #Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.





from seed.types.Deque import Deque
from seed.types.Deque import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):
