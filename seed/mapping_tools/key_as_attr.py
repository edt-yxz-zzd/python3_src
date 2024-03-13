

'''
key_as_attr/key_as_attr_ex
key_as_attr(mapping).xxx =[def]= mapping['xxx']
a wrapper
    wrap a mapping, so that we can assess via attr instead of key
    mapping or pseudo-mapping, if user override IKeyAsAttrBase:
        ___mapping_getitem___
        ___mapping_setitem___
        ___mapping_delitem___


example:
    >>> from seed.tiny import expectError
    >>> d = dict(abc='ABC', f='F')
    >>> rw = key_as_attr(d)
    >>> rw.abc
    'ABC'
    >>> rw.f
    'F'
    >>> assert not expectError(KeyError, lambda:rw.f)
    >>> assert expectError(KeyError, lambda:rw.a)
    >>> rw.a = 'A'
    >>> assert not expectError(KeyError, lambda:rw.a)
    >>> rw.a
    'A'
    >>> rw.f = 'F2'
    >>> rw.f
    'F2'
    >>> assert rw == KeyAsAttr({'abc': 'ABC', 'f': 'F2', 'a': 'A'})


    >>> r = key_as_attr(d, mutable=False)
    >>> r.a
    'A'
    >>> #assert expectError(KeyError, lambda:r.a = 'A2')
    >>> def assignR(): r.a = 'A2'
    >>> assert expectError(KeyError, assignR)
    >>> assert r == KeyAsAttr({'abc': 'ABC', 'f': 'F2', 'a': 'A'})


    >>> w = key_as_attr(d, readable=False)
    >>> assert expectError(KeyError, lambda:w.a)
    >>> w.f = 'F3'
    >>> assert w == KeyAsAttr({'abc': 'ABC', 'f': 'F3', 'a': 'A'})
    >>> del w.abc
    >>> assert w == KeyAsAttr({'f': 'F3', 'a': 'A'})

    >>> rs = key_as_attr_ex(d, has_delitem=False)
    >>> rs.f = 'F4'
    >>> rs.f
    'F4'
    >>> def delRS(): del rs.f
    >>> assert expectError(KeyError, delRS)

    >>> rw
    KeyAsAttrGNOSD({'f': 'F4', 'a': 'A'})
    >>> r
    KeyAsAttrG({'f': 'F4', 'a': 'A'})
    >>> w
    KeyAsAttrNOSD({'f': 'F4', 'a': 'A'})
    >>> rs
    KeyAsAttrGNOS({'f': 'F4', 'a': 'A'})

    >>> rnd = key_as_attr_ex(d, has_overwriteitem=False)
    >>> def assignRND(): rnd.f = 'F5'
    >>> assert expectError(KeyError, assignRND)
    >>> rnd.new = 'NEW'
    >>> rnd
    KeyAsAttrGND({'f': 'F4', 'a': 'A', 'new': 'NEW'})

'''
__all__ = '''
    key_as_attr
    key_as_attr_ex





IKeyAsAttrBase
    IKeyAsAttr__getitem
    IKeyAsAttr__newitem
        IKeyAsAttr__setitem
    IKeyAsAttr__overwriteitem
        IKeyAsAttr__setitem
    IKeyAsAttr__delitem

    KeyAsAttrConcreteBase
    '''.split()

r''' bug: python abc
    use "instance.__class__" instead of "type(instance)"

  File "key_as_attr.py", line 342, in _t
    assert rw == KeyAsAttr({'abc': 'ABC', 'f': 'F2', 'a': 'A'})
  File "key_as_attr.py", line 224, in __eq__
    if not isinstance(other, __class__):return NotImplemented
  File "C:\Python36\lib\abc.py", line 181, in __instancecheck__
    subclass = instance.__class__

'''



'''
IKeyAsAttrBase
    IKeyAsAttr__getitem
        ReadableKeyAsAttr
        IKeyAsAttr
    IMutableKeyAsAttr
        MutableKeyAsAttr
        IKeyAsAttr
    IKeyAsAttr
        KeyAsAttr
'''



from itertools import compress
from seed.abc.abc__ver1 import abstractmethod, ABC
from seed.abc.IReprHelper import IReprHelper

def key_as_attr(mapping, *, mutable=True, readable=True):
    'use the keys of input mapping as the attrs of output obj'
    #T = __get_KeyAsAttr(mutable, readable)
    #return T(mapping)
    has_getitem = bool(readable)
    has_newitem = has_overwriteitem = has_delitem = bool(mutable)
    return key_as_attr_ex(mapping
        , has_getitem=has_getitem
        , has_newitem=has_newitem
        , has_overwriteitem=has_overwriteitem
        , has_delitem=has_delitem
        )

def key_as_attr_ex(mapping, *
        , has_getitem=True
        , has_newitem=True
        , has_overwriteitem=True
        , has_delitem=True):
    key = (has_getitem, has_newitem, has_overwriteitem, has_delitem)
    T = __get_KeyAsAttr(has_getitem, has_newitem, has_overwriteitem, has_delitem)
    return T(mapping)












def final(f): return f
def to_be_override(f): return f
def to_be_override_in_concrete_subclass(f): return f

def the_mapping_getitem(self, name):
    # used in __getattribute__
    #raise KeyError
    mapping = type(self).___get_mapping___(self)
    return mapping[name]
def the_mapping_setitem(self, name, obj):
    # used in __setattr__
    #raise KeyError
    mapping = type(self).___get_mapping___(self)
    mapping[name] = obj

def the_mapping_newitem(self, name, obj):
    # used in __setattr__
    #raise KeyError
    mapping = type(self).___get_mapping___(self)
    if name in mapping:
        # not new key
        raise KeyError('not a new key: {name!r}')
    mapping[name] = obj
def the_mapping_overwriteitem(self, name, obj):
    # used in __setattr__
    #raise KeyError
    mapping = type(self).___get_mapping___(self)
    if name not in mapping:
        # not existed key
        raise KeyError('not a existed key: {name!r}')
    mapping[name] = obj

def the_mapping_delitem(self, name):
    # used in __delattr__
    #raise KeyError
    mapping = type(self).___get_mapping___(self)
    del mapping[name]



class IKeyAsAttrBase(IReprHelper):
    '''a helper class wrapping mapping so that we can use attr as key

IKeyAsAttrBase is neither readable nor writable
raise KeyError instead of AttributeError
abstract: `__slots__, `___please_set_slots_in_concrete_subclass___
wrapped mapping may be pseudo-mapping whose behavior was defined by:
    ___mapping_getitem___
    ___mapping_setitem___
    ___mapping_delitem___



abstract subclass should:
    __slots__ = ()
concrete subclass should:
    * use default ___set_mapping___/___get_mapping___
        1) let self assignable at mapping_attrname:
            # mapping_attrname maybe:
            #   IKeyAsAttrBase.___get_mapping_attrname___()
            __slots__ = (mapping_attrname,)
            __slots__ = '__dict__'
            and so on
        2) override ___get_mapping_attrname___
    * or: override ___set_mapping___, ___get_mapping___ both
'''
    # concrete subclass should override __slots__
    # __slots__ = IKeyAsAttrBase.___get_mapping_attrname___()
    __slots__ = ()
    @to_be_override_in_concrete_subclass
    @abstractmethod
    def ___please_set_slots_in_concrete_subclass___(self):
        # do nothing!
        #   but please check that __slots__ was set
        pass

    # maybe override by subclass
    # used in ___set_mapping___/___get_mapping___ only
    @classmethod
    @to_be_override
    def ___get_mapping_attrname___(cls):
        # which attrname refer to the underlying mapping?
        # mapping = type(self).___get_mapping___(self)
        return '_KeyAsAttrBase__mapping'

    # handle underlying mapping, __getitem__/__setitem__/__delitem__
    @to_be_override
    def ___mapping_getitem___(self, name):
        # __getitem__
        # used in __getattribute__
        # see: the_mapping_getitem
        raise KeyError
    @to_be_override
    def ___mapping_setitem___(self, name, obj):
        # __setitem__
        # used in __setattr__
        # see: the_mapping_setitem
        raise KeyError
    @to_be_override
    def ___mapping_delitem___(self, name):
        # __delitem__
        # used in __delattr__
        # see: the_mapping_delitem
        raise KeyError



    #################### get/set underlying mapping of self

    @final
    def ___set_mapping___(self, mapping):
        # used in __init__
        mapping_attrname = type(self).___get_mapping_attrname___()
        object.__setattr__(self, mapping_attrname, mapping)
    @final
    def ___get_mapping___(self):
        # used everywhere
        mapping_attrname = type(self).___get_mapping_attrname___()
        return object.__getattribute__(self, mapping_attrname)


    ####################

    def __init__(self, mapping):
        #self.__mapping = mapping
        type(self).___set_mapping___(self, mapping)
    def __getattribute__(self, name):
        return type(self).___mapping_getitem___(self, name)
    def __setattr__(self, name, obj):
        type(self).___mapping_setitem___(self, name, obj)
    def __delattr__(self, name):
        type(self).___mapping_delitem___(self, name)

    def ___get_args_kwargs___(self):
        # __get_state__??
        mapping = type(self).___get_mapping___(self)
        return ((mapping,), {})
    def __eq__(self, other):
        #if not isinstance(other, __class__):return NotImplemented
        if not issubclass(type(other), __class__):return NotImplemented
        mappingS = type(self).___get_mapping___(self)
        mappingO = type(other).___get_mapping___(other)
        return mappingS == mappingO

############## abstract mixin subclass

# concrete subclass should override __slots__
# __slots__ = IKeyAsAttrBase.___get_mapping_attrname___()
class IKeyAsAttr__getitem(IKeyAsAttrBase):
    __slots__ = ()
    ___mapping_getitem___ = the_mapping_getitem
class IKeyAsAttr__newitem(IKeyAsAttrBase):
    __slots__ = ()
    ___mapping_setitem___ = the_mapping_newitem
class IKeyAsAttr__overwriteitem(IKeyAsAttrBase):
    __slots__ = ()
    ___mapping_setitem___ = the_mapping_overwriteitem
class IKeyAsAttr__setitem(IKeyAsAttr__overwriteitem, IKeyAsAttr__newitem):
    __slots__ = ()
    ___mapping_setitem___ = the_mapping_setitem
class IKeyAsAttr__delitem(IKeyAsAttrBase):
    __slots__ = ()
    ___mapping_delitem___ = the_mapping_delitem
class IMutableKeyAsAttr(IKeyAsAttr__delitem, IKeyAsAttr__setitem):
    __slots__ = ()
    ___mapping_setitem___ = the_mapping_setitem
    ___mapping_delitem___ = the_mapping_delitem
class IKeyAsAttr(IMutableKeyAsAttr, IKeyAsAttr__getitem):
    # abstract: `__slots__, `___please_set_slots_in_concrete_subclass___
    __slots__ = ()
    ___mapping_getitem___ = the_mapping_getitem
    ___mapping_setitem___ = the_mapping_setitem
    ___mapping_delitem___ = the_mapping_delitem






############## concrete subclass

class KeyAsAttrConcreteBase(IKeyAsAttrBase):
    __slots__ = IKeyAsAttrBase.___get_mapping_attrname___()
    def ___please_set_slots_in_concrete_subclass___(self):pass
class ReadableKeyAsAttr(KeyAsAttrConcreteBase, IKeyAsAttr__getitem):
    __slots__ = ()
class UpdatableKeyAsAttr(KeyAsAttrConcreteBase, IKeyAsAttr__setitem):
    __slots__ = ()
class DeletableKeyAsAttr(KeyAsAttrConcreteBase, IKeyAsAttr__delitem):
    __slots__ = ()
class MutableKeyAsAttr(KeyAsAttrConcreteBase, IMutableKeyAsAttr):
    __slots__ = ()
class KeyAsAttr(KeyAsAttrConcreteBase, IKeyAsAttr):
    # not subclass of ReadableKeyAsAttr/MutableKeyAsAttr
    __slots__ = ()


'''
__mutable_readable2type = (KeyAsAttrConcreteBase, ReadableKeyAsAttr
                        , MutableKeyAsAttr, KeyAsAttr)

def __get_KeyAsAttr(mutable, readable):
    i = (bool(mutable) << 1) | bool(readable)
    T = __mutable_readable2type[i]
    return T
'''
__key2type = {}
def __get_KeyAsAttr(has_getitem, has_newitem, has_overwriteitem, has_delitem):
    key = (has_getitem, has_newitem, has_overwriteitem, has_delitem)
    key = tuple(map(bool, key))

    mayT = __key2type.get(key)
    if mayT is not None:
        T = mayT
        return T
    T = __get_KeyAsAttr__bare(key)
    __key2type[key] = T
    return T

def __get_KeyAsAttr__bare(key):
    (has_getitem, has_newitem, has_overwriteitem, has_delitem) = key
    has_setitem = has_newitem and has_overwriteitem
    seletor = (has_getitem, has_newitem, has_overwriteitem, has_setitem, has_delitem)
    Ts = \
            [ IKeyAsAttr__getitem
            , IKeyAsAttr__newitem
            , IKeyAsAttr__overwriteitem
            , IKeyAsAttr__setitem
            , IKeyAsAttr__delitem
            ]
    Flags = 'GNOSD'

    #bug: [*Ts] = compress(Ts, key)
    assert len(Ts) == len(seletor) == len(Flags)
    [*Ts] = compress(Ts, seletor)
    [*Flags] = compress(Flags, seletor)
    Ts.reverse()
    #Flags.reverse()
    Flags = ''.join(Flags)
    class IKeyAsAttr(*Ts, IKeyAsAttrBase):
        __slots__ = ()
    class KeyAsAttr(KeyAsAttrConcreteBase, IKeyAsAttr):
        # not subclass of ReadableKeyAsAttr/MutableKeyAsAttr
        __slots__ = ()
    KeyAsAttr.__name__ += Flags
    return KeyAsAttr







def _t():
    from seed.tiny import expectError
    d = dict(abc='ABC', f='F')
    rw = key_as_attr(d)
    assert rw.abc == 'ABC'
    assert rw.f == 'F'
    assert not expectError(BaseException, lambda:rw.f)
    assert expectError(KeyError, lambda:rw.a)
    rw.a = 'A'
    assert not expectError(KeyError, lambda:rw.a)
    assert rw.a == 'A'
    rw.f = 'F2'
    assert rw.f == 'F2'
    assert rw == KeyAsAttr({'abc': 'ABC', 'f': 'F2', 'a': 'A'})
    r = key_as_attr(d, mutable=False)
    assert r.a == 'A'
    #assert expectError(KeyError, lambda:r.a = 'A2')
    def assignR(): r.a = 'A2'
    assert expectError(KeyError, assignR)
    assert r == KeyAsAttr({'abc': 'ABC', 'f': 'F2', 'a': 'A'})
    w = key_as_attr(d, readable=False)
    assert expectError(KeyError, lambda:w.a)
    w.f = 'F3'
    assert w == KeyAsAttr({'abc': 'ABC', 'f': 'F3', 'a': 'A'})
    del w.abc
    assert w == KeyAsAttr({'f': 'F3', 'a': 'A'})
_t()


from seed.mapping_tools.key_as_attr import key_as_attr
from seed.mapping_tools.key_as_attr import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()




