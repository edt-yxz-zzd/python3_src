
__all__ = '''
    PyTerminalSetOps
    the_py_terminal_set_ops
    '''.split()

from seed.abc.Ops.IOps import IOps
from .abc import override
from .ITerminalSetOps import ITerminalSetOps

class PyTerminalSetOps(ITerminalSetOps, IOps):
    __slots__ = ()
    # terminal_set_ops for python.set
    @override
    def is_empty(ops, self):
        return not self
    @override
    def is_disjoint(ops, self, other):
        return self.isdisjoint(other)
    @override
    def contains(ops, self, element):
        return element in self
    @override
    def intersection(ops, self, other):
        return self & other
    @override
    def union(ops, self, other):
        return self | other

    @override
    def get_args_for_eq_hash(ops):
        return ()
    def __repr__(self):
        return '{}()'.format(type(self).__name__)

the_py_terminal_set_ops = PyTerminalSetOps()
