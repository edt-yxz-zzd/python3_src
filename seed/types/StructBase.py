
r'''

>>> class I(BasicStructABC):
...     @classmethod
...     def __get_all_user_attr_seq__(cls): return ()
>>> I() #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
TypeError

>>> class I(BasicStructABC):
...     @classmethod
...     def __get_all_impl_attr_set__(cls): return frozenset()
>>> I() #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
TypeError

>>> class B(BasicStructABC):
...     @classmethod
...     def __get_all_impl_attr_set__(cls): return {'_BasicStructABC__hash'}
...     @classmethod
...     def __get_all_user_attr_seq__(cls): return ()
>>> B()
B()


>>> class B(BasicStructABC):
...     @classmethod
...     def __get_all_impl_attr_set__(cls): return {'a', 'b', 'c', 'd', '_BasicStructABC__hash'}
...     @classmethod
...     def __get_all_user_attr_seq__(cls): return ('a', 'b')
...     @classmethod
...     def __get_all_primekey_attr_seq__(cls): return ('b',)
...     @classmethod
...     def __get_cached_attr2calc__(cls):
...         return dict(d=lambda self:self.a+self.b
...                     , **super().__get_cached_attr2calc__())

>>> b = B(b=1, a=4)
>>> b
B(a = 4, b = 1)

>>> b.a
4
>>> b.b
1
>>> b.c #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError

>>> b.a = 3
Traceback (most recent call last):
    ...
AttributeError: a
>>> b.c = 3
>>> b.c
3

>>> del b.a
Traceback (most recent call last):
    ...
AttributeError: a
>>> del b.c
Traceback (most recent call last):
    ...
AttributeError: c

>>> b
B(a = 4, b = 1)
>>> del b.d
Traceback (most recent call last):
    ...
AttributeError: d
>>> b.d
5
>>> del b.d
Traceback (most recent call last):
    ...
AttributeError: d


>>> type(hash(b))
<class 'int'>
>>> b._BasicStructABC__hash == hash(b)
True



>>> class C(StructBase):
...     @classmethod
...     def __iter_all_primekey_attrs__(cls):
...         yield from 'b'
...         yield from super().__iter_all_primekey_attrs__()
...     @classmethod
...     def __iter_all_user_attrs__(cls):
...         yield from 'ab'
...         yield from super().__iter_all_user_attrs__()
...     @classmethod
...     def __iter_all_impl_attrs__(cls):
...         yield from 'abcd'
...         yield from super().__iter_all_impl_attrs__()
...     @classmethod
...     def __iter_all_cached_attr_calc_pairs__(cls):
...         yield ('d', lambda self: self.a+self.b)
...         yield from super().__iter_all_cached_attr_calc_pairs__()


>>> b = B(b=1, a=4)
>>> b
B(a = 4, b = 1)

>>> b.a
4
>>> b.b
1
>>> b.c #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError

>>> b.a = 3
Traceback (most recent call last):
    ...
AttributeError: a
>>> b.c = 3
>>> b.c
3

>>> del b.a
Traceback (most recent call last):
    ...
AttributeError: a
>>> del b.c
Traceback (most recent call last):
    ...
AttributeError: c

>>> b
B(a = 4, b = 1)
>>> del b.d
Traceback (most recent call last):
    ...
AttributeError: d
>>> b.d
5
>>> del b.d
Traceback (most recent call last):
    ...
AttributeError: d


>>> type(hash(b))
<class 'int'>
>>> b._BasicStructABC__hash == hash(b)
True



'''





__all__ = '''
    StructBase
    BasicStructABC
    '''.split()

from seed.tiny import print_err
from seed.helper.repr_input import repr_helper_ex
from seed.abc import abstractmethod, ABC, final, override
import inspect # isabstract
from collections.abc import Set, Sequence, Mapping
from types import MappingProxyType
"""
from seed.types.EmptyMapping import (
    empty_mapping
    ,empty_set
    ,empty_tuple
    ,empty_iterator
    )
"""

def is_str(obj): return type(obj) is str
def are_strs(iterable): return all(map(is_str, iterable))


class BasicStructABC(ABC):
    '''
set(cls.__get_all_primekey_attr_seq__)
    <= set(cls.__get_all_user_attr_seq__)
    <= cls.__get_all_impl_attr_set__()
set(cls.__get_cached_attr2calc__())
    <= cls.__get_all_impl_attr_set__()
set(cls.__get_cached_attr2calc__()).isdisjoint(
    set(cls.__get_all_user_attr_seq__)
    )

    primekey_attr for __eq__
    user_attr for __init__&__repr__
    impl_attr for __setattr__&__getattribute__
    cached_attr for cache@__getattribute__

see:
    ImmutableNamespaceBase
    ImmutableNamespace
StructBase vs ImmutableNamespaceBase vs ImmutableNamespace
    * 1: dynamic or static attrs
        ImmutableNamespace have dynamic attrs
        ImmutableNamespaceBase/StructBase have static attrs
    * 2: has extra attrs??
        StructBase has extra attrs: impl_attrs - user_attrs
        ImmutableNamespaceBase/ImmutableNamespace has no
            # though has implicit "_hash_value"

'''
    @classmethod
    @abstractmethod
    def __get_all_user_attr_seq__(cls):
        # -> Seq # not Set
        raise NotImplementedError
    @classmethod
    @abstractmethod
    def __get_all_impl_attr_set__(cls):
        # -> Set # not Seq
        raise NotImplementedError
    @classmethod
    def __get_all_primekey_attr_seq__(cls):
        return cls.__get_all_user_attr_seq__()
    @classmethod
    def __get_cached_attr2calc__(cls):
        # -> {attr:calc}
        # -> Map String (Instance->Value)
        return {f'_{__class__.__name__}__hash': cls.___hash}

    @classmethod
    def __init_subclass__(cls, **kwargs):
        #print_err('at', __class__, cls)

        super().__init_subclass__(**kwargs)
        may_init_subclass4StructBase = getattr(cls, '_init_subclass4StructBase_', None)
        if may_init_subclass4StructBase is not None:
            init_subclass4StructBase = may_init_subclass4StructBase
            init_subclass4StructBase()

        if inspect.isabstract(cls): return

        primekey_attr_seq = cls.__get_all_primekey_attr_seq__()
        user_attr_seq = cls.__get_all_user_attr_seq__()
        impl_attr_set = cls.__get_all_impl_attr_set__()
        cached_attr2calc = cls.__get_cached_attr2calc__()

        if not isinstance(primekey_attr_seq, Sequence): raise TypeError
        if not isinstance(user_attr_seq, Sequence): raise TypeError
        if not isinstance(impl_attr_set, Set): raise TypeError
        if not isinstance(cached_attr2calc, Mapping): raise TypeError

        if not are_strs(primekey_attr_seq): raise TypeError
        if not are_strs(user_attr_seq): raise TypeError
        if not are_strs(impl_attr_set): raise TypeError
        if not are_strs(cached_attr2calc): raise TypeError

        primekey_attr_set = frozenset(primekey_attr_seq)
        user_attr_set = frozenset(user_attr_seq)
        cached_attr_set = frozenset(cached_attr2calc)
        if len(primekey_attr_set) != len(primekey_attr_seq): raise TypeError
        if len(user_attr_set) != len(user_attr_seq): raise TypeError

        if not primekey_attr_set <= user_attr_set: raise TypeError
        if not user_attr_set <= impl_attr_set: raise TypeError
        if not cached_attr_set <= impl_attr_set: raise TypeError
        if not user_attr_set.isdisjoint(cached_attr_set): raise TypeError
        if not all(map(callable, cached_attr2calc.values())): raise TypeError

    def __init__(self, **kwargs):
        cls = type(self)
        for attr in cls.__get_all_user_attr_seq__():
            value = kwargs.pop(attr)
            setattr(self, attr, value)
        super().__init__(**kwargs)

    def __repr__(self):
        cls = type(self)
        all_user_attr_seq = cls.__get_all_user_attr_seq__()
        return repr_helper_ex(self, (), all_user_attr_seq, {}, ordered_attrs_only=True)
    def __getattribute__(self, attr):
        cls = type(self)
        get = super().__getattribute__
        if attr in cls.__get_all_impl_attr_set__():
            try:
                return get(attr)
            except AttributeError:
                d = cls.__get_cached_attr2calc__()

                Nothing = []
                may_calc = d.get(attr, Nothing)
                if may_calc is Nothing:
                    raise
                calc = may_calc

                value = calc(self)
                #bug: recur
                #   setattr(self, attr, value)
                super().__setattr__(attr, value)
            return get(attr)
        else:
            return get(attr)
        raise AttributeError(attr)

    def __delattr__(self, attr):
        raise AttributeError(attr)
    def __setattr__(self, attr, obj):
        if hasattr(self, attr):
            raise AttributeError(attr)

        cls = type(self)
        if attr in cls.__get_all_impl_attr_set__():
            super().__setattr__(attr, obj)
            return

        raise AttributeError(attr)

    def __eq__(self, other):
        return (type(self) is type(other)
            and all(getattr(self, attr) == getattr(other, attr)
                    for attr in type(self).__get_all_primekey_attr_seq__()
                )
            )
    def __hash__(self):
        return self.__hash
    def ___hash(self):
        cls = type(self)
        primekey_attrs = cls.__get_all_primekey_attr_seq__()
        values = (getattr(self, attr) for attr in primekey_attrs)
        repr_data = id(cls), tuple(values)
        return hash(repr_data)








class StructBase(BasicStructABC):
    @classmethod
    def __iter_all_primekey_attrs__(cls):
        # -> Iter primekey_attr
        return; yield
    @classmethod
    def __iter_all_user_attrs__(cls):
        # -> Iter user_attr
        return; yield
    @classmethod
    def __iter_all_impl_attrs__(cls):
        # -> Iter impl_attr
        return iter(super().__get_cached_attr2calc__().keys())
    @classmethod
    def __iter_all_cached_attr_calc_pairs__(cls):
        # -> Iter (cached_attr, calc)
        # -> Iter (cached_attr, instance->value)
        return iter(super().__get_cached_attr2calc__().items())


    """
    @classmethod
    def __iter_primekey_attrs_at_this_class__(cls):
        # -> Iter primekey_attr
        return; yield
    @classmethod
    def __iter_user_attrs_at_this_class__(cls):
        # -> Iter user_attr
        return; yield
    @classmethod
    def __iter_impl_attrs_at_this_class__(cls):
        # -> Iter impl_attr
        return iter(super().__get_cached_attr2calc__().keys())
    @classmethod
    def __iter_cached_attr_calc_pairs_at_this_class__(cls):
        # -> Iter (cached_attr, calc)
        # -> Iter (cached_attr, instance->value)
        return iter(super().__get_cached_attr2calc__().items())

    @classmethod
    @final
    def __iter_all_XXX(cls, func_name):
        # O(n^2)
        #
        #if not hasattr(cls, func_name): raise AttributeError
        mk_iter = getattr(cls, func_name)
        while True:
            if not isinstance(mk_iter, classmethod): raise TypeError
            subclass = mk_iter.
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        for cls in cls.__mro__:
            may_mk_iter = getattr(cls, func_name, None)
            if may_mk_iter is None: continue
            mk_iter = may_mk_iter
            yield from mk_iter()
    @classmethod
    @final
    def __iter_all_primekey_attrs__(cls):
        # -> Iter primekey_attr
        return cls.__iter_all_XXX('__iter_primekey_attrs_at_this_class__')
    @classmethod
    @final
    def __iter_all_user_attrs__(cls):
        # -> Iter user_attr
        return cls.__iter_all_XXX('__iter_user_attrs_at_this_class__')
    @classmethod
    @final
    def __iter_all_impl_attrs__(cls):
        # -> Iter impl_attr
        return cls.__iter_all_XXX('__iter_impl_attrs_at_this_class__')
    @classmethod
    @final
    def __iter_all_cached_attr_calc_pairs__(cls):
        # -> Iter (cached_attr, calc)
        # -> Iter (cached_attr, instance->value)
        return cls.__iter_all_XXX('__iter_cached_attr_calc_pairs_at_this_class__')
    """


    '''
    @classmethod
    @override
    def __init_subclass__(cls, **kwargs):
        #print_err('at', __class__, cls)
        cls._init_subclass4StructBase_()
        super().__init_subclass__(**kwargs)
    '''

    @classmethod
    def _init_subclass4StructBase_(cls):
        if inspect.isabstract(cls): return
        impl_attr_seq = tuple(cls.__iter_all_impl_attrs__())
        cls.__all_impl_attr_set__ = frozenset(impl_attr_seq)

        cached_attr_calc_pair_seq = tuple(cls.__iter_all_cached_attr_calc_pairs__())
        cls.__cached_attr2calc__ = MappingProxyType(dict(cached_attr_calc_pair_seq))
        try:
            if len(cls.__all_impl_attr_set__) != len(impl_attr_seq): raise TypeError
        except:
            print_err(cls.__all_impl_attr_set__)
            print_err(impl_attr_seq)
            from seed.iters.duplicate_elements import find_duplicate_element_groups
            print_err(find_duplicate_element_groups(impl_attr_seq))
            raise
        if len(cls.__cached_attr2calc__) != len(cached_attr_calc_pair_seq): raise TypeError

        cls.__all_primekey_attr_seq__ = tuple(cls.__iter_all_primekey_attrs__())
        cls.__all_user_attr_seq__ = tuple(cls.__iter_all_user_attrs__())


    @classmethod
    @override
    def __get_all_user_attr_seq__(cls):
        # -> Seq # not Set
        return cls.__all_user_attr_seq__
    @classmethod
    @override
    def __get_all_impl_attr_set__(cls):
        # -> Set # not Seq
        return cls.__all_impl_attr_set__
    @classmethod
    @override
    def __get_all_primekey_attr_seq__(cls):
        return cls.__all_primekey_attr_seq__
    @classmethod
    @override
    def __get_cached_attr2calc__(cls):
        # -> {attr:calc}
        return cls.__cached_attr2calc__







if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


