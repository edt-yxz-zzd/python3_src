

__all__ = ['IUserHeapOps_ABC']
from ..abc import abstractmethod, override, not_implemented
from .IHeapOps_ABC import IHeapOps_ABC

class IUserHeapOps_ABC(IHeapOps_ABC):
    '''


new_methods:
    `get_user_heap_ops
    `wrap_heap

    wrap
    unwrap
    wrapped_obj2key
    can_be_parent_key_of
    can_be_parent_wrapped_obj_of
    basic__can_be_parent_idx_of
    basic__swap
    to_parent_idx
    to_child_idc
    basic__make_heap_inplace
    basic__move_backward_at
    basic__move_forward_at
    xobj2wrapped_obj
    basic__replace_at
    wrapped_obj2xobj
    basic__pop_then_push
    basic__push_then_pop
    basic__pop
    basic__push
    basic__delete_at
'''
    __slots__ = ()
    ###########################
    @not_implemented
    def get_user_heap_ops(ops):
        # -> IHeapOps_ABC
        raise NotImplementedError
    def wrap_heap(ops, heap):
        # heap -> wrapped_obj_seq
        #   get seq from heap-obj or wrap mutable-seq-view above heap-obj
        return ops.get_user_heap_ops().wrap_heap(heap)
    ###########################
    @override
    def wrap(ops, unwrapped_obj, idx):
        # unwrapped_obj -> UInt -> wrapped_obj
        return ops.get_user_heap_ops().wrap(unwrapped_obj, idx)
    @override
    def unwrap(ops, wrapped_obj):
        # wrapped_obj -> unwrapped_obj
        return ops.get_user_heap_ops().unwrap(wrapped_obj)
    @override
    def wrapped_obj2key(ops, wrapped_obj):
        # wrapped_obj -> key
        return ops.get_user_heap_ops().wrapped_obj2key(wrapped_obj)
    @override
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        # key -> key -> Bool
        return ops.get_user_heap_ops().can_be_parent_key_of(parent_wrapped_key, child_wrapped_key)
    def can_be_parent_wrapped_obj_of(ops, parent_wrapped_obj, child_wrapped_obj):
        return ops.get_user_heap_ops().can_be_parent_wrapped_obj_of(parent_wrapped_obj, child_wrapped_obj)
    def basic__can_be_parent_idx_of(ops, wrapped_obj_seq, parent_idx, child_idx):
        # assert 0 <= parent_idx == to_parent_idx(child_idx) < child_idx < len(wrapped_obj_seq)
        return ops.get_user_heap_ops().basic__can_be_parent_idx_of(wrapped_obj_seq, parent_idx, child_idx)
    def basic__swap(ops, wrapped_obj_seq, parent_idx, child_idx):
        # assert 0 <= parent_idx == to_parent_idx(child_idx) < child_idx < len(wrapped_obj_seq)
        return ops.get_user_heap_ops().basic__swap(wrapped_obj_seq, parent_idx, child_idx)

    ####################

    def to_parent_idx(ops, child_idx):
        # child_idx -> parent_idx
        return ops.get_user_heap_ops().to_parent_idx(child_idx)
    def to_child_idc(ops, parent_idx):
        # parent_idx -> (fst_child_idx, snd_child_idx)
        return ops.get_user_heap_ops().to_child_idc(parent_idx)
    def basic__make_heap_inplace(ops, wrapped_obj_seq):
        '''heapify'''
        return ops.get_user_heap_ops().basic__make_heap_inplace(wrapped_obj_seq)


    ####################

    def basic__move_backward_at(ops, wrapped_obj_seq, idx):
        # -> new_idx
        return ops.get_user_heap_ops().basic__move_backward_at(wrapped_obj_seq, idx)

    def basic__move_forward_at(ops, wrapped_obj_seq, idx):
        # -> new_idx
        return ops.get_user_heap_ops().basic__move_forward_at(wrapped_obj_seq, idx)

    ##############

    def xobj2wrapped_obj(ops, xobj, idx, *, wrapped):
        return ops.get_user_heap_ops().xobj2wrapped_obj(xobj, idx, wrapped=wrapped)


    def basic__replace_at(ops, wrapped_obj_seq, idx, xobj, *, wrapped:bool):
        # xobj = unwrapped_obj|wrapped_obj
        # -> new_idx
        return ops.get_user_heap_ops().basic__replace_at(wrapped_obj_seq, idx, xobj, wrapped=wrapped)


    ##############

    def wrapped_obj2xobj(ops, wrapped_obj, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().wrapped_obj2xobj(wrapped_obj, wrapped=wrapped)

    def basic__pop_then_push(ops, wrapped_obj_seq, xobj, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().basic__pop_then_push(wrapped_obj_seq, xobj, wrapped=wrapped)

    def basic__push_then_pop(ops, wrapped_obj_seq, xobj, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().basic__push_then_pop(wrapped_obj_seq, xobj, wrapped=wrapped)

    #################



    def basic__pop(ops, wrapped_obj_seq, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().basic__pop(wrapped_obj_seq, wrapped=wrapped)

    def basic__push(ops, wrapped_obj_seq, xobj, *, wrapped):
        return ops.get_user_heap_ops().basic__push(wrapped_obj_seq, xobj, wrapped=wrapped)

    ###############

    def basic__delete_at(ops, wrapped_obj_seq, idx, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().basic__delete_at(wrapped_obj_seq, idx, wrapped=wrapped)



    #################
    #################
    #################
    #################
    def is_empty(ops, heap):
        # -> bool
        return ops.get_user_heap_ops().is_empty(heap)
    def get_size(ops, heap):
        # -> UInt
        return ops.get_user_heap_ops().get_size(heap)

    ################

    def can_be_parent_idx_of(ops, heap, parent_idx, child_idx):
        # assert 0 <= parent_idx == to_parent_idx(child_idx) < child_idx < len(wrapped_obj_seq)
        return ops.get_user_heap_ops().can_be_parent_idx_of(heap, parent_idx, child_idx)
    def swap(ops, heap, parent_idx, child_idx):
        # assert 0 <= parent_idx == to_parent_idx(child_idx) < child_idx < len(wrapped_obj_seq)
        return ops.get_user_heap_ops().swap(heap, parent_idx, child_idx)

    ####################

    def to_parent_idx(ops, child_idx):
        # child_idx -> parent_idx
        return ops.get_user_heap_ops().to_parent_idx(child_idx)
    def to_child_idc(ops, parent_idx):
        # parent_idx -> (fst_child_idx, snd_child_idx)
        return ops.get_user_heap_ops().to_child_idc(parent_idx)
    def make_heap_inplace(ops, heap):
        '''heapify'''
        return ops.get_user_heap_ops().make_heap_inplace(heap)


    ####################

    def move_backward_at(ops, heap, idx):
        # -> new_idx
        return ops.get_user_heap_ops().move_backward_at(heap, idx)

    def move_forward_at(ops, heap, idx):
        # -> new_idx
        return ops.get_user_heap_ops().move_forward_at(heap, idx)

    ##############

    def xobj2wrapped_obj(ops, xobj, idx, *, wrapped):
        return ops.get_user_heap_ops().xobj2wrapped_obj(xobj, idx, wrapped=wrapped)


    def replace_at(ops, heap, idx, xobj, *, wrapped:bool):
        # xobj = unwrapped_obj|wrapped_obj
        # -> new_idx
        return ops.get_user_heap_ops().replace_at(heap, idx, xobj, wrapped=wrapped)


    ##############

    def wrapped_obj2xobj(ops, wrapped_obj, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().wrapped_obj2xobj(wrapped_obj, wrapped=wrapped)

    def pop_then_push(ops, heap, xobj, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().pop_then_push(heap, xobj, wrapped=wrapped)

    def push_then_pop(ops, heap, xobj, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().push_then_pop(heap, xobj, wrapped=wrapped)

    #################



    def pop(ops, heap, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().pop(heap, wrapped=wrapped)

    def push(ops, heap, xobj, *, wrapped):
        return ops.get_user_heap_ops().push(heap, xobj, wrapped=wrapped)

    ###############

    def delete_at(ops, heap, idx, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().delete_at(heap, idx, wrapped=wrapped)


if __name__ == '__main__':
    XXX = IUserHeapOps_ABC

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


