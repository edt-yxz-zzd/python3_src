
from .BoxUnbox import BoxUnbox
from ..IOps.IFullMappingOps__XXX_name_fullmapping_ops import \
    IFullMappingOps__XXX_name_fullmapping_ops
class FullMappingOps__sequence__XXX_name_fullmapping_ops(
    BoxUnbox, IFullMappingOps__XXX_name_fullmapping_ops):
    def __init__(ops, length, *, iterable2sequence, unbox, box):
        ops.__size = length
        ops.__iterable2sequence = iterable2sequence
        super().__init__(unbox=unbox, box=box)
    def static_make_fullmapping_from_key2value(ops, key2value):
        return ops.box(ops.__iterable2sequence(
            map(key2value, ops.static_iter_keys())))
    def static_iter_keys(ops):
        return iter(range(ops.__size))
    def static_contains_key(ops, key):
        return 0 <= key < ops.__size
    def key2value(ops, self, key):
        return ops.unbox(self)[key]


