#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/CFG/Grammar.py
[[
TODO:
    #iv2xxx&&iiir2xxx:
    ++iv2always_null
    ++iv2always_dead
    ++seperate out:iv2nullable
    ++seperate out:validate:iv2nullable
]]

[[
DONE:
TODO:

\(\<\(\|_\|i\|clas\|cl\|pas\|useles\|var\|arg\|contain\|l\|[lr]h\|item\|key\|value\|x\|v\|_node\|_r\|_ix_iir\|alia\|expression\|num_vertice\|func\|type\|a\|container\|kwargs2Attr\)\|_duplicate\|_[pkviln]\|_iir\|_kwarg\|_arg\|_lib\|_byte\|_item\|_key\|_value\|_[lr]h\)\@<!s\>
    rename: xs --> x_seq/x_set/x_setq/x_iter
idxd_seq_ex5iterable --> idxd_setq_ex5iterable
    not all SortedSet be called _setq
        normal => "_set"
        special => "_setq" only for all&&in_order #see:idxd_setq_ex5iterable
]]

seed.recognize.CFG.Grammar
py -m nn_ns.app.debug_cmd   seed.recognize.CFG.Grammar -x
py -m nn_ns.app.doctest_cmd seed.recognize.CFG.Grammar:__doc__ -ht
py_adhoc_call   seed.recognize.CFG.Grammar   @f
from seed.recognize.CFG.Grammar import *
#]]]'''
__all__ = r'''
VocabularySymbol
    NonterminalSymbol
    TerminalSymbol

check_array
PlainGrammar
    ProductionRule
        SententialForm

BaseTypeError
Bimapping4IndexedHashable
BaseIndexedHashable
    IndexedHashable

idxd_setq_ex5iterable
idxd_vocabulary_symbol_setq_ex5grammar
    iter_vocabulary_symbols5grammar

check_idxd_type_is
check_idxd_type_le
check_idxd_array
GroupedGrammar
    InnerIndexedProductionRule
        InnerIndexedSententialForm
    mk_innidxd_grammar_ex
    group__idxd_innidxd_production_rule_set_
        group__idxd_rule_set_
    group__idxd_vocabulary_symbol_set_
        classify__idxd_vocabulary_symbol_
    idxd_either_iv_iiir_setq_ex5all_iv_setq_and_all_iiir_setq__

SortedDict
SortedSet

State4LR0
    SortedDict8State4LR0
        SortedDict6State4LR0
            SortedSet6State4LR0

lhs_iv5iiir
    child_iv_seq5iiir

mk_closure4state4LR0
auto_feeds4state4LR0
    feed4state4LR0

get_or_cache_eresult8lazy_property_
    cached_mk__dead_nonterminal_symbol_set
    cached_mk_initial_state4LR0
    cached_calc_all_idxd_state_setq4LR0_ex
    cached_mk_raw_bireference_multiplicity
        BireferenceMultiplicity
    cached_mk__node2min_oolen_sentence__respectively_ex
    cached_mk__iv2min_oolen
    cached_mk__iv2nullable
    cached_mk__node2head_iv_set__respectively_ex

cached_detect__same_size_recur
    Error__grammar_has_same_size_recur_nonterminal_symbol

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.tiny_.oo8inf import oo
from seed.for_libs.for_heapq import Heap

from operator import __index__, not_
from seed.tiny_.funcs import fst, snd, echo #no_op, echo_args_kwargs, echo_kwargs, echo_args, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, not_, with_key, mk_fprint, fprint, py_cmp, int2cmp
from seed.tiny_.dict_op__add import set_add# dict_add, dict_update, set_update
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value# filter4dict_value, dict_add__is, dict_add__eq, dict_add__new, group4dict_value
from seed.types.FrozenDict import FrozenDict# empty_FrozenDict as null_FrozenDict
from seed.helper.ConstantRepr import ConstantRepr# repr_as_3dot

from seed.tiny_.containers import mk_tuple #null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_Just, mk_Left, mk_Right
from seed.types.Either import Either# Cased, KindedName
from seed.types.Either import mk_Left, mk_Right
from seed.tiny_.types5py import MapView, curry1# kwargs2Attrs
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

__all__


class _Hashable:
    def __init__(sf, nm, /):
        sf._nm = nm
        sf._h = hash((id(type(sf)), nm))
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and sf._h == ot._h and sf._nm == ot._nm
    def __hash__(sf, /):
        return sf._h
    def __repr__(sf, /):
        return repr_helper(sf, sf._nm)

class VocabularySymbol(_Hashable):
    'vocabulary_symbol'
    _0_frozen_0_ = False
    def __init_subclass__(cls, /):
        if __class__._0_frozen_0_:raise TypeError(cls)
if 1:
    class NonterminalSymbol(VocabularySymbol):
        'nonterminal_symbol'
        pass
    class TerminalSymbol(VocabularySymbol):
        'terminal_symbol'
        pass
VocabularySymbol._0_frozen_0_ = True
#end-class VocabularySymbol

def check_array(T, array, /):
    check_type_is(tuple, array)
    for x in array:
        check_type_le(T, x)
class SententialForm:
    'sentential_form'
    def __init__(sf, vocabulary_symbol_seq, /):
        check_array(VocabularySymbol, vocabulary_symbol_seq)
        sf._ls = vocabulary_symbol_seq
    def __repr__(sf, /):
        return repr_helper(sf, sf._ls)
    @property
    def vocabulary_symbol_seq(sf, /):
        return sf._ls
    #def __len__(sf, /): return len(sf._ls)

class ProductionRule:
    'production_rule'
    def __init__(sf, nonterminal_symbol, sentential_form, /):
        check_type_is(NonterminalSymbol, nonterminal_symbol)
        check_type_is(SententialForm, sentential_form)
        sf._lhs = nonterminal_symbol
        sf._rhs = sentential_form
    def __repr__(sf, /):
        return repr_helper(sf, sf._lhs, sf._rhs)
    def __len__(sf, /):
        return len(sf._rhs.vocabulary_symbol_seq)
    @property
    def lhs_nonterminal_symbol(sf, /):
        return sf._lhs
    @property
    def rhs_sentential_form(sf, /):
        return sf._rhs

#flatten/flat
#plain
class PlainGrammar:
    'plain_grammar'
    def __init__(sf, goal_symbol, production_rule_seq, /):
        check_type_is(NonterminalSymbol, goal_symbol)
        check_array(ProductionRule, production_rule_seq)
        sf._g = goal_symbol
        sf._ls = production_rule_seq
        #idxd_rule_setq, _ = idxd_setq_ex5iterable(production_rule_seq)
        #nonterminal_symbol2idxd_rule_set = group__idxd_rule_set_(idxd_rule_setq)
    def __repr__(sf, /):
        return repr_helper(sf, sf._g, sf._ls)
    @property
    def goal_symbol(sf, /):
        '-> goal_symbol/nonterminal_symbol/NonterminalSymbol'
        return sf._g
    @property
    def production_rule_seq(sf, /):
        '-> production_rule_seq/[ProductionRule]'
        return sf._ls
    #no:__iter__,__len__:production_rule_seq vs nonterminal_symbol_seq
    #def __len__(sf, /): return len(sf._ls)

class Bimapping4IndexedHashable:
    def __init__(sf, /):
        sf._j2x = []
        sf._x2j = {}
        sf._frozen = False
    def freeze(sf, /):
        sf._frozen = True
        sf._x2j = MapView(sf._x2j)
        sf._j2x = mk_tuple(sf._j2x)
    def register(sf, x, /, *, duplicated_ok=False, always_Either=False):
        '-> ((idx4payload/uint | ^KeyError) if not (duplicated_ok or always_Either) else Either idx4payload idx4payload)'
        if sf._frozen:raise TypeError
        d = sf._x2j
        j4x = len(d)
        if not j4x == (_j4x := d.setdefault(x, j4x)):
            if duplicated_ok:
                return mk_Left(_j4x)
            raise KeyError(x)#existed
        sf._j2x.append(x)
        assert len(sf._x2j) == len(sf._j2x)
        if duplicated_ok or always_Either:
            return mk_Right(j4x)
        return j4x
    def __getitem__(sf, j4x, /):
        #if type(j4x) is slice:raise TypeError
        j4x = __index__(j4x)
        return sf._j2x[j4x]
    def index(sf, x, /):
        return (j4x := sf._x2j[x])
    def __len__(sf, /):
        return len(sf._j2x)
    @property
    def idx2payload(sf, /):
        if not sf._frozen:raise TypeError
        return sf._j2x
    @property
    def payload2idx(sf, /):
        if not sf._frozen:raise TypeError
        return sf._x2j

_repr4ignore = ConstantRepr('<...>')
class BaseIndexedHashable:
    #_base_type4payload_ = object
    #def check_payload(sf, x, /):
    #    check_type_le(sf._base_type4payload_, x)
    @classmethod
    def check_referent(cls, referent, /):
        pass
    @classmethod
    def check_payload(cls, x, /):
        pass
    @classmethod
    def _idx2payload_(cls, referent, j4x, /):
        raise NotImplementedError
    def __init__(sf, referent, j4x, x, /):
        cls = type(sf)
        cls.check_referent(referent)
        cls.check_payload(x)
        check_int_ge(0, j4x)

        if not x is cls._idx2payload_(referent, j4x):raise TypeError

        sf._d = referent
        sf._j = j4x
        sf._x = x
    def __eq__(sf, ot, /):
        if sf is ot: return True
        return _cmp(sf, ot, int.__eq__)
    def __ne__(sf, ot, /):
        return not sf == ot
    def __hash__(sf, /):
        return sf._j
    def __repr__(sf, /):
        return repr_helper(sf, _repr4ignore, sf._j, sf._x)
    def __index__(sf, /):
        return sf._j
    @property
    def idx4payload(sf, /):
        return sf._j
    @property
    def payload(sf, /):
        return sf._x

    #for:sorted()
    def __lt__(sf, ot, /):
        if sf is ot: return False
        return _cmp(sf, ot, int.__lt__)
    def __gt__(sf, ot, /):
        if sf is ot: return False
        return _cmp(sf, ot, int.__gt__)
    def __ge__(sf, ot, /):
        return not sf < ot
    def __le__(sf, ot, /):
        return not sf > ot

class BaseTypeError(BaseException):pass
def _cmp(sf, ot, f, /):
    'only for:BaseIndexedHashable#using BaseTypeError to force mapping using keys of same type'
    if not type(sf) is type(ot):raise BaseTypeError(type(ot))
    if not sf._d is ot._d:raise BaseTypeError
    return f(sf._j, ot._j)
#end-BaseIndexedHashable
class IndexedHashable(BaseIndexedHashable):
    '[idxd_obj :: IndexedHashable<payload>][payload :: Hashable] #bimapping used in __eq__'
    #@override
    @classmethod
    def check_referent(cls, referent, /):
        bimapping = referent
        check_type_is(Bimapping4IndexedHashable, bimapping)
    #@override
    @classmethod
    def _idx2payload_(cls, referent, j4x, /):
        bimapping = referent
        return bimapping[j4x]

    if 0:
      def __init__(sf, bimapping, j4x, x, /):
        #j4x = bimapping.register(x)
        if not x is bimapping[j4x]:raise TypeError
        #sf.check_payload(x)
        sf._d = bimapping
        sf._j = j4x
        sf._x = x


#def idxd_seq_ex5iterable(xs, /, *, mkr=IndexedHashable, duplicated_ok=False, to_send_either_idx=False):
def idxd_setq_ex5iterable(xs, /, *, mkr=IndexedHashable, duplicated_ok=False, to_send_either_idx=False):
    '[x] -> ([IndexedHashable<x>], Bimapping4IndexedHashable<x>)'
    #tuple --> setq/SortedSet
    #   !! now: SortedSet vivi seq.__getitem__
    #
    check_type_is(bool, duplicated_ok)
    check_type_is(bool, to_send_either_idx)

    bimapping = Bimapping4IndexedHashable()
    ls = []
    if not to_send_either_idx:
        it = iter(xs)
    else:
        either_j4x = None#init4send not Either indeed
        def f(send):
            try:
                while 1:
                    yield send(either_j4x)
                        # ^StopIteration
            except StopIteration:
                pass
            return
        it = f(iter(xs).send)
    it
    for x in it:
        either_j4x = bimapping.register(x, duplicated_ok=duplicated_ok, always_Either=True)
            #either_j4x used in f()
        if either_j4x.is_left:
            continue
        j4x = either_j4x.right
        idxd_x = mkr(bimapping, j4x, x)
        ls.append(idxd_x)
    #bug:idx2idxd_payload = bimapping.idx2payload
    #idx2idxd_payload = mk_tuple(ls)
    idx2idxd_payload = SortedSet(ls)
    bimapping.freeze()

    #check_type_is(tuple, idx2idxd_payload)
    check_type_is(SortedSet, idx2idxd_payload)
    return (idx2idxd_payload, bimapping)

def iter_vocabulary_symbols5grammar(goal_symbol, production_rule_seq, /):
    '-> Iter VocabularySymbol #[duplicated_ok:=True]'
    yield goal_symbol
    for production_rule in production_rule_seq:
        yield production_rule.lhs_nonterminal_symbol
        yield from production_rule.rhs_sentential_form.vocabulary_symbol_seq

def idxd_vocabulary_symbol_setq_ex5grammar(goal_symbol, production_rule_seq, /):
    '-> ([IndexedHashable<VocabularySymbol>]/SortedSet, Bimapping4IndexedHashable<VocabularySymbol>)'
    vocabulary_symbol_iter = iter_vocabulary_symbols5grammar(goal_symbol, production_rule_seq)
    #return ((idxd_vocabulary_symbol_setq, bimapping4vocabulary) := idxd_setq_ex5iterable(vocabulary_symbol_iter))
    #   SyntaxError: cannot use assignment expressions with tuple
    #
    r = (idxd_vocabulary_symbol_setq, bimapping4vocabulary) = idxd_setq_ex5iterable(vocabulary_symbol_iter)
    #check_type_is(tuple, idxd_vocabulary_symbol_seq)
    check_type_is(SortedSet, idxd_vocabulary_symbol_setq)
    return r




#class IndexedVocabularySymbol:
#    #@override
#    _base_type4payload_ = VocabularySymbol
#class IndexedProductionRule:
#    #@override
#    _base_type4payload_ = ProductionRule




def check_idxd_type_is(T, x, /):
    #check_type_le(IndexedHashable, x)
    check_type_is(IndexedHashable, x)
    check_type_is(T, x.payload)
def check_idxd_type_le(T, x, /):
    #check_type_le(IndexedHashable, x)
    check_type_is(IndexedHashable, x)
    check_type_le(T, x.payload)
def check_idxd_array(T, array, /):
    check_type_is(tuple, array)
    for x in array:
        check_idxd_type_le(T, x)

class InnerIndexedSententialForm:
    'innidxd_sentential_form'
    def __init__(sf, idxd_vocabulary_symbol_seq, /):
        check_idxd_array(VocabularySymbol, idxd_vocabulary_symbol_seq)
        sf._ls = idxd_vocabulary_symbol_seq
    def __repr__(sf, /):
        return repr_helper(sf, sf._ls)
    @property
    def idxd_vocabulary_symbol_seq(sf, /):
        return sf._ls
    #def __len__(sf, /): return len(sf._ls)



class InnerIndexedProductionRule:
    'innidxd_production_rule'
    def __init__(sf, idxd_nonterminal_symbol, innidxd_sentential_form, /):
        check_idxd_type_is(NonterminalSymbol, idxd_nonterminal_symbol)
        check_type_is(InnerIndexedSententialForm, innidxd_sentential_form)
        sf._lhs = idxd_nonterminal_symbol
        sf._rhs = innidxd_sentential_form
    def __repr__(sf, /):
        return repr_helper(sf, sf._lhs, sf._rhs)
    def __len__(sf, /):
        return len(sf._rhs.idxd_vocabulary_symbol_seq)
    @property
    def lhs_idxd_nonterminal_symbol(sf, /):
        return sf._lhs
    @property
    def rhs_innidxd_sentential_form(sf, /):
        return sf._rhs

def mk_innidxd_grammar_ex(goal_symbol, production_rule_seq, /):
    '-> ((idxd_goal_symbol, idxd_innidxd_production_rule_setq), (bimapping4vocabulary, bimapping4innidxd_rule), (idxd_vocabulary_symbol_setq, innidxd_production_rule_seq)) / (innidxd_grammar/(IndexedHashable<NonterminalSymbol>,[IndexedHashable<InnerIndexedProductionRule>]/SortedSet), (Bimapping4IndexedHashable<VocabularySymbol>,Bimapping4IndexedHashable<InnerIndexedProductionRule>), ([IndexedHashable<VocabularySymbol>]/SortedSet, [InnerIndexedProductionRule]{maybe duplicated}))'
    check_type_is(NonterminalSymbol, goal_symbol)
    check_array(ProductionRule, production_rule_seq)

    (idxd_vocabulary_symbol_setq, bimapping4vocabulary) = idxd_vocabulary_symbol_setq_ex5grammar(goal_symbol, production_rule_seq)
    idxd_goal_symbol = bimapping4vocabulary.index(goal_symbol)

    ls = []
    for production_rule in production_rule_seq:
        lhs = production_rule.lhs_nonterminal_symbol
        rhs = production_rule.rhs_sentential_form
        idxd_lhs = bimapping4vocabulary.index(lhs)
        innidxd_sentential_form = InnerIndexedSententialForm(mk_tuple(map(bimapping4vocabulary.index, rhs.vocabulary_symbol_seq)))
        innidxd_production_rule = InnerIndexedProductionRule(idxd_lhs, innidxd_sentential_form)
        ls.append(innidxd_production_rule)
    innidxd_production_rule_seq = mk_tuple(ls)
        #maybe duplicated
    (idxd_innidxd_production_rule_setq, bimapping4innidxd_rule) = idxd_setq_ex5iterable(innidxd_production_rule_seq)
    #bug:assert innidxd_production_rule_seq == bimapping4innidxd_rule.idx2payload
    #       !! idx2payload is not idx2idxd_payload
    #bug:assert innidxd_production_rule_seq == mk_tuple(iiir.payload for iiir in idxd_innidxd_production_rule_setq)
    #       xxx:iir_seq <<== iiir_seq
    #       !! iir_seq maybe duplicated
    innidxd_grammar = (idxd_goal_symbol, idxd_innidxd_production_rule_setq)
    return ((idxd_goal_symbol, idxd_innidxd_production_rule_setq), (bimapping4vocabulary, bimapping4innidxd_rule), (idxd_vocabulary_symbol_setq, innidxd_production_rule_seq))



def group__idxd_rule_set_(idxd_rule_iter, /):
    '[IndexedHashable<ProductionRule>]/iterable -> FrozenDict{NonterminalSymbol:SortedSet{IndexedHashable<ProductionRule>}}'
    nonterminal_symbol2idxd_rule_seq = {}
    for idxd_rule in idxd_rule_iter:
        production_rule = idxd_rule.payload
        lhs = production_rule.lhs_nonterminal_symbol
        ls = nonterminal_symbol2idxd_rule_seq.setdefault(lhs, [])
        ls.append(idxd_rule)
    #nonterminal_symbol2idxd_rule_seq = FrozenDict(fmap4dict_value(tuple, nonterminal_symbol2idxd_rule_seq))
    nonterminal_symbol2idxd_rule_set = FrozenDict(fmap4dict_value(SortedSet, nonterminal_symbol2idxd_rule_seq))
    return nonterminal_symbol2idxd_rule_set


def group__idxd_innidxd_production_rule_set_(idxd_innidxd_production_rule_iter, /):
    '[IndexedHashable<InnerIndexedProductionRule>]/iterable -> SortedDict{IndexedHashable<NonterminalSymbol>:SortedSet{IndexedHashable<InnerIndexedProductionRule>}}'
    d = {}
    for idxd_innidxd_production_rule in idxd_innidxd_production_rule_iter:
        innidxd_production_rule = idxd_innidxd_production_rule.payload
        lhs = innidxd_production_rule.lhs_idxd_nonterminal_symbol
        ls = d.setdefault(lhs, [])
        ls.append(idxd_innidxd_production_rule)
    return (idxd_nonterminal_symbol2idxd_innidxd_production_rule_set := SortedDict(fmap4dict_value(SortedSet, d)))
    #return (idxd_nonterminal_symbol2idxd_innidxd_production_rule_seq := FrozenDict(fmap4dict_value(tuple, d)))

def classify__idxd_vocabulary_symbol_(idxd_vocabulary_symbol, result4T=False, result4N=True, /):
    'IndexedHashable<VocabularySymbol> -> a -> b -> (a if TerminalSymbol else b)'
    iv = idxd_vocabulary_symbol
    check_type_is(IndexedHashable, iv)
    vocabulary_symbol = iv.payload
    cls = type(vocabulary_symbol)
    if cls is TerminalSymbol:
        return result4T
    elif cls is NonterminalSymbol:
        return result4N
    else:
        raise TypeError(cls)
    raise 000
def group__idxd_vocabulary_symbol_set_(idxd_vocabulary_symbol_iter, /):
    '[IndexedHashable<VocabularySymbol>]/iterable -> asif_grouped_idxd_vocabulary/(idxd_terminal_symbol_set, idxd_nonterminal_symbol_set)/({IndexedHashable<VocabularySymbol>}/SortedSet,{IndexedHashable<VocabularySymbol>}/SortedSet)'
    idxd_terminal_symbol_seq = []
    idxd_nonterminal_symbol_seq = []
    ls_ls = (idxd_terminal_symbol_seq, idxd_nonterminal_symbol_seq)
    for iv in idxd_vocabulary_symbol_iter:
        ls = classify__idxd_vocabulary_symbol_(iv, *ls_ls)
        ls.append(iv)
    idxd_terminal_symbol_set = SortedSet(idxd_terminal_symbol_seq)
    idxd_nonterminal_symbol_set = SortedSet(idxd_nonterminal_symbol_seq)
    return (idxd_terminal_symbol_set, idxd_nonterminal_symbol_set)

def idxd_either_iv_iiir_setq_ex5all_iv_setq_and_all_iiir_setq__(idxd_vocabulary_symbol_setq, idxd_innidxd_production_rule_setq, /):
    '[IndexedHashable<VocabularySymbol>]/SortedSet -> [IndexedHashable<InnerIndexedProductionRule>]/SortedSet -> ([idxd_either_iv_iiir/IndexedHashable<either_iv_iiir/(Either IndexedHashable<VocabularySymbol> IndexedHashable<InnerIndexedProductionRule>)>]/SortedSet, Bimapping4IndexedHashable<either_iv_iiir>)'
    def f():
        yield from map(mk_Left, idxd_vocabulary_symbol_setq)
        yield from map(mk_Right, idxd_innidxd_production_rule_setq)

    (idxd_either_iv_iiir_setq, bimapping4either_iv_iiir) = idxd_setq_ex5iterable(f())
    L0 = len(idxd_vocabulary_symbol_setq)
    L1 = len(idxd_innidxd_production_rule_setq)
    iE_setq = idxd_either_iv_iiir_setq
    assert len(iE_setq) == L0+L1
    for j in range(L0+L1):
        assert iE_setq[j].idx4payload == j
    for j in range(L0):
        assert iE_setq[j].payload.left.idx4payload == j
    for j in range(L0, L0+L1):
        assert iE_setq[j].payload.right.idx4payload == j+L0
    return (idxd_either_iv_iiir_setq, bimapping4either_iv_iiir)

class GroupedGrammar:
    'grouped_grammar'
    def __init__(sf, goal_symbol, production_rule_seq, /):
        check_type_is(NonterminalSymbol, goal_symbol)
        check_array(ProductionRule, production_rule_seq)

        ((idxd_goal_symbol, idxd_innidxd_production_rule_setq), (bimapping4vocabulary, bimapping4innidxd_rule), (idxd_vocabulary_symbol_setq, innidxd_production_rule_seq)) = mk_innidxd_grammar_ex(goal_symbol, production_rule_seq)
        idxd_nonterminal_symbol2idxd_innidxd_production_rule_set = group__idxd_innidxd_production_rule_set_(idxd_innidxd_production_rule_setq)
        (idxd_terminal_symbol_set, idxd_nonterminal_symbol_set) = group__idxd_vocabulary_symbol_set_(idxd_vocabulary_symbol_setq)

        #grouped_grammar:asif:dgraph:[vtx==idxd_either_iv_iiir~=either_iv_iiir]
        (idxd_either_iv_iiir_setq, bimapping4either_iv_iiir) = idxd_either_iv_iiir_setq_ex5all_iv_setq_and_all_iiir_setq__(idxd_vocabulary_symbol_setq, idxd_innidxd_production_rule_setq)
        del bimapping4either_iv_iiir # (?=+L0)

        sf._g = goal_symbol
            #all-maybe_dead
        sf._rs = production_rule_seq
            #all-maybe_duplicated

        sf._ix_g = idxd_goal_symbol
            #all-maybe_dead
        sf._ix_iirs = idxd_innidxd_production_rule_setq
            #all&&no_duplicates


        sf._ix_d = iv2iiir_set = idxd_nonterminal_symbol2idxd_innidxd_production_rule_set

        sf._bid4v = bimapping4vocabulary
        sf._bid4iir = bimapping4innidxd_rule
        sf._ix_vs = idxd_vocabulary_symbol_setq
            #all&&no_duplicates
        sf._T = idxd_terminal_symbol_set
            #T-all&&no_duplicates
        sf._N = idxd_nonterminal_symbol_set
            #N-all&&no_duplicates

        sf.__iir_seq__duplicated = innidxd_production_rule_seq
            #all-maybe_duplicated

        sf._nodes = idxd_either_iv_iiir_setq

        #sf._oolen_ex = None
        #sf._raw_biref_count = None
            # !! now:asif_cached_property

        #alias:
        all_iT_set = sf.idxd_terminal_symbol_set
        all_iN_set = sf.idxd_nonterminal_symbol_set
        #all_dead_iN_set = cached_mk__dead_nonterminal_symbol_set(sf)
        iN2child_iiir_set = sf.idxd_nonterminal_symbol2idxd_innidxd_production_rule_set
        all_iiir_setq = sf.idxd_innidxd_production_rule_setq
        all_iv_setq = sf.idxd_vocabulary_symbol_setq

        return
    def __repr__(sf, /):
        return repr_helper(sf, sf._g, sf._rs)
    @property
    def goal_symbol(sf, /):
        '-> goal_symbol/nonterminal_symbol/NonterminalSymbol'
        #all-maybe_dead
        return sf._g
    @property
    def production_rule_seq(sf, /):
        '-> production_rule_seq/[ProductionRule]'
        #all-maybe_duplicated
        return sf._rs
    #no:__iter__,__len__:production_rule_seq vs nonterminal_symbol_seq
    #def __len__(sf, /): return len(sf._rs)
    @property
    def idxd_goal_symbol(sf, /):
        '-> idxd_goal_symbol/idxd_nonterminal_symbol/IndexedHashable<NonterminalSymbol>'
        #all-maybe_dead
        return sf._ix_g
    @property
    def idxd_innidxd_production_rule_setq(sf, /):
        '-> idxd_innidxd_production_rule_setq/[IndexedHashable<InnerIndexedProductionRule>]/SortedSet #all_iiir_setq'
        #all&&no_duplicates
        return sf._ix_iirs
    @property
    def idxd_nonterminal_symbol2idxd_innidxd_production_rule_set(sf, /):
        '-> SortedDict{idxd_nonterminal_symbol: SortedSet{idxd_innidxd_production_rule{.lhs==nonterminal_symbol}}} #iN2child_iiir_set{may exclude dead-iN hence not all}'
        return sf._ix_d
    @property
    def bimapping4vocabulary(sf, /):
        '-> Bimapping4IndexedHashable<VocabularySymbol>'
        return sf._bid4v
    @property
    def bimapping4innidxd_rule(sf, /):
        '-> Bimapping4IndexedHashable<InnerIndexedProductionRule>'
        return sf._bid4iir
    @property
    def idxd_vocabulary_symbol_setq(sf, /):
        '-> [IndexedHashable<VocabularySymbol>]/SortedSet #all_iv_setq'
        #all&&no_duplicates
        return sf._ix_vs
    @property
    def idxd_terminal_symbol_set(sf, /):
        '-> {IndexedHashable<TerminalSymbol>}/SortedSet #all_iT_set'
        #all&&no_duplicates
        return sf._T
    @property
    def idxd_nonterminal_symbol_set(sf, /):
        '-> {IndexedHashable<NonterminalSymbol>}/SortedSet #all_iN_set'
        #all&&no_duplicates
        return sf._N
    @property
    def node_setq4asif_dgraph(sf, /):
        '-> [node/idxd_either_iv_iiir]/[IndexedHashable<(Either IndexedHashable<VocabularySymbol> IndexedHashable<InnerIndexedProductionRule>)>]/SortedSet'
        #all&&no_duplicates
        return sf._nodes
    @property
    def num_vertices4asif_dgraph(sf, /):
        '-> num_vertices/uint'
        return len(sf._nodes)
    def vtx2node4asif_dgraph(sf, vtx, /):
        'vtx/uint -> node/idxd_either_iv_iiir'
        vtx = __index__(vtx)
        check_int_ge(0, vtx)
        return sf._nodes[vtx]
    def vtx5node4asif_dgraph(sf, node, /):
        'node/idxd_either_iv_iiir -> vtx/uint'
        return node.idx4payload
        return __index__(node)
    def iv2vtx4asif_dgraph(sf, iv, /):
        'iv/idxd_vocabulary_symbol -> vtx/uint'
        vtx = iv.idx4payload
        return vtx
    def iiir2vtx4asif_dgraph(sf, iiir, /):
        'iiir/idxd_innidxd_production_rule -> vtx/uint'
        vtx = iiir.idx4payload +len(sf.idxd_vocabulary_symbol_setq)
        return vtx
    def iv2node4asif_dgraph(sf, iv, /):
        'iv/idxd_vocabulary_symbol -> node/idxd_either_iv_iiir'
        vtx = sf.iv2vtx4asif_dgraph(iv)
        node = sf._nodes[vtx]
        assert node.payload.left == iv
        return node
    def iiir2node4asif_dgraph(sf, iiir, /):
        'iiir/idxd_innidxd_production_rule -> node/idxd_either_iv_iiir'
        vtx = sf.iiir2vtx4asif_dgraph(iiir)
        node = sf._nodes[vtx]
        assert node.payload.right == iiir
        return node

    def is_parallel_vtx4asif_dgraph(sf, vtx, /):
        'vtx/uint -> bool'
        return vtx < len(sf.idxd_vocabulary_symbol_setq)
    def is_serial_vtx4asif_dgraph(sf, vtx, /):
        'vtx/uint -> bool'
        return not vtx < len(sf.idxd_vocabulary_symbol_setq)

    def vtx2iter_children4asif_dgraph(sf, vtx, /):
        'vtx/uint -> Iter vtx'
        node = sf.vtx2node4asif_dgraph(vtx)
        either_iv_iiir = node.payload
        if either_iv_iiir.is_left:
            iv = either_iv_iiir.left
            iiir_set = sf.idxd_nonterminal_symbol2idxd_innidxd_production_rule_set.get(iv, '')
            it_vtc = map(sf.iiir2vtx4asif_dgraph, iiir_set)
        else:
            iiir = either_iv_iiir.right
            child_iv_seq = child_iv_seq5iiir(iiir)
            it_vtc = map(sf.iv2vtx4asif_dgraph, child_iv_seq)
        it_vtc
        return it_vtc



    def __getitem__(sf, idxd_nonterminal_symbol, /):
        'idxd_nonterminal_symbol -> [idxd_innidxd_production_rule{.payload.lhs==idxd_nonterminal_symbol}]'
        return sf._ix_d[idxd_nonterminal_symbol]


    r'''[[[
    # !! now:asif_cached_property
    # see:get_or_cache_eresult8lazy_property_
    #   cached_mk__iv2min_oolen()
    #   cached_mk__iv2nullable()

    @property#tmp_property
    def bireference_multiplicity(sf, /):
        '-> BireferenceMultiplicity'
        return BireferenceMultiplicity(sf)
    @property#lazy_property
    def raw_bireference_multiplicity(sf, /):
        '-> (iiir2child_iv2multiplicity, child_iv2iiir2multiplicity)'
        if sf._raw_biref_count is None:
            sf._raw_biref_count = (iiir2child_iv2multiplicity, child_iv2iiir2multiplicity) = cached_mk_raw_bireference_multiplicity(grouped_grammar)
        return sf._raw_biref_count

    @property#lazy_property
    def node2min_oolen_sentence__respectively_ex(sf, /):
        '[#O(M+NlogN):[M==len(all_iv_setq)][N==len(all_iiir_setq)]#] => ((iv2min_oolen, iiir2min_oolen), (iv2nullable, iiir2nullable))'
        if sf._oolen_ex is None:
            sf._oolen_ex = ((iv2min_oolen, iiir2min_oolen), (iv2nullable, iiir2nullable)) = cached_mk__node2min_oolen_sentence__respectively_ex(sf :vs: sf.bireference_multiplicity)
        return sf._oolen_ex
    #]]]'''#'''




    ####old:
    #def __init__(sf, goal_symbol, production_rule_seq, /):
    #    check_type_is(NonterminalSymbol, goal_symbol)
    #    check_array(ProductionRule, production_rule_seq)
    #    idxd_rule_setq, _ = idxd_setq_ex5iterable(production_rule_seq)
    #    nonterminal_symbol2idxd_rule_set = group__idxd_rule_set_(idxd_rule_setq)

    #    sf._g = goal_symbol
    #    sf._rs = production_rule_seq
    #    sf._idxd_ls = idxd_rule_setq
    #    sf._d = nonterminal_symbol2idxd_rule_set
    #@property
    #def indexed_production_rule_setq(sf, /):
    #    '-> idxd_rule_setq/[IndexedHashable<ProductionRule>]'
    #    return sf._idxd_ls
    #@property
    #def nonterminal_symbol2indexed_production_rule_set(sf, /):
    #    '-> {nonterminal_symbol: [idxd_rule{.lhs==nonterminal_symbol}]/SortedSet}/FrozenDict'
    #    return sf._d
    #def __getitem__(sf, nonterminal_symbol, /):
    #    'nonterminal_symbol -> [idxd_rule{.lhs==nonterminal_symbol}]'
    #    return sf._d[nonterminal_symbol]
#end-class GroupedGrammar:


#deprecate by:idxd_either_iv_iiir_setq_ex5all_iv_setq_and_all_iiir_setq__
#class IndexedVocabularySymbolXInnerIndexedProductionRule(BaseIndexedHashable):
#    '[idxd_obj :: IndexedHashable<payload>][payload == (idxd_vocabulary_symbol|idxd_innidxd_production_rule) :: IndexedHashable<(VocabularySymbol|InnerIndexedProductionRule)> <: Hashable] #grouped_grammar used in __eq__'
#    #@override
#    @classmethod
#    def check_referent(cls, referent, /):
#        grouped_grammar = referent
#        check_type_is(GroupedGrammar, grouped_grammar)
#    #@override
#    @classmethod
#    def _idx2payload_(cls, referent, j4x, /):
#        grouped_grammar = referent
#        return grouped_grammar.TODO[j4x]
#





class _SortedDict:
    'Ord k => asif-FrozenDict&&Hashable'
    def __init__(sf, d, /):
        sorted_ps = tuple(sorted(d.items()))
        sf._d = d
        sf._ps = sorted_ps
        sf._h = None
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and hash(sf) == hash(ot) and sf._ps == ot._ps
    def __hash__(sf, /):
        if sf._h is None:
            sf._h = sf._hash()
        return sf._h
    def _hash(sf, /):
        assert sf._h is None
        return hash((id(type(sf)), sf._ps))

    def __repr__(sf, /):
        return repr_helper(sf, sf._ps)
    def __iter__(sf, /):
        return map(fst, sf._ps)
    def __len__(sf, /):
        return len(sf._ps)
    def __contains__(sf, k, /):
        return k in sf._d
    def __getitem__(sf, k, /):
        return sf._d[k]
    def iter_items(sf, /):
        return iter(sf._ps)
    def iter_keys(sf, /):
        return map(fst, sf._ps)
    def iter_values(sf, /):
        return map(snd, sf._ps)
    #for:fmap4dict_value()
    items = iter_items
    keys = iter_keys
    values = iter_values
#end-class _SortedDict:

class SortedDict(_SortedDict):
    @classmethod
    def from_free_dict(cls, d, /):
        return cls(d)
    def __init__(sf, arg4dict, /):
        d = dict(arg4dict)
        super().__init__(d)
#end-class SortedDict:










class SortedDict8State4LR0(_SortedDict):
    r'''[[[
    State4LR0 = SortedDict8State4LR0
    [state4LR0
        <=> {dotted_rule}
        <=> {(rule, idx_ex6rhs4rule)}
        <=> {(rule, len_tail4rhs4rule)}
        <=> {len_tail4rhs4rule:{rule}}
        <=> {len_tail4rhs4rule:{may_vocabulary_symbol:{rule}}}
            # [[len_tail4rhs4rule==0] <==> [may_vocabulary_symbol is None]]
        <=> {len_tail4rhs4rule:{may_idxd_vocabulary_symbol:{idxd_innidxd_production_rule}}}
            # [[len_tail4rhs4rule==0] <==> [may_idxd_vocabulary_symbol is None]]
        <=> {may_idxd_vocabulary_symbol:{len_tail4rhs4rule:{idxd_innidxd_production_rule}}}
        == SortedDict8State4LR0
    ]


    [iv == idxd_vocabulary_symbol]
    [iir == innidxd_production_rule]
    [iiir == idxd_innidxd_production_rule]

    #]]]'''#'''


    @classmethod
    def from_free_dict(cls, d, /):
        return cls(fmap4dict_value(SortedDict6State4LR0.from_free_dict, d))
    def __init__(sf, arg4dict, /):
        d = dict(arg4dict)
        if not d: raise TypeError
        else:
            for k in d:
                if k is None:continue
                check_idxd_type_le(VocabularySymbol, k)
        for v in d.values():
            check_type_is(SortedDict6State4LR0, v)
        if not None is (_d := d.get(None)):
            if not len(_d) == 1:raise TypeError
            if not 0 in _d:raise TypeError

        super().__init__(d)
#end-class SortedDict8State4LR0:


class SortedDict6State4LR0(_SortedDict):
    @classmethod
    def from_free_dict(cls, d, /):
        return cls(fmap4dict_value(SortedSet6State4LR0.from_free_set, d))
    def __init__(sf, arg4dict, /):
        d = dict(arg4dict)
        if not d: raise TypeError
        elif len(d) == 1 and 0 in d:
            for k in d:
                check_int_ge(0, k)
        else:
            for k in d:
                check_int_ge(1, k)
        for v in d.values():
            check_type_is(SortedSet6State4LR0, v)
        for k, v in d.items():
            for iir in v:
                if not k <= len(iir):raise TypeError

        super().__init__(d)
#end-class SortedDict6State4LR0:

class _SortedSet:
    'set --> setq == set&&seq immutable'
    @classmethod
    def from_free_set(cls, s, /):
        return cls(s)
    def __init__(sf, s, /):
        sorted_ks = tuple(sorted(s))
        sf._s = s
        sf._ks = sorted_ks
        sf._h = None

    def __getitem__(sf, x, /):
        r'''[[[
        x -> (tuple(sf)[x] | ^ IndexError)

    tuple vs SortedSet
        __index__(idxd_obj) --> idx
        ???but how: idx --> idxd_obj???
        seq[idx] --> idxd_obj
        set cannot
        #or:SortedSet vivi seq.__getitem__
            #set --> setq{#only for idxd_obj_setq where [idxd_obj_setq[i].idx4payload == i]#}
        #]]]'''#'''
        return sf._ks[x]
            # ^ IndexError
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and hash(sf) == hash(ot) and sf._ks == ot._ks
    def __hash__(sf, /):
        if sf._h is None:
            sf._h = sf._hash()
        return sf._h
    def _hash(sf, /):
        assert sf._h is None
        return hash((id(type(sf)), sf._ks))

    def __repr__(sf, /):
        return repr_helper(sf, sf._ks)
    def __iter__(sf, /):
        return iter(sf._ks)
    def __len__(sf, /):
        return len(sf._ks)
    def __contains__(sf, k, /):
        return k in sf._s
#end-class SortedSet6State4LR0:



class SortedSet(_SortedSet):
    def __init__(sf, arg4set, /):
        s = set(arg4set)
        super().__init__(s)
class SortedSet6State4LR0(_SortedSet):
    def __init__(sf, arg4set, /):
        s = set(arg4set)
        if not s: raise TypeError
        else:
            for k in s:
                check_idxd_type_le(InnerIndexedProductionRule, k)

        super().__init__(s)
#end-class SortedSet6State4LR0:



SortedDict8State4LR0
SortedDict6State4LR0
SortedSet6State4LR0

State4LR0 = SortedDict8State4LR0
def lhs_iv5iiir(iiir, /):
    'IndexedHashable<InnerIndexedProductionRule> -> IndexedHashable<NonterminalSymbol> # asif:(rule->lhs/nonterminal_symbol)'
    lhs_iv = idxd_vocabulary_symbol = iiir.payload.lhs_idxd_nonterminal_symbol
    return lhs_iv
#def rhs_iv_seq5iiir(iiir, /):
def child_iv_seq5iiir(iiir, /):
    'IndexedHashable<InnerIndexedProductionRule> -> [IndexedHashable<VocabularySymbol>] # asif:(rule->rhs/sentential_form)'
    child_iv_seq = idxd_vocabulary_symbol_seq = iiir.payload.rhs_innidxd_sentential_form.idxd_vocabulary_symbol_seq
    return child_iv_seq
def mk_closure4state4LR0(grouped_grammar, incomplete_st, /):
    r'''[[[
    input:
        [incomplete_st :: SortedDict8State4LR0]

    output:
        [st==complete_st :: SortedDict8State4LR0]

    [SortedDict8State4LR0
    == SortedDict8State4LR0{may_idxd_vocabulary_symbol:SortedDict6State4LR0{len_tail4rhs4rule:SortedSet6State4LR0{idxd_innidxd_production_rule}}}
    <=> {may_idxd_vocabulary_symbol:{len_tail4rhs4rule:{idxd_innidxd_production_rule}}}
    ]
            # [[len_tail4rhs4rule==0] <==> [may_idxd_vocabulary_symbol is None]]

    #]]]'''#'''
    check_type_is(GroupedGrammar, grouped_grammar)
    check_type_is(SortedDict8State4LR0, incomplete_st)

    d = grouped_grammar.idxd_nonterminal_symbol2idxd_innidxd_production_rule_set
        # :: {iN/iv:{iiir}}

    new_st = fmap4dict_value(curry1(fmap4dict_value, set), incomplete_st)
        # :: {may_iv:{sz_tail:{iiir}}}
    todo_list = []
        # :: [iv/idxd_vocabulary_symbol]
        #
        # #obsolete# :: [(len_tail4rhs4rule, iv, iiir)]
        #   [len_tail4rhs4rule > 0]
        #   [iv == iiir[-len_tail4rhs4rule]]
    iv_set4done_or_todo = set()
    def _add_iv4todo(idxd_vocabulary_symbol, /):
        iv = idxd_vocabulary_symbol
        if set_add(iv_set4done_or_todo, iv):
            todo_list.append(iv)
    def _adds4new_st(idxd_innidxd_production_rule_set, /):
        for iiir in idxd_innidxd_production_rule_set:
            idxd_vocabulary_symbol_seq = child_iv_seq5iiir(iiir)
            len_tail4rhs4rule = len(idxd_vocabulary_symbol_seq)
            may_iv = may_head = None if len_tail4rhs4rule == 0 else idxd_vocabulary_symbol_seq[0]

            sz2iiir_set = new_st.setdefault(may_iv, {})
            iiir_set = sz2iiir_set.setdefault(len_tail4rhs4rule, set())
            iiir_set.add(iiir)
            if not may_iv is None:
                iv = may_iv
                _add_iv4todo(iv)


    #if not sorted => inconsistent when error
    #   now:using SortedDict8State4LR0
    def init_todo_list():
        sorted = echo
        for may_idxd_vocabulary_symbol, len_tail4rhs4rule2idxd_innidxd_production_rule_set in sorted(incomplete_st.items()):
            #assert len(len_tail4rhs4rule2idxd_innidxd_production_rule_set)
            if may_idxd_vocabulary_symbol is None:
                #assert len(len_tail4rhs4rule2idxd_innidxd_production_rule_set) == 1
                #assert 0 in len_tail4rhs4rule2idxd_innidxd_production_rule_set.keys()
                #assert len(len_tail4rhs4rule2idxd_innidxd_production_rule_set[0])
                continue
            idxd_vocabulary_symbol = may_idxd_vocabulary_symbol
            iv = idxd_vocabulary_symbol
            _add_iv4todo(iv)
            ##assert not 0 in len_tail4rhs4rule2idxd_innidxd_production_rule_set.keys()
            #for len_tail4rhs4rule, idxd_innidxd_production_rule_set in sorted(len_tail4rhs4rule2idxd_innidxd_production_rule_set.items()):
            #    assert len_tail4rhs4rule > 0
            #    #useless:_len_tail4rhs4rule = len_tail4rhs4rule - 1
            #    assert len(idxd_innidxd_production_rule_set)

    def loop_body():
        for iv in it4todo:
            try:
                idxd_innidxd_production_rule_set = d[iv]
            except KeyError:
                continue
            _adds4new_st(idxd_innidxd_production_rule_set)
    init_todo_list()
    while todo_list:
        it4todo = iter(todo_list)
        todo_list = []
        loop_body()
    new_st

    new_st = SortedDict8State4LR0.from_free_dict(new_st)
    return (complete_st := new_st)
#end-mk_closure4state4LR0


def feed4state4LR0(grouped_grammar, complete_st, idxd_vocabulary_symbol, /):
    'GroupedGrammar -> complete_st/SortedDict8State4LR0 -> IndexedHashable<VocabularySymbol> -> next_complete_st/SortedDict8State4LR0 | ^KeyError/vocabulary_symbol-fed-donot-follow-input-st'
    check_type_is(GroupedGrammar, grouped_grammar)
    check_type_is(SortedDict8State4LR0, complete_st)
    check_idxd_type_le(VocabularySymbol, idxd_vocabulary_symbol)

    sz2iiir_set = complete_st[idxd_vocabulary_symbol]
        # ^KeyError
    new_st = {}
    for len_tail4rhs4rule, iiir_set in sz2iiir_set.iter_items():
        assert len_tail4rhs4rule > 0
        _len_tail4rhs4rule = len_tail4rhs4rule -1
        for iiir in iiir_set:
            #vivi:_adds4new_st()
            idxd_vocabulary_symbol_seq = child_iv_seq5iiir(iiir)
            may_iv = may_head = None if _len_tail4rhs4rule == 0 else idxd_vocabulary_symbol_seq[-_len_tail4rhs4rule]

            _sz2iiir_set = new_st.setdefault(may_iv, {})
            _iiir_set = _sz2iiir_set.setdefault(_len_tail4rhs4rule, set())
            _iiir_set.add(iiir)
    new_st

    new_st = SortedDict8State4LR0.from_free_dict(new_st)
    return (next_complete_st := mk_closure4state4LR0(grouped_grammar, new_st))
#end-feed4state4LR0

def auto_feeds4state4LR0(grouped_grammar, complete_st, /):
    'GroupedGrammar -> complete_st/SortedDict8State4LR0 -> {idxd_vocabulary_symbol:next_complete_st}/SortedDict{IndexedHashable<VocabularySymbol>:SortedDict8State4LR0}'
    check_type_is(SortedDict8State4LR0, complete_st)
    iv2st = iv2next_complete_st = {}
    for may_iv in complete_st:
        if may_iv is None:
            continue
        idxd_vocabulary_symbol = iv = may_iv
        st = next_complete_st = feed4state4LR0(grouped_grammar, complete_st, idxd_vocabulary_symbol)
        iv2st[iv] = st
    return SortedDict(iv2next_complete_st)
#end-auto_feeds4state4LR0


def get_or_cache_eresult8lazy_property_(obj, key, mk_val5obj_, Exception=Exception, /):
    #vim: /^def .*(grouped_grammar, \/):
    'asif_cached_property'
    'asif_cached_lazy_property'
    while 1:
        try:
            eresult = vars(obj)[key]
        except KeyError:
            try:
                oresult = mk_val5obj_(obj)
            except Exception as exc:
                eresult = mk_Left(exc)
            else:
                eresult = mk_Right(oresult)
            eresult
            vars(obj)[key] = eresult
            continue
        else:
            eresult
            check_type_is(Either, eresult)
            break
    eresult
    if eresult.is_left:
        raise eresult.left
    return eresult.right

#def findout_all_dead_nonterminal_symbol_set(grouped_grammar, /):
def cached_mk__dead_nonterminal_symbol_set(grouped_grammar, /):
    'GroupedGrammar -> dead_nonterminal_symbol_set/all_dead_iN_set/SortedSet{IndexedHashable<NonterminalSymbol>}'
    check_type_is(GroupedGrammar, grouped_grammar)
    return get_or_cache_eresult8lazy_property_(grouped_grammar, cached_mk__dead_nonterminal_symbol_set, _mk__dead_nonterminal_symbol_set)
def _mk__dead_nonterminal_symbol_set(grouped_grammar, /):
    #all_dead_iN_set = cached_mk__dead_nonterminal_symbol_set(grouped_grammar)
    all_iN_set = grouped_grammar.idxd_nonterminal_symbol_set
    iN2child_iiir_set = grouped_grammar.idxd_nonterminal_symbol2idxd_innidxd_production_rule_set
    return (dead_nonterminal_symbol_set := SortedSet(iN for iN in all_iN_set if iN not in iN2child_iiir_set))

#def mk_initial_state4LR0(grouped_grammar, /):
def cached_mk_initial_state4LR0(grouped_grammar, /):
    'GroupedGrammar -> complete_st/SortedDict8State4LR0 | ^KeyError/dead-goal_symbol'
    check_type_is(GroupedGrammar, grouped_grammar)
    return get_or_cache_eresult8lazy_property_(grouped_grammar, cached_mk_initial_state4LR0, _mk_initial_state4LR0)
def _mk_initial_state4LR0(grouped_grammar, /):
    ig = grouped_grammar.idxd_goal_symbol
    iv2iiir_set = grouped_grammar.idxd_nonterminal_symbol2idxd_innidxd_production_rule_set

    iiir_set = iv2iiir_set[ig]
        # ^KeyError
    assert iiir_set

    new_st = {}
    for iiir in iiir_set:
        #vivi:_adds4new_st()
        idxd_vocabulary_symbol_seq = child_iv_seq5iiir(iiir)
        len_tail4rhs4rule = len(idxd_vocabulary_symbol_seq)
        may_iv = may_head = None if len_tail4rhs4rule == 0 else idxd_vocabulary_symbol_seq[0]

        sz2iiir_set = new_st.setdefault(may_iv, {})
        iiir_set = sz2iiir_set.setdefault(len_tail4rhs4rule, set())
        iiir_set.add(iiir)
    assert new_st
    new_st

    new_st = SortedDict8State4LR0.from_free_dict(new_st)
    return (complete_st := mk_closure4state4LR0(grouped_grammar, new_st))
#end-cached_mk_initial_state4LR0




#def calc_all_idxd_states4LR0_ex(grouped_grammar, /):
def cached_calc_all_idxd_state_setq4LR0_ex(grouped_grammar, /):
    'GroupedGrammar -> (all_idxd_complete_state_setq, bimapping4complete_st, ist2iv2next_ist)/([IndexedHashable<complete_st/SortedDict8State4LR0>]/SortedSet, Bimapping4IndexedHashable<complete_st>, SortedDict{IndexedHashable<complete_st>:SortedDict{IndexedHashable<VocabularySymbol>:IndexedHashable<complete_st>}}) | ^KeyError/dead-goal_symbol # [all_idxd_complete_state_setq[0].payload == initial_state4LR0]'
    check_type_is(GroupedGrammar, grouped_grammar)
    return get_or_cache_eresult8lazy_property_(grouped_grammar, cached_calc_all_idxd_state_setq4LR0_ex, _calc_all_idxd_states4LR0_ex)
def _calc_all_idxd_states4LR0_ex(grouped_grammar, /):
    initial_state4LR0 = cached_mk_initial_state4LR0(grouped_grammar)
        # ^KeyError
    ls = []
        # :: [(j4st, iv2j4next_st)]
    def save(j4st, iv2j4next_st, /):
        ls.append((j4st, iv2j4next_st))
    def f(save, /):
        def put(complete_st, /):
            either_j4x = yield complete_st
            if either_j4x.is_right:
                j4st = either_j4x.right
                todo_list.append((j4st, complete_st))
            return either_j4x

        todo_list = []
            # :: [(j4st, complete_st)]
        either_j4x = yield from put(initial_state4LR0)
        while todo_list:
            it4todo = iter(todo_list)
            todo_list = []
            for (j4st, complete_st) in it4todo:
                iv2next_complete_st = auto_feeds4state4LR0(grouped_grammar, complete_st)
                check_type_is(SortedDict, iv2next_complete_st)
                iv2j4next_st = {}
                for iv, next_complete_st in iv2next_complete_st.items():
                    either_j4x = yield from put(next_complete_st)
                        #update:todo_list
                    j4next_st = either_j4x.payload
                    iv2j4next_st[iv] = j4next_st
                iv2j4next_st
                save(j4st, iv2j4next_st)

    it = f(save)

    (all_idxd_complete_state_setq, bimapping4complete_st) = idxd_setq_ex5iterable(it, duplicated_ok=True, to_send_either_idx=True)
    ls

    ist2iv2next_ist = SortedDict({
        all_idxd_complete_state_setq[j4st]
            #idxd_st
        :SortedDict({iv:
            all_idxd_complete_state_setq[j4next_st]
            #idxd_next_st
            for (iv, j4next_st) in iv2j4next_st.items()
        }) for (j4st, iv2j4next_st) in ls
        })
    return (all_idxd_complete_state_setq, bimapping4complete_st, ist2iv2next_ist)
#def cached_calc_all_idxd_state_setq4LR0_ex



#def mk_raw_bireference_multiplicity(grouped_grammar, /):
def cached_mk_raw_bireference_multiplicity(grouped_grammar, /):
    'GroupedGrammar -> asif_bireference_multiplicity/(iiir2child_iv2multiplicity, child_iv2iiir2multiplicity)/(idxd_innidxd_production_rule2idxd_vocabulary_symbol2multiplicity,idxd_vocabulary_symbol2idxd_innidxd_production_rule2multiplicity)/({IndexedHashable<InnerIndexedProductionRule>:{IndexedHashable<VocabularySymbol>:pint}}, {IndexedHashable<VocabularySymbol>:{IndexedHashable<InnerIndexedProductionRule>:pint}})'
    check_type_is(GroupedGrammar, grouped_grammar)
    return get_or_cache_eresult8lazy_property_(grouped_grammar, cached_mk_raw_bireference_multiplicity, _mk_raw_bireference_multiplicity)
def _mk_raw_bireference_multiplicity(grouped_grammar, /):
    iv2iiir_set = grouped_grammar.idxd_nonterminal_symbol2idxd_innidxd_production_rule_set
    iiir2child_iv2multiplicity = {}
    for iv, iiir_set in iv2iiir_set.items():
        for iiir in iiir_set:
            idxd_vocabulary_symbol_seq = child_iv_seq5iiir(iiir)
            iv2multiplicity = iiir2child_iv2multiplicity[iiir] = {}
            for iv in idxd_vocabulary_symbol_seq:
                multiplicity = iv2multiplicity.get(iv, 0)
                iv2multiplicity[iv] = multiplicity+1

    iiir2child_iv2multiplicity
        #forward_reference_multiplicity

    all_iv_setq = grouped_grammar.idxd_vocabulary_symbol_setq
    child_iv2iiir2multiplicity = {iv:{} for iv in all_iv_setq}
    for iiir, iv2multiplicity in iiir2child_iv2multiplicity.items():
        for iv, multiplicity in iv2multiplicity.items():
            child_iv2iiir2multiplicity[iv][iiir] = multiplicity

    child_iv2iiir2multiplicity
        #backward_reference_multiplicity
    SortedDict
    iiir2child_iv2multiplicity = SortedDict(fmap4dict_value(SortedDict, iiir2child_iv2multiplicity))
    child_iv2iiir2multiplicity = SortedDict(fmap4dict_value(SortedDict, child_iv2iiir2multiplicity))
    return (iiir2child_iv2multiplicity, child_iv2iiir2multiplicity)
#end-def cached_mk_raw_bireference_multiplicity(grouped_grammar, /):
class BireferenceMultiplicity:
    'bireference_multiplicity'
    def __init__(sf, grouped_grammar, /):
        if 1:
            # !! now:asif_cached_property
            (iiir2child_iv2multiplicity, child_iv2iiir2multiplicity) = cached_mk_raw_bireference_multiplicity(grouped_grammar)
        else:
            check_type_is(GroupedGrammar, grouped_grammar)
            (iiir2child_iv2multiplicity, child_iv2iiir2multiplicity) = grouped_grammar.raw_bireference_multiplicity
        sf._gmmr = grouped_grammar
        sf._fwd = iiir2child_iv2multiplicity
        sf._bwd = child_iv2iiir2multiplicity
    def __repr__(sf, /):
        return repr_helper(sf, sf._gmmr)
    @property
    def grouped_grammar(sf, /):
        return sf._gmmr
    @property
    def iiir2child_iv2multiplicity(sf, /):
        return sf._fwd
    @property
    def child_iv2iiir2multiplicity(sf, /):
        return sf._bwd

    def clone_iiir2child_iv2multiplicity(sf, /):
        return fmap4dict_value(dict, sf.iiir2child_iv2multiplicity)
    def clone_child_iv2iiir2multiplicity(sf, /):
        return fmap4dict_value(dict, sf.child_iv2iiir2multiplicity)




#from seed.graph.U2Vtc_To_DigraphABC import IntU2Vtc_To_Digraph
#from seed.graph.strong_connected_components import decompose_to_strong_connected_components_in_reversed_topological_ordering
#IntU2Vtc_To_Digraph.from_vertex_pairs(uv_pairs..., range(num_vertices4asif_dgraph))
#decompose_to_strong_connected_components_in_reversed_topological_ordering
+oo
def __():
  def mk__node2min_oolen_sentence(bireference_multiplicity, /):
    'BireferenceMultiplicity -> node2min_oolen/{node:oolen} #[node==idxd_either_iv_iiir/IndexedHashable<either_iv_iiir/(Either IndexedHashable<VocabularySymbol> IndexedHashable<InnerIndexedProductionRule>)>] #[oolen==oolen_sentence :: (+oo|uint)]'

  def mk__node2min_oolen_sentence__respectively_ex(bireference_multiplicity, /):
    '[#O(M+NlogN):[M==len(all_iv_setq)][N==len(all_iiir_setq)]#] => BireferenceMultiplicity -> ((iv2min_oolen, iiir2min_oolen), (iv2nullable, iiir2nullable))/(({iv:oolen}, {iiir:oolen}), ({iv:nullable}, {iiir:nullable})) #[iv :: IndexedHashable<VocabularySymbol>] #[iiir :: IndexedHashable<InnerIndexedProductionRule>] #[oolen==oolen_sentence :: (+oo|uint)] #[nullable :: bool]'
    check_type_is(BireferenceMultiplicity, bireference_multiplicity)

    child_iv2iiir2multiplicity = bireference_multiplicity.child_iv2iiir2multiplicity
    iiir2child_iv2multiplicity = bireference_multiplicity.iiir2child_iv2multiplicity
    grouped_grammar = bireference_multiplicity.grouped_grammar

#def mk__node2min_oolen_sentence__respectively_ex(grouped_grammar, /):
def cached_mk__node2min_oolen_sentence__respectively_ex(grouped_grammar, /):
    '[#O(M+NlogN):[M==len(all_iv_setq)][N==len(all_iiir_setq)]#] => GroupedGrammar -> ((iv2min_oolen, iiir2min_oolen), (iv2nullable, iiir2nullable))/(({iv:oolen}, {iiir:oolen}), ({iv:nullable}, {iiir:nullable})) #[iv :: IndexedHashable<VocabularySymbol>] #[iiir :: IndexedHashable<InnerIndexedProductionRule>] #[oolen==oolen_sentence :: (+oo|uint)] #[nullable :: bool]'
    # [iv2min_oolen==idxd_vocabulary_symbol2min_oolen_sentence]
    # [iv2nullable==idxd_vocabulary_symbol2is_nullable]

    check_type_is(GroupedGrammar, grouped_grammar)
    return get_or_cache_eresult8lazy_property_(grouped_grammar, cached_mk__node2min_oolen_sentence__respectively_ex, _mk__node2min_oolen_sentence__respectively_ex)
def _mk__node2min_oolen_sentence__respectively_ex(grouped_grammar, /):
    grouped_grammar
    (iiir2child_iv2multiplicity, child_iv2iiir2multiplicity) = cached_mk_raw_bireference_multiplicity(grouped_grammar)
        # !! now:asif_cached_property
    all_iT_set = grouped_grammar.idxd_terminal_symbol_set
    all_iN_set = grouped_grammar.idxd_nonterminal_symbol_set
    iN2child_iiir_set = grouped_grammar.idxd_nonterminal_symbol2idxd_innidxd_production_rule_set
    all_iiir_setq = grouped_grammar.idxd_innidxd_production_rule_setq
    all_iv_setq = grouped_grammar.idxd_vocabulary_symbol_setq


    r'''[[[
eval order - simplified:
    ##
    ##first phase: no +oo
    ##
    iiir2min_len
    heap :: [(min_len, iiir)]
    child_iv2iiir_set
    iiir2len_unsettled_child_iv_set
    iv2min_len

    callback/hook:
    f0:=when:[iiir2len_unsettled_child_iv_set[iiir] := 0]:
        iiir2min_len[iiir] := ...
        heap.heappush(...)
    f1:=when:[iv2min_len[iv] := ...]:
        for iiir in child_iv2iiir_set[iv]:
            iiir2len_unsettled_child_iv_set[iiir] -= 1
                #call:f0
    init:
        heap = []
        iiir2min_len = {}
        child_iv2iiir_set
    init:
        iiir2len_unsettled_child_iv_set
                #call:f0
    init:
        iv2min_len = {}
        for iv in all_iT_set:
            iv2min_len[iv] = 1
                #call:f1
                    #f1:call:f0
    while heap:
        (min_len, iiir) = heap.heappop()
        iv = iiir.lhs
        if not iv in iv2min_len:
            iv2min_len[iv] = min_len
                #call:f1
                    #f1:call:f0
    ##
    ##second phase: fill +oo
    ##
    iv2min_oolen = {**iv2min_len}
    iiir2min_oolen = {**iiir2min_len}
    for iv in all_iN_set:
        iv2min_oolen.setdefault(iv, +oo)
    for iiir in all_iiir_setq:
        iiir2min_oolen.setdefault(iiir, +oo)

    ##
    ##third phase: validate
    ##
    assert len(iiir2min_oolen) == len(all_iiir_setq)
    assert len(iv2min_oolen) == len(all_iv_setq)
    for iiir in all_iiir_setq:
        assert iiir2min_oolen[iiir] == sum(iv2min_oolen[iv] for iv in iiir.rhs)
    for iv in all_iT_set:
        assert iv2min_oolen[iv] == 1
    for iv in all_iN_set:
        assert iv2min_oolen[iv] == min(iiir2min_oolen[iiir] for iiir in iN2child_iiir_set.get(iv), default=+oo)

<<==:
eval order:
    + [min_oolen<node> := eval min_oolen whose args are all known already]
    + loop until no unknown:
        + [upperbound4min_oolen<iN> := min known parallel branch]
        + [global_min_oolen4iN6curr := min global upperbound4min_oolen<iN> for iN in all_unknown_iN_set]
        + [min_oolen<iN> := global_min_oolen4iN6curr if upperbound4min_oolen<iN> == global_min_oolen4iN6curr]
            !! [each unknown branch/rule contains at least one unknown iN]
            => [min_oolen<unknown branch/rule> >= global_min_oolen4iN6curr]
            => [min_oolen<unknown iN> >= min{upperbound4min_oolen<the unknown iN>, global_min_oolen4iN6curr} >= global_min_oolen4iN6curr]
            => [[upperbound4min_oolen<unknown iN> == global_min_oolen4iN6curr] -> [min_oolen<the unknown iN> == global_min_oolen4iN6curr]]
        !! each round: fix at least one iN
        => loop will stop
    #]]]'''#'''

    child_iv2iiir_set = fmap4dict_value(set, child_iv2iiir2multiplicity)
    iiir2len_unsettled_child_iv_set = fmap4dict_value(len, iiir2child_iv2multiplicity)

    iiir2min_len = {}
    heap = Heap([], key=fst)
    def f0(iiir, /):
        if not iiir2len_unsettled_child_iv_set.pop(iiir) == 0:raise 000
        min_len = sum(iv2min_len[iv] for iv in child_iv_seq5iiir(iiir))
        iiir2min_len[iiir] = min_len
        heap.heappush((min_len, iiir))
    def f1(iv, min_len, /):
        if iv in iv2min_len:raise 000
        iv2min_len[iv] = min_len
        for iiir in child_iv2iiir_set[iv]:
            iiir2len_unsettled_child_iv_set[iiir] -= 1
            if iiir2len_unsettled_child_iv_set[iiir] == 0:
                f0(iiir)

    for iiir, sz in iiir2len_unsettled_child_iv_set.items():
        if sz == 0:
            f0(iiir)

    iv2min_len = {}
    for iv in all_iT_set:
        f1(iv, 1)

    while heap:
        (min_len, iiir) = heap.heappop()
        iv = lhs_iv5iiir(iiir)
        if not iv in iv2min_len:
            f1(iv, min_len)

    iv2min_oolen = iv2min_len
    iiir2min_oolen = iiir2min_len
    del iiir2min_len, iv2min_len

    for iv in all_iN_set:
        iv2min_oolen.setdefault(iv, +oo)
    for iiir in all_iiir_setq:
        iiir2min_oolen.setdefault(iiir, +oo)
    iv2min_oolen
    iiir2min_oolen


    #validate:
    assert len(iiir2min_oolen) == len(all_iiir_setq)
    assert len(iv2min_oolen) == len(all_iv_setq)

    for iiir in all_iiir_setq:
        assert iiir2min_oolen[iiir] == sum(iv2min_oolen[iv] for iv in child_iv_seq5iiir(iiir))

    for iv in all_iT_set:
        assert iv2min_oolen[iv] == 1

    for iv in all_iN_set:
        assert iv2min_oolen[iv] == min((iiir2min_oolen[iiir] for iiir in iN2child_iiir_set.get(iv, '')), default=+oo)

    iv2nullable = fmap4dict_value(not_, iv2min_oolen)
    iiir2nullable = fmap4dict_value(not_, iiir2min_oolen)

    iv2nullable = SortedDict(iv2nullable)
    iiir2nullable = SortedDict(iiir2nullable)
    iv2min_oolen = SortedDict(iv2min_oolen)
    iiir2min_oolen = SortedDict(iiir2min_oolen)
    return ((iv2min_oolen, iiir2min_oolen), (iv2nullable, iiir2nullable))
#end-def mk__node2min_oolen_sentence__respectively_ex(bireference_multiplicity, /):
#end-def cached_mk__node2min_oolen_sentence__respectively_ex(grouped_grammar, /):

def cached_mk__iv2min_oolen(grouped_grammar, /):
    '[#O(M+NlogN):[M==len(all_iv_setq)][N==len(all_iiir_setq)]#] => GroupedGrammar -> iv2min_oolen/{iv:oolen} #[iv :: IndexedHashable<VocabularySymbol>] #[oolen==oolen_sentence :: (+oo|uint)]'
    ((iv2min_oolen, iiir2min_oolen), (iv2nullable, iiir2nullable)) = cached_mk__node2min_oolen_sentence__respectively_ex(grouped_grammar)
    return iv2min_oolen
def cached_mk__iv2nullable(grouped_grammar, /):
    '[#O(M+NlogN):[M==len(all_iv_setq)][N==len(all_iiir_setq)]#] => GroupedGrammar -> iv2nullable/{iv:nullable} #[iv :: IndexedHashable<VocabularySymbol>] #[nullable :: bool]'
    ((iv2min_oolen, iiir2min_oolen), (iv2nullable, iiir2nullable)) = cached_mk__node2min_oolen_sentence__respectively_ex(grouped_grammar)
    return iv2nullable

#def mk__node2head_iv_set__respectively_ex(grouped_grammar, /):
def cached_mk__node2head_iv_set__respectively_ex(grouped_grammar, /):
    r'''[[[
    -> ((iv2head_iv_set, iiir2head_iv_set), (iv2head_iT_set, iiir2head_iT_set))
    #??? -> iv2head_iv_set/SortedDict{iv:SortedSet{iv}}

FIRST_set<iv> = head_iT_set4iv<iv> == iv2head_iT_set[iv]
    head_iT_set4iv
    head_iT_set4iiir
    head_iv_set4iv
    head_iv_set4iiir
    #
    iv2head_iT_set
    iiir2head_iT_set
    iv2head_iv_set
    iiir2head_iv_set
    #]]]'''#'''
    check_type_is(GroupedGrammar, grouped_grammar)
    return get_or_cache_eresult8lazy_property_(grouped_grammar, cached_mk__node2head_iv_set__respectively_ex, _mk__node2head_iv_set__respectively_ex)
def _mk__node2head_iv_set__respectively_ex(grouped_grammar, /):
    from seed.graph.strong_connected_components import decompose_to_strong_connected_components_in_reversed_topological_ordering
    from seed.graph.U2Vtc_To_DigraphABC import ObjU2Vtc_To_Digraph

    def f():
        '-> Iter (lhs_iv, child_iv7head) #[duplicated_ok:=True]'
        iv2nullable = cached_mk__iv2nullable(grouped_grammar)
        for iiir in grouped_grammar.idxd_innidxd_production_rule_setq:
            lhs_iv = lhs_iv5iiir(iiir)
            child_iv_seq = child_iv_seq5iiir(iiir)
            for child_iv7head in child_iv_seq:
                # [duplicated_ok:=True]
                yield (lhs_iv, child_iv7head)
                if not iv2nullable[child_iv7head]:
                    break
    #end-def f():

    uv_pairs = set(f())
    dgraph = ObjU2Vtc_To_Digraph.from_vertex_pairs(uv_pairs, grouped_grammar.idxd_vocabulary_symbol_setq)
    strong_connected_components = decompose_to_strong_connected_components_in_reversed_topological_ordering(dgraph)
    iv_set_seq = mk_tuple(map(SortedSet, strong_connected_components))


    all_iT_set = grouped_grammar.idxd_terminal_symbol_set
    all_iN_set = grouped_grammar.idxd_nonterminal_symbol_set
    all_dead_iN_set = cached_mk__dead_nonterminal_symbol_set(grouped_grammar)

    ######################
    #mk:_iv2head_iv_set
    ######################

    #fill for terminal_symbol
    _iv2head_iv_set = {iT:{iT} for iT in all_iT_set}

    #fill for +oo/dead-lhs_iv
    s = set()
    for iv in all_dead_iN_set:
        _iv2head_iv_set[iv] = s

    #fill for live-lhs_iv
    for iv_set in iv_set_seq:
        # [here:iv is iN indeed]
        # [iv_set element has same head_iv_set]
        #
        head_iv_set = set()
        for iv in iv_set:
            vtx = iv
            heads4iv = dgraph.vertex2iter_neighbors(vtx)
                # [edge <=> (lhs_iv, child_iv7head)]
            head_iv_set.update(heads4iv)
        for head_iv in sorted(head_iv_set):
            head_iv_set |= _iv2head_iv_set[head_iv]
                # !! [iv_set_seq 6 reversed_topological_ordering]
                # => computation in order
                # => no:KeyError
        for iv in iv_set:
            _iv2head_iv_set[iv] = head_iv_set
    _iv2head_iv_set



    ######################
    #mk:iv2head_iv_set
    ######################

    #fill for terminal_symbol
    iv2head_iv_set = {iT:SortedSet([iT]) for iT in all_iT_set}

    #fill for +oo/dead-lhs_iv
    s = SortedSet('')
    for iv in all_dead_iN_set:
        iv2head_iv_set[iv] = s

    #fill for live-lhs_iv
    for iv_set in iv_set_seq:
        for iv in iv_set:
            break
        else:
            raise 000
        head_iv_set = _iv2head_iv_set[iv]
        s = SortedSet(head_iv_set)
        for iv in iv_set:
            iv2head_iv_set[iv] = s


    #to:SortedDict
    iv2head_iv_set = SortedDict(iv2head_iv_set)




    #[_iv2head_iv_set :: {iv:{iv}}]
    #[iv2head_iv_set :: SortedDict{iv:SortedSet{iv}}]
    _iv2head_iv_set #used in (mk:iiir2head_iv_set)
    iv2head_iv_set

    ######################
    #mk:iiir2head_iv_set
    ######################
    def g():
        '-> _iiir2head_iv_set/{iiir:{iv}}'
        iv2nullable = cached_mk__iv2nullable(grouped_grammar)
        _iiir2head_iv_set = {}
        for iiir in grouped_grammar.idxd_innidxd_production_rule_setq:
            child_iv_seq = child_iv_seq5iiir(iiir)
            head_iv_set = set()
            for child_iv7head in child_iv_seq:
                # [duplicated_ok:=True]
                head_iv_set |= _iv2head_iv_set[child_iv7head]
                if not iv2nullable[child_iv7head]:
                    break
            _iiir2head_iv_set[iiir] = head_iv_set
        return _iiir2head_iv_set
    #end-def g():
    _iiir2head_iv_set = g()
    iiir2head_iv_set = SortedDict(fmap4dict_value(SortedSet, _iiir2head_iv_set))




    #[_iiir2head_iv_set :: {iiir:{iv}}]
    #[iiir2head_iv_set :: SortedDict{iiir:SortedSet{iv}}]
    _iiir2head_iv_set
    iiir2head_iv_set

    ######################
    ######################
    #[iiir2head_iv_set :: SortedDict{iiir:SortedSet{iv}}]
    #[iv2head_iv_set :: SortedDict{iv:SortedSet{iv}}]
    ######################
    ######################
    def iv_set2iT_set(iv_set, /):
        (iT_set, iN_set) = group__idxd_vocabulary_symbol_set_(iv_set)
        return iT_set
    iv2head_iT_set = SortedDict(fmap4dict_value(iv_set2iT_set, iv2head_iv_set))
    iiir2head_iT_set = SortedDict(fmap4dict_value(iv_set2iT_set, iiir2head_iv_set))
    ######################
    ######################
    #[iiir2head_iT_set :: SortedDict{iiir:SortedSet{iT}}]
    #[iv2head_iT_set :: SortedDict{iv:SortedSet{iT}}]
    ######################
    ######################

    iv2head_iT_set
    iiir2head_iT_set
    iv2head_iv_set
    iiir2head_iv_set
    return ((iv2head_iv_set, iiir2head_iv_set), (iv2head_iT_set, iiir2head_iT_set))

#end-def cached_mk__node2head_iv_set__respectively_ex(grouped_grammar, /):
r'''[[[
TODO

def detect__same_size_recur:
    initial_state4LR0 = cached_mk_initial_state4LR0(grouped_grammar)
class LR0_Earley_Parser__no_same_size_recur:
#]]]'''#'''

class Error__grammar_has_same_size_recur_nonterminal_symbol(Exception):pass
#def detect__same_size_recur(grouped_grammar, /):
def cached_detect__same_size_recur(grouped_grammar, /):
    '-> (dgraph, reversed_topological_ordering) / (ObjU2Vtc_To_Digraph{vtx/iv, dedge/(lhs_iv,child_iv7same_size)}, [vtx/iv]/tuple) | ^Error__grammar_has_same_size_recur_nonterminal_symbol(dgraph, vtx_cycle/tuple<vtx/iv>)'
    check_type_is(GroupedGrammar, grouped_grammar)
    return get_or_cache_eresult8lazy_property_(grouped_grammar, cached_detect__same_size_recur, _detect__same_size_recur)
def _detect__same_size_recur(grouped_grammar, /):
    from seed.graph.U2Vtc_To_DigraphABC import ObjU2Vtc_To_Digraph
    from seed.graph.DAG import list_a_cycle_or_reversed_topological_ordering #is_DAG, find_one_cycle

    def f():
        '-> Iter (lhs_iv, child_iv7same_size) #[duplicated_ok:=True]'
        iv2nullable = cached_mk__iv2nullable(grouped_grammar)
        for iiir in grouped_grammar.idxd_innidxd_production_rule_setq:
            lhs_iv = lhs_iv5iiir(iiir)
            child_iv_seq = child_iv_seq5iiir(iiir)
            nonnullable_child_iv_ls = [iv for iv in child_iv_seq if not iv2nullable[iv]]
            L = len(nonnullable_child_iv_ls)
            if L == 1:
                # one iv same_size
                [child_iv7same_size] = nonnullable_child_iv_ls
                yield (lhs_iv, child_iv7same_size)
            elif L == 0:
                # all iv same_size
                for child_iv7same_size in child_iv_seq:
                    # [duplicated_ok:=True]
                    yield (lhs_iv, child_iv7same_size)

    uv_pairs = set(f())
    dgraph = ObjU2Vtc_To_Digraph.from_vertex_pairs(uv_pairs, grouped_grammar.idxd_vocabulary_symbol_setq)
    (is_ok, vtc) = cased = list_a_cycle_or_reversed_topological_ordering(dgraph)
        # :: (is_DAG/bool, [vtx])/((False, cycle)|(True, reversed_topological_ordering))
    #either__vtx_cycle__or__reversed_topological_ordering = Either(*cased)
    vtc = tuple(vtc)
    if not is_ok:
        vtx_cycle = vtc
        raise Error__grammar_has_same_size_recur_nonterminal_symbol(dgraph, vtx_cycle)
    reversed_topological_ordering = vtc
    return (dgraph, reversed_topological_ordering)

__all__
from seed.recognize.CFG.Grammar import *
