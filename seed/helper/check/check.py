#HHHHH

r'''[[[
ICheckEchor_with_args
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
ICheckCalcor_with_args
    _may_num_args_ = 1
    _std_arg0_ = _std_arg4checkers
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):

TODO:
    #here TODO: def __new__(


py -m seed.helper.check.check
from seed.helper.check.check import check, verify, check_then_calc, verify_then_may_calc, check_then_calc_ex, verify_then_may_calc_ex
from seed.helper.check.check import mk_checker, mk_impl_class_checker, mk_checker__point, mk_checker__pair, mk_checker__array, mk_checker__pairs
from seed.helper.check.check import IChecker, CheckFail, CheckError, CheckException
from seed.helper.check.check import the_checker__is_None, the_fail_checker, the_pass_checker, the_hashable_checker, checker4callable
from seed.helper.check.check import Checker__uint_mod, Checker__int_between, Checker__tuple_maybe, Checker__none_maybe

from seed.helper.check.check import Checker__choice, Checker__switch, Checker__ordered_choice, Checker__ordered_switch
from seed.helper.check.check import


e ../../python3_src/seed/helper/check/check.py
see:
    view ../../python3_src/seed/helper/check/check.py
    view ../../python3_src/seed/helper/check/checkers.py
    view ../../python3_src/nn_ns/Bijection/TypeVerifier.py
    view ../../python3_src/seed/helper/check_utils.py
    view ../../python3_src/seed/types/Tester.py
vs:
    seed.helper.check.check # check+calc
    seed.types.Tester       # verify

why ICheckCalcor?
    why a checker required.calc?
    eg:
        given:
            checker4str
            checker4pseudo_identifier
            checker4identifier
        wanted:
            checker4qual_name
        impl:
            now we need to split input str, i.e. transform input then do further check
            example from:
                seed.helper.check.checks

use at:
    check input arg
        , check immutable input arg
        , for mk immutable obj (output)

immutable type:
    namedtuple
    frozenset
    seed.types.FrozenDict

    tuple
        pair
    str
        keyword
        identifier
        pseudo_identifier
    bytes
    int
        uint
    bool
    fractions.Fraction
    type
        is
        le
        lt
immutable set:
    ...
logic:
    not/and/or/pass/fail



DONE:
    check Lookupable __getitem__
    weaken:
        array --> list --> Sequence
        FrozenDict --> dict/OrderedDict --> Mapping/key hashable
        frozenset -> set -> Set
    mapping
        HalfFrozenDict/list-with-fixed-len
        FrozenDict/tuple
    choice:
        union=Checker__ordered_choice
        FrozenDict
    >> switch ==>> join/fmap
        (case, obj)
        * tuple
        * namedtuple
        * FrozenDict

        #mapping/Lookupable can be array if case is int
        join/switch :: (case, obj<case>) -> {case:checker<(obj<case>->o)>} -> o
        +fmap+/switch_with_case :: (case, obj<case>) -> {case:checker<({case,obj<case>)->o<case>)>} -> {case:o<case>}

    like: Checker__check_func
        Checker__check_then_calc_ex_func
        Checker__check_then_calc_func

    int_ge/int_lt class for repr








>>> mk_checker(None)
Checker__is_obj(None)
>>> mk_checker(False)
Checker__fail()
>>> mk_checker(True)
Checker__pass()


>>> mk_checker(None) is the_checker__is_None
True
>>> mk_checker(False) is the_fail_checker
True
>>> mk_checker(True) is the_pass_checker
True

>>> the_checker__is_None(None)
>>> the_pass_checker(False)
>>> the_checker__is_None(False)
Traceback (most recent call last):
    ...
CheckFail
>>> the_fail_checker(False)
Traceback (most recent call last):
    ...
CheckFail


>>> ~the_fail_checker is the_pass_checker
True

>>> f = the_pass_checker & the_fail_checker
>>> p = the_fail_checker | the_pass_checker
>>> ~~f is f
True
>>> p(0)
>>> (~f)(0)
>>> f(0)
Traceback (most recent call last):
    ...
CheckFail
>>> (~p)(0)
Traceback (most recent call last):
    ...
CheckFail

>>> f_pp = p^p
>>> f_ff = f^f
>>> p_pf = p^f
>>> p_fp = f^p
>>> p_fp(1)
>>> p_pf(1)
>>> (~f_ff)(1)
>>> (~f_pp)(1)

>>> f2 = p-p
>>> p2 = p-f
>>> p2(2)
>>> (~f2)(2)

>>> tf = the_checker__is_True * the_checker__is_False
>>> tf
Checker__py_tuple_as_point((Checker__is_obj(True), Checker__is_obj(False)))
>>> tf[1,0]
False
>>> tf[True, False]
True

>>> checker4callable
Checker__verify_func(<built-in function callable>)
>>> checker4callable[checker4callable]
True

>>> checker4ints = mk_checker(('us', int))
>>> checker4int_str_pairs = mk_checker(('ts', int, str))
>>> checker4ints
Checker__py_tuple_as_array(Checker__ordered_choice((Checker__isinstance(<class 'int'>),)))
>>> checker4int_str_pairs
Checker__py_tuple_as_array(Checker__py_tuple_as_point((Checker__isinstance(<class 'int'>), Checker__isinstance(<class 'str'>))))

>>> checker4ints[0,0,4]
True
>>> checker4ints[0,True]
True
>>> checker4ints[0,'']
False

>>> checker4int_str_pairs[()]
True
>>> checker4int_str_pairs[(7,''),]
True
>>> checker4int_str_pairs[(7,''), (False, 'z')]
True
>>> checker4int_str_pairs[(),]
False
>>> checker4int_str_pairs[('', 7),]
False
>>> checker4int_str_pairs[(1,), (7,'')]
False






>>> check_then_calc(tf, (True, False))
(True, False)
>>> check_then_calc(tf>>at[0:0], (True, False))
()
>>> check_then_calc(tf>>at[0], (True, False))
True
>>> check_then_calc(tf>>snd, (True, False))
False
>>> check_then_calc(tf>>at[-1], (True, False))
False
>>> check_then_calc(tf>>at[1:], (True, False))
(False,)
>>> check_then_calc(tf>>at[1:]>>at[1:], (True, False))
()
>>> check_then_calc(tf>>at[1:]>>at[0], (True, False))
False
>>> check_then_calc(tf>>at[1:]>>at[-1], (True, False))
False
>>> check_then_calc(tf>>at[1:]<<at[-1], (True, False))
False
>>> check_then_calc(tf>>at[1:]<<at[0], (True, False))
True

>>> check_then_calc(tf>>at[1:]<<at[:], (True, False))
(True, False)
>>> check_then_calc(tf>>at[1:]>>at[:], (True, False))
(False,)
>>> check_then_calc(tf%(the_pass_checker>>at[1:]<<at[:]), (True, False))
(True, False)





from seed.helper.check.check import Checker__choice, Checker__switch, Checker__ordered_choice, Checker__ordered_switch
>>> Checker__unordered_switch(())
Traceback (most recent call last):
    ...
CheckFail_Type
>>> Checker__switch({})
Traceback (most recent call last):
    ...
CheckFail_Type
>>> Checker__switch(())
Checker__switch(())
>>> Checker__switch(FrozenDict())
Checker__switch(FrozenDict({}))

>>> Checker__ordered_choice(())
Checker__ordered_choice(())
>>> ft = Checker__ordered_choice((the_fail_checker, the_pass_checker))
>>> check(ft, 'w')
>>> check_then_calc(ft, 'w')
(1, 'w')

>>> ff = Checker__ordered_choice((the_fail_checker, the_fail_checker))
>>> check(ff, 'w')
Traceback (most recent call last):
    ...
CheckFail
>>> check_then_calc(ff, 'w')
Traceback (most recent call last):
    ...
CheckFail

>>> s01 = Checker__ordered_switch((the_fail_checker, the_pass_checker))
>>> check_then_calc(s01, (0, 'w'))
Traceback (most recent call last):
    ...
CheckFail
>>> check_then_calc(s01, (1, 'w'))
'w'
>>> check_then_calc(s01, (2, 'w'))
Traceback (most recent call last):
    ...
IndexError: tuple index out of range



>>> pp = divmod(the_pass_checker, the_pass_checker)
>>> pp
CheckCalcor__DAG_line(False, ((Checker__pass(), True), (Checker__pass(), True)))
>>> check_then_calc(pp, 'w')
('w', 'w')
>>> not_empty = the_pass_checker@bool
>>> not_empty['']
False
>>> not_empty['w']
True


#]]]'''

#HHHHH
#[[[


#[[[
#]]]








































__all__ = '''

CheckException
    CheckFail
    CheckError

mk_checker
    check_PseudoChecker
check
    verify
check_then_calc
    verify_then_may_calc
check_then_calc_ex
    verify_then_may_calc_ex

mk_impl_class_checker
    mk_checker__array
    mk_checker__point
    mk_checker__pair
    mk_checker__pairs







IChecker
    ICheckEchor
    ICheckCalcor
    IChecker_with_args
        ICheckCalcor_with_args
        ICheckEchor_with_args
            IChecker_one_arg
            IChecker_two_args
            ICheckEchor_with_args__verify4check
                ICheckEchor_one_arg__verify
                    ICheckEchor_one_arg__type__verify
                    ICheckEchor_one_arg__type_tree__verify
                    ICheckEchor_one_arg__Container__verify



    ICheckEchor_with_args
        IChecker_with_args__arg0_is_checker
        IChecker_with_args__arg0_is_checkers
        IChecker_with_args__arg0_is_callable
        IChecker_with_args__arg0_is_type_tree
        IChecker_with_args__arg0_is_type
        IChecker_with_args__arg0_is_uint
        IChecker_with_args__arg0_is_int
        IChecker_with_args__arg0_is_bool
        IChecker_with_args__arg0_is_Container
        IChecker_with_args__arg0_is_key2checker

        IChecker_with_args__arg1_is_checker
        IChecker_with_args__arg1_is_checkers
        IChecker_with_args__arg1_is_callable
        IChecker_with_args__arg1_is_type
        IChecker_with_args__arg1_is_uint
        IChecker_with_args__arg1_is_int
        IChecker_with_args__arg1_is_checker_bool_pairs

    IChecker_one_arg
        IChecker_one_arg__checker
        IChecker_one_arg__checkers
        IChecker_one_arg__callable
        IChecker_one_arg__uint
        IChecker_one_arg__int
        IChecker_one_arg__key2checker

    IChecker_two_args
        IChecker_two_args__arg0_is_checker
        IChecker_two_args__arg0_is_uint
        IChecker_two_args__arg0_is_bool
        IChecker_two_args__arg0_is_int
        IChecker_two_args__arg1_is_int
        IChecker_two_args__args_are_int
        IChecker_two_args__arg1_is_checker
        IChecker_two_args__arg1_is_checkers
        IChecker_two_args__arg0_is_bool__arg1_is_checker_bool_pairs
        ICheckCalcor_two_args__hold_input__checker_hold_result_pairs



IChecker
    the_checker__is_None
    Checker__if_else
    Checker__fail
        the_fail_checker
    Checker__pass
        the_pass_checker
    Checker__inv
    Checker__ordered_intersection
    Checker__ordered_choice
      Checker__ordered_union


    ICheckCalcor
        ICheckCalcor__DAG_width_depth
            CheckCalcor__DAG_star
            CheckCalcor__DAG_line
              Checker__ordered_intersection
        CheckCalcor__transform
        Checker__ordered_choice
          Checker__ordered_union

    IChecker_no_args
        Checker__fail
            the_fail_checker
        Checker__pass
            the_pass_checker
        Checker__hashable
            the_hashable_checker

    IChecker_one_arg
        ICheckEchor_one_arg__verify
        IChecker_one_arg__checker
            Checker__inv
        IChecker_one_arg__checkers
            Checker__ordered_intersection
            Checker__ordered_union
        IChecker_one_arg__callable
            Checker__no_calc
            Checker__check_func
            Checker__verify_func
                checker4callable
            Checker__check_then_calc_ex_func
        ICheckEchor_one_arg__type__verify
        ICheckEchor_one_arg__type_tree__verify
            Checker__issubclass
                Checker__le_cls
            Checker__issubclass__allow_nontype
            Checker__is_proper_subclass
                Checker__lt_cls
            Checker__isinstance
                Checker__in_cls
            Checker__type_is
    IChecker_two_args
        IChecker_two_args__arg0_is_checker
        IChecker_two_args__arg1_is_checker
        IChecker_two_args__arg1_is_checkers

    Checker__all
        Checker__iterable
    Checker__py_tuple_as_array
        mk_checker__array
    Checker__py_tuple_as_point
        mk_checker__point
        mk_checker__pair
        mk_checker__pairs
    Checker__py_tuple_as_point__omit
        Checker__tuple_maybe
        Checker__none_maybe

    Checker__is_obj
        the_checker__is_None
        the_checker__is_False
        the_checker__is_True
        the_checker__is_NotImplemented
        the_checker__is_Ellipsis
    Checker__eq_obj
        Checker__eq_obj__same_type
        Checker__le_obj
        Checker__lt_obj
        Checker__ge_obj
        Checker__gt_obj

    Checker__in_set
        Checker__in_set__hash
    Checker__hashable

    Checker__uint_mod
        Checker__int_between
        Checker__int_ge
        Checker__int_lt


    Checker__namedtuple
        Checker__py_namedtuple_as_point
    Checker__FrozenDict_as_record
        Checker__FrozenDict
        Checker__FrozenDict__item
    Checker__frozenset




    ConfigMixin__Lookupable
    IChecker__choice_or_switch
        IChecker__ordered_choice_or_switch
        IChecker__unordered_choice_or_switch

        Checker__choice_many1
        Checker__choice_only_one
        Checker__choice

            Checker__ordered_choice_many1
            Checker__ordered_choice_only_one
            Checker__ordered_choice

            Checker__unordered_choice_many1
            Checker__unordered_choice_only_one
            Checker__unordered_choice

        Checker__switch
        Checker__switch__with_case

            Checker__unordered_switch
            Checker__unordered_switch__with_case

            Checker__ordered_switch
            Checker__ordered_switch__with_case

    Checker__iterable
        mk_impl_class_checker
        Checker__namedtuple
            Checker__py_namedtuple_as_point

        Checker__py_Sequence_as_array
        Checker__py_Sequence_as_point
        Checker__py_Sequence_as_point__omit

            Checker__py_list_as_array
            Checker__py_list_as_point
            Checker__py_list_as_point__omit

            Checker__py_tuple_as_array
            Checker__py_tuple_as_point
            Checker__py_tuple_as_point__omit

        Checker__Mapping
        Checker__Mapping__item
        Checker__Mapping_as_record

            Checker__dict
            Checker__dict__item
            Checker__dict_as_record

            Checker__FrozenDict
            Checker__FrozenDict__item
            Checker__FrozenDict_as_record

            Checker__HalfFrozenDict
            Checker__HalfFrozenDict__item
            Checker__HalfFrozenDict_as_record

        Checker__Set
            Checker__set
            Checker__frozenset



mk_impl_class_checker
    mk_checker__array
    mk_checker__point
    mk_checker__pair
    mk_checker__pairs

    ConfigMixin__Lookupable
        ConfigMixin__Sequence
            ConfigMixin__list
            ConfigMixin__tuple

        ConfigMixin__Mapping
            ConfigMixin__dict
            ConfigMixin__FrozenDict
            ConfigMixin__HalfFrozenDict

    ConfigMixin__Set
        ConfigMixin__set
        ConfigMixin__frozenset























CheckException
    CheckError
        CheckError_Logic
        CheckError_Type
        CheckError_Value
    CheckFail
        CheckFail_Type
        CheckFail_Value
    CheckHelperExc
        CheckHelperExc_not_pseudo_checker
        CheckHelperExc_unknown


check_Lookupable
check_namedtuple_type
check_has_attrs
check_callable
check_subclass
check_instance
check_instance_all
check_type_is
check_tuple
check_len_eq
check_int
check_iterable
check_type_tree
    '''.split()
#]]]
if 0:
    get_last
    _4checker_bool_pairs
    _4bool
    _4checkers
    _4checker
#HHHHH

from seed.lang.class_property import class_property
from seed.abc.abc import abstractmethod, override, not_implemented, ABC
from seed.types.FrozenDict import FrozenDict, HalfFrozenDict
from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from seed.tiny import echo, fst, snd, at, print_err
from collections.abc import Mapping, Set, Sequence
from collections.abc import Container, Iterable

class CheckException(Exception):
    'base exc'

class CheckFail(CheckException):
    'raise by check() to impl verify()'
class CheckError(CheckException):
    'program bug'
class CheckHelperExc(CheckException):
    'program flow control'

class CheckError_Logic(CheckError):pass
class CheckError_Type(CheckError, TypeError):pass
class CheckError_Value(CheckError, ValueError):pass

class CheckFail_Type(CheckFail, TypeError):pass
class CheckFail_Value(CheckFail, ValueError):pass

class CheckHelperExc_not_pseudo_checker(CheckHelperExc, TypeError):pass
#class CheckHelperExc_Type(CheckHelperExc, TypeError):pass
#class CheckHelperExc_Value(CheckHelperExc, ValueError):pass
class CheckHelperExc_unknown(CheckHelperExc):pass



_cases = set('u t us ts n ns'.split())
def mk_checker(pseudo_checker):
    r'''
    :: PseudoChecker -> IChecker
    :: obj -> IChecker|raise CheckHelperExc_not_pseudo_checker/CheckHelperExc_unknown/Exception
    where:
        PseudoChecker = (IChecker|None|False|True|object|type|check_func|tuple<"u"/"t"/"us"/"ts"/"n"/"ns", recur...>)


    the_checker__is_None
    the_pass_checker
        != the_checker__is_True
    the_fail_checker
        != the_checker__is_False

    Checker__py_tuple_as_array  #array
    Checker__py_tuple_as_point  #tuple
    Checker__ordered_intersection #and/intersection
    Checker__ordered_union      #or/union/u<->n
        == Checker__ordered_choice
    Checker__check_func
        != Checker__verify_func
        != Checker__no_calc
        != Checker__check_then_calc_ex_func
    Checker__isinstance
        != Checker__type_is


    #'''
    Error = CheckHelperExc_not_pseudo_checker
    def this(x):
        if isinstance(x, IChecker):
            r = checker = x
        elif x is None:
            r = the_checker__is_None
        elif x is False:
            r = the_fail_checker
        elif x is True or x is object:
            r = the_pass_checker
        elif isinstance(x, type):
            cls = x
            r = Checker__isinstance(cls)
        elif callable(x):
            check_func = x
            r = Checker__check_func(check_func)
        elif type(x) is tuple:
            xs = x
            if not xs: raise Error("no fst; fst should be case")
            case, *xs = xs
            if type(case) is not str: raise Error("fst should be case::str : {type(case)}")
            cases = _cases
            if case not in cases:
                raise Error(f'bad case: {case!r} not in {cases!r}')

            it = map(this, xs)
            if case[0] == 'u':
                mk = Checker__ordered_union
            elif case[0] == 't':
                mk = Checker__py_tuple_as_point #point
                    # vs Checker__py_tuple_as_array
            elif case[0] == 'n':
                mk = Checker__ordered_intersection
            #elif case == 'us':
            #elif case == 'ts':
            #elif case == 'ns':
            else:
                raise CheckError_Logic(f'case={case!r}')
            r = mk(tuple(it))
            if case[-1] == 's':
                r = Checker__py_tuple_as_array(r)
        else:
            raise Error(f"not ICheckerEx: {type(x)}")
        assert isinstance(r, IChecker)
        return r
    if 1:
        return this(pseudo_checker)
    else:
        try:
            return this(pseudo_checker)
        except (Error, CheckHelperExc_unknown):
            raise
        except Exception as e:
            raise CheckHelperExc_unknown(e)


def check_PseudoChecker(x):
    "obj -> None|raise CheckFail_Type/CheckHelperExc_unknown/Exception  #see:mk_checker"
    Error = CheckHelperExc_not_pseudo_checker
    try:
        mk_checker(x)
    except Error:
        raise CheckFail_Type
    else:
        return

def check(pseudo_checker, obj):
    'PseudoChecker -> obj -> None|raise CheckFail/CheckHelperExc_unknown/CheckHelperExc_not_pseudo_checker/CheckError_Type/CheckException/Exception'
    try:
        checker = mk_checker(pseudo_checker)
            #CheckHelperExc_not_pseudo_checker
            #CheckHelperExc_unknown
    except CheckHelperExc:
        raise CheckError_Type

    f = type(checker).___check___
    if 1:
        r = f(checker, obj)
    else:
        try:
            r = f(checker, obj)
            "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        except (CheckFail, CheckHelperExc_unknown):
            raise
        except CheckHelperExc as e:
            raise CheckHelperExc_unknown(e)
        except (CheckException):
            raise
        except Exception as e:
            raise CheckHelperExc_unknown(e)
    if r is not None: raise CheckError_Type
    return

def verify(pseudo_checker, obj):
    'IChecker -> obj -> bool'
    try:
        check(pseudo_checker, obj)
    except CheckFail:
        return False
    else:
        return True


def verify_then_may_calc(pseudo_checker, obj):
    'IChecker -> obj -> maybe result'
    try:
        r = check_then_calc(pseudo_checker, obj)
    except CheckFail:
        return ()
    else:
        return (r,)
def verify_then_may_calc_ex(pseudo_checker, check_only, obj):
    'IChecker -> check_only -> obj -> (bool if check_only else maybe result)'
    f = verify if check_only else verify_then_may_calc
    return f(pseudo_checker, obj)



def check_then_calc(pseudo_checker, obj):
    'PseudoChecker -> obj -> result|raise CheckFail/CheckHelperExc_unknown/CheckHelperExc_not_pseudo_checker/CheckError_Type/CheckException/Exception'
    try:
        checker = mk_checker(pseudo_checker)
            #CheckHelperExc_not_pseudo_checker
            #CheckHelperExc_unknown
    except CheckHelperExc:
        raise CheckError_Type
    #if not isinstance(checker, ICheckCalcor): raise CheckError_Type

    f = type(checker).___check_then_calc___
    r = f(checker, obj)
    return r


def check_then_calc_ex(pseudo_checker, check_only:bool, obj):
    'PseudoChecker -> check_only::bool -> obj -> result|raise CheckFail/CheckHelperExc_unknown/CheckHelperExc_not_pseudo_checker/CheckError_Type/CheckException/Exception'
    if type(check_only) is not bool: raise CheckError_Type
    try:
        checker = mk_checker(pseudo_checker)
            #CheckHelperExc_not_pseudo_checker
            #CheckHelperExc_unknown
    except CheckHelperExc:
        raise CheckError_Type
    #if not isinstance(checker, ICheckCalcor): raise CheckError_Type

    f = type(checker).___check_then_calc_ex___
    r = f(checker, check_only, obj)
    if check_only and r is not None: raise CheckError_Type
    return r














#HHHHH

fst
snd
get_last = at[-1]

def check_Lookupable(obj):
    'check Lookupable __getitem__'
    check_has_attrs(type(obj), ('__getitem__',))
def check_namedtuple_type(obj):
    check_instance(type, obj)
    check_subclass(tuple, obj)
    check_has_attrs(obj, '_make _asdict _replace _fields _field_defaults'.split())

def check_has_attrs(obj, attrs):
    for attr in attrs:
        if not hasattr(obj, attr): raise CheckFail_Type
def check_callable(obj):
    if not callable(obj): raise CheckFail_Type
def check_subclass(cls, obj):
    if not issubclass(obj, cls): raise CheckFail_Type
def check_instance(cls, obj):
    if not isinstance(obj, cls): raise CheckFail_Type
def check_instance_all(cls, objs):
    for obj in objs:
        check_instance(cls, obj)
def check_type_is(cls, obj):
    if type(obj) is not cls: raise CheckFail_Type
def check_len_eq(sz, obj):
    if len(obj) != sz: raise CheckFail
def check_tuple(obj, *, cls=None, sz=None):
    check_type_is(tuple, obj)
    tpl = obj
    if cls is not None: check_instance_all(cls, tpl)
    if sz is not None:
        if len(tpl) != sz: raise CheckFail
def check_int(obj, *, eq=None, min=None, max=None):
    check_type_is(int, obj)
    i = obj
    if not (eq is None or eq == i): raise CheckFail
    if not (min is None or min <= i): raise CheckFail
    if not (max is None or i <= max): raise CheckFail
def check_iterable(obj):
    check_instance(Iterable, obj)
def check_type_tree(obj):
    'for isinstance/issubclass'
    def this(x):
        if type(x) is tuple:
            ys = x
            for y in ys:
                this(y)
        else:
            check_instance(type, x)
    this(obj)










#HHHHH
class IChecker(IReprImmutableHelper):
    #def ___get_args_kwargs___(sf):
    @abstractmethod
    def ___check___(sf, obj):
        "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        return check_then_calc_ex(True, sf, obj)
        check_then_calc(sf, obj)
        return
    @abstractmethod
    def ___check_then_calc___(sf, obj):
        "obj -> result|raise CheckFail/CheckHelperExc_unknown/Exception"
        return check_then_calc_ex(False, sf, obj)
        check(sf, obj)
        return obj
    @abstractmethod
    def ___check_then_calc_ex___(sf, check_only, obj):
        "check_only::bool -> obj -> (None if check_only else result)|raise CheckFail/CheckHelperExc_unknown/Exception"
        if check_only:
            return check(sf, obj) #to test None
        else:
            return check_then_calc(sf, obj)





    def __call__(sf, obj):
        "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        check(sf, obj)
    def check(sf, obj):
        "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        check(sf, obj)

    def __getitem__(sf, obj):
        "obj -> bool"
        return verify(sf, obj)
    def verify(sf, obj):
        "obj -> bool"
        return verify(sf, obj)


    def __invert__(sf):
        return Checker__inv(sf)
    def __and__(lhs, rhs):
        return Checker__ordered_intersection((lhs, rhs))
    def __or__(lhs, rhs):
        return Checker__ordered_union((lhs, rhs))
    def __mul__(lhs, rhs):
        return mk_checker__pair(lhs, rhs)
    def __sub__(lhs, rhs):
        return lhs & ~rhs
    def __xor__(lhs, rhs):
        return Checker__if_else(False, lhs, ~rhs, rhs)

#class ICheckCalcor(IChecker):
    def __neg__(sf):
        '(obj->new) -> obj -> obj'
        if isinstance(sf, ICheckEchor):
            return sf
        return Checker__no_calc(sf)
        return Checker__check_func(sf)
        return CheckCalcor__DAG_star(True, ((sf, False),))>>fst
            #avoid calc
            #use check() instead of check_then_calc()
        return (+sf)>>fst
    def __pos__(sf):
        '(obj->new) -> obj -> (obj, new)'
        return CheckCalcor__DAG_line(True, ((sf, True),))
    def __add__(lhs, rhs):
        '(obj->new0) -> (obj->new1) -> obj -> ((0,new0)|(1,new1))'
        return Checker__ordered_choice((lhs, rhs))
        # vs __or__
        #return Checker__ordered_union((lhs, rhs))

    def __pow__(lhs, rhs):
        '(obj->new0) -> (obj->new1) -> obj -> (new0, new1)'
        return CheckCalcor__DAG_star(False, ((lhs, True), (rhs, True)))
    def __divmod__(lhs, rhs):
        '(obj->new0) -> (new0->new1) -> obj -> (new0, new1)'
        return CheckCalcor__DAG_line(False, ((lhs, True), (rhs, True)))
    def __floordiv__(lhs, rhs):
        '(obj->new0) -> (new0->new1) -> obj -> new0'
        return CheckCalcor__DAG_line(False, ((lhs, True), (rhs, False)))>>at[0]
            #avoid calc
            #use check() instead of check_then_calc()
        return divmod(lhs, rhs)>>fst
    def __mod__(lhs, rhs):
        '(obj->new0) -> (new0->new1) -> obj -> new1'
        return CheckCalcor__DAG_line(False, ((lhs, False), (rhs, True)))>>at[0]
        return divmod(lhs, rhs)>>snd
    def __truediv__(lhs, rhs):
        '(obj->new0) -> (new0->new1) -> obj -> obj'
        return CheckCalcor__DAG_line(True, ((lhs, False), (rhs, False)))>>fst
        return -(lhs//rhs)
    def __matmul__(sf, f):
        '(obj->new) -> f(new->bool) -> obj -> new'
        return sf//Checker__verify_func(f)
    def __lshift__(sf, f):
        '(obj->new0) -> f(old->new1) -> obj -> new1'
        return CheckCalcor__transform(False, sf, f)
    def __rshift__(sf, f):
        '(obj->new0) -> f(new0->new1) -> obj -> new1'
        return CheckCalcor__transform(True, sf, f)




#HHHHH
class ____0:pass
class ____1:pass
class ICheckEchor(____1, ____0, IChecker):
    #def ___check___(sf, obj):
    @override
    def ___check_then_calc___(sf, obj):
        "obj -> result|raise CheckFail/CheckHelperExc_unknown/Exception"
        check(sf, obj)
        return obj #echo@ICheckEchor
    @override
    def ___check_then_calc_ex___(sf, check_only, obj):
        "check_only::bool -> obj -> (None if check_only else result)|raise CheckFail/CheckHelperExc_unknown/Exception"
        if check_only:
            return check(sf, obj) #to test None
        else:
            return check_then_calc(sf, obj)



class ICheckCalcor(____0, ____1, IChecker):
    #def ___check_then_calc_ex___(sf, check_only, obj):
    @override
    def ___check___(sf, obj):
        "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        return check_then_calc_ex(True, sf, obj)
    @override
    def ___check_then_calc___(sf, obj):
        "obj -> result|raise CheckFail/CheckHelperExc_unknown/Exception"
        return check_then_calc_ex(False, sf, obj)














#HHHHH
class _IChecker_with_args(IChecker):
  if 1:
    __x__ICheckEchor = False
    __x__ICheckCalcor = False
  def __init_subclass__(cls, /, **kwargs):
    r'''
    ensure ICheckEchor/\ICheckCalcor=={} forced by ____0&____1
    ensure ICheckEchor/\IChecker_with_args <= ICheckEchor_with_args
    ensure ICheckCalcor/\IChecker_with_args <= ICheckCalcor_with_args
    $'''
    super().__init_subclass__(**kwargs)
    i = 0
    if issubclass(cls, ICheckEchor):
        i += 1
        try:
            super_cls = ICheckEchor_with_args
        except NameError:
            if __class__.__x__ICheckEchor:
                raise CheckError_Logic
            __class__.__x__ICheckEchor = True
        else:
            if not issubclass(cls, super_cls): raise CheckError_Type(fr'not issubclass({cls!r}, {super_cls!r})')


    else: pass
    ##
    if issubclass(cls, ICheckCalcor):
        i += 1
        try:
            super_cls = ICheckCalcor_with_args
        except NameError:
            if __class__.__x__ICheckCalcor:
                raise CheckError_Logic
            __class__.__x__ICheckCalcor = True
        else:
            if not issubclass(cls, super_cls): raise CheckError_Type(fr'not issubclass({cls!r}, {super_cls!r})')
    else: pass

    if i > 1: raise CheckError_Logic('____0 ____1 not work!')


#def _std_argX_(cls, argX): return argX

class IChecker_with_args(_IChecker_with_args):
    @class_property
    @abstractmethod
    def _may_num_args_(cls):
        'None/uint'

    @classmethod
    def _post_check_args_(cls, *args):
        'post: after _std_arg0_ ...'
        return
    r'''
    @classmethod
    def _std_arg0_(cls, arg0):
        return arg0
    #'''
    @override
    def ___get_args_kwargs___(sf):
        return sf.__args, {}
    @classmethod
    @abstractmethod
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [] = args
    @classmethod
    @abstractmethod
    def _check_then_calc_with_args_(cls, args, obj):
        "args -> obj -> result|raise CheckFail/Exception"
        [] = args
    @classmethod
    @abstractmethod
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        "args -> check_only -> obj -> (None if check_only else result)|raise CheckFail/Exception"
        [] = args


    def __new__(cls, *args):
        may_num_args = cls._may_num_args_
        if may_num_args is not None:
            num_args = may_num_args
            if len(args) != num_args: raise CheckError_Type

        sf = super().__new__(cls)
        if cls is not type(sf): raise CheckError_Type
        ls = []
        _std_argX_ = echo
        for i, x in enumerate(args):
            attr = f'_std_arg{i}_'
            std = getattr(cls, attr, _std_argX_)
            #bug: y = std(cls, x)
            y = std(x) #classmethod
            ls.append(y)
        ls = (*ls,)

        r = cls._post_check_args_(*ls)
        if r is not None: raise CheckError_Type
        sf.__args = ls
            # Checker__inv get _IChecker_with_args__args
        return sf
    @override
    def ___check___(sf, obj):
        "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        return type(sf)._check_with_args_(sf.__args, obj) #return to test None
    @override
    def ___check_then_calc___(sf, obj):
        "obj -> result|raise CheckFail/CheckHelperExc_unknown/Exception"
        return type(sf)._check_then_calc_with_args_(sf.__args, obj)
    @override
    def ___check_then_calc_ex___(sf, check_only, obj):
        "check_only::bool -> obj -> (None if check_only else result)|raise CheckFail/CheckHelperExc_unknown/Exception"
        return type(sf)._check_then_calc_ex_with_args_(sf.__args, check_only, obj)


class ICheckCalcor_with_args(IChecker_with_args, ICheckCalcor):
    #def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        check_only = True
        return cls._check_then_calc_ex_with_args_(args, check_only, obj)
    @classmethod
    @override
    def _check_then_calc_with_args_(cls, args, obj):
        "args -> obj -> result|raise CheckFail/Exception"
        check_only = False
        try:
            return cls._check_then_calc_ex_with_args_(args, check_only, obj)
        except TypeError as e:
            if type(e) is TypeError:
                print_err(cls)
            raise

class ICheckEchor_with_args(IChecker_with_args, ICheckEchor):
    #def _check_with_args_(cls, args, obj):
    @classmethod
    @override
    def _check_then_calc_with_args_(cls, args, obj):
        "args -> obj -> result|raise CheckFail/Exception"
        r = cls._check_with_args_(args, obj) #return to test None
        if r is not None: raise CheckError_Type
        return obj
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        "args -> check_only -> obj -> (None if check_only else result)|raise CheckFail/Exception"
        r = cls._check_then_calc_with_args_(args, obj)
        if r is not obj: raise CheckError_Logic
        return None if check_only else obj


class ICheckEchor_with_args__verify4check(ICheckEchor_with_args):
    @classmethod
    @abstractmethod
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        b = cls._verify_with_args_(args, obj)
        #check_type_is(bool, r)
        if type(b) is not bool: raise CheckError_Type
        if not b: raise CheckFail
        return

@classmethod
@override
def _std_arg4checker(cls, arg):
    checker = arg
    check_instance(IChecker, checker)
    return arg
    #return mk_checker(arg)
@classmethod
@override
def _std_arg4checkers(cls, arg):
    checkers = arg
    check_tuple(checkers, cls=IChecker)
    return arg
@classmethod
@override
def _std_arg4callable(cls, arg):
    func = arg
    check_callable(func)
    return arg
@classmethod
@override
def _std_arg4type(cls, arg):
    check_instance(type, arg)
    return arg
@classmethod
@override
def _std_arg4int(cls, arg):
    check_type_is(int, arg)
    return arg
@classmethod
@override
def _std_arg4uint(cls, arg):
    check_int(arg, min=0)
    return arg
@classmethod
@override
def _std_arg4bool(cls, arg):
    check_type_is(bool, arg)
    return arg
@classmethod
@override
def _std_arg4Container(cls, arg):
    check_instance(Container, arg)
    return arg
@classmethod
@override
def _std_arg4checker_bool_pairs(cls, arg):
    _4checker_bool_pairs(arg)
    return arg
    _4checker_bool_pairs(checker_hold_result_pairs)
@classmethod
@override
def _std_arg4checkers_or_key2checker(cls, arg):
    try:
        return _std_arg4checkers.__func__(cls, arg)
    except CheckFail:
        pass
    return _std_arg4key2checker.__func__(cls, arg)
@classmethod
@override
def _std_arg4key2checker(cls, arg):
    #check_instance(Mapping, arg)
    check_type_is(FrozenDict, arg)
    check_instance_all(IChecker, arg.values())
    return arg
@classmethod
@override
def _std_arg4frozenset(cls, arg):
    check_type_is(frozenset, arg)
    return arg
@classmethod
@override
def _std_arg4type_tree(cls, arg):
    check_type_tree(arg)
    return arg






class IChecker_with_args__arg0_is_checker(IChecker_with_args):
    _std_arg0_ = _std_arg4checker

class IChecker_with_args__arg0_is_checkers(IChecker_with_args):
    _std_arg0_ = _std_arg4checkers

class IChecker_with_args__arg0_is_callable(IChecker_with_args):
    _std_arg0_ = _std_arg4callable

class IChecker_with_args__arg0_is_type_tree(IChecker_with_args):
    _std_arg0_ = _std_arg4type_tree

class IChecker_with_args__arg0_is_type(IChecker_with_args):
    _std_arg0_ = _std_arg4type

class IChecker_with_args__arg0_is_uint(IChecker_with_args):
    _std_arg0_ = _std_arg4uint

class IChecker_with_args__arg0_is_int(IChecker_with_args):
    _std_arg0_ = _std_arg4int

class IChecker_with_args__arg0_is_bool(IChecker_with_args):
    _std_arg0_ = _std_arg4bool

class IChecker_with_args__arg0_is_Container(IChecker_with_args):
    _std_arg0_ = _std_arg4Container

class IChecker_with_args__arg0_is_key2checker(IChecker_with_args):
    _std_arg0_ = _std_arg4key2checker

class IChecker_with_args__arg0_is_checkers_or_key2checker(IChecker_with_args):
    _std_arg0_ = _std_arg4checkers_or_key2checker




###################################
class IChecker_with_args__arg1_is_checker(IChecker_with_args):
    _std_arg1_ = _std_arg4checker

class IChecker_with_args__arg1_is_checkers(IChecker_with_args):
    _std_arg1_ = _std_arg4checkers

class IChecker_with_args__arg1_is_callable(IChecker_with_args):
    _std_arg1_ = _std_arg4callable

class IChecker_with_args__arg1_is_type(IChecker_with_args):
    _std_arg1_ = _std_arg4type

class IChecker_with_args__arg1_is_uint(IChecker_with_args):
    _std_arg1_ = _std_arg4uint

class IChecker_with_args__arg1_is_int(IChecker_with_args):
    _std_arg1_ = _std_arg4int

class IChecker_with_args__arg1_is_checker_bool_pairs(IChecker_with_args):
    _std_arg1_ = _std_arg4checker_bool_pairs










#HHHHH
class IChecker_one_arg(IChecker_with_args):
    _may_num_args_ = 1
    r'''
    @classmethod
    def _std_arg0_(cls, arg0):
        return arg0
    #'''

class ICheckEchor_one_arg__verify(IChecker_one_arg, ICheckEchor_with_args__verify4check):pass


class IChecker_one_arg__checker(IChecker_with_args__arg0_is_checker, IChecker_one_arg):pass
class IChecker_one_arg__checkers(IChecker_with_args__arg0_is_checkers, IChecker_one_arg):pass
class IChecker_one_arg__callable(IChecker_with_args__arg0_is_callable, IChecker_one_arg):pass
class IChecker_one_arg__uint(IChecker_with_args__arg0_is_uint, IChecker_one_arg):pass
class IChecker_one_arg__int(IChecker_with_args__arg0_is_int, IChecker_one_arg):pass
class IChecker_one_arg__key2checker(IChecker_with_args__arg0_is_key2checker, IChecker_one_arg):pass
class IChecker_one_arg__checkers_or_key2checker(IChecker_with_args__arg0_is_checkers_or_key2checker, IChecker_one_arg):pass


class ICheckEchor_one_arg__type_tree__verify(IChecker_with_args__arg0_is_type_tree, ICheckEchor_one_arg__verify):pass
class ICheckEchor_one_arg__type__verify(IChecker_with_args__arg0_is_type, ICheckEchor_one_arg__verify):pass


class ICheckEchor_one_arg__Container__verify(IChecker_with_args__arg0_is_Container, ICheckEchor_one_arg__verify):pass
Container







#HHHHH

class IChecker_two_args(IChecker_with_args):
    _may_num_args_ = 2
class IChecker_two_args__arg0_is_checker(IChecker_with_args__arg0_is_checker, IChecker_two_args):pass
class IChecker_two_args__arg0_is_uint(IChecker_with_args__arg0_is_int, IChecker_two_args):pass
class IChecker_two_args__arg0_is_bool(IChecker_with_args__arg0_is_bool, IChecker_two_args):pass
class IChecker_two_args__arg0_is_int(IChecker_with_args__arg0_is_int, IChecker_two_args):pass
class IChecker_two_args__arg1_is_int(IChecker_with_args__arg1_is_int, IChecker_two_args):pass
class IChecker_two_args__args_are_int(IChecker_with_args__arg1_is_int, IChecker_with_args__arg0_is_int, IChecker_two_args):pass




class IChecker_two_args__arg1_is_checker(IChecker_with_args__arg1_is_checker, IChecker_two_args):pass
class IChecker_two_args__arg1_is_checkers(IChecker_with_args__arg1_is_checkers, IChecker_two_args):pass
class IChecker_two_args__arg0_is_bool__arg1_is_checker_bool_pairs(IChecker_with_args__arg1_is_checker_bool_pairs, IChecker_two_args__arg0_is_bool):pass
class ICheckCalcor_two_args__hold_input__checker_hold_result_pairs(IChecker_two_args__arg0_is_bool__arg1_is_checker_bool_pairs, ICheckCalcor_with_args):
    r'''
    'args = (hold_input::bool, checker_hold_result_pairs::[(IChecker, hold_result::bool)])'
    #'''

    _may_num_args_ = 2
    _std_arg0_ = _std_arg4bool
    _std_arg1_ = _std_arg4checker_bool_pairs
    def __new__(cls, hold_input:bool, checker_hold_result_pairs):
        sf = super().__new__(cls, hold_input, checker_hold_result_pairs)
        return sf

























#HHHHH

class IChecker_no_args(ICheckEchor):
    __cls2sf = {}
    def __new__(cls):
        d = __class__.__cls2sf
        m = d.get(cls)
        if m is not None: return m
        sf = super().__new__(cls)
        d[cls] = sf
        return sf
    @override
    def ___get_args_kwargs___(sf):
        return [], {}
class Checker__fail(IChecker_no_args):
    'fail'
    @override
    def ___check___(sf, obj):
        "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        raise CheckFail
    @override
    def __invert__(sf):
        return the_pass_checker

class Checker__pass(IChecker_no_args):
    'pass'
    @override
    def ___check___(sf, obj):
        "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        return
    @override
    def __invert__(sf):
        return the_fail_checker
the_pass_checker = Checker__pass()
the_fail_checker = Checker__fail()

class Checker__hashable(IChecker_no_args):
    @override
    def ___check___(sf, obj):
        "obj -> None|raise CheckFail/CheckHelperExc_unknown/Exception"
        try:
            hash(obj)
        except:
            raise CheckFail
the_hashable_checker = Checker__hashable()





class ICheckCalcor__DAG_width_depth(ICheckCalcor_with_args):
    r'''
    'args = (hold_input::bool, checker_hold_result_pairs::[(IChecker, bool)])'
    'obj -> [obj?, new0?, ...]'
    #'''
    _may_num_args_ = 2
    _std_arg0_ = _std_arg4bool
    _std_arg1_ = _std_arg4checker_bool_pairs
    def __new__(cls, hold_input:bool, checker_hold_result_pairs):
        sf = super().__new__(cls, hold_input, checker_hold_result_pairs)
        return sf

    @class_property
    @abstractmethod
    def _width_(cls):
        'bool: depth(line) or width(star)'

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [h, ps] = [hold_input, checker_hold_result_pairs] = args
        depth = not cls._width_
        calc = not check_only

        if calc:
            ls = []
        def hold(b):
            return calc and b
        if hold(h):
            ls.append(obj)

        pairs = ps
        if depth:
            i_skip = len(pairs)
            if pairs and not hold(pairs[-1][1]):
                i_skip -= 1

        for i, (checker, hold_result) in enumerate(pairs):
            not_skip = depth and i != i_skip
            hold_result = hold(hold_result)
            if hold_result or not_skip:
                r = check_then_calc(checker, obj)
            else:
                check(checker, obj)
            if hold_result:
                ls.append(r)
            if not_skip:
                #depth line #may without last
                obj = r
            r = 0; del r
        return (*ls,) if calc else None
class CheckCalcor__DAG_star(ICheckCalcor__DAG_width_depth):
    _width_ = True
class CheckCalcor__DAG_line(ICheckCalcor__DAG_width_depth):
    _width_ = False


class CheckCalcor__transform(ICheckCalcor_with_args):
    _may_num_args_ = 3
    _std_arg0_ = _std_arg4bool
    _std_arg1_ = _std_arg4checker
    _std_arg2_ = _std_arg4callable

    def __new__(cls, to_continue:bool, pre_checker, transform):
        sf = super().__new__(cls, to_continue, pre_checker, transform)
        return sf

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [to_continue, pre_checker, transform] = args
        if check_only or not to_continue:
            check(pre_checker, obj)
            src = obj
        else:
            mid = check_then_calc(pre_checker, obj)
            src = mid

        if check_only:
            r = None
        else:
            new = transform(src)
            r = new
        return r



class Checker__if_else(ICheckCalcor_with_args):
    _may_num_args_ = 4
    _std_arg0_ = _std_arg4bool
    _std_arg1_ = _std_arg4checker
    _std_arg2_ = _std_arg4checker
    _std_arg3_ = _std_arg4checker

    def __new__(cls, to_continue:bool, if_checker, then_checker, else_checker):
        sf = super().__new__(cls, to_continue, if_checker, then_checker, else_checker)
        return sf

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [to_continue, if_checker, then_checker, else_checker] = args

        bm = verify_then_may_calc_ex(if_checker, not to_continue, obj)
        if bm and to_continue:
            [src] = m = bm
        else:
            src = obj
        if bm:
            next_checker = then_checker
        else:
            next_checker = else_checker

        return check_then_calc_ex(next_checker, check_only, src)





class Checker__no_calc(IChecker_one_arg__checker, ICheckEchor_with_args):
    '==? Checker__check_func?'
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [checker] = args
        check(checker, obj)

class Checker__inv(IChecker_one_arg__checker, ICheckEchor_with_args):
    'not'
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [checker] = args
        if verify(checker, obj):
            raise CheckFail
    @override
    def __invert__(sf):
        #####################
        #####################
        #####################
        [checker] = sf._IChecker_with_args__args
        #####################
        #####################
        #####################
        return checker




























#HHHHH
class ConfigMixin__Lookupable:
    _base_Lookupable_ = Lookupable = (Mapping, Sequence)
    _type_is_base_Lookupable_ = False
    @classmethod
    def _iter_items_(cls, obj):
        '_iter_items4Sequence_, _iter_items4Mapping_'
        if isinstance(obj, Mapping):
            return cls._iter_items4Mapping_(obj)
        elif isinstance(obj, Sequence):
            return cls._iter_items4Sequence_(obj)
        else:
            raise CheckError_Type
    @classmethod
    def _iter_keys_(cls, obj):
        '_iter_keys4Sequence_, _iter_keys4Mapping_'
        if isinstance(obj, Mapping):
            return cls._iter_keys4Mapping_(obj)
        elif isinstance(obj, Sequence):
            return cls._iter_keys4Sequence_(obj)
        else:
            raise CheckError_Type
    @classmethod
    def _iter_values_(cls, obj):
        '_iter_values4Sequence_, _iter_values4Mapping_'
        if isinstance(obj, Mapping):
            return cls._iter_values4Mapping_(obj)
        elif isinstance(obj, Sequence):
            return cls._iter_values4Sequence_(obj)
        else:
            raise CheckError_Type
    @classmethod
    def _lookup_(cls, k, obj):
        return obj[k]
        LookupError
    @classmethod
    def _has_key_(cls, k, obj):
        try:
            cls._lookup_(k)
        except LookupError:
            return False
        else:
            return True
    @classmethod
    def _iter_values4Sequence_(cls, obj):
        seq = obj
        return iter(seq)
    @classmethod
    def _iter_values4Mapping_(cls, obj):
        d = obj
        return iter(d.values())
    @classmethod
    def _iter_keys4Sequence_(cls, obj):
        seq = obj
        return iter(range(len(seq)))
    @classmethod
    def _iter_keys4Mapping_(cls, obj):
        d = obj
        return iter(d.keys())
    @classmethod
    def _iter_items4Sequence_(cls, obj):
        seq = obj
        return enumerate(seq)
    @classmethod
    def _iter_items4Mapping_(cls, obj):
        d = obj
        return iter(d.items())

    @classmethod
    def _check_by_base_Lookupable_(cls, obj):
        if cls._type_is_base_Lookupable_:
            check_type_is(cls._base_Lookupable_, obj)
        else:
            check_instance(cls._base_Lookupable_, obj)


class ConfigMixin__Mapping(ConfigMixin__Lookupable):
    @class_property
    @override
    def _base_Lookupable_(cls):
        return cls._base_Mapping_
    @class_property
    @override
    def _type_is_base_Mapping_(cls):
        return cls._type_is_base_Mapping_
    _iter_items_ = ConfigMixin__Lookupable._iter_items4Mapping_
    _iter_keys_ = ConfigMixin__Lookupable._iter_keys4Mapping_
    _iter_values_ = ConfigMixin__Lookupable._iter_values4Mapping_
    @classmethod
    @override
    def _check_by_base_Lookupable_(cls, obj):
        return cls._check_by_base_Mapping_(obj)

    _base_Mapping_ = Mapping
    _type_is_base_Mapping_ = False
    _output_dict_transform4as_record_ = FrozenDict

    @classmethod
    def _check_by_base_Mapping_(cls, obj):
        if cls._type_is_base_Mapping_:
            check_type_is(cls._base_Mapping_, obj)
        else:
            check_instance(cls._base_Mapping_, obj)
class ConfigMixin__FrozenDict(ConfigMixin__Mapping):
    _base_Mapping_ = FrozenDict
    _type_is_base_Mapping_ = True
class ConfigMixin__HalfFrozenDict(ConfigMixin__Mapping):
    _base_Mapping_ = HalfFrozenDict
    _type_is_base_Mapping_ = True
class ConfigMixin__dict(ConfigMixin__Mapping):
    _base_Mapping_ = dict
    _type_is_base_Mapping_ = True


class ConfigMixin__Set:
    _base_Set_ = Set
    _type_is_base_Set_ = False

    @classmethod
    def _check_by_base_Set_(cls, obj):
        if cls._type_is_base_Set_:
            check_type_is(cls._base_Set_, obj)
        else:
            check_instance(cls._base_Set_, obj)
class ConfigMixin__set(ConfigMixin__Set):
    _base_Set_ = set
    _type_is_base_Set_ = True
class ConfigMixin__frozenset(ConfigMixin__Set):
    _base_Set_ = frozenset
    _type_is_base_Set_ = True


class ConfigMixin__Sequence(ConfigMixin__Lookupable):
    @class_property
    @override
    def _base_Lookupable_(cls):
        return cls._base_Sequence_
    @class_property
    @override
    def _type_is_base_Mapping_(cls):
        return cls._type_is_base_Sequence_
    _iter_items_ = ConfigMixin__Lookupable._iter_items4Sequence_
    _iter_keys_ = ConfigMixin__Lookupable._iter_keys4Sequence_
    _iter_values_ = ConfigMixin__Lookupable._iter_values4Sequence_
    @classmethod
    @override
    def _check_by_base_Lookupable_(cls, obj):
        return cls._check_by_base_Sequence_(obj)


    _base_Sequence_ = Sequence
    _type_is_base_Sequence_ = False

    @classmethod
    def _check_by_base_Sequence_(cls, obj):
        if cls._type_is_base_Sequence_:
            check_type_is(cls._base_Sequence_, obj)
        else:
            check_instance(cls._base_Sequence_, obj)
class ConfigMixin__list(ConfigMixin__Sequence):
    _base_Sequence_ = list
    _type_is_base_Sequence_ = True
class ConfigMixin__tuple(ConfigMixin__Sequence):
    _base_Sequence_ = tuple
    _type_is_base_Sequence_ = True









#HHHHH
class Checker__ordered_intersection(IChecker_one_arg__checkers, ICheckCalcor_with_args):
    'and'
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [checkers] = args
        if check_only:
            for checker in checkers:
                check(checker, obj)
            return
        else:
            return tuple(check_then_calc(checker, obj) for checker in checkers)



r""""
        Checker__ordered_choice_many1
        Checker__ordered_choice_only_one
        Checker__ordered_choice
class Checker__ordered_choice(IChecker_one_arg__checkers, ICheckCalcor_with_args):
    r'''
    'either'
    'ordered_choice :: [(i->o)] -> i -> (i,o)'
    'unordered_choice :: {k:(i->o)} -> i -> (k,o)'
    Checker__unordered_choice
        vs Checker__ordered_choice
    #'''

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [checkers] = args
        for i, checker in enumerate(checkers):
            bm = verify_then_may_calc_ex(checker, check_only, obj)
            if bm:
                break
        else:
            raise CheckFail
        i, bm
        if check_only:
            r = None
        else:
            [x] = m = bm
            r = i, x
        #bug: return i, r
        return r
Checker__ordered_union = Checker__ordered_choice
#"""

r'''
class Checker__ordered_union(IChecker_one_arg__checkers):
    'or'
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [checkers] = args
        for checker in checkers:
            if verify(checker, obj):
                return
        else:
            raise CheckFail
#'''

#HHHHH
class IChecker__choice_or_switch(ConfigMixin__Lookupable, IChecker_one_arg, ICheckCalcor_with_args):
    _std_arg0_ = _std_arg4checkers
    _std_arg0_ = _std_arg4key2checker
    _std_arg0_ = _std_arg4checkers_or_key2checker
    @class_property
    @abstractmethod
    def _std_arg0_(cls, arg0):
        return arg0




class IChecker__unordered_choice_or_switch(ConfigMixin__Mapping, IChecker__choice_or_switch):
    'should before Checker__switch/...'
    _std_arg0_ = _std_arg4key2checker
class IChecker__ordered_choice_or_switch(ConfigMixin__Sequence, IChecker__choice_or_switch):
    'should before Checker__switch/...'
    _std_arg0_ = _std_arg4checkers




class Checker__switch(IChecker__choice_or_switch):
    r'''switch
    unordered_switch :: {k:(i->o)} -> (k,i) -> o
    ordered_switch :: [(i->o)] -> (k,i) -> o
    Checker__unordered_switch
        vs Checker__ordered_switch
    #'''
    _std_arg0_ = _std_arg4checkers_or_key2checker
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [key2checker] = args
        check_tuple(obj, sz=2)
        case, x = obj
        checker = key2checker[case]
            #TypeError/LookupError
        z = check_then_calc_ex(checker, check_only, x) # x not obj
            # not with case
        if check_only:
            return
        else:
            return z # not with case
class Checker__unordered_switch(IChecker__unordered_choice_or_switch, Checker__switch):
    _std_arg0_ = _std_arg4key2checker
class Checker__ordered_switch(IChecker__ordered_choice_or_switch, Checker__switch):
    _std_arg0_ = _std_arg4checkers






class Checker__switch__with_case(IChecker__choice_or_switch):
    r'''switch__with_case
    unordered_switch__with_case :: {k:((k,i)->o)} -> (k,i) -> (k,o)
    ordered_switch__with_case :: [((k,i)->o)] -> (k,i) -> (k,o)
    Checker__unordered_switch__with_case
        vs Checker__ordered_switch__with_case
    #'''
    _std_arg0_ = _std_arg4checkers_or_key2checker
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [key2checker] = args
        check_tuple(obj, sz=2)
        case, x = obj
        checker = key2checker[case]
            #TypeError/LookupError
        z = check_then_calc_ex(checker, check_only, obj) # obj not x
        if check_only:
            return
        else:
            return case, z
class Checker__unordered_switch__with_case(IChecker__unordered_choice_or_switch, Checker__switch__with_case):
    _std_arg0_ = _std_arg4key2checker
class Checker__ordered_switch__with_case(IChecker__ordered_choice_or_switch, Checker__switch__with_case):
    _std_arg0_ = _std_arg4checkers





class Checker__choice_many1(IChecker__choice_or_switch):
    r'''choice_many1
    'unordered_choice_many1 :: {k:(i->o)} -> i -> {k:o}{len>=1}'
    'ordered_choice_many1 :: [(i->o)] -> i -> {k:o}{len>=1}'
    Checker__unordered_choice_many1
        vs Checker__ordered_choice_many1
    #'''
    _std_arg0_ = _std_arg4checkers_or_key2checker
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [key2checker] = args
        d = {}
        it = cls._iter_items_(key2checker)
        for k, checker in it:
            bm = verify_then_may_calc_ex(checker, check_only, obj)
            if bm:
                if check_only: return # >=1
                [x] = bm
                d[k] = x
        if not d: raise CheckFail # ==0
        # >=1
        if check_only: raise CheckError_Logic
        return FrozenDict(d)
class Checker__unordered_choice_many1(IChecker__unordered_choice_or_switch, Checker__choice_many1):
    _std_arg0_ = _std_arg4key2checker
class Checker__ordered_choice_many1(IChecker__ordered_choice_or_switch, Checker__choice_many1):
    _std_arg0_ = _std_arg4checkers


class Checker__choice_only_one(IChecker__choice_or_switch):
    r'''choice_only_one
    'unordered_choice_only_one :: {k:(i->o)} -> i -> (k,o)'
    'ordered_choice_only_one :: [(i->o)] -> i -> (k,o)'
    Checker__unordered_choice_only_one
        vs Checker__ordered_choice_only_one
    #'''
    _std_arg0_ = _std_arg4checkers_or_key2checker
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [key2checker] = args
        m = ()
        it = cls._iter_items_(key2checker)
        for k, checker in it:
            bm = verify_then_may_calc_ex(checker, check_only, obj)
            if bm:
                if m: raise CheckFail # >=2
                m = (k,bm)
        if not m: raise CheckFail # ==0
        # ==1
        (k, bm) = m
        if check_only:
            return
        else:
            [x] = bm
            return (k, x)
class Checker__unordered_choice_only_one(IChecker__unordered_choice_or_switch, Checker__choice_only_one):
    _std_arg0_ = _std_arg4key2checker
class Checker__ordered_choice_only_one(IChecker__ordered_choice_or_switch, Checker__choice_only_one):
    _std_arg0_ = _std_arg4checkers



class Checker__choice(IChecker__choice_or_switch):
    r'''choice
    'unordered_choice :: {k:(i->o)} -> i -> (k,o)'
    'ordered_choice :: [(i->o)] -> i -> (k,o)'
    Checker__unordered_choice
        vs Checker__ordered_choice
    #'''
    _std_arg0_ = _std_arg4checkers_or_key2checker
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [key2checker] = args
        it = cls._iter_items_(key2checker)
        for k, checker in it:
            bm = verify_then_may_calc_ex(checker, check_only, obj)
            if bm: break
        else:
            raise CheckFail
        k, bm
        if check_only:
            return
        else:
            [x] = bm
            return (k, x)
class Checker__unordered_choice(IChecker__unordered_choice_or_switch, Checker__choice):
    _std_arg0_ = _std_arg4key2checker
class Checker__ordered_choice(IChecker__ordered_choice_or_switch, Checker__choice):
    _std_arg0_ = _std_arg4checkers
Checker__ordered_union = Checker__ordered_choice































#HHHHH
class Checker__all(IChecker_one_arg__checker, ICheckCalcor_with_args):
    'iterable'
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [checker] = args
        check_iterable(obj)
        iterable = obj
        if check_only:
            for x in iterable:
                check(checker, x)
            return
        else:
            return tuple(check_then_calc(checker, x) for x in iterable)

Checker__iterable = Checker__all



def mk_impl_class_checker(type_is_impl_cls, impl_cls, interface_pseudo_checker):
    r'''vivi ConfigMixin__Mapping
    eg:
        type_is_impl_cls = True
        impl_cls=FrozenDict
        interface = Mapping
        interface_checker=T(...)
            T = Checker__Mapping/Checker__Mapping__item/Checker__Mapping_as_record
    #'''
    _4bool(type_is_impl_cls)
    if type_is_impl_cls:
        impl_cls_checker = Checker__type_is(impl_cls)
    else:
        impl_cls_checker = Checker__isinstance(impl_cls)
    interface_checker = mk_checker(interface_pseudo_checker)
    concrete_type_checker = impl_cls_checker
    api_and_data_checker = interface_checker
    return concrete_type_checker & api_and_data_checker


class Checker__py_Sequence_as_array(ConfigMixin__Sequence, IChecker_one_arg__checker, ICheckCalcor_with_args):
    'Sequence<T>'

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [checker] = args
        #check_tuple(obj)
        cls._check_by_base_Sequence_(obj)
        seq = obj
        return Checker__all._check_then_calc_ex_with_args_(args, check_only, seq)

class Checker__py_list_as_array(ConfigMixin__list, Checker__py_Sequence_as_array):
    'list<T>'
class Checker__py_tuple_as_array(ConfigMixin__tuple, Checker__py_Sequence_as_array):
    'tuple<T>'

def mk_checker__array(pseudo_checker):
    checker = mk_checker(pseudo_checker)
    return Checker__py_tuple_as_array(checker)

class Checker__py_Sequence_as_point(ConfigMixin__Sequence, IChecker_one_arg__checkers, ICheckCalcor_with_args):
    r'''
    'Sequence<T,...>'

    vs:
        Checker__namedtuple #namedtuple
        Checker__py_Sequence_as_point tuple
    #'''

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [checkers] = args
        #check_tuple(obj, sz=len(checkers))
        cls._check_by_base_Sequence_(obj)
        seq = obj
        return _check_then_calc_ex_with_args4point(-1, checkers, check_only, seq)

class Checker__py_list_as_point(ConfigMixin__list, Checker__py_Sequence_as_point):
    'list<T,...>'
class Checker__py_tuple_as_point(ConfigMixin__tuple, Checker__py_Sequence_as_point):
    'tuple<T,...>'


def mk_checker__point(*pseudo_checkers):
    it = map(mk_checker, pseudo_checkers)
    return Checker__py_tuple_as_point((*it,))
def mk_checker__pair(fst_pseudo_checker, snd_pseudo_checker):
    return mk_checker__point(fst_pseudo_checker, snd_pseudo_checker)
def mk_checker__pairs(fst_pseudo_checker, snd_pseudo_checker):
    return mk_checker__array(mk_checker__pair(fst_pseudo_checker, snd_pseudo_checker))


class Checker__py_Sequence_as_point__omit(ConfigMixin__Sequence, ICheckCalcor_with_args):
    r'''
    'Sequence<T..., S?...>'
    if min_len==-1: no omit
    #'''
    _may_num_args_ = 2
    _std_arg0_ = _std_arg4int #not uint
    _std_arg1_ = _std_arg4checkers
    @classmethod
    @override
    def _post_check_args_(cls, min_len, checkers):
        check_int(min_len, min=-1, max=len(checkers))

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [min_len, checkers] = args
        #check_tuple(obj)
        cls._check_by_base_Sequence_(obj)
        seq = obj
        return _check_then_calc_ex_with_args4point(min_len, checkers, check_only, seq)

class Checker__py_list_as_point__omit(ConfigMixin__list, Checker__py_Sequence_as_point__omit):
    'list<T..., S?...>'
class Checker__py_tuple_as_point__omit(ConfigMixin__tuple, Checker__py_Sequence_as_point__omit):
    'tuple<T..., S?...>'


class Checker__tuple_maybe(IChecker_one_arg__checker, ICheckCalcor_with_args):
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [checker] = args
        check_tuple(obj)
        tpl = obj
        check_int(len(tpl), min=0, max=1)
        m = tpl
        if m:
            [x] = m
            if check_only:
                check(checker, x)
                return
            else:
                z = check_then_calc(checker, x)
                return (z,)
        else:
            return None if check_only else ()


class Checker__none_maybe(IChecker_one_arg__checker, ICheckCalcor_with_args):
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [checker] = args
        if obj is None:
            return None if check_only else ()
        else:
            x = obj
            if check_only:
                check(checker, x)
                return
            else:
                z = check_then_calc(checker, x)
                return (z,)


class Checker__check_then_calc_ex_func(IChecker_one_arg__callable, ICheckCalcor_with_args):
    'vs Checker__check_func'
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [check_then_calc_ex_func] = args
        return check_then_calc_ex_func(check_only, obj)

class Checker__check_func(IChecker_one_arg__callable, ICheckEchor_with_args):
    'vs Checker__no_calc'
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [check_func] = args
        #bug:recur:check(check_func, obj)
        return check_func(obj) #return to test None
class Checker__verify_func(IChecker_one_arg__callable, ICheckEchor_one_arg__verify):
    assert issubclass(ICheckEchor_one_arg__verify, ICheckEchor_with_args__verify4check)
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [verify_func] = args
        return verify_func(obj)
checker4callable = Checker__check_func(check_callable)
checker4callable = Checker__verify_func(callable)


#HHHHH
class Checker__is_obj(ICheckEchor_one_arg__verify):
    __arg_id2sf = {}
    @staticmethod
    def _cached_new_(arg):
        d = __class__.__arg_id2sf
        i = id(arg)
        m = d.get(i)
        if m is None:
            sf = __class__(arg)
            d[i] = sf
        else:
            sf = m
        return sf

    def __new__(cls, x):
        d = __class__.__arg_id2sf
        i = id(x)
        m = d.get(i)
        if m is not None: return m

        sf = super().__new__(cls, x)
        return sf
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [arg] = args
        return obj is arg
the_checker__is_None = Checker__is_obj._cached_new_(None)
the_checker__is_True = Checker__is_obj._cached_new_(True)
the_checker__is_False = Checker__is_obj._cached_new_(False)
the_checker__is_NotImplemented = Checker__is_obj._cached_new_(NotImplemented)
the_checker__is_Ellipsis = Checker__is_obj._cached_new_(Ellipsis)
assert ... is Ellipsis




class Checker__eq_obj(ICheckEchor_one_arg__verify):
    'same type? given pseudo_checker?'
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [arg] = args
        return obj in [arg]


class Checker__eq_obj__same_type(ICheckEchor_one_arg__verify):
    'eg: str/bytes/int'
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [arg] = args
        return type(obj) is type(arg) and obj == arg


class Checker__in_set(ICheckEchor_one_arg__Container__verify):
    'raise when hash fail?'
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [arg] = args
        return obj in arg
class Checker__in_set__hash(ICheckEchor_one_arg__Container__verify):
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [arg] = args
        try:
            return obj in arg
        except Exception as e0:
            try:
                hash(obj)
            except Exception as e1:
                if e1==e0: return False
                raise
            else:
                raise




class Checker__uint_mod(IChecker_one_arg__uint, ICheckEchor_with_args):
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [M] = args
        if M:
            check_int(obj, min=0, max=M-1)
        else:
            check_int(obj)
class Checker__int_between(IChecker_two_args__args_are_int, ICheckEchor_with_args):
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [begin, end] = args
        check_int(obj, min=begin, max=end-1)

class Checker__int_ge(IChecker_one_arg__int, ICheckEchor_with_args):
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [begin] = args
        check_int(obj, min=begin)
class Checker__int_lt(IChecker_one_arg__int, ICheckEchor_with_args):
    @classmethod
    @override
    def _check_with_args_(cls, args, obj):
        "args -> obj -> None|raise CheckFail/Exception"
        [end] = args
        check_int(obj, max=end-1)
Checker__int_ge
Checker__int_lt



class Checker__issubclass(ICheckEchor_one_arg__type_tree__verify):
    'nontype obj?'
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [super_cls] = args
        return issubclass(obj, super_cls)
Checker__le_cls = Checker__issubclass
class Checker__issubclass__allow_nontype(ICheckEchor_one_arg__type_tree__verify):
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [super_cls] = args
        return isinstance(obj, type) and issubclass(obj, super_cls)


class Checker__is_proper_subclass(ICheckEchor_one_arg__type__verify):
    'nontype obj?'
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [super_cls] = args
        return obj is not super_cls and issubclass(obj, super_cls)
Checker__lt_cls = Checker__is_proper_subclass


class Checker__isinstance(ICheckEchor_one_arg__type_tree__verify):
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [typ] = args
        return isinstance(obj,  typ)
Checker__in_cls = Checker__isinstance


class Checker__type_is(ICheckEchor_one_arg__type__verify):
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [typ] = args
        return type(obj) is typ


#HHHHH
class Checker__namedtuple(IChecker_two_args, ICheckCalcor_with_args):
    r'''
    typing.NamedTuple
    collections.namedtuple

    vs:
        Checker__namedtuple #namedtuple
        Checker__py_Sequence_as_point tuple
    #'''
    #'''
    def __new__(cls, T, checkers):
        sf = super().__new__(cls, T, checkers)
        return sf
    @classmethod
    @override
    def _post_check_args_(cls, T, checkers):
        check_tuple(checkers) #for len()
        check_namedtuple_type(T)
        attrs = T._fields
        if len(attrs) != len(checkers): raise CheckError_Type
        #_std_arg4checkers::classmethod #not callable
        check_tuple(checkers, cls=IChecker)

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [T, checkers] = args
        #check_instance(T, obj)
        check_type_is(T, obj)
        seq = obj
        return _check_then_calc_ex_with_args4point(-1, checkers, check_only, seq)
def _check_then_calc_ex_with_args4point(min_len, checkers, check_only, seq):
    if min_len < 0:
        check_len_eq(len(checkers), seq)
    else:
        check_int(len(seq), min=min_len, max=len(checkers))

    f = check if check_only else check_then_calc
    it = map(f, checkers, seq)
    if check_only:
        for _ in it:pass
        return
    else:
        return tuple(it)
Checker__py_namedtuple_as_point = Checker__namedtuple





class Checker__Mapping_as_record(ConfigMixin__Mapping, IChecker_two_args, ICheckCalcor_with_args):
    'Mapping{key=V,...}'
    _std_arg0_ = _std_arg4frozenset
    _std_arg1_ = _std_arg4key2checker

    def __new__(cls, min_keys, key2checker):
        sf = super().__new__(cls, min_keys, key2checker)
        return sf

    @classmethod
    @override
    def _post_check_args_(cls, min_keys, key2checker):
        if not min_keys <= frozenset(key2checker): raise CheckError_Type


    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [min_keys, key2checker] = args
        #check_type_is(FrozenDict, obj)
        cls._check_by_base_Mapping_(obj)
        d = obj

        if not len(min_keys) <= len(d) <= len(key2checker): raise CheckFail
        if not min_keys <= frozenset(d) <= frozenset(key2checker): raise CheckFail

        if not check_only:
            r = {}
        for k, x in d.items():
            checker = key2checker[k]
            if check_only:
                check(checker, x)
            else:
                new = check_then_calc(checker, x)
                r[k] = new
        if check_only:
            return
        else:
            g = cls._output_dict_transform4as_record_
            if g is dict:
                g = echo
            return g(r)

class Checker__HalfFrozenDict_as_record(ConfigMixin__HalfFrozenDict, Checker__Mapping_as_record):
    'seed.types.HalfFrozenDict{key=V,...}'
class Checker__FrozenDict_as_record(ConfigMixin__FrozenDict, Checker__Mapping_as_record):
    'seed.types.FrozenDict{key=V,...}'
class Checker__dict_as_record(ConfigMixin__dict, Checker__Mapping_as_record):
    'dict{key=V,...}'

class Checker__Mapping(ConfigMixin__Mapping, IChecker_two_args, ICheckCalcor_with_args):
    'Mapping<K,V>'
    _may_num_args_ = 2
    _std_arg0_ = _std_arg4checker
    _std_arg1_ = _std_arg4checker
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [key_checker, val_checker] = args
        #check_type_is(FrozenDict, obj)
        cls._check_by_base_Mapping_(obj)
        d = obj

        if check_only:
            for k, x in d.items():
                check(key_checker, k)
                check(val_checker, x)
            return
        else:
            pairs = []
            for k, x in d.items():
                a = check_then_calc(key_checker, k)
                b = check_then_calc(val_checker, x)
                pairs.append((a,b))
            return (*pairs,)

class Checker__dict(ConfigMixin__dict, Checker__Mapping):
    'dict<K,V>'
class Checker__HalfFrozenDict(ConfigMixin__HalfFrozenDict, Checker__Mapping):
    'HalfFrozenDict<K,V>'
class Checker__FrozenDict(ConfigMixin__FrozenDict, Checker__Mapping):
    'FrozenDict<K,V>'



class Checker__Mapping__item(ConfigMixin__Mapping, IChecker_one_arg__checker, ICheckCalcor_with_args):
    'Mapping<Item>'

    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [item_checker] = args
        #check_type_is(FrozenDict, obj)
        cls._check_by_base_Mapping_(obj)
        d = obj
        return Checker__all._check_then_calc_ex_with_args_(args, check_only, d.items())

class Checker__dict__item(ConfigMixin__dict, Checker__Mapping__item):
    'dict<Item>'
class Checker__HalfFrozenDict__item(ConfigMixin__HalfFrozenDict, Checker__Mapping__item):
    'HalfFrozenDict<Item>'
class Checker__FrozenDict__item(ConfigMixin__FrozenDict, Checker__Mapping__item):
    'FrozenDict<Item>'




class Checker__Set(IChecker_one_arg__checker, ICheckCalcor_with_args):
    'Set<K>'
    @classmethod
    @override
    def _check_then_calc_ex_with_args_(cls, args, check_only, obj):
        [checker] = args
        #check_type_is(frozenset, obj)
        cls._check_by_base_Set_(obj)
        s = obj
        return Checker__all._check_then_calc_ex_with_args_(args, check_only, s)

class Checker__set(ConfigMixin__set, Checker__Set):
    'set<K>'
class Checker__frozenset(ConfigMixin__frozenset, Checker__Set):
    'frozenset<K>'







#HHHHH

class Checker__le_obj(ICheckEchor_one_arg__verify):
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [rhs] = args
        return obj <= rhs


class Checker__lt_obj(ICheckEchor_one_arg__verify):
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [rhs] = args
        return obj < rhs


class Checker__ge_obj(ICheckEchor_one_arg__verify):
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [rhs] = args
        return obj >= rhs


class Checker__gt_obj(ICheckEchor_one_arg__verify):
    @classmethod
    @override
    def _verify_with_args_(cls, args, obj):
        "args -> obj -> bool"
        [rhs] = args
        return obj > rhs






the_checker__is_None
the_checker__is_False
the_checker__is_True
the_checker__is_NotImplemented
the_checker__is_Ellipsis


the_pass_checker
the_fail_checker
the_checker__is_None

Checker__py_tuple_as_array
Checker__py_tuple_as_point
Checker__ordered_union
Checker__check_func
Checker__isinstance




_4checker = Checker__isinstance(IChecker)
_4bool = Checker__type_is(bool)
_4checker_bool_pairs = mk_checker__pairs(_4checker, _4bool)
_4checkers = mk_checker__array(_4checker)


_4checker_bool_pairs
_4bool
_4checkers
_4checker


#HHHHH
if 0:
    if __name__ == '__main__':
        classes = [IChecker]
        excludes = '''
            logic
            error
            '''.split()

        from seed.helper.ongo import main
        main(modules=[__name__], classes=classes, excludes=excludes)

    if __name__ == '__main__':
        from seed.helper.print_global_names import print_global_names
        print_global_names(globals())




if __name__ == "__main__":
    import doctest
    doctest.testmod()

#HHHHH




