

'''

op
    array, tuple/pair, choice/either, record, union

    # why use '+'??
    #   so, we can repr this expression without '()'
    x[min,max] == fmap x

    TV.tupleTV(*args) # arg can tuple
    +(x * y * z) == (x,y,z)
    +(x * ...) == (x,)

    TV.RecordTV(**kwargs)
    TV.ChoiceTV(**kwargs)
    +(x | y | z) == {0:x, 1:y, 2:z} # 0 == '0'
    +(x | ...) == {0:x}
    TV.EitherTV(x, y) # x, y can be pair
    +(x / y) == {left:x, right:y}

    TV.UnionTV(*args)
    +(x + y + z) == union(x, y, z)

    +       -       *       **      /       //      %      @
    <<      >>      &       |       ^       ~
    <       >       <=      >=      ==      !=

'''

__all__ = '''
    TypeVerifier

    TupleTV
    RecordTV
    ChoiceTV
    EitherTV
    UnionTV
    '''.split()
from .IRepr import IRepr
from abc import ABCMeta, abstractmethod
from itertools import count



'''
class (TypeVerifier):
    make_args_kwargs
    make_name_args_kwargs
    def get_construct_info(self):
    def get_TypeSpec(self):

    def get_TypeName(self):
    def has_instance(self, obj):
    def iter_examples(self):
    def untypechecked_equal(self, lhs, rhs):
    def __eq__(self, other):
'''

def is_uint(obj):
    return type(obj) is int and obj >= 0
def is_may_uint(obj):
    return obj is None or is_uint(obj)


pos_inf = float('inf')

class TypeVerifier(IRepr):
    # immutable and hashable

    '''
    def __str__(self):
        return self.get_TypeName()
    def __repr__(self):
        return '<{!s}>'.format(self.get_TypeName())
    '''

    @abstractmethod
    def __hash__(self):pass

    @abstractmethod
    def get_TypeName(self):
        # () -> str
        pass
    @abstractmethod
    def get_TypeSpec(self):
        # () -> str
        # shorter than get_TypeName
        # '[a]{m<=len(.)<=M}' vs '[a]{m..M}' and '[a]{m..}' and '[a]{L}'
        pass


    # (obj) -> bool
    @abstractmethod
    def has_instance(self, obj):pass

    # () -> Iter obj
    @abstractmethod
    def iter_examples(self):pass

    # (lhs, rhs) -> bool
    # compare Instance
    def untypechecked_equal(self, lhs, rhs):
        # to be overrided
        return lhs == rhs

    # compare Type
    def __eq__(self, other):
        # to be overrided
        return self is other
    def __ne__(self, other):
        return not (self == other)


    @property
    def idBJ(self):
        from .IdBijection import id_of
        return id_of(self)


    def typechecked_equal(self, lhs, rhs):
        # (lhs, rhs) -> bool or TypeError
        assert self.has_instance(lhs), TypeError
        assert self.has_instance(rhs), TypeError
        return self.untypechecked_equal(lhs, rhs)

    def get_the_single_elem(self):
        # if not is_singletonTV() raise TypeError
        if not self.is_singletonTV(): raise TypeError
        it = self.iter_examples()
        for THE in it:
            break
        else:
            raise TypeError('is_singletonTV() but no elem in iter_examples()')
        for _ in it:
            raise TypeError('is_singletonTV() but more than one elem in iter_examples()')
        return THE

    def is_singletonTV(self):
        # True if has one and only one instance
        # [the_elem] == list(self.iter_examples())
        return self.case_num_instances() == 1
        return False
    def is_emptyTV(self):
        # True if has no instance
        # [] == list(self.iter_examples())
        return self.case_num_instances() == 0
        return False
    def case_num_instances(self):
        # inf, 0, 1 ==>> more than 1 or unknown, only 1, none
        # to be overrided
        return pos_inf
        return (1 if self.is_singletonTV() else
                0 if self.is_emptyTV() else pos_inf)
    @staticmethod
    def _singleton_empty2case(is_singleton, is_empty):
        return 1 if is_singleton else 0 if is_empty else pos_inf



    ###################### op ####################


    def __getitem__(self, key):
        # x[min,max] == [x]{min..max}
        # x[L] == [x]{L..L}
        # x[min,None] == [x]{min..}
        # key is uint or (uint, may_uint)
        if type(key) is int:
            raise TypeError
            assert is_uint(key)
            min, max = key, key
        elif type(key) is tuple:
            assert len(key) == 2
            min, max = key
            assert is_uint(min)
            assert is_may_uint(max)
            assert max is None or min <= max
        else:
            raise TypeError
        from .ArrayTV import ArrayTV
        return ArrayTV(self, min, max)

    def tuple_withTV(self, *args):
        return self.TupleTV(self, *args)
    @staticmethod
    def TupleTV(*args):
        # arg can be nested tuple and TV
        def this_func(args):
            return tupleTV(map(f, args))
        def f(arg):
            # arg is TV or tuple
            # TV or tuple to TV
            if type(arg) == tuple:
                return this_func(arg)
            return arg
        from .TupleTV import tupleTV
        return this_func(args)
    def __mul__(self, other):
        # +(x * y * z) == (x,y,z)
        # +(x * ...) == (x,)
        return TupleHelper(self, other)

    def record_withTV(self, tag, **kwargs):
        assert tag not in kwargs
        kwargs[tag] = self
        return self.RecordTV(**kwargs)
    @staticmethod
    def RecordTV(**kwargs):
        from .RecordTV import RecordTV
        return RecordTV(**kwargs)
    def choice_withTV(self, tag, **kwargs):
        assert tag not in kwargs
        kwargs[tag] = self
        return self.ChoiceTV(**kwargs)
    @staticmethod
    def ChoiceTV(**kwargs):
        from .ChoiceTV import ChoiceTV
        return ChoiceTV(**kwargs)
    def __or__(self, other):
        # +(x | y | z) == {0:x, 1:y, 2:z} # 0 == '0'
        # +(x | ...) == {0:x}
        return ChoiceHelper(self, other)

    def either_withTV(self, rightTV):
        return self.EitherTV(self, rightTV)
    @staticmethod
    def EitherTV(leftTV, rightTV):
        # leftTV, rightTV can be nested pair or TV
        def this_func(x, y):
            x,y = f(x), f(y)
            return make_eitherTV(x, y)
        def f(arg):
            # arg is TV or tuple
            # TV or tuple to TV
            if type(arg) == tuple:
                assert len(arg) == 2
                return this_func(*arg)
            return arg
        from .ChoiceTV import make_eitherTV
        return this_func(leftTV, rightTV)
    def __truediv__(self, other):
        # +(x / y) == {left:x, right:y}
        return EitherHelper(self, other)

    def union_withTV(self, *args):
        return self.UnionTV(self, *args)
    @staticmethod
    def UnionTV(*args):
        from .UnionTV import UnionTV
        return UnionTV(*args)
    def __add__(self, other):
        # +(x + y + z) == union(x, y, z)
        return UnionHelper(self, other)





TupleTV = TypeVerifier.TupleTV
RecordTV = TypeVerifier.RecordTV
ChoiceTV = TypeVerifier.ChoiceTV
EitherTV = TypeVerifier.EitherTV
UnionTV = TypeVerifier.UnionTV






'''
/ArrayTV ArrayTV
/TupleTV tupleTV
/RecordTV RecordTV
/ChoiceTV make_eitherTV
/UnionTV UnionTV unionTV
TupleHelper
ChoiceHelper
EitherHelper
UnionHelper
'''
count
def enumStrInt(begin=0):
    return map(str, count(begin))
class Helper(metaclass=ABCMeta):
    @abstractmethod
    def __pos__(self):pass
class EitherHelper(Helper):
    # +(x / y)
    def __init__(self, lhsTV, rhsTV):
        assert isinstance(lhsTV, TypeVerifier)
        assert isinstance(rhsTV, TypeVerifier)
        self.lhsTV = lhsTV
        self.rhsTV = rhsTV
        from .ChoiceTV import make_eitherTV
        self.EitherTV = make_eitherTV(lhsTV, rhsTV)
    def __pos__(self):
        return self.EitherTV

class ManyOpHelper(Helper):
    # + | * >>
    def __init__(self, TV_or_This, TV_or_Dot3):
        cls = type(self)
        assert type(TV_or_This) == cls or isinstance(TV_or_This, TypeVerifier)
        assert isinstance(TV_or_Dot3, TypeVerifier) or TV_or_Dot3 is ...
        self.fst = TV_or_This
        self.snd = TV_or_Dot3
        self.fst_is_TV = type(TV_or_This) != cls
        if not self.fst_is_TV and self.fst.halt():
            raise ValueError('halt')
    def halt(self):
        return self.snd is ...
    def iter_TVs(self):
        if self.fst_is_TV:
            yield self.fst
        else:
            yield from self.fst.iter_TVs()
        if not self.halt():
            yield self.snd
class ChoiceHelper(ManyOpHelper):
    # +(x | y | z)
    def __pos__(self):
        from .ChoiceTV import ChoiceTV
        bs = self.iter_TVs()
        return ChoiceTV(zip(enumStrInt(), bs))
    def __or__(self, other):
        return __class__(self, other)
class UnionHelper(ManyOpHelper):
    # +(x + y + z)
    def __pos__(self):
        from .UnionTV import unionTV
        bs = self.iter_TVs()
        return unionTV(bs)
    def __add__(self, other):
        return __class__(self, other)
class TupleHelper(ManyOpHelper):
    # +(x * y * z)
    def __pos__(self):
        from .TupleTV import tupleTV
        bs = self.iter_TVs()
        return tupleTV(bs)
    def __mul__(self, other):
        return __class__(self, other)




