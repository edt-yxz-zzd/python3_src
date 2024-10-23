#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/regex/RegexRepr.py

seed.recognize.regex.RegexRepr
py -m nn_ns.app.debug_cmd   seed.recognize.regex.RegexRepr -x
py -m nn_ns.app.doctest_cmd seed.recognize.regex.RegexRepr:__doc__ -ht

Repr --> notation

Concatenation
  x . y
Alternation
  x | y
Repetition
  x *
Grouping
  ( x )

[[

usage<regex>:
    hollow_regex << regex
    dead_regex | regex
    regex % color
    regex / empty_set_repr[:sym:, min_sym::max_sym]
    regex[0:+oo:1]

usage<set_repr>:
    -set_repr
    empty_set_repr | set_repr
    whole_set_repr & set_repr
    set_repr - set_repr
    empty_set_repr//oo[min_sym::, ::max_sym]
    empty_set_repr[:sym:]
    empty_set_repr[min_sym::max_sym]

]]

#>>> hollow_regex
#>>> empty_set_repr
#>>> empty_set_repr[:'a':]
#>>> empty_set_repr[:'a':][:'9':]
#>>> empty_set_repr[:'a':][:'0':,:'9':]
#>>> empty_set_repr[:'a':] | empty_set_repr[:'0':,:'9':]
#>>> empty_set_repr[:'a':] & empty_set_repr[:'0':,:'9':]
#>>> empty_set_repr[:'a':] - empty_set_repr[:'0':,:'9':]
#>>> -empty_set_repr[:'0':,:'9':]
#>>> empty_set_repr//[Solo('0'),oo['9'::,::+oo]]
#>>> empty_set_repr[:'a':]['0'::'9']
#>>> empty_set_repr[:'a':] | empty_set_repr['0'::'9']



>>> hollow_regex
RegexRepr_HollowTransition()
>>> empty_set_repr
SetRepr_5Intervals(())
>>> empty_set_repr[:'a':]
SetRepr_5Intervals((Solo('a'),))
>>> empty_set_repr[:'a':][:'9':]
SetRepr_Union((SetRepr_5Intervals((Solo('a'),)), SetRepr_5Intervals((Solo('9'),))))
>>> empty_set_repr[:'a':][:'0':,:'9':]
SetRepr_Union((SetRepr_5Intervals((Solo('a'),)), SetRepr_5Intervals((Solo('0'), Solo('9')))))
>>> empty_set_repr[:'a':] | empty_set_repr[:'0':,:'9':]
SetRepr_Union((SetRepr_5Intervals((Solo('a'),)), SetRepr_5Intervals((Solo('0'), Solo('9')))))
>>> empty_set_repr[:'a':] & empty_set_repr[:'0':,:'9':]
SetRepr_Intersection((SetRepr_5Intervals((Solo('a'),)), SetRepr_5Intervals((Solo('0'), Solo('9')))))
>>> empty_set_repr[:'a':] - empty_set_repr[:'0':,:'9':]
SetRepr_Diff(SetRepr_5Intervals((Solo('a'),)), SetRepr_5Intervals((Solo('0'), Solo('9'))))
>>> -empty_set_repr[:'0':,:'9':]
SetRepr_Negation(SetRepr_5Intervals((Solo('0'), Solo('9'))))
>>> empty_set_repr//[Solo('0'),oo['9'::,::+oo]]
SetRepr_5Intervals((Solo('0'), oo['9'::, :+oo:]))
>>> empty_set_repr[:'a':]['0'::'9']
SetRepr_Union((SetRepr_5Intervals((Solo('a'),)), SetRepr_5Intervals((oo['0'::, ::'9'],))))
>>> empty_set_repr[:'a':] | empty_set_repr['0'::'9']
SetRepr_Union((SetRepr_5Intervals((Solo('a'),)), SetRepr_5Intervals((oo['0'::, ::'9'],))))






>>> 'a' in (empty_set_repr[:'a':] | empty_set_repr['0'::'9'])
True
>>> '0' in (empty_set_repr[:'a':] | empty_set_repr['0'::'9'])
True
>>> '3' in (empty_set_repr[:'a':] | empty_set_repr['0'::'9'])
True
>>> '9' in (empty_set_repr[:'a':] | empty_set_repr['0'::'9'])
True
>>> '3ab' in (empty_set_repr[:'a':] | empty_set_repr['0'::'9'])
True


>>> not 'a' in (empty_set_repr[:'a':] & empty_set_repr['0'::'9'])
True
>>> not '3' in (empty_set_repr[:'a':] & empty_set_repr['0'::'9'])
True



>>> 'a' in (empty_set_repr[:'a':] - empty_set_repr['0'::'9'])
True
>>> not '3' in (empty_set_repr[:'a':] - empty_set_repr['0'::'9'])
True


>>> not 'a' in -empty_set_repr[:'a':]
True
>>> '3' in -empty_set_repr[:'a':]
True




regex"a"
regex"[a]"
regex"[a-z]"
regex"[a-z0-9AC]"
regex"[^a-z0-9AC]"
regex"a|b"
regex"ab"
regex"a*"
regex"a+"
regex"a?"
regex"a{3,8}"
regex"a{?color:=ccc}"
#>>> hollow_regex / empty_set_repr[:'a':]
#>>> hollow_regex / empty_set_repr['a'::'z']
#>>> hollow_regex / empty_set_repr['a'::'z', '0'::'9', :'A':, :'C':]
#>>> hollow_regex / -empty_set_repr['a'::'z', '0'::'9', :'A':, :'C':]
#>>> hollow_regex / empty_set_repr[:'a':] | hollow_regex / empty_set_repr[:'b':]
#>>> hollow_regex / empty_set_repr[:'a':] << hollow_regex / empty_set_repr[:'b':]
#>>> (hollow_regex / empty_set_repr[:'a':])[:]
#>>> (hollow_regex / empty_set_repr[:'a':])[1:]
#>>> (hollow_regex / empty_set_repr[:'a':])[:1]
#>>> (hollow_regex / empty_set_repr[:'a':])[3:8]
#>>> hollow_regex / empty_set_repr[:'a':]  % "ccc"




>>> hollow_regex / empty_set_repr[:'a':]
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))
>>> hollow_regex / empty_set_repr['a'::'z']
RegexRepr_SolidTransition(SetRepr_5Intervals((oo['a'::, ::'z'],)))
>>> hollow_regex / empty_set_repr['a'::'z', '0'::'9', :'A':, :'C':]
RegexRepr_SolidTransition(SetRepr_5Intervals((oo['a'::, ::'z'], oo['0'::, ::'9'], Solo('A'), Solo('C'))))
>>> hollow_regex / -empty_set_repr['a'::'z', '0'::'9', :'A':, :'C':]
RegexRepr_SolidTransition(SetRepr_Negation(SetRepr_5Intervals((oo['a'::, ::'z'], oo['0'::, ::'9'], Solo('A'), Solo('C')))))
>>> hollow_regex / empty_set_repr[:'a':] | hollow_regex / empty_set_repr[:'b':]
RegexRepr_Alternation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))))
>>> hollow_regex / empty_set_repr[:'a':] << hollow_regex / empty_set_repr[:'b':]
RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))))
>>> (hollow_regex / empty_set_repr[:'a':])[:]
RegexRepr_Repetition(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))))
>>> (hollow_regex / empty_set_repr[:'a':])[1:]
RegexRepr_Many1(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))))
>>> (hollow_regex / empty_set_repr[:'a':])[:1]
RegexRepr_Optional(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))))
>>> (hollow_regex / empty_set_repr[:'a':])[3:8]
RegexRepr_Array(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), 3, 8)
>>> hollow_regex / empty_set_repr[:'a':]  % "ccc"
RegexRepr_Colored(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), 'ccc')








py_adhoc_call   seed.recognize.regex.RegexRepr   @f

#]]]'''
__all__ = r'''
hollow_regex
dead_regex
empty_set_repr
whole_set_repr
SetRepr_5Unicode_property





ISetRepr
    ISetRepr_IntervalBased
        ISetRepr_Wrapper
            SetRepr_5Unicode_property
            SetRepr_Wrapper
                SetRepr_Diff
        SetRepr_5Intervals
            slice2soloXopen_interval
            solo2open_interval
            empty_set_repr
        SetRepr_Negation
        SetRepr_Union
        SetRepr_Intersection

IRegexRepr
    ISetRepr
        ISetRepr_IntervalBased
    Colored
    HollowTransition
    SolidTransition

IRegexRepr
    IRegexRepr__start_pst_is_0__stop_pst_is_1
        offset_uint2pst_
        RegexRepr_Concatenation
        RegexRepr_Alternation
        RegexRepr_Repetition
        RegexRepr_HollowTransition
            hollow_regex
        RegexRepr_SolidTransition
            dead_regex
    RegexRepr_Wrapper
        RegexRepr_Colored
        RegexRepr_Array
        RegexRepr_Optional
        RegexRepr_Many1

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property
from bisect import bisect_left
from collections import deque

from seed.tiny_.containers import mk_tuple, null_tuple
from seed.types.Either import Cased, Either
from seed.tiny_.oo8inf import oo, OpenInterval #(OO8inf|Tag_o0o8inv_inf)
from seed.tiny_.oo8inf import \
(mk_sorted_nonempty_open_intervals
,   merge_sorted_nonempty_open_intervals
,       union_iterable_of_merged_sorted_nonempty_open_intervals
,       mk_merged_sorted_nonempty_open_intervals
,negation_merged_sorted_nonempty_open_intervals
,intersection_iterable_of_merged_sorted_nonempty_open_intervals
)

from seed.tiny_.oo8inf import mk_merged_sorted_nonempty_open_intervals

from seed.tiny_.HashedPair import HashedPair, Solo
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge
from seed.tiny_._Base4repr import _Base4repr #sf._args4repr = (...)
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#class ISetRepr(ABC):
#    'terminal_symbol_set'
class ISetRepr(ABC):
    __slots__ = ()
    @abstractmethod
    def __contains__(sf, k, /):
        '-> bool'
    def __bool__(sf, /):
        '-> bool'
        raise NotImplementedError('ISetRepr.__bool__')
    @cached_property
    #@abstractmethod
    def known_empty(sf, /):
        '-> bool'
        return False
class ISetRepr_IntervalBased(ISetRepr):
    r'''[[[
    'total_ordering'

    usage:
    -set_repr
    empty_set_repr | set_repr
    whole_set_repr & set_repr
    set_repr - set_repr
    empty_set_repr//oo[min_sym::, ::max_sym]
    empty_set_repr[:sym:]
    empty_set_repr[min_sym::max_sym]

    #]]]'''#'''
    __slots__ = ()
    def eq__untyped_(sf, ot, /):
        '-> bool'
        return sf is ot or sf.as_cached_SetRepr_5Intervals.eq__typed_(ot.as_cached_SetRepr_5Intervals)
    @cached_property
    def as_cached_SetRepr_5Intervals(sf, /):
        '-> SetRepr_5Intervals'
        return SetRepr_5Intervals(sf.iter_merged_sorted_nonempty_open_intervals())

    @abstractmethod
    def iter_boundaries4open_intervals(sf, /):
        '-> Iter boundary<OpenInterval>/(OO8inf|Tag_o0o8inv_inf)'

    def __neg__(sf, /):
        '-set_repr'
        return SetRepr_Negation(sf)
    def __or__(sf, ot, /):
        'empty_set_repr | set_repr'
        if not isinstance(ot, ISetRepr):return NotImplemented
        if ot.known_empty:
            return sf
        if sf.known_empty:
            #if sf is empty_set_repr:
            # required by __floordiv__
            return ot
        return SetRepr_Union([sf, ot])
    def __and__(sf, ot, /):
        'whole_set_repr & set_repr'
        if ot is whole_set_repr:
            return sf
        if not isinstance(ot, ISetRepr_IntervalBased):return NotImplemented
        if sf is whole_set_repr:
            return ot
        return SetRepr_Intersection([sf, ot])
    def __sub__(sf, ot, /):
        'set_repr - set_repr'
        if not isinstance(ot, ISetRepr_IntervalBased):return NotImplemented
        if ot.known_empty:
            return sf
        if ot is whole_set_repr:
            return empty_set_repr
        if sf.known_empty:
            return empty_set_repr
        if sf is whole_set_repr:
            return -ot
        return SetRepr_Diff(sf, ot)
        return (sf & -ot)
    def __floordiv__(sf, ls_X_solo_or_intvl, /):
        'empty_set_repr//ls_X_solo_or_intvl # [ls_X_solo_or_intvl :: (Solo|OpenInterval|Iter (Solo|OpenInterval))]'
        'empty_set_repr//oo[min_sym::, ::max_sym]'

        ot = SetRepr_5Intervals(ls_X_solo_or_intvl)
        return (sf | ot)
    def __getitem__(sf, ls_X_slice_or_solo_or_intvl, /):
        'empty_set_repr[:v:, min_v::max_v, oo[...], Solo(v), ...]'
        'empty_set_repr[:sym:]'
        'empty_set_repr[min_sym::max_sym]'
        ls_X_solo_or_intvl = _explain__ls_X_slice_or_solo_or_intvl(ls_X_slice_or_solo_or_intvl)
        return sf // ls_X_solo_or_intvl
    @abstractmethod
    def iter_merged_sorted_nonempty_open_intervals(sf, /):
        '-> (Iter nonempty-OpenInterval){sorted,merged} # components of sf'
        boundaries = sorted({+oo,-oo,*sf.iter_boundaries4open_intervals()})
        assert boundaries[0] is -oo
        assert boundaries[-1] is +oo
        dq = deque()
            # [dq :: [OpenInterval]]
        def put(low, up, /, *, _tm=[]):
            # [_tm :: [(low,up)]{len<=1}]
            match _tm:
                case []:
                    _tm.append((low,up))
                case [(low_, up_)]:
                    _tm.pop()
                    if up_ == low:
                        #merge
                        _tm.append((low_,up))
                    else:
                        #output
                        dq.append(OpenInterval(low_, up_))
                        _tm.append((low,up))
                case _:
                    raise 000

        def f(j, low, /):
            if low in sf:
                put(low, boundaries[j+1])
                return g()
            return ''
        def g():
            while dq:
                intvl = dq.popleft()
                if not intvl:raise 000
                yield intvl
        prev_up, next_low = None, boundaries[0]
        yield from f(0, next_low)
        for j in range(1, len(boundaries)-1):
            prev_up, next_low = boundaries[j].as_sorted_pseudo_boundary_pair()
            yield from f(j, next_low)
        yield from g()
        assert not dq
        return
def _explain__ls_X_slice_or_solo_or_intvl(ls_X_slice_or_solo_or_intvl, /):
    '-> ls_X_solo_or_intvl'
    Ts = (slice, OpenInterval, Solo)
    if type(ls_X_slice_or_solo_or_intvl) in Ts:
        _slice_or_solo_or_intvl = ls_X_slice_or_solo_or_intvl
        ls = (_slice_or_solo_or_intvl,)
    else:
        ls = ls_X_slice_or_solo_or_intvl
    ls
    Ts = (OpenInterval, Solo)
    zs = []
    for x in ls:
        if type(x) is slice:
            x = slice2soloXopen_interval(x)
        if not type(x) in Ts:
            raise TypeError(type(x))
        zs.append(x)
    zs
    return zs

def slice2soloXopen_interval(x, /):
    match x:
        case slice(start=start, stop=stop, step=step):
            pass
        case _:raise TypeError(type(x))
    match (start, stop, step):
        case (None, None, None):
            raise ValueError(x)
        case (None, v, None):
            return Solo(v)
        case (min_v, None, max_v):
            # [min_v..=max_v]
            if None is min_v:
                min_v = -oo
            if None is max_v:
                max_v = +oo
            return oo[min_v::, ::max_v]
        case _:
            raise 000
    raise 000



#end-class ISetRepr_IntervalBased(ISetRepr):
class ISetRepr_Wrapper(ISetRepr_IntervalBased):
    __slots__ = ()
    @property
    #@cached_property
    @abstractmethod
    def _wrapped_(sf, /):
        '-> ISetRepr_IntervalBased'
    @override
    def __contains__(sf, k, /):
        '-> bool'
        return k in sf._wrapped_
    @override
    def __bool__(sf, /):
        '-> bool'
        return bool(sf._wrapped_)
        raise NotImplementedError('ISetRepr.__bool__')
    @cached_property
    @override
    def known_empty(sf, /):
        '-> bool'
        return sf._wrapped_.known_empty
        return False

    @override
    def iter_boundaries4open_intervals(sf, /):
        '-> Iter boundary<OpenInterval>/(OO8inf|Tag_o0o8inv_inf)'
        return sf._wrapped_.iter_boundaries4open_intervals()
    @override
    def iter_merged_sorted_nonempty_open_intervals(sf, /):
        '-> (Iter nonempty-OpenInterval){sorted,merged} # components of sf'
        return sf._wrapped_.iter_merged_sorted_nonempty_open_intervals()
#end-class ISetRepr_Wrapper(ISetRepr_IntervalBased):
class SetRepr_5Unicode_property(ISetRepr_Wrapper, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, ver4unicode, property_alias4unicode, property_value4unicode, /):
        check_type_is(str, ver4unicode)
        check_type_is(str, property_alias4unicode)
        check_type_is(str, property_value4unicode)
        args = (ver4unicode, property_alias4unicode, property_value4unicode)
        sf._args4repr = args
        sf._args4wrapper = args
    @cached_property
    @override
    def _wrapped_(sf, /):
        '-> ISetRepr_IntervalBased'
        from nn_ns.CJK.unicode.ucd_unihan.xml.resource_loader import data_loader4depth2__literal_eval__u8
        from seed.tiny_.oo8inf import mk_open_intervals5hex2sz

        (ver4unicode, property_alias4unicode, property_value4unicode) = sf._args4wrapper
        ver = getattr(data_loader4depth2__literal_eval__u8, ver4unicode)
        (fwd, bwd) = getattr(ver, property_alias4unicode)
        pt2sz = fwd[property_value4unicode]
        open_intervals = mk_open_intervals5hex2sz(pt2sz)
        return SetRepr_5Intervals(open_intervals)
    @property
    @override
    def as_cached_SetRepr_5Intervals(sf, /):
        '-> SetRepr_5Intervals'
        return sf._wrapped_
#end-class SetRepr_5Unicode_property(ISetRepr_Wrapper, _Base4repr):


class SetRepr_Wrapper(ISetRepr_Wrapper, _Base4repr):
    'just used to alias set expr #e.g. SetRepr_Diff'
    ___no_slots_ok___ = True
    def __init__(sf, set_repr, /):
        check_type_le(ISetRepr_IntervalBased, set_repr)
        sf._args4repr = (set_repr,)
        sf._s = set_repr
    @property
    @override
    def _wrapped_(sf, /):
        '-> ISetRepr_IntervalBased'
        return sf._s
class SetRepr_Diff(SetRepr_Wrapper):
    def __init__(sf, lhs_set_repr, rhs_set_repr, /):
        check_type_le(ISetRepr_IntervalBased, lhs_set_repr)
        check_type_le(ISetRepr_IntervalBased, rhs_set_repr)
        whole = lhs_set_repr & -rhs_set_repr
        super().__init__(whole)
        777;    sf._args4repr = (lhs_set_repr, rhs_set_repr)

#class TerminalSymbol:
#class Singleton:
#class Solo:
Solo

def solo2open_interval(solo, /):
    match solo:
        case Solo(v):
            intvl = oo[:v:, :v:]
            if not intvl:
                assert intvl in [-oo, +oo]
                raise ValueError(intvl)
            assert intvl, ValueError(intvl)
            return intvl
        case _:
            raise TypeError(type(solo))
    raise 000
class SetRepr_5Intervals(ISetRepr_IntervalBased, _Base4repr):
    ___no_slots_ok___ = True
    @property
    @override
    def as_cached_SetRepr_5Intervals(sf, /):
        '-> SetRepr_5Intervals'
        return sf
    def __init__(sf, ls_X_solo_or_intvl, /):
        'ls_X_solo_or_intvl # [ls_X_solo_or_intvl :: (Solo|OpenInterval|Iter (Solo|OpenInterval))]'
        Ts = (OpenInterval, Solo)
        if type(ls_X_solo_or_intvl) in Ts:
            _solo_or_intvl = ls_X_solo_or_intvl
            ls = (_solo_or_intvl,)
        else:
            ls = mk_tuple(ls_X_solo_or_intvl)
        ls

        for x in ls:
            if not type(x) in Ts: raise TypeError(type(x), Ts)

        zs = []
        for x in ls:
            if type(x) is Solo:
                x = solo2open_interval(solo:=x)
            check_type_is(OpenInterval, x)
            if x:
                zs.append(x)
        #zs.sort()
        zs = mk_merged_sorted_nonempty_open_intervals(zs)


        sf._args4repr = (ls,)
        sf._ls = ls
        sf._zs = mk_tuple(zs)

    __match_args__ = ('pseudo_intervals',)
    @cached_property
    @override
    def known_empty(sf, /):
        '-> bool'
        return not sf._zs
    @property
    def pseudo_intervals(sf, /):
        return sf._ls
    ##def __hash__(sf, /):
    ##def __eq__(sf, ot, /):
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not type(sf) is type(ot):
            return NotImplemented
        return sf._zs == ot._zs
    def eq__typed_(sf, ot, /):
        '-> bool'
        return sf is ot or (type(sf) is type(ot) and sf._zs == ot._zs)
    @override
    def iter_boundaries4open_intervals(sf, /):
        '-> Iter boundary<OpenInterval>/(OO8inf|Tag_o0o8inv_inf)'
        return (b for intvl in sf._zs for b in intvl.span)
    @override
    def __contains__(sf, k, /):
        '-> bool'
        j = bisect_left(zs:=sf._zs, k, key=OpenInterval.low.fget)
        js = [i for i in [j-1, j] if 0 <= i < len(zs)]
        xs = zs[max(0,j-1):j+1]
        return any(k in intvl for intvl in xs)
        return any(k in intvl for intvl in sf._zs)
    @override
    def iter_merged_sorted_nonempty_open_intervals(sf, /):
        '-> (Iter nonempty-OpenInterval){sorted,merged} # components of sf'
        return iter(sf._zs)

empty_set_repr = SetRepr_5Intervals([])
assert empty_set_repr.known_empty
assert not SetRepr_5Intervals([Solo(0)]).known_empty
whole_set_repr = empty_set_repr[-oo::+oo]
assert not whole_set_repr.known_empty

class SetRepr_Negation(ISetRepr_IntervalBased, _Base4repr):
    ___no_slots_ok___ = True
    def __new__(cls, set_repr, /):
        if not cls is __class__:raise TypeError(cls)
        if isinstance(set_repr, __class__):
            ot = set_repr
            return ot.base_set #not sf
        sf = super(__class__, cls).__new__(cls)
        sf._s = set_repr
        sf._args4repr = (set_repr,)
        return sf

    __match_args__ = ('base_set',)
    @property
    def base_set(sf, /):
        return sf._s
    ##def __hash__(sf, /):
    ##def __eq__(sf, ot, /):
    @override
    def iter_boundaries4open_intervals(sf, /):
        '-> Iter boundary<OpenInterval>/(OO8inf|Tag_o0o8inv_inf)'
        return sf._s.iter_boundaries4open_intervals()
    @override
    def __contains__(sf, k, /):
        '-> bool'
        return not k in sf.base_set
    @override
    def __neg__(sf, /):
        return sf.base_set
    @override
    def iter_merged_sorted_nonempty_open_intervals(sf, /):
        '-> (Iter nonempty-OpenInterval){sorted,merged} # components of sf'
        return negation_merged_sorted_nonempty_open_intervals(sf.base_set.iter_merged_sorted_nonempty_open_intervals())
assert whole_set_repr.eq__typed_((-empty_set_repr).as_cached_SetRepr_5Intervals)
assert whole_set_repr.eq__untyped_(-empty_set_repr)
assert empty_set_repr.eq__untyped_(-whole_set_repr)

class _ISetRepr_Intersection_Union(ISetRepr_IntervalBased, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, sets, /):
        ls = mk_tuple(sets)
        for x in ls:
            check_type_le(ISetRepr_IntervalBased, x)

        sf._args4repr = (ls,)
        sf._ls = ls

    __match_args__ = ('components',)
    @property
    def components(sf, /):
        return sf._ls
    ##def __hash__(sf, /):
    ##def __eq__(sf, ot, /):
    @override
    def iter_boundaries4open_intervals(sf, /):
        '-> Iter boundary<OpenInterval>/(OO8inf|Tag_o0o8inv_inf)'
        return (b for s in sf._ls for b in s.iter_boundaries4open_intervals())
class SetRepr_Union(_ISetRepr_Intersection_Union):
    @override
    def __contains__(sf, k, /):
        '-> bool'
        return any(k in s for s in sf.components)
    @override
    def iter_merged_sorted_nonempty_open_intervals(sf, /):
        '-> (Iter nonempty-OpenInterval){sorted,merged} # components of sf'
        return union_iterable_of_merged_sorted_nonempty_open_intervals(set_repr.iter_merged_sorted_nonempty_open_intervals() for set_repr in sf.components)

class SetRepr_Intersection(_ISetRepr_Intersection_Union):
    @override
    def __contains__(sf, k, /):
        '-> bool'
        return all(k in s for s in sf.components)
    @override
    def iter_merged_sorted_nonempty_open_intervals(sf, /):
        '-> (Iter nonempty-OpenInterval){sorted,merged} # components of sf'
        return intersection_iterable_of_merged_sorted_nonempty_open_intervals(set_repr.iter_merged_sorted_nonempty_open_intervals() for set_repr in sf.components)









class Colored(Cased):
    @property
    def color(sf, /):
        return sf.case
class HollowTransition(_Base4repr, tuple):
    def __new__(cls, src, dst, /):
        return tuple.__new__(cls, [src, dst])
    def __init__(sf, src, dst, /):
        pass

    __match_args__ = ('src', 'dst')
    @property
    def src(sf, /):
        return sf[0]
    @property
    def dst(sf, /):
        return sf[1]
    @property
    def _args4repr(sf, /):
        return sf
class SolidTransition(_Base4repr, tuple):
    def __new__(cls, src, sym_set, dst, /):
        return tuple.__new__(cls, [src, sym_set, dst])
    def __init__(sf, src, sym_set, dst, /):
        pass
    __match_args__ = ('src', 'sym_set', 'dst')
    @property
    def src(sf, /):
        return sf[0]
    @property
    def sym_set(sf, /):
        return sf[1]
    @property
    def dst(sf, /):
        return sf[2]
    @property
    def _args4repr(sf, /):
        return sf


class IRegexRepr(ABC):
    r'''[[[
    [parallel_state =[def]= state of NFA]
    [merged_state =[def]= state of DFA]
    [merged_state <=> {parallel_state}]

        FSM (Finite State Machine)
        DFA (deterministic finite automaton)
        NFA (nondeterministic finite automaton)

        nondeterminisitc Turing machine

    pst = parallel_state
    offset = parallel_state6parent
    color for extra stop_parallel_states
        setting:interesting_colors


    usage:
    hollow_regex << regex
    dead_regex | regex
    regex % color
    regex / empty_set_repr[...]
    regex[0:+oo:1]

    #]]]'''#'''
    __slots__ = ()
    @property
    #@cached_property
    @abstractmethod
    def num_parallel_states(sf, /):
        '-> uint{>=1}'
    @abstractmethod
    def iter_xtransitions_(sf, offset, /):
        '-> Iter (colored_pst|hollow_transition|solid_transition)/(Colored(color,pst<offset>)|HollowTransition(pst<offset>, pst<offset>)|SolidTransition(pst<offset>, terminal_symbol_set, pst<offset>)) #allow dead transitions: i.e. [not terminal_symbol_set]'
        '-> Iter (colored_pst|hollow_transition|solid_transition)'
    @abstractmethod
    def start_parallel_state_(sf, offset, /):
        '-> pst<offset>'
    @abstractmethod
    def stop_parallel_state_(sf, offset, /):
        '-> pst<offset>'

    def __lshift__(sf, ot, /):
        'hollow_regex << regex'
        if ot is hollow_regex:
            #required by _mk_regex_array_eq/_mk_regex_array_le@RegexRepr_Array for regex[sz]
            return sf
        if not isinstance(ot, IRegexRepr):return NotImplemented
        if sf is hollow_regex:
            #required by __truediv__
            return ot
        return RegexRepr_Concatenation(sf, ot)
    #def __add__(sf, ot, /):
    def __or__(sf, ot, /):
        'dead_regex | regex'
        if ot is dead_regex:
            return sf
        if not isinstance(ot, IRegexRepr):return NotImplemented
        if sf is dead_regex:
            return ot
        return RegexRepr_Alternation(sf, ot)
    def __mod__(sf, color, /):
        'regex % color'
        return RegexRepr_Colored(sf, color)
    def __truediv__(sf, terminal_symbol_set, /):
        'regex / empty_set_repr[...]'
        ot = RegexRepr_SolidTransition(terminal_symbol_set)
        return sf << ot
    def __getitem__(sf, k, /):
        'regex[0:+oo:1]'
        check_type_is(slice, k)
        match k:
            case slice(start=start, stop=stop, step=step):
                pass
            case _:raise TypeError(type(k))
        if start is None:
            start = 0
        if step is None:
            step = 1
        if stop is +oo:
            stop = None
        match (start, stop, step):
            case (0, None, 1):
                return RegexRepr_Repetition(sf)
            case (1, None, 1):
                return RegexRepr_Many1(sf)
            case (0, 1, 1):
                return RegexRepr_Optional(sf)
            case _:
                return RegexRepr_Array(sf, start, stop, step)
        raise 000



class IRegexRepr__start_pst_is_0__stop_pst_is_1(IRegexRepr):
    __slots__ = ()
    @override
    def start_parallel_state_(sf, offset, /):
        '-> pst<offset>'
        return offset_uint2pst_(offset, 0)
    @override
    def stop_parallel_state_(sf, offset, /):
        '-> pst<offset>'
        return offset_uint2pst_(offset, 1)

def offset_uint2pst_(offset, u, /):
    check_int_ge(0, u)
    if type(offset) is int:
        return offset + u
    return HashedPair(offset, u)

class _IRegexRepr__01__repr(IRegexRepr__start_pst_is_0__stop_pst_is_1, _Base4repr):
    ___no_slots_ok___ = True
class _IRegexRepr__Concatenation_Alternation(_IRegexRepr__01__repr):
    @property
    @abstractmethod
    def _Concatenation_vs_Alternation_(sf, /):
        '-> bool'
    def __init__(sf, lhs_regex, rhs_regex, /):
        check_type_le(IRegexRepr, lhs_regex)
        check_type_le(IRegexRepr, rhs_regex)

        sf._args4repr = (lhs_regex, rhs_regex)
        sf._lhs = lhs_regex
        sf._rhs = rhs_regex
    @cached_property
    @override
    def num_parallel_states(sf, /):
        '-> uint{>=1}'
        return 2 + sf._lhs.num_parallel_states + sf._rhs.num_parallel_states
    @override
    def iter_xtransitions_(sf, offset, /):
        '-> Iter (colored_pst|hollow_transition|solid_transition)'
        _or = sf._Concatenation_vs_Alternation_

        pst0 = sf.start_parallel_state_(offset)
        pst1 = sf.stop_parallel_state_(offset)
        offset4lhs = offset_uint2pst_(offset, 2)
        offset4rhs = offset_uint2pst_(offset, 2 + sf._lhs.num_parallel_states)

        pst0_4lhs = sf._lhs.start_parallel_state_(offset4lhs)
        pst1_4lhs = sf._lhs.stop_parallel_state_(offset4lhs)

        pst0_4rhs = sf._rhs.start_parallel_state_(offset4rhs)
        pst1_4rhs = sf._rhs.stop_parallel_state_(offset4rhs)

        yield HollowTransition(pst0, pst0_4lhs)
        if _or:
            yield HollowTransition(pst0, pst0_4rhs)
            yield HollowTransition(pst1_4lhs, pst1)
        else:
            yield HollowTransition(pst1_4lhs, pst0_4rhs)
        yield HollowTransition(pst1_4rhs, pst1)

        yield from sf._lhs.iter_xtransitions_(offset4lhs)
        yield from sf._rhs.iter_xtransitions_(offset4rhs)
class RegexRepr_Concatenation(_IRegexRepr__Concatenation_Alternation):
    _Concatenation_vs_Alternation_ = False
class RegexRepr_Alternation(_IRegexRepr__Concatenation_Alternation):
    _Concatenation_vs_Alternation_ = True
class RegexRepr_Repetition(_IRegexRepr__01__repr):
    def __init__(sf, regex, /):
        check_type_le(IRegexRepr, regex)
        sf._args4repr = (regex,)
        sf._rex = regex
    @cached_property
    @override
    def num_parallel_states(sf, /):
        '-> uint{>=1}'
        return 2 + sf._rex.num_parallel_states
    @override
    def iter_xtransitions_(sf, offset, /):
        '-> Iter (colored_pst|hollow_transition|solid_transition)'
        pst0 = sf.start_parallel_state_(offset)
        pst1 = sf.stop_parallel_state_(offset)
        offset4rex = offset_uint2pst_(offset, 2)

        pst0_4rex = sf._rex.start_parallel_state_(offset4rex)
        pst1_4rex = sf._rex.stop_parallel_state_(offset4rex)

        yield HollowTransition(pst0, pst1)
        yield HollowTransition(pst1, pst0_4rex)
        yield HollowTransition(pst1_4rex, pst0)

        yield from sf._rex.iter_xtransitions_(offset4rex)
class RegexRepr_Wrapper(IRegexRepr, _Base4repr):
    'just used to alias regex expr #e.g. RegexRepr_Array/RegexRepr_Colored'
    ___no_slots_ok___ = True
    def __init__(sf, regex, /):
        check_type_le(IRegexRepr, regex)
        sf._args4repr = (regex,)
        sf._rex = regex
    @override
    def start_parallel_state_(sf, offset, /):
        '-> pst<offset>'
        return sf._rex.start_parallel_state_(offset)
    @override
    def stop_parallel_state_(sf, offset, /):
        '-> pst<offset>'
        return sf._rex.stop_parallel_state_(offset)
    @cached_property
    @override
    def num_parallel_states(sf, /):
        '-> uint{>=1}'
        return sf._rex.num_parallel_states
    @override
    def iter_xtransitions_(sf, offset, /):
        '-> Iter (colored_pst|hollow_transition|solid_transition)'
        return sf._rex.iter_xtransitions_(offset)



#class RegexRepr_Colored(_IRegexRepr__01__repr):
class RegexRepr_Colored(RegexRepr_Wrapper):
    'colored stop_parallel_state'
    def __init__(sf, regex, color, /):
        sf._c = color
        super().__init__(regex)
        777;    sf._args4repr = (regex, color)

    @override
    def iter_xtransitions_(sf, offset, /):
        '-> Iter (colored_pst|hollow_transition|solid_transition)'
        pst1 = sf.stop_parallel_state_(offset)
        yield Colored(color:=sf._c, pst1)
        yield from super().iter_xtransitions_(offset)

class RegexRepr_HollowTransition(_IRegexRepr__01__repr):
    'singleton:hollow_regex'
    _args4repr = ()
    #_sf = ...
    def __new__(cls, /):
        if not cls is __class__:raise TypeError(cls, __class__)
        try:
            return cls._sf
        except AttributeError:
            cls._sf = super(__class__, cls).__new__(cls)
            return cls()
    @cached_property
    @override
    def num_parallel_states(sf, /):
        '-> uint{>=1}'
        return 2
    num_parallel_states = 2

    @override
    def iter_xtransitions_(sf, offset, /):
        '-> Iter (colored_pst|hollow_transition|solid_transition)'
        pst0 = sf.start_parallel_state_(offset)
        pst1 = sf.stop_parallel_state_(offset)
        yield HollowTransition(pst0, pst1)
hollow_regex = RegexRepr_HollowTransition()
assert hollow_regex is RegexRepr_HollowTransition()

class RegexRepr_SolidTransition(_IRegexRepr__01__repr):
    '[terminal_symbol_set :: e.g. ISetRepr_IntervalBased]'
    def __init__(sf, terminal_symbol_set, /):
        check_type_le(ISetRepr_IntervalBased, terminal_symbol_set)
        sf._args4repr = (terminal_symbol_set,)
        sf._ts = terminal_symbol_set

    @cached_property
    @override
    def num_parallel_states(sf, /):
        '-> uint{>=1}'
        return 2
    num_parallel_states = 2

    @override
    def iter_xtransitions_(sf, offset, /):
        '-> Iter (colored_pst|hollow_transition|solid_transition)'
        pst0 = sf.start_parallel_state_(offset)
        pst1 = sf.stop_parallel_state_(offset)
        yield SolidTransition(pst0, sf._ts, pst1)

dead_regex = RegexRepr_SolidTransition(empty_set_repr)

class RegexRepr_Array(RegexRepr_Wrapper):
    r'''[[[
    regex[0:]
        tail_recur => RegexRepr_Repetition must be primitive
    regex[0:1]
        regex[0:1] = (regex | hollow_regex)
    regex[sz]
        regex[sz] =[def]= if sz > 0 then (regex << regex[sz-1]) else hollow_regex
    regex[0:sz:step]
        regex[0:sz:step] =[def]= if 0 < sz >= step > 0 then (regex[step] << regex[0:sz-step:step])[0:1] else hollow_regex
        regex[0:sz:step] =[def]= [step>0]regex[step][0:sz//step]
    regex[min:max:step]
        regex[min:max:step] =[def]= if 0 <= statr < max and max-min >= step > 0 then (regex[min] << regex[0:max-min:step]) else hollow_regex
        regex[min:max:step] =[def]= [min>=0][step>0](regex[min] << regex[0:max-min:step])
        regex[min:max:step] =[def]= [min>=0][step>0](regex[min] << regex[step][0:(max-min)//step])
    #]]]'''#'''
    def __init__(sf, regex, min_sz=None, max_sz=None, step_sz=None, /):
        check_type_le(IRegexRepr, regex)
        if min_sz is None:
            min_sz = 0
        if step_sz is None:
            step_sz = 1
        check_int_ge(0, min_sz)
        check_int_ge(1, step_sz)
        if max_sz is None:
            max_sz = +oo
        else:
            check_int_ge(min_sz, max_sz)

        max_num_blocks = (max_sz - min_sz) //step_sz

        header = _mk_regex_array_eq(regex, min_sz)
        block = _mk_regex_array_eq(regex, step_sz)

        if max_num_blocks == +oo:
            body = RegexRepr_Repetition(block)
        else:
            body = _mk_regex_array_le(block, max_num_blocks)
        body
        whole = header << body

        if max_sz == +oo:
            max_sz = None
        args = [regex, min_sz, max_sz, step_sz]
        if step_sz == 1:
            args.pop()
            if max_sz is None:
                args.pop()
                if min_sz == 0:
                    args.pop()
        super().__init__(whole)
        777;    sf._args4repr = (regex, *args)
class RegexRepr_Optional(RegexRepr_Wrapper):
    def __init__(sf, regex, /):
        check_type_le(IRegexRepr, regex)
        whole = _mk_regex_array_le(regex, 1)
        super().__init__(whole)
        777;    sf._args4repr = (regex,)
class RegexRepr_Many1(RegexRepr_Wrapper):
    'positive closure'
    def __init__(sf, regex, /):
        check_type_le(IRegexRepr, regex)
        whole = regex << RegexRepr_Repetition(regex)
        sf._args4repr = (regex,)
        super().__init__(whole)
        777;    sf._args4repr = (regex,)

def _mk_regex_array_le(regex, max_sz, /):
    'regex[0:max_sz] #RegexRepr_Optional'
    check_type_le(IRegexRepr, regex)
    check_int_ge(0, max_sz)
    block = hollow_regex
    for _ in range(max_sz):
        block = (regex << block) | hollow_regex
    block
    return block
def _mk_regex_array_eq(regex, sz, /):
    'regex[sz] #RegexRepr_Array'
    check_type_le(IRegexRepr, regex)
    check_int_ge(0, sz)
    block = hollow_regex
    for _ in range(sz):
        #block <<= regex
        block = regex << block
    block
    return block






r'''[[[
xxx
    @cached_property
    def num_parallel_states(sf, /):
        '-> uint{>=1}'
    @property
    def start_parallel_state(sf, /):
        '-> pst'
    @property
    def stop_parallel_state(sf, /):
        '-> pst'
    def iter_hollow_transitions_(sf, offset, /):
        '-> Iter (pst<offset>, pst<offset>)'
    def iter_solid_transitions_(sf, offset, /):
        '-> Iter (pst<offset>, terminal_symbol_set, pst<offset>) #allow dead transitions: i.e. [not terminal_symbol_set]'
#]]]'''#'''


__all__
from seed.recognize.regex.RegexRepr import hollow_regex, dead_regex, empty_set_repr, whole_set_repr
from seed.recognize.regex.RegexRepr import SetRepr_5Unicode_property
from seed.recognize.regex.RegexRepr import *
