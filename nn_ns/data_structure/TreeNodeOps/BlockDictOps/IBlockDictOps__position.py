
__all__ = '''
    IBlockDictOps__position
    '''.split()


from .abc import not_implemented, abstractmethod, override
from .IBlockDictOps import IBlockDictOps

from itertools import takewhile

class IBlockDictOps__position(IBlockDictOps):
    '''left_bound as tree_key
    override iter_all_touch_or_overlap_block_items
'''
    __slots__ = ()

    @not_implemented
    def get_the_begin_or_end_position(ops, self, end:bool):
        ...
    @not_implemented
    def _left_bound2begin_(ops, self, left_bound):
        # -> position
        # if begin not the begin position of whole:
        #   then left_bound may be inside the range at prev(begin)
        ...
    @not_implemented
    def prev_or_succ_position_of(ops, self, position, succ:bool):
        # -> (position | raise StopIteration)
        # StopIteration if not succ and position is the begin position of whole
        # StopIteration if succ and position is the end position of whole
        ...

    @not_implemented
    def iter_block_items_from_position(ops, self, position, *, reverse=False):
        # assume: +1 for succ, -1 for prev
        # if reverse:   self[position-1], self[position-2], ...
        #   else:       self[position], self[position+1]...
        ...



    def get_the_begin_position(ops, self):
        return ops.get_the_begin_or_end_position(self, False)
    def get_the_end_position(ops, self):
        return ops.get_the_begin_or_end_position(self, True)
    def nonempty_block_key2begin_or_end(ops, self, block_key, end:bool):
        # -> position
        # -> (begin | end)
        isEmptyRange = ops.block_dict_key_ops.isEmptyRange
        if isEmptyRange(block_key): raise ValueError

        left_bound, right_bound = block_key
        if not end:
            return ops.left_bound2begin(self, left_bound)
        else:
            return ops.right_bound2end(self, right_bound)
        pass

    def left_bound2begin(ops, self, left_bound):
        # -> position
        # if begin not the begin position of whole:
        #   then left_bound may be inside the range at prev(begin)
        block_dict_key_ops = ops.block_dict_key_ops
        isTheMinKeyEx = block_dict_key_ops.isTheMinKeyEx
        isLeftBound = block_dict_key_ops.isLeftBound

        if isTheMinKeyEx(left_bound):
            return ops.get_the_begin_position(self)

        if not isLeftBound(left_bound): raise TypeError('not isLeftBound')
        return ops._left_bound2begin_(self, left_bound)

    def right_bound2end(ops, self, right_bound):
        # -> position
        # if end is not the end position of whole
        #   right_bound should not be inside the range at end
        block_dict_key_ops = ops.block_dict_key_ops
        isTheMaxKeyEx = block_dict_key_ops.isTheMaxKeyEx
        R2L = block_dict_key_ops.right_bound2left_bound_more

        # bug: without testing isTheMaxKeyEx(right_bound)
        if isTheMaxKeyEx(right_bound):
            return ops.get_the_end_position(self)
        left_bound_more = R2L(right_bound)
        return ops.left_bound2begin(self, left_bound_more)


    def prev_position_of(ops, self, position):
        # -> StopIteration if position is the begin position of whole
        return ops.prev_or_succ_position_of(self, position, False)
    def succ_position_of(ops, self, position):
        # -> StopIteration if position is the end position of whole
        return ops.prev_or_succ_position_of(self, position, True)


    @override
    def iter_all_touch_or_overlap_block_items(ops, self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        block_dict_key_ops = ops.block_dict_key_ops
        isEmptyRange = block_dict_key_ops.isEmptyRange
        touch_or_cross = block_dict_key_ops.cross if overlap_only else block_dict_key_ops.touch_or_cross
        nonempty_block_key2begin_or_end = ops.nonempty_block_key2begin_or_end
        prev_or_succ_position_of = ops.prev_or_succ_position_of
        iter_block_items_from_position = ops.iter_block_items_from_position
        is_empty = ops.is_empty

        if isEmptyRange(block_key) or is_empty(self):
            # yield nothing
            return

        reverse = bool(reverse)

        end = reverse
        position = nonempty_block_key2begin_or_end(self, block_key, end)
        try:
            succ = reverse
            position = prev_or_succ_position_of(self, position, succ)
        except StopIteration:
            more = False
        else:
            more = True

        k_left_bound, k_right_bound = block_key
        def touch_or_cross_later_entity(later_entity):
            # block_key <= later_entity[0]
            ((e_left_bound, e_right_bound), dict_value) = later_entity
            return touch_or_cross(k_right_bound, e_left_bound)
        def touch_or_cross_befor_entity(befor_entity):
            # block_key >= later_entity[0]
            ((e_left_bound, e_right_bound), dict_value) = befor_entity
            return touch_or_cross(e_right_bound, k_left_bound)

        #def test_more(the_more_entity):
        #def test_entity(entity):
        if True:
            if succ:
                # reverse
                # entity <= block_key <= the_more_entity
                test_more = touch_or_cross_later_entity
                test_entity = touch_or_cross_befor_entity
            else:
                # prev
                # not reverse
                # the_more_entity <= block_key <= entity
                test_more = touch_or_cross_befor_entity
                test_entity = touch_or_cross_later_entity

        it = iter_block_items_from_position(self, position, reverse=reverse)
        assert iter(it) is it # iterator

        if more:
            for the_more_entity in it:
                break
            else:
                # yield nothing
                return

            if test_more(the_more_entity):
                yield the_more_entity

        # bug: yield from filter(test_entity, it)
        yield from takewhile(test_entity, it)
        return

if __name__ == '__main__':
    XXX = IBlockDictOps__position

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


