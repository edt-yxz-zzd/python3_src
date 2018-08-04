

__all__ = '''
    IBlockDictOps__imodify
    '''.split()

#from ..OtherOps.IEqOps import IEqOps
#from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
#from .IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase
#from .IBlockDictOps import IBlockDictOps
from .IBlockDictOps__constructor import IBlockDictOps__constructor

from .abc import not_implemented, abstractmethod, override
#from seed.tiny import fst, snd
#from collections.abc import MutableMapping



def make_ipop():
    Nothing = object()
    def ipop(ops, self, dict_key, default=Nothing):
        # -> ((dict_value|default), new_self) | raise KeyError
        block_items, new_self = ops.ipop_block_items_of_dict_key(self, dict_key)
        if not block_items:
            if default is Nothing:
                raise KeyError(dict_key)
            return default, new_self

        [block_item] = block_items
        block_key, dict_value = block_item
        return dict_value, new_self
    return ipop













class IBlockDictOps__imodify(IBlockDictOps__constructor):
    '''
IBlockDictOps__imodify:
    not (MutableMapping)
    since no __len__/__iter__
        # hence no keys/items/values/popitem

see:
    IBlockDictOps__blind_update
testing:
    BlockDict__ops_biased
'''
    __slots__ = ()

    @not_implemented
    def iset_block_item(ops, self, block_key, dict_value):
        # -> new_self
        # block_key maybe empty
        #
        # if block_key overlap or touch input_block_key
        #   and dict_value_eq(self[block_key], dict_value):
        #   then merge the two ranges/block_keys
        ...

    @not_implemented
    def ipop_block_items_of_block_key(ops, self, block_key, *, reverse=False):
        # -> ([block_item], new_self)
        #
        # block_key maybe empty
        #
        # -> ([block_item], new_self)
        #   not Iter block_item
        ...
    @abstractmethod
    def idiscard_block_key(ops, self, block_key):
        # -> new_self
        # block_key maybe empty
        #
        _, new_self = ops.ipop_block_items_of_block_key(self, block_key)
        return new_self

    @not_implemented
    def ipop_left_or_right_block_item(ops, self, right:bool):
        # -> (block_item, new_self) | raise KeyError
        ...

    @not_implemented
    def iclear(ops, self):
        # -> new_self
        ...

    '''
    @not_implemented
    def swap(ops, self, other):
        # -> new_self
        #since using same ops
        #assert type(self) is type(other)
        ...
    def assign(ops, self, other):
        # old version
        other = ops.copy_block_dict(other)
        ops.swap(self, other)
    '''

    @abstractmethod
    def iassign(ops, self, other):
        # -> new_self
        return ops.copy(other)



    def ipop_left_block_item(ops, self):
        # -> (block_item, new_self) | raise KeyError
        return ops.ipop_left_or_right_block_item(self, False)
    def ipop_right_block_item(ops, self):
        # -> (block_item, new_self) | raise KeyError
        return ops.ipop_left_or_right_block_item(self, True)
    def ipop_block_item(ops, self):
        # -> (block_item, new_self) | raise KeyError
        # no popitem
        return ops.ipop_right_block_item(self)



    def ipop_block_items_of_dict_key(ops, self, dict_key):
        # -> ([block_item], new_self) | raise KeyError
        block_key = ops.mkSingletonRange(dict_key)
        return ops.ipop_block_items_of_block_key(self, block_key)
    def ipop_block_item_of_dict_key(ops, self, dict_key):
        # -> (block_item, new_self) | raise KeyError
        block_items, new_self = ops.ipop_block_items_of_dict_key(self, dict_key)
        if not block_items:
            raise KeyError(dict_key)
        [block_item] = block_items
        return block_item, new_self

    def iupdate_from_items(ops, self, items):
        # -> new_self
        iset_item = ops.iset_item
        for dict_key, dict_value in items:
            self = iset_item(self, dict_key, dict_value)
        return self
    def iupdate_from_block_items(ops, self, block_items):
        # -> new_self
        iset_block_item = ops.iset_block_item
        for block_key, dict_value in block_items:
            self = iset_block_item(self, block_key, dict_value)
        return self

    def iset_dict_key2default(ops, self, dict_key, dict_key2default):
        # -> (dict_value, new_self)
        #
        # dict_key2default :: dict_key->dict_value
        # dict_value may not allow to be None
        #   so, we donot allow (dict_key2default=None)

        new_self = self
        def _dict_key2default(dict_key):
            # not exists
            nonlocal new_self

            default = dict_key2default(dict_key)
            new_self = ops.iset_item(self, dict_key, default)
            return default

        dict_value = ops.dict_key2dict_value(self, dict_key
                    , dict_key2default=_dict_key2default)
        return dict_value, new_self

    def iset_fdefault(ops, self, dict_key, fdefault):
        # -> (dict_value, new_self)
        #
        # dict_value may not allow to be None
        #   so, we donot allow (fdefault=None)
        def dict_key2default(dict_key):
            return fdefault()
        return ops.iset_dict_key2default(self, dict_key, dict_key2default)



    # __setitem__
    def iset_item(ops, self, dict_key, dict_value):
        # -> new_self
        block_key = ops.mkSingletonRange(dict_key)
        return ops.iset_block_item(self, block_key, dict_value)
    # __delitem__
    def idel_item(ops, self, dict_key):
        # -> new_self | raise KeyError
        _, new_self = ops.ipop_block_item_of_dict_key(self, dict_key)
        return new_self

    ipop = make_ipop()

    def iupdate(ops, self, other_or_items):
        # -> new_self
        if not isinstance(other_or_items, __class__):
            items = other_or_items
            return ops.iupdate_from_items(self, items)

        other = other_or_items

        #since using same ops
        #if self.block_dict_key_ops != other.block_dict_key_ops: raise TypeError
        #if other.eq_dict_value_ops != self.eq_dict_value_ops: return TypeError

        block_items = ops.iter_block_items(other)
        return ops.iupdate_from_block_items(self, block_items)
    def isetdefault(ops, self, dict_key, default):
        # -> (dict_value, new_self)
        #
        # None may not be valid dict_value, so, no (default=None)
        return ops.iset_fdefault(self, dict_key, lambda:default)

    @override
    def make_block_dict_from_items(ops, items):
        self = ops.make_empty_block_dict()
        return ops.iupdate_from_items(self, items)
    @override
    def make_block_dict_from_block_items(ops, block_items):
        self = ops.make_empty_block_dict()
        return ops.iupdate_from_block_items(self, block_items)

if __name__ == '__main__':
    XXX = IBlockDictOps__imodify

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)



