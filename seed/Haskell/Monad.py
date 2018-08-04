
from seed.helper.repr_input import repr_helper
from abc import ABCMeta, abstractmethod
from .PreludeBase import const, from_LinkedList_to_list
from itertools import chain
from operator import __irshift__, irshift

class Monad(metaclass=ABCMeta):
    # >>
    def __rshift__(self, other):
        # should type(self) == type(other)??
        self >>= lambda _cls, _: other
        return self
        raise NotImplementedError
    # >>=
    @abstractmethod
    def __irshift__(self, cls_a2other):
        # cls_a2other(cls, a) -> m b
        raise NotImplementedError
    # since not allow:
    #   "return self >>= cls_a2other" and "lambda xx: self>>=..."
    #   now, we have "return self ** cls_a2other"
    #       but no "self ** lambda ..."
    def __pow__(self, cls_a2other):
        return irshift(cls_a2other)


    @classmethod
    @abstractmethod
    def returnM(cls, a):
        raise NotImplementedError
        return cls.return_M()(a)
    def return_M(cls):
        # "_" means missing one arg
        return lambda a: cls.returnM(a)
        raise NotImplementedError
    @classmethod
    def failM(cls, errmsg:str):
        raise Exception(errmsg)
    def __mul__(self, other):
        # m a -> m b -> m (a,b)
        self >>= lambda _, a:\
                irshift(other, lambda cls, b: cls.returnM((a,b)))
                #other ** lambda cls, b: cls.returnM((a,b))
                #other >>= lambda cls, b: cls.returnM((a,b))

        return self

    @classmethod
    def voidM(cls):
        return cls.returnM(())
    def unlessM(self, b, must = None):
        # bool -> m a -> m b -> m b
        return self.whenM(not b, must)
    def whenM(self, b, must = None):
        # bool -> m a -> m b -> m b
        cls = type(self)
        must = cls.voidM if must is None else must
        return self >> must if b else must
    def execM(self, other):
        # m a -> m b -> m a
        # (>><)
        self >>= lambda cls, a: other >> cls.returnM(a)
        return self


def from_LinkedList_to_listM(cls, linked):
    return cls.returnM(from_LinkedList_to_list(linked))



class MonadError(Monad):
    @classmethod
    @abstractmethod
    def throwM(cls, err):
        # throwM :: (?cls) => err -> m a
        raise NotImplementedError

    @abstractmethod
    def catchM(self, cls_err2other):
        # catchM :: (?cls) => m a -> (error -> m a) -> m a
        # cls_err2other :: (cls, err) -> m a
        raise NotImplementedError


class Container2Monad(Monad):
    @classmethod
    @abstractmethod
    def getContainerType(cls):
        raise NotImplementedError
    @classmethod
    def from_iterable(cls, iterable)->'cls':
        return cls(cls._from_iterable(iterable))
    @classmethod
    def _from_iterable(cls, iterable)->'underlying container type':
        return cls.getContainerType()(iterable)
    '''
    def __init__(self, iterable):
        self.__obj = self._from_iterable(iterable)
    '''
    def __init__(self, container):
        # print(container, type(self).getContainerType())
        assert isinstance(container, type(self).getContainerType())
        self.__obj = container
    def __irshift__(self, cls_a2other):
        cls = type(self)
        def f(a):
            return cls_a2other(cls, a)
        it = map(f, self.__obj) # [m b]
        return cls.from_iterable(chain.from_iterable(it))
    @classmethod
    def returnM(cls, a):
        return cls.from_iterable([a])
    def __iter__(self):
        return iter(self.__obj)
    def __repr__(self):
        return repr_helper(self, self.__obj)

class List2Monad(Container2Monad):
    @classmethod
    def getContainerType(cls):
        return list

assert isinstance([], list)
m = List2Monad(list(range(5)))
m >>= lambda cls, b: cls.returnM(b)
print(m)





