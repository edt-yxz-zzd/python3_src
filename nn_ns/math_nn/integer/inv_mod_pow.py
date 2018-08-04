


r'''

problem:
    y = inv_mod_pow(x, B, k) ::=
        given x, gcd(x, B**k) == 1, B>=2, k>=1, find out y s.t. y*x % B**k == 1


assume we know ans when k==1
    since we can call invmod

assume x >= 2
    since:
        * if x < 0, y = -inv_mod_pow(-x, B, k)
        * x != 0
        * if x == 1, y == 1



x_digits = little_endian_digits_of(x, B)
inv_x' = invmod(x_digits[0], B)
power' = 1

while True:
    assert inv_x' * x % B**power' == 1
    assert inv_x' < B**power'
    inv_x := inv_x'

    # find out exact power
    product = inv_x * x
    product_digits = little_endian_digits_of(product)
    assert product_digits[0] == 1
    power = 1+count_head_0s(product_digits[1:])
    assert inv_x < B**power
    assert power >= power'
    if k <= power: return inv_x

    # q = digitsLE2uint(product_digits[power:]) # product >>= power (base B)
    q, r = divmod(product, B**power)
    assert r == 1
    assert q%B > 0
    # product = inv_x * x = q*B**power + 1

    s = (-q)%B**power
    assert s + q%B**power == B**power
    [mod B**(power*2)]:
        inv_x * x =-= q%B**power * B**power + 1
                        == (B**power - s) * B**power + 1
                        == B**(power*2) - s*B**power + 1
                  =-= -s*B**power + 1
        inv_x * x * B**power =-= (-s*B**power + 1) * B**power
                             =-= -s*B**(power*2) + B**power
                             =-= B**power
        s*(inv_x * x * B**power) =-= s*B**power
        inv_x * x + s*(inv_x * x * B**power) =-= 1
        (1 + s*B**power) * inv_x * x =-= 1
        ((1 + s*B**power) * inv_x) * x =-= 1

    power' = power*2
    inv_x' = ((1 + s*B**power) * inv_x) % B**power'



'''


__all__ = ['InvModPow']


from nn_ns.math_nn.integer.mod import invmod
class InvModPow:
    r'''inv_mod_pow<B>(x, k) * x % B**k == 1


example:
    >>> This = InvModPow
    >>> inv_mod_pow = This(2)
    >>> inv_mod_pow(1, 1)
    1
    >>> inv_mod_pow(1, 2)
    1
    >>> inv_mod_pow(1, 3)
    1
    >>> inv_mod_pow(3, 1)
    1
    >>> inv_mod_pow(3, 2)
    3
    >>> inv_mod_pow(3, 3)
    3
    >>> inv_mod_pow(3, 4)
    11
    >>> inv_mod_pow(3, 5)
    11
    >>> inv_mod_pow(3, 6)
    43

    >>> inv_mod_pow = This(12)
    >>> inv_mod_pow(1, 1)
    1
    >>> inv_mod_pow(1, 2)
    1
    >>> inv_mod_pow(1, 3)
    1
    >>> inv_mod_pow(5, 1)
    5
    >>> inv_mod_pow(5, 2)
    29
    >>> inv_mod_pow(5, 3)
    1037
    >>> inv_mod_pow(5, 4)
    16589
    >>> inv_mod_pow(5, 5)
    99533
    >>> inv_mod_pow(5, 6)
    597197



    >>> inv_mod_pow(-1, 1)
    11
    >>> inv_mod_pow(-1, 2)
    143



'''
    def __init__(self, base):
        if not (base >= 2): raise ValueError
        self.base = base
    def inv_mod_base(self, x):
        # gcd(x, base) == 1
        # -> inv_x
        # inv_x * x % base == 1
        # 1 <= inv_x < base
        assert 0 <= x < self.base
        return invmod(x, self.base)
        raise NotImplementedError

    def __call__(self, x, k):
        return self.inv_mod_pow(x, k)
    def inv_mod_pow(self, x, k):
        # gcd(x, base) == 1
        # -> inv_x
        # inv_x * x % base**k == 1
        # 1 <= inv_x < base**k
        if not (k >= 1): raise ValueError
        if x == 0: raise ValueError

        inv_x, M = self.__inv_mod_pow(x, k)
        assert inv_x * x % M == 1
        assert 1 <= inv_x < M
        return inv_x
    def __inv_mod_pow(self, x, k):
        if x < 0:
            inv_x, M = self.__inv_mod_pow(-x, k)
            inv_x = M - inv_x
        else:
            M = self.base**k
            x %= M
            if x == 1:
                inv_x = 1
            else:
                for power, inv_x in self.iter_inv_mod_pow(x):
                    if k <= power:
                        break
                inv_x %= M
            pass
        return inv_x, M

    def iter_inv_mod_pow(self, x):
        # gcd(x, base) == 1
        # x > 1
        # -> Iter (power, inv_x)
        # inv_x * x % base**power == 1
        # inv_x * x % base**(power+1) > 1
        # power strictly increase

        if not (x > 1): raise ValueError
        B = self.base
        inv_x_ = self.inv_mod_base(x%B)
        power_ = 1
        B_power_ = B**power_

        while True:
            #assert inv_x_ * x % B_power_ == 1
            product = inv_x_ * x
            q, r = divmod(product, B_power_)
            assert q != 0 # since x > 1
            assert r == 1
            assert inv_x_ < B_power_
            inv_x = inv_x_

            # find out exact power
            i = 0
            while True:
                # assert q > 0
                _q, r = divmod(q, B)
                # assert 0 <= _q < q
                if r: break
                i += 1
                q = _q
            power = power_ + i

            #B_power = B**power
            B_power = B_power_ * B**i
            assert product == q*B_power + 1
            assert 0 <= inv_x < B_power
            assert power >= power_
            yield power, inv_x

            s = (-q)%B_power
            power_ = power*2
            #B_power_ = B**power_
            B_power_ = B_power**2
            inv_x_ = ((1 + s*B_power) * inv_x) % B_power_



if __name__ == "__main__":
    import doctest
    doctest.testmod()









