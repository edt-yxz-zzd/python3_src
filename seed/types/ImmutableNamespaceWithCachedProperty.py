TODO
#__all__:goto
r'''[[[
e ../../python3_src/seed/types/ImmutableNamespaceWithCachedProperty.py


seed.types.ImmutableNamespaceWithCachedProperty
py -m nn_ns.app.debug_cmd   seed.types.ImmutableNamespaceWithCachedProperty -x
py -m nn_ns.app.doctest_cmd seed.types.ImmutableNamespaceWithCachedProperty:__doc__ -ff -v
py_adhoc_call   seed.types.ImmutableNamespaceWithCachedProperty   @f
from seed.types.ImmutableNamespaceWithCachedProperty import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from seed.graph.DAG import iter_sorted_topological_ordering, list_a_cycle_or_sorted_topological_ordering
from seed.graph.U2Vtc_To_DigraphABC import ObjU2Vtc_To_Digraph, IntU2Vtc_To_Digraph

#def mk_kwds5args_ex(nms, nm_ls, args, kwds, /):
def update_kwargs5args__emplace_(kwds, nms, nm_ls, args, /):
    assert len(nms) == len(nm_ls)

    if not len(args) <= len(nm_ls): raise TypeError((len(args), len(nm_ls)))
    kwds5args = dict(zip(nm_ls, args))
    if (duplicated_nms := kwds5args.keys() & kwds): raise TypeError(duplicated_nms)
    _nms = nms - kwds5args.keys()
    if not len(_nms) == len(nms) -len(args): raise TypeError(mismatched_nms := set(nm_ls) ^ nms)
    kwds.update(kwds5args)
    return
    return (kwds5args, _nms)
def patch_kwargs5defaults__emplace_(kwds, nms, nm2default, /):
    if (extra_nms := kwds.keys() -nms): raise TypeError(extra_nms)
    if (missing_nms := (default_nms := nms -kwds.keys()) -nm2default.keys()): raise TypeError(missing_nms)
    L0 = len(kwds)
    L1 = len(default_nms)
    kwds.update((nm, nm2default[nm]) for nm in default_nms)
    L2 = len(kwds)
    assert L0 + L1 == L2
    assert kwds.keys() == nms
    return
def convert_kwargs__emplace_(kwds, io_nms__ex_inms__converter__triples, /):
    for io_nms, ex_inms, converter in io_nms__ex_inms__converter__triples:
        io = {nm:kwds[nm] for nm in io_nms}
        ex = {nm:kwds[nm] for nm in ex_inms}
        output = converter(**io, **ex)
        if not len(output) == len(io_nms): raise TypeError((io_nms, ex_inms, converter))
        output[:0]
        io_nms[:0]
        kwds.update(zip(io_nms, output))
    return
def check_kwargs_(kwds, inms__checker__pairs, /):
    for inms, checker in inms__checker__pairs:
        input = {nm:kwds[nm] for nm in inms}
        checker(**input)
    return
class ImmutableNamespaceWithCachedProperty:
    r'''[[[
    inheritance...
    default input
    prefix convert input
    postfix check input
    lazy multi-cached property/error
        strict at init donot allow error
    instance method
    classmethod-constructor-mk5...
        repr without cached property
        ???show_verbose with cached property
            validate cached property???
    delta-data
        new attribute names

dict for vars
key/symbol via instance:
    external attached attribute
name via instance:
    core required attribute name seq
        #required_input_attribute_name_seq
    optional:
        arbitrary_one cached property or checkable input attribute or default
        #optional_input_attribute_name_seq
        #is_default_value? for repr??
    standardize_converter
    strict cached property
        #strict_initial_attribute_name_seq
    lazy cached property/exception
        intermediate hidden multi-property/exception
        #attribute_name2attribute_group
        #attribute_group2maker_info
            #maker_info = (maker, input_name_seq, output_name_seq)
                #args include id? hash? ...external attached attribute???
    instance_method
    class_method
        lazy/strict class_property/data
    static_method
        static_property/data
name via class:
    base classes
    converters
    checkers
    defaults

    #]]]'''#'''
    @classmethod
    def _2_get_attribute_name_seq_2_(cls, /):
        '-> Tuple nm'
    @classmethod
    def _2_get_attribute_name_set_2_(cls, /):
        '-> FrozenSet nm'
    @classmethod
    def _2_get_defaults_2_(cls, /):
        '-> FrozenDict nm default'
    @classmethod
    def _2_get_converters_2_(cls, /):
        '-> [(inoutput/[nm], extra_input/[nm], converter)]'
    @classmethod
    def _2_get_checkers_2_(cls, /):
        '-> [(input/[nm], checker)]'
    def _1_get_mutable_vars_1_(sf, /):
        '-> {nm:value}'
        return vars(sf)
    def _2_prepare4new_2_(cls
        ,args, kwds
        ,required_input_attribute_name_seq
        ,optional_input_attribute_name_seq
        ,strict_initial_attribute_name_seq
        ,attribute_name2attribute_group
        ,attribute_group2maker_info
            #maker_info = (maker, input_name_seq, output_name_seq)
        ):

    def __new__(cls, /, *args, **kwds):
        nm_ls = cls._2_get_attribute_name_seq_2_()
        nms = cls._2_get_attribute_name_set_2_()
        nm2default = cls._2_get_defaults_2_()
        #(kwds5args, _nms) = mk_kwds5args_ex(nms, nm_ls, args, kwds)
        #patch_kwargs5defaults__emplace_(kwds, _nms, nm2default)
        update_kwargs5args__emplace_(kwds, nms, nm_ls, args)
        patch_kwargs5defaults__emplace_(kwds, nms, nm2default)

        io_nms__ex_inms__converter__triples = cls._2_get_converters_2_()
        convert_kwargs__emplace_(kwds, io_nms__ex_inms__converter__triples)
        inms__checker__pairs = cls._2_get_checkers_2_()
        check_kwargs_(kwds, inms__checker__pairs)

        sf = super(__class__, cls).__new__(cls)
        d = cls._1_get_mutable_vars_1_(sf)
        d.update(kwds)
        return sf
    __init_subclass__
        build cls.data
    __getattribute__
    __setattr__
    __getattr__
    __delattr__
    __dir__
    __repr__
    _show_verbose_

from seed.graph.DAG import iter_local_sorted_topological_ordering, list_a_cycle_or_local_sorted_topological_ordering

from seed.graph.DAG import validate_topological_ordering_, validate_local_sorted_topological_ordering__local_neighbor_pair_only_

from enum import Enum, auto
class OperatorKind(Enum):
    #variable source: input OR maker; THEN converter
    MAKER = auto()
    DELTA_UPDATER = auto()
    CONVERTER = auto()
    CONVERTER_AND_MAKER = auto()
    CHECKER = auto()
class AttributeNameRole(Enum):
    IRRELEVANT = auto()
    IN = auto()
    INOUT = auto()
    OUT = auto()

#order:
#   inter names per operator: f(in0, in1, ..., /, inout0, inout1, ...) -> (out0, out1, ...)
#   inter operators per name: sorted_cases4per_name
sorted_cases4per_name = [OUT, INOUT, IN]
    #[OUT, INOUT, IN]
    #[(MAKER, OUT), (DELTA_UPDATER, INOUT), (CONVERTER, INOUT), (CHECKER, IN)]
    #[IN, INOUT, OUT]
(op, op_kind, arg_name, nm_role, mro_idx)

e ../../python3_src/seed/math/primality_proving.py
def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__


from seed.types.ImmutableNamespaceWithCachedProperty import *
