#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_max_one.py
    @20241226
max optimal addition chain
max shortest addition chain
see:
    # its-data-is-downloaded-from-www:length-only
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py
see:
    # my-data-is-generated-by:
    view script/搜索冫最短加链长度.py
        20241220


py -m nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one:__doc__ -ht # -ff -df
py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one   @f

[[
prepare:
cp -iv script/搜索冫最短加链长度.py..statistics.up_eq_n.le4333.out.txt.tar.lzma ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_max_one.py..data.statistics.up_eq_n.le4333.tar.lzma
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_read_solo_tarfile_  --xencoding4data:ascii  :../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_max_one.py..data.statistics.up_eq_n.le4333.tar.lzma
]]
[[
py_adhoc_call   script.搜索冫最短加链长度   ,排序冫输出文件纟可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py..statistics.up_eq_n.le4333.out.txt
4333
(0, (1, 0, ((1,), (1, 0, 0))))
... ...
(109283366, (3583, 16, ((1, 2, 4, 8, 16, 32, 64, 128, 256, 320, 328, 329, 649, 1298, 1627, 3254, 3583), (1, 16141962, 109283366))))
35
(0, (1, 0, ((1,), (1, 0, 0))))
(1, (2, 1, ((1, 2), (1, 0, 1))))
(4, (3, 2, ((1, 2, 3), (1, 0, 4))))
(6, (5, 3, ((1, 2, 4, 5), (1, 0, 6))))
(12, (7, 4, ((1, 2, 4, 6, 7), (1, 0, 12))))
(16, (11, 5, ((1, 2, 4, 8, 10, 11), (1, 0, 16))))
(53, (15, 5, ((1, 2, 4, 5, 10, 15), (1, 8, 53))))
(264, (23, 6, ((1, 2, 4, 5, 9, 18, 23), (1, 46, 264))))
(494, (31, 7, ((1, 2, 4, 8, 10, 20, 30, 31), (1, 55, 494))))
(3576, (47, 8, ((1, 2, 4, 8, 12, 13, 26, 39, 47), (1, 426, 3576))))
(6288, (79, 9, ((1, 2, 4, 8, 16, 24, 26, 52, 78, 79), (1, 626, 6288))))
(6686, (93, 9, ((1, 2, 4, 8, 16, 20, 36, 72, 92, 93), (1, 868, 6686))))
(8228, (95, 9, ((1, 2, 4, 8, 16, 20, 21, 37, 74, 95), (1, 1147, 8228))))
(17697, (127, 10, ((1, 2, 4, 8, 16, 32, 40, 42, 84, 126, 127), (1, 1515, 17697))))
(23433, (143, 10, ((1, 2, 4, 8, 16, 32, 36, 37, 74, 111, 143), (1, 2732, 23433))))
(145864, (191, 11, ((1, 2, 4, 8, 16, 32, 48, 52, 53, 106, 159, 191), (1, 13355, 145864))))
(165328, (319, 11, ((1, 2, 4, 8, 16, 24, 25, 49, 98, 196, 294, 319), (1, 31206, 165328))))
(222142, (367, 11, ((1, 2, 4, 8, 9, 17, 34, 68, 77, 145, 290, 367), (1, 50257, 222142))))
(230645, (379, 12, ((1, 2, 4, 8, 16, 32, 64, 96, 104, 105, 210, 315, 379), (1, 21470, 230645))))
(357480, (383, 12, ((1, 2, 4, 8, 16, 32, 64, 80, 84, 85, 149, 298, 383), (1, 38578, 357480))))
(484038, (543, 12, ((1, 2, 4, 8, 16, 32, 36, 72, 144, 180, 181, 362, 543), (1, 89898, 484038))))
(543471, (559, 12, ((1, 2, 4, 8, 16, 32, 33, 66, 132, 165, 197, 394, 559), (1, 106512, 543471))))
(979041, (671, 13, ((1, 2, 4, 8, 16, 32, 64, 128, 136, 138, 266, 532, 670, 671), (1, 112057, 979041))))
(2611347, (767, 13, ((1, 2, 4, 8, 16, 32, 64, 72, 73, 137, 274, 347, 694, 767), (1, 415364, 2611347))))
(5189360, (1111, 14, ((1, 2, 4, 8, 16, 32, 64, 128, 192, 196, 197, 393, 786, 983, 1111), (1, 618902, 5189360))))
(6569756, (1151, 14, ((1, 2, 4, 8, 16, 32, 64, 128, 160, 164, 328, 329, 658, 987, 1151), (1, 842193, 6569756))))
(7052762, (1279, 14, ((1, 2, 4, 8, 16, 32, 64, 128, 136, 137, 201, 402, 539, 1078, 1279), (1, 1057913, 7052762))))
(7624790, (1519, 14, ((1, 2, 4, 8, 16, 32, 64, 96, 97, 194, 388, 485, 970, 1455, 1519), (1, 1376244, 7624790))))
(8938786, (1533, 14, ((1, 2, 4, 8, 16, 32, 64, 80, 81, 162, 242, 484, 968, 1452, 1533), (1, 1658265, 8938786))))
(16353919, (2047, 15, ((1, 2, 4, 8, 16, 32, 64, 128, 256, 288, 292, 584, 585, 1170, 1755, 2047), (1, 2038760, 16353919))))
(16377901, (2207, 15, ((1, 2, 4, 8, 16, 32, 64, 128, 256, 260, 520, 648, 649, 1298, 1947, 2207), (1, 2375970, 16377901))))
(26445982, (2431, 15, ((1, 2, 4, 8, 16, 32, 64, 128, 160, 162, 324, 648, 810, 1620, 2430, 2431), (1, 4529601, 26445982))))
(34593953, (3067, 15, ((1, 2, 4, 8, 16, 32, 64, 65, 130, 146, 211, 357, 714, 1428, 2856, 3067), (1, 7412331, 34593953))))
(45303465, (3199, 15, ((1, 2, 4, 8, 16, 32, 33, 65, 98, 196, 392, 457, 914, 1828, 2742, 3199), (1, 10409484, 45303465))))
(109283366, (3583, 16, ((1, 2, 4, 8, 16, 32, 64, 128, 256, 320, 328, 329, 649, 1298, 1627, 3254, 3583), (1, 16141962, 109283366))))
]]
]]]'''#'''
__all__ = r'''
pint2max_shortest_addition_chain
    pint2max_shortest_addition_chain__first_4333_terms

pint2arbitrary_shortest_addition_chain
    pint2arbitrary_shortest_addition_chain__first_4333_terms




pint2may__i2may_jk4max_shortest_addition_chain
    pint2may__i2may_jk4max_shortest_addition_chain__first_4333_terms
pint2may__i2may_jk4arbitrary_shortest_addition_chain
    pint2may__i2may_jk4arbitrary_shortest_addition_chain__first_4333_terms
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
if 0:
    #see:check_addition_chain_()
    from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length__first_100000_terms as _n2sz

from seed.tiny_.check import check_type_is, check_int_ge
from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
from io import BytesIO
from ast import literal_eval

from seed.for_libs.for_tarfile import iter_read_solo_tarfile_
___end_mark_of_excluded_global_names__0___ = ...
pint2max_shortest_addition_chain__first_4333_terms = (None, *(us
for n, sz, (us, statistics)
in map(literal_eval, iter_read_solo_tarfile_
    (BytesIO(read_under_pkg_
        (__package__
        , 'shortest_addition_chain__the_max_one.py..data.statistics.up_eq_n.le4333.tar.lzma', xencoding=None
        ))
    , xencoding4data='ascii'
    ))
))
#end-pint2max_shortest_addition_chain__first_4333_terms
assert len(pint2max_shortest_addition_chain__first_4333_terms) == 1+4333
assert (__:=pint2max_shortest_addition_chain__first_4333_terms[:10]) == (None, (1,), (1, 2), (1, 2, 3), (1, 2, 4), (1, 2, 4, 5), (1, 2, 4, 6), (1, 2, 4, 6, 7), (1, 2, 4, 8), (1, 2, 4, 8, 9)), __

pint2max_shortest_addition_chain = pint2max_shortest_addition_chain__first_4333_terms


pint2arbitrary_shortest_addition_chain = pint2arbitrary_shortest_addition_chain__first_4333_terms = pint2max_shortest_addition_chain__first_4333_terms




######################
######################
#copy from:view script/搜索冫最短加链长度.py
#def check_addition_chain_ -->:
def _check_addition_chain(addition_chain, /, *, non_shortest_ok:[None, bool], may__i2may_jk=None, to_output__i2may_jk=False, allow_without_statistical_information=True, allow_with_statistical_information=False):
    '[allow non-shortest]:addition_chain/(n/pint, sz/加链长度/uint, us_ex) -> ((None if not to_output__i2may_jk else i2may_jk/[may (j/pint,k/pint)])|^Exception)'
    ######################
    check_type_is(tuple, addition_chain)
    assert len(addition_chain) == 3, TypeError(len(addition_chain))
    (n, sz, us_ex) = addition_chain
    check_int_ge(1, n)
    check_int_ge(0, sz)
    ######################
    if not non_shortest_ok is None:
        check_type_is(bool, non_shortest_ok)
    if non_shortest_ok is False:raise NotImplementedError
    ######################
    if non_shortest_ok is None:
        _n2sz = _get_n2optimal_sz()
    ######################
    if not (non_shortest_ok is True or non_shortest_ok is None and n < len(_n2sz)):raise NotImplementedError
    if non_shortest_ok is None:
        # optimal addition chain
        _n2sz
        assert sz == _n2sz[n], ValueError(n, sz, _n2sz[n])
        #if 0b0001:print_err('ok:', n, sz)
    elif non_shortest_ok is True:
        # non_optimal addition chain
        pass
    else:
        raise 000
    ######################
    # check us_ex
    check_type_is(tuple, us_ex)
    assert us_ex, TypeError
    if not type(us_ex[-1]) is int:
        # [us_ex == (us, statistics)]
        # [with_statistical_information]
        if not allow_with_statistical_information:raise TypeError
        check_type_is(tuple, us_ex[-1])
        assert len(us_ex) == 2, TypeError(len(us_ex))
        (us, statistics) = us_ex
        #########
        # check statistics
        check_type_is(tuple, statistics)
        assert len(statistics) == 3, TypeError(len(statistics))
        (num_fulfilled_uss, num_pops, num_checked_items) = statistics
        check_int_ge(0, num_fulfilled_uss)
        check_int_ge(0, num_pops)
        check_int_ge(0, num_checked_items)
        assert num_fulfilled_uss-1 <= num_pops <= num_checked_items, statistics
        #########
        us
    else:
        # [us_ex == us]
        # [not with_statistical_information]
        if not allow_without_statistical_information:raise TypeError
        us = us_ex
    us
    ######################
    # check us
    check_type_is(tuple, us)
    assert len(us) == sz+1, TypeError(sz, len(us))
    u_ = 0
    for u in us:
        #strict_sorted
        check_int_ge(u_+1, u)
        u_ = u
    assert us, ValueError(us)
    assert us[0] == 1, ValueError(us)
    assert us[-1] == n, ValueError(n, us)

    ######################
    # mk i2may_jk
    if may__i2may_jk:
        i2may_jk = may__i2may_jk
    else:
        i2u = us
        u2i = {u:i for i, u in enumerate(us)}
        i2may_jk = [None]
        for i, ui in enumerate(us):
            if i == 0:continue
            assert len(i2may_jk) == i, 000
            for j in reversed(range(i)):
                uj = us[j]
                uk = ui -uj
                if uk > uj:
                    # fail
                    break
                if not None is (k := u2i.get(uk)):
                    i2may_jk.append((j,k))
                    break
            else:
                #fail
                pass
            if len(i2may_jk) == i:
                #fail
                raise ValueError(addition_chain, i, ui)
            assert len(i2may_jk) == i+1, 000
        assert len(i2may_jk) == len(us), 000
    i2may_jk
    ######################
    # check using i2may_jk
    assert len(i2may_jk) == len(us), TypeError(len(us), len(i2may_jk))
    for i, ui in enumerate(us):
        if i == 0:
            assert i2may_jk[i] is None, TypeError
            assert ui == 1, 000
            continue

        j, k = i2may_jk[i]
        assert i >= j >= k >= 0, TypeError
        assert ui == us[j] + us[k], (addition_chain, i2may_jk, (i, j, k), (ui, us[j], us[k]))
    ######################
    if to_output__i2may_jk:
        return i2may_jk
    return None
    ######################
def _get_n2optimal_sz():
    global _n2sz
    try:
        return _n2sz
    except NameError:
        from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length__first_100000_terms as _n2sz
        return _get_n2optimal_sz()
######################
######################

def _may_us2may_i2may_jk(may_us, /):
    'may us -> may i2may_jk'
    if may_us is None:
        return None
    us = may_us
    i2may_jk = _us2i2may_jk(us)
    return i2may_jk
def _us2i2may_jk(us, /):
    'us -> i2may_jk'
    ######################
    n = us[-1]
    sz = len(us) -1
    addition_chain = (n, sz, us)
    ######################
    i2may_jk = _check_addition_chain(addition_chain, non_shortest_ok=None, may__i2may_jk=None, to_output__i2may_jk=True, allow_without_statistical_information=True, allow_with_statistical_information=False)
    i2may_jk = tuple(i2may_jk)
    check_type_is(tuple, i2may_jk)
    assert i2may_jk
    assert i2may_jk[0] is None
    ######################
    __ = _check_addition_chain(addition_chain, non_shortest_ok=None, may__i2may_jk=i2may_jk, to_output__i2may_jk=False, allow_without_statistical_information=True, allow_with_statistical_information=False)
    assert __ is None
    ######################
    return i2may_jk
pint2may__i2may_jk4max_shortest_addition_chain__first_4333_terms = (*map(_may_us2may_i2may_jk, pint2max_shortest_addition_chain__first_4333_terms),)
assert len(pint2may__i2may_jk4max_shortest_addition_chain__first_4333_terms) == 1+4333
assert (__:=pint2may__i2may_jk4max_shortest_addition_chain__first_4333_terms[:10]) == (None, (None,), (None, (0, 0)), (None, (0, 0), (1, 0)), (None, (0, 0), (1, 1)), (None, (0, 0), (1, 1), (2, 0)), (None, (0, 0), (1, 1), (2, 1)), (None, (0, 0), (1, 1), (2, 1), (3, 0)), (None, (0, 0), (1, 1), (2, 2)), (None, (0, 0), (1, 1), (2, 2), (3, 0))), __

pint2may__i2may_jk4max_shortest_addition_chain = pint2may__i2may_jk4max_shortest_addition_chain__first_4333_terms

pint2may__i2may_jk4arbitrary_shortest_addition_chain = pint2may__i2may_jk4arbitrary_shortest_addition_chain__first_4333_terms = pint2may__i2may_jk4max_shortest_addition_chain__first_4333_terms

__all__
from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one import pint2max_shortest_addition_chain, pint2arbitrary_shortest_addition_chain
from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one import pint2max_shortest_addition_chain__first_4333_terms, pint2arbitrary_shortest_addition_chain__first_4333_terms

from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one import pint2may__i2may_jk4max_shortest_addition_chain, pint2may__i2may_jk4arbitrary_shortest_addition_chain
from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one import pint2may__i2may_jk4max_shortest_addition_chain__first_4333_terms, pint2may__i2may_jk4arbitrary_shortest_addition_chain__first_4333_terms

from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one import *
