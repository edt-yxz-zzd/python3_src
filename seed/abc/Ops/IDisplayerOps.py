
from .abc import not_implemented, ABC
class IDisplayerOps(ABC):
    __slots__ = ()
    @not_implemented
    def display(ops, x, /):
        '-> x -> str'

from seed.abc.Ops.IDisplayerOps import IDisplayerOps
