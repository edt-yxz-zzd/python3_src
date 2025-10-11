#__all__
r'''[[[

seed.iters.PeekableIterator
py -m nn_ns.app.debug_cmd   seed.iters.PeekableIterator -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.PeekableIterator:__doc__,PeekableIterator.__doc__,PeekableIterator__over_PeekableIterator.__doc__  -ht # -ff -df


now:from seed.types.Deque import Deque as deque
since:collections.deque:not support slice:
    dq[n:m] # required by peek_relax_slice
    TypeError: sequence index must be integer, not 'slice'

DONE:
++PeekableIterator__over_PeekableIterator,IPeekableIterator
    view ../../python3_src/seed/recognize/tree/parse_tree.py

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.iters.PeekableIterator:IPeekableIterator@T    =T   +exclude_attrs5listed_in_cls_doc

#]]]'''#'''
__all__ = '''
IPeekableIterator
    echo_or_mk_IPeekableIterator
    PeekableIterator
        echo_or_mk_PeekableIterator
    PeekableIterator__over_PeekableIterator




deque_popleftN
deque_dropleftN
deque_peekN
drop_strict
    '''.split()#'''

if __name__ == "__main__":
    from seed.iters.PeekableIterator import PeekableIterator, echo_or_mk_PeekableIterator


from seed.abc.abc__ver1 import abstractmethod, override, ABC
from collections import deque
from seed.types.Deque import Deque as deque
    #!!  collections.deque:not support slice:
    # dq[n:m]
    # TypeError: sequence index must be integer, not 'slice'
from itertools import islice, chain
from seed.tiny import null_iter


def echo_or_mk_IPeekableIterator(iterable):
    if not isinstance(iterable, IPeekableIterator):
        iterable = PeekableIterator(iterable)
    return iterable
def echo_or_mk_PeekableIterator(iterable):
    'avoid duplicate PeekableIterator; although the two cases are diff'
    if not isinstance(iterable, PeekableIterator):
        iterable = PeekableIterator(iterable)
    return iterable

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



















__all__
class IPeekableIterator(ABC):
    '''
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.iters.PeekableIterator:IPeekableIterator@T    =T   +exclude_attrs5listed_in_cls_doc
==>>:
new_abstract_methods:
    `__next__
    `len_relax
    `_fill_more_
    `_peek_relax_slice_
new_concrete_methods:
    __iter__
    peek_relax_slice
    peek_slice
    peek_le
    read_le
    drop_le
    peek_relax
    read_relax
    read_relax_le
    peek_relax_le
    is_empty
    len_lt
    len_ge
    fill_and_test
    fill_le
    read1
    peek1
    head
    '''#'''
    __slots__ = ()
    #no:__bool__
    @abstractmethod
    def __next__(self):
        # === read1()
        pass
    @abstractmethod
    def len_relax(self):
        'O(1); () -> UInt; len(self.peek_relax())'
    @abstractmethod
    def _fill_more_(self, n, *, to_return_news:bool):
        'not consume; [n>=1]'
        if not n >= 1: raise ValueError
    @abstractmethod
    def _peek_relax_slice_(self, n, m):
        'not consume; [0 <= n < m <= len_relax()] #no:_read_relax_slice_'
        if not 0 <= n < m <= self.len_relax(): raise ValueError(n, m, self.len_relax())



    def __iter__(self):
        return self

    def peek_relax_slice(self, n, m):
        'not consume; [n>=0][m>=0] #no:read_relax_slice'
        if not 0 <= n: raise ValueError(n)
        if not 0 <= m: raise ValueError(m)
        if not n < m:
            return ()
        m = min(m, self.len_relax())
        # [0 <= m <= len_relax()]
        if not n < m:
            return ()
        # [0 <= n < m <= len_relax()]
        return self._peek_relax_slice_(n, m)

    def peek_slice(self, n, m):
        'not consume; if len(result) < n, then self be empty after this call; [n>=0][m>=0] #no:read_slice'
        if not 0 <= n: raise ValueError(n)
        if not 0 <= m: raise ValueError(m)
        if not n < m:
            return ()
        # [0 <= n < m]

        self.fill_le(m)
        # [0 <= n < m <= len_relax()]or[len(self) < m]
        m = min(m, self.len_relax())
        # [0 <= m <= len_relax()]
        if not n < m:
            return ()
        # [0 <= n < m <= len_relax()]
        return self._peek_relax_slice_(n, m)
    #@abstractmethod
    def peek_le(self, n):
        'not consume; if len(result) < n, then self be empty after this call'
        if not n >= 0: raise ValueError
        return self.peek_slice(0, n)

    def read_le(self, n):
        'consume; if len(result) < n, then self be empty after this call'
        if not n >= 0: raise ValueError
        return tuple(islice(self, 0, n))
    def drop_le(self, n):
        if not n >= 0: raise ValueError
        for _ in islice(self, 0, n):pass
    def peek_relax(self):
        return self.peek_le(self.len_relax())

    def read_relax(self):
        return self.read_le(self.len_relax())
    def read_relax_le(self, n):
        if not n >= 0: raise ValueError
        return self.read_le(min(n, self.len_relax()))
    def peek_relax_le(self, n):
        if not n >= 0: raise ValueError
        return self.peek_le(min(n, self.len_relax()))
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
        return self.len_relax() >= n
    def fill_le(self, n):
        'not consume; like peek_le, but return None'
        if not n >= 0: raise ValueError
        sz = self.len_relax()
        if sz < n:
            #self.peek_le(n);return None
            self._fill_more_(n-sz, to_return_news=False)


    def read1(self):
        '-> x|^StopIteration'
        return next(self)
    def peek1(self):
        '-> x|^StopIteration'
        for x in self.peek_le(1):
            return x
        raise StopIteration
    @property
    def head(self):
        '-> x|^StopIteration'
        return self.peek1()


class PeekableIterator__over_PeekableIterator(IPeekableIterator):
    '(x->y) -> IPeekableIterator x -> IPeekableIterator y # fmap over the underlying IPeekableIterator'
    #xxx:'  #some op{fill_le/peek_le} will be O(len_relax) => dont let len_relax be big'
    #   !! ' #new algo{seed.types.Deque=>._peek_relax_slice_()}:O(n{delta}) as expected'
    ___no_slots_ok___ = True
    ######################
    #API:non-IPeekableIterator
    ######################
    def __init__(self, f, it, /):
        assert isinstance(it, IPeekableIterator)
        assert callable(f)
        self._f = f
            # :: x -> y
        self._it = it
            # :: IPeekableIterator x
        self._dq = deque()
            # :: deque y
    @property
    def the_peekable_iterator(self, /):
        return self._it

    def _detach3(self, /, *, to_list=False):
        'assume underlying is PeekableIterator not __class__'
        ys = self._dq
        (xs, it8tail) = self._it.detach()
            # !! PeekableIterator
        self._dq = deque()
        if to_list:
            ys = list(ys)
            xs = list(xs)
            it8tail = list(it8tail)
        return (ys, (xs, it8tail))

    ######################
    ######################
    #override:API:IPeekableIterator:abstractmethod
    ######################
    #no:__bool__
    @override
    def __next__(self):
        # === read1()
        dq = self._dq
        it = self._it
        x = next(it)
        y = dq.popleft() if dq else self._f(x)
        return y
    @override
    def _peek_relax_slice_(self, n, m):
        'not consume; [0 <= n < m <= len_relax()] #no:_read_relax_slice_'
        if not 0 <= n < m <= self.len_relax(): raise ValueError(n, m, self.len_relax())
        dq = self._dq
        return tuple(dq[n:m])
            #collections.deque:not support slice:
            #    TypeError: sequence index must be integer, not 'slice'

    @override
    def len_relax(self):
        'O(1); () -> UInt; len(self.peek_relax())'
        dq = self._dq
        sz = len(dq)
        return sz
    @override
    def _fill_more_(self, n, *, to_return_news:bool):
        # impl after:_peek_relax_slice_
        'not consume; [n>=1]'
        ' #new algo{seed.types.Deque=>._peek_relax_slice_()}:O(n{delta}) as expected'\
                ' #old algo{collections.deque}:!!!O(max(len_relax/2,n)) not O(n)!!!'
        if not n >= 1: raise ValueError
        dq = self._dq
        sz = len(dq)
        new_xs = self._it.peek_slice(sz, sz+n)
        new_ys = tuple(map(self._f, new_xs))
        dq.extend(new_ys)
        new_ys
        if to_return_news:
            return new_ys
    ######################
    #.@override
    #.def _fill_more_(self, n, *, to_return_news:bool):
    #.    # impl before:_peek_relax_slice_
    #.    'not consume; [n>=1]' \
    #.    ' #!!!O(len_relax+n) not O(n)!!!'
    #.    if not n >= 1: raise ValueError
    #.    dq = self._dq
    #.    sz = len(dq)
    #.    xs = self._it.peek_le(sz+n)
    #.    # !! [n > 0]
    #.    #bug:new_xs = xs[-n:]
    #.    new_xs = xs[sz:]
    #.    new_ys = tuple(map(self._f, new_xs))
    #.    dq.extend(new_ys)
    #.    new_ys
    #.    if to_return_news:
    #.        return new_ys
    #.
    #.@override
    #.def peek_le(self, n):
    #.    'not consume; if len(result) < n, then self be empty after this call'
    #.    if not n >= 0: raise ValueError
    #.    self.fill_le(n)
    #.    dq = self._dq
    #.    return tuple(islice(dq, 0, n))
    ######################

#end-class PeekableIterator__over_PeekableIterator(IPeekableIterator):


class PeekableIterator(IPeekableIterator):
    '' # see:below __doc__
    ___no_slots_ok___ = True
    ######################
    #API:non-IPeekableIterator
    ######################
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
    def tmp_peek_iter(self):
        '[unsafe][should ensure no other concurrent read/peek operation]'
        from seed.lang.nonbool import nonbool
        dq = self.__dq
        ################
        #del self.__dq
            # but:assign self.__it after self.__dq, would del self.__it firstly too?
        #self.__dq = NotImplemented
            # but:bool(NotImplemented) may be ok
        self.__dq = nonbool
        ###############
        return self._tmp_peek_iter(dq)
    def _tmp_peek_iter(self, dq):
        try:
            yield from dq
            for x in self.__it:
                dq.append(x)
                yield x
        finally:
            self.__dq = dq
        return
    ######################
    ######################
    ######################
    #override:API:IPeekableIterator:abstractmethod
    ######################
    @override
    def _fill_more_(self, n, *, to_return_news:bool):
        'not consume; [n>=1]'
        if not n >= 1: raise ValueError
        dq = self.__dq
        sz = len(dq)
        dq.extend(islice(self.__it, n))
        if to_return_news:
            return tuple(dq[sz:])
    @override
    def _peek_relax_slice_(self, n, m):
        'not consume; [0 <= n < m <= len_relax()] #no:_read_relax_slice_'
        if not 0 <= n < m <= self.len_relax(): raise ValueError(n, m, self.len_relax())
        dq = self.__dq
        return tuple(dq[n:m])
            #collections.deque:not support slice:
            #    TypeError: sequence index must be integer, not 'slice'
    @override
    def len_relax(self):
        'O(1); () -> UInt; len(self.peek_relax())'
        return len(self.__dq)
    @override
    def __next__(self):
        dq = self.__dq
        if dq:
            return dq.popleft()
        return next(self.__it)
    ######################
    #old ver:API:IPeekableIterator:non-abstractmethod
    ######################
    #.def __iter__(self):
    #.    return self
    #.def read_le(self, n):
    #.    'consume; if len(result) < n, then self be empty after this call'
    #.    if not n >= 0: raise ValueError
    #.    dq = self.__dq
    #.    if len(dq) < n:
    #.        #self.fill_le(n)
    #.        #r = tuple(dq)
    #.        #r = tuple(chain(dq, islice(self.__it, n-len(dq))))
    #.        r = (*dq, *islice(self.__it, n-len(dq)))
    #.        dq.clear()
    #.        assert len(r) <= n
    #.    else:
    #.        r = deque_popleftN(dq, n)
    #.        assert len(r) == n
    #.    return r
    #.    r = self.peek_le(n)
    #.    #del dq[:n] # n >= 0 # do not support
    #.    for _ in range(min(n, len(dq))): dq.popleft()
    #.    return r
    #.def peek_relax(self):
    #.    return tuple(self.__dq)

    #.def peek_le(self, n):
    #.    'not consume; if len(result) < n, then self be empty after this call'
    #.    if not n >= 0: raise ValueError
    #.    self.fill_le(n)

    #.    dq = self.__dq
    #.    r = deque_peekN(dq, n)
    #.    assert len(r) <= n
    #.    assert len(r) == n <= len(dq) or len(dq) == len(r) < n
    #.    return r

    #.def drop_le(self, n):
    #.    if not n >= 0: raise ValueError
    #.    dq = self.__dq
    #.    L = len(dq)
    #.    if n <= L:
    #.        deque_dropleftN(dq, n)
    #.        return
    #.    dq.clear()
    #.    #self.__it = islice(self.__it, n-L, None) # too deep
    #.    drop_strict(self.__it, n-L)
    #.    return None
    #.def read_relax(self):
    #.    r = self.peek_relax()
    #.    self.__dq.clear()
    #.    return r
    #.def read_relax_le(self, n):
    #.    if not n >= 0: raise ValueError
    #.    return deque_popleftN(self.__dq, n)
    #.def peek_relax_le(self, n):
    #.    if not n >= 0: raise ValueError
    #.    return deque_peekN(self.__dq, n)
    #.def is_empty(self):
    #.    return self.len_lt(1)
    #.def len_lt(self, n):
    #.    'O(n)*ops'
    #.    return not self.len_ge(n)
    #.def len_ge(self, n):
    #.    'O(n)*ops'
    #.    if n <= 0: return True
    #.    return self.fill_and_test(n)
    #.def fill_and_test(self, n=1):
    #.    'not consume; like fill_le, but return bool; test has at least n elements'
    #.    self.fill_le(n)
    #.    return len(self.__dq) >= n
    #.def fill_le(self, n):
    #.    'not consume; like peek_le, but return None'
    #.    if not n >= 0: raise ValueError
    #.    #if n <= 0: return
    #.    dq = self.__dq
    #.    if len(dq) < n:
    #.        dq.extend(islice(self.__it, n-len(dq)))
    #.    # assert len(dq) >= n or __it is empty
    #.    return None
    #.def read1(self):
    #.    # may raise StopIteration
    #.    return next(self)
    #.def peek1(self):
    #.    # may raise StopIteration
    #.    dq = self.__dq
    #.    if not dq:
    #.        dq.append(next(self.__it))
    #.    return dq[0]

    #.@property
    #.def head(self):
    #.    # may raise StopIteration
    #.    return self.peek1()
    ######################
#end-class PeekableIterator(IPeekableIterator):
PeekableIterator.__doc__ +=\
    r'''iterator with peek/read ops

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.iters.PeekableIterator:PeekableIterator@T    =T   -exclude_attrs5listed_in_cls_doc
==>>:
new_concrete_methods:
    ___no_slots_ok___
    chain_detach
    detach
    append_left
    __init__
    tmp_peek_iter
    _tmp_peek_iter
    _fill_more_
    _peek_relax_slice_
    len_relax
    __next__


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
    tmp_peek_iter
        '[unsafe][should ensure no other concurrent read/peek operation]'
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
'''#'''
PeekableIterator.__doc__

PeekableIterator__over_PeekableIterator.__doc__ +=\
    r'''

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.iters.PeekableIterator:PeekableIterator__over_PeekableIterator@T    =T   -exclude_attrs5listed_in_cls_doc
==>>:
new_concrete_methods:
    ___no_slots_ok___
    __init__
    the_peekable_iterator
    _detach3
    __next__
    _peek_relax_slice_
    len_relax
    _fill_more_


example:
    >>> it = PeekableIterator('123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)

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

    # no:detach
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)

    # [] + [0,1,2,3]
    >>> it.read_le(2)
    (0, 1)
    >>> it.head
    2

    # [2] + [3]
    >>> it._detach3(to_list=True)
    ([2], (['2'], ['3']))

    # no:append_left
    # no:chain_detach


    # fill_and_test
    >>> it = PeekableIterator(range(4))
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
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
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
    >>> it.fill_le(3)
    >>> it.peek_relax()
    (0, 1, 2)
    >>> it.fill_le(2)
    >>> it.peek_relax()
    (0, 1, 2)

    # drop_le
    >>> it = PeekableIterator(range(4))
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
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
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
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
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
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
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
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
    >>> it = PeekableIterator('0')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
    >>> it.is_empty()
    False
    >>> it = PeekableIterator(range(0))
    >>> it = PeekableIterator('')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
    >>> it.is_empty()
    True

    # len_relax
    >>> it = PeekableIterator(range(4))
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
    >>> it.len_relax()
    0
    >>> it.fill_le(3)
    >>> it.len_relax()
    3

    # read_relax
    >>> it = PeekableIterator(range(4))
    >>> it = PeekableIterator('0123')
    >>> it = PeekableIterator__over_PeekableIterator(int, it)
    >>> it.read_relax()
    ()
    >>> it.fill_le(2)
    >>> it.read_relax()
    (0, 1)


methods ordered:
    __next__
    #no:append_left
    #no:chain_detach
    #no:detach
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
    #no:tmp_peek_iter
        '[unsafe][should ensure no other concurrent read/peek operation]'
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
        #no:append_left
        #no:chain_detach
        #no:detach
        len_relax
        peek_relax
        read_relax

no __bool__
    since other iterator has no such usage, may cause bug
    use "self.len_ge(1)" instead
    use "not self.is_empty()" instead
'''#'''
PeekableIterator__over_PeekableIterator.__doc__


#.r"""
#.class IterableReserveLastElement:
#.    '''should access the last element via self.head not iter'''
#.    @classmethod
#.    def may_from_nonempty_iterable(cls, iterable):
#.        # -> (cls|None)
#.        it = iter(iterable)
#.        for head in it:
#.            return cls(head, it)
#.        return None
#.    @classmethod
#.    def from_nonempty_iterable(cls, iterable):
#.        # -> (cls|raise StopIteration)
#.        it = iter(iterable)
#.        return cls(next(it), it)
#.        for head in it:
#.            return cls(head, it)
#.        raise StopIteration('should not input an empty iterable')
#.
#.    def __init__(self, head, iterable):
#.        self.head = head
#.        self.iterator = iter(iterable)
#.    def __next__(self):
#.        self.head, r = next(self.iterator), self.head
#.        # will not return last element
#.        return r
#.    def iter_without_last_element(self):
#.        # will not yield last element
#.        maylast = self.head
#.        # if maylast indeed is last element, then not be yield
#.        for self.head in self.iterator:
#.            # store MUST before yield
#.            yield maylast
#.            maylast = self.head
#.
#.    def iter_with_last_element(self):
#.        # will yield last element
#.        yield from self.iter_without_last_element()
#.        yield self.head
#.    def __iter__(self):
#.        # will yield last element
#.        return self.iter_with_last_element()
#.
#.#"""
__doc__
if __name__ == "__main__":
    print('\n'.join(s for s in dir(PeekableIterator) if not s.startswith('_')))
    import doctest
    doctest.testmod()


#.echo_or_mk_PeekableIterator = lazy_import4func_('seed.iters.PeekableIterator', 'echo_or_mk_PeekableIterator', __name__)
from seed.iters.PeekableIterator import PeekableIterator, echo_or_mk_PeekableIterator
from seed.iters.PeekableIterator import *
