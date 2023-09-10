#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/prefixes2tree.py
    view ../../python3_src/seed/seq_tools/avoid_substrs.py


seed.seq_tools.prefixes2tree
py -m nn_ns.app.debug_cmd   seed.seq_tools.prefixes2tree -x
py -m nn_ns.app.doctest_cmd seed.seq_tools.prefixes2tree:__doc__ -ff -v


from seed.seq_tools.prefixes2tree import strings2prefix_st_tree_ex_
#xxx from seed.seq_tools.prefixes2tree import prefixes2tree_ex_


#]]]'''
__all__ = r'''
    strings2prefix_st_tree_ex_
'''.split()#'''
    #prefixes2tree_ex_
__all__

from seed.seq_tools.avoid_substrs import strings2prefix_st_tree_ex_


r'''[[[

from seed.tiny import ifNonef, ifNone, echo
from seed.tiny import fst, snd, mk_tuple
from seed.tiny_.check import check_int_ge

import itertools # islice, count


st2k2st__as_forward_tree
st2k2st__as_transition_table #not auto drop avoid_substrs yet
    st2is_end_st4avoid_anywhere
    st2is_end_st4avoid_except_start
    st2is_end_st4avoid_except_end
noninit_st2longest_suffix_st
    st2suffix_end_sts
    st2prev_end_sts
def strings2prefix_st_tree_ex_(strings, /):
    'strings/[[k]]{num_strings} -> (ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_forward_tree)/(ks/{k}, st0/uint, istr2end_st/[uint]{num_strings}, end_st2istrs/[[uint]]{num_sts}, st2istrs/[[uint]]{num_sts}, st2len/[uint]{num_sts}, forward_tree/st2k2st__as_forward_tree/[{k:st}]{num_sts}) #[st0 == 0] #forward_tree =!= transition_table4avoid_substrs'
    ks = {*[]}
    st0 = 0
    istr2end_st = []
    end_st2istrs = [[]]
    st2istrs = [[]]
    st2len = [0]
    st2k2st__as_forward_tree = [{}]
        #node2edge2child
        #node2children
    next_st = len(st2len)
    for istr, s in enumerate(strings):
        st = st0
        for len4st, k in enumerate(s, 1):
            ks.add(k)
            st2istrs[st].append(istr)
            #st2k2st__as_forward_tree[st][k] = _st
            _st = st2k2st__as_forward_tree[st].setdefault(k, next_st)
            if _st == next_st:
                #new st
                next_st += 1
                st2len.append(len4st)
                st2istrs.append([])
                end_st2istrs.append([])
                st2k2st__as_forward_tree.append({})
                assert next_st == len(st2len)
            assert st2len[_st] == len4st
            st = _st
        else:
            st2istrs[st].append(istr)
            end_st = st
            end_st2istrs[end_st].append(istr)
            istr2end_st.append(end_st)
    assert len(end_st2istrs) == len(st2istrs) == len(st2len) == len(st2k2st__as_forward_tree) == next_st #num_sts

    num_sts = len(st2len)
    num_strings = len(istr2end_st)

    ######################
    assert num_strings == sum(map(len, end_st2istrs))
    assert num_strings == (1 + max(itertools.chain.from_iterable(end_st2istrs), default=-1))

    return (ks, st0, istr2end_st, end_st2istrs, st2istrs, st2len, st2k2st__as_forward_tree)
#end-def strings2prefix_st_tree_ex_(strings, /):
#]]]'''#'''

r'''[[[
def prefixes2tree_ex_(prefixes, /, *, may_element2hashable=None):
    '[[x]] -> (*may_element2hashable/may (x->k)) -> (k2xs/{k:[x]}, st2len/[uint], st2idc4prefixes/[[uint]], end_st2idc4prefixes/[[uint]], idx4prefix2end_st/[uint], forward_tree/st2k2st__as_forward_tree/[{k:st}]) #[st0 == 0] #forward_tree =!= transition_table4avoid_substrs'
    element2hashable = ifNone(may_element2hashable, echo)

    k2xs = {}
    st2len = [0]
    st2idc4prefixes = [[]]
    end_st2idc4prefixes = [[]]
    st2k2st__as_forward_tree = [{}]
        #node2edge2child
        #node2children
    next_st = len(st2len)
    st0 = 0
    for i, prefix in enumerate(prefixes):
        st = st0
        for sz, x in enumerate(prefix, 1):
            st2idc4prefixes[st].append(i)
            k = element2hashable(x)
            k2xs.setdefault(k, []).append(x)
            #st2k2st__as_forward_tree[st][k] = _st
            _st = st2k2st__as_forward_tree[st].setdefault(k, next_st)
            if _st == next_st:
                next_st += 1
                st2len.append(sz)
                st2idc4prefixes.append([])
                end_st2idc4prefixes.append([])
                st2k2st__as_forward_tree.append({})
            assert st2len[_st] == sz
            st = _st
        else:
            st2idc4prefixes[st].append(i)
            end_st2idc4prefixes[st].append(i)
    assert len(st2len) == len(st2idc4prefixes) == len(end_st2idc4prefixes) == len(st2k2st__as_forward_tree) == next_st

    #bad_st = -1
    #for end_st, idc4prefixes in enumerate(end_st2idc4prefixes):
    #    if idc4prefixes:

    ######################
    num_prefixes = sum(map(len, end_st2idc4prefixes))
    assert num_prefixes == (1 + max(itertools.chain.from_iterable(end_st2idc4prefixes), default=-1))

    idx4prefix2end_st = [None]*num_prefixes
    for end_st, idc4prefixes in enumerate(end_st2idc4prefixes):
        for idx4prefix in idc4prefixes:
            idx4prefix2end_st[idx4prefix] = end_st
    idx4prefix2end_st

    assert all(end_st is not None for end_st in idx4prefix2end_st)

    return (k2xs, st2len, st2idc4prefixes, end_st2idc4prefixes, idx4prefix2end_st, st2k2st__as_forward_tree)
#end-def prefixes2tree_ex_(prefixes, /, *, may_element2hashable=None):
#]]]'''#'''




























__all__


from seed.seq_tools.prefixes2tree import prefixes2tree_ex_
from seed.seq_tools.prefixes2tree import *
if __name__ == "__main__":
    pass


