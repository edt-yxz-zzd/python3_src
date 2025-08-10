#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func.py

seed.helper.lazy_import__func
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func:__doc__ -ht # -ff -df

[[
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7ast import mk_decorator4lazy_import__funcs_, decorator4lazy_import__funcs_

===
usage:
from seed.helper.lazy_import__func import lazy_import4func_
lazy_import4func_('seed.tiny', 'echo', __name__)
    ##if toplevel then almost eqv:
echo = lazy_import4func_('seed.tiny', 'echo')
    ##not overwrite global.echo
best:
echo = lazy_import4func_('seed.tiny', 'echo', __name__)

lazy_import4func_('seed.tiny', 'ifNone', __name__, '_ifNone_')
    ##if toplevel then almost eqv:
_ifNone_ = lazy_import4func_('seed.tiny', 'ifNone')
    ##not overwrite global._ifNone_
best:
_ifNone_ = lazy_import4func_('seed.tiny', 'ifNone', __name__, '_ifNone_')

===
usage:
from seed.helper.lazy_import__func import lazy_import4funcs_
lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)
    ##if toplevel then almost eqv:
[fst,_snd_] = lazy_import4funcs_('seed.tiny', 'fst,snd')
    ##not overwrite global.fst/_snd_
best:
[fst,_snd_] = lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)

===
usage:
from seed.helper.lazy_import__func7ast import mk_decorator4lazy_import__funcs_, decorator4lazy_import__funcs_
@decorator4lazy_import__funcs_
def __():
    from seed.tiny import fst, snd as _snd_
    ##if toplevel then eqv:
@mk_decorator4lazy_import__funcs_(__name__)
def __():
    from seed.tiny import fst, snd as _snd_


]]


######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_check_int_ge'
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge')
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_check_int_ge'
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge', __name__, '_check_int_ge')
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # yes:sf
_LazyImport4Func('seed.tiny_.check', 'check_int_ge', 'seed.helper.lazy_import__func', '_check_int_ge')
>>> this_mdl._check_int_ge(0, 1)
>>> this_mdl._check_int_ge # yes:f #doctest: +ELLIPSIS
<function check_int_ge at 0x...>
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge', __name__)
>>> this_mdl.check_int_ge # yes:sf
_LazyImport4Func('seed.tiny_.check', 'check_int_ge', 'seed.helper.lazy_import__func', '')
>>> this_mdl.check_int_ge(0, 1)
>>> this_mdl.check_int_ge # yes:f #doctest: +ELLIPSIS
<function check_int_ge at 0x...>




######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.echo # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'echo'
>>> this_mdl._echo_ # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_echo_'
>>> x = lazy_import4func_('seed.tiny', 'echo', __name__)
>>> y = lazy_import4func_('seed.tiny', 'echo', __name__, '_echo_')
>>> this_mdl.echo # yes:sf
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '')
>>> this_mdl._echo_ # yes:sf
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '_echo_')
>>> this_mdl.echo(666)
666
>>> this_mdl._echo_(999)
999
>>> this_mdl.echo # yes:f #doctest: +ELLIPSIS
<function <lambda> at 0x...>
>>> this_mdl._echo_ # yes:f #doctest: +ELLIPSIS
<function <lambda> at 0x...>
>>> x
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '')
>>> y
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '_echo_')


######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.fst # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'fst'
>>> this_mdl._snd_ # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_snd_'
>>> xs = lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)
>>> this_mdl.fst # yes:sf
_LazyImport4Func('seed.tiny', 'fst', 'seed.helper.lazy_import__func', '')
>>> this_mdl._snd_ # yes:sf
_LazyImport4Func('seed.tiny', 'snd', 'seed.helper.lazy_import__func', '_snd_')
>>> this_mdl.fst([666,999])
666
>>> this_mdl._snd_([666,999])
999
>>> this_mdl.fst # yes:f #doctest: +ELLIPSIS
<function fst at 0x...>
>>> this_mdl._snd_ # yes:f #doctest: +ELLIPSIS
<function snd at 0x...>
>>> xs
[_LazyImport4Func('seed.tiny', 'fst', 'seed.helper.lazy_import__func', ''), _LazyImport4Func('seed.tiny', 'snd', 'seed.helper.lazy_import__func', '_snd_')]

######################



py_adhoc_call   seed.helper.lazy_import__func   @f
]]]'''#'''
__all__ = r'''
lazy_import4func_
    lazy_import4funcs_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property

from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name
from seed.tiny_.check import check_callable
from seed.pkg_tools.import_object import import_object, import4qobject
#def import4qobject(may_qname4module, may_qname4obj, /):

from seed.helper.repr_input import repr_helper

#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

def _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst, /):
    if 0b0000:
        from seed.tiny import print_err
        print_err((sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst))
    f = sf if may_func8dst is None else may_func8dst
    if smay_qnm4mdl8dst:
        #inject...
        qnm4mdl8dst = smay_qnm4mdl8dst
        nm4func8dst = smay_nm4func8dst
        mdl8dst = import4qobject(qnm4mdl8dst, None)
        ########
        try:
            #x = import4qobject(mdl8dst, nm4func8dst)
            x = getattr(mdl8dst, nm4func8dst)
        except AttributeError:
            #ok
            pass
        else:
            if not x is sf:
                raise Exception('dst exist:', (mdl8dst, nm4func8dst), x)
        ########
        setattr(mdl8dst, nm4func8dst, f)
        x = getattr(mdl8dst, nm4func8dst)
        if not x is f:raise Exception('setattr fail?:', (mdl8dst, nm4func8dst), x, f)
        ########

class _LazyImport4Func:
    @cached_property
    def _func_(sf, /):
        (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst) = sf._args
        f = import4qobject(qnm4mdl8src, qnm4func8src)
        check_callable(f)
        _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst:=f)
        return f
    def __init__(sf, qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst, /):
        sf._args4repr = (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)
        check_pseudo_qual_name(qnm4mdl8src)
        check_pseudo_qual_name(qnm4func8src)
        check_smay_pseudo_qual_name(smay_qnm4mdl8dst)
        check_smay_pseudo_identifier(smay_nm4func8dst)
        if smay_nm4func8dst and not smay_qnm4mdl8dst:raise TypeError
        if smay_qnm4mdl8dst and not smay_nm4func8dst:
            check_pseudo_identifier(smay_nm4func8dst:=qnm4func8src)
        assert bool(smay_qnm4mdl8dst) is bool(smay_nm4func8dst)
        sf._args = (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)

    def __call__(sf, /, *args, **kwds):
        return sf._func_(*args, **kwds)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
def lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst='', smay_nm4func8dst='', /):
    sf = _LazyImport4Func(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)
    (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst) = sf._args
        # updated:smay_nm4func8dst
    _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst:=None)
    return sf
def lazy_import4funcs_(qnm4mdl8src, xqnms4func8src, smay_qnm4mdl8dst='', /):
    r'''[[[
    [xqnms4func8src :: (Iter xqnm4func8src) | xqnms4func8src__str]
    [xqnms4func8src__str <- regex"{xqnm4func8src}(,{xqnm4func8src})*"]
    [xqnm4func8src <- regex"{qnm4func8src}(:{nm4func8dst})?"]
    #]]]'''#'''
    if type(xqnms4func8src) is str:
        xqnms4func8src = xqnms4func8src.split(',')
    xs = []
    for xqnm4func8src in xqnms4func8src:
        qnm4func8src, _, smay_nm4func8dst = xqnm4func8src.partition(':')
        x = lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)
        xs.append(x)
    return xs

__all__
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func import *
