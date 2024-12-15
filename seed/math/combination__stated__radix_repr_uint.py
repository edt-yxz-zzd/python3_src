#__all__:goto
r'''[[[
e ../../python3_src/seed/math/combination__stated__radix_repr_uint.py
view ../../python3_src/seed/math/combination__stated.py
view ../../python3_src/seed/int_tools/digits/uint2radix_repr.py
view ../../python3_src/seed/int_tools/digits/radix_repr2uint.py
TODO: begin,end,imay_radix4beyond(at_least 1 digit >= radix4beyond)


seed.math.combination__stated__radix_repr_uint
py -m nn_ns.app.debug_cmd   seed.math.combination__stated__radix_repr_uint -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.combination__stated__radix_repr_uint:__doc__ -ht # -ff -df


>>> it = RadixNumerationIterator.mk5params_(10, 8, 210, imay_radix4beyond=8, _may_digits4begin_=None, _may_digits4end_=None)
>>> iter(it) is it
True
>>> st = it.tell()
>>> ls = [*it]
>>> len(ls)
74
>>> len(ls) - (210 - 0o210)
0
>>> for x in ls:x
(8, (8,))
(9, (9,))
(18, (1, 8))
(19, (1, 9))
(28, (2, 8))
(29, (2, 9))
(38, (3, 8))
(39, (3, 9))
(48, (4, 8))
(49, (4, 9))
(58, (5, 8))
(59, (5, 9))
(68, (6, 8))
(69, (6, 9))
(78, (7, 8))
(79, (7, 9))
(80, (8, 0))
(81, (8, 1))
(82, (8, 2))
(83, (8, 3))
(84, (8, 4))
(85, (8, 5))
(86, (8, 6))
(87, (8, 7))
(88, (8, 8))
(89, (8, 9))
(90, (9, 0))
(91, (9, 1))
(92, (9, 2))
(93, (9, 3))
(94, (9, 4))
(95, (9, 5))
(96, (9, 6))
(97, (9, 7))
(98, (9, 8))
(99, (9, 9))
(108, (1, 0, 8))
(109, (1, 0, 9))
(118, (1, 1, 8))
(119, (1, 1, 9))
(128, (1, 2, 8))
(129, (1, 2, 9))
(138, (1, 3, 8))
(139, (1, 3, 9))
(148, (1, 4, 8))
(149, (1, 4, 9))
(158, (1, 5, 8))
(159, (1, 5, 9))
(168, (1, 6, 8))
(169, (1, 6, 9))
(178, (1, 7, 8))
(179, (1, 7, 9))
(180, (1, 8, 0))
(181, (1, 8, 1))
(182, (1, 8, 2))
(183, (1, 8, 3))
(184, (1, 8, 4))
(185, (1, 8, 5))
(186, (1, 8, 6))
(187, (1, 8, 7))
(188, (1, 8, 8))
(189, (1, 8, 9))
(190, (1, 9, 0))
(191, (1, 9, 1))
(192, (1, 9, 2))
(193, (1, 9, 3))
(194, (1, 9, 4))
(195, (1, 9, 5))
(196, (1, 9, 6))
(197, (1, 9, 7))
(198, (1, 9, 8))
(199, (1, 9, 9))
(208, (2, 0, 8))
(209, (2, 0, 9))
>>> [*it]
[]
>>> ls == [*it]
False
>>> it.seek(st)
>>> ls == [*it]
True
>>> it2 = RadixNumerationIterator.mk5params_(10, 0, 210, imay_radix4beyond=8, _may_digits4begin_=None, _may_digits4end_=None)
>>> ls == [*it2]
True


py_adhoc_call   seed.math.combination__stated__radix_repr_uint   @f
#]]]'''
__all__ = r'''
IBaseStatedIterator
    RadixNumerationIterator
        next_ex4radix_numeration_
            Mutable_st4radix_numeration
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.int_tools.digits.uint2radix_repr import uint2radix_repr__big_endian
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny_._Base4repr import _Base4repr
from seed.helper.repr_input import repr_helper

from seed.tiny_.check import check_type_is, check_int_ge, check_non_ABC, check_may_

#from seed.math.combination__stated import SinglyLinkedList4idx, Mutable_st4perm, Mutable_st4comb, Mutable_st4comb__descending, Mutable_st4prod
from seed.math.combination__stated import IBase4TellSeekState
from seed.abc.IStated import IStated, IStated__mk_dummy, BoxedXState
from seed.abc.IStated import IStated, IStated__mk_dummy, IStated__eq_immutable_core_xstate_isolated, IStated__immutable_core_xstate_is_Eq, IStated__immutable_core_xstate_is_IEqTmpVal
from seed.abc.IStated import IStated, copy2boxed_xstate_, tell_, seek_, save_as_boxed_wst_, half_seek_, mk_obj5boxed_wst_, mk5boxed_wst_
from seed.types.attr.special_method6class_and_class_only_property import special_method6class

___end_mark_of_excluded_global_names__0___ = ...

class _IBase4TellSeekState(IBase4TellSeekState, IStated__mk_dummy):
    '[IBase4TellSeekState.st =[def]= IStated__mk_dummy.boxed_wst{boxed_rwst}]'
    __slots__ = ()
    @override
    def __getstate__(sf, /):
        '-> may st # [None=>skip __setstate__]'
        st = boxed_wst = save_as_boxed_wst_(sf, save_time=True)
        boxed_wst.rwst#boxed_rwst
        return st
    @override
    def __setstate__(sf, st, /):
        'st{not None} -> None'
        half_seek_(sf, boxed_wst:=st)
    @classmethod
    @override
    def mk5st_(cls, st, /):
        return mk5boxed_wst_(cls, boxed_wst:=st)

    @special_method6class
    @abstractmethod
    def _copy2xstate_(sf, /, *, core_only:bool, mutable_only:bool, to_copy:bool):
        '-> (vst if mutable_only else wst)/xst/(may immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate) # [to_copy=>xst@now][not to_copy=>xst@(view|original_inuse_data)]'
    @special_method6class
    @abstractmethod
    def _copy5vstate_(sf, vst, /, *, core_only:bool, to_copy:bool):
        'vst/(None, mutable_core_xstate, None, may mutable_redundant_xstate) -> None # [mutable_only===True] # [not to_copy=>move vst, vst will be invalid]'
    @special_method6class
    @abstractmethod
    def _get_emay_may_may_args_may_kwds4repr_(sf, /, *, to_copy:bool):
        '-> emay may (may args, may kwds) # [... => using object.__repr__]'
    @special_method6class
    @classmethod
    @abstractmethod
    def _mk_dummy5immutable_part_(cls, immutable_core_xstate, may_immutable_redundant_xstate, /, *, core_only:bool):
        '-> sf7dummy/cls # be used to impl _make5wstate_()'
    #.@special_method6class
    #.@classmethod
    #.@abstractmethod
    #.def _make5wstate_(cls, wst, /, *, core_only:bool, to_copy:bool):
    #.    'wst/(immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate) -> sf/cls # [mutable_only===False] # [not to_copy=>move wst, wst will be invalid]'

class IBaseStatedIterator(IBase4TellSeekState):
    #using old-simpler-API
    #class IBaseStatedIterator(_IBase4TellSeekState):
    #__slots__ = ()
    ___no_slots_ok___ = True
    @property#@classmethod
    @abstractmethod
    def _type4mutable_st_(sf, /):
        '-> type(mutable_st) <: IBase4TellSeekState'
    @abstractmethod
    def _next_ex4item_(sf, mutable_st, /):
        'mutable_st -> (item, known_stop/bool)|^StopIteration'
    @override
    def __getstate__(sf, /):
        may_mutable_st = sf._m
        if None is may_mutable_st:
            return False
        mutable_st = may_mutable_st
        return mutable_st.tell()
    @override
    def __setstate__(sf, st, /):
        if st is False:
            may_mutable_st = None
        else:
            mutable_st = type(sf)._type4mutable_st_.mk5st_(st)
            may_mutable_st = mutable_st
        sf.__init__(may_mutable_st)
    def __repr__(sf, /):
        return repr_helper(sf, sf._m)
    def __init__(sf, may_mutable_st, /):
        if not None is may_mutable_st:
            mutable_st = may_mutable_st
            check_type_is(type(sf)._type4mutable_st_, mutable_st)
        sf._m = may_mutable_st
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        may_mutable_st = sf._m
        if None is may_mutable_st:
            raise StopIteration
        mutable_st = may_mutable_st
        try:
            r = sf._next_ex4item_(mutable_st)
        except StopIteration:
            sf._m = None
            raise
        (item, known_stop) = r
        if known_stop:
            sf._m = None
        return item


class Mutable_st4radix_numeration(_IBase4TellSeekState, IStated__immutable_core_xstate_is_Eq):
    #using new-more_complex-API
    #class Mutable_st4radix_numeration(IBase4TellSeekState, _Base4repr):
    ___no_slots_ok___ = True

    def __init__(sf, radix, begin, may_end, /, *, imay_radix4beyond=-1, _may_digits4begin_=None, _may_digits4end_=None):
        #def __init__(sf, radix, begin, may_end, /, *, imay_radix4beyond, _may_digits4begin_, _may_digits4end_):
        sf._rwst = type(sf)._prepare4init_(radix, begin, may_end, raise_vs_None=False, imay_radix4beyond=imay_radix4beyond, _may_digits4begin_=_may_digits4begin_, _may_digits4end_=_may_digits4end_)
            # ^TypeError
        return
        ######################
        sf._rwst = [immutable_core_xstate, mutable_core_xstate, immutable_redundant_xstate, mutable_redundant_xstate]
        return
        sf._rwst
        (immutable_core_xstate, mutable_core_xstate, immutable_redundant_xstate, mutable_redundant_xstate) = sf.rwst
        ((radix, may_end, imay_radix4beyond), begin, may_digits4end, digits4begin) = sf.rwst
        ######################
    @classmethod
    def mk_may_(cls, radix, begin, may_end, /, *, imay_radix4beyond=-1, _may_digits4begin_=None, _may_digits4end_=None):
        '-> may sf'
        may_rwst = cls._prepare4init_(radix, begin, may_end, raise_vs_None=True, imay_radix4beyond=imay_radix4beyond, _may_digits4begin_=_may_digits4begin_, _may_digits4end_=_may_digits4end_)
        if may_rwst is None:
            may_sf = None
        else:
            rwst = may_rwst
            ((radix, may_end, imay_radix4beyond), begin, may_digits4end, digits4begin) = rwst
            sf = cls(radix, begin, may_end, imay_radix4beyond=imay_radix4beyond, _may_digits4begin_=_may_digits4begin_, _may_digits4end_=_may_digits4end_)
            may_sf = sf
        return may_sf
    @classmethod
    def _prepare4init_(cls, radix, begin, may_end, /, *, raise_vs_None, imay_radix4beyond=-1, _may_digits4begin_=None, _may_digits4end_=None):
        '-> may rwst if raise_vs_None else (rwst|^TypeError)'
        check_type_is(bool, raise_vs_None)
        b_err = False
        if not raise_vs_None:
            # ->rwst|^TypeError
            def on_err():
                raise TypeError
        else:
            # ->may_rwst
            def on_err():
                nonlocal b_err
                b_err = True
        on_err

        ######################
        check_int_ge(2, radix)
        check_int_ge(0, begin)
        #check_may_([check_int_ge, begin+1], may_end)
            #check_int_ge(begin+1, end)
        if not may_end is None:
            end = may_end
            #check_int_ge(begin, end)
            check_int_ge(0, end)
            if not begin < end: on_err()


        ######################
        check_int_ge(-1, imay_radix4beyond)
        #if not imay_radix4beyond < radix:raise TypeError
        if not imay_radix4beyond < radix: on_err()

        ######################
        check_may_([check_type_is, list], _may_digits4begin_)
        check_may_([check_type_is, list], _may_digits4end_)
        if may_end is None is not _may_digits4end_:raise TypeError
        if may_end is not None is _may_digits4end_:
            end = may_end
            #check_int_ge(begin+1, end)
            digits4end = list(uint2radix_repr__big_endian(radix, end))
            _may_digits4end_ = digits4end
        may_digits4end = _may_digits4end_
        may_digits4end
        if None is _may_digits4begin_:
            digits4begin = list(uint2radix_repr__big_endian(radix, begin))
        else:
            digits4begin = _may_digits4begin_
        digits4begin

        ######################
        check_may_([check_type_is, list], may_digits4end)
        check_type_is(list, digits4begin)
        assert not (digits4begin and digits4begin[0] == 0)
        if not may_digits4end is None:
            digits4end = may_digits4end
            assert not (digits4end and digits4end[0] == 0)
            #check_int_ge(begin+1, end)
            #assert not len(digits4begin) > len(digits4end), TypeError
            #assert not (len(digits4begin) == len(digits4end) and digits4begin >= digits4end), TypeError
            if len(digits4begin) > len(digits4end): on_err()
            elif (len(digits4begin) == len(digits4end) and digits4begin >= digits4end): on_err()
        ######################
        #assert (imay_radix4beyond == -1 or any(j >= imay_radix4beyond for j in digits4begin))
        #if not (imay_radix4beyond == -1 or any(j >= imay_radix4beyond for j in digits4begin)): on_err()
        if 0 <= imay_radix4beyond < radix:
            radix4beyond = imay_radix4beyond
            if not any(j >= radix4beyond for j in digits4begin):
                if not digits4begin:
                    delta4begin = 1 if radix4beyond == 0 else radix4beyond
                    digits4begin.append(delta4begin)
                else:
                    delta4begin = radix4beyond - digits4begin[-1]
                    digits4begin[-1] = radix4beyond
                assert 0 < delta4begin < radix
                begin += delta4begin
                if may_end is not None and end <= begin: on_err()
        ######################
        b_err
        ######################
        radix, begin, may_end, imay_radix4beyond, digits4begin, may_digits4end
        ######################
        immutable_core_xstate = (radix, may_end, imay_radix4beyond)
        mutable_core_xstate = begin
        immutable_redundant_xstate = may_digits4end
        mutable_redundant_xstate = digits4begin
        ######################
        rwst = [immutable_core_xstate, mutable_core_xstate, immutable_redundant_xstate, mutable_redundant_xstate]
        ######################
        may_rwst = None if b_err else rwst
        return may_rwst
        ######################
    @property
    def rwst(sf, /):
        return tuple(sf._rwst)
    @property
    def radix(sf, /):
        return sf._rwst[0][0]
    @property
    def may_end(sf, /):
        return sf._rwst[0][1]
    @property
    def imay_radix4beyond(sf, /):
        return sf._rwst[0][2]
    @property
    def begin(sf, /):
        return sf._rwst[1]
    @begin.setter
    def begin(sf, begin, /):
        sf._rwst[1] = begin
    @property
    def may_digits4end(sf, /):
        return sf._rwst[2]
    @property
    def digits4begin(sf, /):
        return sf._rwst[3]

    @special_method6class
    @override
    def _copy2xstate_(sf, /, *, core_only:bool, mutable_only:bool, to_copy:bool):
        '-> (vst if mutable_only else wst)/xst/(may immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate) # [to_copy=>xst@now][not to_copy=>xst@(view|original_inuse_data)]'
        (may_immutable_core_xstate, mutable_core_xstate, may_immutable_redundant_xstate, may_mutable_redundant_xstate) = (immutable_core_xstate, mutable_core_xstate, immutable_redundant_xstate, mutable_redundant_xstate) = sf.rwst
        if core_only:
            may_immutable_redundant_xstate = None
            may_mutable_redundant_xstate = None
        if mutable_only:
            may_immutable_core_xstate = None
            may_immutable_redundant_xstate = None
        if to_copy:
            mutable_core_xstate
                #begin
            may_mutable_redundant_xstate
                #may digits4begin
            if not None is may_mutable_redundant_xstate:
                digits4begin = may_mutable_redundant_xstate
                may_mutable_redundant_xstate = digits4begin.copy()
        xst = (may_immutable_core_xstate, mutable_core_xstate, may_immutable_redundant_xstate, may_mutable_redundant_xstate)
        return xst
    @special_method6class
    @override
    def _copy5vstate_(sf, vst, /, *, core_only:bool, to_copy:bool):
        'vst/(None, mutable_core_xstate, None, may mutable_redundant_xstate) -> None # [mutable_only===True] # [not to_copy=>move vst, vst will be invalid]'
        (_, mutable_core_xstate, _, may_mutable_redundant_xstate) = vst
        if sf.begin == mutable_core_xstate:
            return
        assert core_only is (may_mutable_redundant_xstate is None)
        if to_copy and may_mutable_redundant_xstate is not None:
            digits4begin = may_mutable_redundant_xstate
            may_mutable_redundant_xstate = digits4begin.copy()
        if may_mutable_redundant_xstate is None:
            begin = mutable_core_xstate
            digits4begin = list(uint2radix_repr__big_endian(sf.radix, begin))
            may_mutable_redundant_xstate = digits4begin
        mutable_redundant_xstate = may_mutable_redundant_xstate
        sf._rwst[1] = mutable_core_xstate
        sf._rwst[3] = mutable_redundant_xstate
    @special_method6class
    @override
    def _get_emay_may_may_args_may_kwds4repr_(sf, /, *, to_copy:bool):
        '-> emay may (may args, may kwds) # [... => using object.__repr__]'
        boxed_rwst = copy2boxed_xstate_(sf, core_only=False, mutable_only=False, to_copy=to_copy)
        (immutable_core_xstate, mutable_core_xstate, immutable_redundant_xstate, mutable_redundant_xstate) = boxed_rwst.rwst
        ((radix, may_end, imay_radix4beyond), begin, may_digits4end, digits4begin) = boxed_rwst.rwst
        args = (radix, begin, may_end)
        kwds = dict(imay_radix4beyond=imay_radix4beyond, _may_digits4begin_=digits4begin, _may_digits4end_=may_digits4end)
        return (args, kwds)
    @special_method6class
    @classmethod
    @override
    def _mk_dummy5immutable_part_(cls, immutable_core_xstate, may_immutable_redundant_xstate, /, *, core_only:bool):
        '-> sf7dummy/cls # be used to impl _make5wstate_()'
        assert core_only is (may_immutable_redundant_xstate is None)
        (radix, may_end, imay_radix4beyond) = immutable_core_xstate
        may_digits4end = may_immutable_redundant_xstate
        (begin, digits4begin) = (0, []) if immutable_core_xstate == -1 else (imay_radix4beyond, [imay_radix4beyond])
        return cls(radix, begin, may_end, imay_radix4beyond=imay_radix4beyond, _may_digits4begin_=digits4begin, _may_digits4end_=may_digits4end)
check_non_ABC(Mutable_st4radix_numeration)



class _IBaseBoundedIterator(IBaseStatedIterator):
    #@override
    _type4mutable_st_ = Mutable_st4radix_numeration
    @classmethod
    def mk5params_(cls, radix, begin, may_end, /, *, imay_radix4beyond, _may_digits4begin_, _may_digits4end_):
        'radix/uint -> begin/uint -> may_end/(may uint) -> (kw:imay_radix4beyond/int{>=-1}) -> (kw:_may_digits4begin_/(may [uint%radix])) -> (kw:_may_digits4end_/(may [uint%radix]))  -> sf/__class__ # [at_least 1 digit >= radix4beyond if not imay_radix4beyond == -1][_may_digits4begin_/_may_digits4end_ is used to fast restore, redundant of begin/may_end]'
        #, avoid_leading_zero:bool=True
        #def mk5params_(cls, radix, boundary4item, /, *, avoid_leading_zero:bool):
        may_mutable_st = cls._mk_may_mutable_st5params_(radix, begin, may_end, imay_radix4beyond=imay_radix4beyond, _may_digits4begin_=_may_digits4begin_, _may_digits4end_=_may_digits4end_)
        sf = cls(may_mutable_st)
        return sf
    @classmethod
    #@abstractmethod
    def _mk_may_mutable_st5params_(cls, radix, begin, may_end, /, *, imay_radix4beyond, _may_digits4begin_, _may_digits4end_):
        'radix/uint -> begin/uint -> may_end/(may uint) -> (kw:imay_radix4beyond/int{>=-1}) -> (kw:_may_digits4begin_/(may [uint%radix])) -> (kw:_may_digits4end_/(may [uint%radix]))  -> may_mutable_st # [at_least 1 digit >= radix4beyond if not imay_radix4beyond == -1][_may_digits4begin_/_may_digits4end_ is used to fast restore, redundant of begin/may_end]'
        if not imay_radix4beyond < radix:
            may_mutable_st = None
        elif None is not may_end <= begin:
            may_mutable_st = None
        else:
            may_mutable_st = Mutable_st4radix_numeration.mk_may_(radix, begin, may_end, imay_radix4beyond=imay_radix4beyond, _may_digits4begin_=_may_digits4begin_, _may_digits4end_=_may_digits4end_)
        may_mutable_st
        return may_mutable_st


class RadixNumerationIterator(_IBaseBoundedIterator):
    r'''[[[
    [item4radix_numeration == (u, digits4u) == item]
    [mutable_st :: Mutable_st4radix_numeration]
    #]]]'''#'''

    @override
    def _next_ex4item_(sf, mutable_st, /):
        return next_ex4radix_numeration_(mutable_st)
def next_ex4radix_numeration_(mutable_st, /):
    'Mutable_st4radix_numeration -> (item4radix_numeration, known_stop/bool)|^StopIteration'
    ((radix, may_end, imay_radix4beyond), begin, may_digits4end, digits4begin) = mutable_st.rwst
    u = begin
    digits4u = digits4begin
    item4radix_numeration = (u, tuple(digits4u))
    ######################
    # vivi: 999+1-->1000
    # vivi: 666999+1-->667000
    avoid = radix-1
    for k4j, j in zip(reversed(range(len(digits4u))), reversed(digits4u)):
        if not j == avoid:
            #bug:assert imay_radix4beyond <= j < avoid, (imay_radix4beyond, radix, digits4u, k4j, j, avoid)
            assert j < avoid, (imay_radix4beyond, radix, digits4u, k4j, j, avoid)
            acc = False
            break
    else:
        acc = True
    acc
    m = max(0, imay_radix4beyond)
    if acc:
        digits4u[:] = [0]*(1+len(digits4u))
        digits4u[0] = 1
    else:
        k4j, j
        digits4u[k4j+1:] = [0]*(len(digits4u)-k4j-1)
        digits4u[k4j] = j+1
    delta = 1
    if not (imay_radix4beyond == -1 or any(j >= imay_radix4beyond for j in digits4u)):
        delta += imay_radix4beyond - digits4u[-1]
        digits4u[-1] = imay_radix4beyond
    delta, digits4u
    u += delta
    mutable_st.begin = begin = u
    known_stop = None is not may_end <= begin
    ######################
    return (item4radix_numeration, known_stop)







__all__
from seed.math.combination__stated__radix_repr_uint import IBaseStatedIterator
from seed.math.combination__stated__radix_repr_uint import RadixNumerationIterator
from seed.math.combination__stated__radix_repr_uint import *
