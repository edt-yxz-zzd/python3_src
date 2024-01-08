#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/avoid_substrs.py
    view ../../python3_src/seed/seq_tools/prefixes2tree.py


seed.seq_tools.avoid_substrs
py -m nn_ns.app.debug_cmd   seed.seq_tools.avoid_substrs -x
py -m nn_ns.app.doctest_cmd seed.seq_tools.avoid_substrs:__doc__ -ff -v

from seed.seq_tools.avoid_substrs import Helper4AutoCalc4AvoidSubstr
from seed.seq_tools.avoid_substrs import check_dual_end_marker_have_no_nonempty_overlaps
from seed.seq_tools.avoid_substrs import strings2prefix_st_tree_ex_

from seed.seq_tools.avoid_substrs import iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_, iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_, iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_

from seed.seq_tools.avoid_substrs import iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_, iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_, iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_, iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_, iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_



[[
20231126:
===
directly
===
bits encode: regex"1{n}[01]*0{n}" where [n>=2] && middle part doesnot contain prefix/suffix
    st:curr suffix regex'(^$)|(((^|0)1{m}|(^|1)0{m})$)', [1 <= m <= n], [0 <= st < 2*n+1]
        special st:
            0 - curr suffix: regex'(^$)'
            n - curr suffix: regex'((^|0)1{n}$)'
                ???
                bug:indeed two states instead of one as definition:
                * curr suffix: regex'(^1{n}$)'
                    intermedia state: next state is '10$'
                * curr suffix: regex'(01{n}$)'
                    dead state: no next state
            2*n - curr suffix: regex'((^|1)0{n}$)'
                #indeed: 2*n - curr suffix: regex'(10{n}$)'
                    terminal state: no next state
            ===
        normal st:
            m - curr suffix: regex'((^|0)1{m}$)' where [1<=m<n]
            m - curr suffix: regex'((^|1)0{m}$)' where [n+1<=m<2*n]
                #indeed: m - curr suffix: regex'(10{m}$)' where [n+1<=m<2*n]
            ===
===
def iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, /, *, with_st2cnt=True, may_args4islice=None):
    #see:iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_{directly:=True}
===
py_adhoc_call   seed.seq_tools.avoid_substrs   ,11:iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_  =2  =2 =1 =1
(0, 0, [1, 0, 0, 0, 0]) # ''
(1, 0, [0, 1, 0, 0, 0]) # '1'
(2, 0, [0, 0, 1, 0, 0]) # '11'
(3, 0, [0, 0, 0, 1, 0]) # '110'
(4, 1, [0, 1, 0, 0, 1]) # '1101', '1100'
(5, 0, [0, 0, 1, 1, 0]) # '11011', '11010'
(6, 1, [0, 1, 0, 0, 1]) # '110101', '110100'
(7, 0, [0, 0, 1, 1, 0]) # '1101011', '1101010'
(8, 1, [0, 1, 0, 0, 1]) # '11010101', '11010100'
(9, 0, [0, 0, 1, 1, 0]) # '110101011', '110101010'
(10, 1, [0, 1, 0, 0, 1]) # '1101010101', '1101010100'
===
]]




[[
avoid_substrs
  e ../../python3_src/seed/seq_tools/prefixes2tree.py
  e ../../python3_src/seed/seq_tools/avoid_substrs.py
  prefixes2tree
    字节串首比特流:额外带宽:
      额定带宽:
        [n>=2]:
          (*): 1{n} 0{n}
          (*): 1{n} (0 [01]{n-2} 1)* (0 [01]{0,n-2} 1) 0{n}
            # if '.' === [01]
            #   (*): 1{n} ([^1] .{n-2} [^0])* ([^1] .{0,n-2} [^0]) 0{n}
      额外带宽:
        即 所有合法串 减去 额定带宽
        即 所有串 减去 中间串含1{n}或0{n}的串 减去 额定带宽
    e ../../python3_src/seed/types/namedtuple.txt
    e ../../python3_src/seed/types/NamedTupleBase.py
]]


[[
k :: hashable representive key for a disjoint subset of partition of subset of alphabet
    eg:
        alphabet : 0bxxxx_xxxx : byte : [0..<2**8]
        sz4alphabet = 2**8
        ks = {0b0xxx_xxxx, 0b10xx_xxxx}
        sz4alphabet4k<0b0xxx_xxxx> = 2**7
        sz4alphabet4k<0b10xx_xxxx> = 2**6
        sz4alphabet4fallback >= 2**8 -2**7 -2**6

st :: uint : state <==> prefix/[k]
hst :: (has_meet_begin_marker/bool, st)
    has_meet_begin_marker donot consider st yet
    #hst2k2hst__as_transition_table
    if not has_meet_begin_marker and not st2is_gt_end_st4begin_marker[st] and st2is_ge_end_st4begin_marker[st]:
        _has_meet_begin_marker = True
    if not has_meet_begin_marker and not st2is_gt_end_st4begin_marker[st] and not st2is_ge_end_st4begin_marker[st]:
        _has_meet_begin_marker = False
    if not has_meet_begin_marker and st2is_gt_end_st4begin_marker[st]:
        raise logic-err
    if has_meet_begin_marker:
        _has_meet_begin_marker = True

string :: [k]
substrs :: [[k]]
st2k2st__as_forward_tree
    #:: {st:{k:st}}
    :: [{k:st}]

三个状态变换:
    ===
    * st2k2st__as_transition_table[]
        被接受的字串:要求:
            #substrs4avoid===strings4forbidden_substr
            * substrs4avoid不得出现
    ===
    * mk_has_meet_begin_marker4post_st()
        用于补完状态变换，完成st到hst的提升
        st2k2st__as_transition_table+mk_has_meet_begin_marker4post_st ==>> hst2k2hst__as_transition_table
    ===
    * hst2k2hst__as_transition_table[]
        被接受的字串:要求:
            #begin_markers===strings4begin_marker
            #end_markers===strings4end_marker
            #substrs4avoid===strings4forbidden_substr
            #
            * 必须以begin_markers其中之一为前缀
            * 必须以end_markers其中之一为后缀
            * begin_markers只出现一次
            * end_markers只出现一次
            * substrs4avoid不得出现
    ===
    [[[
    #[def____permit_pattern4hst8transition_table]:goto
    copy here:
    ===
        #NOTE:[eq |>=| ge&&(not gt) == fst_eq]
        # [fst_eq =[def]= ge&&(not gt)]
        #permit pattern:
        # (False, (not ge)) -> k -> (False, (not ge)||fst_eq)
        # (False, fst_eq) -> k -> (True, [to_del eq]||(not eq))
        # (True, (not eq)) -> k -> (True, [to_del eq]||(not eq))
        ###[hst0 =[def]= (False, st0)]
        ###[hsts4fallback =[def]= [(False, st0), (True, st0)]]
        ###[hst0 MUST BE permitted]
        ###[hsts4fallback MUST BE permitted]
        # (False, st0:(not ge)) -> k -> (False, (not ge)||fst_eq)
        # (True, st0:(not eq)) -> k -> (True, [to_del eq]||not eq)
    ]]]
]]


[[
[vs___7_iter_num_strs_ex]:here
vs:
    iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_: begin_marker=???, end_marker=???, substrs4avoid=???, may_k2sz4alphabet=??? : impl via iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_
        iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_: len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker : begin_marker='1'*len4both_marker, end_marker='0'*len4both_marker, may_k2sz4alphabet={'1':sz4alphabet4k4begin_marker,'0':sz4alphabet4k4end_marker} but impl only count layout_with_std_both_marker : k===cell : sz4alphabet=sz4cell : impl via iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_
            iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_:api is same as api of iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_ : impl via step_()<=>matrix.__mul__
            iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_: num_bits4word, len4both_marker : k===cell===word{num_bits4word} : sz4alphabet=sz4cell=sz4word=2**num_bits4word, sz4alphabet4k4begin_marker=sz4alphabet4k4end_marker=2**(num_bits4word-1) : impl via iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_
        iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_: len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker : begin_marker='1'*len4both_marker, end_marker='0'*len4both_marker, may_k2sz4alphabet={'1':sz4alphabet4k4begin_marker,'0':sz4alphabet4k4end_marker} but impl only count std_layout : k===cell : sz4alphabet=sz4cell
            iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_: num_bits4word, len4both_marker : k===cell===word{num_bits4word} : sz4alphabet=sz4cell=sz4word=2**num_bits4word, sz4alphabet4k4begin_marker=sz4alphabet4k4end_marker=2**(num_bits4word-1) : impl via iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_
                iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_: num_bits4word, len4both_marker : count num_bits4token directly (std_layout only)
]]









__all__
>>> from seed.helper.stable_repr import stable_repr
>>> from seed.helper.stable_repr import stable_repr_print
>>> from seed.helper.stable_repr import stable_repr_print__expand_top_layer
>>> show = lambda x, /:stable_repr_print(None, x)
>>> expand1 = lambda x, /:stable_repr_print__expand_top_layer(None, x)
>>> expand1_islice_ = lambda args4islice, it, /:stable_repr_print__expand_top_layer(None, [*apply_may_args4islice_(args4islice, it)])
>>> list_islice_ = lambda args4islice, it, /:[*apply_may_args4islice_(args4islice, it)]
>>> from seed.seq_tools.avoid_substrs import strings2prefix_st_tree_ex_


def strings2prefix_st_tree_ex_(strings, /):
    '-> (ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_OutTree)'
>>> show(strings2prefix_st_tree_ex_(['111', '000']))
({'0', '1'}, 0, [3, 6], [[], [], [], [0], [], [], [1]], [[0, 1], [0], [0], [0], [1], [1], [1]], [0, 1, 2, 3, 1, 2, 3], [{'0': 4, '1': 1}, {'1': 2}, {'1': 3}, {}, {'0': 5}, {'0': 6}, {}])



>>> (begin_markers, end_markers, substrs4avoid) = ['111'], ['000'], []
>>> setting4multi_cell_token = Setting4MultiCellToken(begin_markers, end_markers, substrs4avoid)
>>> setting4multi_cell_token
<Setting4MultiCellToken(istr2is_begin_marker = [True, False], istr2is_end_marker = [False, True], istr2is_forbidden_substr = [False, False], strings = ['111', '000'])>
>>> (sz4alphabet, may_k2sz4alphabet) = 2, None
>>> sf = Counter4AvoidSubstrs__using_dual_end_delimiter(setting4multi_cell_token, sz4alphabet, may_k2sz4alphabet)
>>> expand1(sf._vars)
{'end_st2istrs'
: [[], [], [], [0], [], [], [1]]
,'istr2end_st'
: [3, 6]
,'ks'
: {'0', '1'}
,'len2sts'
: [[0], [1, 4], [2, 5], [3, 6]]
,'may_k2sz4alphabet'
: None
,'noninit_st2longest_proper_suffix_st'
: [None, 0, 1, 2, 0, 4, 5]
,'noninit_st2st_k_pair__as_InTree'
: [None, (0, '1'), (1, '1'), (2, '1'), (0, '0'), (4, '0'), (5, '0')]
,'st2is_eq_end_st4whole'
: [False, False, False, True, False, False, True]
,'st2istrs'
: [[0, 1], [0], [0], [0], [1], [1], [1]]
,'st2k2st__as_OutTree'
: [{'0': 4, '1': 1}, {'1': 2}, {'1': 3}, {}, {'0': 5}, {'0': 6}, {}]
,'st2k2st__as_transition_table'
: [{'0': 4, '1': 1}, {'0': 4, '1': 2}, {'0': 4, '1': 3}, {'0': 4, '1': 3}, {'0': 5, '1': 1}, {'0': 6, '1': 1}, {'0': 6, '1': 1}]
,'st2len'
: [0, 1, 2, 3, 1, 2, 3]
,'st2suffix_end_sts'
: [[], [], [], [3], [], [], [6]]
}
>>> expand1(sf._vars__export)
{'basic_setting4multi_cell_token'
: Setting4MultiCellToken(istr2is_begin_marker= [True, False], istr2is_end_marker= [False, True], istr2is_forbidden_substr= [False, False], strings= ['111', '000'])
,'hst2k2hst__as_transition_table'
: {(False, 0): {'0': (False, 4), '1': (False, 1)}, (False, 1): {'0': (False, 4), '1': (False, 2)}, (False, 2): {'0': (False, 4), '1': (False, 3)}, (False, 3): {'0': (True, 4), '1': (True, 3)}, (False, 4): {'0': (False, 5), '1': (False, 1)}, (False, 5): {'0': (False, 6), '1': (False, 1)}, (False, 6): {'0': (False, 6), '1': (False, 1)}, (True, 0): {'0': (True, 4), '1': (True, 1)}, (True, 1): {'0': (True, 4), '1': (True, 2)}, (True, 2): {'0': (True, 4), '1': (True, 3)}, (True, 4): {'0': (True, 5), '1': (True, 1)}, (True, 5): {'0': (True, 6), '1': (True, 1)}, (True, 6): {'0': (True, 6), '1': (True, 1)}}
,'k2sz4alphabet'
: {'0': 1, '1': 1}
,'setting4multi_cell_token'
: Setting4MultiCellToken(istr2is_begin_marker= [True, False], istr2is_end_marker= [False, True], istr2is_forbidden_substr= [False, False], strings= ['111', '000'])
,'st0'
: 0
,'st2is_ge_end_st4begin_marker'
: [False, False, False, True, False, False, False]
,'st_info4begin_marker'
: StInfo4BeginMarker(st2is_eq_end_st4begin_marker= [False, False, False, True, False, False, False], st2is_ge_end_st4begin_marker= [False, False, False, True, False, False, False], st2is_gt_end_st4begin_marker= [False, False, False, False, False, False, False], st2prev_substr_end_sts4begin_marker= [[], [], [], [3], [], [], []])
,'st_info4body'
: StInfo4Body(st2is_ge_end_st4end_marker= [False, False, False, False, False, False, True], st2is_ge_end_st4forbidden_substr= [False, False, False, False, False, False, False], st2is_gt_end_st4end_marker= [False, False, False, False, False, False, False])
,'sz4alphabet'
: 2
}
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2**8, [["0b11xx_xxxx"]], [["0b10xx_xxxx"]], [], may_k2sz4alphabet=None, may_args4islice=[6], _ver_=1)])
[(0, 0, {}, ({(False, 0): 1}, {}))
,(1, 0, {}, ({}, {(False, 1): 1}))
,(2, 1, {(True, 2): 1}, ({}, {(True, 0): 254, (True, 2): 1}))
,(3, 254, {(True, 2): 254}, ({}, {(True, 0): 64516, (True, 2): 254}))
,(4, 64516, {(True, 2): 64516}, ({}, {(True, 0): 16387064, (True, 2): 64516}))
,(5, 16387064, {(True, 2): 16387064}, ({}, {(True, 0): 4162314256, (True, 2): 16387064}))
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2**8, [["0b11xx_xxxx"]], [["0b10xx_xxxx"]], [], may_k2sz4alphabet=None, may_args4islice=[6], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({}, {(False, 1): 1}))
,(2, 0, True, 1, {(True, 2): 1}, ({}, {(True, 0): 254, (True, 2): 1}))
,(3, 7, False, 254, {(True, 2): 254}, ({}, {(True, 0): 64516, (True, 2): 254}))
,(4, 15, False, 64516, {(True, 2): 64516}, ({}, {(True, 0): 16387064, (True, 2): 64516}))
,(5, 23, False, 16387064, {(True, 2): 16387064}, ({}, {(True, 0): 4162314256, (True, 2): 16387064}))
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2**8, [["0b11xx_xxxx"]], [["0b10xx_xxxx"]], [], may_k2sz4alphabet={"0b11xx_xxxx":2**6, "0b10xx_xxxx":2**6}, may_args4islice=[6], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({}, {(False, 1): 64}))
,(2, 12, True, 4096, {(True, 2): 4096}, ({}, {(True, 0): 8192, (True, 2): 4096}))
,(3, 19, True, 524288, {(True, 2): 524288}, ({}, {(True, 0): 1048576, (True, 2): 524288}))
,(4, 26, True, 67108864, {(True, 2): 67108864}, ({}, {(True, 0): 134217728, (True, 2): 67108864}))
,(5, 33, True, 8589934592, {(True, 2): 8589934592}, ({}, {(True, 0): 17179869184, (True, 2): 8589934592}))
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2**2, [["0b11xx_xxxx"]], [["0b10xx_xxxx"]], [], may_k2sz4alphabet=None, may_args4islice=[6], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({}, {(False, 1): 1}))
,(2, 0, True, 1, {(True, 2): 1}, ({}, {(True, 0): 2, (True, 2): 1}))
,(3, 1, True, 2, {(True, 2): 2}, ({}, {(True, 0): 4, (True, 2): 2}))
,(4, 2, True, 4, {(True, 2): 4}, ({}, {(True, 0): 8, (True, 2): 4}))
,(5, 3, True, 8, {(True, 2): 8}, ({}, {(True, 0): 16, (True, 2): 8}))
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(3, [["0b11xx_xxxx"]], [["0b10xx_xxxx"]], [], may_k2sz4alphabet=None, may_args4islice=[6], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({}, {(False, 1): 1}))
,(2, 0, True, 1, {(True, 2): 1}, ({}, {(True, 0): 1, (True, 2): 1}))
,(3, 0, True, 1, {(True, 2): 1}, ({}, {(True, 0): 1, (True, 2): 1}))
,(4, 0, True, 1, {(True, 2): 1}, ({}, {(True, 0): 1, (True, 2): 1}))
,(5, 0, True, 1, {(True, 2): 1}, ({}, {(True, 0): 1, (True, 2): 1}))
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2, [["0b11xx_xxxx"]], [["0b10xx_xxxx"]], [], may_k2sz4alphabet=None, may_args4islice=[6], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({}, {(False, 1): 1}))
,(2, 0, True, 1, {(True, 2): 1}, ({}, {(True, 2): 1}))
]

>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2, ["111"], ["000"], [], may_k2sz4alphabet=None, may_args4islice=[12], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({(False, 1): 1}, {}))
,(2, None, None, 0, {}, ({(False, 2): 1}, {}))
,(3, None, None, 0, {}, ({}, {(False, 3): 1}))
,(4, None, None, 0, {}, ({}, {(True, 4): 1}))
,(5, None, None, 0, {}, ({}, {(True, 1): 1, (True, 5): 1}))
,(6, 0, True, 1, {(True, 6): 1}, ({}, {(True, 1): 1, (True, 2): 1, (True, 4): 1, (True, 6): 1}))
,(7, None, None, 0, {}, ({}, {(True, 1): 1, (True, 2): 1, (True, 4): 2, (True, 5): 1}))
,(8, 0, True, 1, {(True, 6): 1}, ({}, {(True, 1): 3, (True, 2): 1, (True, 4): 2, (True, 5): 2, (True, 6): 1}))
,(9, 1, True, 2, {(True, 6): 2}, ({}, {(True, 1): 4, (True, 2): 3, (True, 4): 4, (True, 5): 2, (True, 6): 2}))
,(10, 1, True, 2, {(True, 6): 2}, ({}, {(True, 1): 6, (True, 2): 4, (True, 4): 7, (True, 5): 4, (True, 6): 2}))
,(11, 2, True, 4, {(True, 6): 4}, ({}, {(True, 1): 11, (True, 2): 6, (True, 4): 10, (True, 5): 7, (True, 6): 4}))
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2**2, ["111"], ["000"], [], may_k2sz4alphabet={'0':2,'1':2}, may_args4islice=[12], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({(False, 1): 2}, {}))
,(2, None, None, 0, {}, ({(False, 2): 4}, {}))
,(3, None, None, 0, {}, ({}, {(False, 3): 8}))
,(4, None, None, 0, {}, ({}, {(True, 4): 16}))
,(5, None, None, 0, {}, ({}, {(True, 1): 32, (True, 5): 32}))
,(6, 6, True, 64, {(True, 6): 64}, ({}, {(True, 1): 64, (True, 2): 64, (True, 4): 64, (True, 6): 64}))
,(7, None, None, 0, {}, ({}, {(True, 1): 128, (True, 2): 128, (True, 4): 256, (True, 5): 128}))
,(8, 8, True, 256, {(True, 6): 256}, ({}, {(True, 1): 768, (True, 2): 256, (True, 4): 512, (True, 5): 512, (True, 6): 256}))
,(9, 10, True, 1024, {(True, 6): 1024}, ({}, {(True, 1): 2048, (True, 2): 1536, (True, 4): 2048, (True, 5): 1024, (True, 6): 1024}))
,(10, 11, True, 2048, {(True, 6): 2048}, ({}, {(True, 1): 6144, (True, 2): 4096, (True, 4): 7168, (True, 5): 4096, (True, 6): 2048}))
,(11, 13, True, 8192, {(True, 6): 8192}, ({}, {(True, 1): 22528, (True, 2): 12288, (True, 4): 20480, (True, 5): 14336, (True, 6): 8192}))
]


>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2, ["11"], ["00"], [], may_k2sz4alphabet=None, may_args4islice=[12], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({(False, 1): 1}, {}))
,(2, None, None, 0, {}, ({}, {(False, 2): 1}))
,(3, None, None, 0, {}, ({}, {(True, 3): 1}))
,(4, 0, True, 1, {(True, 4): 1}, ({}, {(True, 1): 1, (True, 4): 1}))
,(5, None, None, 0, {}, ({}, {(True, 3): 1}))
,(6, 0, True, 1, {(True, 4): 1}, ({}, {(True, 1): 1, (True, 4): 1}))
,(7, None, None, 0, {}, ({}, {(True, 3): 1}))
,(8, 0, True, 1, {(True, 4): 1}, ({}, {(True, 1): 1, (True, 4): 1}))
,(9, None, None, 0, {}, ({}, {(True, 3): 1}))
,(10, 0, True, 1, {(True, 4): 1}, ({}, {(True, 1): 1, (True, 4): 1}))
,(11, None, None, 0, {}, ({}, {(True, 3): 1}))
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(2**2, ["11"], ["00"], [], may_k2sz4alphabet={'0':2,'1':2}, may_args4islice=[12], turnon__floor_log2_total_count=True, _ver_=1)])
[(0, None, None, 0, {}, ({(False, 0): 1}, {}))
,(1, None, None, 0, {}, ({(False, 1): 2}, {}))
,(2, None, None, 0, {}, ({}, {(False, 2): 4}))
,(3, None, None, 0, {}, ({}, {(True, 3): 8}))
,(4, 4, True, 16, {(True, 4): 16}, ({}, {(True, 1): 16, (True, 4): 16}))
,(5, None, None, 0, {}, ({}, {(True, 3): 32}))
,(6, 6, True, 64, {(True, 4): 64}, ({}, {(True, 1): 64, (True, 4): 64}))
,(7, None, None, 0, {}, ({}, {(True, 3): 128}))
,(8, 8, True, 256, {(True, 4): 256}, ({}, {(True, 1): 256, (True, 4): 256}))
,(9, None, None, 0, {}, ({}, {(True, 3): 512}))
,(10, 10, True, 1024, {(True, 4): 1024}, ({}, {(True, 1): 1024, (True, 4): 1024}))
,(11, None, None, 0, {}, ({}, {(True, 3): 2048}))
]


以"00"结尾并且不含"11"的比特串数量，对于比特串长度>=2，恒为 1
    1?(01)*00
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(2, ["00"], ["11"], may_k2sz4alphabet=None, may_args4islice=[12])])
[(0, 0, {}, ({0: 1},))
,(1, 0, {}, ({1: 1, 3: 1},))
,(2, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(3, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(4, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(5, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(6, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(7, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(8, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(9, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(10, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
,(11, 1, {2: 1}, ({1: 1, 2: 1, 3: 1},))
]


不含"11"的比特串数量，对于比特串长度而成的序列，是 Fibonacci_number
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11"], may_k2sz4alphabet=None, may_args4islice=[12])])
[(0, 1, {0: 1})
,(1, 2, {0: 1, 1: 1})
,(2, 3, {0: 2, 1: 1})
,(3, 5, {0: 3, 1: 2})
,(4, 8, {0: 5, 1: 3})
,(5, 13, {0: 8, 1: 5})
,(6, 21, {0: 13, 1: 8})
,(7, 34, {0: 21, 1: 13})
,(8, 55, {0: 34, 1: 21})
,(9, 89, {0: 55, 1: 34})
,(10, 144, {0: 89, 1: 55})
,(11, 233, {0: 144, 1: 89})
]




##old:py_adhoc_call   seed.seq_tools.prefixes2tree   ,stable_repr.iter_num_strs_ex__avoid_substrs_  =2  '=["11", "00"]'  :1  '--args4islice=(9,)'  +with_vars
    iter_num_strs_ex__avoid_substrs_
        --> iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11", "00"], may_prefix='1', may_k2sz4alphabet=None, may_args4islice=[7])])
[(1, 1, {1: 1})
,(2, 1, {3: 1})
,(3, 1, {1: 1})
,(4, 1, {3: 1})
,(5, 1, {1: 1})
,(6, 1, {3: 1})
,(7, 1, {1: 1})
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11", "00"], may_prefix='1', may_k2sz4alphabet=None, may_args4islice=[7], with_state_inside_prefix=True)])
[(0, 1, {0: 1})
,(1, 1, {1: 1})
,(2, 1, {3: 1})
,(3, 1, {1: 1})
,(4, 1, {3: 1})
,(5, 1, {1: 1})
,(6, 1, {3: 1})
]



>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(3, ["11", "00"], may_prefix='1', may_k2sz4alphabet=None, may_args4islice=[10])])
[(1, 1, {1: 1})
,(2, 2, {0: 1, 3: 1})
,(3, 5, {0: 2, 1: 2, 3: 1})
,(4, 12, {0: 5, 1: 3, 3: 4})
,(5, 29, {0: 12, 1: 9, 3: 8})
,(6, 70, {0: 29, 1: 20, 3: 21})
,(7, 169, {0: 70, 1: 50, 3: 49})
,(8, 408, {0: 169, 1: 119, 3: 120})
,(9, 985, {0: 408, 1: 289, 3: 288})
,(10, 2378, {0: 985, 1: 696, 3: 697})
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(3, ["11", "00"], may_prefix='1', may_k2sz4alphabet=None, may_args4islice=[10], with_state_inside_prefix=True)])
[(0, 1, {0: 1})
,(1, 1, {1: 1})
,(2, 2, {0: 1, 3: 1})
,(3, 5, {0: 2, 1: 2, 3: 1})
,(4, 12, {0: 5, 1: 3, 3: 4})
,(5, 29, {0: 12, 1: 9, 3: 8})
,(6, 70, {0: 29, 1: 20, 3: 21})
,(7, 169, {0: 70, 1: 50, 3: 49})
,(8, 408, {0: 169, 1: 119, 3: 120})
,(9, 985, {0: 408, 1: 289, 3: 288})
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(3, ["11", "00"], may_prefix='', may_k2sz4alphabet=None, may_args4islice=[10])])
[(0, 1, {0: 1})
,(1, 3, {0: 1, 1: 1, 3: 1})
,(2, 7, {0: 3, 1: 2, 3: 2})
,(3, 17, {0: 7, 1: 5, 3: 5})
,(4, 41, {0: 17, 1: 12, 3: 12})
,(5, 99, {0: 41, 1: 29, 3: 29})
,(6, 239, {0: 99, 1: 70, 3: 70})
,(7, 577, {0: 239, 1: 169, 3: 169})
,(8, 1393, {0: 577, 1: 408, 3: 408})
,(9, 3363, {0: 1393, 1: 985, 3: 985})
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(9, ["11", "00"], may_prefix='', may_k2sz4alphabet=None, may_args4islice=[10])])
[(0, 1, {0: 1})
,(1, 9, {0: 7, 1: 1, 3: 1})
,(2, 79, {0: 63, 1: 8, 3: 8})
,(3, 695, {0: 553, 1: 71, 3: 71})
,(4, 6113, {0: 4865, 1: 624, 3: 624})
,(5, 53769, {0: 42791, 1: 5489, 3: 5489})
,(6, 472943, {0: 376383, 1: 48280, 3: 48280})
,(7, 4159927, {0: 3310601, 1: 424663, 3: 424663})
,(8, 36590017, {0: 29119489, 1: 3735264, 3: 3735264})
,(9, 321839625, {0: 256130119, 1: 32854753, 3: 32854753})
]


#prefix include some forbidden_substr
#   ==>> num_strs == 0
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11", "00"], may_prefix='11', may_k2sz4alphabet=None, may_args4islice=[10])])
[]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11", "00"], may_prefix='11', may_k2sz4alphabet=None, may_args4islice=[10], with_state_inside_prefix=True)])
[(0, 1, {0: 1})
,(1, 1, {1: 1})
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11", "00"], may_prefix='001', may_k2sz4alphabet=None, may_args4islice=[10])])
[]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11", "00"], may_prefix='001', may_k2sz4alphabet=None, may_args4islice=[10], with_state_inside_prefix=True)])
[(0, 1, {0: 1})
,(1, 1, {3: 1})
]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11", "00"], may_prefix='1001', may_k2sz4alphabet=None, may_args4islice=[10])])
[]
>>> expand1([*main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(2, ["11", "00"], may_prefix='1001', may_k2sz4alphabet=None, may_args4islice=[10], with_state_inside_prefix=True)])
[(0, 1, {0: 1})
,(1, 1, {1: 1})
,(2, 1, {3: 1})
]



>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_(8, 2, may_args4islice=[9])])
[(4, 268435456)
,(6, 4398046511104)
,(8, 72057594037927936)
,(10, 1180591620717411303424)
,(12, 19342813113834066795298816)
,(14, 316912650057057350374175801344)
,(16, 5192296858534827628530496329220096)
,(18, 85070591730234615865843651857942052864)
,(20, 1393796574908163946345982392040522594123776)
]
>>> expand1([*iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(8, 2, may_args4islice=[9], with_num_strs=True)])
[(4, 28, 268435456)
,(6, 42, 4398046511104)
,(8, 56, 72057594037927936)
,(10, 70, 1180591620717411303424)
,(12, 84, 19342813113834066795298816)
,(14, 98, 316912650057057350374175801344)
,(16, 112, 5192296858534827628530496329220096)
,(18, 126, 85070591730234615865843651857942052864)
,(20, 140, 1393796574908163946345982392040522594123776)
]


>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, 2, may_args4islice=[9])])
[(4, 1)
,(6, 1)
,(8, 1)
,(10, 1)
,(12, 1)
,(14, 1)
,(16, 1)
,(18, 1)
,(20, 1)
]
>>> expand1([*iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, 2, may_args4islice=[9])])
[(4, 0)
,(6, 0)
,(8, 0)
,(10, 0)
,(12, 0)
,(14, 0)
,(16, 0)
,(18, 0)
,(20, 0)
]
>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, 3, may_args4islice=[9])])
[(6, 1)
,(8, 1)
,(9, 2)
,(11, 2)
,(12, 4)
,(14, 4)
,(15, 8)
,(17, 8)
,(18, 16)
]
>>> expand1([*iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, 3, may_args4islice=[9])])
[(6, 0)
,(8, 0)
,(9, 1)
,(11, 1)
,(12, 2)
,(14, 2)
,(15, 3)
,(17, 3)
,(18, 4)
]


>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, 4, may_args4islice=[9])])
[(8, 1)
,(10, 1)
,(11, 2)
,(12, 4)
,(14, 4)
,(15, 8)
,(16, 16)
,(18, 16)
,(19, 32)
]
>>> expand1([*iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, 4, may_args4islice=[9])])
[(8, 0)
,(10, 0)
,(11, 1)
,(12, 2)
,(14, 2)
,(15, 3)
,(16, 4)
,(18, 4)
,(19, 5)
]




>>> expand1([*iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(8, 4, may_args4islice=[9])])
[(8, 56)
,(10, 70)
,(11, 78)
,(12, 86)
,(14, 100)
,(15, 108)
,(16, 116)
,(18, 130)
,(19, 138)
]



[vs___7_iter_num_strs_ex]:goto
def iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_(sz4alphabet, begin_marker, end_marker, substrs4avoid, /, *, may_k2sz4alphabet=None, may_args4islice=None):
>>> expand1([*iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_(2, '1'*4, '0'*4, [], may_args4islice=[20], _ver_=2)])
[(0, 0)
,(1, 0)
,(2, 0)
,(3, 0)
,(4, 0)
,(5, 0)
,(6, 0)
,(7, 0)
,(8, 1)
,(9, 0)
,(10, 1)
,(11, 2)
,(12, 4)
,(13, 6)
,(14, 12)
,(15, 22)
,(16, 41)
,(17, 74)
,(18, 137)
,(19, 252)
]
>>> expand1([*iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(2, 4, 1, 1, may_args4islice=[20], _ver_=2)])
[(0, 0)
,(1, 0)
,(2, 0)
,(3, 0)
,(4, 0)
,(5, 0)
,(6, 0)
,(7, 0)
,(8, 1)
,(9, 0)
,(10, 1)
,(11, 2)
,(12, 4)
,(13, 6)
,(14, 12)
,(15, 22)
,(16, 41)
,(17, 74)
,(18, 137)
,(19, 252)
]
>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(1, 4, may_args4islice=[20], _ver_=2)])
[(0, 0)
,(1, 0)
,(2, 0)
,(3, 0)
,(4, 0)
,(5, 0)
,(6, 0)
,(7, 0)
,(8, 1)
,(9, 0)
,(10, 1)
,(11, 2)
,(12, 4)
,(13, 6)
,(14, 12)
,(15, 22)
,(16, 41)
,(17, 74)
,(18, 137)
,(19, 252)
]
>>> expand1([*iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_(2, 4, 1, 1, may_args4islice=[9])])
[(8, 1)
,(10, 1)
,(11, 2)
,(12, 4)
,(14, 4)
,(15, 8)
,(16, 16)
,(18, 16)
,(19, 32)
]
>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, 4, may_args4islice=[9])])
[(8, 1)
,(10, 1)
,(11, 2)
,(12, 4)
,(14, 4)
,(15, 8)
,(16, 16)
,(18, 16)
,(19, 32)
]
>>> expand1([*iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, 4, may_args4islice=[9], with_num_strs=True)])
[(8, 0, 1)
,(10, 0, 1)
,(11, 1, 2)
,(12, 2, 4)
,(14, 2, 4)
,(15, 3, 8)
,(16, 4, 16)
,(18, 4, 16)
,(19, 5, 32)
]


主要对比:即layout_with_std_both_marker之中std_layout的占有率:
    #>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(1, ???, may_args4islice=[20])])
    #>>> expand1([*iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(1, ???, may_args4islice=[9], with_num_strs=True)])
    [len4both_marker==4]:
        [len4curr_str==19]:
            [total_count<std_layout>/total_count<layout_with_std_both_marker> == 32/252]



iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_
    iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, may_args4islice=may_args4islice)
    iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, may_args4islice=may_args4islice, directly=True)
    iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(num_bits4word, len4both_marker, may_args4islice=may_args4islice, directly=True)

directly
>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(1, 4, may_args4islice=[20], directly=True, with_st2cnt_if_directly=True, _ver_=2)])
[(0, 0, [1, 0, 0, 0, 0, 0, 0, 0, 0])
,(1, 0, [0, 1, 0, 0, 0, 0, 0, 0, 0])
,(2, 0, [0, 0, 1, 0, 0, 0, 0, 0, 0])
,(3, 0, [0, 0, 0, 1, 0, 0, 0, 0, 0])
,(4, 0, [0, 0, 0, 0, 1, 0, 0, 0, 0])
,(5, 0, [0, 0, 0, 0, 0, 1, 0, 0, 0])
,(6, 0, [0, 1, 0, 0, 0, 0, 1, 0, 0])
,(7, 0, [0, 1, 1, 0, 0, 1, 0, 1, 0])
,(8, 1, [0, 2, 1, 1, 0, 2, 1, 0, 1])
,(9, 0, [0, 3, 2, 1, 1, 4, 2, 1, 0])
,(10, 1, [0, 7, 3, 2, 1, 6, 4, 2, 1])
,(11, 2, [0, 12, 7, 3, 2, 12, 6, 4, 2])
,(12, 4, [0, 22, 12, 7, 3, 22, 12, 6, 4])
,(13, 6, [0, 40, 22, 12, 7, 41, 22, 12, 6])
,(14, 12, [0, 75, 40, 22, 12, 74, 41, 22, 12])
,(15, 22, [0, 137, 75, 40, 22, 137, 74, 41, 22])
,(16, 41, [0, 252, 137, 75, 40, 252, 137, 74, 41])
,(17, 74, [0, 463, 252, 137, 75, 464, 252, 137, 74])
,(18, 137, [0, 853, 463, 252, 137, 852, 464, 252, 137])
,(19, 252, [0, 1568, 853, 463, 252, 1568, 852, 464, 252])
]
>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(1, 4, may_args4islice=[20], directly=True, _ver_=2)])
[(0, 0)
,(1, 0)
,(2, 0)
,(3, 0)
,(4, 0)
,(5, 0)
,(6, 0)
,(7, 0)
,(8, 1)
,(9, 0)
,(10, 1)
,(11, 2)
,(12, 4)
,(13, 6)
,(14, 12)
,(15, 22)
,(16, 41)
,(17, 74)
,(18, 137)
,(19, 252)
]

not directly
>>> expand1([*iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(1, 4, may_args4islice=[20], _ver_=2)])
[(0, 0)
,(1, 0)
,(2, 0)
,(3, 0)
,(4, 0)
,(5, 0)
,(6, 0)
,(7, 0)
,(8, 1)
,(9, 0)
,(10, 1)
,(11, 2)
,(12, 4)
,(13, 6)
,(14, 12)
,(15, 22)
,(16, 41)
,(17, 74)
,(18, 137)
,(19, 252)
]


directly
>>> expand1([*iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(2, 4, 1, 1, may_args4islice=[20], directly=True, with_st2cnt_if_directly=True, _ver_=2)])
[(0, 0, [1, 0, 0, 0, 0, 0, 0, 0, 0])
,(1, 0, [0, 1, 0, 0, 0, 0, 0, 0, 0])
,(2, 0, [0, 0, 1, 0, 0, 0, 0, 0, 0])
,(3, 0, [0, 0, 0, 1, 0, 0, 0, 0, 0])
,(4, 0, [0, 0, 0, 0, 1, 0, 0, 0, 0])
,(5, 0, [0, 0, 0, 0, 0, 1, 0, 0, 0])
,(6, 0, [0, 1, 0, 0, 0, 0, 1, 0, 0])
,(7, 0, [0, 1, 1, 0, 0, 1, 0, 1, 0])
,(8, 1, [0, 2, 1, 1, 0, 2, 1, 0, 1])
,(9, 0, [0, 3, 2, 1, 1, 4, 2, 1, 0])
,(10, 1, [0, 7, 3, 2, 1, 6, 4, 2, 1])
,(11, 2, [0, 12, 7, 3, 2, 12, 6, 4, 2])
,(12, 4, [0, 22, 12, 7, 3, 22, 12, 6, 4])
,(13, 6, [0, 40, 22, 12, 7, 41, 22, 12, 6])
,(14, 12, [0, 75, 40, 22, 12, 74, 41, 22, 12])
,(15, 22, [0, 137, 75, 40, 22, 137, 74, 41, 22])
,(16, 41, [0, 252, 137, 75, 40, 252, 137, 74, 41])
,(17, 74, [0, 463, 252, 137, 75, 464, 252, 137, 74])
,(18, 137, [0, 853, 463, 252, 137, 852, 464, 252, 137])
,(19, 252, [0, 1568, 853, 463, 252, 1568, 852, 464, 252])
]
>>> expand1([*iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(2, 4, 1, 1, may_args4islice=[20], directly=True, _ver_=2)])
[(0, 0)
,(1, 0)
,(2, 0)
,(3, 0)
,(4, 0)
,(5, 0)
,(6, 0)
,(7, 0)
,(8, 1)
,(9, 0)
,(10, 1)
,(11, 2)
,(12, 4)
,(13, 6)
,(14, 12)
,(15, 22)
,(16, 41)
,(17, 74)
,(18, 137)
,(19, 252)
]

not directly
>>> expand1([*iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(2, 4, 1, 1, may_args4islice=[20], _ver_=2)])
[(0, 0)
,(1, 0)
,(2, 0)
,(3, 0)
,(4, 0)
,(5, 0)
,(6, 0)
,(7, 0)
,(8, 1)
,(9, 0)
,(10, 1)
,(11, 2)
,(12, 4)
,(13, 6)
,(14, 12)
,(15, 22)
,(16, 41)
,(17, 74)
,(18, 137)
,(19, 252)
]

check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker
check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker
check_dual_end_marker_have_no_nonempty_overlaps

>>> check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker(['111'], ['000'])
>>> check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(['111'], ['000'])
>>> check_dual_end_marker_have_no_nonempty_overlaps(['111'], ['000'])

>>> check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker(['1110'], ['1000']) #ok
>>> check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(['1110'], ['1000'])
Traceback (most recent call last):
    ...
ValueError: [5]
>>> check_dual_end_marker_have_no_nonempty_overlaps(['1110'], ['1000'])
Traceback (most recent call last):
    ...
ValueError: [5]

>>> check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker(['1000'], ['1110'])
Traceback (most recent call last):
    ...
ValueError: [5]
>>> check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(['1000'], ['1110']) #ok
>>> check_dual_end_marker_have_no_nonempty_overlaps(['1000'], ['1110'])
Traceback (most recent call last):
    ...
ValueError: [5]

>>> check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker(['1110'], ['0001'])
Traceback (most recent call last):
    ...
ValueError: [5]
>>> check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(['1110'], ['0001'])
Traceback (most recent call last):
    ...
ValueError: [5]
>>> check_dual_end_marker_have_no_nonempty_overlaps(['1110'], ['0001'])
Traceback (most recent call last):
    ...
ValueError: [5]

>>> check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker(['11101'], ['00010'])
>>> check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(['11101'], ['00010'])
>>> check_dual_end_marker_have_no_nonempty_overlaps(['11101'], ['00010'])



mk_st2is_inside_end_marker
mk_st2is_inside_begin_marker
mk_st2is_le_end_st4xxx
iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver2_
    iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_
iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_

def iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(sz4alphabet, begin_markers, end_markers, substrs4avoid, /, *, _ver_, may_k2sz4alphabet=None, _debug=False):
>>> expand1_islice_([12], iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(2, ["111"], ["000"], [], _ver_=1))
[(0, 0, {}, ({(False, 0): 1}, {}))
,(1, 0, {}, ({(False, 1): 1}, {}))
,(2, 0, {}, ({(False, 2): 1}, {}))
,(3, 0, {}, ({}, {(False, 3): 1}))
,(4, 0, {}, ({}, {(True, 4): 1}))
,(5, 0, {}, ({}, {(True, 1): 1, (True, 5): 1}))
,(6, 1, {(True, 6): 1}, ({}, {(True, 1): 1, (True, 2): 1, (True, 4): 1, (True, 6): 1}))
,(7, 0, {}, ({}, {(True, 1): 1, (True, 2): 1, (True, 4): 2, (True, 5): 1}))
,(8, 1, {(True, 6): 1}, ({}, {(True, 1): 3, (True, 2): 1, (True, 4): 2, (True, 5): 2, (True, 6): 1}))
,(9, 2, {(True, 6): 2}, ({}, {(True, 1): 4, (True, 2): 3, (True, 4): 4, (True, 5): 2, (True, 6): 2}))
,(10, 2, {(True, 6): 2}, ({}, {(True, 1): 6, (True, 2): 4, (True, 4): 7, (True, 5): 4, (True, 6): 2}))
,(11, 4, {(True, 6): 4}, ({}, {(True, 1): 11, (True, 2): 6, (True, 4): 10, (True, 5): 7, (True, 6): 4}))
]
>>> expand1_islice_([12], iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(2, ["111"], ["000"], [], _ver_=2))
[(0, 0, {}, ({(False, 0): 1},))
,(1, 0, {}, ({(False, 1): 1},))
,(2, 0, {}, ({(False, 2): 1},))
,(3, 0, {}, ({(False, 3): 1},))
,(4, 0, {}, ({(True, 4): 1},))
,(5, 0, {}, ({(True, 1): 1, (True, 5): 1},))
,(6, 1, {(True, 6): 1}, ({(True, 1): 1, (True, 2): 1, (True, 4): 1, (True, 6): 1},))
,(7, 0, {}, ({(True, 1): 1, (True, 2): 1, (True, 4): 2, (True, 5): 1},))
,(8, 1, {(True, 6): 1}, ({(True, 1): 3, (True, 2): 1, (True, 4): 2, (True, 5): 2, (True, 6): 1},))
,(9, 2, {(True, 6): 2}, ({(True, 1): 4, (True, 2): 3, (True, 4): 4, (True, 5): 2, (True, 6): 2},))
,(10, 2, {(True, 6): 2}, ({(True, 1): 6, (True, 2): 4, (True, 4): 7, (True, 5): 4, (True, 6): 2},))
,(11, 4, {(True, 6): 4}, ({(True, 1): 11, (True, 2): 6, (True, 4): 10, (True, 5): 7, (True, 6): 4},))
]

##test for kw:drop_head
>>> list_islice_([1], [111, 222, 333])
[111]
>>> list_islice_([1, None], [111, 222, 333])
[222, 333]

>>> cnts100__std3__1bit__ver1 = list_islice_([100], map(snd, iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(2, ["111"], ["000"], [], _ver_=1)))
>>> cnts100__std3__1bit__ver2 = list_islice_([100], map(snd, iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(2, ["111"], ["000"], [], _ver_=2)))
>>> cnts100__std3__1bit__ver1 == cnts100__std3__1bit__ver2
True
>>> cnts100__std3__1bit__ver1
[0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 4, 7, 10, 17, 28, 44, 72, 117, 188, 305, 494, 798, 1292, 2091, 3382, 5473, 8856, 14328, 23184, 37513, 60696, 98209, 158906, 257114, 416020, 673135, 1089154, 1762289, 2851444, 4613732, 7465176, 12078909, 19544084, 31622993, 51167078, 82790070, 133957148, 216747219, 350704366, 567451585, 918155952, 1485607536, 2403763488, 3889371025, 6293134512, 10182505537, 16475640050, 26658145586, 43133785636, 69791931223, 112925716858, 182717648081, 295643364940, 478361013020, 774004377960, 1252365390981, 2026369768940, 3278735159921, 5305104928862, 8583840088782, 13888945017644, 22472785106427, 36361730124070, 58834515230497, 95196245354568, 154030760585064, 249227005939632, 403257766524697, 652484772464328, 1055742538989025, 1708227311453354, 2763969850442378, 4472197161895732, 7236167012338111, 11708364174233842, 18944531186571953, 30652895360805796, 49597426547377748, 80250321908183544, 129847748455561293, 210098070363744836, 339945818819306129, 550043889183050966, 889989708002357094, 1440033597185408060, 2330023305187765155, 3770056902373173214, 6100080207560938369, 9870137109934111584]

>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(1, 3, _ver_=1)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(1, 3, _ver_=2)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(1, 3, _ver_=None, directly=True)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(2, 3, 1, 1, _ver_=1)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(2, 3, 1, 1, _ver_=2)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(2, 3, 1, 1, _ver_=None, directly=True)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_(2, 3, 1, 1)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_(2, "111", "000", [], _ver_=1)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_(2, "111", "000", [], _ver_=2)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(2, ["111"], ["000"], [], _ver_=1)))
True
>>> cnts100__std3__1bit__ver1 == list_islice_([100], map(snd, iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(2, ["111"], ["000"], [], _ver_=2)))
True


[[[
substring avoid
view ../../python3_src/seed/seq_tools/avoid_substrs.py
===
0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 4, 7, 10, 17, 28, 44, 72, 117, 188, 305, 494, 798, 1292, 2091, 3382, 5473, 8856, 14328, 23184, 37513, 60696
https://oeis.org/A094686
A094686		A Fibonacci convolution.		14
1, 0, 1, 2, 2, 4, 7, 10, 17, 28, 44, 72, 117, 188, 305, 494, 798, 1292, 2091, 3382, 5473, 8856, 14328, 23184, 37513, 60696, 98209, 158906, 257114, 416020, 673135, 1089154, 1762289, 2851444, 4613732, 7465176, 12078909, 19544084, 31622993, 51167078 
  * Stefano Bilotta, Variable-length Non-overlapping Codes, arXiv preprint arXiv:1605.03785 [cs.IT], 2016 [See Table 2].
    https://arxiv.org/abs/1605.03785
      https://arxiv.org/pdf/1605.03785
      Variable-length Non-overlapping Codes(2016)(Stefano Bilotta).pdf
  * Elena Barcucci, Antonio Bernini, Stefano Bilotta, Renzo Pinzani, Non-overlapping matrices, arXiv:1601.07723 [cs.DM], 2016 (see 1st column of Table 1 p. 8).
    https://arxiv.org/abs/1601.07723
      https://arxiv.org/pdf/1601.07723
      Non-overlapping matrices(2016)(Elena Barcucci).pdf

===
1, 0, 1, 2, 4, 6, 12, 22, 41, 74, 137, 252, 464, 852
https://oeis.org/A283834
A283834		Number of length-n binary vectors beginning with 0, ending with 1, and avoiding 4 consecutive 0's and 4 consecutive 1's.		2
1, 0, 1, 2, 4, 6, 12, 22, 41, 74, 137, 252, 464, 852, 1568, 2884, 5305, 9756, 17945, 33006, 60708, 111658, 205372, 377738, 694769, 1277878, 2350385, 4323032, 7951296, 14624712, 26899040, 49475048, 90998801, 167372888, 307846737, 566218426, 1041438052 (list; graph; refs; listen; history; text; internal format)
OFFSET	
0,4
LINKS	
  Stefano Bilotta, Variable-length Non-overlapping Codes, arXiv preprint arXiv:1605.03785 [cs.IT], 2016 [See Table 2].
  Index entries for linear recurrences with constant coefficients, signature (0,1,2,3,2,1).

]]]
>>> expand1_islice_(5, (list_islice_([50], map(snd, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_(2, L, 1, 1))) for L in itertools.count(2)))
[[0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
,[0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 4, 7, 10, 17, 28, 44, 72, 117, 188, 305, 494, 798, 1292, 2091, 3382, 5473, 8856, 14328, 23184, 37513, 60696, 98209, 158906, 257114, 416020, 673135, 1089154, 1762289, 2851444, 4613732, 7465176, 12078909, 19544084, 31622993, 51167078, 82790070, 133957148, 216747219, 350704366]
,[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 4, 6, 12, 22, 41, 74, 137, 252, 464, 852, 1568, 2884, 5305, 9756, 17945, 33006, 60708, 111658, 205372, 377738, 694769, 1277878, 2350385, 4323032, 7951296, 14624712, 26899040, 49475048, 90998801, 167372888, 307846737, 566218426, 1041438052, 1915503214, 3523159692, 6480100958, 11918763865, 21922024514]
,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 4, 8, 14, 28, 54, 104, 201, 386, 745, 1436, 2768, 5336, 10284, 19824, 38212, 73656, 141977, 273668, 527513, 1016814, 1959972, 3777968, 7282266, 14037020, 27057226, 52154480, 100530993, 193779718, 373522417, 719987608, 1387820736, 2675110480, 5156441240, 9939360064, 19158732520, 36929644304]
,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 4, 8, 16, 30, 60, 118, 232, 456, 897, 1762, 3465, 6812, 13392, 26328, 51760, 101756, 200048, 393284, 773176, 1520024, 2988289, 5874820, 11549593, 22705902, 44638628, 87757232, 172526176, 339177530, 666805468, 1310905034, 2577171440, 5066585648, 9960645121, 19582112710]
]


>>> collect_src_names(Helper4AutoCalc4AvoidSubstr) == {'sz4alphabet', 'may_k2sz4alphabet', 'begin_markers', 'end_markers', 'substrs4avoid'}
True

>>> h = Helper4AutoCalc4AvoidSubstr(sz4alphabet=2, may_k2sz4alphabet=None, begin_markers=['11'], end_markers=['00'], substrs4avoid=[])
>>> h
Helper4AutoCalc4AvoidSubstr(begin_markers = ['11'], end_markers = ['00'], may_k2sz4alphabet = None, substrs4avoid = [], sz4alphabet = 2)
>>> len(dir(h))
48
>>> len(calc_all(h)) ##fill
48
>>> len(dir(h))
48
>>> expand1({nm: getattr(h, nm) for nm in dir(h) if not nm == 'counter4avoid_substrs__using_dual_end_delimiter'})
{'basic_setting4multi_cell_token'
: Setting4MultiCellToken(istr2is_begin_marker= [True, False], istr2is_end_marker= [False, True], istr2is_forbidden_substr= [False, False], strings= ['11', '00'])
,'begin_markers'
: ['11']
,'end_markers'
: ['00']
,'end_st2istrs'
: [[], [], [0], [], [1]]
,'hst2k2hst__as_transition_table'
: {(False, 0): {'0': (False, 3), '1': (False, 1)}, (False, 1): {'0': (False, 3), '1': (False, 2)}, (False, 2): {'0': (True, 3), '1': (True, 2)}, (False, 3): {'0': (False, 4), '1': (False, 1)}, (False, 4): {'0': (False, 4), '1': (False, 1)}, (True, 0): {'0': (True, 3), '1': (True, 1)}, (True, 1): {'0': (True, 3), '1': (True, 2)}, (True, 3): {'0': (True, 4), '1': (True, 1)}, (True, 4): {'0': (True, 4), '1': (True, 1)}}
,'istr2end_st'
: [2, 4]
,'istr2is_begin_marker'
: [True, False]
,'istr2is_end_marker'
: [False, True]
,'istr2is_forbidden_substr'
: [False, False]
,'k2sz4alphabet'
: {'0': 1, '1': 1}
,'ks'
: {'0', '1'}
,'len2sts'
: [[0], [1, 3], [2, 4]]
,'len_strs'
: 2
,'may_k2sz4alphabet'
: None
,'noninit_st2longest_proper_suffix_st'
: [None, 0, 1, 0, 3]
,'noninit_st2st_k_pair__as_InTree'
: [None, (0, '1'), (1, '1'), (0, '0'), (3, '0')]
,'setting4multi_cell_token'
: Setting4MultiCellToken(istr2is_begin_marker= [True, False], istr2is_end_marker= [False, True], istr2is_forbidden_substr= [False, False], strings= ['11', '00'])
,'st0'
: 0
,'st2is_eq_end_st4begin_marker'
: [False, False, True, False, False]
,'st2is_eq_end_st4end_marker'
: [False, False, False, False, True]
,'st2is_eq_end_st4forbidden_substr'
: [False, False, False, False, False]
,'st2is_eq_end_st4suffix'
: [False, False, True, False, True]
,'st2is_eq_end_st4whole'
: [False, False, True, False, True]
,'st2is_eq_end_st4whole4begin_marker'
: [False, False, True, False, False]
,'st2is_eq_end_st4whole4effective_begin_marker'
: [False, False, True, False, False]
,'st2is_ge_end_st4begin_marker'
: [False, False, True, False, False]
,'st2is_ge_end_st4end_marker'
: [False, False, False, False, True]
,'st2is_ge_end_st4forbidden_substr'
: [False, False, False, False, False]
,'st2is_gt_end_st4begin_marker'
: [False, False, False, False, False]
,'st2is_gt_end_st4end_marker'
: [False, False, False, False, False]
,'st2is_gt_end_st4forbidden_substr'
: [False, False, False, False, False]
,'st2is_inside_begin_marker'
: [True, True, True, False, False]
,'st2is_inside_end_marker'
: [True, False, False, True, True]
,'st2istrs'
: [[0, 1], [0], [0], [1], [1]]
,'st2k2st__as_OutTree'
: [{'0': 3, '1': 1}, {'1': 2}, {}, {'0': 4}, {}]
,'st2k2st__as_transition_table'
: [{'0': 3, '1': 1}, {'0': 3, '1': 2}, {'0': 3, '1': 2}, {'0': 4, '1': 1}, {'0': 4, '1': 1}]
,'st2len'
: [0, 1, 2, 1, 2]
,'st2prev_substr_end_sts'
: [[], [], [2], [], [4]]
,'st2prev_substr_end_sts4begin_marker'
: [[], [], [2], [], []]
,'st2prev_substr_end_sts4end_marker'
: [[], [], [], [], [4]]
,'st2prev_substr_end_sts4forbidden_substr'
: [[], [], [], [], []]
,'st2suffix_end_sts'
: [[], [], [2], [], [4]]
,'st_info4begin_marker'
: StInfo4BeginMarker(st2is_eq_end_st4begin_marker= [False, False, True, False, False], st2is_ge_end_st4begin_marker= [False, False, True, False, False], st2is_gt_end_st4begin_marker= [False, False, False, False, False], st2prev_substr_end_sts4begin_marker= [[], [], [2], [], []])
,'st_info4body'
: StInfo4Body(st2is_ge_end_st4end_marker= [False, False, False, False, True], st2is_ge_end_st4forbidden_substr= [False, False, False, False, False], st2is_gt_end_st4end_marker= [False, False, False, False, False])
,'strings'
: ['11', '00']
,'substrs4avoid'
: []
,'sz4alphabet'
: 2
}

>>> type(h.counter4avoid_substrs__using_dual_end_delimiter) is Counter4AvoidSubstrs__using_dual_end_delimiter
True
>>> expand1(h.counter4avoid_substrs__using_dual_end_delimiter._vars)
{'end_st2istrs'
: [[], [], [0], [], [1]]
,'istr2end_st'
: [2, 4]
,'ks'
: {'0', '1'}
,'len2sts'
: [[0], [1, 3], [2, 4]]
,'may_k2sz4alphabet'
: None
,'noninit_st2longest_proper_suffix_st'
: [None, 0, 1, 0, 3]
,'noninit_st2st_k_pair__as_InTree'
: [None, (0, '1'), (1, '1'), (0, '0'), (3, '0')]
,'st2is_eq_end_st4whole'
: [False, False, True, False, True]
,'st2istrs'
: [[0, 1], [0], [0], [1], [1]]
,'st2k2st__as_OutTree'
: [{'0': 3, '1': 1}, {'1': 2}, {}, {'0': 4}, {}]
,'st2k2st__as_transition_table'
: [{'0': 3, '1': 1}, {'0': 3, '1': 2}, {'0': 3, '1': 2}, {'0': 4, '1': 1}, {'0': 4, '1': 1}]
,'st2len'
: [0, 1, 2, 1, 2]
,'st2suffix_end_sts'
: [[], [], [2], [], [4]]
}
>>> expand1({nm: x for nm, x in vars(h.counter4avoid_substrs__using_dual_end_delimiter).items() if not nm.startswith('_')})
{'basic_setting4multi_cell_token'
: Setting4MultiCellToken(istr2is_begin_marker= [True, False], istr2is_end_marker= [False, True], istr2is_forbidden_substr= [False, False], strings= ['11', '00'])
,'hst2k2hst__as_transition_table'
: {(False, 0): {'0': (False, 3), '1': (False, 1)}, (False, 1): {'0': (False, 3), '1': (False, 2)}, (False, 2): {'0': (True, 3), '1': (True, 2)}, (False, 3): {'0': (False, 4), '1': (False, 1)}, (False, 4): {'0': (False, 4), '1': (False, 1)}, (True, 0): {'0': (True, 3), '1': (True, 1)}, (True, 1): {'0': (True, 3), '1': (True, 2)}, (True, 3): {'0': (True, 4), '1': (True, 1)}, (True, 4): {'0': (True, 4), '1': (True, 1)}}
,'k2sz4alphabet'
: {'0': 1, '1': 1}
,'setting4multi_cell_token'
: Setting4MultiCellToken(istr2is_begin_marker= [True, False], istr2is_end_marker= [False, True], istr2is_forbidden_substr= [False, False], strings= ['11', '00'])
,'st0'
: 0
,'st2is_ge_end_st4begin_marker'
: [False, False, True, False, False]
,'st_info4begin_marker'
: StInfo4BeginMarker(st2is_eq_end_st4begin_marker= [False, False, True, False, False], st2is_ge_end_st4begin_marker= [False, False, True, False, False], st2is_gt_end_st4begin_marker= [False, False, False, False, False], st2prev_substr_end_sts4begin_marker= [[], [], [2], [], []])
,'st_info4body'
: StInfo4Body(st2is_ge_end_st4end_marker= [False, False, False, False, True], st2is_ge_end_st4forbidden_substr= [False, False, False, False, False], st2is_gt_end_st4end_marker= [False, False, False, False, False])
,'sz4alphabet'
: 2
}


__all__
def main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(sz4alphabet, begin_markers, end_markers, substrs4avoid, /, *, may_k2sz4alphabet=None, may_args4islice=None):
def main4iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(sz4alphabet, end_markers, substrs4avoid, /, *, may_k2sz4alphabet=None, may_prefix=None, with_state_inside_prefix=False, _debug=False, may_args4islice=None, turnon__floor_log2_total_count=False):
def main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(sz4alphabet, substrs4avoid, /, *, may_k2sz4alphabet=None, may_prefix=None, with_state_inside_prefix=False, _debug=False, may_args4islice=None, turnon__floor_log2_total_count=False):
[[[
py_adhoc_call   seed.seq_tools.avoid_substrs   ,stable_repr.main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_ '=2**8' '=[["0b11xx_xxxx"]]' '=[["0b10xx_xxxx"]]' '=[]' --may_k2sz4alphabet='{"0b11xx_xxxx":2**6, "0b10xx_xxxx":2**6}' --may_args4islice=6 +turnon__floor_log2_total_count
===
(0, None, None, 0, {}, ({(False, 0): 1}, {}))
(1, None, None, 0, {}, ({}, {(False, 1): 64}))
(2, 12, True, 4096, {(True, 2): 4096}, ({}, {(True, 0): 8192, (True, 2): 4096}))
(3, 19, True, 524288, {(True, 2): 524288}, ({}, {(True, 0): 1048576, (True, 2): 524288}))
(4, 26, True, 67108864, {(True, 2): 67108864}, ({}, {(True, 0): 134217728, (True, 2): 67108864}))
(5, 33, True, 8589934592, {(True, 2): 8589934592}, ({}, {(True, 0): 17179869184, (True, 2): 8589934592}))
]]]

[[[
py_adhoc_call   seed.seq_tools.avoid_substrs   ,stable_repr__expand_top_layer.main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_ '=2**8' '=[["0b11xx_xxxx"]]' '=[["0b10xx_xxxx"]]' '=[]' --may_k2sz4alphabet='{"0b11xx_xxxx":2**6, "0b10xx_xxxx":2**6}' --may_args4islice=6 +turnon__floor_log2_total_count +_debug
===
]]]
[[[
py_adhoc_call   seed.seq_tools.avoid_substrs   ,stable_repr__expand_all_layer.main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_ '=2**8' '=[["0b11xx_xxxx"]]' '=[["0b10xx_xxxx"]]' '=[]' --may_k2sz4alphabet='{"0b11xx_xxxx":2**6, "0b10xx_xxxx":2**6}' --may_args4islice=6 +turnon__floor_log2_total_count +_debug
===
]]]


#]]]'''
__all__ = r'''
StInfo4BeginMarker
    mk_st2is_le_end_st4xxx
        mk_end_sts4xxx
        mk_st2is_inside_end_marker
        mk_st2is_inside_begin_marker
StInfo4Body


Helper4AutoCalc4AvoidSubstr

BasicSetting4MultiCellToken
    Setting4MultiCellToken
BasicCounter4AvoidSubstrs__using_dual_end_delimiter
    Counter4AvoidSubstrs__using_dual_end_delimiter
    _feed__using_hst_
        feed0
        feed_full_steps
        feed_full_step
        iter_feed_full_steps
        feed
        feeds__k_seq
        feeds__ks_seq
        iter_feeds__k_seq
        iter_feeds__ks_seq
    _feed__using_only_st_
        feed0__using_only_end_delimiter_
        feed_full_steps__using_only_end_delimiter_
        feed_full_step__using_only_end_delimiter_
        iter_feed_full_steps__using_only_end_delimiter_
        feed__using_only_end_delimiter_
        feeds__k_seq__using_only_end_delimiter_
        feeds__ks_seq__using_only_end_delimiter_
        iter_feeds__k_seq__using_only_end_delimiter_
        iter_feeds__ks_seq__using_only_end_delimiter_

main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_
    iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_
        iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver1_
        iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver2_
            iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_

main4iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_
    iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_

main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_
    iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_

strings2prefix_st_tree_ex_
    mk_len2sts
    mk_noninit_st2st_k_pair__as_InTree
    mk_noninit_st2longest_proper_suffix_st

    mk_hst2k2hst__as_transition_table_ex
        mk_hst2k2hst__as_transition_table
            mk_st2k2st__as_transition_table_ex2
                mk_st2k2st__as_transition_table_ex

            mk_has_meet_begin_marker4init
            mk_has_meet_begin_marker4post_st
            is_hst_good_as_input
            is_hst_good_as_output
            mk_hst0
            mk_hst2cnt4init

    iadd_
    iter_descendants__ge_

    mk_st2is_eq_end_st4whole
    mk_st2suffix_end_sts
    mk_st2is_eq_end_st4suffix

    mk_st2prev_substr_end_sts
    mk_st2prev_substr_end_sts4xxx
    mk_st2is_ge_end_st4xxx
    mk_st2is_gt_end_st4xxx
    mk_st2is_eq_end_st4xxx
        mk_st2is_ge_end_st4begin_marker
        mk_st2is_gt_end_st4begin_marker
        mk_st2is_eq_end_st4begin_marker
        mk_st2prev_substr_end_sts4begin_marker

    mk_st_infos4xxx
        mk_st_info4body
        mk_st_info4begin_marker
            mk_st_infos4begin_marker

    mk_k2sz4alphabet__5may_
        check_sz4alphabet

    steps5st_
        prefix_sts5st_
        prefix_ks5st_

    mk_st2is_le_sts4xxx

    mk_st2is_eq_end_st4whole4effective_begin_marker
        mk_st2is_eq_end_st4whole4begin_marker



iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_
    iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_
        iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_
            check_settings4layout_with_std_both_marker
        iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_

    iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_
        iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_
            iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_



check_dual_end_marker_have_no_nonempty_overlaps
    check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker
    check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker


'''.split()#'''
__all__

#from seed.seq_tools.prefixes2tree import prefixes2tree_ex_
#from seed.seq_tools.prefixes2tree import calc_transition_table4avoid_substrs_


#from seed.types.NamedTupleBase import NamedTupleBase, mk_NamedTuple, as_dict, replace, extract_as, format_as, as_mapping_view, MappingView4NamedTuple
#def mk_NamedTuple(qname4type, field_names, /, *, defaults=None, module=None, ):
#from seed.seq_tools.prefixes2tree import prefixes2tree_ex_

from seed.tiny import fst, snd, mk_tuple
from seed.tiny import ifNonef, ifNone, echo
from seed.tiny_.check import check_int_ge, check_type_le
from seed.tiny import group4dict_key
from seed.tiny import filter4dict_key, filter4dict_item
from seed.tiny_.mk_reiterable import mk_reiterable, mk_reiterables, mk_reiterable__depth_
from seed.iters.index_iter_ import index_iter_
from itertools import islice, compress# count as count_
import itertools #count
from seed.iters.apply_may_args4islice_ import apply_may_args4islice_
from seed.tiny import chains
from seed.math.floor_ceil import floor_log2
from seed.helper.repr_input import repr_helper
from seed.helper.stable_repr import IGetFuncNameArgsOrderedKwds4stable_repr# register4get__funcname__args__ordered_kwdxxxs, get4get__funcname__args__ordered_kwdxxxs
from seed.helper.auto_calc import BaseAutoCalcAndCache, Injector4Property4AutoCalcAndCache, calc_all #, mk_Property4AutoCalcAndCache
from seed.helper.auto_calc import is_DAG4dependency_graph_, collect_src_names, check_DAG4dependency_graph_, iter_topological_ordering4dependency_graph_
#from seed.helper.auto_calc import mk_onm2inms4dependency_graph_dedges__reversed, collect_src_names, iter_topological_ordering4dependency_graph_, is_DAG4dependency_graph_, mk_reversed_dependency_digraph_, NotDAG_Error, check_DAG4dependency_graph_

__all__


#class BadStepSrc(Exception):pass
class _:
    'cst - complete st'
    def get_cst0(sf, cst, k, /):
        '-> cst0 # maybe not is_cst_good_as_step_src,is_cst_good_as_step_dst'
    def cst2fallback_cst(sf, cst, /):
        '-> cst if step fallback k'
    def cst2iter_nonplain_ks(sf, cst, /):
        '-> Iter k #nonplain#non-fallback'
    def cst2k2cst_(sf, cst, k, /):
        '-> tmay cst'
        '-> cst|BadStepSrc'
    def is_cst_good_as_step_src(sf, cst, /):
        'vs is_hst_good_as_step_src'
    def is_cst_good_as_step_dst(sf, cst, /):
        'vs is_hst_good_as_step_src'
class Helper4AutoCalc4AvoidSubstr(BaseAutoCalcAndCache):
    'calc_all(sf)'
    ###[End__Helper4AutoCalc4AvoidSubstr]:goto
    pass
_injector = Injector4Property4AutoCalcAndCache(Helper4AutoCalc4AvoidSubstr)



r'''[[[
st2k2st__as_OutTree
st2k2st__as_transition_table #not auto drop avoid_substrs yet
noninit_st2longest_proper_suffix_st
    st2suffix_end_sts
    st2prev_substr_end_sts
#]]]'''#'''
@_injector
def strings2prefix_st_tree_ex_(strings, /) -> '(ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_OutTree)':
    'strings/[[k]]{num_strings} -> (ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_OutTree)/(ks/{k}, st0/uint, istr2end_st/[uint]{num_strings}, end_st2istrs/[[uint]]{num_sts}, st2istrs/[[uint]]{num_sts}, st2len/[uint]{num_sts}, forward_tree/st2k2st__as_OutTree/[{k:st}]{num_sts}) #[st0 == 0] #forward_tree =!= transition_table4avoid_substrs'
    ks = {*[]}
    st0 = 0
    istr2end_st = []
    end_st2istrs = [[]]
    st2istrs = [[]]
    st2len = [0]
    st2k2st__as_OutTree = [{}]
        #node2edge2child
        #node2children
    next_st = len(st2len)
    for istr, s in enumerate(strings):
        st = st0
        for len4st, k in enumerate(s, 1):
            ks.add(k)
            st2istrs[st].append(istr)
            #st2k2st__as_OutTree[st][k] = _st
            _st = st2k2st__as_OutTree[st].setdefault(k, next_st)
            if _st == next_st:
                #new st
                next_st += 1
                st2len.append(len4st)
                st2istrs.append([])
                end_st2istrs.append([])
                st2k2st__as_OutTree.append({})
                assert next_st == len(st2len)
            assert st2len[_st] == len4st
            st = _st
        else:
            st2istrs[st].append(istr)
            end_st = st
            end_st2istrs[end_st].append(istr)
            istr2end_st.append(end_st)
    assert len(end_st2istrs) == len(st2istrs) == len(st2len) == len(st2k2st__as_OutTree) == next_st #num_sts

    num_sts = len(st2len)
    num_strings = len(istr2end_st)

    ######################
    assert num_strings == sum(map(len, end_st2istrs))
    assert num_strings == (1 + max(chains(end_st2istrs), default=-1))

    return (ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_OutTree)
#end-def strings2prefix_st_tree_ex_(strings, /):

@_injector
def mk_len2sts(st2len, /):
    '-> len2sts'
    max_len4st = max(st2len, default=-1)
    len2sts = [[] for _ in range(max_len4st+1)]
    for st, len4st in enumerate(st2len):
        len2sts[len4st].append(st)
    return len2sts
    #num_sts = len(st2len)
    #max_len4st = len(len2sts)-1

@_injector
def mk_noninit_st2st_k_pair__as_InTree(st0, st2k2st__as_OutTree, /):
    '-> noninit_st2st_k_pair__as_InTree'
    num_sts = len(st2k2st__as_OutTree)
    ######################
    noninit_st2st_k_pair__as_InTree = [None]*num_sts
        #node2may_parent
        # :: [(st,k)]

    if 1:
        noninit_st2st_k_pair__as_InTree[st0] = None

    for st_, k2st__as_branches in enumerate(st2k2st__as_OutTree):
        for k, _st in k2st__as_branches.items():
            # (st_/parent, k/edge, _st/child)
            noninit_st2st_k_pair__as_InTree[_st] = (st_, k)
    noninit_st2st_k_pair__as_InTree

    assert noninit_st2st_k_pair__as_InTree[st0] is None
    assert all((noninit_st2st_k_pair__as_InTree[st] is None) is (st is st0) for st in range(num_sts))
    assert sum(map(len, st2k2st__as_OutTree)) == num_sts - 1 #树边的数目 == 树节点的数目-1
    ######################
    return noninit_st2st_k_pair__as_InTree




#@_injector #use mk_st2k2st__as_transition_table_ex instead
def mk_noninit_st2longest_proper_suffix_st(len2sts, st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, /) -> 'noninit_st2longest_proper_suffix_st':
    'see:mk_st2k2st__as_transition_table_ex'
    num_sts = len(st2k2st__as_OutTree)
    ######################
    noninit_st2longest_proper_suffix_st = [None]*num_sts
        #==>> [prefix_of_(st).endswith(prefix_of_(noninit_st2longest_proper_suffix_st[st]))]

    if 1:
        len4st = 0
        if len4st < len(len2sts):
            [st0] = len2sts[len4st]
            noninit_st2longest_proper_suffix_st[st0] = None

    if 1:
        len4st = 1
        if len4st < len(len2sts):
            for st in len2sts[len4st]:
                noninit_st2longest_proper_suffix_st[st] = st0

    if 1:
        #if 2 < L:
        for len4st in range(2, len(len2sts)):
            for _st in len2sts[len4st]:
                (st_, k) = noninit_st2st_k_pair__as_InTree[_st]
                _st_ = noninit_st2longest_proper_suffix_st[st_]
                while not (_st_ == st0 or k in st2k2st__as_OutTree[_st_]):
                    #slow? see:mk_st2k2st__as_transition_table_ex
                    _st_ = noninit_st2longest_proper_suffix_st[_st_]
                __st = st2k2st__as_OutTree[_st_].get(k, st0)
                noninit_st2longest_proper_suffix_st[_st] = __st
    noninit_st2longest_proper_suffix_st

    assert noninit_st2longest_proper_suffix_st[st0] is None
    assert all((noninit_st2longest_proper_suffix_st[st] is None) is (st is st0) for st in range(num_sts))

    ######################
    return noninit_st2longest_proper_suffix_st


@_injector
def mk_st2k2st__as_transition_table_ex(len2sts, noninit_st2st_k_pair__as_InTree, st2k2st__as_OutTree, /):
    '-> (noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table)'
    num_sts = len(st2k2st__as_OutTree)
    ######################
    st2k2st__as_transition_table = [{} for _ in range(num_sts)]
    noninit_st2longest_proper_suffix_st = [None]*num_sts

    if 1:
        len4st = 0
        if len4st < len(len2sts):
            [st0] = len2sts[len4st]
            st2k2st__as_transition_table[st0].update(st2k2st__as_OutTree[st0])
            noninit_st2longest_proper_suffix_st[st0] = None

    if 1:
        len4st = 1
        if len4st < len(len2sts):
            for _st in len2sts[len4st]:
                (st_, k) = noninit_st2st_k_pair__as_InTree[_st]
                assert st_ == st0
                noninit_st2longest_proper_suffix_st[_st] = st0

    for len4st in range(1, len(len2sts)):
        #initialized: noninit_st2longest_proper_suffix_st@len2sts
        #uninitialized yet: st2k2st__as_transition_table@len2sts
        for _st in len2sts[len4st]:
            (st_, k) = noninit_st2st_k_pair__as_InTree[_st]
            __st = noninit_st2longest_proper_suffix_st[_st]
            _d = st2k2st__as_transition_table[__st]
            st2k2st__as_transition_table[_st].update(_d)
            #overwrite above:
            d = st2k2st__as_OutTree[_st]
            st2k2st__as_transition_table[_st].update(d)
            ######################
            #init next layer sts of len4st+1
            for k, next_layer_st in d.items():
                noninit_st2longest_proper_suffix_st[next_layer_st] = _d.get(k, st0)
                #assert st2len[next_layer_st] == len4st+1


    ######################
    return (noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table)
    ######################

def mk_has_meet_begin_marker4init():
    return False
def mk_has_meet_begin_marker4post_st(st2is_ge_end_st4begin_marker, has_meet_begin_marker, st, /):
    'hst:has_meet_begin_marker donot consider st yet'
    #to mk hst2k2hst__as_transition_table
    return has_meet_begin_marker or st2is_ge_end_st4begin_marker[st]
    ########
    if has_meet_begin_marker:
        _has_meet_begin_marker = True
    #elif st2is_gt_end_st4begin_marker[st]:
    #    _has_meet_begin_marker = True
    #    #raise ValueError
    else:
        _has_meet_begin_marker = st2is_ge_end_st4begin_marker[st]
    return _has_meet_begin_marker



def is_hst_good_as_input(st2is_eq_end_st4begin_marker, st2is_gt_end_st4begin_marker, st2is_ge_end_st4begin_marker, st2prev_substr_end_sts4begin_marker, hst, /):
    'input side(key) of hst2k2hst__as_transition_table'
    #[def____permit_pattern4hst8transition_table]:goto
    'NOTE:[eq |>=| ge&&(not gt) == fst_eq]'
    has_meet_begin_marker, st = hst
    if has_meet_begin_marker:
        # (True, not eq) -> k -> (True, [to_del eq]||not eq)
        return not st2is_eq_end_st4begin_marker[st] and len(st2prev_substr_end_sts4begin_marker[st]) < 2
    else:
        # (False, not ge) -> k -> (False, (not ge)||fst_eq)
        # (False, fst_eq) -> k -> (True, [to_del eq]||not eq)
        return (not st2is_gt_end_st4begin_marker[st])
def is_hst_good_as_output(st2is_eq_end_st4begin_marker, st2is_gt_end_st4begin_marker, st2is_ge_end_st4begin_marker, st2prev_substr_end_sts4begin_marker, hst, /):
    'output side(value) of hst2k2hst__as_transition_table'
    #[def____permit_pattern4hst8transition_table]:goto
    'NOTE:[eq |>=| ge&&(not gt) == fst_eq]'
    #[def____permit_pattern4hst8transition_table]:goto
    has_meet_begin_marker, st = hst
    if has_meet_begin_marker:
        # (True, not eq) -> k -> (True, [to_del eq]||not eq)
        return len(st2prev_substr_end_sts4begin_marker[st]) < 2 or (len(st2prev_substr_end_sts4begin_marker[st]) == 2 and st2is_eq_end_st4begin_marker[st])
    else:
        # (False, not ge) -> k -> (False, (not ge)||fst_eq)
        # (False, fst_eq) -> k -> (True, [to_del eq]||not eq)
        return (not st2is_gt_end_st4begin_marker[st])
    raise logic-err
    #!! [del eq]@True
    #   now, output pattern <=> input pattern
    #return is_hst_good_as_input(st2is_eq_end_st4begin_marker, st2is_ge_end_st4begin_marker, hst)

def _check_st0(_is_hst_good_as_input, _is_hst_good_as_output, st2is_eq_end_st4begin_marker, st2is_ge_end_st4begin_marker, st0, /):
    #[def____permit_pattern4hst8transition_table]:goto
    hst0 = mk_hst0(st0)
    hsts4fallback = [(False, st0), (True, st0)]
    if not _is_hst_good_as_input(hst0): raise ValueError
        # !! [hst0 MUST BE permitted]
    #xxx if st2is_eq_end_st4begin_marker[st0]: raise ValueError
        # !! [hsts4fallback MUST BE permitted]

    if not all(map(_is_hst_good_as_output, hsts4fallback)): raise ValueError
        # !! [hsts4fallback MUST BE permitted]

class _Base4Repr(IGetFuncNameArgsOrderedKwds4stable_repr):
    def _get_vars(sf, /):
        _vars__export = filter4dict_key(lambda nm:not nm.startswith('_'), vars(sf))
        return _vars__export
        d = {**vars(sf)}
        #for k in '__class__ _vars'.split():
        for k in '__class__'.split():
            d.pop(k, 0)
        #print(' '.join(sorted(d)))
        return d
    def __repr__(sf, /):
        return '<{}>'.format(repr_helper(sf, **sf._get_vars()))
    def ___get__funcname__args__ordered_kwdxxxs___(sf):
        return (None, [], sorted(sf._get_vars().items()))

#st_info4begin_marker
class StInfo4BeginMarker(_Base4Repr):
    'without end_marker/forbidden_substr'
    #mk_st_infos4xxx/StInfo4BeginMarker/StInfo4Body
    def __init__(sf, st2is_eq_end_st4begin_marker, st2is_ge_end_st4begin_marker, st2is_gt_end_st4begin_marker, st2prev_substr_end_sts4begin_marker, /):
        sf.st2is_eq_end_st4begin_marker = st2is_eq_end_st4begin_marker
        sf.st2is_ge_end_st4begin_marker = st2is_ge_end_st4begin_marker
        sf.st2is_gt_end_st4begin_marker = st2is_gt_end_st4begin_marker
        sf.st2prev_substr_end_sts4begin_marker = st2prev_substr_end_sts4begin_marker
        #sf.x = x
    def is_hst_good_as_input(sf, hst, /):
        'input side(key) of hst2k2hst__as_transition_table'
        return is_hst_good_as_input(sf.st2is_eq_end_st4begin_marker, sf.st2is_gt_end_st4begin_marker, sf.st2is_ge_end_st4begin_marker, sf.st2prev_substr_end_sts4begin_marker, hst)
    def is_hst_good_as_output(sf, hst, /):
        'output side(value) of hst2k2hst__as_transition_table'
        return is_hst_good_as_output(sf.st2is_eq_end_st4begin_marker, sf.st2is_gt_end_st4begin_marker, sf.st2is_ge_end_st4begin_marker, sf.st2prev_substr_end_sts4begin_marker, hst)
    def check_st0(sf, st0, /):
        _check_st0(sf.is_hst_good_as_input, sf.is_hst_good_as_output, sf.st2is_eq_end_st4begin_marker, sf.st2is_ge_end_st4begin_marker, st0)
    def mk_has_meet_begin_marker4post_st(sf, hst, /):
        (has_meet_begin_marker_, st_) = hst
        _has_meet_begin_marker = mk_has_meet_begin_marker4post_st(sf.st2is_ge_end_st4begin_marker, has_meet_begin_marker_, st_)
        return _has_meet_begin_marker

@_injector
def _mk_st_info4begin_marker(st2is_eq_end_st4begin_marker, st2is_ge_end_st4begin_marker, st2is_gt_end_st4begin_marker, st2prev_substr_end_sts4begin_marker, /) -> 'st_info4begin_marker':
    'vs mk_st_info4begin_marker'
    st_info4begin_marker = StInfo4BeginMarker(st2is_eq_end_st4begin_marker, st2is_ge_end_st4begin_marker, st2is_gt_end_st4begin_marker, st2prev_substr_end_sts4begin_marker)
    return st_info4begin_marker

def mk_hst0(st0, /):
    has_meet_begin_marker = mk_has_meet_begin_marker4init()
    hst0 = (has_meet_begin_marker, st0)
    return hst0

@_injector
#def mk_hst2k2hst__as_transition_table(st_info4begin_marker:StInfo4BeginMarker, len2sts, noninit_st2st_k_pair__as_InTree, st2k2st__as_transition_table, /):
def mk_hst2k2hst__as_transition_table(st_info4begin_marker:StInfo4BeginMarker, st2k2st__as_transition_table, /) -> 'hst2k2hst__as_transition_table':
    'vs mk_hst2k2hst__as_transition_table_ex'
    sf = st_info4begin_marker
    ft = False, True
    hst2k2hst__as_transition_table = {}
        #[def____permit_pattern4hst8transition_table]:here
        #NOTE:[eq |>=| ge&&(not gt) == fst_eq]
        # [fst_eq =[def]= ge&&(not gt)]
        #permit pattern:
        # (False, (not ge)) -> k -> (False, (not ge)||fst_eq)
        # (False, fst_eq) -> k -> (True, [to_del eq]||(not eq))
        # (True, (not eq)) -> k -> (True, [to_del eq]||(not eq))
        ###[hst0 =[def]= (False, st0)]
        ###[hsts4fallback =[def]= [(False, st0), (True, st0)]]
        ###[hst0 MUST BE permitted]
        ###[hsts4fallback MUST BE permitted]
        # (False, st0:(not ge)) -> k -> (False, (not ge)||fst_eq)
        # xxx (False, st0:fst_eq) -> k -> (True, [to_del eq]||not eq)
        # (True, st0:(not eq)) -> k -> (True, [to_del eq]||not eq)
        ### xxx ??? ==>> [st0 MUST BE (not eq)]
        ### xxx ??? ==>> [not st2is_eq_end_st4begin_marker[st0]]
    #print(sf.st2is_ge_end_st4begin_marker)
    for st_, k2_st in enumerate(st2k2st__as_transition_table):
        for k, _st in k2_st.items():
            for has_meet_begin_marker_ in ft:
                hst_ = (has_meet_begin_marker_, st_)
                if not sf.is_hst_good_as_input(hst_): continue
                k2_hst = hst2k2hst__as_transition_table.setdefault(hst_, {})
                    # ==>> [[hst in hst2k2hst__as_transition_table] <-> [_is_hst_good_as_input(hst)]]
                    # ==>> distinguish fallback and bad_hst
                    #see:_feed__using_hst_()::_is_hst_bad()
                ##########
                #_has_meet_begin_marker = mk_has_meet_begin_marker4post_st(sf.st2is_ge_end_st4begin_marker, has_meet_begin_marker_, st_)
                _has_meet_begin_marker = sf.mk_has_meet_begin_marker4post_st(hst_)
                _hst = (_has_meet_begin_marker, _st)
                if not sf.is_hst_good_as_output(_hst): continue
                k2_hst[k] = _hst

    return hst2k2hst__as_transition_table

    r'''[[[
    ##bug:logic-err:below: not use st2k2st__as_transition_table; using(len2sts,noninit_st2st_k_pair__as_InTree) make nonsense
    #
    xxx sf = st_info4begin_marker
    xxx hst2k2hst__as_transition_table = {}
    xxx if 1:
    xxx     len4st = 0
    xxx     if len4st < len(len2sts):
    xxx         [st0] = len2sts[len4st]
    xxx         sf.check_st0(st0)

    xxx if 1:
    xxx     ft = False, True
    xxx     for len4st in range(1, len(len2sts)):
    xxx         for _st in len2sts[len4st]:
    xxx             (st_, k) = noninit_st2st_k_pair__as_InTree[_st]
    xxx             for has_meet_begin_marker_ in ft:
    xxx                 hst_ = (has_meet_begin_marker_, st_)
    xxx                 if not sf.is_hst_good_as_input(hst_): continue
    xxx                 k2_hst = hst2k2hst__as_transition_table.setdefault(hst_, {})
    xxx                     # ==>> [[hst in hst2k2hst__as_transition_table] <-> [_is_hst_good_as_input(hst)]]
    xxx                     # ==>> distinguish fallback and bad_hst
    xxx                     #see:_feed__using_hst_()::_is_hst_bad()
    xxx                 ##########
    xxx                 _has_meet_begin_marker = mk_has_meet_begin_marker4post_st(sf.st2is_ge_end_st4begin_marker, has_meet_begin_marker_, st_)
    xxx                 _hst = (_has_meet_begin_marker, _st)
    xxx                 if not sf.is_hst_good_as_output(_hst): continue
    xxx                 k2_hst[k] = _hst

    xxx return hst2k2hst__as_transition_table
    #]]]'''#'''
def check_sz4alphabet(k2sz4alphabet, sz4alphabet, /):
    if not all(sz >= 0 for sz in k2sz4alphabet.values()): raise ValueError
    if not sum(k2sz4alphabet.values()) <= sz4alphabet: raise ValueError

def mk_hst2cnt4init(st0, cnt=1, /):
    assert cnt >= 0
    hst0 = mk_hst0(st0)
    return {hst0:cnt}
def _feed__using_hst_(sz4alphabet, k2sz4alphabet, st0, st2is_ge_end_st4begin_marker, hst2k2hst__as_transition_table, hst2cnt, ks8step, /, *, _full_step_):
    r'''
    consider begin_marker only, donot take end_marker/forbidden_substr into account
    _feed__using_hst_ :: sz4alphabet/uint -> k2sz4alphabet/{k:uint} -> st0/uint -> st2is_ge_end_st4begin_marker/[bool] -> hst2k2hst__as_transition_table/{hst:{k:hst}} -> hst2cnt/{hst:uint} -> ks8step/{k} -> hst2cnt/{hst:uint}
        [#st0 to mk hsts4fallback#]
        [#hst = (has_meet_begin_marker/bool, st/uint)#]
        [k2sz4alphabet:eg.sz4alphabet=2**8,k=0b1xxx_xxx,sz4alphabet4k=2**7#]'
    '''#'''
    #check_sz4alphabet(k2sz4alphabet, sz4alphabet)
    if not _full_step_ is (ks8step is True): raise TypeError
    if not _full_step_:
        if not ks8step <= k2sz4alphabet.keys():raise ValueError
        if not len(ks8step) == len(frozenset(ks8step)):raise ValueError

    def _is_hst_good_as_input(hst, /):
        return hst in hst2k2hst__as_transition_table
    def _is_hst_bad(hst, /):
        return not hst in hst2k2hst__as_transition_table

    _hst2cnt = {}
    for hst_, cnt_ in hst2cnt.items():
        if not cnt_ >= 0: raise ValueError
        if cnt_ == 0:
            continue
        if _is_hst_bad(hst_):
            continue
        k2_hst = hst2k2hst__as_transition_table[hst_]
        ##########
        sz4alphabet4fallback4full = sz4alphabet
        sz4alphabet4fallback4skips = 0
        if _full_step_:
            ks8step = k2_hst.keys()
        for k in ks8step:
            sz4alphabet4k = k2sz4alphabet[k]
            if not sz4alphabet4k >= 0: raise ValueError
            if sz4alphabet4k == 0:
                continue
            if not k in k2_hst:
                sz4alphabet4fallback4full += sz4alphabet4k
                continue
                #count as fallback
            sz4alphabet4fallback4full -= sz4alphabet4k
            if not sz4alphabet4fallback4full >= 0: raise ValueError
            ########
            _hst = k2_hst[k]
            if _is_hst_bad(_hst):
                #discard sz4alphabet4k
                continue
            _cnt = cnt_ * sz4alphabet4k
            assert _cnt > 0
            iadd_(_hst2cnt, _hst, _cnt)
        if not sz4alphabet4fallback4full >= 0: raise ValueError
        if not sz4alphabet4fallback4skips >= 0: raise ValueError

        sz4alphabet4fallback = sz4alphabet4fallback4full if _full_step_ else sz4alphabet4fallback4skips

        if sz4alphabet4fallback > 0:
            #fallback
            has_meet_begin_marker_, st_ = hst_
            #bug:_hst = (has_meet_begin_marker_, st0)
            _has_meet_begin_marker = mk_has_meet_begin_marker4post_st(st2is_ge_end_st4begin_marker, has_meet_begin_marker_, st_)
            _st = st0
            _hst = (_has_meet_begin_marker, _st)
            if _is_hst_bad(_hst):
                #discard sz4alphabet4fallback
                continue
            _cnt = cnt_ * sz4alphabet4fallback
            assert _cnt > 0
            iadd_(_hst2cnt, _hst, _cnt)
    return _hst2cnt

def iadd_(_st2n, _st, n, /):
    assert n > 0
    _n = _st2n.get(_st, 0)
    _st2n[_st] = _n + n

#st_info4body
class StInfo4Body(_Base4Repr):
    'without begin_marker'
    #mk_st_infos4xxx/StInfo4BeginMarker/StInfo4Body
    def __init__(sf, st2is_ge_end_st4forbidden_substr, st2is_ge_end_st4end_marker, st2is_gt_end_st4end_marker, /):
        sf.st2is_ge_end_st4forbidden_substr = st2is_ge_end_st4forbidden_substr
        sf.st2is_ge_end_st4end_marker = st2is_ge_end_st4end_marker
        sf.st2is_gt_end_st4end_marker = st2is_gt_end_st4end_marker
    ########
    def is_st_good_as_step_src(sf, st, /):
        return not (sf.st2is_ge_end_st4forbidden_substr[st] or sf.st2is_ge_end_st4end_marker[st])
    def is_st_good_as_step_dst(sf, st, /):
        return not (sf.st2is_ge_end_st4forbidden_substr[st] or sf.st2is_gt_end_st4end_marker[st])

    ########
    def is_hst_good_as_step_src(sf, hst, /):
        has_meet_begin_marker, st = hst
        return sf.is_st_good_as_step_src(st)
    def is_hst_good_as_step_dst(sf, hst, /):
        has_meet_begin_marker, st = hst
        return sf.is_st_good_as_step_dst(st)
    ########

@_injector
def _mk_st_info4body(st2is_ge_end_st4forbidden_substr, st2is_ge_end_st4end_marker, st2is_gt_end_st4end_marker, /) -> 'st_info4body':
    'vs mk_st_info4body'
    st_info4body = StInfo4Body(st2is_ge_end_st4forbidden_substr, st2is_ge_end_st4end_marker, st2is_gt_end_st4end_marker)
    return st_info4body

def feed0(st_info4body:StInfo4Body, hst2k2hst__as_transition_table, hst2cnt, /):
    hst2cnt = feed(st_info4body, None, None, None, None, hst2k2hst__as_transition_table, hst2cnt, None, _no_step_=True)
    return hst2cnt
def feed_full_steps(st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, num_steps, /):
    hst2cnt__iter = iter_feed_full_steps(st_info4body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt)
    hst2cnt__seq = [*islice(hst2cnt__iter, 1+num_steps)]
    return hst2cnt__seq
def feed_full_step(st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, /):
    [_, hst2cnt] = feed_full_steps(st_info4body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, 1)
    return hst2cnt
def iter_feed_full_steps(st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, /):
    hst2cnt = feed0(st_info4body, hst2k2hst__as_transition_table, hst2cnt)
    while 1:
        yield hst2cnt
        hst2cnt = feed(st_info4body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, True, _full_step_=True)
    #return hst2cnt
#def feed(st_info4body:StInfo4Body, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, ks8step, /, *, _no_step_=False, _full_step_=False):
def feed(st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, ks8step, /, *, _no_step_=False, _full_step_=False):
    st2is_ge_end_st4begin_marker
    if 1:
        iter_feed_full_steps
        if not _full_step_ is (ks8step is True): raise TypeError
    if 1:
        feed0
        if not _no_step_ is (ks8step is None): raise TypeError
        if not _no_step_ is (k2sz4alphabet is None): raise TypeError
        if not _no_step_ is (sz4alphabet is None): raise TypeError
        if not _no_step_ is (st0 is None): raise TypeError
        if not _no_step_ is (st2is_ge_end_st4begin_marker is None): raise TypeError

    def _is_hst_good_src(hst, /):
        return hst in hst2k2hst__as_transition_table and st_info4body.is_hst_good_as_step_src(hst)
    def _is_hst_good_dst(hst, /):
        return hst in hst2k2hst__as_transition_table and st_info4body.is_hst_good_as_step_dst(hst)
            #begin_marker   &&   end_marker&&forbidden_substr

    #hst2cnt_ = filter4dict_key(st_info4body.is_hst_good_as_step_src, hst2cnt)
    if _no_step_:
        #no step ==>> no step_src
        hst2cnt_ = hst2cnt
    else:
        hst2cnt_ = filter4dict_item(lambda hst,cnt,/:cnt>0 and _is_hst_good_src(hst), hst2cnt)

    hst2cnt_;       del hst2cnt
    if _no_step_:
        assert ks8step is None
        _hst2cnt = hst2cnt_
    else:
        assert not ks8step is None
        _hst2cnt = _feed__using_hst_(sz4alphabet, k2sz4alphabet, st0, st2is_ge_end_st4begin_marker, hst2k2hst__as_transition_table, hst2cnt_, ks8step, _full_step_=_full_step_)

    _hst2cnt;       del hst2cnt_
    _2_hst2cnt = filter4dict_key(_is_hst_good_dst, _hst2cnt)

    _2_hst2cnt;     del _hst2cnt
    return _2_hst2cnt
feed

@_injector
def mk_st2is_eq_end_st4whole(end_st2istrs, /):
    '-> st2is_eq_end_st4whole'
    st2is_eq_end_st4whole = [*map(bool, end_st2istrs)]
    return st2is_eq_end_st4whole

@_injector
#def mk_st2suffix_end_sts(len2sts, st2is_eq_end_st4whole, noninit_st2longest_proper_suffix_st, /):
def mk_st2suffix_end_sts(st2is_eq_end_st4whole, noninit_st2longest_proper_suffix_st, /):
    '-> st2suffix_end_sts'
    def put(st, ls, /):
        st2suffix_end_sts[st] = [*ls, st] if st2is_eq_end_st4whole[st] else [*ls]
    num_sts = len(st2is_eq_end_st4whole)
    #st2suffix_end_sts = [[] for _ in range(num_sts)]
    st2suffix_end_sts = [None]*num_sts
    sts = [*range(num_sts)]
    while sts:
        st = sts[-1]
        if not st2suffix_end_sts[st] is None:
            #repeat st in sts
            sts.pop()
            continue
        may_suffix_st = noninit_st2longest_proper_suffix_st[st]
        if may_suffix_st is None:
            [st0] = [st for st,m in enumerate(noninit_st2longest_proper_suffix_st) if m is None]
            assert st == st0
            ls = []
        else:
            suffix_st = may_suffix_st
            if st2suffix_end_sts[suffix_st] is None:
                #recur call
                sts.append(suffix_st)
                continue
            ls = st2suffix_end_sts[suffix_st]
        put(st, ls)
        sts.pop()
    assert all(not s is None for s in st2suffix_end_sts)
    return st2suffix_end_sts

def iter_descendants__ge_(st2k2st__as_OutTree, st, /):
    ls = [st]
    while ls:
        st = ls.pop()
        yield st
        ls.extend(st2k2st__as_OutTree[st].values())
def mk_st2prev_substr_end_sts4xxx(st2is_eq_end_st4xxx, st2k2st__as_OutTree, /):
    num_sts = len(st2is_eq_end_st4xxx)
    st2prev_substr_end_sts4xxx = [[] for _ in range(num_sts)]
    for st in range(num_sts):
        if st2is_eq_end_st4xxx[st]:
            prev_substr_end_st4xxx = st
            for _st in iter_descendants__ge_(st2k2st__as_OutTree, prev_substr_end_st4xxx):
                st2prev_substr_end_sts4xxx[_st].append(prev_substr_end_st4xxx)
    return st2prev_substr_end_sts4xxx

@_injector
def mk_st2is_eq_end_st4suffix(st2suffix_end_sts, /) -> 'st2is_eq_end_st4suffix':
    'mk_st2is_eq_end_st4whole vs mk_st2is_eq_end_st4suffix'
    st2is_eq_end_st4suffix = [*map(bool, st2suffix_end_sts)]
    return st2is_eq_end_st4suffix
@_injector
def mk_st2prev_substr_end_sts(st2is_eq_end_st4suffix, st2k2st__as_OutTree, /) -> 'st2prev_substr_end_sts':
    st2prev_substr_end_sts = mk_st2prev_substr_end_sts4xxx(st2is_eq_end_st4suffix, st2k2st__as_OutTree)
    return st2prev_substr_end_sts
def mk_st2is_ge_end_st4xxx(st2prev_substr_end_sts4xxx, /):
    st2is_ge_end_st4xxx = [*map(bool, st2prev_substr_end_sts4xxx)]
    return st2is_ge_end_st4xxx
def mk_st2is_gt_end_st4xxx(noninit_st2st_k_pair__as_InTree, st2prev_substr_end_sts4xxx, st2is_ge_end_st4xxx, /):
    num_sts = len(st2prev_substr_end_sts4xxx)
    if num_sts:
        [st0] = [st for st,m in enumerate(noninit_st2st_k_pair__as_InTree) if m is None]
    st2is_gt_end_st4xxx = [(not st == st0) and st2is_ge_end_st4xxx[noninit_st2st_k_pair__as_InTree[st][0]] for st in range(num_sts)]
    return st2is_gt_end_st4xxx


def mk_st2is_eq_end_st4xxx(istr2is_xxx, end_st2istrs, st2suffix_end_sts):
    num_sts = len(st2suffix_end_sts)
    st2is_eq_end_st4xxx = [any(istr2is_xxx[istr] for istr in end_st2istrs[st]) for st in range(num_sts)]
    return st2is_eq_end_st4xxx

#st2suffix_end_sts
#st2prev_substr_end_sts

#st2prev_substr_end_sts4begin_marker

@_injector
def mk_st2is_eq_end_st4begin_marker(istr2is_begin_marker, end_st2istrs, st2suffix_end_sts, /) -> 'st2is_eq_end_st4begin_marker':
    st2is_eq_end_st4begin_marker = mk_st2is_eq_end_st4xxx(istr2is_begin_marker, end_st2istrs, st2suffix_end_sts)
    return st2is_eq_end_st4begin_marker

@_injector
def mk_st2prev_substr_end_sts4begin_marker(st2is_eq_end_st4begin_marker, st2k2st__as_OutTree, /) -> 'st2prev_substr_end_sts4begin_marker':
    st2prev_substr_end_sts4begin_marker = mk_st2prev_substr_end_sts4xxx(st2is_eq_end_st4begin_marker, st2k2st__as_OutTree)
    return st2prev_substr_end_sts4begin_marker
@_injector
def mk_st2is_ge_end_st4begin_marker(st2prev_substr_end_sts4begin_marker, /) -> 'st2is_ge_end_st4begin_marker':
    st2is_ge_end_st4begin_marker = mk_st2is_ge_end_st4xxx(st2prev_substr_end_sts4begin_marker)
    return st2is_ge_end_st4begin_marker
@_injector
def mk_st2is_gt_end_st4begin_marker(noninit_st2st_k_pair__as_InTree, st2prev_substr_end_sts4begin_marker, st2is_ge_end_st4begin_marker, /) -> 'st2is_gt_end_st4begin_marker':
    st2is_gt_end_st4begin_marker = mk_st2is_gt_end_st4xxx(noninit_st2st_k_pair__as_InTree, st2prev_substr_end_sts4begin_marker, st2is_ge_end_st4begin_marker)
    return st2is_gt_end_st4begin_marker

#@_injector _mk_st_info4body
def mk_st_info4body(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_forbidden_substr, istr2is_end_marker, /):
    'mk_st_infos4xxx/StInfo4BeginMarker/StInfo4Body'
    (st2is_eq_end_st4forbidden_substr, st2is_ge_end_st4forbidden_substr, st2is_gt_end_st4forbidden_substr, st2prev_substr_end_sts4forbidden_substr) = mk_st_infos4xxx(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_forbidden_substr)
    (st2is_eq_end_st4end_marker, st2is_ge_end_st4end_marker, st2is_gt_end_st4end_marker, st2prev_substr_end_sts4end_marker) = mk_st_infos4xxx(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_end_marker)
    st_info4body = StInfo4Body(st2is_ge_end_st4forbidden_substr, st2is_ge_end_st4end_marker, st2is_gt_end_st4end_marker)
    return st_info4body
#@_injector _mk_st_info4begin_marker
def mk_st_info4begin_marker(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_begin_marker, /):
    'mk_st_infos4xxx/StInfo4BeginMarker/StInfo4Body'
    st_info4begin_marker = StInfo4BeginMarker(*mk_st_infos4begin_marker(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_begin_marker))
    return st_info4begin_marker
def mk_st_infos4begin_marker(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_begin_marker, /):
    'mk_st_infos4xxx/StInfo4BeginMarker/StInfo4Body'
    return mk_st_infos4xxx(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_begin_marker)
    ########
    istr2is_begin_marker
    ########
    st2is_eq_end_st4begin_marker = mk_st2is_eq_end_st4begin_marker(istr2is_begin_marker, end_st2istrs, st2suffix_end_sts)
    st2prev_substr_end_sts4begin_marker = mk_st2prev_substr_end_sts4begin_marker(st2is_eq_end_st4begin_marker, st2k2st__as_OutTree)
    st2is_ge_end_st4begin_marker = mk_st2is_ge_end_st4begin_marker(st2prev_substr_end_sts4begin_marker)
    st2is_gt_end_st4begin_marker = mk_st2is_gt_end_st4begin_marker(noninit_st2st_k_pair__as_InTree, st2prev_substr_end_sts4begin_marker, st2is_ge_end_st4begin_marker)
    return (st2is_eq_end_st4begin_marker, st2is_ge_end_st4begin_marker, st2is_gt_end_st4begin_marker, st2prev_substr_end_sts4begin_marker)



def mk_st_infos4xxx(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_xxx, /):
    'StInfo4BeginMarker/StInfo4Body'
    #mk_st_infos4begin_marker
    #mk_st_info4begin_marker
    istr2is_xxx
    ########
    st2is_eq_end_st4xxx = mk_st2is_eq_end_st4xxx(istr2is_xxx, end_st2istrs, st2suffix_end_sts)
    st2prev_substr_end_sts4xxx = mk_st2prev_substr_end_sts4xxx(st2is_eq_end_st4xxx, st2k2st__as_OutTree)
    st2is_ge_end_st4xxx = mk_st2is_ge_end_st4xxx(st2prev_substr_end_sts4xxx)
    st2is_gt_end_st4xxx = mk_st2is_gt_end_st4xxx(noninit_st2st_k_pair__as_InTree, st2prev_substr_end_sts4xxx, st2is_ge_end_st4xxx)
    return (st2is_eq_end_st4xxx, st2is_ge_end_st4xxx, st2is_gt_end_st4xxx, st2prev_substr_end_sts4xxx)



def mk_st2k2st__as_transition_table_ex2(st0, st2len, st2k2st__as_OutTree, /):
    len2sts = mk_len2sts(st2len)
    noninit_st2st_k_pair__as_InTree = mk_noninit_st2st_k_pair__as_InTree(st0, st2k2st__as_OutTree)
    (noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table) = mk_st2k2st__as_transition_table_ex(len2sts, noninit_st2st_k_pair__as_InTree, st2k2st__as_OutTree)
        #noninit_st2longest_proper_suffix_st = mk_noninit_st2longest_proper_suffix_st(len2sts, st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree)
    return (len2sts, noninit_st2st_k_pair__as_InTree, noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table)
def mk_hst2k2hst__as_transition_table_ex(st0, end_st2istrs, st2len, st2k2st__as_OutTree, istr2is_begin_marker, /):
    r'''-> (len2sts, noninit_st2st_k_pair__as_InTree, noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table, st2is_eq_end_st4whole, st2suffix_end_sts, st_info4begin_marker, hst2k2hst__as_transition_table)

        vs mk_hst2k2hst__as_transition_table
    '''#'''
    (len2sts, noninit_st2st_k_pair__as_InTree, noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table) = mk_st2k2st__as_transition_table_ex2(st0, st2len, st2k2st__as_OutTree)
    st2is_eq_end_st4whole = mk_st2is_eq_end_st4whole(end_st2istrs)
    st2suffix_end_sts = mk_st2suffix_end_sts(st2is_eq_end_st4whole, noninit_st2longest_proper_suffix_st)
    st_info4begin_marker = mk_st_info4begin_marker(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_begin_marker)

    #hst2k2hst__as_transition_table = mk_hst2k2hst__as_transition_table(st_info4begin_marker, len2sts, noninit_st2st_k_pair__as_InTree, st2k2st__as_transition_table)
    hst2k2hst__as_transition_table = mk_hst2k2hst__as_transition_table(st_info4begin_marker, st2k2st__as_transition_table)
    if 1:
    #done:
        #len2sts
        #noninit_st2st_k_pair__as_InTree
        #noninit_st2longest_proper_suffix_st
        #st2k2st__as_transition_table
        #st2is_eq_end_st4whole
        #st2suffix_end_sts
        #st_info4begin_marker
        st0
        end_st2istrs
        st2len
        st2k2st__as_OutTree
            #(ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_OutTree) = strings2prefix_st_tree_ex_(strings, /)
        istr2is_begin_marker
    return (len2sts, noninit_st2st_k_pair__as_InTree, noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table, st2is_eq_end_st4whole, st2suffix_end_sts, st_info4begin_marker, hst2k2hst__as_transition_table)


def feeds__k_seq(st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, k_seq, /):
    'len(output) == 1+len(input)'
    hst2cnt__iter = iter_feeds__k_seq(st_info4body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, k_seq)
    hst2cnt__seq = [*hst2cnt__iter]
    return hst2cnt__seq
def iter_feeds__k_seq(st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, k_seq, /):
    'len(output) == 1+len(input)'
    ks_seq = ({k} for k in k_seq)
    hst2cnt__iter = iter_feeds__ks_seq(st_info4body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, ks_seq)
    return hst2cnt__iter
def feeds__ks_seq(st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, ks_seq, /):
    'len(output) == 1+len(input)'
    hst2cnt__iter = iter_feeds__ks_seq(st_info4body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, ks_seq)
    hst2cnt__seq = [*hst2cnt__iter]
    return hst2cnt__seq
def iter_feeds__ks_seq(st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, ks_seq, /):
    'len(output) == 1+len(input)'
    hst2cnt = feed0(st_info4body, hst2k2hst__as_transition_table, hst2cnt)
    yield hst2cnt
    for ks8step in ks_seq:
        hst2cnt = feed(st_info4body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, hst2cnt, ks8step)
        yield hst2cnt
    return

#basic_setting4multi_cell_token
class BasicSetting4MultiCellToken(_Base4Repr):
    r'''[[[
    eg:
        [byte]
        0b11xx_xxxx 0b0xxx_xxxx* 0b10xx_xxxx
        begin_marker    body     end_marker
    eg:
        [byte]
        0b11xx_xxxx 0b01xx_xxxx* 0b10xx_xxxx
        begin_marker    body     end_marker of fst token kind
        0b00xx_xxxx
        forbidden_substr of fst token kind
        begin_marker&&end_marker of snd token kind
    eg:
        [byte]
        begin_marker: 0b1xxx_xxxx{3}
        end_marker: 0b0xxx_xxxx{3}
    eg:
        [bit]
        11           (01)*  00
        begin_marker        end_marker
    #]]]'''#'''
    def __init__(sf, istr2is_begin_marker, istr2is_end_marker, istr2is_forbidden_substr, /):
        sf.istr2is_begin_marker = istr2is_begin_marker
        sf.istr2is_end_marker = istr2is_end_marker
        sf.istr2is_forbidden_substr = istr2is_forbidden_substr

#setting4multi_cell_token
class Setting4MultiCellToken(BasicSetting4MultiCellToken, _Base4Repr):
    def __init__(sf, strings4begin_marker, strings4end_marker, strings4forbidden_substr, /):
        strings = [*strings4begin_marker]
        L1 = len(strings)
        strings.extend(strings4end_marker)
        L2 = len(strings)
        strings.extend(strings4forbidden_substr)
        num_strs = len(strings)
        istr2is_begin_marker = [istr < L1 for istr in range(num_strs)]
        istr2is_end_marker = [L1 <= istr < L2 for istr in range(num_strs)]
        istr2is_forbidden_substr = [L2 <= istr for istr in range(num_strs)]
        sf.strings = strings
        super().__init__(istr2is_begin_marker, istr2is_end_marker, istr2is_forbidden_substr)

@_injector
def _mk_setting4multi_cell_token(begin_markers, end_markers, substrs4avoid, /) -> 'setting4multi_cell_token':
    strings4begin_marker = begin_markers
    strings4end_marker = end_markers
    strings4forbidden_substr = substrs4avoid
    setting4multi_cell_token = Setting4MultiCellToken(strings4begin_marker, strings4end_marker, strings4forbidden_substr)
    return setting4multi_cell_token
class BasicCounter4AvoidSubstrs__using_dual_end_delimiter(_Base4Repr):
    def __init__(sf, basic_setting4multi_cell_token:BasicSetting4MultiCellToken, st_info4body:StInfo4Body, st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table, /):
        #st_info4begin_marker.check_st0(st0)
        check_sz4alphabet(k2sz4alphabet, sz4alphabet)
        check_type_le(BasicSetting4MultiCellToken, basic_setting4multi_cell_token)
        check_type_le(StInfo4Body, st_info4body)
        ########
        sf.basic_setting4multi_cell_token = basic_setting4multi_cell_token
        sf.st_info4body = st_info4body
        sf.st2is_ge_end_st4begin_marker = st2is_ge_end_st4begin_marker
        sf.sz4alphabet = sz4alphabet
        sf.k2sz4alphabet = k2sz4alphabet
        sf.st0 = st0
        sf.hst2k2hst__as_transition_table = hst2k2hst__as_transition_table
        ########
    def _hst2cnt5may_(sf, may_hst2cnt, /):
        hst2cnt = ifNonef(may_hst2cnt, lambda:mk_hst2cnt4init(sf.st0))
        return hst2cnt
    def feed0(sf, may_hst2cnt, /):
        hst2cnt = sf._hst2cnt5may_(may_hst2cnt)
        hst2cnt = feed0(sf.st_info4body, sf.hst2k2hst__as_transition_table, hst2cnt)
        return hst2cnt
    def iter_feed_full_steps(sf, may_hst2cnt, /):
        hst2cnt = sf._hst2cnt5may_(may_hst2cnt)
        hst2cnt__iter = iter_feed_full_steps(sf.st_info4body, sf.st2is_ge_end_st4begin_marker, sf.sz4alphabet, sf.k2sz4alphabet, sf.st0, sf.hst2k2hst__as_transition_table, hst2cnt)
        return hst2cnt__iter
    def feed_full_steps(sf, may_hst2cnt, num_steps, /):
        hst2cnt = sf._hst2cnt5may_(may_hst2cnt)
        hst2cnt__seq = feed_full_steps(sf.st_info4body, sf.st2is_ge_end_st4begin_marker, sf.sz4alphabet, sf.k2sz4alphabet, sf.st0, sf.hst2k2hst__as_transition_table, hst2cnt, num_steps)
        return hst2cnt__seq
    def feed_full_step(sf, may_hst2cnt, /):
        [_, hst2cnt] = sf.feed_full_steps(may_hst2cnt, 1)
        return hst2cnt
    def feed(sf, may_hst2cnt, ks8step, /):
        hst2cnt = sf._hst2cnt5may_(may_hst2cnt)
        hst2cnt = feed(sf.st_info4body, sf.st2is_ge_end_st4begin_marker, sf.sz4alphabet, sf.k2sz4alphabet, sf.st0, sf.hst2k2hst__as_transition_table, hst2cnt, ks8step)
        return hst2cnt
    def feeds__ks_seq(sf, may_hst2cnt, ks_seq, /):
        hst2cnt = sf._hst2cnt5may_(may_hst2cnt)
        hst2cnt__seq = feeds__ks_seq(sf.st_info4body, sf.st2is_ge_end_st4begin_marker, sf.sz4alphabet, sf.k2sz4alphabet, sf.st0, sf.hst2k2hst__as_transition_table, hst2cnt, ks_seq)
        return hst2cnt__seq
    def feeds__k_seq(sf, may_hst2cnt, k_seq, /):
        hst2cnt = sf._hst2cnt5may_(may_hst2cnt)
        hst2cnt__seq = feeds__k_seq(sf.st_info4body, sf.st2is_ge_end_st4begin_marker, sf.sz4alphabet, sf.k2sz4alphabet, sf.st0, sf.hst2k2hst__as_transition_table, hst2cnt, k_seq)
        return hst2cnt__seq
    def iter_num_strs_ex_(sf, may_hst2cnt=None, may_k_seq=None, /):
        'see:iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_'
        ########
        k_seq = ifNone(may_k_seq, ())
        hst2cnt = sf._hst2cnt5may_(may_hst2cnt)
        ########
        hst2cnt__seq = sf.feeds__k_seq(hst2cnt, k_seq)
        d = hst2cnt__seq[-1].copy()
        yield from hst2cnt__seq
        #bug:modify by user:hst2cnt__iter = sf.iter_feed_full_steps(hst2cnt__seq[-1])
        hst2cnt__iter = sf.iter_feed_full_steps(d)
        for head in hst2cnt__iter:
            #discard head
            #   hst2cnt__iter[0] == hst2cnt__seq[-1]
            if not head == d:
                raise logic-err
            break
        yield from hst2cnt__iter

class Counter4AvoidSubstrs__using_dual_end_delimiter(BasicCounter4AvoidSubstrs__using_dual_end_delimiter, _Base4Repr):
    def __init__(sf, setting4multi_cell_token:Setting4MultiCellToken, sz4alphabet, may_k2sz4alphabet, /):
        #
        ##################
        check_type_le(Setting4MultiCellToken, setting4multi_cell_token)
        ##################
        basic_setting4multi_cell_token = setting4multi_cell_token
        ##################
        _result1 = (ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_OutTree) = strings2prefix_st_tree_ex_(setting4multi_cell_token.strings)
        ##################
        _result2 =  (len2sts, noninit_st2st_k_pair__as_InTree, noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table, st2is_eq_end_st4whole, st2suffix_end_sts, st_info4begin_marker, hst2k2hst__as_transition_table) = mk_hst2k2hst__as_transition_table_ex(st0, end_st2istrs, st2len, st2k2st__as_OutTree, basic_setting4multi_cell_token.istr2is_begin_marker)
        ##################
        check_type_le(StInfo4BeginMarker, st_info4begin_marker)
        st_info4begin_marker.check_st0(st0)
        ##################
        st_info4body = mk_st_info4body(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, basic_setting4multi_cell_token.istr2is_forbidden_substr, basic_setting4multi_cell_token.istr2is_end_marker)
        ##################
        if 1:
            ks, _result1
            k2sz4alphabet = mk_k2sz4alphabet__5may_(ks, sz4alphabet, may_k2sz4alphabet)
                #check_sz4alphabet(k2sz4alphabet, sz4alphabet)
                #   via super().__init__()
        ##################
        _vars = {**locals()}
        ##################
        sf._result1 = _result1
        sf._result2 = _result2
        sf.setting4multi_cell_token = setting4multi_cell_token
        sf.st_info4begin_marker = st_info4begin_marker
        ##################
        super().__init__(basic_setting4multi_cell_token, st_info4body, st_info4begin_marker.st2is_ge_end_st4begin_marker, sz4alphabet, k2sz4alphabet, st0, hst2k2hst__as_transition_table)
        ##################
        del _vars['sf']
        del _vars['_result1']
        del _vars['_result2']
        _vars.pop('__class__', 0)
        [_vars.pop(nm) for nm in [nm for nm in _vars if nm.startswith('_')]]
        [_vars.pop(nm, 0) for nm in [*vars(sf)]]
        #sf._vars__private = _vars
        sf._vars = _vars
        sf._vars__export = filter4dict_key(lambda nm:not nm.startswith('_'), vars(sf))

    def mk_st2is_inside_begin_marker(sf, /):
        istr2is_begin_marker = sf.basic_setting4multi_cell_token.istr2is_begin_marker
        st0 = sf.st0
        st2istrs = sf._vars['st2istrs']
        noninit_st2st_k_pair__as_InTree = sf._vars['noninit_st2st_k_pair__as_InTree']
        st2is_inside_begin_marker = mk_st2is_inside_begin_marker(istr2is_begin_marker, st0, st2istrs, noninit_st2st_k_pair__as_InTree)
        return st2is_inside_begin_marker

    def mk_st2is_inside_end_marker(sf, /):
        istr2is_end_marker = sf.basic_setting4multi_cell_token.istr2is_end_marker
        st0 = sf.st0
        st2istrs = sf._vars['st2istrs']
        noninit_st2st_k_pair__as_InTree = sf._vars['noninit_st2st_k_pair__as_InTree']
        st2is_inside_end_marker = mk_st2is_inside_end_marker(istr2is_end_marker, st0, st2istrs, noninit_st2st_k_pair__as_InTree)
        return st2is_inside_end_marker
@_injector
def _mk_counter4avoid_substrs__using_dual_end_delimiter(setting4multi_cell_token, sz4alphabet, may_k2sz4alphabet, /) -> 'counter4avoid_substrs__using_dual_end_delimiter':
    counter4avoid_substrs__using_dual_end_delimiter = Counter4AvoidSubstrs__using_dual_end_delimiter(setting4multi_cell_token, sz4alphabet, may_k2sz4alphabet)
    return counter4avoid_substrs__using_dual_end_delimiter


@_injector
def mk_st2is_inside_end_marker(istr2is_end_marker, st0, st2istrs, noninit_st2st_k_pair__as_InTree, /) -> 'st2is_inside_end_marker':
    st2is_inside_end_marker = mk_st2is_le_end_st4xxx(istr2is_end_marker, st0, st2istrs, noninit_st2st_k_pair__as_InTree)
    return st2is_inside_end_marker
@_injector
def mk_st2is_inside_begin_marker(istr2is_begin_marker, st0, st2istrs, noninit_st2st_k_pair__as_InTree, /) -> 'st2is_inside_begin_marker':
    st2is_inside_begin_marker = mk_st2is_le_end_st4xxx(istr2is_begin_marker, st0, st2istrs, noninit_st2st_k_pair__as_InTree)
    return st2is_inside_begin_marker
    ########old ver:
    num_sts = len(st2istrs)
    ########
    end_sts4begin_marker = [st for st in range(num_sts) if any(istr2is_begin_marker[istr] for istr in st2istrs[st])]
    st2is_inside_begin_marker = mk_st2is_le_sts4xxx(st0, noninit_st2st_k_pair__as_InTree, end_sts4begin_marker)
    return st2is_inside_begin_marker
def mk_end_sts4xxx(istr2is_xxx, st2istrs, /):
    num_sts = len(st2istrs)
    end_sts4xxx = [st for st in range(num_sts) if any(istr2is_xxx[istr] for istr in st2istrs[st])]
    return end_sts4xxx
        #end_sts4begin_marker
        #end_sts4end_marker
def mk_st2is_le_end_st4xxx(istr2is_xxx, st0, st2istrs, noninit_st2st_k_pair__as_InTree, /):
    end_sts4xxx = mk_end_sts4xxx(istr2is_xxx, st2istrs)
    st2is_le_end_st4xxx = mk_st2is_le_sts4xxx(st0, noninit_st2st_k_pair__as_InTree, end_sts4xxx)
    return st2is_le_end_st4xxx
        #st2is_inside_begin_marker
        #st2is_inside_end_marker

@_injector
def mk_k2sz4alphabet__5may_(ks, sz4alphabet, may_k2sz4alphabet, /) -> 'k2sz4alphabet':
    k2sz4alphabet = ifNonef(may_k2sz4alphabet, lambda:{k:1 for k in ks}) #defaultdict(lambda:1)
    if not ks <= k2sz4alphabet.keys(): raise ValueError
    check_sz4alphabet(k2sz4alphabet, sz4alphabet)
    return k2sz4alphabet
    ##################
def steps5st_(noninit_st2st_k_pair__as_InTree, st0, _st, /):
    steps4prefix = []
    while not _st == st0:
        st_, k = noninit_st2st_k_pair__as_InTree[_st]
        steps4prefix.append((st_, k, _st))
        _st = st_
    steps4prefix.reverse()
    return steps4prefix


def prefix_sts5st_(noninit_st2st_k_pair__as_InTree, st0, _st, /):
    steps4prefix = steps5st_(noninit_st2st_k_pair__as_InTree, st0, _st)
    sts4prefix = [*map(fst, steps4prefix), _st]
    return sts4prefix
#def ks5st_(noninit_st2st_k_pair__as_InTree, st0, _st, /):
def prefix_ks5st_(noninit_st2st_k_pair__as_InTree, st0, _st, /):
    steps4prefix = steps5st_(noninit_st2st_k_pair__as_InTree, st0, _st)
    ks4prefix = [*map(snd, steps4prefix)]
    return ks4prefix
    ########
    ks4prefix = []
    while not _st == st0:
        st_, k = noninit_st2st_k_pair__as_InTree[_st]
        ks4prefix.append(k)
        _st = st_
    ks4prefix.reverse()
    return ks4prefix
def mk_st2is_le_sts4xxx(st0, noninit_st2st_k_pair__as_InTree, sts4xxx, /):
    num_sts = len(noninit_st2st_k_pair__as_InTree)
    st2is_le_sts4xxx = [False]*num_sts
    for _st4xxx in sts4xxx:
        for st in prefix_sts5st_(noninit_st2st_k_pair__as_InTree, st0, _st4xxx):
            st2is_le_sts4xxx[st] = True
    return st2is_le_sts4xxx
@_injector
def mk_st2is_eq_end_st4whole4begin_marker(len_strs, istr2end_st, istr2is_begin_marker, /) -> 'st2is_eq_end_st4whole4begin_marker':
    #num_sts = len(st2is_gt_end_st4begin_marker)
    num_sts = 1+max(istr2end_st, default=-1)
    st2is_eq_end_st4whole4begin_marker = [False]*num_sts
    for istr in range(len_strs):
        if not istr2is_begin_marker[istr]:
            continue
        istr4begin_marker = istr
        end_st4begin_marker = istr2end_st[istr4begin_marker]
        st2is_eq_end_st4whole4begin_marker[end_st4begin_marker] = True
    return st2is_eq_end_st4whole4begin_marker

@_injector
def mk_st2is_eq_end_st4whole4effective_begin_marker(st2is_eq_end_st4whole4begin_marker, st2is_gt_end_st4begin_marker, st_info4body, /) -> 'st2is_eq_end_st4whole4effective_begin_marker':
    num_sts = len(st2is_gt_end_st4begin_marker)
    assert num_sts == len(st2is_eq_end_st4whole4begin_marker)
    st2is_eq_end_st4whole4effective_begin_marker = [False]*num_sts
    #end_sts4begin_marker = set() # :: {end_st4begin_marker}
    for st, is_eq_end_st4whole4begin_marker in enumerate(st2is_eq_end_st4whole4begin_marker):
        if not is_eq_end_st4whole4begin_marker:
            continue
        end_st4begin_marker = st
        #if end_st4begin_marker in end_sts4begin_marker:
        if st2is_gt_end_st4begin_marker[end_st4begin_marker]:
            #filter out
            continue
        if not st_info4body.is_st_good_as_step_dst(end_st4begin_marker):
            #filter out
            continue
        #end_sts4begin_marker.add(end_st4begin_marker)
        end_st4effective_begin_marker = end_st4begin_marker
        st2is_eq_end_st4whole4effective_begin_marker[end_st4effective_begin_marker] = True
    return st2is_eq_end_st4whole4effective_begin_marker


assert collect_src_names(Helper4AutoCalc4AvoidSubstr) == {'istr2is_end_marker', 'st2is_ge_end_st4end_marker', 'st2is_gt_end_st4end_marker', 'end_markers', 'sz4alphabet', 'begin_markers', 'st2is_ge_end_st4forbidden_substr', 'strings', 'may_k2sz4alphabet', 'len_strs', 'istr2is_begin_marker', 'substrs4avoid'}
def __():
    'sz4alphabet'
    'begin_markers'
    'end_markers'
    'substrs4avoid'
    'may_k2sz4alphabet'

    'istr2is_begin_marker'
    'istr2is_end_marker'
    'st2is_ge_end_st4end_marker'
    'st2is_gt_end_st4end_marker'
    'st2is_ge_end_st4forbidden_substr'
    'strings'
    'len_strs'
    @_injector
    def _get_istr2is_begin_marker(basic_setting4multi_cell_token, /) -> 'istr2is_begin_marker':
        return basic_setting4multi_cell_token.istr2is_begin_marker
    @_injector
    def _get_istr2is_end_marker(basic_setting4multi_cell_token, /) -> 'istr2is_end_marker':
        return basic_setting4multi_cell_token.istr2is_end_marker
    @_injector
    def _get_istr2is_forbidden_substr(basic_setting4multi_cell_token, /) -> 'istr2is_forbidden_substr':
        return basic_setting4multi_cell_token.istr2is_forbidden_substr

    @_injector
    def _get_strings(setting4multi_cell_token, /) -> 'strings':
        return setting4multi_cell_token.strings
    @_injector
    def _get_basic_setting4multi_cell_token(setting4multi_cell_token, /) -> 'basic_setting4multi_cell_token':
        basic_setting4multi_cell_token = setting4multi_cell_token
        return basic_setting4multi_cell_token
    @_injector
    def _get_len_strs(strings, /) -> 'len_strs':
        return len(strings)
    if 0:
        #seed.helper.auto_calc.NotDAG_Error: ['st_info4body', 'st2is_ge_end_st4end_marker']
        @_injector
        def _get_st2is_ge_end_st4end_marker(st_info4body, /) -> 'st2is_ge_end_st4end_marker':
            return st_info4body.st2is_ge_end_st4end_marker
        @_injector
        def _get_st2is_gt_end_st4end_marker(st_info4body, /) -> 'st2is_gt_end_st4end_marker':
            return st_info4body.st2is_gt_end_st4end_marker
        @_injector
        def _get_st2is_ge_end_st4forbidden_substr(st_info4body, /) -> 'st2is_ge_end_st4forbidden_substr':
            return st_info4body.st2is_ge_end_st4forbidden_substr
    #see:def mk_st_info4body(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_forbidden_substr, istr2is_end_marker, /):
    @_injector
    def _mk_st_infos4forbidden_substr(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_forbidden_substr, /) -> '(st2is_eq_end_st4forbidden_substr, st2is_ge_end_st4forbidden_substr, st2is_gt_end_st4forbidden_substr, st2prev_substr_end_sts4forbidden_substr)':
        (st2is_eq_end_st4forbidden_substr, st2is_ge_end_st4forbidden_substr, st2is_gt_end_st4forbidden_substr, st2prev_substr_end_sts4forbidden_substr) = mk_st_infos4xxx(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_forbidden_substr)
        return (st2is_eq_end_st4forbidden_substr, st2is_ge_end_st4forbidden_substr, st2is_gt_end_st4forbidden_substr, st2prev_substr_end_sts4forbidden_substr)
    @_injector
    def _mk_st_infos4end_marker(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_end_marker, /) -> '(st2is_eq_end_st4end_marker, st2is_ge_end_st4end_marker, st2is_gt_end_st4end_marker, st2prev_substr_end_sts4end_marker)':
        (st2is_eq_end_st4end_marker, st2is_ge_end_st4end_marker, st2is_gt_end_st4end_marker, st2prev_substr_end_sts4end_marker) = mk_st_infos4xxx(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, istr2is_end_marker)
        return (st2is_eq_end_st4end_marker, st2is_ge_end_st4end_marker, st2is_gt_end_st4end_marker, st2prev_substr_end_sts4end_marker)
__()

if 1:
    del _injector
    ###[End__Helper4AutoCalc4AvoidSubstr]:here
    ###end-Helper4AutoCalc4AvoidSubstr
    #if not is_DAG4dependency_graph_(Helper4AutoCalc4AvoidSubstr): raise logic-err
    check_DAG4dependency_graph_(Helper4AutoCalc4AvoidSubstr)
    assert collect_src_names(Helper4AutoCalc4AvoidSubstr) == {'sz4alphabet', 'may_k2sz4alphabet', 'begin_markers', 'end_markers', 'substrs4avoid'}, collect_src_names(Helper4AutoCalc4AvoidSubstr)
    assert [*iter_topological_ordering4dependency_graph_(Helper4AutoCalc4AvoidSubstr)] == (
    ['begin_markers', 'end_markers', 'substrs4avoid'
    , 'setting4multi_cell_token', 'basic_setting4multi_cell_token'

    , 'may_k2sz4alphabet', 'sz4alphabet'
    , 'counter4avoid_substrs__using_dual_end_delimiter'
    , 'strings', 'end_st2istrs', 'st2len', 'len2sts', 'st0', 'st2k2st__as_OutTree', 'noninit_st2st_k_pair__as_InTree'
    , 'st2k2st__as_transition_table', 'istr2is_begin_marker', 'noninit_st2longest_proper_suffix_st', 'st2is_eq_end_st4whole', 'st2suffix_end_sts', 'st2is_eq_end_st4begin_marker', 'st2prev_substr_end_sts4begin_marker', 'st2is_ge_end_st4begin_marker', 'st2is_gt_end_st4begin_marker', 'st_info4begin_marker'
    , 'hst2k2hst__as_transition_table', 'istr2end_st', 'istr2is_end_marker', 'istr2is_forbidden_substr', 'ks'
    , 'k2sz4alphabet', 'len_strs', 'st2is_eq_end_st4end_marker', 'st2is_eq_end_st4forbidden_substr', 'st2is_eq_end_st4suffix', 'st2is_eq_end_st4whole4begin_marker', 'st2is_ge_end_st4end_marker', 'st2is_ge_end_st4forbidden_substr', 'st2is_gt_end_st4end_marker', 'st_info4body', 'st2is_eq_end_st4whole4effective_begin_marker', 'st2is_gt_end_st4forbidden_substr', 'st2istrs', 'st2is_inside_begin_marker', 'st2is_inside_end_marker', 'st2prev_substr_end_sts', 'st2prev_substr_end_sts4end_marker', 'st2prev_substr_end_sts4forbidden_substr']
    )

    {'sz4alphabet', 'may_k2sz4alphabet', 'begin_markers', 'end_markers', 'substrs4avoid'}


def main4iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_(sz4alphabet, begin_markers, end_markers, substrs4avoid, /, *, _ver_, may_k2sz4alphabet=None, _debug=False, may_args4islice=None, turnon__floor_log2_total_count=False):
    'uint -> [[k]] -> [[k]] -> [[k]] -> (*may_k2sz4alphabet/may {k:uint}) -> (*may_args4islice/may [uint]) -> Iter (len4curr_str, total_count, hst2cnt__END, (hst2cnt__pre, hst2cnt__post))/Iter (uint, uint, hst2cnt, (hst2cnt, hst2cnt)) # hst2cnt/{(bool,uint):pint}'
    it = iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(sz4alphabet, begin_markers, end_markers, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet, _debug=_debug, _ver_=_ver_)
    if _debug:
        return it

    it = apply_may_args4islice_(may_args4islice, it)
    if turnon__floor_log2_total_count:
        def f(it, /):
            #ver1:for (len4curr_str, total_count, hst2cnt__END, (hst2cnt__pre, hst2cnt__post)) in it:
            #ver2:for (len4curr_str, total_count, hst2cnt__END, (hst2cnt,)) in it:
            for (len4curr_str, total_count, hst2cnt__END, inner_state) in it:
                lb = floor_log2(total_count) if total_count else None
                is_eq = 2**lb==total_count if total_count else None
                yield (len4curr_str, lb, is_eq, total_count, hst2cnt__END, inner_state)
        it = f(it)

    return it
def iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver1_(sz4alphabet, begin_markers, end_markers, substrs4avoid, /, *, may_k2sz4alphabet=None, _debug=False):
    'uint -> [[k]] -> [[k]] -> [[k]] -> (*may_k2sz4alphabet/may {k:uint}) -> Iter (len4curr_str, total_count, hst2cnt__END, (hst2cnt__pre, hst2cnt__post))/Iter (uint, uint, hst2cnt, (hst2cnt, hst2cnt)) # hst2cnt/{(bool,uint):pint}'
    setting4multi_cell_token = Setting4MultiCellToken(begin_markers, end_markers, substrs4avoid)
    sf = Counter4AvoidSubstrs__using_dual_end_delimiter(setting4multi_cell_token, sz4alphabet, may_k2sz4alphabet)
    if _debug:
        yield sf
        return

    strings = sf.setting4multi_cell_token.strings
    istr2is_begin_marker = sf.basic_setting4multi_cell_token.istr2is_begin_marker
    istr2end_st = sf._vars['istr2end_st']
    st_info4body = sf.st_info4body
    st2is_gt_end_st4begin_marker = sf.st_info4begin_marker.st2is_gt_end_st4begin_marker
    st0 = sf.st0
#
    st2is_eq_end_st4whole4begin_marker = mk_st2is_eq_end_st4whole4begin_marker(len(strings), istr2end_st, istr2is_begin_marker)
    st2is_eq_end_st4whole4effective_begin_marker = mk_st2is_eq_end_st4whole4effective_begin_marker(st2is_eq_end_st4whole4begin_marker, st2is_gt_end_st4begin_marker, st_info4body)

    if 0:
        seqs = []
        end_st2istrs = sf._vars['end_st2istrs']
        for st, is_eq_end_st4whole4effective_begin_marker in enumerate(st2is_eq_end_st4whole4effective_begin_marker):
            if not is_eq_end_st4whole4effective_begin_marker:
                continue
            end_st4effective_begin_marker = st
            istr4___ = end_st2istrs[end_st4effective_begin_marker][0]
            effective_begin_marker = strings[istr4___]
            #hst2cnt__iter = sf.iter_num_strs_ex_(None, begin_marker)
            hst2cnt = mk_hst2cnt4init(st0)
            hst2cnt__seq = sf.feeds__k_seq(hst2cnt, effective_begin_marker)
            seqs.append(hst2cnt__seq)
        assert all(seqs)
    ########
    if 1:
        st0
        noninit_st2st_k_pair__as_InTree = sf._vars['noninit_st2st_k_pair__as_InTree']
        st2is_eq_end_st4whole4effective_begin_marker
        #end_sts4begin_marker
        end_sts4effective_begin_marker = [st for st, is_eq_end_st4whole4effective_begin_marker in enumerate(st2is_eq_end_st4whole4effective_begin_marker) if is_eq_end_st4whole4effective_begin_marker]
        st2is_inside_effective_begin_marker = mk_st2is_le_sts4xxx(st0, noninit_st2st_k_pair__as_InTree, end_sts4effective_begin_marker)
        #neednot this
        # !! [after filter end_sts4begin_marker by st2is_gt_end_st4begin_marker] -> [st unique for begin_markers] -> [directly merge hst2cnt]
    st2len = sf._vars['st2len']

    #def merge__overwrite__same_value(lhs__hst2cnt, rhs__hst2cnt, /):
    #    dict_add__eq
    #    ...
    def merge__add_value(lhs__hst2cnt, rhs__hst2cnt, /):
        hst2cnt = lhs__hst2cnt.copy()
        imerge__add_value(hst2cnt, rhs__hst2cnt)
        return hst2cnt
    def imerge__add_value(lhs__hst2cnt, rhs__hst2cnt, /):
        for hst, cnt in rhs__hst2cnt.items():
            iadd_(lhs__hst2cnt, hst, cnt)
        return None
    def split_(len4curr_str, hst2cnt__pre, hst2cnt__post, /):
        hst2cnt__pre = keep_inside_effective_begin_marker(len4curr_str, hst2cnt__pre)
        assert hst2cnt__pre.keys().isdisjoint(hst2cnt__post.keys()), (hst2cnt__pre.keys() & hst2cnt__post.keys())
            #AssertionError: {(False, 0)}
            #   ==>> ++ _is_st_ok__pre_()::st2len
            #因为 等长(st折叠则赶不上)+hst2cnt__pre锚定于起始空串+st-inside-effective-begin_marker唯一定位

        g2hst2cnt = group4dict_key(lambda hst,/:st2is_eq_end_st4whole4effective_begin_marker[snd(hst)], hst2cnt__pre)
        _hst2cnt__pre = g2hst2cnt.get(False, {})
        hst2cnt__EQ = g2hst2cnt.get(True, {})
        _hst2cnt__post = merge__add_value(hst2cnt__post, hst2cnt__EQ)
        assert len(_hst2cnt__post) == len(hst2cnt__post) + len(hst2cnt__EQ), 'effective_begin_marker???"effective" bug'
        return (_hst2cnt__pre, _hst2cnt__post)

    def _is_st_ok__pre_(len4curr_str, st, /):
        return st2len[st] == len4curr_str and st2is_inside_effective_begin_marker[st]
    def keep_inside_effective_begin_marker(len4curr_str, hst2cnt__pre, /):
        def _is_hst_ok__pre_(hst, /):
            _, st = hst
            return _is_st_ok__pre_(len4curr_str, st)
        hst2cnt__pre = filter4dict_key(_is_hst_ok__pre_, hst2cnt__pre)
        return hst2cnt__pre
    hst2cnt = sf._hst2cnt5may_(None)
    hst2cnt__pre = hst2cnt
        # apply feed_full_step with keep_inside_effective_begin_marker
    hst2cnt__post = {}
        # apply feed_full_step without keep_inside_effective_begin_marker
    for len4curr_str in itertools.count():
        (hst2cnt__pre, hst2cnt__post) = split_(len4curr_str, hst2cnt__pre, hst2cnt__post)
        if not (hst2cnt__pre or hst2cnt__post):
            break
        hst2cnt__sum = merge__add_value(hst2cnt__post, hst2cnt__pre)
        assert len(hst2cnt__sum) == len(hst2cnt__post) + len(hst2cnt__pre), 'effective_begin_marker???"effective" bug'
        1;      del hst2cnt__sum
        hst2cnt__END = filter4dict_key(lambda hst,/:st_info4body.st2is_ge_end_st4end_marker[snd(hst)], hst2cnt__post)
            # only "post", no "pre"
            # since ["post" ==>> begin_marker occurs]
        total_count = sum(hst2cnt__END.values())
        yield (len4curr_str, total_count, hst2cnt__END, (hst2cnt__pre, hst2cnt__post))

        ########next round:
        hst2cnt__pre = sf.feed_full_step(hst2cnt__pre)
        hst2cnt__post = sf.feed_full_step(hst2cnt__post)
    return
iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver1_

def iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver2_(sz4alphabet, begin_markers, end_markers, substrs4avoid, /, *, may_k2sz4alphabet=None, _debug=False):
    'uint -> [[k]] -> [[k]] -> [[k]] -> (*may_k2sz4alphabet/may {k:uint}) -> Iter (len4curr_str, total_count, hst2cnt__END, (hst2cnt__pre, hst2cnt__post))/Iter (uint, uint, hst2cnt, (hst2cnt, hst2cnt)) # hst2cnt/{(bool,uint):pint}'
    setting4multi_cell_token = Setting4MultiCellToken(begin_markers, end_markers, substrs4avoid)
    sf = Counter4AvoidSubstrs__using_dual_end_delimiter(setting4multi_cell_token, sz4alphabet, may_k2sz4alphabet)
    if _debug:
        yield sf
        return
    st_info4begin_marker = sf.st_info4begin_marker
    st_info4body = sf.st_info4body
    st2len = sf._vars['st2len']
    st2is_inside_begin_marker = sf.mk_st2is_inside_begin_marker()


    def keep_inside_begin_marker_if_pre(len4curr_str, hst2cnt, /):
        # "pre" <==> [not has_meet_begin_marker]
        def _is_hst_ok__pre_(hst, /):
            has_meet_begin_marker, st = hst
            return has_meet_begin_marker or (st2len[st] == len4curr_str and st2is_inside_begin_marker[st])
        hst2cnt = filter4dict_key(_is_hst_ok__pre_, hst2cnt)
        return hst2cnt

    def _is_hst_END(hst, /):
        has_meet_begin_marker, st = hst
        return (not st_info4body.is_st_good_as_step_src(st)
            # and st_info4body.is_st_good_as_step_dst(st)
                # <<== feed0/feed_full_step
            and st_info4begin_marker.mk_has_meet_begin_marker4post_st(hst)
                #<==> and (has_meet_begin_marker or st_info4begin_marker.mk_has_meet_begin_marker4post_st(hst))
            )
    #end-def _is_hst_END(hst, /):
    ########
    hst2cnt = sf._hst2cnt5may_(None)
    hst2cnt = sf.feed0(hst2cnt)

    for len4curr_str in itertools.count():
        hst2cnt = keep_inside_begin_marker_if_pre(len4curr_str, hst2cnt)
        if not hst2cnt: break
        hst2cnt__END = filter4dict_key(_is_hst_END, hst2cnt)
        total_count = sum(hst2cnt__END.values())
        yield (len4curr_str, total_count, hst2cnt__END, (hst2cnt,))

        ########next round:
        hst2cnt = sf.feed_full_step(hst2cnt)

    return
iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver2_
iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_ = iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver2_

def iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(sz4alphabet, begin_markers, end_markers, substrs4avoid, /, *, _ver_, may_k2sz4alphabet=None, _debug=False):
    check_int_ge(1, _ver_)
    nm = f'iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__ver{_ver_}_'
    iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verY_ = globals()[nm]
    it = iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verY_(sz4alphabet, begin_markers, end_markers, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet, _debug=_debug)
    return it

#
r'''[[[
st2end_sts4begin_marker
mk_st2k2st__as_transition_table_ex
feed
_feed__using_hst_
noninit_st2longest_proper_suffix_st
    st2suffix_end_sts
    st2prev_substr_end_sts

istr2is_begin_marker
istr2is_end_marker
istr2is_forbidden_substr
has_meet_begin_marker
st2is_eq_end_st4begin_marker
st2is_eq_end_st4end_marker
st2is_eq_end_st4forbidden_substr
begin_marker
end_marker
forbidden_substr?
forbidden_subgraph?
K5,K3_3,K[5],K[3,3]
grep 'K\[5\]' -r ../lots/NOTE/graph/ -l -a -i
view ../lots/NOTE/graph/planar/nonplanar condition of ugraph.txt
grep 'K\[5\]' -r ../../python3_src/nn_ns/graph/  -l -a -i

#]]]'''#'''



_feed__using_hst_
def _feed__using_only_st_(sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, ks8step, /, *, _full_step_):
    'feed :: sz4alphabet/uint -> k2sz4alphabet/{k:uint} -> st0/uint -> st2k2st__as_transition_table/{st:{k:st}} -> st2cnt/{st:uint} -> ks8step/{k} -> st2cnt/{st:uint} #k2sz4alphabet[#eg.sz4alphabet=2**8,k=0b1xxx_xxx,sz4alphabet4k=2**7#]'
    #check_sz4alphabet(k2sz4alphabet, sz4alphabet)
    if not _full_step_ is (ks8step is True): raise TypeError
    if not _full_step_:
        if not ks8step <= k2sz4alphabet.keys():raise ValueError
        if not len(ks8step) == len(frozenset(ks8step)):raise ValueError
        if not len(ks8step) <= sz4alphabet: raise ValueError


    num_sts = len(st2k2st__as_transition_table)
    if not 0 <= st0 < num_sts: raise ValueError
    #if not len(ks) <= sz4alphabet: raise ValueError
    #if not all(sz >= 0 for sz in k2sz4alphabet.values()): raise ValueError
    #if not sum(k2sz4alphabet.values()) <= sz4alphabet: raise ValueError
    _st2cnt = {}
    for st_, cnt_ in st2cnt.items():
        #if not cnt_ > 0: continue
        if not cnt_ > 0: raise ValueError
        k2_st = st2k2st__as_transition_table[st_]
        sz4alphabet4fallback4full = sz4alphabet
        sz4alphabet4fallback4skips = 0
        if _full_step_:
            ks8step = k2_st.keys()
        for k in ks8step:
            sz4alphabet4k = k2sz4alphabet[k]
            if not sz4alphabet4k >= 0: raise ValueError
            if sz4alphabet4k == 0:
                continue
            if not k in k2_st:
                sz4alphabet4fallback4skips += sz4alphabet4k
                continue
            sz4alphabet4fallback4full -= sz4alphabet4k
            if not sz4alphabet4fallback4full >= 0: raise ValueError
            _st = k2_st[k]
            _cnt = cnt_ * sz4alphabet4k
            iadd_(_st2cnt, _st, _cnt)
        if not sz4alphabet4fallback4full >= 0: raise ValueError
        if not sz4alphabet4fallback4skips >= 0: raise ValueError

        sz4alphabet4fallback = sz4alphabet4fallback4full if _full_step_ else sz4alphabet4fallback4skips

        if sz4alphabet4fallback > 0:
            _st = st0
            _cnt = cnt_ * sz4alphabet4fallback
            iadd_(_st2cnt, _st, _cnt)
    return _st2cnt


feed0
def feed0__using_only_end_delimiter_(st_info4body, st2cnt, /):
    return feed__using_only_end_delimiter_(st_info4body, None, None, None, None, st2cnt, None, _no_step_=True)
feed_full_steps
def feed_full_steps__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, num_steps, /):
    st2cnt__iter = iter_feed_full_steps__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt)
    st2cnt__seq = [*islice(st2cnt__iter, 1+num_steps)]
    return st2cnt__seq
feed_full_step
def feed_full_step__using_only_end_delimiter_(st_info4body:StInfo4Body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, /):
    [_, st2cnt] = feed_full_steps__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, 1)
    return st2cnt
iter_feed_full_steps
def iter_feed_full_steps__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, /):
    st2cnt = feed0__using_only_end_delimiter_(st_info4body, st2cnt)
    while 1:
        yield st2cnt
        st2cnt = feed__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, True, _full_step_=True)
feed
def feed__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, ks8step, /, *, _no_step_=False, _full_step_=False):
    r'''
    use feed__using_only_end_delimiter_ as feed__using_none_end_delimiter_
    #to define???feed__using_none_end_delimiter_???:diff only require [not any(st_info4body.st2is_ge_end_st4end_marker)] [#<==> no end_markers]'
    '''#'''
    if 0:(st_info4body
        .st2is_gt_end_st4end_marker
        .st2is_ge_end_st4end_marker
        .st2is_ge_end_st4forbidden_substr
        .is_st_good_as_step_src
        .is_st_good_as_step_dst
        )

    if 1:
        iter_feed_full_steps
        if not _full_step_ is (ks8step is True): raise TypeError
    if 1:
        feed0
        if not _no_step_ is (ks8step is None): raise TypeError
        if not _no_step_ is (k2sz4alphabet is None): raise TypeError
        if not _no_step_ is (sz4alphabet is None): raise TypeError
        if not _no_step_ is (st0 is None): raise TypeError
        if not _no_step_ is (st2k2st__as_transition_table is None): raise TypeError

    if _no_step_:
        #no step ==>> no step_src
        st2cnt_ = st2cnt
    else:
        st2cnt_ = filter4dict_item(lambda st,cnt,/:cnt>0 and st_info4body.is_st_good_as_step_src(st), st2cnt)

    st2cnt_;        del st2cnt
    if _no_step_:
        assert ks8step is None
        _st2cnt = st2cnt_
    else:
        assert not ks8step is None
        _st2cnt = _feed__using_only_st_(sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt_, ks8step, _full_step_=_full_step_)

    _st2cnt;        del st2cnt_
    _2_st2cnt = filter4dict_key(st_info4body.is_st_good_as_step_dst, _st2cnt)

    _2_st2cnt;      del _st2cnt
    return _2_st2cnt
feed__using_only_end_delimiter_


feeds__k_seq
def feeds__k_seq__using_only_end_delimiter_(st_info4body:StInfo4Body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, k_seq, /):
    'len(output) == 1+len(input)'
    st2cnt__iter = iter_feeds__k_seq__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, k_seq)
    st2cnt__seq = [*st2cnt__iter]
    return st2cnt__seq
iter_feeds__k_seq
def iter_feeds__k_seq__using_only_end_delimiter_(st_info4body:StInfo4Body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, k_seq, /):
    'len(output) == 1+len(input)'
    ks_seq = ({k} for k in k_seq)
    st2cnt__iter = iter_feeds__ks_seq__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, ks_seq)
    return st2cnt__iter
feeds__ks_seq
def feeds__ks_seq__using_only_end_delimiter_(st_info4body:StInfo4Body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, ks_seq, /):
    'len(output) == 1+len(input)'
    st2cnt__iter = iter_feeds__ks_seq__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, ks_seq)
    st2cnt__seq = [*st2cnt__iter]
    return st2cnt__seq
def iter_feeds__ks_seq__using_only_end_delimiter_(st_info4body:StInfo4Body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, ks_seq, /):
    'len(output) == 1+len(input)'
    st2cnt = feed0__using_only_end_delimiter_(st_info4body, st2cnt)
    yield st2cnt

    for ks8step in ks_seq:
        st2cnt = feed__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, ks8step)
        yield st2cnt
    return



iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_
def _prepare4iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(sz4alphabet, end_markers, substrs4avoid, /, *, may_k2sz4alphabet=None, may_prefix=None, with_state_inside_prefix=False):
    [_vars] = iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(sz4alphabet, end_markers, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet, may_prefix=may_prefix, with_state_inside_prefix=with_state_inside_prefix, _prepare=True)
    return _vars
def iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(sz4alphabet, end_markers, substrs4avoid, /, *, may_k2sz4alphabet=None, may_prefix=None, with_state_inside_prefix=False, _debug=False, _prepare=False):
    '-> Iter (len4curr_str, total_count, st2cnt__END, (st2cnt,))'
    ##################
    prefix = ifNone(may_prefix, '')
        # here prefix is not begin_marker
    ##################
    begin_markers = [] # useless # as-if
    setting4multi_cell_token = Setting4MultiCellToken(begin_markers, end_markers, substrs4avoid)
    if 1:
        ##################
        basic_setting4multi_cell_token = setting4multi_cell_token
        ##################
        _result1 = (ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_OutTree) = strings2prefix_st_tree_ex_(setting4multi_cell_token.strings)
        ##################
        (len2sts, noninit_st2st_k_pair__as_InTree, noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table) = mk_st2k2st__as_transition_table_ex2(st0, st2len, st2k2st__as_OutTree)
        ##################
        st2is_eq_end_st4whole = mk_st2is_eq_end_st4whole(end_st2istrs)
        ##################
        st2suffix_end_sts = mk_st2suffix_end_sts(st2is_eq_end_st4whole, noninit_st2longest_proper_suffix_st)
        ##################
        ks
        k2sz4alphabet = mk_k2sz4alphabet__5may_(ks, sz4alphabet, may_k2sz4alphabet)
        ##################
    ##################
    st_info4body = mk_st_info4body(st2k2st__as_OutTree, noninit_st2st_k_pair__as_InTree, st2suffix_end_sts, end_st2istrs, basic_setting4multi_cell_token.istr2is_forbidden_substr, basic_setting4multi_cell_token.istr2is_end_marker)
    ##################
    if _prepare or _debug:
        _vars = {**locals()}
        [_vars.pop(nm) for nm in [nm for nm in _vars if nm.startswith('_')]]
        yield _vars
        return

    ##################
    ##################
    def f(st2cnt__iter, /, *, drop_head):
        nonlocal st2cnt, len4curr_str
        if drop_head:
            len4curr_str += 1
            st2cnt__iter = islice(st2cnt__iter, 1, None) # it[1:]
                # islice(it, 1) ==>> it[:1]
                # islice(it, 1, None) ==>> it[1:]

        for len4curr_str, st2cnt in enumerate(st2cnt__iter, len4curr_str):
                    # update st2cnt via "nonlocal"
            if not st2cnt:break
            st2cnt__END = filter4dict_key(lambda st:not st_info4body.is_st_good_as_step_src(st), st2cnt)
                # <==> [st_info4body.is_st_good_as_step_dst(st)][not st_info4body.is_st_good_as_step_src(st)]
                # omit [.is_st_good_as_step_dst(st)], since feed*() postcondition
            total_count = sum(st2cnt__END.values())
            yield (len4curr_str, total_count, st2cnt__END, (st2cnt,))

        return
    ##################
    ##################
    len4curr_str = 0
    st2cnt = {st0:1}

    ##################
    prefix
    st2cnt__iter = iter_feeds__k_seq__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt, prefix)
    it = f(st2cnt__iter, drop_head=False)
            # update st2cnt in f()
    if with_state_inside_prefix:
        yield from it
    else:
        for _ in it:pass
    ##################
    st2cnt__iter = iter_feed_full_steps__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt)
            # using updated st2cnt
    #yield from f(st2cnt__iter, drop_head=True)
    yield from f(st2cnt__iter, drop_head=with_state_inside_prefix)
    ##################
    return
iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_


def iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(sz4alphabet, substrs4avoid, /, *, may_k2sz4alphabet=None, may_prefix=None, with_state_inside_prefix=False, _debug=False):
    '-> Iter (len4curr_str, total_count, st2cnt__END)'
    end_markers = []
    it = iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(sz4alphabet, end_markers, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet, may_prefix=may_prefix, with_state_inside_prefix=with_state_inside_prefix, _debug=_debug)

    if _debug:
        yield from it
        return

    for (len4curr_str, total_count, st2cnt__END, (st2cnt,)) in it:
        assert not st2cnt__END # !![not end_markers]
        assert not total_count # !![not end_markers]
        st2cnt__END = st2cnt
        total_count = sum(st2cnt__END.values())
        yield (len4curr_str, total_count, st2cnt__END)

    return
    ##################old ver: without may_prefix
    end_markers = []
    _vars = _prepare4iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(sz4alphabet, end_markers, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet)


    ##################
    if _debug:
        yield _vars
        return

    ##################
    ##################
    #st0 = _vars['st0']
    st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table = map(_vars.__getitem__, 'st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table'.split(', '))
    ##################
    ##################
    st2cnt = {st0:1}

    st2cnt__iter = iter_feed_full_steps__using_only_end_delimiter_(st_info4body, sz4alphabet, k2sz4alphabet, st0, st2k2st__as_transition_table, st2cnt)

    for len4curr_str, st2cnt in enumerate(st2cnt__iter):
        if not st2cnt:break
        st2cnt__END = st2cnt
        total_count = sum(st2cnt__END.values())
        yield (len4curr_str, total_count, st2cnt__END)

    return

def main4iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(sz4alphabet, substrs4avoid, /, *, may_k2sz4alphabet=None, may_prefix=None, with_state_inside_prefix=False, _debug=False, may_args4islice=None, turnon__floor_log2_total_count=False):
    it = iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_(sz4alphabet, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet, may_prefix=may_prefix, with_state_inside_prefix=with_state_inside_prefix, _debug=_debug)

    if _debug:
        return it

    it = apply_may_args4islice_(may_args4islice, it)
    if turnon__floor_log2_total_count:
        def f(it, /):
            for (len4curr_str, total_count, st2cnt__END) in it:
                lb = floor_log2(total_count) if total_count else None
                is_eq = 2**lb==total_count if total_count else None
                yield (len4curr_str, lb, is_eq, total_count, st2cnt__END)
        it = f(it)

    return it



def main4iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(sz4alphabet, end_markers, substrs4avoid, /, *, may_k2sz4alphabet=None, may_prefix=None, with_state_inside_prefix=False, _debug=False, may_args4islice=None, turnon__floor_log2_total_count=False):
    it = iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_(sz4alphabet, end_markers, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet, may_prefix=may_prefix, with_state_inside_prefix=with_state_inside_prefix, _debug=_debug)

    if _debug:
        return it

    it = apply_may_args4islice_(may_args4islice, it)
    if turnon__floor_log2_total_count:
        def f(it, /):
            for (len4curr_str, total_count, st2cnt__END, (st2cnt,)) in it:
                lb = floor_log2(total_count) if total_count else None
                is_eq = 2**lb==total_count if total_count else None
                yield (len4curr_str, lb, is_eq, total_count, st2cnt__END, (st2cnt,))
        it = f(it)

    return it


__all__ #mark a

















































def _may_xdivmod_(n, d, /):
    assert 2 <= d
    assert 2 <= n
    q, r = divmod(n, d)
    if r == 1:
        return None
    if r == 0:
        assert q > 0
        q -= 1
        r = d
    assert q >= 0
    assert 2 <= r <= d
    assert n == d*q+r
    return (q, r)

#multi-cell-delimiter token
#多单元前缀联合
if 0:
  def iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_(sz4alphabet, prefix, suffix, substrs4avoid, /, *, may_k2sz4alphabet=None):
    begin_marker = prefix
        # here prefix is begin_marker
    end_marker = suffix
#def iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_(sz4alphabet, prefix, suffix, substrs4avoid, /, *, may_k2sz4alphabet=None):
def iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_(sz4alphabet, begin_marker, end_marker, substrs4avoid, /, *, _ver_, may_k2sz4alphabet=None, may_args4islice=None):
    r'''
-> Iter (len4curr_str, total_count)
-> Iter (len4curr_str, total_count<all_layout>)
    '''#'''
    begin_markers = [begin_marker]
    end_markers = [end_marker]
    it = iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter__verX_(sz4alphabet, begin_markers, end_markers, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet, _ver_=_ver_)
    it = apply_may_args4islice_(may_args4islice, it)
    #ver1 only:for (len4curr_str, total_count, hst2cnt__END, (hst2cnt__pre, hst2cnt__post)) in it:
    #ver2 only:for (len4curr_str, total_count, hst2cnt__END, (hst2cnt,)) in it:
    for (len4curr_str, total_count, hst2cnt__END, _) in it:
        yield (len4curr_str, total_count)
    return


def check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker(begin_markers, end_markers, /):
    (_begin_markers, _end_markers) = (end_markers, begin_markers)
    check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(_begin_markers, _end_markers)

def check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(begin_markers, end_markers, /):
    #_end_markers = end_markers
    #_begin_markers = [[*reversed(begin_marker)] for begin_marker in begin_markers]
    #st2suffix_end_sts
    #xxx____st2suffix_sts
    #st2is_eq_end_st4whole
    #st2is_eq_end_st4whole4begin_marker
    if 0:
        r'''[[[
        vivi:
        st2is_eq_end_st4whole4effective_begin_marker = mk_st2is_eq_end_st4whole4effective_begin_marker(st2is_eq_end_st4whole4begin_marker, st2is_gt_end_st4begin_marker, st_info4body)
        end_sts4effective_begin_marker = [st for st, is_eq_end_st4whole4effective_begin_marker in enumerate(st2is_eq_end_st4whole4effective_begin_marker) if is_eq_end_st4whole4effective_begin_marker]
        st2is_inside_effective_begin_marker = mk_st2is_le_sts4xxx(st0, noninit_st2st_k_pair__as_InTree, end_sts4effective_begin_marker)
        #]]]'''#'''
        #end_sts4end_marker = [st for st, is_eq_end_st4whole4end_marker in enumerate(st2is_eq_end_st4whole4end_marker) if is_eq_end_st4whole4end_marker]
        ########
        #end_sts4end_marker = [st for st in range(num_sts) if any(istr2is_end_marker[istr] for istr in st2istrs[st])]
        #st2is_inside_end_marker = mk_st2is_le_sts4xxx(st0, noninit_st2st_k_pair__as_InTree, end_sts4end_marker)

    substrs4avoid = [] # useless # as-if
    setting4multi_cell_token = Setting4MultiCellToken(begin_markers, end_markers, substrs4avoid)
    if 1:
        ##################
        basic_setting4multi_cell_token = setting4multi_cell_token
        ##################
        _result1 = (ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_OutTree) = strings2prefix_st_tree_ex_(setting4multi_cell_token.strings)
        ##################
        (len2sts, noninit_st2st_k_pair__as_InTree, noninit_st2longest_proper_suffix_st, st2k2st__as_transition_table) = mk_st2k2st__as_transition_table_ex2(st0, st2len, st2k2st__as_OutTree)

    istr2is_begin_marker = basic_setting4multi_cell_token.istr2is_begin_marker
    istr2is_end_marker = basic_setting4multi_cell_token.istr2is_end_marker
    istr2end_st
    st2istrs
    noninit_st2longest_proper_suffix_st
    st0
    len2sts
    _impl4check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(istr2is_begin_marker, istr2is_end_marker, istr2end_st, st2istrs, noninit_st2longest_proper_suffix_st, len2sts)

def _impl4check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(istr2is_begin_marker, istr2is_end_marker, istr2end_st, st2istrs, noninit_st2longest_proper_suffix_st, len2sts, /):
    [st0] = len2sts[0]
    num_sts = len(st2istrs)
    st2is_inside_end_marker = [any(istr2is_end_marker[istr] for istr in st2istrs[st]) for st in range(num_sts)]
    end_sts4begin_marker = [end_st for istr, end_st in enumerate(istr2end_st) if istr2is_begin_marker[istr]]

    st2to_test = [False]*num_sts
    for end_st4begin_marker in end_sts4begin_marker:
        st2to_test[end_st4begin_marker] = True
    st2to_test # not completely initialized yet

    bad_sts4overlap = []
    for len4st in reversed(range(1, len(len2sts))):
        for st in len2sts[len4st]:
            if st2to_test[st]:
                if st2is_inside_end_marker[st]:
                    bad_sts4overlap.append(st)
                else:
                    suffix_st = noninit_st2longest_proper_suffix_st[st]
                    if not suffix_st == st0:
                        st2to_test[suffix_st] = True
    st2to_test # completely initialized
    bad_sts4overlap

    if bad_sts4overlap: raise ValueError(bad_sts4overlap)

def check_dual_end_marker_have_no_nonempty_overlaps(begin_markers, end_markers, /):
    begin_markers = mk_reiterables(begin_markers)
    end_markers = mk_reiterables(end_markers)
    check_no_nonempty_suffix4begin_marker_eq_prefix4end_marker(begin_markers, end_markers)
    check_no_nonempty_prefix4begin_marker_eq_suffix4end_marker(begin_markers, end_markers)
def check_settings4layout_with_std_both_marker(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, /):
    check_int_ge(2, sz4alphabet) #include {'0', '1'}
    check_int_ge(2, len4both_marker) #at least: prefix='11', suffix='00'
    check_int_ge(1, sz4alphabet4k4begin_marker)
    check_int_ge(1, sz4alphabet4k4end_marker)
    check_int_ge(sz4alphabet4k4begin_marker+sz4alphabet4k4end_marker, sz4alphabet) # [alphabet4prefix/-\alphabet4suffix == {}][alphabet4prefix\-/alphabet4suffix |<=| alphabet]

def iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, /, *, with_st2cnt=True, may_args4islice=None):
    '-> Iter (len4curr_str, total_count, st2cnt/[uint])'
    #see:iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_{directly:=True}
    it = _impl4iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, with_st2cnt=with_st2cnt)
    it = apply_may_args4islice_(may_args4islice, it)
    return it

def _impl4iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, /, *, with_st2cnt):
    '-> Iter (len4curr_str, total_count, st2cnt/[uint])'
    ########
    check_settings4layout_with_std_both_marker(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker)
    ########
    num_sts = 1+2*len4both_marker
    #sts = range(num_sts)
    sts = range(-len4both_marker, 1+len4both_marker)
    assert len(sts) == num_sts
    assert [*sts] == [*range(-len4both_marker, -1), -1, 0, *range(+1, +len4both_marker), +len4both_marker]

    sts4mid4begin_marker = range(+1, +len4both_marker)
    sts4mid4end_marker = range(-len4both_marker, -1)
    assert [*sts] == [*sts4mid4end_marker, -1, 0, *sts4mid4begin_marker, +len4both_marker]

    ########
    if with_st2cnt:
        def f(len4curr_str, total_count, st2cnt, /):
            return (len4curr_str, total_count, st2cnt)
    else:
        def f(len4curr_str, total_count, st2cnt, /):
            return (len4curr_str, total_count)
    ########
    assert len4both_marker > 0
    def step_(st2cnt_, /):
        #feed_full_steps
        #step_()<=>matrix.__mul__

        _st2cnt = [0]*num_sts
        for st_ in sts4mid4begin_marker:
            _st = st_ + 1
            _st2cnt[_st] = st2cnt_[st_]
        for st_ in sts4mid4end_marker:
            _st = st_ + 1
            _st2cnt[_st] = st2cnt_[st_]
        if 1:
            #discard st2cnt_[+len4both_marker]
                # end_st<begin_marker>
            #discard st2cnt_[-1]
                # end_st<end_marker>
            pass
        if 1:
            assert st2cnt_[st0] == 0, (len4both_marker > 0, len4both_marker)
            #discard st2cnt_[st0]
                #ignore st2cnt_[st0]


        _st2cnt[+1] = sum(st2cnt_[sts4mid4end_marker.start : sts4mid4end_marker.stop])
                # end_st<begin_marker[:1]>
        _st2cnt[-len4both_marker] = sum(st2cnt_[sts4mid4begin_marker.start : sts4mid4begin_marker.stop])
                # end_st<end_marker[:1]>
        return _st2cnt
    #end-def step_(st2cnt_, /):
    ########


    if 1:
        st0 = 0
        st2cnt = [0]*num_sts
            #here st2cnt is [cnt] not {st:cnt}
        st2cnt[st0] = 1
        len4curr_str = 0

    #as-if feeds__ks_seq: [1{n} 0]
    next_cnt = 1
    for len4curr_str, st in enumerate(range(st0, st0+1+len4both_marker), len4curr_str):
        curr_cnt = next_cnt
        st2cnt = [0]*num_sts
        #st2cnt[st] = sz4alphabet4k4begin_marker**len4curr_str
        st2cnt[st] = curr_cnt
        total_count = st2cnt[-1]
        yield f(len4curr_str, total_count, st2cnt)
        next_cnt = sz4alphabet4k4begin_marker*curr_cnt
        ########
    else:
        curr_cnt
        next_cnt = sz4alphabet4k4end_marker*curr_cnt
        ########
        len4curr_str += 1
        curr_cnt = next_cnt
        st = -len4both_marker
        st2cnt = [0]*num_sts
        st2cnt[st] = curr_cnt
        total_count = st2cnt[-1]
        yield f(len4curr_str, total_count, st2cnt)


    for len4curr_str in itertools.count(1+len4curr_str):
        st2cnt = step_(st2cnt)
        total_count = st2cnt[-1]
        yield f(len4curr_str, total_count, st2cnt)
    return
def iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, /, *, _ver_, may_args4islice=None, directly=False, with_st2cnt_if_directly=False):
    r'''[[[
-> Iter (len4curr_str, total_count<layout_with_std_both_marker>)
-> Iter (len4curr_str, total_count<layout_with_std_both_marker>, st2cnt) if directly and with_st2cnt_if_directly

multi-cell-delimiter token:layout_with_std_both_marker
    (*): 1{n} 0{n}
    #(*): 1{n} [^10] 0{n}
    #(*): 1{n} [^1] [^0] 0{n}
    (*): (1{n} .* 0{n}) exclude (.+ 1{n} .* | .* 0{n} .+)
        #vs:layout_with_std_both_marker-prefix-bit-version: (*): (1{n} [01]* 0{n}) exclude ([01]+ 1{n} [01]* | [01]* 0{n} [01]+)
        ########
        #vs:std_layout-version: (*): 1{n} ([^1] .{n-2} [^0])* ([^1] .{0,n-2} [^0]) 0{n}
            #vs:std_layout-prefix-bit-version: (*): 1{n} (0 [01]{n-2} 1)* (0 [01]{0,n-2} 1) 0{n}
        #len4both_marker===n
    #]]]'''#'''
    if directly:
        it = iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, may_args4islice=may_args4islice, with_st2cnt=with_st2cnt_if_directly)
        return it

    check_settings4layout_with_std_both_marker(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker)

    begin_marker = '1'*len4both_marker
    end_marker = '0'*len4both_marker
    may_k2sz4alphabet = {'1':sz4alphabet4k4begin_marker, '0':sz4alphabet4k4end_marker}
    substrs4avoid = []
    it = iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_(sz4alphabet, begin_marker, end_marker, substrs4avoid, may_k2sz4alphabet=may_k2sz4alphabet, may_args4islice=may_args4islice, _ver_=_ver_)
    return it


def iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(num_bits4word, len4both_marker, /, *, _ver_, may_args4islice=None, directly=False, with_st2cnt_if_directly=False):
    r'''[[[
-> Iter (len4curr_str, total_count<layout_with_std_both_marker>)

multi-word-delimiter token:layout_with_std_both_marker
    (*): 1{n} 0{n}
    (*): (1{n} [01]* 0{n}) exclude ([01]+ 1{n} [01]* | [01]* 0{n} [01]+)
        #vs:std_layout-prefix-bit-version: (*): 1{n} (0 [01]{n-2} 1)* (0 [01]{0,n-2} 1) 0{n}
        #len4both_marker===n
    #]]]'''#'''
    check_int_ge(1, num_bits4word)
    sz4alphabet = 2**num_bits4word
    sz4alphabet4k4begin_marker = sz4alphabet4k4end_marker = sz4alphabet//2
    it = iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, may_args4islice=may_args4islice, directly=directly, with_st2cnt_if_directly=with_st2cnt_if_directly, _ver_=_ver_)
    return it


#def _iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_(sz4alphabet, len4bothfix, sz4alphabet4prefix, sz4alphabet4suffix, /):
def _iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, /):
    r'''[[[
-> Iter (len4curr_str, total_count<std_layout>)
-> Iter (sz, count4std_layout)

multi-cell-delimiter token:std layout:
    (*): 1{n} 0{n}
    (*): 1{n} ([^1] .{n-2} [^0])* ([^1] .{0,n-2} [^0]) 0{n}
        #vs:prefix-bit-version: (*): 1{n} (0 [01]{n-2} 1)* (0 [01]{0,n-2} 1) 0{n}
        #len4both_marker===n
    #]]]'''#'''
    check_settings4layout_with_std_both_marker(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker)

    LL = 2*len4both_marker
    NN = (sz4alphabet4k4begin_marker*sz4alphabet4k4end_marker)**len4both_marker


    if 1:
        mid_sz = 0
        sz = LL+mid_sz
        count4std_layout = NN
        yield sz, count4std_layout

    for mid_sz in itertools.count(2):
        sz = LL+mid_sz
        m = _may_xdivmod_(mid_sz, len4both_marker)
        if m is None:
            continue
        (q, r) = m

        num_partial_frees = q*2 + 2

        num_frees = q*(len4both_marker-2) + (r-2)
        assert num_partial_frees + num_frees == mid_sz
        count4std_layout = NN * sz4alphabet**num_frees * ((sz4alphabet-sz4alphabet4k4begin_marker)*(sz4alphabet-sz4alphabet4k4end_marker))**(num_partial_frees//2)
        yield sz, count4std_layout


#def iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_(sz4alphabet, len4bothfix, sz4alphabet4prefix, sz4alphabet4suffix, /, *, args4islice=None):
def iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, /, *, may_args4islice=None):
    r'''[[[
-> Iter (len4curr_str, total_count<std_layout>)

multi-cell-delimiter token:std layout:
    (*): 1{n} 0{n}
    (*): 1{n} ([^1] .{n-2} [^0])* ([^1] .{0,n-2} [^0]) 0{n}
        #len4both_marker===n
    #]]]'''#'''
    it = _iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker)
    it = apply_may_args4islice_(may_args4islice, it)
    return it

#def iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_(num_bits4word, len4bothfix, /, *, args4islice=None):
def iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_(num_bits4word, len4both_marker, /, *, may_args4islice=None):
    r'''[[[
-> Iter (len4curr_str, total_count<std_layout>)

multi-word-delimiter token:std layout:
    (*): 1{n} 0{n}
    (*): 1{n} (0 [01]{n-2} 1)* (0 [01]{0,n-2} 1) 0{n}
        #len4both_marker===n
    #]]]'''#'''
    check_int_ge(1, num_bits4word)
    sz4alphabet = 2**num_bits4word
    sz4alphabet4k4begin_marker = sz4alphabet4k4end_marker = sz4alphabet//2
    return iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_(sz4alphabet, len4both_marker, sz4alphabet4k4begin_marker, sz4alphabet4k4end_marker, may_args4islice=may_args4islice)






#def _iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(num_bits4word, len4bothfix, /, *, with_num_strs):
def _iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(num_bits4word, len4both_marker, /, *, with_num_strs):
    r'''
-> Iter (len4curr_str, log2_total_count<std_layout>) if not with_num_strs
-> Iter (len4curr_str, log2_total_count<std_layout>, total_count<std_layout>) if with_num_strs
    '''#'''

    check_int_ge(1, num_bits4word)
    check_int_ge(2, len4both_marker) #at least: prefix='11', suffix='00'

    LL = 2*len4both_marker
    log2_NN = (num_bits4word-1)*LL


    if with_num_strs:
        def f(sz, log2_count4std_layout, /):
            num_strs = 2**log2_count4std_layout
            return (sz, log2_count4std_layout, num_strs)
    else:
        def f(sz, log2_count4std_layout, /):
            return (sz, log2_count4std_layout)

    if 1:
        mid_sz = 0
        sz = LL+mid_sz
        log2_count4std_layout = log2_NN
        yield f(sz, log2_count4std_layout)

    for mid_sz in itertools.count(2):
        sz = LL+mid_sz
        m = _may_xdivmod_(mid_sz, len4both_marker)
        if m is None:
            continue
        (q, r) = m

        num_partial_frees = q*2 + 2

        num_frees = q*(len4both_marker-2) + (r-2)
        assert num_partial_frees + num_frees == mid_sz
        log2_count4std_layout = log2_NN + num_bits4word*num_frees + (num_bits4word-1)*num_partial_frees
        yield f(sz, log2_count4std_layout)

#def iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(num_bits4word, len4bothfix, /, *, with_num_strs=False, args4islice=None):
def iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(num_bits4word, len4both_marker, /, *, with_num_strs=False, may_args4islice=None):
    r'''[[[
-> Iter (len4curr_str, log2_total_count<std_layout>) if not with_num_strs
-> Iter (len4curr_str, log2_total_count<std_layout>, total_count<std_layout>) if with_num_strs

multi-word-delimiter token:std layout:
    (*): 1{n} 0{n}
    (*): 1{n} (0 .{n-2} 1)* (0 .{0,n-2} 1) 0{n}
        #len4both_marker===n
    #]]]'''#'''
    it = _iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_(num_bits4word, len4both_marker, with_num_strs=with_num_strs)
    it = apply_may_args4islice_(may_args4islice, it)
    return it











































































__all__


from seed.seq_tools.avoid_substrs import Helper4AutoCalc4AvoidSubstr
from seed.seq_tools.avoid_substrs import check_dual_end_marker_have_no_nonempty_overlaps
from seed.seq_tools.avoid_substrs import strings2prefix_st_tree_ex_
from seed.seq_tools.avoid_substrs import iter_num_strs_ex__avoid_substrs__using_dual_end_delimiter_, iter_num_strs_ex__avoid_substrs__using_only_end_delimiter_, iter_num_strs_ex__avoid_substrs__using_none_end_delimiter_
from seed.seq_tools.avoid_substrs import iter_num_strs_ex__multi_cell_delimiter_token__all_layout__via_avoid_substrs_, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_, iter_num_strs_ex__multi_cell_delimiter_token__layout_with_std_both_marker__via_directly_, iter_num_strs_ex__multi_word_delimiter_token__layout_with_std_both_marker__via_avoid_substrs_, iter_num_strs_ex__multi_cell_delimiter_token__std_layout_only_, iter_num_strs_ex__multi_word_delimiter_token__std_layout_only_, iter_log2_num_strs_ex__multi_word_delimiter_token__std_layout_only_


from seed.seq_tools.avoid_substrs import *
if __name__ == "__main__":
    pass
