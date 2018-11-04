from .BoxUnbox import BoxUnbox
from ..IOps.IMutableSetOps__alternative_name_mutable_set_ops import \
    IMutableSetOps__alternative_name_mutable_set_ops
class MutableSetOps__alternative_name_mutable_set_ops(BoxUnbox, IMutableSetOps__alternative_name_mutable_set_ops):
    def __init__(ops, *, unbox, box):
        super().__init__(unbox=unbox, box=box)
    def static_make_empty_set(ops):
        return ops.box(set())
    def add(ops, self, element):
        ops.unbox(self).add(element)

