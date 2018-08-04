'''
to hold tokens:
    rex"[...]" and rex"[^...]"

'''


from abc import ABCMeta, abstractmethod
import operator
from functools import reduce, total_ordering
#from itertools import chain

@total_ordering
class NegAbleSetABC(metaclass=ABCMeta):
    '''immutable set;
not require __hash__, __len__, __iter__

using this class in regex to use below methods strictly.
# e is element|token; a,b are sets.
~a
a&b
e in a
a == b
cls.from_iterable(iterable) # make a set
a.nsize
    if None ==>> N/A (i.e. some enumerate set)
    if >= 0 ==>> pos set with size nsize
    if < 0 ==>> neg set with size -nsize-1
    

############## auto ###############

a.size = a.nsize if int >=0 other None
    # return size or None if not available (i.e. a neg set)

a <= b ::= a&b == a
a < b :: not a == b and a <= b
a/b=(assert b <= a); a&~b
a//b = a/(a&b)
a|b = ~(~a&~b)
a^b = (a|b) - (a&b) = (a//b)|(b//a) = (a/(a&b))|(b/(a&b))

bool(a) ::= a != cls.empty_set()
not a = not bool(a)
a.is_empty() = not a
a.is_full() = not ~a
a.is_singleton() = a.size == 1
a.is_disjoint(b) = not (a&b)

cls.from_iterable_ex(iterable, neg) ::= s = cls.from_iterable(iterable); ~s if neg else s
cls.empty_set() = cls.from_iterable([])
cls.singleton_set(e) = cls.from_iterable([e])
cls.full_set() = ~cls.empty_set()
cls.union_(sets) = cls.empty_set().union(sets)
cls.interset_(sets) = cls.full_set().interset(sets)

a.union(sets) = reduce(operator.or_, sets, a)
a.interset(sets) = reduce(operator.and_, sets, a)
'''
    ############### basic ###################
    
    @abstractmethod
    def __invert__(self):
        raise NotImplementedError
    @abstractmethod
    def __contains__(self, elem):
        raise NotImplementedError
    @abstractmethod
    def __and__(self, other):
        raise NotImplementedError
    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError
    @classmethod
    @abstractmethod
    def from_iterable(cls, iterable):
        raise NotImplementedError
    @property
    @abstractmethod
    def nsize(self):
        raise NotImplementedError

        
    ####################### auto ###################
    
    @property
    def size(self):
        s = self.nsize
        if s is None or s < 0:
            return None
        return s
    
    def __le__(self, other):
        return (self & other) == self
    def __lt__(self, other):
        return not (self == other) and self <= other
    def __truediv__(self, other):
        if not other <= self:
            raise ValueError('not b <= a @a/b')
        return self & ~other
    def __floordiv__(self, other):
        return self / (self & other)
    def __or__(self, other):
        return ~(~self & ~other)
    def __xor__(self, other):
        common = self & other
        return (self/common) | (other/common)

    def __bool__(self):
        return not self == type(self).empty_set()
    def is_empty(self):
        return not self
    def is_full(self):
        return not ~self
    def is_singleton(self):
        return self.size == 1
    def is_disjoint(self, other):
        return not (self & other)
    @classmethod
    def from_iterable_ex(cls, iterable, neg):
        s = cls.from_iterable(iterable)
        return ~s if neg else s
    @classmethod
    def empty_set(cls):
        return cls.from_iterable([])
    @classmethod
    def full_set(cls):
        return ~cls.empty_set()
    @classmethod
    def singleton_set(cls, elem):
        return cls.from_iterable([elem])

    @staticmethod
    def union1(sets):
        sets = iter(sets)
        first = next(sets)
        return first.union(sets)
    @staticmethod
    def interset1(sets):
        sets = iter(sets)
        first = next(sets)
        return first.interset(sets)
    
    def union(self, sets):
        return reduce(operator.or_, sets, self)
    def interset(self, sets):
        return reduce(operator.and_, sets, self)
    @classmethod
    def union_(cls, sets):
        return cls.empty_set().union(sets)
    @classmethod
    def interset_(cls, sets):
        return cls.full_set().interset(sets)
    
class Set2NegAble(NegAbleSetABC):
    '''convert a normal set to NegAbleSet

py_set_obj requirements:
__contains__; __sub__; __and__; __eq__; __len__; type(...)(iterable)
'''
    def __init__(self, neg, py_set_obj):
        self.__neg = bool(neg)
        self.__set = py_set_obj

    def __check(self, other):
        if type(self) is not type(other):
            raise TypeError('type(self) is not type(other)')

    def __invert__(self):
        return type(self)(not self.__neg, self.__set)

    def __contains__(self, elem):
        return bool(elem in self.__set) ^ self.__neg

    def __and__(self, other):
        self.__check(other)
        n0, n1 = self.__neg, other.__neg
        s0, s1 = self.__set, other.__set
        n = False
        if n0:
            if n1:
                s = s0 | s1
                n = True
            else:
                # 0 neg; 1 pos
                s = s1 - s0
        else:
            if n1:
                # 0 pos; 1 neg
                s = s0 - s1
            else:
                s = s0 & s1
        return type(self)(n, s)
    
    def __eq__(self, other):
        self.__check(other)
        return self.__neg == other.__neg and self.__set == other.__set
    
    @classmethod
    def from_iterable(cls, iterable):
        return cls(False, type(self.__set)(iterable))
    @property
    def nsize(self):
        s = len(self.__set)
        return -s-1 if self.__neg else s


    
    
        
    
class _NegAbleSetWrapper(NegAbleSetABC):
    'using this class in regex to use below methods strictly.'
    def __init__(self, neg_able_set_obj):
        self.__set = neg_able_set_obj

    def __check(self, other):
        if type(self) is not type(other):
            raise TypeError('type(self) is not type(other)')

    ############### basic ###################
        
    def __invert__(self):
        return type(self)(~self.__set)
    def __contains__(self, elem):
        return elem in self.__set
    def __and__(self, other):
        self.__check(other)
        return type(self)(self.__set & other.__set)
    def __eq__(self, other):
        self.__check(other)
        return self.__set == other.__set
    @classmethod
    def from_iterable(cls, iterable):
        return cls(type(self.__set).from_iterable(iterable))
    @property
    def nsize(self):
        s = self.__set.nsize
        assert s is None or type(s) is int
        return s

    


