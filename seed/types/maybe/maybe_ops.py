

'''

example:
    >>> ops = theNoneTupleBasedMaybeOps
    >>> assert ops.Nothing() is None
    >>> assert ops.Just(1) == (1,)

    >>> nul = ops.Nothing()
    >>> just1 = ops.Just(1)
    >>> just4 = ops.Maybe([4])

    >>> assert ops.is_Nothing(nul)
    >>> assert not ops.is_Just(nul)
    >>> assert not ops.is_Nothing(just1)
    >>> assert ops.is_Just(just1)
    >>> ops.len(nul)
    0
    >>> ops.len(just4)
    1

    >>> assert ops.maybe_eq(nul, nul)
    >>> assert not ops.maybe_eq(nul, just1)
    >>> assert ops.maybe_eq(just1, just1)
    >>> assert not ops.maybe_eq(just1, just4)

    >>> assert 1 == ops.unjust(just1)
    >>> assert 3 == ops.unjust(nul, lambda:3)
    >>> assert 3 == ops.maybe(nul, lambda x: error, 3)
    >>> assert 2 == ops.unjust(ops.fmap(just1, lambda x:x+1))
    >>> assert ops.is_Nothing(ops.fmap(nul, lambda x:x+1))
    >>> assert [1] == list(ops.iter(just1))
    >>> assert [1] == list(ops.chain(nul, just1))
    >>> assert [1,4] == list(ops.chains([nul, just1, just4]))

    >>> assert ops.to_TupleBasedMaybe(nul) == ()
    >>> assert ops.to_NoneTupleBasedMaybe(nul) is None
    >>> assert ops.to_NoneBasedIncompleteMaybe(nul) is None
    >>> assert ops.to_TupleBasedMaybe(just1) == (1,)
    >>> assert ops.to_NoneTupleBasedMaybe(just1) == (1,)
    >>> assert ops.to_NoneBasedIncompleteMaybe(just1) == 1
'''

__all__ = '''
    theMaybeOps
    theTupleBasedMaybeOps
    theNoneTupleBasedMaybeOps
    theNoneBasedIncompleteMaybeOps

IMaybeOps
    IMaybeOps__Complete
        IMaybeOps__JustIsCollection__FaultNothing
            ICollectionBasedMaybeOps
                TheMaybeOps
                    theMaybeOps
                TupleBasedMaybeOps
                    theTupleBasedMaybeOps
            IMaybeOps__JustIsCollection__NothingIsNone
                NoneTupleBasedMaybeOps
                    theNoneTupleBasedMaybeOps
    IMaybeOps__NothingIsNone
        IMaybeOps__JustIsCollection__NothingIsNone
        NoneBasedIncompleteMaybeOps
            theNoneBasedIncompleteMaybeOps
    '''.split()

from abc import ABC, abstractmethod
from itertools import chain
from ..to_container import is_reiterable, iter_adj2, seq_adj2
from . import Maybe as M


########## to export #############
#   the_empty_tuple, null_iter, echo, lazy, iter_adj2, seq_adj2
the_empty_tuple = ()
null_iter = iter('')
echo = lambda x:x
lazy = lambda obj: lambda:obj


def may_fdefault_fException2fdefault(may_fdefault, fException):
    # may_fdefault :: None | (() -> default)
    # fException :: () -> Exception
    # fdefault :: () -> default
    if may_fdefault is None:
        return may_fdefault
    return fException2fdefault(fException)
def fException2fdefault(fException):
    # fException :: () -> Exception
    # fdefault :: () -> default
    def fdefault():
        raise fException()
    return fdefault
#############################









###################

class IMaybeOps(ABC):
    '''maybe ops

abstractmethod:
    Just
    Nothing
    is_Nothing
    bare_iter_just
maybe overrided:
    bare_unjust
    is_Just
    iter
    Maybe

    '''
    __slots__ = ()

    @abstractmethod
    def Just(self, x):
        raise NotImplementedError

    @abstractmethod
    def Nothing(self):
        raise NotImplementedError

    @abstractmethod
    def is_Maybe(self, obj):
        'is_Nothing is under assumtion is_Maybe'
        raise NotImplementedError
    @abstractmethod
    def is_Nothing(self, m):
        'assume m is Maybe'
        raise NotImplementedError
        return not m
    @abstractmethod
    def bare_iter_just(self, j):
        # j is not Nothing
        # unsafe
        raise NotImplementedError
        return iter(j)

    ######## maybe overrided

    def bare_unjust(self, j):
        # j is not Nothing
        # unsafe
        [x] = self.bare_iter_just(j)
        return x

    def iter(self, m):
        if self.is_Nothing(m):
            return null_iter
        return self.bare_iter_just(m)

    def is_Just(self, m):
        'assume m is Maybe'
        return not self.is_Nothing(m)

    def maybe_payload_eq(self, x, y):
        return x == y
    def bare_justs_all_eq(self, justs, eq=None):
        unjust = self.bare_unjust
        d = {id(j): unjust(j) for j in justs} # is...
        if len(d) < 2: return True

        if eq is None:
            eq = self.maybe_payload_eq
        payloads = d.values()
        return all(map(eq, iter_adj2(payloads)))

    def maybes_all_eq(self, maybes, eq=None):
        isN = self.is_Nothing
        def to_bool(maybe):
            return bool(isN(maybe))
        def bool_eq(b,b2): return b is b2
        # all Nothing or all Just
        if is_reiterable(maybes):
            if not all(map(bool_eq, iter_adj2(map(to_bool, maybes)))):
                return False
            for h in maybes:
                if isN(h):
                    # all Nothing
                    return True
                break
            else:
                return True
            # all Just
            return self.bare_justs_all_eq(maybes, eq)

        if eq is None:
            eq = self.maybe_payload_eq
        f = self.maybe_eq
        return all(f(maybe0, maybe1, eq) for maybe0, maybe1 in iter_adj2(maybes))

    def maybe_eq(self, maybe0, maybe1, eq=None):
        if maybe0 is maybe1:
            return True

        if self.is_Nothing(maybe0):
            return self.is_Nothing(maybe1)
        if not self.is_Just(maybe1):
            return False
        # both justs
        x = self.bare_unjust(maybe0)
        y = self.bare_unjust(maybe1)
        if eq is None:
            eq = self.maybe_payload_eq

        return eq(x, y)

    def to_another_maybe(self, m, other_ops):
        return other_ops.Maybe(self.iter(m))
    def to_TupleBasedMaybe(self, m):
        return self.to_another_maybe(m, theTupleBasedMaybeOps)
    def to_NoneTupleBasedMaybe(self, m):
        return self.to_another_maybe(m, theNoneTupleBasedMaybeOps)
    def to_NoneBasedIncompleteMaybe(self, m):
        return self.to_another_maybe(m, theNoneBasedIncompleteMaybeOps)



    ################
    def len(self, maybe):
        return int(self.is_Just(maybe))
    def chain(self, *maybes):
        return self.chains(maybes)
    def chains(self, maybes):
        justs = filter(self.is_Just, maybes)
        return chain.from_iterable(map(self.bare_iter_just, justs))
    def fmap(self, m, f):
        if self.is_Nothing(m):
            return m
        return self.Just(f(self.bare_unjust(m)))
        return self.lazy_maybe(m, lambda x: self.Just(f(x)), lambda:self.Nothing())
        return self.Maybe(map(f, self.iter(m)))


    def maybe(self, m, v2r, default=None):
        return self.lazy_maybe(m, v2r, lazy(default))
    def maybeError(self, m, v2r, Exception):
        return self.lazy_maybeError(m, v2r, lazy(Exception))
    def lazy_maybeError(self, m, v2r, fException):
        return self.lazy_maybe(m, v2r, fException2fdefault(fException))
    def lazy_maybe(self, m, v2r, fdefault):
        if self.is_Nothing(m):
            return fdefault()
        return v2r(self.bare_unjust(m))



    def unjust_or_Error(self, j, fException):
        return self.unjust(j, fException2fdefault(fException))
    def unjust(self, j, fdefault = None):
        # why not default?
        #   unjust except Just instead of Maybe
        #   so, Nothing case should be rare
        if fdefault is None:
            return self.lazy_maybeError(j, echo
                    , lambda:ValueError('unjust Nothing'))
        return self.lazy_maybe(j, echo, fdefault)

    def Maybe(self, iterable):
        # constructor
        it = iter(iterable)
        for head in it:
            break
        else:
            return self.Nothing()
        for _ in it: raise TypeError('too many args')
        return self.Just(head)






##############
class IMaybeOps__Complete(IMaybeOps):
    'maybe is complete; e.g. Just can hold any object'
    __slots__ = ()
class IMaybeOps__JustIsCollection__FaultNothing(IMaybeOps__Complete):
    '''Just is a collection; bool(Nothing) == False

abstractmethod:
    Nothing
maybe overrided:
    Just
    iter
'''
    __slots__ = ()
    def Just(self, x):
        return (x,)
    def is_Nothing(self, m):
        return not m
    def bare_iter_just(self, m):
        return iter(m)

class ICollectionBasedMaybeOps(IMaybeOps__JustIsCollection__FaultNothing):
    'Nothing is empty collection'
    def Nothing(self):
        return the_empty_tuple
    def iter(self, m):
        return iter(m)
class TheMaybeOps(ICollectionBasedMaybeOps):
    '''see: .Maybe.Maybe'''
    def is_Maybe(self, obj):
        return M.is_Maybe(obj)
    def Just(self, x):
        return M.Just(x)
    def Nothing(self):
        return M.Nothing
    def bare_iter_just(self, m):
        return iter(m)
    def bare_unjust(self, m):
        return M.unjust(m)
    def iter(self, m):
        return iter(m)
    def Maybe(self, iterable):
        return M.Maybe(iterable)
theMaybeOps = TheMaybeOps()

class TupleBasedMaybeOps(ICollectionBasedMaybeOps):
    def Maybe(self, iterable):
        m = tuple(iterable)
        if len(m) > 1: raise TypeError('too many args')
        return m
    def is_Maybe(self, obj):
        return type(x) is tuple and len(x) < 2
    def Nothing(self):
        return the_empty_tuple
    def Just(self, x):
        return (x,)
    def to_TupleBasedMaybe(self, m):
        return m
    pass
theTupleBasedMaybeOps = TupleBasedMaybeOps()


class IMaybeOps__NothingIsNone(IMaybeOps):
    '''Nothing is None; bool(Just) maybe False!!

abstractmethod:
    Just
    bare_iter_just
maybe overrided:
    bare_unjust
    is_Just
    iter
'''
    def is_Nothing(self, m):
        return m is None
    def Nothing(self):
        return None
    def is_Just(self, m):
        return m is not None
class IMaybeOps__JustIsCollection__NothingIsNone(
            IMaybeOps__NothingIsNone
            , IMaybeOps__JustIsCollection__FaultNothing
            ):
    '''

abstractmethod:
    Just
maybe overrided:
    iter
'''
    def is_Just(self, m):
        return bool(m)
    def bare_iter_just(self, m):
        return iter(m)

    # redefine here
    def is_Nothing(self, m):
        return m is None
    def Nothing(self):
        return None
class NoneTupleBasedMaybeOps(IMaybeOps__JustIsCollection__NothingIsNone):
    'None | (x,)'
    def is_Maybe(self, obj):
        return obj is None or type(x) is tuple and len(x) == 1
    def Just(self, x):
        return (x,)
    def to_NoneTupleBasedMaybe(self, m):
        return m
theNoneTupleBasedMaybeOps = NoneTupleBasedMaybeOps()

class NoneBasedIncompleteMaybeOps(IMaybeOps__NothingIsNone):
    '(None | not None); incomplete; Just cannot hold None'
    def is_Maybe(self, obj):
        return True
    def Just(self, x):
        if x is None: raise TypeError('NoneBasedMaybe cannot (Just None)')
        return x
    def bare_iter_just(self, j):
        yield j
    def bare_unjust(self, m):
        return m
    def iter(self, m):
        if m is None: return
        yield m
    def to_NoneBasedIncompleteMaybe(self, m):
        return m
theNoneBasedIncompleteMaybeOps = NoneBasedIncompleteMaybeOps()



def _t():
    opss = [theMaybeOps, theTupleBasedMaybeOps, theNoneTupleBasedMaybeOps, theNoneBasedIncompleteMaybeOps]
    for ops in opss:
        _t1(ops)
def _t1(ops):
    nul = ops.Nothing()
    just1 = ops.Just(1)
    just4 = ops.Maybe([4])

    assert ops.is_Nothing(nul)
    assert not ops.is_Just(nul)
    assert not ops.is_Nothing(just1)
    assert ops.is_Just(just1)
    assert ops.len(nul) == 0
    assert ops.len(just4) == 1

    assert ops.maybe_eq(nul, nul)
    assert not ops.maybe_eq(nul, just1)
    assert ops.maybe_eq(just1, just1)
    assert not ops.maybe_eq(just1, just4)

    assert 1 == ops.unjust(just1)
    assert 3 == ops.unjust(nul, lambda:3)
    assert 3 == ops.maybe(nul, lambda x: error, 3)
    assert 2 == ops.unjust(ops.fmap(just1, lambda x:x+1))
    assert ops.is_Nothing(ops.fmap(nul, lambda x:x+1))
    assert [1] == list(ops.iter(just1))
    assert [1] == list(ops.chain(nul, just1))
    assert [1,4] == list(ops.chains([nul, just1, just4]))

    assert ops.to_TupleBasedMaybe(nul) == ()
    assert ops.to_NoneTupleBasedMaybe(nul) is None
    assert ops.to_NoneBasedIncompleteMaybe(nul) is None
    assert ops.to_TupleBasedMaybe(just1) == (1,)
    assert ops.to_NoneTupleBasedMaybe(just1) == (1,)
    assert ops.to_NoneBasedIncompleteMaybe(just1) == 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    _t()

