from .abc import ABC, abstractmethod
class IFullMappingOps__XXX_name_fullmapping_ops(ABC):
    # alternative_name_fullmapping_ops
    # rule_name_fullmapping_ops
    def static_make_fullmapping_from_fdefault(ops, fdefault):
        key2value = lambda key: fdefault()
        return ops.static_make_fullmapping_from_key2value(key2value)
    @abstractmethod
    def static_make_fullmapping_from_key2value(ops, key2value):
        pass

    @abstractmethod
    def static_iter_keys(ops):
        pass
    @abstractmethod
    def static_contains_key(ops, key):
        pass
    @abstractmethod
    def key2value(ops, self, key):
        pass
    def iter_values(ops, self):
        return (ops.key2value(self, k) for k in ops.static_iter_keys())
    def iter_items(ops, self):
        return ((k, ops.key2value(self, k)) for k in ops.static_iter_keys())



