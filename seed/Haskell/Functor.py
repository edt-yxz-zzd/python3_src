

from abc import ABCMeta, abstractmethod
from .PreludeBase import curry

class Functor(metaclass=ABCMeta):
    @abstractmethod
    def fmapF(self, a2b):
        # fmapF :: f a -> (a->b) -> f b
        raise NotImplementedError

class FunctorWrapper(Functor):
    def __init__(self, obj, fmap):
        # fmap :: (a2b, f a) -> f b
        self.obj = obj
        self.fmap = fmap
    def fmapF(self, a2b):
        return self.fmap(a2b, self.obj)
functor_wrapper_for_container =\
    FunctorWrapper(obj, lambda a2b, ls: type(ls)(map(a2b, ls)))
# table_type2FunctorWrapper :: Map type (f a -> (a->b) -> f b)
table_type2FunctorWrapper =\
    { list: functor_wrapper_for_container
    , tuple: functor_wrapper_for_container
    }
def get_fmap(fa):
    # g = fa.fmap
    g = getattr(fa, 'fmap', None)
    if g is None:
        g_ = table_type2FunctorWrapper.get(type(fa))
        if g_ is None:
            raise TypeError('not Functor')
        return g_(fa)
    return g
def fmap(a2b, fa):
    g = get_fmap(fa) # == fa.fmap
    return g(a2b)

fmap_ = curry(fmap)




