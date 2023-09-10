r'''
e ../../python3_src/seed/types/ImmutableNamespaceBase.py
    view ../../python3_src/seed/types/namedtuple.txt
    view ../../python3_src/seed/types/mk_ordered_field_name_seq_.py
    view ../../python3_src/seed/types/NamedTupleBase.py
        similar:basecls



ImmutableNamespaceBase vs ImmutableNamespace
    ImmutableNamespaceBase requires cls.ordered_attr_name_seq
    instance of concrete subclass of ImmutableNamespaceBase have same attrs
    instances of ImmutableNamespace have diff attrs

see: ImmutableNamespace





py -m nn_ns.app.debug_cmd   seed.types.ImmutableNamespaceBase -x
py -m seed.types.ImmutableNamespaceBase
py -m nn_ns.app.doctest_cmd seed.types.NamedTupleBase:__doc__ -ff -v


from seed.types.ImmutableNamespaceBase import ImmutableNamespaceBase




>>> from seed.types.ImmutableNamespaceBase import ImmutableNamespaceBase
>>> class NoAttrs(ImmutableNamespaceBase, ordered_attr_name_seq=''):pass
>>> class A(ImmutableNamespaceBase, ordered_attr_name_seq='a'):pass
>>> class AB(ImmutableNamespaceBase, ordered_attr_name_seq='ab'):pass



>>> NoAttrs()
NoAttrs()
>>> A(a = 1)
A(a = 1)
>>> AB(b = 0, a = 1)
AB(a = 1, b = 0)

>>> ns = NoAttrs()
>>> ns.a = 1
Traceback (most recent call last):
    ...
AttributeError: a
>>> ns
NoAttrs()
>>> vars(ns)
mappingproxy({})

>>> ns = AB(b = 0, a = 1)
>>> ns.a = 2
Traceback (most recent call last):
    ...
AttributeError: a
>>> del ns.a
Traceback (most recent call last):
    ...
AttributeError: a
>>> ns.a
1
>>> dir(ns)
['a', 'b']
>>> ns == ns
True
>>> ns <= ns
True
>>> ns >= ns
True
>>> ns < ns
False
>>> ns > ns
False

>>> type(hash(ns))
<class 'int'>

>>> A.a
NamedReadOnlyProperty('a')
>>> AB.b
NamedReadOnlyProperty('b')


>>> class AB(ImmutableNamespaceBase, type_attr4ordered_attr_name_seq='attrs'):
...     attrs = 'ab'
>>> AB.b
NamedReadOnlyProperty('b')
>>> AB(b=-3, a=-1)
AB(a = -1, b = -3)
>>> class AB(ImmutableNamespaceBase, type2ordered_attr_name_seq=lambda cls:cls.attrs):
...     attrs = 'ab'
>>> AB.b
NamedReadOnlyProperty('b')
>>> AB(b=-3, a=-1)
AB(a = -1, b = -3)


'''#'''

__all__ = '''
    ImmutableNamespaceBase
    '''.split()

from .NamedReadOnlyProperty import NamedReadOnlyProperty
from .CachedProperty import CachedProperty
from seed.helper.repr_input import repr_helper_ex
from types import MappingProxyType

from seed.types.mk_ordered_field_name_seq_ import mk_ordered_field_name_seq_

def _get_kwargs(self):
    return super(ImmutableNamespaceBase, self).__getattribute__('_ImmutableNamespaceBase__kwargs')
def _set_kwargs(self, kwargs):
    super(ImmutableNamespaceBase, self).__setattr__('_ImmutableNamespaceBase__kwargs', kwargs)
def _set_hash_value(self, hash_value):
    super(ImmutableNamespaceBase, self).__setattr__('_ImmutableNamespaceBase__hash_value', hash_value)



class ImmutableNamespaceBase:
    __slots__ = '''
        _ImmutableNamespaceBase__kwargs
        _ImmutableNamespaceBase__hash_value
        '''.split()

    @classmethod
    def __init_subclass__(cls, *
        , ordered_attr_name_seq=None
        , type2ordered_attr_name_seq=None
        , type_attr4ordered_attr_name_seq=None
        , **kwargs
        ):
        ordered_attr_name_seq = mk_ordered_field_name_seq_(cls
            , ordered_field_name_seq
            = ordered_attr_name_seq
            , type2ordered_field_name_seq
            = type2ordered_attr_name_seq
            , type_field_name4ordered_field_name_seq
            = type_attr4ordered_attr_name_seq
            )

        cls.ordered_attr_name_seq = ordered_attr_name_seq
        cls.attr_name_set = frozenset(ordered_attr_name_seq)

        for name in ordered_attr_name_seq:
            setattr(cls, name, NamedReadOnlyProperty(name))

        super().__init_subclass__(**kwargs)


    def __init__(self, **kwargs):
        cls = type(self)
        missing_names = cls.attr_name_set - frozenset(kwargs)
        if missing_names:
            raise TypeError(f'missing: {missing_names!r}')

        if len(kwargs) > len(cls.attr_name_set):
            d = {name: kwargs.pop(name) for name in cls.attr_name_set}
        else:
            d = kwargs
            kwargs = {}

        _set_kwargs(self, MappingProxyType(d))
        super().__init__(**kwargs)

    def __getattribute__(self, attr):
        d = _get_kwargs(self)
        try:
            return d[attr]
        except KeyError:
            pass

        if attr == '__dict__':
            # kwargs as __dict__ for user!
            return d
            return MappingProxyType(d)

        return super().__getattribute__(attr)

    def __dir__(self):
        cls = type(self)
        return cls.ordered_attr_name_seq
    def __setattr__(self, attr, obj):
        raise AttributeError(attr)
    def __delattr__(self, attr):
        raise AttributeError(attr)

    def __iter_ordered_values(self):
        values = (v for k, v in self.__iter_ordered_items())
        return values
    def __iter_ordered_items(self):
        cls = type(self)
        d = _get_kwargs(self)
        keys = cls.ordered_attr_name_seq
        items = ((k, d[k]) for k in keys)
        return items

    def __repr__(self):
        cls = type(self)
        return repr_helper_ex(self, (), cls.ordered_attr_name_seq, {}, ordered_attrs_only=True)
        """
        cls = type(self)
        items = self.__iter_ordered_items()
        item_strs = ("{}={!r}".format(k, v) for k, v in items)
        return "{}({})".format(cls.__name__, ", ".join(item_strs))
        """

    def __eq__(self, other):
        if self is other: return True
        #if not isinstance(other, __class__): return NotImplemented
        return (type(self) is type(other)
            and hash(self) == hash(other)
            and all(a == b for a, b in zip(self.__iter_ordered_values()
                                        , other.__iter_ordered_values())
                )
            )
    def __lt__(self, other):
        #if not isinstance(other, __class__): return NotImplemented
        if type(self) is not type(other): raise TypeError #NotImplementedError
        for a, b in zip(self.__iter_ordered_values()
                        , other.__iter_ordered_values()):
            if a == b: continue
            return a < b
        return False
    def __le__(self, other):
        if type(self) is not type(other): raise TypeError #NotImplementedError
        return not (other < self)
    def __gt__(self, other):
        return not (self <= other)
    def __ge__(self, other):
        return not (self < other)

    def __hash__(self):
        try:
            return self.__hash_value
        except AttributeError:
            cls = type(self)
            hash_value = cls.__calc_hash_value__(self)
            #self.__hash_value = hash_value
            _set_hash_value(self, hash_value)
        return self.__hash_value
    #@CachedProperty.at(instance2cached_dict=_get_vars)
    def __calc_hash_value__(self):
        cls = type(self)
        items = self.__iter_ordered_items()
        repr_data = id(cls), tuple(items)
        return hash(repr_data)


from seed.types.ImmutableNamespaceBase import ImmutableNamespaceBase
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

