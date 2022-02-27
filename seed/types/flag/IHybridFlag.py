#################################
#[[[__doc__-begin
r'''
xxTODO
    DONE: all keys are legal+NO_CONSTRAINTS
    No: case cmp by is?? singleton per instance?

seed.types.flag.IHybridFlag
py -m seed.types.flag.IHybridFlag
py -m nn_ns.app.debug_cmd   seed.types.flag.IHybridFlag
py -m nn_ns.app.debug_cmd   seed.types.flag.IHybridFlag  > $my_tmp/out4py/seed.types.flag.IHybridFlag.4.__all__.txt
    echo $my_tmp/out4py/seed.types.flag.IHybridFlag.4.__all__.txt
    view /sdcard/0my_files/tmp//out4py/seed.types.flag.IHybridFlag.4.__all__.txt
from seed.types.flag.IHybridFlag import \
    (get_view_of_active_key_set_of_hybrid_flag
        ,IHybridFlag
        ,HybridFlagBaseError
        ,Flag__discrete_mutex_groups_only_ie_no_key_pair_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
        ,Case__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
        ,Case__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
    ,mk_k2minfo_ex__from_mgroups_without_cgroups
        ,IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str
        ,case4hybrid_flag_constraint__IProposition
        ,case4hybrid_flag_constraint__ALL_STARMAP_SIMPLE_VAR_IMPLY
        ,case4hybrid_flag_constraint__NO_CONSTRAINTS
        ,case4hybrid_flag_constraint__NotImplemented
        ,ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str
        ,IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str
    )
    #see:example_classes: HybridFlag4test, HybridFlag4test_constraints, Flag4test, Case4test, Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only
    #from seed.types.logic.ZerothOrderLogic import IProposition, ICachedEnvironment, eval_proposition_at_configuration__tribool, ICachedEnvironment__cache_is_dict
        # prop.eval_at_configuration__bool
    #from seed.types.logic.ZerothOrderLogic import SIMPLE_VAR_IMPLY, AND, OR, XOR, XNOR, IMPLY, FLIP_IMPLY, TOTAL
    #from seed.types.logic.ZerothOrderLogic import VAR, NOT, NOT_VAR, the_FALSE, the_TRUE, the_YET, ERROR, EvalError




e ../../python3_src/seed/types/flag/IHybridFlag.py
    see:
        e ../../python3_src/seed/types/flag/Flag.py
        seed.types.flag.Flag

1. 约束 与 互斥 区别:
    hybrid_flag << keys
        自动清空互斥标志
    比如：声明 a b 互斥
        expr1 ::= ((hybrid_flag << [a]) << [b])
            第二个『<<』由b导致清除a
        如果 只是在 约束中 表达 [a => not b][b => a]，则 expr1 认为 a b 是不互斥的标志，试图同时 激活，最终 在构造对象时 被 约束 阻止，以抛出异常的方式
        前一种 正常执行，清除a
        后一种 抛出异常

2. 概念性错误
    互斥 并非 等价关系，而是 两不同标志之间的关系，不该使用 等价划分

    {legal_key:互斥群的集合}
        互斥群的集合
        = {(互斥区, 取消互斥, 互斥区, 取消互斥, , ...)}
            理论上，无需 三层以上（含）
        ={互斥区:{取消互斥:互斥群的集合}}

    两两关系，但一一列举十分繁琐，检查约束也耗时长久
        用 整个组 内部 两两互斥 来简化列举与检查
        显然，同一 合法键 可出现在不同的 互斥组 中
        legal_key2mutex_group_name_set
        if legal_key2mutex_group_name_set[a] & legal_key2mutex_group_name_set[b]:
            # a b 同属于 某些 互斥组
            ==>> a b 互斥
        存在 互斥组X，[a,b<-X][a!=b] ==>> [a,b 互斥]

    如何 表达 集合A与集合B的元素之间 两两互斥，但，集合内部 并不两两互斥？
        声明 取消互斥 的 取消组
            取消组 是 互斥组 的 依赖性下级概念，只取消特定 互斥组 声明的互斥关系，并不 影响 其他 互斥组 的 声明
        legal_key2mutex_group_name_cancel_group_name_pair_set
            {legal_key:{(mutex_group_name,cancel_group_name)}}
            <==>{legal_key:{mutex_group_name:{cancel_group_name}}}
        原先:两个键 属于 同一个 互斥组，则 互斥
        变成:两个键 属于 同一个 互斥组，且 同属于 该互斥组的某个 取消组，则 本互斥组 取消 对 此两键 的 互斥声明
    ====
    一般的，泛化后，我们有:
        合法键互斥归组信息={合法键:互斥组信息}
        互斥组信息={互斥组:取消组信息}
        取消组信息={取消组:互斥组信息}
            #递归
        极大组名路径<合法键> =[def]= (互斥组,取消组,...,某组名) 当 合法键互斥归组信息[互斥组][取消组][...][某组名]=={}

        #两个合法键互斥的判定条件:
        def 两个合法键互斥 合法键a 合法键b = a != b && 某个互斥组起作用 合法键互斥归组信息[a] 合法键互斥归组信息[b]
        def 某个互斥组起作用 互斥组信息X 互斥组信息Y = any(not (某个取消组起作用 X[g] Y[g]) | 互斥组g <- X/-\Y)
        def 某个取消组起作用 取消组信息P 取消组信息Q = any(not (某个互斥组起作用 P[g] Q[g]) | 取消组g <- P/-\Q)



cancel

alias, not-, deduce-



gvim:
    /cls[.]\w*([^s]
    #       )
    should be:
        cls.fff(sf, ...)



#[[[doctest_examples-begin
see:
    class _doctest_examples___IHybridFlag:
    class _doctest_examples___from_deprecated_old_Flag:
#]]]doctest_examples-end
#'''
#]]]__doc__-end

#################################
    #see:example_classes: HybridFlag4test, HybridFlag4test_constraints, Flag4test, Case4test, Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only
__all__ = '''
get_view_of_active_key_set_of_hybrid_flag
    IHybridFlag
    HybridFlagBaseError

    Flag__discrete_mutex_groups_only_ie_no_key_pair_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
    Case__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
    Case__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str

mk_k2minfo_ex__from_mgroups_without_cgroups
    IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str

    case4hybrid_flag_constraint__IProposition
    case4hybrid_flag_constraint__ALL_STARMAP_SIMPLE_VAR_IMPLY
    case4hybrid_flag_constraint__NO_CONSTRAINTS
    case4hybrid_flag_constraint__NotImplemented

    ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str
    IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str



ICachedEnvironment__env_is_hybrid_flag
    CachedEnvironment__env_is_hybrid_flag
Helper4HybridFlag___mutex
_View___k2minfo












HybridFlagBaseError
    ObjNotKeyError
    KeyNotLegalError
        KeyNotLegalError_AttributeError
    LegalKeysNotMutex
    LegalKeysNotSatisfiedConstraintsError





IHybridFlag
    get_view_of_active_key_set_of_hybrid_flag

    IHybridFlag__using_mutext_cancel_group
        mk_k2minfo_ex__from_mgroups_without_cgroups
        Helper4HybridFlag___mutex

    IHybridFlag__legal_keys_are_finite
    IHybridFlag__key_is_str
    IHybridFlag__instance_state_is_active_keys_only

    IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only
        abstract___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
        abstract___of_obj_at_cls__the_partial_legal_key2mgroup_info___

        IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str


    IHybridFlag__all_keys_are_legal

    IHybridFlag__active_keys_constraints_check_nonempty_only
        ICase__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints
            Case__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str

    IHybridFlag__without_active_keys_constraints
        IHybridFlag__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only
            IHybridFlag__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
    IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex
        Flag__discrete_mutex_groups_only_ie_no_key_pair_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
    ICase__single_mutex_group_only_ie_pairwise_key_mutex
        ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only
            Case__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str


    IHybridFlag__active_keys_constraints_using_ZerothOrderLogic
        ICachedEnvironment__env_is_hybrid_flag
            CachedEnvironment__env_is_hybrid_flag

        IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls
            abstract___of_obj_at_cls__the_proposition4active_keys_constraints___

            IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only
                IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str

                IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only
                    Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only
                        case4hybrid_flag_constraint__IProposition
                        case4hybrid_flag_constraint__ALL_STARMAP_SIMPLE_VAR_IMPLY
                        case4hybrid_flag_constraint__NO_CONSTRAINTS
                        case4hybrid_flag_constraint__NotImplemented

                    ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only
                        ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str

                    IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only
                        IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str




    '''.split()
    #_View___k2minfo
    #_View___recur_mapping_value_is_mapping
    #
    #
    #see:example_classes: HybridFlag4test, HybridFlag4test_constraints, Flag4test, Case4test, Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only
    #
    #
#################################

___begin_mark_of_excluded_global_names__0___ = ...



import operator as opss # __or__, __and__, __sub__
import collections # defaultdict
import collections.abc # Mapping


import itertools # chain, starmap
#from seed.helper.repr_input import repr_helper
#from seed.types.FrozenDict import FrozenDict
from seed.helper.AttrCollector import AttrCollector
from seed.abc.abc import abstractmethod, override # , ABC
from seed.abc.IReprImmutableHelper import IReprImmutableHelper

from seed.tiny import mk_tuple, mk_frozenset, null_frozenset, null_mapping_view, null_iter, print_err
from seed.types.view.View import SetView, MapView
from seed.types.logic.ZerothOrderLogic import IProposition, ICachedEnvironment, ICachedEnvironment__cache_is_dict # , eval_proposition_at_configuration__tribool
    # prop.eval_at_configuration__bool
#from seed.types.logic.ZerothOrderLogic import ALL_STARMAP_SIMPLE_VAR_IMPLY, SIMPLE_VAR_IMPLY, AND, OR, XOR, XNOR, IMPLY, FLIP_IMPLY, TOTAL
#from seed.types.logic.ZerothOrderLogic import VAR, NOT, NOT_VAR, the_FALSE, the_TRUE, the_YET, ERROR, EvalError
from seed.types.logic.ZerothOrderLogic import the_TRUE, ALL_STARMAP_SIMPLE_VAR_IMPLY

___end_mark_of_excluded_global_names__0___ = ...



#class xxxObjNotBoolError(TypeError):pass
#class xxxObjNotFrozensetError(TypeError):pass
class HybridFlagBaseError(Exception):pass
class ObjNotKeyError(HybridFlagBaseError, TypeError):pass
class KeyError_AttributeError(KeyError, AttributeError):pass
class KeyNotLegalError(HybridFlagBaseError, KeyError):pass
class KeyNotLegalError_AttributeError(KeyNotLegalError, KeyError_AttributeError):pass
_KeyError_AttributeError = KeyError_AttributeError
del KeyError_AttributeError

class LegalKeysNotMutex(HybridFlagBaseError, ValueError):pass
class LegalKeysNotSatisfiedConstraintsError(HybridFlagBaseError, ValueError):pass





def get_view_of_active_key_set_of_hybrid_flag(hybrid_flag, /):
    cls = type(hybrid_flag)
    view_of_active_key_set = cls.get_view_of_active_key_set(hybrid_flag)
    return view_of_active_key_set
class IHybridFlag(IReprImmutableHelper):
    r'''
    key typing:
        active_key <: legal_key <: possible_key <: obj
        if not possible_key: raise ObjNotKeyError
        if not legal_key: raise KeyNotLegalError
            #__getattribute__:KeyNotLegalError_AttributeError

    finite:
        given hybrid_flag: finite active_keys
        given (hybrid_flag, legal_key): finite mutex_grouping_info 互斥组信息
    #'''
    __slots__ = ()

    #################################
    #################################
    #IReprImmutableHelper
    #   ___get_args_kwargs___
    #   ___get_args_kwargs4repr___
    #

    @abstractmethod
    def ___check__obj_is_key___(sf, obj, /):
        'check__obj_is_key #ObjNotKeyError'
    @abstractmethod
    def ___is_key_legal___(sf, key, /):
        'is_key_legal #NOTE:extra_legal_keys4not_mutex_with_others/discrete/isolated'
        # +k2minfo#合法键互斥归组信息
        # +extra_legal_keys4discrete_mutex_groups
    @abstractmethod
    def ___get_view_of_active_key_set___(sf, /):
        'get_view_of_active_key_set'
    @abstractmethod
    def ___immutable_replace__whole_active_keys_configuration___(sf, valid_active_keys_configuration, /):
        'immutable_replace__whole_active_keys_configuration #validded'
    @abstractmethod
    def ___iter_findout_lhs_legal_keys_not_mutex_between___(sf, lhs_legal_key_set, rhs_legal_key_set, /):
        'iter_findout_lhs_legal_keys_not_mutex_between #Helper4HybridFlag___mutex'
    @abstractmethod
    def ___iter_findout_legal_keys_not_mutex_insides___(sf, legal_key_set, /):
        'iter_findout_legal_keys_not_mutex_insides #Helper4HybridFlag___mutex'
    @abstractmethod
    def ___check__legal_key_set_satisfy_active_keys_constraints___besides_mutex___(sf, legal_key_set, /):
        'check__legal_key_set_satisfy_active_keys_constraints___besides_mutex #LegalKeysNotSatisfiedConstraintsError'

    #################################
    #################################
    #################################
    #################################

    def check__obj_is_key(sf, obj, /):
        r'''
        obj -> None
            if not possible_key: raise ObjNotKeyError
        #'''
        cls = type(sf)
        cls.___check__obj_is_key___(sf, obj)
    def check__objs_are_keys(sf, objs, /):
        r'''
        Iter obj -> None
            if not possible_key: raise ObjNotKeyError
        #'''
        cls = type(sf)
        for obj in objs:
            cls.check__obj_is_key(sf, obj)
                #raise ObjNotKeyError

    def check__objs_are_legal_keys(sf, objs, /):
        r'''
        Iter obj -> None
            if not possible_key: raise ObjNotKeyError
            if not legal_key: raise Error
        #'''
        cls = type(sf)
        if not all(cls.is_key_legal(sf, obj) for obj in objs): raise KeyNotLegalError

    def is_key_legal(sf, key, /):
        r'''
        key -> bool
        obj -> bool
            if not possible_key: raise ObjNotKeyError
        #'''
        cls = type(sf)
        cls.check__obj_is_key(sf, key)
            #raise ObjNotKeyError
        return cls.___is_key_legal___(sf, key)

    def is_legal_key_active(sf, legal_key, Error, /):
        r'''
        legal_key -> bool
        obj -> bool
            if not possible_key: raise ObjNotKeyError
            if not legal_key: raise Error

        why Error not simply KeyNotLegalError?
            hasattr() depends on AttributeError
            so, using KeyNotLegalError_AttributeError
        #'''
        cls = type(sf)
        if not cls.is_key_legal(sf, legal_key):
            ### not possible_key
            #raise ObjNotKeyError
            ### not legal_key
            raise Error
        view_of_active_key_set = cls.___get_view_of_active_key_set___(sf)
        return legal_key in view_of_active_key_set

    def get_view_of_active_key_set(sf, /):
        r'''
        -> view_of_active_key_set
        #'''
        cls = type(sf)
        view_of_active_key_set = cls.___get_view_of_active_key_set___(sf)
        return view_of_active_key_set

    def escape__legal_key2attr(sf, legal_key, /):
        'legal_key -> attr/identifier'
        raise NotImplementedError
    def unescape__attr2as_legal_key(sf, attr_as_legal_key, /):
        'attr -> obj/as_legal_key #unescape'
        return attr_as_legal_key

    def immutable_replace__whole_active_keys_configuration__fvalue(sf, fvalue, /, *args, **kwargs):
        r'''
        #mk_hybrid_flag based on sf besides active_keys
        #
        (fvalue :: view_of_active_key_set -> legal_keys/as_active_keys) -> (*args) -> (**kwargs) -> hybrid_flag
            #active_keys as configuration
        #'''
        cls = type(sf)
        view_of_active_key_set = cls.get_view_of_active_key_set(sf)
        legal_keys_as_active_keys = fvalue(view_of_active_key_set, *args, **kwargs)
        hybrid_flag = cls.immutable_replace__whole_active_keys_configuration(sf, legal_keys_as_active_keys)
        return hybrid_flag

    def immutable_replace__whole_active_keys_configuration(sf, legal_keys_as_active_keys, /):
        r'''
        #mk_hybrid_flag based on sf besides active_keys
        #
        legal_keys/as_active_keys -> hybrid_flag
            #active_keys as configuration
        #'''
        cls = type(sf)
        legal_key_frozenset = mk_frozenset(legal_keys_as_active_keys)
        del legal_keys_as_active_keys
        cls.check__legal_key_frozenset_is_valid_active_keys_configuration(sf, legal_key_frozenset)
        valid_active_keys_configuration = legal_key_frozenset
        hybrid_flag = cls.___immutable_replace__whole_active_keys_configuration___(sf, valid_active_keys_configuration)
        return hybrid_flag

    def immutable_overwrite__active_keys_configuration(sf, legal_keys_to_del, legal_keys_to_set, /,*, allow_illegal_keys4to_del:bool):
        r'''
        #mk_hybrid_flag based on sf with active_keys
        #
        legal_keys_to_del -> legal_keys_to_set/as_extra_new_active_keys -> hybrid_flag

        vs immutable_replace__whole_active_keys_configuration:
            * replace:
                valid<active_keys_configuration> legal_keys_as_active_keys
                    raise if findout_legal_keys_not_mutex_insides(legal_keys_as_active_keys)
                new_sf.active_keys = legal_keys_as_active_keys
                    #replace whole here

            * overwrite:
                raise if (legal_keys_to_del & legal_keys_to_set)
                raise if findout_legal_keys_not_mutex_insides(legal_keys_to_set)
                new_active_keys = sf.active_keys - legal_keys_to_del
                new_active_keys -= findout_lhs_legal_keys_not_mutex_between(new_active_keys, legal_keys_to_set)
                    #overwrite not_mutex_keys here
                new_active_keys |= legal_keys_to_set
                valid<active_keys_configuration> new_active_keys
                new_sf.active_keys = new_active_keys
        #'''
        cls = type(sf)
        (legal_keys_to_del, legal_keys_to_set) = map(mk_frozenset, [legal_keys_to_del, legal_keys_to_set])

        if 1:
            if legal_keys_to_del:
                if allow_illegal_keys4to_del:
                    cls.check__objs_are_keys(sf, legal_keys_to_del)
                else:
                    cls.check__objs_are_legal_keys(sf, legal_keys_to_del)

            if legal_keys_to_set:
                cls.check__objs_are_legal_keys(sf, legal_keys_to_set)

            if legal_keys_to_del & legal_keys_to_set: raise ValueError('to del&set same key at same time')
            cls.check__legal_key_set_are_pairwise_mutex(sf, legal_keys_to_set)
        #
        #
        view_of_active_key_set = cls.get_view_of_active_key_set(sf)
        new_active_key_frozenset = mk_frozenset(view_of_active_key_set) - legal_keys_to_del
        new_active_key_frozenset -= cls.findout_lhs_legal_keys_not_mutex_between(sf, new_active_key_frozenset, legal_keys_to_set)
            #overwrite not_mutex_keys here
        new_active_key_frozenset |= legal_keys_to_set

        hybrid_flag = cls.immutable_replace__whole_active_keys_configuration(sf, new_active_key_frozenset)
        return hybrid_flag

    def iter_findout_lhs_legal_keys_not_mutex_between(sf, lhs_legal_key_set, rhs_legal_key_set, /):
        'lhs_legal_key_set -> rhs_legal_key_set -> Iter<legal_key@lhs>'
        len(lhs_legal_key_set)
        len(rhs_legal_key_set)
        cls = type(sf)
        return cls.___iter_findout_lhs_legal_keys_not_mutex_between___(sf, lhs_legal_key_set, rhs_legal_key_set)
    def iter_findout_legal_keys_not_mutex_insides(sf, legal_key_set, /):
        'legal_key_set -> Iter<legal_key>'
        len(legal_key_set)
        cls = type(sf)
        return cls.___iter_findout_legal_keys_not_mutex_insides___(sf, legal_key_set)

    def findout_lhs_legal_keys_not_mutex_between(sf, lhs_legal_key_set, rhs_legal_key_set, /):
        'lhs_legal_key_set -> rhs_legal_key_set -> frozenset<legal_key@lhs>'
        cls = type(sf)
        it = cls.iter_findout_lhs_legal_keys_not_mutex_between(sf, lhs_legal_key_set, rhs_legal_key_set)
        return mk_frozenset(it)
    def findout_legal_keys_not_mutex_insides(sf, legal_key_set, /):
        'legal_key_set -> frozenset<legal_key>'
        cls = type(sf)
        it = cls.iter_findout_legal_keys_not_mutex_insides(sf, legal_key_set)
        return mk_frozenset(it)




    def check__legal_key_frozenset_is_valid_active_keys_configuration(sf, legal_key_frozenset, /):
        if not type(legal_key_frozenset) is frozenset: raise TypeError
        cls = type(sf)
        cls.check__objs_are_legal_keys(sf, legal_key_frozenset)
        cls.check__legal_key_set_are_pairwise_mutex(sf, legal_key_frozenset)
        cls.check__legal_key_set_satisfy_active_keys_constraints___besides_mutex(sf, legal_key_frozenset)

    def check__legal_key_set_are_pairwise_mutex(sf, legal_key_set, /):
        'legal_key_set -> None|raise LegalKeysNotMutex/ObjNotKeyError/KeyNotLegalError'
        cls = type(sf)
        it = cls.iter_findout_legal_keys_not_mutex_insides(sf, legal_key_set)
        for _ in it:
            raise LegalKeysNotMutex
        return
    def check__legal_key_set_satisfy_active_keys_constraints___besides_mutex(sf, legal_key_set, /):
        r'''
        legal_key_set -> None|raise LegalKeysNotSatisfiedConstraintsError/ObjNotKeyError/KeyNotLegalError

        valid satisfy constraints
            but not valid mutex
        #'''
        len(legal_key_set)
        cls = type(sf)
        cls.___check__legal_key_set_satisfy_active_keys_constraints___besides_mutex___(sf, legal_key_set)

    #################################
    #################################
    #################################
    #################################
    # IReprImmutableHelper:
    #   __repr__
    #   __eq__
    #   __hash__
    #
    def __getattribute__(sf, attr_as_legal_key, /):
        '-> (unescape__attr2as_legal_key(attr) in active_keys)'
        cls = type(sf)
        as_legal_key = cls.unescape__attr2as_legal_key(sf, attr_as_legal_key)
        return cls.is_legal_key_active(sf, as_legal_key, KeyNotLegalError_AttributeError)
        return sf[attr_as_legal_key]
    def __getitem__(sf, legal_key, /):
        '-> (legal_key in active_keys)'
        cls = type(sf)
        return cls.is_legal_key_active(sf, legal_key, KeyNotLegalError)
    def __contains__(sf, key, /):
        '-> (key in legal_keys)'
        cls = type(sf)
        return cls.is_key_legal(sf, key)
    def __bool__(sf, /):
        '-> len(active_keys)'
        cls = type(sf)
        view_of_active_key_set = cls.get_view_of_active_key_set(sf)
        return bool(view_of_active_key_set)
    def __len__(sf, /):
        '-> len(active_keys)'
        cls = type(sf)
        view_of_active_key_set = cls.get_view_of_active_key_set(sf)
        return len(view_of_active_key_set)
    def __iter__(sf, /):
        '-> Iter active_key'
        cls = type(sf)
        view_of_active_key_set = cls.get_view_of_active_key_set(sf)
        return iter(view_of_active_key_set)

    # | & << - **
    def __or__(sf, legal_keys, /):
        legal_keys = mk_frozenset(legal_keys)
        cls = type(sf)
        #return cls.immutable_set_opOR_configuration_of_hybrid_flag(sf, legal_keys)
        return cls.immutable_replace__whole_active_keys_configuration__fvalue(sf, opss.__or__, legal_keys)
    def __and__(sf, legal_keys, /):
        cls = type(sf)
        #return cls.immutable_set_opAND_configuration_of_hybrid_flag(sf, legal_keys)
        legal_keys = mk_frozenset(legal_keys)
        cls = type(sf)
        cls.check__objs_are_legal_keys(sf, legal_keys)
        return cls.immutable_replace__whole_active_keys_configuration__fvalue(sf, opss.__and__, legal_keys)

    def __pow__(sf, legal_keys_to_del_set_pair__or__legal_key2bool, /):
        cls = type(sf)
        #return cls.immutable_overwrite_configuration_of(sf, legal_keys_to_del_set_pair__or__legal_key2bool, allow_illegal_keys=False)
        if (type(legal_keys_to_del_set_pair__or__legal_key2bool) is tuple and len(legal_keys_to_del_set_pair__or__legal_key2bool)==2):
            #pair
            legal_keys_to_del_set_pair = legal_keys_to_del_set_pair__or__legal_key2bool
        else:
            #mapping
            legal_key2bool = legal_keys_to_del_set_pair__or__legal_key2bool
            (legal_keys_to_del, legal_keys_to_set) = legal_keys_to_del_set_pair = [], []
            for legal_key, to_set in legal_key2bool.items():
                if not type(to_set) is bool: raise TypeError
                ls = legal_keys_to_set if to_set else legal_keys_to_del
                ls.append(legal_key)
        #
        legal_keys_to_del_set_pair
        (legal_keys_to_del, legal_keys_to_set) = map(mk_frozenset, legal_keys_to_del_set_pair)
        return cls.immutable_overwrite__active_keys_configuration(sf, legal_keys_to_del, legal_keys_to_set, allow_illegal_keys4to_del=False)

    def __lshift__(sf, legal_keys_to_set, /):
        return sf ** ([], legal_keys_to_set)
    def __sub__(sf, legal_keys_to_del, /):
        return sf ** (legal_keys_to_del, [])
        legal_keys = mk_frozenset(legal_keys_to_del)
        del legal_keys_to_del
        cls = type(sf)
        cls.check__objs_are_legal_keys(sf, legal_keys)
        return cls.immutable_replace__whole_active_keys_configuration__fvalue(sf, opss.__sub__, legal_keys)


class Helper4HybridFlag___mutex:
    r'''
    to impl:
        hybrid_flag.___iter_findout_lhs_legal_keys_not_mutex_between___
        hybrid_flag.___iter_findout_legal_keys_not_mutex_insides___


    合法键互斥归组信息={合法键:互斥组信息}
    互斥组信息={互斥组:取消组信息}
    取消组信息={取消组:互斥组信息}
        #递归

    #两个合法键互斥的判定条件:
    def 两个合法键互斥 合法键a 合法键b = a != b && 某个互斥组起作用 合法键互斥归组信息[a] 合法键互斥归组信息[b]
    def 某个互斥组起作用 互斥组信息X 互斥组信息Y = any(not (某个取消组起作用 X[g] Y[g]) | 互斥组g <- X/-\Y)
    def 某个取消组起作用 取消组信息P 取消组信息Q = any(not (某个互斥组起作用 P[g] Q[g]) | 取消组g <- P/-\Q)


    #mgroup=mutex_group 互斥组
    #cgroup=cancel_group 取消组
    #minfo=mgroup_info 互斥组信息
    #cinfo=cgroup_info 取消组信息
    #k2minfo=合法键互斥归组信息
    #
    #k2minfo.get(legal_key, null_mapping_view) -> minfo
    #   null_mapping_view for extra_legal_keys4not_mutex_with_others
    #
    #minfo[mgroup]->cinfo
    #cinfo[cgroup]->minfo
    #
    #'''
    def are_two_legal_keys_mutex(sf, lkey, rkey, /):
        if lkey == rkey: return False
        k2minfo_get = sf.合法键互斥归组信息_get
        lhs_minfo = k2minfo_get(lkey, null_mapping_view)
        rhs_minfo = k2minfo_get(rkey, null_mapping_view)
        return sf.do_two_minfos_take_effect(lhs_minfo, rhs_minfo)
    def do_two_minfos_take_effect(sf, lhs_minfo, rhs_minfo, /):
        common = lhs_minfo.keys() & rhs_minfo.keys()
        return any(not sf.do_two_cinfos_take_effect(lhs_minfo[mgroup], rhs_minfo[mgroup]) for mgroup in common)
    def do_two_cinfos_take_effect(sf, lhs_cinfo, rhs_cinfo, /):
        common = lhs_cinfo.keys() & rhs_cinfo.keys()
        return any(not sf.do_two_minfos_take_effect(lhs_cinfo[cgroup], rhs_cinfo[cgroup]) for cgroup in common)

    def __init__(sf, 合法键互斥归组信息_get, /):
        sf.合法键互斥归组信息_get = 合法键互斥归组信息_get
    def iter_findout_lhs_legal_keys_not_mutex_between(sf, lhs_legal_key_set, rhs_legal_key_set, /,*, __rhs_appendto_lhs=False):
        r'''
        to impl:
            hybrid_flag.___iter_findout_lhs_legal_keys_not_mutex_between___
        #'''
        if 1:
            k2minfo_get = sf.合法键互斥归组信息_get
            #lkey=lhs_legal_key
            #rkey=rhs_legal_key

            #lhs_legal_keys4not_mutex = set()
            lkey2cached_sets = collections.defaultdict(list)
                #yielded_lkeys = set()
                #yield lkey then remove lkey from cached_sets
                ##
                #ref to mgroup2not_yielded_lkeys
            mgroup2not_yielded_lkeys = collections.defaultdict(set)
                #{mgroup:not_yielded_lkeys}

        ######################
        ######################
        def _add(s, k, /):
            #-> is_new
            L = len(s)
            s.add(k)
            return not L == len(s)

        ######################
        def _post_yield(yielded_lkey, /):
            #keep condition on mgroup2not_yielded_lkeys
            if 0b0: print_err(f'@_post_yield::yielded_lkey={yielded_lkey!r}')
            for cached_set in lkey2cached_sets[yielded_lkey]:
                cached_set.remove(yielded_lkey)
            return

        ######################
        def _init_on_lkey(lkey, /):
            # for __rhs_appendto_lhs: input rkey
            minfo = k2minfo_get(lkey, null_mapping_view)
                #null_mapping_view for extra_legal_keys4not_mutex_with_others
            #for mgroup, cinfo in minfo.items():
            for mgroup in minfo:
                cached_set = mgroup2not_yielded_lkeys[mgroup]
                if _add(cached_set, lkey):
                    lkey2cached_sets[lkey].append(cached_set)
            return


        ######################
        ######################
        def _main(lhs_legal_key_set, /):
            if not type(__rhs_appendto_lhs) is bool: raise TypeError
            if __rhs_appendto_lhs and lhs_legal_key_set is not None: raise TypeError
            if __rhs_appendto_lhs:
                if lhs_legal_key_set is not None: raise logic-err
                lhs_legal_key_set = null_frozenset


            ok_pairs = set()
                # {(lkey, rkey) if 同属某些 互斥组 但 并不互斥}

            for lkey in lhs_legal_key_set:
                _init_on_lkey(lkey)

            global_yielded_lkeys = set()
            handled_rkeys = set()
            for rkey in rhs_legal_key_set:
                if not _add(handled_rkeys, rkey): continue
                minfo = k2minfo_get(rkey, null_mapping_view)
                for mgroup in minfo:
                    #rhs mgroup
                    not_yielded_lkeys = mgroup2not_yielded_lkeys[mgroup]

                    local_yielded_lkeys = []
                    for not_yielded_lkey in not_yielded_lkeys:
                        #共同 lhs,rhs mgroup
                        pair = (not_yielded_lkey, rkey)
                        if pair in ok_pairs:
                            pass
                        elif not sf.are_two_legal_keys_mutex(not_yielded_lkey, rkey):
                            ok_pairs.add(pair)
                        else:
                            #mutex
                            try:
                                if not _add(global_yielded_lkeys, not_yielded_lkey): raise logic-err
                            except:
                                print_err(f'not_yielded_lkey={not_yielded_lkey!r}')
                                print_err(f'not_yielded_lkeys={not_yielded_lkeys!r}')
                                print_err(f'ok_pairs={ok_pairs!r}')
                                print_err(f'rkey={rkey!r}')
                                print_err(f'mgroup={mgroup!r}')
                                print_err(f'global_yielded_lkeys={global_yielded_lkeys!r}')
                                print_err(f'handled_rkeys={handled_rkeys!r}')
                                print_err(f'mgroup2not_yielded_lkeys={mgroup2not_yielded_lkeys!r}')
                                print_err(f'lkey2cached_sets={lkey2cached_sets!r}')
                                print_err(f'__rhs_appendto_lhs={__rhs_appendto_lhs!r}')
                                print_err(f'lhs_legal_key_set={lhs_legal_key_set!r}')
                                print_err(f'rhs_legal_key_set={rhs_legal_key_set!r}')
                                raise
                            yield not_yielded_lkey
                            yielded_lkey = not_yielded_lkey; del not_yielded_lkey
                            #_post_yield(yielded_lkey)
                            #   move outside loop since will modify the current iterating obj: not_yielded_lkeys
                            local_yielded_lkeys.append(yielded_lkey)
                            if 0b0: print_err(f'@after local_yielded_lkeys.append::yielded_lkey={yielded_lkey!r}')
                        #end-if
                    #end-for
                    if 0b0: print_err(f'local_yielded_lkeys={local_yielded_lkeys!r}')
                    for yielded_lkey in local_yielded_lkeys:
                        _post_yield(yielded_lkey)

                ##########################
                ##########################
                ##########################
                ##########################
                if __rhs_appendto_lhs:
                    _init_on_lkey(rkey)
            return
        #end-def _main(lhs_legal_key_set, /):
        return _main(lhs_legal_key_set)
        ######################

    def iter_findout_legal_keys_not_mutex_insides(sf, legal_key_set, /):
        r'''
        to impl:
            hybrid_flag.___iter_findout_legal_keys_not_mutex_insides___
        #'''
        return sf.iter_findout_lhs_legal_keys_not_mutex_between(None, legal_key_set, _Helper4HybridFlag___mutex__rhs_appendto_lhs=True)
        return sf.iter_findout_lhs_legal_keys_not_mutex_between(None, legal_key_set, __rhs_appendto_lhs=True)
#end-class Helper4HybridFlag___mutex:


r'''
__using_mutext_cancel_group
__legal_keys_are_finite
__instance_state_is_active_keys_only
__key_is_str
#'''

def mk_k2minfo_ex__from_mgroups_without_cgroups(legal_key_mutex_groups, extra_legal_keys4discrete_mutex_groups, /,*, shrinkage_k2minfo:bool, result_mutable_vs_view:bool):
    'Iter (Iter key) -> Iter key -> ((k2minfo, extra_legal_keys), (xgroup_descriptor2legal_key_group, legal_key_group2xgroup_descriptor))'
    extra_discrete_mutex_groups = ([key] for key in extra_legal_keys4discrete_mutex_groups)
    del extra_legal_keys4discrete_mutex_groups
    legal_key_mutex_groups = itertools.chain(legal_key_mutex_groups, extra_discrete_mutex_groups)
    ######################
    ######################
    legal_key_mutex_groups = mk_frozenset(filter(bool, map(mk_frozenset, legal_key_mutex_groups)))
    assert all(legal_key_mutex_groups)
    ######################
    ######################

    #legal_keys = null_frozenset.union(*legal_key_mutex_groups)
    legal_key2xgroup_descriptor2null_mapping = collections.defaultdict(dict)
    legal_key_group2xgroup_descriptor = {}
    xgroup_descriptor2legal_key_group = []
    for i, legal_key_group in enumerate(legal_key_mutex_groups):
        assert legal_key_group
        if 1:
            xgroup_descriptor = legal_key_group2xgroup_descriptor.setdefault(legal_key_group, len(legal_key_group2xgroup_descriptor))
            if xgroup_descriptor == len(xgroup_descriptor2legal_key_group):
                xgroup_descriptor2legal_key_group.append(legal_key_group)
            assert len(xgroup_descriptor2legal_key_group) == len(legal_key_group2xgroup_descriptor)
        xgroup_descriptor

        for legal_key in legal_key_group:
            legal_key2xgroup_descriptor2null_mapping[legal_key][xgroup_descriptor] = null_mapping_view

    k2minfo = legal_key2xgroup_descriptor2null_mapping = dict(legal_key2xgroup_descriptor2null_mapping)
    extra_legal_keys = extra_keys4discrete_mutex_groups = set()
    if shrinkage_k2minfo:
        #k2minfo >> extra_legal_keys
        for k, minfo in k2minfo.items():
            if minfo.keys() <= {mk_frozenset([k])}:
                #discrete = True
                extra_legal_keys.add(k)
        for k in extra_legal_keys:
            del k2minfo[k]
    else:
        pass

    if result_mutable_vs_view:
        #view
        k2minfo = _View___k2minfo(k2minfo)
        extra_legal_keys = mk_frozenset(extra_legal_keys)
        xgroup_descriptor2legal_key_group = mk_tuple(xgroup_descriptor2legal_key_group)
        legal_key_group2xgroup_descriptor = MapView(legal_key_group2xgroup_descriptor)
    return ((k2minfo, extra_legal_keys), (xgroup_descriptor2legal_key_group, legal_key_group2xgroup_descriptor))
#end-def mk_k2minfo_ex__from_mgroups_without_cgroups(legal_key_mutex_groups, extra_legal_keys4discrete_mutex_groups, /,*, shrinkage_k2minfo:bool, result_mutable_vs_view:bool):


class IHybridFlag__using_mutext_cancel_group(IHybridFlag):
    r'''
    using 合法键互斥归组信息
    #'''
    __slots__ = ()

    @abstractmethod
    def ___get__partial_legal_key2mgroup_info__get_default___(sf, /):
        'get__partial_legal_key2mgroup_info__get_default'
    def get__partial_legal_key2mgroup_info__get_default(sf, /):
        r'''
        -> k2minfo_get
            where
                minfo = k2minfo.get/k2minfo_get(legal_key, default)
                #using callable instead of mapping since legal_keys may be infinite

        partial_legal_key2mgroup_info
            see: Helper4HybridFlag___mutex.__doc__
            #k2minfo=合法键互斥归组信息
        if legal_key is not key/legal_key:
            undefined_behavior
        #'''
        cls = type(sf)
        k2minfo_get = cls.___get__partial_legal_key2mgroup_info__get_default___(sf)
        return k2minfo_get

    @override
    def ___iter_findout_lhs_legal_keys_not_mutex_between___(sf, lhs_legal_key_set, rhs_legal_key_set, /):
        'iter_findout_lhs_legal_keys_not_mutex_between #Helper4HybridFlag___mutex'
        cls = type(sf)
        k2minfo_get = cls.get__partial_legal_key2mgroup_info__get_default(sf)
        helper = Helper4HybridFlag___mutex(k2minfo_get)
        return helper.iter_findout_lhs_legal_keys_not_mutex_between(lhs_legal_key_set, rhs_legal_key_set)

    @override
    def ___iter_findout_legal_keys_not_mutex_insides___(sf, legal_key_set, /):
        'iter_findout_legal_keys_not_mutex_insides #Helper4HybridFlag___mutex'
        cls = type(sf)
        k2minfo_get = cls.get__partial_legal_key2mgroup_info__get_default(sf)
        helper = Helper4HybridFlag___mutex(k2minfo_get)
        return helper.iter_findout_legal_keys_not_mutex_insides(legal_key_set)

class IHybridFlag__legal_keys_are_finite(IHybridFlag__using_mutext_cancel_group):
    __slots__ = ()

    @abstractmethod
    def ___get_view_of_extra_legal_keys4not_mutex_with_others___(sf, /):
        'get_view_of_extra_legal_keys4not_mutex_with_others #-> set neednot SetView'
    @abstractmethod
    def ___get_view_of_partial_legal_key2mgroup_info___(sf, /):
        'get_view_of_partial_legal_key2mgroup_info #-> k2minfo neednot _View___k2minfo'
    def get_view_of_partial_legal_key2mgroup_info(sf, /):
        r'''
        -> view_of_partial_legal_key2mgroup_info
            see: _View___k2minfo

        partial_legal_key2mgroup_info
            see: Helper4HybridFlag___mutex.__doc__
            #k2minfo=合法键互斥归组信息
        #'''
        cls = type(sf)
        k2minfo = cls.___get_view_of_partial_legal_key2mgroup_info___(sf)
        view_of_partial_legal_key2mgroup_info = _View___k2minfo(k2minfo)
        return view_of_partial_legal_key2mgroup_info
    def get_view_of_extra_legal_keys4not_mutex_with_others(sf, /):
        r'''
        -> view_of_extra_legal_keys4not_mutex_with_others
        legal_key_set
            = partial_legal_key2mgroup_info.keys()
            | extra_legal_keys4not_mutex_with_others
        #'''
        cls = type(sf)
        extra_legal_keys4not_mutex_with_others = cls.___get_view_of_extra_legal_keys4not_mutex_with_others___(sf)
        view_of_extra_legal_keys4not_mutex_with_others = SetView(extra_legal_keys4not_mutex_with_others)
        return view_of_extra_legal_keys4not_mutex_with_others

    @override
    def ___is_key_legal___(sf, key, /):
        'is_key_legal #NOTE:extra_legal_keys4not_mutex_with_others/discrete/isolated'
        # +k2minfo#合法键互斥归组信息
        # +extra_legal_keys4discrete_mutex_groups
        cls = type(sf)
        return key in cls.get_view_of_extra_legal_keys4not_mutex_with_others(sf) or key in cls.get_view_of_partial_legal_key2mgroup_info(sf)
    @override
    def ___get__partial_legal_key2mgroup_info__get_default___(sf, /):
        cls = type(sf)
        k2minfo = cls.get_view_of_partial_legal_key2mgroup_info(sf)
        k2minfo_get = k2minfo.get
        return k2minfo_get


class IHybridFlag__key_is_str(IHybridFlag):
    __slots__ = ()

    @override
    def ___check__obj_is_key___(sf, obj, /):
        'check__obj_is_key #ObjNotKeyError'
        if not type(obj) is str: raise ObjNotKeyError

class IHybridFlag__instance_state_is_active_keys_only(IHybridFlag):
    r'''
    #'''
    @classmethod
    def mk_hybrid_flag_builder(cls, /):
        return AttrCollector(cls)
    def __init__(sf, legal_keys_as_active_keys=None, /):
        #see:immutable_replace__whole_active_keys_configuration
        #see:___get_args_kwargs4repr___==>>[=None]
        #see:mk_hybrid_flag_builder==>>[instance_state_is_active_keys_only]
        if legal_keys_as_active_keys is None:
            legal_keys_as_active_keys = null_frozenset
        cls = type(sf)
        legal_key_frozenset = mk_frozenset(legal_keys_as_active_keys)
        del legal_keys_as_active_keys
        cls.check__legal_key_frozenset_is_valid_active_keys_configuration(sf, legal_key_frozenset)
        valid_active_keys_configuration = legal_key_frozenset
        object.__setattr__(sf, '_active_keys', valid_active_keys_configuration)
            #sf._active_keys = valid_active_keys_configuration
        return
    @override
    def ___get_view_of_active_key_set___(sf, /):
        'get_view_of_active_key_set'
        view_of_active_key_set = object.__getattribute__(sf, '_active_keys')
            #since frozenset
        return view_of_active_key_set
    @override
    def ___immutable_replace__whole_active_keys_configuration___(sf, valid_active_keys_configuration, /):
        'immutable_replace__whole_active_keys_configuration #validded'
        cls = type(sf)
        return cls(valid_active_keys_configuration)

    @override
    def ___get_args_kwargs___(sf, /):
        '-> ((active_key_frozenset,), {})'
        view_of_active_key_set = get_view_of_active_key_set_of_hybrid_flag(sf)
        args = (mk_frozenset(view_of_active_key_set),)
        return (args, {})

    @override
    def ___get_args_kwargs4repr___(sf, /):
        '-> (tmay active_key_set, {})'
        if sf:
            view_of_active_key_set = get_view_of_active_key_set_of_hybrid_flag(sf)
            active_key_set = set(view_of_active_key_set)
            args = (active_key_set,)
        else:
            args = ()
        return (args, {})



class IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only(IHybridFlag__legal_keys_are_finite, IHybridFlag__instance_state_is_active_keys_only):
    r'''
    ==>> of_obj_at_cls:
        extra_legal_keys4not_mutex_with_others
        partial_legal_key2mgroup_info
    #'''
    @abstractmethod
    class ___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___:pass
    @abstractmethod
    class ___of_obj_at_cls__the_partial_legal_key2mgroup_info___:pass

    @override
    def ___get_view_of_extra_legal_keys4not_mutex_with_others___(sf, /):
        'get_view_of_extra_legal_keys4not_mutex_with_others #-> set neednot SetView'
        cls = type(sf)
        return cls.___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
    @override
    def ___get_view_of_partial_legal_key2mgroup_info___(sf, /):
        'get_view_of_partial_legal_key2mgroup_info #-> k2minfo neednot _View___k2minfo'
        cls = type(sf)
        return cls.___of_obj_at_cls__the_partial_legal_key2mgroup_info___
abstract___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___ = IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only.___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
abstract___of_obj_at_cls__the_partial_legal_key2mgroup_info___ = IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only.___of_obj_at_cls__the_partial_legal_key2mgroup_info___


class IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str(IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only, IHybridFlag__key_is_str):
    r'''
    ___check__legal_key_set_satisfy_active_keys_constraints___besides_mutex___
    ___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
    ___of_obj_at_cls__the_partial_legal_key2mgroup_info___
    #'''
    pass


if 0:
    IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str()
    #TypeError: Can't instantiate abstract class IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str with abstract methods ___check__legal_key_set_satisfy_active_keys_constraints___besides_mutex___, ___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___, ___of_obj_at_cls__the_partial_legal_key2mgroup_info___


class _View___recur_mapping_value_is_mapping(collections.abc.Mapping):
    r'''
    to impl:
        ___get_view_of_partial_legal_key2mgroup_info___
            view_of_partial_legal_key2mgroup_info
    #'''
    def __init__(sf, mapping__recur_value_is_mapping, /):
        sf._d = mapping__recur_value_is_mapping
    def __getitem__(sf, key, /):
        return __class__(sf._d[key])
    def __len__(sf, /):
        return len(sf._d)
    def __iter__(sf, /):
        return iter(sf._d)

_View___k2minfo = _View___recur_mapping_value_is_mapping
_View___k2minfo({})



#class IHybridFlag__using_mutext_cancel_group(IHybridFlag):








class ICachedEnvironment__env_is_hybrid_flag(ICachedEnvironment):
    __slots__ = ()

    @abstractmethod
    def ___hybrid_flag__is_key_legal___(sf, env_variable_name, /):
        '___query__env_variable_name2tribool___'
    @abstractmethod
    def ___hybrid_flag__is_legal_key_active___(sf, env_variable_name, /):
        '___query__env_variable_name2tribool___'
    @override
    def ___query__env_variable_name2tribool___(sf, env_variable_name, /):
        'query__env_variable_name2tribool'
        cls = type(sf)
        if not cls.___hybrid_flag__is_key_legal___(sf, env_variable_name): raise KeyNotLegalError
        return cls.___hybrid_flag__is_legal_key_active___(sf, env_variable_name)

class CachedEnvironment__env_is_hybrid_flag(ICachedEnvironment__env_is_hybrid_flag, ICachedEnvironment__cache_is_dict):
    def __init__(sf, ops4hybrid_flag, may_hybrid_flag, may_legal_keys_as_active_keys, cache=None, /):
        if cache is None:
            cache = {}
        sf._ops4hybrid_flag = ops4hybrid_flag
            #for legal_keys at cls/ops
        sf._may_hybrid_flag = may_hybrid_flag
            #for legal_keys at obj
        if may_legal_keys_as_active_keys is None:
            #if may_legal_keys_as_active_keys is None and may_hybrid_flag is None: raise TypeError
            legal_keys_as_active_keys = ops4hybrid_flag.get_view_of_active_key_set(may_hybrid_flag)
        else:
            legal_keys_as_active_keys = may_legal_keys_as_active_keys
                #for active_keys be checked before mk obj / not at obj yet
        #len(legal_keys_as_active_keys)
        sf._legal_keys_as_active_keys = SetView(legal_keys_as_active_keys)
        sf._cache = cache
    @override
    def ___get_cache___(sf, /):
        '-> cache'
        return sf._cache
    @override
    def ___hybrid_flag__is_key_legal___(sf, env_variable_name, /):
        '___query__env_variable_name2tribool___'
        return sf._ops4hybrid_flag.is_key_legal(sf._may_hybrid_flag, env_variable_name)
    @override
    def ___hybrid_flag__is_legal_key_active___(sf, env_variable_name, /):
        '___query__env_variable_name2tribool___'
        return env_variable_name in sf._legal_keys_as_active_keys
        return sf._ops4hybrid_flag.is_legal_key_active(sf._may_hybrid_flag, env_variable_name)



class IHybridFlag__all_keys_are_legal(IHybridFlag):
    __slots__ = ()

    @override
    def ___is_key_legal___(sf, key, /):
        'is_key_legal #NOTE:extra_legal_keys4not_mutex_with_others/discrete/isolated'
        return True
class IHybridFlag__without_active_keys_constraints(IHybridFlag):
    __slots__ = ()

    @override
    def ___check__legal_key_set_satisfy_active_keys_constraints___besides_mutex___(sf, legal_key_set, /):
        'check__legal_key_set_satisfy_active_keys_constraints___besides_mutex #LegalKeysNotSatisfiedConstraintsError'
        return#do no check
class IHybridFlag__active_keys_constraints_check_nonempty_only(IHybridFlag):
    __slots__ = ()

    @override
    def ___check__legal_key_set_satisfy_active_keys_constraints___besides_mutex___(sf, legal_key_set, /):
        'check__legal_key_set_satisfy_active_keys_constraints___besides_mutex #LegalKeysNotSatisfiedConstraintsError'
        if not legal_key_set: raise LegalKeysNotSatisfiedConstraintsError
        return



class IHybridFlag__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only(IHybridFlag__without_active_keys_constraints, IHybridFlag__all_keys_are_legal, IHybridFlag__instance_state_is_active_keys_only):
    __slots__ = ()

    pass


class IHybridFlag__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str(IHybridFlag__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only, IHybridFlag__key_is_str):
    r'''
    ___iter_findout_legal_keys_not_mutex_insides___
    ___iter_findout_lhs_legal_keys_not_mutex_between___
    #'''
    __slots__ = ()

    pass

class IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex(IHybridFlag):
    __slots__ = ()

    @override
    def ___iter_findout_lhs_legal_keys_not_mutex_between___(sf, lhs_legal_key_set, rhs_legal_key_set, /):
        'iter_findout_lhs_legal_keys_not_mutex_between #Helper4HybridFlag___mutex'
        #bug:yield from (lhs_legal_key_set & rhs_legal_key_set)
        return null_iter

    @override
    def ___iter_findout_legal_keys_not_mutex_insides___(sf, legal_key_set, /):
        'iter_findout_legal_keys_not_mutex_insides #Helper4HybridFlag___mutex'
        return null_iter

class ICase__single_mutex_group_only_ie_pairwise_key_mutex(IHybridFlag):
    __slots__ = ()

    @override
    def ___iter_findout_lhs_legal_keys_not_mutex_between___(sf, lhs_legal_key_set, rhs_legal_key_set, /):
        'iter_findout_lhs_legal_keys_not_mutex_between #Helper4HybridFlag___mutex'
        #bug:yield from (lhs_legal_key_set & rhs_legal_key_set)
        L = len(rhs_legal_key_set)
        if L == 0:
            return;yield
        elif L == 1:
            yield from (lhs_legal_key_set - rhs_legal_key_set)
        elif L >= 2:
            yield from lhs_legal_key_set
        else:
            raise logic-err

    @override
    def ___iter_findout_legal_keys_not_mutex_insides___(sf, legal_key_set, /):
        'iter_findout_legal_keys_not_mutex_insides #Helper4HybridFlag___mutex'
        L = len(legal_key_set)
        if L >= 2:
            yield from legal_key_set
class ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only(ICase__single_mutex_group_only_ie_pairwise_key_mutex, IHybridFlag__active_keys_constraints_check_nonempty_only):
    __slots__ = ()
    pass
class ICase__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints(ICase__single_mutex_group_only_ie_pairwise_key_mutex, IHybridFlag__without_active_keys_constraints):
    __slots__ = ()
    pass

class Flag__discrete_mutex_groups_only_ie_no_key_pair_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str(IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex, IHybridFlag__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str):
    pass
class Case__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str(ICase__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints, IHybridFlag__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str):
    pass
class Case__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str(ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only, IHybridFlag__all_keys_are_legal, IHybridFlag__instance_state_is_active_keys_only, IHybridFlag__key_is_str):
    pass



class IHybridFlag__active_keys_constraints_using_ZerothOrderLogic(IHybridFlag):
    __slots__ = ()

    @abstractmethod
    def ___get_the_proposition4active_keys_constraints___(sf, /):
        'get_the_proposition4active_keys_constraints'
    def get_the_proposition4active_keys_constraints(sf, /):
        '-> IProposition'
        cls = type(sf)
        prop = cls.___get_the_proposition4active_keys_constraints___(sf)
        if not isinstance(prop, IProposition): raise TypeError
        return prop

    @override
    def ___check__legal_key_set_satisfy_active_keys_constraints___besides_mutex___(sf, legal_key_set, /):
        'check__legal_key_set_satisfy_active_keys_constraints___besides_mutex #LegalKeysNotSatisfiedConstraintsError'
        cls = type(sf)
        cached_env = CachedEnvironment__env_is_hybrid_flag(cls, sf, legal_key_set)
        prop = cls.get_the_proposition4active_keys_constraints(sf)
        if not prop.eval_at_configuration__bool(cached_env): raise LegalKeysNotSatisfiedConstraintsError

class IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic):
    __slots__ = ()

    @abstractmethod
    class ___of_obj_at_cls__the_proposition4active_keys_constraints___:pass
    @override
    def ___get_the_proposition4active_keys_constraints___(sf, /):
        'get_the_proposition4active_keys_constraints'
        cls = type(sf)
        return cls.___of_obj_at_cls__the_proposition4active_keys_constraints___
abstract___of_obj_at_cls__the_proposition4active_keys_constraints___ = IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls.___of_obj_at_cls__the_proposition4active_keys_constraints___
class IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls, IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only):
    pass


class IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only, IHybridFlag__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
    r'''
    ___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
    ___of_obj_at_cls__the_partial_legal_key2mgroup_info___
    ___of_obj_at_cls__the_proposition4active_keys_constraints___
    #'''
    pass
if 0:
    IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str()
class Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
    (___of_obj_at_cls__the_partial_legal_key2mgroup_info___
    ,___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
    ) = mk_k2minfo_ex__from_mgroups_without_cgroups([{'IProposition', 'ALL_STARMAP_SIMPLE_VAR_IMPLY', 'NO_CONSTRAINTS'}], [], shrinkage_k2minfo=True, result_mutable_vs_view=True)[0]
    ___of_obj_at_cls__the_proposition4active_keys_constraints___ = the_TRUE

case4hybrid_flag_constraint__IProposition = Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only(['IProposition'])
case4hybrid_flag_constraint__ALL_STARMAP_SIMPLE_VAR_IMPLY = Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only(['ALL_STARMAP_SIMPLE_VAR_IMPLY'])
case4hybrid_flag_constraint__NO_CONSTRAINTS = Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only(['NO_CONSTRAINTS'])
case4hybrid_flag_constraint__NotImplemented = Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only()


class IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only):
    def __init_subclass__(cls, /,*, may_cased_constraint=None, **kwargs):
        if may_cased_constraint is not None:
            cased_constraint = may_cased_constraint
            (case, constraint) = cased_constraint
            assert isinstance(case, Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only)
            if case.IProposition:
                prop = constraint
                either__prop__abstract_ver = prop
            elif case.ALL_STARMAP_SIMPLE_VAR_IMPLY:
                fs_ts_choices__triples = constraint
                prop = ALL_STARMAP_SIMPLE_VAR_IMPLY(fs_ts_choices__triples)
                either__prop__abstract_ver = prop
            #elif case.NO_CONSTRAINTS:
            elif case.NO_CONSTRAINTS:
                if constraint is not None: raise TypeError
                prop = the_TRUE
                either__prop__abstract_ver = prop
            elif case:
                raise Exception(f'unknown case: {case!r}')
            else:
                #raise logic-err
                if constraint is not NotImplemented: raise TypeError
                abstract_ver = abstract___of_obj_at_cls__the_proposition4active_keys_constraints___
                either__prop__abstract_ver = abstract_ver
            #end-case-of
            cls.___of_obj_at_cls__the_proposition4active_keys_constraints___ = either__prop__abstract_ver
        super().__init_subclass__(**kwargs)
class ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only(IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only):
    def __init_subclass__(cls, /,*, may_legal_keys=None, may_cased_constraint=None, **kwargs):
        if may_legal_keys is None:
            pass
        elif may_legal_keys is NotImplemented:
            (cls.___of_obj_at_cls__the_partial_legal_key2mgroup_info___
            ,cls.___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
            ) = (abstract___of_obj_at_cls__the_partial_legal_key2mgroup_info___
                ,abstract___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
                )
        else:
            legal_keys = may_legal_keys
            (cls.___of_obj_at_cls__the_partial_legal_key2mgroup_info___
            ,cls.___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
            ) = mk_k2minfo_ex__from_mgroups_without_cgroups([legal_keys], null_frozenset, shrinkage_k2minfo=True, result_mutable_vs_view=True)[0]
        super().__init_subclass__(may_cased_constraint=may_cased_constraint, **kwargs)

class IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only(IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only):
    def __init_subclass__(cls, /,*, may_legal_keys=None, may_cased_constraint=None, **kwargs):
        if may_legal_keys is None:
            pass
        elif may_legal_keys is NotImplemented:
            (cls.___of_obj_at_cls__the_partial_legal_key2mgroup_info___
            ,cls.___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
            ) = (abstract___of_obj_at_cls__the_partial_legal_key2mgroup_info___
                ,abstract___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
                )
        else:
            legal_keys = may_legal_keys
            (cls.___of_obj_at_cls__the_partial_legal_key2mgroup_info___
            ,cls.___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
            ) = mk_k2minfo_ex__from_mgroups_without_cgroups(null_frozenset, legal_keys, shrinkage_k2minfo=True, result_mutable_vs_view=True)[0]
        super().__init_subclass__(may_cased_constraint=may_cased_constraint, **kwargs)

class ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str(ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only, IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
    pass

class IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str(IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only, IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
    pass
if 0:
    ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str()

if 0:
    IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str()


#################################
#################################
#################################
#################################
#################################
#################################
class _doctest_examples___IHybridFlag:
    r'''
#[[[doctest_examples-begin

>>> from seed.types.logic.ZerothOrderLogic import VAR, NOT, NOT_VAR, the_FALSE, the_TRUE, the_YET, ERROR, EvalError

>>> class HybridFlag__tmp0(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
...     ___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___ = frozenset('abcdxyz')
...     ___of_obj_at_cls__the_partial_legal_key2mgroup_info___ = _View___k2minfo({})
...     ___of_obj_at_cls__the_proposition4active_keys_constraints___ = the_TRUE

>>> HybridFlag__tmp0()
HybridFlag__tmp0()
>>> HybridFlag__tmp0('a')
HybridFlag__tmp0({'a'})
>>> sorted(HybridFlag__tmp0('abcdxyz'))
['a', 'b', 'c', 'd', 'x', 'y', 'z']
>>> HybridFlag__tmp0('u')
Traceback (most recent call last):
    ...
KeyNotLegalError





>>> Flag = Flag__discrete_mutex_groups_only_ie_no_key_pair_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
>>> Case = Case__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str
>>> Case1 = Case__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str


>>> Flag('abcdxyz') #doctest: +ELLIPSIS
Flag__discrete_mutex_groups_only_ie_no_key_pair_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str({'...', '...', '...', '...', '...', '...', '...'})
>>> sorted(Flag('abcdxyz'))
['a', 'b', 'c', 'd', 'x', 'y', 'z']
>>> len(Flag('abcdxyz'))
7
>>> not Flag('abcdxyz')
False
>>> Flag('abcdxyz').k
False
>>> Flag('abcdxyz').x
True
>>> Flag('abcdxyz')['k']
False
>>> Flag('abcdxyz')['x']
True
>>> Flag('abcdxyz') == Flag('abcdxyz')
True
>>> Flag('abcdxyz') == Flag('abcdxyzw')
False
>>> Flag('abcdxyz') | 'www' == Flag('abcdxyzw')
True
>>> Flag('abcdxyz') == Flag('abcdxyzw') & 'abcdxyz4568'
True
>>> Flag('abcdxyz') << 'www' == Flag('abcdxyzw')
True
>>> Flag('abcdxyz') == Flag('abcdxyzw') - 'www13445'
True



>>> Case()
Case__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str()
>>> Case('ab')
Traceback (most recent call last):
    ...
LegalKeysNotMutex
>>> Case('aaa')
Case__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str({'a'})
>>> sorted(Case('aaa'))
['a']
>>> len(Case('aaa'))
1
>>> not Case('aaa')
False
>>> Case('aaa').k
False
>>> Case('aaa').a
True
>>> Case('aaa')['k']
False
>>> Case('aaa')['a']
True
>>> Case('aaa') == Case('a')
True
>>> Case('') == Case()
True
>>> Case('aaa') == Case('')
False
>>> Case('aaa') == Case('b')
False
>>> Case('aaa') | 'www'
Traceback (most recent call last):
    ...
LegalKeysNotMutex
>>> Case() | 'www'
Case__single_mutex_group_only_ie_pairwise_key_mutex__without_active_keys_constraints__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str({'w'})
>>> Case('aaa') == Case('aaa') & 'abcdxyz4568'
True
>>> Case('aaa') << 'www' == Case('w')
True
>>> Case('aaa') == Case('aaa') - 'www13445'
True




>>> Case1()
Traceback (most recent call last):
    ...
LegalKeysNotSatisfiedConstraintsError
>>> Case1('ab')
Traceback (most recent call last):
    ...
LegalKeysNotMutex
>>> Case1('aaa')
Case__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_check_nonempty_only__all_keys_are_legal__instance_state_is_active_keys_only__key_is_str({'a'})




#]]]doctest_examples-end
    #'''




class _doctest_examples___from_deprecated_old_Flag:
    r'''
based from [deprecated] seed.types.flag.Flag::__doc__::doctest_examples
example_classes: HybridFlag4test, HybridFlag4test_constraints, Flag4test, Case4test, Case4IHybridFlag__init_subclass__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only

#[[[doctest_examples-begin

>>> from seed.types.logic.ZerothOrderLogic import ALL_STARMAP_SIMPLE_VAR_IMPLY, SIMPLE_VAR_IMPLY, AND, OR, XOR, XNOR, IMPLY, FLIP_IMPLY, TOTAL, ALL
>>> from seed.types.logic.ZerothOrderLogic import VAR, NOT, NOT_VAR, the_FALSE, the_TRUE, the_YET, ERROR, EvalError

#>>> from seed.tiny import expectError

#old_src: >>> class HybridFlag4test(IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, constraints=[], partition=['xyz', '', 'w', 'ab', 't', 'ab']): pass
>>> class HybridFlag4test(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
...     (___of_obj_at_cls__the_partial_legal_key2mgroup_info___
...     ,___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
...     ) = mk_k2minfo_ex__from_mgroups_without_cgroups(['xyz', '', 'w', 'ab', 't', 'ab'], [], shrinkage_k2minfo=True, result_mutable_vs_view=True)[0]
...     ___of_obj_at_cls__the_proposition4active_keys_constraints___ = the_TRUE


>>> hybrid_flag_builder = HybridFlag4test.mk_hybrid_flag_builder()
>>> hybrid_flag_builder.x()
HybridFlag4test({'x'})
>>> sorted(hybrid_flag_builder.x.b.t.w())
['b', 't', 'w', 'x']

>>> sf = hybrid_flag = HybridFlag4test()

>>> sf
HybridFlag4test()

>>> sf.x
False
>>> sf.w
False
>>> sf['t']
False

>>> sf.ab
Traceback (most recent call last):
    ...
KeyNotLegalError_AttributeError

KeyError_AttributeError

>>> sf['c']
Traceback (most recent call last):
    ...
KeyNotLegalError

KeyError

>>> sf << ['t']
HybridFlag4test({'t'})
>>> sorted(sf << 'xaw')
['a', 'w', 'x']
>>> sf
HybridFlag4test()
>>> ot = sf
>>> ot <<= 'xaw'
>>> sf
HybridFlag4test()
>>> sorted(ot)
['a', 'w', 'x']
>>> sorted(ot << 'tz')
['a', 't', 'w', 'z']
>>> sorted(ot ** ('abyx', 'tz'))
['t', 'w', 'z']
>>> sorted(ot ** dict(t=True, z=True, a=False, b=False, y=False, x=False))
['t', 'w', 'z']
>>> sorted(ot - 'xyzw')
['a']
>>> sorted(ot & 'azw')
['a', 'w']
>>> sorted(ot | 'atw')
['a', 't', 'w', 'x']
>>> 'a' in ot
True
>>> ot['a']
True
>>> 't' in ot
True
>>> ot['t']
False

>>> 'q' in ot
False
>>> ot['q']
Traceback (most recent call last):
    ...
KeyNotLegalError

KeyError

>>> 0 in ot
Traceback (most recent call last):
    ...
ObjNotKeyError

TypeError

>>> ot[0]
Traceback (most recent call last):
    ...
ObjNotKeyError

TypeError


>>> ot.a
True
>>> ot.b
False
>>> ot.q
Traceback (most recent call last):
    ...
KeyNotLegalError_AttributeError

KeyError_AttributeError


>>> not sf
True
>>> not ot
False
>>> len(sf)
0
>>> len(ot)
3

>>> _ = hash(ot)
>>> sf == ot
False
>>> sf == sf
True
>>> ot == ot
True


#################################
#try conflict, not mutex
>>> HybridFlag4test('ab')
Traceback (most recent call last):
    ...
LegalKeysNotMutex

ValueError: active_key_set is invalid configuration

>>> sorted(ot | 'a')
['a', 'w', 'x']
>>> ot | 'b'
Traceback (most recent call last):
    ...
LegalKeysNotMutex

ValueError: active_key_set is invalid configuration

>>> ot | 'ab'
Traceback (most recent call last):
    ...
LegalKeysNotMutex

ValueError: active_key_set is invalid configuration

>>> ot << 'ab'
Traceback (most recent call last):
    ...
LegalKeysNotMutex

ValueError: not mutex

>>> ot ** ('', 'ab')
Traceback (most recent call last):
    ...
LegalKeysNotMutex

ValueError: not mutex

>>> ot ** ('a', 'a')
Traceback (most recent call last):
    ...
ValueError: to del&set same key at same time

ValueError: to set&del same key

#ok
>>> ot & 'ab'
HybridFlag4test({'a'})
>>> sorted(ot | ot)
['a', 'w', 'x']
>>> sorted(ot - 'ab')
['w', 'x']
>>> sorted(ot ** ('ab', ''))
['w', 'x']

#################################
#################################
# test constraints

#old_src: >>> class HybridFlag4test_constraints(IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, constraints=[('tz', ['w'], [('b', 'x'), ('', 'yb')])], partition=['xyz', '', 'w', 'ab', 't', 'ab']): pass
>>> class HybridFlag4test_constraints(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
...     (___of_obj_at_cls__the_partial_legal_key2mgroup_info___
...     ,___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
...     ) = mk_k2minfo_ex__from_mgroups_without_cgroups(['xyz', '', 'w', 'ab', 't', 'ab'], [], shrinkage_k2minfo=True, result_mutable_vs_view=True)[0]
...     ___of_obj_at_cls__the_proposition4active_keys_constraints___ = ALL_STARMAP_SIMPLE_VAR_IMPLY([('tz', ['w'], [('b', 'x'), ('', 'yb')])])

#...     ___of_obj_at_cls__the_proposition4active_keys_constraints___ = ALL(*itertools.starmap(SIMPLE_VAR_IMPLY, [('tz', ['w'], [('b', 'x'), ('', 'yb')])]))



>>> sf = hybrid_flag = HybridFlag4test_constraints()

>>> sf
HybridFlag4test_constraints()

>>> sf.x
False
>>> sf << 'w'
Traceback (most recent call last):
    ...
LegalKeysNotSatisfiedConstraintsError

ValueError: active_key_set is invalid configuration

>>> sorted(sf << 'wt')
['t', 'w']
>>> sorted(sf << 'wz')
['w', 'z']
>>> sorted(sf << 'wx')
['w', 'x']
>>> sf << 'wy'
Traceback (most recent call last):
    ...
LegalKeysNotSatisfiedConstraintsError

ValueError: active_key_set is invalid configuration

>>> sorted(sf << 'wyb')
['b', 'w', 'y']




#################################
#################################
# test ICase_.../IFlag_...

#old_src: >>> class Flag4test(IFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___mutex_groups_are_all_discrete, constraints=[], keys4discrete_mutex_groups=['xyz', '', 'w', 'ab', 't', 'ab']): pass
>>> class Flag4test(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
...     (___of_obj_at_cls__the_partial_legal_key2mgroup_info___
...     ,___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
...     ) = mk_k2minfo_ex__from_mgroups_without_cgroups([], ['xyz', '', 'w', 'ab', 't', 'ab'], shrinkage_k2minfo=True, result_mutable_vs_view=True)[0]
...     ___of_obj_at_cls__the_proposition4active_keys_constraints___ = the_TRUE


>>> class Flag4test(IFlag__discrete_mutex_groups_only_ie_no_key_pair_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str, may_legal_keys=['xyz', '', 'w', 'ab', 't', 'ab'], may_cased_constraint=(case4hybrid_flag_constraint__NO_CONSTRAINTS, None)):pass


>>> flag_builder = Flag4test.mk_hybrid_flag_builder()
>>> Flag4test()
Flag4test()

>>> flag_builder()
Flag4test()
>>> flag_builder.xyz()
Flag4test({'xyz'})
>>> sorted(flag_builder.xyz.ab())
['ab', 'xyz']
>>> flag_builder.x()
Traceback (most recent call last):
    ...
KeyNotLegalError

KeyError: 'x'





#old_src: >>> class Case4test(ICase__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___single_mutex_group_only, constraints=[], keys4the_only_mutex_group=['xyz', '', 'w', 'ab', 't', 'ab']): pass
>>> class Case4test(IHybridFlag__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str):
...     (___of_obj_at_cls__the_partial_legal_key2mgroup_info___
...     ,___of_obj_at_cls__the_extra_legal_keys4not_mutex_with_others___
...     ) = mk_k2minfo_ex__from_mgroups_without_cgroups([['xyz', '', 'w', 'ab', 't', 'ab']], [], shrinkage_k2minfo=True, result_mutable_vs_view=True)[0]
...     ___of_obj_at_cls__the_proposition4active_keys_constraints___ = the_TRUE


>>> class Case4test(ICase__single_mutex_group_only_ie_pairwise_key_mutex__active_keys_constraints_using_ZerothOrderLogic_at_cls__legal_keys_are_finite__instance_state_is_active_keys_only__key_is_str, may_legal_keys=['xyz', '', 'w', 'ab', 't', 'ab'], may_cased_constraint=(case4hybrid_flag_constraint__NO_CONSTRAINTS, None)):pass


>>> case_builder = Case4test.mk_hybrid_flag_builder()
>>> Case4test()
Case4test()

>>> case_builder()
Case4test()
>>> case_builder.xyz()
Case4test({'xyz'})
>>> case_builder.xyz.ab()
Traceback (most recent call last):
    ...
LegalKeysNotMutex

ValueError: active_key_set is invalid configuration

>>> case_builder.x()
Traceback (most recent call last):
    ...
KeyNotLegalError

KeyError: 'x'



#]]]doctest_examples-end

#'''


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):



