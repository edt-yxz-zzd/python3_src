r'''
seed.data_funcs.lnkls
py -m nn_ns.app.debug_cmd   seed.data_funcs.lnkls
from seed.data_funcs.lnkls import lflnkls_ops, empty_lflnkls, lflnkls_ipush_left, lflnkls_ipop_left, lflnkls2iterable, lflnkls5reversed_iterable

from seed.data_funcs.lnkls import lflnkls5reverseable, lflnkls5args


from seed.data_funcs.lnkls import rglnkls_ops, empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable

from seed.data_funcs.lnkls import rglnkls2list




e ../../python3_src/seed/data_funcs/lnkls.py
see:
    view ../../python3_src/seed/types/pair_based_leftward_list.py

lnkls = singly-linked-list


lflnkls = leftward-lnkls
rglnkls = rightward-lnkls

lflnkls = () | (x, lflnkls)
    push at front
    append_left

rglnkls = () | (rglnkls, x)
    push at end
    append_right

#'''

__all__ = '''
    lflnkls_ops
        empty_lflnkls

        lflnkls_ipush_left
        lflnkls_ipop_left

        lflnkls2iterable
        lflnkls5reversed_iterable

        lflnkls5reverseable
        lflnkls5args


    rglnkls_ops
        empty_rglnkls

        rglnkls_ipush_right
        rglnkls_ipop_right

        rglnkls2reversed_iterable
        rglnkls5iterable

        rglnkls2list


    '''.split()

#empty_lflnkls = empty_rglnkls = ()
_empty_lnkls = ()


#[[[
def _mk_lflnkls_ops():
    empty_lflnkls = _empty_lnkls
    def ipush_left(lflnkls, x, /):
        _lflnkls = (x, lflnkls)
        result = None
        return _lflnkls, result
    def ipop_left(lflnkls, /):
        (x, _lflnkls) = lflnkls
        result = x
        return _lflnkls, result

    def lflnkls2iterable(lflnkls, /):
        while lflnkls:
            lflnkls, x = ipop_left(lflnkls)
            yield x
    def lflnkls5reversed_iterable(reversed_iter, /):
        lflnkls = empty_lflnkls
        for x in reversed_iter:
            lflnkls, _ = ipush_left(lflnkls, x)
        return lflnkls
    def lflnkls5reverseable(reverseable, /):
        return lflnkls5reversed_iterable(reversed(reverseable))
    def lflnkls5args(*args):
        return lflnkls5reverseable(args)
    ######################
    return (empty_lflnkls, ipush_left, ipop_left, lflnkls2iterable, lflnkls5reversed_iterable, lflnkls5reverseable, lflnkls5args)
    ######################
#end def _mk_lflnkls_ops():


lflnkls_ops = _mk_lflnkls_ops()
(empty_lflnkls, lflnkls_ipush_left, lflnkls_ipop_left, lflnkls2iterable, lflnkls5reversed_iterable, lflnkls5reverseable, lflnkls5args) = lflnkls_ops
class lflnkls_ops:
    __slots__ = ()
    (empty_lflnkls, ipush_left, ipop_left, lflnkls2iterable, lflnkls5reversed_iterable, lflnkls5reverseable, lflnkls5args) = map(staticmethod, lflnkls_ops)
lflnkls_ops = lflnkls_ops()
#]]]








#[[[
def _mk_rglnkls_ops():
    empty_rglnkls = _empty_lnkls
    def ipush_right(rglnkls, x, /):
        _rglnkls = (rglnkls, x)
        result = None
        return _rglnkls, result
    def ipop_right(rglnkls, /):
        (_rglnkls, x) = rglnkls
        result = x
        return _rglnkls, result

    def rglnkls2reversed_iterable(rglnkls, /):
        while rglnkls:
            rglnkls, x = ipop_right(rglnkls)
            yield x
    def rglnkls2list(rglnkls, /):
        ls = [*rglnkls2reversed_iterable(rglnkls)]
        ls.reverse()
        return ls

    def rglnkls5iterable(it, /):
        rglnkls = empty_rglnkls
        for x in it:
            rglnkls, _ = ipush_right(rglnkls, x)
        return rglnkls
    ######################
    return (empty_rglnkls, ipush_right, ipop_right, rglnkls2reversed_iterable, rglnkls2list, rglnkls5iterable)
    ######################
#end def _mk_rglnkls_ops():

rglnkls_ops = _mk_rglnkls_ops()
(empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls2list, rglnkls5iterable) = rglnkls_ops
class rglnkls_ops:
    __slots__ = ()
    (empty_rglnkls, ipush_right, ipop_right, rglnkls2reversed_iterable, rglnkls2list, rglnkls5iterable) = map(staticmethod, rglnkls_ops)
rglnkls_ops = rglnkls_ops()
#]]]
