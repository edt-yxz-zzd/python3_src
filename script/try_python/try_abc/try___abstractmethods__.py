
from abc import *

class A(metaclass=ABCMeta):pass
print(A.__abstractmethods__)

A()

A.__abstractmethods__ = {'afaf'}

try:
    A()
    # TypeError: Can't instantiate abstract class A with abstract methods afaf
except TypeError: pass
else: raise ...

