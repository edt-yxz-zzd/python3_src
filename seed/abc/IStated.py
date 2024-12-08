#__all__:goto
r'''[[[
e ../../python3_src/seed/abc/IStated.py
++__reduce__()
    view ../../python3_src/seed/for_libs/for_pickle.py
sf._xxx_(...) --> type(sf)._xxx_(sf, ...)
    %s/\(sf\w*\)\.\(_\w*_\)(/type(\1).\2(\1, /g
        #))
sf.xxx_ --> sf.__xxx___
    # intended: 2 "_" and 3 "_"
    %s/\<\(copy2boxed_xstate_\|tell_\|seek_\|save_as_boxed_wst_\|mk5boxed_wst_\)\>/__\0__/g
    /\(copy2boxed_xstate_\|tell_\|seek_\|save_as_boxed_wst_\|mk5boxed_wst_\)
e ../../python3_src/seed/abc/IStated.py
e ../../python3_src/seed/helper/lazy_import.py
e ../../python3_src/seed/for_libs/for_importlib.py



py -m seed.abc.IStated
    for:_testing_via_RadixNumerationCounter()
py -m nn_ns.app.debug_cmd   seed.abc.IStated -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.abc.IStated:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.abc.IStated:__doc__ -ht     >  /sdcard/0my_files/tmp/0tmp      2>&1
view /sdcard/0my_files/tmp/0tmp
















######################
BoxedXState
>>> boxed_xst = BoxedXState(type4obj:=None, core_only:=False, mutable_only:=False, copied:=False, xst:=(None, None, None, None))
>>> boxed_xst.xst is boxed_xst.rst is boxed_xst.wst is boxed_xst.rwst
True
>>> boxed_xst = BoxedXState(type4obj:=None, core_only:=False, mutable_only:=False, copied:=True, xst:=(None, None, None, None))
>>> boxed_xst.xst is boxed_xst.rst is boxed_xst.wst is boxed_xst.rwst
True

>>> boxed_xst = BoxedXState(type4obj:=None, core_only:=False, mutable_only:=True, copied:=False, xst:=(None, None, None, None))
>>> boxed_xst.xst is boxed_xst.rst is boxed_xst.vst is boxed_xst.rvst
True
>>> boxed_xst = BoxedXState(type4obj:=None, core_only:=False, mutable_only:=True, copied:=True, xst:=(None, None, None, None))
>>> boxed_xst.xst is boxed_xst.rst is boxed_xst.vst is boxed_xst.rvst
True

>>> boxed_xst = BoxedXState(type4obj:=None, core_only:=True, mutable_only:=False, copied:=False, xst:=(None, None, None, None))
>>> boxed_xst.xst is boxed_xst.kst is boxed_xst.wst is boxed_xst.kwst
True
>>> boxed_xst = BoxedXState(type4obj:=None, core_only:=True, mutable_only:=False, copied:=True, xst:=(None, None, None, None))
>>> boxed_xst.xst is boxed_xst.kst is boxed_xst.wst is boxed_xst.kwst
True

>>> boxed_xst = BoxedXState(type4obj:=None, core_only:=True, mutable_only:=True, copied:=False, xst:=(None, None, None, None))
>>> boxed_xst.xst is boxed_xst.kst is boxed_xst.vst is boxed_xst.kvst
True
>>> boxed_xst = BoxedXState(type4obj:=None, core_only:=True, mutable_only:=True, copied:=True, xst:=(None, None, None, None))
>>> boxed_xst.xst is boxed_xst.kst is boxed_xst.vst is boxed_xst.kvst
True



>>> def _1_test_BoxedXState(boxed_xst, /):
...     rk = 'rk'[boxed_xst.core_only]
...     wv = 'wv'[boxed_xst.mutable_only]
...     assert boxed_xst.xst is getattr(boxed_xst, f'{rk}{wv}st')
...     assert boxed_xst.xst is getattr(boxed_xst, f'{wv}st')
...     assert boxed_xst.xst is getattr(boxed_xst, f'{rk}st')
...     #
...     kr = 'rk'[not boxed_xst.core_only]
...     vw = 'wv'[not boxed_xst.mutable_only]
...     #
...     assert not hasattr(boxed_xst, f'{kr}st')
...     assert not hasattr(boxed_xst, f'{vw}st')
...     #
...     assert not hasattr(boxed_xst, f'{kr}vst')
...     assert not hasattr(boxed_xst, f'{kr}wst')
...     #
...     assert not hasattr(boxed_xst, f'k{vw}st')
...     assert not hasattr(boxed_xst, f'r{vw}st')
...     #
...     #
...     assert not hasattr(boxed_xst, f'{kr}{vw}st')
...     assert not hasattr(boxed_xst, f'{kr}{wv}st')
...     assert not hasattr(boxed_xst, f'{rk}{vw}st')
...     assert     hasattr(boxed_xst, f'{rk}{wv}st')
>>> def _999_test_BoxedXState():
...     from itertools import product
...     type4obj = None
...     xst = (None, None, None, None)
...     for (core_only, mutable_only, copied) in product([False, True], repeat=3):
...         boxed_xst = BoxedXState(type4obj, core_only, mutable_only, copied, xst)
...         _1_test_BoxedXState(boxed_xst)
>>> _999_test_BoxedXState()









######################
>>> import pickle
>>> import copy

######################
>>> _RadixNumerationCounter = _testing_via_RadixNumerationCounter()


pickle.dumps(_RadixNumerationCounter(8, 999))
    AttributeError: Can't pickle local object '_testing_via_RadixNumerationCounter.<locals>.RadixNumerationCounter'
        since only toplvl class can be pickled
==>>:
>>> class RadixNumerationCounter(_RadixNumerationCounter):pass

pickle.dumps(RadixNumerationCounter(8, 999))
    _pickle.PicklingError: Can't pickle <class 'seed.abc.IStated.RadixNumerationCounter'>: attribute lookup RadixNumerationCounter on seed.abc.IStated failed
        since only toplvl class can be pickled
==>>:
>>> import seed.abc.IStated
>>> seed.abc.IStated.RadixNumerationCounter = RadixNumerationCounter








######################
>>> c = RadixNumerationCounter(8, 999)
>>> c
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> oct(999)
'0o1747'
>>> bs = pickle.dumps(c)
>>> x = pickle.loads(bs)
>>> copy.copy(c) is c
False
>>> copy.copy(c)
RadixNumerationCounter(8, 999, [1, 7, 4, 7])

>>> p = RadixNumerationCounter(2, 666)
>>> p
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
>>> bin(666)
'0b1010011010'


>>> q = RadixNumerationCounter(8, 666)
>>> q
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> oct(666)
'0o1232'

######################
copy2boxed_xstate_
>>> copy2boxed_xstate_(c, core_only=False, mutable_only=False, to_copy=False)
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=False, copied=False, xst=(8, 999, None, [1, 7, 4, 7]))
>>> copy2boxed_xstate_(c, core_only=False, mutable_only=False, to_copy=True)
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=False, copied=True, xst=(8, 999, None, [1, 7, 4, 7]))
>>> copy2boxed_xstate_(c, core_only=False, mutable_only=True, to_copy=False)
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=True, copied=False, xst=(None, 999, None, [1, 7, 4, 7]))
>>> copy2boxed_xstate_(c, core_only=False, mutable_only=True, to_copy=True)
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=True, copied=True, xst=(None, 999, None, [1, 7, 4, 7]))
>>> copy2boxed_xstate_(c, core_only=True, mutable_only=False, to_copy=False)
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=False, copied=False, xst=(8, 999, None, None))
>>> copy2boxed_xstate_(c, core_only=True, mutable_only=False, to_copy=True)
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=False, copied=True, xst=(8, 999, None, None))
>>> copy2boxed_xstate_(c, core_only=True, mutable_only=True, to_copy=False)
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=True, copied=False, xst=(None, 999, None, None))
>>> copy2boxed_xstate_(c, core_only=True, mutable_only=True, to_copy=True)
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=True, copied=True, xst=(None, 999, None, None))


######################
tell_
seek_
>>> boxed_vst4Q_0 = tell_(q, save_time=False)
>>> boxed_vst4Q_0
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=True, copied=True, xst=(None, 666, None, None))
>>> boxed_vst4Q_0.vst
(None, 666, None, None)
>>> boxed_vst4Q_1 = tell_(q, save_time=True)
>>> boxed_vst4Q_1
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=True, copied=True, xst=(None, 666, None, [1, 2, 3, 2]))
>>> boxed_vst4Q_1.vst
(None, 666, None, [1, 2, 3, 2])

>>> boxed_vst4C_0 = tell_(c, save_time=False)
>>> boxed_vst4C_0
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=True, copied=True, xst=(None, 999, None, None))
>>> boxed_vst4C_0.vst
(None, 999, None, None)
>>> boxed_vst4C_1 = tell_(c, save_time=True)
>>> boxed_vst4C_1
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=True, copied=True, xst=(None, 999, None, [1, 7, 4, 7]))
>>> boxed_vst4C_1.vst
(None, 999, None, [1, 7, 4, 7])


>>> q
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> seek_(q, boxed_vst4C_0)
>>> q
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> seek_(q, boxed_vst4Q_0)
>>> q
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> seek_(q, boxed_vst4C_1)
>>> q
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> seek_(q, boxed_vst4Q_1)
>>> q
RadixNumerationCounter(8, 666, [1, 2, 3, 2])


######################
save_as_boxed_wst_
half_seek_
>>> boxed_wst4Q_0 = save_as_boxed_wst_(q, save_time=False)
>>> boxed_wst4Q_0
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=False, copied=True, xst=(8, 666, None, None))
>>> boxed_wst4Q_0.wst
(8, 666, None, None)
>>> boxed_wst4Q_1 = save_as_boxed_wst_(q, save_time=True)
>>> boxed_wst4Q_1
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=False, copied=True, xst=(8, 666, None, [1, 2, 3, 2]))
>>> boxed_wst4Q_1.wst
(8, 666, None, [1, 2, 3, 2])

>>> boxed_wst4C_0 = save_as_boxed_wst_(c, save_time=False)
>>> boxed_wst4C_0
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=False, copied=True, xst=(8, 999, None, None))
>>> boxed_wst4C_0.wst
(8, 999, None, None)
>>> boxed_wst4C_1 = save_as_boxed_wst_(c, save_time=True)
>>> boxed_wst4C_1
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=False, copied=True, xst=(8, 999, None, [1, 7, 4, 7]))
>>> boxed_wst4C_1.wst
(8, 999, None, [1, 7, 4, 7])


>>> q
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> half_seek_(q, boxed_wst4C_0)
>>> q
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> half_seek_(q, boxed_wst4Q_0)
>>> q
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> half_seek_(q, boxed_wst4C_1)
>>> q
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> half_seek_(q, boxed_wst4Q_1)
>>> q
RadixNumerationCounter(8, 666, [1, 2, 3, 2])



>>> boxed_wst4P_0 = save_as_boxed_wst_(p, save_time=False)
>>> boxed_wst4P_0
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=True, mutable_only=False, copied=True, xst=(2, 666, None, None))
>>> boxed_wst4P_0.wst
(2, 666, None, None)
>>> boxed_wst4P_1 = save_as_boxed_wst_(p, save_time=True)
>>> boxed_wst4P_1
BoxedXState(type4obj=<class 'seed.abc.IStated.RadixNumerationCounter'>, core_only=False, mutable_only=False, copied=True, xst=(2, 666, None, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]))
>>> boxed_wst4P_1.wst
(2, 666, None, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

>>> p
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
>>> half_seek_(p, boxed_wst4C_0)
Traceback (most recent call last):
    ...
seed.abc.IStated.Error__unmatched_immutable_core_xstate
>>> p
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
>>> half_seek_(p, boxed_wst4P_0)
>>> p
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
>>> half_seek_(p, boxed_wst4C_1)
Traceback (most recent call last):
    ...
seed.abc.IStated.Error__unmatched_immutable_core_xstate
>>> p
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
>>> half_seek_(p, boxed_wst4P_1)
>>> p
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])




######################
save_as_boxed_wst_
mk5boxed_wst_
>>> mk5boxed_wst_(RadixNumerationCounter, boxed_wst4C_0)
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> mk5boxed_wst_(RadixNumerationCounter, boxed_wst4C_1)
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> mk5boxed_wst_(RadixNumerationCounter, boxed_wst4Q_0)
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> mk5boxed_wst_(RadixNumerationCounter, boxed_wst4Q_1)
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> mk5boxed_wst_(RadixNumerationCounter, boxed_wst4P_0)
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
>>> mk5boxed_wst_(RadixNumerationCounter, boxed_wst4P_1)
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])




######################
save_as_boxed_wst_
mk_obj5boxed_wst_
>>> mk_obj5boxed_wst_(boxed_wst4C_0)
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> mk_obj5boxed_wst_(boxed_wst4C_1)
RadixNumerationCounter(8, 999, [1, 7, 4, 7])
>>> mk_obj5boxed_wst_(boxed_wst4Q_0)
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> mk_obj5boxed_wst_(boxed_wst4Q_1)
RadixNumerationCounter(8, 666, [1, 2, 3, 2])
>>> mk_obj5boxed_wst_(boxed_wst4P_0)
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
>>> mk_obj5boxed_wst_(boxed_wst4P_1)
RadixNumerationCounter(2, 666, [1, 0, 1, 0, 0, 1, 1, 0, 1, 0])




######################
>>> del seed.abc.IStated.RadixNumerationCounter


py_adhoc_call   seed.abc.IStated   @f
#]]]'''
__all__ = r'''
BoxedXState
    mk_obj5boxed_wst_

IStated
    copy2boxed_xstate_
    tell_
    seek_
    save_as_boxed_wst_
    mk5boxed_wst_
    half_seek_

IStated
    IStated__mk_dummy
    IStated__eq_immutable_core_xstate_isolated
        IStated__immutable_core_xstate_is_Eq
        IStated__immutable_core_xstate_is_IEqTmpVal



Error
    Error__unmatched_immutable_core_xstate
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.attr.special_method6class_and_class_only_property import special_method6class

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import ifNone
#from seed.tiny_._Base4repr import _Base4repr
from seed.helper.repr_input import repr_helper

from seed.tiny_.check import check_type_is, check_int_ge, check_non_ABC

from seed.abc.IEqTmpVal import IEqTmpVal, IEqTmpVal__via_iter_sized_args_kwds
from seed.abc.IEqTmpVal import eq8obj, eq8tmp_val, whether_obj_vs_val_
from seed.abc.IEqTmpVal import lookup_ops8IEqTmpVal4cls_, register_ops8IEqTmpVal4cls_
from collections import namedtuple

___end_mark_of_excluded_global_names__0___ = ...

class BoxedXState(namedtuple('_BoxedXState', 'type4obj core_only mutable_only copied xst')):
    'boxed_xst'

    def seek_obj_(sf, obj, /):
        '[mutable_only==True] => sf/boxed_vst -> obj -> None'
        if not sf.type4obj is type(obj):raise TypeError(sf.type4obj, type(obj))
        #obj.__seek___(sf)
        seek_(obj, sf)
        return
    def mk_obj5boxed_wst_(sf, /):
        '[mutable_only==False] => sf/boxed_wst -> obj'
        #return sf.type4obj.__mk5boxed_wst___(sf)
        return mk5boxed_wst_(sf.type4obj, sf)

    @property
    def vst(sf, /):
        '[mutable_only==True] => sf/boxed_vst -> vst'
        if not sf.mutable_only:raise AttributeError('vst')
        return sf.xst
    @property
    def wst(sf, /):
        '[mutable_only==False] => sf/boxed_wst -> wst'
        if sf.mutable_only:raise AttributeError('wst')
        return sf.xst

    @property
    def kst(sf, /):
        '[core_only==True] => sf/boxed_kst -> kst'
        if not sf.core_only:raise AttributeError('kst')
        return sf.xst
    @property
    def rst(sf, /):
        '[core_only==False] => sf/boxed_rst -> rst'
        if sf.core_only:raise AttributeError('rst')
        return sf.xst

    @property
    def kvst(sf, /):
        '[core_only==True][mutable_only==True] => sf/boxed_kvst -> kvst'
        if not sf.core_only:raise AttributeError('kvst')
        if not sf.mutable_only:raise AttributeError('kvst')
        return sf.xst
    @property
    def rvst(sf, /):
        '[core_only==False][mutable_only==True] => sf/boxed_rvst -> rvst'
        if sf.core_only:raise AttributeError('rvst')
        if not sf.mutable_only:raise AttributeError('kvst')
        return sf.xst

    @property
    def kwst(sf, /):
        '[core_only==True][mutable_only==False] => sf/boxed_kwst -> kwst'
        if not sf.core_only:raise AttributeError('kwst')
        if sf.mutable_only:raise AttributeError('kwst')
        return sf.xst
    @property
    def rwst(sf, /):
        '[core_only==False][mutable_only==False] => sf/boxed_rwst -> rwst'
        if sf.core_only:raise AttributeError('rwst')
        if sf.mutable_only:raise AttributeError('rwst')
        return sf.xst

def mk_obj5boxed_wst_(boxed_wst, /):
    '[boxed_wst.mutable_only==False] => boxed_wst/boxed_wst -> obj # toplvl-func for pickle'
    return boxed_wst.mk_obj5boxed_wst_()
    #return boxed_wst.type4obj.__mk5boxed_wst___(boxed_wst)

class Error(Exception):pass
class Error__unmatched_immutable_core_xstate(Error):pass
#from:IBase4TellSeekState@seed.math.combination__stated
class IStated(ABC):
    r'''[[[

    [boxed_xst =[def]= BoxedXState(type4obj, core_only, mutable_only, copied, xst)]
        [boxed_wst =[def]= boxed_xst{mutable_only=False}]
        [boxed_vst =[def]= boxed_xst{mutable_only=True}]

    [xst :: xstate/either_state{core_only,mutable_only}]

    [wst :: wstate/whole_state{core_only}]
    [vst :: vstate/varable_state{core_only}]
        [wst{core_only} =[def]= xst{core_only,mutable_only=False}]
        [vst{core_only} =[def]= xst{core_only,mutable_only=True}]

    [rst :: rstate/redundant_state{mutable_only}]
    [kst :: kstate/kernel_state/core_state{mutable_only}]
        [rst{mutable_only} =[def]= xst{core_only=False,mutable_only}]
        [kst{mutable_only} =[def]= xst{core_only=True,mutable_only}]

    [xst =[def]= (may immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate)]
        [kst = xst{core_only=True} =[def]= (may immutable_core_xstate, mutable_core_xstate, None, None)]
        [rst = xst{core_only=False} =[def]= (may immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, mutable_redundant_xstate)]

        [vst = xst{mutable_only=True} =[def]= (None, mutable_core_xstate, None, may mutable_redundant_xstate)]
        [wst = xst{mutable_only=False} =[def]= (immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate)]

        [kvst = xst{core_only=True,mutable_only=True} =[def]= (None, mutable_core_xstate, None, None)]
        [kwst = xst{core_only=True,mutable_only=False} =[def]= (immutable_core_xstate, mutable_core_xstate, None, None)]

        [rvst = xst{core_only=False,mutable_only=True} =[def]= (None, mutable_core_xstate, None, mutable_redundant_xstate)]
        [rwst = xst{core_only=False,mutable_only=False} =[def]= (immutable_core_xstate, mutable_core_xstate, immutable_redundant_xstate, mutable_redundant_xstate)]

    [core_only := False]:
        to save computation time of redundant info
    [core_only := True]:
        to save storage space of redundant info
    [mutable_only := False]:
        wst
        ._make5wstate_()
        #bug:__tell___/__seek___ performed inter-instances of same type
        create new instance
            #copy
            #reduce+pickle
    [mutable_only := True]:
        vst
        ._copy5vstate_()
        __tell___/__seek___ performed on same instance
            #tell_/seek_

    #]]]'''#'''
    __slots__ = ()
    @special_method6class
    def __copy2boxed_xstate___(sf, /, *, core_only:bool, mutable_only:bool, to_copy:bool):
        '-> boxed_xst/BoxedXState'
        check_type_is(bool, core_only)
        check_type_is(bool, mutable_only)
        check_type_is(bool, to_copy)
        xst = type(sf)._copy2xstate_(sf, core_only=core_only, mutable_only=mutable_only, to_copy=True)
        boxed_xst = BoxedXState(type(sf), core_only, mutable_only, copied:=to_copy, xst)
        return boxed_xst
    @special_method6class
    @abstractmethod
    def _copy2xstate_(sf, /, *, core_only:bool, mutable_only:bool, to_copy:bool):
        '-> (vst if mutable_only else wst)/xst/(may immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate) # [to_copy=>xst@now][not to_copy=>xst@(view|original_inuse_data)]'
        #def _get_xstate_(sf, /, *, immutable_core:bool, mutable_core:bool, immutable_redundant:bool, mutable_redundant:bool):
    @special_method6class
    @abstractmethod
    def _copy5vstate_(sf, vst, /, *, core_only:bool, to_copy:bool):
        'vst/(None, mutable_core_xstate, None, may mutable_redundant_xstate) -> None # [mutable_only===True] # [not to_copy=>move vst, vst will be invalid] #see:_half_copy5wstate_'
        #def _set_xstate_(sf, xst, /, *, core_only:bool, mutable_only:bool):
        #xxx 'xst/(may immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate) -> None'
    @special_method6class
    @abstractmethod
    def _is_matched_immutable_core_xstate_(sf, immutable_core_xstate, /):
        'immutable_core_xstate -> bool #see:._half_copy5wstate_ #see:IEqTmpVal/IEqTmpVal__via_iter_sized_args_kwds'

    @special_method6class
    def _half_copy5wstate_(sf, wst, /, *, core_only:bool, to_copy:bool):
        'wst/(immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate) -> None|^Error__unmatched_immutable_core_xstate # [mutable_only===True] # [not to_copy=>move wst, wst will be invalid] #see:_copy5vstate_'
        (immutable_core_xstate, mutable_core_xstate, may_immutable_redundant_xstate, may_mutable_redundant_xstate) = wst
        if not type(sf)._is_matched_immutable_core_xstate_(sf, immutable_core_xstate): raise Error__unmatched_immutable_core_xstate
        vst = (None, mutable_core_xstate, None, may_mutable_redundant_xstate)
        type(sf)._copy5vstate_(sf, vst, core_only=core_only, to_copy=to_copy)
        return None
    @special_method6class
    @classmethod
    @abstractmethod
    def _make5wstate_(cls, wst, /, *, core_only:bool, to_copy:bool):
        'wst/(immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate) -> sf/cls # [mutable_only===False] # [not to_copy=>move wst, wst will be invalid]'
    @special_method6class
    @abstractmethod
    def _get_emay_may_may_args_may_kwds4repr_(sf, /, *, to_copy:bool):
        '-> emay may (may args, may kwds) # [... => using object.__repr__]'
        return ...
    #@special_method6class
    def __repr__(sf, /):
        em = type(sf)._get_emay_may_may_args_may_kwds4repr_(sf, to_copy=False)
        if em is ...:
            return object.__repr__(sf)
        m = em
        may_args, may_kwds = ifNone(m, (None, None))
        args = ifNone(may_args, [])
        kwds = ifNone(may_kwds, {})
        return repr_helper(sf, *args, **kwds)

    @special_method6class
    def __tell___(sf, /, *, save_time:bool):
        '-> boxed_vst'
        #xxx def __tell___(sf, /, *, save_time:bool, inter_instances:bool):
        #return type(sf)._copy2xstate_(sf, core_only=not save_time, mutable_only=not inter_instances, to_copy=True)
        check_type_is(bool, save_time)
        #boxed_vst = sf.__copy2boxed_xstate___(core_only=not save_time, mutable_only=True, to_copy=True)
        boxed_vst = copy2boxed_xstate_(sf, core_only=not save_time, mutable_only=True, to_copy=True)
        return boxed_vst
    @special_method6class
    def __seek___(sf, boxed_vst, /):
        'boxed_vst -> None'
        #xxx def __seek___(sf, xst, /, *, save_time:bool, inter_instances:bool):
        check_type_is(BoxedXState, boxed_vst)
        vst = boxed_vst.vst
        if not boxed_vst.type4obj is type(sf):raise TypeError(boxed_vst.type4obj, type(sf))
        type(sf)._copy5vstate_(sf, vst, core_only=boxed_vst.core_only, to_copy=True)
        return
    @special_method6class
    def __half_seek___(sf, boxed_wst, /):
        'boxed_wst -> None'
        check_type_is(BoxedXState, boxed_wst)
        wst = boxed_wst.wst
        if not boxed_wst.type4obj is type(sf):raise TypeError(boxed_wst.type4obj, type(sf))
        type(sf)._half_copy5wstate_(sf, wst, core_only=boxed_wst.core_only, to_copy=True)
        return
    @special_method6class
    def __save_as_boxed_wst___(sf, /, *, save_time:bool):
        '-> boxed_wst/BoxedXState{core_only=not save_time}'
        check_type_is(bool, save_time)
        #boxed_wst = sf.__copy2boxed_xstate___(core_only=not save_time, mutable_only=False, to_copy=True)
        boxed_wst = copy2boxed_xstate_(sf, core_only=not save_time, mutable_only=False, to_copy=True)
        return boxed_wst
    @special_method6class
    @classmethod
    def __mk5boxed_wst___(cls, boxed_wst, /):
        'boxed_wst/BoxedXState{core_only} -> sf/cls'
        check_type_is(BoxedXState, boxed_wst)
        wst = boxed_wst.wst
        if not boxed_wst.type4obj is cls:raise TypeError(boxed_wst.type4obj, cls)
        sf = cls._make5wstate_(wst, core_only=boxed_wst.core_only, to_copy=True)
        check_type_is(cls, sf)
        return sf
    @special_method6class
    def __reduce__(sf, /):
        #boxed_wst = sf.__save_as_boxed_wst___()
        boxed_wst = save_as_boxed_wst_(sf, save_time=False)
        return (mk_obj5boxed_wst_, (boxed_wst,))
def copy2boxed_xstate_(sf, /, *, core_only:bool, mutable_only:bool, to_copy:bool):
    'IStated -> boxed_xst/BoxedXState'
    boxed_xst = type(sf).__copy2boxed_xstate___(sf, core_only=core_only, mutable_only=mutable_only, to_copy=to_copy)
    return boxed_xst
def tell_(sf, /, *, save_time:bool):
    'IStated -> boxed_vst #see:seek_'
    boxed_vst = type(sf).__tell___(sf, save_time=save_time)
    return boxed_vst
def seek_(sf, boxed_vst, /):
    'IStated -> boxed_vst -> None # [half_seek_ vs seek_: half_seek_ will validate immutable_core_xstate]'
    type(sf).__seek___(sf, boxed_vst)
        # update sf inplace
        # half_seek_ vs seek_: half_seek_ will validate immutable_core_xstate
    return None
def save_as_boxed_wst_(sf, /, *, save_time:bool):
    'IStated -> boxed_wst/BoxedXState{core_only=not save_time} #see:half_seek_,mk5boxed_wst_,mk_obj5boxed_wst_'
    boxed_wst = type(sf).__save_as_boxed_wst___(sf, save_time=save_time)
    return boxed_wst
def mk5boxed_wst_(cls, boxed_wst, /):
    'subclass{IStated} -> boxed_wst/BoxedXState{core_only} -> sf/cls #see:mk_obj5boxed_wst_'
    #check_type_le(type, cls)
    sf = cls.__mk5boxed_wst___(boxed_wst)
    return sf
def half_seek_(sf, boxed_wst, /):
    'IStated -> boxed_wst -> None # [half_seek_ vs seek_: half_seek_ will validate immutable_core_xstate]'
    type(sf).__half_seek___(sf, boxed_wst)
        # update sf inplace
        # half_seek_ vs seek_: half_seek_ will validate immutable_core_xstate
    return None

#end-class IStated(ABC):
class IStated__eq_immutable_core_xstate_isolated(IStated):
    __slots__ = ()
    @special_method6class
    @classmethod
    @abstractmethod
    def _eq_immutable_core_xstate_isolated_(cls, lhs4immutable_core_xstate, rhs4immutable_core_xstate, /):
        'immutable_core_xstate -> immutable_core_xstate -> bool'
    @special_method6class
    @override
    def _is_matched_immutable_core_xstate_(sf, immutable_core_xstate, /):
        '[immutable_core_xstate <: IEqTmpVal] => immutable_core_xstate -> bool #see:._half_copy5wstate_ #see:IEqTmpVal/IEqTmpVal__via_iter_sized_args_kwds'
        kwst = type(sf)._copy2xstate_(sf, core_only=True, mutable_only=False, to_copy=False)
        (_immutable_core_xstate, _mutable_core_xstate, _, _) = kwst
        return type(sf)._eq_immutable_core_xstate_isolated_(_immutable_core_xstate, immutable_core_xstate)
class IStated__immutable_core_xstate_is_Eq(IStated__eq_immutable_core_xstate_isolated):
    '[override _eq_immutable_core_xstate_isolated_ := (==)]'
    __slots__ = ()
    @special_method6class
    @classmethod
    @override
    def _eq_immutable_core_xstate_isolated_(cls, lhs4immutable_core_xstate, rhs4immutable_core_xstate, /):
        'immutable_core_xstate -> immutable_core_xstate -> bool'
        return lhs4immutable_core_xstate == rhs4immutable_core_xstate
class IStated__immutable_core_xstate_is_IEqTmpVal(IStated__eq_immutable_core_xstate_isolated):
    '[override _eq_immutable_core_xstate_isolated_ := eq8tmp_val]'
    __slots__ = ()
    @special_method6class
    @classmethod
    @override
    def _eq_immutable_core_xstate_isolated_(cls, lhs4immutable_core_xstate, rhs4immutable_core_xstate, /):
        'immutable_core_xstate -> immutable_core_xstate -> bool'
        return eq8tmp_val(lhs4immutable_core_xstate, rhs4immutable_core_xstate)

class IStated__mk_dummy(IStated):
    __slots__ = ()

    #.@special_method6class
    #.@classmethod
    #.@abstractmethod
    #.def _copy_may_may_args_may_kwds4dummy_(sf, /, *, to_copy:bool):
    #.    '-> may (may args4dummy, may kwds4dummy)'
    #.@special_method6class
    #.@classmethod
    #.@abstractmethod
    #.def _mk_dummy_(cls, /, *args4dummy, **kwds4dummy):
    #.    '(*args4dummy) -> (**kwds4dummy) -> sf/cls # be used to impl _make5wstate_()'

    @special_method6class
    @classmethod
    @abstractmethod
    def _mk_dummy5immutable_part_(cls, immutable_core_xstate, may_immutable_redundant_xstate, /, *, core_only:bool):
        '-> sf7dummy/cls # be used to impl _make5wstate_()'
    @special_method6class
    @classmethod
    @override
    def _make5wstate_(cls, wst, /, *, core_only:bool, to_copy:bool):
        (immutable_core_xstate, mutable_core_xstate, may_immutable_redundant_xstate, may_mutable_redundant_xstate) = wst
        sf7dummy = cls._mk_dummy5immutable_part_(immutable_core_xstate, may_immutable_redundant_xstate, core_only=core_only)
        #seek_(sf7dummy, ...) #.__seek___()
        vst = (None, mutable_core_xstate, None, may_mutable_redundant_xstate)
        type(sf7dummy)._copy5vstate_(sf7dummy, vst, core_only=core_only, to_copy=True)
        777;    sf = sf7dummy
        return sf

def _testing_via_RadixNumerationCounter():
  if 1:
    #from seed.tiny_._Base4repr import _Base4repr
    from seed.int_tools.digits.radix_repr2uint import radix_repr2uint__big_endian
    from seed.int_tools.digits.uint2radix_repr import uint2radix_repr__big_endian
  class RadixNumerationCounter(IStated__mk_dummy, IStated__immutable_core_xstate_is_Eq):
    'radix_numeration_counter'
    ___no_slots_ok___ = True
    #@special_method6class
    def __init__(sf, radix, u=0, may_digits=None, /, *, to_copy=True):
        check_int_ge(2, radix)
        check_int_ge(0, u)
        if may_digits is None:
            digits = list(uint2radix_repr__big_endian(radix, u))
        else:
            digits = may_digits
            if to_copy:
                digits = list(digits)
        check_type_is(list, digits)

        sf._radix = radix
        sf._u = u
        sf._digits = digits

    @special_method6class
    @override
    def _copy2xstate_(sf, /, *, core_only:bool, mutable_only:bool, to_copy:bool):
        '-> (vst if mutable_only else wst)/xst/(may immutable_core_xstate, mutable_core_xstate, may immutable_redundant_xstate, may mutable_redundant_xstate) # [to_copy=>xst@now][not to_copy=>xst@(view|original_inuse_data)]'
        immutable_core_xstate = sf._radix
        mutable_core_xstate = sf._u
        immutable_redundant_xstate = None
        mutable_redundant_xstate = sf._digits

        ######################
        may_immutable_core_xstate = immutable_core_xstate
        mutable_core_xstate
        may_immutable_redundant_xstate = immutable_redundant_xstate
        may_mutable_redundant_xstate = mutable_redundant_xstate
        ######################
        if core_only:
            may_immutable_redundant_xstate = None
            may_mutable_redundant_xstate = None
        if mutable_only:
            may_immutable_core_xstate = None
            may_immutable_redundant_xstate = None
        if to_copy:
            if not may_mutable_redundant_xstate is None:
                may_mutable_redundant_xstate = mutable_redundant_xstate.copy()
        ######################
        xst = (may_immutable_core_xstate, mutable_core_xstate, may_immutable_redundant_xstate, may_mutable_redundant_xstate)
        return xst

    @special_method6class
    @override
    def _copy5vstate_(sf, vst, /, *, core_only:bool, to_copy:bool):
        'vst/(None, mutable_core_xstate, None, may mutable_redundant_xstate) -> None # [mutable_only===True] # [not to_copy=>move vst, vst will be invalid]'
        radix = sf._radix

        (_, mutable_core_xstate, _, may_mutable_redundant_xstate) = vst
        u = mutable_core_xstate
        may_digits = may_mutable_redundant_xstate
        assert core_only is (may_digits is None)
        check_int_ge(0, u)
        if may_digits is None:
            digits = list(uint2radix_repr__big_endian(radix, u))
        else:
            digits = may_digits
            if to_copy:
                digits = list(digits)
        check_type_is(list, digits)


        sf._u = u
        sf._digits = digits

    @special_method6class
    @override
    def _get_emay_may_may_args_may_kwds4repr_(sf, /, *, to_copy:bool):
        '-> emay may (may args, may kwds) # [... => using object.__repr__]'
        boxed_wst = save_as_boxed_wst_(sf, save_time=not to_copy)
        wst = boxed_wst.wst
        (immutable_core_xstate, mutable_core_xstate, may_immutable_redundant_xstate, may_mutable_redundant_xstate) = wst
        radix = immutable_core_xstate
        u = mutable_core_xstate
        may_digits = may_mutable_redundant_xstate
        args = (radix, u, may_digits)
        may_args = args
        may_kwds = None
        return (may_args, may_kwds)
    @special_method6class
    @classmethod
    @override
    def _mk_dummy5immutable_part_(cls, immutable_core_xstate, may_immutable_redundant_xstate, /, *, core_only:bool):
        '-> sf7dummy/cls # be used to impl _make5wstate_()'
        radix = immutable_core_xstate
        assert may_immutable_redundant_xstate is None
        return cls(radix)
  if 1:
    RadixNumerationCounter
  if 1:
    RadixNumerationCounter(2)
    return RadixNumerationCounter

if __name__ == "__main__":
    _testing_via_RadixNumerationCounter()

__all__
from seed.abc.IStated import IStated, IStated__mk_dummy, BoxedXState



from seed.abc.IStated import BoxedXState, mk_obj5boxed_wst_

from seed.abc.IStated import IStated, copy2boxed_xstate_, tell_, seek_, save_as_boxed_wst_, half_seek_, mk_obj5boxed_wst_, mk5boxed_wst_

from seed.abc.IStated import IStated, IStated__mk_dummy, IStated__eq_immutable_core_xstate_isolated, IStated__immutable_core_xstate_is_Eq, IStated__immutable_core_xstate_is_IEqTmpVal

from seed.abc.IStated import Error, Error__unmatched_immutable_core_xstate

from seed.abc.IStated import *
