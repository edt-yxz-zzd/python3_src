
__all__ = '''
    PeekableIterator
    '''.split()


from collections import deque
from itertools import islice, chain
from seed.tiny import null_iter


def deque_popleftN(dq, n):
    # return tuple(dq[:n]) and del dq[:n]
    n = min(n, len(dq))
    if n == len(dq):
        r = tuple(dq)
        dq.clear()
        return r
    return tuple(dq.popleft() for _ in range(n))
def deque_dropleftN(dq, n):
    # del dq[:n]
    n = min(n, len(dq))
    if n == len(dq):
        dq.clear()
    else:
        for _ in range(n): dq.popleft()
    return None

def deque_peekN(dq, n):
    # tuple(dq[:n])
    if n >= len(dq):
        return tuple(dq)
    return tuple(islice(dq, n))

def drop_strict(iterator, n):
    # strict v.s. lazy
    #
    # del iterator[:n]
    # islice(iterator, n, None)
    assert hasattr(type(iterator), '__next__')
    #for _ in zip(range(n), iterator):pass
    for _ in islice(iterator, n):pass
    return None

class PeekableIterator:
    r'''iterator with peek/read ops


example:
    # see: merge_two_sorted_iterables
    # see: intersect_two_sorted_iterables
    # see: icut_to
    # see: seed.data_funcs.rngs
    >>> it = PeekableIterator([1,2,3])

    # [] + [1,2,3]
    # peek_relax
    >>> it.peek_relax()
    ()

    # peek1/head
    >>> it.peek1()
    1
    >>> it.head
    1
    >>> it.peek_relax()
    (1,)

    # [1] + [2,3]
    # peek_le
    >>> it.peek_le(2)
    (1, 2)
    >>> it.peek_relax()
    (1, 2)

    # [1,2] + [3]
    # iterator
    >>> next(it)
    1
    >>> it.peek_relax()
    (2,)
    >>> it.peek1()
    2

    # [2] + [3]
    # read1
    >>> it.read1()
    2
    >>> it.peek_relax()
    ()

    # [] + [3]
    # read_le
    >>> it.read_le(0)
    ()
    >>> it.peek_relax()
    ()
    >>> it.read_le(4)
    (3,)

    # [] + []
    ### end
    >>> it.peek1()
    Traceback (most recent call last):
      ...
    StopIteration
    >>> it.head
    Traceback (most recent call last):
      ...
    StopIteration
    >>> next(it)
    Traceback (most recent call last):
      ...
    StopIteration
    >>> it.peek_le(2)
    ()
    >>> it.peek_relax()
    ()

    # detach
    >>> it.detach() # doctest: +ELLIPSIS
    ((), ...)
    >>> it = PeekableIterator(range(4))

    # [] + [0,1,2,3]
    >>> it.read_le(2)
    (0, 1)
    >>> it.head
    2

    # [2] + [3]
    >>> buffer, remains = it.detach()
    >>> it.peek_le(5)
    ()
    >>> buffer
    (2,)
    >>> list(remains)
    [3]

    # append_left
    >>> it = PeekableIterator(range(2))
    >>> it.append_left(-1)
    >>> buffer, remains = it.detach()
    >>> buffer
    (-1,)
    >>> list(remains)
    [0, 1]

    # chain_detach
    >>> it = PeekableIterator(range(4))
    >>> it.head
    0
    >>> [*it.chain_detach()]
    [0, 1, 2, 3]


    # fill_and_test
    >>> it = PeekableIterator(range(4))
    >>> it.fill_and_test(3)
    True
    >>> it.peek_relax()
    (0, 1, 2)
    >>> it.fill_and_test(2)
    True
    >>> it.peek_relax()
    (0, 1, 2)
    >>> it.fill_and_test(6)
    False
    >>> it.peek_relax()
    (0, 1, 2, 3)


    # fill_le
    >>> it = PeekableIterator(range(4))
    >>> it.fill_le(3)
    >>> it.peek_relax()
    (0, 1, 2)
    >>> it.fill_le(2)
    >>> it.peek_relax()
    (0, 1, 2)

    # drop_le
    >>> it = PeekableIterator(range(4))
    >>> it.drop_le(2)
    >>> it.peek_relax()
    ()
    >>> it.fill_le(2)
    >>> it.peek_relax()
    (2, 3)
    >>> it.drop_le(1)
    >>> it.peek_relax()
    (3,)

    # peek_relax_le
    >>> it = PeekableIterator(range(4))
    >>> it.peek_relax_le(2)
    ()
    >>> it.fill_le(1)
    >>> it.peek_relax_le(2)
    (0,)
    >>> it.peek_relax()
    (0,)
    >>> it.fill_le(2)
    >>> it.peek_relax_le(2)
    (0, 1)
    >>> it.fill_le(3)
    >>> it.peek_relax_le(2)
    (0, 1)
    >>> it.peek_relax()
    (0, 1, 2)

    # read_relax_le
    >>> it = PeekableIterator(range(4))
    >>> it.read_relax_le(2)
    ()
    >>> it.fill_le(1)
    >>> it.read_relax_le(2)
    (0,)
    >>> it.peek_relax()
    ()
    >>> it.fill_le(3)
    >>> it.read_relax_le(2)
    (1, 2)
    >>> it.peek_relax()
    (3,)

    # len_ge/len_lt
    >>> it = PeekableIterator(range(4))
    >>> it.is_empty()
    False
    >>> it.len_ge(2)
    True
    >>> it.peek_relax()
    (0, 1)
    >>> it.len_lt(3)
    False
    >>> it.peek_relax()
    (0, 1, 2)
    >>> it = PeekableIterator(range(1))
    >>> it.is_empty()
    False
    >>> it = PeekableIterator(range(0))
    >>> it.is_empty()
    True

    # len_relax
    >>> it = PeekableIterator(range(4))
    >>> it.len_relax()
    0
    >>> it.fill_le(3)
    >>> it.len_relax()
    3

    # read_relax
    >>> it = PeekableIterator(range(4))
    >>> it.read_relax()
    ()
    >>> it.fill_le(2)
    >>> it.read_relax()
    (0, 1)


methods ordered:
    __next__
    append_left
    chain_detach
    detach
    fill_and_test
    fill_le
    head
    is_empty
    len_ge
    len_lt
    len_relax
    peek1
    peek_le
    peek_relax
    peek_relax_le
    read1
    read_le
    read_relax
    read_relax_le

methods classified:
    # may raise StopIteration
    __next__
    head
    peek1
    read1

    # may raise ValueError
        # __next__
        peek_le
        read_le
        fill_and_test
        fill_le
        drop_le

        # no __next__
        peek_relax_le
        read_relax_le

    # safe
        # fill_le
        is_empty
        len_ge
        len_lt

        # no fill_le
        append_left
        chain_detach
        detach
        len_relax
        peek_relax
        read_relax

no __bool__
    since other iterator has no such usage, may cause bug
    use "self.len_ge(1)" instead
    use "not self.is_empty()" instead
#'''
    def chain_detach(self):
        'like detach, but chain the output'
        dq = self.__dq
        it = chain(dq, self.__it) if dq else self.__it

        self.__dq = deque()
        self.__it = null_iter
        return it

    def detach(self):
        'remove and return (self.peek_relax(), underlying_iterator)'
        r = self.peek_relax(), self.__it
        self.__dq.clear()
        self.__it = null_iter
        return r
    def append_left(self, x):
        self.__dq.appendleft(x)

    def __init__(self, iterable):
        self.__dq = deque()
        self.__it = iter(iterable)
    def __iter__(self):
        return self
    def __next__(self):
        if self.__dq:
            return self.__dq.popleft()
        return next(self.__it)
    def read_le(self, n):
        'consume; if len(result) < n, then self be empty after this call'
        if not n >= 0: raise ValueError
        dq = self.__dq
        if len(dq) < n:
            #self.fill_le(n)
            #r = tuple(dq)
            #r = tuple(chain(dq, islice(self.__it, n-len(dq))))
            r = (*dq, *islice(self.__it, n-len(dq)))
            dq.clear()
            assert len(r) <= n
        else:
            r = deque_popleftN(dq, n)
            assert len(r) == n
        return r
        r = self.peek_le(n)
        #del dq[:n] # n >= 0 # do not support
        for _ in range(min(n, len(dq))): dq.popleft()
        return r
    def peek_relax(self):
        return tuple(self.__dq)

    def peek_le(self, n):
        'not consume; if len(result) < n, then self be empty after this call'
        if not n >= 0: raise ValueError
        self.fill_le(n)

        dq = self.__dq
        r = deque_peekN(dq, n)
        assert len(r) <= n
        assert len(r) == n <= len(dq) or len(dq) == len(r) < n
        return r

    def drop_le(self, n):
        if not n >= 0: raise ValueError
        dq = self.__dq
        L = len(dq)
        if n <= L:
            deque_dropleftN(dq, n)
            return
        dq.clear()
        #self.__it = islice(self.__it, n-L, None) # too deep
        drop_strict(self.__it, n-L)
        return None
    def read_relax(self):
        r = self.peek_relax()
        self.__dq.clear()
        return r
    def read_relax_le(self, n):
        if not n >= 0: raise ValueError
        return deque_popleftN(self.__dq, n)
    def peek_relax_le(self, n):
        if not n >= 0: raise ValueError
        return deque_peekN(self.__dq, n)
    def len_relax(self):
        'O(1); () -> UInt; len(self.peek_relax())'
        return len(self.__dq)
    def is_empty(self):
        return self.len_lt(1)
    def len_lt(self, n):
        'O(n)*ops'
        return not self.len_ge(n)
    def len_ge(self, n):
        'O(n)*ops'
        if n <= 0: return True
        return self.fill_and_test(n)
    def fill_and_test(self, n=1):
        'not consume; like fill_le, but return bool; test has at least n elements'
        self.fill_le(n)
        return len(self.__dq) >= n
    def fill_le(self, n):
        'not consume; like peek_le, but return None'
        if not n >= 0: raise ValueError
        #if n <= 0: return
        dq = self.__dq
        if len(dq) < n:
            dq.extend(islice(self.__it, n-len(dq)))
        # assert len(dq) >= n or __it is empty
        return None
    def read1(self):
        # may raise StopIteration
        return next(self)
    def peek1(self):
        # may raise StopIteration
        dq = self.__dq
        if not dq:
            dq.append(next(self.__it))
        return dq[0]

    @property
    def head(self):
        # may raise StopIteration
        return self.peek1()


r"""
class IterableReserveLastElement:
    '''should access the last element via self.head not iter'''
    @classmethod
    def may_from_nonempty_iterable(cls, iterable):
        # -> (cls|None)
        it = iter(iterable)
        for head in it:
            return cls(head, it)
        return None
    @classmethod
    def from_nonempty_iterable(cls, iterable):
        # -> (cls|raise StopIteration)
        it = iter(iterable)
        return cls(next(it), it)
        for head in it:
            return cls(head, it)
        raise StopIteration('should not input an empty iterable')

    def __init__(self, head, iterable):
        self.head = head
        self.iterator = iter(iterable)
    def __next__(self):
        self.head, r = next(self.iterator), self.head
        # will not return last element
        return r
    def iter_without_last_element(self):
        # will not yield last element
        maylast = self.head
        # if maylast indeed is last element, then not be yield
        for self.head in self.iterator:
            # store MUST before yield
            yield maylast
            maylast = self.head

    def iter_with_last_element(self):
        # will yield last element
        yield from self.iter_without_last_element()
        yield self.head
    def __iter__(self):
        # will yield last element
        return self.iter_with_last_element()

#"""

if __name__ == "__main__":
    print('\n'.join(s for s in dir(PeekableIterator) if not s.startswith('_')))
    import doctest
    doctest.testmod()

