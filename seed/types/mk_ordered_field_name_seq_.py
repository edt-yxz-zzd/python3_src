#__all__:goto
r'''[[[
e ../../python3_src/seed/types/mk_ordered_field_name_seq_.py



used in NamedTupleBase/ImmutableNamespaceBase.__init_subclass__()
    view ../../python3_src/seed/types/NamedTupleBase.py
    view ../../python3_src/seed/types/ImmutableNamespaceBase.py




seed.types.mk_ordered_field_name_seq_
py -m nn_ns.app.debug_cmd   seed.types.mk_ordered_field_name_seq_ -x
py -m nn_ns.app.doctest_cmd seed.types.mk_ordered_field_name_seq_:__doc__ -ff -v
py_adhoc_call   seed.types.mk_ordered_field_name_seq_   @f

from seed.types.mk_ordered_field_name_seq_ import mk_ordered_field_name_seq_, mk_field_name2default_
#]]]'''
__all__ = r'''
    mk_ordered_field_name_seq_
    mk_field_name2default_
'''.split()#'''
__all__

from seed.verify.common_verify import is_Sequence
from seed.tiny import ifNone, MapView

def mk_ordered_field_name_seq_(cls, *
    , ordered_field_name_seq=None
    , type2ordered_field_name_seq=None
    , type_field_name4ordered_field_name_seq=None
    ):
    'cls -> may [x] -> may (cls->[x]) -> may type_field_name -> ordered_field_name_seq/[x] #used in NamedTupleBase/ImmutableNamespaceBase.__init_subclass__()'
    if not 1 == sum(x is not None for x in [ordered_field_name_seq, type2ordered_field_name_seq, type_field_name4ordered_field_name_seq]): raise TypeError

    if not (ordered_field_name_seq is None
            or is_Sequence(ordered_field_name_seq)): raise TypeError
    if not (type2ordered_field_name_seq is None
            or callable(type2ordered_field_name_seq)): raise TypeError
    if not (type_field_name4ordered_field_name_seq is None
            or type(type_field_name4ordered_field_name_seq) is str): raise TypeError
    #if ordered_field_name_seq is None or iter(ordered_field_name_seq):

    if ordered_field_name_seq is not None:
        pass
    elif type2ordered_field_name_seq is not None:
        # callable
        ordered_field_name_seq = type2ordered_field_name_seq(cls)
    elif type_field_name4ordered_field_name_seq is not None:
        # str
        type_field_name = type_field_name4ordered_field_name_seq
        ordered_field_name_seq = getattr(cls, type_field_name)
    else:
        raise logic-err

    # verify result of cls->ordered_field_name_seq
    if not is_Sequence(ordered_field_name_seq): raise TypeError

    ordered_field_name_seq = tuple(ordered_field_name_seq)
    return ordered_field_name_seq


def mk_field_name2default_(ordered_field_name_seq, /, *
    , field_name2default=None
    , field_defaults=()
    #, field_defaults=None
        # mimic: py.namedtuple._field_defaults
        #   right align
    ):
    field_name_set = frozenset(ordered_field_name_seq)

    #if not 1 >= sum(not x is None for x in [field_name2default, field_defaults])
    field_name2default = ifNone(field_name2default, {})
    field_defaults = ifNone(field_defaults, [])

    num_fields_without_defaults = len(ordered_field_name_seq) - len(field_defaults)
    if not num_fields_without_defaults >= 0: TypeError('too long: "field_defaults"')

    _1_field_name2default = dict(zip(ordered_field_name_seq[num_fields_without_defaults:], field_defaults))




    unknown_keys = (field_name2default.keys() - field_name_set)
    if unknown_keys: raise TypeError(unknown_keys)


    overlap_keys = field_name2default.keys() & _1_field_name2default.keys()
    if overlap_keys: raise TypeError(overlap_keys)

    _2_field_name2default = {**field_name2default, **_1_field_name2default}
    assert _2_field_name2default.keys() <= field_name_set
    assert len(_2_field_name2default) == len(field_name2default) + len(_1_field_name2default)

    field_name2default = MapView(_2_field_name2default)
    return field_name2default



from seed.types.mk_ordered_field_name_seq_ import mk_ordered_field_name_seq_, mk_field_name2default_
from seed.types.mk_ordered_field_name_seq_ import *
