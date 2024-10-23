#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/regex/NFA5RegexRepr.py
view ../../python3_src/seed/recognize/regex/RegexRepr.py

seed.recognize.regex.NFA5RegexRepr
py -m nn_ns.app.debug_cmd   seed.recognize.regex.NFA5RegexRepr -x
py -m nn_ns.app.doctest_cmd seed.recognize.regex.NFA5RegexRepr:__doc__ -ht


[[
DONE: DFA5NFA
DONE:tmay_color4original_stop_pst --> colors4original_stop_pst
]]


[[
raw_colored_fwd_dgraph
    :: (raw_fwd/{src_pst:{dst_pst:(nullable/bool, [tkey_set])}}, color_scheme/{pst:{color}}, start_pst, stop_pst)
    # may contain unreachable-or-unproductive parts
    # colored pst may be extra/potential stop_pst
        setting:interesting_colors
        setting:whole_tkey_set

clean_colored_fwd_dgraph
    :: (clean_fwd/{src_pst:{dst_pst:(nullable/bool, std_tkey_set/(frozenset|SetRepr_5Intervals){<=whole_tkey_set}){nullable or nonempty-std_tkey_set}}}, interesting_color_scheme/{new_stop_pst:{interesting-color}{nonempty}}, start_pst)
    # repr stop_pst as a special color or turnoff
    # turnoff_original_stop_pst if not colors4original_stop_pst
    # interesting_color_scheme ==>> new_stop_psts/{stop_pst whose has {interesting-color}}
    #
    # no unreachable-or-unproductive parts
    # but removable-relay-pst still exists

compacted_clean_colored_fwd_dgraph
    :: (compacted_fwd/{src_pst:{dst_pst:nonempty-std_tkey_set}}, interesting_color_scheme/{new_stop_pst:{interesting-color}{nonempty}}, start_pst)
    # no unreachable-or-unproductive parts
    # no removable relay pst[#no:nullable#]
    # space(O(N)-->O(N**2))



partitioned_compacted_clean_colored_fwd_dgraph
    :: (partitioned_fwd4NFA/(jpartition2may_src2dst_set/[may {src_pst:{dst_pst}{nonempty}}]{no_neighbor_may_tags_eq}, jpartition2low_boundary/[low_boundary/(-oo|1/[+-]oo+sym)[#no:+oo|sym#]]{sorted,unique}), interesting_color_scheme/{new_stop_pst:{interesting-color}{nonempty}}, start_pst)

    ### :: (partitioned_fwd4NFA/jpartition2may_src2dst_set/[may {src_pst:{dst_pst}{nonempty}}], interesting_color_scheme/{new_stop_pst:{interesting-color}{nonempty}}, start_pst, whole_open_interval_partition/jpartition2open_interval/[open_interval]{sorted,nonoverlapped,merged_if_touched_and_may_tags_eq})


]]





py_adhoc_call   seed.recognize.regex.NFA5RegexRepr   @f


[[
view ../../python3_src/seed/recognize/regex/RegexRepr.py

usage<regex>:
    hollow_regex << regex
    dead_regex | regex
    regex % color
    regex / empty_set_repr[:sym:, min_sym::max_sym]
    regex[0:+oo:1]

usage<set_repr>:
    -set_repr
    empty_set_repr | set_repr
    whole_set_repr & set_repr
    set_repr - set_repr
    empty_set_repr//oo[min_sym::, ::max_sym]
    empty_set_repr[:sym:]
    empty_set_repr[min_sym::max_sym]

]]

>>> from seed.recognize.regex.RegexRepr import hollow_regex, dead_regex, empty_set_repr, whole_set_repr
>>> from seed.recognize.regex.RegexRepr import SetRepr_5Unicode_property
>>> from seed.recognize.regex.NFA5RegexRepr import NFA5RegexRepr
>>> from seed.tiny_.HashedPair import HashedPair, Solo
>>> regex__AsB = (hollow_regex / empty_set_repr[:'a':])[0::] << hollow_regex / empty_set_repr[:'b':] % 999
>>> raw_colored_fwd_dgraph = raw_colored_fwd_dgraph5regex_repr(config:=config4int, regex__AsB, offset:=0)
>>> raw_colored_fwd_dgraph == ({0: {2: (True, [])}, 2: {3: (True, [])}, 3: {6: (True, []), 4: (True, [])}, 6: {7: (False, [SetRepr_5Intervals((Solo('b'),))])}, 7: {1: (True, [])}, 4: {5: (False, [SetRepr_5Intervals((Solo('a'),))])}, 5: {2: (True, [])}}, {7: {999}}, 0, 1)
True
>>> clean_colored_fwd_dgraph = cleanup_raw_colored_fwd_dgraph(config, raw_colored_fwd_dgraph, colors4original_stop_pst:=(), may_interesting_colors:=None, whole_set4tkey:=whole_set_repr)
>>> clean_colored_fwd_dgraph == ({0: {2: (True, SetRepr_5Intervals(()))}, 3: {6: (True, SetRepr_5Intervals(())), 4: (True, SetRepr_5Intervals(()))}, 7: {}, 2: {3: (True, SetRepr_5Intervals(()))}, 5: {2: (True, SetRepr_5Intervals(()))}, 4: {5: (False, SetRepr_5Intervals((oo[97::, 98::],)))}, 6: {7: (False, SetRepr_5Intervals((oo[98::, 99::],)))}}, {7: {999}}, 0)
True
>>> compacted_clean_colored_fwd_dgraph = compact_clean_colored_fwd_dgraph(config, clean_colored_fwd_dgraph, whole_set4tkey)
>>> compacted_clean_colored_fwd_dgraph == ({0: {0: SetRepr_5Intervals((oo[97::, 98::],)), 1: SetRepr_5Intervals((oo[98::, 99::],))}}, {1: frozenset({999})}, 0)
True
>>> partitioned_compacted_clean_colored_fwd_dgraph = partition_compacted_clean_colored_fwd_dgraph(config, compacted_clean_colored_fwd_dgraph)
>>> (partitioned_fwd4NFA, interesting_color_scheme, start_pst) =  partitioned_compacted_clean_colored_fwd_dgraph
>>> partitioned_fwd4NFA == ((None, {0: {0}}, {0: {1}}, None), ((-oo), (1/-oo+97), (1/-oo+98), (1/-oo+99)))  #old: ((None, {0: {0}}, {0: {1}}, None), (oo[:-oo:, 97::], oo[97::, 98::], oo[98::, 99::], oo[99::, :+oo:]))
True
>>> interesting_color_scheme
{1: frozenset({999})}
>>> start_pst
0


>>> nfa__AsB = NFA5RegexRepr(regex__AsB, ())
>>> nfa__AsB
NFA5RegexRepr(RegexRepr_Concatenation(RegexRepr_Repetition(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))), RegexRepr_Colored(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), 999)), frozenset())
>>> str(nfa__AsB) #old:"NFA5RegexRepr(RegexRepr_Concatenation(RegexRepr_Repetition(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))), RegexRepr_Colored(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), 999)), ())[<fwd=((None, {0: {0}}, {0: {1}}, None), (oo[:-oo:, 97::], oo[97::, 98::], oo[98::, 99::], oo[99::, :+oo:]))>][<stop_pst2colors={1: frozenset({999})}>][<start_mst=frozenset({0})>]"
"NFA5RegexRepr(RegexRepr_Concatenation(RegexRepr_Repetition(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))), RegexRepr_Colored(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), 999)), frozenset())[<fwd=((None, {0: {0}}, {0: {1}}, None), ((-oo), (1/-oo+97), (1/-oo+98), (1/-oo+99)))>][<stop_pst2colors={1: frozenset({999})}>][<start_mst=frozenset({0})>]"


>>> nfa__AsB.feeds(None, 'aaabba', key=ord, greedy=False)
(True, 4, frozenset({1}), 4)
>>> nfa__AsB.feeds(None, 'aaabba', key=ord, greedy=True)
(True, 4, frozenset({1}), 5)
>>> nfa__AsB.feeds(None, 'aaabba', key=ord, greedy=False, to_output_colors=True)
(True, 4, frozenset({1}), 4, frozenset({999}), False, False)
>>> nfa__AsB.feeds(None, 'aaabba', key=ord, greedy=True, to_output_colors=True)
(True, 4, frozenset({1}), 5, frozenset({999}), True, False)



>>> regex__A_B = hollow_regex / empty_set_repr[:'a':] % 666 | hollow_regex / empty_set_repr[:'b':] % 999
>>> nfa__A_B = NFA5RegexRepr(regex__A_B, ())

>>> nfa__A_B.feeds(None, 'ab', key=ord, greedy=False, to_output_colors=True)
(True, 1, frozenset({1}), 1, frozenset({666}), False, False)
>>> nfa__A_B.feeds(None, 'ab', key=ord, greedy=True, to_output_colors=True)
(True, 1, frozenset({1}), 2, frozenset({666}), True, False)
>>> nfa__A_B.feeds(None, 'ba', key=ord, greedy=False, to_output_colors=True)
(True, 1, frozenset({2}), 1, frozenset({999}), False, False)
>>> nfa__A_B.feeds(None, 'ba', key=ord, greedy=True, to_output_colors=True)
(True, 1, frozenset({2}), 2, frozenset({999}), True, False)




>>> regex__leAs_geBs = (hollow_regex / empty_set_repr[::'a'])[1::] % 666 | (hollow_regex / empty_set_repr['b'::])[1::] % 999
>>> nfa__leAs_geBs = NFA5RegexRepr(regex__leAs_geBs, ())


#>>> nfa__leAs_geBs.feeds(None, 'ab', key=ord, greedy=False, to_output_colors=True)
#>>> nfa__leAs_geBs.feeds(None, 'ab', key=ord, greedy=True, to_output_colors=True)
#>>> nfa__leAs_geBs.feeds(None, 'ba', key=ord, greedy=False, to_output_colors=True)
#>>> nfa__leAs_geBs.feeds(None, 'ba', key=ord, greedy=True, to_output_colors=True)
#
#
#>>> nfa__leAs_geBs.feeds(None, 'a00b', key=ord, greedy=False, to_output_colors=True)
#>>> nfa__leAs_geBs.feeds(None, 'a00b', key=ord, greedy=True, to_output_colors=True)
#>>> nfa__leAs_geBs.feeds(None, 'bcca', key=ord, greedy=False, to_output_colors=True)
#>>> nfa__leAs_geBs.feeds(None, 'bcca', key=ord, greedy=True, to_output_colors=True)
#




>>> nfa__leAs_geBs.feeds(None, 'ab', key=ord, greedy=False, to_output_colors=True)
(True, 1, frozenset({1}), 1, frozenset({666}), False, False)
>>> nfa__leAs_geBs.feeds(None, 'ab', key=ord, greedy=True, to_output_colors=True)
(True, 1, frozenset({1}), 2, frozenset({666}), True, False)
>>> nfa__leAs_geBs.feeds(None, 'ba', key=ord, greedy=False, to_output_colors=True)
(True, 1, frozenset({2}), 1, frozenset({999}), False, False)
>>> nfa__leAs_geBs.feeds(None, 'ba', key=ord, greedy=True, to_output_colors=True)
(True, 1, frozenset({2}), 2, frozenset({999}), True, False)

>>> nfa__leAs_geBs.feeds(None, 'a00b', key=ord, greedy=False, to_output_colors=True)
(True, 1, frozenset({1}), 1, frozenset({666}), False, False)
>>> nfa__leAs_geBs.feeds(None, 'a00b', key=ord, greedy=True, to_output_colors=True)
(True, 3, frozenset({1}), 4, frozenset({666}), True, False)
>>> nfa__leAs_geBs.feeds(None, 'bcca', key=ord, greedy=False, to_output_colors=True)
(True, 1, frozenset({2}), 1, frozenset({999}), False, False)
>>> nfa__leAs_geBs.feeds(None, 'bcca', key=ord, greedy=True, to_output_colors=True)
(True, 3, frozenset({2}), 4, frozenset({999}), True, False)



>>> jpartition2low_boundary = [-oo, 1/-oo+999, 1/+oo+999]
>>> for sym in [-oo, 1/-oo+999, 999, 1/+oo+999, +oo]:
...     jpartition = bisect__jpartition2low_boundary_(jpartition2low_boundary, sym)
...     print((jpartition, sym))
(0, (-oo))
(0, (1/-oo+999))
(1, 999)
(2, (1/+oo+999))
(2, (+oo))

>>> jpartition2low_boundary = [-oo, 1/+oo+666, 1/+oo+777, 1/-oo+888, 1/-oo+999, 1/+oo+999]
>>> xsyms = jpartition2representative_element__5__jpartition2low_boundary(jpartition2low_boundary)
>>> xsyms
((-oo), (1/+oo+666), (1/+oo+777), 888, 999, (1/+oo+999))
>>> for sym in xsyms:
...     jpartition = bisect__jpartition2low_boundary_(jpartition2low_boundary, sym)
...     print((jpartition, sym))
(0, (-oo))
(1, (1/+oo+666))
(2, (1/+oo+777))
(3, 888)
(4, 999)
(5, (1/+oo+999))


>>> dfa__AsB = DFA5RegexRepr(nfa__AsB)
>>> dfa__A_B = DFA5RegexRepr(nfa__A_B)
>>> dfa__leAs_geBs = DFA5RegexRepr(nfa__leAs_geBs)
>>> dfa__AsB.num_states
2
>>> dfa__A_B.num_states
3
>>> dfa__leAs_geBs.num_states
3
>>> nfa__AsB.num_parallel_states
2
>>> nfa__A_B.num_parallel_states
3
>>> nfa__leAs_geBs.num_parallel_states
3

>>> dfa__AsB
DFA5RegexRepr(NFA5RegexRepr(RegexRepr_Concatenation(RegexRepr_Repetition(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))), RegexRepr_Colored(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), 999)), frozenset()))
>>> str(dfa__AsB)
"DFA5RegexRepr(NFA5RegexRepr(RegexRepr_Concatenation(RegexRepr_Repetition(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))), RegexRepr_Colored(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), 999)), frozenset()))[<fwd=(((-oo), (1/-oo+97), (1/-oo+98), (1/-oo+99)), (None, {0: 0}, {0: 1}, None))>][<stop_st2colors={1: frozenset({999})}>][<tmay_start_st=(0,)>]"


######################
>>> dfa__AsB.feeds__tmay_(None, 'aaabba', key=ord, greedy=False)
(True, 4, (1,), 4)
>>> dfa__AsB.feeds__tmay_(None, 'aaabba', key=ord, greedy=True)
(True, 4, (1,), 5)
>>> dfa__AsB.feeds__tmay_(None, 'aaabba', key=ord, greedy=False, to_output_colors=True)
(True, 4, (1,), 4, frozenset({999}), False, False)
>>> dfa__AsB.feeds__tmay_(None, 'aaabba', key=ord, greedy=True, to_output_colors=True)
(True, 4, (1,), 5, frozenset({999}), True, False)



######################
>>> dfa__A_B.feeds__tmay_(None, 'ab', key=ord, greedy=False, to_output_colors=True)
(True, 1, (1,), 1, frozenset({666}), False, False)
>>> dfa__A_B.feeds__tmay_(None, 'ab', key=ord, greedy=True, to_output_colors=True)
(True, 1, (1,), 2, frozenset({666}), True, False)
>>> dfa__A_B.feeds__tmay_(None, 'ba', key=ord, greedy=False, to_output_colors=True)
(True, 1, (2,), 1, frozenset({999}), False, False)
>>> dfa__A_B.feeds__tmay_(None, 'ba', key=ord, greedy=True, to_output_colors=True)
(True, 1, (2,), 2, frozenset({999}), True, False)



######################
>>> dfa__leAs_geBs.feeds__tmay_(None, 'ab', key=ord, greedy=False, to_output_colors=True)
(True, 1, (1,), 1, frozenset({666}), False, False)
>>> dfa__leAs_geBs.feeds__tmay_(None, 'ab', key=ord, greedy=True, to_output_colors=True)
(True, 1, (1,), 2, frozenset({666}), True, False)
>>> dfa__leAs_geBs.feeds__tmay_(None, 'ba', key=ord, greedy=False, to_output_colors=True)
(True, 1, (2,), 1, frozenset({999}), False, False)
>>> dfa__leAs_geBs.feeds__tmay_(None, 'ba', key=ord, greedy=True, to_output_colors=True)
(True, 1, (2,), 2, frozenset({999}), True, False)

>>> dfa__leAs_geBs.feeds__tmay_(None, 'a00b', key=ord, greedy=False, to_output_colors=True)
(True, 1, (1,), 1, frozenset({666}), False, False)
>>> dfa__leAs_geBs.feeds__tmay_(None, 'a00b', key=ord, greedy=True, to_output_colors=True)
(True, 3, (1,), 4, frozenset({666}), True, False)
>>> dfa__leAs_geBs.feeds__tmay_(None, 'bcca', key=ord, greedy=False, to_output_colors=True)
(True, 1, (2,), 1, frozenset({999}), False, False)
>>> dfa__leAs_geBs.feeds__tmay_(None, 'bcca', key=ord, greedy=True, to_output_colors=True)
(True, 3, (2,), 4, frozenset({999}), True, False)





######################
nfa.feeds4search
nfa__AsB
nfa__A_B
nfa__leAs_geBs
(is_stop, sz4dst, dst_pst2jjhead, sz4read, colors4dst, may(color2minmax_jjhead, minmax_jjhead4colors), known_non_eof, known_eof) = nfa.feeds4search(offset4syms, may_src_pst2jjhead, syms, greedy=True, to_output_colors=True)
>>> nfa__AsB.feeds4search(0, None, 'cccaaabbb', key=ord, locked_begin_at_min=False, greedy=True, to_output_colors=True)
(True, 9, mappingproxy({0: (9, 9), 1: (8, 8)}), 9, frozenset({999}), ({999: (8, 8)}, (8, 8)), False, True)
>>> nfa__AsB.feeds4search(0, None, 'cccaaabbb', key=ord, locked_begin_at_min=True, greedy=True, to_output_colors=True) #before『calc_may_min_jhead()』:(True, 8, mappingproxy({1: (7, 7)}), 9, frozenset({999}), ({999: (7, 7)}, (7, 7)), True, False)
(True, 7, mappingproxy({0: (7, 7), 1: (3, 6)}), 8, frozenset({999}), ({999: (3, 6)}, (3, 6)), True, False)

>>> nfa__A_B.feeds4search(0, None, 'cccaaabbb', key=ord, locked_begin_at_min=True, greedy=True, to_output_colors=True)
(True, 4, mappingproxy({0: (4, 4), 1: (3, 3)}), 5, frozenset({666}), ({666: (3, 3)}, (3, 3)), True, False)
>>> nfa__leAs_geBs.feeds4search(0, None, 'cccaaabbb', key=ord, locked_begin_at_min=True, greedy=True, to_output_colors=True)
(True, 3, mappingproxy({0: (3, 3), 2: (0, 2)}), 4, frozenset({999}), ({999: (0, 2)}, (0, 2)), True, False)
>>> nfa__leAs_geBs.feeds4search(0, None, 'cab', key=ord, locked_begin_at_min=True, greedy=True, to_output_colors=True)
(True, 1, mappingproxy({0: (1, 1), 2: (0, 0)}), 2, frozenset({999}), ({999: (0, 0)}, (0, 0)), True, False)
>>> nfa__leAs_geBs.feeds4search(0, None, 'cccbbbaaa', key=ord, locked_begin_at_min=True, greedy=True, to_output_colors=True)
(True, 6, mappingproxy({0: (6, 6), 2: (0, 5)}), 7, frozenset({999}), ({999: (0, 5)}, (0, 5)), True, False)


######################

#]]]'''
__all__ = r'''
NFA5RegexRepr
DFA5RegexRepr










NFA5RegexRepr
    match4NFA
    fullmatch4NFA
    search4NFA
DFA5RegexRepr
    match4DFA
    fullmatch4DFA

feed4search_
feed_
IConfig4NFA5RegexRepr
    Config4NFA5RegexRepr__int__ISetRepr_IntervalBased
        config4int
    raw_colored_fwd_dgraph5regex_repr
    cleanup_raw_colored_fwd_dgraph
    compact_clean_colored_fwd_dgraph
    partition_compacted_clean_colored_fwd_dgraph
        core_partition_compacted_clean_colored_fwd_dgraph
            partition_whole_set4tkey_
                bisect__jpartition2low_boundary_
jpartition2representative_element__5__jpartition2low_boundary
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property
from itertools import pairwise, chain
from collections import defaultdict
from bisect import bisect_left, bisect_right



from seed.graph.U2Vtc_To_DigraphABC import ObjU2Vtc_To_Digraph# IntU2Vtc_To_Digraph
from seed.graph.strong_connected_components import decompose_to_strong_connected_components_in_reversed_topological_ordering
from seed.types.StackStyleSet import StackStyleSet# MultiSetStyleStack



from seed.tiny_.oo8inf import oo, OpenInterval, OO8inf, Tag_o0o8inv_inf
from seed.recognize.regex.RegexRepr import whole_set_repr
from seed.recognize.regex.RegexRepr import IRegexRepr, ISetRepr_IntervalBased
from seed.recognize.regex.RegexRepr import SetRepr_5Intervals, SetRepr_Union
from seed.recognize.regex.RegexRepr import Colored, HollowTransition, SolidTransition
from seed.tiny import mk_frozenset, mk_tuple, null_tuple, null_frozenset, fst, snd, echo, ifNone, print_err, MapView, null_mapping_view
from seed.tiny_.check import check_pair, check_tmay
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
#from seed.helper.repr_input import repr_helper
from seed.tiny_._Base4repr import _Base4repr #sf._args4repr = (...)
___end_mark_of_excluded_global_names__0___ = ...

class IConfig4NFA5RegexRepr(ABC):
    __slots__ = ()
    @abstractmethod
    def is_empty_set_(sf, sym_set, /):
        '-> bool'
        return bool(sym_set)
    @abstractmethod
    def std_set_(sf, whole_set4tkey, sym_sets, /):
        '-> std_sym_set/std_tkey_set'
    @abstractmethod
    def iter_open_intervals5std_set_(sf, std_sym_set, /):
        'std_sym_set/std_tkey_set -> Iter open_interval'


class Config4NFA5RegexRepr__int__ISetRepr_IntervalBased(IConfig4NFA5RegexRepr):
    '[tkey/sym :: int][sym_set :: ISetRepr_IntervalBased] #see:SetRepr_5Unicode_property'
    __slots__ = ()
    #___no_slots_ok___ = True
    @override
    def is_empty_set_(sf, sym_set, /):
        '-> bool'
        return sym_set.as_cached_SetRepr_5Intervals.known_empty
        return sym_set.known_empty
        return bool(sym_set)
    @override
    def std_set_(sf, whole_set4tkey, sym_sets, /):
        '-> std_sym_set/std_tkey_set'
        s = SetRepr_Union(sym_sets) & whole_set4tkey
        s = s.as_cached_SetRepr_5Intervals
        std_sym_set = SetRepr_5Intervals(intvl.to_then_from_rng(char_ok=True, inf_ok=True) for intvl in s.iter_merged_sorted_nonempty_open_intervals())
        #if 0b001:print_err(s)
        #if 0b001:print_err(std_sym_set)
        assert all((intvl.low == -oo or intvl.low.gt_vs_lt) and (intvl.up == +oo or intvl.up.gt_vs_lt) for intvl in std_sym_set.iter_merged_sorted_nonempty_open_intervals())
        return std_sym_set
    @override
    def iter_open_intervals5std_set_(sf, std_sym_set, /):
        'std_sym_set/std_tkey_set -> Iter open_interval'
        return std_sym_set.iter_merged_sorted_nonempty_open_intervals()
config4int = Config4NFA5RegexRepr__int__ISetRepr_IntervalBased()





def raw_colored_fwd_dgraph5regex_repr(config, regex_repr, offset=0, /):
    'IConfig4NFA5RegexRepr -> IRegexRepr -> raw_colored_fwd_dgraph/(raw_fwd/{src_pst:{dst_pst:(nullable/bool, [tkey_set])}}, color_scheme/{pst:{color}}, start_pst, stop_pst) # may contain unreachable-or-unproductive parts'
    check_type_le(IRegexRepr, regex_repr)
    pst0 = regex_repr.start_parallel_state_(offset)
    pst1 = regex_repr.stop_parallel_state_(offset)
    it = regex_repr.iter_xtransitions_(offset)
    start_pst = pst0
    stop_pst = pst1
    raw_fwd = defaultdict(lambda:defaultdict(lambda:[False, []]))
    color_scheme = defaultdict(set)
    for xtransition in it:
        match xtransition:
            case Colored(color, pst):
                color_scheme[pst].add(color)
            case HollowTransition(src_pst, dst_pst):
                pair = raw_fwd[src_pst][dst_pst]
                pair[0] = True#nullable
            case SolidTransition(src_pst, sym_set, dst_pst):
                if not config.is_empty_set_(sym_set):
                    pair = raw_fwd[src_pst][dst_pst]
                    pair[1].append(sym_set) #[tkey_set]
            case _:
                raise TypeError(type(xtransition))

    raw_fwd = {src:{dst:(nullable, ls4tkey_set) for dst, (nullable, ls4tkey_set) in dst2pair.items()} for src, dst2pair in raw_fwd.items()}
    color_scheme = {pst:color_set for pst, color_set in color_scheme.items()}
    raw_colored_fwd_dgraph = (raw_fwd, color_scheme, start_pst, stop_pst)
    return raw_colored_fwd_dgraph
#end-def raw_colored_fwd_dgraph5regex_repr(config, regex_repr, offset=0, /):

def cleanup_raw_colored_fwd_dgraph(config, raw_colored_fwd_dgraph, colors4original_stop_pst, may_interesting_colors, whole_set4tkey, /):
    'IConfig4NFA5RegexRepr -> raw_colored_fwd_dgraph -> Iter color4old_stop -> may {interesting-color} -> whole_tkey_set -> clean_colored_fwd_dgraph/(clean_fwd/{src_pst:{dst_pst:(nullable/bool, std_tkey_set/(frozenset|SetRepr_5Intervals){<=whole_tkey_set}){nullable or nonempty-std_tkey_set}}}, interesting_color_scheme/{new_stop_pst:{interesting-color}{nonempty}}, start_pst) # repr stop_pst as a special color or turnoff # no unreachable-or-unproductive parts, but removable relay pst still exists'
    # turnoff_original_stop_pst if not colors4original_stop_pst
    # interesting_color_scheme ==>> new_stop_psts/{stop_pst whose has {interesting-color}}
    (raw_fwd, color_scheme, start_pst, stop_pst) = raw_colored_fwd_dgraph
    #interesting_colors
    if not may_interesting_colors is None:
        interesting_colors = may_interesting_colors
    else:
        interesting_colors = (c for pst, colors in color_scheme.items() for c in colors)
    interesting_colors = mk_frozenset(interesting_colors)

    colors4original_stop_pst = mk_frozenset(colors4original_stop_pst) & interesting_colors
    cs = color_scheme.get(stop_pst, null_frozenset)
    if not colors4original_stop_pst <= cs:
        color_scheme = dict(color_scheme)
        color_scheme[stop_pst] = cs | colors4original_stop_pst
    del stop_pst
    del colors4original_stop_pst

    interesting_color_scheme = {pst:color_set & interesting_colors for pst, color_set in color_scheme.items() if color_set}
    interesting_color_scheme = {pst:color_set for pst, color_set in interesting_color_scheme.items() if color_set}
    assert all(interesting_color_scheme.values())

    #if 0b001:print_err(-111, start_pst)
    #if 0b001:print_err(111, interesting_color_scheme)

    whole_set4tkey
    def f(config, raw_fwd, /):
        halfway_fwd = defaultdict(dict)
        for src, dst2pair in raw_fwd.items():
            for dst, (nullable, ls4tkey_set) in dst2pair.items():
                std_tkey_set = config.std_set_(whole_set4tkey, ls4tkey_set)
                if nullable or not config.is_empty_set_(std_tkey_set):
                    halfway_fwd[src][dst] = (nullable, std_tkey_set)
        halfway_fwd = dict(halfway_fwd)
        return halfway_fwd
    def g(config, halfway_fwd, /):
        for src, dst2ex_std_tkey_set in halfway_fwd.items():
            for dst in dst2ex_std_tkey_set:
                yield (src, dst)
        ######################
        ######################
        # to used with "decompose_to_strong_connected_components_in_reversed_topological_ordering" to distinguish "unreachable-or-unproductive parts"
        #
        for new_stop_pst in interesting_color_scheme:
            yield (new_stop_pst, start_pst)

    halfway_fwd = f(config, raw_fwd)
    uv_pairs = g(config, halfway_fwd)
    g = ObjU2Vtc_To_Digraph.from_vertex_pairs(uv_pairs, ())
    vss = decompose_to_strong_connected_components_in_reversed_topological_ordering(g, [start_pst])

    #if 0b001:print_err(222, halfway_fwd)
    #if 0b001:print_err(-333, g)
    #if 0b001:print_err(333, vss)

    for vtc in vss:
        if start_pst in vtc:
            break
    else:
        raise 000
    vtc
    vs = reachable_productive_pst_set = set(vtc)
    #if 0b001:print_err(444, vs)

    interesting_color_scheme = {pst:color_set for pst, color_set in interesting_color_scheme.items() if pst in vs}
    #if 0b001:print_err(555, interesting_color_scheme)

    new_stop_pst_set = interesting_color_scheme.keys()
    if not new_stop_pst_set:
        #raise Exception('dead-regex')???
        vs = reachable_productive_pst_set = {start_pst}

    vs
    clean_fwd = {src:{dst:ex_std_tkey_set for dst, ex_std_tkey_set in dst2ex_std_tkey_set.items() if dst in vs} for src, dst2ex_std_tkey_set in halfway_fwd.items() if src in vs}

    clean_colored_fwd_dgraph = (clean_fwd, interesting_color_scheme, start_pst)
    return clean_colored_fwd_dgraph
#end-def cleanup_raw_colored_fwd_dgraph(config, raw_colored_fwd_dgraph, colors4original_stop_pst, may_interesting_colors, whole_set4tkey, /):







def compact_clean_colored_fwd_dgraph(config, clean_colored_fwd_dgraph, whole_set4tkey, /):
    'IConfig4NFA5RegexRepr -> clean_colored_fwd_dgraph -> whole_tkey_set -> compacted_clean_colored_fwd_dgraph/(compacted_fwd/{src_pst:{dst_pst:nonempty-std_tkey_set}}, interesting_color_scheme/{new_stop_pst:{interesting-color}{nonempty}}, start_pst) # no unreachable-or-unproductive parts, no removable relay pst[#no:nullable#] # space(O(N)-->O(N**2))'
    #pst --> completed_pst_set --> colors & stoppable
    #completed_pst_set --> blocked_pst_set [#no removable relay pst#]
    #==>>:
    #pst --> (colors, stoppable, blocked_pst_set/new_big_pst)
    (clean_fwd, interesting_color_scheme, start_pst) = clean_colored_fwd_dgraph
    def through_(pst, d=clean_fwd, /):
        return {dst for dst, (nullable, std_tkey_set) in d.get(pst, null_mapping_view).items() if nullable}
        return {dst for dst, (nullable, std_tkey_set) in d[pst].items() if nullable}
    def throughout_(pst, /):
        s = StackStyleSet([pst])
        for pst in s.iter_values4closure_(0):
            s.update(through_(pst))
        vs = {*s}
        return vs
    v2vs_ = throughout_
    def vs2colors_(vs, d=interesting_color_scheme, /):
        return mk_frozenset(c for pst in vs for c in d.get(pst, ''))
    ## def vs2tvs_(vs, d=clean_fwd, is_empty_set_=config.is_empty_set_, /):
    ##     return mk_frozenset(src for src in vs for dst, (nullable, std_tkey_set) in d[src].items() if not is_empty_set_(std_tkey_set))
    ## # pst <=> vs <=> (colors, tvs)
    def mk_t2v2s_(d=clean_fwd, is_empty_set_=config.is_empty_set_, /):
        t2v2s = {}
        for src, dst2ex_std_tkey_set in d.items():
            v2s = {}
            for dst, (nullable, std_tkey_set) in dst2ex_std_tkey_set.items():
                if not is_empty_set_(std_tkey_set):
                    v2s[dst] = std_tkey_set
            if v2s:
                t2v2s[src] = v2s
        return t2v2s
    t2v2s = mk_t2v2s_()
    def vs2tvs_(vs, t2v2s=t2v2s, /):
        return mk_frozenset(v for v in vs if v in t2v2s)
    # pst <=> vs <=> (colors, tvs)
    def f(start_pst=start_pst, t2v2s=t2v2s, /):
        v2j4cs_tvs = {}
            #xxx:v0_tv2j4cs_tvs = {}
            #(tv -solid-> dst) but (dst may be not tv)
        cs_tvs_pair_set = StackStyleSet()
        pst_set = StackStyleSet([start_pst])
        for pst in pst_set.iter_values4closure_(0):
            vs = v2vs_(pst)
            colors = vs2colors_(vs)
            tvs = vs2tvs_(vs)
            cs_tvs_pair = (colors, tvs)
            (is_new, j4pair) = cs_tvs_pair_set.add_ex(cs_tvs_pair)
            v2j4cs_tvs[pst] = j4pair#cs_tvs_pair
            #bug:pst_set.update(tvs)
            pst_set.update(v for tv in tvs for v in t2v2s[tv])
        start_and_tv_set = pst_set
        j4pair8start = v2j4cs_tvs[start_pst]
        assert j4pair8start == 0
        return (j4pair8start, cs_tvs_pair_set, v2j4cs_tvs)
    (j4pair8start, cs_tvs_pair_set, v2j4cs_tvs) = f()
    # pst <=> vs <=> (colors, tvs)
    whole_set4tkey
    def g(union_=config.std_set_, w=whole_set4tkey, t2v2s=t2v2s, v2j=v2j4cs_tvs, /):
        j2j2ss = cpc_fwd = defaultdict(lambda:defaultdict(list))
        for j4pair, (cs, tvs) in enumerate(cs_tvs_pair_set):
         for tv in tvs:
          for dst, std_tkey_set in t2v2s[tv].items():
            _j = v2j[dst]
            j2j2ss[j4pair][_j].append(std_tkey_set)
                #assert not is_empty_set_(std_tkey_set)
                #(tv -solid-> dst) but (dst may be not tv)
                # space(O(N)-->O(N**2))
        j2j2ss
        j2j2s = {j:{_j: union_(w,ss) for _j, ss in _j2ss.items()} for j, _j2ss in j2j2ss.items()}
        j2cs = {j:cs for j, cs in enumerate(map(fst, cs_tvs_pair_set)) if cs}
        return (j2cs, j2j2s)
    (j2cs, j2j2s) = g()
    # new-pst :: j4pair
    start_pst = j4pair8start
    interesting_color_scheme = j2cs
    compacted_fwd = j2j2s

    compacted_clean_colored_fwd_dgraph = (compacted_fwd, interesting_color_scheme, start_pst)
    return compacted_clean_colored_fwd_dgraph
#end-def compact_clean_colored_fwd_dgraph(config, clean_colored_fwd_dgraph, whole_set4tkey, /):




def partition_whole_set4tkey_(interval_tag_pairs, /):
    '(Iter (open_interval, tag)){unordered} -> low_boundary__may_tags__pairs/[(low_boundary/(-oo|1/[+-]oo+sym)[#no:+oo|sym#], may {tag})]{sorted,unique,no_neighbor_may_tags_eq}'
    ######################
    '(Iter (open_interval, tag)){unordered} -> open_interval__may_tags__pairs/[(open_interval, may {tag})]{sorted,nonoverlapped,merged_if_touched_and_may_tags_eq}'
    ######################
    r'''[[[
    :: (Iter (open_interval, tag)){unordered} -> open_interval__may_tags__pairs/[(open_interval, may {tag})]{sorted,nonoverlapped,merged_if_touched_and_may_tags_eq}




partition whole_tkey_set
open_interval --> jpartition/uint
    {tag:[open_interval]{merged,sorted,nonempty}} --> (j2partition/[open_interval], j2may_tags/[may {tag}])
    # [tag :: (src_pst,dst_pst)]
    # algo:
    #   flatten --> [(boundary, dst_vs_src, tag)]
    #       sorted: dst before src if same boundary
    #   grouped --> [(boundary, close_vs_open, {tag})]
    #       sorted: close before open if same boundary
    #   partition --> [(open_interval, {tag})]
    #   partition --> [(open_interval, may {tag})]
    #]]]'''#'''
    ######################

    def flatten(interval_tag_pairs, /):
        j = -1
        for open_interval, tag in interval_tag_pairs:
            match open_interval:
                case OpenInterval(low,up):
                    pass
                case _:
                    raise TypeError(type(OpenInterval))
            if not open_interval:
                continue
            j += 1
            #low, up = open_interval
            assert low < up
            # dst_vs_src==close_vs_open==up_vs_low
            yield (up, False, j, tag)
                #config.up before ot.low if config.up==ot.low
            yield (low, True, j, tag)
        return
    ls = sorted(flatten(interval_tag_pairs))
    def merge(ls, /):
        tmp = []
        j2k = {}
        prev_boundary = -oo
        for up_or_low, up_vs_low, j, tag in ls:
            #prev_boundary = tmp[-1][0].up
            old = tmp and up_or_low == prev_boundary
            if not old:
                open_interval = OpenInterval(prev_boundary, up_or_low)
                assert open_interval or (up_vs_low and up_or_low==-oo and not tmp)
                tmp.append((open_interval, set()))
                prev_boundary = up_or_low


            assert tmp
            if up_vs_low:
                low = up_or_low
                j2k[j] = k = len(tmp)-1
                assert low == tmp[k][0].up
            else:
                up = up_or_low
                assert tmp
                k = j2k[j]
                low = tmp[k][0].up
                for i in range(k+1, len(tmp)):
                    tmp[i][1].add(tag)
            assert tmp[-1][0].up == up_or_low
        tmp
        assert not (tmp and tmp[0][0] and tmp[0][1])
        rs = tmp[1:]
        rs = [(open_interval, (mk_frozenset(tags) if tags else None)) for (open_interval, tags) in rs]
        if not rs:
            rs.append((OpenInterval(-oo,+oo), None))
        else:
            if not (low:=rs[0][0].low) == -oo:
                rs.insert(0, (OpenInterval(-oo,low), None))
            ###########
            if not (up:=rs[-1][0].up) == +oo:
                rs.append((OpenInterval(up,+oo), None))

        assert rs
        assert rs[0][0].low == -oo
        assert rs[-1][0].up == +oo

        assert all(map(fst, rs)), rs
        assert all(ab.up == cd.low for ab, cd in pairwise(map(fst, rs))), rs
        assert all(may_tags is None or len(may_tags) > 0 for may_tags in map(snd, rs)), rs
        assert not any(may_tags0 == may_tags1 for may_tags0, may_tags1 in pairwise(map(snd, rs))), rs
        return rs
    #end-def merge(ls, /):
    rs = merge(ls)
    open_interval__may_tags__pairs = rs
    #return open_interval__may_tags__pairs
    ps = low_boundary__may_tags__pairs = mk_tuple((intvl.low, m) for intvl, m in open_interval__may_tags__pairs)
    assert not any(may_tags0 == may_tags1 for may_tags0, may_tags1 in pairwise(map(snd, ps))), ps
    assert ps
    assert ps[0][0] == -oo
    assert ps[-1][0] < +oo
    assert all(a < c for a, c in pairwise(map(fst, ps))), ps
    return low_boundary__may_tags__pairs
#end-def partition_whole_set4tkey_(interval_tag_pairs, /):


def partition_compacted_clean_colored_fwd_dgraph(config, compacted_clean_colored_fwd_dgraph, /):
    'IConfig4NFA5RegexRepr -> compacted_clean_colored_fwd_dgraph -> partitioned_compacted_clean_colored_fwd_dgraph/(partitioned_fwd4NFA/(jpartition2may_src2dst_set/[may {src_pst:{dst_pst}{nonempty}}]{no_neighbor_may_tags_eq}, jpartition2low_boundary/[low_boundary/(-oo|1/[+-]oo+sym)[#no:+oo|sym#]]{sorted,unique}), interesting_color_scheme/{new_stop_pst:{interesting-color}{nonempty}}, start_pst)'
    # 'IConfig4NFA5RegexRepr -> compacted_clean_colored_fwd_dgraph -> partitioned_compacted_clean_colored_fwd_dgraph/(partitioned_fwd4NFA/(jpartition2may_src2dst_set/[may {src_pst:{dst_pst}{nonempty}}], whole_open_interval_partition/jpartition2open_interval/[open_interval]{sorted,nonoverlapped,merged_if_touched_and_may_tags_eq}), interesting_color_scheme/{new_stop_pst:{interesting-color}{nonempty}}, start_pst)'
    (compacted_fwd, interesting_color_scheme, start_pst) = compacted_clean_colored_fwd_dgraph
    partitioned_fwd4NFA = core_partition_compacted_clean_colored_fwd_dgraph(config, compacted_fwd)
    partitioned_compacted_clean_colored_fwd_dgraph = (partitioned_fwd4NFA, interesting_color_scheme, start_pst)
    return partitioned_compacted_clean_colored_fwd_dgraph
def core_partition_compacted_clean_colored_fwd_dgraph(config, compacted_fwd, /):
    'IConfig4NFA5RegexRepr -> compacted_fwd -> partitioned_fwd4NFA/(jpartition2may_src2dst_set/[may {src_pst:{dst_pst}{nonempty}}]{no_neighbor_may_tags_eq}, jpartition2low_boundary/[low_boundary/(-oo|1/[+-]oo+sym)[#no:+oo|sym#]]{sorted,unique})'
    def tagged_flatten_(compacted_fwd, f=config.iter_open_intervals5std_set_, /):
        'compacted_fwd/{src_pst:{dst_pst:nonempty-std_tkey_set}} -> interval_tag_pairs/(Iter (open_interval, tag/(src,dst)))'
        for src, dst2std_set in compacted_fwd.items():
            for dst, std_set in dst2std_set.items():
                tag = (src, dst)
                for open_interval in f(std_set):
                    yield (open_interval, tag)
    def group_(may_tags, /):
        'may {tag/(src,dst)} -> may {src:{dst}}'
        if may_tags is None:
            return None
        tags = may_tags
        src_dst_pairs = tags
        d = defaultdict(set)
        for (src, dst) in src_dst_pairs:
            d[src].add(dst)
        may_src2dst_set = dict(d)
        return may_src2dst_set
    interval_tag_pairs = tagged_flatten_(compacted_fwd)
    #open_interval__may_tags__pairs = partition_whole_set4tkey_(interval_tag_pairs)
    #jpartition2open_interval = mk_tuple(map(fst, open_interval__may_tags__pairs))
    #jpartition2may_src2dst_set = mk_tuple(map(group_, map(snd, open_interval__may_tags__pairs)))

    low_boundary__may_tags__pairs = partition_whole_set4tkey_(interval_tag_pairs)
    jpartition2low_boundary = mk_tuple(map(fst, low_boundary__may_tags__pairs))
    jpartition2may_src2dst_set = mk_tuple(map(group_, map(snd, low_boundary__may_tags__pairs)))

    partitioned_fwd4NFA = (jpartition2may_src2dst_set, jpartition2low_boundary)
    return partitioned_fwd4NFA
#end-def core_partition_compacted_clean_colored_fwd_dgraph(config, compacted_fwd, /):
#end-def partition_compacted_clean_colored_fwd_dgraph(config, compacted_clean_colored_fwd_dgraph, /):

def jpartition2representative_element__5__jpartition2low_boundary(jpartition2low_boundary, /):
    'jpartition2low_boundary -> jpartition2representative_element/[xboundary/(sym|boundary)]  # [jpartition2low_boundary :: [low_boundary/(-oo|1/[+-]oo+sym)[#no:+oo|sym#]]{sorted,unique}] # [xboundary :: (sym|Tag_o0o8inv_inf|OO8inf)]'
    jpartition2representative_element = mk_tuple(OpenInterval(low, up).the_min_or_raise for low, up in pairwise(chain(jpartition2low_boundary, [+oo])))
    return jpartition2representative_element

_Ts4feed = (OO8inf, Tag_o0o8inv_inf)
def bisect__jpartition2low_boundary_(jpartition2low_boundary, sym, /):
    'jpartition2low_boundary -> tkey/sym -> jpartition/uint  # [jpartition2low_boundary :: [low_boundary/(-oo|1/[+-]oo+sym)[#no:+oo|sym#]]{sorted,unique}]'
    #(bisect_left|bisect_right)<k4sym> => delta_j
    # 1/-oo+sym <- (-oo, 1/-oo+sym)
    # 00000+sym <- (1/-oo+sym, 1/+oo+sym)
    # 1/+oo+sym <- (1/+oo+sym, +oo)
    k = None
    zs = jpartition2low_boundary
    if type(sym) in _Ts4feed:
        k4sym = sym
        if type(sym) is Tag_o0o8inv_inf:
            if sym.gt_vs_lt:
                # 1/-oo+sym <- (-oo, 1/-oo+sym)
                bisect_xxx = bisect_left
            else:
                # 1/+oo+sym <- (1/+oo+sym, +oo)
                bisect_xxx = bisect_right
            delta_j = -1
        elif -oo == sym:
            k = 0
        elif +oo == sym:
            k = len(zs) -1
            assert k >= 0
        else:
            raise 000
        assert not k is None or bisect_xxx
    else:
        k4sym = 1/+oo+sym
        # 00000+sym <- (1/-oo+sym, 1/+oo+sym)
        bisect_xxx = bisect_left
        delta_j = -1
    assert not k is None or bisect_xxx
    k4sym
    if k is None:
        j = bisect_xxx(zs, k4sym)# key=OpenInterval.low.fget
        #assert zs
        #assert zs[-1].up == +oo
        #assert zs[0].low == -oo
            #assert -oo < sym
            #assert 0 < j <= len(zs)
        #assert 0 <= j <= len(zs)
        #if j == 0:
        #    assert -oo == sym
        #    raise ValueError(sym)
        #k = j-1
        #assert 0 <= k < len(zs)
        #assert sym in zs[k]
        k = j+delta_j
    k
    assert 0 <= k < len(zs)
    assert sym in OpenInterval(zs[k], zs[k+1] if k+1 < len(zs) else +oo)
    return (jpartition := k)

def _init4feed(partitioned_fwd4NFA, sym, /):
    'partitioned_fwd4NFA -> tkey/sym -> may src2dst_set/{pst:{pst}}'
    (jpartition2may_src2dst_set, jpartition2low_boundary) = partitioned_fwd4NFA
    jpartition = bisect__jpartition2low_boundary_(jpartition2low_boundary, sym)
    may__src2dst_set = jpartition2may_src2dst_set[jpartition]
    return may__src2dst_set
def feed_(partitioned_fwd4NFA, src_mst, sym, /):
    'partitioned_fwd4NFA -> src_mst/{pst} -> tkey/sym -> dst_mst/{pst} # [merged_state <=> {parallel_state}]'
    m = _init4feed(partitioned_fwd4NFA, sym)
    if not m:
        return null_frozenset
    src2dst_set = m
    dst_mst = mk_frozenset(dst_pst for src_pst in src_mst for dst_pst in src2dst_set.get(src_pst, ''))
    return dst_mst
#end-def feed_(partitioned_fwd4NFA, src_mst, sym, /):

def feed4search_(start_mst, partitioned_fwd4NFA, src_pst2jjhead, sym, j4next_sym, /):
    'mst0/{pst} -> partitioned_fwd4NFA -> src_pst2jjhead/{pst:jjhead} -> tkey/sym -> j4next_sym/uint -> dst_pst2jjhead/{pst:jjhead} # [merged_state <=> {parallel_state}] # [jjhead :: (min_jhead, max_jhead)/(uint,uint)]'
    d = dict.fromkeys(start_mst, (j4next_sym, j4next_sym))
    dst_pst2jjhead = MapView(d)
    assert dst_pst2jjhead #<<==now:using『locked』
        #xxx:assert dst_pst2jjhead
        #xxx   <<== locked_begin_at_min
    m = _init4feed(partitioned_fwd4NFA, sym)
    if not m:
        #bug:return null_mapping_view
        return dst_pst2jjhead if dst_pst2jjhead else null_mapping_view
    src2dst_set = m
    #if 0b001: print_err('++start', d)
    #if 0b001: print_err('src_pst2jjhead', src_pst2jjhead)
    #if 0b001: print_err('transition', src2dst_set)
    f = _iadd_merge4jjhead
    for src_pst, jjhead in src_pst2jjhead.items():
        for dst_pst in src2dst_set.get(src_pst, ''):
            f(d, dst_pst, jjhead)
    #if 0b001: print_err('=>return', d)
    return dst_pst2jjhead
#end-def feed4search_(start_mst, partitioned_fwd4NFA, src_pst2jjhead, sym, j4next_sym, /):
def _merge4jjhead(lhs, rhs, /):
    min0, max0 = lhs
    min1, max1 = rhs
    jjhead = (min(min0,min1), max(max0,max1))
    return jjhead
def _iadd_merge4jjhead(d, dst_pst, jjhead, _f=_merge4jjhead, /):
    m = d.get(dst_pst)
    if m:
        jjhead = _f(jjhead, m)
    d[dst_pst] = jjhead


class NFA5RegexRepr(_Base4repr):
    '[mst==merged_state][pst==parallel_state][merged_state <=> {parallel_state}]'
    #def __init__(sf, config, regex_repr, offset=0, /):
    def __init__(sf, main_arg, /, *args):
        'see:init5regex_|init5partitioned_fwd4NFA_'
        if isinstance(main_arg, IRegexRepr):
            sf.init5regex_(main_arg, *args)
        elif isinstance(main_arg, tuple) and len(main_arg) == 2:
            sf.init5partitioned_fwd4NFA_(main_arg, *args)
        else:
            raise TypeError(type(main_arg))
    def init5regex_(sf, regex_repr, colors4original_stop_pst, may_config=None, may_interesting_colors=None, may_whole_set4tkey=None, /):
        'IRegexRepr -> tmay color -> may IConfig4NFA5RegexRepr -> may {color} -> may ISetRepr_IntervalBased -> None'
        #####
        check_type_le(IRegexRepr, regex_repr)
        #####
        colors4original_stop_pst = mk_frozenset(colors4original_stop_pst)
            #for sf._args4repr
        #may_colors4original_stop_pst = None if not colors4original_stop_pst else colors4original_stop_pst

        #####
        config = ifNone(may_config, config4int)
        check_type_le(IConfig4NFA5RegexRepr, config)
        may_config = None if type(config) is Config4NFA5RegexRepr__int__ISetRepr_IntervalBased else config
            #for sf._args4repr


        #####
        whole_set4tkey = ifNone(may_whole_set4tkey, whole_set_repr)
        check_type_le(ISetRepr_IntervalBased, whole_set4tkey)
        whole_set4tkey = whole_set4tkey.as_cached_SetRepr_5Intervals
        may_whole_set4tkey = None if whole_set4tkey.eq__typed_(whole_set_repr) else whole_set4tkey
            #for sf._args4repr
        #####
        may_interesting_colors = None if may_interesting_colors is None else mk_frozenset(may_interesting_colors)
            #for sf._args4repr
        #####

        raw_colored_fwd_dgraph = raw_colored_fwd_dgraph5regex_repr(config, regex_repr, offset:=0)
        clean_colored_fwd_dgraph = cleanup_raw_colored_fwd_dgraph(config, raw_colored_fwd_dgraph, colors4original_stop_pst, may_interesting_colors, whole_set4tkey)
        compacted_clean_colored_fwd_dgraph = compact_clean_colored_fwd_dgraph(config, clean_colored_fwd_dgraph, whole_set4tkey)
        partitioned_compacted_clean_colored_fwd_dgraph = partition_compacted_clean_colored_fwd_dgraph(config, compacted_clean_colored_fwd_dgraph)
        (partitioned_fwd4NFA, interesting_color_scheme, start_pst) =  partitioned_compacted_clean_colored_fwd_dgraph


        #sf._args4repr = (config, regex_repr) if offset == 0 else (config, regex_repr, offset)
        args = [regex_repr, colors4original_stop_pst, may_config, may_interesting_colors, may_whole_set4tkey]
        while args[-1] is None:
            args.pop()
        assert len(args) >= 2
        sf.init5partitioned_fwd4NFA_(partitioned_fwd4NFA, interesting_color_scheme, start_merged_state := mk_frozenset([start_pst]))
        777;    sf._args4repr = (*args,)
    def init5partitioned_fwd4NFA_(sf, partitioned_fwd4NFA, interesting_color_scheme, start_merged_state, /):
        'partitioned_fwd4NFA<pst> -> interesting_color_scheme<pst> -> start_merged_state/mst/{pst} -> None'
        start_merged_state = mk_frozenset(start_merged_state)
        sf._args4repr = (partitioned_fwd4NFA, interesting_color_scheme, start_merged_state)
        sf._fwd = partitioned_fwd4NFA
        sf._stop2cs = interesting_color_scheme
        sf._mst0 = start_merged_state
    def __str__(sf, /):
        return f'{sf!r}[<fwd={sf._fwd}>][<stop_pst2colors={sf._stop2cs}>][<start_mst={sf._mst0}>]'
    @cached_property
    def num_parallel_states(sf, /):
        '-> uint'
        (j2may_pst2psts, j2low) = partitioned_fwd4NFA = sf._fwd
        psts0 = mst0 = sf._mst0
        s = set(psts0)
        for m in j2may_pst2psts:
            if not m:
                continue
            pst2psts = m
            s.update(pst2psts.keys())
            s.update(pst for psts in pst2psts.values() for pst in psts)
        return len(s)

    @property
    def start_merged_state(sf, /):
        '-> mst/{pst}'
        return sf._mst0
    def merged_state2color_set_(sf, mst, /):
        'mst/{pst} -> color_set/{color} # [is_stop := bool(color_set)]'
        return mk_frozenset(sf._iter_cs5mst(mst))
    def _iter_cs5mst(sf, mst, /):
        'mst/{pst} -> Iter color'
        v2cs = sf._stop2cs
        return (c for pst in mst for c in v2cs.get(pst, ''))
    def is_stop_(sf, mst, /):
        'mst/{pst} -> bool'
        for _ in sf._iter_cs5mst(mst):
            return True
        return False
        return bool(sf.merged_state2color_set_(mst))
    def is_dead_(sf, mst, /):
        'mst/{pst} -> bool'
        return not mst
    def feed1(sf, src_mst, sym, /):
        'src_mst/{pst} -> tkey/sym -> dst_mst/{pst}'
        partitioned_fwd4NFA = sf._fwd
        return feed_(partitioned_fwd4NFA, src_mst, sym)
    def feeds(sf, may_src_mst, syms, min_num_feeds=0, /, *, key, greedy:bool, to_output_colors=False):
        'may src_mst/{pst} -> Iter tkey/sym -> uint -> (is_stop/bool, sz4dst, dst_mst/{pst}, sz4read, ?to_output_colors=>colors4dst/{color}?, ?known_non_eof, ?known_eof) # [0 <= sz4dst <= sz4read]'
            # _mst => ' # [eof >= [[[sz4dst < sz4read][not is_dead_(_mst)]]or[[not is_dead_(dst_mst)][not is_stop]]]]'
        check_type_is(bool, greedy)
        check_type_is(bool, to_output_colors)
        syms = _std__syms(key, syms)

        src_mst = ifNone(may_src_mst, sf.start_merged_state)
        mst = mk_frozenset(src_mst)
        ex_syms = enumerate(syms, 1)
        del may_src_mst, src_mst, syms
        sz = 0
        eof = False
        def f(mst, fwd=sf._fwd, ex_syms=ex_syms, /):
            '-> (eof/bool, may mst)'
            nonlocal sz
            for sz, sym in ex_syms:
                mst = feed_(fwd, mst, sym)
                return (False, mst)
            else:
                return (True, None)
        for _ in range(min_num_feeds):
            if not mst:break
            (eof, m) = f(mst)
            if eof:break
            mst = m
        ######################
        r = None
        while mst:
            if sf.is_stop_(mst):
                r = (True, sz, mst)
                if not greedy:
                    break
            (eof, m) = f(mst)
            if eof:break
            mst = m
        if r is None:
            r = (False, sz, mst)

        rx = (*r, sz)
        (is_stop, sz4dst, dst_mst, sz4read) = rx
        assert [0 <= sz4dst <= sz4read]
        assert eof >= ((sz4dst < sz4read and bool(mst)) or (bool(dst_mst) and not is_stop)), (eof, rx)
            #bug:assert eof >= ((sz4dst < sz4read) or (bool(dst_mst) and not is_stop)), (eof, rx)
            # (False, (True, 4, frozenset({1}), 5))
            #       <<== [not mst]
        known_non_eof = sz4dst < sz4read
        known_eof = not known_non_eof and eof
        if to_output_colors:
            colors = sf.merged_state2color_set_(dst_mst)
            return (*rx, colors, known_non_eof, known_eof)

        return rx
    def feeds4search(sf, offset4syms, may_src_pst2jjhead, syms, min_num_feeds=0, /, *, key, locked_begin_at_min:bool, greedy:bool, to_output_colors=False):
        'uint -> may src_pst2jjhead/{pst:jjhead} -> Iter tkey/sym -> uint -> (is_stop/bool, sz4dst, dst_pst2jjhead/{pst:jjhead}, sz4read, ?to_output_colors=>colors4dst/{color}?, ?may (color2minmax_jjhead, minmax_jjhead4colors)?, ?known_non_eof, ?known_eof) # [0 <= sz4dst <= sz4read] # [jjhead :: (min_jhead, max_jhead)/(uint,uint)]'
        check_type_is(bool, locked_begin_at_min)
        check_type_is(bool, greedy)
        check_type_is(bool, to_output_colors)
        syms = _std__syms(key, syms)

        _locked8min = locked_begin_at_min
        mst0 = sf.start_merged_state
        if may_src_pst2jjhead is None:
            jjhead0 = (offset4syms, offset4syms)
            src_pst2jjhead = dict.fromkeys(mst0, jjhead0)
        else:
            src_pst2jjhead = may_src_pst2jjhead
        src_pst2jjhead
        pst2jjhead = MapView(src_pst2jjhead)
        ex_syms = enumerate(syms, 1)
        del may_src_pst2jjhead, src_pst2jjhead, syms
        sz = 0
        eof = False
        locked = False
        def f(pst2jjhead, fwd=sf._fwd, ex_syms=ex_syms, /):
            '-> (eof/bool, may pst2jjhead)'
            nonlocal sz
            for sz, sym in ex_syms:
                pst2jjhead = feed4search_(mst0, fwd, pst2jjhead, sym, offset4syms+sz)
                assert pst2jjhead#or (locked8min and not mst0)
                #if not mst0:
                if locked:
                    may_min_jhead = calc_may_min_jhead(pst2jjhead)
                    if may_min_jhead is None:
                        assert not sf.is_stop_(pst2jjhead)
                        pst2jjhead = null_mapping_view
                    else:
                        min_jhead = may_min_jhead
                        if not the_min_jhead == min_jhead:
                            assert the_min_jhead < min_jhead
                            pst2jjhead = null_mapping_view
                return (False, pst2jjhead)
            else:
                return (True, None)
        def calc_may_min_jhead(pst2jjhead, /):
            v2cs = sf._stop2cs
            return min((min_jhead for pst, (min_jhead, _) in pst2jjhead.items() if v2cs.get(pst, '')), default=None)

        for _ in range(min_num_feeds):
            if not pst2jjhead:break
            (eof, m) = f(pst2jjhead)
            if eof:break
            pst2jjhead = m
        ######################
        r = None
        while pst2jjhead:
            if sf.is_stop_(pst2jjhead.keys()):
                #if mst0 and locked8min:
                if _locked8min and not locked:
                    #mst0 = null_frozenset
                    locked = True
                    _locked8min = False
                    the_min_jhead = calc_may_min_jhead(pst2jjhead)
                    assert not the_min_jhead is None
                r = (True, sz, pst2jjhead)
                if not greedy:
                    break
            (eof, m) = f(pst2jjhead)
            if eof:break
            pst2jjhead = m
        if r is None:
            r = (False, sz, pst2jjhead)

        rx = (*r, sz)
        (is_stop, sz4dst, dst_pst2jjhead, sz4read) = rx
        #(is_stop, sz4dst, dst_pst2jjhead, sz4read, colors4dst, may (color2minmax_jjhead, minmax_jjhead4colors), known_non_eof, known_eof)
        assert [0 <= sz4dst <= sz4read]
        assert eof >= ((sz4dst < sz4read and bool(pst2jjhead)) or (bool(dst_pst2jjhead) and not is_stop)), (eof, rx)
        known_non_eof = sz4dst < sz4read
        known_eof = not known_non_eof and eof
        def __():
            d = color2minmax_jjhead = {}
            v2cs = sf._stop2cs
            for dst_pst, jjhead in dst_pst2jjhead.items():
                for c in v2cs.get(dst_pst, ''):
                    _iadd_merge4jjhead(d, c, jjhead)
            assert d, (dst_pst2jjhead)
            it = iter(d.values())
            jjhead = next(it)
            for _jjhead in it:
                jjhead = _merge4jjhead(jjhead, _jjhead)
            minmax_jjhead4colors = jjhead
            return (color2minmax_jjhead, minmax_jjhead4colors)
        if to_output_colors:
            colors = sf.merged_state2color_set_(dst_pst2jjhead.keys())
            if is_stop:
                mm = (color2minmax_jjhead, minmax_jjhead4colors) = __()
                assert colors == color2minmax_jjhead.keys()
            else:
                mm = None
            return (*rx, colors, mm, known_non_eof, known_eof)

        return rx



    @cached_property
    def as_cached_args4DFA(sf, /):
        '-> (partitioned_fwd4DFA, interesting_color_scheme, tmay_start_state)'
        (jpartition2may_src2dst_set, jpartition2low_boundary) = partitioned_fwd4NFA = sf._fwd
        j2sym = jpartition2representative_element__5__jpartition2low_boundary(jpartition2low_boundary)
        pst2j2psts = defaultdict(lambda:defaultdict(set))
        #for j, m in jpartition2may_src2dst_set.items():
        for j, m in enumerate(jpartition2may_src2dst_set):
            #if m is None:
            if not m:
                continue
            pst2psts = m
            for pst, psts in pst2psts.items():
                pst2j2psts[pst][j] = psts
        pst2j2psts = {pst:dict(j2psts) for pst, j2psts in pst2j2psts.items()}
        mst0 = sf.start_merged_state
        if not mst0:
            jpartition2low_boundary = (-oo,)
            jpartition2may_src2dst = (None,)
            partitioned_fwd4DFA = (jpartition2low_boundary, jpartition2may_src2dst)
            interesting_color_scheme = {}
            tmay_start_state = null_tuple
            return (partitioned_fwd4DFA, interesting_color_scheme, tmay_start_state)
        assert mst0
        st2j2st = {}
        s = StackStyleSet([mst0])
            # == (st2mst/[mst], mst2st/{mst:st})
        st0 = 0
        assert s[st0] == mst0
        for src_st, src_mst in s.iter_items4closure_(0):
            assert src_mst
            js = set()
            for pst in src_mst:
                j2psts = pst2j2psts.get(pst, '')
                js.update(j2psts)
            js
            st2j2st[src_st] = j2st = {}
            for j in js:
                dst_mst = sf.feed1(src_mst, sym:=j2sym[j])
                if dst_mst:
                    (is_new, dst_st) = s.add_ex(dst_mst)
                    j2st[j] = dst_st
            s
            st2j2st
        s
        st2j2st
        #st2mst = [*s]

        j2st2st = [{} for _ in range(len(j2sym))]
        for src_st, j2st in sorted(st2j2st.items()):
            for j, dst_st in sorted(j2st.items()):
                j2st2st[j][src_st] = dst_st
        j2st2st
        jpartition2may_src2dst = mk_tuple(st2st if st2st else None for st2st in j2st2st)
        st2cs = {}
        for st, mst in enumerate(s):
            cs = sf.merged_state2color_set_(mst)
            if cs:
                st2cs[st] = cs
        st2cs
        partitioned_fwd4DFA = (jpartition2low_boundary, jpartition2may_src2dst)
        interesting_color_scheme = st2cs
        tmay_start_state = (st0,)
        return (partitioned_fwd4DFA, interesting_color_scheme, tmay_start_state)
    ######################
    ######################
    ######################
    def fullmatch(nfa, syms, /, *, key:ord, greedy=True):
        'NFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors)'
        return fullmatch4NFA(nfa, syms, key=key, greedy=greedy)
    def match(nfa, syms, /, *, key:ord, greedy=True):
        'NFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors, known_non_eof/bool, known_eof/bool)'
        return match4NFA(nfa, syms, key=key, greedy=greedy)
    ######################
    def search(nfa, syms, /, *, key:ord, greedy=True, offset4syms=0, locked_begin_at_min=True):
        'NFA5RegexRepr -> Iter sym -> may (end/uint, color2minmax_begin/{color:minmax_begin}, minmax_begin4colors/(min_begin, max_begin)/(uint,uint), known_non_eof/bool, known_eof/bool)'
        return search4NFA(nfa, syms, key=key, greedy=greedy, offset4syms=offset4syms, locked_begin_at_min=locked_begin_at_min)
    ######################
    ######################
    ######################
#end-class NFA5RegexRepr(_Base4repr):



class DFA5RegexRepr(_Base4repr):
    def __init__(sf, main_arg, /, *args):
        'see:init5NFA_|init5partitioned_fwd4DFA_'
        if isinstance(main_arg, NFA5RegexRepr):
            sf.init5NFA_(main_arg, *args)
        elif isinstance(main_arg, tuple) and len(main_arg) == 2:
            sf.init5partitioned_fwd4DFA_(main_arg, *args)
        else:
            raise TypeError(type(main_arg))

    def init5NFA_(sf, an_NFA, /):
        'NFA5RegexRepr -> None'
        check_type_le(NFA5RegexRepr, an_NFA)
        (partitioned_fwd4DFA, interesting_color_scheme, tmay_start_state) = an_NFA.as_cached_args4DFA
        sf.init5partitioned_fwd4DFA_(partitioned_fwd4DFA, interesting_color_scheme, tmay_start_state)
        777;    sf._args4repr = (an_NFA,)
    def init5partitioned_fwd4DFA_(sf, partitioned_fwd4DFA, interesting_color_scheme, tmay_start_state, /):
        'partitioned_fwd4DFA(jpartition2low_boundary, jpartition2may_src2dst/[may {st:st}{nonempty}]) -> interesting_color_scheme<st>/{st:{color}{nonempty}} -> tmay_start_state/tmay st -> None'
        #vs:init5partitioned_fwd4NFA_(sf, partitioned_fwd4NFA, interesting_color_scheme, tmay_start_state, /):
        #partitioned_fwd4NFA<pst:=st> ~=~ partitioned_fwd4DFA == (jpartition2low_boundary, jpartition2may_src2dst)
        check_pair(partitioned_fwd4DFA)
        check_tmay(tmay_start_state)
        assert all(interesting_color_scheme.values())
        (jpartition2low_boundary, jpartition2may_src2dst) = partitioned_fwd4DFA
        check_type_is(tuple, jpartition2low_boundary)
        check_type_is(tuple, jpartition2may_src2dst)
        assert len(jpartition2low_boundary) == len(jpartition2may_src2dst) > 0
        assert jpartition2low_boundary[0] == -oo
        assert jpartition2low_boundary[-1] < +oo
        sf._args4repr = (partitioned_fwd4DFA, interesting_color_scheme, tmay_start_state)
        #sf._j2may_st2st = jpartition2may_src2dst
        #sf._j2low = jpartition2low_boundary
        sf._fwd = partitioned_fwd4DFA
        sf._st2cs = interesting_color_scheme
        sf._tm_st0 = tmay_start_state
    def __str__(sf, /):
        return f'{sf!r}[<fwd={sf._fwd}>][<stop_st2colors={sf._st2cs}>][<tmay_start_st={sf._tm_st0}>]'
    @cached_property
    def num_states(sf, /):
        '-> uint'
        (j2low, j2may_st2st) = sf._fwd
        tmay_start_st = sf._tm_st0
        s = set(tmay_start_st)
        for m in j2may_st2st:
            if not m:
                continue
            st2st = m
            s.update(st2st.keys())
            s.update(st2st.values())
        return len(s)
    @property
    def tmay_start_state(sf, /):
        '-> tmay st'
        return sf._tm_st0
    def state2color_set_(sf, st, /):
        'st -> color_set/{color} # [is_stop := bool(color_set)]'
        return sf._st2cs.get(st, null_frozenset)
    def is_stop_(sf, st, /):
        'st -> bool'
        return bool(sf.state2color_set_(st))
    def feed1__tmay_(sf, src_st, sym, /):
        'src_st/st -> sym -> tmay dst_st/st'
        #(jpartition2low_boundary, jpartition2may_src2dst) = partitioned_fwd4DFA = sf._fwd
        (j2low, j2may_st2st) = sf._fwd
        k = bisect__jpartition2low_boundary_(j2low, sym)
        m = j2may_st2st[k]
        if not m:
            return null_tuple
        st2st = m
        m = st2st.get(src_st, Nothing:=object())
        if m is Nothing:
            return null_tuple
        dst_st = m
        return (dst_st,)
    def feeds__tmay_(sf, may_tmay_src_st, syms, min_num_feeds=0, /, *, key, greedy:bool, to_output_colors=False):
        'may tmay src_st/st -> Iter tkey/sym -> uint -> (is_stop/bool, sz4dst, tmay dst_st/st, sz4read, ?to_output_colors=>colors4dst/{color}?, ?known_non_eof, ?known_eof) # [0 <= sz4dst <= sz4read]'
        syms = _std__syms(key, syms)
        tmay_src_st = ifNone(may_tmay_src_st, sf.tmay_start_state)
        check_tmay(tmay_src_st)
        tmay_st = tmay_src_st

        it = enumerate(syms, 1)
        del syms
        sz = 0
        def f(st, it=it, /):
            nonlocal sz
            for sz, sym in it:
                eof = False
                tmay_st = sf.feed1__tmay_(st, sym)
                break
            else:
                eof = True
                tmay_st = null_tuple
            return (eof, tmay_st)
        for _ in range(min_num_feeds):
            if not tmay_st:break
            [st] = tmay_st
            (eof, tm) = f(st)
            if eof:break
            tmay_st = tm
        ######################
        r = None
        while tmay_st:
            [st] = tmay_st
            if sf.is_stop_(st):
                r = (True, sz, tmay_st)
                if not greedy:
                    break
            (eof, tm) = f(st)
            if eof:break
            tmay_st = tm
        if r is None:
            r = (False, sz, tmay_st)

        rx = (*r, sz)
        (is_stop, sz4dst, tmay_dst_st, sz4read) = rx
        assert [0 <= sz4dst <= sz4read]
        assert eof >= ((sz4dst < sz4read and bool(tmay_st)) or (bool(tmay_dst_st) and not is_stop)), (eof, rx)
        known_non_eof = sz4dst < sz4read
        known_eof = not known_non_eof and eof
        if to_output_colors:
            match tmay_dst_st:
                case [dst_st]:
                    colors = sf.state2color_set_(dst_st)
                case []:
                    colors = null_frozenset
                case _:
                    raise 000
            colors
            return (*rx, colors, known_non_eof, known_eof)

        return rx
    ######################
    ######################
    ######################
    def fullmatch(dfa, syms, /, *, key:ord, greedy=True):
        'DFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors)'
        return fullmatch4DFA(dfa, syms, key=key, greedy=greedy)
    def match(dfa, syms, /, *, key:ord, greedy=True):
        'DFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors, known_non_eof/bool, known_eof/bool)'
        return match4DFA(dfa, syms, key=key, greedy=greedy)
    ######################
    #no:def search(dfa, ...)
    ######################
    ######################
    ######################
jpartition2representative_element__5__jpartition2low_boundary
#end-class DFA5RegexRepr(_Base4repr):


def _std__syms(key, syms, /):
    key = ifNone(key, echo)
    if not key is echo:
        syms = map(key, syms)
    return syms

######################
def _fullmatch4XFA(match4XFA, xfa, syms, /, *, key, greedy:bool):
    '(XFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors, known_non_eof/bool, known_eof/bool)) -> XFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors)'
    syms = iter(syms)
    m = match4XFA(xfa, syms, key=key, greedy=greedy)
    if m is None:
        return None
    (sz4span, colors, known_non_eof, known_eof) = m
    assert not (known_eof and known_non_eof)
    if known_non_eof:
        return None
    if not known_eof:
        for _ in syms:
            #not eof:
            return None
        known_eof = True
    assert known_eof
    assert not known_non_eof
    return (sz4span, colors)
#end-def _fullmatch4XFA(match4XFA, xfa, syms, /, *, greedy:bool):
def fullmatch4NFA(nfa, syms, /, *, key, greedy:bool):
    'NFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors)'
    return _fullmatch4XFA(match4NFA, nfa, syms, key=key, greedy=greedy)
def fullmatch4DFA(dfa, syms, /, *, key, greedy:bool):
    'DFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors)'
    return _fullmatch4XFA(match4DFA, dfa, syms, key=key, greedy=greedy)



######################
def match4NFA(nfa, syms, /, *, key, greedy:bool):
    'NFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors, known_non_eof/bool, known_eof/bool)'
    (is_stop, sz4dst, dst_mst, sz4read, colors4dst, known_non_eof, known_eof) = nfa.feeds(may_src_mst:=None, syms, key=key, greedy=greedy, to_output_colors=True)
    if not is_stop:
        return None
    assert colors4dst
    assert not (known_non_eof and known_eof)
    return (sz4span:=sz4dst, colors:=colors4dst, known_non_eof, known_eof)

######################
def search4NFA(nfa, syms, /, *, key, greedy:bool, offset4syms=0, locked_begin_at_min=True):
    'NFA5RegexRepr -> Iter sym -> may (end/uint, color2minmax_begin/{color:minmax_begin}, minmax_begin4colors/(min_begin, max_begin)/(uint,uint), known_non_eof/bool, known_eof/bool)'
    (is_stop, sz4dst, dst_pst2jjhead, sz4read, colors4dst, mm, known_non_eof, known_eof) = nfa.feeds4search(offset4syms, may_src_pst2jjhead:=None, syms, key=key, locked_begin_at_min=locked_begin_at_min, greedy=greedy, to_output_colors=True)
    if not is_stop:
        return None
    (color2minmax_jjhead, minmax_jjhead4colors) = mm
    assert colors4dst
    assert not (known_non_eof and known_eof)
    assert colors4dst == color2minmax_jjhead.keys()
    end = offset4syms + sz4dst
    color2minmax_begin = color2minmax_jjhead
    minmax_begin4colors = minmax_jjhead4colors
    return (end, color2minmax_begin, minmax_begin4colors, known_non_eof, known_eof)





######################
def match4DFA(dfa, syms, /, *, key, greedy:bool):
    'DFA5RegexRepr -> Iter sym -> may (sz4span/uint, colors, known_non_eof/bool, known_eof/bool)'
    (is_stop, sz4dst, tmay_dst_mst, sz4read, colors4dst, known_non_eof, known_eof) = dfa.feeds__tmay_(may_tmay_src_st:=None, syms, key=key, greedy=greedy, to_output_colors=True)
    if not is_stop:
        return None
    assert tmay_dst_mst
    [dst_mst] = tmay_dst_mst
    assert colors4dst
    assert not (known_non_eof and known_eof)
    return (sz4span:=sz4dst, colors:=colors4dst, known_non_eof, known_eof)

######################



__all__
from seed.recognize.regex.NFA5RegexRepr import NFA5RegexRepr, DFA5RegexRepr
from seed.recognize.regex.NFA5RegexRepr import match4NFA, fullmatch4NFA, search4NFA
from seed.recognize.regex.NFA5RegexRepr import match4DFA, fullmatch4DFA
from seed.recognize.regex.NFA5RegexRepr import *
