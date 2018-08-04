'''
given prime p,q [p!=q]
phi(p*q) = (p-1)(q-1)

[gcd(a, p*q)==1]:
    mod p*q: a**phi(p*q) == 1
        a**(i*phi(p*q) + 1) == 1
        let (mod phi(p*q)): P*S == 1
        (a**P)**S = a**(i*phi(p*q) + 1) == 1

let a in 0..p*q-1
choose P, s.t. gcd(P, phi(p*q)) == 1
let S = P^-1 mod phi(p*q)

public (P,p*q) to encode
using (S,p*q) to decode





'''

from collections import namedtuple
from fractions import gcd
from nn_ns.math_nn.integer.mod import invmod as mod_inv


class TransformByModPow(
    namedtuple('TransformByModPow_Base', 'exp, pq'.split(', '))):
    def __call__(self, a):
        assert 0 <= a < self.pq
        return pow(a, self.exp, self.pq)
    
class EncodeByModPow(
    namedtuple('EncodeByModPow_Base', 'p, q, pq, P, S'.split(', '))):
    def __new__(cls, p, q, P):
        if not (p > 0 and q > 0 and p!=q):
            raise ValueError
        pq = p*q
        M = (p-1)*(q-1)
        if not gcd(P, M) == 1:
            raise ValueError()

        P = P % M
        S = mod_inv(P, M)
        self = super(__class__, cls).__new__(cls, p, q, pq, P, S)
        return self

    def __repr__(self):
        return '{}{}'.format(__class__.__name__, (self.p, self.q, self.P))
    def encode(self, a):
        assert 0 <= a < self.pq
        return pow(a, self.P, self.pq)
    def decode(self, h):
        assert 0 <= h < self.pq
        return pow(h, self.S, self.pq)

    def get_encoder(self):
        return TransformByModPow(self.P, self.pq)

    def get_decoder(self):
        return TransformByModPow(self.S, self.pq)


if __name__ == '__main__':
    T = EncodeByModPow
    t = T(41, 11, 7)
    for i in range(t.pq):
        assert i == t.encode(t.decode(i))

















    
