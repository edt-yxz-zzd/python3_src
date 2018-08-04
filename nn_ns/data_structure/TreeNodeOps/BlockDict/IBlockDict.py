

__all__ = '''
    IBlockDict
    '''.split()

from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase

from .abc import ABC, not_implemented
from seed.tiny import fst, snd, null_iter, echo
from .bd_helper import \
    (is_one_piece_block_key
    ,is_exactly_block_key
    ,block_key2iter_block_entities
    ,bd_subtract
    ,bd_intersection
    )
from itertools import chain



set_entity2block_key = echo
set_ireplace_block_key_of_entity = lambda entity, block_key: block_key
def ireplace_block_key_of_entity(entity, block_key):
    # :: entity -> block_key -> new_entity
    return block_key, entity[1]

entity2block_key = lambda e: e[0]
class IBlockDict(ABC):
    '''
not (MutableMapping):
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

'''
    __slots__ = ()

    def get_total_dict_key_ops(self):
        # about dict_key
        return self.block_dict_key_ops.total_key_ops
    def get_block_dict_key_ops(self):
        bdk_ops = self._get_block_dict_key_ops_()
        assert isinstance(bdk_ops, IBlockDictKeyOps)
        return bdk_ops
    def get_eq_dict_value_ops(self):
        edv_ops = self._get_eq_dict_value_ops_()
        assert isinstance(edv_ops, IEqOps)
        return edv_ops


    @not_implemented
    def _get_block_dict_key_ops_(self):
        # -> IBlockDictKeyOps<dict_key, KeyEx<dict_key> >
        #
        # dict_key vs tree_key
        #   dict_key = basic_key = key in IBlockDictKeyOps
        #   tree_key = lkey_ex = left_key_ex = left_bound
        #       is key_ex in IBlockDictKeyOps
        ...
    @not_implemented
    def _get_eq_dict_value_ops_(self):
        # -> IEqOps<dict_value>
        ...

    '''
    @not_implemented
    def block_key2iter_block_items(self, block_key, *, reverse=False):
        # -> Iter (block_key, dict_value)
        # all block_key result inside input_block_key
        ...
    '''

    @not_implemented
    def get_num_block_keys(self):
        # no __len__
        ...
    @not_implemented
    def iter_block_items(self, *, reverse=False):
        # no items
        ...

    @not_implemented
    def copy(self):
        ...

    @not_implemented
    def self_make_empty_block_dict(self):
        ...
    @not_implemented
    def self_make_block_dict_from_items(self, items):
        ...
    @not_implemented
    def self_make_block_dict_from_block_items(self, block_items):
        ...

    @not_implemented
    def iter_all_touch_or_overlap_block_items(self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        ...
    @not_implemented
    def _index_block_item_at_(self, i:'UInt'):
        # -> block_item
        assert 0 <= i < self.get_num_block_keys()
        ...
    def index_block_item_at(self, i:'Int'):
        # -> block_item | IndexError
        # normally, O(log(n)), maybe O(1), should not >O(n)
        # position may not be index
        # see: IBlockDictOps__position
        L = self.get_num_block_keys()
        if i < 0:
            i += L
        if not 0 <= i < L: raise IndexError
        return self._index_block_item_at_(i)
    def get_first_or_last_block_item(self, last:bool):
        # -> block_item | IndexError
        L = self.get_num_block_keys()
        if not L: raise IndexError
        #bug: i = L-1 if L else 0
        i = L-1 if last else 0
        return self._index_block_item_at_(i)
    def get_first_block_item(self):
        # -> block_item | IndexError
        return self.get_first_or_last_block_item(False)
    def get_last_block_item(self):
        # -> block_item | IndexError
        return self.get_first_or_last_block_item(True)





    def self_make_block_dict_from_iterable(self, iterable, is_block_items:bool):
        if is_block_items:
            f = self.self_make_block_dict_from_block_items
        else:
            f = self.self_make_block_dict_from_items
        return f(iterable)

    def self_make_whole_block_dict(self, dict_value):
        rng = self.block_dict_key_ops.getWholeRange()
        return self.self_make_block_dict_from_block_items([(rng, dict_value)])
    def self_make_complement_block_dict(self, block_key2dict_value):
        block_dict_key_ops = self.block_dict_key_ops
        rng = block_dict_key_ops.getWholeRange()
        def block_key2iter_block_keys(block_key):
            return map(fst, self.block_key2block_items(block_key))
        block_keys = bd_subtract(
                set_entity2block_key
                , set_ireplace_block_key_of_entity
                    # :: entity -> block_key -> new_entity
                , block_dict_key_ops
                , [rng]
                , block_key2iter_block_keys
                )
        block_items = ((block_key, block_key2dict_value(block_key))
                        for block_key in block_keys)
        return self.self_make_block_dict_from_block_items(block_items)

    def __bool__(self):
        return bool(self.get_num_block_keys())

    @property
    def mkSingletonRange(self):
        return self.get_block_dict_key_ops().mkSingletonRange
    @property
    def eq_dict_value_ops(self):
        return self.get_eq_dict_value_ops()
    @property
    def dict_value_eq(self):
        return self.eq_dict_value_ops.eq
    @property
    def block_dict_key_ops(self):
        return self.get_block_dict_key_ops()
    @property
    def total_dict_key_ops(self):
        return self.get_total_dict_key_ops()



    def block_key2block_items(self, block_key, *, reverse=False):
        # -> [(block_key, dict_value)]
        return list(self.block_key2iter_block_items(block_key, reverse=reverse))
    def iter_block_keys(self, *, reverse=False):
        # no __iter__/keys
        return map(fst, self.iter_block_items(reverse=reverse))
    def iter_dict_values(self, *, reverse=False):
        # no values
        return map(snd, self.iter_block_items(reverse=reverse))




    def is_one_piece_block_key(self, block_key):
        # not empty range and inside one of iter_block_keys()
        return is_one_piece_block_key(
                block_key
                , entity2block_key
                , self.block_dict_key_ops
                , self.iter_all_touch_or_overlap_block_items)

    def is_exactly_block_key(self, block_key):
        # be one of iter_block_keys()
        return is_exactly_block_key(
                block_key
                , entity2block_key
                , self.block_dict_key_ops
                , self.iter_all_touch_or_overlap_block_items)

    def list_all_touch_or_overlap_block_items(self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        # block_key may be empty
        iter_all_of = self.iter_all_touch_or_overlap_block_items
        return [*iter_all_of(block_key, overlap_only, reverse=reverse)]



    def dict_key2block_items(self, dict_key):
        block_key = self.mkSingletonRange(dict_key)
        block_items = self.block_key2block_items(block_key)
        return block_items







    def __getitem__(self, dict_key):
        block_items = self.dict_key2block_items(dict_key)
        if not block_items:
            raise KeyError(dict_key)
        [block_item] = block_items
        (block_key_, dict_value) = block_item
        return dict_value
    def __contains__(self, dict_key):
        block_items = self.dict_key2block_items(dict_key)
        return bool(block_items)

    def get(self, dict_key, default=None):
        block_items = self.dict_key2block_items(dict_key)
        if not block_items:
            return default

        [block_item] = block_items
        block_key, dict_value = block_item
        return dict_value

    def __eq__(self, other):
        if self is other: return True

        if not isinstance(other, __class__): return NotImplemented
        self.__check_other(other)
        if self.get_num_block_keys() != other.get_num_block_keys():
            return False

        block_dict_key_ops = self.block_dict_key_ops
        dict_value_eq = self.dict_value_eq
        eqRange = block_dict_key_ops.eqRange
        for lhs, rhs in zip(self.iter_block_items(), other.iter_block_items()):
            lrng, lval = lhs
            rrng, rval = rhs
            if not (eqRange(lrng, rrng) and dict_value_eq(lval, rval)):
                return False
        return True

    def __ne__(self, other):
        return not (self == other)



    ###############

    def block_key2iter_block_items(self, block_key, *, reverse=False):
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
                    , self.block_dict_key_ops
                    , self.iter_all_touch_or_overlap_block_items
                    )





    def __check_other(self, other):
        if not isinstance(other, __class__): raise TypeError
        if self.block_dict_key_ops != other.block_dict_key_ops: raise TypeError
        if other.eq_dict_value_ops != self.eq_dict_value_ops: raise TypeError

    def make_union(self, other, combine):
        # self | other
        # combine :: self_dict_value -> other_dict_value -> dict_value
        #
        self.__check_other(other)
        common = self.make_intersection(other, combine)
        nonoverlaps = self.make_symmetric_difference(other)
        block_items = chain(common.iter_block_items()
                        , nonoverlaps.iter_block_items())
        return self.self_make_block_dict_from_block_items(block_items)
    def make_intersection(self, other, combine):
        # self & other
        # combine :: self_dict_value -> other_dict_value -> dict_value
        #

        self.__check_other(other)
        block_dict_key_ops = self.block_dict_key_ops
        iter_block_items = self.iter_block_items
        block_key2iter_block_items = other.block_key2iter_block_items

        block_items = \
            bd_intersection(
                echo    # entity2block_item
                , echo  # block_item2entity
                , combine
                    # :: self_dict_value -> other_dict_value -> dict_value
                , block_dict_key_ops
                , iter_block_items() # self_iter_block_entities
                    # :: Iter block_item
                , block_key2iter_block_items
                    # other_block_key2iter_block_entities
                )
        return self.self_make_block_dict_from_block_items(block_items)

    def __sub__(self, other):
        return self.make_difference(other)
    def make_difference(self, other):
        # self - other
        self.__check_other(other)
        block_dict_key_ops = self.block_dict_key_ops
        iter_block_items = self.iter_block_items
        block_key2iter_block_items = other.block_key2iter_block_items

        block_items = bd_subtract(
                entity2block_key
                , ireplace_block_key_of_entity
                    # :: entity -> block_key -> new_entity
                , block_dict_key_ops
                , iter_block_items()
                , block_key2iter_block_items
                )
        return self.self_make_block_dict_from_block_items(block_items)

    def __xor__(self, other):
        return self.make_symmetric_difference(other)
    def make_symmetric_difference(self, other):
        # set ^ other
        self.__check_other(other)
        block_dict_key_ops = self.block_dict_key_ops

        block_items1 = bd_subtract(
                entity2block_key
                , ireplace_block_key_of_entity
                    # :: entity -> block_key -> new_entity
                , block_dict_key_ops
                , self.iter_block_items()
                , other.block_key2iter_block_items
                )
        block_items2 = bd_subtract(
                entity2block_key
                , ireplace_block_key_of_entity
                    # :: entity -> block_key -> new_entity
                , block_dict_key_ops
                , other.iter_block_items()
                , self.block_key2iter_block_items
                )
        block_items = chain(block_items1, block_items2)
        return self.self_make_block_dict_from_block_items(block_items)





if __name__ == '__main__':
    XXX = IBlockDict

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)



