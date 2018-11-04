
from .BoxUnbox import Unbox
from ..IOps.ISetOps__alternative_name_set_ops import \
    ISetOps__alternative_name_set_ops
class SetOps__alternative_name_set_ops(Unbox, ISetOps__alternative_name_set_ops):
    def __init__(ops, *, unbox):
        super().__init__(unbox=unbox)
    def iter(ops, self):
        return iter(ops.unbox(self))

