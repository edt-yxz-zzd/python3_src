
from typing import TypeVar, Generic, Callable, Any, Sequence, Tuple, Union
from abc import ABC, abstractmethod

R = TypeVar('R')
R2 = TypeVar('R2')
M = TypeVar('M')
E = TypeVar('E')
'''
class IMonad(Generic[M,R], ABC):pass
    # error: Name 'IMonad' already defined
    # why? i just to forward reference
'''

#IM = 'IMonad[M,R]'

# Void = Tuple[] # error: invalid syntax
# Void = () # Invalid type "Monad.Void"
# Void = Tuple() # error: "_SpecialForm" not callable
# Void = Tuple[...] # Unexpected '...'
Void = None
Single = Tuple[R]
# Maybe = Union[Void, Single] # Void = None; Invalid type "Monad.Void"???
Maybe = Union[None, Single] # if may: ... else [x]=may
# HList = Union[Void, Tuple[R, 'HList']] # Monad.py:21: error: Recursive types not fully supported yet, nested types replaced with "Any"

class IMonad(ABC, Generic[M,R]):
    @classmethod
    @abstractmethod
    def returnM(cls, r:R2) -> 'IMonad[M,R2]':
        pass
    @abstractmethod
    def feedM(self, f:Callable[[R], 'IMonad[M,R2]']) -> 'IMonad[M,R2]':
        # >>=
        pass

    @classmethod
    @abstractmethod
    def failM(cls, s:str) -> 'IMonad[M,Any]':
        pass

'''
    @classmethod
    @abstractmethod
    def seqM(cls, ma_ls : Sequence[IMonad[M,R]], *, __i=0) -> IMonad[M, Sequence[R]]:
        if __i < len(ma_ls):
            ma = ma_ls[__i]
            m_ls = cls.seqM(ma_ls, __i=__i+1)
            return 
        return cls.returnM([])
        if 
'''


IM = IMonad[M,R]
IMC_Any = 'IMonadCatch[M,Any,E]'
IMC_R = 'IMonadCatch[M,R,E]' # error: Invalid type "Monad.IMC_R"

class IMonadCatch(IM, Generic[M,E,R]):
    @classmethod
    @abstractmethod
    def raiseM(cls, e:E) -> 'IMonadCatch[M,E,Any]':
        pass
    @abstractmethod
    def catchM(self, e:Callable[[E], 'IMonadCatch[M,R,E]']) -> 'IMonadCatch[M,E,R]':
        pass





