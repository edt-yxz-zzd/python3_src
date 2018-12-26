
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

'''

__all__ = '''
    Deque
    '''.split()

from seed.helper.repr_input import repr_helper
import operator # .index

class _Nothing:pass
class Deque:
    '''
methods:
    __len__
    __getitem__
    __repr__
    to_list

    extend_left
    extend_right
    append_left
    append_right
    pop_left
    pop_right

'''
    def __init__(self, iterable=None):
        # __begin == 0 or 0 < __begin < len(__ls)
        self.__ls = []
        self.__begin = 0
        self.__size = 0

        if iterable is not None:
            self.extend_right(iterable)
    def __len__(self):
        return self.__size
    def extend_left(self, iterable):
        for _ in map(self.append_left, iterable): pass
    def extend_right(self, iterable):
        for _ in map(self.append_right, iterable): pass

    def __getitem__(self, idx_or_slice):
        if type(idx_or_slice) is slice:
            # return __class__(...)
            raise NotImplementedError
        #elif isinstance(idx_or_slice, int):
        idx = operator.index(idx_or_slice)
        sz = self.__size
        if not -sz <= idx < sz: raise IndexError('out-of-range')
        if idx < 0:
            idx += sz

        idx += self.__begin
        L = len(self.__ls)
        if idx > L:
            idx -= L
        return self.__ls[idx]

    #def __iter__(self):
        #????? what if modified while __iter__ ????
        # use to_list instead
    #def __eq__(self, other): return 
    def to_list(self):
        ls = self.__ls
        i = self.__begin
        sz = self.__size
        fst_half = ls[i:i+sz]

        snd_sz = sz - len(fst_half)
        if snd_sz:
            snd_half = ls[:snd_sz]
            assert fst_half
            r = fst_half + snd_half
        else:
            r = fst_half
        return r
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
        if sz == len(ls):
            # full
            if not sz:
                ls.append(_Nothing)
                ls.append(_Nothing)
            else:
                assert sz > 0
                ls.extend_right(_Nothing for _ in range(sz))
    def __post_pop(self):
        # 1/4 full ==>> half the size
        sz = self.__size
        ls = self.__ls
        L = len(ls)
        if not sz:
            self.__ls.clear()
            assert self.__begin == 0
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
            del j

            if sz_to_del:
                # to del before __begin
                sz_to_del_before_begin = sz_to_del
                del ls[i-sz_to_del_before_begin:i]
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


    def pop_left(self):
        if not self: raise IndexError
        i = self.__begin
        ls = self.__ls
        x = ls[i]
        ls[i] = _Nothing

        i += 1
        if i == len(ls):
            i = 0
        self.__begin = i
        self.__size -= 1
        self.__post_pop()
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
        return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):
