r'''
seed.iters.cmp4iterable
from seed.iters.cmp4iterable import eq4iterable, cmp4iterable, lt4iterable, le4iterable
from seed.iters.cmp4iterable import cmp4iterable__lt, lt4iterable__lt

#'''

__all__ = '''
    eq4iterable
    cmp4iterable
        cmp4iterable__lt
        lt4iterable
            lt4iterable__lt
            le4iterable

    '''.split()

from seed.tiny import echo, neg_flip
import operator
from seed.func_tools.cmp import std_cmp, le2lt, lt2le, lt2eq, lt2cmp, cmp2lt, cmp2eq, cmp2le

def eq4iterable(lhs_iterable, rhs_iterable, /, *, lhs_key=None, rhs_key=None, key=None, __eq__=None):
    'Iter a -> Iter b -> (lhs_key::a->x) -> (rhs_key::b->y) -> (key::((x->u)|(y->v))) -> (__eq__::u->v->bool).-> bool'
    lhs_iterable = iter(lhs_iterable)
    rhs_iterable = iter(rhs_iterable)
    if lhs_key is None:
        lhs_key = echo
    if rhs_key is None:
        rhs_key = echo
    if key is None:
        key = echo
    if __eq__ is None:
        __eq__ = operator.__eq__
    for x in lhs_iterable:
        try:
            y = next(rhs_iterable)
        except StopIteration:
            return False
        x = key(lhs_key(x))
        y = key(rhs_key(y))

        if not __eq__(x, y):
            return False
    else:
        try:
            next(rhs_iterable)
        except StopIteration:
            return True
        else:
            return False



def cmp4iterable__lt(lhs_iterable, rhs_iterable, /, *, lhs_key=None, rhs_key=None, key=None, __lt__=None):
    'Iter a -> Iter b -> (lhs_key::a->x) -> (rhs_key::b->y) -> (key::((x->k)|(y->k))) -> (__lt__::k->k->bool).-> [-1..+1] #(-1|0|+1) #(<|==|>)#(before|same|after)'
    __cmp__ = lt2cmp(__lt__)
    return cmp4iterable(lhs_iterable, rhs_iterable, lhs_key=lhs_key, rhs_key=rhs_key, key=key, __cmp__=__cmp__)

def cmp4iterable(lhs_iterable, rhs_iterable, /, *, lhs_key=None, rhs_key=None, key=None, __cmp__=None):
    'Iter a -> Iter b -> (lhs_key::a->x) -> (rhs_key::b->y) -> (key::((x->u)|(y->v))) -> (__cmp__::u->v->[-1..+1]).-> [-1..+1] #(-1|0|+1) #(<|==|>)#(before|same|after)'
    lhs_iterable = iter(lhs_iterable)
    rhs_iterable = iter(rhs_iterable)
    if lhs_key is None:
        lhs_key = echo
    if rhs_key is None:
        rhs_key = echo
    if key is None:
        key = echo
    if __cmp__ is None:
        __cmp__ = std_cmp
    for x in lhs_iterable:
        try:
            y = next(rhs_iterable)
        except StopIteration:
            # [x] > []
            return +1
        x = key(lhs_key(x))
        y = key(rhs_key(y))

        r = __cmp__(x, y)
        if r:
            if r < 0:
                # x < y
                return -1
            else:
                # x > y
                return +1
        # x == y
    else:
        try:
            next(rhs_iterable)
        except StopIteration:
            # [].== []
            return 0
        else:
            # [] < [y]
            return -1

def lt4iterable__lt(lhs_iterable, rhs_iterable, /, *, lhs_key=None, rhs_key=None, key=None, __lt__=None):
    'Iter a -> Iter b -> (lhs_key::a->x) -> (rhs_key::b->y) -> (key::((x->k)|(y->k))) -> (__lt__::k->k->bool).-> bool'
    __cmp__ = lt2cmp(__lt__)
    return lt4iterable(lhs_iterable, rhs_iterable, lhs_key=lhs_key, rhs_key=rhs_key, key=key, __cmp__=__cmp__)

def lt4iterable(lhs_iterable, rhs_iterable, /, *, lhs_key=None, rhs_key=None, key=None, __cmp__=None):
    'Iter a -> Iter b -> (lhs_key::a->x) -> (rhs_key::b->y) -> (key::((x->u)|(y->v))) -> (__cmp__::u->v->[-1..+1]).-> bool'
    def cmp(lhs_iterable, rhs_iterable):
        return cmp4iterable(lhs_iterable, rhs_iterable, lhs_key=lhs_key, rhs_key=rhs_key, key=key, __cmp__=__cmp__)
    lt = cmp2lt(cmp)
    return lt(lhs_iterable, rhs_iterable)

def le4iterable(lhs_iterable, rhs_iterable, /, *, lhs_key=None, rhs_key=None, key=None, __cmp__=None):
    'Iter a -> Iter b -> (lhs_key::a->x) -> (rhs_key::b->y) -> (key::((x->u)|(y->v))) -> (__cmp__::u->v->[-1..+1]).-> bool # x <= y <==> not x > y <==> not y < x'
    def cmp(lhs_iterable, rhs_iterable):
        return cmp4iterable(lhs_iterable, rhs_iterable, lhs_key=lhs_key, rhs_key=rhs_key, key=key, __cmp__=__cmp__)
    le = cmp2le(cmp)
    return le(lhs_iterable, rhs_iterable)
    # !!!flip!!!
    return not lt4iterable(rhs_iterable, lhs_iterable, lhs_key=rhs_key, rhs_key=lhs_key, key=key, __cmp__=neg_flip(__cmp__))


