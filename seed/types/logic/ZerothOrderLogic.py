
#################################
#[[[__doc__-begin
r'''
py -m seed.types.logic.ZerothOrderLogic
py -m nn_ns.app.debug_cmd   seed.types.logic.ZerothOrderLogic
from seed.types.logic.ZerothOrderLogic import IProposition, ICachedEnvironment, eval_proposition_at_configuration__tribool as eval_prop_at
from seed.types.logic.ZerothOrderLogic import ALL_STARMAP_SIMPLE_VAR_IMPLY, SIMPLE_VAR_IMPLY, AND, OR, XOR, XNOR, IMPLY, FLIP_IMPLY, TOTAL
from seed.types.logic.ZerothOrderLogic import VAR, NOT, NOT_VAR, the_FALSE, the_TRUE, the_YET, ERROR, EvalError


雷同:
    seed.types.Tester
        完全可以用此模块实现目标功能
        测试的对象 就是 变量配置
        但 希望 repr 相对简洁...
由来:
    seed.types.flag.IHybridFlag
        IHybridFlag.___check__legal_key_set_satisfy_active_keys_constraints___besides_mutex___
            需要 表达 约束 并对不同的变量配置进行求值

=====
[[[更名
??first order logic
??propositional logic

e ../../python3_src/seed/types/logic/ZerothOrderLogic.py
    <--- e ../../python3_src/seed/types/logic/FirstOrderLogic.py
    !mv ../../python3_src/seed/types/logic/FirstOrderLogic.py   ../../python3_src/seed/types/logic/ZerothOrderLogic.py
    FirstOrderLogic ---> ZerothOrderLogic
    IFirstOrderLogic ---> IProposition
    一阶 不是指 谓词 的 参数 最多只能是1，而是指 谓词 可以是 集合<个体>（即 变量 只能是 个体），但不能是 集合<集合<个体> >（即 变量 不能是 集合<个体>），
    零阶逻辑 即 命题逻辑 无限定词+变量 只考虑 原子个体/布尔变量+命题连接词
    谓词逻辑 分析 命题内部结构，使用 限定词(All/Some(Exist))
    e others/数学/编程/logic/命题逻辑vs一阶谓词逻辑.txt
]]]
=====

=====
[[[
op<num_arg0s> from op<2>
    constraints:
        [@x. op<num_arg0s=1>(x) == op<2>(op<num_arg0s>(), x)]
        or [@x. op<num_arg0s>(x) == op<2>(x, op<num_arg0s>())]
        or ???like pairwise-EQU

    unordered-fold op<2> start arg0s
        XOR
    foldl op<2> start arg0s
        IMPLY
    foldr op<2> start arg0s
        FLIP_IMPLY
        #foldr logical/conceptual
        #   indeed eval shortcut from left to right
        #
    pairwise-then-unordered-fold pairwise-op<2> fold-op<2> fold-start arg0s
        O(n**2)
    ######################
    #bool-op only
    pairwise op<2> arg0s
        O(n**2)
        = pairwise-then-unordered-fold pairwise-op<2> bool_and True arg0s
        ######################
        #equivalent-relationship only
        pairwise__eqv op<2> arg0s
            O(n)
            = chain-pair-then-foldl op<2> arg0s
    chain-pair-then-foldl op<2> arg0s
        O(n)
        ##vivi py a<=b<c!=0>=...
=====
]]]







[[[
改动2:
    prime:
        ODD_TOTAL_TRUE
        EXACTLY_SINGLE_TRUE
        EXACTLY_SINGLE_FALSE
        EVEN_TOTAL_FALSE
        PAIRWISE_EQU
    XOR --->
        # XOR___+...
        * FOLDU_XOR/ODD_TOTAL_TRUE
        * EXACTLY_SINGLE_TRUE
            exactly single True
        * EXACTLY_SINGLE_FALSE
        # not $ XNOR___...
        * NOT_FOLDU_XNOR/ODD_TOTAL_FALSE
        * NOT_PAIRWISE_EQU/SOME_NOT_EQU/NOT_ALL_THE_SAME/NOT_ALL_EQU/ANY_NOT_EQU
    NOT_XOR/XNOR --->
        # XNOR___+...
        * FOLDU_XNOR/EVEN_TOTAL_FALSE
        * PAIRWISE_EQU/EQU/ALL_THE_SAME/ALL_EQU
        # not $ XOR___...
        * NOT_FOLDU_XOR/EVEN_TOTAL_TRUE
        * NOT_EXACTLY_SINGLE_TRUE
        * NOT_EXACTLY_SINGLE_FALSE
    XOR
    XOR_NOT
    XOR_VAR
    NOT_XOR
    NOT_XOR_NOT
    NOT_XOR_VAR
    --->>
    for z in above list:
        XOR___ z
        NOT_XOR___ z
        XOR_NOT___ z
        NOT_XOR_NOT___ z

        XOR_VAR___ z
        NOT_XOR_VAR___ z
        XOR_NOT_VAR___ z
        NOT_XOR_NOT_VAR___ z

        XNOR___ z
        NOT_XNOR___ z
        XNOR_NOT___ z
        NOT_XNOR_NOT___ z

        XNOR_VAR___ z
        NOT_XNOR_VAR___ z
        XNOR_NOT_VAR___ z
        NOT_XNOR_NOT_VAR___ z

改动1:
    本文件 更名 解释 何为 零阶逻辑/命题逻辑
        e ../../python3_src/seed/types/AddrAsHashWrapper.py
            同步更新
    使用 ICachedEnvironment 替代 variable_name2tribool
    TriBoolOps 更新 NOT_XOR/NXOR --->XNOR

]]]



#[[[doctest_examples-begin
fold:
    OR
    AND
    IMPLY
    FLIP_IMPLY
    ...
TOTAL
    ALL
    ANY
    xor:
        ODD_TOTAL_TRUE
        EXACTLY_SINGLE_TRUE
        EXACTLY_SINGLE_FALSE
    xnor:
        EVEN_TOTAL_FALSE
        PAIRWISE_EQU
CHAIN_NEIGHBOR
SIMPLE_VAR_IMPLY
ALL_STARMAP_SIMPLE_VAR_IMPLY

basic:
    TRUE
    FALSE
    YET
    ERROR
    NOT
    VAR
    NOT_VAR

    NOT_ALL
    NOT_ANY
    ALL_VAR
    ANY_VAR
    ALL_NOT_VAR
    ANY_NOT_VAR
#]]]doctest_examples-end





#'''
#]]]__doc__-end

#################################
r'''
py -m nn_ns.app.debug_cmd   seed.types.logic.ZerothOrderLogic   > $my_tmp/out4py/seed.types.logic.ZerothOrderLogic--__all__.txt
echo $my_tmp/out4py/seed.types.logic.ZerothOrderLogic--__all__.txt
/sdcard/0my_files/tmp//out4py/seed.types.logic.ZerothOrderLogic--__all__.txt
view /sdcard/0my_files/tmp/out4py/seed.types.logic.ZerothOrderLogic--__all__.txt
#'''
__all__ = '''

eval_proposition_at_configuration__tribool

ICachedEnvironment
    CachedEnvironment__env_is_callable

IProposition
    the_FALSE
    the_TRUE
    the_YET

    ERROR
        EvalError
    NOT
    VAR
    NOT_VAR

    CHAIN_NEIGHBOR
    SIMPLE_VAR_IMPLY
    ALL_STARMAP_SIMPLE_VAR_IMPLY


    OR
    AND

    FOLDU_XOR
    FOLDU_XNOR
    FOLDL_IMPLY
    FOLDL_NOT_FLIP_IMPLY
    FOLDR_FLIP_IMPLY
    FOLDR_NOT_IMPLY

    TOTAL
        ALL
        ANY
            NOT_ALL
            NOT_ANY
                ALL_VAR
                ANY_VAR
                NOT_ALL_VAR
                NOT_ANY_VAR



        ODD_TOTAL_TRUE
        EXACTLY_SINGLE_TRUE
        EXACTLY_SINGLE_FALSE

        EVEN_TOTAL_FALSE
        PAIRWISE_EQU











ICachedEnvironment
    ICachedEnvironment__cache_is_dict
        CachedEnvironment__env_is_callable

eval_proposition_at_configuration__tribool

IProposition
    OR
    AND

    FOLDU_XOR
    FOLDU_XNOR
    FOLDL_IMPLY
    FOLDL_NOT_FLIP_IMPLY
    FOLDR_FLIP_IMPLY
    FOLDR_NOT_IMPLY

        NOR
        NAND

        XOR
        XNOR
        IMPLY
        NOT_FLIP_IMPLY
        FLIP_IMPLY
        NOT_IMPLY


    TOTAL
        ALL
        ANY

        ODD_TOTAL_TRUE
        EXACTLY_SINGLE_TRUE
        EXACTLY_SINGLE_FALSE

        EVEN_TOTAL_FALSE
        PAIRWISE_EQU

            ODD_TOTAL_FALSE
            NOT_FOLDU_XNOR
            NOT_PAIRWISE_EQU
            SOME_NOT_EQU
            NOT_ALL_THE_SAME
            NOT_ALL_EQU
            ANY_NOT_EQU

            EQU
            ALL_THE_SAME
            ALL_EQU
            EVEN_TOTAL_TRUE
            NOT_FOLDU_XOR
            NOT_EXACTLY_SINGLE_TRUE
            NOT_EXACTLY_SINGLE_FALSE

                XOR___ODD_TOTAL_TRUE
                XOR___EXACTLY_SINGLE_TRUE
                XOR___EXACTLY_SINGLE_FALSE

                XNOR___EVEN_TOTAL_FALSE
                XNOR___PAIRWISE_EQU

                XOR___FOLDU_XOR
                XOR___ODD_TOTAL_FALSE
                XOR___NOT_FOLDU_XNOR
                XOR___NOT_PAIRWISE_EQU
                XOR___SOME_NOT_EQU
                XOR___NOT_ALL_THE_SAME
                XOR___NOT_ALL_EQU
                XOR___ANY_NOT_EQU

                XNOR___FOLDU_XNOR
                XNOR___EQU
                XNOR___ALL_THE_SAME
                XNOR___ALL_EQU
                XNOR___EVEN_TOTAL_TRUE
                XNOR___NOT_FOLDU_XOR
                XNOR___NOT_EXACTLY_SINGLE_TRUE
                XNOR___NOT_EXACTLY_SINGLE_FALSE


    VAR

    FALSE
    TRUE
    YET
        the_FALSE
        the_TRUE
        the_YET

    EvalError
    ERROR

    NOT
    NOT_VAR

    NOT_ALL
    NOT_ANY
    ANY_NOT
    ALL_NOT
    NOT_ALL_NOT
    NOT_ANY_NOT

    XOR_VAR
    XNOR_VAR

    ALL_VAR
    ANY_VAR
    NOT_ALL_VAR
    NOT_ANY_VAR
    ALL_NOT_VAR
    ANY_NOT_VAR
    NOT_ALL_NOT_VAR
    NOT_ANY_NOT_VAR

    CHAIN_NEIGHBOR
    SIMPLE_VAR_IMPLY
    ALL_STARMAP_SIMPLE_VAR_IMPLY


    '''.split()
r'''comment-out
    NOT_FLIP_IMPLY
    XOR
    XOR_NOT = XOR<2>
    NOT_XOR = XNOR<2>
    NOT_XOR_NOT = XNOR<2>
    XOR_VAR
    NOT_XOR_VAR = XNOR_VAR<2>
    NOT_XOR_NOT_VAR = XNOR_VAR<2>
#'''
#################################

___begin_mark_of_excluded_global_names__0___ = ...

from seed.abc.abc import ABC, abstractmethod, override, ABC__no_slots
from seed.abc.ISingleton import ISingleton
from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from seed.types.TriBoolOps import TriBoolOps, LazyTriBoolOps
from seed.helper.check.checkers import checks, checkers, check_funcs
from seed.helper.check.check import Checker__FrozenDict, Checker__int_ge, Checker__type_is, mk_checker__pairs, checker4callable, mk_checker__array

from seed.tiny import null_iter, null_tuple, null_frozenset, null_mapping_view, MapView, mk_tuple, snd, print_err, is_iterator
from seed.iters.fold import foldl0
#from seed.types.AddrAsHashWrapper import AddrAsHashWrapper
from seed.abc.eq_by_id.AddrAsHashWrapper import AddrAsHashWrapper
from seed.types.FrozenDict import FrozenDict
from seed.data_funcs.rngs import sorted_rngs_to_iter_nontouch_ranges, make_Ranges
from seed.seq_tools.bisearch import bisearch


import collections
import operator as opss
import itertools



___end_mark_of_excluded_global_names__0___ = ...


class ICachedEnvironment(ABC):
    r'''
    ICachedEnvironment = cache + env
        immutable env :: {env_variable_name : tribool}
            #configuration
        mutable cache :: {AddrAsHashWrapper<IProposition> : Either Exception Tribool}
            #cache result of eval prop@env
    #'''
    __slots__ = ()
    @abstractmethod
    def ___cache__get__tmay___(sf, wrapped_prop, /):
        'cache__set_fdefault_with_exc'
    @abstractmethod
    def ___cache__set___(sf, wrapped_prop, either_exc_tribool, /):
        'cache__set_fdefault_with_exc'
    @abstractmethod
    def ___query__env_variable_name2tribool___(sf, env_variable_name, /):
        'query__env_variable_name2tribool'

    def cache__set_fdefault_with_exc(sf, prop, fdefault_with_exc, /):
        'prop -> (()->tribool) -> tribool|raise exc'
        wrapped_prop = AddrAsHashWrapper(prop)
        cls = type(sf)
        tmay = cls.___cache__get__tmay___(sf, wrapped_prop)
        if not tmay:
            try:
                tribool = fdefault_with_exc()
            except Exception as exc:
                either_exc_tribool = (False, exc)
            else:
                if not TriBoolOps.is_tribool(tribool): raise TypeError
                either_exc_tribool = (True, tribool)
            either_exc_tribool
            cls.___cache__set___(sf, wrapped_prop, either_exc_tribool)
            tmay = cls.___cache__get__tmay___(sf, wrapped_prop)
            if not tmay: raise logic-err
        [either_exc_tribool] = tmay
        (is_tribool, exc_or_tribool) = either_exc_tribool
        if is_tribool:
            tribool = exc_or_tribool
            return tribool
        else:
            exc = exc_or_tribool
            raise exc
    #end-def cache__set_fdefault_with_exc(sf, prop, fdefault_with_exc, /):

    def query__env_variable_name2tribool(sf, env_variable_name, /):
        'env_variable_name -> tribool'
        cls = type(sf)
        tribool = cls.___query__env_variable_name2tribool___(sf, env_variable_name)
        if not TriBoolOps.is_tribool(tribool): raise TypeError
        return tribool
    def query__env_variable_name2bool(sf, env_variable_name, /):
        'env_variable_name -> bool'
        cls = type(sf)
        b = cls.___query__env_variable_name2tribool___(sf, env_variable_name)
        if not TriBoolOps.is_bool(b): raise TypeError
        return b




class ICachedEnvironment__cache_is_dict(ICachedEnvironment):
    __slots__ = ()
    @abstractmethod
    def ___get_cache___(sf, /):
        '-> cache'
    @override
    def ___cache__get__tmay___(sf, wrapped_prop, /):
        'cache__set_fdefault_with_exc'
        cls = type(sf)
        cache = cls.___get_cache___(sf)
        if wrapped_prop in cache:
            return (cache[wrapped_prop],)
        return ()
    @override
    def ___cache__set___(sf, wrapped_prop, either_exc_tribool, /):
        'cache__set_fdefault_with_exc'
        cls = type(sf)
        cache = cls.___get_cache___(sf)
        if wrapped_prop in cache: raise KeyError('duplicate cache result for same prop')
        cache[wrapped_prop] = either_exc_tribool






class CachedEnvironment__env_is_callable(ICachedEnvironment__cache_is_dict, ABC__no_slots):
    #__slots__ = ()
    def __init__(sf, env_variable_name2tribool, cache=None, /):
        checker4callable(env_variable_name2tribool)
        if cache is None:
            cache = {}
        sf._env_variable_name2tribool = env_variable_name2tribool
        sf._cache = cache

    @override
    def ___get_cache___(sf, /):
        '-> cache'
        return sf._cache
    @override
    def ___query__env_variable_name2tribool___(sf, env_variable_name, /):
        'query__env_variable_name2tribool'
        return sf._env_variable_name2tribool(env_variable_name)
        return sf._env_variable_name2tribool[env_variable_name]



def eval_proposition_at_configuration__tribool(env_variable_name2tribool, prop:'IProposition', /):
    if callable(env_variable_name2tribool):
        f = env_variable_name2tribool
    else:
        def f(env_variable_name, /):
            return env_variable_name2tribool[env_variable_name]
    cached_env = CachedEnvironment__env_is_callable(f)
    return prop.eval_at_configuration__tribool(cached_env)







class IProposition(IReprImmutableHelper):
    __slots__ = ()
    #################################
    @abstractmethod
    def ___iter_variable_names___(sf, /):
        'iter_variable_names'
    @abstractmethod
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
    #################################
    #################################
    def ___eval_at_configuration__bool___(sf, cached_env, /):
        'eval_at_configuration__bool'
        cls = type(sf)
        return cls.___eval_at_configuration__tribool___(sf, cached_env)
    #################################
    #################################
    #################################
    #################################
    def iter_variable_names(sf, /):
        '-> Iter<variable_name> #may duplicate'
        cls = type(sf)
        return cls.___iter_variable_names___(sf)
    def collect_variable_names(sf, /):
        '-> frozenset<variable_name>'
        return frozenset(sf.iter_variable_names())
    def eval_at_configuration__tribool(sf, cached_env, /):
        'ICachedEnvironment -> tribool'
        assert isinstance(cached_env, ICachedEnvironment)
        cls = type(sf)
        tribool = cls.___eval_at_configuration__tribool___(sf, cached_env)
        if not TriBoolOps.is_tribool(tribool): raise TypeError
        return tribool

    def eval_at_configuration__bool(sf, cached_env, /):
        'ICachedEnvironment -> bool'
        assert isinstance(cached_env, ICachedEnvironment)
        cls = type(sf)
        b = cls.___eval_at_configuration__bool___(sf, cached_env)
        if not TriBoolOps.is_bool(b):
            if TriBoolOps.is_tribool(b): raise TypeError('cached_env<bool> may be indeed cached_env<tribool>')
            if not TriBoolOps.is_bool(b): raise TypeError
            raise logic-err
        #if type(b) is not bool: raise logic-err
        return b
    #################################
    #################################
    #################################
    #op<2>
    # no: % / @ * .+. +. -. // ** # <= => >=
    # has: ~; .-. ^ & | >> <<
    def __invert__(sf, /):
        '~rhs =[def]= [not rhs]'
        return NOT(sf)
    def __sub__(sf, ot, /):
        'lhs - rhs =[def]= [lhs and not rhs] <==> [not [lhs -->> rhs]]'
        return NOT_IMPLY(sf, ot)
    def __xor__(sf, ot, /):
        return XOR(sf, ot)
    def __or__(sf, ot, /):
        return OR(sf, ot)
    def __and__(sf, ot, /):
        return AND(sf, ot)
    def __lshift__(sf, ot, /):
        'lhs << rhs =[def]= [lhs <<-- rhs]'
        return FLIP_IMPLY(sf, ot)
    def __rshift__(sf, ot, /):
        'lhs >> rhs =[def]= [lhs -->> rhs]'
        return IMPLY(sf, ot)
    #################################
    #################################
    #################################
#end-class IProposition(IReprImmutableHelper):


class _INOT_super(IProposition):
    __slots__ = ()
    'NOT'
    @override
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        return TriBoolOps.NOT(super().___eval_at_configuration__tribool___(cached_env))


class _IBase4args_props(IProposition, ABC__no_slots):
    def __init__(sf, /, *props, props_false=False, props_vs_vars=False):
        saved_args = props
        saved_kwargs = dict(props_false=props_false, props_vs_vars=props_vs_vars)
        saved_kwargs = MapView({k:v for k, v in saved_kwargs.items() if v})
        #suffix:
        #...NOT
        #...VAR
        #...NOT_VAR

        if props_vs_vars:
            variable_names = props
            props = map(VAR, variable_names)
        if props_false:
            props = map(NOT, props)
        props = mk_tuple(props)
        if any(map(is_iterator, props)): raise TypeError
        try:
            check_funcs.instance_all(IProposition, props)
        except:
            print_err(props)
            raise
        sf._props = props
        sf._saved_args = saved_args
        sf._saved_kwargs = saved_kwargs

    @override
    def ___get_args_kwargs___(sf, /):
        return (sf._saved_args, sf._saved_kwargs)
        return (sf._props, {})
    @override
    def ___iter_variable_names___(sf, /):
        'iter_variable_names'
        for x in sf._props:
            yield from x.iter_variable_names()
class _IBase4two_args_props(_IBase4args_props):
    'op<2>'
    def __init__(sf, lhs_prop, rhs_prop, /,*, props_false=False, props_vs_vars=False):
        super().__init__(lhs_prop, rhs_prop, props_false=props_false, props_vs_vars=props_vs_vars)


class _IBase4foldl0(_IBase4args_props):
    @abstractmethod
    class ___the_tribool_op_name___:pass
    @override
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        #return all(x.eval_at_configuration__tribool(cached_env) for x in sf._props)
        cls = type(sf)
        tribool_op_name = cls.___the_tribool_op_name___
        tribool_op = getattr(TriBoolOps, tribool_op_name)
        lazy_info = (std_name, (lhs_determine_value, result4lhs_determine_value, maybe_foldl0_start_value), (rhs_determine_value, result4rhs_determine_value, maybe_foldr0_start_value)) = LazyTriBoolOps.binary_tribool_op_std_name2lazy_info[tribool_op_name]
        if maybe_foldl0_start_value is None: raise logic-err
        lhs = maybe_foldl0_start_value
        has_shortcut = result4lhs_determine_value is lhs_determine_value

        #if not has_shortcut: raise logic-err
            # FOLDL_IMPLY has no shortcut
        if maybe_foldl0_start_value is lhs_determine_value: raise logic-err
        for x in sf._props:
            if has_shortcut:
                #rhs occur hence lhs is real lhs
                #   this block cannot put after lhs = tribool_op(lhs, rhs)
                #   because next rhs may not exist!
                if lhs is lhs_determine_value:
                    return result4lhs_determine_value
            if lhs is lhs_determine_value:
                # local shortcut when has no global shortcut
                lhs = result4lhs_determine_value
            else:
                rhs = x.eval_at_configuration__tribool(cached_env)
                lhs = tribool_op(lhs, rhs)
        return lhs

class OR(_IBase4foldl0):
    ___the_tribool_op_name___ = 'OR'
class AND(_IBase4foldl0):
    ___the_tribool_op_name___ = 'AND'
class FOLDU_XOR(_IBase4foldl0):
    #class XOR(_IBase4foldl0):
    r'''
    = unordered-fold-XOR=ODD_TOTAL_TRUE
    ----
    0 op x => x
    1 op x => not x
    unordered-fold-XOR(bits) => [is_odd num_1s]
    ----another possible:
    但是 xor=exclusive-or=[def]=[1==num_1s]

    ----
    重命名为 FOLDU_XOR/ODD_TOTAL_TRUE

    ----

    XOR --->
        # XOR___+...
        * FOLDU_XOR/ODD_TOTAL_TRUE
        * EXACTLY_SINGLE_TRUE
            exactly single True
        # not $ XNOR___...
        * NOT_FOLDU_XNOR/ODD_TOTAL_FALSE
        * EXACTLY_SINGLE_FALSE
        * NOT_PAIRWISE_EQU/SOME_NOT_EQU/NOT_ALL_THE_SAME/NOT_ALL_EQU/ANY_NOT_EQU
改
    #'''
    ___the_tribool_op_name___ = 'XOR'
#class ODD_TOTAL_TRUE(FOLDU_XOR):pass
    #class ODD_TOTAL_TRUE(XOR):pass
class FOLDU_XNOR(_IBase4foldl0):
    r'''
    0 op x => not x
    1 op x => x
    unordered-fold-XNOR(bits) => [is_even num_0s]
    双操作数时，同或 XNOR 可以叫 NOT_XOR___...
    但 这里 扩张到 任意数量的操作数，就不行
        NOT_XOR___...(...)=[def]=NOT(XOR___...(...))
    重命名为 FOLDU_XNOR/EVEN_TOTAL_FALSE

    ======
    同或 XNOR
        e others/数学/编程/术语/同或XNOR.txt
        异或 XOR = [is_odd total_1s]
        同或 XNOR = ???
            if = not $ fold XOR<2> =[is_even total_1s]
            if = fold XNOR<2> =[is_even total_0s]
            if = pairwise EQU<2> =[0 == total_0s]or[0 == total_1s]
        同或 XNOR/ENOR/ExNOR 同或门=异或非门
    =====

    NOT_XOR/XNOR --->
        # XNOR___+...
        * FOLDU_XNOR/EVEN_TOTAL_FALSE
        * PAIRWISE_EQU/EQU/ALL_THE_SAME/ALL_EQU
        * NOT_EXACTLY_SINGLE_FALSE
        # not $ XOR___...
        * NOT_FOLDU_XOR/EVEN_TOTAL_TRUE
        * NOT_EXACTLY_SINGLE_TRUE
    #'''
    ___the_tribool_op_name___ = 'XNOR'
#class EVEN_TOTAL_FALSE(FOLDU_XNOR):pass

class FOLDL_IMPLY(_IBase4foldl0):
    #class IMPLY(_IBase4foldl0):
    r'''
    = foldl-IMPLY
    ===
    foldr-IMPLY a..z = a -> (b->(...->(z))) = all(a..y) -> z
    foldl-IMPLY a..z = (((a)...)->y) -> z
        = not (((a)...->x)->y) or z
        = not (not ((a)...->x) or y) or z
        = (((a)...->x) and not y) or z
        = (((a)...->x) or z)   and   (not y or z)
        = (((a)...->x) or z)   and   (not y or z)
        = (((((a)...->v)->w)->x) or z)   and   (not y or z)
        = ((((a)...->v)->w) -> (x or z))   and   (not y or z)
        = ((((a)...->u)->v) or x or z)   and   (not w or x or z)   and   (not y or z)
        = (((a)...->u) -> (v or x or z))   and   (not w or x or z)   and   (not y or z)
    #'''
    ___the_tribool_op_name___ = 'IMPLY'
class FOLDL_NOT_FLIP_IMPLY(_IBase4foldl0):
    #class NOT_FLIP_IMPLY(_IBase4foldl0):
    ___the_tribool_op_name___ = 'NOT_FLIP_IMPLY'


LazyTriBoolOps.binary_tribool_op_std_name2lazy_info['AND']
'lazy_info = (std_name, (lhs_determine_value, result4lhs_determine_value, maybe_foldl0_start_value), (rhs_determine_value, result4rhs_determine_value, maybe_foldr0_start_value))'
AND()


class _IBase4foldr0_evalL(_IBase4args_props):
    r'''
    as-if-foldr-but-eval-from_letf_to_right<op<2> >
    #'''
    @abstractmethod
    class ___the_tribool_flip_op_name___:pass
    @override
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        cls = type(sf)

        tribool_flip_op_name = cls.___the_tribool_flip_op_name___
        lazy_info = (std_name, (lhs_determine_value, result4lhs_determine_value, maybe_foldl0_start_value), (rhs_determine_value, result4rhs_determine_value, maybe_foldr0_start_value)) = LazyTriBoolOps.binary_tribool_op_std_name2lazy_info[tribool_flip_op_name]
        if maybe_foldr0_start_value is not None: raise logic-err
            #hence eval at-least one before detect shortcut
        if maybe_foldl0_start_value is None: raise logic-err
        v0 = maybe_foldl0_start_value
        if maybe_foldl0_start_value is lhs_determine_value: raise logic-err


        tribool_flip_op = getattr(TriBoolOps, tribool_flip_op_name)
        determine_value = rhs_determine_value
        result4determine_value = result4rhs_determine_value
        if determine_value is None: raise logic-err
        if not tribool_flip_op(v0, determine_value) is result4determine_value: raise logic-err
        if not result4determine_value is determine_value: raise logic-err

        cls = type(sf)

        rs = []
        for x in sf._props:
            r = x.eval_at_configuration__tribool(cached_env)
            if 0:
                if r is determine_value:
                    #shortcut
                    rs.append(result4determine_value)
                    break
                rs.append(r)
            else:
                rs.append(r)
                if r is determine_value:
                    #shortcut
                    #since op(determine_value, v0) == result4determine_value
                    #ie. flip_op(v0, determine_value) == result4determine_value
                    break
        return foldl0(tribool_flip_op, v0, reversed(rs))
            # not tribool_op


class FOLDR_FLIP_IMPLY(_IBase4foldr0_evalL):
    #class FOLDR_FLIP_IMPLY(_IBase4args_props):
    #class FLIP_IMPLY(_IBase4args_props):
    r'''
    as-if-foldr-but-eval-from_letf_to_right<flip-IMPLY>
    ====
    * FLIP_IMPLY
        (a <<== (b <<== (c <<== (... <<== (x <<== (y <<== (z <<== True)))))))

    * IMPLY
        (((((((True ==>> z) ==>> y) ==>> x) ==>> ...) ==>> c) ==>> b) ==>> a)

    ----
    FLIP_IMPLY(a,b,..,y,z, True) =[logic-when-no-err]= IMPLY(True, z,y,..,b,a)
        diff in eval path, shortcut diff
            FLIP_IMPLY eval (a or not FLIP_IMPLY(b,...z))
            IMPLY eval (not IMPLY(z,...b) or a)
    #'''
    ___the_tribool_flip_op_name___ = 'IMPLY' # 'FLIP_IMPLY'

    if 0:
      @override
      def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        cls = type(sf)

        is_rhs_NOT_phase = False
            # [x <<-- y]
            # x or not y
        rs = []
        for x in sf._props:
            r = x.eval_at_configuration__tribool(cached_env)
            rs.append(r)
            if r is True:
                #shortcut
                break
        return foldl0(TriBoolOps.IMPLY, True, reversed(rs))
            # not TriBoolOps..FLIP_IMPLY



class FOLDR_NOT_IMPLY(_IBase4foldr0_evalL):
    #class FOLDR_NOT_IMPLY(_IBase4args_props):
    r'''
    as-if-foldr-but-eval-from_letf_to_right<not-IMPLY>
    ====
    * NOT_IMPLY<2> x y = not (not x or y) = x and not y

    ----
    FOLDR_NOT_IMPLY(a,b,..,y,z, False) =[logic-when-no-err]= FOLDL_NOT_FLIP_IMPLY(False, z,y,..,b,a)
        diff in eval path, shortcut diff
            FOLDR_NOT_IMPLY eval (a and not FOLDR_NOT_IMPLY(b,...z))
            FOLDL_NOT_FLIP_IMPLY eval (not FOLDL_NOT_FLIP_IMPLY(z,...b) and a)
    #'''
    ___the_tribool_flip_op_name___ = 'NOT_IMPLY' # 'NOT_FLIP_IMPLY'

    if 0:
      @override
      def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        cls = type(sf)
        is_rhs_NOT_phase = False
            # [not [x -->> y]]
            # x and not y
        rs = []
        for x in sf._props:
            r = x.eval_at_configuration__tribool(cached_env)
            rs.append(r)
            if r is False:
                #shortcut
                break
        return foldl0(TriBoolOps.FLIP_NOT_IMPLY, False, reversed(rs))
            # not TriBoolOps..NOT_IMPLY


FOLDR_FLIP_IMPLY()
class NOR(_INOT_super, OR, _IBase4two_args_props):pass
class NAND(_INOT_super, AND, _IBase4two_args_props):pass
class XOR(FOLDU_XOR, _IBase4two_args_props):pass
class XNOR(FOLDU_XNOR, _IBase4two_args_props):pass
class IMPLY(FOLDL_IMPLY, _IBase4two_args_props):pass
class NOT_FLIP_IMPLY(FOLDL_NOT_FLIP_IMPLY, _IBase4two_args_props):pass
class FLIP_IMPLY(FOLDR_FLIP_IMPLY, _IBase4two_args_props):pass
class NOT_IMPLY(FOLDR_NOT_IMPLY, _IBase4two_args_props):pass











___begin_mark_of_excluded_global_names__233___ = ... #[[[
if 1:
    checker4callable_array = mk_checker__array(checker4callable)
    checker4uint = Checker__int_ge(0)
    checker4int = Checker__type_is(int)
    checker4std_mod2minmaxs = Checker__FrozenDict(checker4uint, mk_checker__pairs(checker4int, checker4int))

def _to_std__minmaxs(minmaxs, /):
    return mk_tuple(map(mk_tuple, minmaxs))
def _to_std__mod2minmaxs(mod2minmaxs, /):
    mod2minmaxs = dict(mod2minmaxs)
    mod2minmaxs = FrozenDict((mod, _to_std__minmaxs(minmaxs)) for mod, minmaxs in mod2minmaxs.items())
    return mod2minmaxs
def _check__mod2minmaxs(mod2minmaxs, /):
    checker4std_mod2minmaxs(mod2minmaxs)
def _iter_rngs_from_bouned_mod_minmaxs(total_input_props, mod, minmaxs, /):
    '-> Iter<rng> #unsorted_rngs'
    assert total_input_props >= 0
    assert mod > 0 # 0-->total_input_props+1
    END = total_input_props+1
    for m, M in minmaxs:
        m %= mod
        M %= mod
        if M < m:
            rngs = [(m, mod), (0, M+1)]
        else:
            rngs = [(m, M+1)]
        for begin, end in rngs:
            while True:
                if END < end:
                    if begin < END:
                        yield (begin, END)
                    break
                yield (begin, end)
                begin += mod
                end += mod
    return
if 0:
  def mod2minmaxs_to_solutiions(total_input_props, mod2minmaxs, /):
    solutions___acc_by_intersect = make_Ranges([(0, total_input_props+1)])
        # [rng] as set<uint>
        # rng = (min, max+1)
    for mod, minmaxs in mod2minmaxs.items():
        if mod < 0: raise TypeError
        if mod == 0:
            mod = total_input_props+1
        assert mod >= 1
        #solutions___acc_by_union = []
            # [rng] as set<uint>
        unsorted_rngs = _iter_rngs_from_bouned_mod_minmaxs(total_input_props, mod, minmaxs)
        #sorted_disjoint_rngs = merge unsorted_rngs to sorted_disjoint_rngs(unsorted_rngs)
        solutions___from_one_constraint = make_Ranges(sorted_rngs_to_iter_nontouch_ranges(sorted(unsorted_rngs)))
        solutions___acc_by_intersect &= solutions___from_one_constraint
    solutions = solutions___acc_by_intersect
    return solutions
else:
  def mod2minmaxs_to_solutiions(total_input_props, mod2minmaxs, /):
    solutions___acc_by_intersect = make_Ranges([(0, total_input_props+1)])
        # [rng] as set<uint>
        # rng = (min, max+1)
    def handle_neg(i):
        if i < 0:
            i += total_input_props+1
        #if not i >= 0:raise ValueError
        return i # may i < 0 again!!!
    for mod, minmaxs in mod2minmaxs.items():
        if mod < 0: raise TypeError
        elif mod < 0:
            #deprecated
            mod = handle_neg(mod)
            if mod <= 0: continue
        minmaxs = tuple((handle_neg(m), handle_neg(M)) for m,M in minmaxs)
        if mod == 0:
            minmaxs = ((max(m,0), min(M, total_input_props)) for m,M in minmaxs)
            minmaxs = tuple((m, M) for m,M in minmaxs if m<=M)
            mod = total_input_props+1
        assert mod >= 1
        #solutions___acc_by_union = []
            # [rng] as set<uint>
        unsorted_rngs = _iter_rngs_from_bouned_mod_minmaxs(total_input_props, mod, minmaxs)
        #sorted_disjoint_rngs = merge unsorted_rngs to sorted_disjoint_rngs(unsorted_rngs)
        solutions___from_one_constraint = make_Ranges(sorted_rngs_to_iter_nontouch_ranges(sorted(unsorted_rngs)))
        solutions___acc_by_intersect &= solutions___from_one_constraint
    solutions = solutions___acc_by_intersect
    return solutions
___end_mark_of_excluded_global_names__233___ = ... #]]]





class TOTAL(_IBase4args_props):
    r'''
    计数型
    测试 total_0s, total_1s, total_Ys 的 取值范围（可选 求模 之后）
    mod2minmaxs4F, mod2minmaxs4T, mod2minmaxs4Y ::{unt: [(int, int)]}
        mod/min/nax uniform on neg int:
        min/nax uniform on neg int:
            -1 = total_input_props
            -2 = total_input_props-1
            ... ...
            not i%mod!!!
            not i%(total_input_props+1)!!!

    ====deprecated:[[[
    why deprecated?
        cannot impl ANY
        ANY require abs hard lower bound
    mod2minmaxs4F, mod2minmaxs4T, mod2minmaxs4Y ::{uint: [(int, int)]}
        F - False - total_0s
        T - True - total_1s
        Y - Yet - total_Ys
        minmaxs :: [(int, int)]
            means "or"/"union" minmax ranges
        min, max :: int
            if mod > 0:
                -1 = (mod-1)%mod
                -2 = (mod-2)%mod
                ...
                NOTE: (-2, 1) means [-2..-1]++[0..1]
            if mod == 0:
                #as-if mod=num_props+1
                -1 = num_props = total_input_props
                -2 = num_props-1
                ...
    ====deprecated:]]]

    shortcut iff:
        ====static:
        total_input_props
        solutions4F, solutions4Y
        nonsolutions4F, nonsolutions4Y
            #mk solutions4F for mod2minmaxs4F,mod2minmaxs4T
            # NOTE: total_input_props==total_0s+total_1s+total_Ys ~~~ total_0s+total_1s
            #   total_Ys assume to be 0, since Y = {0,1} parallel at same time
        ====runtime:
        curr_num_0s
        curr_num_1s
        curr_num_Ys
        curr_num_remain_Ys
        =====
        assert total_input_props == (curr_num_0s + curr_num_1s + curr_num_Ys + curr_num_remain_Ys)
        =====
        #total_0s <- [curr_num_0s .. total_input_props-curr_num_1s]
        total_0s_possible_set_based_curr_info = [curr_num_0s .. total_input_props-curr_num_1s]
        total_Ys_possible_set_based_curr_info = [curr_num_Ys .. total_input_props-curr_num_0s-curr_num_1s]
        ===== shortcut for True iff
            && total_0s_possible_set_based_curr_info |<=| solutions4F
            && total_Ys_possible_set_based_curr_info |<=| solutions4Y
            return True
        ===== shortcut for False iff
            || total_0s_possible_set_based_curr_info |<=| nonsolutions4F
            || total_Ys_possible_set_based_curr_info |<=| nonsolutions4Y
            return False
        ===== shortcut for Yet/Ellipsis iff
            && [NEVER [total_0s_possible_set_based_curr_info |<=| nonsolutions4F]]
            && [NEVER [total_Ys_possible_set_based_curr_info |<=| nonsolutions4Y]]
            && (
                || [NEVER [total_0s_possible_set_based_curr_info |<=| solutions4F]]
                || [NEVER [total_Ys_possible_set_based_curr_info |<=| solutions4Y]]
                        #impossible/useless
                        #见下面推导
                )
            <==>
            && [NEVER [total_0s_possible_set_based_curr_info |<=| nonsolutions4F]]
            && [NEVER [total_0s_possible_set_based_curr_info |<=| solutions4F]]
            && [total_Ys_possible_set_based_curr_info |<=| solutions4Y]

            ######################
            for 0s * solutions4F/nonsolutions4F:
                [NEVER [possible_rng |<=| rngs]]
                <==> [curr_num_Ys >= max ({0}\-/{len rng | rng <- rngs /-\ possible_rng_based_curr_info})]
            ######################
            for Ys * solutions4Y/nonsolutions4Y:
                [NEVER [possible_rng |<=| rngs]]
                <==> [{} == rngs /-\ possible_rng_based_curr_info]
                因为 curr_num_remain_Ys 可能全部分配给0/1，最终total_Ys==curr_num_Ys，只要 上面的交集非空，则必可 通过分配 curr_num_remain_Ys 而使total_Ys跻身其中。
                curr_num_0s有个不确定因素curr_num_Ys
                而curr_num_Ys则没有，或者说值为0，这样一来，0s的结论 便退化为Ys的结论
                [NEVER [total_Ys_possible_set_based_curr_info |<=| nonsolutions4Y]]
                <==> [{} == total_Ys_possible_set_based_curr_info/-\nonsolutions4Y]
                <==> [total_Ys_possible_set_based_curr_info |<=| solutions4Y]
        ===== otherwise not-shortcut
        raise logic-err
        return ...#Tribool::Yet

    #'''
    @override
    def ___get_args_kwargs___(sf, /):
        args, kwargs = super().___get_args_kwargs___()
        extra_kwargs = dict(
            mod2minmaxs4F = sf._mod2minmaxs4F
            ,mod2minmaxs4T = sf._mod2minmaxs4T
            ,mod2minmaxs4Y = sf._mod2minmaxs4Y
            )
        return (args, {**kwargs, **extra_kwargs})
    def __init__(sf, /, *props, mod2minmaxs4F, mod2minmaxs4T, mod2minmaxs4Y, props_false=False, props_vs_vars=False):
        super().__init__(*props, props_false=props_false, props_vs_vars=props_vs_vars)
        sf._mod2minmaxs4F = mod2minmaxs4F
        sf._mod2minmaxs4T = mod2minmaxs4T
        sf._mod2minmaxs4Y = mod2minmaxs4Y
        ######################
        ######################
        ######################
        if 1:
            #std&check
            #std immutable check
            ls = [mod2minmaxs4F, mod2minmaxs4T, mod2minmaxs4Y]

            [*ls] = map(_to_std__mod2minmaxs, ls)
            [mod2minmaxs4F, mod2minmaxs4T, mod2minmaxs4Y] = ls
            [*_] = map(_check__mod2minmaxs, ls)
        ######################
        ######################
        ######################
        total_input_props = len(sf._props)

        if 1:
            #mk solutions4F for mod2minmaxs4F,mod2minmaxs4T
            # NOTE: total_input_props==total_0s+total_1s+total_Ys ~~~ total_0s+total_1s
            #   total_Ys assume to be 0, since Y = {0,1} parallel at same time
            #
            #
            local_solutions4F = mod2minmaxs_to_solutiions(total_input_props, mod2minmaxs4F)
            local_solutions4T = mod2minmaxs_to_solutiions(total_input_props, mod2minmaxs4T)
            local_solutions4F__fromT = make_Ranges((total_input_props-end+1, total_input_props-begin+1) for begin, end in reversed(local_solutions4T.to_nontouch_ranges()))
            solutions4F = local_solutions4F & local_solutions4F__fromT
            del local_solutions4F
            del local_solutions4T
            del local_solutions4F__fromT
        solutions4F

        solutions4Y = mod2minmaxs_to_solutiions(total_input_props, mod2minmaxs4Y)

        if 0:
            whole_set = make_Ranges([(0, total_input_props+1)])
            nonsolutions4F = whole_set - solutions4F
            nonsolutions4Y = whole_set - solutions4Y

        ######################
        ######################
        total_input_props
        solutions4F, solutions4Y
        if 0:
            nonsolutions4F, nonsolutions4Y
        ######################
        sf._total_input_props = total_input_props
        sf._solutions4F = solutions4F
        sf._solutions4Y = solutions4Y
        if 0:
            sf._nonsolutions4F = nonsolutions4F
            sf._nonsolutions4Y = nonsolutions4Y
        ######################
        ######################
        sf._args4F = _ShortCutDetect.mk_args_from_nontouch_ranges_between(0, total_input_props+1, solutions4F.to_nontouch_ranges())
        sf._args4Y = _ShortCutDetect.mk_args_from_nontouch_ranges_between(0, total_input_props+1, solutions4Y.to_nontouch_ranges())

    @override
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        cls = type(sf)
        total_input_props = sf._total_input_props
        solutions4F = sf._solutions4F
        solutions4Y = sf._solutions4Y
        #nonsolutions4F = sf._nonsolutions4F
        #nonsolutions4Y = sf._nonsolutions4Y
        detect4F = _ShortCutDetect(solutions4F, (0, total_input_props+1), *sf._args4F)
        detect4Y = _ShortCutDetect(solutions4Y, (0, total_input_props+1), *sf._args4Y)
        def detect_shortcut():
            #-> tribool
            f = detect4F.get_result_tribool()
            y = detect4Y.get_result_tribool()
            #return f is False or y is False or (f is True is y)
            if f is False or y is False:
                return False
            if (f is True is y):
                return True
            if (f is ... and True is y):
                return ...
            return None

        for x in sf._props:
            if detect_shortcut() is not None:
                break
            ######################
            r = x.eval_at_configuration__tribool(cached_env)
            if r is False:
                #num_0s += 1
                detect4F.inc_begin()
                detect4Y.dec_end()
                #no: detect4Y.inc_num_indetermine()
                #   Ys itself is num_indetermine, has no num_indetermine about it
            elif r is True:
                #num_1s += 1
                detect4F.dec_end()
                detect4Y.dec_end()
                pass
            elif r is ...:
                #num_Ys += 1
                detect4Y.inc_begin()
                #no: detect4F.dec_end()
                #   since Y contains 0
                detect4F.inc_num_indetermine()
            else:
                raise logic-err
        #else: raise logic-err
        #return detect_shortcut()
        r = detect_shortcut()
        if r is None:
            if detect_shortcut() is None: raise logic-err
            raise logic-err
        return r


    #sorted_rngs_to_iter_nontouch_ranges
    #make_Ranges

if 1:
    #internal util class 4 class-TOTAL
    class _MultiSet4keys_are_frozen_lens:
        def copy(sf, /):
            return __class__(sf._rnggap_len2jjj, sf._jjj2rnggap_len_count_pair)
        def __init__(sf, rnggap_len2jjj, jjj2rnggap_len_count_pair, /):
            sf._rnggap_len2jjj = rnggap_len2jjj
            sf._jjj2rnggap_len_count_pair = list(jjj2rnggap_len_count_pair)
                #used-as-mutable-multiset
            sf._valid()
        def _valid(sf, /):
            if not (not sf._jjj2rnggap_len_count_pair or sf._jjj2rnggap_len_count_pair[-1][1] > 0):raise logic-err
        def remove_one_rnggap_len(sf, rnggap_len, /):
            if not rnggap_len > 0: raise KeyError
            j = sf._rnggap_len2jjj[rnggap_len]
            (_saved_rnggap_len_, _old_count_) = sf._jjj2rnggap_len_count_pair[j]
            assert _saved_rnggap_len_ == rnggap_len
            if not _old_count_ > 0: raise KeyError
            sf._jjj2rnggap_len_count_pair[j] = (_saved_rnggap_len_, _old_count_-1)
            while sf._jjj2rnggap_len_count_pair and sf._jjj2rnggap_len_count_pair[-1][1]==0:
                sf._jjj2rnggap_len_count_pair.pop()
            sf._valid()
        def get_max_rnggap_len_or_0(sf, /):
            return 0 if not sf._jjj2rnggap_len_count_pair else sf._jjj2rnggap_len_count_pair[-1][0]
        def __bool__(sf, /):
            raise logic-err
        r'''
        def __len__(sf, /):
            return len(sf._jjj2rnggap_len_count_pair)
        #'''

    class _ShortCutDetect:
        @classmethod
        def mk_args_from_nontouch_ranges_between(cls, begin, end, nontouch_ranges, /):
            if not begin < end: raise ValueError
                # nonempty...
            rnggap_bounaries = [i for rng in nontouch_ranges for i in rng]
            if rnggap_bounaries:
                if not begin <= rnggap_bounaries[0]: raise ValueError
                if not rnggap_bounaries[-1] <= end: raise ValueError
            if not rnggap_bounaries or rnggap_bounaries[0]:
                rnggap_bounaries.insert(0, begin)
            if rnggap_bounaries[-1] != end:
                rnggap_bounaries.append(end)
            assert 2 <= len(rnggap_bounaries) <= end-begin+1
            rnggap_lens = tuple(map(opss.__sub__, rnggap_bounaries[1:], rnggap_bounaries[:-1]))
            if not all(L > 0 for L in rnggap_lens): raise ValueError
            assert sum(rnggap_lens) == end-begin
            assert 1 <= len(rnggap_lens) == len(rnggap_bounaries)-1 <= end-begin
            iii2rnggap_bounaries = rnggap_bounaries
            iii2rnggap_lens = rnggap_lens
            rnggap_len2count = collections.Counter(rnggap_lens)
            jjj2rnggap_len_count_pair = rnggap_len_count_pairs = tuple(sorted(rnggap_len2count.items()))
            #jjj2rnggap_len = (*map(fst, rnggap_len_count_pairs),)
            #jjj2count = (*map(snd, rnggap_len_count_pairs),)
            rnggap_len2jjj = [None]*(1+max(rnggap_lens))
            for j, (rnggap_len, count) in enumerate(rnggap_len_count_pairs):
                rnggap_len2jjj[rnggap_len] = j
            rnggap_len2jjj = (*rnggap_len2jjj,)

            return (iii2rnggap_bounaries, rnggap_len2jjj, jjj2rnggap_len_count_pair)
        def __init__(sf, solutions:'Ranges', initial_possible_rng, iii2rnggap_bounaries, rnggap_len2jjj, jjj2rnggap_len_count_pair, /):
            sf.solution_rngs = solutions.to_nontouch_ranges()
            sf.begin, sf.end = initial_possible_rng
            sf.eqv_end = sf._search()
            ######################

            if 1:
                #put this section before calling sf._calc_result_tribool()
                ######################
                sf._iii2rnggap_bounaries = iii2rnggap_bounaries
                assert iii2rnggap_bounaries
                if not sf.begin == iii2rnggap_bounaries[0] == 0: raise logic-err
                if not sf.end == iii2rnggap_bounaries[-1]: raise logic-err # == total_input_props+1
                assert sf.begin < sf.end

                sf.ibegin = 0
                sf.iend = len(iii2rnggap_bounaries)-1
                assert sf.begin < sf.end
                assert sf.ibegin < sf.iend
                sf._check__xxx__ixxx(sf.begin, sf.ibegin)
                sf._check__xxx__ixxx(sf.end, sf.iend)
                #sf._on_begin_leaving_boundary()
                #sf._on_end_leaving_boundary()
                sf._end_side_incomplete_rnggap_len = 0
                sf._begin_side_incomplete_rnggap_len = 0
                sf.num_indetermine = 0
                sf._ms = _MultiSet4keys_are_frozen_lens(rnggap_len2jjj, jjj2rnggap_len_count_pair)
            ######################


            sf.result_tribool = None
            sf.result_tribool = sf._calc_result_tribool()
                # False -> . <= nonsolutions
                # True -> . <= solutions
                # ... -> [NEVER [[. <= nonsolutions]or[. <= solutions]]]
                # None -> not shortcut
            ######################
        def _check__xxx__ixxx(sf, xxx, ixxx, /):
            if not 0 <= ixxx < len(sf._iii2rnggap_bounaries):raise TypeError
            if not (sf._iii2rnggap_bounaries[ixxx] <= xxx): raise logic-err
            if not (ixxx == len(sf._iii2rnggap_bounaries)-1 or xxx < sf._iii2rnggap_bounaries[ixxx+1]): raise logic-err
        def _get_rnggap_len__begin_at_iii(sf, iii, /):
            return sf._iii2rnggap_bounaries[iii+1] - sf._iii2rnggap_bounaries[iii]
        def _on_end_leaving_boundary(sf, /):
            assert sf.begin < sf.end
            assert sf.ibegin < sf.iend
            if not (sf._iii2rnggap_bounaries[sf.iend] == sf.end): raise logic-err
            if not 0 == sf._end_side_incomplete_rnggap_len: raise logic-err
            sf.iend -= 1
            assert sf.ibegin <= sf.iend
            if sf.ibegin < sf.iend or (sf._iii2rnggap_bounaries[sf.ibegin] == sf.begin):
                rnggap_len = sf._get_rnggap_len__begin_at_iii(sf.iend)
                sf._ms.remove_one_rnggap_len(rnggap_len)
                sf._end_side_incomplete_rnggap_len = rnggap_len -1
            else:
                pass#leave 0
            #sf.end -= 1
        def _on_begin_leaving_boundary(sf, /):
            assert sf.begin < sf.end
            #may not:assert sf.ibegin < sf.iend
            assert sf.ibegin <= sf.iend
            if not (sf._iii2rnggap_bounaries[sf.ibegin] == sf.begin): raise logic-err
            if not 0 == sf._begin_side_incomplete_rnggap_len: raise logic-err
            #no: sf.ibegin += 1
            if sf.ibegin < sf.iend:
                rnggap_len = sf._get_rnggap_len__begin_at_iii(sf.ibegin)
                sf._ms.remove_one_rnggap_len(rnggap_len)
                sf._begin_side_incomplete_rnggap_len = rnggap_len -1
                if 0:
                    #move out to inc_begin()
                    if rnggap_len == 1:
                        sf.ibegin += 1
            else:
                pass#leave 0
            #sf.begin += 1

        def get_result_tribool(sf, /):
            return sf.result_tribool
        def _calc_result_tribool(sf, /):
            r = sf.__calc_result_tribool()
            assert sf.result_tribool is None or r is sf.result_tribool
            return r
        def __calc_result_tribool(sf, /):
            assert sf.begin < sf.end
            if sf.eqv_end == len(sf.solution_rngs):
                return False
            rng_begin, rng_end = sf.solution_rngs[sf.eqv_end]
            assert sf.begin < rng_end
            assert sf.eqv_end==0 or sf.solution_rngs[sf.eqv_end-1][-1] <= sf.begin
            if sf.begin < sf.end <= rng_begin < rng_end:
                # on left side
                # |<=| nonsolutions
                return False
            if rng_begin <= sf.begin < sf.end <= rng_end:
                # inside
                # |<=| solutions
                return True
            #
            #
            #
            #if sf.begin < rng_begin < rng_end < sf.end:
                # enclose
            #if sf.begin < rng_begin < sf.end <= rng_end:
                # left-cross
            #if rng_begin <= sf.begin < rng_end < sf.end:
                # right-cross
            #
            #
            #
            if sf.num_indetermine >= max(sf._begin_side_incomplete_rnggap_len, sf._ms.get_max_rnggap_len_or_0(), sf._end_side_incomplete_rnggap_len):
                return ...
            return None
        def _search(sf, /):
            'find i s.t. rngs[i-1].end <= sf.begin < rngs[i].end'
            eqv_begin, eqv_end = bisearch(sf.begin, sf.solution_rngs, key=snd)
            return eqv_end
        def inc_num_indetermine(sf, /):
            sf.num_indetermine += 1
            sf.result_tribool = sf._calc_result_tribool()
        def inc_begin(sf, /):
            assert sf.begin < sf.end
            #may not:assert sf.ibegin < sf.iend
            assert sf.ibegin <= sf.iend
            if sf._begin_side_incomplete_rnggap_len == 0:
                #[sf.ibegin == sf.iend] ==>> [_begin_side_incomplete_rnggap_len == 0] means Nothing not means at boundary!!!
                #[sf.ibegin < sf.iend] ==>> [_begin_side_incomplete_rnggap_len == 0] means at boundary!!!
                if sf.ibegin < sf.iend:
                    sf._on_begin_leaving_boundary()
                    is_new_begin_side_incomplete_rnggap_len = True
                else:
                    is_new_begin_side_incomplete_rnggap_len = False
            else:
                sf._begin_side_incomplete_rnggap_len -= 1
                is_new_begin_side_incomplete_rnggap_len = True
            if sf._begin_side_incomplete_rnggap_len == 0 and is_new_begin_side_incomplete_rnggap_len:

                if 0 and not sf.ibegin < sf.iend:
                    print_err(f'sf.ibegin={sf.ibegin}')
                    print_err(f'sf.iend={sf.iend}')
                    print_err(f'sf.begin={sf.begin}')
                    print_err(f'sf.end={sf.end}')
                assert sf.ibegin < sf.iend
                sf.ibegin += 1
                assert sf.ibegin <= sf.iend
            sf.begin += 1
            if not sf.begin < sf.end: raise logic-err
            if not sf.eqv_end == len(sf.solution_rngs):
                rng_begin, rng_end = sf.solution_rngs[sf.eqv_end]
                if not sf.begin < rng_end:
                    sf.eqv_end += 1

            if not sf.eqv_end == len(sf.solution_rngs):
                rng_begin, rng_end = sf.solution_rngs[sf.eqv_end]
                assert sf.begin < rng_end

            sf.result_tribool = sf._calc_result_tribool()

        def dec_end(sf, /):
            if sf._end_side_incomplete_rnggap_len == 0:
                #see: inc_begin
                if sf.ibegin < sf.iend:
                    sf._on_end_leaving_boundary()
                else:
                    pass
            else:
                sf._end_side_incomplete_rnggap_len -= 1
            sf.end -= 1
            if not sf.begin < sf.end: raise logic-err
            sf.result_tribool = sf._calc_result_tribool()



if 1:
    #alias for XOR/XNOR
    if 1:
        # prime:
        class _IBase4kwargs_at_cls4TOTAL(TOTAL):
            @abstractmethod
            class ___the_mod2minmaxs4F___:pass
            @abstractmethod
            class ___the_mod2minmaxs4T___:pass
            @abstractmethod
            class ___the_mod2minmaxs4Y___:pass
            @override
            def ___get_args_kwargs___(sf, /):
                args, kwargs = super().___get_args_kwargs___()
                kwargs = {**kwargs}
                del kwargs['mod2minmaxs4F']
                del kwargs['mod2minmaxs4T']
                del kwargs['mod2minmaxs4Y']
                return (args, kwargs)
            def __init__(sf, /, *props, props_false=False, props_vs_vars=False):
                cls = type(sf)
                super().__init__(*props, props_false=props_false, props_vs_vars=props_vs_vars, mod2minmaxs4F=cls.___the_mod2minmaxs4F___, mod2minmaxs4T=cls.___the_mod2minmaxs4T___, mod2minmaxs4Y=cls.___the_mod2minmaxs4Y___)
        class ALL(_IBase4kwargs_at_cls4TOTAL):
            ___the_mod2minmaxs4F___ = {}
            ___the_mod2minmaxs4T___ = {0:[(-1,-1)]}
            ___the_mod2minmaxs4Y___ = {}
        class ANY(_IBase4kwargs_at_cls4TOTAL):
            ___the_mod2minmaxs4F___ = {}
            ___the_mod2minmaxs4T___ = {0:[(1,-1)]}
            ___the_mod2minmaxs4Y___ = {}
        class ODD_TOTAL_TRUE(_IBase4kwargs_at_cls4TOTAL):
            #XOR___ODD_TOTAL_TRUE
            ___the_mod2minmaxs4F___ = {}
            ___the_mod2minmaxs4T___ = {2:[(1,1)]}
            ___the_mod2minmaxs4Y___ = {}
        class EXACTLY_SINGLE_TRUE(_IBase4kwargs_at_cls4TOTAL):
            #XOR___EXACTLY_SINGLE_TRUE
            ___the_mod2minmaxs4F___ = {}
            ___the_mod2minmaxs4T___ = {0:[(1,1)]}
            ___the_mod2minmaxs4Y___ = {}
        class EXACTLY_SINGLE_FALSE(_IBase4kwargs_at_cls4TOTAL):
            #XOR___EXACTLY_SINGLE_FALSE
            ___the_mod2minmaxs4F___ = {0:[(1,1)]}
            ___the_mod2minmaxs4T___ = {}
            ___the_mod2minmaxs4Y___ = {}
        class EVEN_TOTAL_FALSE(_IBase4kwargs_at_cls4TOTAL):
            #XNOR___EVEN_TOTAL_FALSE
            ___the_mod2minmaxs4F___ = {2:[(0,0)]}
            ___the_mod2minmaxs4T___ = {}
            ___the_mod2minmaxs4Y___ = {}
        class PAIRWISE_EQU(_IBase4kwargs_at_cls4TOTAL):
            #XNOR___PAIRWISE_EQU
            ___the_mod2minmaxs4F___ = {0:[(0,0),(-1,-1)]}
            ___the_mod2minmaxs4T___ = {}
            ___the_mod2minmaxs4Y___ = {}
    if 1:
        # prime:
        ODD_TOTAL_TRUE
        EXACTLY_SINGLE_TRUE
        EXACTLY_SINGLE_FALSE
        EVEN_TOTAL_FALSE
        PAIRWISE_EQU
    if 1:
        # derived
        # XOR___+...
        #class FOLDU_XOR(ODD_TOTAL_TRUE):pass
        # not $ XNOR___...
        class ODD_TOTAL_FALSE(_INOT_super, EVEN_TOTAL_FALSE):pass
        if 1:
            class NOT_FOLDU_XNOR(ODD_TOTAL_FALSE):pass
        class NOT_PAIRWISE_EQU(_INOT_super, PAIRWISE_EQU):pass
        if 1:
            class SOME_NOT_EQU(NOT_PAIRWISE_EQU):pass
            class NOT_ALL_THE_SAME(NOT_PAIRWISE_EQU):pass
            class NOT_ALL_EQU(NOT_PAIRWISE_EQU):pass
            class ANY_NOT_EQU(NOT_PAIRWISE_EQU):pass
    #NOT_XOR/XNOR --->
        # XNOR___+...
        if 1:
            #class FOLDU_XNOR(EVEN_TOTAL_FALSE):pass
            pass
        if 1:
            class EQU(PAIRWISE_EQU):pass
            class ALL_THE_SAME(PAIRWISE_EQU):pass
            class ALL_EQU(PAIRWISE_EQU):pass
        # not $ XOR___...
        class EVEN_TOTAL_TRUE(_INOT_super, ODD_TOTAL_TRUE):pass
        if 1:
            class NOT_FOLDU_XOR(EVEN_TOTAL_TRUE):pass
        class NOT_EXACTLY_SINGLE_TRUE(_INOT_super, EXACTLY_SINGLE_TRUE):pass
        class NOT_EXACTLY_SINGLE_FALSE(_INOT_super, EXACTLY_SINGLE_FALSE):pass

if 0:
    # prefix: XOR___...
    # prefix: XNOR___...
    XOR___ODD_TOTAL_TRUE = ODD_TOTAL_TRUE
    XOR___EXACTLY_SINGLE_TRUE = EXACTLY_SINGLE_TRUE
    XOR___EXACTLY_SINGLE_FALSE = EXACTLY_SINGLE_FALSE

    XNOR___EVEN_TOTAL_FALSE = EVEN_TOTAL_FALSE
    XNOR___PAIRWISE_EQU = PAIRWISE_EQU

    if 1:
        # derived
        # XOR___+...
        #.,.+11s/^\(\s*\)class \(\w*\)(.*$/\1XOR___\2 = \2
        XOR___FOLDU_XOR = FOLDU_XOR
        # not $ XNOR___...
        XOR___ODD_TOTAL_FALSE = ODD_TOTAL_FALSE
        if 1:
            XOR___NOT_FOLDU_XNOR = NOT_FOLDU_XNOR
        XOR___NOT_PAIRWISE_EQU = NOT_PAIRWISE_EQU
        if 1:
            XOR___SOME_NOT_EQU = SOME_NOT_EQU
            XOR___NOT_ALL_THE_SAME = NOT_ALL_THE_SAME
            XOR___NOT_ALL_EQU = NOT_ALL_EQU
            XOR___ANY_NOT_EQU = ANY_NOT_EQU
        # XNOR___+...
        #.,.+11s/^\(\s*\)class \(\w*\)(.*$/\1XNOR___\2 = \2
        if 1:
            XNOR___FOLDU_XNOR = FOLDU_XNOR
        if 1:
            XNOR___EQU = EQU
            XNOR___ALL_THE_SAME = ALL_THE_SAME
            XNOR___ALL_EQU = ALL_EQU
        # not $ XOR___...
        XNOR___EVEN_TOTAL_TRUE = EVEN_TOTAL_TRUE
        if 1:
            XNOR___NOT_FOLDU_XOR = NOT_FOLDU_XOR
        XNOR___NOT_EXACTLY_SINGLE_TRUE = NOT_EXACTLY_SINGLE_TRUE
        XNOR___NOT_EXACTLY_SINGLE_FALSE = NOT_EXACTLY_SINGLE_FALSE




else:
    # prefix: XOR___...
    # prefix: XNOR___...

    #.,.+36s/^\(\s*\)\(\w*\) = \(\w*\)$/\1class \2(\3):pass
    class XOR___ODD_TOTAL_TRUE(ODD_TOTAL_TRUE):pass
    class XOR___EXACTLY_SINGLE_TRUE(EXACTLY_SINGLE_TRUE):pass
    class XOR___EXACTLY_SINGLE_FALSE(EXACTLY_SINGLE_FALSE):pass

    class XNOR___EVEN_TOTAL_FALSE(EVEN_TOTAL_FALSE):pass
    class XNOR___PAIRWISE_EQU(PAIRWISE_EQU):pass

    if 1:
        # derived
        # XOR___+...
        #.,.+11s/^\(\s*\)class \(\w*\)(.*$/\1XOR___\2 = \2
        class XOR___FOLDU_XOR(FOLDU_XOR):pass
        # not $ XNOR___...
        class XOR___ODD_TOTAL_FALSE(ODD_TOTAL_FALSE):pass
        if 1:
            class XOR___NOT_FOLDU_XNOR(NOT_FOLDU_XNOR):pass
        class XOR___NOT_PAIRWISE_EQU(NOT_PAIRWISE_EQU):pass
        if 1:
            class XOR___SOME_NOT_EQU(SOME_NOT_EQU):pass
            class XOR___NOT_ALL_THE_SAME(NOT_ALL_THE_SAME):pass
            class XOR___NOT_ALL_EQU(NOT_ALL_EQU):pass
            class XOR___ANY_NOT_EQU(ANY_NOT_EQU):pass
        # XNOR___+...
        #.,.+11s/^\(\s*\)class \(\w*\)(.*$/\1XNOR___\2 = \2
        if 1:
            class XNOR___FOLDU_XNOR(FOLDU_XNOR):pass
        if 1:
            class XNOR___EQU(EQU):pass
            class XNOR___ALL_THE_SAME(ALL_THE_SAME):pass
            class XNOR___ALL_EQU(ALL_EQU):pass
        # not $ XOR___...
        class XNOR___EVEN_TOTAL_TRUE(EVEN_TOTAL_TRUE):pass
        if 1:
            class XNOR___NOT_FOLDU_XOR(NOT_FOLDU_XOR):pass
        class XNOR___NOT_EXACTLY_SINGLE_TRUE(NOT_EXACTLY_SINGLE_TRUE):pass
        class XNOR___NOT_EXACTLY_SINGLE_FALSE(NOT_EXACTLY_SINGLE_FALSE):pass






r'''
VAR
常数，未定义/错误
NOT
proxy underlying expr
    ALL ANY
    NOT_ALL NOT_ANY
    ALL_NOT ANY_NOT
    NOT_ALL_NOT NOT_ANY_NOT

    ALL_VAR ANY_VAR ...
    NOT_ALL_VAR NOT_ANY_VAR ...
    ALL_NOT_VAR ANY_NOT_VAR ...
    NOT_ALL_NOT_VAR NOT_ANY_NOT_VAR ...

    ALL = AND
    ANY = OR
    ANY_NOT = NOT_ALL
    ALL_NOT = NOT_ANY
    NOT_ALL_NOT = ANY
    NOT_ANY_NOT = ALL

计数型:
    至少 几个 1/0...
    num_0s, num_1s, mod div...
#'''


class VAR(IProposition, ABC__no_slots):
    #__slots__ = '_var'
    def __init__(sf, variable_name, /):
        if isinstance(variable_name, IProposition):raise TypeError
        #hash(variable_name)
        sf._var = variable_name

    @override
    def ___get_args_kwargs___(sf, /):
        return ((sf._var,), {})
    @override
    def ___iter_variable_names___(sf, /):
        'iter_variable_names'
        yield sf._var
    @override
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        return cached_env.query__env_variable_name2tribool(sf._var)

class _IBase4const(IProposition, ISingleton, final=None):
    __slots__ = ()
    @abstractmethod
    class ___the_tribool_value___:pass
    #def __init__(sf, /): return

    @override
    def ___get_args_kwargs___(sf, /):
        return ((), {})
    @override
    def ___iter_variable_names___(sf, /):
        'iter_variable_names'
        return null_iter
    @override
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        cls = type(sf)
        return cls.___the_tribool_value___

class FALSE(_IBase4const):
    __slots__ = ()
    ___the_tribool_value___ = False
class TRUE(_IBase4const):
    __slots__ = ()
    ___the_tribool_value___ = True
class YET(_IBase4const):
    __slots__ = ()
    ___the_tribool_value___ = ...
the_FALSE = FALSE()
the_TRUE = TRUE()
the_YET = YET()
assert the_FALSE is FALSE()
assert the_TRUE is TRUE()
assert the_YET is YET()


class EvalError(Exception):pass
class ERROR(IProposition, ABC__no_slots):
    def __init__(sf, fmt, /, *env_variable_names, **fmt_var_name2env_variable_name):
        sf._fmt = fmt
        sf._env_variable_names = env_variable_names
        sf._fmt_var_name2env_variable_name = fmt_var_name2env_variable_name

    @override
    def ___get_args_kwargs___(sf, /):
        return ((sf._fmt, *sf._env_variable_names), MapView(sf._fmt_var_name2env_variable_name))
    @override
    def ___iter_variable_names___(sf, /):
        'iter_variable_names'
        yield from sf._env_variable_names
        yield from sf._fmt_var_name2env_variable_name.values()

    @override
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        f = cached_env.query__env_variable_name2tribool
        args = map(f, sf._env_variable_names)
        kwargs = {fmt_var:f(env_var) for fmt_var, env_var in sf._fmt_var_name2env_variable_name.items()}
        err_msg = sf._fmt.format(*args, **kwargs)
        raise EvalError(err_msg)





class _Base4proxy(IProposition, ABC__no_slots):
    'ECHO'
    def __init__(sf, proposition, /):
        check_funcs.instance(IProposition, proposition)
        sf._prop = proposition

    @override
    def ___get_args_kwargs___(sf, /):
        return ((sf._prop,), {})
    @override
    def ___iter_variable_names___(sf, /):
        'iter_variable_names'
        return sf._prop.iter_variable_names()
    @override
    def ___eval_at_configuration__tribool___(sf, cached_env, /):
        'eval_at_configuration__tribool'
        return (sf._prop.eval_at_configuration__tribool(cached_env))




class NOT(_INOT_super, _Base4proxy): pass
class NOT_VAR(_INOT_super, VAR): pass




#class ALL(AND):pass
#class ANY(OR):pass
class NOT_ALL(_INOT_super, ALL):pass
class NOT_ANY(_INOT_super, ANY):pass
#class XNOR(_INOT_super, XOR):pass
#class ODD_TOTAL_TRUE(XOR):pass
#class EVEN_TOTAL_TRUE(XNOR):pass
#class ODD_TOTAL_FALSE(_INOT_super, EVEN_TOTAL_FALSE):pass

#.,.+7s/^\(\w*\)\s*=\s*\(\w*\)$/class \1(\2):pass
if 0:
    #XOR_NOT = ODD_TOTAL_FALSE
    #XNOR_NOT = EVEN_TOTAL_FALSE
    XOR_NOT = XOR #op<2>
    XNOR_NOT = XNOR #op<2>
    #
    ANY_NOT = NOT_ALL
    ALL_NOT = NOT_ANY
    NOT_ALL_NOT = ANY
    NOT_ANY_NOT = ALL
else:
    #class XOR_NOT(ODD_TOTAL_FALSE):pass
    #class XNOR_NOT(EVEN_TOTAL_FALSE):pass
    #class XOR_NOT(XOR):pass #op<2>
    #class XNOR_NOT(XNOR):pass #op<2>
    #
    class ANY_NOT(NOT_ALL):pass
    class ALL_NOT(NOT_ANY):pass
    class NOT_ALL_NOT(ANY):pass
    class NOT_ANY_NOT(ALL):pass




class _IBase4args_false_props(_IBase4args_props):
    'suffix:...NOT'
    def __init__(sf, /, *props):
        sf.__false_props = props
        super().__init__(*map(NOT, props))
    @override
    def ___get_args_kwargs___(sf, /):
        return (sf.__false_props, {})
class _IBase4args_vars(_IBase4args_props):
    'suffix:...VAR'
    def __init__(sf, /, *variable_names):
        sf._variable_names = variable_names
        super().__init__(*map(VAR, variable_names))

    @override
    def ___get_args_kwargs___(sf, /):
        return (sf._variable_names, {})
class _IBase4args_false_vars(_IBase4args_vars, _IBase4args_false_props):
    'suffix:...NOT_VAR'
    pass

class _IBase4two_args_vars(_IBase4args_vars, _IBase4two_args_props):
    'op<2>'
    def __init__(sf, lhs_var_name, rhs_var_name, /,*, props_false=False, props_vs_vars=False):
        super().__init__(lhs_var_name, rhs_var_name, props_false=props_false, props_vs_vars=props_vs_vars)

if 0:
    # this bases order is fail to take kwargs
    class XOR_VAR(XOR, _IBase4two_args_vars):pass
    class XNOR_VAR(XNOR, _IBase4two_args_vars):pass
    class ALL_VAR(ALL, _IBase4args_vars):pass
    class ANY_VAR(ANY, _IBase4args_vars):pass
else:
    class XOR_VAR(_IBase4args_vars, XOR):pass
    class XNOR_VAR(_IBase4args_vars, XNOR):pass
    class ALL_VAR(_IBase4args_vars, ALL):pass
    class ANY_VAR(_IBase4args_vars, ANY):pass


class NOT_ALL_VAR(_INOT_super, ALL_VAR):pass
class NOT_ANY_VAR(_INOT_super, ANY_VAR):pass
#class XNOR_VAR(_INOT_super, XOR_VAR):pass

#.,.+7s/^\(\w*\)\s*=\s*\(\w*\)$/class \1(\2):pass
if 0:
    ALL_NOT_VAR = NOT_ANY_VAR
    ANY_NOT_VAR = NOT_ALL_VAR
    NOT_ALL_NOT_VAR = ANY_VAR
    NOT_ANY_NOT_VAR = ALL_VAR
else:
    class ALL_NOT_VAR(NOT_ANY_VAR):pass
    class ANY_NOT_VAR(NOT_ALL_VAR):pass
    class NOT_ALL_NOT_VAR(ANY_VAR):pass
    class NOT_ANY_NOT_VAR(ALL_VAR):pass



class CHAIN_NEIGHBOR(_IBase4args_props, _Base4proxy):
    def __init__(sf, prop0, bin_op, prop1, /, *op_prop_eithers, props_false=False, props_vs_vars=False):
        if len(op_prop_eithers)%2: raise TypeError
        sf.__saved_args = (prop0, bin_op, prop1, *op_prop_eithers)
        del prop0, bin_op, prop1

        pseudo_props = sf.__saved_args[0::2]
        bin_op_ls = sf.__saved_args[1::2]
        assert 1 <= len(bin_op_ls) == len(pseudo_props)-1
        #not: check_funcs.instance_all(IProposition, pseudo_props)
        #   maybe variable_names
        #check_funcs.instance_all(Callable, bin_op_ls)
        checker4callable_array(bin_op_ls)

        #bug: missing "sf": _IBase4args_props.__init__(*pseudo_props, props_false=props_false, props_vs_vars=props_vs_vars)
        _IBase4args_props.__init__(sf, *pseudo_props, props_false=props_false, props_vs_vars=props_vs_vars)
        real_props = sf._props
        assert len(bin_op_ls)+1 == len(pseudo_props) == len(real_props)
        #bug: missing "*": whole_prop = ALL((op(lhs, rhs) for lhs, op, rhs in zip(real_props[:-1], bin_op_ls, real_props[1:])))
        whole_prop = ALL(*(op(lhs, rhs) for lhs, op, rhs in zip(real_props[:-1], bin_op_ls, real_props[1:])))
            #cache is importance here ICachedEnvironment
        _Base4proxy.__init__(sf, whole_prop)

    @override
    def ___get_args_kwargs___(sf, /):
        args, kwargs = super().___get_args_kwargs___()
        return sf.__saved_args, kwargs



class SIMPLE_VAR_IMPLY(_Base4proxy):
    r'''
    SIMPLE_VAR_IMPLY(['a', 'b'], ['c', 'd'], [(['s', 't'], ['u', 'v']), (['w', 'x'], ['y', 'z'])])
        <==> [[!a][!b][c][d] -->> [[!s][!t][u][v]or[!w][!x][y][z]]]
    #'''
    def __init__(sf, false_var_names, true_var_names, alternatives, /):
        false_var_names = mk_tuple(false_var_names)
        true_var_names = mk_tuple(true_var_names)
        alternatives = mk_tuple((mk_tuple(false_var_names), mk_tuple(true_var_names)) for false_var_names, true_var_names in alternatives)
        sf._saved_args = (false_var_names, true_var_names, alternatives)
        def _mk_prop(fs_ts):
            (false_var_names, true_var_names) = fs_ts
            return AND(ALL_NOT_VAR(*false_var_names), ALL_VAR(*true_var_names))
        prop = IMPLY(_mk_prop((false_var_names, true_var_names)), OR(*map(_mk_prop, alternatives)))
        _Base4proxy.__init__(sf, prop)

    @override
    def ___get_args_kwargs___(sf, /):
        return sf._saved_args, {}


class ALL_STARMAP_SIMPLE_VAR_IMPLY(_Base4proxy):
    r'''
    ALL(*itertools.starmap(SIMPLE_VAR_IMPLY, [('tz', ['w'], [('b', 'x'), ('', 'yb')])]))
    SIMPLE_VAR_IMPLY(['a', 'b'], ['c', 'd'], [(['s', 't'], ['u', 'v']), (['w', 'x'], ['y', 'z'])])
        <==> [[!a][!b][c][d] -->> [[!s][!t][u][v]or[!w][!x][y][z]]]
    #'''
    def __init__(sf, false_var_names__true_var_names__alternatives___triples, /):
        def _2immutable___triples(triples, /):
            return mk_tuple(map(_2immutable___triple, triples))
        def _2immutable___triple(fs_ts_ps, /):
            fs, ts, ps = fs_ts_ps
            fs, ts = _2immutable___fs_ts((fs, ts))
            ps = mk_tuple(map(_2immutable___fs_ts, ps))
            return fs, ts, ps
        def _2immutable___fs_ts(fs_ts, /):
            fs, ts = map(mk_tuple, fs_ts)
            return fs, ts
        false_var_names__true_var_names__alternatives___triples = _2immutable___triples(false_var_names__true_var_names__alternatives___triples)
        sf.__saved_args = false_var_names__true_var_names__alternatives___triples
        prop = ALL(*itertools.starmap(SIMPLE_VAR_IMPLY, false_var_names__true_var_names__alternatives___triples))
        _Base4proxy.__init__(sf, prop)

    @override
    def ___get_args_kwargs___(sf, /):
        return ([*sf.__saved_args],), {}








r'''


flip imply
cached env expr value
    variable_name2bool/variable_name2tribool ---> cached_env
    cached_env
        ... = cached_env.set_fdefault(prop, eval)
        cached_env._query_env_variable(env_variable_name) -> tribool
total
    mod2minmaxs4T
    mod2minmaxs4F
    mod2minmaxs4Y
     mod 0
     -1 mod-1?
eq/ge/le/gt/lt/ne/mod
    num_1s={mod/uint:eq/uint/(min/uint,max/int)}
    num_0s
    num_Ys
IMPLY-deep_left-eval_from_left2right
FLIP_IMPLY-deep_right-eval_from_left2right
#'''

######################
class _doctest_examples___basic:
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool



>>> the_FALSE
FALSE()
>>> the_FALSE is FALSE()
True
>>> eval_prop_at({}, the_FALSE)
False
>>> eval_prop_at({}, the_TRUE)
True
>>> eval_prop_at({}, the_YET)
Ellipsis


>>> ERROR('{}:{}:{a}:{b}', 'v_0', 'v_1', a = 'v_a', b = 'v_b')
ERROR('{}:{}:{a}:{b}', 'v_0', 'v_1', a = 'v_a', b = 'v_b')
>>> err_prop = _
>>> eval_prop_at(dict(v_0=False, v_1=True, v_a=False, v_b=...), err_prop)
Traceback (most recent call last):
    ...
EvalError: False:True:False:Ellipsis


>>> VAR('zzz')
VAR('zzz')
>>> eval_prop_at({'zzz':False}, VAR('zzz'))
False
>>> eval_prop_at({'zzz':True}, VAR('zzz'))
True
>>> eval_prop_at({'zzz':...}, VAR('zzz'))
Ellipsis


>>> NOT_VAR('zzz')
NOT_VAR('zzz')
>>> eval_prop_at({'zzz':False}, NOT_VAR('zzz'))
True
>>> eval_prop_at({'zzz':True}, NOT_VAR('zzz'))
False
>>> eval_prop_at({'zzz':...}, NOT_VAR('zzz'))
Ellipsis


>>> NOT(VAR('zzz'))
NOT(VAR('zzz'))
>>> eval_prop_at({'zzz':False}, NOT(VAR('zzz')))
True
>>> eval_prop_at({'zzz':True}, NOT(VAR('zzz')))
False
>>> eval_prop_at({'zzz':...}, NOT(VAR('zzz')))
Ellipsis



#]]]doctest_examples-end
#'''

######################

######################
# ANY vs OR: impl by total or foldl
# .,$s/\<OR(/ANY(/g
#   ))
######################
class _doctest_examples___ANY:
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> ANY()
ANY()
>>> ANY(the_FALSE)
ANY(FALSE())
>>> ANY(the_FALSE, the_TRUE, the_YET)
ANY(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, ANY())
False
>>> eval_prop_at({}, ANY(the_FALSE))
False
>>> eval_prop_at({}, ANY(the_TRUE))
True
>>> eval_prop_at({}, ANY(the_YET))
Ellipsis
>>> eval_prop_at({}, ANY(the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, ANY(the_TRUE, the_FALSE))
True
>>> eval_prop_at({}, ANY(the_YET, the_FALSE))
Ellipsis
>>> eval_prop_at({}, ANY(the_FALSE, the_TRUE))
True
>>> eval_prop_at({}, ANY(the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, ANY(the_YET, the_TRUE))
True
>>> eval_prop_at({}, ANY(the_FALSE, the_YET))
Ellipsis
>>> eval_prop_at({}, ANY(the_TRUE, the_YET))
True
>>> eval_prop_at({}, ANY(the_YET, the_YET))
Ellipsis


>>> eval_prop_at({}, ANY(ERROR('')))
Traceback (most recent call last):
    ...
EvalError

>>> eval_prop_at({}, ANY(the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, ANY(the_TRUE, ERROR('')))
True
>>> eval_prop_at({}, ANY(the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError


>>> eval_prop_at({}, ANY(ERROR(''), the_FALSE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, ANY(ERROR(''), the_TRUE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, ANY(ERROR(''), the_YET))
Traceback (most recent call last):
    ...
EvalError


>>> eval_prop_at({}, ANY(the_FALSE, the_YET, the_FALSE, the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, ANY(the_FALSE, the_YET, the_FALSE, the_YET, the_TRUE, ERROR('')))
True


#]]]doctest_examples-end
#'''

######################
# ALL vs AND: impl by total or foldl
# .,$s/\<AND(/ALL(/g
#   ))
######################
class _doctest_examples___ALL:
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> ALL()
ALL()
>>> ALL(the_FALSE)
ALL(FALSE())
>>> ALL(the_FALSE, the_TRUE, the_YET)
ALL(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, ALL())
True
>>> eval_prop_at({}, ALL(the_FALSE))
False
>>> eval_prop_at({}, ALL(the_TRUE))
True
>>> eval_prop_at({}, ALL(the_YET))
Ellipsis
>>> eval_prop_at({}, ALL(the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, ALL(the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, ALL(the_YET, the_FALSE))
False
>>> eval_prop_at({}, ALL(the_FALSE, the_TRUE))
False
>>> eval_prop_at({}, ALL(the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, ALL(the_YET, the_TRUE))
Ellipsis
>>> eval_prop_at({}, ALL(the_FALSE, the_YET))
False
>>> eval_prop_at({}, ALL(the_TRUE, the_YET))
Ellipsis
>>> eval_prop_at({}, ALL(the_YET, the_YET))
Ellipsis


>>> eval_prop_at({}, ALL(ERROR('')))
Traceback (most recent call last):
    ...
EvalError

>>> eval_prop_at({}, ALL(the_FALSE, ERROR('')))
False
>>> eval_prop_at({}, ALL(the_TRUE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, ALL(the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError


>>> eval_prop_at({}, ALL(ERROR(''), the_FALSE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, ALL(ERROR(''), the_TRUE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, ALL(ERROR(''), the_YET))
Traceback (most recent call last):
    ...
EvalError


>>> eval_prop_at({}, ALL(the_TRUE, the_YET, the_TRUE, the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, ALL(the_TRUE, the_YET, the_TRUE, the_YET, the_FALSE, ERROR('')))
False



#]]]doctest_examples-end
#'''



######################
# .,$s/\<ALL(/FOLDU_XOR(/g
#       ))
######################
class _doctest_examples___XOR:
    # common for non-op<2>
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> eval_prop_at({}, XOR(the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, XOR(the_TRUE, the_FALSE))
True
>>> eval_prop_at({}, XOR(the_YET, the_FALSE))
Ellipsis
>>> eval_prop_at({}, XOR(the_FALSE, the_TRUE))
True
>>> eval_prop_at({}, XOR(the_TRUE, the_TRUE))
False
>>> eval_prop_at({}, XOR(the_YET, the_TRUE))
Ellipsis
>>> eval_prop_at({}, XOR(the_FALSE, the_YET))
Ellipsis
>>> eval_prop_at({}, XOR(the_TRUE, the_YET))
Ellipsis
>>> eval_prop_at({}, XOR(the_YET, the_YET))
Ellipsis



>>> eval_prop_at({}, XOR(the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, XOR(the_TRUE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, XOR(the_YET, ERROR('')))
Ellipsis

>>> eval_prop_at({}, XOR(ERROR(''), the_FALSE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, XOR(ERROR(''), the_TRUE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, XOR(ERROR(''), the_YET))
Traceback (most recent call last):
    ...
EvalError




#]]]doctest_examples-end
#'''





def _doc_replace(old, new, /):
    #__doc__ = _doctest_examples___ANY.__doc__.replace('ANY', 'OR')
    old_doc = globals()[f'_doctest_examples___{old}'].__doc__
    new_doc = old_doc.replace(old, new)
    if new_doc == old_doc: raise logic-err
    return new_doc

class _doctest_examples___FOLDU_XOR:
    __doc__ = _doc_replace('XOR', 'FOLDU_XOR') +\
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> FOLDU_XOR()
FOLDU_XOR()
>>> FOLDU_XOR(the_FALSE)
FOLDU_XOR(FALSE())
>>> FOLDU_XOR(the_FALSE, the_TRUE, the_YET)
FOLDU_XOR(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, FOLDU_XOR())
False
>>> eval_prop_at({}, FOLDU_XOR(the_FALSE))
False
>>> eval_prop_at({}, FOLDU_XOR(the_TRUE))
True
>>> eval_prop_at({}, FOLDU_XOR(the_YET))
Ellipsis

>>> eval_prop_at({}, FOLDU_XOR(ERROR('')))
Traceback (most recent call last):
    ...
EvalError




>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_YET, ERROR('')))
Ellipsis


>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_TRUE))
True
>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_FALSE))
True
>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_TRUE))
False


>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_FALSE, the_FALSE))
True
>>> eval_prop_at({}, FOLDU_XOR(the_TRUE, the_FALSE, the_FALSE, the_TRUE))
False





#]]]doctest_examples-end
#'''




######################
# .,$s/\<FOLDU_XOR(/FOLDU_XNOR(/g
#       ))
######################
class _doctest_examples___XNOR:
    # common for non-op<2>
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> eval_prop_at({}, XNOR(the_FALSE, the_FALSE))
True
>>> eval_prop_at({}, XNOR(the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, XNOR(the_YET, the_FALSE))
Ellipsis
>>> eval_prop_at({}, XNOR(the_FALSE, the_TRUE))
False
>>> eval_prop_at({}, XNOR(the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, XNOR(the_YET, the_TRUE))
Ellipsis
>>> eval_prop_at({}, XNOR(the_FALSE, the_YET))
Ellipsis
>>> eval_prop_at({}, XNOR(the_TRUE, the_YET))
Ellipsis
>>> eval_prop_at({}, XNOR(the_YET, the_YET))
Ellipsis



>>> eval_prop_at({}, XNOR(the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, XNOR(the_TRUE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, XNOR(the_YET, ERROR('')))
Ellipsis

>>> eval_prop_at({}, XNOR(ERROR(''), the_FALSE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, XNOR(ERROR(''), the_TRUE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, XNOR(ERROR(''), the_YET))
Traceback (most recent call last):
    ...
EvalError



#]]]doctest_examples-end
#'''




class _doctest_examples___FOLDU_XNOR:
    __doc__ = _doc_replace('XNOR', 'FOLDU_XNOR') +\
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> FOLDU_XNOR()
FOLDU_XNOR()
>>> FOLDU_XNOR(the_FALSE)
FOLDU_XNOR(FALSE())
>>> FOLDU_XNOR(the_FALSE, the_TRUE, the_YET)
FOLDU_XNOR(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, FOLDU_XNOR())
True
>>> eval_prop_at({}, FOLDU_XNOR(the_FALSE))
False
>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE))
True
>>> eval_prop_at({}, FOLDU_XNOR(the_YET))
Ellipsis

>>> eval_prop_at({}, FOLDU_XNOR(ERROR('')))
Traceback (most recent call last):
    ...
EvalError




>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_YET, ERROR('')))
Ellipsis


>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_TRUE))
True
>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_FALSE))
True
>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_TRUE))
False


>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_TRUE, the_FALSE))
True
>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_TRUE, the_TRUE))
False
>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, FOLDU_XNOR(the_TRUE, the_FALSE, the_FALSE, the_TRUE))
True




#]]]doctest_examples-end
#'''



######################
class _doctest_examples___OR:
    __doc__ = _doc_replace('ANY', 'OR')
class _doctest_examples___AND:
    __doc__ = _doc_replace('ALL', 'AND')

class _doctest_examples___ODD_TOTAL_TRUE:
    __doc__ = _doc_replace('FOLDU_XOR', 'ODD_TOTAL_TRUE')
class _doctest_examples___EVEN_TOTAL_FALSE:
    __doc__ = _doc_replace('FOLDU_XNOR', 'EVEN_TOTAL_FALSE')



######################
r'''
    EXACTLY_SINGLE_TRUE
    EXACTLY_SINGLE_FALSE
    PAIRWISE_EQU

    diff:
        ODD_TOTAL_TRUE
        EVEN_TOTAL_FALSE
        FOLDU_XOR
        FOLDU_XNOR
        EXACTLY_SINGLE_TRUE
        EXACTLY_SINGLE_FALSE
        PAIRWISE_EQU
#'''
######################
class _doctest_examples___EXACTLY_SINGLE_TRUE:
    #__doc__ = _doc_replace('FOLDU_XOR', 'EXACTLY_SINGLE_TRUE')
    __doc__ = _doc_replace('XOR', 'EXACTLY_SINGLE_TRUE') +\
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> EXACTLY_SINGLE_TRUE()
EXACTLY_SINGLE_TRUE()
>>> EXACTLY_SINGLE_TRUE(the_FALSE)
EXACTLY_SINGLE_TRUE(FALSE())
>>> EXACTLY_SINGLE_TRUE(the_FALSE, the_TRUE, the_YET)
EXACTLY_SINGLE_TRUE(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE())
False
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_FALSE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE))
True
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_YET))
Ellipsis

>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(ERROR('')))
Traceback (most recent call last):
    ...
EvalError




>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_TRUE, ERROR('')))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_YET, the_YET, ERROR('')))
False


>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_YET, ERROR('')))
Ellipsis
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_YET, the_FALSE, the_FALSE, ERROR('')))
Ellipsis


>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_FALSE, the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_FALSE, the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_FALSE, the_YET))
Ellipsis
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_FALSE, the_FALSE, the_FALSE, the_YET))
Ellipsis


>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_TRUE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_TRUE))
False


>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_TRUE, the_TRUE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_FALSE, the_FALSE))
True
>>> eval_prop_at({}, EXACTLY_SINGLE_TRUE(the_TRUE, the_FALSE, the_FALSE, the_TRUE))
False





#]]]doctest_examples-end
#'''




class _doctest_examples___EXACTLY_SINGLE_FALSE:
    #__doc__ = _doc_replace('FOLDU_XOR', 'EXACTLY_SINGLE_FALSE')
    __doc__ = _doc_replace('XOR', 'EXACTLY_SINGLE_FALSE') +\
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> EXACTLY_SINGLE_FALSE()
EXACTLY_SINGLE_FALSE()
>>> EXACTLY_SINGLE_FALSE(the_FALSE)
EXACTLY_SINGLE_FALSE(FALSE())
>>> EXACTLY_SINGLE_FALSE(the_FALSE, the_TRUE, the_YET)
EXACTLY_SINGLE_FALSE(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE())
False
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_FALSE))
True
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_YET))
Ellipsis

>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(ERROR('')))
Traceback (most recent call last):
    ...
EvalError




>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_FALSE, the_FALSE, ERROR('')))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_FALSE, ERROR('')))
False


>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_YET, ERROR('')))
Ellipsis
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_YET, the_TRUE, the_TRUE, ERROR('')))
Ellipsis




>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_YET, the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_YET))
Ellipsis
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_TRUE, the_TRUE, the_TRUE, the_YET))
Ellipsis


>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_TRUE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_TRUE))
True


>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, EXACTLY_SINGLE_FALSE(the_TRUE, the_FALSE, the_FALSE, the_TRUE))
False





#]]]doctest_examples-end
#'''




class _doctest_examples___PAIRWISE_EQU:
    #__doc__ = _doc_replace('FOLDU_XNOR', 'PAIRWISE_EQU')
    __doc__ = _doc_replace('XNOR', 'PAIRWISE_EQU') +\
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> PAIRWISE_EQU()
PAIRWISE_EQU()
>>> PAIRWISE_EQU(the_FALSE)
PAIRWISE_EQU(FALSE())
>>> PAIRWISE_EQU(the_FALSE, the_TRUE, the_YET)
PAIRWISE_EQU(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, PAIRWISE_EQU())
True
>>> eval_prop_at({}, PAIRWISE_EQU(the_FALSE))
True
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE))
True
>>> eval_prop_at({}, PAIRWISE_EQU(the_YET))
True

>>> eval_prop_at({}, PAIRWISE_EQU(ERROR('')))
True




>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, ERROR('')))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_FALSE, the_TRUE, ERROR('')))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_YET, the_TRUE, the_FALSE, ERROR('')))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_FALSE, the_YET, the_TRUE, ERROR('')))
False



>>> eval_prop_at({}, PAIRWISE_EQU(the_YET, ERROR('')))
Ellipsis
>>> eval_prop_at({}, PAIRWISE_EQU(the_YET, the_YET, the_YET, ERROR('')))
Ellipsis





>>> eval_prop_at({}, PAIRWISE_EQU(the_FALSE, the_FALSE, the_FALSE, the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_TRUE, the_TRUE, the_TRUE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_YET, the_TRUE, the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, PAIRWISE_EQU(the_FALSE, the_YET, the_FALSE, the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError

>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_TRUE, the_TRUE, the_TRUE, the_YET))
Ellipsis


>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_TRUE))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_TRUE))
False


>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, the_TRUE, the_TRUE))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, PAIRWISE_EQU(the_TRUE, the_FALSE, the_FALSE, the_TRUE))
False





#]]]doctest_examples-end
#'''




######################
r'''
    FOLDL_IMPLY
    FOLDR_FLIP_IMPLY

#'''
######################

######################
class _doctest_examples___IMPLY:
    # common for non-op<2>
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> eval_prop_at({}, IMPLY(the_FALSE, the_FALSE))
True
>>> eval_prop_at({}, IMPLY(the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, IMPLY(the_YET, the_FALSE))
Ellipsis
>>> eval_prop_at({}, IMPLY(the_FALSE, the_TRUE))
True
>>> eval_prop_at({}, IMPLY(the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, IMPLY(the_YET, the_TRUE))
True
>>> eval_prop_at({}, IMPLY(the_FALSE, the_YET))
True
>>> eval_prop_at({}, IMPLY(the_TRUE, the_YET))
Ellipsis
>>> eval_prop_at({}, IMPLY(the_YET, the_YET))
Ellipsis



>>> eval_prop_at({}, IMPLY(the_FALSE, ERROR('')))
True
>>> eval_prop_at({}, IMPLY(the_TRUE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, IMPLY(the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError

>>> eval_prop_at({}, IMPLY(ERROR(''), the_FALSE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, IMPLY(ERROR(''), the_TRUE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, IMPLY(ERROR(''), the_YET))
Traceback (most recent call last):
    ...
EvalError



#]]]doctest_examples-end
#'''




######################
class _doctest_examples___FLIP_IMPLY:
    # common for non-op<2>
    r'''
#[[[doctest_examples-begin

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> eval_prop_at({}, FLIP_IMPLY(the_FALSE, the_FALSE))
True
>>> eval_prop_at({}, FLIP_IMPLY(the_TRUE, the_FALSE))
True
>>> eval_prop_at({}, FLIP_IMPLY(the_YET, the_FALSE))
True
>>> eval_prop_at({}, FLIP_IMPLY(the_FALSE, the_TRUE))
False
>>> eval_prop_at({}, FLIP_IMPLY(the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, FLIP_IMPLY(the_YET, the_TRUE))
Ellipsis
>>> eval_prop_at({}, FLIP_IMPLY(the_FALSE, the_YET))
Ellipsis
>>> eval_prop_at({}, FLIP_IMPLY(the_TRUE, the_YET))
True
>>> eval_prop_at({}, FLIP_IMPLY(the_YET, the_YET))
Ellipsis



>>> eval_prop_at({}, FLIP_IMPLY(the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, FLIP_IMPLY(the_TRUE, ERROR('')))
True
>>> eval_prop_at({}, FLIP_IMPLY(the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError

>>> eval_prop_at({}, FLIP_IMPLY(ERROR(''), the_FALSE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, FLIP_IMPLY(ERROR(''), the_TRUE))
Traceback (most recent call last):
    ...
EvalError
>>> eval_prop_at({}, FLIP_IMPLY(ERROR(''), the_YET))
Traceback (most recent call last):
    ...
EvalError



#]]]doctest_examples-end
#'''


######################
######################
def _doc_replace__op2(old, new, /):
    old_doc = globals()[f'_doctest_examples___{old}__op2'].__doc__
    new_doc = old_doc.replace(old, new)
    if new_doc == old_doc: raise logic-err
    return new_doc
class _doctest_examples___XOR__op2:
    #only spec for op<2>
    r'''
#[[[doctest_examples-begin
>>> XOR()
Traceback (most recent call last):
    ...
TypeError: __init__() missing 2 required positional arguments: 'lhs_prop' and 'rhs_prop'
>>> XOR(the_YET)
Traceback (most recent call last):
    ...
TypeError: __init__() missing 1 required positional argument: 'rhs_prop'
>>> XOR(the_YET, the_YET, the_YET)
Traceback (most recent call last):
    ...
TypeError: __init__() takes 3 positional arguments but 4 were given

#]]]doctest_examples-end
#'''
class _doctest_examples___XNOR__op2:
    __doc__ = _doc_replace__op2('XOR', 'XNOR')
class _doctest_examples___IMPLY__op2:
    __doc__ = _doc_replace__op2('XOR', 'IMPLY')
class _doctest_examples___FLIP_IMPLY__op2:
    __doc__ = _doc_replace__op2('XOR', 'FLIP_IMPLY')

######################
######################
class _doctest_examples___FOLDL_IMPLY:
    __doc__ = _doc_replace('IMPLY', 'FOLDL_IMPLY') +\
    r'''
#[[[doctest_examples-begin
FOLDL_IMPLY

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> FOLDL_IMPLY()
FOLDL_IMPLY()
>>> FOLDL_IMPLY(the_FALSE)
FOLDL_IMPLY(FALSE())
>>> FOLDL_IMPLY(the_FALSE, the_TRUE, the_YET)
FOLDL_IMPLY(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, FOLDL_IMPLY())
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_FALSE))
False
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_YET))
Ellipsis

>>> eval_prop_at({}, FOLDL_IMPLY(ERROR('')))
Traceback (most recent call last):
    ...
EvalError




>>> eval_prop_at({}, FOLDL_IMPLY(the_FALSE, ERROR('')))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_FALSE, ERROR(''), the_TRUE))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_FALSE, ERROR(''), the_FALSE))
False
>>> eval_prop_at({}, FOLDL_IMPLY(the_FALSE, ERROR(''), the_YET))
Ellipsis
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, ERROR('')))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_YET, the_TRUE, the_FALSE, ERROR('')))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_YET, the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError



>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE, ERROR('')))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_YET, ERROR('')))
Traceback (most recent call last):
    ...
EvalError


>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_FALSE))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_TRUE))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_TRUE))
True


>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE))
False
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_FALSE, the_FALSE))
False
>>> eval_prop_at({}, FOLDL_IMPLY(the_TRUE, the_FALSE, the_FALSE, the_TRUE))
True





#]]]doctest_examples-end
#'''






######################
class _doctest_examples___FOLDR_FLIP_IMPLY:
    __doc__ = _doc_replace('FLIP_IMPLY', 'FOLDR_FLIP_IMPLY') +\
    r'''
#[[[doctest_examples-begin
FOLDR_FLIP_IMPLY

>>> eval_prop_at = eval_proposition_at_configuration__tribool


>>> FOLDR_FLIP_IMPLY()
FOLDR_FLIP_IMPLY()
>>> FOLDR_FLIP_IMPLY(the_FALSE)
FOLDR_FLIP_IMPLY(FALSE())
>>> FOLDR_FLIP_IMPLY(the_FALSE, the_TRUE, the_YET)
FOLDR_FLIP_IMPLY(FALSE(), TRUE(), YET())


>>> eval_prop_at({}, FOLDR_FLIP_IMPLY())
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_FALSE))
False
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_YET))
Ellipsis

>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(ERROR('')))
Traceback (most recent call last):
    ...
EvalError




>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, ERROR('')))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, ERROR(''), ERROR('')))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_FALSE, the_TRUE, ERROR('')))
False
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_YET, the_TRUE, ERROR('')))
Ellipsis
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_YET, the_TRUE, the_FALSE, ERROR('')))
Ellipsis
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_YET, the_FALSE, ERROR('')))
Traceback (most recent call last):
    ...
EvalError



>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE, ERROR('')))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_YET, ERROR('')))
True


>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_FALSE))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE, the_TRUE))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_FALSE))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_TRUE, the_TRUE))
True


>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_FALSE))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_TRUE, the_TRUE))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_FALSE, the_FALSE))
True
>>> eval_prop_at({}, FOLDR_FLIP_IMPLY(the_TRUE, the_FALSE, the_FALSE, the_TRUE))
True





#]]]doctest_examples-end
#'''






######################
r'''
    CHAIN_NEIGHBOR
    SIMPLE_VAR_IMPLY
    ALL_STARMAP_SIMPLE_VAR_IMPLY
#'''
######################

######################
class _doctest_examples___CHAIN_NEIGHBOR:
    r'''
#[[[doctest_examples-begin
CHAIN_NEIGHBOR

>>> eval_prop_at = eval_proposition_at_configuration__tribool

>>> CHAIN_NEIGHBOR()
Traceback (most recent call last):
    ...
TypeError: __init__() missing 3 required positional arguments: 'prop0', 'bin_op', and 'prop1'
>>> CHAIN_NEIGHBOR(the_YET)
Traceback (most recent call last):
    ...
TypeError: __init__() missing 2 required positional arguments: 'bin_op' and 'prop1'
>>> CHAIN_NEIGHBOR(the_YET, the_YET)
Traceback (most recent call last):
    ...
TypeError: __init__() missing 1 required positional argument: 'prop1'


>>> CHAIN_NEIGHBOR(the_YET, the_YET, the_YET)
Traceback (most recent call last):
    ...
seed.helper.check.check.CheckFail

    #fail since arg1@op is not Callable




>>> CHAIN_NEIGHBOR(the_YET, AND, the_YET) #doctest: +ELLIPSIS
CHAIN_NEIGHBOR(YET(), <class '....AND'>, YET())

>>> CHAIN_NEIGHBOR(the_YET, AND, the_YET, the_YET)
Traceback (most recent call last):
    ...
TypeError


>>> eval_prop_at({}, CHAIN_NEIGHBOR(the_YET, AND, the_YET))
Ellipsis
>>> eval_prop_at({}, CHAIN_NEIGHBOR(the_YET, AND, the_YET, OR, the_TRUE))
Ellipsis
>>> eval_prop_at({}, CHAIN_NEIGHBOR(the_YET, AND, the_TRUE, OR, the_TRUE))
Ellipsis
>>> eval_prop_at({}, CHAIN_NEIGHBOR(the_FALSE, AND, the_TRUE, OR, the_TRUE))
False
>>> eval_prop_at({}, CHAIN_NEIGHBOR(the_TRUE, AND, the_TRUE, OR, the_TRUE))
True



>>> eval_prop_at({}, CHAIN_NEIGHBOR(the_TRUE, IMPLY, the_TRUE, IMPLY, the_TRUE))
True
>>> eval_prop_at({}, CHAIN_NEIGHBOR(the_TRUE, IMPLY, the_FALSE, IMPLY, the_TRUE))
False
>>> eval_prop_at({}, CHAIN_NEIGHBOR(the_FALSE, IMPLY, the_FALSE, IMPLY, the_TRUE))
True



#]]]doctest_examples-end
#'''



######################
class _doctest_examples___SIMPLE_VAR_IMPLY:
    r'''
#[[[doctest_examples-begin
SIMPLE_VAR_IMPLY

>>> eval_prop_at = eval_proposition_at_configuration__tribool

>>> SIMPLE_VAR_IMPLY()
Traceback (most recent call last):
    ...
TypeError: __init__() missing 3 required positional arguments: 'false_var_names', 'true_var_names', and 'alternatives'
>>> SIMPLE_VAR_IMPLY(the_YET)
Traceback (most recent call last):
    ...
TypeError: __init__() missing 2 required positional arguments: 'true_var_names' and 'alternatives'
>>> SIMPLE_VAR_IMPLY(the_YET, the_YET)
Traceback (most recent call last):
    ...
TypeError: __init__() missing 1 required positional argument: 'alternatives'
>>> SIMPLE_VAR_IMPLY(the_YET, the_YET, the_YET, the_YET)
Traceback (most recent call last):
    ...
TypeError: __init__() takes 4 positional arguments but 5 were given


>>> SIMPLE_VAR_IMPLY(the_YET, the_YET, the_YET)
Traceback (most recent call last):
    ...
TypeError: 'YET' object is not iterable


>>> SIMPLE_VAR_IMPLY([], [], [])
SIMPLE_VAR_IMPLY((), (), ())


>>> SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')])
SIMPLE_VAR_IMPLY(('a', 'b'), ('c', 'd'), ((('s', 't'), ('u', 'v')), (('w', 'x'), ('y', 'z'))))

>>> eval_prop_at({}, SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')]))
Traceback (most recent call last):
    ...
KeyError: 'a'


>>> eval_prop_at(dict(a=True), SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')]))
True
>>> eval_prop_at(dict(a=False, b=True), SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')]))
True
>>> eval_prop_at(dict(a=False, b=False, c=False), SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')]))
True
>>> eval_prop_at(dict(a=False, b=False, c=True, d=False), SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')]))
True
>>> eval_prop_at(dict(a=False, b=False, c=True, d=True, s=False, t=False, u=True, v=True), SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')]))
True
>>> eval_prop_at(dict(a=False, b=False, c=True, d=True, s=True, w=False, x=False, y=True, z=True), SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')]))
True
>>> eval_prop_at(dict(a=False, b=False, c=True, d=True, s=True, w=True), SIMPLE_VAR_IMPLY('ab', 'cd', [('st', 'uv'), ('wx', 'yz')]))
False



#]]]doctest_examples-end
#'''






######################
class _doctest_examples___ALL_STARMAP_SIMPLE_VAR_IMPLY:
    r'''
#[[[doctest_examples-begin
ALL_STARMAP_SIMPLE_VAR_IMPLY
ALL(*itertools.starmap(SIMPLE_VAR_IMPLY, [('tz', ['w'], [('b', 'x'), ('', 'yb')])]))

>>> eval_prop_at = eval_proposition_at_configuration__tribool

>>> triples = false_var_names__true_var_names__alternatives___triples = [('tz', ['w'], [('b', 'x'), ('', 'yb')]), ('ab', 'cd', [('st', 'uv'), ('wx', 'yz')])]

>>> ALL_STARMAP_SIMPLE_VAR_IMPLY([])
ALL_STARMAP_SIMPLE_VAR_IMPLY([])
>>> ALL_STARMAP_SIMPLE_VAR_IMPLY(the_YET)
Traceback (most recent call last):
    ...
TypeError: 'YET' object is not iterable
>>> ALL_STARMAP_SIMPLE_VAR_IMPLY(triples)
ALL_STARMAP_SIMPLE_VAR_IMPLY([(('t', 'z'), ('w',), ((('b',), ('x',)), ((), ('y', 'b')))), (('a', 'b'), ('c', 'd'), ((('s', 't'), ('u', 'v')), (('w', 'x'), ('y', 'z'))))])
>>> eval_prop_at(dict(a=False, b=False, c=True, d=True, s=True, w=True), ALL_STARMAP_SIMPLE_VAR_IMPLY(triples))
Traceback (most recent call last):
    ...
KeyError: 't'

>>> eval_prop_at(dict(t=True, a=False, b=False, c=True, d=True, s=True, w=True), ALL_STARMAP_SIMPLE_VAR_IMPLY(triples))
False



#]]]doctest_examples-end
#'''





######################
r'''
TODO:
    FOLDL_NOT_FLIP_IMPLY
    FOLDR_NOT_IMPLY
#'''
######################



######################
class _doctest_examples___op2:
    # has: ~; .-. ^ & | >> <<
    r'''
#[[[doctest_examples-begin

>>> ~the_YET
NOT(YET())
>>> the_YET - the_TRUE
NOT_IMPLY(YET(), TRUE())
>>> the_YET ^ the_TRUE
XOR(YET(), TRUE())
>>> the_YET & the_TRUE
AND(YET(), TRUE())
>>> the_YET | the_TRUE
OR(YET(), TRUE())
>>> the_YET << the_TRUE
FLIP_IMPLY(YET(), TRUE())
>>> the_YET >> the_TRUE
IMPLY(YET(), TRUE())

#]]]doctest_examples-end
#'''

######################
class _doctest_examples___z:
    r'''
#[[[doctest_examples-begin
#]]]doctest_examples-end
#'''



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

# TODO: shortcut for Ellipsis


