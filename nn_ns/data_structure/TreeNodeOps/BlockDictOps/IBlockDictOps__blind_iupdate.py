__all__ = '''
    IBlockDictOps__blind_iupdate
    '''.split()


from .abc import not_implemented, abstractmethod, override
from .IBlockDictOps__imodify import IBlockDictOps__imodify

from seed.tiny import fst, snd
from itertools import takewhile

class IBlockDictOps__blind_iupdate(IBlockDictOps__imodify):
    __slots__ = ()

    @not_implemented
    def _blind_iupdate_exactly_(
            ops, self, block_keys_to_del, block_items_to_insert):
        # -> new_self
        #
        # assume self is a dict<block_key, dict_value>
        #   update directly
        #   donot care whether block_key is empty, insert/remove it directly
        #   treat all block_keys as exaclty block_keys
        #   see: is_exactly_block_key
        ...






    #############################################################

    @override
    def idiscard_block_key(ops, self, block_key):
        # -> new_self
        block_items, new_self = ops.ipop_block_items_of_block_key(self, block_key)
        return new_self
    @override
    def ipop_block_items_of_block_key(ops, self, block_key, *, reverse=False):
        # -> ([block_item], new_self)
        #   not Iter block_item
        isEmptyRange = ops.block_dict_key_ops.isEmptyRange

        if isEmptyRange(block_key): return [], self

        affected_block_items = ops.list_all_touch_or_overlap_block_items(self, block_key, False)

        middles = affected_block_items[1:-1]
        del affected_block_items[1:-1]
        end_block_items = affected_block_items; del affected_block_items

        L = len(end_block_items)
        assert L <= 2

        block_items_to_output = []
        if not L:
            return block_items_to_output, self


        block_keys_to_del = []
        block_items_to_insert = []

        f = ops.__pop_block_items_of_block_key__handle_left_or_right_end

        left_end = end_block_items[0]
        outputs, dels, inserts = f(self, block_key, left_end)
        block_items_to_output += outputs
        block_keys_to_del += dels
        block_items_to_insert += inserts


        block_items_to_output.extend(middles)
        block_keys_to_del.extend(map(fst, middles))

        if L == 2:
            right_end = end_block_items[1]
            outputs, dels, inserts = f(self, block_key, right_end)
            block_items_to_output += outputs
            block_keys_to_del += dels
            block_items_to_insert += inserts

        new_self = ops._blind_iupdate_exactly_(
                self, block_keys_to_del, block_items_to_insert)

        if reverse:
            block_items_to_output.reverse()
        return block_items_to_output, new_self


    def __pop_block_items_of_block_key__handle_left_or_right_end(
            ops, self, block_key, left_or_right_end_block_item):
        # -> (block_items_to_output, block_keys_to_del, block_items_to_insert)

        subtract_two_touch_or_cross_ranges = ops.block_dict_key_ops.subtract_two_touch_or_cross_ranges
        isEmptyRange = ops.block_dict_key_ops.isEmptyRange
        intersection_ranges1 = ops.block_dict_key_ops.intersection_ranges1

        rng, the_dict_value = left_or_right_end_block_item
        common_range = intersection_ranges1(block_key, rng)
        if not isEmptyRange(common_range):
            block_items_to_output = [(common_range, the_dict_value)]
            block_keys_to_del = [rng]
            nonempty_rngs = subtract_two_touch_or_cross_ranges(rng, block_key)
            block_items_to_insert = [(rng, the_dict_value) for rng in nonempty_rngs]
        else:
            block_items_to_output = []
            block_keys_to_del = []
            block_items_to_insert = []
        return block_items_to_output, block_keys_to_del, block_items_to_insert










    #############################################################

    @override
    def iset_block_item(ops, self, block_key, dict_value):
        # -> new_self
        #
        # if block_key overlap or touch input_block_key
        #   and block_dict_value_eq(self[block_key], dict_value):
        #   then merge the two ranges/block_keys

        isEmptyRange = ops.block_dict_key_ops.isEmptyRange
        if isEmptyRange(block_key): return self

        affected_block_items = ops.list_all_touch_or_overlap_block_items(self, block_key, False)

        block_keys_to_del = []
        block_items_to_insert = []

        middles = affected_block_items[1:-1]
        del affected_block_items[1:-1]
        end_block_items = affected_block_items; del affected_block_items
        assert len(end_block_items) <= 2

        f = ops.__set_block_item__handle_left_or_right_end
        for end in end_block_items:
            block_key, dels, inserts = f(self, block_key, dict_value, end)
            block_keys_to_del.extend(dels)
            block_items_to_insert.extend(inserts)


        block_keys_to_del.extend(map(fst, middles))
        block_items_to_insert.append((block_key, dict_value))

        new_self = ops._blind_iupdate_exactly_(
                self, block_keys_to_del, block_items_to_insert)
        return new_self

    def __set_block_item__handle_left_or_right_end(
            ops, self, block_key, dict_value, left_or_right_end_block_item):
        # -> (new_block_key_to_be_inserted, block_keys_to_del, block_items_to_insert)
        #       where block_items_to_insert donot include the new_block_key_to_be_inserted
        #
        # left_or_right_end_block_item comes from:
        #   affected_block_items = ops.list_all_touch_or_overlap_block_items(self, block_key, False)
        #   affected_block_items[0] or [-1]

        block_dict_key_ops = ops.block_dict_key_ops
        dict_value_eq = ops.dict_value_eq
        isEmptyRange = block_dict_key_ops.isEmptyRange
        union_touch_or_cross_ranges1 = block_dict_key_ops.union_touch_or_cross_ranges1
        intersection_ranges1 = block_dict_key_ops.intersection_ranges1
        subtract_two_touch_or_cross_ranges = block_dict_key_ops.subtract_two_touch_or_cross_ranges

        (rng, the_dict_value) = left_or_right_end_block_item
        if dict_value_eq(dict_value, the_dict_value):
            # merge
            new_block_key = union_touch_or_cross_ranges1(block_key, rng)
            block_keys_to_del = [rng]
            block_items_to_insert = [] # except the new_block_key
        else:
            new_block_key = block_key # the old one
            common_range = intersection_ranges1(block_key, rng)
            if isEmptyRange(common_range):
                # touch
                block_keys_to_del = []
                block_items_to_insert = []
            else:
                # overlap
                block_keys_to_del = [rng]

                # rng - block_key = two may empty rngs
                nonempty_rngs = subtract_two_touch_or_cross_ranges(rng, block_key)
                block_items_to_insert = [(rng, the_dict_value) for rng in nonempty_rngs]
        return new_block_key, block_keys_to_del, block_items_to_insert
















if __name__ == '__main__':
    XXX = IBlockDictOps__blind_iupdate

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


