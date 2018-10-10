

__all__ = '''
    INamedHeapOps_ABC__more1
    WrappedObj
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps_ABC import INamedHeapOps_ABC, InnerHeapOps




class WrappedObj:
    def __init__(self, unwrapped_obj, idx):
        self.__obj = unwrapped_obj
        self.idx = idx
    @property
    def unwrapped_obj(self):
        return self.__obj


class INamedHeapOps_ABC__more1(INamedHeapOps_ABC):
    '''

wrapped_obj :: WrappedObj
'''
    __slots__ = ()
    ####################
    @not_implemented
    def make_heap_from_parts(ops, idx2wrapped_obj, name2wrapped_obj):
        # -> heap
        #idx2wrapped_obj is wrapped_obj_seq
        assert len(name2wrapped_obj) == len(idx2wrapped_obj)
        raise NotImplementedError
    @not_implemented
    def make_new_name_dict(ops):
        # -> Map name v
        raise NotImplementedError

    ####################

    @override
    def wrap(ops, unwrapped_obj, idx):
        return WrappedObj(unwrapped_obj, idx)
    @override
    def unwrap(ops, wrapped_obj:WrappedObj):
        return wrapped_obj.unwrapped_obj
    @override
    def set_idx_of_wrapped_obj(ops, wrapped_obj, idx):
        wrapped_obj.idx = idx
    @override
    def get_idx_of_wrapped_obj(ops, wrapped_obj, idx):
        return wrapped_obj.idx


    ####################

    @override
    def make_heap_from_iterable(ops, iter_unwrapped_objs):
        # Iter (name, key, payload) -> Heap
        idx2wrapped_obj = wrapped_obj_seq = []
        name2wrapped_obj = ops.make_new_name_dict()
        for idx, (name, key, payload) in enumerate(iter_unwrapped_objs):
            wrapped_obj = ops.wrap((name, key, payload), idx)

            name2wrapped_obj[name] = wrapped_obj
            wrapped_obj_seq.append(wrapped_obj)
            if len(name2wrapped_obj) != len(idx2wrapped_obj):
                raise KeyError(f'key duplicated in make_heap_from_iterable: {name!r}')
        assert len(name2wrapped_obj) == len(idx2wrapped_obj)

        ops.get_inner_heap_ops().make_heap_inplace(wrapped_obj_seq)
        return ops.make_heap_from_parts(idx2wrapped_obj, name2wrapped_obj)

if __name__ == '__main__':
    XXX = INamedHeapOps_ABC__more1

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


