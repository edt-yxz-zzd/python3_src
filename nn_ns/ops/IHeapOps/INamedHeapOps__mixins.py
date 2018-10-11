
__all__ = '''
    INamedHeapOps__mixins
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps import INamedHeapOps



class INamedHeapOps__mixins(INamedHeapOps):
    '''

override:
    delete_name
    discard_name
    pop_then_push
    push
    push_ex
    push_then_pop

    is_empty
    add_or_update_name
    push_then_pop_ex
    pop
methods:
    `can_be_parent_key_of
    is_empty
    `get_size
    `exists
    `add_name
    `update_name
    add_or_update_name
    `pop_name
    delete_name
    discard_name
    `peek
    `pop_then_push_ex
    push_then_pop_ex
    pop_then_push
    push_then_pop
    pop
    push
    push_ex

'''
    __slots__ = ()
    #################

    @override
    def delete_name(ops, heap, name):
        # -> None
        ops.pop_name(heap, name)
    @override
    def discard_name(ops, heap, name):
        # -> Bool
        # return True if existed
        # delete_name if existing
        if ops.exists(heap, name):
            ops.delete_name(heap, name)
            return True
        return False

    @override
    def pop_then_push(ops, heap, unwrapped_obj):
        # -> unwrapped_obj
        name, key, payload = unwrapped_obj
        return ops.pop_then_push_ex(heap, name, key, payload)
    @override
    def push_then_pop(ops, heap, unwrapped_obj):
        # -> unwrapped_obj
        name, key, payload = unwrapped_obj
        return ops.push_then_pop_ex(heap, name, key, payload)
    @override
    def push(ops, heap, unwrapped_obj):
        # -> None
        name, key, payload = unwrapped_obj
        ops.add_name(heap, name, key, payload)
    @override
    def push_ex(ops, heap, name, key, payload):
        # -> None
        ops.add_name(heap, name, key, payload)



    #################
    #################
    #################
    @override
    def is_empty(ops, heap):
        # -> bool
        return not ops.get_size(heap)

    @override
    def add_or_update_name(ops, heap, name, key, payload):
        # -> new_inner_pointer
        # add non-existing name or update existing name
        if ops.exists(heap, name):
            f = ops.update_name
        else:
            f = ops.add_name
        return f(heap, name, key, payload)

    @override
    def push_then_pop_ex(ops, heap, name, key, payload):
        # -> unwrapped_obj
        assert not ops.exists(heap, name)

        unwrapped_obj = (name, key, payload)
        if ops.is_empty(heap):
            return unwrapped_obj

        _name, _key, _payload = _unwrapped_obj = ops.peek(heap)
        if ops.can_be_parent_key_of(key, _key):
            return unwrapped_obj
        return ops.pop_then_push_ex(heap, name, key, payload)



    @override
    def pop(ops, heap):
        # -> unwrapped_obj
        assert not ops.is_empty(heap)
        name, key, payload = unwrapped_obj = ops.peek(heap)
        return ops.pop_name(heap, name)



if __name__ == '__main__':
    XXX = INamedHeapOps__mixins

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)



