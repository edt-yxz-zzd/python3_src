
__all__ = '''
    INamedHeapOps_ABC

    NAME_IDX
    KEY_IDX
    PAYLOAD_IDX

    InnerArrayHeapOps
    InnerSeq
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps__mixins import INamedHeapOps__mixins
from .IArrayHeapOps_ABC import IArrayHeapOps_ABC
from .IHeapOps__with_IWrappedObjectOps import IHeapOps__with_IWrappedObjectOps
from .IWrappedObjectOpsEx import IWrappedObjectOpsEx

from collections import UserList





NAME_IDX, KEY_IDX, PAYLOAD_IDX = range(3)

class INamedHeapOps_ABC(INamedHeapOps__mixins):
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
    def get_size(ops, heap):
        # -> UInt
        return len(ops.get_idx2wrapped_obj(heap))
        assert len(ops.get_idx2wrapped_obj(heap)) == len(ops.get_name2wrapped_obj(heap))
    @override
    def exists(ops, heap, name):
        return name in ops.get_name2wrapped_obj(heap)

    ####################

    def get_inner_array_heap_ops(ops):
        # -> IHeapOps
        return InnerArrayHeapOps(ops)
    @override
    def add_name(ops, heap, name, key, payload):
        # -> new_idx
        # -> new_inner_pointer
        # add existing name
        if ops.exists(heap, name): raise KeyError(f'key exists: {name!r}')
        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        L = len(wrapped_obj_seq)

        unwrapped_obj = name, key, payload
        wrapped_obj = ops.wrap(unwrapped_obj, L)
        new_idx = ops.get_inner_array_heap_ops().push(
            wrapped_obj_seq, wrapped_obj, wrapped=True)
        name2wrapped_obj[name] = wrapped_obj
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        return new_idx

    @override
    def update_name(ops, heap, name, key, payload):
        # -> new_idx
        # -> new_inner_pointer
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
        new_idx = ops.get_inner_array_heap_ops().replace_at(
            wrapped_obj_seq, idx, new_wrapped_obj, wrapped=True)
        name2wrapped_obj[name] = new_wrapped_obj
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        return new_idx


    @override
    def pop_name(ops, heap, name):
        # -> unwrapped_obj
        if not ops.exists(heap, name): raise KeyError(f'key not exists: {name!r}')

        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)

        old_wrapped_obj = name2wrapped_obj[name]
        idx = ops.get_idx_of_wrapped_obj(old_wrapped_obj)

        old_unwrapped_obj = ops.get_inner_array_heap_ops().delete_at(
                    wrapped_obj_seq, idx, wrapped=False)
        del name2wrapped_obj[name]
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        return old_unwrapped_obj


    ##############

    @override
    def peek(ops, heap):
        # -> unwrapped_obj
        if ops.is_empty(heap): raise KeyError('peek empty heap')
        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        return ops.get_inner_array_heap_ops().peek(
            wrapped_obj_seq, wrapped=False)

    @override
    def pop_then_push_ex(ops, heap, name, key, payload):
        # -> unwrapped_obj
        if ops.is_empty(heap): raise KeyError('pop empty heap')
        #name_eq?????
        #if ops.peek(heap)[NAME_IDX] != name and ops.exists(heap, name):
        #    raise KeyError(f'key exists: {name!r} and not head name')
        new_name = name; del name

        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)

        result_unwrapped_obj = old_unwrapped_obj = ops.peek(heap)
        old_name = old_unwrapped_obj[NAME_IDX]
        del name2wrapped_obj[old_name]
        if new_name in name2wrapped_obj:
            # we have no "name_eq"
            #   , so cannot compare (old_name, new_name) at beginning
            #
            # rollback
            # restore
            old_wrapped_obj = ops.get_inner_array_heap_ops().peek(
                wrapped_obj_seq, wrapped=True)
            name2wrapped_obj[old_name] = old_wrapped_obj
            assert len(wrapped_obj_seq) == len(name2wrapped_obj)
            raise KeyError(f'key exists: {new_name!r} and not head name')


        new_unwrapped_obj = new_name, key, payload
        new_wrapped_obj = ops.wrap(new_unwrapped_obj, 0)
        name2wrapped_obj[new_name] = new_wrapped_obj
        old_wrapped_obj = ops.get_inner_array_heap_ops().pop_then_push(
            wrapped_obj_seq, new_wrapped_obj, wrapped=True)
        assert len(wrapped_obj_seq) == len(name2wrapped_obj)
        return result_unwrapped_obj


    @override
    def check_named_heap(ops, heap):
        # -> (None|raise ValueError)
        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        name2wrapped_obj = ops.get_name2wrapped_obj(heap)
        if len(wrapped_obj_seq) != len(name2wrapped_obj): raise ValueError('seq and dict have diff sizes')
        for i, wrapped_obj in enumerate(wrapped_obj_seq):
            if i != ops.get_idx_of_wrapped_obj(wrapped_obj): raise ValueError('idx2wrapped_obj: wrapped_obj.idx is wrong')
            name, key, payload = ops.unwrap(wrapped_obj)
            _wrapped_obj = name2wrapped_obj[name]
            if i != ops.get_idx_of_wrapped_obj(_wrapped_obj): raise ValueError('name2wrapped_obj: wrapped_obj.idx is wrong')


        # compare two wrapped_obj sets
        idc = list(map(ops.get_idx_of_wrapped_obj, name2wrapped_obj.values()))
        L = len(name2wrapped_obj)
        if not all(0 <= i < L for i in idc): raise ValueError('name2wrapped_obj: wrapped_obj.idx out-of-range; name2wrapped_obj and idx2wrapped_obj contain diff wrapped_objs')
        idx2count = [0]*L
        for i in idc:
            idx2count[i] += 1
        if not all(count==1 for count in idx2count): raise ValueError('name2wrapped_obj: wrapped_obj.idx out-of-range; name2wrapped_obj and idx2wrapped_obj contain diff wrapped_objs')
        if set(range(L)) != set(idc): raise ValueError('name2wrapped_obj: wrapped_obj.idx out-of-range; name2wrapped_obj and idx2wrapped_obj contain diff wrapped_objs')

        ops.get_inner_array_heap_ops().check_heap(wrapped_obj_seq)
        return None

    @override
    def make_unwrapped_obj_list(ops, heap):
        # -> [unwrapped_obj]
        # -> [(name, key, payload)]
        wrapped_obj_seq = ops.get_idx2wrapped_obj(heap)
        return list(map(ops.unwrap, wrapped_obj_seq))



########################################################################
########################################################################
########################InnerArrayHeapOps###############################
############################InnerSeq####################################
########################################################################
########################################################################
class InnerArrayHeapOps(IArrayHeapOps_ABC):#(, IHeapOps__with_IWrappedObjectOps):
    # non-static inner class inside INamedHeapOps_ABC
    typeof_outer_ops = INamedHeapOps_ABC
    #typeof_outer_ops = IWrappedObjectOpsEx
    def __init__(ops, outer_ops:typeof_outer_ops):
        ops.__outer_ops = outer_ops


    def set_idx_of_wrapped_obj(ops, wrapped_obj, idx):
        return ops.__outer_ops.set_idx_of_wrapped_obj(wrapped_obj, idx)
    @override
    def wrap_heap(ops, heap):
        # -> wrapped_obj_seq/idx2wrapped_obj
        #return ops.InnerSeq(ops, ops.outer_ops.get_idx2wrapped_obj(heap))
        #assume heap is wrapped_obj_seq
        return InnerSeq(ops, heap)
    @override
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        return ops.__outer_ops.can_be_parent_key_of(
            parent_wrapped_key, child_wrapped_key)

    if typeof_outer_ops is IWrappedObjectOpsEx:
        @override
        def get_wrapped_obj_ops(ops):
            return ops.__outer_ops
    else:
        @override
        def wrap(ops, unwrapped_obj, idx):
            return ops.__outer_ops.wrap(unwrapped_obj, idx)
        @override
        def unwrap(ops, wrapped_obj):
            return ops.__outer_ops.unwrap(wrapped_obj)
        @override
        def wrapped_obj2key(ops, wrapped_obj):
            return ops.unwrap(wrapped_obj)[KEY_IDX]


    def get_hash_state(ops):
        return type(ops), ops.__outer_ops
    @override
    def __eq__(ops, other):
        if type(ops) is not type(other):
            return False
            return NotImplemented
        return ops.__outer_ops == other.__outer_ops
    @override
    def __hash__(ops):
        return hash(ops.get_hash_state())

class InnerSeq(UserList):
    # non-static inner class inside INamedHeapOps_ABC.InnerArrayHeapOps
    def __init__(self, outer_self:InnerArrayHeapOps, seq):
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

InnerArrayHeapOps(None)

if __name__ == '__main__':
    XXX = INamedHeapOps_ABC

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)



