
__all__ = '''
    IBlockDictOps__constructor
    '''.split()

#from ..OtherOps.IEqOps import IEqOps
#from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
#from .IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase
from .IBlockDictOps import IBlockDictOps

from .abc import not_implemented, abstractmethod
from seed.tiny import echo, fst #, snd
#from collections.abc import MutableMapping

from ..BlockDictOps.bd_helper import bd_subtract, bd_intersection
from itertools import chain



# as BlockSet when use bd_subtract
set_entity2block_key = echo
set_ireplace_block_key_of_entity = lambda entity, block_key: block_key
def ireplace_block_key_of_entity(entity, block_key):
    # :: entity -> block_key -> new_entity
    return block_key, entity[1]
entity2block_key = lambda e: e[0]


class IBlockDictOps__constructor(IBlockDictOps):
    __slots__ = ()

    @not_implemented
    def make_empty_block_dict(ops):
        ...
    @not_implemented
    def make_block_dict_from_items(ops, items):
        ...
    @not_implemented
    def make_block_dict_from_block_items(ops, block_items):
        ...

    def make_whole_block_dict(ops, dict_value):
        rng = ops.block_dict_key_ops.getWholeRange()
        return ops.make_block_dict_from_block_items([(rng, dict_value)])

    def make_complement_block_dict_of(ops, self, block_key2dict_value):
        block_key2iter_block_items = ops.block_key2iter_block_items
        block_dict_key_ops = ops.block_dict_key_ops
        rng = block_dict_key_ops.getWholeRange()

        def block_key2iter_block_keys(block_key):
            return map(fst, block_key2iter_block_items(self, block_key))
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
        return ops.make_block_dict_from_block_items(block_items)
    def make_block_dict_from_iterable(ops, iterable, is_block_items:bool):
        if is_block_items:
            f = ops.make_block_dict_from_block_items
        else:
            f = ops.make_block_dict_from_items
        return f(iterable)


    def make_union(ops, self, other, combine):
        # self | other
        # combine :: self_dict_value -> other_dict_value -> dict_value
        #
        common = ops.make_intersection(self, other, combine)
        nonoverlaps = ops.make_symmetric_difference(self, other)
        block_items = chain(
                            ops.iter_block_items(common)
                            , ops.iter_block_items(nonoverlaps)
                            )
        return ops.make_block_dict_from_block_items(block_items)
    def make_intersection(ops, self, other, combine):
        # self & other
        # combine :: self_dict_value -> other_dict_value -> dict_value
        #

        block_dict_key_ops = ops.block_dict_key_ops
        iter_block_items = ops.iter_block_items
        block_key2iter_block_items = ops.block_key2iter_block_items

        block_items = \
            bd_intersection(
                echo    # entity2block_item
                , echo  # block_item2entity
                , combine
                    # :: self_dict_value -> other_dict_value -> dict_value
                , block_dict_key_ops
                , iter_block_items(self) # self_iter_block_entities
                    # :: Iter block_item
                , block_key2iter_block_items
                    # other_block_key2iter_block_entities
                , other # *args_for_other_block_key2iter_block_entities
                )
        return ops.make_block_dict_from_block_items(block_items)

    def make_difference(ops, self, other):
        # self - other
        block_dict_key_ops = ops.block_dict_key_ops
        iter_block_items = ops.iter_block_items
        block_key2iter_block_items = ops.block_key2iter_block_items

        block_items = bd_subtract(
                entity2block_key
                , ireplace_block_key_of_entity
                    # :: entity -> block_key -> new_entity
                , block_dict_key_ops
                , iter_block_items(self)
                , block_key2iter_block_items
                , other
                )
        return ops.make_block_dict_from_block_items(block_items)

    def make_symmetric_difference(ops, self, other):
        # set ^ other
        block_dict_key_ops = ops.block_dict_key_ops
        iter_block_items = ops.iter_block_items
        block_key2iter_block_items = ops.block_key2iter_block_items

        block_items1 = bd_subtract(
                entity2block_key
                , ireplace_block_key_of_entity
                    # :: entity -> block_key -> new_entity
                , block_dict_key_ops
                , iter_block_items(self)
                , block_key2iter_block_items
                , other
                )
        block_items2 = bd_subtract(
                entity2block_key
                , ireplace_block_key_of_entity
                    # :: entity -> block_key -> new_entity
                , block_dict_key_ops
                , iter_block_items(other)
                , block_key2iter_block_items
                , self
                )
        block_items = chain(block_items1, block_items2)
        return ops.make_block_dict_from_block_items(block_items)

if __name__ == '__main__':
    XXX = IBlockDictOps__constructor

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)



