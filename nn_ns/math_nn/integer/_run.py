from nn_ns.math_nn.integer.CertificatedPrime__using_sympy import *

p211 = make_certificated_prime(211)
print(p211, repr(p211))

print(make_certificated_prime(203))
assert factor_int(203) == {29: 1, 7: 1}
