
r'''
call by
    ops[qsymbol, kw_ex:arg, ...]
    all method inform:
        def f(..., /,*, qsymbol2arg)

constraint on subclass
    constraint on single kw/qsymbol
        subclass.kwarg <= super.kwarg
            __le__/topo_partial_le/ipcmp
        conflict/collision resolve:
            pseudo_min/topo_lower_bound(superA.kwarg, superB.kwarg)
                virtual topo_lower_bound subclass
    dict 4 class def
        OrderedDict<name, ([tuple<x>], [x])>
            +modified_order:growonly_seq<(name, i, j)>
            save all overwrited/deleted value

qsymbol vs bsymbol
    qual/absolute vs base/bare/relative
    when class defining, cls is not exist yet
        we can only has bsymnol not qsymbol
    xsymbol = qsymbol | bsymnol
    kxsymbol = qsymbol | bsymnol | kw_name
    kqsymbol = qsymbol | kw_name
bsymbol
    = (area_name, attr_name)
    = (area_name, attr_name, kw_name)
qsymbol
    = (cls, area_name, attr_name)
        4 param/var/attr
    | (cls, area_name, attr_name, kw_name)
        4 kw of collaboration_method
            collaboration_method
                unordered
                class_inherit_topo_partial_ordered
                    #all need not super()
                    normal:
                        super_last
                        super_first
                    yield twice:
                        super_between #vivi __new__/__init__
                        super_around #???


private_method

    def f(private_area_getattr, protected_area_getattr, sf, ...):


_f:
    protected?
    __f:
        private?
___f___#3:
    raw_method
    protected?
    final f() yield twice: one 4 call, one 4 return
    of_class_only_and_access_via_cls
    _____f_____#5:
        4 delta_method_per_class
        of_class_only_and_access_via_cls_dict

____f____#4:
    ____init_subclass____
    ____init____
    ____new____
        yield twice
        result == (inited?, sf_or_obj)
    forbid override __init__/__new__/__init_subclass__
        but allow override ____init____/____new____/____init_subclass____
    final __init__
        _____check_self_____(sf)
            #unordered_collaboration_method
        _____check_self__super_last_____(sf)
            #super_last_class_inherit_topo_partial_ordered_collaboration_method
        _____check_self__super_first_____(sf)
            #super_first_class_inherit_topo_partial_ordered_collaboration_method

    final __new__
        inited, sf = ____new____(...)
        if not inited:
            check_type_is(cls, sf)
            m = ____init____(sf, ...)
            check_is_None(m)
            sf.__dict__ = view
    final __init_subclass__
        #all collaboration_method:
        ____init_subclass____
        ____check_subclass____
        ____check_subclass__super_last____
        ____check_subclass__super_first____



class constraint
    final? tribool?
    abstract? tribool
    eqv xsymbol delta



all_base_class_set :: functional set impl #finger_tree/red_black_tree
calc mro.#reorder by hand
property(value/theobj) or functional_impl_detail/pseudo_method(anobj)
    of class or obj_or_class
    init...
    eqv group...
    cache/optional by value/calc
    constraint
    mutable?

qsymbol2arg = mapping<(qsymbol, arg)|(subcls, bsymbol2arg)>


attr_decl =
    (of_class_only|of_class_only_and_access_via_cls|of_class_only_and_access_via_cls_dict|of_instance_or_class
    , mutable|readonly|immutable of payload obj/value itself
    , final/overridable?
    , may constraint4this_attr
    , property_spec_decl|functional_impl_detail_decl
    , tmay_default_arg__or__xsymbol_frozenset2calc
    )
    constraint4subclass_at_this_property
        sometimes 'is' is not allow
        sometimes must be overrided
    tmay_default_arg__or__xsymbol_frozenset2calc or put at ___get_delta_xsymbol2tmay_default_arg___
property_spec_decl =
    (setattr_ok4of_instance?
    , value/theobj/anobj
    , may topo_partial_le4subclass_at_this_property
    , may topo_lower_bound4subclass_at_this_property
    )
functional_impl_detail_spec_decl =
    (free_function(staticmethod|free_function_of_instance_only)|classmethod|instancemethod|instance_property|class_property|decriptor|...
    , ordered_collaboration_method_chain|delta_method_per_class
    setattr_ok===False
    anobj
    delta_method_per_class:
        order:
            unordered
                unordered_collaboration_method
            class_inherit_topo_partial_ordering
                not (yield twice)
                e.g. collaboration_method+unordered/super_last/super_first, but not super_between/super_around
                input side: from lower/subcls to upper/super
                output side: from upper/super to lower/subcls
            mro??? no!
        e.g.
            delta check
            delta get_config/setting
            delta init
            delta output
        input side:
            collaboration_method
            +xsymbol_decl 4 kwargs
                dispatch
        output side:
            delta_arg4unorder_collector+unorder_collector
                unorder_collector=set/multiset/decomposable<unorder_collector>(tuple_as_pointunorder_collector,...>, mapping_as_record<k~unorder_collector, ...>)|commutable_binary_op(add/min/...)/...


class C(IOps):
@mk_IOps(delta_equivalence_relationship=...
    ,is_final_class=...
    ,is_abstract_class=...
    )
class C(...):
    class classwise(delta bsymbol2decl???):
        ____delta_equivalence_relationship____ :: [(kxsymbol, kxsymbol)]
    class public(delta bsymbol2decl???):
        attr = attr_decl
        attr = attr_decl
        attr = attr_decl
        @decl4def_new_method(
            ,kw=attr_decl[kw]
            ,kw=attr_decl[kw]
            ,final=?
            ,abstract=?
            )
        def attr(..., /,*, qsymbol2arg):

        # collaboration_method
        @collaboration_method_decl4method(may xsymbol #qsymbol@override, may attr@def_new_qsymbol4method
            ,order=unordered|super_last|...
            #for qsymbol2arg
                ,kxsymbol2tmay_default # 4 qsymbol2arg
                ,kxsymbol2decl
            ,idx2decl
            ,decl4args
            ,decl4kwargs
            )
        def attr(..., sf, qsymbol2arg, ..., /,*):

        #############below is bad###############
        or:
        @class_as_method_setting
        class attr(..., __dict__=from_xxxx):
            @_def_
            def attr(...):#__class__???
            @_kw_
            class _kw2decl_(...):
                kw = kw_decl
                kw = kw_decl
                kw = kw_decl
                kw = kw_decl

    class protected(???):
    class private(???):
#'''
class IOps(ABC):
    @classmethod
    def xsymbol2stdrepr_qsymbol(cls, defining_cls, xsymbol):
        'defining_cls -> xsymbol -> qsymbol'
        ,,,
    @classmethod
    def kxsymbol2stdrepr_kqsymbol(cls, defining_cls, area, attr, kxsymbol):
        'defining_cls -> area -> attr -> kxsymbol -> kqsymbol'
        ,,,
    if 0:
        r"""[
        @classmethod
        @delta_method_per_class
        @abstractmethod
        def ___get_public_bsymbol2decl___(cls, /):
            'new public member@__class__ attr_decl'
        @classmethod
        @delta_method_per_class
        @abstractmethod
        def ___get_protected_bsymbol2decl___(cls, /):
            'new protected member@__class__ attr_decl'
        @classmethod
        @delta_method_per_class
        @abstractmethod
        def ___get_private_bsymbol2decl___(cls, /):
            'new private member@__class__ attr_decl'
        @classmethod
        @delta_method_per_class
        @abstractmethod
        def ___get_delta_xsymbol2tmay_default_arg___(cls, /):
            r'''tmay_default_arg__or__xsymbol_frozenset2calc :: (tmay x | Map<xsymbol_frozenset, (cls -> decl_cls -> xsymbol2arg -> x)>)#signature
            cls 4 classmethod calc
            decl_cls 4 [xsymbol2arg ==>> qsymbol2arg]
            '''

        @classmethod
        @delta_method_per_class
        @abstractmethod
        def ___get_delta_xsymbol_frozenset2check_func___(cls, /):
            'check order = sz from 0 to +oo'
        def __init_subclass__(cls, /,*, base_class_set, qsymbol2arg):
        @classmethod
        @abstractmethod
        def ___check_possible_default_args4subclass___(cls, /,*, qsymbol2arg):
        #"""[

    def __init_subclass__(cls, /,*, base_class_set):
        area_ex2inner_cls = cls.__dict__ = MapView/mk_FrozenDict(cls.__dict__)
            #setattr forbidden
        area_names = (*'public protected private'.split(),)
        other_names = (*'classwise'.split(),)
        if not set(area_ex2inner_cls) <= set(area_names): raise TypeError
        #public_attr2decl = area_ex2inner_cls['public'].__dict__
        #protected_attr2decl = area_ex2inner_cls['protected'].__dict__
        #private_attr2decl = area_ex2inner_cls['private'].__dict__
            #attr2decl
        def main():
            for area_name in area_names:
                handle__area(area_name, area_ex2inner_cls)
            handle__classwise(area_ex2inner_cls)

        def handle__classwise(area_ex2inner_cls):
            attr2decl = area_ex2inner_cls['classwise'].__dict__
            . .
        def handle__area(area_name, area_ex2inner_cls):
            #__class__!
            attr2decl = area_ex2inner_cls[area_name].__dict__
            #del attr2decl['__class__']
            each method __closure__
                __class__
                    is __defining_class__
                ____public_area____
                ____protected_area____
                ____private_area____
            if not all(type(attr) is str for attr in attr2decl): raise TypeError
            #if not all(isinstance(decl, AllDeclTypes4IOps) for decl in attr2decl.values()): raise TypeError
            if not all(type(decl) in AllDeclTypes4IOps for decl in attr2decl.values()): raise TypeError
            . .
        #end of def handle__area(area_name, area_ex2inner_cls):
        main()
    #end of def __init_subclass__(cls, /,*, base_class_set):


AllDeclTypes4IOps = (
