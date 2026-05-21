#__all__:goto
r'''[[[
e ../../python3_src/seed/math/primality_test/errors.py

seed.math.primality_test.errors
py -m nn_ns.app.debug_cmd   seed.math.primality_test.errors -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.primality_test.errors:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.primality_test.errors   @f

]]]'''#'''
__all__ = r'''
Error
    IsPrimeError
    IsStrongProbablePrimeError
    PrimalityUndeterminedError
        OverflowError__Miller_Rabin_primality_test__A014233
        Bool5TriboolFail__probably_prime
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

class Error(Exception):pass
class IsPrimeError(Error):pass
class IsStrongProbablePrimeError(Error):pass
class PrimalityUndeterminedError(Error):pass
class OverflowError__Miller_Rabin_primality_test__A014233(PrimalityUndeterminedError):pass
class Bool5TriboolFail__probably_prime(PrimalityUndeterminedError):pass
    #used by: view ../../python3_src/seed/math/prime_gens__7objs.py


__all__
from seed.math.primality_test.errors import Error, IsPrimeError, IsStrongProbablePrimeError, PrimalityUndeterminedError, OverflowError__Miller_Rabin_primality_test__A014233, Bool5TriboolFail__probably_prime
from seed.math.primality_test.errors import *
