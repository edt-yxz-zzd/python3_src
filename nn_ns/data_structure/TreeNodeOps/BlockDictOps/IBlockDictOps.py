

__all__ = '''
    IBlockDictOps
    '''.split()

from ..OtherOps.IOps import IOps
from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase

from .abc import not_implemented, abstractmethod
from seed.tiny import fst, snd, null_iter
#from collections.abc import MutableMapping
from .bd_helper import \
    (is_one_piece_block_key
    ,is_exactly_block_key
    ,block_key2iter_block_entities
    )


def ireplace_block_key_of_entity(entity, block_key):
    # :: entity -> block_key -> new_entity
    return block_key, entity[1]

entity2block_key = lambda e: e[0]


class IBlockDictOps(IOps):
    '''
readonly
    e.g. binary search on sorted[(block_key, dict_value)]

IBlockDictOps__modify:
    not (MutableMapping)
    since no __len__/__iter__
        # hence no keys/items/values/popitem

dict_key :: ITotalOrderingOps
    # to using KeyOrderedTree
dict_value :: IEqOps
    # to merge two touch/overlap blocks with same dict_value

dict_key = basic_key = key :: Key in IBlockDictKeyOps
    # BlockDict implement details:
    # tree_key = lkey_ex = left_key_ex = left_bound :: KeyEx in IBlockDictKeyOps

item = (dict_key, dict_value)

block_key = (lkey_ex, rkey_ex) = range :: Range
block_item = (block_key, dict_value) = entity


why not m[begin:end] for get/set/del?
    # block_key2iter_block_items
    # set_block_item
    # pop_block_items_of_block_key/discard_block_key
    since we donot know what Key is.
    Key may be slice, so confuse...

see:
    IBlockDictKeyOps__position.iter_all_touch_or_overlap_block_items
testing:
    BlockDict__ops_biased
'''
    __slots__ = ()

    def get_total_dict_key_ops(ops):
        # about dict_key
        return ops.block_dict_key_ops.total_key_ops
    def get_block_dict_key_ops(ops):
        bdk_ops = ops._get_block_dict_key_ops_()
        assert isinstance(bdk_ops, IBlockDictKeyOps)
        return bdk_ops
    def get_eq_dict_value_ops(ops):
        edv_ops = ops._get_eq_dict_value_ops_()
        assert isinstance(edv_ops, IEqOps)
        return edv_ops


    @not_implemented
    def _get_block_dict_key_ops_(ops):
        # -> IBlockDictKeyOps<dict_key, KeyEx<dict_key> >
        #
        # dict_key vs tree_key
        #   dict_key = basic_key = key in IBlockDictKeyOps
        #   tree_key = lkey_ex = left_key_ex = left_bound
        #       is key_ex in IBlockDictKeyOps
        ...
    @not_implemented
    def _get_eq_dict_value_ops_(ops):
        # -> IEqOps<dict_value>
        ...


    '''
    @not_implemented
    def block_key2iter_block_items(ops, self, block_key, *, reverse=False):
        # -> Iter (block_key, dict_value)
        # all block_key result inside input_block_key
        ...
    '''

    @not_implemented
    def iter_all_touch_or_overlap_block_items(ops, self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        # block_key may be empty
        # see: IBlockDictKeyOps__position
        isEmptyRange = ops.block_dict_key_ops.isEmptyRange
        if isEmptyRange(block_key):
            # yield nothing
            return
        ...

    @not_implemented
    def get_num_block_keys(ops, self):
        # no __len__
        ...
    @not_implemented
    def iter_block_items(ops, self, *, reverse=False):
        # no items
        ...
    @not_implemented
    def copy_block_dict(ops, self):
        ...
    @not_implemented
    def _index_block_item_at_(ops, self, i:'UInt'):
        # -> block_item
        assert 0 <= i < ops.get_num_block_keys(self)
        ...
    def index_block_item_at(ops, self, i:'Int'):
        # -> block_item | IndexError
        # normally, O(log(n)), maybe O(1), should not >O(n)
        # position may not be index
        # see: IBlockDictOps__position
        L = ops.get_num_block_keys(self)
        if i < 0:
            i += L
        if not 0 <= i < L: raise IndexError
        return ops._index_block_item_at_(self, i)
    def get_first_or_last_block_item(ops, self, last:bool):
        # -> block_item | IndexError
        L = ops.get_num_block_keys(self)
        if not L: raise IndexError
        #bug: i = L-1 if L else 0
        i = L-1 if last else 0
        return ops._index_block_item_at_(self, i)
    def get_first_block_item(ops, self):
        # -> block_item | IndexError
        return ops.get_first_or_last_block_item(self, False)
    def get_last_block_item(ops, self):
        # -> block_item | IndexError
        return ops.get_first_or_last_block_item(self, True)


    def is_one_piece_block_key(ops, self, block_key):
        # not empty range and inside one of iter_block_keys()
        return is_one_piece_block_key(
                block_key
                , entity2block_key
                , ops.block_dict_key_ops
                , ops.iter_all_touch_or_overlap_block_items
                , self
                )

    def is_exactly_block_key(ops, self, block_key):
        # be one of iter_block_keys()
        return is_exactly_block_key(
                block_key
                , entity2block_key
                , ops.block_dict_key_ops
                , ops.iter_all_touch_or_overlap_block_items
                , self
                )


    def list_all_touch_or_overlap_block_items(ops, self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        # block_key may be empty
        iter_all_of = ops.iter_all_touch_or_overlap_block_items
        return [*iter_all_of(self, block_key, overlap_only, reverse=reverse)]



    @property
    def eq_dict_value_ops(ops):
        return ops.get_eq_dict_value_ops()
    @property
    def dict_value_eq(ops):
        return ops.eq_dict_value_ops.eq
    @property
    def block_dict_key_ops(ops):
        return ops.get_block_dict_key_ops()
    @property
    def total_dict_key_ops(ops):
        return ops.get_total_dict_key_ops()
    @property
    def mkSingletonRange(ops):
        return ops.block_dict_key_ops.mkSingletonRange
    @property
    def eqRange(ops):
        return ops.block_dict_key_ops.eqRange



    def block_key2block_items(ops, self, block_key, *, reverse=False):
        # block_key may be empty
        # -> [(block_key, dict_value)]
        return list(ops.block_key2iter_block_items(self, block_key, reverse=reverse))
    def iter_block_keys(ops, self, *, reverse=False):
        # no __iter__/keys
        return map(fst, ops.iter_block_items(self, reverse=reverse))
    def iter_dict_values(ops, self, *, reverse=False):
        # no values
        return map(snd, ops.iter_block_items(self, reverse=reverse))




    def dict_key2block_items(ops, self, dict_key):
        block_key = ops.mkSingletonRange(dict_key)
        block_items = ops.block_key2block_items(self, block_key)
        return block_items




    # __bool__
    def is_empty(ops, self):
        #bug: return bool(ops.get_num_block_keys(self))
        return not ops.get_num_block_keys(self)

    # __getitem__
    def dict_key2dict_value(ops, self, dict_key, *
            , dict_key2default=None
            , dict_value2result=None):
        block_items = ops.dict_key2block_items(self, dict_key)
        if not block_items:
            if dict_key2default is None:
                raise KeyError(dict_key)
            return dict_key2default(dict_key)

        [block_item] = block_items
        (block_key_, dict_value) = block_item

        if dict_value2result is None:
            return dict_value
        return dict_value2result(dict_value)

    # __contains__
    def contains_dict_key(ops, self, dict_key):
        block_items = ops.dict_key2block_items(self, dict_key)
        return bool(block_items)

    # get
    def getdefault(ops, self, dict_key, default=None, *, dict_value2result=None):
        def dict_key2default(dict_key):
            return default
        return ops.dict_key2dict_value(self, dict_key
                    , dict_key2default=dict_key2default
                    , dict_value2result=dict_value2result)




    # __eq__
    def block_dict_eq(ops, self, other):
        if self is other: return True

        # since using same ops
        #if not isinstance(other, __class__): return NotImplemented
        #if self.block_dict_key_ops != other.block_dict_key_ops: raise TypeError
        #if other.eq_dict_value_ops != self.eq_dict_value_ops: return TypeError

        if ops.get_num_block_keys(self) != ops.get_num_block_keys(other):
            return False

        block_dict_key_ops = ops.block_dict_key_ops
        dict_value_eq = ops.dict_value_eq
        eqRange = block_dict_key_ops.eqRange
        for lhs, rhs in zip(ops.iter_block_items(self), ops.iter_block_items(other)):
            lrng, lval = lhs
            rrng, rval = rhs
            if not (eqRange(lrng, rrng) and dict_value_eq(lval, rval)):
                return False
        return True


    def block_key2iter_block_items(ops, self, block_key, *, reverse=False):
        # intput_block_key may be empty
        #
        # -> Iter (block_key, dict_value)
        #   all output_block_keys are nonempty and inside input_block_key
        return block_key2iter_block_entities(
                    block_key
                    , bool(reverse)
                    , entity2block_key
                    , ireplace_block_key_of_entity
                        # :: entity -> block_key -> new_entity
                    , ops.block_dict_key_ops
                    , ops.iter_all_touch_or_overlap_block_items
                    , self
                    )



if __name__ == '__main__':
    XXX = IBlockDictOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)



