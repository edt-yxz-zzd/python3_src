
import hashlib
m1 = hashlib.sha512()
m2 = hashlib.sha512()
assert m1 is not m2
assert m1.digest_size == 64 == 512//8

bs1 = b'a'
bs2 = b'afsfsgdg'

m1.update(bs1+bs2)
d1 = m1.digest()

m2.update(bs1)
m2.digest() # what if digest() between updates? conclusion no effect
m2.update(bs2)
d2 = m2.digest()

assert d1 == d2

