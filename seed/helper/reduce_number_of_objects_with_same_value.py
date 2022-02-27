
#'''
#################################
#[[[__doc__-begin
r'''

seed.helper.reduce_number_of_objects_with_same_value
py -m seed.helper.reduce_number_of_objects_with_same_value
py -m nn_ns.app.debug_cmd   seed.helper.reduce_number_of_objects_with_same_value


from seed.helper.reduce_number_of_objects_with_same_value import mk_new_register_point, get_or_mk_named_register_point, StdValue2FastKeyWrapper, Value2Weakable, get_or_register_the_std_obj_with_same_value_at, is3_the_std_obj_with_same_value_at, get_the_std_obj_with_same_value_at, SpecialKeyByNonHashable, SpecialKey, ALL_KEYS


if value_obj is not weakable:
    register_name = ...
    value_obj = ...
    standardize_all_subobj4weakable_value_obj = ...
    weakable_value_obj = Value2Weakable(value_obj)
    del value_obj
    register_point = get_or_mk_named_register_point(register_name)
    std_weakable_value_obj = get_the_std_obj_with_same_value_at(register_point, weakable_value_obj)
        #std_weakable_value_obj = get_or_register_the_std_obj_with_same_value_at(register_point, weakable_value_obj, standardize_all_subobj=standardize_all_subobj4weakable_value_obj)
    del weakable_value_obj
    std_value_obj = std_weakable_value_obj.the_value_obj
    ##################################
    ######using std_value_obj but hold std_weakable_value_obj
    #################################
if value_obj is weakable:
    register_name = ...
    value_obj = ...
    standardize_all_subobj4value_obj = ...
    register_point = get_or_mk_named_register_point(register_name)
    std_value_obj = get_the_std_obj_with_same_value_at(register_point, value_obj)
        #std_weakable_value_obj = get_or_register_the_std_obj_with_same_value_at(register_point, value_obj, standardize_all_subobj=standardize_all_subobj4value_obj)
    del value_obj
    #################################
    #####using&hold std_value_obj
    #################################
if use std_value_obj as mapping key:
    #use wrapped_std_value_obj instead
    wrapped_std_value_obj = StdValue2FastKeyWrapper(std_weakable_value_obj)




减少同一值的重复对象
reduce_num_of_objs_with_same_value
reduce_number_of_objects_with_same_value
    #weak_point2weak_value2itself
    #or: register_point.weak_value2itself
    register_point = get_or_mk_named_register_point(name_key)
    register_point = mk_new_register_point()
    value_obj = get_the_std_obj_with_same_value_at(register_point, value_obj)
    Value2Weakable
    weak_value = weakref.ref(Value2Weakable(value_obj))
    from weakref import WeakKeyDictionary


=====
Several built-in types such as list and dict do not directly support weak references but can add support through subclassing:
CPython implementation detail: Other built-in types such as tuple and int do not support weak references even when subclassed.



######################################
######################################


#[[[doctest_examples-begin
>>>
...
#]]]doctest_examples-end
#'''
#]]]__doc__-end

#################################
__all__ = '''
    mk_new_register_point
    get_or_mk_named_register_point
    StdValue2FastKeyWrapper
    Value2Weakable
    get_or_register_the_std_obj_with_same_value_at
    is3_the_std_obj_with_same_value_at
    get_the_std_obj_with_same_value_at

    SpecialKeyByNonHashable
        SpecialKey
        ALL_KEYS

    '''.split()
#################################



import weakref#WeakKeyDictionary, ref
from seed.mapping_tools.fdefault import mapping_set_fdefault__cxxxvalue_
#def mapping_set_fdefault__cxxxvalue_(mapping, key, imay_xdefault_rank, xdefault, /,*, get_vs_pop, try_vs_Nothing_vs_in):





class _RegisterPoint:
    __slots__ = ('_d',)
    def __init__(sf, /):
        sf._d = weakref.WeakKeyDictionary()
    def __eq__(sf, ot, /):
        return sf is ot
    def __hash__(sf, /):
        return id(sf)

_name_key2register_point = {}

def mk_new_register_point():
    register_point = _RegisterPoint()
    return register_point
def get_or_mk_named_register_point(name_key, /):
    (is_old_value, xvalue) = mapping_set_fdefault__cxxxvalue_(_name_key2register_point, name_key, 0, mk_new_register_point, get_vs_pop=False, try_vs_Nothing_vs_in=None)
    register_point = xvalue
    assert type(register_point) is _RegisterPoint
    return register_point



from seed.abc.eq_by_id.AddrAsHashWrapper import AddrAsHashWrapper as StdValue2FastKeyWrapper
def _xxx():
  #comment out
  class StdValue2FastKeyWrapper:
    __slots__ = ('_v',)
    __doc__ = r'''
    since the std value is unique
        we neednot to hash/eq too heavy
        ie replace by id/is

        eg.
            register_point :: {weakref<std_value_obj>: weakref<std_value_obj>}
            may update to register_point :: {weakref<std_value_obj>: weakref<wrapped_std_value_obj>}
                but not faster, only when wrap the key of dict
            ====
            old_version_d :: {std_value_obj: ...}
            new_version_d :: {wrapped_std_value_obj: ...}
                #faster!!!
    #'''
    def __new__(cls, value_obj, /):
        if cls is not StdValue2FastKeyWrapper: raise TypeError
        sf = object.__new__(StdValue2FastKeyWrapper)
        if type(sf) is not StdValue2FastKeyWrapper: raise TypeError
        StdValue2FastKeyWrapper.___init___(sf, value_obj)
        return sf
    def ___init___(sf, value_obj, /):
        sf._v = value_obj
    def __eq__(sf, ot, /):
        #bug: return sf is ot
        return sf._v is ot._v
    def __hash__(sf, /):
        #bug:return id(sf)
        return id(sf._v)
    @property
    def the_value_obj(sf, /):
        return sf._v
    def __call__(sf, /):
        return sf._v



class Value2Weakable:
    __slots__ = ('_v', '_h',)
    __doc__ = r'''
    see below: _try_builtins_weakable()
        ok_ls=[frozenset(), set(), TypeError, repr, type]
        bad_ls=[(), '', b'', 1, True, None, Ellipsis, NotImplemented, [], {}]
    #'''
    def __new__(cls, value_obj, /):
        if cls is not Value2Weakable: raise TypeError
        sf = object.__new__(Value2Weakable)
        if type(sf) is not Value2Weakable: raise TypeError
        Value2Weakable.___init___(sf, value_obj)
        return sf
    def ___init___(sf, value_obj, /):
        sf._v = value_obj
        sf._h = hash((type(sf), value_obj))
    def __eq__(sf, ot, /):
        #bug:return sf._h == ot._h and sf._v == ot._v
        return type(sf) is type(ot) and sf._h == ot._h and sf._v == ot._v
    def __hash__(sf, /):
        return sf._h
    @property
    def the_value_obj(sf, /):
        return sf._v
    def __call__(sf, /):
        return sf._v

def _try_builtins_weakable():
    ls = [
        frozenset()
        ,()
        ,''
        ,b''
        ,1
        ,True
        ,None
        ,...
        ,NotImplemented
        ######################
        ,[]
        ,{}
        ,set()
        ,TypeError
        ,repr
        ,type
        ]
    ok_ls = []
    bad_ls = []
    for a in ls:
        try:
            weakref.ref(a)
        except TypeError as e:
            #print(f'{type(a)}: {a!r}')
            #print(f'   {e}')
            bad_ls.append(a)
        else:
            ok_ls.append(a)
    #print(f'ok_ls={ok_ls}')
    #print(f'bad_ls={bad_ls}')
    assert ok_ls==[frozenset(), set(), TypeError, repr, type]
    assert bad_ls==[(), '', b'', 1, True, None, Ellipsis, NotImplemented, [], {}]
if __name__ == "__main__":
    _try_builtins_weakable()





r'''failure: user should hold weakable_value_obj himself
def get_the_std_obj_with_same_value_at(register_point, value_obj, /):
    wrapped_value_obj = Value2Weakable(value_obj)
    weak_wrapped_value2itself = register_point._d
    weak_value = weakref.ref(Value2Weakable(value_obj))
#'''
def is3_the_std_obj_with_same_value_at(register_point, weakable_value_obj, /):
    '-> [-1..+1]; -1 std_obj not exist yet; 0 input_obj is std_obj; +1 input_obj is not std_obj'
    weak_value2itself = register_point._d
    may_ref = weak_value2itself.get(weakable_value_obj)
    if may_ref is None:
        return -1
    ref = may_ref
    std_value_obj = ref()
    return 0 if weakable_value_obj is std_value_obj else +1
def get_the_std_obj_with_same_value_at(register_point, weakable_value_obj):
    'raise KeyError if not found'
    weak_value2itself = register_point._d
    ref = weak_value2itself[weakable_value_obj]
        #may raise KeyError here
    del weakable_value_obj
    std_value_obj = ref()
    return std_value_obj
def get_or_register_the_std_obj_with_same_value_at(register_point, weakable_value_obj, /,*, standardize_all_subobj):
    #cannot use mapping_set_fdefault__cxxxvalue_ here!!!
    #   "key is value" not "value=standardize_all_subobj(key)"
    weak_value2itself = register_point._d
    may_ref = weak_value2itself.get(weakable_value_obj)
    if may_ref is None:
        reduced_weakable_value_obj = standardize_all_subobj(weakable_value_obj)
        del weakable_value_obj
        std_value_obj = _get_or_register_the_std_obj_with_same_value_at(register_point, weakable_value_obj_____whose_subobj_are_all_standardized=reduced_weakable_value_obj)
        del reduced_weakable_value_obj
    else:
        del weakable_value_obj
        ref = may_ref
        std_value_obj = ref()
    return std_value_obj
def _get_or_register_the_std_obj_with_same_value_at(register_point, /,*, weakable_value_obj_____whose_subobj_are_all_standardized):
    r'''
    bug: once named _get_or_register_the_std_obj_with_same_value_at as get_the_std_obj_with_same_value_at
    why is bug?
        when there are multi-levels to reduce/standardize
        #key is hashable#may be mutable if eq==is
        #   nonstd means may not cached in some-a-register_point
        #   std means known cached in some-a-register_point
        #
        #
        nonstd_key -> std_key
            #ok
        nonstd_set<std_key> -> std_set<std_key>
            #ok
        nonstd_set<nonstd_key> -> std_set<nonstd_key>
            #bug!!!
    #'''
    weak_value2itself = register_point._d
    weakable_value_obj = weakable_value_obj_____whose_subobj_are_all_standardized
    #ref = weak_value2itself.setdefault(weakable_value_obj, weakref.ref(weakable_value_obj))
    ref = mapping_set_fdefault__cxxxvalue_(weak_value2itself, weakable_value_obj, 0, lambda:weakref.ref(weakable_value_obj), get_vs_pop=False, try_vs_Nothing_vs_in=None)
        #since assign both (key,value)
        #   should avoid (nonstd-k, std-v)
        #   so, cannot use standardize_all_subobj here!
    std_value_obj = ref()
    return std_value_obj

class SpecialKey:
    r'''non_hashable but immutable'

    #SpecialKeyByNonHashable
    #SpecialKey
    #   通常 默认允许功能不断增加，但不允许减少。其实，禁止某些功能的增加，也很重要。
    #   del d[ALL_KEYS] # "ALL_KEYS" is not hashable to distinguish normal hashable key. that is the way to create special keys.
    #     # slice is unhashable
            >>> {}[:]
            Traceback (most recent call last):
                ...
            TypeError: unhashable type: 'slice'

    special_keys = ...
    wrapped_special_keys = {*map(StdValue2FastKeyWrapper, special_keys)}
    special_key_id2method = {
        id(ALL_KEYS): on_all_keys
        ,...
        }
    def __setitem__(sf, key, value, /):
        if getattr(type(key), '__hash__', None) is None:
            if id(key) in __class__.special_key_id2method:
                ...
    #'''
    def __init__(sf, description, /):
        sf._description = description
    __hash__ = None
    def __eq__(sf, ot, /):
        return sf is ot
    def __repr__(sf, /):
        return f'{__class__.__name__!s}({sf._description!r})'
SpecialKeyByNonHashable = SpecialKey
ALL_KEYS = SpecialKeyByNonHashable("ALL_KEYS")


TODO:
    #
    #SpecialKeyByNonHashable
    #   del d[ALL_KEYS] # "ALL_KEYS" is not hashable to distinguish normal hashable key. that is the way to create special keys.
    #   通常 默认允许功能不断增加，但不允许减少。其实，禁止某些功能的增加，也很重要。
    #
    #
    #TODO: global_funcs -> ops.funcs
    #   to avoid global naming conflict
    #       why not use unamed register_point?
    #           <<== global_type_fmt_style_register_point_name
    #
    #
    #TODO: global_type_fmt_style_register_point_name
    #   system naming by obj-type
    #
    #
    #TODO: is3 update to is for faster detection
    #   register_point add .weak_value_dict<weakref<wrapped_std>, std>
    #   or: weakref.finialize/override __setitem__ + set<id<std> >
    #
    #
    is_std<xxx>
    to_std<xxx>
        #mk/get
        xxx =
            fkey
            wsfkey_set
            ...
    is_std__fkey(fkey) == is_std_("sfkey", fkey)
        #"sfkey" local name
    local_register_point_name2global_type_fmt_style_register_point_name
        local_register_point_name =
            "sfkey"
            "wsfkey_sset"
            "wsfkey_s2wsfkey_sset"
            "wsfkey_wsset_s2sfkey"
        global_type_fmt_style_register_point_name example:
            #str - key
            #Value2Weakable<str> - fkey
            #get_or_register_the_std_obj_with_same_value_at$<Value2Weakable<str> > - sfkey
            #StdValue2FastKeyWrapper<get_or_register_the_std_obj_with_same_value_at$<Value2Weakable<str> > > - wsfkey
            #
            #
            #using 3 builtins ops:
            #   id4hash$
            #   std$
            #   weakable$
            #
            #
            #whole global name should startswith "std$"
            #   frozenset[id4hash$std$...]
            #   FrozenDict[id4hash$std$...,std$...]
            "std$weakable$str"
            "std$frozenset[id4hash$std$weakable$str]"
            "std$FrozenDict[id4hash$std$weakable$str,std$frozenset[id4hash$std$weakable$str]]"
            "std$FrozenDict[id4hash$std$frozenset[id4hash$std$weakable$str,std$weakable$str]]"

