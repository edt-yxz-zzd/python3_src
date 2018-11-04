


'''
biased-binop???
    but negable set donot support
    value set not object set
'''

__all__ = '''
    ISetOps__iunion
    ISetOps__union

    ISetOps__iintersection
    ISetOps__intersection

    ISetOps__idifference
    ISetOps__difference

    ISetOps__isymmetric_difference
    ISetOps__symmetric_difference

    ISetOps__iupdates
    ISetOps__binary_operaters
    '''.split()

from .abc import not_implemented, define, override
from .ISetOps import ISetOps

class ISetOps__iunion(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def iunion(ops, self, other):
        # return modify self and return self
        #       or make a new immutable/mutable set and return it
        pass

class ISetOps__union(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def union(ops, self, other):
        # make a new immutable/mutable set and return it
        pass

class ISetOps__iintersection(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def iintersection(ops, self, other):
        # return modify self and return self
        #       or make a new immutable/mutable set and return it
        pass


class ISetOps__intersection(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def intersection(ops, self, other):
        # make a new immutable/mutable set and return it
        pass


class ISetOps__idifference(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def idifference(ops, self, other):
        # return modify self and return self
        #       or make a new immutable/mutable set and return it
        pass

class ISetOps__difference(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def difference(ops, self, other):
        # make a new immutable/mutable set and return it
        pass


class ISetOps__isymmetric_difference(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def isymmetric_difference(ops, self, other):
        # return modify self and return self
        #       or make a new immutable/mutable set and return it
        pass

class ISetOps__symmetric_difference(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def symmetric_difference(ops, self, other):
        # make a new immutable/mutable set and return it
        pass

class ISetOps__binary_operaters(
    ISetOps__symmetric_difference
    , ISetOps__difference
    , ISetOps__intersection
    , ISetOps__union
    ):
    @override
    def intersection(ops, self, other):
        return ops.difference(self, ops.difference(self, other))
    @override
    def symmetric_difference(ops, self, other):
        return ops.union(ops.difference(other, self), ops.difference(self, other))

class ISetOps__iupdates(
    ISetOps__isymmetric_difference
    , ISetOps__idifference
    , ISetOps__iintersection
    , ISetOps__iunion
    ):
    # can not impl iintersection/isymmetric_difference
    pass




