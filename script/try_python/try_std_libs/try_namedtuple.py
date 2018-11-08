
from collections import namedtuple
A = namedtuple('A', ['a'])
B = namedtuple('B', ['b'])
a = A(0)
b = B(0)
assert hash(a) == hash(b)
assert a == b

# when use as key, be replaced!!!
