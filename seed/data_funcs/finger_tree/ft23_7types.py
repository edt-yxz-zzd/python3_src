#__all__:goto
#TODO:goto
#   property5wrapper4ft_xxx_and_key6auto_
#       #xxx:_settle7lazy_attr
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/ft23_7types.py

seed.data_funcs.finger_tree.ft23_7types
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.ft23_7types -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.ft23_7types:__doc__ -ht # -ff -df
#######

[[
取消:@20260402
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.data_funcs.finger_tree.ft23_7types   @f
]]]'''#'''
__all__ = r'''
Ops4FingerTree
    Ops4Auto6FingerTree
        IOps4Attr4Auto6FingerTree

IOps4Attr4Auto6FingerTree
    Ops4Attr4Auto6FingerTree__sized
        ops4attr_len
    Ops4Attr4Auto6FingerTree__hash
        ops4attr_hash
    Ops4Attr4Auto6FingerTree__may_hash
        ops4attr_may_hash
    IOps4Attr4Auto6FingerTree__ord_key
        IOps4Attr4Auto6FingerTree__mixin__init_key_func
            IOps4Attr4Auto6FingerTree__max
                Ops4Attr4Auto6FingerTree__max
                    ops4attr_max7echo
            IOps4Attr4Auto6FingerTree__min
                Ops4Attr4Auto6FingerTree__min
                    ops4attr_min7echo
            IOps4Attr4Auto6FingerTree__rightmost
                Ops4Attr4Auto6FingerTree__rightmost
                    ops4attr_rightmost7echo
            IOps4Attr4Auto6FingerTree__leftmost
                Ops4Attr4Auto6FingerTree__leftmost
                    ops4attr_leftmost7echo

ops4attr_len
    check_ops4sized_finger_tree_
    len5sized_finger_tree_
    split_sized_finger_tree_
ops4attr_hash
    check_ops4hashable_finger_tree_
    hash5hashable_finger_tree_
ops4attr_may_hash
    check_ops4mhashable_finger_tree_
    may_hash5mhashable_finger_tree_
ops4attr_leftmost7echo
    check_ops4descend_finger_tree_
    tmay_leftmost5descend_finger_tree_
    split_descend_finger_tree_
ops4attr_rightmost7echo
    check_ops4ascend_finger_tree_
    tmay_rightmost5ascend_finger_tree_
    split_ascend_finger_tree_
ops4attr_max7echo
    check_ops4maxheap_finger_tree_
    tmay_max5maxheap_finger_tree_
    split_maxheap_finger_tree_
ops4attr_min7echo
    check_ops4minheap_finger_tree_
    tmay_min5minheap_finger_tree_
    split_minheap_finger_tree_



mkr4check_ops4finger_tree_with_keys6autoT_
    check_ops4finger_tree_with_keys6auto_

    check_ops4sized_finger_tree_
    check_ops4descend_finger_tree_
    check_ops4ascend_finger_tree_
    check_ops4maxheap_finger_tree_
    check_ops4minheap_finger_tree_

mkr4get_attr5finger_tree_with_keys6autoT_
    get_attr5finger_tree_with_keys6auto_

    len5sized_finger_tree_
    tmay_leftmost5descend_finger_tree_
    tmay_rightmost5ascend_finger_tree_
    tmay_max5maxheap_finger_tree_
    tmay_min5minheap_finger_tree_

mkr4split_finger_tree_with_keys6autoT_
    split_finger_tree_with_keys6auto_

    split_sized_finger_tree_
    split_descend_finger_tree_
    split_ascend_finger_tree_
    split_maxheap_finger_tree_
    split_minheap_finger_tree_




rightmost
leftmost





default_Nothing
IFiller4PartialAuto__7keys6auto
    Filler4PartialAuto__7keys6auto__auto_is_RecordWithFutureSettleSlots

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
null_frozenset = frozenset()

#.from itertools import islice
from seed.tiny_.check import check_type_le, check_type_is, check_int_ge, check_non_ABC
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.data_funcs.finger_tree.ft23 import IOps4FingerTree, IBasicOps4FingerTree, IBaseOps4Auto6FingerTree
from seed.data_funcs.finger_tree.ft23 import mk_auto5chain_many_
from seed.data_funcs.finger_tree.ft23 import Wrapper4ft_tree, Visit4Wrapper4ft_xxx__7fill_part6auto, IFiller4PartialAuto
from seed.types.DefaultDict import DefaultDict2
import sys
_MODULUS = sys.hash_info.modulus
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.containers import mk_tuple, mk_tuple__split_first_if_str
    from seed.helper.repr_input import repr_helper
    from seed.debug.print_err import print_err
    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
    #    def _check6make_(sf, /):
    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import collect_tuple_subclasses_with_cached_property
    #assert not (__:=collect_tuple_subclasses_with_cached_property(globals(), to_print_err=True)), __
    from seed.types.FrozenDict import mk_FrozenDict
    from seed.tiny_.types5py import mk_MapView

    from seed.types.Record import mk_RecordType_
        #vs:
    from seed.types.RecordWithFutureSettleSlots import mk_RecordTypeWithFutureSettleSlots_
    #def mk_RecordTypeWithFutureSettleSlots_(__module__, __qualname__, _field_key_seq_, Nothing, /):

    #.from seed.data_funcs.finger_tree.ft23 import std_eval_seq_hash_size_pair5hash_size_pairs_

    from seed.seq_tools.find_sequent_indices import find_sequent_indices_
    from seed.types.CachedProperty import CachedProperty

    #from seed.helper.ifNone import ifNone,ifNonef
#from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
from seed.tiny_.funcs import box, echo#fst,snd
___end_mark_of_excluded_global_names__0___ = ...

__all__
def _mk_LeafType():
    Leaf = mk_named_pseudo_tuple_(__name__, 'Leaf', 'auto data')
    Leaf._depth_ = 0
    Leaf._is_leaf_ = True
    return Leaf

def _check6make_7NonLeaf_(sf, /):
    depth = sf._depth_
    _nodes = sf.nodes
    _check_nodes(2, 3, -1+depth, _nodes)
def _depth2NonLeaf_(depth, /):
    check_int_ge(1, depth)
    NonLeaf = mk_named_pseudo_tuple_(__name__, 'NonLeaf', 'auto nodes')
    NonLeaf._depth_ = depth
    NonLeaf._is_leaf_ = False
    NonLeaf._check6make_ = _check6make_7NonLeaf_
    return NonLeaf
_depth2NodeType = DefaultDict2({0:_mk_LeafType()}, 1, _depth2NonLeaf_)


def _check6make_7TwigX_(sf, /):
    depth = sf._depth_
    nodes = sf.nodes
    _check_nodes(1, 3, depth, nodes)
def _depth2TwigL_(depth, /):
    check_int_ge(0, depth)
    TwigL = mk_named_pseudo_tuple_(__name__, 'TwigL', 'auto nodes')
    TwigL._depth_ = depth
    TwigL._atL_vs_atR_ = False
    TwigL._check6make_ = _check6make_7TwigX_
    return TwigL
_depth2TwigLType = DefaultDict2({}, 1, _depth2TwigL_)

def _depth2TwigR_(depth, /):
    check_int_ge(0, depth)
    TwigR = mk_named_pseudo_tuple_(__name__, 'TwigR', 'auto nodes')
    TwigR._depth_ = depth
    TwigR._atL_vs_atR_ = True
    TwigR._check6make_ = _check6make_7TwigX_
    return TwigR
_depth2TwigRType = DefaultDict2({}, 1, _depth2TwigR_)

def _check6make_7Cane_(sf, /):
    depth = sf._depth_
    nodes = sf.nodes
    _check_nodes(0, 3, depth, nodes)
def _depth2Cane_(depth, /):
    check_int_ge(0, depth)
    Cane = mk_named_pseudo_tuple_(__name__, 'Cane', 'auto nodes')
    Cane._depth_ = depth
    Cane._is_fork_ = False
    Cane._check6make_ = _check6make_7Cane_
    return Cane
_depth2CaneType = DefaultDict2({}, 1, _depth2Cane_)

def _check6make_7Fork_(sf, /):
    depth = sf._depth_
    etree = sf.etree
    check_type_is(tuple, etree)
    assert len(etree) == 3
    (twigL, stem, twigR) = etree
    _check_twigL(depth, twigL)
    _check_twigR(depth, twigR)
    _check_tree(1+depth, stem)
def _depth2Fork_(depth, /):
    check_int_ge(0, depth)
    #Fork = mk_named_pseudo_tuple_(__name__, 'Fork', 'auto twigL stem twigR')
    Fork = mk_named_pseudo_tuple_(__name__, 'Fork', 'auto etree')
    Fork._depth_ = depth
    Fork._is_fork_ = True
    Fork._check6make_ = _check6make_7Fork_
    return Fork
_depth2ForkType = DefaultDict2({}, 1, _depth2Fork_)



__all__
class Ops4FingerTree(IOps4FingerTree):
    ___no_slots_ok___ = True
    def __init__(sf, ops4auto, /):
        check_type_le(IBaseOps4Auto6FingerTree, ops4auto)
        sf._ops = ops4auto
    #########
    @property
    def ops4auto(sf, /):
        return sf._ops
    #########
    @override
    def get_auto8null_(sf, /):
        '-> auto'
        return sf._ops.get_auto8null_()
    @override
    def mk_auto5chain_two_(sf, lhs_auto, rhs_auto, /):
        'auto -> auto -> auto #maybe noncommutable'
        return sf._ops.mk_auto5chain_two_(lhs_auto, rhs_auto)
    @override
    def mk_auto5data_(sf, data, /):
        'data -> auto'
        return sf._ops.mk_auto5data_(data)
    #########
    #:#########
    #:#@20260402
    #:@override
    #:def _get_emay_may_hash6auto_(sf, auto, /):
    #:    return sf._ops._get_emay_may_hash6auto_(auto)
    #:@override
    #:def _set_may_hash6auto_(sf, auto, may_hash, /):
    #:    return sf._ops._set_may_hash6auto_(auto, may_hash)
    #:@override
    #:def _get_may_size6auto_(sf, auto, /):
    #:    return sf._ops._get_may_size6auto_(auto)
    #:@override
    #:def eval_seq_hash_size_pair5hash_size_pairs_(sf, hash_size_pairs, /):
    #:    return sf._ops.eval_seq_hash_size_pair5hash_size_pairs_(hash_size_pairs)
    #:#########
    #########

    #########
    #@20260403
    @property
    @override
    def available_keys6auto(sf, /):
        '-> {key6auto}'
        return sf._ops.available_keys6auto
    @override
    def key_closure5key6auto_(sf, key6auto, /):
        'key6auto -> [key6auto] | ^KeyError'
        return sf._ops.key_closure5key6auto_(key6auto)
    @override
    def tmay_property5auto_and_key6auto_(sf, auto, key6auto, /):
        'auto -> key6auto -> tmay property6auto | ^KeyError # {() => lazy; (property6auto,)=>settled; ^KeyError=>illegal key}'
        return sf._ops.tmay_property5auto_and_key6auto_(auto, key6auto)
    @override
    def property5wrapper4ft_xxx_and_key6auto_(sf, wrapper4ft_xxx, key6auto, /):
        'IWrapper4ft_xxx -> key6auto -> property6auto | ^KeyError'
        #resolve and settle lazy attr
        wrapper4ft_xxx.ops4ft # >= sf
        return sf._ops.property5wrapper4ft_xxx_and_key6auto_(wrapper4ft_xxx, key6auto)
    #########

    #########
    @override
    def _mk_node7leaf_(sf, auto, data, /):
        'auto -> data -> leaf/node{depth==0}'
        return _depth2NodeType[depth:=0](auto, data=data)
    @override
    def _mk_node7nonleaf_(sf, depth, auto, _nodes, /):
        'depth/uint{>0} -> auto -> [node{-1+depth}]{2<=len<=3} -> node{depth>0}'
        assert depth > 0
        _nodes = mk_tuple(_nodes)
        return _depth2NodeType[depth](auto, nodes=_nodes)
    @override
    def _mk_twigL_(sf, depth, auto, nodes, /):
        'depth/uint -> auto -> [node{depth}]{1<=len<=3} -> twigL{depth}'
        nodes = mk_tuple(nodes)
        return _depth2TwigLType[depth](auto, nodes)
    @override
    def _mk_twigR_(sf, depth, auto, nodes, /):
        'depth/uint -> auto -> [node{depth}]{1<=len<=3} -> twigR{depth}'
        nodes = mk_tuple(nodes)
        return _depth2TwigRType[depth](auto, nodes)
    @override
    def _mk_tree7fork_(sf, depth, auto, etree, /):
        'depth/uint -> auto -> etree/(twigL{depth}, stem{depth}/finger_tree{1+depth}, twigR{depth}) -> fork{depth}/finger_tree{depth}'
        etree = mk_tuple(etree)
        return _depth2ForkType[depth](auto, etree)
    @override
    def _mk_tree7cane_(sf, depth, auto, nodes, /):
        'depth/uint -> auto -> [node{depth}]{0<=len<=3} -> cane{depth}/finger_tree{depth}'
        nodes = mk_tuple(nodes)
        return _depth2CaneType[depth](auto, nodes)

    #########
    @override
    def is_fork_tree_(sf, depth, tree, /):
        'depth/uint -> finger_tree{depth} -> bool/(cane_vs_fork)'
        _check_tree(depth, tree)
        return tree._is_fork_
    #########
    @override
    def get_auto5node_(sf, depth, node, /):
        'depth/uint -> node{depth} -> auto #(leaf|nonleaf)'
        _check_node(depth, node)
        return node.auto
    @override
    def get_auto5twigL_(sf, depth, twigL, /):
        'depth/uint -> twigL{depth} -> auto'
        _check_twigL(depth, twigL)
        return twigL.auto
    @override
    def get_auto5twigR_(sf, depth, twigR, /):
        'depth/uint -> twigR{depth} -> auto'
        _check_twigR(depth, twigR)
        return twigR.auto
    #########
    @override
    def get_auto5tree_(sf, depth, tree, /):
        'depth/uint -> finger_tree{depth} -> auto # (fork|cane)'
        _check_tree(depth, tree)
        return tree.auto

    #########
    @override
    def get_data5leaf_(sf, leaf, /):
        'leaf -> data'
        _check_leaf(leaf)
        return leaf.data
    @override
    def get_nodes5nonleaf_(sf, depth, nonleaf, /):
        'depth/uint{>0} -> nonleaf/node{depth} -> [node{-1+depth}]'
        _check_nonleaf(depth, nonleaf)
        return nonleaf.nodes
    @override
    def get_nodes5cane_(sf, depth, cane, /):
        'depth/uint -> cane{depth} -> [node{depth}]'
        _check_cane(depth, cane)
        return cane.nodes
    @override
    def get_nodes5twigL_(sf, depth, twigL, /):
        'depth/uint -> twigL{depth} -> [node{depth}]'
        _check_twigL(depth, twigL)
        return twigL.nodes
    @override
    def get_nodes5twigR_(sf, depth, twigR, /):
        'depth/uint -> twigR{depth} -> [node{depth}]'
        _check_twigR(depth, twigR)
        return twigR.nodes
    @override
    def get_etree5fork_(sf, depth, fork, /):
        'depth/uint -> fork{depth} -> etree{depth}'
        _check_fork(depth, fork)
        return fork.etree
    @override
    def get_stem5fork_(sf, depth, fork, /):
        'depth/uint -> fork{depth} -> stem{depth}/finger_tree{1+depth}'
        _check_fork(depth, fork)
        return fork.etree[1]
    @override
    def get_twigL5fork_(sf, depth, fork, /):
        'depth/uint -> fork{depth} -> twigL{depth}'
        _check_fork(depth, fork)
        return fork.etree[0]
    @override
    def get_twigR5fork_(sf, depth, fork, /):
        'depth/uint -> fork{depth} -> twigR{depth}'
        _check_fork(depth, fork)
        return fork.etree[2]
    #########
check_non_ABC(Ops4FingerTree)

def _check_leaf(leaf, /):
    assert leaf._depth_ == 0
    assert leaf._is_leaf_
def _check_nonleaf(depth, nonleaf, /):
    assert nonleaf._depth_ == depth
    assert not nonleaf._is_leaf_
def _check_node(depth, node, /):
    node._is_leaf_
def _check_nodes(min_sz, max_sz, depth, nodes, /):
    check_type_is(tuple, nodes)
    assert min_sz <= len(nodes) <= max_sz
    for node in nodes:
        _check_node(depth, node)
def _check_twigL(depth, twigL, /):
    assert twigL._depth_ == depth
    assert not twigL._atL_vs_atR_
def _check_twigR(depth, twigR, /):
    assert twigR._depth_ == depth
    assert twigR._atL_vs_atR_
def _check_fork(depth, fork, /):
    assert fork._depth_ == depth
    assert fork._is_fork_
def _check_cane(depth, cane, /):
    assert cane._depth_ == depth
    assert not cane._is_fork_
def _check_tree(depth, tree, /):
    assert tree._depth_ == depth
    tree._is_fork_


__all__
default_Nothing = object()
class Ops4Auto6FingerTree(IBaseOps4Auto6FingerTree):
    '[auto :: mapping_view]'
    ___no_slots_ok___ = True
    def __init__(sf, seq4ops4attr4auto, Nothing=default_Nothing, seq4ops4lazy_attr4auto=(), /):
        '[IOps4Attr4Auto6FingerTree] -> None'
        #TODO:++Nothing,seq4ops4lazy_attr4auto/num_lazy_attrs:@20260402
        #   lazy_part:seq4ops4attr4auto[len()-num_lazy_attrs:]
        #   mk_RecordTypeWithFutureSettleSlots_
        if Nothing is None:raise TypeError

        seq4ops4attr4auto = mk_tuple(seq4ops4attr4auto)
        seq4ops4lazy_attr4auto = mk_tuple(seq4ops4lazy_attr4auto)
        j2ops7all = seq4ops4attr4auto + seq4ops4lazy_attr4auto
        for ops4attr4auto in j2ops7all:
            check_type_le(IOps4Attr4Auto6FingerTree, ops4attr4auto)

        #_field_key_seq_ = j2k
        #_field_key2seq_idx_ = k2j


        #.k2j = {ops4attr4auto.key6auto:j for j, ops4attr4auto in enumerate(seq4ops4attr4auto)}
        #.if not len(k2j) == len(seq4ops4attr4auto):raise Exception('duplicated key')
        #.sf._j2ops7strict = seq4ops4attr4auto
        #.sf._k2j = k2j
        ###news:
        num_strict_attrs = len(seq4ops4attr4auto)
        num_lazy_attrs = len(seq4ops4lazy_attr4auto)

        j2k = [ops4attr4auto.key6auto for ops4attr4auto in j2ops7all]
        strict = 0 == num_lazy_attrs
        if strict:
            Auto = mk_RecordType_(__name__, 'Auto', j2k)
        else:
            Auto = mk_RecordTypeWithFutureSettleSlots_(__name__, 'Auto', j2k, Nothing)
        Auto
        777;del j2k
        k2j = Auto._field_key2seq_idx_
        j2k = Auto._field_key_seq_

        for j, ops4attr4auto in enumerate(j2ops7all):
            for k in ops4attr4auto.using_keys6auto:
                if not k2j[k] < j:raise ValueError(j2ops7all, ops4attr4auto, k, (j, k2j[k]))

        j2ks = []
        for j, ops4attr4auto in enumerate(j2ops7all):
            ks4j = {ops4attr4auto.key6auto}
            for k in ops4attr4auto.using_keys6auto:
                _ks = j2ks[k2j[k]]
                ks4j |= _ks
            j2ks.append(ks4j)
        j2js = [sorted(k2j[k] for k in ks) for ks in j2ks]
        j2js = tuple(map(tuple, j2js))
        k2ks = {j2k[j]:tuple(j2k[j] for j in js) for j, js in enumerate(j2js)}
        k2ks = mk_MapView(k2ks)

        sf._Auto = Auto
        sf._j2ops7all = j2ops7all
        sf._j2ops7strict = seq4ops4attr4auto
        sf._k2j = k2j
        sf._sz0 = num_strict_attrs
        sf._sz1 = num_lazy_attrs
        sf._strict = strict
        sf._no = Nothing
        sf._j2js = j2js
        sf._k2ks = k2ks
    #########

    #########
    #@20260403
    @property
    @override
    def available_keys6auto(sf, /):
        '-> {key6auto}'
        return sf._k2j.keys()
    @override
    def key_closure5key6auto_(sf, key6auto, /):
        'key6auto -> [key6auto] | ^KeyError'
        return sf._k2ks[key6auto]
    @override
    def tmay_property5auto_and_key6auto_(sf, auto, key6auto, /):
        'auto -> key6auto -> tmay property6auto | ^KeyError # {() => lazy; (property6auto,)=>settled; ^KeyError=>illegal key}'
        _check_key6auto(key6auto)
        x = auto[key6auto]
            # ^KeyError
        if not sf._strict:
            Nothing = sf._no
            if Nothing is x:
                return ()
        return (x,)
    @override
    def property5wrapper4ft_xxx_and_key6auto_(sf, wrapper4ft_xxx, key6auto, /):
        'IWrapper4ft_xxx -> key6auto -> property6auto | ^KeyError'
        #resolve and settle lazy attr
        wrapper4ft_xxx.ops4ft # >= sf
        auto = wrapper4ft_xxx.auto
        #########
        tm = sf.tmay_property5auto_and_key6auto_(auto, key6auto)
        if tm:
            [x] = tm
            return x
        #########
        ks = sf.key_closure5key6auto_(key6auto)
        assert ks[-1] == key6auto
        #_ks = [k for k in ks if not sf.tmay_property5auto_and_key6auto_(auto, k)]
        keys6auto7filling = ks #closure
        #bug:{not closure}:keys6auto7filling = _ks
        #_js = find_sequent_indices_(keys6auto7filling, ks)

        j2ops7all = sf._j2ops7all
        k2j = sf._k2j
        js = [k2j[k] for k in keys6auto7filling]
        seq4ops4attr4auto7filling = tuple(j2ops7all[k2j[k]] for k in keys6auto7filling)
        #IFiller4PartialAuto
        filler = Filler4PartialAuto__7keys6auto__auto_is_RecordWithFutureSettleSlots(ops4auto:=sf, seq4ops4attr4auto7filling)
        visitor = Visit4Wrapper4ft_xxx__7fill_part6auto(filler)
        visitor.visit_wrapper4ft_xxx_(wrapper4ft_xxx)
        #########
        tm = sf.tmay_property5auto_and_key6auto_(auto, key6auto)
        if tm:
            [x] = tm
            return x
        raise 000
        #########
        raise NotImplementedError
    #########


    #########
    def _mk_auto5strict_part_(sf, strict_part, /):
        '-> auto'
        len(strict_part)
        Auto = sf._Auto
        if not sf._strict:
            Nothing = Auto.Nothing#sf._no
            if any(v is Nothing for v in strict_part):raise TypeError(strict_part)
        return Auto(*strict_part)
    #########
    @override
    def get_auto8null_(sf, /):
        '-> auto'
        d = {}
        ls = []
        mapping_view8partial_auto = mk_MapView(d)
        seq4ops4attr4auto = sf._j2ops7strict
        for ops4attr4auto in seq4ops4attr4auto:
            k = ops4attr4auto.key6auto
            v = ops4attr4auto.mk_property6auto8null_(mapping_view8partial_auto)
            d[k] = v
            ls.append(v)
        d
        ls
        #.auto = mk_FrozenDict(d)
        #.auto = sf._Auto(*ls)
            #.from_iterable(ls)#.from_mapping(d)
        auto = sf._mk_auto5strict_part_(ls)
        return auto
    @override
    def mk_auto5chain_two_(sf, lhs_auto, rhs_auto, /):
        'auto -> auto -> auto #maybe noncommutable'
        d = {}
        ls = []
        mapping_view8partial_auto = mk_MapView(d)
        seq4ops4attr4auto = sf._j2ops7strict
        for ops4attr4auto in seq4ops4attr4auto:
            k = ops4attr4auto.key6auto
            v = ops4attr4auto.mk_property6auto5chain_two_(lhs_auto, rhs_auto, lhs_auto[k], rhs_auto[k], mapping_view8partial_auto)
            d[k] = v
            ls.append(v)
        d
        ls
        if sf._strict:
            assert len(lhs_auto) == len(d)
            assert len(rhs_auto) == len(d)
        #.auto = mk_FrozenDict(d)
        #.auto = sf._Auto(*ls)
        auto = sf._mk_auto5strict_part_(ls)
        return auto
    @override
    def mk_auto5data_(sf, data, /):
        'data -> auto'
        d = {}
        ls = []
        mapping_view8partial_auto = mk_MapView(d)
        seq4ops4attr4auto = sf._j2ops7strict
        for ops4attr4auto in seq4ops4attr4auto:
            k = ops4attr4auto.key6auto
            v = ops4attr4auto.mk_property6auto5data_(data, mapping_view8partial_auto)
            d[k] = v
            ls.append(v)
        d
        ls
        #.auto = mk_FrozenDict(d)
        #.auto = sf._Auto(*ls)
        auto = sf._mk_auto5strict_part_(ls)
        return auto
    #########
    #:#########
    #:#@20260402
    #:@override
    #:def _get_emay_may_hash6auto_(sf, auto, /):
    #:    return None#unsupport lazy-hash yet
    #:@override
    #:def _set_may_hash6auto_(sf, auto, may_hash, /):
    #:    raise 000
    #:    raise TypeError
    #:    raise NotImplementedError
    #:@override
    #:def _get_may_size6auto_(sf, auto, /):
    #:    raise 000
    #:@override
    #:def eval_seq_hash_size_pair5hash_size_pairs_(sf, hash_size_pairs, /):
    #:    return std_eval_seq_hash_size_pair5hash_size_pairs_(hash_size_pairs)
    #:#########
    #########
check_non_ABC(Ops4Auto6FingerTree)

_Ts = (int, slice)
def _check_key6auto(key6auto, /):
    # !! RecordWithFutureSettleSlots
    if type(key6auto) in _Ts:raise TypeError

#.def _settle7lazy_attr(ops4finger_tree, depth, finger_tree, key6auto, /):
#.    #TODO
#.    Visit4Wrapper4ft_xxx__7fill_part6auto
#.    IFiller4PartialAuto
#.    #TODO:++get_value5key_(ops4finger_tree, wrapper4ft_xxx, key6auto)->value{settle lazy...} @(IBaseOps4Auto6FingerTree&&IOps4FingerTree)
#.    raise NotImplementedError

#################################
class IFiller4PartialAuto__7keys6auto(IFiller4PartialAuto):
    __slots__ = ()
    @property
    @abstractmethod
    def seq4ops4attr4auto7filling(sf, /):
        '-> [IOps4Attr4Auto6FingerTree] # ordered, closure'
        #bug:'-> [ft23_7types.IOps4Attr4Auto6FingerTree] # ordered, closure-strict_part, missing_part{target-wrapper4ft_xxx}'

    @abstractmethod
    def tmay_property5auto_and_key6auto_(sf, auto, key6auto, /):
        'auto -> key6auto -> tmay property6auto | ^KeyError # {() => lazy; (property6auto,)=>settled; ^KeyError=>illegal key}'
    @abstractmethod
    def _set_new6key6auto_(sf, auto, key6auto, property6auto, /):
        '[key6auto not in auto] => auto -> key6auto -> property6auto -> None'

    #########
    @CachedProperty
    def keys6auto7filling(sf, /):
        '-> [key6auto] # ~ seq4ops4attr4auto7filling'
        return tuple(ops4attr4auto.key6auto for ops4attr4auto in sf.seq4ops4attr4auto7filling)
    #########
    @override
    def get_tmay_part6auto_(sf, auto, /):
        'auto -> tmay part4auto'
        d = {}# ls = []
        for key6auto in sf.keys6auto7filling:
            tm = sf.tmay_property5auto_and_key6auto_(auto, key6auto)
            if not tm:return ()
            [property6auto] = tm
            d[key6auto] = property6auto
            #ls.append(property6auto)
        part4auto = mk_MapView(d)
        return (part4auto,)
    @override
    def _setdefault_part6auto_(sf, auto, part4auto, /):
        'auto -> part4auto -> None'
        # property6auto must match if exist
        for key6auto in sf.keys6auto7filling:
            property6auto = part4auto[key6auto]
            tm = sf.tmay_property5auto_and_key6auto_(auto, key6auto)
            if not tm:
                sf._set_new6key6auto_(auto, key6auto, property6auto)
            else:
                [_property6auto] = tm
                if not property6auto in tm:raise Exception(auto, part4auto, key6auto, (_property6auto, property6auto))
    @override
    def eq_part4auto_(sf, lhs_part4auto, rhs_part4auto, /):
        'part4auto -> part4auto -> bool'
        return lhs_part4auto == rhs_part4auto
        return dict(lhs_part4auto) == dict(rhs_part4auto)
    #IBaseOps4Auto6FingerTree
    @override
    def get_null_part4auto_(sf, /):
        '-> part4auto'
        return sf._null_part4auto
    @CachedProperty
    def _null_part4auto(sf, /):
        '-> part4auto'
        d = {}
        mapping_view8partial_auto = mk_MapView(d)
        for ops4attr4auto in sf.seq4ops4attr4auto7filling:
            key6auto = ops4attr4auto.key6auto
            property6auto = ops4attr4auto.mk_property6auto8null_(mapping_view8partial_auto)
            d[key6auto] = property6auto
        part4auto = mk_MapView(d)
        return part4auto
    @override
    def mk_part4auto5data_(sf, data, auto, /):
        'data -> auto -> part4auto'
        d = {}
        mapping_view8partial_auto = mk_MapView(d)
        for ops4attr4auto in sf.seq4ops4attr4auto7filling:
            key6auto = ops4attr4auto.key6auto
            tm = sf.tmay_property5auto_and_key6auto_(auto, key6auto)
            if tm:
                [property6auto] = tm
            else:
                property6auto = ops4attr4auto.mk_property6auto5data_(data, mapping_view8partial_auto)
            property6auto

            d[key6auto] = property6auto
        part4auto = mk_MapView(d)
        return part4auto
    @override
    def chain_two_parts4auto_(sf, lhs_part4auto, rhs_part4auto, /):
        'part4auto -> part4auto -> part4auto'
        lhs_auto = lhs_part4auto
        rhs_auto = rhs_part4auto

        d = {}
        mapping_view8partial_auto = mk_MapView(d)
        tm = () #has no:auto
        for ops4attr4auto in sf.seq4ops4attr4auto7filling:
            key6auto = ops4attr4auto.key6auto
            #tm = sf.tmay_property5auto_and_key6auto_(auto, key6auto)
            if tm:
                [property6auto] = tm
            else:
                lhs_property6auto = lhs_part4auto[key6auto]
                rhs_property6auto = rhs_part4auto[key6auto]
                property6auto = ops4attr4auto.mk_property6auto5chain_two_(lhs_auto, rhs_auto, lhs_property6auto, rhs_property6auto, mapping_view8partial_auto)
            property6auto

            d[key6auto] = property6auto
        part4auto = mk_MapView(d)
        return part4auto

#################################
class Filler4PartialAuto__7keys6auto__auto_is_RecordWithFutureSettleSlots(IFiller4PartialAuto__7keys6auto):
    'required:[auto :: RecordWithFutureSettleSlots]'
    ___no_slots_ok___ = True
    def __init__(sf, ops4auto, seq4ops4attr4auto7filling, /):
        ops4auto.tmay_property5auto_and_key6auto_
        seq4ops4attr4auto7filling = mk_tuple(seq4ops4attr4auto7filling)
        sf._ops4auto = ops4auto
        sf._seq4ops = seq4ops4attr4auto7filling
    @property
    @override
    def seq4ops4attr4auto7filling(sf, /):
        return sf._seq4ops

    @property
    @override
    def tmay_property5auto_and_key6auto_(sf, /):
        #def tmay_property5auto_and_key6auto_(sf, auto, key6auto, /):
        return sf._ops4auto.tmay_property5auto_and_key6auto_
    @override
    def _set_new6key6auto_(sf, auto, key6auto, property6auto, /):
        Auto = type(auto)
        Nothing = Auto.Nothing
        auto[Nothing:key6auto] = property6auto
            #=> required:[auto :: RecordWithFutureSettleSlots]


#################################




class IOps4Attr4Auto6FingerTree(ABC):
    'ops4attr4auto:[auto :: {key6auto:property6auto}]'
    __slots__ = ()
    #########
    @property
    @abstractmethod
    def key6auto(sf, /):
        '-> key6auto'
    @property
    @abstractmethod
    def using_keys6auto(sf, /):
        '-> {key6auto}'
    @abstractmethod
    def mk_property6auto8null_(sf, mapping_view8partial_auto, /):
        '{key6auto:property6auto} -> property6auto{sf.key6auto}'
    @abstractmethod
    def mk_property6auto5chain_two_(sf, lhs_auto, rhs_auto, lhs_property6auto, rhs_property6auto, mapping_view8partial_auto, /):
        'MapView{auto} -> MapView{auto} -> {key6auto:property6auto} -> property6auto{sf.key6auto} -> property6auto{sf.key6auto} -> property6auto{sf.key6auto} #maybe noncommutable'
    @abstractmethod
    def mk_property6auto5data_(sf, data, mapping_view8partial_auto, /):
        'data -> {key6auto:property6auto} -> property6auto{sf.key6auto}'
    #########

class Ops4Attr4Auto6FingerTree__sized(IOps4Attr4Auto6FingerTree):
    ___no_slots_ok___ = True
    #########
    #@override
    key6auto = 'len'
    #@override
    using_keys6auto = null_frozenset

    @override
    def mk_property6auto8null_(sf, mapping_view8partial_auto, /):
        return 0
    @override
    def mk_property6auto5chain_two_(sf, lhs_auto, rhs_auto, lhs_property6auto, rhs_property6auto, mapping_view8partial_auto, /):
        return lhs_property6auto + rhs_property6auto
    @override
    def mk_property6auto5data_(sf, data, mapping_view8partial_auto, /):
        return 1
    #########
check_non_ABC(Ops4Attr4Auto6FingerTree__sized)
ops4attr_len = Ops4Attr4Auto6FingerTree__sized()




class Ops4Attr4Auto6FingerTree__hash(IOps4Attr4Auto6FingerTree):
    'required:[ops4attr_len before ops4attr_hash]'
    ___no_slots_ok___ = True
    #########
    #@override
    key6auto = 'hash'
    #@override
    using_keys6auto = frozenset(['len'])

    @override
    def mk_property6auto8null_(sf, mapping_view8partial_auto, /):
        return 0
    @override
    def mk_property6auto5chain_two_(sf, lhs_auto, rhs_auto, lhs_property6auto, rhs_property6auto, mapping_view8partial_auto, /):
        rhs_sz = rhs_auto['len']
        return (lhs_property6auto*pow(5, rhs_sz, _MODULUS)  +  rhs_property6auto) %_MODULUS
    @override
    def mk_property6auto5data_(sf, data, mapping_view8partial_auto, /):
        return hash(data) %_MODULUS
    #########
check_non_ABC(Ops4Attr4Auto6FingerTree__hash)
ops4attr_hash = Ops4Attr4Auto6FingerTree__hash()


class Ops4Attr4Auto6FingerTree__may_hash(IOps4Attr4Auto6FingerTree):
    'required:[ops4attr_len before ops4attr_may_hash]'
    ___no_slots_ok___ = True
    #########
    #@override
    key6auto = 'may_hash'
    #@override
    using_keys6auto = frozenset(['len'])

    @override
    def mk_property6auto8null_(sf, mapping_view8partial_auto, /):
        return 0
    @override
    def mk_property6auto5chain_two_(sf, lhs_auto, rhs_auto, lhs_property6auto, rhs_property6auto, mapping_view8partial_auto, /):
        if None is lhs_property6auto:return None
        if None is rhs_property6auto:return None
        rhs_sz = rhs_auto['len']
        return (lhs_property6auto*pow(5, rhs_sz, _MODULUS)  +  rhs_property6auto) %_MODULUS
    @override
    def mk_property6auto5data_(sf, data, mapping_view8partial_auto, /):
        try:
            return hash(data) %_MODULUS
        except TypeError:
            return None
    #########
check_non_ABC(Ops4Attr4Auto6FingerTree__may_hash)
ops4attr_may_hash = Ops4Attr4Auto6FingerTree__may_hash()





class IOps4Attr4Auto6FingerTree__ord_key(IOps4Attr4Auto6FingerTree):
    __slots__ = ()
    #########
    @property
    @abstractmethod
    def key_func(sf, /):
        '-> (data -> ord_key)'
    @property
    @abstractmethod
    def selector(sf, /):
        '-> (ord_key -> ord_key)'


    @override
    def mk_property6auto8null_(sf, mapping_view8partial_auto, /):
        return ()
    @override
    def mk_property6auto5chain_two_(sf, lhs_auto, rhs_auto, lhs_property6auto, rhs_property6auto, mapping_view8partial_auto, /):
        if not lhs_property6auto:
            return rhs_property6auto
        if not rhs_property6auto:
            return lhs_property6auto
        try:
            [lhs_ord_key] = lhs_property6auto
            [rhs_ord_key] = rhs_property6auto
        except TypeError as exc:
            raise TypeError(exc, sf.key6auto)
        ord_key = sf.selector(lhs_ord_key, rhs_ord_key)
        return (ord_key,)
    @override
    def mk_property6auto5data_(sf, data, mapping_view8partial_auto, /):
        ord_key = sf.key_func(data)
        return (ord_key,)
    #########

class IOps4Attr4Auto6FingerTree__mixin__init_key_func(IOps4Attr4Auto6FingerTree__ord_key):
    ___no_slots_ok___ = True
    def __init__(sf, key_func, /):
        sf._kf = key_func
    @property
    @override
    def key_func(sf, /):
        '-> (data -> ord_key)'
        return sf._kf







class IOps4Attr4Auto6FingerTree__max(IOps4Attr4Auto6FingerTree__ord_key):
    'max_heap'
    __slots__ = ()
    #@override
    key6auto = 'max'
    #@override
    using_keys6auto = null_frozenset
    #@override
    selector = staticmethod(max)
class Ops4Attr4Auto6FingerTree__max(IOps4Attr4Auto6FingerTree__max, IOps4Attr4Auto6FingerTree__mixin__init_key_func):pass
check_non_ABC(Ops4Attr4Auto6FingerTree__max)





class IOps4Attr4Auto6FingerTree__min(IOps4Attr4Auto6FingerTree__ord_key):
    'min_heap'
    __slots__ = ()
    #@override
    key6auto = 'min'
    #@override
    using_keys6auto = null_frozenset
    #@override
    selector = staticmethod(min)
class Ops4Attr4Auto6FingerTree__min(IOps4Attr4Auto6FingerTree__min, IOps4Attr4Auto6FingerTree__mixin__init_key_func):pass
check_non_ABC(Ops4Attr4Auto6FingerTree__min)



def rightmost(a, b, /):
    return b
def leftmost(a, b, /):
    return a
class IOps4Attr4Auto6FingerTree__leftmost(IOps4Attr4Auto6FingerTree__ord_key):
    'descend_set'
    __slots__ = ()
    #@override
    key6auto = 'leftmost'
    #@override
    using_keys6auto = null_frozenset
    #@override
    selector = staticmethod(leftmost)
class Ops4Attr4Auto6FingerTree__leftmost(IOps4Attr4Auto6FingerTree__leftmost, IOps4Attr4Auto6FingerTree__mixin__init_key_func):pass
check_non_ABC(Ops4Attr4Auto6FingerTree__leftmost)

class IOps4Attr4Auto6FingerTree__rightmost(IOps4Attr4Auto6FingerTree__ord_key):
    'ascend_set'
    __slots__ = ()
    #@override
    key6auto = 'rightmost'
    #@override
    using_keys6auto = null_frozenset
    #@override
    selector = staticmethod(rightmost)
class Ops4Attr4Auto6FingerTree__rightmost(IOps4Attr4Auto6FingerTree__rightmost, IOps4Attr4Auto6FingerTree__mixin__init_key_func):pass
check_non_ABC(Ops4Attr4Auto6FingerTree__rightmost)

ops4attr_rightmost7echo = Ops4Attr4Auto6FingerTree__rightmost(echo)
    #ascend_set
ops4attr_leftmost7echo = Ops4Attr4Auto6FingerTree__leftmost(echo)
    #descend_set
        #obsolete『!! useless{curr impl has yet no split search from right to left}』
        #   !! now has:.split_tree__max_treeX__offset_
ops4attr_min7echo = Ops4Attr4Auto6FingerTree__min(echo)
    #min_heap
ops4attr_max7echo = Ops4Attr4Auto6FingerTree__max(echo)
    #max_heap






def check_ops4finger_tree_with_keys6auto_(ops4finger_tree, keys6auto, /, *, _no_check=False):
    check_type_is(Ops4FingerTree, ops4finger_tree)
    if _no_check: return
    ops4auto = ops4finger_tree.ops4auto
    check_type_is(Ops4Auto6FingerTree, ops4auto)
    for k in keys6auto:
        if not k in ops4auto.available_keys6auto:raise TypeError(k)
def mkr4check_ops4finger_tree_with_keys6autoT_(keys6auto, /):
    keys6auto = mk_tuple__split_first_if_str(keys6auto)
    def check_ops4finger_tree_with_keys6auto_(ops4finger_tree, /, *, _no_check=False):
        check_ops4finger_tree_with_keys6auto_(ops4finger_tree, keys6auto, _no_check=_no_check)
    return check_ops4finger_tree_with_keys6auto_
#.def check_ops4sized_finger_tree_(ops4sized_finger_tree, /, *, _no_check=False):
#.    check_ops4finger_tree_with_keys6auto_(ops4finger_tree, 'len', _no_check=_no_check)
check_ops4sized_finger_tree_ = mkr4check_ops4finger_tree_with_keys6autoT_('len')
check_ops4hashable_finger_tree_ = mkr4check_ops4finger_tree_with_keys6autoT_('hash')
check_ops4mhashable_finger_tree_ = mkr4check_ops4finger_tree_with_keys6autoT_('may_hash')
check_ops4descend_finger_tree_ = mkr4check_ops4finger_tree_with_keys6autoT_('leftmost')
check_ops4ascend_finger_tree_ = mkr4check_ops4finger_tree_with_keys6autoT_('rightmost')
check_ops4maxheap_finger_tree_ = mkr4check_ops4finger_tree_with_keys6autoT_('max')
check_ops4minheap_finger_tree_ = mkr4check_ops4finger_tree_with_keys6autoT_('min')









def mkr4get_attr5finger_tree_with_keys6autoT_(key6auto, /, *, is_lazy_attr:bool):
    check_type_is(bool, is_lazy_attr)
    keys6auto = (key6auto,)
    def get_attr5finger_tree_with_keys6auto_(ops4finger_tree, depth, finger_tree, /, *, _no_check=False):
        '-> attr6auto{key6auto}'
        check_ops4finger_tree_with_keys6auto_(ops4finger_tree, keys6auto, _no_check=_no_check)
        sf = ops4finger_tree
        auto = sf.get_auto5tree_(depth, finger_tree)
        if not is_lazy_attr:
            return auto[key6auto]
        #ops4ft = ops4finger_tree
        wrapper4ft_xxx = Wrapper4ft_tree(ops4finger_tree, depth, finger_tree)
        return ops4finger_tree.property5wrapper4ft_xxx_and_key6auto_(wrapper4ft_xxx, key6auto)
        #.#lazy_v = fxxx(ops4finger_tree, depth, finger_tree, key6auto)
        #.#return auto[key6auto:'lazy':lazy_v]
        #.x = auto[key6auto]
        #.if not x is type(auto.Nothing):
        #.    return x
        #._settle7lazy_attr(ops4finger_tree, depth, finger_tree, key6auto)
        #.y = auto[key6auto]
        #.if y is x:raise 000
        #.return y
    return get_attr5finger_tree_with_keys6auto_
def get_attr5finger_tree_with_keys6auto_(ops4finger_tree, depth, key6auto, finger_tree, /, *, is_lazy_attr:bool, _no_check=False):
    '-> attr6auto{key6auto}'
    return mkr4get_attr5finger_tree_with_keys6autoT_(key6auto, is_lazy_attr=is_lazy_attr)(ops4finger_tree, depth, finger_tree, _no_check=_no_check)

def mkr4split_finger_tree_with_keys6autoT_(key6auto, /, *, attr2tmay_):
    #attr5finger_tree_ = mkr4get_attr5finger_tree_with_keys6autoT_(key6auto)
    keys6auto = (key6auto,)
    #force_lazy_imported_func_(echo)
    #force_lazy_imported_func_(box)
    attr2tmay_ = attr2tmay_ if not attr2tmay_ is None else box
    def split_finger_tree_with_keys6auto_(ops4finger_tree, depth, max_key4treeL, finger_tree, /, *, _no_check=False, key=None):
        '-> (treeL, treeR)'
        check_ops4finger_tree_with_keys6auto_(ops4finger_tree, keys6auto, _no_check=_no_check)
        key1_ = key if not key is None else echo
        777;del key
        sf = ops4finger_tree
        def auto2whether_treeL_(auto, /):
            tmay_attr = attr2tmay_(auto[key6auto])
            match tmay_attr:
                case [attr]:
                    return key1_(attr) <= max_key4treeL
                case []:
                    # attr is -oo
                    return True
                case _:
                    raise TypeError(tmay_attr)
                #case
            raise 000
        (treeL, autoM, treeR) = sf.split_tree__max_treeL_(depth, auto2whether_treeL_, finger_tree, known_begin_ok=False, known_end_not_ok=False)
        return (treeL, treeR)
    return split_finger_tree_with_keys6auto_
def split_finger_tree_with_keys6auto_(ops4finger_tree, depth, key6auto, max_key4treeL, finger_tree, /, *, attr2tmay_, _no_check=False, key=None):
    return mkr4split_finger_tree_with_keys6autoT_(key6auto)(ops4finger_tree, depth, max_key4treeL, finger_tree, _no_check=_no_check, key=key, attr2tmay_=attr2tmay_)



hash5hashable_finger_tree_ = mkr4get_attr5finger_tree_with_keys6autoT_('hash', is_lazy_attr=False)
may_hash5mhashable_finger_tree_ = mkr4get_attr5finger_tree_with_keys6autoT_('may_hash', is_lazy_attr=True)


split_sized_finger_tree_ = mkr4split_finger_tree_with_keys6autoT_('len', attr2tmay_=box)
len5sized_finger_tree_ = mkr4get_attr5finger_tree_with_keys6autoT_('len', is_lazy_attr=False)

tmay_leftmost5descend_finger_tree_ = mkr4get_attr5finger_tree_with_keys6autoT_('leftmost', is_lazy_attr=False)
split_descend_finger_tree_ = mkr4split_finger_tree_with_keys6autoT_('leftmost', attr2tmay_=echo)

tmay_rightmost5ascend_finger_tree_ = mkr4get_attr5finger_tree_with_keys6autoT_('rightmost', is_lazy_attr=False)
split_ascend_finger_tree_ = mkr4split_finger_tree_with_keys6autoT_('rightmost', attr2tmay_=echo)
    #split_ascend_finger_tree_ = mkr4split_finger_tree_with_keys6autoT_('rightmost', attr2tmay_=force_lazy_imported_func_(echo))

tmay_max5maxheap_finger_tree_ = mkr4get_attr5finger_tree_with_keys6autoT_('max', is_lazy_attr=False)
split_maxheap_finger_tree_ = mkr4split_finger_tree_with_keys6autoT_('max', attr2tmay_=echo)

tmay_min5minheap_finger_tree_ = mkr4get_attr5finger_tree_with_keys6autoT_('min', is_lazy_attr=False)
split_minheap_finger_tree_ = mkr4split_finger_tree_with_keys6autoT_('min', attr2tmay_=echo)

r'''[[[
def len5sized_finger_tree_(ops4sized_finger_tree, depth, sized_finger_tree, /, *, _no_check=False):
    check_ops4sized_finger_tree_(ops4sized_finger_tree, _no_check=_no_check)
    sf = ops4sized_finger_tree
    auto = sf.get_auto5tree_(depth, sized_finger_tree)
    return auto['len']
def split_sized_finger_tree_(ops4sized_finger_tree, depth, len4treeL, sized_finger_tree, /, *, _no_check=False):
    check_int_ge(0, len4treeL)
    sz = len5sized_finger_tree_(ops4sized_finger_tree, depth, sized_finger_tree, _no_check=_no_check)
    sf = ops4sized_finger_tree
    if len4treeL == 0:
        treeL = sf.mk_empty_tree_(depth)
        treeR = sized_finger_tree
    elif len4treeL == sz:
        treeL = sized_finger_tree
        treeR = sf.mk_empty_tree_(depth)
    else:
        def auto2whether_treeL_(auto, /):
            return auto['len'] <= len4treeL
        (treeL, autoM, treeR) = sf.split_tree__max_treeL_(depth, auto2whether_treeL_, sized_finger_tree, known_begin_ok=True, known_end_not_ok=True)
    return (treeL, treeR)
#]]]'''#'''








__all__
from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, IOps4Attr4Auto6FingerTree

from seed.data_funcs.finger_tree.ft23_7types import IOps4Attr4Auto6FingerTree, IOps4Attr4Auto6FingerTree__ord_key, IOps4Attr4Auto6FingerTree__mixin__init_key_func, IOps4Attr4Auto6FingerTree__max, IOps4Attr4Auto6FingerTree__min, IOps4Attr4Auto6FingerTree__rightmost, IOps4Attr4Auto6FingerTree__leftmost

from seed.data_funcs.finger_tree.ft23_7types import Ops4Attr4Auto6FingerTree__sized, ops4attr_len, Ops4Attr4Auto6FingerTree__hash, ops4attr_hash, Ops4Attr4Auto6FingerTree__max, ops4attr_max7echo, Ops4Attr4Auto6FingerTree__min, ops4attr_min7echo, Ops4Attr4Auto6FingerTree__rightmost, ops4attr_rightmost7echo, Ops4Attr4Auto6FingerTree__leftmost, ops4attr_leftmost7echo

from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, ops4attr_len, check_ops4sized_finger_tree_, len5sized_finger_tree_, split_sized_finger_tree_, ops4attr_hash, check_ops4hashable_finger_tree_, hash5hashable_finger_tree_, default_Nothing, ops4attr_may_hash, check_ops4mhashable_finger_tree_, may_hash5mhashable_finger_tree_


from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, ops4attr_rightmost7echo, check_ops4ascend_finger_tree_, tmay_rightmost5ascend_finger_tree_, split_ascend_finger_tree_

from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, ops4attr_leftmost7echo, check_ops4descend_finger_tree_, tmay_leftmost5descend_finger_tree_, split_descend_finger_tree_

from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, ops4attr_max7echo, check_ops4maxheap_finger_tree_, tmay_max5maxheap_finger_tree_, split_maxheap_finger_tree_

from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, ops4attr_min7echo, check_ops4minheap_finger_tree_, tmay_min5minheap_finger_tree_, split_minheap_finger_tree_


from seed.data_funcs.finger_tree.ft23_7types import *
