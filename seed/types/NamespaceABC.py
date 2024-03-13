
r'''
>>> class S(StaticImmutableNamespaceBase, ordered_user_attr_seq='ab'):pass
>>> ns = S(b=-1, a=2)
>>> del ns.a #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError
>>> ns.c = 2 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError
>>> ns.a = 3 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError
>>> ns.a
2
>>> ns
S(a = 2, b = -1)
>>> type(S.__hash__(ns)) is int
True
>>> hash(ns) == object.__getattribute__(ns, '_hash_value_')
True



>>> ns = DynamicImmutableNamespace(b=-1, a=2)
>>> del ns.a #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError
>>> ns.c = 2 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError
>>> ns.a = 3 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError
>>> ns.a
2
>>> ns
DynamicImmutableNamespace(a = 2, b = -1)
>>> type(DynamicImmutableNamespace.__hash__(ns)) is int
True
>>> hash(ns) == object.__getattribute__(ns, '_hash_value_')
True



#'''

__all__ = '''
    NamespaceABC
        ImmutableNamespaceABC
            StaticImmutableNamespaceABC
        UserCachedNamespaceABC
            SetUserDictOnceNamespaceABC
        ImplDictNamespaceABC
            ImplCachedNamespaceABC
                SetImplDictOnceNamespaceABC

        StaticImmutableNamespaceBase
        DynamicImmutableNamespace
    '''.split()

r"""
class NamespaceABC(ABC):
class ImmutableNamespaceABC(NamespaceABC):
class StaticImmutableNamespaceABC(ImmutableNamespaceABC):
class UserCachedNamespaceABC(NamespaceABC):
class ImplDictNamespaceABC(NamespaceABC):
class ImplCachedNamespaceABC(ImplDictNamespaceABC):
class SetUserDictOnceNamespaceABC(UserCachedNamespaceABC):
class SetImplDictOnceNamespaceABC(ImplCachedNamespaceABC):

class StaticImmutableNamespaceBase(StaticImmutableNamespaceABC, _ImmutableNamespaceBase):
class DynamicImmutableNamespace(_ImmutableNamespaceBase):
#"""



#from collections.abc import Set, Sequence, Mapping
from types import MappingProxyType
import inspect # isabstract
from seed.types.empty_containers import empty_mapping
#from seed.types.NamedReadOnlyProperty import NamedReadOnlyProperty
from seed.verify.common_verify import is_Sequence
from seed.tiny import null_iter, print_err
from seed.helper.repr_input import repr_helper_ex
#from seed.abc import abstractmethod, ABC, final, override
from seed.abc.abc__ver1 import abstractmethod, override, final, ABC #, ABC__no_slots
from seed.decorators.__special_method__ import (
    __static_method__
    ,__class_method__
    ,__instance_method__
    )

class NamespaceABC(ABC):
    '''
two dicts:
    user_dict
        user_attrs + user_cached_attrs
    impl_dict
        impl_attrs:
            hash_value
            user_cached_attr2eval
            impl_cached_attr2eval
            ...


primekey_attrs
user_attrs
    primekey_attrs <= user_attrs <= user_dict.keys()
        user_dict.keys() may contains user_cached_attrs
    ordered_user_attrs:
        used in __repr__
    primekey_attrs:
        used in __hash__/__eq__/__lt__


abstract_methods:
    `__get_num_primekey_attrs__
    `__get_readonly_user_dict__
    `__iter_ordered_primekey_attrs__
    `__iter_ordered_user_attrs__
    `__iter_unstable_primekey_attrs__
    `__iter_unstable_user_attrs__
    `__make_ordered_primekey_attr_seq__
    `__make_ordered_user_attr_seq__
'''
    __slots__ = ()

    @__instance_method__
    @abstractmethod
    def __make_ordered_user_attr_seq__(self):
        return tuple(type(self).__iter_ordered_user_attrs__(self))
    @__instance_method__
    @abstractmethod
    def __iter_ordered_user_attrs__(self):
        raise NotImplementedError
    @__instance_method__
    @abstractmethod
    def __iter_unstable_user_attrs__(self):
        return type(self).__iter_ordered_user_attrs__(self)
        raise NotImplementedError

    @__instance_method__
    @abstractmethod
    def __get_num_primekey_attrs__(self):
        raise NotImplementedError
    @__instance_method__
    @abstractmethod
    def __make_ordered_primekey_attr_seq__(self):
        return tuple(type(self).__iter_ordered_primekey_attrs__(self))
        raise NotImplementedError
    @__instance_method__
    @abstractmethod
    def __iter_ordered_primekey_attrs__(self):
        raise NotImplementedError
    @__instance_method__
    @abstractmethod
    def __iter_unstable_primekey_attrs__(self):
        return type(self).__iter_ordered_primekey_attrs__(self)
        raise NotImplementedError
    @__instance_method__
    def __iter_ordered_primekey_items__(self):
        for attr in type(self).__iter_ordered_primekey_attrs__(self):
            yield attr, getattr(self, attr)
        #raise NotImplementedError


    @__instance_method__
    @abstractmethod
    def __get_readonly_user_dict__(self):
        raise AttributeError
        raise NotImplementedError

    #@__instance_method__
    def __getattribute__(self, attr):
        cls = type(self)
        d = cls.__get_readonly_user_dict__(self)
        try:
            return d[attr]
        except KeyError:
            #print_err(f'KeyError: {attr!r}')
            #print_err(f'user_dict = {d!r}')
            pass

        if attr == '__dict__':
            # user_dict as __dict__ for user!
            return d
            return MappingProxyType(d)

        return super(__class__, cls).__getattribute__(self, attr)

    @__instance_method__
    def __dir__(self):
        cls = type(self)
        return list(cls.__iter_unstable_user_attrs__(self))
    #@__instance_method__
    def __setattr__(self, attr, obj):
        raise AttributeError(attr)
    #@__instance_method__
    def __delattr__(self, attr):
        raise AttributeError(attr)




    #@__instance_method__
    def __repr__(self):
        cls = type(self)
        ordered_user_attrs = cls.__iter_ordered_user_attrs__(self)
        return repr_helper_ex(self
            , (), ordered_user_attrs, {}, ordered_attrs_only=True)

    @__instance_method__
    def __ne__(self, other):
        return not (self == other)
    @__instance_method__
    def __eq__(self, other):
        if self is other: return True
        #if not isinstance(other, __class__): return NotImplemented

        cls = type(self)
        ocls = type(other)
        if cls is not ocls: return False

        gnum = cls.__get_num_primekey_attrs__
        if not (gnum(self) == gnum(other) and hash(self) == hash(other)):
            return False

        gseq = cls.__make_ordered_primekey_attr_seq__
        ordered_primekey_attr_seq = gseq(self)
        if ordered_primekey_attr_seq != gseq(other): return False

        #bug: gattr = cls.__getattribute__
        #       NOTE: __getattr__
        return all(getattr(self, attr) == getattr(other, attr)
                    for attr in ordered_primekey_attr_seq)

    @__instance_method__
    def __lt__(self, other):
        #if not isinstance(other, __class__): return NotImplemented
        if self is other: return False
        if type(self) is not type(other): raise TypeError #NotImplementedError
        cls = type(self)
        iitems = cls.__iter_ordered_primekey_items__
        for a, b in zip(iitems(self), iitems(other)):
            if a == b: continue
            return a < b
        return False
    @__instance_method__
    def __le__(self, other):
        if type(self) is not type(other): raise TypeError #NotImplementedError
        return not (other < self)
    @__instance_method__
    def __gt__(self, other):
        return not (self <= other)
    @__instance_method__
    def __ge__(self, other):
        return not (self < other)




    @__instance_method__
    @final
    def __set_attr_once__(self, fget, fset, attr, obj):
        try:
            fget(self, attr)
        except AttributeError:
            # not set yet
            pass
        else:
            # already set
            raise AttributeError
        fset(self, attr, obj)
        if fget(self, attr) is not obj: raise logic-error



    @__instance_method__
    @final
    def __named_set_once__(self, fget, fset, obj):
        try:
            fget(self)
        except AttributeError:
            # not set yet
            pass
        else:
            # already set
            raise AttributeError
        fset(self, obj)
        if fget(self) is not obj: raise logic-error

class ImmutableNamespaceABC(NamespaceABC):
    '''
hash

abstract_methods:
    `__get_hash_value__
    `__get_num_primekey_attrs__
    `__get_readonly_user_dict__
    `__iter_ordered_primekey_attrs__
    `__iter_ordered_user_attrs__
    `__iter_unstable_primekey_attrs__
    `__iter_unstable_user_attrs__
    `__make_ordered_primekey_attr_seq__
    `__make_ordered_user_attr_seq__
    `__set_hash_value_once__
'''
    __slots__ = ()

    @__instance_method__
    @abstractmethod
    def __get_hash_value__(self):
        raise AttributeError
        raise NotImplementedError
    @__instance_method__
    @abstractmethod
    def __set_hash_value_once__(self, hash_value):
        raise AttributeError
        raise NotImplementedError



    #@__instance_method__
    @final
    def __hash__(self):
        cls = type(self)
        try:
            return cls.__get_hash_value__(self)
        except AttributeError:
            hash_value = cls.__calc_hash_value__(self)
            #self.__hash_value = hash_value
            cls.__set_hash_value_once__(self, hash_value)
        return cls.__get_hash_value__(self)

    @__instance_method__
    @final
    def __calc_hash_value__(self):
        cls = type(self)
        iitems = cls.__iter_ordered_primekey_items__(self)
        repr_data = id(cls), tuple(iitems)
        return hash(repr_data)

class StaticImmutableNamespaceABC(ImmutableNamespaceABC):
    '''
hash
static:
    ordered_primekey_attr_seq
    ordered_user_attr_seq

abstract_methods:
    `__get_hash_value__
    `__get_readonly_user_dict__
    `__set_hash_value_once__
    `__static_get_readonly_ordered_primekey_attr_seq__
    `__static_get_readonly_ordered_user_attr_seq__
'''
    __slots__ = ()

    @__class_method__
    @abstractmethod
    def __static_get_readonly_ordered_user_attr_seq__(cls):
        raise AttributeError
    @__class_method__
    @abstractmethod
    def __static_get_readonly_ordered_primekey_attr_seq__(cls):
        raise AttributeError

    @__instance_method__
    @override
    def __make_ordered_user_attr_seq__(self):
        return type(self).__static_get_readonly_ordered_user_attr_seq__()
    @__instance_method__
    @override
    def __iter_ordered_user_attrs__(self):
        return iter(type(self).__static_get_readonly_ordered_user_attr_seq__())
    @__instance_method__
    @override
    def __iter_unstable_user_attrs__(self):
        return type(self).__iter_ordered_user_attrs__(self)

    @__instance_method__
    @override
    def __get_num_primekey_attrs__(self):
        return len(type(self).__static_get_readonly_ordered_primekey_attr_seq__())
    @__instance_method__
    @override
    def __make_ordered_primekey_attr_seq__(self):
        return type(self).__static_get_readonly_ordered_primekey_attr_seq__()
    @__instance_method__
    @override
    def __iter_ordered_primekey_attrs__(self):
        return iter(type(self).__static_get_readonly_ordered_primekey_attr_seq__())
    @__instance_method__
    @override
    def __iter_unstable_primekey_attrs__(self):
        return type(self).__iter_ordered_primekey_attrs__(self)






class UserCachedNamespaceABC(NamespaceABC):
    '''
user_cached_attr2eval :: Map attr (instance->value)

abstract_methods:
    `__get_num_primekey_attrs__
    `__get_readonly_user_dict__
    `__get_user_cached_attr2eval__
    `__iter_ordered_primekey_attrs__
    `__iter_ordered_user_attrs__
    `__iter_unstable_primekey_attrs__
    `__iter_unstable_user_attrs__
    `__make_ordered_primekey_attr_seq__
    `__make_ordered_user_attr_seq__
    `__set_user_cached_value_once__
'''
    __slots__ = ()

    @__instance_method__
    @abstractmethod
    def __get_user_cached_attr2eval__(self):
        raise AttributeError
    @__instance_method__
    @abstractmethod
    def __set_user_cached_value_once__(self, attr, value):
        raise AttributeError


    """
    @__instance_method__
    @abstractmethod
    def __set_user_cached_attr2eval_once__(self, user_cached_attr2eval):
        raise AttributeError

    @__static_method__
    def __new__(cls, *, user_dict, user_cached_attr2eval, **kwargs):
        self = super(__class__, cls).__new__(cls, user_dict=user_dict, **kwargs)
        cls.__set_user_cached_attr2eval_once__(self, user_cached_attr2eval)
        return self
    """

    #@__instance_method__
    def __getattribute__(self, attr):
        cls = type(self)
        get = super(__class__, cls).__getattribute__
        try:
            return get(self, attr)
        except AttributeError:
            user_cached_attr2eval = cls.__get_user_cached_attr2eval__(self)
            try:
                calc = user_cached_attr2eval[attr]
            except KeyError:
                pass # to raise
            else:
                value = calc(self)
                cls.__set_user_cached_value_once__(self, attr, value)
                return get(self, attr)
            raise







class ImplDictNamespaceABC(NamespaceABC):
    __slots__ = ()

    @__instance_method__
    @abstractmethod
    def __get_impl_cached_attr__(self, attr):
        raise AttributeError
class ImplCachedNamespaceABC(ImplDictNamespaceABC):
    '''
impl_cached_attr2eval :: Map attr (instance->value)

abstract_methods:
    `__get_impl_cached_attr2eval__
    `__get_impl_cached_attr_directly__
    `__get_num_primekey_attrs__
    `__get_readonly_user_dict__
    `__iter_ordered_primekey_attrs__
    `__iter_ordered_user_attrs__
    `__iter_unstable_primekey_attrs__
    `__iter_unstable_user_attrs__
    `__make_ordered_primekey_attr_seq__
    `__make_ordered_user_attr_seq__
    `__set_impl_cached_value_once__
'''
    __slots__ = ()

    @__instance_method__
    @abstractmethod
    def __get_impl_cached_attr2eval__(self):
        raise AttributeError
    @__instance_method__
    @abstractmethod
    def __set_impl_cached_value_once__(self, attr, value):
        raise AttributeError
    @__instance_method__
    @abstractmethod
    def __get_impl_cached_attr_directly__(self, attr):
        raise AttributeError

    @__instance_method__
    @final
    @override
    def __get_impl_cached_attr__(self, attr):
        cls = type(self)
        get = cls.__get_impl_cached_attr_directly__
        try:
            return get(self, attr)
        except AttributeError:
            impl_cached_attr2eval = cls.__get_impl_cached_attr2eval__(self)
            try:
                calc = impl_cached_attr2eval[attr]
            except KeyError:
                pass # to raise
            else:
                value = calc(self)
                cls.__set_impl_cached_value_once__(self, attr, value)
                return get(self, attr)
            raise



class SetUserDictOnceNamespaceABC(UserCachedNamespaceABC):
    '''
abstract_methods:
    `__get_growing_user_dict__
    `__get_num_primekey_attrs__
    `__get_readonly_user_dict__
    `__get_user_cached_attr2eval__
    `__iter_ordered_primekey_attrs__
    `__iter_ordered_user_attrs__
    `__iter_unstable_primekey_attrs__
    `__iter_unstable_user_attrs__
    `__make_ordered_primekey_attr_seq__
    `__make_ordered_user_attr_seq__
    `__set_user_dict_once__
'''
    __slots__ = ()

    @__instance_method__
    @abstractmethod
    def __set_user_dict_once__(self, kwargs):
        raise AttributeError
    @__instance_method__
    @abstractmethod
    def __get_growing_user_dict__(self, kwargs):
        raise AttributeError

    @__static_method__
    def __new__(cls, *, user_dict, **kwargs):
        self = super(__class__, cls).__new__(cls, **kwargs)
        cls.__set_user_dict_once__(self, user_dict)
        return self

    @__instance_method__
    @override
    def __set_user_cached_value_once__(self, attr, value):
        cls = type(self)
        d = cls.__get_growing_user_dict__(self)

        if attr in d:
            raise logic-error-('already set')
        d[attr] = value







class SetImplDictOnceNamespaceABC(ImplCachedNamespaceABC):
    '''
abstract_methods:
    `__get_growing_impl_dict__
    `__get_impl_cached_attr2eval__
    `__get_num_primekey_attrs__
    `__get_readonly_impl_dict__
    `__get_readonly_user_dict__
    `__iter_ordered_primekey_attrs__
    `__iter_ordered_user_attrs__
    `__iter_unstable_primekey_attrs__
    `__iter_unstable_user_attrs__
    `__make_ordered_primekey_attr_seq__
    `__make_ordered_user_attr_seq__
    `__set_impl_dict_once__
'''
    __slots__ = ()

    @__instance_method__
    @abstractmethod
    def __set_impl_dict_once__(self, impl_dict):
        raise AttributeError
    @__instance_method__
    @abstractmethod
    def __get_growing_impl_dict__(self):
        raise AttributeError
    @__instance_method__
    @abstractmethod
    def __get_readonly_impl_dict__(self):
        raise AttributeError

    @__static_method__
    def __new__(cls, *, impl_dict, **kwargs):
        self = super(__class__, cls).__new__(cls, **kwargs)
        cls.__set_impl_dict_once__(self, impl_dict)
        return self

    @__instance_method__
    @override
    def __get_impl_cached_attr_directly__(self, attr):
        cls = type(self)
        d = cls.__get_readonly_impl_dict__(self)
        try:
            return d[attr]
        except KeyError:
            raise AttributeError(attr)

    @__instance_method__
    @override
    def __set_impl_cached_value_once__(self, attr, value):
        cls = type(self)
        d = cls.__get_growing_impl_dict__(self)
        if attr in d:
            raise logic-error
        d[attr] = value






class _ImmutableNamespaceBase(
    ImmutableNamespaceABC
    ,SetUserDictOnceNamespaceABC
    ):
    '''
overrided abstract_methods:
    `__get_growing_user_dict__
    `__get_hash_value__
    `__get_readonly_user_dict__
    `__get_user_cached_attr2eval__
    `__set_hash_value_once__
    `__set_user_dict_once__
'''
    __slots__ = (
        '_user_dict_'
        ,'_hash_value_'
        )
    @__instance_method__
    @override
    def __get_growing_user_dict__(self):
        return type(self).__get_readonly_user_dict__(self)
    @__instance_method__
    @override
    def __get_hash_value__(self):
        return object.__getattribute__(self, '_hash_value_')

    @__instance_method__
    @override
    def __get_readonly_user_dict__(self):
        return object.__getattribute__(self, '_user_dict_')
    @__instance_method__
    @override
    def __get_user_cached_attr2eval__(self):
        return empty_mapping

    @__instance_method__
    @override
    def __set_hash_value_once__(self, hash_value):
        cls = type(self)
        fset = object.__setattr__
        fget = object.__getattribute__
        attr = '_hash_value_'
        cls.__set_attr_once__(self, fget, fset, attr, hash_value)

    @__instance_method__
    @override
    def __set_user_dict_once__(self, user_dict):
        cls = type(self)
        fset = object.__setattr__
        fget = object.__getattribute__
        attr = '_user_dict_'
        cls.__set_attr_once__(self, fget, fset, attr, user_dict)


class StaticImmutableNamespaceBase(
        StaticImmutableNamespaceABC
        ,_ImmutableNamespaceBase
        ):
    '''
overrided abstract_methods:
    `__static_get_readonly_ordered_primekey_attr_seq__
    `__static_get_readonly_ordered_user_attr_seq__
'''
    __slots__ = ()


    @__class_method__
    def __init_subclass__(cls, *
        , ordered_user_attr_seq=None
        , type2ordered_user_attr_seq=None
        , type_attr4ordered_user_attr_seq=None
        , **kwargs
        ):
        if not inspect.isabstract(cls) and not cls is __class__:
            cls.__init_subclass(
                ordered_user_attr_seq=ordered_user_attr_seq
                ,type2ordered_user_attr_seq=type2ordered_user_attr_seq
                ,type_attr4ordered_user_attr_seq=type_attr4ordered_user_attr_seq
                )
        #super(__class__, cls).__init_subclass__(cls, **kwargs)
        super(__class__, cls).__init_subclass__(**kwargs)

    @__class_method__
    def __init_subclass(cls, *
        , ordered_user_attr_seq=None
        , type2ordered_user_attr_seq=None
        , type_attr4ordered_user_attr_seq=None
        ):
        if sum(x is not None for x in [ordered_user_attr_seq, type2ordered_user_attr_seq, type_attr4ordered_user_attr_seq]) != 1: raise TypeError

        if not (ordered_user_attr_seq is None
                or is_Sequence(ordered_user_attr_seq)): raise TypeError
        if not (type2ordered_user_attr_seq is None
                or callable(type2ordered_user_attr_seq)): raise TypeError
        if not (type_attr4ordered_user_attr_seq is None
                or type(type_attr4ordered_user_attr_seq) is str): raise TypeError
        #if ordered_user_attr_seq is None or iter(ordered_user_attr_seq):

        if ordered_user_attr_seq is not None:
            pass
        elif type2ordered_user_attr_seq is not None:
            # callable
            ordered_user_attr_seq = type2ordered_user_attr_seq(cls)
        elif type_attr4ordered_user_attr_seq is not None:
            # str
            attr = type_attr4ordered_user_attr_seq
            ordered_user_attr_seq = getattr(cls, attr)
        else:
            raise logic-error

        # verify result of cls->ordered_user_attr_seq
        if not is_Sequence(ordered_user_attr_seq): raise TypeError

        ordered_user_attr_seq = tuple(ordered_user_attr_seq)
        cls.ordered_user_attr_seq = ordered_user_attr_seq
        cls.ordered_user_attr_set = frozenset(ordered_user_attr_seq)

        """
        for name in ordered_user_attr_seq:
            setattr(cls, name, NamedReadOnlyProperty(name))
        """



    @__static_method__
    def __new__(__cls, **kwargs):
        ordered_user_attr_seq = __cls.__static_get_readonly_ordered_user_attr_seq__()
        missing = frozenset(ordered_user_attr_seq) - frozenset(kwargs)
        if missing:
            raise TypeError(f'missing: {missing}')

        if len(ordered_user_attr_seq) == len(kwargs):
            user_dict = kwargs
            kwargs = {}
            #print_err(f'user_dict = {user_dict}')
        else:
            user_dict = {attr: kwargs.pop(attr) for attr in ordered_user_attr_seq}

        return super(__class__, __cls).__new__(__cls
            , user_dict=MappingProxyType(user_dict), **kwargs)


    @__class_method__
    @override
    def __static_get_readonly_ordered_primekey_attr_seq__(cls):
        return cls.ordered_user_attr_seq
    @__class_method__
    @override
    def __static_get_readonly_ordered_user_attr_seq__(cls):
        return cls.ordered_user_attr_seq



class DynamicImmutableNamespace(_ImmutableNamespaceBase):
    '''
overrided abstract_methods:
    `__get_num_primekey_attrs__
    `__iter_ordered_primekey_attrs__
    `__iter_ordered_user_attrs__
    `__iter_unstable_primekey_attrs__
    `__iter_unstable_user_attrs__
    `__make_ordered_primekey_attr_seq__
    `__make_ordered_user_attr_seq__

'''
    __slots__ = ()

    @__static_method__
    def __new__(__cls, **kwargs):
        return super(__class__, __cls).__new__(__cls
            , user_dict=MappingProxyType(kwargs))

    @__instance_method__
    @override
    def __get_num_primekey_attrs__(self):
        return len(type(self).__get_readonly_user_dict__(self))

    @__instance_method__
    @override
    def __iter_ordered_primekey_attrs__(self):
        return type(self).__iter_ordered_user_attrs__(self)
    @__instance_method__
    @override
    def __iter_ordered_user_attrs__(self):
        return iter(type(self).__make_ordered_user_attr_seq__(self))
    @__instance_method__
    @override
    def __iter_unstable_primekey_attrs__(self):
        return type(self).__iter_unstable_user_attrs__(self)
    @__instance_method__
    @override
    def __iter_unstable_user_attrs__(self):
        return iter(type(self).__get_readonly_user_dict__(self))
    @__instance_method__
    @override
    def __make_ordered_primekey_attr_seq__(self):
        return type(self).__make_ordered_user_attr_seq__(self)
    @__instance_method__
    @override
    def __make_ordered_user_attr_seq__(self):
        return sorted(type(self).__iter_unstable_user_attrs__(self))










if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

if __name__ == '__main__':
    classes = [
    NamespaceABC
        ,ImmutableNamespaceABC
            ,StaticImmutableNamespaceABC
        ,UserCachedNamespaceABC
            ,SetUserDictOnceNamespaceABC
        ,ImplDictNamespaceABC
            ,ImplCachedNamespaceABC
                ,SetImplDictOnceNamespaceABC
        ,StaticImmutableNamespaceBase
        ,DynamicImmutableNamespace
        ]
    excludes = '''
        logic
        error
        '''.split()

    from seed.helper.ongo import main
    main(modules=[__name__], classes=classes, excludes=excludes)

from seed.types.NamespaceABC import StaticImmutableNamespaceBase
from seed.types.NamespaceABC import DynamicImmutableNamespace
from seed.types.NamespaceABC import *
