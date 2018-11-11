
__all__ = '''
    PyTerminalSetOps__with_any
    TheAnySet
    the_py_terminal_set_ops__with_any
    '''.split()

from seed.abc.Ops.IOps import IOps
from .abc import override
from .ITerminalSetOps import ITerminalSetOps

class TheAnySet:
    #use TheAnySet directly
    # donot use instance
    # assume TheAnySet is not empty
    pass
assert TheAnySet

class PyTerminalSetOps__with_any(ITerminalSetOps, IOps):
    __slots__ = ()
    # terminal_set_ops for python.set and TheAnySet
    @override
    def is_empty(ops, self):
        # assume TheAnySet is not empty
        return not self

    @override
    def is_disjoint(ops, self, other):
        if self is TheAnySet:
            return ops.is_empty(other)
        if other is TheAnySet:
            return ops.is_empty(self)
        return self.isdisjoint(other)
    @override
    def contains(ops, self, element):
        if self is TheAnySet: return True
        return element in self
    @override
    def intersection(ops, self, other):
        if self is TheAnySet:
            if other is TheAnySet:
                return TheAnySet
            return set(other)
        if other is TheAnySet:
            return set(self)
        return self & other
    @override
    def union(ops, self, other):
        if self is TheAnySet:
            return TheAnySet
        if other is TheAnySet:
            return TheAnySet
        return self | other

    @override
    def get_args_for_eq_hash(ops):
        return ()
    def __repr__(ops):
        return '{}()'.format(type(ops).__name__)

the_py_terminal_set_ops__with_any = PyTerminalSetOps__with_any()


