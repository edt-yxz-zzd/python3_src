#__all__:goto
r'''
e ../../python3_src/seed/types/Either.py
py -m nn_ns.app.debug_cmd   seed.types.Either -x
py -m nn_ns.app.doctest_cmd seed.types.Either:__doc__ -ht # -ff -df

>>> issubclass(Cased, tuple)
True
>>> issubclass(Either, Cased)
True
>>> issubclass(KindedName, Cased)
True
>>> Cased(666, 999)
Cased(666, 999)
>>> Either(True, 999)
Either(True, 999)
>>> mk_Left(666)
Either(False, 666)
>>> mk_Right(999)
Either(True, 999)
>>> KindedName(int, 999)
KindedName(<class 'int'>, 999)


>>> Cased(666, 999).case
666
>>> Cased(666, 999).payload
999
>>> KindedName(int, 999).kind
<class 'int'>
>>> KindedName(int, 999).name
999







>>> TagT(666)
TagT(666)
>>> TagT(666).tag
666
>>> TagT(666)(999)
(666, 999)
>>> CaseT(666)
CaseT(666)
>>> CaseT(666).case
666
>>> CaseT(666)(999)
Cased(666, 999)
>>> EitherT(666)
Traceback (most recent call last):
    ...
TypeError: <class 'int'>
>>> EitherT(True)
EitherT(True)
>>> EitherT(True).case
True
>>> EitherT(True)(999)
Either(True, 999)

>>> TupleT(666)
TupleT(666)
>>> TupleT(666).args
(666,)
>>> TupleT(666)(999)
(666, 999)
>>> TupleT(666, 777)
TupleT(666, 777)
>>> TupleT(666, 777).args
(666, 777)
>>> TupleT(666, 777)(888, 111, 999)
(666, 777, 888, 111, 999)
>>> TupleT(666, 777)(888, 111, 999, curry=True)
TupleT(666, 777, 888, 111, 999)
>>> TupleT(666, 777).curry_(888, 111, 999)
TupleT(666, 777, 888, 111, 999)
>>> TupleT(666, 777)[888, 111, 999]
TupleT(666, 777, 888, 111, 999)
>>> TupleT(666, 777)[:1]
TupleT(666)

'''#'''

__all__ = '''
Cased
Either mk_Left mk_Right
KindedName

TagT
CaseT
EitherT
TupleT
'''.split()#'''

___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_type_le
from seed.tiny_.catched_call__either import catched_call__either# cached_catched_call__either, get_or_cached_catched_call__either
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper')
#.from seed.helper.repr_input import repr_helper
from seed.tiny_.containers import null_tuple
from collections.abc import Hashable as IHashable
___end_mark_of_excluded_global_names__0___ = ...

def _apply_may_f(may_f, x, /):
    return x if may_f is None else may_f(x)
class Cased(tuple):
    @classmethod
    def from_catched_lazy_value(cls, may_Base4Exception, lazy_value, /):
        return cls(*catched_call__either(may_Base4Exception, lazy_value))
        return cls.from_pair(catched_call__either(may_Base4Exception, lazy_value))
    @classmethod
    def from_pair(cls, pair, /):
        assert len(pair) == 2
        return cls(*pair)
    def __repr__(sf, /):
        return repr_helper(sf, *sf)
    @classmethod
    def _check_case_(cls, case, /):
        pass
    @classmethod
    def _check_payload_(cls, payload, /):
        pass
    @classmethod
    def _check_case_payload_(cls, case, payload, /):
        pass
    def __new__(cls, case, payload, /):
        #check_type_is(bool, case)
        cls._check_case_(case)
        cls._check_payload_(payload)
        cls._check_case_payload_(case, payload)
        return tuple.__new__(cls, [case, payload])
    ######################
    __match_args__ = ('case', 'payload')
    @property
    def case(sf, /):
        return sf[0]
    @property
    def payload(sf, /):
        return sf[1]

    ######################
    ######################
    def fmap4payload(sf, may_f, /):
        if may_f is None: return sf
        p1 = may_f(p0:=sf.payload)
        if p1 is p0: return sf
        return type(sf)(sf.case, p1)
    def fmap4case(sf, may_f, /):
        if may_f is None: return sf
        c1 = may_f(c0:=sf.case)
        if c1 is c0: return sf
        return type(sf)(c1, sf.payload)
    def fmap4both(sf, may_f4case, may_f4payload, /):
        if may_f4payload is None is may_f4case:
            return sf
        return (sf.ireplace__both
        (_apply_may_f(may_f4case, sf.case)
        ,_apply_may_f(may_f4payload, sf.payload)
        ))
#
    ######################
    def case_is_(sf, case, /):
        return sf.case is case
    def case_eq_(sf, case, /):
        return sf.case == case
    ######################
    def ireplace__both(sf, case, payload, /):
        if case is sf.case and payload is sf.payload:
            return sf
        return type(sf)(case, payload)
    def ireplace__case(sf, case, /):
        if case is sf.case:
            return sf
        return type(sf)(case, sf.payload)
    def ireplace__payload(sf, payload, /):
        if payload is sf.payload:
            return sf
        return type(sf)(sf.case, payload)
    ######################
    def itag__payload(sf, tag, /):
        return sf.ireplace__payload(Cased(tag, sf.payload))
    def untag__payload(sf, /):
        tag, _payload = sf.payload
        return (tag, sf.ireplace__payload(_payload))
    ######################
    ######################
    def ireplace__payload__if_(sf, b, payload, /):
        return sf if not b else sf.ireplace__payload(payload)
    def ireplace__payload__if_case_is_(sf, case, payload, /):
        return sf.ireplace__payload__if_(sf.case_is_(case), payload)
    def ireplace__payload__if_case_eq_(sf, case, payload, /):
        return sf.ireplace__payload__if_(sf.case_eq_(case), payload)

    ######################
    def to_tmay_payload__if_(sf, b, /):
        return null_tuple if not b else (sf.payload,)
    def to_tmay_payload__if_case_is_(sf, case, /):
        return sf.to_tmay_payload__if_(sf.case_is_(case))
    def to_tmay_payload__if_case_eq_(sf, case, /):
        return sf.to_tmay_payload__if_(sf.case_eq_(case))

    ######################
    ######################
    def to_payload__default__if_(sf, b, default, /):
        return default if not b else sf.payload
    def to_payload__default__if_case_is_(sf, case, default, /):
        return sf.to_payload__default__if_(sf.case_is_(case), default)
    def to_payload__default__if_case_eq_(sf, case, default, /):
        return sf.to_payload__default__if_(sf.case_eq_(case), default)
    ######################
    def to_payload__fdefault__if_(sf, b, fdefault, /):
        return fdefault() if not b else sf.payload
    def to_payload__fdefault__if_case_is_(sf, case, fdefault, /):
        return sf.to_payload__fdefault__if_(sf.case_is_(case), fdefault)
    def to_payload__fdefault__if_case_eq_(sf, case, fdefault, /):
        return sf.to_payload__fdefault__if_(sf.case_eq_(case), fdefault)
    ######################
class KindedName(Cased):
    @classmethod
    #@override
    def _check_case_(cls, kind, /):
        check_type_le(type, kind)
        super()._check_case_(kind)
    @classmethod
    #@override
    def _check_payload_(cls, nm, /):
        check_type_le(IHashable, nm)
        super()._check_payload_(nm)
    @property
    def kind(sf, /):
        return sf.case
    @property
    def name(sf, /):
        return sf.payload

class Either(Cased):
    @classmethod
    def from_left(cls, left, /):
        return cls(False, left)
    @classmethod
    def from_right(cls, right, /):
        return cls(True, right)
    @classmethod
    #@override
    def _check_case_(cls, case, /):
        check_type_is(bool, case)
        super()._check_case_(case)
    if 0:
        def __new__(cls, exc_vs_val, exc_or_val, /):
            check_type_is(bool, exc_vs_val)
            return super(__class__, cls).__new__(cls, exc_vs_val, exc_or_val)
    def __invert__(sf, /):
        return sf.ireplace__case(not sf.case)
    def flip(sf, /):
        return ~sf

    @property
    def is_left(sf, /):
        return not sf[0]
    @property
    def is_right(sf, /):
        return sf[0]

    def assert_left(sf, /):
        if not sf.is_left: raise AttributeError('left')
    def assert_right(sf, /):
        if not sf.is_right: raise AttributeError('right')
    @property
    def left(sf, /):
        sf.assert_left()
        return sf[1]
    @property
    def right(sf, /):
        sf.assert_right()
        return sf[1]

    ######################
    def fmap4left(sf, may_f, /):
        sf.assert_left()
        return sf.fmap4payload(may_f)
    def fmap4right(sf, may_f, /):
        sf.assert_right()
        return sf.fmap4payload(may_f)

    ######################
    def fmap_if_left(sf, may_f, /):
        return sf if may_f is None or not sf.is_left else sf.fmap4payload(may_f)
    def fmap_if_right(sf, may_f, /):
        return sf if may_f is None or not sf.is_right else sf.fmap4payload(may_f)
    def fmap4either(sf, may_f4left, may_f4right, /):
        if sf.is_right:
            return sf.fmap4payload(may_f4right)
        return sf.fmap4payload(may_f4left)

    ######################
    def fold4either(sf, may_f4left, may_f4right, /):
        may_f = may_f4right if sf.is_right else may_f4left
        return _apply_may_f(may_f, sf.payload)

    ######################
    def ireplace__left(sf, left, /):
        sf.assert_left()
        return sf.ireplace__payload(left)
    def ireplace__right(sf, right, /):
        sf.assert_right()
        return sf.ireplace__payload(right)
    def ireplace__either(sf, left, right, /):
        return sf.ireplace__payload(left) if  sf.is_left else sf.ireplace__payload(right)

    ######################
    def ireplace__if_left(sf, left, /):
        return sf if not sf.is_left else sf.ireplace__payload(left)

    def ireplace__if_right(sf, right, /):
        return sf if not sf.is_right else sf.ireplace__payload(right)
    ######################
    def to_tmay_left(sf, /):
        return sf.to_tmay_payload__if_(sf.is_left)
    def to_tmay_right(sf, /):
        return sf.to_tmay_payload__if_(sf.is_right)
    ######################
    def to_left__default_(sf, default, /):
        return sf.to_payload__default__if_(sf.is_left, default)
    def to_right__default_(sf, default, /):
        return sf.to_payload__default__if_(sf.is_right, default)
    ######################
    def to_left__fdefault_(sf, fdefault, /):
        return sf.to_payload__fdefault__if_(sf.is_left, fdefault)
    def to_right__fdefault_(sf, fdefault, /):
        return sf.to_payload__fdefault__if_(sf.is_right, fdefault)
    ######################

def mk_Left(left, /):
    'a -> Either a b'
    return Either.from_left(left)
def mk_Right(right, /):
    'b -> Either a b'
    return Either.from_right(right)


class _BaseTagT:
    def __init__(sf, tag, /):
        sf._t = tag
        sf._check6make_()
    def _check6make_(sf, /):
        pass
    def __repr__(sf, /):
        return repr_helper(sf, sf._tag_)
    @property
    def _tag_(sf, /):
        return sf._t
    def __call__(sf, payload, /):
        return (sf.tag, payload)
class TagT(_BaseTagT):
    @property
    def tag(sf, /):
        return sf._tag_
    def __call__(sf, payload, /):
        return (sf.tag, payload)
class CaseT(_BaseTagT):
    @property
    def case(sf, /):
        return sf._tag_
    def __call__(sf, payload, /):
        return Cased(sf.case, payload)
class EitherT(CaseT):
    def _check6make_(sf, /):
        check_type_is(bool, sf.case)
    def __call__(sf, payload, /):
        return Either(sf.case, payload)

class TupleT:
    def __init__(sf, /, *args):
        sf._t = args
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
    @property
    def args(sf, /):
        return sf._t
    def __call__(sf, /, *more_args, curry=False):
        if curry:
            return __class__(*sf.args, *more_args)
        return (*sf.args, *more_args)
    def curry_(sf, /, *more_args):
        return sf(*more_args, curry=True)
    def __getitem__(sf, slice_or_more_args, /):
        match slice_or_more_args:
            #case slice(sl):
                #^TypeError: slice() accepts 0 positional sub-patterns (1 given)
            #case slice() & sl:
                #^SyntaxError: invalid syntax
            case slice():
                sl = slice_or_more_args
                return __class__(*sf.args[sl])
            case more_args:
                return sf(*more_args, curry=True)
            #
        raise 000



from seed.types.Either import Cased, Either, KindedName
from seed.types.Either import mk_Left, mk_Right
from seed.types.Either import TagT, CaseT, EitherT, TupleT
from seed.types.Either import *
