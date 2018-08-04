

'''
X[i+1] = f(X[i]), for i >= 0
given X[0], calc X[n] or X[0..n]
'''
__all__ = ''' '''.split()
from itertools import chain
from abc import ABCMeta, abstractmethod, ABC
from .View import SeqView

class IRecurCollect(ABC):
    @abstractmethod
    def push(self, x):pass
    @abstractmethod
    def top(self):pass
class IRecurCollectSeq(IRecurCollect):
    @abstractmethod
    def seq(self):pass
class IRecurCollectView(IRecurCollectSeq):
    @abstractmethod
    def seq_view(self):pass
    def seq(self):
        return list(self.seq_view())

class RecurCollect1(IRecurCollect):
    def __init__(self, x):
        self.__object = x
    def push(self, x):
        self.__object = x
    def top(self):
        return self.__object
    pass
class RecurCollectN(IRecurCollectSeq):
    # bug: def seq_view(self): return SeqView(self.__xs)
    def seq(self):
        ls = self.__xs
        i = self.__last_idx + 1
        if i == len(xs):
            return list(ls)
        return ls[i:] + ls[:i]
    def __init__(self, n, xs):
        n = n.__index__()
        xs = iter(xs)
        if n < 1: raise ValueError('n<=0')
        self.__n = n
        self.__xs = []
        for x in xs:
            self.__xs.append(x)
            break
        else: raise ValueError('len(xs) == 0')

        self.__last_idx = 0

        for x in xs: self.push(x)
    def top(self):
        return self.__xs[self.__last_idx]
    def push(self, x):
        if len(self.__xs) < self.__n:
            self.__xs.append(x)
            self.__last_idx += 1
        else:
            # assert len(self.__xs) == self.__n >= 1
            # assert 0 <= self.__last_idx < self.__n
            i = self.__last_idx + 1
            if i == self.__n: i = 0
            self.__last_idx = i
            self.__xs[i] = x

class RecurCollectOO(IRecurCollectSeq):
    def seq_view(self): return SeqView(self.__xs)
    def __init__(self, xs):
        self.__xs = list(xs)
        if not self.__xs: raise ValueError('len(xs) == 0')
    def top(self):
        return self.__xs[-1]
    def push(self, x):
        return self.__xs.append(x)

def RecurCollect(n):
    if n is None:
        return RecurCollectOO
    if n == 1:
        return lambda xs: RecurCollect1(*xs)
    return lambda xs: RecurCollectN(n, xs)



