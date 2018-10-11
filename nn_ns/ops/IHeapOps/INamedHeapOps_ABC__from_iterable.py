

__all__ = '''
    INamedHeapOps_ABC__from_iterable
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps__from_iterable import INamedHeapOps__from_iterable
from .INamedHeapOps_ABC import INamedHeapOps_ABC
#from seed.tiny import print_err



class INamedHeapOps_ABC__from_iterable(INamedHeapOps_ABC, INamedHeapOps__from_iterable):
    '''
'''
    __slots__ = ()
    #################
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

    ####################

    @override
    def make_heap_from_iterable(ops, iter_unwrapped_objs):
        # Iter (name, key, payload) -> Heap
        it = iter(iter_unwrapped_objs); del iter_unwrapped_objs

        idx2wrapped_obj = wrapped_obj_seq = []
        name2wrapped_obj = ops.make_new_name_dict()
        for idx, (name, key, payload) in enumerate(it):
            wrapped_obj = ops.wrap((name, key, payload), idx)

            name2wrapped_obj[name] = wrapped_obj
            wrapped_obj_seq.append(wrapped_obj)
            if len(name2wrapped_obj) != len(idx2wrapped_obj):
                raise KeyError(f'key duplicated in make_heap_from_iterable: {name!r}')
        assert len(name2wrapped_obj) == len(idx2wrapped_obj)

        #print_err(list(map(ops.unwrap, wrapped_obj_seq)))
        ops.get_inner_array_heap_ops().make_array_heap_inplace(wrapped_obj_seq)
        #print_err(list(map(ops.unwrap, wrapped_obj_seq)))
        return ops.make_heap_from_parts(idx2wrapped_obj, name2wrapped_obj)



if __name__ == '__main__':
    XXX = INamedHeapOps_ABC__from_iterable

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)



