
r'''

seed.types.Tester
from seed.types.Tester import is_good, ITester, the_Tester_True, the_Tester_False, Tester_True, Tester_False, TesterNOT, TesterAND, TesterXOR, TesterNOTXOR, TesterOR, ITesterNoArgs, ITesterUnaryOp, ITesterBinaryOp, ITesterArg, ITesterArgs, Tester__is_obj, Tester__eq_obj, Tester__in_obj, ITesterArg__with_cls, Tester__cls_is, Tester__cls_le, Tester__cls_lt, ITesterArgs, ITesterArgs__with_strs, Tester__obj_hasattrs, Tester__cls_hasattrs, return__False, test__False, ITesterArg__with_str, Tester__obj_getattr_test, Tester__obj_getattr_call, Tester__cls_getattr_call

from seed.types.Tester import

from seed.types.Tester import is_good, ITester
from seed.types.Tester import the_Tester_True, the_Tester_False, Tester_True, Tester_False, TesterNOT, TesterAND, TesterXOR, TesterNOTXOR, TesterOR
from seed.types.Tester import ITesterNoArgs, ITesterUnaryOp, ITesterBinaryOp, ITesterArg, ITesterArgs, ITesterArg__with_cls, ITesterArgs__with_strs, ITesterArg__with_str, ITesterArg__with_callable
from seed.types.Tester import Tester__is_obj, Tester__eq_obj, Tester__in_obj, Tester__cls_is, Tester__cls_le, Tester__cls_lt, Tester__obj_hasattrs, Tester__cls_hasattrs, Tester__obj_getattr_test, Tester__obj_getattr_call, Tester__cls_getattr_call, Tester__test_func
from seed.types.Tester import return__False, test__False


see:
    seed.helper.repr.repr_sys
    seed.helper.repr.repr_api
    seed.types.Tester
    seed.types.SinkTester

#'''

__all__ = '''
    is_good
    the_Tester_True
    the_Tester_False
    ITester
        ITesterNoArgs
            Tester_True
            Tester_False
        ITesterUnaryOp
            TesterNOT
        ITesterBinaryOp
            TesterAND
            TesterXOR
            TesterNOTXOR
            TesterOR
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
    return__False
    test__False
    '''.split()

from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from seed.abc.IGetArgsKwargs import IGetArgsKwargs
from seed.abc.abc import ABC, abstractmethod, override




def is_good(__sf, __x):
    '-> bool'
    cls = type(__sf)
    b = cls.__is_good__(__sf, __x)
    if type(b) is not bool: raise TypeError
    return b
class ITester(IReprImmutableHelper):
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




class ITesterNoArgs(ITester):
    @override
    def ___get_args_kwargs___(sf):
        return [], {}
class Tester_True(ITesterNoArgs):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return True
class Tester_False(ITesterNoArgs):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return False
the_Tester_True = Tester_True()
the_Tester_False = Tester_False()


class ITesterUnaryOp(ITester):
    def __init__(sf, rhs):
        if not isinstance(rhs, ITester): raise TypeError
        sf.__rhs = rhs
    @property
    def rhs(sf):
        return sf.__rhs
    @override
    def ___get_args_kwargs___(sf):
        return [sf.rhs], {}


class ITesterBinaryOp(ITester):
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


class ITesterArgs(ITester):
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

class ITesterArg(ITester):
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
    def __is_good__(sf, x):
        '-> bool'
        return is_good(sf.lhs, x) and is_good(sf.rhs, x)
class TesterXOR(ITesterBinaryOp):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return is_good(sf.lhs, x) ^ is_good(sf.rhs, x)
class TesterNOTXOR(ITesterBinaryOp):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return is_good(sf.lhs, x) is is_good(sf.rhs, x)
class TesterOR(ITesterBinaryOp):
    @override
    def __is_good__(sf, x):
        '-> bool'
        return is_good(sf.lhs, x) or is_good(sf.rhs, x)




class TesterNOT(ITesterUnaryOp):
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





