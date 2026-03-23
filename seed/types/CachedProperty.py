#__all__:goto

r'''
e ../../python3_src/seed/types/CachedProperty.py

py -m seed.types.CachedProperty
py -m nn_ns.app.debug_cmd   seed.types.CachedProperty -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.CachedProperty:__doc__ -ht # -ff -df



>>> instance2calc_value = lambda self: hash(self.xxx)
>>> class B:
...     @CachedProperty
...     def hash_value(self):
...         print('eval hash_value')
...         return id(self)
...     def __hash__(self):
...         return self.hash_value

>>> b = B()
>>> hash(b) == id(b)
eval hash_value
True
>>> b.hash_value == id(b) # no "eval hash_value" printed
True
>>> vars(b)['hash_value'] is b.hash_value # no "eval hash_value" printed
True
>>> hash(b) == b.hash_value
True
>>> hash(b) == type(b).hash_value(b) #used asif func
True
>>> type(b).__hash__(b) == type(b).hash_value(b) #used asif func
True

>>> type(b).hash_value(b) #doctest: +SKIP

>>> from abc import abstractmethod
>>> @CachedProperty
... @abstractmethod
... def f(self):pass
>>> @CachedProperty
... def g(self):pass
>>> f.__isabstractmethod__
True
>>> g.__isabstractmethod__
False



[[
e ../lots/NOTE/Python/python-bug/cached_property-bug.txt
>>> from functools import cached_property
>>> class C:
...     @cached_property
...     def a(sf, /):
...         return 111
>>> x = C()
>>> vars(x)
{}
>>> x.a
111
>>> vars(x)['a']
111
>>> x.a = 222  #???why not raise AttributeError?
>>> x.a
222
>>> vars(x)['a']
222

>>> C.a  #doctest: +ELLIPSIS
<functools.cached_property object at 0x...>

]]

[[
>>> class C:
...     @CachedProperty
...     def a(sf, /):
...         return 111
>>> x = C()
>>> vars(x)
{}
>>> x.a
111
>>> vars(x)['a']
111
>>> x.a = 222  #???why not raise AttributeError?
Traceback (most recent call last):
    ...
AttributeError: a
>>> x.a
111
>>> vars(x)['a']
111

>>> C.a  #doctest: +ELLIPSIS
CachedProperty(<function C.a at 0x...>, attribute_name = 'a')




>>> from abc import abstractmethod, ABC
>>> class C(ABC):
...     @CachedProperty
...     @abstractmethod
...     def a(sf, /):...
>>> C()
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class C with abstract method a
>>> C.a  #doctest: +ELLIPSIS
CachedProperty(<function C.a at 0x...>, attribute_name = 'a')

>>> class C:
...     @CachedProperty(writable=True)
...     def b(sf, /):return 333
>>> x = C()
>>> x.b
333
>>> x.b = 222
>>> x.b
222
>>> del x.b
>>> del x.b
Traceback (most recent call last):
    ...
AttributeError: b
>>> x.b
333
>>> del x.b
>>> x.b = 444
>>> x.b
444

>>> CachedProperty.at(writable=True)
functools.partial(<class 'seed.types.CachedProperty.CachedProperty'>, writable=True)
>>> CachedProperty(writable=True)
functools.partial(<class 'seed.types.CachedProperty.CachedProperty'>, writable=True)
>>> mk_cached_propertyT_(writable=True)
functools.partial(<class 'seed.types.CachedProperty.CachedProperty'>, writable=True)

>>> CachedProperty(str, writable=True)
CachedProperty(<class 'str'>, writable = True)
>>> mk_cached_propertyT_(str, writable=True)
CachedProperty(<class 'str'>, writable = True)


]]
'''#'''

__all__ = '''
    CachedProperty
    mk_cached_propertyT_
    '''.split()#'''

___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.repr_input import repr_helper
from functools import update_wrapper, partial
from functools import cached_property as __
___end_mark_of_excluded_global_names__0___ = ...

r'''
.class Partial_Instance2CachedValue:
.    def __init__(self, *, maybe_instance2cached_dict, maybe_attribute_name):
.        # attribute_name maybe None
.        if maybe_instance2cached_dict is None:
.            instance2cached_dict = vars
.        else:
.            instance2cached_dict = maybe_instance2cached_dict
.        self.instance2cached_dict = instance2cached_dict
.        self.maybe_attribute_name = maybe_attribute_name
.    def make_instance2cached_value(self, *, property_name):
.        maybe_attribute_name = self.maybe_attribute_name
.        if maybe_attribute_name is None:
.            attribute_name = property_name
.        else:
.            # allow property_name != attribute_name
.            attribute_name = maybe_attribute_name
.        return Instance2CachedValue(
.                instance2cached_dict=self.instance2cached_dict
.                ,attribute_name=attribute_name
.                )
.
.
.class Instance2CachedValue:
.    def __init__(self, *, instance2cached_dict, attribute_name):
.        self.instance2cached_dict = instance2cached_dict
.        self.attribute_name = attribute_name
.    def __call__(self, instance):
.        return self.instance2cached_dict(instance)[self.attribute_name]

'''#'''














def check_args4CachedProperty(instance2calc_value=None, *, instance2cached_dict=None, attribute_name=None, writable=False):
    #if not callable(instance2calc_value): raise TypeError
    if not (instance2calc_value is None or callable(instance2calc_value)): raise TypeError
    if not (instance2cached_dict is None or callable(instance2cached_dict)): raise TypeError
    if not (attribute_name is None or type(attribute_name) is str and attribute_name.isidentifier()): raise TypeError
    if not type(writable) is bool:raise TypeError



class CachedProperty:
    r'''allow property_name != attribute_name

getattr(type(instance), property_name) is the property
getattr(instance, property_name) is the value
    == vars(instance)[attribute_name]
getattr(instance, attribute_name) is the value or fail
    attribute_name may not be a valid python identifier
    e.g.
        attribute_name = '@xxx@'

        #XXX: since need to be cached, unlike operator.attrgetter
        #   # unlike operator.attrgetter
        #   attribute_name =/= 'xxx.yyy'
        #   attribute_name =/= ('fst.xxx', 'snd.yyy')


now update "attribute_name" to "instance2cached_dict"+"attribute_name"
'''#'''
    r"""
    __slots__ = r'''
        instance2calc_value
        instance2cached_dict
        attribute_name
        __isabstractmethod__
        '''.split()#'''
    """#"""

    @classmethod
    def at(cls, *
        ,instance2cached_dict=None
        ,attribute_name=None
        ,writable=False
        ):
        return mk_cached_propertyT_(instance2cached_dict=instance2cached_dict, attribute_name=attribute_name, writable=writable, cls=cls)
        return (lambda instance2calc_value:
            __class__(instance2calc_value
                ,instance2cached_dict=instance2cached_dict
                ,attribute_name=attribute_name
                ,writable=writable
                )
            )
    def __new__(cls, /, instance2calc_value=None, *
        ,instance2cached_dict=None
        ,attribute_name=None
        ,writable=False
        ):
        if instance2calc_value is None:
            return mk_cached_propertyT_(instance2cached_dict=instance2cached_dict, attribute_name=attribute_name, writable=writable, cls=cls)

        check_args4CachedProperty(instance2calc_value, instance2cached_dict=instance2cached_dict, attribute_name=attribute_name, writable=writable)
        if not callable(instance2calc_value): raise TypeError

        if instance2cached_dict is None:
            instance2cached_dict = vars

        __self = super(__class__, cls).__new__(cls)
        d = vars(__self)
        d['instance2calc_value'] = instance2calc_value
        d['instance2cached_dict'] = instance2cached_dict
        d['attribute_name'] = attribute_name
        d['writable'] = writable
        if 1:
            d['__isabstractmethod__'] = getattr(instance2calc_value, '__isabstractmethod__', False)
        else:
            #fail<<==:
                #update_wrapper(wrapper, wrapped, assigned=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), updated=('__dict__',))
            update_wrapper(__self, instance2calc_value)
            assert hasattr(__self, '__isabstractmethod__') is hasattr(instance2calc_value, '__isabstractmethod__')
        return __self
    def __repr__(self):
        #.return repr_helper(self, self.instance2calc_value, instance2cached_dict=self.instance2cached_dict, attribute_name=self.attribute_name)
        kwds = _mk_kwds(instance2cached_dict=self.instance2cached_dict, attribute_name=self.attribute_name, writable=self.writable)
        return repr_helper(self, self.instance2calc_value, **kwds)
    def __call__(self, instance):
        '# [=> type(instance).xxx(instance)]'
        return _get(self, instance)

    @property
    def instance2calc_value(self):
        #error:return object.__getattribute__(self, 'instance2calc_value')
        return vars(self)['instance2calc_value']
    @property
    def instance2cached_dict(self):
        return vars(self)['instance2cached_dict']
    @property
    def attribute_name(self):
        return vars(self)['attribute_name']
    @property
    def writable(self):
        return vars(self)['writable']
    def __setattr__(self, name, value):
        raise AttributeError(name)
    def __delattr__(self, name, value):
        raise AttributeError(name)

    def __set_name__(self, owner, property_name):
        if self.attribute_name is None:
            vars(self)['attribute_name'] = property_name
            assert self.attribute_name == property_name
        else:
            # allow property_name != attribute_name
            """
            if self.attribute_name != property_name:
                raise ValueError(f'attribute_name = {self.attribute_name!r} != {property_name!r} = property_name')
        assert self.attribute_name == property_name
        """

    def __get__(self, instance, owner):
        return _get(self, instance)

    # MUST define "__set__" to make self a data_descriptor
    #   otherwise, instance override self
    def __set__(self, instance, value):
        return _set(self, instance, value)
        raise AttributeError(self.attribute_name)
    def __delete__(self, instance):
        return _del(self, instance)
        raise AttributeError(self.attribute_name)













    r"""
    def __repr__(self):
        return repr_helper(self, self.attribute_name)
    """#"""

    r'''
    def ireplace(self, *, instance2calc_value=None, instance2cached_dict=None, attribute_name):
        d = dict(instance2calc_value=self.instance2calc_value, instance2cached_dict=self.instance2cached_dict, attribute_name=self.attribute_name)
        if instance2calc_value is not None:
            d['instance2calc_value'] = instance2calc_value
        if instance2cached_dict is not None:
            d['instance2cached_dict'] = instance2cached_dict
        if attribute_name is not None:
            d['attribute_name'] = attribute_name
        return __class__(**d)
    '''#'''

def _get(self, instance):
    if instance is None:
        return self

    attribute_name = self.attribute_name
    d = self.instance2cached_dict(instance)
    try:
        return d[attribute_name]
    except KeyError:
        d[attribute_name] = self.instance2calc_value(instance)
    #.return d[attribute_name]
    return _get(self, instance)

def _set(self, instance, value):
    attribute_name = self.attribute_name
    if not self.writable:
        raise AttributeError(attribute_name)
    d = self.instance2cached_dict(instance)
    try:
        d[attribute_name] = value
    except KeyError:
        raise AttributeError(attribute_name)
def _del(self, instance):
    attribute_name = self.attribute_name
    if not self.writable:
        raise AttributeError(attribute_name)
    d = self.instance2cached_dict(instance)
    try:
        del d[attribute_name]
    except KeyError:
        raise AttributeError(attribute_name)


mk_cached_propertyT_ = CachedProperty.at
def mk_cached_propertyT_(instance2calc_value=None, *, instance2cached_dict=None, attribute_name=None, writable=False, cls=CachedProperty):
    if not instance2calc_value is None:
        return cls(instance2calc_value, instance2cached_dict=instance2cached_dict, attribute_name=attribute_name, writable=writable)

    check_args4CachedProperty(instance2calc_value, instance2cached_dict=instance2cached_dict, attribute_name=attribute_name, writable=writable)
    kwds = _mk_kwds(instance2cached_dict=instance2cached_dict, attribute_name=attribute_name, writable=writable)
    mk_cached_property_ = partial(cls, **kwds)
    return mk_cached_property_
def _mk_kwds(*, instance2cached_dict=None, attribute_name=None, writable=False):
    if instance2cached_dict is None or instance2cached_dict is vars:
        del instance2cached_dict
    if attribute_name is None:
        del attribute_name
    if not writable:
        del writable
    kwds = dict(locals())
    #kwds = {nm:v for nm, v in kwds.items() if not (v is None or v is False)}
    return kwds


from seed.types.CachedProperty import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
from seed.types.CachedProperty import *


