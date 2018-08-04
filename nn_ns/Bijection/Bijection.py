
'''

op
    inv, id, chain, array, tuple/pair, choice/either, record, union
    ~x == x.invBJ
    tv.idBJ

    # why use '+'??
    #   so, we can repr this expression without '()'
    +(x >> y >> z) == chainBJ(x, y, z)
    x[min,max] == fmap x

    BJ.TupleBJ(*args) # arg can tuple
    +(x * y * z) == (x,y,z)
    +(x * ...) == (x,)

    BJ.RecordBJ(**kwargs)
    BJ.ChoiceBJ(**kwargs)
    +(x | y | z) == {0:x, 1:y, 2:z} # 0 == '0'
    +(x | ...) == {0:x}
    BJ.EitherBJ(x, y) # x, y can be pair
    +(x / y) == {left:x, right:y}

    BJ.UnionBJ(*args)
    +(x + y + z) == union(x, y, z)

    +       -       *       **      /       //      %      @
    <<      >>      &       |       ^       ~
    <       >       <=      >=      ==      !=

'''

__all__ = '''
    Bijection
    invBJ
    TupleBJ
    RecordBJ
    ChoiceBJ
    EitherBJ
    UnionBJ
    ChainBJ
    mayBJs2TupleBJ
    '''.split()


from .IRepr import IRepr
from abc import ABCMeta, abstractmethod
from itertools import count
'''
class Bijection:
    make_args_kwargs
    make_name_args_kwargs
    def get_construct_info(self):
        return self.make_args_kwargs(self.)

    def get_InputType(self):
    def get_OutputType(self):
    def untypechecked_forward(self, input):
    def untypechecked_backward(self, output):
'''

def is_uint(obj):
    return type(obj) is int and obj >= 0
def is_may_uint(obj):
    return obj is None or is_uint(obj)

class Bijection(IRepr):
    # we may have dynamic chained bijection, so I/O is not depended on cls
    # return an instance of TypeVerifier
    @abstractmethod
    def get_InputType(self):pass
    @abstractmethod
    def get_OutputType(self):pass
    @abstractmethod
    def untypechecked_forward(self, input):pass
    @abstractmethod
    def untypechecked_backward(self, output):pass

    def is_idBJ(self):
        return False
    # def chain(self, other):pass
    def typechecked_forward(self, input):
        assert self.get_InputType().has_instance(input)
        output = self.untypechecked_forward(input)
        assert self.get_OutputType().has_instance(output)
        return output
    def typechecked_backward(self, output):
        assert self.get_OutputType().has_instance(output)
        input = self.untypechecked_backward(output)
        assert self.get_InputType().has_instance(input)
        return input

    ####
    def test(self):
        I = self.get_InputType()
        O = self.get_OutputType()
        inputs = I.iter_examples()
        outputs = O.iter_examples()
        for i, o in zip(inputs, outputs):
            o2 = self.untypechecked_forward(i)
            i2 = self.untypechecked_backward(o2)
            assert I.untypechecked_equal(i, i2)
            i2 = self.untypechecked_backward(o)
            o2 = self.untypechecked_forward(i2)
            assert O.untypechecked_equal(o, o2)

    ###################### op ####################

    def invBJ(self):
        # ~self == self.invBJ
        from .InverseBijection import inverse_bijection
        return inverse_bijection(self)
    def __invert__(self):
        return self.invBJ()


    def __getitem__(self, key):
        # x[min,max] == fmap x
        # x[min] == fmap x
        # x[min,None] == fmap x
        # key is uint or (uint, may_uint)
        if type(key) is int:
            raise TypeError
            assert is_uint(key)
            min, max = key, None
        elif type(key) is tuple:
            assert len(key) == 2
            min, max = key
            assert is_uint(min)
            assert is_may_uint(max)
            assert max is None or min <= max
        else:
            raise TypeError
        from .ArrayBijection import ArrayBijection
        return ArrayBijection(self, min, max)

    def chain_withBJ(self, *args):
        return self.ChainBJ(self, *args)
    @staticmethod
    def ChainBJ(*args):
        from .ChainedBijection import chain_bijections
        return chain_bijections(args)
    def __rshift__(self, other):
        # +(x >> y >> z) == chainBJ(x, y, z)
        return ChainHelper(self, other)
    def tuple_withBJ(self, *args):
        return self.TupleBJ(self, *args)
    @staticmethod
    def TupleBJ(*args):
        # arg can be nested tuple and BJ
        def this_func(args):
            return tuple_bijection(map(f, args))
        def f(arg):
            # arg is BJ or tuple
            # BJ or tuple to BJ
            if type(arg) == tuple:
                return this_func(arg)
            return arg
        from .TupleBijection import tuple_bijection
        return this_func(args)
    def __mul__(self, other):
        # +(x * y * z) == (x,y,z)
        # +(x * ...) == (x,)
        return TupleHelper(self, other)

    @staticmethod
    def MayBJs2TupleBJ(InputTV, mayBJs):
        from .TupleBijection import mayBJs2TupleBJ
        return mayBJs2TupleBJ(InputTV, mayBJs)

    def record_withBJ(self, tag, **kwargs):
        assert tag not in kwargs
        kwargs[tag] = self
        return self.RecordBJ(**kwargs)
    @staticmethod
    def RecordBJ(**kwargs):
        from .RecordBijection import record_bijection
        return record_bijection(**kwargs)
    def choice_withBJ(self, tag, **kwargs):
        assert tag not in kwargs
        kwargs[tag] = self
        return self.ChoiceBJ(**kwargs)
    @staticmethod
    def ChoiceBJ(**kwargs):
        from .ChoiceBijection import choice_bijection
        return choice_bijection(**kwargs)
    def __or__(self, other):
        # +(x | y | z) == {0:x, 1:y, 2:z} # 0 == '0'
        # +(x | ...) == {0:x}
        return ChoiceHelper(self, other)

    def either_withBJ(self, rightBJ):
        return self.EitherBJ(self, rightBJ)
    @staticmethod
    def EitherBJ(leftBJ, rightBJ):
        # leftBJ, rightBJ can be nested pair or BJ
        def this_func(x, y):
            x,y = f(x), f(y)
            return make_eitherBJ(x, y)
        def f(arg):
            # arg is BJ or tuple
            # BJ or tuple to BJ
            if type(arg) == tuple:
                assert len(arg) == 2
                return this_func(*arg)
            return arg
        from .ChoiceBijection import make_eitherBJ
        return this_func(leftBJ, rightBJ)
    def __truediv__(self, other):
        # +(x / y) == {left:x, right:y}
        return EitherHelper(self, other)

    def union_withBJ(self, *args):
        return self.UnionBJ(self, *args)
    @staticmethod
    def UnionBJ(*args):
        from .UnionBijection import UnionBijection
        return UnionBijection(*args)
    def __add__(self, other):
        # +(x + y + z) == union(x, y, z)
        return UnionHelper(self, other)





invBJ = Bijection.invBJ
TupleBJ = Bijection.TupleBJ
RecordBJ = Bijection.RecordBJ
ChoiceBJ = Bijection.ChoiceBJ
EitherBJ = Bijection.EitherBJ
UnionBJ = Bijection.UnionBJ
ChainBJ = Bijection.ChainBJ
mayBJs2TupleBJ = Bijection.MayBJs2TupleBJ






'''
/ArrayBijection ArrayBijection
/TupleBijection tuple_bijection mayBJs2TupleBJ
/RecordBijection record_bijection
/ChoiceBijection choice_bijection ChoiceBijection make_eitherBJ
/UnionBijection UnionBijection union_bijection
/ChainedBijection chain_bijections
ChainHelper
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
    def __init__(self, lhsBJ, rhsBJ):
        assert isinstance(lhsBJ, Bijection)
        assert isinstance(rhsBJ, Bijection)
        self.lhsBJ = lhsBJ
        self.rhsBJ = rhsBJ
        from .ChoiceBijection import make_eitherBJ
        self.EitherBJ = make_eitherBJ(lhsBJ, rhsBJ)
    def __pos__(self):
        return self.EitherBJ

class ManyOpHelper(Helper):
    # + | * >>
    def __init__(self, BJ_or_This, BJ_or_Dot3):
        cls = type(self)
        assert type(BJ_or_This) == cls or isinstance(BJ_or_This, Bijection)
        assert isinstance(BJ_or_Dot3, Bijection) or BJ_or_Dot3 is ...
        self.fst = BJ_or_This
        self.snd = BJ_or_Dot3
        self.fst_is_BJ = type(BJ_or_This) != cls
        if not self.fst_is_BJ and self.fst.halt():
            raise ValueError('halt')
    def halt(self):
        return self.snd is ...
    def iter_bijections(self):
        if self.fst_is_BJ:
            yield self.fst
        else:
            yield from self.fst.iter_bijections()
        if not self.halt():
            yield self.snd
class ChoiceHelper(ManyOpHelper):
    # +(x | y | z)
    def __pos__(self):
        from .ChoiceBijection import ChoiceBijection
        bs = self.iter_bijections()
        return ChoiceBijection(zip(enumStrInt(), bs))
    def __or__(self, other):
        return __class__(self, other)
class ChainHelper(ManyOpHelper):
    # +(x >> y >> z)
    def __pos__(self):
        from .ChainedBijection import chain_bijections
        bs = self.iter_bijections()
        return chain_bijections(bs)
    def __rshift__(self, other):
        return __class__(self, other)
class UnionHelper(ManyOpHelper):
    # +(x + y + z)
    def __pos__(self):
        from .UnionBijection import union_bijection
        bs = self.iter_bijections()
        return union_bijection(bs)
    def __add__(self, other):
        return __class__(self, other)
class TupleHelper(ManyOpHelper):
    # +(x * y * z)
    def __pos__(self):
        from .TupleBijection import tuple_bijection
        bs = self.iter_bijections()
        return tuple_bijection(bs)
    def __mul__(self, other):
        return __class__(self, other)




