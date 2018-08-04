
'''
bijection between FrozenDict(k0,v0) and FrozenDict(k1,v1)
    bijection(FD) = bijection(k0<->k1) + bijection(v0<->v1)
    if v0(k0), see: RecordTV
'''
from .import_FrozenDict import FrozenDict


class DictTV(...):
    def __init__(self, KeyType, ValueType, min_len=0, max_len=None):
