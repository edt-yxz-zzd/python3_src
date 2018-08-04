

__all__ = '''
    BlockSet
    '''.split()

#from collections.abc import Set, MutableSet
from .abc import override
from ..app.BlockDict import BlockDict
from ..BlockSet.IBlockSet__mutable import IBlockSet__mutable
from seed.helper.repr_input import repr_helper
from seed.tiny import fst
from seed.tiny import null_iter

def map_fst(iterable):
    return map(fst, iterable)
def with_None(iterable):
    return ((x, None) for x in iterable)




class BlockSet(IBlockSet__mutable):
    '''

to override:
        `_get_block_dict_key_ops_
        `add_block_key
        `clear
        `copy
        `discard_block_key
        `get_num_block_keys
        `iter_all_touch_or_overlap_block_keys
        `iter_block_keys
        `pop_block_keys_of_block_key
        `pop_left_or_right_block_key
        `self_make_empty_block_set
        `swap
'''
    __slots__ = ['_d']
    def __init__(self
            , block_dict_key_ops
            , iterable=None, *
            , is_block_keys=False):
        if iterable is None:
            iterable = null_iter

        self._d = BlockDict(block_dict_key_ops, None
                    , with_None(iterable), is_block_items=is_block_keys)

    def __repr__(self):
        block_dict_key_ops = self.block_dict_key_ops

        kwargs = {}
        if self:
            kwargs['is_block_keys'] = True
            args = ([*self.iter_block_keys()],)
        else:
            args = ()
        return repr_helper(self, block_dict_key_ops
                        , *args, **kwargs)

    @override
    def _get_block_dict_key_ops_(self):
        return self._d.block_dict_key_ops
    @override
    def copy(self):
        other = self.self_make_empty_block_set()
        other._d.assign(self._d)
        #bug: forgor return other
        return other

    @override
    def get_num_block_keys(self):
        return self._d.get_num_block_keys()
    @override
    def iter_block_keys(self, *, reverse=False):
        return self._d.iter_block_keys(reverse=reverse)
    @override
    def _index_block_key_at_(self, i:'UInt'):
        return self._d._index_block_item_at_(i)[0]



    @override
    def self_make_block_set_from_block_keys(self, block_keys):
        return __class__(self.block_dict_key_ops, block_keys, is_block_keys=True)
    @override
    def self_make_block_set_from_dict_keys(self, dict_keys):
        return __class__(self.block_dict_key_ops, dict_keys)
    @override
    def self_make_empty_block_set(self):
        return type(self).make_empty_block_set(self.block_dict_key_ops)
    @classmethod
    def make_empty_block_set(cls, block_dict_key_ops):
        return __class__(block_dict_key_ops)


    @override
    def iter_all_touch_or_overlap_block_keys(self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        return map_fst(self._d.iter_all_touch_or_overlap_block_items(
                    block_key, overlap_only, reverse=reverse))


    @override
    def add_block_key(self, block_key):
        # if block_key overlap or touch input_block_key
        #   then merge the two ranges/block_keys
        self._d.set_block_item(block_key, None)

    @override
    def pop_block_keys_of_block_key(self, block_key, *, reverse=False):
        # -> [block_key]
        #   not Iter block_key
        pairs = self._d.pop_block_items_of_block_key(block_key, reverse=reverse)
        return [*map_fst(pairs)]
    @override
    def discard_block_key(self, block_key):
        self._d.discard_block_key(block_key)

    @override
    def pop_left_or_right_block_key(self, right:bool):
        return self._d.pop_left_or_right_block_item(right)[0]

    @override
    def clear(self):
        self._d.clear()

    @override
    def swap(self, other):
        if self is other: return
        if not isinstance(other, __class__): raise TypeError
        if self.block_dict_key_ops != other.block_dict_key_ops: raise TypeError
        self._d.swap(other._d)



if __name__ == '__main__':
    XXX = BlockSet

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)



