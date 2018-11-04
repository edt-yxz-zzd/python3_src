from .BoxUnbox import BoxUnbox
from ..IOps.IFullMappingOps__XXX_name_fullmapping_ops import \
    IFullMappingOps__XXX_name_fullmapping_ops
class FullMappingOps__mapping__XXX_name_fullmapping_ops(
    BoxUnbox, IFullMappingOps__XXX_name_fullmapping_ops):
    def __init__(ops, keys, *, items2mapping, unbox, box):
        ops.__keys = frozenset(keys)
        ops.__items2mapping = items2mapping
        super().__init__(unbox=unbox, box=box)
    def static_make_fullmapping_from_key2value(ops, key2value):
        return ops.box(ops.__items2mapping(
            (k, key2value(k)) for k in ops.static_iter_keys()))
    def static_iter_keys(ops):
        return iter(ops.__keys)
    def static_contains_key(ops, key):
        return key in ops.__keys
    def key2value(ops, self, key):
        return ops.unbox(self)[key]


