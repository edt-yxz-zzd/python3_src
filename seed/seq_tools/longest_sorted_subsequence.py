#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/longest_sorted_subsequence.py
view ../../python3_src/nn_ns/LCS/longest_common_subsequence_problem.py
view ../../python3_src/seed/seq_tools/bisearch.py

seed.seq_tools.longest_sorted_subsequence
py -m nn_ns.app.debug_cmd   seed.seq_tools.longest_sorted_subsequence -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.seq_tools.longest_sorted_subsequence:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.seq_tools.longest_sorted_subsequence:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
源起:
view script/最长同序字符串牜一龥区.py
]]



'#'; __doc__ = r'#'

######################
>>> xs = [9, 8, 7, 8, 9, 0, 1, 0, 3, 2]
>>> longest_sorted_subsequence_of_ex_(xs)
[[(0, 9), (1, 8), (2, 7), (5, 0)], [(3, 8), (6, 1), (7, 0)], [(4, 9), (8, 3), (9, 2)]]
>>> common_of_all_longest_sorted_subsequences_of_(xs)
()
>>> min_longest_sorted_subsequence_of_(xs)
(0, 0, 2)
>>> [*iter_all_longest_sorted_subsequences_of_(xs)] #unsorted
[(0, 0, 2), (0, 1, 2), (0, 0, 3), (0, 1, 3), (7, 8, 9), (8, 8, 9)]
>>> [*sorted_iter_all_longest_sorted_subsequences_of_(xs)] #sorted
[(0, 0, 2), (0, 0, 3), (0, 1, 2), (0, 1, 3), (7, 8, 9), (8, 8, 9)]
>>> len(_) #total
6



>>> common_of_all_longest_sorted_subsequences_of_(xs, with_idx=True)
()
>>> min_longest_sorted_subsequence_of_(xs, with_idx=True)
((5, 0), (7, 0), (9, 2))
>>> [*iter_all_longest_sorted_subsequences_of_(xs, with_idx=True)] #unsorted
[((5, 0), (7, 0), (9, 2)), ((5, 0), (6, 1), (9, 2)), ((5, 0), (7, 0), (8, 3)), ((5, 0), (6, 1), (8, 3)), ((2, 7), (3, 8), (4, 9)), ((1, 8), (3, 8), (4, 9))]
>>> [*sorted_iter_all_longest_sorted_subsequences_of_(xs, with_idx=True)] #sorted
[((5, 0), (7, 0), (9, 2)), ((5, 0), (7, 0), (8, 3)), ((5, 0), (6, 1), (9, 2)), ((5, 0), (6, 1), (8, 3)), ((2, 7), (3, 8), (4, 9)), ((1, 8), (3, 8), (4, 9))]


>>> tmay_total = []; it = sorted_iter_all_longest_sorted_subsequences_of_(xs, may_output_total_=tmay_total.append, leading_None=True)
>>> tmay_total
[]
>>> next(it) is None
True
>>> tmay_total
[6]



######################
>>> xs = [9, 0, 1, 0, 3, 2, 1]
>>> longest_sorted_subsequence_of_ex_(xs) # -> szmm2jxs{unrefined/extendable}
[[(0, 9), (1, 0)], [(2, 1), (3, 0)], [(4, 3), (5, 2), (6, 1)]]
>>> longest_sorted_subsequence_of_ex_(xs, to_refine=True) # -> szmm2jxs{refined/unextendable}
(((1, 0),), ((2, 1), (3, 0)), ((4, 3), (5, 2), (6, 1)))
>>> common_of_all_longest_sorted_subsequences_of_(xs)
(0,)
>>> min_longest_sorted_subsequence_of_(xs)
(0, 0, 1)
>>> [*iter_all_longest_sorted_subsequences_of_(xs)] #unsorted
[(0, 0, 1), (0, 1, 1), (0, 0, 2), (0, 1, 2), (0, 0, 3), (0, 1, 3)]
>>> [*sorted_iter_all_longest_sorted_subsequences_of_(xs)] #sorted
[(0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 1), (0, 1, 2), (0, 1, 3)]
>>> [*iter_all_longest_sorted_subsequences_of_(xs, to_refine=True)] #unsorted # 'to_refine' donot affect main output
[(0, 0, 1), (0, 1, 1), (0, 0, 2), (0, 1, 2), (0, 0, 3), (0, 1, 3)]
>>> [*sorted_iter_all_longest_sorted_subsequences_of_(xs, to_refine=True)] #sorted # 'to_refine' donot affect main output
[(0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 1), (0, 1, 2), (0, 1, 3)]
>>> common_of_all_longest_sorted_subsequences_of_(xs, with_idx=True)
((1, 0),)
>>> min_longest_sorted_subsequence_of_(xs, with_idx=True)
((1, 0), (3, 0), (6, 1))
>>> [*iter_all_longest_sorted_subsequences_of_(xs, with_idx=True)] #unsorted
[((1, 0), (3, 0), (6, 1)), ((1, 0), (2, 1), (6, 1)), ((1, 0), (3, 0), (5, 2)), ((1, 0), (2, 1), (5, 2)), ((1, 0), (3, 0), (4, 3)), ((1, 0), (2, 1), (4, 3))]
>>> [*sorted_iter_all_longest_sorted_subsequences_of_(xs, with_idx=True)] #sorted
[((1, 0), (3, 0), (6, 1)), ((1, 0), (3, 0), (5, 2)), ((1, 0), (3, 0), (4, 3)), ((1, 0), (2, 1), (6, 1)), ((1, 0), (2, 1), (5, 2)), ((1, 0), (2, 1), (4, 3))]
>>> [*iter_all_longest_sorted_subsequences_of_(xs, with_idx=True, to_refine=True)] #unsorted # 'to_refine' donot affect main output
[((1, 0), (3, 0), (6, 1)), ((1, 0), (2, 1), (6, 1)), ((1, 0), (3, 0), (5, 2)), ((1, 0), (2, 1), (5, 2)), ((1, 0), (3, 0), (4, 3)), ((1, 0), (2, 1), (4, 3))]
>>> [*sorted_iter_all_longest_sorted_subsequences_of_(xs, with_idx=True, to_refine=True)] #sorted # 'to_refine' donot affect main output
[((1, 0), (3, 0), (6, 1)), ((1, 0), (3, 0), (5, 2)), ((1, 0), (3, 0), (4, 3)), ((1, 0), (2, 1), (6, 1)), ((1, 0), (2, 1), (5, 2)), ((1, 0), (2, 1), (4, 3))]





######################
def iter_all_longest_sorted_subsequences_of_(xs, /, *, key=None, __lt__=None, with_idx=False, may_output_=None, to_output_total=False, leading_None=False, to_refine=False, _flip=False):

>>> xs = [-1, 9, 0, 1, 0, 3, 2, 1]

#########
, to_refine=False
>>> tmay_output = []; it = iter_all_longest_sorted_subsequences_of_(xs, may_output_=tmay_output.append, leading_None=True)
>>> tmay_output
[]
>>> next(it) is None
True
>>> tmay_output # tmay (szmm2jxs, szmmmm2szmm_rngs)
[([[(0, -1)], [(1, 9), (2, 0)], [(3, 1), (4, 0)], [(5, 3), (6, 2), (7, 1)]], [[(0, 1), (0, 1)], [(1, 2), (1, 2)], [(0, 2), (0, 2), (0, 2)]])]
>>> [*it]
[(-1, 0, 0, 1), (-1, 0, 1, 1), (-1, 0, 0, 2), (-1, 0, 1, 2), (-1, 0, 0, 3), (-1, 0, 1, 3)]


>>> tmay_output = []; it = iter_all_longest_sorted_subsequences_of_(xs, may_output_=tmay_output.append, to_output_total=True, leading_None=True)
>>> tmay_output
[]
>>> next(it) is None
True
>>> tmay_output # tmay (szmm2jxs, szmmmm2szmm_rngs, szmm2totals, total)
[([[(0, -1)], [(1, 9), (2, 0)], [(3, 1), (4, 0)], [(5, 3), (6, 2), (7, 1)]], [[(0, 1), (0, 1)], [(1, 2), (1, 2)], [(0, 2), (0, 2), (0, 2)]], [(1,), (1, 1), (1, 1), (2, 2, 2)], 6)]
>>> [*it]
[(-1, 0, 0, 1), (-1, 0, 1, 1), (-1, 0, 0, 2), (-1, 0, 1, 2), (-1, 0, 0, 3), (-1, 0, 1, 3)]



>>> tmay_total = []; it = sorted_iter_all_longest_sorted_subsequences_of_(xs, may_output_total_=tmay_total.append, leading_None=True)
>>> tmay_total
[]
>>> next(it) is None
True
>>> tmay_total
[6]
>>> [*it]
[(-1, 0, 0, 1), (-1, 0, 0, 2), (-1, 0, 0, 3), (-1, 0, 1, 1), (-1, 0, 1, 2), (-1, 0, 1, 3)]


#########
, to_refine=True
>>> tmay_output = []; tmay_common = []; it = iter_all_longest_sorted_subsequences_of_(xs, may_output_=tmay_output.append, may_output_common_part_=tmay_common.append, leading_None=True, to_refine=True)
>>> tmay_output
[]
>>> tmay_common
[]
>>> next(it) is None
True
>>> tmay_output # tmay (szmm2jxs, szmmmm2szmm_rngs)
[((((0, -1),), ((2, 0),), ((3, 1), (4, 0)), ((5, 3), (6, 2), (7, 1))), [[(0, 1)], [(0, 1), (0, 1)], [(0, 2), (0, 2), (0, 2)]])]
>>> tmay_common
[((0, -1), (2, 0))]
>>> [*it]
[(-1, 0, 0, 1), (-1, 0, 1, 1), (-1, 0, 0, 2), (-1, 0, 1, 2), (-1, 0, 0, 3), (-1, 0, 1, 3)]


>>> tmay_output = []; tmay_common = []; it = iter_all_longest_sorted_subsequences_of_(xs, may_output_=tmay_output.append, may_output_common_part_=tmay_common.append, to_output_total=True, leading_None=True, to_refine=True)
>>> tmay_output
[]
>>> tmay_common
[]
>>> next(it) is None
True
>>> tmay_output # tmay (szmm2jxs, szmmmm2szmm_rngs, szmm2totals, total)
[((((0, -1),), ((2, 0),), ((3, 1), (4, 0)), ((5, 3), (6, 2), (7, 1))), [[(0, 1)], [(0, 1), (0, 1)], [(0, 2), (0, 2), (0, 2)]], [(1,), (1,), (1, 1), (2, 2, 2)], 6)]
>>> tmay_common
[((0, -1), (2, 0))]
>>> [*it]
[(-1, 0, 0, 1), (-1, 0, 1, 1), (-1, 0, 0, 2), (-1, 0, 1, 2), (-1, 0, 0, 3), (-1, 0, 1, 3)]



>>> tmay_total = []; tmay_common = []; it = sorted_iter_all_longest_sorted_subsequences_of_(xs, may_output_total_=tmay_total.append, may_output_common_part_=tmay_common.append, leading_None=True, to_refine=True)
>>> tmay_total
[]
>>> tmay_common
[]
>>> next(it) is None
True
>>> tmay_total
[6]
>>> tmay_common
[((0, -1), (2, 0))]
>>> [*it]
[(-1, 0, 0, 1), (-1, 0, 0, 2), (-1, 0, 0, 3), (-1, 0, 1, 1), (-1, 0, 1, 2), (-1, 0, 1, 3)]











###############################

py_adhoc_call   seed.seq_tools.longest_sorted_subsequence   @f
]]]'''#'''
__all__ = r'''
common_of_all_longest_sorted_subsequences_of_
min_longest_sorted_subsequence_of_
    longest_sorted_subsequence_of_ex_
    iter_all_longest_sorted_subsequences_of_
    sorted_iter_all_longest_sorted_subsequences_of_

_min_lsseq5szmm2jxs_
_common_lsseq5szmm2jxs_
_refine_szmm2jxs_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import operator
from itertools import pairwise, accumulate, compress
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
lazy_import4funcs_('seed.tiny', 'mk_tuple,print_err,ifNone,echo,fst,snd', __name__)
if 0:from seed.tiny import mk_tuple,print_err,ifNone,echo,fst,snd #xxx:null_tuple #xxx:,fst

lazy_import4funcs_('seed.seq_tools.bisearch', 'bisearch', __name__)
if 0:from seed.seq_tools.bisearch import bisearch
#def bisearch(x, array, /, begin=None, end=None, *, key=None, __lt__=None, result_case=2):
#       0 - lower_end == middle_begin
#       1 - middle_end == upper_begin
#       2 - (middle_begin, middle_end)

#.merge_two_sorted_iterables = lazy_import4func_('seed.iters.merge_two_sorted_iterables', 'merge_two_sorted_iterables', __name__)
#.if 0:from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
#.#def merge_two_sorted_iterables(lefts, rights, /, *, left_key=None, right_key=None, before=None, Left=None, Right=None):
#.#    ':: (a->b->Bool) -> [a] -> [b] -> [Either a b] # before :: KeyA -> KeyB -> Bool'

lazy_import4funcs_('seed.iters.batch_find_insert_indices4two_sorted_iterables', 'batch_find_insert_indices4two_sorted_iterables', __name__)
if 0:from seed.iters.batch_find_insert_indices4two_sorted_iterables import batch_find_insert_indices4two_sorted_iterables

___end_mark_of_excluded_global_names__0___ = ...


__all__
def _prepare__key__lt(key, __lt__, /):
    echo(0)#lazy_import__func
    key = ifNone(key, echo)
    __lt__ = ifNone(__lt__, operator.__lt__)
    return (key, __lt__)
    (key, __lt__) = _prepare__key__lt(key, __lt__)

def sorted_iter_all_longest_sorted_subsequences_of_(xs, /, *, key=None, __lt__=None, with_idx=False, may_output_total_=None, may_output_common_part_=None, leading_None=False, to_refine=False):
    r'''[[[
    :: Ord k => Iter x -> (Iter longest_sorted_subsequence/[x]){sorted}
    [sorted_iter_all_longest_sorted_subsequences_of_(xs) =[def]= let [ls:=list(xs)] in iter(sorted(iter_all_longest_common_subsequences_of_(ls, sorted(ls))))]

    [key :: x -> k]
    [__lt__ :: k -> k -> bool]
    [may_output_total_ :: may (total/uint -> None)]
    [may_output_common_part_ :: may (common_longest_sorted_subsequence{with_idx} -> None)]
        see:_common_lsseq5szmm2jxs_()
    #]]]'''#'''
    (key, __lt__) = _prepare__key__lt(key, __lt__)
    #######
    xs = mk_tuple(xs)
    L = len(xs)
    rev_ks = tuple(map(key, reversed(xs)))
    777;key = None
    #######
    def gt_(k0, k1, /):
        # [k0 > k1]
        # [k1 < k0]
        return __lt__(k1, k0)
    #######
    to_output_total = not may_output_total_ is None
    if to_output_total:
        tmay_result = []
        may_output_ = tmay_result.append
    else:
        may_output_ = None
    may_output_
    #######
    if not None is may_output_common_part_:
        #def _output_common_part_(common_longest_sorted_subsequence__with_idx, /):
        tmay_common = []
        _output_common_part_ = tmay_common.append
        _may_output_common_part_ = _output_common_part_
    else:
        _may_output_common_part_ = None
    _may_output_common_part_
    #######
    jkss = iter_all_longest_sorted_subsequences_of_(rev_ks, key=None, __lt__=gt_, with_idx=True, _flip=True, may_output_=may_output_, to_output_total=to_output_total, may_output_common_part_=_may_output_common_part_, leading_None=True, to_refine=to_refine)
    777;next(jkss) # to force output_()
    ######################
    if to_output_total:
        [result] = tmay_result
        (_szmm2jxs, _szmmmm2szmm_rngs, _szmm2total, total) = result
        #only total meaningful
        #   others ~ rev_ks
        output_total_ = may_output_total_
        output_total_(total)
    ######################
    if not None is may_output_common_part_:
        output_common_part_ = may_output_common_part_
        [rev_common_longest_sorted_sub_key_seq__with_rev_idx] = tmay_common
            # :: reversed[(rev_idx,key)]
        Lmm = L-1
        def rev_jk2jx_(rev_jk, /):
            (rev_j,key4x) = rev_jk
            j = Lmm-rev_j
            x = xs[j]
            jx = (j,x)
            return jx
        common_longest_sorted_subsequence__with_idx = tuple(map(rev_jk2jx_, reversed(rev_common_longest_sorted_sub_key_seq__with_rev_idx)))
        output_common_part_(common_longest_sorted_subsequence__with_idx)
    ######################




    ######################
    if leading_None:
        yield None#to force output_total_()
    ######################
    Lmm = L-1
    if with_idx:
        def j2r_(j, /):
            i = Lmm-j
            y = xs[i]
            iy = (i,y)
            return iy
    else:
        def j2r_(j, /):
            i = Lmm-j
            y = xs[i]
            return y
    for jks in jkss:
        rs = tuple(j2r_(j) for j,k in reversed(jks))
        yield rs
    ######################
    return


def iter_all_longest_sorted_subsequences_of_(xs, /, *, key=None, __lt__=None, with_idx=False, may_output_=None, to_output_total=False, leading_None=False, to_refine=False, may_output_common_part_=None, _flip=False):
    r'''[[[
    :: Ord k => Iter x -> (Iter longest_sorted_subsequence/[(x if not with_idx else (uint, x))]){unsorted}
    [iter_all_longest_sorted_subsequences_of_(xs) =[def]= let [ls:=list(xs)] in iter_all_longest_common_subsequences_of_(ls, sorted(ls))]

    [key :: x -> k]
    [__lt__ :: k -> k -> bool]
    [may_output_ :: may (((szmm2jxs, szmmmm2szmm_rngs) if to_output_total (szmm2jxs, szmmmm2szmm_rngs, szmm2totals, total)) -> None)]
    [may_output_common_part_ :: may (common_longest_sorted_subsequence{with_idx} -> None)]
        see:_common_lsseq5szmm2jxs_()
    #]]]'''#'''
    (key, __lt__) = _prepare__key__lt(key, __lt__)

    ######################
    szmm2jxs = longest_sorted_subsequence_of_ex_(xs, key=key, __lt__=__lt__, to_refine=to_refine)
    if not szmm2jxs:
    ######################
        if leading_None:
            yield None#to force output_()
        return

    szmm2jks = [[(j, key(x)) for j,x in jxs] for jxs in szmm2jxs]
    ######################



    ######################
    #szmmmm2szmm_rngs
    #.jx@(szmm+1) --> iw@szmm: s.t:
    #.    w <= x  => begin # w dec
    #.    i < j   => end   # i inc
    szmmmm2szmm_rngs = []
    for iks, jks in pairwise(szmm2jks):
        L = len(iks)
        begins = []
        idx = 0
        for j, kx in jks:
            for idx in range(idx, L):
                kw = iks[idx][1]
                if not __lt__(kx, kw):
                    # [not (kx < kw)]
                    # [(kx >= kw)]
                    # ~= [w <= x]
                    break
            else:
                raise 000
            begin = idx
            begins.append(begin)
        begins
        ends = []
        idx = L -1
        for j, kx in reversed(jks):
            for idx in range(idx, -1, -1):
                i = iks[idx][0]
                if i < j:
                    break
            else:
                raise 000
            end = 1+idx
            ends.append(end)
        #bug:ends #without 『.reverse()』
        ends.reverse()
        assert all(begin < end for (begin, end) in zip(begins, ends))
        rngs = [*zip(begins, ends)]
        szmmmm2szmm_rngs.append(rngs)
    szmmmm2szmm_rngs
    assert len(szmm2jxs) == 1+len(szmmmm2szmm_rngs)
    if 0b0000:
        print_err(szmm2jxs)
        [[(0, 9), (1, 8), (2, 7), (5, 0)], [(3, 8), (6, 1), (7, 0)], [(4, 9), (8, 3), (9, 2)]]
        print_err(szmmmm2szmm_rngs)
        #bug:before『.reverse()』:[[(1, 4), (3, 4), (3, 3)], [(0, 3), (1, 3), (1, 1)]]
        [[(1, 3), (3, 4), (3, 4)], [(0, 1), (1, 3), (1, 3)]]
    ######################






    ######################
    #(szmm2totals, total)
    if to_output_total:
        szmm2totals = [(1,)*len(szmm2jks[0])]
        prev_totals = szmm2totals[0]
        for szmm, rngs, in enumerate(szmmmm2szmm_rngs, 1):
            accs = (0, *accumulate(prev_totals))
            curr_totals = tuple(accs[end] -accs[begin] for begin, end in rngs)
            szmm2totals.append(curr_totals)
            prev_totals = curr_totals
        szmm2totals
        total = sum(szmm2totals[-1])
    ######################







    ######################
    result = (szmm2jxs, szmmmm2szmm_rngs)
    if to_output_total:
        (szmm2totals, total)
        result = (*result, szmm2totals, total)
    if not may_output_ is None:
        output_ = may_output_
        output_(result)
    ######################
    if not may_output_common_part_ is None:
        output_common_part_ = may_output_common_part_
        common_longest_sorted_subsequence__with_idx = _common_lsseq5szmm2jxs_(_with_idx:=True, szmm2jxs, refined:=to_refine, key, __lt__)
        output_common_part_(common_longest_sorted_subsequence__with_idx)
    ######################







    ######################
    if leading_None:
        yield None#to force output_()
    ######################
    L = len(szmm2jxs)
    Lmm = L -1
    ys = []
    #bug:stk = [('call', (szmm:=Lmm, rng:=(0,L)))]
    stk = [('call', (szmm:=Lmm, rng:=(0,len(szmm2jxs[Lmm]))))]
    while stk:
        match stk[-1]:
            case ('call', (szmm, rng)):
                jxs = szmm2jxs[szmm]
                (begin, end) = rng
                idc = range(begin, end)
                if not _flip:
                    idc = idc[::-1]
                it = zip(idc, map(jxs.__getitem__, idc))
                jxs
                    # Iter (idx, jx)
                stk[-1] = ('loop', (szmm, it))
                continue
            case ('loop', (szmm, it)):
                for idx, jx in it:
                    break
                else:
                    stk.pop()
                    if ys:
                        ys.pop()#x@parent
                    else:
                        assert szmm == Lmm
                    continue
                (j, x) = jx
                ys.append(x if not with_idx else jx)
                if szmm == 0:
                    assert len(ys) == L
                    yield tuple(reversed(ys))
                    ys.pop()
                else:
                    szmmmm = szmm-1
                    rng = szmmmm2szmm_rngs[szmmmm][idx]
                    stk.append(('call', (szmm:=szmmmm, rng)))
                continue
            case _:
                raise 000
        raise 000
    assert not stk
    assert not ys
    ######################
    return



#critical essential necessary
def common_of_all_longest_sorted_subsequences_of_(xs, /, *, key=None, __lt__=None, with_idx=False):
    r'''[[[
    :: Ord k => Iter x -> (common_longest_sorted_subsequence/[x] if not with_idx else [(uint, x)])
    [common_of_all_longest_sorted_subsequences_of_(xs) =[def]= sorted(intersection(map(set, iter_all_longest_sorted_subsequences_of_(xs))))]

    [key :: x -> k]
    [__lt__ :: k -> k -> bool]
    #]]]'''#'''
    (key, __lt__) = _prepare__key__lt(key, __lt__)
    szmm2jxs = longest_sorted_subsequence_of_ex_(xs, key=key, __lt__=__lt__, to_refine=True)
    # [szmm2jxs refined]
    return _common_lsseq5szmm2jxs_(with_idx, szmm2jxs, refined:=True, key, __lt__)
#def _common_lsseq5szmm2jxs_(with_idx, szmm2jxs, /):
def _common_lsseq5szmm2jxs_(with_idx, szmm2jxs, refined:bool, key, __lt__, /):
    '-> common_longest_sorted_subsequence{?with_idx?}'
    # MAYBE:[szmm2jxs not refined]
    if 0:
        # MAYBE:[szmm2jxs not refined]
        pass
        ####bug####
        raise 000
    else:
        # MAYBE:[szmm2jxs not refined]
        #if not szmm2jxs_refined:
        if not refined:
            szmm2jxs = _refine_szmm2jxs_(key, __lt__, szmm2jxs)
        # [szmm2jxs refined]
    # [szmm2jxs refined]
    common_jys = [jxs[0] for jxs in szmm2jxs if len(jxs) == 1]
    jx2r_ = echo if with_idx else snd
    rs = tuple(map(jx2r_, common_jys))
        # [rs == (ys|iys)]
    return rs
def _refine_szmm2jxs_(key, __lt__, szmm2jxs, /):
    # MAYBE:[szmm2jxs not refined]

    def before(iw, jx, /):
        'to find begin4rng6iws for jx # (cmp w x) but required i,j'
        i,w = iw
        j,x = jx
        return i<j and __lt__(key(x),key(w))
        return i<j and w>x
    szmm2jxs = list(map(mk_tuple, szmm2jxs))
    #if len(szmm2jxs) < 2: return szmm2jxs
    #for jxs in reversed(szmm2jxs):
    for szmm in reversed(range(-1+len(szmm2jxs))):
        #jxs = szmm2jxs[szmm]
        #777;succ_jxs = szmm2jxs[1+szmm]
        iws = szmm2jxs[szmm]
        777;jxs = szmm2jxs[1+szmm]
            # iws,jxs:idx ascending『<』, but key descending『>』

        #merge_two_sorted_iterables
        (_, idc4JintoIWS) = batch_find_insert_indices4two_sorted_iterables(iws, jxs, left_key=fst, right_key=fst)
            # 'to find end4rng6iws for jx # (cmp i j)'
        (_, idc4XintoIWS) = batch_find_insert_indices4two_sorted_iterables(iws, jxs, left_key=None, right_key=None, before=before)
            # 'to find begin4rng6iws for jx # (cmp w x) but required i,j'
        i2ok = [False]*len(iws)
        for rng in map(range, idc4XintoIWS, idc4JintoIWS):
            for i in rng:
                i2ok[i] = True
        i2ok
        if not all(i2ok):
            iws = tuple(compress(iws, i2ok))
            szmm2jxs[szmm] = iws
        szmm2jxs
    szmm2jxs
    # [szmm2jxs refined]

    szmm2jxs = tuple(szmm2jxs)
    return szmm2jxs

def min_longest_sorted_subsequence_of_(xs, /, *, key=None, __lt__=None, with_idx=False):
    r'''[[[
    :: Ord k => Iter x -> (min_longest_sorted_subsequence/[x] if not with_idx else [(uint, x)])
    [min_longest_sorted_subsequence_of_(xs) =[def]= min(iter_all_longest_sorted_subsequences_of_(xs))]
    [len_longest_sorted_subsequence_of_(xs) == len(min_longest_sorted_subsequence_of_(xs))]

    [key :: x -> k]
    [__lt__ :: k -> k -> bool]
    #]]]'''#'''
    szmm2jxs = longest_sorted_subsequence_of_ex_(xs, key=key, __lt__=__lt__)
    return _min_lsseq5szmm2jxs_(with_idx, szmm2jxs)
def _min_lsseq5szmm2jxs_(with_idx, szmm2jxs, /):
    jx2r_ = echo if with_idx else snd
    rs = tuple(jx2r_(jxs[-1]) for jxs in szmm2jxs)
        # [rs == (ys|iys)]
    return rs
def longest_sorted_subsequence_of_ex_(xs, /, *, key=None, __lt__=None, to_refine=False):
    r'''[[[
    :: Ord k => Iter x -> szmm2jxs/[[(uint,x)]]
    [longest_sorted_subsequence_of_ex_(xs) =[def]= let [ls:=list(xs)] in longest_common_subsequence_of_ex_(ls, sorted(ls))]
    [len_longest_sorted_subsequence_of_(xs) =[def]= let [ls:=list(xs)] in len_longest_common_subsequence_of_(ls, sorted(ls))]
    [len_longest_sorted_subsequence_of_(xs) == len(longest_sorted_subsequence_of_ex_(xs))]

    [to_refine :: bool]
        refine szmm2jxs by cleanup jx which is not part of any longest_common_subsequence
        # -> szmm2jxs{refined/unextendable}

    [key :: x -> k]
    [__lt__ :: k -> k -> bool]
    [szmm2jxs :: [[(uint,x)]]]
        [all(szmm2jxs)]
        [sorted([jx for jxs in szmm2jxs for jx in jxs], key=fst) == [*enumerate(xs)]]
        [all(i < j and w > x for jxs in szmm2jxs for (i,w), (j,x) in pairwise(jxs))]
            # same height => jxs:idx ascending『<』, but key descending『>』
        [all(any((i < j and w <= x) for (i,w) in iws) for iws,jxs in pairwise(szmm2jxs) for (j,x) in jxs)]
            => [all(any((i < j and w <= x) for (i,w) in iws) and all((i < j or w < x) for (i,w) in iws) for iws,jxs in pairwise(szmm2jxs) for (j,x) in jxs)]
            # [i=!=j]
            # diff height => fixed (j,x) => (MAYBE_HAVE_SOME(i<j and w>x) ++ MUST_HAVE_SOME(i<j and w<=x) ++ MAYBE_HAVE_SOME(i>j and w<x))
            ############
            #.bug:[all(not (i < j and w > x) for iws,jxs in pairwise(szmm2jxs) for (i,w), (j,x) in product(iws,jxs))]
            #.    # [i=!=j]
            #.    # diff height => (i>j or w<=x)
            #.    # diff height => (i>j or i<j and w<=x)
            #.    # diff height => (i>j and w<x or i<j and w<=x)
            #.      #bug:since miss MAYBE_HAVE_SOME(i<j and w>x)
            ############
        [all(w <= x for iws,jxs in pairwise(szmm2jxs) for (i,w), (j,x) in product(iws[-1:],jxs[-1:]))]
            # => min key @snd(szmm2jxs[0][-1])
        [len_longest_sorted_subsequence_of_(xs) == len(szmm2jxs)]
        [all([len_longest_sorted_subsequence_of_(filter(x.__ge__, xs[:j+1])) == 1+szmm] for szmm, jxs in enumerate(szmm2jxs) for j, x in jxs)]
                # [szmm =[def]= -1+len_longest_sorted_subsequence] # i.e. len_longest_sorted_subsequence minus 1

    #]]]'''#'''
    (key, __lt__) = _prepare__key__lt(key, __lt__)
    def _key(i, /):
        return key(szmm2jxs[i][-1][1])
                #key(snd(szmm2jxs[i][-1]))

    szmm2jxs = []
    777;L = len(szmm2jxs)
    777;idc = range(L)
    for jx in enumerate(xs):
        # [all(w <= x for iws,jxs in pairwise(szmm2jxs) for (i,w), (j,x) in product(iws[-1:],jxs[-1:]))]
        j, x = jx
        k = key(x)
        middle_end = bisearch(k, idc, key=_key, __lt__=__lt__, result_case=1)
        if middle_end == L:
            szmm2jxs.append([])
            777;L = len(szmm2jxs)
            777;idc = range(L)
        szmm2jxs[middle_end].append(jx)
        # [all(w <= x for iws,jxs in pairwise(szmm2jxs) for (i,w), (j,x) in product(iws[-1:],jxs[-1:]))]
    szmm2jxs
    # [szmm2jxs not refined]
    if to_refine:
        szmm2jxs = _refine_szmm2jxs_(key, __lt__, szmm2jxs)
        # [szmm2jxs refined]
    # MAYBE:[szmm2jxs not refined]
    szmm2jxs
    return szmm2jxs

__all__
#[common_of_all_longest_sorted_subsequences_of_,min_longest_sorted_subsequence_of_,longest_sorted_subsequence_of_ex_,iter_all_longest_sorted_subsequences_of_,sorted_iter_all_longest_sorted_subsequences_of_] = lazy_import4funcs_('seed.seq_tools.longest_sorted_subsequence', 'common_of_all_longest_sorted_subsequences_of_,min_longest_sorted_subsequence_of_,longest_sorted_subsequence_of_ex_,iter_all_longest_sorted_subsequences_of_,sorted_iter_all_longest_sorted_subsequences_of_', __name__)
from seed.seq_tools.longest_sorted_subsequence import common_of_all_longest_sorted_subsequences_of_, min_longest_sorted_subsequence_of_, longest_sorted_subsequence_of_ex_, iter_all_longest_sorted_subsequences_of_, sorted_iter_all_longest_sorted_subsequences_of_

#[_min_lsseq5szmm2jxs_,_common_lsseq5szmm2jxs_,_refine_szmm2jxs_] = lazy_import4funcs_('seed.seq_tools.longest_sorted_subsequence', '_min_lsseq5szmm2jxs_,_common_lsseq5szmm2jxs_,_refine_szmm2jxs_', __name__)
from seed.seq_tools.longest_sorted_subsequence import _min_lsseq5szmm2jxs_,_common_lsseq5szmm2jxs_,_refine_szmm2jxs_

from seed.seq_tools.longest_sorted_subsequence import *
