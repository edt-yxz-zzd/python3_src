
from seed.abc.Ops.IDisplayerOps import IDisplayerOps
from .abc import override
class DisplayerOps4py_repr(IDisplayerOps):
    'show py_repr'
    __slots__ = ()
    @override
    def display(ops, x, /):
        '-> x -> str'
        return repr(x)
class DisplayerOps4py_str(IDisplayerOps):
    'show py_str'
    __slots__ = ()
    @override
    def display(ops, x, /):
        '-> x -> str'
        return str(x)


displayer_ops4py_repr = DisplayerOps4py_repr()
displayer_ops4py_str = DisplayerOps4py_str()

from seed.abc.Ops__concrete.DisplayerOps import DisplayerOps4py_repr, DisplayerOps4py_str
from seed.abc.Ops__concrete.DisplayerOps import displayer_ops4py_repr, displayer_ops4py_str
