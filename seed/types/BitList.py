r'''[[[
e ../../python3_src/seed/types/BitList.py
seed.types.BitList
py -m seed.types.BitList
from seed.types.BitList import BitList


>>> [] < ()
Traceback (most recent call last):
  ...
TypeError: '<' not supported between instances of 'list' and 'tuple'

>>> ls=[]
>>> ls[0]=1
Traceback (most recent call last):
  ...
IndexError: list assignment index out of range
>>> ls[0:5]=[]
>>> ls[0:5]=[2,3]
>>> ls
[2, 3]
>>> ls[0:5:6]=[2,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 2 to extended slice of size 1
>>> ls[0:5:2]=[2,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 2 to extended slice of size 1
>>> ls[0:5:1]=[2,3]
>>> ls
[2, 3]
>>> ls[0:5:2]=[4]
>>> ls
[4, 3]
>>> ls[0:5:2]=iter([4])
>>> ls
[4, 3]
>>> ls[0:5:2]=iter([5,6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 2 to extended slice of size 1
>>> ls
[4, 3]
>>> ls[0:5:2]=iter([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 0 to extended slice of size 1
>>> ls
[4, 3]
>>> ls[0:5:-1]=iter([])
>>> ls
[4, 3]
>>> ls[0:5:1]=iter([])
>>> ls
[]
>>> ls=[1,2]
>>> ls[5:-1:-1]=iter([])
>>> ls
[1, 2]
>>> ls[5:0:-1]=iter([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 0 to extended slice of size 1
>>> ls[-1:0:-1]=iter([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 0 to extended slice of size 1
>>> ls[-1:-1:-1]=iter([])
>>> ls
[1, 2]
>>> ls[-1:-1:-1]
[]
>>> ls[-1:0:-1]
[2]
>>> ls[-1::-1]
[2, 1]
>>> ls[-1::-1]=iter([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 0 to extended slice of size 2
>>> ls[-1::]=iter([])
>>> ls
[1]
>>> ls[5::]=iter([])
>>> ls[5::]=iter([1]) #WTF?!
>>> ls
[1, 1]
>>> ls=[1,1,2,1]
>>> ls.remove(1)
>>> ls
[1, 2, 1]
>>>

#>>> help(list.remove)
remove(self, value, /)
    Remove first occurrence of value.

    Raises ValueError if the value is not present.

index(self, value, start=0, stop=9223372036854775807, /)
    Return first index of value.

    Raises ValueError if the value is not present.


sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.

    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

    If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.

    The reverse flag can be set to sort in descending order.


#>>> help(slice.indices)
indices(...)
    S.indices(len) -> (start, stop, stride)

    Assuming a sequence of length len, calculate the start and stop indices, and the stride length of the extended slice described by S. Out of bounds indices are clipped in a manner consistent with the handling of normal slices.




class array(builtins.object)
 |  array(typecode [, initializer]) -> array
 |
 |  Return a new array whose items are restricted
by typecode, and
|  initialized from the optional initializer valu
e, which must be a list,
|  string or iterable over elements of the approp
riate type.
 |
 |  Arrays represent basic values and behave very much like lists, except
 |  the type of objects stored in them is constrained. The type is specified
 |  at object creation time by using a type code, which is a single character.
 |  The following type codes are defined:
 |
 |      Type code   C Type             Minimum size in bytes
 |      'b'         signed integer     1
 |      'B'         unsigned integer   1
 |      'u'         Unicode character  2 (see note)
 |      'h'         signed integer     2
 |      'H'         unsigned integer   2
 |      'i'         signed integer     2
 |      'I'         unsigned integer   2
 |      'l'         signed integer     4
 |      'L'         unsigned integer   4
 |      'q'         signed integer     8 (see note)
 |      'Q'         unsigned integer   8 (see note)
 |      'f'         floating point     4
 |      'd'         floating point     8
 |
 |  NOTE: The 'u' typecode corresponds to Python's unicode character. On
 |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
 |
 |  NOTE: The 'q' and 'Q' type codes are only available if the platform
 |  C compiler used to build Python supports 'long long', or, on Windows,
 |  '__int64'.
 |

#]]]'''
__all__ = '''
    BitList

    '''.split()
from collections.abc import MutableSequence
from itertools import chain, repeat, islice
from seed.helper.repr_input import repr_helper
from seed.iters.cmp4iterable import cmp4iterable



def iter5reverse(reverse, /):
    f = reversed if reverse else iter
    return f
def iter_(reverse, iterable, /):
    _iter = iter5reverse(reverse)
    return _iter(iterable)
def iter_01s5uint8s_(reverse, uint8s, /):
    _iter = iter5reverse(reverse)
    for u in _iter(uint8s):
        assert 0 <= u < 256
        #bug:s = f'{u:8>0b}'
        s = f'{u:0>8b}'
        yield from iter_01s5str(_iter(s))
    pass
def iter_01s5str_(reverse, s, /):
    _iter = iter5reverse(reverse)
    return iter_01s5str(_iter(s))
def reversed_iter_01s5str(s, /):
    return iter_01s5str(reversed(s))
def iter_01s5str(s, /):
    for ch in s:
        if ch == '1':
            yield 1
        elif ch == '0':
            yield 0
        elif ch in '_':
            pass
        else:
            raise ValueError(f'bad char: {ch!r}')
    pass
def reversed_iter_01s5uint8s(uint8s, /):
    return iter_01s5uint8s_(True, uint8s)
def iter_01s5uint8s(uint8s, /):
    return iter_01s5uint8s_(False, uint8s)

assert [*iter_01s5uint8s(b'\0')] == [0,0,0,0,0,0,0,0,], [*iter_01s5uint8s(b'\0')]
assert [*iter_01s5uint8s(b'\0\1\x80\xfe')] == [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,1, 1,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,0,], [*iter_01s5uint8s(b'\0\1\x80\xfe')]


def divmod_8_(i, /):
    assert i >= 0
    r = i&0b0111
    q = i>>3
    return (q, r)

def mk_uint_from_01s(_01s, /):
    s = ''.join(map(str, _01s))
    u = int(s, 2)
    assert u >= 0
    return u

def pint2payload_01s_str(u, /):
    if not type(u) is int: raise TypeError
    if not u > 0: raise ValueError
    s = bin(u)
    assert s.startswith('0b1')
    s = s[3:]
    return s

class BitList(MutableSequence):
    def __init__(self, may_01s_or_01str_or_payload_pint=None, /):
        self._bs = bytearray()
        self._tail = []
        self._sz = 0

        if type(may_01s_or_01str_or_payload_pint) is int:
            payload_pint = may_01s_or_01str_or_payload_pint
            _01str = pint2payload_01s_str(payload_pint)
            may_01s_or_01str = _01str
            del payload_pint, _01str
        else:
            may_01s_or_01str = may_01s_or_01str_or_payload_pint
        del may_01s_or_01str_or_payload_pint
        may_01s_or_01str

        if type(may_01s_or_01str) is str:
            _01str = may_01s_or_01str
            _01s = iter_01s5str(_01str)
            may_01s = _01s
            del _01str, _01s
        else:
            may_01s = may_01s_or_01str
        del may_01s_or_01str
        may_01s


        if may_01s is None:
            _01s = ()
        else:
            _01s = may_01s
        del may_01s
        _01s

        _01s = iter(_01s)
        self.extend(_01s)

    def _unbox__BitList(self, /):
        bs = self._bs
        tail = self._tail
        sz = self._sz
        return (sz, tail, bs)
    def _verify__BitList(self, /):
        (sz, tail, bs) = self._unbox__BitList()
        if not 0 <= len(tail) < 8: raise Exception
        if not len(bs)*8 + len(tail) == sz: raise Exception
        if not set(tail) <= {0,1}: raise Exception
    def _iter_as_01s(self, /):
        self._verify__BitList()
        (sz, tail, bs) = self._unbox__BitList()
        yield from iter_01s5uint8s(bs)
        yield from tail
    def _reversed_iter_as_01s(self, /):
        self._verify__BitList()
        (sz, tail, bs) = self._unbox__BitList()
        yield from reversed(tail)
        yield from reversed_iter_01s5uint8s(bs)
    def __iter__(self, /):
        return self._iter_as_01s()
    def __reversed__(self, /):
        return self._reversed_iter_as_01s()



    def to_01str(self, /):
        _01str = ''.join(map(str, self._iter_as_01s()))
        return _01str
    def to_payload_pint(self, /):
        _01str = self.to_01str()
        payload_pint = int('1'+_01str, 2)
        return payload_pint

    def __repr__(self, /):
        _01str = self.to_01str()
        return repr_helper(self, _01str)

    def __eq__(self, other, /):
        return self._unbox__BitList() == other._unbox__BitList()
    def __ne__(self, other, /):
        return not self == other
    def __ge__(self, other, /):
        return not self < other
    def __le__(self, other, /):
        return not self > other

    def __gt__(self, other, /):
        if not isinstance(other, __class__): raise TypeError
        return other < self
    def __lt__(self, other, /):
        if not isinstance(other, __class__): raise TypeError
        return cmp4iterable(self._iter_as_01s(), other._iter_as_01s(), __cmp__=int.__sub__) < 0


    def _check__element4BitList(self, x, /):
        if not (type(x) in (int, bool) and 0 <= x < 2): raise TypeError
    def _check_and_convert__element4BitList(self, x, /):
        self._check__element4BitList(x)
        x = 1 if x else 0
        return x
        #x = int(x)
        #assert x is 1
        #return x
    def __contains__(self, x, /):
        x = self._check_and_convert__element4BitList(x)

        (sz, tail, bs) = self._unbox__BitList()
        if x:
            return any(tail) or any(bs)
        else:
            return (not all(tail)) or any(map(0xff .__ne__, bs))
        pass
    def __len__(self, /):
        return self._sz

    def __getitem__(self, i, /):
        (sz, tail, bs) = self._unbox__BitList()
        def _get(i, /):
            assert 0 <= i < sz
            (q, r) = divmod_8_(i)
            if q == len(bs):
                x = tail[r]
            else:
                u = bs[q]
                #bug:x = (u>>r)&1
                x = (u>>(7^r))&1
            return x

        if type(i) is int:
            if not -sz <= i < sz: raise IndexError(i)
            if i < 0:
                i += sz
            return _get(i)

        elif type(i) is slice:
            sl = i
            del i
            (start, stop, stride) = sl.indices(sz)
            return self.mk_BitList__from_01s(map(_get, range(start, stop, stride)))
        raise TypeError(type(i))

    def mk_BitList__from_01s(self, _01s, /):
        #not classmethod!!
        return type(self)(iter(_01s))

    def __setitem__(self, i, x, /):
        (sz, tail, bs) = self._unbox__BitList()
        def _set(i, x, /):
            assert 0 <= i < sz
            (q, r) = divmod_8_(i)
            if q == len(bs):
                tail[r] = x
            else:
                u = bs[q]
                #bug:y = (u>>r)&1
                y = (u>>(7^r))&1
                if not y==x:
                    u ^= 1<<(7^r)
                    bs[q] = u
            return None

        if type(i) is int:
            if not -sz <= i < sz: raise IndexError(i)
            if i < 0:
                i += sz
            return _set(i, x)

        elif type(i) is slice:
            sl = i
            xs = x
            del i, x
            (start, stop, stride) = sl.indices(sz)
            rs = range(start, stop, stride)
            L = len(rs)
            #if sl.stop is None is sl.stride:
            if stop==sz and stride==1:
                #del+extend
                del self[start:]
                self.extend(xs)
            else:
                #set exactly; sz not change
                try:
                    len_xs = len(xs)
                except TypeError:
                    xs = [*xs]
                    len_xs = len(xs)
                    pass
                if not len_xs == L: raise IndexError
                for _ in map(_set, rs, xs):pass

            return None
        raise TypeError(type(i))

    def _del_tail_from__mod8(self, i, /):
        assert 0 <= i
        #del self[i:]
        (sz, tail, bs) = self._unbox__BitList()
        #if not i < sz: return
        if not 0 <= i < sz: raise logic-err
        (q, r) = divmod_8_(i)
        removed_tail = [*iter_01s5uint8s(bs[q:]), *tail]
        #new_bs = bs[:q]
        del bs[q:]
        tail.clear()
        #return (new_bs, removed_tail, q8, q, r)
        self._sz -= len(removed_tail)
        return (removed_tail, q, r)
    def __delitem__(self, i, /):
        (sz, tail, bs) = self._unbox__BitList()
        if type(i) is int:
            #assert sz > 0
            sl = slice(i, sz, sz+1)
        elif type(i) is slice:
            sl = i
        else:
            raise TypeError(type(i))
        del i
        sl
        (start, stop, stride) = sl.indices(sz)
        assert start >= 0
        assert stop >= 0
        #assert stride >= 0
        rs = range(start, stop, stride)
        if not rs:
            return
        idx4min = -1 if stride < 0 else +0
        true_start = rs[idx4min]

        #del self[start///8*8:]
        #bug:(removed_tail, q, r) = self._del_tail_from__mod8(start)
        if true_start >= sz:
            return
        (removed_tail, q, r) = self._del_tail_from__mod8(true_start)
        q8 = q<<3
        assert q8+r == true_start
        del removed_tail[start-q8:stop-q8:stride]
        _sf = __class__(iter(removed_tail))
        self._iadd__sz_mod8_eq0(_sf)
        assert self._sz == q8 + _sf._sz
        #self._verify__BitList()
        assert self._sz == (len(bs)<<3)+len(tail)
        L = len(rs)
        assert self._sz == sz - L
        return





    def __add__(self, other, /):
        #if not isinstance(other, __class__): raise TypeError(type(other))
        return self.mk_BitList__from_01s(chain(self, other))
    if 0:
      def __radd__(self, other, /):
        if not isinstance(other, __class__): raise TypeError(type(other))
        return other + self

    def _iadd__sz_mod8_eq0(self, other, /):
        assert not self._tail
        if not isinstance(other, __class__):
            other = __class__(iter(other))
        self._bs += other._bs
        self._tail += other._tail
        self._sz += other._sz
        return self
    def __iadd__(self, other, /):
        if not self._tail:
            self._iadd__sz_mod8_eq0(other)
        else:
            if other is self:
                other = [*other]
            self.extend(other)
        return self

    def __mul__(self, n, /):
        if not type(n) is int: raise TypeError
        ''*n
        it = chain.from_iterable(repeat(self, n))
        return self.mk_BitList__from_01s(it)
    if 0:
        __rmul__ = __mul__

    def _swap__BitList(self, other, /):
        if not isinstance(other, __class__): raise TypeError(type(other))
        [(self._sz, self._tail, self._bs)
        ,(other._sz, other._tail, other._bs)
        ]=(
        [(other._sz, other._tail, other._bs)
        ,(self._sz, self._tail, self._bs)
        ])
    def __imul__(self, n, /):
        tmp = self*n
        self._swap__BitList(tmp)
        return self
    def append(self, x, /):
        x = self._check_and_convert__element4BitList(x)

        (sz, tail, bs) = self._unbox__BitList()
        tail.append(x)
        if len(tail) == 8:
            u = mk_uint_from_01s(tail)
            assert 0 <= u < 0x100
            bs.append(u)
            tail.clear()
        self._sz += 1

    def insert(self, i, x, /):
        x = self._check_and_convert__element4BitList(x)

        (sz, tail, bs) = self._unbox__BitList()
        if type(i) is int:
            #assert sz > 0
            sl = slice(i, sz, sz+1)
        else:
            raise TypeError(type(i))
        del i
        sl
        (start, stop, stride) = sl.indices(sz)
        assert start >= 0
        assert stop == sz
        assert stride >= 1
        #del self[start///8*8:]
        if start > sz: raise IndexError
        if start == sz:
            self.append(x)
            return
        (removed_tail, q, r) = self._del_tail_from__mod8(start)
        q8 = q<<3
        assert q8+r == start
        removed_tail.insert(start-q8, x)
        _sf = __class__(iter(removed_tail))
        self._iadd__sz_mod8_eq0(_sf)
        return

    def pop(self, i=-1, /):
        (sz, tail, bs) = self._unbox__BitList()
        r'''[[[

        if type(i) is int:
            #if not sz: raise IndexError
            #assert sz > 0
            sl = slice(i, sz, sz+1)
        else:
            raise TypeError(type(i))
        del i
        sl
        (start, stop, stride) = sl.indices(sz)
        assert start >= 0
        assert stop == sz
        assert stride >= 1
        if start >= sz: raise IndexError
            bug:since assert slice(-4, 3, 3+1).indices(3) == (0, 3, 4)
        #]]]'''
        if type(i) is int:
            if not -sz <= i < sz: raise IndexError
            start = i
            if start < 0:
                start += sz
            assert 0 <= start < sz
        else:
            raise TypeError(type(i))

        #del self[start///8*8:]
        (removed_tail, q, r) = self._del_tail_from__mod8(start)
        q8 = q<<3
        assert q8+r == start
        x = removed_tail.pop(start-q8)
        _sf = __class__(iter(removed_tail))
        self._iadd__sz_mod8_eq0(_sf)
        return x

    def remove(self, x, /):
        i = self.index(x)
        del self[i]
        return
    def clear(self, /):
        self._bs.clear()
        self._tail.clear()
        self._sz = 0

    def copy(self, /):
        other = __class__()
        other._bs = self._bs.copy()
        other._tail = self._tail.copy()
        other._sz = self._sz
        return other
        return self.mk_BitList__from_01s(self)

    def count(self, x, /):
        x = self._check_and_convert__element4BitList(x)
        it = self._iter_as_01s()
        if x:
            n = sum(it)
        else:
            n = sum(map(1 .__sub__, it))
        return n
    def flip_01s__emplace(self, /):
        (sz, tail, bs) = self._unbox__BitList()
        for i in range(len(tail)):
            tail[i] = 1^tail[i]
        for i in range(len(bs)):
            bs[i] = 0xff^bs[i]

    def flip_01s__immutable(self, /):
        other = self.copy()
        other.flip_01s__emplace()
        return other

    #def index(self, x, /, *args):
    def index(self, x, start=None, stop=None, /):
        x = self._check_and_convert__element4BitList(x)
        (sz, tail, bs) = self._unbox__BitList()
        sl = slice(start, stop, None)
        (start, stop, stride) = sl.indices(sz)
        if not start < stop: raise ValueError
        (q0,r0) = divmod_8_(start)
        (q1,r1) = divmod_8_(stop)
        it0 = iter_01s5uint8s(bs[q0:q1+1])
        it1 = iter(tail)
        it = chain(it0, it1)
        it = islice(it, r0, r0+stop-start)
        for i, y in enumerate(it, start):
            if y==x:
                return i
        raise ValueError

    def reverse(self, /):
        tmp = self.mk_BitList__from_01s(reversed(self))
        self._swap__BitList(tmp)
    def sort(self, /, *, key=None, reverse=False):
        num_1s = self.count(1)
        num_0s = len(self)-num_1s
        if num_1s == 0 or num_0s == 0:
            return

        vs = [0,1]
        if key is not None:
            vs = [*map(key, vs)]
        if vs[0] == vs[1]:
            return

        _1s = repeat(1, num_1s)
        _0s = repeat(0, num_0s)
        bss = [_0s, _1s]
        if (vs[0] > vs[1]) ^ bool(reverse):
            bss.reverse()
        tmp = self.mk_BitList__from_01s(chain(*bss))
        self._swap__BitList(tmp)

    def extend(self, other, /):
        for x in other:
            self.append(x)


    ######################
    ######################
    ######################
    ######################
    ######################
    ######################
    def __invert__(self, /):
        '~self'
        return self.flip_01s__immutable()
        return self.mk_BitList__from_01s(map(1 .__xor__, self))


    def _binop_helper(self, other, /):
        if not isinstance(other, __class__): raise TypeError(type(other))
        L = len(other) - len(self)
        if L < 0:
            lhs, rhs = other, self
            L = -L
        else:
            lhs, rhs = self, other
        assert L == len(rhs) - len(lhs) >= 0
        return (L, lhs, rhs)
    def __xor__(self, other, /):
        (L, lhs, rhs) = self._binop_helper(other)
        lhs = chain(lhs, repeat(0, L))
        rhs = iter(rhs)
        return self.mk_BitList__from_01s(map(int.__xor__, lhs, rhs))

        tmp = self.copy()
        tmp ^= other
        return tmp
    def __or__(self, other, /):
        (L, lhs, rhs) = self._binop_helper(other)
        lhs = chain(lhs, repeat(0, L))
        rhs = iter(rhs)
        return self.mk_BitList__from_01s(map(int.__or__, lhs, rhs))

        tmp = self.copy()
        tmp |= other
        return tmp
    def __and__(self, other, /):
        (L, lhs, rhs) = self._binop_helper(other)
        #lhs = chain(lhs, repeat(0, L))
        lhs = iter(lhs)
        rhs = iter(rhs)
        return self.mk_BitList__from_01s(map(int.__and__, lhs, rhs))

        tmp = self.copy()
        tmp &= other
        return tmp
    def __ixor__(self, other, /):
        tmp = self ^ other
        self._swap__BitList(tmp)
        return self
    def __ior__(self, other, /):
        tmp = self | other
        self._swap__BitList(tmp)
        return self
    def __iand__(self, other, /):
        tmp = self & other
        self._swap__BitList(tmp)
        return self

BitList.__doc__ = r'''[[[

>>> from seed.types.BitList import BitList

#__init__,__repr__
>>> BitList()
BitList('')
>>> BitList(None)
BitList('')
>>> BitList([])
BitList('')
>>> BitList([1,0,0])
BitList('100')
>>> BitList('')
BitList('')
>>> BitList('100')
BitList('100')
>>> BitList(0b1)
BitList('')
>>> BitList(0b1100)
BitList('100')
>>> BitList(0b1_10100100010000100000)
BitList('10100100010000100000')

#__iter__,__reversed__
>>> [*iter(BitList('100'))]
[1, 0, 0]
>>> [*reversed(BitList('100'))]
[0, 0, 1]
>>> [*iter(BitList('10100100010000'))]
[1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
>>> [*reversed(BitList('10100100010000'))]
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]
>>> [*iter(BitList('10100100010000100000'))]
[1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
>>> [*reversed(BitList('10100100010000100000'))]
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]



#to_01str,to_payload_pint
>>> BitList().to_01str()
''
>>> BitList('10100100010000100000').to_01str()
'10100100010000100000'
>>> BitList().to_payload_pint()
1
>>> BitList('10100100010000100000').to_payload_pint() == 0b1_10100100010000100000
True


#cmp:__eq__
>>> BitList('10100100010000100000') == BitList('10100100010000100000')
True
>>> BitList('10100100010000100000') != BitList('10100100010000100000')
False
>>> BitList('10100100010000') == BitList('10100100010000100000')
False
>>> BitList('10100100010000') != BitList('10100100010000100000')
True


>>> BitList('10100100010000100000') <= BitList('10100100010000100000')
True
>>> BitList('10100100010000100000') < BitList('10100100010000100000')
False
>>> BitList('10100100010000100000') >= BitList('10100100010000100000')
True
>>> BitList('10100100010000100000') > BitList('10100100010000100000')
False



>>> BitList('10100100010000') <= BitList('10100100010000100000')
True
>>> BitList('10100100010000') < BitList('10100100010000100000')
True
>>> BitList('10100100010000') >= BitList('10100100010000100000')
False
>>> BitList('10100100010000') > BitList('10100100010000100000')
False



#__contains__
>>> 1 in BitList('10100100010000100000')
True
>>> 0 in BitList('10100100010000100000')
True
>>> 1 in BitList('')
False
>>> 0 in BitList('')
False
>>> 1 in BitList('111')
True
>>> 0 in BitList('111')
False
>>> 1 in BitList('000')
False
>>> 0 in BitList('000')
True
>>> 0 in BitList('11111111111')
False
>>> 1 in BitList('00000000000')
False
>>> 0 in BitList('11011111111')
True
>>> 1 in BitList('00100000000')
True
>>> 0 in BitList('11111111101')
True
>>> 1 in BitList('00000000010')
True

#__len__
>>> len(BitList(''))
0
>>> len(BitList('10100'))
5
>>> len(BitList('10100100010000100000'))
20

#__getitem__
>>> BitList('10100100010000100000')[0]
1
>>> BitList('10100100010000100000')[1]
0
>>> BitList('10100100010000100000')[9]
1
>>> BitList('10100100010000100000')[10]
0
>>> BitList('10100100010000100000')[-1]
0
>>> BitList('10100100010000100000')[-5]
0
>>> BitList('10100100010000100000')[-6]
1
>>> BitList('10100100010000100000')[:]
BitList('10100100010000100000')
>>> BitList('10100100010000100000')[::-1]
BitList('00000100001000100101')
>>> BitList('10100100010000100000')[8:14]
BitList('010000')
>>> BitList('10100100010101010000')[7:16:2]
BitList('01111')
>>> BitList('10100100010101010000')[-4:7:-2]
BitList('00000')
>>> BitList('10100100010101010000')[-4-1:7-1:-2]
BitList('11110')

#mk_BitList__from_01s
>>> BitList().mk_BitList__from_01s([0,0,1,0])
BitList('0010')

#__setitem__
>>> ls = BitList('0000000000')
>>> ls[0] = 1
>>> ls
BitList('1000000000')
>>> ls[6] = 1
>>> ls
BitList('1000001000')
>>> ls[9] = 1
>>> ls
BitList('1000001001')
>>> ls[9:] = [0,0,1]
>>> ls
BitList('100000100001')
>>> ls[100:] = [0,0,1]
>>> ls
BitList('100000100001001')
>>> ls[::2] = [1]*((len(ls)+1)//2)
>>> ls
BitList('101010101011101')
>>> ls[::-2] = [1]*((len(ls)+1)//2)
>>> ls
BitList('101010101011101')
>>> ls[::-2] = [0]*((len(ls)+1)//2)
>>> ls
BitList('000000000001000')
>>> ls[-2::-2] = [1]*((len(ls))//2)
>>> ls
BitList('010101010101010')

#__delitem__
>>> ls = BitList('000010101000001')
>>> del ls[6]
>>> ls
BitList('00001001000001')
>>> del ls[6:4:-1]
>>> ls
BitList('000011000001')
>>> del ls[6:10]
>>> ls
BitList('00001101')



#append
>>> ls = BitList('')
>>> for _ in map(ls.append, [0,1,0,0,1,0,0,0,1,1,0,0,0,0,1]):pass
>>> ls
BitList('010010001100001')

#insert
>>> ls = BitList('')
>>> for x in [0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0]:ls.insert(-4,x)
>>> ls
BitList('10001100001110000010')
>>> ls = []
>>> for x in [0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0]:ls.insert(-4,x)
>>> ls
[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0]


#pop
>>> ls = BitList('10001100001110000010')
>>> [ls.pop(-4) for _ in range(len(ls)-3)]
[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
>>> ls
BitList('010')
>>> ls.pop(-4)
Traceback (most recent call last):
  ...
IndexError
>>> ls
BitList('010')
>>> ls = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0]
>>> [ls.pop(-4) for _ in range(len(ls)-3)]
[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
>>> ls
[0, 1, 0]
>>> ls.pop(-4)
Traceback (most recent call last):
  ...
IndexError: pop index out of range
>>> ls
[0, 1, 0]
>>> slice(-4, 3, 3+1).indices(3)
(0, 3, 4)
>>> slice(-4, 2, 2+1).indices(2)
(0, 2, 3)
>>> slice(-4, 1, 1+1).indices(1)
(0, 1, 2)
>>> slice(-4, 0, 0+1).indices(0)
(0, 0, 1)


#remove
>>> ls = BitList('10001100001110000010')
>>> ls.remove(0)
>>> ls
BitList('1001100001110000010')
>>> ls.remove(1)
>>> ls
BitList('001100001110000010')
>>> ls.remove(1)
>>> ls
BitList('00100001110000010')
>>> ls.remove(0)
>>> ls
BitList('0100001110000010')

#clear
>>> ls = BitList('10001100001110000010')
>>> ls.clear()
>>> ls
BitList('')

#copy
>>> ls = BitList('10001100001110000010')
>>> ls2 = ls.copy()
>>> ls.clear()
>>> ls
BitList('')
>>> ls2
BitList('10001100001110000010')

#count
>>> ls = BitList('10001100001110000010')
>>> ls.count(1)
7
>>> ls.count(0)
13


#flip_01s__emplace
#flip_01s__immutable
>>> ls = BitList('10001100001110000010')
>>> ls.flip_01s__emplace()
>>> ls
BitList('01110011110001111101')
>>> ls.flip_01s__immutable()
BitList('10001100001110000010')
>>> ls
BitList('01110011110001111101')


#index
>>> ls = BitList('10001100001110000010')
>>> ls.index(0)
1
>>> ls.index(1)
0
>>> ls.index(0,3)
3
>>> ls.index(0,4)
6
>>> ls.index(1,1)
4


#reverse
>>> ls = BitList('10001100001110000010')
>>> ls.reverse()
>>> ls
BitList('01000001110000110001')


#sort
>>> ls = BitList('10001100001110000010')
>>> ls.sort()
>>> ls
BitList('00000000000001111111')
>>> ls = BitList('10001100001110000010')
>>> ls.sort(reverse=True)
>>> ls
BitList('11111110000000000000')
>>> ls = BitList('10001100001110000010')
>>> ls.sort(key=lambda _:3)
>>> ls
BitList('10001100001110000010')
>>> ls = BitList('10001100001110000010')
>>> ls.sort(key=lambda x:1-x)
>>> ls
BitList('11111110000000000000')
>>> ls = BitList('10001100001110000010')
>>> ls.sort(key=lambda x:1-x, reverse=True)
>>> ls
BitList('00000000000001111111')

#extend
>>> ls = BitList('10001100001110000010')
>>> #bug:ls.extend(ls)
>>> ls.extend([0,1]*5)
>>> ls
BitList('100011000011100000100101010101')

#__add__
>>> ls = BitList('10001100001110000010')
>>> ls+ls
BitList('1000110000111000001010001100001110000010')
>>> ls
BitList('10001100001110000010')

#__iadd__
>>> ls = ls2 = BitList('10001100001110000010')
>>> ls+=ls
>>> ls is ls2
True
>>> ls2
BitList('1000110000111000001010001100001110000010')

#__mul__
>>> ls = BitList('10001100001110000010')
>>> ls*3
BitList('100011000011100000101000110000111000001010001100001110000010')
>>> ls
BitList('10001100001110000010')

#__imul__
>>> ls = ls2 = BitList('10001100001110000010')
>>> ls*=3
>>> ls is ls2
True
>>> ls2
BitList('100011000011100000101000110000111000001010001100001110000010')

######################
######################
######################
######################
######################
######################
#__invert__
>>> ls = BitList('10001100001110000010')
>>> ~ls
BitList('01110011110001111101')
>>> ls
BitList('10001100001110000010')

#__xor__
>>> ls = BitList('10001100001110000010')
>>> ls^ls
BitList('00000000000000000000')
>>> ls^BitList('100010100011')
BitList('00000110000010000010')
>>> ls
BitList('10001100001110000010')

#__ixor__
>>> ls = ls2 = BitList('10001100001110000010')
>>> ls^=ls
>>> ls is ls2
True
>>> ls2
BitList('00000000000000000000')

>>> ls = ls2 = BitList('10001100001110000010')
>>> ls^=BitList('100010100011')
>>> ls is ls2
True
>>> ls2
BitList('00000110000010000010')

#__or__
>>> ls = BitList('10001100001110000010')
>>> ls|ls
BitList('10001100001110000010')
>>> ls|~ls
BitList('11111111111111111111')
>>> ls|~BitList('100010100011')
BitList('11111101111110000010')
>>> ls
BitList('10001100001110000010')

#__ior__
>>> ls = ls2 = BitList('10001100001110000010')
>>> ls|=ls
>>> ls is ls2
True
>>> ls2
BitList('10001100001110000010')

>>> ls = ls2 = BitList('10001100001110000010')
>>> ls|=~ls
>>> ls is ls2
True
>>> ls2
BitList('11111111111111111111')

>>> ls = ls2 = BitList('10001100001110000010')
>>> ls|=~BitList('100010100011')
>>> ls is ls2
True
>>> ls2
BitList('11111101111110000010')

#__and__
>>> ls = BitList('10001100001110000010')
>>> ls&ls
BitList('10001100001110000010')
>>> ls&~ls
BitList('00000000000000000000')
>>> ls&~BitList('100010100011')
BitList('000001000000')
>>> ls
BitList('10001100001110000010')

#__iand__
>>> ls = ls2 = BitList('10001100001110000010')
>>> ls&=ls
>>> ls is ls2
True
>>> ls2
BitList('10001100001110000010')

>>> ls = ls2 = BitList('10001100001110000010')
>>> ls&=~ls
>>> ls is ls2
True
>>> ls2
BitList('00000000000000000000')

>>> ls = ls2 = BitList('10001100001110000010')
>>> ls&=~BitList('100010100011')
>>> ls is ls2
True
>>> ls2
BitList('000001000000')


#



#]]]'''

if __name__ == "__main__":
    import doctest
    doctest.testmod()

