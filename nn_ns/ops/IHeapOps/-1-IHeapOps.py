


__all__ = ['IHeapOps']
from .abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from .IOps import IOps

echo
operator
class IHeapOps(IOps):
    '''

input:
    xobj :: a|w
    unwrapped_obj :: a
        unwrapped obj
    wrapped_obj_seq :: INOUT [w]
        self == wrapped_obj_seq == heap
        wrapped obj seq
    wrap :: None|(a->UInt->w)
    key :: None|(w->k)
    __le__ :: None|(k->k->Bool)
    reverse :: Bool
    swap :: None|(INOUT [w] -> UInt -> UInt -> None)
        why?
            now, (swap+wrap)==>>we can add position_change_listener
            # maybe we should override wrapped_obj_seq.__setitem__??

    idx :: UInt # not allow negative integer
'''
    __slots__ = ()

    @classmethod
    def static_heap_std_kwargs(cls, *, key, __le__, reverse, swap):
        is_max_heap = bool(reverse)
        if key is None:
            key = echo
        if __le__ is None:
            __le__ = operator.__le__
        if is_max_heap:
            # max heap
            def is_well_key(parent_key, child_key):
                return __le__(child_key, parent_key)
        else:
            # min heap
            def is_well_key(parent_key, child_key):
                return __le__(parent_key, child_key)
            is_well_key = __le__
        def is_well_idx(wrapped_obj_seq, parent_idx, child_idx):
            return is_well_key(key(wrapped_obj_seq[parent_idx]), key(wrapped_obj_seq[child_idx]))

        if swap is None:
            def swap(wrapped_obj_seq, i, j):
                if i == j: return
                (wrapped_obj_seq[i], wrapped_obj_seq[j]
                ) = wrapped_obj_seq[j], wrapped_obj_seq[i]

        return key, is_well_key, is_well_idx, swap #, wrap


    @classmethod
    def static_to_parent_idx(cls, child_idx):
        assert child_idx > 0
        return (child_idx-1)//2
    @classmethod
    def static_to_child_idc(cls, parent_idx):
        assert parent_idx >= 0
        first_child_idx = parent_idx*2+1
        second_child_idx = first_child_idx+1
        return (first_child_idx, second_child_idx)

    @classmethod
    def static_heap_move_backward(cls, wrapped_obj_seq, idx, *, key, __le__, reverse, swap):
        # -> new_idx
        assert idx >= 0
        key, is_well_key, is_well_idx, swap = cls.static_heap_std_kwargs(
            key=key, __le__=__le__, reverse=reverse, swap=swap)

        L = len(wrapped_obj_seq)
        if L < 2:
            return idx

        max_child_idx = L-1
        assert max_child_idx > 0
        max_parent_idx = cls.static_to_parent_idx(max_child_idx)
        max_parent_idx_has_only_one_child = bool(max_child_idx&1)
        if max_parent_idx_has_only_one_child:
            max_two_children_parent_idx = max_parent_idx - 1
        else:
            max_two_children_parent_idx = max_parent_idx

        def move_back(parent_idx):
            # -> new_idx
            # parent_idx has two children
            fst_child_idx, snd_child_idx = cls.static_to_child_idc(parent_idx)
            idc = [parent_idx, fst_child_idx, snd_child_idx]
            #idc.sort(key=)
            keys = [key(wrapped_obj_seq[idx]) for idx in idc]
            [parent_key, fst_child_key, snd_child_key] = keys
            (next_parent_key, next_parent_idx) = (
                (fst_child_key, fst_child_idx)
                    if is_well_key(fst_child_key, snd_child_key) else
                (snd_child_key, snd_child_idx)
                )
            if is_well_key(parent_key, next_parent_key):
                return parent_idx
            else:
                swap(wrapped_obj_seq, parent_idx, next_parent_idx)
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
        if is_well_idx(wrapped_obj_seq, max_parent_idx, max_child_idx):
            return max_parent_idx
        swap(wrapped_obj_seq, max_parent_idx, max_child_idx)
        return max_child_idx


    @classmethod
    def static_heap_move_forward(cls, wrapped_obj_seq, idx, *, key, __le__, reverse, swap):
        # -> new_idx
        assert idx >= 0
        key, is_well_key, is_well_idx, swap = cls.static_heap_std_kwargs(
            key=key, __le__=__le__, reverse=reverse, swap=swap)

        child_idx = idx; del idx
        while child_idx:
            parent_idx = cls.static_to_parent_idx(child_idx)
            if is_well_idx(wrapped_obj_seq, parent_idx, child_idx):
                break
            swap(wrapped_obj_seq, parent_idx, child_idx)
            child_idx = parent_idx
        return child_idx

    @classmethod
    def static_heap_replace_at(cls, wrapped_obj_seq, idx, xobj, *, key, __le__, reverse, swap, wrap, wrapped):
        # -> new_idx
        assert idx >= 0
        wrapped_obj = cls.static_heap_may_wrap_obj(xobj, idx, wrap=wrap, wrapped=wrapped)
        wrapped_obj_seq[idx] = wrapped_obj

        new_idx = cls.static_heap_move_forward(wrapped_obj_seq, idx
            , key=key, __le__=__le__, reverse=reverse, swap=swap)
        if new_idx == idx:
            new_idx = cls.static_heap_move_backward(wrapped_obj_seq, idx
                , key=key, __le__=__le__, reverse=reverse, swap=swap)
        else:
            assert new_idx < idx
        return new_idx

    @classmethod
    def static_heap_may_wrap_obj(cls, xobj, idx, *, wrap, wrapped):
        assert idx >= 0
        if wrapped:
            wrapped_obj = xobj
        else:
            unwrapped_obj = xobj
            if wrap is None:
                def wrap(unwrapped_obj, idx):
                    wrapped_obj = unwrapped_obj
                    return wrapped_obj
            wrapped_obj = wrap(unwrapped_obj, idx)
        return wrapped_obj

    @classmethod
    def static_heap_pop_then_push(cls, wrapped_obj_seq, xobj, *, key, __le__, reverse, swap, wrap, wrapped):
        # -> wrapped_obj
        assert wrapped_obj_seq
        result = wrapped_obj_seq[0]
        cls.static_heap_replace_at(wrapped_obj_seq, 0, xobj
            , key=key, __le__=__le__, reverse=reverse, swap=swap
            , wrap=wrap, wrapped=wrapped)
        return result

    @classmethod
    def static_heap_push_then_pop(cls, wrapped_obj_seq, xobj, *, key, __le__, reverse, swap, wrap, wrapped):
        # -> wrapped_obj
        wrapped_obj = cls.static_heap_may_wrap_obj(xobj, 0, wrap=wrap, wrapped=wrapped)
        if not wrapped_obj_seq:
            return wrapped_obj

        key, is_well_key, is_well_idx, swap = cls.static_heap_std_kwargs(
            key=key, __le__=__le__, reverse=reverse, swap=swap)

        head = wrapped_obj_seq[0]
        if is_well_key(key(wrapped_obj), key(head)):
            return wrapped_obj
        return cls.static_heap_pop_then_push(wrapped_obj_seq, wrapped_obj
            , key=key, __le__=__le__, reverse=reverse, swap=swap
            , wrap=wrap, wrapped=True)
    @classmethod
    def static_heap_pop(cls, wrapped_obj_seq, *, key, __le__, reverse, swap):
        # -> wrapped_obj
        assert wrapped_obj_seq
        last = wrapped_obj_seq.pop()
        if not wrapped_obj_seq:
            head = last
            return head

        return cls.static_heap_pop_then_push(wrapped_obj_seq, last
            , key=key, __le__=__le__, reverse=reverse, swap=swap
            , wrap=None, wrapped=True)

    @classmethod
    def static_heap_push(cls, wrapped_obj_seq, xobj, *, key, __le__, reverse, swap, wrap, wrapped):
        L = len(wrapped_obj_seq)
        wrapped_obj = cls.static_heap_may_wrap_obj(xobj, L, wrap=wrap, wrapped=wrapped)
        wrapped_obj_seq.append(wrapped_obj)
        cls.static_heap_move_forward(wrapped_obj_seq, L
            , key=key, __le__=__le__, reverse=reverse, swap=swap)

    @classmethod
    def static_make_heap_inplace(cls, wrapped_obj_seq, *, key, __le__, reverse, swap):
        '''INOUT [w] -> (key::w->k) -> (__le__::k->k->Bool) -> (reverse::Bool) -> (swap::INOUT [w] -> UInt -> UInt -> None) -> None

# reverse = is_max_heap?
if reverse: max heap
else:       min heap


0 -> (1, 2)
1 -> (3, 4)
2 -> (5, 6)
3 -> (7, 8)
n -> (2*n+1, 2*n+2)
n = (N-1)//2
'''
        key, is_well_key, is_well_idx, swap = cls.static_heap_std_kwargs(
            key=key, __le__=__le__, reverse=reverse, swap=swap)
        #for i in reversed(range(len(wrapped_obj_seq))) if i > 0:
        for child_idx in range(len(wrapped_obj_seq)-1, 0, -1):
            parent_idx = cls.static_to_parent_idx(child_idx)
            assert parent_idx < child_idx
            #parent_key = key(wrapped_obj_seq[parent_idx])
            #child_key = key(wrapped_obj_seq[child_idx])
            if not is_well_idx(wrapped_obj_seq, parent_idx, child_idx):
                swap(wrapped_obj_seq, parent_idx, child_idx)

    @not_implemented
    def make_heap_inplace(ops, wrapped_obj_seq):

IHeapOps
