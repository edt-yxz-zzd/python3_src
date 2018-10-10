


__all__ = '''
    IHeapOps_ABC
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .IHeapOps import IHeapOps

class IHeapOps_ABC(IHeapOps):
    '''

types:
    unwrapped_obj :: a
        unwrapped obj
    wrapped_obj :: w
        wrapped obj
    key :: k
        used to compare by can_be_parent_key_of # __le__
    idx :: UInt # not allow negative integer
        0 <= idx < len(wrapped_obj_seq)
    heap
        the heap obj
    wrapped_obj_seq :: INOUT [w]
        wrapped obj seq

    xobj :: a|w
        xobj = unwrapped_obj|wrapped_obj
    wrapped :: Bool
        if wrapped:
            input/output xobj is wrapped_obj
        else:
            input/output xobj is unwrapped_obj



new_methods:
    `wrap_heap
    `wrap
    `unwrap
    `wrapped_obj2key
    `can_be_parent_key_of
    can_be_parent_wrapped_obj_of
    basic__can_be_parent_idx_of
    basic__swap
    to_parent_idx
    to_child_idc
    basic__make_heap_inplace
    basic__verify_heap
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
    basic__peek_at

    is_empty
    get_size

    can_be_parent_idx_of
    swap
    make_heap_inplace
    move_backward_at
    move_forward_at
    replace_at
    pop_then_push
    push_then_pop
    pop
    push
    delete_at
    peek_at

'''
    __slots__ = ()
    ###########################
    @not_implemented
    def wrap_heap(ops, heap):
        # heap -> wrapped_obj_seq
        #   get seq from heap-obj or wrap mutable-seq-view above heap-obj
        raise NotImplementedError
        wrapped_obj_seq = heap
        return wrapped_obj_seq

    def can_be_parent_wrapped_obj_of(ops, parent_wrapped_obj, child_wrapped_obj):
        parent_wrapped_key = ops.wrapped_obj2key(parent_wrapped_obj)
        child_wrapped_key = ops.wrapped_obj2key(child_wrapped_obj)
        return ops.can_be_parent_key_of(parent_wrapped_key, child_wrapped_key)
    def basic__can_be_parent_idx_of(ops, wrapped_obj_seq, parent_idx, child_idx):
        # assert 0 <= parent_idx == to_parent_idx(child_idx) < child_idx < len(wrapped_obj_seq)
        return ops.can_be_parent_wrapped_obj_of(
            wrapped_obj_seq[parent_idx], wrapped_obj_seq[child_idx])
    def basic__swap(ops, wrapped_obj_seq, parent_idx, child_idx):
        # assert 0 <= parent_idx == to_parent_idx(child_idx) < child_idx < len(wrapped_obj_seq)
        (wrapped_obj_seq[parent_idx], wrapped_obj_seq[child_idx]
        ) = wrapped_obj_seq[child_idx], wrapped_obj_seq[parent_idx]

    ####################

    def to_parent_idx(ops, child_idx):
        '''child_idx -> parent_idx

0 -> (1, 2)
1 -> (3, 4)
2 -> (5, 6)
3 -> (7, 8)
n -> (2*n+1, 2*n+2)
n = (N-1)//2
'''
        assert child_idx > 0
        return (child_idx-1)//2
    def to_child_idc(ops, parent_idx):
        # parent_idx -> (fst_child_idx, snd_child_idx)
        assert parent_idx >= 0
        first_child_idx = parent_idx*2+1
        second_child_idx = first_child_idx+1
        return (first_child_idx, second_child_idx)


    def basic__make_heap_inplace(ops, wrapped_obj_seq):
        '''heapify using sift_down; O(N)

https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
heapify using sift_down instead of sift_up

N = sum 2**i {i=0..n} = 2**(n+1)-1
floor_log2(N) = n
O(heapify-using-sift_down)
    = sum max-sift_down-steps[level] * num_nodes[level] {level}
    = sum max-distance-to-leaf[level] * num_nodes[level] {level}
    = sum (n - level) * 2**level {level=0..n}
    = sum n * 2**level {level=0..n}
    - sum level * 2**level {level=0..n}
    = n*N - sum level * 2**level {level=0..n}
    # D(x*e**x)/Dx = e**x + x*e**x
    # Integral (D(x*e**x)/Dx - e**x) Dx == Integral x*e**x Dx
    # x*e**x - e**x + C == Integral x*e**x Dx
    # let n*2**n *A - 2**n *B + C == sum level * 2**level {level=0..n}
    #   -B + C == 0
    #   2*A - 2*B + C == 2 == 2A-B
    #   8*A - 4*B + C == 10 == 8A-3B
    #   A=B=C=2
    # f(n) = (n-1)*2**(n+1) + 2 == sum level * 2**level {level=0..n}
    # f(0) = 0
    # f(n+1) - f(n) = 2*n*2**(n+1) - (n-1)*2**(n+1) = (n+1)*2**(n+1)
    = n*N - ((n-1)*2**(n+1) + 2)
    = n*N - ((n-1)*(N+1) + 2)
    = n*N - (n*N+n -N-1 + 2)
    = N-n-1
    = O(N)

O(heapify-using-sift_up)
    = sum max-sift_up-steps[level] * num_nodes[level] {level}
    = sum max-distance-to-root[level] * num_nodes[level] {level}
    = sum level * 2**level {level=0..n}
    = (n-1)*2**(n+1) + 2
    = (n-1)*(N+1) + 2
    = O(N*logN)
'''
        # ver2
        L = len(wrapped_obj_seq)
        if L < 2: return
        # L >= 2
        # L-1 >= 1
        max_child_idx = L-1
        assert max_child_idx > 0
        max_parent_idx = ops.to_parent_idx(max_child_idx)
        for parent_idx in range(max_parent_idx, -1, -1):
            ops.basic__move_backward_at(wrapped_obj_seq, parent_idx)
        assert ops.basic__verify_heap(wrapped_obj_seq)
        return

        # ver1 bug: forgot sift_down!!!!
        #for i in reversed(range(len(wrapped_obj_seq))) if i > 0:
        for child_idx in range(len(wrapped_obj_seq)-1, 0, -1):
            parent_idx = ops.to_parent_idx(child_idx)
            assert parent_idx < child_idx
            if not ops.basic__can_be_parent_idx_of(wrapped_obj_seq
                , parent_idx, child_idx):
                ops.basic__swap(wrapped_obj_seq, parent_idx, child_idx)
        assert ops.basic__verify_heap(wrapped_obj_seq)

    def basic__verify_heap(ops, wrapped_obj_seq):
        for child_idx in range(len(wrapped_obj_seq)-1, 0, -1):
            parent_idx = ops.to_parent_idx(child_idx)
            if not ops.basic__can_be_parent_idx_of(wrapped_obj_seq
                , parent_idx, child_idx):
                return False
        return True

    ####################

    def basic__move_backward_at(ops, wrapped_obj_seq, idx):
        # -> new_idx
        # sift_down
        assert 0 <= idx < len(wrapped_obj_seq)
        L = len(wrapped_obj_seq)
        if L < 2:
            return idx

        max_child_idx = L-1
        assert max_child_idx > 0
        max_parent_idx = ops.to_parent_idx(max_child_idx)
        max_parent_idx_has_only_one_child = bool(max_child_idx&1)
        if max_parent_idx_has_only_one_child:
            max_two_children_parent_idx = max_parent_idx - 1
        else:
            max_two_children_parent_idx = max_parent_idx

        def move_back(parent_idx):
            # -> new_idx
            # parent_idx has two children
            fst_child_idx, snd_child_idx = ops.to_child_idc(parent_idx)
            idc = [parent_idx, fst_child_idx, snd_child_idx]
            #idc.sort(key=)
            keys = [ops.wrapped_obj2key(wrapped_obj_seq[i]) for i in idc]
            [parent_key, fst_child_key, snd_child_key] = keys
            (next_parent_key, next_parent_idx) = (
                (fst_child_key, fst_child_idx)
                    if ops.can_be_parent_key_of(
                        fst_child_key, snd_child_key) else
                (snd_child_key, snd_child_idx)
                )
            if ops.can_be_parent_key_of(parent_key, next_parent_key):
                return parent_idx
            else:
                ops.basic__swap(wrapped_obj_seq, parent_idx, next_parent_idx)
                return next_parent_idx
        # end of move_back()

        parent_idx = idx; del idx
        while parent_idx <= max_two_children_parent_idx:
            new_idx = move_back(parent_idx)
            if new_idx == parent_idx:
                return new_idx
            parent_idx = new_idx

        if parent_idx > max_parent_idx:
            return parent_idx

        assert parent_idx == max_parent_idx
        assert max_two_children_parent_idx < max_parent_idx
        assert max_parent_idx_has_only_one_child

        # is_odd(max_child_idx)
        # max_parent_idx has only one child
        if ops.basic__can_be_parent_idx_of(wrapped_obj_seq
            , max_parent_idx, max_child_idx):
            return max_parent_idx
        ops.basic__swap(wrapped_obj_seq, max_parent_idx, max_child_idx)
        return max_child_idx


    def basic__move_forward_at(ops, wrapped_obj_seq, idx):
        # -> new_idx
        # sift_up
        assert 0 <= idx < len(wrapped_obj_seq)
        child_idx = idx; del idx
        #rint(f'wrapped_obj_seq={wrapped_obj_seq}')
        while child_idx:
            #rint(f'child_idx={child_idx}')
            parent_idx = ops.to_parent_idx(child_idx)
            if ops.basic__can_be_parent_idx_of(wrapped_obj_seq, parent_idx, child_idx):
                break
            ops.basic__swap(wrapped_obj_seq, parent_idx, child_idx)
            child_idx = parent_idx
        return child_idx


    ##############

    def xobj2wrapped_obj(ops, xobj, idx, *, wrapped):
        assert idx >= 0
        if wrapped:
            wrapped_obj = xobj
        else:
            unwrapped_obj = xobj
            wrapped_obj = ops.wrap(unwrapped_obj, idx)
        return wrapped_obj

    def basic__replace_at(ops, wrapped_obj_seq, idx, xobj, *, wrapped:bool):
        # xobj = unwrapped_obj|wrapped_obj
        # -> new_idx
        assert 0 <= idx < len(wrapped_obj_seq)
        wrapped_obj = ops.xobj2wrapped_obj(xobj, idx, wrapped=wrapped)
        wrapped_obj_seq[idx] = wrapped_obj

        new_idx = ops.basic__move_forward_at(wrapped_obj_seq, idx)
        if new_idx == idx:
            new_idx = ops.basic__move_backward_at(wrapped_obj_seq, idx)
        else:
            assert 0 <= new_idx < idx
        return new_idx



    ##############

    def wrapped_obj2xobj(ops, wrapped_obj, *, wrapped):
        # -> xobj
        if wrapped:
            xobj = wrapped_obj
        else:
            unwrapped_obj = ops.unwrap(wrapped_obj)
            xobj = unwrapped_obj
        return xobj


    def basic__pop_then_push(ops, wrapped_obj_seq, xobj, *, wrapped):
        # -> xobj
        assert wrapped_obj_seq
        wrapped = bool(wrapped)
        idx = 0
        result_wrapped_obj = wrapped_obj_seq[idx]
        result_xobj = ops.wrapped_obj2xobj(result_wrapped_obj, wrapped=wrapped)

        ops.basic__replace_at(wrapped_obj_seq, idx, xobj, wrapped=wrapped)
        return result_xobj

    def basic__push_then_pop(ops, wrapped_obj_seq, xobj, *, wrapped):
        # -> xobj
        wrapped = bool(wrapped)
        if not wrapped_obj_seq:
            return xobj

        idx = 0
        wrapped_obj = ops.xobj2wrapped_obj(xobj, idx, wrapped=wrapped)

        head_wrapped_obj = wrapped_obj_seq[idx]
        if ops.can_be_parent_wrapped_obj_of(wrapped_obj, head_wrapped_obj):
            result_wrapped_obj = wrapped_obj
        else:
            result_wrapped_obj = ops.basic__pop_then_push(
                        wrapped_obj_seq, wrapped_obj, wrapped=True)
            assert result_wrapped_obj is head_wrapped_obj

        result_xobj = ops.wrapped_obj2xobj(result_wrapped_obj, wrapped=wrapped)
        return result_xobj

    #################



    def basic__pop(ops, wrapped_obj_seq, *, wrapped):
        # -> xobj
        assert wrapped_obj_seq
        last_wrapped_obj = wrapped_obj_seq.pop()
        head_wrapped_obj = ops.basic__push_then_pop(
            wrapped_obj_seq, last_wrapped_obj, wrapped=True)
        head_xobj = ops.wrapped_obj2xobj(head_wrapped_obj, wrapped=wrapped)
        return head_xobj


    def basic__push(ops, wrapped_obj_seq, xobj, *, wrapped):
        # -> new_idx
        idx = len(wrapped_obj_seq)
        wrapped_obj = ops.xobj2wrapped_obj(xobj, idx, wrapped=wrapped)
        wrapped_obj_seq.append(wrapped_obj)
        return ops.basic__move_forward_at(wrapped_obj_seq, idx)

    #################

    def basic__delete_at(ops, wrapped_obj_seq, idx, *, wrapped):
        # -> xobj
        assert 0 <= idx < len(wrapped_obj_seq)
        result_wrapped_obj = wrapped_obj_seq[idx]
        result_xobj = ops.wrapped_obj2xobj(result_wrapped_obj, wrapped=wrapped)

        last_wrapped_obj = wrapped_obj_seq.pop()
        if idx == len(wrapped_obj_seq):
            assert last_wrapped_obj is result_wrapped_obj
            pass
        else:
            ops.basic__replace_at(wrapped_obj_seq, idx, last_wrapped_obj, wrapped=True)
        return result_xobj

    def basic__peek_at(ops, wrapped_obj_seq, idx, *, wrapped):
        # -> xobj
        assert 0 <= idx < len(wrapped_obj_seq)
        result_wrapped_obj = wrapped_obj_seq[idx]
        result_xobj = ops.wrapped_obj2xobj(result_wrapped_obj, wrapped=wrapped)
        return result_xobj




    #####################
    #####################
    #####################
    #####################
    #####################
    def is_empty(ops, heap):
        # -> bool
        wrapped_obj_seq = ops.wrap_heap(heap)
        return not wrapped_obj_seq
    def get_size(ops, heap):
        # -> UInt
        wrapped_obj_seq = ops.wrap_heap(heap)
        return len(wrapped_obj_seq)
    def can_be_parent_idx_of(ops, heap, parent_idx, child_idx):
        # assert 0 <= parent_idx == to_parent_idx(child_idx) < child_idx < len(wrapped_obj_seq)
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__can_be_parent_idx_of(wrapped_obj_seq, parent_idx, child_idx)
    def swap(ops, heap, parent_idx, child_idx):
        # assert 0 <= parent_idx == to_parent_idx(child_idx) < child_idx < len(wrapped_obj_seq)
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__swap(wrapped_obj_seq, parent_idx, child_idx)

    ####################

    def make_heap_inplace(ops, heap):
        '''heapify'''
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__make_heap_inplace(wrapped_obj_seq)


    ####################

    def move_backward_at(ops, heap, idx):
        # -> new_idx
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__move_backward_at(wrapped_obj_seq, idx)

    def move_forward_at(ops, heap, idx):
        # -> new_idx
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__move_forward_at(wrapped_obj_seq, idx)

    ##############

    def replace_at(ops, heap, idx, xobj, *, wrapped:bool):
        # xobj = unwrapped_obj|wrapped_obj
        # -> new_idx
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__replace_at(wrapped_obj_seq, idx, xobj, wrapped=wrapped)


    ##############

    def pop_then_push(ops, heap, xobj, *, wrapped):
        # -> xobj
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__pop_then_push(wrapped_obj_seq, xobj, wrapped=wrapped)

    def push_then_pop(ops, heap, xobj, *, wrapped):
        # -> xobj
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__push_then_pop(wrapped_obj_seq, xobj, wrapped=wrapped)

    #################



    def pop(ops, heap, *, wrapped):
        # -> xobj
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__pop(wrapped_obj_seq, wrapped=wrapped)

    def push(ops, heap, xobj, *, wrapped):
        # -> new_idx
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__push(wrapped_obj_seq, xobj, wrapped=wrapped)

    ###############

    def delete_at(ops, heap, idx, *, wrapped):
        # -> xobj
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__delete_at(wrapped_obj_seq, idx, wrapped=wrapped)

    def peek_at(ops, heap, idx, *, wrapped):
        # -> xobj
        wrapped_obj_seq = ops.wrap_heap(heap)
        return ops.basic__peek_at(wrapped_obj_seq, idx, wrapped=wrapped)






if __name__ == '__main__':
    XXX = IHeapOps_ABC

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


