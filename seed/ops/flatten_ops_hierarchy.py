
r'''[[[[[
e ../../python3_src/seed/ops/flatten_ops_hierarchy.py
py -m seed.ops.flatten_ops_hierarchy


external attachment type system env
    generic-type-parameter, converter:
        Map<K, V, PK, key_transform::K->PK>
            key_transform = echo | AddrAsHashWrapper | ...
            #see:ImmutableDictItem.__doc__
            key4init_overwrite_old_item
                key4new_key
            key4query_pop_overwrite_old_value
                key4old_key

obj = Obj ops obj_state
    allow external attachment property/lazy/dependent-cached~~auto-discard[public_symbol+private_symbol]...
    xobj_state
        = immutable-or-view?obj_state
        | mutable?shadow_obj_state #contains obj_state
        | mutable-or-immutable?pure_virtual_obj_state #contains no obj_state

ops = Ops interpreter ops_state
    allow external attachment descriptor...
    ops_state may be obj again
        or ops may be obj again?
            ops_obj_union = OO_Union interpreter4ops ops4obj ops_obj_union_state
                howto mk_Ops? mk-new-ops from old-base-opss? final-ops/descriptor/descriptor-constraints...
                    via mk_Obj+OO_Union
        or obj may be ops again?
            obj = Obj ops{.interpreter4obj_state_as_ops} obj_state
obj_or_ops = Bind handler state
    #MUST in derived_most-cls-dict not via mro!!!
    get_dict4cls(type(handler))[symbol4get_ops__whole_bind_as_obj](handler)
    get_dict4cls(type(handler))[symbol4get_interpreter__whole_bind_as_ops](handler)
        see:mk_body4type4ops #prepare

sgii_protocol = static_global_interpreter_interpreter{mk_Obj, mk_Ops, mk_interpreter, ...}
    unbox_Obj, unbox_Ops are private
    mk_Obj mk-py-type also, to support __hash__/..., see DisabledClassAttr/DisabledAllDefaultClassAttr
        mk_Ops => bind Obj-py-type to each ops via redirect attr in mro.__dict__ or delete/overwrite by DisabledClassAttr


method requires addr/may_addr/neednot_addr + decomposed

interpreter is weakable FrozenDict<public_symbol>
    interpreter is immutable as whole
    set(interpreter.keys()) is defined by sgii_protocol
        get_descriptor4ops
    all method in 3 form:
        * decomposed-form-pre_init-inter_modify
        interpreter[public_symbol](interpreter, ops_state, /, *args, **kwargs)
        ###
        interpreter[get_descriptor4ops](interpreter, ops_state, public_symbol, /)
            get-data@ops #class attr
                method-static(*args, **kwargs)
            get-method:
                method-obj(ops, xobj_state, /, *args, **kwargs)
                    #not only obj_state
                    property-getter
                method-ops(ops, /, *args, **kwargs)
                #################################
                method-interpreter(interpreter, /, *args, **kwargs)
                method-ops_info(public_symbol2ops_data, extracter2ops_info, /, *args, **kwargs)
                method-obj_info(public_symbol2ops_data, extracter2ops_info, public_symbol2obj_data, extracter2obj_info, /, *args, **kwargs)
                    may redirect as kwargs
        * addr-form-post_init-inter_modify
            decomposed-info+addr
            method-addr(id(ops), ...info..., , /, ...)
        * external-form-post_init-inter_modify
            method-external(ops, /, ...)
        * interpreter-form-constructor/Singleton-pattern/...
            method-interpreter(interpreter, /, ...)
        * static-form
            method-static(/, ...)
        public_symbol.__class__.__dict__[method-form-descriptor:private_symbol]
            input: requires which info or shadow_obj_state for update in wild-form/violate-constraints
            output: eg: method-update(...)-> (result, delta)
        * protocol-form
            interpreter[public_symbol] -> name2protocol
            name2protocol :: {public_symbol-protocol_name:registered-protocol}
            protocol :: {public_symbol-interpreter.key:descriptor-for-data/method-form}
            external-register-protocol:
                    public_symbol-protocol_name -> set<public_symbol-impl_protocol_name>
                public_symbol-impl_protocol_name -> registered-protocol
                dependences:
                    public_symbol-protocol_name -> set<public_symbol-protocol_name>
                    public_symbol-impl_protocol_name -> set<public_symbol-protocol_name>
    hidden-attr: cache for init-checked


symbol = public_symbol | private_symbol
    private_symbol not Reprable, show addr and description
        __new__(description)
        __repr__ ->

    public_symbol <: Reprable
        #input4mk_and_register & properties
        #mk_and_register_public_symbol(...)
        module_qname4original, entity_object_attrs4original, virtual_concept_type_qname, virtual_concept_qname, *args, **kwargs
            source-original-description
            identity
            lookup_public_symbol(module_qname4original, entity_object_attrs4original, virtual_concept_type_qname, virtual_concept_qname, *args, **kwargs) -> public_symbol
        module_qname4storage, entity_object_attrs4storage, symbol_object_attrs
            storage-path
            identity
            __repr__ -> f'get_public_symbol(module_qname4storage, entity_object_attrs4storage, symbol_object_attrs)'
        symbols4intent :: frozenset<public_symbol | private_symbol>
            kind/intent/purpose
                at where be used


ops
    ops is immutable as whole



>>> class T(tuple):
...     __slots__ = ('__weakref__',)
Traceback (most recent call last):
    ...
TypeError: nonempty __slots__ not supported for subtype of 'tuple'

>>> class D(dict):
...     __slots__ = ('__weakref__',)

>>> type(D.__dict__) is MappingProxyType
True
>>> type(type.__getattribute__(D, '__dict__')) is MappingProxyType
True
>>> type(object.__getattribute__(D, '__dict__')) is MappingProxyType
True

>>> type.__mro__
(<class 'type'>, <class 'object'>)

>>> D.__dict__ = {}
Traceback (most recent call last):
    ...
AttributeError: attribute '__dict__' of 'type' objects is not writable
>>> type.__setattr__(D, '__dict__', {})
Traceback (most recent call last):
    ...
AttributeError: attribute '__dict__' of 'type' objects is not writable
>>> object.__setattr__(D, '__dict__', {})
Traceback (most recent call last):
    ...
TypeError: can't apply this __setattr__ to type object







>>> weakref.ref(XFrozenDict())() is empty_XFrozenDict is XFrozenDict()
True

>>> XFrozenDict().__dict__
Traceback (most recent call last):
    ...
AttributeError: 'XFrozenDict' object has no attribute '__dict__'


>>> XFrozenDict() == {}
False
>>> XFrozenDict() == XFrozenDict()
True
>>> hash(XFrozenDict()) == 3^hash(XFrozenDict)
True
>>> hash(XFrozenDict({1:3})) == hash(XFrozenDict({1:2}))
False
>>> (XFrozenDict({1:3})) == (XFrozenDict({1:2}))
False
>>> (XFrozenDict({1:3})) == (XFrozenDict({1:3}))
True



>>> s = frozenset({1})
>>> s[1]
Traceback (most recent call last):
    ...
TypeError: 'frozenset' object is not subscriptable



>>> d = XFrozenDict([])
>>> d is empty_XFrozenDict
True
>>> d = XFrozenDict()
>>> d is empty_XFrozenDict
True
>>> d
XFrozenDict()
>>> d is XFrozenDict(d)
True
>>> len(d)
0
>>> bool(d)
False
>>> it = iter(d)
>>> iter(it) is it is not d
True
>>> [*it]
[]

>>> d = XFrozenDict({1:2,3:4}, a=6)
>>> d is XFrozenDict(d)
True
>>> d
XFrozenDict({'a': 6, 1: 2, 3: 4})
>>> len(d)
3
>>> bool(d)
True
>>> it = iter(d)
>>> iter(it) is it is not d
True
>>> {*it} == {'a', 1, 3}
True


>>> d[1]
2
>>> 3 in d
True
>>> 9 in d
False
>>> d[7]
Traceback (most recent call last):
    ...
KeyError: 7




class.__instancecheck__(self, instance)
    Return true if instance should be considered a (direct or indirect) instance of class. If defined, called to implement isinstance(instance, class).

class.__subclasscheck__(self, subclass)
    Return true if subclass should be considered a (direct or indirect) subclass of class. If defined, called to implement issubclass(subclass, class).

#__subclasscheck__/__subclasshook__ cannot affect superclass-frozenset 4 XFrozenDict
#__subclasscheck__/__subclasshook__: fail
>>> issubclass(XFrozenDict, frozenset)
True
>>> isinstance(XFrozenDict(), frozenset)
True


>>> frozenset in XFrozenDict.__mro__
False
>>> XFrozenDict.__mro__ == (XFrozenDict, *XFrozenDict.__bases__[:-2], *Mapping.__mro__)
True


>>> XFrozenDict.__bases__ == (MappingMixin4check_key4set, MappingMixin4get_item, MappingMixin4singleton_immutable_empty_dict, MappingMixin4hash, MappingMixin4shallow_stable_repr, Mapping, frozenset)
True
>>> XFrozenDict.__base__ is frozenset
True

#class XFrozenDict(MappingMixin4check_key4set, MappingMixin4get_item, MappingMixin4singleton_immutable_empty_dict, MappingMixin4hash, MappingMixin4shallow_stable_repr, Mapping, frozenset, metaclass=Meta4XFrozenDict):
>>> type.__getattribute__(XFrozenDict, '__mro__') is get_mro4cls(XFrozenDict)
True
>>> type.__getattribute__(XFrozenDict, '__mro__') == (XFrozenDict, *XFrozenDict.__bases__[:-2], *Mapping.__mro__[:-1], frozenset, object)
True


>>> hasattr(frozenset(), 'union')
True
>>> hasattr(XFrozenDict(), 'union')
False
>>> hasattr(frozenset(), '__or__')
True
>>> hasattr(XFrozenDict(), '__or__')
False
>>> hasattr(frozenset(), 'update')
False
>>> hasattr(XFrozenDict(), 'update')
False


>>> hasattr(frozenset, 'union')
True
>>> hasattr(XFrozenDict, 'union')
False
>>> hasattr(frozenset, '__or__')
True
>>> hasattr(XFrozenDict, '__or__')
False
>>> hasattr(frozenset, 'update')
False
>>> hasattr(XFrozenDict, 'update')
False



#]]]]]'''

from types import MappingProxyType
import weakref
from collections.abc import Mapping, Set
from seed.abc.abc__ver1 import ABCMeta, abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import slice2triple

import seed
import operator
import types
import inspect

if 0:
    class Mapping(Mapping, ABC):
        __slots__ = ()

_descriptor4get_dict = inspect.getattr_static(object, '__dict__')
#_descriptor4get_dict = inspect.getattr_static(type('X', (), {})(), '__dict__')

def get_mro4cls(cls, /):
    r'''
#see:get_mro4cls()
>>> class X:pass
>>> x = X()
>>> x.__mro__ = 1
>>> type.__getattribute__(x, '__mro__')
Traceback (most recent call last):
    ...
TypeError: descriptor '__getattribute__' requires a 'type' object but received a 'X'
>>> object.__getattribute__(x, '__mro__')
1
>>> object.__getattribute__(X, '__mro__') is type.__getattribute__(X, '__mro__')
True

>>> get_mro4cls(X) == (X, object)
True

    #'''
    return type.__getattribute__(cls, '__mro__')
def get_base4cls(cls, /):
    r'''
#see:get_base4cls()
>>> class X:pass
>>> x = X()
>>> x.__base__ = 1
>>> type.__getattribute__(x, '__base__')
Traceback (most recent call last):
    ...
TypeError: descriptor '__getattribute__' requires a 'type' object but received a 'X'
>>> object.__getattribute__(x, '__base__')
1
>>> object.__getattribute__(X, '__base__') is type.__getattribute__(X, '__base__')
True

>>> get_base4cls(X) is object
True

>>> class Y(tuple, X):pass
>>> get_base4cls(Y) is tuple
True
>>> object.__new__(Y)
Traceback (most recent call last):
    ...
TypeError: object.__new__(Y) is not safe, use Y.__new__()
>>> type(tuple.__new__(Y)) is Y
True
>>> get_base4cls(tuple) is object
True
>>> object.__new__(tuple)
Traceback (most recent call last):
    ...
TypeError: object.__new__(tuple) is not safe, use tuple.__new__()


>>> y = Y()
>>> weakref.ref(y)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'Y' object
>>> object.__getattribute__(y, '__dict__')
{}

>>> class Z:
...     __slots__ = 'a'
>>> Z_a = Z.a
>>> del Z.a
>>> class W(Z):
...     __slots__ = 'a'
>>> W_a = W.a
>>> del W.a
>>> get_base4cls(Z) is object
True
>>> get_base4cls(W) is Z
True
>>> type(get_base4cls(W).__new__(W)) is W
True
>>> type(get_base4cls(Z).__new__(Z)) is Z
True
>>> type(object.__new__(W)) is W
True
>>> type(object.__new__(Z)) is Z
True

    #'''
    return type.__getattribute__(cls, '__base__')



def get_bases4cls(cls, /):
    r'''
#see:get_bases4cls()
>>> class X:pass
>>> x = X()
>>> x.__bases__ = 1
>>> type.__getattribute__(x, '__bases__')
Traceback (most recent call last):
    ...
TypeError: descriptor '__getattribute__' requires a 'type' object but received a 'X'
>>> object.__getattribute__(x, '__bases__')
1
>>> object.__getattribute__(X, '__bases__') is type.__getattribute__(X, '__bases__')
True

>>> get_bases4cls(X) == (object,)
True

    #'''
    return type.__getattribute__(cls, '__bases__')


def get_type(obj, /):
    return type(obj)
    return object.__getattribute__(obj, '__class__')
#def get_type_of_class(obj, /):
    #return type.__getattribute__(cls, '__class__')
def get_dict4cls(cls, /):
    return type.__getattribute__(cls, '__dict__')
def get_dict4obj(obj, /):
    return object.__getattribute__(obj, '__dict__')

def iter_dicts(obj, /):
    '-> Iter Mapping'
    try:
        mro = get_mro4cls(obj) #obj is cls?
    except TypeError:
        try:
            d = get_dict4obj(obj)
        except AttributeError:
            pass
        else:
            yield d #obj.__dict__
    else:
        yield from map(get_dict4cls, mro)

def get_dict(obj, /):
    r'''
#see:get_dict(), get_dict4cls(), get_dict4obj(), iter_dicts()
>>> class X:pass
>>> x = X()
>>> type.__getattribute__(x, '__dict__')
Traceback (most recent call last):
    ...
TypeError: descriptor '__getattribute__' requires a 'type' object but received a 'X'
>>> object.__getattribute__(x, '__dict__')
{}
>>> object.__getattribute__(X, '__dict__') is type.__getattribute__(X, '__dict__')
False
>>> object.__getattribute__(X, '__dict__') == type.__getattribute__(X, '__dict__')
True
>>> type(object.__getattribute__(X, '__dict__')) is MappingProxyType is type(type.__getattribute__(X, '__dict__'))
True


>>> class C:
...     __dict__ = 1
>>> c = C()
>>> c.__dict__
1
>>> object.__getattribute__(c, '__dict__')
1
>>> object.__getattr__(c, '__dict__')
Traceback (most recent call last):
    ...
AttributeError: type object 'object' has no attribute '__getattr__'

>>> c.x = 2
>>> c.x
2

>>> import inspect
>>> inspect.getattr_static(object, '__dict__')
<attribute '__dict__' of 'type' objects>
>>> inspect.getattr_static(type, '__dict__')
<attribute '__dict__' of 'type' objects>
>>> inspect.getattr_static(object, '__dict__') is inspect.getattr_static(type, '__dict__')
True
>>> inspect.getattr_static(object(), '__dict__')
Traceback (most recent call last):
    ...
AttributeError: __dict__
>>> inspect.getattr_static(c, '__dict__')
1

#>>> _descriptor4get_dict.__get__(c)
>>> inspect.getattr_static(object, '__dict__').__get__(c)
Traceback (most recent call last):
    ...
TypeError: descriptor '__dict__' for 'type' objects doesn't apply to a 'C' object


>>> inspect.getattr_static(c, '__dict__').__get__(c)
Traceback (most recent call last):
    ...
AttributeError: 'int' object has no attribute '__get__'
>>> inspect.getattr_static(C, '__dict__').__get__(c)
Traceback (most recent call last):
    ...
AttributeError: 'int' object has no attribute '__get__'


    #'''
    return object.__getattribute__(obj, '__dict__')
    return inspect.getattr_static(obj, '__dict__').__get__(obj)
    return _get_dict(obj)
    return _descriptor4get_dict.__get__(obj)
    #bug:return object.__getattribute__(obj, '__dict__')
_get_dict = _descriptor4get_dict.__get__





class ImmutableDictItem(tuple):
    r'''

>>> d = {ImmutableDictItem(1,2):3}
>>> d[ImmutableDictItem(1,4)]
3
>>> d
{ImmutableDictItem(1, 2): 3}
>>> d[ImmutableDictItem(1,4)] = 5
>>> d
{ImmutableDictItem(1, 2): 5}

>>> del d[ImmutableDictItem(1,4)]
>>> d[ImmutableDictItem(1,4)] = 6
>>> d
{ImmutableDictItem(1, 4): 6}
>>> d.pop(ImmutableDictItem(1,2))
6
>>> d[ImmutableDictItem(1,4)] = 6
>>> d.popitem(ImmutableDictItem(1,2))
Traceback (most recent call last):
    ...
TypeError: popitem() takes no arguments (1 given)

    #'''
    def __new__(cls, k, v, /):
        return tuple.__new__(cls, [k,v])
    def __eq__(sf, ot, /):
        if type(ot) is ImmutableDictItem is type(sf):
            k, v = sf
            k_, v_ = ot
            return k == k_
        return NotImplemented
    def __hash__(sf, /):
        k, v = sf
        return hash(k)
    def __repr__(sf, /):
        return (f'{type(sf).__name__!s}{tuple.__repr__(sf)!s}')
class ReaderMutableDictItem(tuple):
    r'''

>>> p12 = ImmutableDictItem(1,2)
>>> p13 = ImmutableDictItem(1,3)
>>> p45 = ImmutableDictItem(4,5)
>>> p1_ = ReaderMutableDictItem(1)
>>> p1_ == p45
False
>>> p45 == p1_
False
>>> p1_[-1]
[]
>>> repr(p1_)
Traceback (most recent call last):
    ...
TypeError: ReaderMutableDictItem(1, [])
>>> tuple.__repr__(p1_)
'(1, [])'

>>> p1_ == p12
True
>>> p13 == p1_
True
>>> p1_[-1]
[ImmutableDictItem(1, 2), ImmutableDictItem(1, 3)]
>>> repr(p1_)
Traceback (most recent call last):
    ...
TypeError: ReaderMutableDictItem(1, [ImmutableDictItem(1, 2), ImmutableDictItem(1, 3)])
>>> tuple.__repr__(p1_)
'(1, [ImmutableDictItem(1, 2), ImmutableDictItem(1, 3)])'

>>> hash(p1_) == hash(p12) == hash(p12)
True

    #'''

    def __new__(cls, k, /):
        return tuple.__new__(cls, [k, []])
    def __eq__(sf, ot, /):
        if type(ot) is ImmutableDictItem and ReaderMutableDictItem is type(sf):
            k, kvs = sf
            k_, v_ = ot
            r = k == k_
            if r:
                kvs.append(ot)
            return r
        return NotImplemented
    def __hash__(sf, /):
        k, kvs = sf
        return hash(k)
    def __repr__(sf, /):
        raise TypeError(f'{type(sf).__name__!s}{tuple.__repr__(sf)!s}')



class Meta4XFrozenDict(ABCMeta):
    __slots__ = ()
    def __getattribute__(sf, attr, /):
        if attr == '__mro__':
            return _mro
        if attr in _disabled_attrs:
            raise AttributeError(attr)
        return super(__class__, type(sf)).__getattribute__(sf, attr)
    if 0:
        def __subclasscheck__(cls, subclass, /):
            r'''
            'fail: frozenset is superclass not subclass'
#__subclasscheck__/__subclasshook__: fail
>>> issubclass(XFrozenDict, frozenset)
True
>>> isinstance(XFrozenDict(), frozenset)
True

            #'''
            if subclass is frozenset:
                return False
            return super().__subclasscheck__(subclass)

super(ABCMeta, Meta4XFrozenDict)
def _disabled_attrs():
    #_disabled_attrs = frozenset(frozenset.__dict__.keys() - Mapping.__dict__.keys() - {'__getattribute__', '__repr__', '__slots__', '__new__'})
    #_disabled_attrs = frozenset(frozenset.__dict__.keys() - Mapping.__dict__.keys() - XFrozenDict.__dict__.keys())
    s = frozenset.__dict__.keys()
    for C in Mapping.__mro__[:-1]:
        s -= C.__dict__.keys()
    s -= {'__getattribute__', '__repr__', '__slots__', '__new__'} #XFrozenDict.__dict__.keys()
    return frozenset(s)
_disabled_attrs = _disabled_attrs()
#print(sorted(_disabled_attrs))
assert sorted(_disabled_attrs) == ['__and__', '__ge__', '__gt__', '__le__', '__lt__', '__ne__', '__or__', '__rand__', '__reduce__', '__ror__', '__rsub__', '__rxor__', '__sizeof__', '__sub__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']



class MappingMixin4shallow_stable_repr(Mapping):
    __slots__ = ()
    def __repr__(sf, /):
        'stable repr if key, value using stable repr'
        cls = type(sf)
        #if not cls is __class__: raise TypeError
        ls = [(repr(k), repr(v)) for k, v in sf.items()]
        ls.sort()
        s = ', '.join('{!s}: {!s}'.format(k, v) for k, v in ls)
        if s:
            s = ''.join(['{', s, '}'])
        s = f'{cls.__name__}({s!s})'
        return s
class MappingMixin4hash(Mapping):
    __slots__ = ()
    #__eq__ = Mapping.__eq__
    #__hash__ = Mapping.__hash__
    def __ne__(sf, ot, /):
        return not (sf == ot)
    def __eq__(sf, ot, /):
        #why cls take part in? OrderDict, hash collision...
        #Mapping.__eq__: return dict(self.items()) == dict(other.items())
        return type(ot) is type(sf) and len(ot) == len(sf) and Mapping.__eq__(sf, ot)
        #################################
        if type(ot) is type(sf):
            return Mapping.__eq__(sf, ot)
        return NotImplemented
    def __hash__(sf, /):
        h = 3^hash(type(sf))
        for hh in map(hash, sf.items()):
            h ^= hh
        return h

class MappingMixin4singleton_immutable_empty_dict(MappingMixin4hash):
    __slots__ = ()
    ___DictType4new___ = dict #OrderDict
    @abstractmethod
    def ___get_or_mk_from_fresh_dict___(cls, fresh_dict, /):
        'fresh_dict -> sf'
    def __new__(cls, /, *args, **kwargs):
        #if not cls is __class__: raise TypeError
        if not kwargs and len(args) == 1:
            [x] = args
            if type(x) is cls:
                return x
        d = cls.___DictType4new___(*args, **kwargs)
        if not d:
            try:
                return cls.__dict__['__the_empty_FrozenDict']
            except KeyError:
                pass
        sf = cls.___get_or_mk_from_fresh_dict___(cls, d)

        if not d:
            if type(sf) is cls:
                setattr(cls, '__the_empty_FrozenDict', sf)
                if not sf is cls(*args, **kwargs): raise logic-err
        return sf

class MappingMixin4get_item(Mapping):
    __slots__ = ()
    if 0:
        def __getitem__(sf, k, /):
            cls = type(sf)
            (old_k, v) = cls.___get_item___(sf, k)
            return v
    @abstractmethod
    def ___get_item___(sf, key4detect, /):
        '-> (old_k, old_v)'
    @abstractmethod
    def ___post_process4getitem___(sf, post_action, exists_or_value_or_item, *args, **kwargs):
        'see:___check_and_converter_key4get___'
    @abstractmethod
    def ___check_and_converter_key4get___(sf, key4get, /):
        'key4get-from-__getitem__ -> (key4detect, access_case, may (post_action, args, kwargs)) #access_case=False-detect|True-value|Ellipsis-old_item #see:___post_process4getitem___'
    def __getitem__(sf, key4get, /):
        cls = type(sf)
        (key4detect, access_case, may_action_args_kwargs) = cls.___check_and_converter_key4get___(sf, key4get)
        if access_case is False:
            #detect
            r = key4detect in sf
        else:
            (old_k, v) = cls.___get_item___(sf, key4detect)
            if access_case is True:
                r = v
            elif access_case is ...:
                r = (old_k, v)
            else:
                raise TypeError(f'access_case is not tribool: {access_case!r}')

        if may_action_args_kwargs is None:
            return r
        (post_action, args, kwargs) = may_action_args_kwargs
        return cls.___post_process4getitem___(sf, post_action, r, *args, **kwargs)

class MappingMixin4check_key4set(Mapping):
    __slots__ = ()
    @classmethod
    @abstractmethod
    def ___check_key4set___(cls, key4set, /):
        pass

class XFrozenDict(MappingMixin4check_key4set, MappingMixin4get_item, MappingMixin4singleton_immutable_empty_dict, MappingMixin4hash, MappingMixin4shallow_stable_repr, Mapping, frozenset, metaclass=Meta4XFrozenDict):
    #class XFrozenDict(Mapping):
    r'''
    not FrozenDict since has frozenset.api
        not subclass of frozenset, too, since not compatibility
        just an impl obj...

>>> XFrozenDict() is XFrozenDict() is empty_XFrozenDict
True

>>> weakref.ref(XFrozenDict())() is empty_XFrozenDict is XFrozenDict()
True

>>> XFrozenDict().__dict__
Traceback (most recent call last):
    ...
AttributeError: 'XFrozenDict' object has no attribute '__dict__'


>>> XFrozenDict() == {}
False
>>> XFrozenDict() == XFrozenDict()
True
>>> hash(XFrozenDict()) == 3^hash(XFrozenDict)
True
>>> hash(XFrozenDict({1:3})) == hash(XFrozenDict({1:2}))
False
>>> (XFrozenDict({1:3})) == (XFrozenDict({1:2}))
False
>>> (XFrozenDict({1:3})) == (XFrozenDict({1:3}))
True




    #'''
    #__slots__ = ('__weakref__',)
    #TypeError: __weakref__ slot disallowed: either we already got one, or __itemsize__ != 0
    __slots__ = ()
    #__getitem__, __iter__, __len__
    __getattribute__ = frozenset.__getattribute__
        #see: _4disabled_attrs()


    def __len__(sf, /):
        return frozenset.__len__(sf)
    def __iter__(sf, /):
        for k, v in frozenset.__iter__(sf):
            yield k
    def __contains__(sf, key4detect, /):
        item = ImmutableDictItem(key4detect, 0)
        return frozenset.__contains__(sf, item)
    @override
    def ___get_item___(sf, key4detect, /):
        '-> (old_k, old_v)'
        '-> item<old_k, old_v>'
        reader = ReaderMutableDictItem(key4detect)

        if frozenset.__contains__(sf, reader):
            _k, kvs = reader
            [item] = kvs
            #return item
            (old_k, old_v) = item
            return (old_k, old_v)
        else:
            raise KeyError(key4detect)
    @override
    def ___post_process4getitem___(sf, post_action, exists_or_value_or_item, *args, **kwargs):
        'see:___check_and_converter_key4get___'
        raise NotImplementedError
    @override
    def ___check_and_converter_key4get___(sf, key4get, /):
        'key4get-from-__getitem__ -> (key4detect, access_case, may (post_action, args, kwargs)) #access_case=False-detect|True-value|Ellipsis-old_item #see:___post_process4getitem___'
        if type(key4get) is slice:
            key4detect, access_case, may_action_args_kwargs = slice2triple(slice)
        else:
            key4detect = key4get
            access_case = True#value
            may_action_args_kwargs = None
        return key4detect, access_case, may_action_args_kwargs


    @classmethod
    @override
    def ___check_key4set___(cls, key4set, /):
        pass
    @override
    def ___get_or_mk_from_fresh_dict___(cls, fresh_dict, /):
        'fresh_dict -> sf'
        T = ImmutableDictItem
        for _ in map(cls.___check_key4set___, fresh_dict):pass
        items = (T(k, v) for k, v in fresh_dict.items())
        sf = frozenset.__new__(cls, items)
        return sf
    if 0:
        @classmethod
        #@override
        def __subclasshook__(cls, C, /):
            r'''
            'fail: frozenset is superclass not subclass'
#__subclasscheck__/__subclasshook__: fail
>>> issubclass(XFrozenDict, frozenset)
True
>>> isinstance(XFrozenDict(), frozenset)
True

            #'''
            # ABCMeta::__subclasshook__
            if C is frozenset:
                return False
            return NotImplemented
empty_XFrozenDict = _empty_XFrozenDict = XFrozenDict()
def _mro():
    _mro = type.__getattribute__(XFrozenDict, '__mro__')
    i = _mro.index(frozenset)
    _mro = tuple(t for t in _mro if t is not frozenset)
    return _mro
_mro = _mro()
assert frozenset not in XFrozenDict.__mro__

class DisabledClassAttr:
    def __init__(sf, may_owner, name, /):
        sf.__set_name__(may_owner, name)
    def __get__(sf, instance, may_owner=None, /):
        attr = sf.name
        if instance is None:
            if may_owner is None: raise TypeError
            raise AttributeError(attr)
        elif 1:
            for d in iter_dicts(instance):
                if attr in d:
                    return d[attr]
            raise AttributeError(attr)
        else:
            try:
                #bug:return instance.__dict__[attr]
                return get_dict(instance)[attr]
            except KeyError:
                raise AttributeError(attr)
    def __set_name__(sf, owner, name, /):
        sf.may_owner = owner
        sf.name = name
    def __repr__(sf, /):
        pair = sf.may_owner, sf.name
        return (f'{type(sf).__name__!s}{tuple.__repr__(pair)!s}')

def _4disabled_attrs(cls, _disabled_attrs, /):
    try:
        for attr in _disabled_attrs:
            type.__setattr__(cls, attr, DisabledClassAttr(cls, attr))
    except AttributeError as e:
        raise AttributeError((attr, e))
_4disabled_attrs(XFrozenDict, _disabled_attrs)

def _t():
    d = XFrozenDict()
    weakref.ref(d)
    assert not hasattr(d, '__dict__')
    assert d is empty_XFrozenDict
    #d[1]
    #assert not issubclass(XFrozenDict, frozenset)
    #assert not isinstance(d, frozenset)
_t()

#Set.register(XFrozenDict)
#Mapping.register(XFrozenDict)



def is_special_attr(attr, /):
    return type(attr) is str and attr.startswith('__') and attr.endswith('__')
def _disabled_all_default_attrs4obj():
    def f(pkg, /):
        attrs = {*filter(is_special_attr, pkg.__dict__)}
        return attrs
    adds = '__hash__ __int__ __bool__ __len__ __repr__ __str__ __binary__ __bytes__ __ascii__'.split()
    excludes = {'__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__'}
    #print(sorted(f(operator) & f(types)))
    #print(sorted(f(seed))) #pkg without __all__
    #print(sorted(f(types))) #builtins-module without __path__
    #assert excludes <= f(operator), excludes - f(operator)
    assert excludes <= f(types) | f(seed.abc)
    attrs = f(operator) - excludes - f(types) - f(seed)
    assert sorted(attrs) == [
            '__abs__', '__add__', '__and__', '__concat__', '__contains__', '__delitem__', '__eq__', '__floordiv__', '__ge__', '__getitem__', '__gt__'
            , '__iadd__', '__iand__', '__iconcat__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__inv__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__itruediv__', '__ixor__'
            , '__le__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__not__', '__or__', '__pos__', '__pow__', '__rshift__', '__setitem__', '__sub__', '__truediv__', '__xor__']
    attrs.update(adds)
    attrs = sorted(attrs)
    return attrs
_disabled_all_default_attrs4obj = (_disabled_all_default_attrs4obj())
#print(_disabled_all_default_attrs4obj)
assert _disabled_all_default_attrs4obj == r'''
    __abs__
    __add__
    __and__
    __ascii__
    __binary__
    __bool__
    __bytes__
    __concat__
    __contains__
    __delitem__
    __eq__
    __floordiv__
    __ge__
    __getitem__
    __gt__
    __hash__
    __iadd__
    __iand__
    __iconcat__
    __ifloordiv__
    __ilshift__
    __imatmul__
    __imod__
    __imul__
    __index__
    __int__
    __inv__
    __invert__
    __ior__
    __ipow__
    __irshift__
    __isub__
    __itruediv__
    __ixor__
    __le__
    __len__
    __lshift__
    __lt__
    __matmul__
    __mod__
    __mul__
    __ne__
    __neg__
    __not__
    __or__
    __pos__
    __pow__
    __repr__
    __rshift__
    __setitem__
    __str__
    __sub__
    __truediv__
    __xor__
    #'''.split()[:-1], _disabled_all_default_attrs4obj


def _mk_dict4disabled_all_default_attrs(disabled_all_default_attrs, /, *, excludes):
    s = {*disabled_all_default_attrs}
    s -= {*excludes}
    d = {attr:DisabledClassAttr(None, attr) for attr in s}
    return d

class DisabledAllDefaultClassAttr(ABC):
    __slots__ = ()
    locals().update(_mk_dict4disabled_all_default_attrs(_disabled_all_default_attrs4obj, excludes = ''.split()))
#object.__new__(DisabledAllDefaultClassAttr)
#print(DisabledAllDefaultClassAttr.__new__)
#print(DisabledAllDefaultClassAttr.__dict__)
def _t2():
    x = DisabledAllDefaultClassAttr()
    assert not hasattr(DisabledAllDefaultClassAttr, '__hash__')
    assert not hasattr(x, '__hash__')
    class C:pass
    assert hasattr(C, '__hash__')
    assert hasattr(C(), '__hash__')
_t2()

r"""[[[[[  mk_Ops => bind Obj-py-type to each ops via redirect attr in mro.__dict__ or delete/overwrite by DisabledClassAttr
if __name__ == "__main__":
    import doctest
    doctest.testmod()


def _disabled_all_default_attrs4cls():
    attrs = _disabled_all_default_attrs(object)
    return attrs
def _disabled_all_default_attrs4obj():
    #attrs = _disabled_all_default_attrs(object())
    class C:pass
    attrs = _disabled_all_default_attrs(C())
    return attrs
def _disabled_all_default_attrs(obj, /):
    cls = type(obj)
    mro = get_mro4cls(cls)
    s = set()
    s = s.union(dir(obj), get_dict(obj).keys())#(, dir(cls), get_dict(cls).keys())
    s = s.union(*(get_dict4cls(cls).keys() for cls in mro))
    #excludes = '__getattribute__ __new__ __init__'.split()
    s = sorted(s)
    return s
    print(s)
    #['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__weakrefoffset__', 'mro']
_disabled_all_default_attrs4obj = (_disabled_all_default_attrs4obj())
_disabled_all_default_attrs4cls = (_disabled_all_default_attrs4cls())

#print(_disabled_all_default_attrs4obj)
#print(_disabled_all_default_attrs4cls)
assert _disabled_all_default_attrs4obj == ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
assert _disabled_all_default_attrs4cls == ['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__weakrefoffset__', 'mro']
raise
_disabled_all_default_attrs = _disabled_all_default_attrs()
_disabled_all_default_attrs = ['__call__', '__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__le__', '__lt__', '__ne__', '__new__', '__prepare__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__str__', '__subclasscheck__', '__subclasshook__']

def _mk_dict4disabled_all_default_attrs(*, excludes):
    s = {*_disabled_all_default_attrs}
    s -= {*excludes}
    d = {attr:DisabledClassAttr(None, attr) for attr in s}
    return d
def _4disabled_all_default_attrs(cls, /, *, excludes):
    s = {*_disabled_all_default_attrs}
    s -= {*excludes}
    _4disabled_attrs(cls, s)
DisabledClassAttr
class Meta4DisabledAllDefaultClassAttr(ABCMeta):
    __slots__ = ()
    locals().update(_mk_dict4disabled_all_default_attrs(excludes = '__qualname__ __new__ __call__'.split()))

#_4disabled_all_default_attrs(Meta4DisabledAllDefaultClassAttr, excludes = '__getattribute__ __new__ __init__'.split())
#_4disabled_all_default_attrs(Meta4DisabledAllDefaultClassAttr, excludes = '__bases__ __base__ __basicsize__'.split())
if 0:
    class DisabledAllDefaultClassAttr(ABC, metaclass=Meta4DisabledAllDefaultClassAttr):
        __slots__ = ()
        locals().update(_mk_dict4disabled_all_default_attrs(excludes = '__qualname__'.split()))
    #_4disabled_all_default_attrs(DisabledAllDefaultClassAttr, excludes = ''.split())
    object.__new__(DisabledAllDefaultClassAttr)
    print(DisabledAllDefaultClassAttr.__new__)
    print(DisabledAllDefaultClassAttr.__dict__)
#]]]]]"""





r"""[[[[[ MappingProxyType cannot be base class
class WFrozenDict(MappingMixin4singleton_immutable_empty_dict, MappingMixin4hash, MappingMixin4shallow_stable_repr, MappingProxyType, Mapping):
    #TypeError: type 'mappingproxy' is not an acceptable base type
    'wrapper-impl-FrozenDict'
    __slots__ = ()
    @override
    def ___get_or_mk_from_fresh_dict___(cls, fresh_dict, /):
        'fresh_dict -> sf'
        sf = MappingProxyType.__new__(cls, fresh_dict)
        return sf
#]]]]]"""
r"""[[[[[
#]]]]]"""

#################################
#################################
#################################
#################################
#################################
#################################
#################################
#################################


def mk_type4ops(meta, attr2symbol, attr2descriptor, /):
    symbol2descriptor = mk_body4type4ops(attr2symbol, attr2descriptor)
    bases = ()
    return type(name, bases, symbol2descriptor, metaclass=meta)
def mk_body4type4ops(attr2symbol, attr2descriptor, /):
    r'''

#>>> c = object.__new__(C)
#   raise since object.__new__ assume __abstractmethods__ are all str

>>> class C(ABC__no_slots):
...     locals().update({999:abstractmethod(lambda:0)})
>>> c = object.__new__(C)
Traceback (most recent call last):
    ...
TypeError: sequence item 0: expected str instance, int found

>>> C.__abstractmethods__
frozenset({999})

>>> class C(ABC__no_slots):
...     locals().update({999:(lambda:0)})
>>> c = object.__new__(C)
>>> c = C()
>>> C.__abstractmethods__
frozenset()


>>> class C(ABC__no_slots):
...     locals().update(mk_body4type4ops({'f':999}, {'f':abstractmethod(lambda:0)}))
>>> C.__abstractmethods__
frozenset({999})


>>> mk_body4type4ops(dict(f=999, a=-1), dict(g=111, a=-2))
Traceback (most recent call last):
    ...
ValueError: extra_attrs4symbol={'f'}, extra_attrs4descriptor={'g'}
>>> mk_body4type4ops(dict(f=999, g=999, a=-1), dict(f=111, g=111, a=-2))
Traceback (most recent call last):
    ...
ValueError: symbols4duplicate={999}
>>> mk_body4type4ops(dict(f=999, g=888, a=-1), dict(f=111, g=111, a=-2)) == {999: 111, 888: 111, -1: -2}
True

    #'''
    attrs4symbol = attr2symbol.keys()
    attrs4descriptor = attr2descriptor.keys()
    if not attrs4symbol == attrs4descriptor:
        extra_attrs4symbol = set(attrs4symbol - attrs4descriptor)
        extra_attrs4descriptor = set(attrs4descriptor - attrs4symbol)
        raise ValueError(f'extra_attrs4symbol={extra_attrs4symbol}, extra_attrs4descriptor={extra_attrs4descriptor}')

    symbol2descriptor = {}
    symbols4duplicate = set()
    for attr, symbol in attr2symbol.items():
        descriptor = attr2descriptor[attr]
        if symbol in symbol2descriptor:
            symbols4duplicate.add(symbol)
        else:
            symbol2descriptor[symbol] = descriptor
    if symbols4duplicate:
        raise ValueError(f'symbols4duplicate={symbols4duplicate}')
    symbols = set(attr2symbol.values())
    if not len(symbols) == len(attr2symbol) == len(symbol2descriptor): raise logic-err
    return symbol2descriptor

from seed.abc.eq_by_id.AddrAsHash import BaseAddrAsHash, le_AddrAsHash, AddrAsHash as EqById

class AbstractAttr(EqById, tuple):
    __slots__ = ()
    def __new__(cls, __name__, __doc__, /):
        sf = super(__class__, cls).__new__(cls, [__name__, __doc__])
        return sf
    @property
    def __isabstractmethod__(sf, /):
        return True

#e ../../python3_src/seed/hierarchy/symbol/PrivateSymbol.py
from seed.hierarchy.symbol.PrivateSymbol import PrivateSymbol
symbol4get_ops__whole_bind_as_obj = PrivateSymbol('@symbol4get_ops__whole_bind_as_obj: used as key only, not callable')
symbol4get_interpreter__whole_bind_as_ops = PrivateSymbol('@symbol4get_interpreter__whole_bind_as_ops: used as key only, not callable')
class IHandler4Bind4Ops(ABC):
    'whole_bind as ops ==>> get_interpreter :: handler -> interpreter'
    __slots__ = ()
    locals().update({symbol4get_interpreter__whole_bind_as_ops:AbstractAttr('symbol4get_interpreter__whole_bind_as_ops', 'obj_or_ops = Bind handler state ==>> get_dict4cls(type(handler))[symbol4get_interpreter__whole_bind_as_ops](handler)')})

class IHandler4Bind4Obj(ABC):
    'whole_bind as obj ==>> get_ops :: handler -> ops'
    __slots__ = ()
    locals().update({symbol4get_ops__whole_bind_as_obj:AbstractAttr('symbol4get_ops__whole_bind_as_obj', 'obj_or_ops = Bind handler state ==>> get_dict4cls(type(handler))[symbol4get_ops__whole_bind_as_obj](handler)')})

class IHandler4Bind4UnionOpsObj(IHandler4Bind4Obj, IHandler4Bind4Ops):
    'whole_bind as obj&ops'
    __slots__ = ()
class SymbolAccessError(Exception):pass
    #LookupError, AttributeError
def get_ops__whole_bind_as_obj(handler, /):
    ops = get_via_shadow_cls_dict(handler, symbol4get_ops__whole_bind_as_obj)
    return ops
def get_interpreter__whole_bind_as_ops(handler, /):
    interpreter = get_via_shadow_cls_dict(handler, symbol4get_interpreter__whole_bind_as_ops)
    return interpreter
def get_via_shadow_cls_dict(handler, symbol, /):
    d = get_dict4cls(type(handler))
    if symbol not in d: raise SymbolAccessError(symbol)

    getter = d[symbol]
    return getter(handler)

class Bind(DisabledAllDefaultClassAttr):
    __slots__ = ('__weakref__', 'handler', 'state')
    __new__ = DisabledClassAttr(None, None)
    __init__ = DisabledClassAttr(None, None)
_descriptor4handler = Bind.handler
_descriptor4state = Bind.state
del Bind.handler
del Bind.state
Bind.__slots__ = ()


PrivateSymbol
from seed.hierarchy.symbol.PrivateSymbol import PrivateSymbol
#e ../../python3_src/seed/hierarchy/symbol/PrivateSymbol.py
#e ../../python3_src/seed/hierarchy/register/AttachmentDataRegister4cls.py
from seed.hierarchy.register.AttachmentDataRegister4cls import attachment_data_register4cls, mk_private_attr, mk_private_attr__using_permanent_objs_as_path, IHandler4AttachmentDataRegister4cls, default_handler4AttachmentDataRegister4cls, FunctionalHandler4AttachmentDataRegister4cls, mk_FunctionalHandler4AttachmentDataRegister4cls__human
#e ../../python3_src/seed/hierarchy/plugin_api4register/stable_repr4export_long_term_storage.py

#e ../../python3_src/seed/hierarchy/symbol/check_symbol.py
py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/hierarchy/symbol/check_symbol.py
check_symbol = check_Weakable_EqById
#e ../../python3_src/seed/hierarchy/plugin_api4register/getattr4symbol.py
py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/hierarchy/plugin_api4register/getattr4symbol.py

from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash, le_AddrAsHash
public_symbol4getattr4symbol = PublicSymbol(...)
attachment_data_register4cls.register_handler4symbol(public_symbol4getattr4symbol, default_handler4AttachmentDataRegister4cls)
    #check may callable?? FunctionalHandler4AttachmentDataRegister4cls?
    mk_FunctionalHandler4AttachmentDataRegister4cls__human(check_data=check_callable)

BaseError__getattr4symbol
TypeError__getattr4symbol
protocol-example:
    get :: (sf, private_vs_public, symbol, level4sf, level4attr, /, *, explain:bool) -> result
    private_vs_public:bool
        target_concept is private/public attribute
    explain:bool
        False: result is sth like descriptor
        True: result is sth like MethodType(sf/cls, f), property(f)(sf)...
    level-at-type-system
    0=level4ground:
        level4ground is level for ground_obj where the target_concept belong to
    level4sf:int
        means [sf is (type**level4sf)(ground_obj)]
        level4sf=0: sf is ground_obj
        level4sf=1: sf is cls=type(ground_obj)
        level4sf=2: sf is meta=type(type(ground_obj))
        level4sf=-1: cls=type(sf) is ground_obj
        level4sf=-2: meta=type(type(sf) is ground_obj)
    level4attr:uint
        means [(?lvl:uint, [lvl >= level4attr] -> [attr_obj which repr the target_concept is storaged at (type**lvl)(ground_obj)])]
        level4attr=0: attr_obj is storaged at ground_obj, instance_property#instance_method
        level4attr=1: attr_obj is storaged at cls=type(ground_obj), class_property#classmethod

import weakref
def check_callable(symbol, /):
    if not callable(symbol): raise TypeError
def check_Weakable_EqById(symbol, /):
    weakref.ref(symbol)
    if not le_AddrAsHash(type(symbol)): raise TypeError
def check_callable_Weakable_EqById(symbol, /):
    check_callable(symbol)
    check_Weakable_EqById(symbol)
check_symbol = check_Weakable_EqById

def getattr4symbol(sf, api_symbol4protocol, /, *args, **kwargs):
    r'''
    api_symbol4protocol :: (tmay_result, sf4getattr4symbol, api_symbol4protocol, *args, **kwargs) -> None
        symbol4protocol&callable4test_input_output&Weakable&le_AddrAsHash
    ___getattr4symbol___(sf, api_symbol4protocol, *args, **kwargs) -> result

    cls.___getattr4symbol___
        mimic cls.__getattribute__
    attachment_data_register4cls.get_data4cls(cls, api_symbol4protocol)
        mimic object.__getattribute__
    attachment_data_register4cls.get_data4cls(cls, public_symbol4getattr4symbol)
        mimic cls.__getattr__
    #'''
    def sf2___getattr4symbol___(sf, /):
        cls = type(sf)
        f = getattr(cls, '___getattr4symbol___', IGetAttr4symbol.___getattr4symbol___)
        return f
    return apply4___getattr4symbol___(sf2___getattr4symbol___, sf, api_symbol4protocol, *args, **kwargs):
class IGetAttr4symbol:
    def __subclasshook__ mro hasattr ___getattr4symbol___ and fst not None ??check callable??
    @abstractmethod
    def ___getattr4symbol___(sf, api_symbol4protocol, /, *args, **kwargs):
        r'''
    api_symbol4protocol :: (tmay_result, sf4getattr4symbol, api_symbol4protocol, *args, **kwargs) -> None
        symbol4protocol&callable4test_input_output
        #'''
        def sf2___getattr4symbol___(sf, /):
            cls = type(sf)
            #f = getattr(cls, '___getattr4symbol___', IGetAttr4symbol.___getattr4symbol___)
            Nothing = object()
            m = Nothing
            if 0:
                #deprecated:
                #___getattr4symbol___
                #   mimic cls.__getattribute__
                if m is Nothing:
                    m = getattr(cls, '___getattr4symbol___', Nothing)
            #api_symbol4protocol
            #   mimic object.__getattribute__
            if m is Nothing and attachment_data_register4cls.detect_handler4symbol(api_symbol4protocol):
                tmay = attachment_data_register4cls.get_tmay_data4cls(cls, api_symbol4protocol)
                if tmay:
                    [m] = tmay
                else:
                    pass
            #public_symbol4getattr4symbol
            #   mimic cls.__getattr__
            if m is Nothing:
                tmay = attachment_data_register4cls.get_tmay_data4cls(cls, public_symbol4getattr4symbol)
                if tmay:
                    [m] = tmay
                else:
                    pass
            if m is Nothing or m is None::
                raise TypeError__getattr4symbol(f'not support getattr4symbol(): cls={cls!r}')
            f = ___getattr4symbol___ = m
            return f
        return apply4___getattr4symbol___(sf2___getattr4symbol___, sf, api_symbol4protocol, *args, **kwargs):

def apply4___getattr4symbol___(sf2___getattr4symbol___, sf, api_symbol4protocol, *args, **kwargs):
    check_callable(sf2___getattr4symbol___)
    check_callable_Weakable_EqById(api_symbol4protocol)

    if not None is api_symbol4protocol((), sf, api_symbol4protocol, *args, **kwargs): raise TypeError #check input 4 baisc requirements

    ___getattr4symbol___ = sf2___getattr4symbol___(sf)
    if not callable(___getattr4symbol___): raise TypeError__getattr4symbol(f'not callable:cls.___getattr4symbol___: cls={cls!r}')
    r = ___getattr4symbol___(sf, api_symbol4protocol, *args, **kwargs)
    if not None is api_symbol4protocol((r,), sf, api_symbol4protocol, *args, **kwargs): raise TypeError #check output 4 baisc requirements
    return r



from types import MethodType
class AttachmentDataRegister:
    __slots__ = ('_d',)
    def __init__(sf, /):
        sf._d = {}
    def check_key(sf, cls, /):
        pass
    def check_value(sf, data, /):
        pass
    def __contains__(sf, cls, /):
        return cls in sf._d
    def __getitem__(sf, cls, /):
        return sf._d[cls]
    def __setitem__(sf, cls, data, /):
        sf.check_key(cls)
        sf.check_value(data)
        if cls in sf: raise KeyError
        if not data is sf._d.setdefault(cls, data): raise logic-err
        if not data is sf._d[cls]: raise logic-err
class AttachmentXxxMethodRegister(AttachmentDataRegister):
    __slots__ = ()
    def check_key(sf, cls, /):
        get_mro4cls(cls)
    def check_value(sf, data, /):
        if not callable(data):raise TypeError
class AttachmentInstanceMethodRegister(AttachmentXxxMethodRegister):
    __slots__ = ()
    def __call__(sf, instance, /, *args, **kwargs):
        cls = type(instance)
        f = sf[cls]
        return f(instance, *args, **kwargs)
    def bind(sf, instance, /):
        cls = type(instance)
        f = sf[cls]
        return MethodType(f, instance)
class AttachmentClassMethodRegister(AttachmentXxxMethodRegister):
    __slots__ = ()
    def call4obj(sf, instance, /, *args, **kwargs):
        cls = type(instance)
        return sf.call4cls(cls, *args, **kwargs)
    def call4cls(sf, cls, /, *args, **kwargs):
        f = sf[cls]
        return f(cls, *args, **kwargs)
    def bind4obj(sf, instance, /):
        cls = type(instance)
        return sf.bind4cls(cls)
    def bind4cls(sf, cls, /):
        f = sf[cls]
        return MethodType(f, cls)


r"""[[[[[
is_immutable_pyobj
    register...
recur_deep_view
    register...
batch_recur_deep_immutable_pyobj_converter
    register...
    #DAG
batch_recur_deep_burn_to_immutable_emplace
def is_Interpreter(x, /):
    ..
    return ... and is_immutable_pyobj(x)
def gk_Ops(interpreter, *args, **kwargs, /):
    if not is_Interpreter(Interpreter): raise TypeError
    (case, payload) = interpreter[get_or_mk_ops](interpreter, *args, **kwargs)
    if not type(case) is bool: raise TypeError
    else:
        is_new = case
        if is_new is False:
            sf = old_sf = payload
            _interpreter, _ops_state = __unbox_Ops()
            sgii_protocol[is_subops_of](sf, interpreter, ops_state)
            if not is_Ops(sf): raise TypeError
        else:
            ops_state = payload
            sf = _mk_Ops(interpreter, ops_state)
            if not is_Ops(sf): raise TypeError

def _mk_Ops(interpreter, ops_state, /):
    'immutable'
    if not is_Interpreter(Interpreter): raise TypeError
    ops_state = interpreter[pre_init_transform](interpreter, ops_state)
        #eg. std, immutable
    if not is_immutable_pyobj(ops_state): raise TypeError
    interpreter[pre_init_check](interpreter, ops_state)
    sf = __mk_Bind(interpreter, ops_state)
    interpreter[post_init_check](id(sf), interpreter, ops_state)
    interpreter[post_init_process](sf)
    return sf
        #interpreter[pre_update_check](interpreter, old_ops_state, delta)
        #interpreter[post_update_check](id(sf), interpreter, old_ops_state, delta, new_ops_state)
        #interpreter[post_update_process](sf, old_ops_state)

def __mk_Bind(handler, state, /):
    sf = object.__new__(Bind)
    _descriptor4handler.__set__(sf, handler)
    _descriptor4state.__set__(sf, state)
    return sf


def _mk_Obj(ops, obj_state, /):
def is_Obj(x, /):
    ..
def _mk_UnoinOpsObj(interpreter__when_whole_as_ops, obj_as_whole_ops_state, /):
    r'''
    #def mk_UnoinOpsObj(interpreter__when_whole_as_ops, ops__when_whole_as_obj, xstate, /):
    'immutable'

    whole_bind as ops:
        interpreter__when_whole_as_ops ~ whole_ops_state@(ops__when_whole_as_obj, xstate)
            immutable
            as-ops can access member@as-obj
    whole_bind as obj:
        no:
            ops__when_whole_as_obj ~ whole_obj_state@(interpreter__when_whole_as_ops, xstate)
                as-obj can access member@as-ops
        yes:
            ops__when_whole_as_obj ~ whole_obj_state@xstate
    #'''
    if 0:
        if is_UnoinOpsObj(obj_as_whole_ops_state):
            obj_as_whole_ops_state = get_xstate(obj_as_whole_ops_state)
        if is_UnoinOpsObj(obj_as_whole_ops_state): raise TypeError
        if is_Ops(obj_as_whole_ops_state): raise TypeError

    if not is_Obj(obj_as_whole_ops_state): raise TypeError
    return _mk_Ops(interpreter__when_whole_as_ops, obj_as_whole_ops_state)
#]]]]]"""


r"""[[[[[
#]]]]]"""
r"""[[[[[
class HierarchyAPI:
    @staticmethod
    def get_ops4obj(obj, /):
        cls = type(obj)
        ops = cls.___get_ops4obj___(obj)
        return ops
    @staticmethod
    def get_hierarchy_api4ops(ops, /):
        cls = type(ops)
        hierarchy_api = cls.___get_hierarchy_api4ops___(ops)
        return hierarchy_api
    @staticmethod
    def get_hierarchy_api4obj(obj, /):
        return get_hierarchy_api4ops(get_ops4obj(obj))
    @staticmethod
    def get_ops_and_hierarchy_api4obj(obj, /):
        ops = get_ops4obj(obj)
        hierarchy_api = get_hierarchy_api4ops(ops)
        return (ops, hierarchy_api)

    #################################
    #################################
    #################################
    @staticmethod
    def repr__per_call(obj, /):
        '-> repr #random per call'
    @staticmethod
    def repr__per_runtime(obj, /):
        '-> repr #addr/hash'
    @staticmethod
    def repr__longterm_stable(obj, /):
        '-> repr #external protocol representation'
    #################################
    #################################
    @staticmethod
    def get_or_mk(ops, /, *args, **kwargs):
        '-> (is_new:bool, obj<subops of ops>)|(Ellipsis, other_obj)'

    #################################
    #################################
    @staticmethod
    def get_descriptor4ops(ops, symbol, /):
    #################################
    @staticmethod
    def get_property4obj(obj, symbol, /):
    @staticmethod
    def set_property4obj(obj, symbol, /):
    @staticmethod
    def del_property4obj(obj, symbol, /):
    #################################
    #################################
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
    @staticmethod
get_ops4obj = HierarchyAPI.get_ops4obj
get_hierarchy_api4ops = HierarchyAPI.get_hierarchy_api4ops
get_hierarchy_api4obj = HierarchyAPI.get_hierarchy_api4obj

class IGetOps(ABC):
    'obj <: IGetOps'
    def ___get_ops4obj___(obj, /):
        'obj -> ops'
class IGetHierarchyAPI(ABC):
    'ops <: IGetHierarchyAPI'
    def ___get_hierarchy_api4ops___(ops, /):
        'ops -> hierarchy_api'
class IHierarchyAPI(ABC):
    r'''
    ops <: immutable
    obj = true_ops_instance
    xobj = pseudo_obj | obj
    pseudo_obj = pure_virtual_obj | shadow_obj
        vs:
            [obj <: IGetOps]
            [not [pseudo_obj <: IGetOps]]
        vs:
            [pure_virtual_obj doesnot contain obj]
            [shadow_obj contains obj]

        using pure_virtual_obj to prepare new obj #see:prepare4gk
        using shadow_obj to catch delta-modify
        commit batch update at once to keep obj in valid state
            #decomposed-delta-check on modified members
            shadow_obj may be set in invalid state, violate constraints
    #'''
    @abstractmethod
    def is_shadow_obj(api, ops, xobj, /):
        'xobj -> bool'
    @abstractmethod
    def gk_shadow_obj(api, ops, obj, /):
        'obj -> shadow_obj #obj binds at most one shadow_obj at one time'
    @abstractmethod
    def mk_shadow_obj(api, ops, obj, updates, /):
        'obj -> updates -> shadow_obj #for prepare4gk/repr__per_call/...'
    @abstractmethod
    def mk_pure_virtual_obj(api, ops, updates, /):
        'updates -> pure_virtual_obj #for prepare4gk/repr__per_call/...'
    @abstractmethod
    def commit_batch_updates(api, ops, shadow_obj, /):
        '!not pure_virtual_obj!#check-before-commit'
    #################################
    #################################
    #################################
    @abstractmethod
    def repr__per_call(api, ops, xobj, /):
        '-> repr #random per call'
    @abstractmethod
    def repr__per_runtime(api, ops, xobj, /):
        '-> repr #addr/hash'
    @abstractmethod
    def repr__longterm_stable(api, ops, xobj, /):
        '-> repr #external protocol representation'
    #################################
    #################################
    @abstractmethod
    def get_or_mk(api, ops, /, *args, **kwargs):
        '-> (is_new:bool, obj<subops of ops>)|(Ellipsis, other_obj)'
        #ops[prepare4gk] :: ... -> (False, old-cached-obj) | (True, pseudo_obj-to-mk-new-obj)

    #################################
    #################################
    @abstractmethod
    def get_descriptor4ops(api, ops, symbol, /):
    #################################
    @abstractmethod
    def get_property4obj(api, ops, xobj, symbol, /):
    @abstractmethod
    def set_property4obj(api, ops, xobj, symbol, /):
    @abstractmethod
    def del_property4obj(api, ops, xobj, symbol, /):
    #################################
    #################################

#################################


#]]]]]"""





if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):







