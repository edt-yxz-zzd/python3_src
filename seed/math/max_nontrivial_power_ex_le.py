#__all__:goto
r'''[[[
e ../../python3_src/seed/math/max_nontrivial_power_ex_le.py

seed.math.max_nontrivial_power_ex_le
py -m nn_ns.app.debug_cmd   seed.math.max_nontrivial_power_ex_le -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.max_nontrivial_power_ex_le:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.math.max_nontrivial_power_ex_le:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
]]


'#'; __doc__ = r'#'

######################
>>> def test__us_(us, /, *, to_show):
...     for u in us:
...         t = max_nontrivial_power_ex_le(u)
...         _t = _max_nontrivial_power_ex_le(u)
...         assert t == _t, (u, t, _t)
...         if to_show:print(u, t)
>>> def test__u_a_b_(u, a, b, /, *, to_show):
...     test__us_(range(u-a, 1+u+b), to_show=False)

>>> test__us_(range(4, 5+2**12), to_show=False)
>>> test__u_a_b_(3**(2**3 *3**2 *5), 9, 9, to_show=False)


######################
>>> greedy_power_uint_notation_of_(99999999999, validate=True)
(1, ((2, 316227), (2, 696), (2, 7), (2, 2)))

>>> r0 = uint2recur_greedy_power_uint_notation_(99999999999)
>>> r0
(1, ((2, (2, ((2, (1, ((2, (3, ((4, (2, ())), (2, (2, ()))))), (5, (2, ()))))), (2, (3, ((4, (2, ())),))), (4, (2, ())), (2, (2, ()))))), (2, (0, ((2, (1, ((2, (1, ((2, (2, ())),))),))), (4, (2, ())), (2, (2, ()))))), (2, (3, ((2, (2, ())),))), (2, (2, ()))))

(1, ((2, (0, ((2, (0, ((2, (1, ((4, (0, ())), (2, (0, ()))))), (3, (1, ())), (2, (0, ()))))), (2, (1, ((4, (0, ())),))), (4, (0, ())), (2, (0, ()))))), (2, (2, ((2, (0, ((4, (0, ())), (3, (0, ()))))), (4, (0, ()))))), (2, (1, ((2, (0, ())),))), (2, (0, ()))))
    # <<== base_minus2 #base-2

>>> uint5recur_greedy_power_uint_notation_(r0)
99999999999




######################
>>> greedy_square_uint_notation_of_(99999999999, validate=True)
(1, (316227, 696, 7, 2))

>>> r1 = uint2recur_greedy_square_uint_notation_(99999999999)
>>> r1
(1, ((2, ((0, ((3, ((0, ((2, ()),)), (2, ()))), (1, ((2, ()),)), (2, ()), (2, ()))), (3, ((0, ((2, ()),)),)), (0, ((2, ()),)), (2, ()))), (0, ((1, ((1, ((2, ()),)),)), (0, ((2, ()),)), (2, ()))), (3, ((2, ()),)), (2, ())))

(1, ((0, ((2, ((1, ((2, ()), (0, ()))), (3, ()), (0, ()))), (1, ((2, ()),)), (2, ()), (0, ()))), (2, ((0, ((2, ()), (0, ()), (0, ()))), (2, ()))), (1, ((0, ()),)), (0, ())))
    # <<== base_minus2 #base-2

>>> uint5recur_greedy_square_uint_notation_(r1)
99999999999








######################
!!bug:since [r0 contains exps...][r0 is not quaternary_tree]
#.>>> s0 = quaternary_tree2quinary_str_(r0)
#.>>> r0 == quaternary_tree5quinary_str_(s0)
#.True
#.>>> s0
#.>>> u0 = quaternary_tree2quinary_uint_(r0)
#.>>> r0 == quaternary_tree5quinary_uint_(u0)
#.True
#.>>> u0


######################
>>> s1 = quaternary_tree2quinary_str_(r1)
>>> r1 == quaternary_tree5quinary_str_(s1)
True
>>> s1
'120302442441244242443024440244244011244402442443244244'
>>> u1 = quaternary_tree2quinary_uint_(r1)
>>> r1 == quaternary_tree5quinary_uint_(u1)
True
>>> u1
15820176394452354837929750818599587449






######################
py_adhoc_call   seed.math.max_nontrivial_power_ex_le   @f
]]]'''#'''
__all__ = r'''
max_nontrivial_power_ex_le
    greedy_power_uint_notation_of_
    uint2recur_greedy_power_uint_notation_
        uint5recur_greedy_power_uint_notation_

greedy_square_uint_notation_of_
    uint2recur_greedy_square_uint_notation_
        uint5recur_greedy_square_uint_notation_







quaternary_tree5iter_quinary_digits_
    quaternary_tree2iter_quinary_digits_
quaternary_tree5quinary_str_
    quaternary_tree2quinary_str_
quaternary_tree5quinary_uint_
    quaternary_tree2quinary_uint_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_

is_kth_power_ = lazy_import4func_('seed.math.factor_pint_as_pefect_power_', 'is_kth_power_', __name__)
if 0:from seed.math.factor_pint_as_pefect_power_ import is_kth_power_
##from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_

II__p2e_ = lazy_import4func_('seed.math.II', 'II__p2e_', __name__)
if 0:from seed.math.II import II__p2e_

lazy_import4funcs_('seed.math.floor_ceil', 'floor_log2,floor_kth_root_,floor_sqrt', __name__)
if 0:from seed.math.floor_ceil import floor_log2, floor_kth_root_, floor_sqrt

___end_mark_of_excluded_global_names__0___ = ...


def _max_nontrivial_power_ex_le(u, /):
    check_int_ge(4, u)
    ez = u.bit_length() - 1 #floor_log2(u)
    def __(u, /):
        from seed.math.floor_ceil import floor_kth_root_
        for e in range(2, 1+ez):
            rt = floor_kth_root_(e, u)
            assert rt >= 2
            pw = rt**e
            df = u-pw
            yield (pw, e, rt, df)
    return max(__(u))
def max_nontrivial_power_ex_le(u, /):
    'u/uint{>=4} -> (max_nontrivial_power, exp, base, diff) # [[u :: uint{>=4}] => [max_nontrivial_power_ex_le(u) =[def]= max{(power, exp, base, diff) | [[exp:<-[2..]][base:<-[2..]][power:=exp**base][power <= u][diff:=u-power]]}]]'
    check_int_ge(4, u)
    ez = u.bit_length() - 1 #floor_log2(u)
    zpow = 1<<ez
    dz = u - zpow
    assert 0 <= dz < zpow
    tz = (zpow, ez, 2, dz)
    if dz == 0:
        return tz

    from seed.math.prime_gens import prime_gen
    #bug:ls = [(zpow, ez, 2, dz)]
    #   [ez is not prime]
    ls = []
    min_df = dz
    for ep in prime_gen.iter__lt_(ez):
        #bug:if ez %ep == 0:continue
        #   AssertionError: (25, (16, 4, 2, 9), (25, 2, 5, 0))
        rt = floor_kth_root_(ep, u)
        pw = rt**ep
        df = u -pw
        if df <= min_df:
            if not df == min_df:
                min_df = df
                ls.clear()
            ls.append((pw, ep, rt, df))
    ls
    if not ls or min_df == dz:
        return tz
    (max_pw, ep0, rt0, _min_df) = ls[0]
    ps = [ep for (pw, ep, rt, df) in ls]
    rt = rt0
    p2e = {ep0:1}
    for p in ps[1:]:
        rt = floor_kth_root_(p, rt)
        p2e[p] = 1
    for p in ps:
        while is_kth_power_(p, rt):
            assert rt >= 2, (u, ls, ps)
            rt = floor_kth_root_(p, rt)
            p2e[p] += 1
    rt, p2e
    exp = II__p2e_(p2e)
    base = rt
    return (max_pw, exp, base, min_df)

def greedy_power_uint_notation_of_(u, /, *, validate=False):
    'u/uint -> greedy_power_uint_notation/(uint%4, [(exp/uint{>=2},base/uint{>=2})]){u==greedy_power_uint_notation[0]+sum(base**exp for exp,base in greedy_power_uint_notation[1])}'
    check_int_ge(0, u)
    ls = []
    v = u
    while v >= 4:
        (pw, e, rt, df) = max_nontrivial_power_ex_le(v)
        ls.append((e,rt))
        v = df
    v, ls
    ts = tuple(ls)
    h = v
    r = (h, ts)
    if validate:
        (h, ts) = r
        assert 0 <= h < 4
        assert all(exp >= 2 and base >=2 for exp, base in ts)
        if not u == h+sum(base**exp for exp,base in ts):raise AssertionError(u, ts)
    return r

def greedy_square_uint_notation_of_(u, /, *, validate=False):
    'u/uint -> greedy_square_uint_notation/(uint%4,[base/uint{>=2}]){u==greedy_square_uint_notation[0]+sum(base**2 for base in greedy_square_uint_notation[1])}'
    check_int_ge(0, u)
    ls = []
    v = u
    while v >= 4:
        rt = floor_sqrt(v)
        pw = rt**2
        df = v-pw
        ls.append(rt)
        v = df
    v, ls
    ts = tuple(ls)
    h = v
    r = (h, ts)
    if validate:
        (h, ts) = r
        assert 0 <= h < 4
        assert all(base >=2 for base in ts)
        if not u == h+sum(base**2 for base in ts):raise AssertionError(u, r)
    return r



def _mk_25():
    from seed.func_tools.recur5yield__strict import BoxedTailRecur, BoxedFinalResult
    from seed.func_tools.recur5yield__strict import IDecorator4recur5yield, Decorator4recur5yield
    from seed.func_tools.recur5yield__strict import IExecutor4recur5yield, IExecutor4recur5yield__dispatch_by_dict, Executor4recur5yield__dispatch_by_dict

    st = None
    dr2 = Decorator4recur5yield(Executor4recur5yield__dispatch_by_dict(None, True, True, None))
    ######################
    @dr2
    def uint2recur_greedy_power_uint_notation_(u, /):
        return (st, _r5u_(u))
    def _r5u_(u, /):
        greedy_power_uint_notation = greedy_power_uint_notation_of_(u)
        (h, ts) = greedy_power_uint_notation
        assert 0 <= h < 4
        ls = []
        for exp, base in ts:
            assert exp >= 2
            assert base >= 2
            #.base_minus2 = base-2
            #.recur_notation4base_minus2 = yield _r5u_(base_minus2)
            #.ls.append((exp, recur_notation4base_minus2))
            recur_notation4base = yield _r5u_(base)
            ls.append((exp, recur_notation4base))

        ls
        ts = tuple(ls)
        return BoxedFinalResult((h, ts))

    @dr2
    def uint5recur_greedy_power_uint_notation_(recur_greedy_power_uint_notation, /):
        return (st, _r2u_(recur_greedy_power_uint_notation))
    def _r2u_(recur_greedy_power_uint_notation, /):
        (h, ts) = recur_greedy_power_uint_notation
        assert 0 <= h < 4
        u = h
        #.for exp, recur_notation4base_minus2 in ts:
        for exp, recur_notation4base in ts:
            assert exp >= 2
            #.base_minus2 = yield _r2u_(recur_notation4base_minus2)
            #.base = 2+base_minus2
            base = yield _r2u_(recur_notation4base)
            assert base >= 2
            pw = base**exp
            u += pw
        u
        return BoxedFinalResult(u)
    ######################

    ######################
    @dr2
    def uint2recur_greedy_square_uint_notation_(u, /):
        return (st, _rz5u_(u))
    def _rz5u_(u, /):
        greedy_square_uint_notation = greedy_square_uint_notation_of_(u)
        (h, ts) = greedy_square_uint_notation
        assert 0 <= h < 4
        ls = []
        for base in ts:
            assert base >= 2
            #.base_minus2 = base-2
            #.recur_notation4base_minus2 = yield _rz5u_(base_minus2)
            #.ls.append(recur_notation4base_minus2)
            recur_notation4base = yield _rz5u_(base)
            ls.append(recur_notation4base)

        ls
        ts = tuple(ls)
        return BoxedFinalResult((h, ts))

    @dr2
    def uint5recur_greedy_square_uint_notation_(recur_greedy_square_uint_notation, /):
        return (st, _rz2u_(recur_greedy_square_uint_notation))
    def _rz2u_(recur_greedy_square_uint_notation, /):
        (h, ts) = recur_greedy_square_uint_notation
        assert 0 <= h < 4
        u = h
        #.for recur_notation4base_minus2 in ts:
        for recur_notation4base in ts:
            #.base_minus2 = yield _rz2u_(recur_notation4base_minus2)
            #.base = 2+base_minus2
            base = yield _rz2u_(recur_notation4base)
            assert base >= 2
            pw = base**2
            u += pw
        u
        return BoxedFinalResult(u)
    ######################
    return ((uint2recur_greedy_power_uint_notation_, uint5recur_greedy_power_uint_notation_), (uint2recur_greedy_square_uint_notation_, uint5recur_greedy_square_uint_notation_))
    ######################
def _inject_25():
    global _u2r, _u5r, _u2rz, _u5rz, _mk_25, _inject_25
    ((_u2r, _u5r), (_u2rz, _u5rz)) = _mk_25()
    del _mk_25, _inject_25
    return (_u2r, _u5r)
def _u2r(u, /):
    _inject_25()
    return _u2r(u)
def _u5r(r, /):
    _inject_25()
    return _u5r(r)
def _u2rz(u, /):
    _inject_25()
    return _u2rz(u)
def _u5rz(r, /):
    _inject_25()
    return _u5rz(r)
######################
def uint5recur_greedy_power_uint_notation_(recur_greedy_power_uint_notation, /):
    'recur_greedy_power_uint_notation -> uint #see:uint2recur_greedy_power_uint_notation_()'
    return _u5r(recur_greedy_power_uint_notation)
def uint2recur_greedy_power_uint_notation_(u, /):
    'u/uint -> recur_greedy_power_uint_notation/(uint%4, [(exp/uint{>=2},recur_notation4base/recur_greedy_power_uint_notation)]){u==uint5recur_greedy_power_uint_notation_(recur_greedy_power_uint_notation)==recur_greedy_power_uint_notation[0]+sum((uint5recur_greedy_power_uint_notation_(recur_notation4base))**exp for exp,recur_notation4base in recur_greedy_power_uint_notation[1])}'
    #.'u/uint -> recur_greedy_power_uint_notation/(uint%4, [(exp/uint{>=2},recur_notation4base_minus2/recur_greedy_power_uint_notation)]){u==uint5recur_greedy_power_uint_notation_(recur_greedy_power_uint_notation)==recur_greedy_power_uint_notation[0]+sum((uint5recur_greedy_power_uint_notation_(recur_notation4base_minus2)+2)**exp for exp,recur_notation4base_minus2 in recur_greedy_power_uint_notation[1])}'
    return _u2r(u)
######################

######################
def uint5recur_greedy_square_uint_notation_(recur_greedy_square_uint_notation, /):
    'recur_greedy_square_uint_notation -> uint #see:uint2recur_greedy_square_uint_notation_()'
    return _u5rz(recur_greedy_square_uint_notation)
def uint2recur_greedy_square_uint_notation_(u, /):
    'u/uint -> recur_greedy_square_uint_notation/(uint%4, [recur_notation4base/recur_greedy_square_uint_notation]){u==uint5recur_greedy_square_uint_notation_(recur_greedy_square_uint_notation)==recur_greedy_square_uint_notation[0]+sum((uint5recur_greedy_square_uint_notation_(recur_notation4base))**2 for recur_notation4base in recur_greedy_square_uint_notation[1])}'
    #.'u/uint -> recur_greedy_square_uint_notation/(uint%4, [recur_notation4base_minus2/recur_greedy_square_uint_notation]){u==uint5recur_greedy_square_uint_notation_(recur_greedy_square_uint_notation)==recur_greedy_square_uint_notation[0]+sum((uint5recur_greedy_square_uint_notation_(recur_notation4base_minus2)+2)**2 for recur_notation4base_minus2 in recur_greedy_square_uint_notation[1])}'
    return _u2rz(u)
######################



######################
#.def quaternary_tree5iter_senary_digits_(senary_digits, /):
#.    'Iter senary_digit/uint%6 -> tree{quaternary_digit/uint%4} # [tree{T} =[def]= (T, [tree{T}])]'
#.    return quaternary_tree
#.def quaternary_tree2iter_senary_digits_(quaternary_tree, /):
#.    'tree{quaternary_digit/uint%4} -> Iter senary_digit/uint%6 # [tree{T} =[def]= (T, [tree{T}])]'
#.    return senary_digits
######################
def quaternary_tree5iter_quinary_digits_(quinary_digits, /):
    'Iter quinary_digit/uint%5 -> tree{quaternary_digit/uint%4} # [tree{T} =[def]= (T, [tree{T}])]'
    _close = 4
    def impl_(digits, /):
        it = iter(digits)
        u = _next(it)
        return _1_recur_(u, it)
    def _next(it, /):
        for u in it:
            break
        else:
            raise ValueError('tree empty or incomplete')
        return u
    def _1_recur_(u, it, /):
        assert 0 <= u < _close
        #_open = u
        children = []
        while 1:
            v = _next(it)
            if v == _close:break
            subtree = _1_recur_(v, it)
            children.append(subtree)
        children = tuple(children)
        tree = (u, children)
        return tree
    quaternary_tree = impl_(quinary_digits)
    return quaternary_tree
def quaternary_tree2iter_quinary_digits_(quaternary_tree, /):
    'tree{quaternary_digit/uint%4} -> Iter quinary_digit/uint%5 # [tree{T} =[def]= (T, [tree{T}])]'
    _close = 4
    def recur_(tree, /):
        (u, children) = tree
        assert 0 <= u < _close
        _open = u
        yield _open
        for subtree in children:
            yield from recur_(subtree)
        yield _close
        return
    quinary_digits = recur_(quaternary_tree)
    return quinary_digits
######################
def quaternary_tree5quinary_str_(quinary_str, /):
    'quinary_str/str -> tree{quaternary_digit/uint%4} # [tree{T} =[def]= (T, [tree{T}])]'
    #.quinary_digits = map(ord('0').__rsub__, map(ord, quinary_str))
    quinary_digits = map(int, quinary_str)
    quaternary_tree = quaternary_tree5iter_quinary_digits_(quinary_digits)
    return quaternary_tree
def quaternary_tree2quinary_str_(quaternary_tree, /):
    'tree{quaternary_digit/uint%4} -> quinary_str/str # [tree{T} =[def]= (T, [tree{T}])]'
    quinary_digits = quaternary_tree2iter_quinary_digits_(quaternary_tree)
    #.quinary_str = ''.join(map(chr, map(ord('0').__add__, quinary_digits)))
    quinary_str = ''.join(map(str, quinary_digits))
    return quinary_str
######################
def quaternary_tree5quinary_uint_(quinary_uint, /):
    'quinary_uint/uint -> tree{quaternary_digit/uint%4} # [tree{T} =[def]= (T, [tree{T}])]'
    from seed.int_tools.digits.uint2radix_repr import uint2radix_repr__big_endian
    quinary_str = uint2radix_repr__big_endian(5, quinary_uint)
    quaternary_tree = quaternary_tree5quinary_str_(quinary_str)
    return quaternary_tree
def quaternary_tree2quinary_uint_(quaternary_tree, /):
    'tree{quaternary_digit/uint%4} -> quinary_uint/uint # [tree{T} =[def]= (T, [tree{T}])]'
    quinary_str = quaternary_tree2quinary_str_(quaternary_tree)
    quinary_uint = int(quinary_str, 5)
    return quinary_uint
######################


__all__
#[max_nontrivial_power_ex_le,greedy_power_uint_notation_of_] = lazy_import4funcs_('seed.math.max_nontrivial_power_ex_le', 'max_nontrivial_power_ex_le,greedy_power_uint_notation_of_', __name__)
from seed.math.max_nontrivial_power_ex_le import max_nontrivial_power_ex_le, greedy_power_uint_notation_of_

#[uint2recur_greedy_power_uint_notation_,uint5recur_greedy_power_uint_notation_] = lazy_import4funcs_('seed.math.max_nontrivial_power_ex_le', 'uint2recur_greedy_power_uint_notation_,uint5recur_greedy_power_uint_notation_', __name__)
from seed.math.max_nontrivial_power_ex_le import uint2recur_greedy_power_uint_notation_, uint5recur_greedy_power_uint_notation_

#[uint2recur_greedy_square_uint_notation_,uint5recur_greedy_square_uint_notation_] = lazy_import4funcs_('seed.math.max_nontrivial_power_ex_le', 'uint2recur_greedy_square_uint_notation_,uint5recur_greedy_square_uint_notation_', __name__)
from seed.math.max_nontrivial_power_ex_le import uint2recur_greedy_square_uint_notation_, uint5recur_greedy_square_uint_notation_


from seed.math.max_nontrivial_power_ex_le import quaternary_tree5iter_quinary_digits_, quaternary_tree2iter_quinary_digits_
from seed.math.max_nontrivial_power_ex_le import quaternary_tree5quinary_str_, quaternary_tree2quinary_str_
from seed.math.max_nontrivial_power_ex_le import quaternary_tree5quinary_uint_, quaternary_tree2quinary_uint_

from seed.math.max_nontrivial_power_ex_le import *
