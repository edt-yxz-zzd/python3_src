
__all__ = '''
    INamedHeapOps_ABC
    InnerHeapOps

    NAME_IDX
    KEY_IDX
    PAYLOAD_IDX
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps import INamedHeapOps
from .IHeapOps_ABC import IHeapOps_ABC

from collections import UserList





NAME_IDX, KEY_IDX, PAYLOAD_IDX = range(3)

class INamedHeapOps_ABC(INamedHeapOps):
    __slots__ = ()
    #################
    @not_implemented
    def get_idx2wrapped_obj(ops, heap):
        # heap -> wrapped_obj_seq
        raise NotImplementedError
    @not_implemented
    def get_name2wrapped_obj(ops, heap):
        # heap -> Map name wrapped_obj
        raise NotImplementedError
    @not_implemented
    def wrap(ops, unwrapped_obj, idx):
        # -> wrapped_obj
        raise NotImplementedError
    @not_implemented
    def unwrap(ops, wrapped_obj):
        # -> unwrapped_obj
        raise NotImplementedError
    @not_implemented
    def set_idx_of_wrapped_obj(ops, wrapped_obj, idx):
        # -> None
        raise NotImplementedError
    @not_implemented
    def get_idx_of_wrapped_obj(ops, wrapped_obj):
        # -> idx
        raise NotImplementedError

    #################
    @override
    def is_empty(ops, heap):
        # -> bool
        return not ops.get_idx2wrapped_obj(heap)
    @override
    def get_size(ops, heap):
        # -> UInt
        return len(ops.get_idx2wrapped_obj(heap))
        assert len(ops.get_idx2wrapped_obj(heap)) == len(ops.get_name2wrapped_obj(heap))
    @override
    def exists(ops, heap, name):
        return name in ops.get_name2wrapped_obj(heap)

    ####################

    def get_inner_heap_ops(ops):
        # -> IHeapOps
        return InnerHeapOps(ops)
    @override
    def add_name(ops, heap, name, key, payload):
        # add existing name
        if ops.exists(heap, name): raise KeyError(f'key exists: {name!r}')
        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        L = len(wrapped_obj_seq)

        unwrapped_obj = name, key, payload
        wrapped_obj = ops.wrap(unwrapped_obj, L)
        ops.get_inner_heap_ops().push(
            wrapped_obj_seq, wrapped_obj, wrapped=True)
        name2wrapped_obj[name] = wrapped_obj
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)

    @override
    def update_name(ops, heap, name, key, payload):
        # update existing name
        if not ops.exists(heap, name): raise KeyError(f'key not exists: {name!r}')

        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)

        old_wrapped_obj = name2wrapped_obj[name]
        #unwrapped_obj = ops.unwrap(old_wrapped_obj)
        #_name, _, _ = unwrapped_obj; assert name == _name
        idx = ops.get_idx_of_wrapped_obj(old_wrapped_obj)

        new_unwrapped_obj = name, key, payload
        new_wrapped_obj = ops.wrap(new_unwrapped_obj, idx)
        ops.get_inner_heap_ops().replace_at(
            wrapped_obj_seq, idx, new_wrapped_obj, wrapped=True)
        name2wrapped_obj[name] = new_wrapped_obj
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)


    @override
    def add_or_update_name(ops, heap, name, key, payload):
        # add non-existing name or update existing name
        if ops.exists(heap, name):
            f = ops.update_name
        else:
            f = ops.add_name
        f(heap, name, key, payload)

    @override
    def pop_name(ops, heap, name):
        # -> unwrapped_obj
        if not ops.exists(heap, name): raise KeyError(f'key not exists: {name!r}')

        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)

        old_wrapped_obj = name2wrapped_obj[name]
        idx = ops.get_idx_of_wrapped_obj(old_wrapped_obj)

        old_unwrapped_obj = ops.get_inner_heap_ops().delete_at(
                    wrapped_obj_seq, idx, wrapped=False)
        del name2wrapped_obj[name]
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        return old_unwrapped_obj


    ##############

    @override
    def pop_then_push_ex(ops, heap, name, key, payload):
        # -> unwrapped_obj
        if ops.exists(heap, name): raise KeyError(f'key exists: {name!r}')
        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)

        new_unwrapped_obj = name, key, payload
        new_wrapped_obj = ops.wrap(new_unwrapped_obj, 0)
        old_wrapped_obj = ops.get_inner_heap_ops().pop_then_push(
            wrapped_obj_seq, new_wrapped_obj, wrapped=True)

        result = old_unwrapped_obj = ops.unwrap(old_wrapped_obj)
        old_name = old_unwrapped_obj[NAME_IDX]
        new_name = name
        del name2wrapped_obj[old_name]
        name2wrapped_obj[new_name] = new_wrapped_obj
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        return result

    @override
    def push_then_pop_ex(ops, heap, name, key, payload):
        # -> unwrapped_obj
        if ops.exists(heap, name): raise KeyError(f'key exists: {name!r}')
        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)

        new_unwrapped_obj = name, key, payload
        new_wrapped_obj = ops.wrap(new_unwrapped_obj, 0)
        old_wrapped_obj = ops.get_inner_heap_ops().push_then_pop(
            wrapped_obj_seq, new_wrapped_obj, wrapped=True)

        if old_wrapped_obj is new_wrapped_obj:
            result = new_unwrapped_obj
        else:
            result = old_unwrapped_obj = ops.unwrap(old_wrapped_obj)
            old_name = old_unwrapped_obj[NAME_IDX]
            new_name = name
            del name2wrapped_obj[old_name]
            name2wrapped_obj[new_name] = new_wrapped_obj
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        return result


    #################

    @override
    def pop(ops, heap):
        # -> unwrapped_obj
        if ops.is_empty(heap): raise KeyError('pop empty heap')

        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)

        old_unwrapped_obj = ops.get_inner_heap_ops().pop(
            wrapped_obj_seq, wrapped=False)

        old_name = old_unwrapped_obj[NAME_IDX]
        del name2wrapped_obj[old_name]
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        return old_unwrapped_obj



########################################################################
########################################################################
#############################InnerHeapOps###############################
########################################################################
########################################################################
class InnerHeapOps(IHeapOps_ABC):
    # non-static inner class inside INamedHeapOps_ABC
    def __init__(ops, outer_ops:INamedHeapOps_ABC):
        ops.__outer_ops = outer_ops

    class InnerSeq(UserList):
        def __init__(self, outer_self, seq):
            super().__init__()
            self.data = seq
            assert self.data is seq
            self.__outer_self = outer_self
        def __setitem__(self, i, v):
            # donot consider slice
            #assert isinstance(i, int)
            #assert isinstance(v, WrappedObj)
            #assert type(i) is int, TypeError
            #assert type(v) is WrappedObj, TypeError
            self.data[i] = v
            #v.idx = i
            self.__outer_self.set_idx_of_wrapped_obj(v, i)
        def append(self, v):
            #assert type(v) is WrappedObj, TypeError
            self.data.append(v)
            i = len(self) - 1
            #v.idx = i
            self.__outer_self.set_idx_of_wrapped_obj(v, i)

    def set_idx_of_wrapped_obj(ops, wrapped_obj, idx):
        return self.__outer_ops.set_idx_of_wrapped_obj(wrapped_obj, idx)
    @override
    def wrap_heap(ops, heap):
        # -> wrapped_obj_seq/idx2wrapped_obj
        #return ops.InnerSeq(ops, ops.outer_ops.get_idx2wrapped_obj(heap))
        #assume heap is wrapped_obj_seq
        return ops.InnerSeq(ops, heap)
    @override
    def wrap(ops, unwrapped_obj, idx):
        return self.__outer_ops.wrap(unwrapped_obj, idx)
    @override
    def unwrap(ops, wrapped_obj):
        return self.__outer_ops.unwrap(wrapped_obj)
    @override
    def wrapped_obj2key(ops, wrapped_obj):
        return ops.unwrap(wrapped_obj)[KEY_IDX]
    @override
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        return ops.__outer_ops.can_be_parent_key_of(
            parent_wrapped_key, child_wrapped_key)


if __name__ == '__main__':
    XXX = INamedHeapOps_ABC

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)



