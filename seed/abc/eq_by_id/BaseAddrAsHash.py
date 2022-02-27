r'''
NOTE!!!:
    assert not issubclass(object, BaseAddrAsHash)
    assert not issubclass(ISingleton, BaseAddrAsHash)
    assert not isinstance(ISingleton, BaseAddrAsHash)
    so, when test issubclass/isinstance, should use AddrAsHash instead BaseAddrAsHash

seed.abc.eq_by_id.BaseAddrAsHash
py -m seed.abc.eq_by_id.BaseAddrAsHash
py -m nn_ns.app.debug_cmd   seed.abc.eq_by_id.BaseAddrAsHash

from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash, le_AddrAsHash
see:
    seed.abc.eq_by_id.BaseAddrAsHash
        from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash, le_AddrAsHash
    seed.abc.eq_by_id.AddrAsHash
        from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById
    seed.abc.eq_by_id.AddrAsHashWrapper
        from seed.abc.eq_by_id.AddrAsHashWrapper import AddrAsHashWrapper



>>> class _Tuple__EqById(tuple, BaseAddrAsHash): pass
Traceback (most recent call last):
    ...
NameError: name 'logic' is not defined

>>> x = BaseAddrAsHash()
>>> (__hash__ver_in_use__==1 and hash(x) == hash(id(x))) or (__hash__ver_in_use__==2 and hash(x) == (object.__hash__(x)))
True
>>> x == x
True
>>> BaseAddrAsHash() == BaseAddrAsHash()
False

>>> x = object()
>>> hash(x) == hash(id(x))
False
>>> hash(x) == id(x)
False
>>> object() == object()
False
>>> x == x
True

>>> class X:pass
>>> x = X()
>>> hash(x) == hash(id(x))
False
>>> hash(x) == id(x)
False
>>> X() == X()
False
>>> x == x
True
>>> x.a = 1
>>> x.a
1

# hash . hash === hash
#>>> id(x)
#>>> hash(id(x))
#>>> hash(x)
>>> id(x) == hash(id(x))
False
>>> id(x) == hash(x)
False
>>> hash(x) == hash(id(x))
False
>>> hash(id(x)) == hash(hash(id(x)))
True
>>> hash(x) == hash(hash(x))
True


#'''

__all__ = '''
    BaseAddrAsHash
    le_AddrAsHash
    '''.split()



#from abc import ABCMeta
import operator
import builtins
from seed.lang.basic_descriptors import BasicNonDataDescriptor4InstanceMethod as NonDataDescriptor4InstanceMethod
from seed.lang.apply_descriptor_protocol import is_descriptor, is_data_descriptor, is_non_data_descriptor
#from seed.abc.IDescriptor import NonDataDescriptor4InstanceMethod #try staticmethod but fail!!
#from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash
    #split out BaseAddrAsHash to avoid recur caused by seed.abc.abc.ABC(maybe abc__ver2) && NonDataDescriptor4InstanceMethod
#from seed.abc.abc import abstractmethod, override, ABC



def le_AddrAsHash(C, /):
    return (id(C.__hash__) in _ids4hash) and (id(C.__eq__) in _ids4eq) and (id(C.__ne__) in _ids4ne)
    #return (C.__hash__ is object.__hash__ or C.__hash__ is id or C.__hash__ is BaseAddrAsHash.__hash__) and (C.__eq__ is object.__eq__ or C.__eq__ is operator.is_ or C.__eq__ is BaseAddrAsHash.__eq__) and (C.__ne__ is object.__ne__ or C.__ne__ is operator.is_not or C.__ne__ is BaseAddrAsHash.__ne__)
if 0:
    # use:check_instance(AddrAsHash, cls) instead
    # use:check_subclass(AddrAsHash, cls) instead
    def check_le_AddrAsHash(cls, /):
        'use:check_instance(AddrAsHash, cls)'
        #check_instance(type, cls)
        if not isinstance(cls, type):raise TypeError
        if not le_AddrAsHash(cls):raise TypeError
    def check_type_le_AddrAsHash(obj, /):
        if not le_AddrAsHash(type(obj)):raise TypeError
    #######################
    #######################
    check_le_AddrAsHash
    check_type_le_AddrAsHash

__hash_descriptor_ver1__ = NonDataDescriptor4InstanceMethod(id)
__hash_descriptor_ver2__ = object.__hash__
if 1:
    assert is_non_data_descriptor(__hash_descriptor_ver1__)
    assert is_non_data_descriptor(__hash_descriptor_ver2__)
    type(__hash_descriptor_ver1__).__get__
    type(__hash_descriptor_ver2__).__get__

__hash__ver_in_use__ = 2
if 1:
    if __hash__ver_in_use__ == 1:
        __hash_descriptor_in_use__ = __hash_descriptor_ver1__
    elif __hash__ver_in_use__ == 2:
        __hash_descriptor_in_use__ = __hash_descriptor_ver2__
    else:
        raise logic-err

class BaseAddrAsHash:
    r'''
    #AddrAsHash should be named as EqById
    #   since ver2 donot use id as __hash__

    __eq__ is "is"
    __hash__ using id@ver1 or object.__hash__@ver2

    not allow overrided:
        __eq__
        __ne__
        __hash__
    #'''
    __slots__ = ()
    def __init_subclass__(cls, /,*args, **kwargs):
        if cls.__hash__ is not __class__.__hash__:raise logic-err
        if cls.__eq__ is not __class__.__eq__:raise logic-err
        if cls.__ne__ is not __class__.__ne__:raise logic-err
        #bug:super().__init_subclass__(cls, *args, **kwargs)
        super().__init_subclass__(*args, **kwargs)
    r'''
    def __hash__(sf, /):
        return id(sf)
    def __eq__(sf, ot, /):
        return sf is ot
    #'''
    __hash__ = builtins.id
    __eq__ = operator.is_
    __ne__ = operator.is_not
    assert __hash__ is id
    assert __eq__(__hash__, id)
    assert not __ne__(__hash__, id)
    #bug:NonDataDescriptor4InstanceMethod = staticmethod
    __hash__ = NonDataDescriptor4InstanceMethod(__hash__)
    __eq__ = NonDataDescriptor4InstanceMethod(__eq__)
    __ne__ = NonDataDescriptor4InstanceMethod(__ne__)
    __hash__ = object.__hash__
        #not id()!!! now!!!
    __hash__ = __hash_descriptor_in_use__

    if 0:
        def __hash__(*args, **kwargs):
            #hash(BaseAddrAsHash())
            #   TypeError: id() takes exactly one argument (0 given)
            print(args)
            print(kwargs)
            print(id)
            print(type(id))
            r'''
            (<__main__.BaseAddrAsHash object at 0xb69766d0>,)
            {}
            <built-in function id>
            <class 'builtin_function_or_method'>

            (<seed.abc.eq_by_id.BaseAddrAsHash object at 0xb6976788>,)
            <built-in function id>
            <class 'builtin_function_or_method'>
            #'''
            return id(*args, **kwargs)

def _to_ids(objs, /):
    return tuple(map(id, objs))
_ids4hash = _to_ids([object.__hash__, id, BaseAddrAsHash.__hash__])
_ids4eq = _to_ids([object.__eq__, operator.is_, BaseAddrAsHash.__eq__])
_ids4ne = _to_ids([object.__ne__, operator.is_not, BaseAddrAsHash.__ne__])

assert BaseAddrAsHash.__eq__ is operator.is_
assert BaseAddrAsHash.__ne__ is operator.is_not
if __hash__ver_in_use__ == 1:
    assert BaseAddrAsHash.__hash__ is id is builtins.id
    assert (lambda x: hash(x) == hash(id(x)))(BaseAddrAsHash())
elif __hash__ver_in_use__ == 2:
    assert BaseAddrAsHash.__hash__ is object.__hash__
    assert not (lambda x: hash(x) == hash(id(x)))(BaseAddrAsHash())
    assert (lambda x: hash(x) == hash(object.__hash__(x)))(BaseAddrAsHash())
    assert (lambda x: hash(x) == (object.__hash__(x)))(BaseAddrAsHash())
else:
    raise logic-err

assert BaseAddrAsHash() != BaseAddrAsHash()
assert hash is builtins.hash
BaseAddrAsHash.__hash__(BaseAddrAsHash())
hash(BaseAddrAsHash())
assert le_AddrAsHash(BaseAddrAsHash)



if __name__ == "__main__":
    assert not issubclass(object, BaseAddrAsHash)
    #from seed.abc.ISingleton import ISingleton
    #assert not issubclass(ISingleton, BaseAddrAsHash)
def _t():
    try:
        BaseAddrAsHash().x=1
    except AttributeError as e:
        assert repr(e) == '''AttributeError("'BaseAddrAsHash' object has no attribute 'x'")'''
    else:
        raise logic-err
_t()



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


