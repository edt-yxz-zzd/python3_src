#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/least_positive_primitive_root_of_prime.py
view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
both:
    * least_positive_primitive_root_of_prime
        may be composite
    * least_positive_prime_primitive_root_of_prime
        * least_positive_prime_primitive_root_of_prime__except_1_for_2
        * least_positive_prime_primitive_root_of_prime__force_3_for_2

nn_ns.math_nn.numbers.least_positive_primitive_root_of_prime
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.least_positive_primitive_root_of_prime -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.least_positive_primitive_root_of_prime:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   nn_ns.math_nn.numbers.least_positive_primitive_root_of_prime   @f

]]]'''#'''
__all__ = r'''
j2prime
    j2min_primitive_root
    j2min_prime_primitive_root__head_eq_1
    j2min_prime_primitive_root__head_eq_3

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

___end_mark_of_excluded_global_names__0___ = ...

def _load():
    from seed.pkg_tools.load_resource import read_under_pkg_
    txt = read_under_pkg_(__package__, '_patch_prime_..b001918.b002233.out.txt', xencoding='u8')
    lines = txt.strip().split('\n')
    assert len(lines) == 10**4
    assert lines[0] == '0 2 1 1'
    assert lines[-1] is lines[9999] == '9999 104729 12 23'
    ts = [tuple(map(int, line.split())) for line in lines]
    assert len(ts) == 10**4
    assert ts[0] == (0, 2, 1, 1)
    assert ts[-1] is ts[9999] == (9999, 104729, 12, 23)
    return ts
def _load_then_transpose():
    ts = _load()
    sz = len(ts)
    i2ls = [tuple(tpl[i] for tpl in ts) for i in range(4)]
    (j2j, j2prime, j2min_g, j2min_prime_g__1a2) = i2ls
    assert j2j == tuple(range(10**4))
    del j2j
    j2min_prime_g__3a2 = (3,)+j2min_prime_g__1a2[1:]
    assert len(j2min_prime_g__3a2) == len(j2min_prime_g__1a2)
    return (j2prime, j2min_g, j2min_prime_g__1a2, j2min_prime_g__3a2)
(j2prime, j2min_primitive_root, j2min_prime_primitive_root__head_eq_1, j2min_prime_primitive_root__head_eq_3) = _load_then_transpose()

__all__
from nn_ns.math_nn.numbers.least_positive_primitive_root_of_prime import j2prime, j2min_primitive_root, j2min_prime_primitive_root__head_eq_1, j2min_prime_primitive_root__head_eq_3
from nn_ns.math_nn.numbers.least_positive_primitive_root_of_prime import *
