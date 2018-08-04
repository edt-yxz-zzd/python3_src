
'''
http://oeis.org/A181565
    A181565 a(n) = 3*2^n + 1
        4, 7, 13, 25, 49, 97, 193, 385, 769, 1537, 3073, 6145, 12289, 24577, 49153, 98305, 196609, 393217, 786433, 1572865, 3145729, 6291457, 12582913, 25165825, 50331649, 100663297, 201326593, 402653185, 805306369, 1610612737, 3221225473
    http://oeis.org/A004119/a004119.pdf
        Properties of the sequence 3.2^n+1
'''


def is_prime_of_3_2_pow2N_add1(N):
    # is_prime(3*2**(2*N)+1)
    # [N >= 1][M=3*2**(2*N)+1] ==>> [is_prime(M) <==> [3\MultiplicativeOrder(2, M)] <==> [2^(M-1) % M == 1][2^2^(2*N) % M != 1]]
    #if N < 1: return False
    M = 3*2**(2*N)+1
    return pow(2, M-1, M) == 1 and pow(2, 2**(2*N), M) != 1

for N in range(20):
    print(N, 3*2**(2*N)+1, is_prime_of_3_2_pow2N_add1(N))
for i in range(20):
    N = 2**i
    N2 = 2**(i+1)
    print(i+1, N2, 3*2**(2*N)+1, is_prime_of_3_2_pow2N_add1(N))
raise


from nn_ns.math_nn.numbers.prime_number import prime_number
from nn_ns.math_nn.factor_int import factor_int
L = 100
prime_number[L]
# min{i > 0 | 2**i % p == 1}
# MultiplicativeOrder[2, Prime[n]]
# http://oeis.org/A014664
ls = []
for i in range(1, L):
    p = prime_number[i]
    for i in range(1, p):
        if 2**i % p == 1:
            break
    else:
        raise logic-error
    ls.append((i, p))
print(ls)
print([i for i,p in ls])

