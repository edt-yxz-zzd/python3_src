#__all__:goto
r'''[[[
e ../../python3_src/seed/types/Symbol.py
view ../../python3_src/seed/hierarchy/symbol/PrivateSymbol.py


seed.types.Symbol
py -m nn_ns.app.debug_cmd   seed.types.Symbol -x
py -m nn_ns.app.doctest_cmd seed.types.Symbol:__doc__ -ht



symbol
    ===commom:setitem:cache<wkey,v>
    #wkey as weakref.key
    symbol[wkey::] = v
    v = symbol[wkey::]
    del symbol[wkey::]
    ===commom:setitem:cache<pkey,v>
    #pkey as permanent.key
    symbol[::pkey] = v
    v = symbol[::pkey]
    del symbol[::pkey]
    ===
    public
        ===repr:
        getP('xxx.yyy', 'aaa.bbb')
        getP('xxx.yyy:aaa.bbb')
        P.xxx.yyy().aaa.bbb
        ===mk:
        mk_public_symbol(__module__, __qualname__, __doc__, **kwds)
            eg:kw:__isabstractmethod__
        @public_symbol5cls
        class aaa:
            class bbb:
                pass
    private
        ===repr:
        smay4repr/emay_smay4str
            emay ==>> smay4repr
            old:smay ==>> {<__doc__>}
            new:smay ==>> {<smay_mdl4creator:smay_qnm4creator:__doc__>}
        ===mk:
        old:mk_private_symbol(smay4repr, emay_smay4str, __doc__, **kwds)
            eg:kw:__isabstractmethod__
        new:mk_private_symbol(smay4repr, emay_smay4str, __doc__, smay_mdl4creator, smay_qnm4creator, **kwds)





>>> import builtins
>>> import seed.types.Symbol

#old-version
>>> _P
P
>>> _P()
P()
>>> _P.a()
P.a()
>>> _P.a.b()
P.a.b()
>>> _P.a.b().c
P.a.b().c
>>> _P.a.b().c.d
P.a.b().c.d
>>> _P.seed.types.Symbol().P
P.seed.types.Symbol().P
>>> _P()() is builtins
True
>>> _P()() is __builtins__
False
>>> _P().id() is id
True
>>> _P.seed.types.Symbol().P() is P
True
>>> _P.seed.types.Symbol().ISymbol() is ISymbol
True
>>> _P.seed.types.Symbol().ISymbol.private_vs_public() is ISymbol.private_vs_public
True




#new-version
>>> P
P
>>> P.a
P.a
>>> P.a.b
P.a.b


>>> P() is builtins
True
>>> P() is __builtins__
False
>>> P().id is id
True
>>> P.seed.types.Symbol
P.seed.types.Symbol
>>> P.seed.types.Symbol() is seed.types.Symbol
True
>>> P.seed.types.Symbol().ISymbol is ISymbol
True
>>> P.seed.types.Symbol().ISymbol.private_vs_public is ISymbol.private_vs_public
True




>>> @public_symbol5cls
... class _aaa:
...     class bbb:
...         @private_symbol5cls
...         class AAA:
...             pass
...     class ccc:
...         @private_symbol5cls
...         class BBB:
...             'ooooooxxxxxx'
...             @public_symbol5cls
...             class uuu:
...                 pass
...             t = 666
...             I = int
...     class ddd:
...         class eee:
...             class vvv:
...                 pass
...     def fff():pass
...     k = 999
>>> _aaa
P.seed.types.Symbol()._aaa
>>> P.seed.types.Symbol()._aaa is _aaa
Traceback (most recent call last):
    ...
AttributeError: module 'seed.types.Symbol' has no attribute '_aaa'
>>> print(_aaa)
[<PublicSymbol('seed.types.Symbol', '_aaa', '', bbb = P.seed.types.Symbol()._aaa.bbb, ccc = P.seed.types.Symbol()._aaa.ccc, ddd = P.seed.types.Symbol()._aaa.ddd, fff = P.seed.types.Symbol()._aaa.fff, k = 999)>]
>>> _aaa.ccc.BBB
[<seed.types.Symbol:_aaa.ccc.BBB:'ooooooxxxxxx'>]

old:[<'ooooooxxxxxx'>]

>>> print(_aaa.ccc.BBB)
[<PrivateSymbol('', '', 'ooooooxxxxxx', 'seed.types.Symbol', '_aaa.ccc.BBB', I = <class 'int'>, t = 666, uuu = P.seed.types.Symbol()._aaa.ccc.BBB.uuu)>]

old:[<PrivateSymbol('', '', 'ooooooxxxxxx', I = <class 'int'>, t = 666, uuu = P.seed.types.Symbol()._aaa.ccc.BBB.uuu)>]

>>> _aaa.bbb
P.seed.types.Symbol()._aaa.bbb
>>> print(_aaa.bbb)
[<PublicSymbol('seed.types.Symbol', '_aaa.bbb', '', AAA = [<'seed.types.Symbol:_aaa.bbb.AAA'>])>]
>>> _aaa.bbb.AAA
[<'seed.types.Symbol:_aaa.bbb.AAA'>]
>>> print(_aaa.bbb.AAA)
[<PrivateSymbol("[<'seed.types.Symbol:_aaa.bbb.AAA'>]", '', '', '', '')>]

old:[<PrivateSymbol('', '', 'seed.types.Symbol:_aaa.bbb.AAA')>]


>>> del _aaa



#]]]'''
__all__ = r'''
ISymbol
    apply_key_
    explain_key_
    check_wkey
ISymbol
    ISymbol__mixins
    PublicSymbol
        mk_public_symbol
        public_symbol5cls
        P
        getP
    PrivateSymbol
        mk_private_symbol
        private_symbol5cls



NamedWeakKey

'''.split()#'''
#move out:
    #ReDefRepr
    #DottedAttrCollector
__all__

from seed.tiny_.check import check_type_is
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById, le_AddrAsHash # BaseAddrAsHash
from seed.helper.repr_input import repr_helper
from seed.tiny import MapView
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name
from seed.pkg_tools.import_object import import4qobject
from seed.types.DottedAttrCollector import DottedAttrCollector, ReDefRepr

from weakref import WeakKeyDictionary

class __:
    def fff():pass
__.__module__
__.__qualname__
__.__doc__

__.fff.__module__
__.fff.__qualname__
__.fff.__doc__


class ISymbol(EqById):
    __slots__ = ()
    @property
    @abstractmethod
    def private_vs_public(sf, /):
        '-> bool'
    @abstractmethod
    def __repr__(sf, /):
        '-> str'
    @abstractmethod
    def __str__(sf, /):
        '-> str'


    @abstractmethod
    def _set5wkey_(sf, wkey, hhh, /):
        '-> wkey -> hhh -> None'
    @abstractmethod
    def _set5pkey_(sf, pkey, vvv, /):
        '-> pkey -> vvv -> None'

    @abstractmethod
    def _get5wkey_(sf, wkey, /):
        '-> wkey -> hhh'
    @abstractmethod
    def _get5pkey_(sf, pkey, /):
        '-> pkey -> vvv'

    @abstractmethod
    def _del5wkey_(sf, wkey, /):
        '-> wkey -> None'
    @abstractmethod
    def _del5pkey_(sf, pkey, /):
        '-> pkey -> None'

    @abstractmethod
    def __getattr__(sf, nm, /):
        '-> nm -> mmm'

    def __detattr__(sf, nm, /):
        raise AttributeError(nm)
    def __setattr__(sf, nm, _, /):
        raise AttributeError(nm)
    def __delitem__(sf, wkey_nn_or_nn_pkey, /):
        '-> wkey_nn_or_nn_pkey -> None'
        return apply_key_(sf._del5wkey_, sf._del5pkey_, wkey_nn_or_nn_pkey)
    def __getitem__(sf, wkey_nn_or_nn_pkey, /):
        '-> wkey_nn_or_nn_pkey -> hhh/vvv'
        return apply_key_(sf._get5wkey_, sf._get5pkey_, wkey_nn_or_nn_pkey)
    def __setitem__(sf, wkey_nn_or_nn_pkey, hhh_or_vvv, /):
        '-> wkey_nn_or_nn_pkey -> hhh/vvv -> None'
        return apply_key_(sf._set5wkey_, sf._set5pkey_, wkey_nn_or_nn_pkey, hhh_or_vvv)
def apply_key_(f4wkey, f4pkey, wkey_nn_or_nn_pkey, /, *args):
    (wkey_vs_pkey, wkey_or_pkey) = explain_key_(wkey_nn_or_nn_pkey)
    f = f4wkey if not wkey_vs_pkey else f4pkey
    return f(wkey_or_pkey, *args)
def explain_key_(wkey_nn_or_nn_pkey, /):
    '-> (wkey_vs_pkey, wkey_or_pkey)'
    check_type_is(slice, sl:=wkey_nn_or_nn_pkey)
    if not sl.stop is None:raise TypeError(f'SHOULD-BE: symbol[wkey::] or symbol[::pkey] : {sl}')
    if sl.start is None:
        # [::pkey]
        pkey = sl.step
        return (True, pkey)
    else:
        if not sl.step is None:raise TypeError(f'SHOULD-BE: symbol[wkey::] or symbol[::pkey] : {sl}')
        wkey = sl.start
        check_wkey(wkey)
        return (False, wkey)

def check_wkey(wkey, /):
    if not le_AddrAsHash(cls:=type(wkey)): raise TypeError
#end-class ISymbol(EqById):

class ISymbol__mixins(ISymbol):
    #__slots__ = ()
    #__slots__ = ('__weakref__', '__dict__')
    #___no_slots_ok___ = True
    __slots__ = ('__weakref__', '_a', '_p', '_w')
        #_a: attrs: {nm:mmm}
        #_p: permanent: {pkey:vvv}
        #_w: weakref: {wkey:hhh}
    def __init__(sf, /, **kwds):
        _init_a(sf, kwds)

    @override
    def _set5wkey_(sf, wkey, hhh, /):
        '-> wkey -> hhh -> None'
        _set('_init_w', _wg, sf, wkey, hhh)
    @override
    def _set5pkey_(sf, pkey, vvv, /):
        '-> pkey -> vvv -> None'
        _set('_init_p', _pg, sf, pkey, vvv)

    @override
    def _get5wkey_(sf, wkey, /):
        '-> wkey -> hhh'
        return _get(_wg, sf, wkey)
    @override
    def _get5pkey_(sf, pkey, /):
        '-> pkey -> vvv'
        return _get(_pg, sf, pkey)

    @override
    def _del5wkey_(sf, wkey, /):
        '-> wkey -> None'
        _del(_wg, sf, wkey)
    @override
    def _del5pkey_(sf, pkey, /):
        '-> pkey -> None'
        _del(_pg, sf, pkey)

    @override
    def __getattr__(sf, nm, /):
        '-> nm -> mmm'
        try:
            return _ag(sf)[nm]
        except KeyError:
            raise AttributeError(nm)
if 1:
    __ = ISymbol__mixins
    _sym_a = __._a
    del __._a
    _sym_p = __._p
    del __._p
    _sym_w = __._w
    del __._w
    ######################
    _ag = _sym_a.__get__
    _pg = _sym_p.__get__
    _wg = _sym_w.__get__
    ######################
    _as = _sym_a.__set__
    _ps = _sym_p.__set__
    _ws = _sym_w.__set__
    ######################
    def _init_x_(set_, get, sf, d, /):
        try:
            get(sf)
        except AttributeError:
            pass
        else:
            raise AttributeError('had been initialized')
        set_(sf, d)
        get(sf)
    def _init_a(sf, d, /):
        check_type_is(dict, d)
        _init_x_(_as, _ag, sf, MapView(d))
    def _init_p(sf, /):
        _init_x_(_ps, _pg, sf, {})
    def _init_w(sf, /):
        _init_x_(_ws, _wg, sf, WeakKeyDictionary())

def _g_(get, sf, k, /):
    try:
        return get(sf)
    except AttributeError:
        raise KeyError(k)
def _del(get, sf, k, /):
    del _g_(get, sf, k)[k]
        # ^KeyError
def _get(get, sf, k, /):
    return _g_(get, sf, k)[k]
        # ^KeyError
def _set(nm4init, get, sf, k, v, /):
    try:
        d = get(sf)
            # ^AttributeError
    except AttributeError:
        globals()[nm4init](sf)
        d = get(sf)
    d[k] = v

#end-class ISymbol__mixins(ISymbol):


class NamedWeakKey(EqById, str):
    __slots__ = '__weakref__'
    def __bool__(sf, /):
        return True
    def __len__(sf, /):
        raise AttributeError
    def __repr__(sf, /):
        return str(sf)
_wkey4attrs = NamedWeakKey('_wkey4private_attrs')
assert repr(_wkey4attrs) == '_wkey4private_attrs', repr(_wkey4attrs)
assert NamedWeakKey('')
assert not NamedWeakKey('') == NamedWeakKey('')
assert NamedWeakKey('') != NamedWeakKey('')

def _mk_private_attrs4PublicSymbol(__module__, __qualname__, __doc__, /):
    return MapView(dict(locals()))

class PublicSymbol(ISymbol__mixins):
    __slots__ = ()
    private_vs_public = True
    #def __init__(sf, /, __module__, __qualname__, __doc__, **kwds):
        #super().__init__(__module__=__module__, __qualname__=__qualname__, __doc__=__doc__, **kwds)
    def __init__(sf, __module__, __qualname__, __doc__, /, **kwds):
        check_smay_pseudo_qual_name(__module__)
        check_pseudo_qual_name(__qualname__)
        check_type_is(str, __doc__)
        ######################
        _init_a(sf, kwds)
        sf[_wkey4attrs:] = _mk_private_attrs4PublicSymbol(__module__, __qualname__, __doc__)
        ######################
    @override
    def __repr__(sf, /):
        '-> str'
        #brief
        d = sf[_wkey4attrs:]
        mdl = d['__module__']
        qnm = d['__qualname__']
        #new-version:
        if not mdl:
            return f'P().{qnm!s}'
        return f'P.{mdl!s}().{qnm!s}'
        #old-version:
        if not mdl:
            return f'P().{qnm!s}()'
        return f'P.{mdl!s}().{qnm!s}()'
    @override
    def __str__(sf, /):
        '-> str'
        #verbose
        d = sf[_wkey4attrs:]
        mdl = d['__module__']
        qnm = d['__qualname__']
        doc = d['__doc__']
        kwds = _ag(sf)
        s = repr_helper(sf, mdl, qnm, doc, **kwds)
        return f'[<{s!s}>]'
#end-class PublicSymbol(ISymbol__mixins):
def mk_public_symbol(__module__, __qualname__, __doc__, /, **kwds):
    'eg:kw:__isabstractmethod__'
    try:
        getP(__module__, __qualname__)
    except AttributeError:
        #except ImportError:true-exc!!!
        pass
    else:
        raise AttributeError(f'existed: "{__module__}:{__qualname__}"')
    return PublicSymbol(__module__, __qualname__, __doc__, **kwds)
def public_symbol5cls(Type, /):
    if not isinstance(Type, type): raise TypeError
    return _echo_or_public_symbol5xxx(Type)
    #usage:
    @public_symbol5cls
    class aaa:
        class bbb:
            pass





def __repr4PP(P_nms, /):
    return repr(P_nms) + '()'
def __call4P(P_nms, /):
    return DottedAttrCollector(__call4PP, ReDefRepr(__repr4PP, P_nms), (), None)
def __call4PP(PP_nms, /):
    [f, obj, lnkls8nms, may_repr4obj] = PP_nms
    PP = obj #PP_nms.obj
    [P_nms] = PP.args4func
    snm4mdl = type(P_nms).__mk_qname4attr__(P_nms)
    snm4qnm = type(PP_nms).__mk_qname4attr__(PP_nms)
    return getP(snm4mdl, snm4qnm)
_P = DottedAttrCollector(__call4P, NamedWeakKey('P'), (), None)
    #old version: P.a.b().c.d()
    #--> new version: P.a.b()

def __call4P__new_version(P_nms, /):
    snm4mdl = type(P_nms).__mk_qname4attr__(P_nms)
    return import4qobject(__module__:=snm4mdl, __qualname__:='')
P = DottedAttrCollector(__call4P__new_version, NamedWeakKey('P'), (), None)
    # new version: P.a.b()

def getP(__module__='', __qualname__=None, /):
    check_type_is(str, __module__)
    if __qualname__ is None:
        if not 1 == __module__.count(':'): raise ValueError
        __module__, __qualname__ = __module__.split(':')
    check_smay_pseudo_qual_name(__module__)
    check_smay_pseudo_qual_name(__qualname__)
    if 0:check_pseudo_qual_name(__qualname__)
    #return import4qobject(snm4mdl, snm4obj)
    #xxx:check_wkey()
    return import4qobject(__module__, __qualname__)






def _mk_private_attrs4PrivateSymbol(smay4repr, emay_smay4str, __doc__, smay_mdl4creator, smay_qnm4creator, /):
    return MapView(dict(locals()))


class PrivateSymbol(ISymbol__mixins):
    __slots__ = ()
    private_vs_public = False
    def __init__(sf, smay4repr, emay_smay4str, __doc__, smay_mdl4creator, smay_qnm4creator, /, **kwds):
        check_type_is(str, smay4repr)
        if not emay_smay4str is ...:
            check_type_is(str, emay_smay4str)
        check_type_is(str, __doc__)
        check_smay_pseudo_qual_name(smay_mdl4creator)
        check_smay_pseudo_qual_name(smay_qnm4creator)
        ######################
        _init_a(sf, kwds)
        sf[_wkey4attrs:] = _mk_private_attrs4PrivateSymbol(smay4repr, emay_smay4str, __doc__, smay_mdl4creator, smay_qnm4creator)
        ######################
    @override
    def __repr__(sf, /):
        '-> str'
        #brief
        d = sf[_wkey4attrs:]
        s = d['smay4repr']
        if s:
            return s
        doc = d['__doc__']
        mdl4cr = d['smay_mdl4creator']
        qnm4cr = d['smay_qnm4creator']
        return f'[<{mdl4cr!s}:{qnm4cr!s}:{doc!r}>]'
        #old:
        return f'[<{doc!r}>]'
    @override
    def __str__(sf, /):
        '-> str'
        #verbose
        d = sf[_wkey4attrs:]
        em = d['emay_smay4str']
        if em is ...:
            return repr(sf)
        s = em
        if s:
            return s
        r = d['smay4repr']
        doc = d['__doc__']
        mdl4cr = d['smay_mdl4creator']
        qnm4cr = d['smay_qnm4creator']
        kwds = _ag(sf)
        s = repr_helper(sf, r, s, doc, mdl4cr, qnm4cr, **kwds)
        return f'[<{s!s}>]'
        return f'[<{doc!r}>]'



def mk_private_symbol(smay4repr, emay_smay4str, __doc__, smay_mdl4creator, smay_qnm4creator, /, **kwds):
    'eg:kw:__isabstractmethod__'
    return PrivateSymbol(smay4repr, emay_smay4str, __doc__, smay_mdl4creator, smay_qnm4creator, **kwds)
def private_symbol5cls(Type, /):
    if not isinstance(Type, type): raise TypeError
    return _echo_or_private_symbol5xxx(Type)
    #usage:
    @private_symbol5cls
    class aaa:
        class bbb:
            pass
def __():pass
_types4mk_symbol = (type, type(__))
_excluded_attrs4type = '__dict__ __doc__ __module__ __weakref__'.split()
def _echo_or_symbol5xxx(_mk_symbol, xxx, snm4mdl='', qnm4parent='', /):
    if not isinstance(xxx, _types4mk_symbol):
        # e.g. symbol
        return xxx
    qnm4mdl = xxx.__module__
    qnm = xxx.__qualname__
    nm = xxx.__name__
    doc = xxx.__doc__
    if snm4mdl and not (qnm4mdl==snm4mdl and qnm == f'{qnm4parent}.{nm}'):
        #not defined inside parent
        return xxx
    if doc is None:
        doc = ''
    if isinstance(xxx, type):
        # recur@type
        kwds = {nm:_echo_or_symbol5xxx(_mk_symbol, yyy, qnm4mdl, qnm) for nm, yyy in xxx.__dict__.items() if nm not in _excluded_attrs4type}
    else:
        # stop@func
        kwds = {}
    return _mk_symbol(__module__:=qnm4mdl, __qualname__:=qnm, __doc__:=doc, **kwds)
    return mk_public_symbol(__module__:=qnm4mdl, __qualname__:=qnm, __doc__:=doc, **kwds)
    return mk_private_symbol(smay4repr:='', emay_smay4str:='', __doc__:=doc, smay_mdl4creator:=qnm4mdl, smay_qnm4creator:=qnm, **kwds)

def __mk_symbol4private(__module__, __qualname__, __doc__, /, **kwds):
    if not __doc__:
        r = f"[<'{__module__}:{__qualname__}'>]"
        return mk_private_symbol(smay4repr:=r, emay_smay4str:='', __doc__:='', smay_mdl4creator:='', smay_qnm4creator:='', **kwds)
    return mk_private_symbol(smay4repr:='', emay_smay4str:='', __doc__, smay_mdl4creator:=__module__, smay_qnm4creator:=__qualname__, **kwds)
    #old:
    if not __doc__:
        __doc__ = f'{__module__}:{__qualname__}'
    return mk_private_symbol(smay4repr:='', emay_smay4str:='', __doc__, **kwds)
def _echo_or_private_symbol5xxx(xxx, /):
    return _echo_or_symbol5xxx(_mk_symbol:=__mk_symbol4private, xxx)
def _echo_or_public_symbol5xxx(xxx, /):
    return _echo_or_symbol5xxx(_mk_symbol:=mk_public_symbol, xxx)
_echo_or_private_symbol5xxx
_echo_or_public_symbol5xxx



def __():
    # ^TypeError: '__.<locals>.aaa.bbb'
    #   check_pseudo_qual_name
    @public_symbol5cls
    class aaa:
        class bbb:
            pass
#__()


def __():
    # ^TypeError: '__.<locals>.aaa.bbb'
    #   check_pseudo_qual_name
    @private_symbol5cls
    class aaa:
        class bbb:
            pass
#__()

class __:
    @public_symbol5cls
    class aaa:
        class bbb:
            pass
class __:
    @private_symbol5cls
    class aaa:
        class bbb:
            pass

if __name__ == "__main__":
    ...
__all__
from seed.types.Symbol import ISymbol, ISymbol__mixins
from seed.types.Symbol import apply_key_, explain_key_, check_wkey
from seed.types.Symbol import PublicSymbol, mk_public_symbol, public_symbol5cls, P, getP
from seed.types.Symbol import PrivateSymbol, mk_private_symbol, private_symbol5cls
from seed.types.Symbol import *
