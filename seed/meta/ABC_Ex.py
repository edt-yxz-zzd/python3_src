

__all__ = '''
    ABC_Ex
    '''.split()

from abc import ABCMeta, abstractmethod
class ABCMeta_Ex(ABCMeta): # not metaclass=ABCMeta
    # allow cls to define __instancecheck__/__subclasscheck__
    def __instancecheck__(cls, instance):
        return (super().__instancecheck__(cls, instance)
            or  cls._instancecheck_(instance)
            )
    def __subclasscheck__(cls, subclass):
        return (super().__subclasscheck__(cls, subclass)
            or  cls._subclasscheck_(subclass)
            )

class ABC_Ex(metaclass=ABCMeta_Ex):
    @classmethod
    @abstractmethod
    def _instancecheck_(cls, instance): return False
    @classmethod
    @abstractmethod
    def _subclasscheck_(cls, subclass): return False

@abstractmethod
def __no_new__():pass
class NoNewABCMeta_Ex(ABCMeta_Ex): # not metaclass=ABCMeta
    def __new__(mcls, name, bases, namespace):
        namespace = dict(namespace)
        namespace['__new__'] = __no_new__
        super().__new__(mcls, name, bases, namespace)
class ObjABC_Ex(ABC_Ex, metaclass=NoNewABCMeta_Ex):
    # use subclass of ObjABC_Ex as object
    # e.g. nn_ns.Bijection.TypeVerifier
    pass


