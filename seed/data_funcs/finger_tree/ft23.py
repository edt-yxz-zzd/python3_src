#__all__:goto
#.DONE:设计冫树构造算法:pushs:采用直构方法:O(N) vs O(NlnN)
#TODO:(leaf|nonleaf|twig|cane|fork).auto.cached_lazy_may_hash: ftSeq 依照 元素 动态确定是否可以 散列(可行方案:tmay_hash实时计算)，另外 为了避免不必要的浪费，散列值应当按需惰性计算
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/ft23.py

seed.data_funcs.finger_tree.ft23
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.ft23 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.ft23:__doc__ -ht # -ff -df
#######

[[
源起:
e script/对称多项式讠基表达.py
    需要:排列组合:幂次讠重数@乸瓧称重式.eval(序列纟变量值)
e ../../python3_src/seed/math/combination__parts.py
    排列组合:简化实现 或 泛化实现 都需要 全序集合 或 全序序列
        #具体到 三层排列组合 需要 两个 双向链表 而且 还有痛点 有待考虑。

e ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_seq.py
e ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_ascend_set.py
    ft23_7sized_sorted_set
]]

[[
2_3_finger_tree
[finger_tree{depth} == (cane{depth}|fork{depth})]
# (branch,trunk,branch)

[fork{depth} :: (auto, etree{depth})]
[etree{depth} :: (twig{depth}, stem{depth}, twig{depth})]
[stem{depth} :: finger_tree{1+depth}]
    !!!
[twig{depth} :: (auto, nodes/[node{depth}])]
[cane{depth} :: (auto, nodes/[node{depth}])]
[node{depth} == if depth==0 then leaf else nonleaf{depth}]
[nonleaf == (auto, nodes/[node{-1+depth}])]
    !!!
[leaf == (auto, data)]

[0 <= len(cane.nodes) <= 3]
[1 <= len(twig.nodes) <= 3]
[2 <= len(nonleaf.nodes) <= 3]
    #2_3_finger_tree

basic_types:
    + data
    + auto
    + leaf
        .auto
        .data
    + nonleaf
        .auto
        .nodes
    + cane
        .auto
        .nodes
    + twigL
        .auto
        .nodes
    + twigR
        .auto
        .nodes
    + fork
        .auto
        .etree
            .twigL
            .stem
            .twigR
]]
[[
path:
[path{finger_tree} == (path{cane}|path{fork})]
[path{cane} == (0,path{cane.nodes})]
[path{fork} == (1,path{fork.etree})]
[path{xs} == (L, uint{2*[0..=L]}|(L, uint{1+2*[0..<L]}, path{x})) where [L:=len(xs)]]

[path{twigL} == path{twigL.nodes}]
[path{twigR} == path{twigR.nodes}]
[path{nonleaf} == path{nonleaf.nodes}]
[path{leaf} :: uint%3]
    0:起
    1:data
    2:讫

]]

[[
取消:@20260402
news:
    _get_emay_may_hash6auto_
    _set_may_hash6auto_
    _get_may_size6auto_
    eval_seq_hash_size_pair5hash_size_pairs_
news:
    get_may_hash6tree_
    get_may_hash6twigX_
    get_may_hash6node_
    _gget_may_hash_size_pair6tree_
    _gget_may_hash_size_pair6twigX_
    _gget_may_hash_size_pair6node_
    _gget_may_hash_size_pair6nodes_

]]
[[
@20260402
to impl lazy_auto_properties (eg: hash)
    some auto_properties be strict: eg:len, max, min, ...
    some auto_properties be lazy: eg:hash, ...

IWrapper4ft_xxx
    Wrapper4ft_tree
    Wrapper4ft_twigX
    Wrapper4ft_node_seq
    Wrapper4ft_node
IVisit4Wrapper4ft_xxx
    Visit4Wrapper4ft_xxx__7fill_part6auto
        IFiller4PartialAuto

]]



'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.data_funcs.finger_tree.ft23   @f
]]]'''#'''
__all__ = r'''
BaseFingerTreeError
    EmptyError
    BadOffsetError

IBaseOps4Auto6FingerTree
    mk_auto5chain_many_
    std_eval_seq_hash_size_pair5hash_size_pairs_
    IBasicOps4FingerTree
        IOps4FingerTree









IWrapper4ft_xxx
    Wrapper4ft_tree
    Wrapper4ft_twigX
    Wrapper4ft_node_seq
    Wrapper4ft_node
IVisit4Wrapper4ft_xxx
    Visit4Wrapper4ft_xxx__7fill_part6auto
        IFiller4PartialAuto

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_le, check_type_is, check_int_ge
    from seed.tiny_.containers import mk_tuple
    from seed.iters.chains import chains
    from itertools import islice, chain
    from seed.iters.FixedSizeTailTrapIterator import FixedSizeTailTrapIterator
        #FixedSizeTailTrapIterator(maxlen4trap, iterable)
        #   .eof
        #   .len_trap
        #   .trap2tuple_()

    from seed.iters.generator_iterator2result_ import generator_iterator2result_
    from seed.iters.flatten_recur import flatten_recur
    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):

___end_mark_of_excluded_global_names__0___ = ...

class BaseFingerTreeError(Exception):pass
class EmptyError(BaseFingerTreeError):pass
class BadOffsetError(BaseFingerTreeError):pass

#.    ___no_slots_ok___ = True
class IBaseOps4Auto6FingerTree(ABC):
    __slots__ = ()
    #########
    @abstractmethod
    def get_auto8null_(sf, /):
        '-> auto'
    @abstractmethod
    def mk_auto5chain_two_(sf, lhs_auto, rhs_auto, /):
        'auto -> auto -> auto #maybe noncommutable'
    @abstractmethod
    def mk_auto5data_(sf, data, /):
        'data -> auto'
    #########
    #:#########
    #:#@20260402
    #:@abstractmethod
    #:def _get_emay_may_hash6auto_(sf, auto, /):
    #:    'auto -> emay may hash/uint # {...=>not yet eval; None=>unhashable or unsupported ops; uint=>cached hash value}'
    #:@abstractmethod
    #:def _set_may_hash6auto_(sf, auto, may_hash, /):
    #:    '[... is _get_emay_may_hash6auto_(auto)] => auto -> may hash/uint -> None | ^Exception if [not ... is _get_emay_may_hash6auto_(auto)]'
    #:@abstractmethod
    #:def _get_may_size6auto_(sf, auto, /):
    #:    'auto -> may size{num_leafs/num_datas}/uint # None=>unsupported'
    #:@abstractmethod
    #:def eval_seq_hash_size_pair5hash_size_pairs_(sf, hash_size_pairs, /):
    #:    'Iter (hash, num_datas) -> (hash, num_datas)'
    #:#########
    #########
    #########
    #@20260403
    @property
    @abstractmethod
    def available_keys6auto(sf, /):
        '-> {key6auto}'
        return frozenset() #_lazy_null_frozenset_() #null_frozenset
    @abstractmethod
    def key_closure5key6auto_(sf, key6auto, /):
        'key6auto -> [key6auto] | ^KeyError'
        raise KeyError(key6auto)
    @abstractmethod
    def tmay_property5auto_and_key6auto_(sf, auto, key6auto, /):
        'auto -> key6auto -> tmay property6auto | ^KeyError # {() => lazy; (property6auto,)=>settled; ^KeyError=>illegal key}'
        raise KeyError(key6auto)
    @abstractmethod
    def property5wrapper4ft_xxx_and_key6auto_(sf, wrapper4ft_xxx, key6auto, /):
        'IWrapper4ft_xxx -> key6auto -> property6auto | ^KeyError'
        #resolve and settle lazy attr
        wrapper4ft_xxx.ops4ft # >= sf
        raise KeyError(key6auto)
    #########
def std_eval_seq_hash_size_pair5hash_size_pairs_(hash_size_pairs, /):
    'Iter (hash, num_datas) -> (hash, num_datas)'
    import sys
    M = sys.hash_info.modulus
    it = iter(hash_size_pairs)
    h = 0
    sz = 0
    for (h, sz) in it:
        break
    for (_h, _sz) in it:
        #.h = hash(h*5**sz + _h)
        #.h = (h*5**_sz + _h)%M
        h = (h*pow(5, _sz, M) + _h)%M
        sz += _sz
    return (h, sz)
def mk_auto5chain_many_(sf, autos, /):
    it = iter(autos)
    for acc in it:
        break
    else:
        acc = sf.get_auto8null_()
    acc
    for rhs_auto in it:
        acc = sf.mk_auto5chain_two_(acc, rhs_auto)
    auto = acc
    return auto
class IBasicOps4FingerTree(IBaseOps4Auto6FingerTree):
    __slots__ = ()
    #########
    @abstractmethod
    def _mk_node7leaf_(sf, auto, data, /):
        'auto -> data -> leaf/node{depth==0}'
    @abstractmethod
    def _mk_node7nonleaf_(sf, depth, auto, _nodes, /):
        'depth/uint{>0} -> auto -> [node{-1+depth}]{2<=len<=3} -> node{depth>0}'
    @abstractmethod
    def _mk_twigL_(sf, depth, auto, nodes, /):
        'depth/uint -> auto -> [node{depth}]{1<=len<=3} -> twigL{depth}'
    @abstractmethod
    def _mk_twigR_(sf, depth, auto, nodes, /):
        'depth/uint -> auto -> [node{depth}]{1<=len<=3} -> twigR{depth}'
    @abstractmethod
    def _mk_tree7fork_(sf, depth, auto, etree, /):
        'depth/uint -> auto -> etree/(twigL{depth}, stem{depth}/finger_tree{1+depth}, twigR{depth}) -> fork{depth}/finger_tree{depth}'
    @abstractmethod
    def _mk_tree7cane_(sf, depth, auto, nodes, /):
        'depth/uint -> auto -> [node{depth}]{0<=len<=3} -> cane{depth}/finger_tree{depth}'

    #########
    @abstractmethod
    def is_fork_tree_(sf, depth, tree, /):
        'depth/uint -> finger_tree{depth} -> bool/(cane_vs_fork)'
    #########
    @abstractmethod
    def get_auto5node_(sf, depth, node, /):
        'depth/uint -> node{depth} -> auto #(leaf|nonleaf)'
    @abstractmethod
    def get_auto5twigL_(sf, depth, twigL, /):
        'depth/uint -> twigL{depth} -> auto'
    @abstractmethod
    def get_auto5twigR_(sf, depth, twigR, /):
        'depth/uint -> twigR{depth} -> auto'
    #.def get_auto5fork_(sf, depth, fork, /):
    #.    'depth/uint -> fork{depth} -> auto'
    #.def get_auto5cane_(sf, depth, cane, /):
    #.    'depth/uint -> cane{depth} -> auto'
    #########
    @abstractmethod
    def get_auto5tree_(sf, depth, tree, /):
        'depth/uint -> finger_tree{depth} -> auto # (fork|cane)'
        #.if sf.is_fork_tree_(depth, tree):
        #.    fork = tree
        #.    auto = sf.get_auto5fork_(depth, fork)
        #.else:
        #.    cane = tree
        #.    auto = sf.get_auto5cane_(depth, cane)
        #.auto
        #.return auto

    #########
    @abstractmethod
    def get_data5leaf_(sf, leaf, /):
        'leaf -> data'
    @abstractmethod
    def get_nodes5nonleaf_(sf, depth, nonleaf, /):
        'depth/uint{>0} -> nonleaf/node{depth} -> [node{-1+depth}]'
    @abstractmethod
    def get_nodes5cane_(sf, depth, cane, /):
        'depth/uint -> cane{depth} -> [node{depth}]'
    @abstractmethod
    def get_nodes5twigL_(sf, depth, twigL, /):
        'depth/uint -> twigL{depth} -> [node{depth}]'
    @abstractmethod
    def get_nodes5twigR_(sf, depth, twigR, /):
        'depth/uint -> twigR{depth} -> [node{depth}]'
    @abstractmethod
    def get_etree5fork_(sf, depth, fork, /):
        'depth/uint -> fork{depth} -> etree{depth}'
    @abstractmethod
    def get_stem5fork_(sf, depth, fork, /):
        'depth/uint -> fork{depth} -> stem{depth}/finger_tree{1+depth}'
    @abstractmethod
    def get_twigL5fork_(sf, depth, fork, /):
        'depth/uint -> fork{depth} -> twigL{depth}'
    @abstractmethod
    def get_twigR5fork_(sf, depth, fork, /):
        'depth/uint -> fork{depth} -> twigR{depth}'
    #########










class IOps4FingerTree(IBasicOps4FingerTree):
    __slots__ = ()
    #########
    #:#########
    #:#@20260402
    #:def get_may_hash6tree_(sf, depth, tree, /):
    #:    'depth -> tree -> may hash/uint # {None=>unhashable or unsupported ops; uint=>cached hash value}'
    #:    autoT = sf.get_auto5tree_(depth, tree)
    #:    emmh = sf._get_emay_may_hash6auto_(autoT)
    #:    if not ... is emmh:
    #:        may_hash = may_hash
    #:        return may_hash
    #:    mhzT = generator_iterator2result_(sf._gget_may_hash_size_pair6tree_(depth, tree))
    #:    if None is mhzT:
    #:        mhT = None
    #:    else:
    #:        (hT, szT) = hzT = mhzT
    #:        mhT = hT
    #:    sf._set_may_hash6auto_(autoT, mhT)
    #:    return sf.get_may_hash6tree_(depth, tree)
    #:def get_may_hash6twigX_(sf, depth, twigX, /, *, atL_vs_atR:bool):
    #:    'depth -> twigX -> may hash/uint'
    #:    autoW = sf.get_auto5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)
    #:    emmh = sf._get_emay_may_hash6auto_(autoW)
    #:    if not ... is emmh:
    #:        may_hash = may_hash
    #:        return may_hash
    #:    mhzW = generator_iterator2result_(sf._gget_may_hash_size_pair6twigX_(depth, twigX, atL_vs_atR=atL_vs_atR))
    #:    if None is mhzW:
    #:        mhW = None
    #:    else:
    #:        (hW, szW) = hzW = mhzW
    #:        mhW = hW
    #:    sf._set_may_hash6auto_(autoW, mhW)
    #:    return sf.get_may_hash6twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)

    #:def get_may_hash6node_(sf, depth, node, /):
    #:    'depth -> node -> may hash/uint'
    #:    autoN = sf.get_auto5node_(depth, node)
    #:    emmh = sf._get_emay_may_hash6auto_(autoN)
    #:    if not ... is emmh:
    #:        may_hash = may_hash
    #:        return may_hash
    #:    mhzN = generator_iterator2result_(sf._gget_may_hash_size_pair6node_(depth, node))
    #:    if None is mhzN:
    #:        mhN = None
    #:    else:
    #:        (hN, szN) = hzN = mhzN
    #:        mhN = hN
    #:    sf._set_may_hash6auto_(autoN, mhN)
    #:    return sf.get_may_hash6node_(depth, node)

    #:def _gget_may_hash_size_pair6tree_(sf, depth, tree, /):
    #:    'depth -> tree -> GI{may (hash/uint, num_datas/uint)}'
    #:    autoT = sf.get_auto5tree_(depth, tree)
    #:    mszT = sf._get_may_size6auto_(autoT)
    #:    if None is mszT: return None
    #:    szT = mszT
    #:    emmh = sf._get_emay_may_hash6auto_(autoT)
    #:    if not ... is emmh:
    #:        mhT = emmh
    #:        if mhT is None:return None
    #:        hT = mhT
    #:        return (hT, szT)
    #:    if sf.is_fork_tree_(depth, tree):
    #:        fork = tree
    #:        (twigL, stem, twigR) = sf.get_etree5fork_(depth, fork)
    #:        mhzL = yield from sf._gget_may_hash_size_pair6twigX_(depth, twigL, atL_vs_atR=False)
    #:        if None is mhzL: return None
    #:        hL = mhzL
    #:        (hL, szL) = mhzL
    #:        mhzR = yield from sf._gget_may_hash_size_pair6twigX_(depth, twigR, atL_vs_atR=True)
    #:        if None is mhzR: return None
    #:        (hR, szR) = mhzR
    #:        mhzM = yield from sf._gget_may_hash_size_pair6tree_(1+depth, stem)
    #:        if None is mhzM: return None
    #:        (hM, szM) = mhzM
    #:        (hT, _szT) = sf.eval_seq_hash_size_pair5hash_size_pairs_([(hL, szL), (hM, szM), (hR, szR)])
    #:    else:
    #:        cane = tree
    #:        nodes = sf.get_nodes5cane_(depth, cane)
    #:        mhzT = yield from sf._gget_may_hash_size_pair6nodes_(depth, nodes)
    #:        if None is mhzT: return None
    #:        (hT, _szT) = mhzT
    #:    if not szT == _szT:raise 000
    #:    return (hT, szT)
    #:    #return sf.get_may_hash6tree_(depth, tree)
    #:def _gget_may_hash_size_pair6twigX_(sf, depth, twigX, /, *, atL_vs_atR:bool):
    #:    'depth -> twigX -> GI{may (hash/uint, num_datas/uint)}'
    #:    autoW = sf.get_auto5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)
    #:    mszW = sf._get_may_size6auto_(autoW)
    #:    if None is mszW: return None
    #:    szW = mszW
    #:    emmh = sf._get_emay_may_hash6auto_(autoW)
    #:    if not ... is emmh:
    #:        mhW = emmh
    #:        if mhW is None:return None
    #:        hW = mhW
    #:        return (hW, szW)
    #:    nodes = sf.get_nodes5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)
    #:    mhzW = yield from sf._gget_may_hash_size_pair6nodes_(depth, nodes)
    #:    if None is mhzW: return None
    #:    (hW, _szW) = mhzW
    #:    if not szW == _szW:raise 000
    #:    return (hW, szW)
    #:def _gget_may_hash_size_pair6node_(sf, depth, node, /):
    #:    'depth -> node -> GI{may (hash/uint, num_datas/uint)}'
    #:    autoN = sf.get_auto5node_(depth, node)
    #:    mszN = sf._get_may_size6auto_(autoN)
    #:    if None is mszN: return None
    #:    szN = mszN
    #:    emmh = sf._get_emay_may_hash6auto_(autoN)
    #:    if not ... is emmh:
    #:        mhN = emmh
    #:        if mhN is None:return None
    #:        hN = mhN
    #:        return (hN, szN)
    #:    if depth == 0:
    #:        leaf = node
    #:        _szN = 1
    #:        data = sf.get_data5leaf_(leaf)
    #:        try:
    #:            hN = hash(data)
    #:        except TypeError:
    #:            mhN = None
    #:            return None
    #:        hN
    #:    else:
    #:        nonleaf = node
    #:        _nodes = sf.get_nodes5nonleaf_(depth, nonleaf)
    #:        mhzN = yield from sf._gget_may_hash_size_pair6nodes_(-1+depth, _nodes)
    #:        if None is mhzN: return None
    #:        (hN, _szN) = mhzN
    #:    if not szN == _szN:raise 000
    #:    return (hN, szN)
    #:def _gget_may_hash_size_pair6nodes_(sf, depth, nodes, /):
    #:    'depth -> Iter node -> GI{may (hash/uint, num_datas/uint)}'
    #:    szS = 0
    #:    ps = []
    #:    for node in nodes:
    #:        mhzN = yield from sf._gget_may_hash_size_pair6node_(depth, node)
    #:        if mhzN is None:return None
    #:        hzN = mhzN
    #:        ps.append(hzN)
    #:        (hN, szN) = hzN
    #:        szS += szN
    #:    (hS, _szS) = sf.eval_seq_hash_size_pair5hash_size_pairs_(ps)
    #:    if not szS == _szS:raise 000
    #:    return (hS, szS)
    #:#########
    #########
    def mk_empty_tree_(sf, depth, /):
        'depth/uint  -> finger_tree{depth}{len==0}'
        tree = cane = sf.mk_tree7cane_(depth, nodes:=lazy_null_tuple())
        return tree
    #########
    def _mk_twigX_(sf, depth, auto, nodes, /, *, atL_vs_atR:bool):
        'depth/uint -> auto -> [node{depth}]{1<=len<=3} -> twigX{depth,atL_vs_atR}'
        f = sf._mk_twigL_ if not atL_vs_atR else sf._mk_twigR_
        return f(depth, auto, nodes)
    def get_auto5twigX_(sf, depth, twigX, /, *, atL_vs_atR:bool):
        'depth/uint -> twigX{depth,atL_vs_atR} -> auto'
        f = sf.get_auto5twigL_ if not atL_vs_atR else sf.get_auto5twigR_
        return f(depth, twigX)
    def get_nodes5twigX_(sf, depth, twigX, /, *, atL_vs_atR:bool):
        'depth/uint -> twigX{depth,atL_vs_atR} -> [node{depth}]'
        f = sf.get_nodes5twigL_ if not atL_vs_atR else sf.get_nodes5twigR_
        return f(depth, twigX)
    def get_twigX5fork_(sf, depth, fork, /, *, atL_vs_atR:bool):
        'depth/uint -> fork{depth} -> twigX{depth,atL_vs_atR}'
        f = sf.get_twigL5fork_ if not atL_vs_atR else sf.get_twigR5fork_
        return f(depth, fork)
    #########
    def mk_auto5nodes_(sf, depth, nodes, /):
        'depth/uint -> [node{depth}] -> auto'
        return mk_auto5chain_many_(sf, (sf.get_auto5node_(depth, node) for node in nodes))
    #########
    def mk_node7leaf_(sf, data, /):
        'data -> leaf/node{depth==0}'
        auto = sf.mk_auto5data_(data)
        leaf = sf._mk_node7leaf_(auto, data)
        return leaf
    def mk_node7nonleaf_(sf, depth, _nodes, /):
        'depth/uint{>0} -> [node{-1+depth}]{2<=len<=3} -> node{depth>0}'
        _nodes = mk_tuple(_nodes)
        _depth = -1+depth
        assert 2 <= len(_nodes) <= 3
        auto = sf.mk_auto5nodes_(_depth, _nodes)
        nonleaf = sf._mk_node7nonleaf_(depth, auto, _nodes)
        return nonleaf
    def mk_twigX_(sf, depth, nodes, /, *, atL_vs_atR:bool):
        'depth/uint -> [node{depth}]{1<=len<=3} -> twigX{depth,atL_vs_atR}'
        nodes = mk_tuple(nodes)
        assert 1 <= len(nodes) <= 3
        auto = sf.mk_auto5nodes_(depth, nodes)
        twigX = sf._mk_twigX_(depth, auto, nodes, atL_vs_atR=atL_vs_atR)
        return twigX
    def mk_twigL_(sf, depth, nodes, /):
        'depth/uint -> [node{depth}]{1<=len<=3} -> twigL{depth}'
        return sf.mk_twigX_(depth, nodes, atL_vs_atR=False)
    def mk_twigR_(sf, depth, nodes, /):
        'depth/uint -> [node{depth}]{1<=len<=3} -> twigR{depth}'
        return sf.mk_twigX_(depth, nodes, atL_vs_atR=True)
    def mk_tree7fork_(sf, depth, etree, /):
        'depth/uint -> etree/(twigL{depth}, stem{depth}/finger_tree{1+depth}, twigR{depth}) -> fork{depth}/finger_tree{depth}'
        (twigL, stem, twigR) = etree = mk_tuple(etree)
        autos = (
        [sf.get_auto5twigL_(depth, twigL)
        ,sf.get_auto5tree_(1+depth, stem)
        ,sf.get_auto5twigR_(depth, twigR)
        ])
        auto = mk_auto5chain_many_(sf, autos)
        fork = sf._mk_tree7fork_(depth, auto, etree)
        return fork
    def mk_tree7cane_(sf, depth, nodes, /):
        'depth/uint -> [node{depth}]{0<=len<=3} -> cane{depth}/finger_tree{depth}'
        nodes = mk_tuple(nodes)
        assert 0 <= len(nodes) <= 3
        auto = sf.mk_auto5nodes_(depth, nodes)
        cane = sf._mk_tree7cane_(depth, auto, nodes)
        return cane
    #########
    def iter_nodes5nonleaf_(sf, depth, nonleaf, /, *, reverse:bool):
        'depth/uint -> nonleaf{depth} -> Iter node{-1+depth}'
        assert depth > 0
        nodes = sf.get_nodes5nonleaf_(depth, nonleaf)
        return _iter_(reverse, nodes)
    #########
    def iter_nodes5cane_(sf, depth, cane, /, *, reverse:bool):
        'depth/uint -> cane{depth} -> Iter node{depth}'
        nodes = sf.get_nodes5cane_(depth, cane)
        return _iter_(reverse, nodes)
    def iter_nodes5twigL_(sf, depth, twigL, /, *, reverse:bool):
        'depth/uint -> twigL{depth} -> Iter node{depth}'
        nodes = sf.get_nodes5twigL_(depth, twigL)
        return _iter_(reverse, nodes)
    def iter_nodes5twigR_(sf, depth, twigR, /, *, reverse:bool):
        'depth/uint -> twigR{depth} -> Iter node{depth}'
        nodes = sf.get_nodes5twigR_(depth, twigR)
        return _iter_(reverse, nodes)
    #########
    def iter_nodes5tree_(sf, depth, tree, /, *, reverse:bool):
        'depth/uint -> finger_tree{depth} -> Iter node{depth}'
        if sf.is_fork_tree_(depth, tree):
            fork = tree
            (twigL, stem, twigR) = sf.get_etree5fork_(depth, fork)
            _depth = 1+depth
            ls = (
            [sf.iter_nodes5twigL_(depth, twigL, reverse=reverse)
            ,chains(sf.iter_nodes5nonleaf_(_depth, nonleaf, reverse=reverse) for nonleaf in sf.iter_nodes5tree_(_depth, stem, reverse=reverse))
            ,sf.iter_nodes5twigR_(depth, twigR, reverse=reverse)
            ])
            for it in _iter_(reverse, ls):
                yield from it
        else:
            cane = tree
            yield from sf.iter_nodes5cane_(depth, cane, reverse=reverse)
        return
    #########
    def iter_leafs5node_(sf, depth, node, /, *, reverse:bool):
        'depth/uint -> node{depth} -> Iter leaf'
        if depth == 0:
            leaf = node
            yield leaf
            return
        nonleaf = node
        _depth = -1+depth
        for _node in sf.iter_nodes5nonleaf_(depth, nonleaf, reverse=reverse):
            yield from sf.iter_leafs5node_(_depth, _node, reverse=reverse)
    def iter_leafs5tree_(sf, depth, tree, /, *, reverse:bool):
        'depth/uint -> finger_tree{depth} -> Iter leaf'
        for node in sf.iter_nodes5tree_(depth, tree, reverse=reverse):
            yield from sf.iter_leafs5node_(depth, node, reverse=reverse)
    #########
    def iter_datas5tree_(sf, depth, tree, /, *, reverse:bool):
        'depth/uint -> finger_tree{depth} -> Iter data'
        for leaf in sf.iter_leafs5tree_(depth, tree, reverse=reverse):
            data = sf.get_data5leaf_(leaf)
            yield data
    #########
    def mk_twigX7push_ex_(sf, depth, node, twigX, /, *, atL_vs_atR:bool):
        'depth/uint -> node{depth} -> twigX{depth,atL_vs_atR} -> (twigX{depth,atL_vs_atR}, may nonleaf{1+depth})'
        nodes = sf.get_nodes5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)
        nodes = _mk_nodes7push_(depth, node, nodes, atL_vs_atR=atL_vs_atR)
        if len(nodes) == 4:
            nodess = [nodes[:2], nodes[2:]]
            if atL_vs_atR:
                nodess.reverse()
            [nodesX, nodesY] = nodess
            twigX = sf.mk_twigX_(depth, nodesX, atL_vs_atR=atL_vs_atR)
            nonleaf = sf.mk_node7nonleaf_(1+depth, nodesY)
            may_nonleaf = nonleaf
        else:
            assert 1 <= len(nodes) <= 3
            twigX = sf.mk_twigX_(depth, nodes, atL_vs_atR=atL_vs_atR)
            may_nonleaf = None
        return (twigX, may_nonleaf)
    def mk_tree7push_(sf, depth, node, tree, /, *, atL_vs_atR:bool):
        'depth/uint -> node{depth} -> finger_tree{depth} -> finger_tree{depth}'
        if sf.is_fork_tree_(depth, tree):
            fork = tree
            #twigX = sf.get_twigX5fork_(depth, fork, atL_vs_atR=atL_vs_atR)
            #.etree = sf.get_etree5fork_(depth, fork)
            #.(twigX, stem, twigY) = _iter_(atL_vs_atR, etree)
            (twigX, stem, twigY) = sf.get_etreeX5fork_(depth, fork, reverse=atL_vs_atR)
            (twigX, may_nonleaf) = sf.mk_twigX7push_ex_(depth, node, twigX, atL_vs_atR=atL_vs_atR)
            if not None is may_nonleaf:
                nonleaf = may_nonleaf
                stem = sf.mk_tree7push_(1+depth, nonleaf, stem, atL_vs_atR=atL_vs_atR)
            stem
            #.etree = mk_tuple(_iter_(atL_vs_atR, (twigX, stem, twigY)))
            #.fork = sf.mk_tree7fork_(depth, etree)
            fork = sf.mk_tree7forkX_(depth, (twigX, stem, twigY), reverse=atL_vs_atR)
            tree = fork
        else:
            cane = tree
            nodes = sf.get_nodes5cane_(depth, cane)
            nodes = _mk_nodes7push_(depth, node, nodes, atL_vs_atR=atL_vs_atR)
            if len(nodes) == 4:
                twigL = sf.mk_twigL_(depth, nodes[:2])
                twigR = sf.mk_twigR_(depth, nodes[2:])
                stem = _tree = sf.mk_empty_tree_(1+depth)
                etree = (twigL, stem, twigR)
                fork = sf.mk_tree7fork_(depth, etree)
                tree = fork
            else:
                assert 1 <= len(nodes) <= 3
                cane = sf.mk_tree7cane_(depth, nodes)
                tree = cane
            tree
        tree
        return tree
    def mk_tree7pushs_(sf, depth, nodes, tree, /, *, atL_vs_atR:bool, reverse:bool):
        'depth/uint -> nodes/(Iter node{depth}) -> finger_tree{depth} -> finger_tree{depth} # reverse{nodes}'
        # [:设计冫树构造算法]:goto
        check_type_is(bool, atL_vs_atR)
        check_type_is(bool, reverse)
        ##################
        #old-ver:using:_reversed():
        ##################
        #.if 0:
        #.    if reverse is atL_vs_atR:
        #.        nodes = _reversed(nodes)
        #.        777;reverse = not reverse
        #.    assert reverse is (not atL_vs_atR)
        #.    for node in nodes:
        #.        tree = sf.mk_tree7push_(depth, node, tree, atL_vs_atR=atL_vs_atR)
        #.    return tree
        ##################
        tails = iter(nodes)
        777;del nodes
        heads = _take_le(4, tails)
        if len(heads) < 4:
            nodes = heads
            if reverse is atL_vs_atR:
                nodes = reversed(nodes)
                777;reverse = not reverse
            assert reverse is (not atL_vs_atR)
            for node in nodes:
                tree = sf.mk_tree7push_(depth, node, tree, atL_vs_atR=atL_vs_atR)
            return tree
        tails
        (reverse, (heads, tails))

        if not sf.is_fork_tree_(depth, tree):
            cane = tree
            nodes8cane = sf.iter_nodes5tree_(depth, cane, reverse=reverse)
            nodes8in = chain(heads, tails)
            ls = [nodes8cane, nodes8in]
                #atR and not reverse
                #atL and reverse
                #<=> atL_vs_atR is not reverse
            if reverse is atL_vs_atR:
                ls.reverse()
                # [ls := [nodes8in, nodes8cane]]
                #atL and not reverse
                #atR and reverse
                #<=> atL_vs_atR is not reverse
            nodes = chain(*ls)
            tree = sf.mk_tree5nodes_(depth, nodes, reverse=reverse)
        else:
            fork = tree
            (twigX, stem, twigY) = sf.get_etreeX5fork_(depth, fork, reverse=atL_vs_atR)
            twigX#focus:twigX not twigY
            # nodes{reverse?}++twigX++stem++twigY
            nodesX = sf.get_nodes5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)
            args_as_nodes8in = (reverse, (heads, tails))
            args_as_fork = (atL_vs_atR, (nodesX, stem, twigY))
            tree = _mk_tree7half_fork_pushs7sz_ge_4_(sf, depth, args_as_nodes8in, args_as_fork)
        return tree
        ##################
    #########
    def mk_tree5nodes_(sf, depth, nodes, /, *, reverse:bool):
        'depth/uint -> nodes/(Iter node{depth}) -> finger_tree{depth} # reverse{nodes}'
        check_type_is(bool, reverse)
        ##################
        #.if 0:
        #.    tree = sf.mk_empty_tree_(depth)
        #.    tree = sf.mk_tree7pushs_(depth, nodes, tree, atL_vs_atR=not reverse, reverse=reverse)
        #.    return tree
        ##################
        # [:设计冫树构造算法]:goto
        tails = iter(nodes)
        777;del nodes
        heads = _take_le(6, tails)
        if len(heads) < 6:
            nodes = heads
            if reverse:
                nodes = nodes[::-1]
                777;reverse = not reverse
            assert not reverse
            if len(heads) < 4:
                #cane
                tree = cane = sf.mk_tree7cane_(depth, nodes)
            else:
                #hollow_fork:2+(2|3)
                nodesL, nodesR = nodes[:2], nodes[2:]
                twigL = sf.mk_twigL_(depth, nodesL)
                twigR = sf.mk_twigR_(depth, nodesR)
                empty_stem = sf.mk_empty_tree_(1+depth)
                etree = (twigL, empty_stem, twigR)
                tree = hollow_fork = sf.mk_tree7fork_(depth, etree)
            tree
            return tree
        tails
        (reverse, (heads, tails))
        assert len(heads) >= 6

        atL_vs_atR = not reverse
        rv_nodesY = heads[:2]
        heads = heads[2:]
        (reverse, (rv_nodesY, heads, tails))
        assert len(heads) >= 4

        nodesY = rv_nodesY[::-1] if reverse else rv_nodesY
        twigY = sf.mk_twigY_(depth, nodesY, atL_vs_atR=atL_vs_atR)
        empty_stem = sf.mk_empty_tree_(1+depth)
        empty_nodesX = ()

        args_as_nodes8in = (reverse, (heads, tails))
        args_as_fork = (atL_vs_atR, (empty_nodesX, empty_stem, twigY))
        tree = _mk_tree7half_fork_pushs7sz_ge_4_(sf, depth, args_as_nodes8in, args_as_fork)
        return tree

    def mk_tree5leafs_(sf, leafs, /, *, reverse:bool):
        'leafs/(Iter leaf) -> finger_tree{depth==0} # reverse{leafs}'
        return sf.mk_tree5nodes_(depth:=0, leafs, reverse=reverse)
    def mk_tree5datas_(sf, datas, /, *, reverse:bool):
        'datas/(Iter data) -> finger_tree{depth==0} # reverse{datas}'
        leafs = map(sf.mk_node7leaf_, datas)
        return sf.mk_tree5leafs_(leafs, reverse=reverse)
    #########
    def mk_tree7chainLMR_(sf, depth, treeL, nodesM, treeR, /):
        'depth/uint -> finger_tree{depth} -> nodes/(Iter node{depth}) -> finger_tree{depth} -> finger_tree{depth}'
        # [:设计冫树构造算法]:goto
        if not sf.is_fork_tree_(depth, treeR):
            caneR = treeR
            nodes = chain(nodesM, sf.iter_nodes5tree_(depth, caneR, reverse=False))
            tree = sf.mk_tree7pushs_(depth, nodes, treeL, atL_vs_atR=True, reverse=False)
        elif not sf.is_fork_tree_(depth, treeL):
            caneL = treeL
            #new-ver:avoid:_reversed():
            nodes = chain(sf.iter_nodes5tree_(depth, caneL, reverse=False), nodesM)
            tree = sf.mk_tree7pushs_(depth, nodes, treeR, atL_vs_atR=False, reverse=False)

            #old-ver:using:_reversed():
            #.nodes = chain(_reversed(nodesM), sf.iter_nodes5tree_(depth, caneL, reverse=True))
            #.tree = sf.mk_tree7pushs_(depth, nodes, treeR, atL_vs_atR=False, reverse=True)
        else:
            forkL = treeL
            forkR = treeR
            (twigL, stemL, twigR6L) = sf.get_etree5fork_(depth, forkL)
            (twigL6R, stemR, twigR) = sf.get_etree5fork_(depth, forkR)
            _nodesM = _merge_nodes5LMR(sf, depth, twigR6L, nodesM, twigL6R)
            stem = sf.mk_tree7chainLMR_(1+depth, stemL, _nodesM, stemR)
            etree = (twigL, stem, twigR)
            fork = sf.mk_tree7fork_(depth, etree)
            tree = fork
        return tree
    #########
    #########
    #########
    def is_empty_tree_(sf, depth, tree, /):
        'depth/uint -> finger_tree{depth} -> bool'
        if sf.is_fork_tree_(depth, tree):
            fork = tree
            return False
        else:
            cane = tree
            nodes = sf.get_nodes5cane_(depth, cane)
            return len(nodes) == 0
    #########
    def mk_twigX7pop_ex_(sf, depth, twigX, stem, /, *, atL_vs_atR:bool):
        'depth/uint -> twigX{depth,atL_vs_atR} -> stem{depth} -> (node{depth}, twigX{depth,atL_vs_atR}, stem{depth}) | ^EmptyError'
        nodesX = sf.get_nodes5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)
        if len(nodesX) == 1:
            [nodeX] = nodesX
            (nonleafX, stem) = sf.mk_tree7pop_(1+depth, stem, atL_vs_atR=atL_vs_atR)
                # ^EmptyError
            _nodesX = sf.get_nodes5nonleaf_(1+depth, nonleafX)
        else:
            assert len(nodesX) >= 2
            (nodeX, _nodesX) = _mk_nodes7pop_(depth, nodesX, atL_vs_atR=atL_vs_atR)
        nodeX, _nodesX, stem
        twigX = sf.mk_twigX_(depth, _nodesX, atL_vs_atR=atL_vs_atR)
        return (nodeX, twigX, stem)

    def mk_tree7pop_(sf, depth, tree, /, *, atL_vs_atR:bool):
        'depth/uint -> finger_tree{depth} -> (node{depth}, finger_tree{depth}) | ^EmptyError'
        if sf.is_empty_tree_(depth, tree):
            raise EmptyError
        if sf.is_fork_tree_(depth, tree):
            fork = tree
            #.etree = sf.get_etree5fork_(depth, fork)
            #.(twigX, stem, twigY) = _iter_(atL_vs_atR, etree)
            (twigX, stem, twigY) = sf.get_etreeX5fork_(depth, fork, reverse=atL_vs_atR)
            try:
                (nodeX, twigX, stem) = sf.mk_twigX7pop_ex_(depth, twigX, stem, atL_vs_atR=atL_vs_atR)
            except EmptyError:
                # [stem empty]
                # [len(twigX.nodes) == 1]
                assert sf.is_empty_tree_(1+depth, stem)
                nodesX = sf.get_nodes5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)
                assert len(nodesX) == 1
                [nodeX] = nodesX
                nodesY = sf.get_nodes5twigY_(depth, twigY, atL_vs_atR=atL_vs_atR)
                _cane = sf.mk_tree7cane_(depth, nodesY)
                _tree = _cane
            else:
                nodeX
                #._etree = mk_tuple(_iter_(atL_vs_atR, (twigX, stem, twigY)))
                #._fork = sf.mk_tree7fork_(depth, _etree)
                _fork = sf.mk_tree7forkX_(depth, (twigX, stem, twigY), reverse=atL_vs_atR)
                _tree = _fork
            (nodeX, _tree)
        else:
            cane = tree
            nodes = sf.get_nodes5cane_(depth, cane)
            (nodeX, _nodes) = _mk_nodes7pop_(depth, nodes, atL_vs_atR=atL_vs_atR)
            _cane = sf.mk_tree7cane_(depth, _nodes)
            _tree = _cane
        (nodeX, _tree)
        return (nodeX, _tree)
    #########
    def mk_tree7pops_(sf, depth, num_pops, tree, /, *, atL_vs_atR:bool, reverse:bool):
        'depth/uint -> finger_tree{depth} -> (node{depth}, finger_tree{depth}) | ^EmptyError # reverse{nodes}'
        #vs:mk_tree7pushs_
        check_int_ge(0, num_pops)
        check_type_is(bool, atL_vs_atR)
        check_type_is(bool, reverse)
        nodes = []
        for _ in range(num_pops):
            (nodeX, tree) = sf.mk_tree7pop_(depth, tree, atL_vs_atR=atL_vs_atR)
            nodes.append(nodeX)
        if not reverse is atL_vs_atR:
            nodes.reverse()
            777;reverse = not reverse
        assert reverse is atL_vs_atR
        return (mk_tuple(nodes), tree)
    #########
    #########
    def split_tree__max_treeR_(sf, depth, auto2whether_treeR_, tree, /, *, known_begin_ok:bool, known_end_not_ok:bool):
        'depth/uint -> auto2whether_treeR_/(auto -> bool) -> finger_tree{depth} -> (treeR, autoM, treeL)/(finger_tree{depth}, finger_tree{depth}) | ^BadOffsetError # [tree == (treeL++treeR)][autoM == (treeR.auto)][auto2whether_treeR_(autoM) is True][treeR as long as possible]'
        return sf.split_tree__max_treeR__offset_(depth, sf.get_auto8null_(), auto2whether_treeR_, tree, known_begin_ok=known_begin_ok, known_end_not_ok=known_end_not_ok)
    def split_tree__max_treeR__offset_(sf, depth, auto8offset, auto2whether_treeR_, tree, /, *, known_begin_ok:bool, known_end_not_ok:bool):
        'depth/uint -> auto8offset/auto -> auto2whether_treeR_/(auto -> bool) -> finger_tree{depth} -> (treeR, autoM, treeL)/(finger_tree{depth}, finger_tree{depth}) | ^BadOffsetError # [tree == (treeL++treeR)][autoM == (treeR.auto<++>auto8offset)][auto2whether_treeR_(autoM) is True][treeR as long as possible]'
        return sf.split_tree__max_treeX__offset_(depth, auto8offset, auto2whether_treeR_, tree, known_begin_ok=known_begin_ok, known_end_not_ok=known_end_not_ok, atL_vs_atR=True)
    #########
    def split_tree__max_treeL_(sf, depth, auto2whether_treeL_, tree, /, *, known_begin_ok:bool, known_end_not_ok:bool):
        'depth/uint -> auto2whether_treeL_/(auto -> bool) -> finger_tree{depth} -> (treeL, autoM, treeR)/(finger_tree{depth}, finger_tree{depth}) | ^BadOffsetError # [tree == (treeL++treeR)][autoM == (treeL.auto)][auto2whether_treeL_(autoM) is True][treeL as long as possible]'
        return sf.split_tree__max_treeL__offset_(depth, sf.get_auto8null_(), auto2whether_treeL_, tree, known_begin_ok=known_begin_ok, known_end_not_ok=known_end_not_ok)
    def split_tree__max_treeL__offset_(sf, depth, auto8offset, auto2whether_treeL_, tree, /, *, known_begin_ok:bool, known_end_not_ok:bool):
        'depth/uint -> auto8offset/auto -> auto2whether_treeL_/(auto -> bool) -> finger_tree{depth} -> (treeL, autoM, treeR)/(finger_tree{depth}, finger_tree{depth}) | ^BadOffsetError # [tree == (treeL++treeR)][autoM == (auto8offset<++>treeL.auto)][auto2whether_treeL_(autoM) is True][treeL as long as possible]'
        return sf.split_tree__max_treeX__offset_(depth, auto8offset, auto2whether_treeL_, tree, known_begin_ok=known_begin_ok, known_end_not_ok=known_end_not_ok, atL_vs_atR=False)
        r'''[[[
        #.#########
        #.if not known_begin_ok:
        #.    if not auto2whether_treeL_(auto8offset):
        #.        raise BadOffsetError
        #.    known_begin_ok = True
        #.#########
        #.if not known_end_not_ok:
        #.    auto7end = sf.mk_auto5chain_two_(auto8offset, sf.get_auto5tree_(depth, tree))
        #.    if auto2whether_treeL_(auto7end):
        #.        treeL = tree
        #.        autoM = auto7end
        #.        treeR = sf.mk_empty_tree_(depth)
        #.        return (treeL, autoM, treeR)
        #.    known_end_not_ok = True
        #.#########
        #.assert known_begin_ok
        #.assert known_end_not_ok
        #.#########
        #.if sf.is_fork_tree_(depth, tree):
        #.    fork = tree
        #.    (twigL, stem, twigR) = sf.get_etree5fork_(depth, fork)
        #.    if not auto2whether_treeL_(autoL:=sf.mk_auto5chain_two_(auto8offset, sf.get_auto5twigL_(depth, twigL))):
        #.        #into:twigL
        #.        nodesLL = sf.get_nodes5twigL_(depth, twigL)
        #.        (nodesL, autoM, _nodesR) = _split_nodes__max_treeL__offset_(sf, depth, auto8offset, auto2whether_treeL_, nodesLL)
        #.        treeL = sf.mk_tree7cane_(depth, nodesL)
        #.        _, treeR = sf.mk_tree7pops_(depth, num_pops:=len(nodesL), tree, atL_vs_atR=False, reverse=False)
        #.    elif auto2whether_treeL_(autoR:=sf.mk_auto5chain_two_(autoL, sf.get_auto5tree_(1+depth, stem))):
        #.        #into:twigR
        #.        nodesRR = sf.get_nodes5twigR_(depth, twigR)
        #.        (_nodesL, autoM, nodesR) = _split_nodes__max_treeL__offset_(sf, depth, autoR, auto2whether_treeL_, nodesRR)
        #.        treeR = sf.mk_tree7cane_(depth, nodesR)
        #.        _, treeL = sf.mk_tree7pops_(depth, num_pops:=len(nodesR), tree, atL_vs_atR=True, reverse=True)
        #.    else:
        #.        #into:stem
        #.        (stemL, autoM_, _stemR) = sf.split_tree__max_treeL__offset_(1+depth, autoL, auto2whether_treeL_, stem, known_begin_ok=True, known_end_not_ok=True)
        #.        # [stemL maybe empty]
        #.        # [_stemR not empty]
        #.        (nonleafL6R, stemR) = sf.mk_tree7pop_(1+depth, _stemR, atL_vs_atR=False)
        #.        nodes = sf.get_nodes5nonleaf_(1+depth, nonleafL6R)
        #.        (_nodesL, autoM, _nodesR) = _split_nodes__max_treeL__offset_(sf, depth, autoM_, auto2whether_treeL_, nodes)
        #.        autoM
        #.        # [_nodesL maybe empty]
        #.        # [_nodesR not empty]
        #.        if not _nodesR:raise 000
        #.        if not _nodesL:
        #.            #tmp_node = sf.iter_nodes5tree_(depth, tree, reverse=False)
        #.            tmp_node = _nodesR[0]
        #.            tmp_twigR6L = sf.mk_twigR_(depth, [tmp_node])
        #.            _treeL = sf.mk_tree7fork_(depth, (twigL, stemL, tmp_twigR6L))
        #.            _, treeL = sf.mk_tree7pop_(depth, _treeL, atL_vs_atR=True)
        #.        else:
        #.            twigR6L = sf.mk_twigR_(depth, _nodesL)
        #.            treeL = sf.mk_tree7fork_(depth, (twigL, stemL, twigR6L))
        #.        treeL
        #.        twigL6R = sf.mk_twigL_(depth, _nodesR)
        #.        treeR = sf.mk_tree7fork_(depth, (twigL6R, stemR, twigR))
        #.    (treeL, autoM, treeR)
        #.else:
        #.    cane = tree
        #.    nodes = sf.get_nodes5cane_(depth, cane)
        #.    (nodesL, autoM, nodesR) = _split_nodes__max_treeL__offset_(sf, depth, auto8offset, auto2whether_treeL_, nodes)
        #.    treeL = sf.mk_tree7cane_(depth, nodesL)
        #.    treeR = sf.mk_tree7cane_(depth, nodesR)
        #.return (treeL, autoM, treeR)
        #.#########

        #]]]'''#'''

    #########
    def split_tree__max_treeX_(sf, depth, auto2whether_treeX_, tree, /, *, atL_vs_atR:bool, known_begin_ok:bool, known_end_not_ok:bool):
        'depth/uint -> auto2whether_treeX_/(auto -> bool) -> finger_tree{depth} -> (treeX, autoM, treeY)/(finger_tree{depth}, finger_tree{depth}) | ^BadOffsetError # [tree == (treeX++treeY if not atL_vs_atR else treeY++treeX)][autoM == treeX.auto][auto2whether_treeX_(autoM) is True][treeX as long as possible]'
        return sf.split_tree__max_treeX__offset_(depth, sf.get_auto8null_(), auto2whether_treeX_, tree, known_begin_ok=known_begin_ok, known_end_not_ok=known_end_not_ok, atL_vs_atR=atL_vs_atR)

    def get_etreeX5fork_(sf, depth, fork, /, *, reverse:bool):
        'depth/uint -> fork{depth} -> etreeX{depth,reverse}'
        etree = sf.get_etree5fork_(depth, fork)
        etreeX = etree if not reverse else etree[::-1]
        return etreeX
    def mk_tree7forkX_(sf, depth, etreeX, /, *, reverse:bool):
        'depth/uint -> etreeX{depth,reverse} -> fork{depth}'
        #etreeX = (twigX, stemX, twigY6X)
        etree = (etreeX if not reverse else etreeX[::-1])
        tree7fork = sf.mk_tree7fork_(depth, etree)
        return tree7fork
    def mk_twigY_(sf, depth, nodes, /, *, atL_vs_atR:bool):
        'depth/uint -> [node{depth}]{1<=len<=3} -> twigY{depth,atL_vs_atR}/twigX{depth,not atL_vs_atR}'
        return sf.mk_twigX_(depth, nodes, atL_vs_atR=not atL_vs_atR)
    def get_nodes5twigY_(sf, depth, twigY, /, *, atL_vs_atR:bool):
        'depth/uint -> twigY{depth,atL_vs_atR}/twigX{depth,not atL_vs_atR} -> [node{depth}]'
        return sf.get_nodes5twigX_(depth, twigY, atL_vs_atR=not atL_vs_atR)
    def mk_auto5chain_twoX_(sf, autoX, autoY, /, *, reverse:bool):
        if reverse:
            (autoX, autoY) = (autoY, autoX)
        return sf.mk_auto5chain_two_(autoX, autoY)
        #.(autoL, autoR) = (autoY, autoX) if reverse else (autoX, autoY)
        #.return sf.mk_auto5chain_two_(autoL, autoR)
    def split_tree__max_treeX__offset_(sf, depth, auto8offset, auto2whether_treeX_, tree, /, *, atL_vs_atR:bool, known_begin_ok:bool, known_end_not_ok:bool):
        'depth/uint -> auto8offset/auto -> auto2whether_treeX_/(auto -> bool) -> finger_tree{depth} -> (treeX, autoM, treeY)/(finger_tree{depth}, finger_tree{depth}) | ^BadOffsetError # [tree == (treeX++treeY if not atL_vs_atR else treeY++treeX)][autoM == (auto8offset<++>treeX.auto if not atL_vs_atR else treeX.auto<++>auto8offset)][auto2whether_treeX_(autoM) is True][treeX as long as possible]'
        #########
        if not known_begin_ok:
            if not auto2whether_treeX_(auto8offset):
                raise BadOffsetError
            known_begin_ok = True
        #########
        if not known_end_not_ok:
            auto7end = sf.mk_auto5chain_twoX_(auto8offset, sf.get_auto5tree_(depth, tree), reverse=atL_vs_atR)
            if auto2whether_treeX_(auto7end):
                treeX = tree
                autoM = auto7end
                treeY = sf.mk_empty_tree_(depth)
                return (treeX, autoM, treeY)
            known_end_not_ok = True
        #########
        assert known_begin_ok
        assert known_end_not_ok
        del known_begin_ok
        del known_end_not_ok
        #########
        if sf.is_fork_tree_(depth, tree):
            fork = tree
            #.(twigX, stem, twigY) = _iter_(atL_vs_atR, sf.get_etree5fork_(depth, fork))
            (twigX, stem, twigY) = sf.get_etreeX5fork_(depth, fork, reverse=atL_vs_atR)
            if not auto2whether_treeX_(autoX:=sf.mk_auto5chain_twoX_(auto8offset, sf.get_auto5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR), reverse=atL_vs_atR)):
                #into:twigX
                nodesXX = sf.get_nodes5twigX_(depth, twigX, atL_vs_atR=atL_vs_atR)
                (nodesX, autoM, _nodesY) = _split_nodes__max_treeX__offset_(sf, depth, auto8offset, auto2whether_treeX_, nodesXX, atL_vs_atR=atL_vs_atR)
                treeX = sf.mk_tree7cane_(depth, nodesX)
                _, treeY = sf.mk_tree7pops_(depth, num_pops:=len(nodesX), tree, atL_vs_atR=atL_vs_atR, reverse=atL_vs_atR)
            elif auto2whether_treeX_(autoY:=sf.mk_auto5chain_twoX_(autoX, sf.get_auto5tree_(1+depth, stem), reverse=atL_vs_atR)):
                #into:twigY
                nodesYY = sf.get_nodes5twigY_(depth, twigY, atL_vs_atR=atL_vs_atR)
                (_nodesX, autoM, nodesY) = _split_nodes__max_treeX__offset_(sf, depth, autoY, auto2whether_treeX_, nodesYY, atL_vs_atR=atL_vs_atR)
                treeY = sf.mk_tree7cane_(depth, nodesY)
                _, treeX = sf.mk_tree7pops_(depth, num_pops:=len(nodesY), tree, atL_vs_atR=not atL_vs_atR, reverse=not atL_vs_atR)
            else:
                #into:stem
                (stemX, autoM_, _stemY) = sf.split_tree__max_treeX__offset_(1+depth, autoX, auto2whether_treeX_, stem, known_begin_ok=True, known_end_not_ok=True, atL_vs_atR=atL_vs_atR)
                # [stemX maybe empty]
                # [_stemY not empty]
                (nonleafX6Y, stemY) = sf.mk_tree7pop_(1+depth, _stemY, atL_vs_atR=atL_vs_atR)
                nodes = sf.get_nodes5nonleaf_(1+depth, nonleafX6Y)
                (_nodesX, autoM, _nodesY) = _split_nodes__max_treeX__offset_(sf, depth, autoM_, auto2whether_treeX_, nodes, atL_vs_atR=atL_vs_atR)
                autoM
                # [_nodesX maybe empty]
                # [_nodesY not empty]
                if not _nodesY:raise 000
                #######
                #_nodesX -> treeX
                #######
                if not _nodesX:
                    #tmp_node = sf.iter_nodes5tree_(depth, tree, reverse=False)
                    tmp_node = _nodesY[0]
                    tmp_twigY6X = sf.mk_twigY_(depth, [tmp_node], atL_vs_atR=atL_vs_atR)
                    _treeX = sf.mk_tree7forkX_(depth, (twigX, stemX, tmp_twigY6X), reverse=atL_vs_atR)
                    _, treeX = sf.mk_tree7pop_(depth, _treeX, atL_vs_atR=not atL_vs_atR)
                else:
                    twigY6X = sf.mk_twigY_(depth, _nodesX, atL_vs_atR=atL_vs_atR)
                    treeX = sf.mk_tree7forkX_(depth, (twigX, stemX, twigY6X), reverse=atL_vs_atR)
                treeX
                #######
                #_nodesY -> treeY
                #######
                _nodesY
                twigX6Y = sf.mk_twigX_(depth, _nodesY, atL_vs_atR=atL_vs_atR)
                treeY = sf.mk_tree7forkX_(depth, (twigX6Y, stemY, twigY), reverse=atL_vs_atR)
                #######
            (treeX, autoM, treeY)
        else:
            cane = tree
            nodes = sf.get_nodes5cane_(depth, cane)
            (nodesX, autoM, nodesY) = _split_nodes__max_treeX__offset_(sf, depth, auto8offset, auto2whether_treeX_, nodes, atL_vs_atR=atL_vs_atR)
            treeX = sf.mk_tree7cane_(depth, nodesX)
            treeY = sf.mk_tree7cane_(depth, nodesY)
        return (treeX, autoM, treeY)
        #########

    #def split_tree_at_(sf, depth, path, tree, /):
    #########
    #########
    #########
    #########
    #########
    #########
    #########
    #########
    #########
    #########
    #########
    #########
    #########
    r'''[[[
        if sf.is_fork_tree_(depth, tree):
            fork = tree
        else:
            cane = tree
    #]]]'''#'''

def _take_le(sz, it, /):
    assert iter(it) is it
    return tuple(islice(it, 0, sz))
def _take2(it, /):
    return tuple(islice(it, 0, 2))
def _merge_nodes5LMR(sf, depth, twigR6L, nodesM, twigL6R, /):
    it = nodes = chain(*''
        ,sf.iter_nodes5twigR_(depth, twigR6L, reverse=False)
        ,iter(nodesM)
        ,sf.iter_nodes5twigL_(depth, twigL6R, reverse=False)
        )
    return _merge_nodes7sink7sz_ge_2(sf, depth, it, reverse=False)
def _merge_nodes7sink7sz_ge_2(sf, depth, nodes7sz_ge_2, /, *, reverse:bool):
    '[len(nodes7sz_ge_2) >= 2]'
    it = iter(nodes7sz_ge_2)
    _depth = 1+depth
    def f(*nodes):
        return sf.mk_node7nonleaf_(_depth, nodes)
    if reverse:
        g = f
        def f(*nodes):
            return g(*reversed(nodes))
    (a, b) = _take2(it)
        # !! [len(nodes7sz_ge_2) >= 2]
    while 1:
        ls = _take2(it)
        if len(ls) < 2:
            yield f(a, b, *ls)
            break
        yield f(a, b)
        (a, b) = ls
    return
def _iter_(reverse, ls, /):
    f = iter if not reverse else reversed
    return f(ls)
#.def _reversed(it, /):
#.    try:
#.        return reversed(it)
#.    except TypeError:
#.        pass
#.    return reversed([*it])
def _mk_nodes7pop_(depth, nodes, /, *, atL_vs_atR:bool):
    if len(nodes) == 0:
        raise EmptyError
    nodeX = nodes[0] if not atL_vs_atR else nodes[-1]
    _nodes = nodes[1:] if not atL_vs_atR else nodes[:-1]
    return (nodeX, _nodes)
def _mk_nodes7push_(depth, node, nodes, /, *, atL_vs_atR:bool):
    nodes = (node, *nodes) if not atL_vs_atR else (*nodes, node)
    return nodes


def _split_nodes__max_treeL__offset_(sf, depth, auto8offset, auto2whether_treeL_, nodes, /):
    '[known_begin_ok][known_end_not_ok] => ... -> (nodesL, autoM, nodesR)'
    return _split_nodes__max_treeX__offset_(sf, depth, auto8offset, auto2whether_treeL_, nodes, atL_vs_atR=False)
    r'''[[[
    #.#assert known_begin_ok
    #.#assert known_end_not_ok
    #.assert len(nodes) >= 1
    #.    # !! [known_begin_ok][known_end_not_ok]

    #.assert len(nodes) <= 3
    #.    # !! nonleaf.nodes
    #.    # !! twigX.nodes
    #.    # !! cane.nodes
    #.auto7acc = auto8offset
    #.for j, node in enumerate(nodes[:-1]):
    #.    autoM = auto7acc
    #.    auto7acc = sf.mk_auto5chain_two_(auto7acc, sf.get_auto5node_(depth, node))
    #.    if not auto2whether_treeL_(auto7acc):
    #.        break
    #.else:
    #.    j = -1+len(nodes)
    #.    autoM = auto7acc
    #.j
    #.(nodesL, nodesR) = nodes[:j], nodes[j:]
    #.return (nodesL, autoM, nodesR)

    #]]]'''#'''
def _split_nodes__max_treeX__offset_(sf, depth, auto8offset, auto2whether_treeX_, nodes, /, *, atL_vs_atR:bool):
    '[known_begin_ok][known_end_not_ok] => ... -> (nodesX, autoM, nodesY)'
    #assert known_begin_ok
    #assert known_end_not_ok
    assert len(nodes) >= 1
        # !! [known_begin_ok][known_end_not_ok]

    assert len(nodes) <= 3
        # !! nonleaf.nodes
        # !! twigX.nodes
        # !! cane.nodes
    auto7acc = auto8offset
    for j, node in enumerate(nodes[:-1] if not atL_vs_atR else reversed(nodes[1::])):
        autoM = auto7acc
        auto7acc = sf.mk_auto5chain_twoX_(auto7acc, sf.get_auto5node_(depth, node), reverse=atL_vs_atR)
        if not auto2whether_treeX_(auto7acc):
            break
    else:
        j = -1+len(nodes)
        autoM = auto7acc
    j
    if atL_vs_atR:
        j = len(nodes) -j
    j
    (nodesX, nodesY) = nodes[:j], nodes[j:]
    if atL_vs_atR:
        (nodesX, nodesY) = (nodesY, nodesX)
    return (nodesX, autoM, nodesY)




def _mk_tree7half_fork_pushs7sz_ge_4_(sf, depth, args_as_nodes8in, args_as_fork, /):
    # [:设计冫树构造算法]:goto
    (reverse, (heads, tails)) = args_as_nodes8in
    (atL_vs_atR, (nodesX, stem, twigY)) = args_as_fork
    assert len(heads) >= 4
        #but required only:
    assert len(heads)+len(nodesX) >= 4
        # MAYBE:[len(nodesX) == 0]
        #   see:empty_nodesX@mk_tree5nodes_
    assert 0 <= len(nodesX) <= 3
    r'''[[[
    if reverse is atL_vs_atR:
        if not reverse:
            #atL
            #heads++tails++nodesX++stem++twigY
        else:
            #atR
            #twigY++stem++nodesX++~tails++~heads
    else:
        #std/expected:
        if not reverse:
            #atR
            #twigY++stem++nodesX++heads++tails
        else:
            #atL
            #~tails++~heads++nodesX++stem++twigY
    #]]]'''#'''
    rv_nodesX = _iter_(reverse, nodesX)

    if reverse is atL_vs_atR:
        rv_nodesXX = chain(heads, tails, rv_nodesX)
    else:
        rv_nodesXX = chain(rv_nodesX, heads, tails)
    rv_nodesXX#rv_nodesXX{reverse}
    777;del nodesX, heads, tails
    ##################common:
    # (atL_vs_atR, ((reverse, rv_nodesXX), stem, twigY))
    ##################



    ##################ver2-iter:
    # (atL_vs_atR, ((reverse, rv_nodesXX), stem, twigY))
    ############
    if reverse is atL_vs_atR:
        new_nodesX = _take_le(2, rv_nodesXX)
        if reverse:
            new_nodesX = new_nodesX[::-1]
    else:
        rv_nodesXX = FixedSizeTailTrapIterator(2, rv_nodesXX)
    rv_nodesXX
    rv_nodesXXXX = _sink7iter7sz_ge_2(sf, depth, rv_nodesXX, reverse=reverse)

    new_stem = sf.mk_tree7pushs_(1+depth, rv_nodesXXXX, stem, atL_vs_atR=atL_vs_atR, reverse=reverse)
    # (atL_vs_atR, ((new_nodesX|FixedSizeTailTrapIterator), new_stem, twigY))
    if reverse is atL_vs_atR:
        new_nodesX
    else:
        rv_nodesXX
        assert rv_nodesXX.eof
        new_nodesX = rv_nodesXX.trap2tuple_()
        if reverse:
            new_nodesX = new_nodesX[::-1]
    new_nodesX
    # (atL_vs_atR, (new_nodesX, new_stem, twigY))

    new_twigX = sf.mk_twigX_(depth, new_nodesX, atL_vs_atR=atL_vs_atR)
    # (atL_vs_atR, (new_twigX, new_stem, twigY))
    tree = fork = sf.mk_tree7forkX_(depth, (new_twigX, new_stem, twigY), reverse=atL_vs_atR)
    return tree


    ##################ver1-seq:
    # (atL_vs_atR, ((reverse, rv_nodesXX), stem, twigY))
    ############
    #.rv_nodesXX = [*rv_nodesXX]
    #.if reverse is atL_vs_atR:
    #.    rv_nodesXX.reverse()
    #.    777;reverse = not reverse
    #.assert reverse is (not atL_vs_atR)
    #.assert len(rv_nodesXX) >= 4
    #.new_nodesX = rv_nodesXX[-2:]
    #.if reverse:new_nodesX.reverse()
    #.777;del rv_nodesXX[-2:]

    #.assert len(rv_nodesXX) >= 2
    #.rv_nodesXXXX = _sink7seq7sz_ge_2(sf, depth, rv_nodesXX, reverse=reverse)

    #.new_twigX = sf.mk_twigX_(depth, new_nodesX, atL_vs_atR=atL_vs_atR)
    #.# (atL_vs_atR, (new_twigX, ((reverse, rv_nodesXXXX), stem), twigY))
    #.new_stem = sf.mk_tree7pushs_(1+depth, rv_nodesXXXX, stem, atL_vs_atR=atL_vs_atR, reverse=reverse)
    #.# (atL_vs_atR, (new_twigX, new_stem, twigY))
    #.tree = fork = sf.mk_tree7forkX_(depth, (new_twigX, new_stem, twigY), reverse=atL_vs_atR)
    #.return tree

def _sink7seq7sz_ge_2(sf, depth, node_seq7sz_ge_2, /, *, reverse:bool):
    '-> Iter node{1+depth}'
    assert len(node_seq7sz_ge_2) >= 2
    nodes = node_seq7sz_ge_2
    _depth = 1+depth
    sz = 2 + (len(nodes) &1)
    L = len(nodes) -sz
    for j in range(0, L, 2):
        yield sf.mk_node7nonleaf_(_depth, nodes[j:j+2])
    yield sf.mk_node7nonleaf_(_depth, nodes[L:])
def _sink7iter7sz_ge_2(sf, depth, node_iter7sz_ge_2, /, *, reverse:bool):
    return _merge_nodes7sink7sz_ge_2(sf, depth, node_iter7sz_ge_2, reverse=reverse)
    #it = FixedSizeTailTrapIterator(2, node_iter7sz_ge_2)
r'''[[[
[:设计冫树构造算法]:here
mk_tree7chainLMR_
mk_tree7pushs_
mk_tree5nodes_
_mk_tree7half_fork_pushs7sz_ge_4_

[node{depth}.min_num_leafs == 1 if depth==0 else 2*node{-1+depth}.min_num_leafs == 2**depth]
[node{depth}.max_num_leafs == 1 if depth==0 else 3*node{-1+depth}.max_num_leafs == 3**depth]
[2**(1+depth) <= 3**depth]
    <==> [depth >= 2]

[twigX{depth}.min_num_leafs == 1*node{depth}.min_num_leafs == 2**depth]
[twigX{depth}.max_num_leafs == 3*node{depth}.max_num_leafs == 3**(1+depth)]

[cane{depth}.min_num_leafs == 0]
[cane{depth}.max_num_leafs == 3*node{depth}.max_num_leafs == 3**(1+depth)]

[0..=3] => cane
[4..=5] => hollow_fork # with empty stem
    [4==2+0+2]
    [5==2+0+3]
[6..] => [2+middle{>=2}+2]

归组:nodes{depth} -> [2,4,8,...,2**(1+j),...,2**L]{len==L>=0}+tail{<2**(1+L)}{>=0}
    (2**(1+L)-2)+tail
case:
    * []+[0..1] -> cane
    * [2]+[0..3] -> cane or hollow_fork
    # [total>=6]:
    * [L>=1] => [2,...,2**(1+L)]+tail/[0..<2**(2+L)]:
        bin(tail)
        [2*2**0,2*2**1,...,2*2**(L-1),2*2**L==1*2**(1+L); ?*2**L,?*2**(L-1),...,?*2**1,?*2**0]
            [『?』<-{0,1}]
        退两位:
        [2*2**0,2*2**1,...,2*2**(L-1),0*2**L==0*2**(1+L); (1+?)*2**L,(1+?)*2**(L-1),...,(1+?)*2**1,(2+?)*2**0]
            [『(2+?)』<-{2,3}]
            [『(1+?)』<-{1,2}]

case:
    #mk_tree7chainLMR_
    * tree++nodes++tree
        * fork++nodes++fork
            => twigL ++(stemL++sink(twigR6L++nodes++twigL6R)++stemR)++twigR
                recur
        * cane++nodes++tree
            => image:
        * tree++nodes++cane
            => tree++nodes
                pushs
    #mk_tree7pushs_
    * tree++nodes
        #pushs
        * tree++nodes{len<=3}
            => for_loop:push
        * tree++nodes{len>=4}
            * cane++nodes{len>=4}
                => nodes
                    from_nodes
            * fork++nodes{len>=4-fork.twigR.num_nodes}
                => twigL++stem++(twigR++nodes){len>=4}
                    half_fork_pushs7sz_ge_4
    #mk_tree5nodes_
    * nodes
        #from_nodes
        * nodes{len<=3}
            => cane
        * nodes{4<=len<=5}
            => hollow_fork
        * nodes{len>=6}
            => twigL++empty_stem++nodes{len>=4}
                half_fork_pushs7sz_ge_4
    #_mk_tree7half_fork_pushs7sz_ge_4_
    * twigL++stem++nodes{len>=4}
        #half_fork_pushs7sz_ge_4
        => twigL ++(stem++sink(nodes[:-2]))++twigR(nodes[-2:])
            pushs
#]]]'''#'''







#################################
#@20260402
#################################
class IWrapper4ft_xxx(ABC):
    __slots__ = ()
    #########
    @property
    @abstractmethod
    def ops4ft(sf, /):
        '-> ops4ft/IOps4FingerTree'
    @property
    @abstractmethod
    def depth(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def auto(sf, /):
        '-> auto'
    @property
    @abstractmethod
    def ft_kind(sf, /):
        '-> str/regex"tree|twig|node|node_seq"'
    @property
    @abstractmethod
    def is_leaf(sf, /):
        '-> bool'
    @abstractmethod
    def iter_children_(sf, /):
        '-> Iter IWrapper4ft_xxx | ^TypeError if is_leaf'
    #########
class Wrapper4ft_tree(IWrapper4ft_xxx):
    'cane|fork'
    ___no_slots_ok___ = True
    def __init__(sf, ops4ft, depth, tree, /):
        sf._ops = ops4ft
        sf._dph = depth
        sf._t = tree
    @property
    @override
    def ops4ft(sf, /):
        return sf._ops
    @property
    @override
    def depth(sf, /):
        return sf._dph
    @property
    def tree(sf, /):
        '-> finger_tree'
        return sf._t
    @property
    def is_cane(sf, /):
        '-> bool'
        return not sf.ops4ft.is_fork_tree_(sf.depth, sf.tree)
    @property
    @override
    def auto(sf, /):
        return sf.ops4ft.get_auto5tree_(sf.depth, sf.tree)
    #@override
    ft_kind = 'tree'
    #@override
    is_leaf = False
    @override
    def iter_children_(sf, /):
        ops4ft = sf.ops4ft
        depth = sf.depth
        if sf.is_cane:
            cane = sf.tree
            node_seq = ops4ft.get_nodes5cane_(depth, cane)
            yield Wrapper4ft_node_seq(ops4ft, depth, node_seq, sf.auto)
        else:
            fork = sf.tree
            (twigL, stem, twigR) = ops4ft.get_etree5fork_(depth, fork)
            yield Wrapper4ft_twigX(ops4ft, depth, twigL, False)
            yield Wrapper4ft_tree(ops4ft, 1+depth, stem)
            yield Wrapper4ft_twigX(ops4ft, depth, twigR, True)
class Wrapper4ft_twigX(IWrapper4ft_xxx):
    ___no_slots_ok___ = True
    def __init__(sf, ops4ft, depth, twigX, atL_vs_atR, /):
        check_type_is(bool, atL_vs_atR)
        sf._ops = ops4ft
        sf._dph = depth
        sf._w = twigX
        sf._R = atL_vs_atR
    @property
    @override
    def ops4ft(sf, /):
        return sf._ops
    @property
    @override
    def depth(sf, /):
        return sf._dph
    @property
    def twigX(sf, /):
        '-> twigX'
        return sf._w
    @property
    def atL_vs_atR(sf, /):
        '-> twigX'
        return sf._R
    @property
    def atL(sf, /):
        '-> bool'
        return not sf.atL_vs_atR
    @property
    @override
    def auto(sf, /):
        return sf.ops4ft.get_auto5twigX_(sf.depth, sf.twigX, atL_vs_atR=sf.atL_vs_atR)
    #@override
    ft_kind = 'twig'
    #@override
    is_leaf = False
    @override
    def iter_children_(sf, /):
        ops4ft = sf.ops4ft
        depth = sf.depth
        node_seq = ops4ft.get_nodes5twigX_(depth, sf.twigX, atL_vs_atR=sf.atL_vs_atR)
        yield Wrapper4ft_node_seq(ops4ft, depth, node_seq, sf.auto)
class Wrapper4ft_node_seq(IWrapper4ft_xxx):
    ___no_slots_ok___ = True
    def __init__(sf, ops4ft, depth, node_seq, auto, /):
        #get_nodes5cane_
        len(node_seq)
        node_seq[:0]
        sf._ops = ops4ft
        sf._dph = depth
        sf._ns = node_seq
        sf._au = auto
    @property
    @override
    def ops4ft(sf, /):
        return sf._ops
    @property
    @override
    def depth(sf, /):
        return sf._dph
    @property
    def node_seq(sf, /):
        '-> [node]'
        return sf._ns
    @property
    @override
    def auto(sf, /):
        return sf._au
    #@override
    ft_kind = 'node_seq'
    #@override
    is_leaf = False
    @override
    def iter_children_(sf, /):
        ops4ft = sf.ops4ft
        depth = sf.depth
        for node in sf.node_seq:
            yield Wrapper4ft_node(ops4ft, depth, node)
class Wrapper4ft_node(IWrapper4ft_xxx):
    'leaf|nonleaf'
    ___no_slots_ok___ = True
    def __init__(sf, ops4ft, depth, node, /):
        sf._ops = ops4ft
        sf._dph = depth
        sf._nd = node
    @property
    @override
    def ops4ft(sf, /):
        return sf._ops
    @property
    @override
    def depth(sf, /):
        return sf._dph
    @property
    def node(sf, /):
        '-> node'
        return sf._nd
    @property
    @override
    def auto(sf, /):
        return sf.ops4ft.get_auto5node_(sf.depth, sf.node)
    #@override
    ft_kind = 'node'
    @property
    @override
    def is_leaf(sf, /):
        return 0 == sf.depth
    @override
    def iter_children_(sf, /):
        if sf.is_leaf: raise TypeError
        nonleaf = sf.node
        ops4ft = sf.ops4ft
        depth = sf.depth
        _node_seq = ops4ft.get_nodes5nonleaf_(depth, nonleaf)
        yield Wrapper4ft_node_seq(ops4ft, -1+depth, _node_seq, sf.auto)
    @property
    def data(sf, /):
        '[is_leaf] => -> data'
        if not sf.is_leaf: raise TypeError
        leaf = sf.node
        ops4ft = sf.ops4ft
        depth = sf.depth
        data = ops4ft.get_data5leaf_(leaf)
        return data
IWrapper4ft_xxx
#################################
class IVisit4Wrapper4ft_xxx(ABC):
    'used to eval lazy_properties6auto'
    #view ../../python3_src/seed/types/VisitTree__ver2.py
    __slots__ = ()
    @abstractmethod
    def _enter_wrapper4ft_xxx_(sf, wrapper4ft_xxx, /):
        'IWrapper4ft_xxx -> tmay oresult # {() => step into; (oresult,) => step over/skip subtree}'
    @abstractmethod
    def _exit_wrapper4ft_xxx_7not_leaf_(sf, wrapper4ft_xxx7not_leaf, child_oresult_seq, /):
        'IWrapper4ft_xxx{not .is_leaf} -> [oresult] -> oresult'
    @abstractmethod
    def _exit_wrapper4ft_xxx_7is_leaf_(sf, wrapper4ft_xxx7is_leaf, /):
        'IWrapper4ft_xxx{.is_leaf} -> oresult'
    def visit_wrapper4ft_xxx_(sf, wrapper4ft_xxx, /):
        'IWrapper4ft_xxx -> oresult'
        gi = _gi_visit_wrapper4ft_xxx_(sf, wrapper4ft_xxx)
        oresult = flatten_recur(gi)
        return oresult

def _gi_visit_wrapper4ft_xxx_(sf, wrapper4ft_xxx, /):
    'IWrapper4ft_xxx -> GI{oresult}'
    match sf._enter_wrapper4ft_xxx_(wrapper4ft_xxx):
        case [oresult]:
            return oresult
        case []:
            pass
        case bad:
            raise TypeError(bad)
    if wrapper4ft_xxx.is_leaf:
        oresult = sf._exit_wrapper4ft_xxx_7is_leaf_(wrapper4ft_xxx)
    else:
        rs = []
        for child in wrapper4ft_xxx.iter_children_():
            child_oresult = yield _gi_visit_wrapper4ft_xxx_(sf, child)
            rs.append(child_oresult)
        child_oresult_seq = tuple(rs)
        oresult = sf._exit_wrapper4ft_xxx_7not_leaf_(wrapper4ft_xxx, child_oresult_seq)
    oresult
    return oresult
IVisit4Wrapper4ft_xxx
#################################
class Visit4Wrapper4ft_xxx__7fill_part6auto(IVisit4Wrapper4ft_xxx):
    '[oresult := part4auto]'
    ___no_slots_ok___ = True
    def __init__(sf, filler, /):
        check_type_le(IFiller4PartialAuto, filler)
        sf._filler = filler
    @override
    def _enter_wrapper4ft_xxx_(sf, wrapper4ft_xxx, /):
        filler = sf._filler
        auto = wrapper4ft_xxx.auto
        return filler.get_tmay_part6auto_(auto)
    @override
    def _exit_wrapper4ft_xxx_7not_leaf_(sf, wrapper4ft_xxx7not_leaf, child_oresult_seq, /):
        filler = sf._filler
        auto = wrapper4ft_xxx7not_leaf.auto
        parts4auto = child_oresult_seq
        part4auto = filler.chain_many_parts4auto_(parts4auto)
        filler.setdefault_part6auto_(auto, part4auto)
        oresult = part4auto
        return oresult
    @override
    def _exit_wrapper4ft_xxx_7is_leaf_(sf, wrapper4ft_xxx7is_leaf, /):
        filler = sf._filler
        auto = wrapper4ft_xxx7is_leaf.auto
        data = wrapper4ft_xxx7is_leaf.data
        part4auto = filler.mk_part4auto5data_(data, auto)
        filler.setdefault_part6auto_(auto, part4auto)
        oresult = part4auto
        return oresult

#################################
class IFiller4PartialAuto(ABC):
    'used by Visit4Wrapper4ft_xxx__7fill_part6auto'
    __slots__ = ()
    @abstractmethod
    def get_tmay_part6auto_(sf, auto, /):
        'auto -> tmay part4auto'
    @abstractmethod
    def _setdefault_part6auto_(sf, auto, part4auto, /):
        'auto -> part4auto -> None'
    @abstractmethod
    def eq_part4auto_(sf, lhs_part4auto, rhs_part4auto, /):
        'part4auto -> part4auto -> bool'
    #IBaseOps4Auto6FingerTree
    @abstractmethod
    def get_null_part4auto_(sf, /):
        '-> part4auto'
    @abstractmethod
    def mk_part4auto5data_(sf, data, auto, /):
        'data -> auto -> part4auto'
    @abstractmethod
    def chain_two_parts4auto_(sf, lhs_part4auto, rhs_part4auto, /):
        'part4auto -> part4auto -> part4auto'
    def chain_many_parts4auto_(sf, parts4auto, /):
        'Iter part4auto -> part4auto'
        it = iter(parts4auto)
        #.lhs_part4auto = sf.get_null_part4auto_()
        #.lhs_part4auto = next(it, lhs_part4auto)
        for lhs_part4auto in it:
            break
        else:
            lhs_part4auto = sf.get_null_part4auto_()
        lhs_part4auto
        for rhs_part4auto in it:
            lhs_part4auto = sf.chain_two_parts4auto_(lhs_part4auto, rhs_part4auto)
        return lhs_part4auto
    def setdefault_part6auto_(sf, auto, part4auto, /):
        'auto -> part4auto -> None'
        if not (tm:=sf.get_tmay_part6auto_(auto)):
            sf._setdefault_part6auto_(auto, part4auto)
            if not (tm:=sf.get_tmay_part6auto_(auto)):raise Exception(sf, auto, part4auto)
        tm
        [_part4auto] = tm
        if not sf.eq_part4auto_(part4auto, _part4auto):raise Exception(sf, auto, part4auto, _part4auto)
        return
IFiller4PartialAuto
#################################
#################################

__all__
from seed.data_funcs.finger_tree.ft23 import BaseFingerTreeError, EmptyError, BadOffsetError


from seed.data_funcs.finger_tree.ft23 import IOps4FingerTree, IBasicOps4FingerTree, IBaseOps4Auto6FingerTree
from seed.data_funcs.finger_tree.ft23 import mk_auto5chain_many_

from seed.data_funcs.finger_tree.ft23 import *
