#__all__:goto
r'''[[[
e ../../python3_src/seed/math/is_complete_factorization_of__ft2e_.py


seed.math.is_complete_factorization_of__ft2e_
py -m nn_ns.app.debug_cmd   seed.math.is_complete_factorization_of__ft2e_ -x
py -m nn_ns.app.doctest_cmd seed.math.is_complete_factorization_of__ft2e_:__doc__ -ht
py_adhoc_call   seed.math.is_complete_factorization_of__ft2e_   @f
from seed.math.is_complete_factorization_of__ft2e_ import *
#]]]'''
__all__ = r'''
is_complete_factorization_of__ft2e_
    check_complete_factorization_of__ft2e_
'''.split()#'''
__all__




from seed.tiny_.check_container import is_mapping, check_mapping
from seed.math.II import II__ft2e_

def check_complete_factorization_of__ft2e_(N, ft2e4N, /):
    'not required:primality'
    if not is_complete_factorization_of__ft2e_(N, ft2e4N):raise ValueError(N, ft2e4N)
def is_complete_factorization_of__ft2e_(N, ft2e4N, /):
    'not required:primality'
    check_mapping(ft2e4N)
    return all((ft >= 2 and (ft&1 == 1 or ft == 2) and e >= 1) for ft, e in ft2e4N.items()) and II__ft2e_(ft2e4N) == N


__all__
from seed.math.is_complete_factorization_of__ft2e_ import is_complete_factorization_of__ft2e_, check_complete_factorization_of__ft2e_
from seed.math.is_complete_factorization_of__ft2e_ import *
