r'''
NOTE!!!:
    assert not issubclass(object, BaseAddrAsHash)
    assert not issubclass(ISingleton, BaseAddrAsHash)
    assert not isinstance(ISingleton, BaseAddrAsHash)
    so, when test issubclass/isinstance, should use AddrAsHash instead BaseAddrAsHash

seed.abc.eq_by_id.AddrAsHash
py -m seed.abc.eq_by_id.AddrAsHash
py -m nn_ns.app.debug_cmd   seed.abc.eq_by_id.AddrAsHash

from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash, le_AddrAsHash
from seed.abc.eq_by_id.AddrAsHash import BaseAddrAsHash, le_AddrAsHash, AddrAsHash as EqById
from seed.abc.eq_by_id.AddrAsHash import IAddrAsHash__with_value, value_hash, value_eq, Mixin4AddrAsHash__with_value
see:
    seed.abc.eq_by_id.BaseAddrAsHash
        from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash, le_AddrAsHash
    seed.abc.eq_by_id.AddrAsHash
        from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById
    seed.abc.eq_by_id.AddrAsHashWrapper
        from seed.abc.eq_by_id.AddrAsHashWrapper import AddrAsHashWrapper




>>> class _Tuple__EqById(tuple, EqById): pass
Traceback (most recent call last):
    ...
NameError: name 'logic' is not defined



#'''

__all__ = '''
    BaseAddrAsHash
        le_AddrAsHash
    AddrAsHash
        EqById
    IAddrAsHash__with_value
        value_hash
        value_eq
        Mixin4AddrAsHash__with_value
    '''.split()



#from abc import ABCMeta
import operator
import builtins
#from seed.lang.basic_descriptors import BasicNonDataDescriptor4InstanceMethod as NonDataDescriptor4InstanceMethod
#from seed.abc.IDescriptor import NonDataDescriptor4InstanceMethod #try staticmethod but fail!!
from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash, le_AddrAsHash
    #split out BaseAddrAsHash to avoid recur caused by seed.abc.abc.ABC(maybe abc__ver2) && NonDataDescriptor4InstanceMethod
from seed.abc.abc__ver1 import abstractmethod, override, ABC



le_AddrAsHash
class AddrAsHash(BaseAddrAsHash, ABC):
    #   .__subclasshook__()/.register()
    #       class AddrAsHash(object):
    #
    r'''
    ######################
    #AddrAsHash should be named as EqById
    #   since ver2 donot use id as __hash__

    ######################
    BaseAddrAsHash+__subclasshook__
        '__eq__ is "is"; with .__subclasshook__()/.register()'

    ######################
    #AddrAsHash should be named as EqById
    #   since ver2 donot use id as __hash__

    diff AddrAsHashWrapper vs AddrAsHash:
        AddrAsHashWrapper
            sf.__hash__ be id(sf.the_value_obj/the_wrapped_obj)
                shouldnot be object.__hash__(sf.the_value_obj/the_wrapped_obj)
                    to avoid collide with the_wrapped_obj
        AddrAsHash
            sf.__hash__ be id(sf) or object.__hash__(sf)
    ######################

    ######################
    __subclasshook__/register
    __eq__ is "is"
    __hash__ using id@ver1 or object.__hash__@ver2

    not allow overrided:
        __eq__
        __ne__
        __hash__
    ######################
    ######################
    #'''
    __slots__ = ()
    @classmethod
    @override
    def __subclasshook__(cls, C, /):
        # ABCMeta::__subclasshook__
        if cls is __class__:
            #assert isinstance(C, type)
            #if any("__iter__" in B.__dict__ for B in C.__mro__):
            if le_AddrAsHash(C):
            #if (C.__hash__ is object.__hash__ or C.__hash__ is id or C.__hash__ is __class__.__hash__) and (C.__eq__ is object.__eq__ or C.__eq__ is __class__.__eq__) and (C.__ne__ is object.__ne__ or C.__ne__ is __class__.__ne__):
                return True
        return NotImplemented
assert le_AddrAsHash(BaseAddrAsHash)
assert le_AddrAsHash(AddrAsHash)

AddrAsHash.register(BaseAddrAsHash)
assert issubclass(BaseAddrAsHash, AddrAsHash)
assert issubclass(AddrAsHash, BaseAddrAsHash)

EqById = AddrAsHash
assert issubclass(type, EqById)
assert isinstance(type, EqById)
assert issubclass(EqById, EqById)
assert isinstance(EqById, EqById)
if __name__ == "__main__":
    from seed.abc.ISingleton import ISingleton
    assert issubclass(ISingleton, BaseAddrAsHash)
    assert issubclass(ISingleton, EqById)
    assert isinstance(ISingleton, EqById)
    assert not isinstance(ISingleton, BaseAddrAsHash)
def _t():
    try:
        AddrAsHash().x=1
    except AttributeError as e:
        assert repr(e) == '''AttributeError("'AddrAsHash' object has no attribute 'x'")'''
    else:
        raise logic-err
_t()



def value_hash(x, /):
    return type(x).___value_hash___(x)
def value_eq(x, y, /):
    r = type(x).___value_eq___(x, y)
    if r is NotImplemented:
        r = type(y).___value_eq___(y, x)
    if r is NotImplemented: raise TypeError
    if type(r) is not bool: raise TypeError
    return r


class IAddrAsHash__with_value(AddrAsHash):
    __slots__ = ()

    @abstractmethod
    def ___value_hash___(sf, /):
        raise NotImplementedError
        return id(sf)
    @abstractmethod
    def ___value_eq___(sf, ot, /):
        raise NotImplementedError
        return sf is ot

class Mixin4AddrAsHash__with_value(IAddrAsHash__with_value):
    __slots__ = ()

    @override
    def ___value_hash___(sf, /):
        raise NotImplementedError
        return id(sf)
    @override
    def ___value_eq___(sf, ot, /):
        raise NotImplementedError
        return sf is ot



class Tuple__EqById(IAddrAsHash__with_value, tuple):
    __slots__ = ()
    #@override
    ___value_hash___ = tuple.__hash__
    #@override
    ___value_eq___ = tuple.__eq__
    pass
Tuple__EqById()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


