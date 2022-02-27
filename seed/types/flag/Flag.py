
def _deprecated_by():
    '!!!!!but doc is required by IHybridFlag; so, donot delete this module!!!!!'
    import warnings, sys
    DeprecationWarning
    warning_msg = "deprecated, use seed.types.flag.IHybridFlag instead of seed.types.flag.Flag"
    warnings.warn(warning_msg, DeprecationWarning)
    print(warning_msg, file=sys.stderr)
_deprecated_by()

#################################
#[[[__doc__-begin
__doc__ = r'''
e ../../python3_src/seed/types/flag/Flag.py
e ../../python3_src/seed/helper/case.py
  -->> e ../../python3_src/seed/types/flag/Flag.py
!mv -n ../../python3_src/seed/helper/case.py ../../python3_src/seed/types/flag/case-old.py

seed.types.flag.Flag
py -m seed.types.flag.Flag
py -m nn_ns.app.debug_cmd   seed.types.flag.Flag
from seed.types.flag.Flag import get_view_of_active_key_set_of_hybrid_flag, get_ops4hybrid_flag_of_hybrid_flag, IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, IFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___mutex_groups_are_all_discrete, ICase__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___single_mutex_group_only

from seed.types.flag.Flag import KeyError_AttributeError, IOps4Key, IOps4Partition, get_view_of_active_key_set_of_hybrid_flag, get_ops4hybrid_flag_of_hybrid_flag, IHybridFlag, IOps4HybridFlag, Ops4Key__key_is_str, Partition__key_is_str__legal_keys_finite, Ops4Partition__key_is_str__legal_keys_finite, Ops4HybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, IFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___mutex_groups_are_all_discrete, ICase__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___single_mutex_group_only


of_flag --> of_hybrid_flag

e ../../python3_src/seed/helper/case.py
  -->> e ../../python3_src/seed/types/flag/Flag.py
  介绍 设计思路
  cased_tuple
  if case=='xxx' => if case.xxx
  avoid literal error => legal_keys
  multi-flag => active_keys
  discrete vs single => hybrid => partition
  init case => mk_case.xxx
  init flag => mutable
  ...
  标志位 默认皆假
  任何时候只有有限的开启标志位

  flag:
    __getattribute__
    ___get_ops4hybrid_flag___
  ops4hybrid_flag:
    #不能是 type(flag)
    get_of_hybrid_flag___xxx(ops, flag)
    get_tmay_of_hybrid_flag_at_ops___xxx(ops)


标志位 依赖？检查约束？
    ==>> implies 蕴含
    ###precondition => 反向蕴含 #似乎也不对！ 1）是否有多种可能的前置条件（并联）2）也可解释为 蕴含（不反向）
    ======
    [x] -->> [y]
        [not x]or[y]
        依赖
    [x] -->> [not y]
        [not x]or[not y]
        不并立，不相容，互斥
            #对立事件 是 互斥+概率和为一
            #互斥 允许 皆假
    ======
    [xxx] ==>> [yyy]
        xxx 开启 必须在 yyy 开启后
        xxx 依赖于 yyy
    [xxx] ==>> [not yyy]
        互斥
    因为 标志位 默认皆假，任何时候只有有限的开启标志位
        故此 不存在: [not xxx] ==>> [...] 的 形式
        (合法标志位配置 | 合法标志位配置) 结果仍是 合法标志位配置
            x|UnInit -> x
            True|False -> raise
            x|x -> x
        ==>> 针对特定标志位，存在 多个 极小合法标志位配置
            所有 其他 合法标志位配置，必是 极小合法标志位配置 的结合
        但 极小合法标志位配置 可能有许多，不易列出，甚至无穷。所以 可用规则:
            [置真的非空标志位集][置假的允空标志位集] ==>> 并联or-any{ [所要求的其他标志位真假配置] }
                rhs 所有极小依赖
    ====
    三态:
        True-开启
        False-关闭
        #not use:None/NotImplemented
        UnInit-未初始化
        class Flag:
            xxx_1 = {xxx:True, yyy:True, zzz=False}
                xxx_1 表示 一个 开启 xxx 的 极小条件/极小合法标志位配置，里面 必须含有 xxx:True
    UnInit
        __bool__ = None
            三态逻辑 防止误用
            if tribool
            if tribool is True
        __eq__ = is
        __hash__ = None?? SpecialKey-API？？



=====
设计思路/由来
    =====ooooooo
    ===case
    函数返回，区分不同情形==>>并联数据
        cased_tuple = (case, ...payload)
        return ("xxx", ...)
    但是直接使用 字符串字面常量，即不方便输入，且容易出错。符号化:
        class Case:
            xxx = ...
        return (Case.xxx, ...)
        if case==Case.xxx:...
    可见 if-测试 语句 相对繁琐，可进一步简化为:
        mk_case = MkCase(legal_keys=["xxx", ...])
        return (mk_case.xxx, ...)
        MkCase = MkCaseMeta(case_name=..., legal_keys=["xxx", ...])
        class MkCase(legal_keys=..., metaclass=MkCaseMeta)
        return (MkCase.xxx, ...)
        if case.xxx:...
    =====ooooooo
    ===flag
    case 只是设置 多个互斥标志位，但 多个相容标志位 flag 也很常见。
        比如：不同的可选功能实现与否 的 关系 是 相容的
        class Flag(legal_keys=..., metaclass=FlagMeta):
        flag = Flag(active_keys=["xxx", "yyy", ...])
        flag = get_flag.xxx | get_flag.yyy | ...
        flag = build_flag.xxx.yyy. ... .zzz()
            __bool__ = None
    =====ooooooo
    ===hybrid_flag
    case 是 多个互斥标志位 的组合
    flag 是 多个相容标志位 的组合
    -->
    case 是 单组相容的 多个互斥标志位 的组合
        single_mutex_group_flag
    flag 是 多组相容的 单个互斥标志位 的组合
        discrete_mutex_groups_flag
    -->
    hybrid_flag 混合策略标志位配置
        比如：open(fpath, "rt")
            open_mode=(r|w|x|a)*(|+)*(t|b)
                3组相容的互斥组
    划分/相容的互斥组的分组:
        grouping = legal_key2mutex_group
        legal_keys = grouping.keys()
        mutex_groups = grouping.values()
        legal_keys = set.union(mutex_groups)
            完全覆盖
        len(legal_keys) == sum(map len mutex_groups)
            没有重叠
            => mutex_groups 是 划分
        all(legal_key in mutex_group for legal_key,mutex_group in grouping.items())
            一一对应
            => grouping 是 分组/归类
        partition = (legal_keys, mutex_groups, grouping)

        class HybridFlag(partition=..., metaclass=HybridFlagMeta)
        hybrid_flag = HybridFlag(active_keys)
        hybrid_flag = build_hybrid_flag.xxx.yyy()
            __bool__ = None

    =====ooooooo
    ===query
        * query legal_keys
            key in hybrid_flag
        * query active_keys
            repr(hybrid_flag)
            len(hybrid_flag)
                ==>> 有限 活跃标志位，构造、输出 更方便
            bool(hybrid_flag)
            iter(hybrid_flag)
            ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
            hybrid_flag[key] -> bool
            hybrid_flag.key -> bool
        * eq?hash?
    =====ooooooo
    ===create, modify
        为了方便构造，引入 build_hybrid_flag
        为了方便构建，引入 builder:build_hybrid_flag
        * immutable:
            #not hybrid_flag | hybrid_flag
            #   since rhs.partition diff
            hybrid_flag | active_keys
                raise lhs-rhs-conflict-error
            hybrid_flag & active_keys

            hybrid_flag << active_keys
                raise active_keys-not-mutex-error
                如果左右冲突，则右操作数的相应标志位覆盖左操作数的
            ops4hybrid_flag.ireplace(hybrid_flag, key2bool)
            ops4hybrid_flag.ireplace__kwargs(hybrid_flag, **key2bool)
            hybrid_flag - keys
            hybrid_flag ** (keys_to_del, keys_to_set)/key2bool
            build_hybrid_flag.xxx.yyy.zzz(HybridFlag)
                to mk/build flag:
                    AttrCollector(Flag).xxx.yyy()
                    AttrCollector().xxx.yyy(Flag)
                build_hybrid_flag.xxx.yyy.zzz(mk_HybridFlag_from_active_keys)

            mk_hybrid_flag___if_only_active_keys(ops4hybrid_flag, hybrid_flag, active_keys)
            repr_hybrid_flag___if_only_active_keys(ops4hybrid_flag, hybrid_flag)
        * mutable:
            取消！<<==不利于 检查约束
            hybrid_flag |= hybrid_flag
                raise lhs-rhs-conflict-error
            hybrid_flag <<= active_keys
                raise active_keys-not-mutex-error
            hybrid_flag -= keys
            hybrid_flag[key] = True/False
            hybrid_flag.key = True/False
            del hybrid_flag[key]
            del hybrid_flag.key
    =====ooooooo
    ===依赖，三态
        ...
        默认构造，皆假 必须是 合法配置
        ==>> 有限 活跃标志位，检查约束 更方便
        见上面
    =====ooooooo
    ===ops4hybrid_flag
        why ops4hybrid_flag is not type(flag)
        ...
    =====ooooooo
    ===ops4partition, ops4key_standardiz
        why ops4partition is not type(partition)
        why standardiz+wrap...
            取消！
            ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)的实现 可能很麻烦
        ...







#[[[doctest_examples-begin
#>>> from seed.tiny import expectError

>>> class HybridFlag4test(IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, constraints=[], partition=['xyz', '', 'w', 'ab', 't', 'ab']): pass
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
KeyError_AttributeError
>>> sf['c']
Traceback (most recent call last):
    ...
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
KeyError

>>> 0 in ot
Traceback (most recent call last):
    ...
TypeError
>>> ot[0]
Traceback (most recent call last):
    ...
TypeError

>>> ot.a
True
>>> ot.b
False
>>> ot.q
Traceback (most recent call last):
    ...
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
ValueError: active_key_set is invalid configuration
>>> sorted(ot | 'a')
['a', 'w', 'x']
>>> ot | 'b'
Traceback (most recent call last):
    ...
ValueError: active_key_set is invalid configuration
>>> ot | 'ab'
Traceback (most recent call last):
    ...
ValueError: active_key_set is invalid configuration
>>> ot << 'ab'
Traceback (most recent call last):
    ...
ValueError: not mutex
>>> ot ** ('', 'ab')
Traceback (most recent call last):
    ...
ValueError: not mutex
>>> ot ** ('a', 'a')
Traceback (most recent call last):
    ...
ValueError: to del&set same key at same time

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

# before flip ts_fs to fs_ts: >>> class HybridFlag4test_constraints(IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, constraints=[(['w'], 'tz', [('x', 'b'), ('yb', '')])], partition=['xyz', '', 'w', 'ab', 't', 'ab']): pass
>>> class HybridFlag4test_constraints(IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, constraints=[('tz', ['w'], [('b', 'x'), ('', 'yb')])], partition=['xyz', '', 'w', 'ab', 't', 'ab']): pass

>>> sf = hybrid_flag = HybridFlag4test_constraints()

>>> sf
HybridFlag4test_constraints()

>>> sf.x
False
>>> sf << 'w'
Traceback (most recent call last):
    ...
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
ValueError: active_key_set is invalid configuration
>>> sorted(sf << 'wyb')
['b', 'w', 'y']




#################################
#################################
# test ICase_.../IFlag_...

>>> class Flag4test(IFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___mutex_groups_are_all_discrete, constraints=[], keys4discrete_mutex_groups=['xyz', '', 'w', 'ab', 't', 'ab']): pass
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
KeyError: 'x'





>>> class Case4test(ICase__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___single_mutex_group_only, constraints=[], keys4the_only_mutex_group=['xyz', '', 'w', 'ab', 't', 'ab']): pass
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
ValueError: active_key_set is invalid configuration
>>> case_builder.x()
Traceback (most recent call last):
    ...
KeyError: 'x'



#]]]doctest_examples-end

#'''

#]]]__doc__-end

#################################
__all__ = '''
    KeyError_AttributeError

    IHybridFlag
        get_view_of_active_key_set_of_hybrid_flag
        get_ops4hybrid_flag_of_hybrid_flag

        IOps4Key
        IOps4Partition
        IOps4HybridFlag


    IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only
        IFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___mutex_groups_are_all_discrete
        ICase__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___single_mutex_group_only

        Ops4Key__key_is_str
        Ops4Partition__key_is_str__legal_keys_finite
            Partition__key_is_str__legal_keys_finite
                iter_chain__mutex_groups__with__extra_discrete_mutex_group_keys
        Ops4HybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only
    '''.split()
#################################


___begin_mark_of_excluded_global_names__0___ = ...
import operator as opss
import itertools
import collections
from seed.helper.repr_input import repr_helper
from seed.types.FrozenDict import FrozenDict
from seed.helper.AttrCollector import AttrCollector
from seed.abc.abc import ABC, abstractmethod, override
from seed.abc.IReprImmutableHelper import IReprImmutableHelper

from seed.tiny import mk_tuple, mk_frozenset, null_frozenset
___end_mark_of_excluded_global_names__0___ = ...

class KeyError_AttributeError(KeyError, AttributeError):pass
class IOps4Key(ABC):
    r'''
    ops4key
    #'''
    @abstractmethod
    def check__obj_is_key(ops4key, obj, /):
        'obj -> None|raise TypeError'
    def check__objs_are_keys(ops4key, objs, /):
        for x in objs:
            ops4key.check__obj_is_key(x)
                #raise TypeError

class IOps4Partition(ABC):
    r'''
    # ops4partition
    conceptual:
        group :: Set Key
        partition = mutex_groups :: Set group
            mutex pairwise

    xgroup_descriptor @partition:
        describe a group in non_discrete_mutex_groups
            or describe all discrete_mutex_groups
            # "or" ==>> "x" in "xgroup_descriptor"
        concrete impl:
            * set<key>
            * prefix if key::seq<a>
    #'''
    @abstractmethod
    def get_tmay_xgroup_descriptor4discrete_mutex_groups(ops4partition, partition, /):
        'partition -> tmay xgroup_descriptor4discrete_mutex_groups'
        return partition.tmay_xgroup_descriptor4discrete_mutex_groups

    @abstractmethod
    def legal_key2xgroup_descriptor__callable(ops4partition, partition, legal_key, /):
        'partition -> legal_key -> xgroup_descriptor|raise KeyError #may be infinite legal_keys'
        return partition.legal_key2xgroup_descriptor__mapping[legal_key]

    @abstractmethod
    def get_ops4key_of(ops4partition, partition, /):
        'partition -> ops4key'
        return partition.ops4key
    ###################################
    ###################################
    ###################################
    ###################################
    def check__obj_is_key(ops4partition, partition, obj, /):
        'partition -> obj -> None|raise TypeError'
        ops4key = ops4partition.get_ops4key_of(partition)
        ops4key.check__obj_is_key(obj)
            #raise TypeError
    def check__objs_are_keys(ops4partition, partition, objs, /):
        ops4key = ops4partition.get_ops4key_of(partition)
        ops4key.check__objs_are_keys(objs)
            #raise TypeError

    def check__obj_is_legal_key(ops4partition, partition, obj, /):
        'partition -> obj -> None|raise TypeError/KeyError'
        ops4partition.check__obj_is_key(partition, obj)
            #raise TypeError
        ops4partition.legal_key2xgroup_descriptor__callable(partition, obj)
            #raise KeyError

    def check__objs_are_legal_keys(ops4partition, partition, objs, /):
        for x in objs:
            ops4partition.check__obj_is_legal_key(partition, x)
                #raise TypeError/KeyError

    def is_key_legal(ops4partition, partition, key, /):
        'partition -> key -> bool|raise TypeError'
        try:
            ops4partition.check__obj_is_legal_key(partition, key)
                #raise TypeError/KeyError
        except KeyError:
            return False
        return True
    def are_keys_legal(ops4partition, partition, keys, /):
        return all(ops4partition.is_key_legal(partition, key) for key in keys)
            #raise TypeError
    def to_immutable___legal_key2xgroup_descriptor__mapping(ops4partition, legal_key2xgroup_descriptor__mapping, /):
        return FrozenDict(legal_key2xgroup_descriptor__mapping)
    r'''
    def to_immutable_amd_filter___legal_key_mutex_groups(ops4partition, legal_key_mutex_groups, /):
        legal_key_mutex_groups = mk_frozenset(filter(bool, map(mk_frozenset, legal_key_mutex_groups)))
        return legal_key_mutex_groups
    #'''
    def mk_partition_members___if_legal_keys_finite(ops4partition, partition, legal_key_mutex_groups, /,*, allow_illegal_keys:bool):
        legal_key_mutex_groups = mk_frozenset(filter(bool, map(mk_frozenset, legal_key_mutex_groups)))
        assert all(legal_key_mutex_groups)
        if allow_illegal_keys:
            _check = ops4partition.check__objs_are_keys
                # raise TypeError
        else:
            _check = ops4partition.check__objs_are_legal_keys
                # raise TypeError/KeyError
        _check(partition, itertools.chain.from_iterable(legal_key_mutex_groups))
            # raise TypeError/KeyError

        #legal_keys = frozenset().union(*legal_key_mutex_groups)
        legal_key2xgroup_descriptor__mapping = {}
        #keys4discrete_mutex_groups = set()
        num_discrete_mutex_groups = 0
        for i, legal_key_group in enumerate(legal_key_mutex_groups):
            if len(legal_key_group)==1:
                #discrete_mutex_group
                #[legal_key] = legal_key_group
                #keys4discrete_mutex_groups.add(legal_key)
                i = -1
                num_discrete_mutex_groups += 1
            for legal_key in legal_key_group:
                legal_key2xgroup_descriptor__mapping[legal_key] = i
        if len(legal_key2xgroup_descriptor__mapping) != sum(map(len, legal_key_mutex_groups)):raise ValueError('not mutex')
        if num_discrete_mutex_groups:
            tmay_xgroup_descriptor4discrete_mutex_groups = (-1,)
        else:
            tmay_xgroup_descriptor4discrete_mutex_groups = ()

        legal_key2xgroup_descriptor__mapping = ops4partition.to_immutable___legal_key2xgroup_descriptor__mapping(legal_key2xgroup_descriptor__mapping)
        return tmay_xgroup_descriptor4discrete_mutex_groups, legal_key2xgroup_descriptor__mapping, legal_key_mutex_groups
    #end-def mk_partition_members___if_legal_keys_finite(ops4partition, partition, legal_key_mutex_groups, /,*, allow_illegal_keys:bool):

    def check_partition_members___if_legal_keys_finite(ops4partition, partition, tmay_xgroup_descriptor4discrete_mutex_groups, legal_key2xgroup_descriptor__mapping, /):
        len(tmay_xgroup_descriptor4discrete_mutex_groups)
        len(legal_key2xgroup_descriptor__mapping)
        ops4partition.check__objs_are_legal_keys(partition, legal_key2xgroup_descriptor__mapping)
            # raise TypeError/KeyError

        xgroupname2keys = collections.defaultdict(set)
        for key, xgroupname in legal_key2xgroup_descriptor__mapping.items():
            xgroupname2keys[xgroupname].add(key)

        tmay_the_duplicates_ok_groupname = tmay_xgroup_descriptor4discrete_mutex_groups
        if tmay_the_duplicates_ok_groupname:
            [the_duplicates_ok_groupname] = tmay_the_duplicates_ok_groupname
            if the_duplicates_ok_groupname not in xgroupname2keys: raise ValueError('xgroup_descriptor4discrete_mutex_groups has no legal_keys, but tmay not Nothing')
        for xgroupname, keys in xgroupname2keys.items():
            if not keys: raise logic-err
            elif not (len(keys)>=2 or xgroupname in tmay_the_duplicates_ok_groupname): raise ValueError(f'{keys!r} is discrete_mutex_group, but not grouped into xgroup_descriptor4discrete_mutex_groups')

    def is_active_key_set_mutex(ops4partition, partition, active_key_set, /):
        'partition -> active_key_set -> bool'
        tmay_the_duplicates_ok_groupname = tmay_xgroup_descriptor4discrete_mutex_groups = ops4partition.get_tmay_xgroup_descriptor4discrete_mutex_groups(partition)

        groupname_count_pairs = collections.Counter(ops4partition.legal_key2xgroup_descriptor__callable(partition, key) for key in active_key_set).items()#.most_common(2)
        return all(count <= 1 or groupname in tmay_the_duplicates_ok_groupname for groupname, count in groupname_count_pairs)






def get_view_of_active_key_set_of_hybrid_flag(hybrid_flag, /):
    ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(hybrid_flag)
    view_of_active_key_set = ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
    return view_of_active_key_set
def get_ops4hybrid_flag_of_hybrid_flag(hybrid_flag, /):
    cls = type(hybrid_flag)
    ops4hybrid_flag = cls.___get_ops4hybrid_flag___()
    return ops4hybrid_flag
class IHybridFlag(IReprImmutableHelper):
    @classmethod
    @abstractmethod
    def ___get_ops4hybrid_flag___(cls, /):
        '-> ops4hybrid_flag'
    def __getattribute__(sf, attr, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.is_legal_key_active(sf, attr, KeyError_AttributeError)
        return sf[attr]
    def __getitem__(sf, key, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.is_legal_key_active(sf, key, KeyError)
    def __contains__(sf, key, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.is_key_legal(sf, key)
    def __bool__(sf, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.bool4active_keys_of(sf)
    def __len__(sf, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.len4active_keys_of(sf)
    def __iter__(sf, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.iter4active_keys_of(sf)
    r'''
    @abstractmethod
    def __repr__(sf, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.repr_hybrid_flag___if_only_active_keys(sf)
    #'''

    # | & << - **
    def __or__(sf, keys, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.immutable_set_opOR_configuration_of_hybrid_flag(sf, keys)
    def __and__(sf, keys, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.immutable_set_opAND_configuration_of_hybrid_flag(sf, keys)
    def __pow__(sf, keys_to_del_set_pair__or__key2bool, /):
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        return ops4hybrid_flag.immutable_overwrite_configuration_of(sf, keys_to_del_set_pair__or__key2bool, allow_illegal_keys=False)
    def __sub__(sf, keys_to_del, /):
        return sf ** (keys_to_del, [])
    def __lshift__(sf, keys_to_set, /):
        return sf ** ([], keys_to_set)



class IOps4HybridFlag(ABC):
    r'''
    # ops4hybrid_flag

    constraints :: {constraint}
    constraint :: (lhs_all__false0s, lhs_all__true1s, rhs_any__alternatives)
        皆假 必须是 合法状态/合法配置 ==>> true1s 非空
    alternatives :: {alternative}
    alternative :: (false0s, true0s)
    false0s, true0s :: {legal_key}
    #'''

    r'''
    @classmethod
    @abstractmethod
    def get_ops4hybrid_flag_of(cls, hybrid_flag, /):
        '-> ops4hybrid_flag'
        #ops is result???
        ...
    #'''
    ###################################
    ###################################
    @abstractmethod
    def get_ops4partition_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> ops4partition'
    @abstractmethod
    def get_partition_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> partition'
    @abstractmethod
    def get_constraints_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> constraints'
    @abstractmethod
    def get_view_of_active_key_set_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> view_of_active_key_set'

    def mk_hybrid_flag___if_only_active_keys(ops4hybrid_flag, hybrid_flag, active_keys, /):
        r'''
        hybrid_flag -> active_keys -> hybrid_flag
            if there is only active_key_set in args/hybrid_flag-instance-state
        #'''
        active_key_set = mk_frozenset(active_keys)
        del active_keys
        assert type(active_key_set) is frozenset
        if not ops4hybrid_flag.is_active_key_set_valid_configuration_of_hybrid_flag(hybrid_flag, active_key_set): raise ValueError('active_key_set is invalid configuration')
        valid_active_key_frozenset = active_key_set
        return ops4hybrid_flag._ooo__mk_hybrid_flag_from_valid_active_key_frozenset__ooo_(hybrid_flag, valid_active_key_frozenset)
    @abstractmethod
    def _ooo__mk_hybrid_flag_from_valid_active_key_frozenset__ooo_(ops4hybrid_flag, hybrid_flag, valid_active_key_frozenset, /):
        return type(hybrid_flag)(valid_active_key_frozenset)

    ###################################
    ###################################
    ###################################
    ###################################
    def get_ops4key_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> ops4key'
        ops4partition = ops4hybrid_flag.get_ops4partition_of(hybrid_flag)
        partition = ops4hybrid_flag.get_partition_of(hybrid_flag)
        ops4key = ops4partition.get_ops4key_of(partition)
        return ops4key
    def check__obj_is_key(ops4hybrid_flag, hybrid_flag, obj, /):
        'hybrid_flag -> obj -> None|raise TypeError'
        ops4key = ops4hybrid_flag.get_ops4key_of(hybrid_flag)
        ops4key.check__obj_is_key(obj)
            #raise TypeError
    def check__objs_are_keys(ops4hybrid_flag, hybrid_flag, objs, /):
        'hybrid_flag -> objs -> None|raise TypeError'
        ops4key = ops4hybrid_flag.get_ops4key_of(hybrid_flag)
        ops4key.check__objs_are_keys(objs)
            #raise TypeError
    def check__obj_is_legal_key(ops4hybrid_flag, hybrid_flag, obj, /):
        'hybrid_flag -> obj -> None|raise TypeError/KeyError'
        ops4partition = ops4hybrid_flag.get_ops4partition_of(hybrid_flag)
        partition = ops4hybrid_flag.get_partition_of(hybrid_flag)
        ops4partition.check__obj_is_legal_key(partition, obj)
            # raise TypeError/KeyError
    def check__objs_are_legal_keys(ops4hybrid_flag, hybrid_flag, objs, /):
        'hybrid_flag -> objs -> None|raise TypeError/KeyError'
        ops4partition = ops4hybrid_flag.get_ops4partition_of(hybrid_flag)
        partition = ops4hybrid_flag.get_partition_of(hybrid_flag)
        ops4partition.check__objs_are_legal_keys(partition, objs)
            # raise TypeError/KeyError

    def check_constraints_of(ops4hybrid_flag, hybrid_flag, /):
        constraints = ops4hybrid_flag.get_constraints_of(hybrid_flag)
        ops4partition = ops4hybrid_flag.get_ops4partition_of(hybrid_flag)
        partition = ops4hybrid_flag.get_partition_of(hybrid_flag)
        __class__.check_constraints___static(ops4partition, partition, constraints)

    @staticmethod
    def check_constraints___static(ops4partition, partition, constraints, /):
        def _check_legal_keys_pair(fs_ts):
            _check_tuple(2, fs_ts)
            fs, ts = fs_ts
            _check_legal_keys(fs)
            _check_legal_keys(ts)
        def _check_legal_keys(xs):
            _check_container(xs)
            ops4partition.check__objs_are_legal_keys(partition, xs)
                #raise TypeError/KeyError
        def _check_tuple(n, xs):
            if not (type(xs) is tuple and len(xs)==n): raise TypeError
        def _check_container(xs):
            len(xs)
            if not (iter(xs) is not xs): raise TypeError
        ######################
        _check_container(constraints)
        for constraint in constraints:
            _check_tuple(3, constraint)
            (lhs_all__false0s, lhs_all__true1s, rhs_any__alternatives) = constraint
            _check_legal_keys(lhs_all__false0s)
            _check_legal_keys(lhs_all__true1s)
            if not lhs_all__true1s: raise TypeError
            _check_container(rhs_any__alternatives)
            for fs_ts in rhs_any__alternatives:
                _check_legal_keys_pair(fs_ts)


    def is_active_key_set_valid_configuration_of_hybrid_flag(ops4hybrid_flag, hybrid_flag, active_key_set, /):
        r'''
        hybrid_flag -> active_key_set -> bool
        to impl __new__/__init__
            if there is only active_key_set in args
        #'''
        len(active_key_set)
        ops4hybrid_flag.check__objs_are_legal_keys(hybrid_flag, active_key_set)
            #raise TypeError/KeyError

        ops4partition = ops4hybrid_flag.get_ops4partition_of(hybrid_flag)
        partition = ops4hybrid_flag.get_partition_of(hybrid_flag)
        return ops4partition.is_active_key_set_mutex(partition, active_key_set) and ops4hybrid_flag.does_active_key_set_satisfy_constraints__besides_mutex(hybrid_flag, active_key_set)

    def does_active_key_set_satisfy_constraints__besides_mutex(ops4hybrid_flag, hybrid_flag, active_key_set, /):
        'hybrid_flag -> active_key_set -> bool'
        constraints = ops4hybrid_flag.get_constraints_of(hybrid_flag)
        def _satisfies(false0s_true0s):
            false0s, true0s = false0s_true0s #fs_ts
            return all(x not in active_key_set for x in false0s) and all(y in active_key_set for y in true0s)

        return all(any(map(_satisfies, rhs_any__alternatives)) for (lhs_all__false0s, lhs_all__true1s, rhs_any__alternatives) in constraints if _satisfies((lhs_all__false0s, lhs_all__true1s)))

    def is_key_legal(ops4hybrid_flag, hybrid_flag, key, /):
        r'''
        key in hybrid_flag
            #raise TypeError
        #'''
        ops4partition = ops4hybrid_flag.get_ops4partition_of(hybrid_flag)
        partition = ops4hybrid_flag.get_partition_of(hybrid_flag)
        return ops4partition.is_key_legal(partition, key)
            #raise TypeError
    def len4active_keys_of(ops4hybrid_flag, hybrid_flag, /):
        r'''
        len(hybrid_flag)
            ==>> 有限 活跃标志位，构造、输出 更方便
        #'''
        view_of_active_key_set = ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
        return len(view_of_active_key_set)
    def bool4active_keys_of(ops4hybrid_flag, hybrid_flag, /):
        r'''
        bool(hybrid_flag)
        #'''
        view_of_active_key_set = ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
        return bool(view_of_active_key_set)

    def iter4active_keys_of(ops4hybrid_flag, hybrid_flag, /):
        r'''
        iter(hybrid_flag)
        #'''
        view_of_active_key_set = ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
        return iter(view_of_active_key_set)
    def is_legal_key_active(ops4hybrid_flag, hybrid_flag, legal_key, Error, /):
        r'''hybrid_flag -> legal_key -> bool
        hybrid_flag[legal_key] -> bool
        hybrid_flag.legal_key -> bool
            raise TypeError/the-input-Error
        #'''
        if not ops4hybrid_flag.is_key_legal(hybrid_flag, legal_key):
            #raise TypeError above
            ####################
            ####################
            raise Error
            raise KeyError or KeyError_AttributeError

        view_of_active_key_set = ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
        return legal_key in (view_of_active_key_set)
    def repr_hybrid_flag___if_only_active_keys(ops4hybrid_flag, hybrid_flag, /):
        r'''
        repr(hybrid_flag)
            if there is only active_key_set in args/hybrid_flag-instance-state
        #'''
        view_of_active_key_set = ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
        if view_of_active_key_set:
            return repr_helper(hybrid_flag, set(view_of_active_key_set))
        else:
            return repr_helper(hybrid_flag)

    @staticmethod
    def to_immutable___constraints___static(constraints, /):
        def _4constraint(constraint):
            (lhs_all__false0s, lhs_all__true1s, rhs_any__alternatives) = constraint
            (lhs_all__false0s, lhs_all__true1s) = _4fs_ts((lhs_all__false0s, lhs_all__true1s))
            rhs_any__alternatives = mk_frozenset(map(_4fs_ts, rhs_any__alternatives))
            constraint = (lhs_all__false0s, lhs_all__true1s, rhs_any__alternatives)
            return constraint
        def _4fs_ts(fs_ts):
            fs, ts = map(_4legal_keys, fs_ts)
            return fs, ts
        def _4legal_keys(legal_keys):
            return mk_frozenset(legal_keys)
        return mk_frozenset(map(_4constraint, constraints))
    def immutable_overwrite_configuration_of(ops4hybrid_flag, hybrid_flag, keys_to_del_set_pair__or__key2bool, /,*, allow_illegal_keys:bool):
        r'''
        #raise TypeError/KeyError/ValueError
        hybrid_flag ** (keys_to_del, keys_to_set)
        hybrid_flag ** key2bool
            if there is only active_key_set in args/hybrid_flag-instance-state
        ==>>
            hybrid_flag << keys_to_set
            hybrid_flag - keys_to_del
            ops4hybrid_flag.ireplace(hybrid_flag, key2bool)
            ops4hybrid_flag.ireplace__kwargs(hybrid_flag, **key2bool)
        #'''
        if (type(keys_to_del_set_pair__or__key2bool) is tuple and len(keys_to_del_set_pair__or__key2bool)==2):
            #pair
            keys_to_del_set_pair = keys_to_del_set_pair__or__key2bool
        else:
            #mapping
            (keys_to_del, keys_to_set) = keys_to_del_set_pair = [], []
            key2bool = keys_to_del_set_pair__or__key2bool
            for key, to_set in key2bool.items():
                if not type(to_set) is bool: raise TypeError
                ls = keys_to_set if to_set else keys_to_del
                ls.append(key)
        (keys_to_del, keys_to_set) = map(mk_frozenset, keys_to_del_set_pair)

        if allow_illegal_keys:
            _check = ops4hybrid_flag.check__objs_are_keys
                #raise TypeError
            #ops4key = ops4hybrid_flag.get_ops4key_of(hybrid_flag)
            #ops4key.check__objs_are_keys
        else:
            _check = ops4hybrid_flag.check__objs_are_legal_keys
                #raise TypeError/KeyError
            #ops4partition = ops4hybrid_flag.get_ops4partition_of(hybrid_flag)
            #partition = ops4hybrid_flag.get_partition_of(hybrid_flag)
            #ops4partition.check__objs_are_legal_keys
        _check(hybrid_flag, keys_to_set)
        _check(hybrid_flag, keys_to_del)
                #raise TypeError/KeyError

        if keys_to_del & keys_to_set: raise ValueError('to del&set same key at same time')

        ops4partition = ops4hybrid_flag.get_ops4partition_of(hybrid_flag)
        partition = ops4hybrid_flag.get_partition_of(hybrid_flag)
        if not ops4partition.is_active_key_set_mutex(partition, keys_to_set): raise ValueError('not mutex')

        view_of_active_key_set = ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
        active_keys = set(view_of_active_key_set)
        active_keys -= keys_to_del

        def _key2xgroupname(key):
            return ops4partition.legal_key2xgroup_descriptor__callable(partition, key)
        if 0:
            #bug: ignore tmay_the_duplicates_ok_groupname
            configuration = xgroupname2key = {_key2xgroupname(key): key for key in active_keys}
            keys_to_set -= active_keys
            for key in keys_to_set:
                xgroupname2key[_key2xgroupname(key)] = key
                    #may overwrite old-key at same xgroupname
                    #   but, not cause conflict
            new_active_key_set = mk_frozenset(xgroupname2key.values())
        else:
            tmay_the_duplicates_ok_groupname = tmay_xgroup_descriptor4discrete_mutex_groups = ops4partition.get_tmay_xgroup_descriptor4discrete_mutex_groups(partition)
            configuration4discrete_mutex_groups = set()
                #set<active_key>
            configuration4non_discrete_mutex_groups = {}
                #dict<xgroup_descriptor, active_key>
                #dict<xgroupname, active_key>
            for key in itertools.chain(active_keys, keys_to_set):
                xgroupname = _key2xgroupname(key)
                if xgroupname in tmay_the_duplicates_ok_groupname:
                    configuration4discrete_mutex_groups.add(key)
                else:
                    configuration4non_discrete_mutex_groups[xgroupname] = key
                        #may overwrite old-key at same xgroupname
                        #   but, not cause conflict
            new_active_key_set = mk_frozenset(itertools.chain(configuration4discrete_mutex_groups, configuration4non_discrete_mutex_groups.values()))
        return ops4hybrid_flag.mk_hybrid_flag___if_only_active_keys(hybrid_flag, new_active_key_set)
    #end-def immutable_overwrite_configuration_of(ops4hybrid_flag, hybrid_flag, keys_to_del_set_pair__or__key2bool, /,*, allow_illegal_keys:bool):
    def immutable__apply_set_op_on_configuration_of_hybrid_flag(ops4hybrid_flag, hybrid_flag, set_op, /, *args):
        view_of_active_key_set = ops4hybrid_flag.get_view_of_active_key_set_of(hybrid_flag)
        active_keys = mk_frozenset(view_of_active_key_set)
        new_active_key_set = set_op(active_keys, *args)
        return ops4hybrid_flag.mk_hybrid_flag___if_only_active_keys(hybrid_flag, new_active_key_set)
    def immutable_set_opOR_configuration_of_hybrid_flag(ops4hybrid_flag, hybrid_flag, keys, /):
        r'''
        #raise TypeError/KeyError/ValueError
        hybrid_flag | active_keys
            if there is only active_key_set in args/hybrid_flag-instance-state
        #'''
        return ops4hybrid_flag.immutable__apply_set_op_on_configuration_of_hybrid_flag(hybrid_flag, opss.__or__, mk_frozenset(keys))
    def immutable_set_opAND_configuration_of_hybrid_flag(ops4hybrid_flag, hybrid_flag, keys, /):
        r'''
        #raise TypeError/KeyError/ValueError
        hybrid_flag & active_keys
            if there is only active_key_set in args/hybrid_flag-instance-state
        #'''
        return ops4hybrid_flag.immutable__apply_set_op_on_configuration_of_hybrid_flag(hybrid_flag, opss.__and__, mk_frozenset(keys))







def iter_chain__mutex_groups__with__extra_discrete_mutex_group_keys(legal_key_mutex_groups, extra_legal_keys4discrete_mutex_groups, /):
    'Iter (Iter key) -> Iter key -> Iter (Iter key)'
    extra_discrete_mutex_groups = ([key] for key in extra_legal_keys4discrete_mutex_groups)
    del extra_legal_keys4discrete_mutex_groups
    legal_key_mutex_groups = itertools.chain(legal_key_mutex_groups, extra_discrete_mutex_groups)
    return legal_key_mutex_groups
class Ops4Key__key_is_str(IOps4Key):
    @override
    def check__obj_is_key(ops4key, obj, /):
        'obj -> None|raise TypeError'
        if not type(obj) is str: raise TypeError

class Partition__key_is_str__legal_keys_finite:
    def __init__(sf, legal_key_mutex_groups, extra_legal_keys4discrete_mutex_groups=(), /):
        legal_key_mutex_groups = iter_chain__mutex_groups__with__extra_discrete_mutex_group_keys(legal_key_mutex_groups, extra_legal_keys4discrete_mutex_groups)
        #################################
        #ops4partition = object.__new__(IOps4Partition)
        ops4partition = Ops4HybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only.___ops4partition_at_ops4hybrid_flag___
        partition = None#sf
        (tmay_xgroup_descriptor4discrete_mutex_groups, legal_key2xgroup_descriptor__mapping, legal_key_mutex_groups) = ops4partition.mk_partition_members___if_legal_keys_finite(partition, legal_key_mutex_groups, allow_illegal_keys=True)
        #################################
        sf._tmay_xgroup_descriptor4discrete_mutex_groups_ = tmay_xgroup_descriptor4discrete_mutex_groups
        sf._legal_key2xgroup_descriptor__mapping_ = legal_key2xgroup_descriptor__mapping
        sf._legal_key_mutex_groups_ = legal_key_mutex_groups

class Ops4Partition__key_is_str__legal_keys_finite(IOps4Partition):
    r'''
    #'''
    r'''
    ___ops4key_at_ops4partition___ = Ops4Key__key_is_str()
    ___legal_key_mutex_groups_at_ops4partition___ = NotImplemented
    ___tmay_xgroup_descriptor4discrete_mutex_groups_at_ops4partition___ = NotImplemented
    ___legal_key2xgroup_descriptor__mapping_at_ops4partition___ = NotImplemented
    def __init_subclass__(cls, /,*, legal_key_mutex_groups):
        if legal_key_mutex_groups is not NotImplemented:
            ops4partition = object.__new__(__class__)
            partition = None
            (tmay_xgroup_descriptor4discrete_mutex_groups, legal_key2xgroup_descriptor__mapping, legal_key_mutex_groups) = ops4partition.mk_partition_members___if_legal_keys_finite(partition, legal_key_mutex_groups, allow_illegal_keys=True)
            cls.___tmay_xgroup_descriptor4discrete_mutex_groups_at_ops4partition___ = tmay_xgroup_descriptor4discrete_mutex_groups
            cls.___legal_key2xgroup_descriptor__mapping_at_ops4partition___ = legal_key2xgroup_descriptor__mapping
            cls.___legal_key_mutex_groups_at_ops4partition___ = legal_key_mutex_groups
    #'''

    ___ops4key_at_ops4partition___ = Ops4Key__key_is_str()

    @override
    def get_tmay_xgroup_descriptor4discrete_mutex_groups(ops4partition, partition, /):
        'partition -> tmay xgroup_descriptor4discrete_mutex_groups'
        return partition._tmay_xgroup_descriptor4discrete_mutex_groups_

    @override
    def legal_key2xgroup_descriptor__callable(ops4partition, partition, legal_key, /):
        'partition -> legal_key -> xgroup_descriptor|raise KeyError #may be infinite legal_keys'
        return partition._legal_key2xgroup_descriptor__mapping_[legal_key]

    @override
    def get_ops4key_of(ops4partition, partition, /):
        'partition -> ops4key'
        return type(ops4partition).___ops4key_at_ops4partition___
        return partition._ops4key_









class Ops4HybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only(IOps4HybridFlag):
    #___ops4key_at_ops4partition___ = Ops4Key__key_is_str()
    ___ops4partition_at_ops4hybrid_flag___ = Ops4Partition__key_is_str__legal_keys_finite()

    @override
    def get_ops4partition_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> ops4partition'
        cls = type(ops4hybrid_flag)
        return cls.___ops4partition_at_ops4hybrid_flag___
    @override
    def get_partition_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> partition'
        cls = type(hybrid_flag)
        return cls.___partition_at_hybrid_flag_cls___
    @override
    def get_constraints_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> constraints'
        cls = type(hybrid_flag)
        return cls.___constraints_at_hybrid_flag_cls___
    @override
    def get_view_of_active_key_set_of(ops4hybrid_flag, hybrid_flag, /):
        'hybrid_flag -> view_of_active_key_set'
        cls = type(hybrid_flag)
        return cls.___get_view_of_active_key_set___(hybrid_flag)
    @override
    def _ooo__mk_hybrid_flag_from_valid_active_key_frozenset__ooo_(ops4hybrid_flag, hybrid_flag, valid_active_key_frozenset, /):
        return type(hybrid_flag)(valid_active_key_frozenset)



class IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only(IHybridFlag):
    ___ops4hybrid_flag_at_hybrid_flag_cls___ = Ops4HybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only()
    ___partition_at_hybrid_flag_cls___ = NotImplemented
    ___constraints_at_hybrid_flag_cls___ = NotImplemented

    def __init_subclass__(cls, /,*, partition, constraints):
        updated = False
        #################################
        if partition is not NotImplemented and partition is not None:
            if not isinstance(partition, Partition__key_is_str__legal_keys_finite):
                legal_key_mutex_groups = partition
                partition = Partition__key_is_str__legal_keys_finite(legal_key_mutex_groups)
            if not isinstance(partition, Partition__key_is_str__legal_keys_finite):raise TypeError
            cls.___partition_at_hybrid_flag_cls___ = partition
            updated = True
        #################################
        if constraints is not NotImplemented and constraints is not None:
            constraints = IOps4HybridFlag.to_immutable___constraints___static(constraints)
            cls.___constraints_at_hybrid_flag_cls___ = constraints
            updated = True
        #################################
        if updated:
            partition = cls.___partition_at_hybrid_flag_cls___
            constraints = cls.___constraints_at_hybrid_flag_cls___
            if not (partition is NotImplemented or constraints is NotImplemented):
                ops4partition = cls.___get_ops4hybrid_flag___().___ops4partition_at_ops4hybrid_flag___
                IOps4HybridFlag.check_constraints___static(ops4partition, partition, constraints)
        #################################


    @classmethod
    def mk_hybrid_flag_builder(cls, /):
        return AttrCollector(cls)
    def __init__(sf, active_key_set=null_frozenset, /):
        cls = type(sf)
        if cls.___partition_at_hybrid_flag_cls___ is NotImplemented: raise TypeError
        if cls.___constraints_at_hybrid_flag_cls___ is NotImplemented: raise TypeError
        #################################
        active_key_set = mk_frozenset(active_key_set)
        ops4hybrid_flag = get_ops4hybrid_flag_of_hybrid_flag(sf)
        if not ops4hybrid_flag.is_active_key_set_valid_configuration_of_hybrid_flag(sf, active_key_set): raise ValueError('active_key_set is invalid configuration')
        valid_active_key_frozenset = active_key_set
        del active_key_set
        sf._active_keys = valid_active_key_frozenset
        #################################


    @override
    def ___get_view_of_active_key_set___(sf, /):
        '-> view_of_active_key_set'
        return object.__getattribute__(sf, '_active_keys')

    @classmethod
    @override
    def ___get_ops4hybrid_flag___(cls, /):
        '-> ops4hybrid_flag'
        return cls.___ops4hybrid_flag_at_hybrid_flag_cls___
    r'''
    @override
    def __repr__(sf, /):
        return IHybridFlag.__repr__(sf)
    #'''
    @override
    def ___get_args_kwargs___(sf, /):
        '-> ((active_key_set,), {})'
        view_of_active_key_set = get_view_of_active_key_set_of_hybrid_flag(sf)
        args = (view_of_active_key_set,)
        return (args, {})

    @override
    def ___get_args_kwargs4repr___(sf):
        '-> (tmay active_key_set, {})'
        if sf:
            view_of_active_key_set = get_view_of_active_key_set_of_hybrid_flag(sf)
            active_key_set = set(view_of_active_key_set)
            args = (active_key_set,)
        else:
            args = ()
        return (args, {})
class IFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___mutex_groups_are_all_discrete(IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, constraints=NotImplemented, partition=NotImplemented):
    def __init_subclass__(cls, /,*, keys4discrete_mutex_groups, constraints):
        if keys4discrete_mutex_groups is NotImplemented or keys4discrete_mutex_groups is None:
            partition = NotImplemented
        else:
            partition = Partition__key_is_str__legal_keys_finite([], keys4discrete_mutex_groups)
        super(__class__, cls).__init_subclass__(partition=partition, constraints=constraints)

class ICase__key_is_str__legal_keys_finite__instance_state_is_active_keys_only___single_mutex_group_only(IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, constraints=NotImplemented, partition=NotImplemented):
    def __init_subclass__(cls, /,*, keys4the_only_mutex_group, constraints):
        if keys4the_only_mutex_group is NotImplemented or keys4the_only_mutex_group is None:
            partition = NotImplemented
        else:
            partition = Partition__key_is_str__legal_keys_finite([keys4the_only_mutex_group])
        super(__class__, cls).__init_subclass__(partition=partition, constraints=constraints)






def _t():
    from seed.tiny import expectError
    class HybridFlag4test(IHybridFlag__key_is_str__legal_keys_finite__instance_state_is_active_keys_only, constraints=[], partition=['xyz', '', 'w', 'ab', 't', 'ab']): pass
    sf = hybrid_flag = HybridFlag4test([])
    assert not sf.x
    assert not sf.y
    assert not sf.z

    assert not sf.a
    assert not sf.b

    assert not sf.w
    assert not sf.t

    expectError(KeyError, lambda:sf.c)
_t()






if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


