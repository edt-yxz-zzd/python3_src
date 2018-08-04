
from abc import ABCMeta, abstractmethod
class Base(metaclass = ABCMeta):
    @abstractmethod
    def __hash__(self):pass
    def __eq__(self, other):
        return self is other

class C(Base):
    def __eq__(self, other):
        return self is other
class D(Base):pass
C() # OK, why?
D()
# TypeError: Can't instantiate abstract class D with abstract methods __hash__

