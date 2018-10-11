

__all__ = '''
    INamedHeapOps
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from ..IOps import IOps

class INamedHeapOps(IOps):
    '''

data NamedHeap seq map name key payload =
        {idx2wrapped_obj :: seq wrapped_obj
        ,name2wrapped_obj :: map name wrapped_obj
        }
    where wrapped_obj = WrappedObj name key payload
data WrappedObj name key payload = (UnWrappedObj name key payload, mutable UInt)
data UnWrappedObj name key payload = (name, key, payload)



new_methods:
    `can_be_parent_key_of
    `is_empty
    `get_size
    `exists
    ##`make_heap_from_iterable
    `add_name
    `update_name
    `add_or_update_name
    `pop_name
    `delete_name
    `discard_name
    `peek
    `pop_then_push_ex
    `push_then_pop_ex
    `pop_then_push
    `push_then_pop
    `pop
    `push
    `push_ex
'''
    __slots__ = ()
    #################
    @not_implemented
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        # key -> key -> Bool
        # __le__
        raise NotImplementedError
        return parent_wrapped_key <= child_wrapped_key

    #################
    @not_implemented
    def is_empty(ops, heap):
        # -> bool
        raise NotImplementedError
        return not ops.get_size(heap)
    @not_implemented
    def get_size(ops, heap):
        # -> UInt
        raise NotImplementedError
    @not_implemented
    def exists(ops, heap, name):
        # -> Bool
        raise NotImplementedError

    ####################


    @not_implemented
    def add_name(ops, heap, name, key, payload):
        # -> new_inner_pointer
        # add non-existing name
        assert not ops.exists(heap, name)
        raise NotImplementedError
    @not_implemented
    def update_name(ops, heap, name, key, payload):
        # -> new_inner_pointer
        # update existing name
        assert ops.exists(heap, name)
        raise NotImplementedError
    @not_implemented
    def add_or_update_name(ops, heap, name, key, payload):
        # -> new_inner_pointer
        # add non-existing name or update existing name
        raise NotImplementedError

    @not_implemented
    def pop_name(ops, heap, name):
        # -> unwrapped_obj
        assert ops.exists(heap, name)
        raise NotImplementedError
    @not_implemented
    def delete_name(ops, heap, name):
        # -> None
        raise NotImplementedError
    @not_implemented
    def discard_name(ops, heap, name):
        # -> Bool
        # return True if existed
        # delete_name if existing
        raise NotImplementedError


    ##############

    @not_implemented
    def peek(ops, heap):
        # -> unwrapped_obj
        assert not ops.is_empty(heap)
        raise NotImplementedError

    @not_implemented
    def pop_then_push_ex(ops, heap, name, key, payload):
        # -> unwrapped_obj
        assert not ops.is_empty(heap)
        assert not ops.exists(heap, name) or ops.NOT-EXIST.name_eq(ops.peek(heap)[0], name)
        raise NotImplementedError

    @not_implemented
    def push_then_pop_ex(ops, heap, name, key, payload):
        # -> unwrapped_obj
        assert not ops.exists(heap, name)
        raise NotImplementedError

    @not_implemented
    def pop_then_push(ops, heap, unwrapped_obj):
        # -> unwrapped_obj
        raise NotImplementedError
    @not_implemented
    def push_then_pop(ops, heap, unwrapped_obj):
        # -> unwrapped_obj
        raise NotImplementedError
    #################



    @not_implemented
    def pop(ops, heap):
        # -> unwrapped_obj
        assert not ops.is_empty(heap)
        raise NotImplementedError

    @not_implemented
    def push(ops, heap, unwrapped_obj):
        # -> new_inner_pointer
        raise NotImplementedError
    @not_implemented
    def push_ex(ops, heap, name, key, payload):
        # -> new_inner_pointer
        raise NotImplementedError


if __name__ == '__main__':
    XXX = INamedHeapOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)



