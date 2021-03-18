#HHHHH
TODO
    #TODO: lazy tribool op, output lazy too
    #TODO: TriBoolOps... move to new file
    #TODO: TesterAND... impl ___always_tri_test___
r'''

seed.types.Tester
py -m seed.types.Tester

from seed.types.Tester import

from seed.types.Tester import is_good, ITester, IAlwaysTriTester
from seed.types.Tester import the_Tester_True, the_Tester_False, Tester_True, Tester_False, TesterNOT, TesterAND, TesterXOR, TesterNOTXOR, TesterOR
from seed.types.Tester import ITesterMayAlways, ITesterNotAlways, ITesterNoArgs, ITesterUnaryOp, ITesterBinaryOp, ITesterArg, ITesterArgs, ITesterArg__with_cls, ITesterArgs__with_strs, ITesterArg__with_str, ITesterArg__with_callable
from seed.types.Tester import Tester__is_obj, Tester__eq_obj, Tester__in_obj, Tester__cls_is, Tester__cls_le, Tester__cls_lt, Tester__obj_hasattrs, Tester__cls_hasattrs, Tester__obj_getattr_test, Tester__obj_getattr_call, Tester__cls_getattr_call, Tester__test_func
from seed.types.Tester import return__False, test__False


see:
    seed.helper.repr.repr_sys
    seed.helper.repr.repr_api
    seed.types.Tester
    seed.types.SinkTester
see:
    view ../../python3_src/seed/helper/check/check.py
    view ../../python3_src/seed/helper/check/checkers.py
    view ../../python3_src/nn_ns/Bijection/TypeVerifier.py
    view ../../python3_src/seed/helper/check_utils.py
    view ../../python3_src/seed/types/Tester.py
vs:
    seed.helper.check.check # check+calc
    seed.types.Tester       # verify


#'''

#HHHHH
__all__ = '''
    is_good
    the_Tester_True
    the_Tester_False
    ITester

    return__False
    test__False

IAlwaysTriTester
    ITester
        ITesterNoArgs
            Tester_True
                the_Tester_True
            Tester_False
                the_Tester_False
        ITesterMayAlways
            ITesterUnaryOp
                TesterNOT
            ITesterBinaryOp
                TesterAND
                TesterXOR
                TesterNOTXOR
                TesterOR
        ITesterNotAlways
            ITesterArg
                Tester__is_obj
                Tester__eq_obj
                Tester__in_obj
                ITesterArg__with_cls
                    Tester__cls_is
                    Tester__cls_le
                    Tester__cls_lt
                ITesterArg__with_str
                    Tester__obj_getattr_test
                    Tester__obj_getattr_call
                    Tester__cls_getattr_call
                ITesterArg__with_callable
                    Tester__test_func
            ITesterArgs
                ITesterArgs__with_strs
                    Tester__obj_hasattrs
                    Tester__cls_hasattrs
    '''.split()

#HHHHH
from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from seed.abc.IGetArgsKwargs import IGetArgsKwargs
from seed.abc.abc import ABC, abstractmethod, override
from seed.abc.ISingleton import ISingleton

from seed.tiny import assert_eq, assert_eq_f, mk_assert_eq_f
import itertools


#HHHHH

class TriBoolOps:
    r'''
    tri_bool :: TriBool = (False|True|...)

    NOT
    AND OR XOR~NOT_EQU

    NXOR=NOT_XOR~EQU
    NAND=NOT_AND
    NOR=NOT_OR
    IMPLY = NOT_THEN_OR
    FLIP_IMPLY = OR_NOT
    NOT_IMPLY = AND_NOT
    NOT_FLIP_IMPLY = FLIP_NOT_IMPLY = NOT_THEN_AND

1 vars bool ops: (out=T/F)**((in=T/F)**1) = 2**2**1 = 4
    need no vars:2
    need 1 var = remain 2
2 vars bool ops: (out=T/F)**((in=T/F)**2) = 2**2**2 = 16
    need no vars:2
    need 1 vars:(choose=L/R)*(1 var ops&need 1 var) = 2*(2**2-2) =4
    need both = remain 10:
        symmetry = 6:
            AND OR XOR
            NAND NOR NXOR
        asymmetry = 4:
            IMPLY  FLIP_IMPLY
            NOT_IMPLY  NOT_FLIP_IMPLY


2 vars tribool ops: 3**3**2 = 3**9 = 19683
    need no vars:3
    need 1 vars:(choose=L/R)*(1 var ops&need 1 var) = 2*(3**3-3) = 48
    need both = remain 19632
    required bool closoure:
        3**(3**2-2**2) * 2**(2**2) = 3888

    constraint: ... = [True|False]
        i.e. when input var is ..., input both, if output both then out is ...

    #'''
    @classmethod
    def is_bool(cls, x):
        return x is True or x is False
        return type(x) is bool
    @classmethod
    def is_tribool(cls, x):
        return x is ... or x is True or x is False
        return x is ... or cls.is_bool(x)
    @classmethod
    def NOT(cls, rhs):
        if rhs is ...:
            return ...
        if rhs is False:
            return True
        if rhs is True:
            return False
        raise TypeError
        return not rhs

    @classmethod
    def AND(cls, lhs, rhs):
        if lhs is False or rhs is False:
            return False
        if lhs is ... or rhs is ...:
            return ...
        if lhs is True is rhs:
            return True
        raise TypeError
    @classmethod
    def OR(cls, lhs, rhs):
        if lhs is True or rhs is True:
            return True
        if lhs is ... or rhs is ...:
            return ...
        if lhs is False is rhs:
            return False
        raise TypeError
    @classmethod
    def XOR(cls, lhs, rhs):
        if lhs is ... or rhs is ...:
            return ...
        if lhs is rhs:
            return False
        if lhs is True and rhs is False:
            return True
        if lhs is False and rhs is True:
            return True
        raise TypeError
    @classmethod
    def IMPLY(cls, lhs, rhs):
        if lhs is False or rhs is True:
            return True
        if lhs is ... or rhs is ...:
            return ...
        if lhs is True and rhs is False:
            return False
        raise TypeError
    @classmethod
    def FLIP_IMPLY(cls, lhs, rhs):
        return cls.IMPLY(rhs, lhs)
    @classmethod
    def NOT_FLIP_IMPLY(cls, lhs, rhs):
        return cls.NOT(cls.FLIP_IMPLY(lhs, rhs))
    @classmethod
    def NOT_IMPLY(cls, lhs, rhs):
        return cls.NOT(cls.IMPLY(lhs, rhs))
    @classmethod
    def NOT_XOR(cls, lhs, rhs):
        return cls.NOT(cls.XOR(lhs, rhs))
    @classmethod
    def NOT_OR(cls, lhs, rhs):
        return cls.NOT(cls.OR(lhs, rhs))
    @classmethod
    def NOT_AND(cls, lhs, rhs):
        return cls.NOT(cls.AND(lhs, rhs))
    NXOR = NOT_XOR
    NOR = NOT_OR
    NAND = NOT_AND

    NOT_THEN_OR = IMPLY
    OR_NOT = FLIP_IMPLY
    AND_NOT = NOT_IMPLY
    NOT_THEN_AND = FLIP_NOT_IMPLY = NOT_FLIP_IMPLY


#HHHHH
class test_TriBool_binary_ops:
    #test bool by py op
    #test tribool by bool and constraint
    #test all tribool by assert output tables are all diff


    @classmethod
    def test_bool_by_py_op(cls, tribool_op, py_op):
        for x, y in  itertools.product([False, True], repeat=2):
            r = py_op(x, y)
            assert_eq_f(r, tribool_op, x, y)
    @classmethod
    def bools2tri(cls, bools):
        [a, *ls] = set(bools)
        return ... if ls else a
    @classmethod
    def tri2bools(cls, tribool):
        if tribool is ...:
            return (True, False)
        return (tribool,)
    @classmethod
    def test_tribool_by_bool_and_constraint(cls, tribool_op, py_op):

        for xy in  itertools.product([..., False, True], repeat=2):
            r = cls.bools2tri(py_op(a,b) for a, b in  itertools.product(*map(cls.tri2bools, xy)))
            assert_eq_f(r, tribool_op, *xy)

    @classmethod
    def mk_table_of_tribpol_binary_op(cls, tribool_op):
        d = {}
        for xy in  itertools.product([..., False, True], repeat=2):
            r = tribool_op(*xy)
            d[xy] = r
        return d

    @classmethod
    def test_all_tribool_by_assert_output_tables_are_all_diff(cls, all_tribool_ops):
        all_tribool_ops = tuple(all_tribool_ops)
        ls = tuple(frozenset(cls.mk_table_of_tribpol_binary_op(f).items()) for f in all_tribool_ops)
        ss = set(ls)
        assert_eq(len(ls), len(ss))
    @classmethod
    def get_all_xbool_ops(cls, T):
        x = T
        return (x.AND, x.OR, x.XOR, x.IMPLY, x.FLIP_IMPLY, x.NOT_AND, x.NOT_OR, x.NOT_XOR, x.NOT_IMPLY, x.NOT_FLIP_IMPLY)
    @classmethod
    def main_test(cls):
        T = TriBoolOps
        B = BoolOps
        all_tribool_ops = cls.get_all_xbool_ops(T)
        all_py_bool_ops = cls.get_all_xbool_ops(B)
        for tribool_op, py_op in zip(all_tribool_ops, all_py_bool_ops):
            cls.test_bool_by_py_op(tribool_op, py_op)
            cls.test_tribool_by_bool_and_constraint(tribool_op, py_op)
        cls.test_all_tribool_by_assert_output_tables_are_all_diff(all_tribool_ops)

#HHHHH
class BoolOps:
    @classmethod
    def NOT(cls, rhs):
        return not rhs
    @classmethod
    def AND(cls, lhs, rhs):
        return lhs and rhs
    @classmethod
    def OR(cls, lhs, rhs):
        return lhs or rhs
    @classmethod
    def XOR(cls, lhs, rhs):
        return lhs ^ rhs
    @classmethod
    def IMPLY(cls, lhs, rhs):
        return not lhs or rhs
    @classmethod
    def FLIP_IMPLY(cls, lhs, rhs):
        return cls.IMPLY(rhs, lhs)
    @classmethod
    def NOT_FLIP_IMPLY(cls, lhs, rhs):
        return cls.NOT(cls.FLIP_IMPLY(lhs, rhs))
    @classmethod
    def NOT_IMPLY(cls, lhs, rhs):
        return cls.NOT(cls.IMPLY(lhs, rhs))
    @classmethod
    def NOT_XOR(cls, lhs, rhs):
        return cls.NOT(cls.XOR(lhs, rhs))
    @classmethod
    def NOT_OR(cls, lhs, rhs):
        return cls.NOT(cls.OR(lhs, rhs))
    @classmethod
    def NOT_AND(cls, lhs, rhs):
        return cls.NOT(cls.AND(lhs, rhs))
    NXOR = NOT_XOR
    NOR = NOT_OR
    NAND = NOT_AND

    NOT_THEN_OR = IMPLY
    OR_NOT = FLIP_IMPLY
    AND_NOT = NOT_IMPLY
    NOT_THEN_AND = FLIP_NOT_IMPLY = NOT_FLIP_IMPLY

test_TriBool_binary_ops.main_test()

#HHHHH






def always_tri_test(__sf, __x, /):
    'IAlwaysTriTester -> (...|bool)'
    cls = type(__sf)
    r = cls.___always_tri_test___(__sf, __x)
    if not (r is ... or type(r) is bool): raise TypeError
    return r
def is_good(__sf, __x, /):
    'ITester -> bool'
    cls = type(__sf)
    b = cls.__is_good__(__sf, __x)
    if type(b) is not bool: raise TypeError
    return b
#HHHHH
class IAlwaysTriTester(IReprImmutableHelper):
    #def ___get_args_kwargs___(sf):
    @abstractmethod
    def ___always_tri_test___(sf, x):
        r'''-> (...|bool)
        not classmethod
        ... -> not always
        True -> always True
        False -> always False
        #'''
        return ...
class ITester(IAlwaysTriTester):
    #def ___get_args_kwargs___(sf):
    #def ___always_tri_test___(sf, x):
    @abstractmethod
    def __is_good__(sf, x):
        '-> bool'
    r'''
    def __call__(__sf, __x):
        '-> bool'
        return __sf.is_good(__x)
    #'''
    def __and__(sf, ot):
        return TesterAND(sf, ot)
    def __xor__(sf, ot):
        return TesterXOR(sf, ot)
    def __or__(sf, ot):
        return TesterOR(sf, ot)
    def __invert__(sf, ot):
        return TesterNOT(sf)




#HHHHH
class ITesterMayAlways(ITester):
    #def ___get_args_kwargs___(sf):
    #def __is_good__(sf, x):
    #def ___always_tri_test___(sf, x):
    pass
class ITesterNotAlways(ITester):
    #def ___get_args_kwargs___(sf):
    #def __is_good__(sf, x):
    @override
    def ___always_tri_test___(sf, x):
        return ...

ITester
class ITesterNoArgs(ITester, ISingleton):
    #def ___always_tri_test___(sf, x):
    @override
    def ___get_args_kwargs___(sf):
        return [], {}
    @override
    def __is_good__(sf, x):
        r = always_tri_test(sf, x)
        if r is ...: raise Exception(f'logic-err: {type(sf)!r} : {sf!r}')
        return r
class Tester_True(ITesterNoArgs):
    @override
    def ___always_tri_test___(sf, x):
        '-> bool'
        return True
class Tester_False(ITesterNoArgs):
    @override
    def ___always_tri_test___(sf, x):
        '-> bool'
        return False
the_Tester_True = Tester_True()
the_Tester_False = Tester_False()


#HHHHH
class ITesterUnaryOp(ITesterMayAlways):
    def __init__(sf, rhs):
        if not isinstance(rhs, ITester): raise TypeError
        sf.__rhs = rhs
    @property
    def rhs(sf):
        return sf.__rhs
    @override
    def ___get_args_kwargs___(sf):
        return [sf.rhs], {}


class ITesterBinaryOp(ITesterMayAlways):
    def __init__(sf, lhs, rhs):
        if not isinstance(lhs, ITester): raise TypeError
        if not isinstance(rhs, ITester): raise TypeError
        sf.__lhs = lhs
        sf.__rhs = rhs
    @property
    def lhs(sf):
        return sf.__lhs
    @property
    def rhs(sf):
        return sf.__rhs
    @override
    def ___get_args_kwargs___(sf):
        return [sf.lhs, sf.rhs], {}


class ITesterArgs(ITesterNotAlways):
    def _check_args_(sf, args):
        return
    def __init__(sf, *args):
        sf._check_args_(args)
        sf.__args = args
    @property
    def args(sf):
        return sf.__args
    @override
    def ___get_args_kwargs___(sf):
        return sf.args, {}

class ITesterArg(ITesterNotAlways):
    def _convert_arg_(sf, arg):
        return arg
    def __init__(sf, arg):
        sf.__arg = sf._convert_arg_(arg)
    @property
    def arg(sf):
        return sf.__arg
    @override
    def ___get_args_kwargs___(sf):
        return [sf.arg], {}

class ITesterArg__with_cls(ITesterArg):
    @override
    def _convert_arg_(sf, arg):
        if not isinstance(arg, type): raise TypeError
        return arg

class ITesterArg__with_str(ITesterArg):
    @override
    def _convert_arg_(sf, arg):
        if not isinstance(arg, str): raise TypeError
        return arg

class ITesterArg__with_callable(ITesterArg):
    @override
    def _convert_arg_(sf, arg):
        if not callable(arg): raise TypeError
        return arg

class ITesterArgs__with_strs(ITesterArgs):
    def _check_args_(sf, args):
        if not all(type(arg) is str for arg in args):raise TypeError
        return

















class TesterAND(ITesterBinaryOp):
    @override
    def ___always_tri_test___(sf, x):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return is_good(sf.lhs, x) and is_good(sf.rhs, x)
class TesterXOR(ITesterBinaryOp):
    @override
    def ___always_tri_test___(sf, x):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return is_good(sf.lhs, x) ^ is_good(sf.rhs, x)
class TesterNOTXOR(ITesterBinaryOp):
    @override
    def ___always_tri_test___(sf, x):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return is_good(sf.lhs, x) is is_good(sf.rhs, x)
class TesterOR(ITesterBinaryOp):
    @override
    def ___always_tri_test___(sf, x):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return is_good(sf.lhs, x) or is_good(sf.rhs, x)




class TesterNOT(ITesterUnaryOp):
    @override
    def ___always_tri_test___(sf, x):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return not is_good(sf.rhs, x)














class Tester__is_obj(ITesterArg):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return x is sf.arg

class Tester__eq_obj(ITesterArg):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return x == sf.arg

class Tester__in_obj(ITesterArg):
    @override
    def _convert_arg_(sf, arg):
        if not hasattr(type(arg), '__contains__'): raise TypeError
        return arg
    @override
    def __is_good__(sf, x):
        '-> bool'
        return x in sf.arg

class Tester__cls_is(ITesterArg__with_cls):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return type(x) is sf.arg

class Tester__cls_le(ITesterArg__with_cls):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return isinstance(x, sf.arg)

class Tester__cls_lt(ITesterArg__with_cls):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return type(x) is not sf.arg and isinstance(x, sf.arg)



class Tester__obj_hasattrs(ITesterArgs__with_strs):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return all(hasattr(x, arg) for arg in sf.args)

class Tester__cls_hasattrs(ITesterArgs__with_strs):
    @override
    def __is_good__(sf, x):
        '-> bool'
        cls = type(x)
        return all(hasattr(cls, arg) for arg in sf.args)




def return__False():
    return False
def test__False(x):
    return False
class Tester__obj_getattr_test(ITesterArg__with_str):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return bool(getattr(x, sf.arg, False))

class Tester__obj_getattr_call(ITesterArg__with_str):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return getattr(x, sf.arg, return__False)()

class Tester__cls_getattr_call(ITesterArg__with_str):
    @override
    def __is_good__(sf, x):
        '-> bool'
        cls = type(x)
        return getattr(cls, sf.arg, test__False)(x)



class Tester__test_func(ITesterArg__with_callable):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return sf.arg(x)





