#__all__:goto
r'''[[[
e ../../python3_src/seed/math/log.py

seed.math.log
py -m nn_ns.app.debug_cmd   seed.math.log -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.log:__doc__ -ht # -ff -df
py_adhoc_call   seed.math.log   @f
#]]]'''
__all__ = r'''

    log_
    ln_
    lb_

    e
    log
    log10
    log1p
    log2
    exp
    exp2
    expm1
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...
from math import e, log, log10, log1p, log2, exp, exp2, expm1

def log_(base, x, /):
    'base -> x -> log<base>(x)'
    return log(x, base)

def ln_(x, /):
    'x -> log<e>(x)'
    return log(x)

def lb_(x, /):
    'x -> log<2>(x)'
    return log2(x)
#lg_ = lb_
#   log2 or log10

__all__
from seed.math.log import log_, ln_, lb_
from seed.math.log import e, log, log10, log1p, log2, exp, exp2, expm1
from seed.math.log import *
