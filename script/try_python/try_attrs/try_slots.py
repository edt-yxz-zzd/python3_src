#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
e ../../python3_src/script/try_python/try_attrs/try_slots.py
    见下面 B_a
        隐藏 attr 的方法有了！
          定义__slots__，取出descriptor，删除cls.__dict__中的descriptor

script.try_python.try_attrs.try_slots
py -m    script.try_python.try_attrs.try_slots
py -m nn_ns.app.debug_cmd   script.try_python.try_attrs.try_slots


#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin


#slots treat str diff tuple
>>> class A:
...     __slots__ = 'x y'
Traceback (most recent call last):
    ...
TypeError: __slots__ must be identifiers
>>> class A:
...     __slots__ = ()
>>> class A:
...     __slots__ = ''
Traceback (most recent call last):
    ...
TypeError: __slots__ must be identifiers
>>> class A:
...     __slots__ = 'xy'
>>> a = A()
>>> a.xy = 1
>>> a.xy
1
>>> a.x = 1
Traceback (most recent call last):
    ...
AttributeError: 'A' object has no attribute 'x'


#no __slots__ ==>> __dict__,__weakref__
>>> class A:
...     __slots__ = ('z',)
>>> class B(A):pass
>>> a = A()
>>> b = B()
>>> a.z = 1
>>> a.z
1
>>> a.x = 1
Traceback (most recent call last):
    ...
AttributeError: 'A' object has no attribute 'x'
>>> b.z = 1
>>> b.z
1
>>> b.x = 1 #no __slots__ ==>> __dict__,__weakref__
>>> b.__dict__
{'x': 1}
>>> b.__weakref__
>>> b.__weakref__ is None
True
>>> a.__dict__
Traceback (most recent call last):
    ...
AttributeError: 'A' object has no attribute '__dict__'
>>> a.__weakref__
Traceback (most recent call last):
    ...
AttributeError: 'A' object has no attribute '__weakref__'
>>> import weakref
>>> w1 = weakref.ref(b)
>>> w2 = weakref.ref(b)
>>> w2() is w1() is b
True
>>> b.__weakref__ is w1 is w2
True

>>> del b.__weakref__
Traceback (most recent call last):
    ...
AttributeError: attribute '__weakref__' of 'B' objects is not writable

>>> b.__weakref__ = None
Traceback (most recent call last):
    ...
AttributeError: attribute '__weakref__' of 'B' objects is not writable




#multi-inherit with nonempty slots is error
>>> class A:
...     __slots__ = ('a',)
>>> class B:
...     __slots__ = ('b',)
>>> class C(B, A):
...     __slots__ = ()
Traceback (most recent call last):
    ...
TypeError: multiple bases have instance lay-out conflict

#single-inherit with nonempty slots is ok
>>> class A:
...     __slots__ = ('a',)
>>> class B:
...     __slots__ = ()
>>> class C(B, A):
...     __slots__ = ('c',)


>>> A.a
<member 'a' of 'A' objects>
>>> C.c
<member 'c' of 'C' objects>

#>>> A.__dict__
mappingproxy({'__module__': '__main__', '__slots__': ('a',), 'a': <member 'a' of 'A' objects>, '__doc__': None})
#>>> C.__dict__
mappingproxy({'__module__': '__main__', '__slots__': ('c',), 'c': <member 'c' of 'C' objects>, '__doc__': None})
>>> c = C()
>>> A.a.__get__(c)
Traceback (most recent call last):
    ...
AttributeError: a
>>> A.a.__set__(c, 0)
>>> A.a.__get__(c)
0




##[[hidden]]???? see below [[hidden]]
>>> class A:
...     __slots__ = ('a',)
>>> class B(A):
...     __slots__ = ('a',)

#>>> A.__dict__
mappingproxy({'__module__': '__main__', '__slots__': ('a',), 'a': <member 'a' of 'A' objects>, '__doc__': None})
#>>> B.__dict__
mappingproxy({'__module__': '__main__', '__slots__': ('a',), 'a': <member 'a' of 'B' objects>, '__doc__': None})

>>> b = B()
>>> b.__dict__
Traceback (most recent call last):
    ...
AttributeError: 'B' object has no attribute '__dict__'
>>> b.a = 2
>>> b.a
2
>>> A.__setattr__(b, 'a', 1)
>>> b.a
1
>>> A.__getattribute__(b, 'a')
1
>>> super(B, b).__setattr__('a', 0)
>>> b.a
0
>>> A.__getattribute__(b, 'a')
0
>>> A.a.__get__(b)
Traceback (most recent call last):
    ...
AttributeError: a

>>> A.__dict__['a'].__set__(b, -1)
>>> A.a.__get__(b)
-1
>>> b.a
0
>>> A_a = A.a
>>> B_a = B.a
>>> del B.a
>>> b.a
-1
>>> B_a
<member 'a' of 'B' objects>
>>> B.a
<member 'a' of 'A' objects>
>>> A.a
<member 'a' of 'A' objects>
>>> A_a.__get__(b)
-1
>>> B_a.__get__(b)
0
>>> B_a.__set__(b, -2)
>>> B_a.__get__(b)
-2
>>> A_a.__get__(b)
-1
>>> B_a.__delete__(b)
>>> B_a.__get__(b)
Traceback (most recent call last):
    ...
AttributeError: a
>>> A_a.__get__(b)
-1
>>> B_a.__set__(b, -2)
>>> B_a.__get__(b)
-2
>>> A_a.__get__(b)
-1

>>> b.a = 4
>>> b.a
4
>>> B_a.__get__(b)
-2
>>> A_a.__get__(b)
4

>>> del B.a
Traceback (most recent call last):
    ...
AttributeError: a
>>> B.a
<member 'a' of 'A' objects>
>>> del A.a
>>> B.a
Traceback (most recent call last):
    ...
AttributeError: type object 'B' has no attribute 'a'

>>> b.a = 4
Traceback (most recent call last):
    ...
AttributeError: 'B' object has no attribute 'a'

>>> class C(B):
...     __slots__ = ('c',)
>>> c = C()
>>> B_a.__get__(c)
Traceback (most recent call last):
    ...
AttributeError: a
>>> B_a.__set__(c, 0)
>>> B_a.__get__(c)
0

B_a:
    隐藏 attr 的方法有了！
      定义__slots__，取出descriptor，删除cls.__dict__中的descriptor

##[[hidden]]???? see above [[hidden]]
>>> class C(B):
...     __slots__ = ('a',)
>>> c = C()
>>> B_a.__get__(c)
Traceback (most recent call last):
    ...
AttributeError: a
>>> B_a.__set__(c, 0)
>>> B_a.__get__(c)
0
>>> c.a
Traceback (most recent call last):
    ...
AttributeError: a


>>> import inspect
>>> d = dict(inspect.getmembers(B))
>>> sorted(d)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__']
>>> d = dict(inspect.getmembers(c))
>>> sorted(d)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__']

#>>> dir(inspect)
>>> inspect.getattr_static(c, 'a')
<member 'a' of 'C' objects>
>>> inspect.getattr_static(C, 'a')
<member 'a' of 'C' objects>
>>> inspect.getattr_static(B, 'a')
Traceback (most recent call last):
    ...
AttributeError: a
>>> inspect.getattr_static(B(), 'a')
Traceback (most recent call last):
    ...
AttributeError: a




try non-str-attr
try non-str-slots
>>> class S:
...     locals()[1] = 2
>>> S.__dict__[1]
2
>>> S.__dict__ is object.__getattribute__(S, '__dict__')
False
>>> S.__dict__ is type.__getattribute__(S, '__dict__')
False
>>> object.__getattribute__(S, '__dict__') is type.__getattribute__(S, '__dict__')
False
>>> S.__dict__ is object.__getattribute__(S, '__dict__') is type.__getattribute__(S, '__dict__')
False
>>> type(S.__dict__) is type(object.__getattribute__(S, '__dict__')) is type(type.__getattribute__(S, '__dict__'))
True
>>> type(S.__dict__) is dict
False
>>> type(S.__dict__) # is MappingProxyType
<class 'mappingproxy'>
>>> class S:
...     __slots__ = (1,)
Traceback (most recent call last):
    ...
TypeError: __slots__ items must be strings, not 'int'
>>> class S:
...     __slots__ = dict(a=1)
>>> class S:
...     __slots__ = {3:str}
Traceback (most recent call last):
    ...
TypeError: __slots__ items must be strings, not 'int'

>>> object.__getattribute__(object, 2)
Traceback (most recent call last):
    ...
TypeError: attribute name must be string, not 'int'
>>> class X:pass
>>> x = X()
>>> x.__setattr__('a', 4)
>>> x.__dict__
{'a': 4}
>>> x.a
4

>>> X.__dict__ = d = {}
Traceback (most recent call last):
    ...
AttributeError: attribute '__dict__' of 'type' objects is not writable
>>> x.__dict__ = d = {}
>>> d is x.__dict__
True
>>> from types import MappingProxyType
>>> x.__dict__ = d = MappingProxyType({})
Traceback (most recent call last):
    ...
TypeError: __dict__ must be set to a dictionary, not a 'mappingproxy'

>>> class Dict(dict):
...     def __delitem__(sf, k, /): raise KeyError
...     def __setitem__(sf, k, v, /): raise KeyError
>>> x.__dict__ = d = Dict()
>>> d is x.__dict__
True
>>> type(d) is Dict
True
>>> d['a'] = 5
Traceback (most recent call last):
    ...
KeyError
>>> x.a = 1
>>> x.a
1
>>> d
{'a': 1}
>>> x.__dict__ = d = object.__new__(Dict)
Traceback (most recent call last):
    ...
TypeError: object.__new__(Dict) is not safe, use Dict.__new__()
>>> class _(dict, tuple):pass
Traceback (most recent call last):
    ...
TypeError: multiple bases have instance lay-out conflict





>>> o = object()
>>> o.a = 5
Traceback (most recent call last):
    ...
AttributeError: 'object' object has no attribute 'a'
>>> object.__slots__
Traceback (most recent call last):
    ...
AttributeError: type object 'object' has no attribute '__slots__'
>>> sorted(object.__dict__)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']





>>> class S:
...     locals()[1] = 2
>>> S.__dict__[1]
2

ns = namespace = locals = metaclass.__prepare__(name, bases2, **kwds2)
>>> class Meta(type):
...     @classmethod
...     def __prepare__(sf_as_meta, name, bases, /,**kwargs):
...         d = super().__prepare__(name, bases, **kwargs)
...         d[3] = 5
...         return d
>>> class S(metaclass=Meta):pass
>>> S.__dict__[3]
5

#>>> S.__dict__
mappingproxy({3: 5, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'S' objects>, '__weakref__': <attribute '__weakref__' of 'S' objects>, '__doc__': None})
>>> s = S()
>>> s.a = 1

>>> class Dict2(dict):
...     def __getitem__(sf, k, /):
...         print('__getitem__', k)
...         return super().__getitem__(k)
...     def __delitem__(sf, k, /):
...         print('__delitem__', k)
...         return super().__delitem__(k)
...     def __setitem__(sf, k, v, /):
...         print('__setitem__', k)
...         return super().__setitem__(k, v)

>>> d2 = Dict2(d)
>>> class Meta(type):
...     @classmethod
...     def __prepare__(sf_as_meta, name, bases, /,**kwargs):
...         d = super().__prepare__(name, bases, **kwargs)
...         assert type(d) is dict
...         d2.update(d)
...         d2[6] = 9
...         return d2
>>> class S(metaclass=Meta):pass
__setitem__ 6
__getitem__ __name__
__setitem__ __module__
__setitem__ __qualname__
>>> S.__dict__[6]
9

上面没有！__getitem__ 6！通过dict而不是通过Dict2！
下面没有！__setitem__ a！通过dict而不是D通过ict2！

>>> s = S()
>>> s.a = 1

#>>> d2
{'a': 1, 6: 9, '__module__': '__main__', '__qualname__': 'S'}
>>> d2['a']
__getitem__ a
1

>>> type(object.__getattribute__(S, '__dict__'))
<class 'mappingproxy'>
>>> type(object.__getattribute__(S, '__dict__')) is MappingProxyType
True




>>> type(inspect.getattr_static(type, '__mro__'))
<class 'member_descriptor'>
>>> type(inspect.getattr_static(type, '__dict__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(type, '__weakref__'))
Traceback (most recent call last):
    ...
AttributeError: __weakref__
>>> type(inspect.getattr_static(type, '__getattribute__'))
<class 'wrapper_descriptor'>

>>> type(inspect.getattr_static(object, '__mro__'))
<class 'member_descriptor'>
>>> type(inspect.getattr_static(object, '__dict__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(object, '__weakref__'))
Traceback (most recent call last):
    ...
AttributeError: __weakref__
>>> type(inspect.getattr_static(object, '__getattribute__'))
<class 'wrapper_descriptor'>

>>> type(inspect.getattr_static(tuple, '__mro__'))
<class 'member_descriptor'>
>>> type(inspect.getattr_static(tuple, '__dict__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(tuple, '__weakref__'))
Traceback (most recent call last):
    ...
AttributeError: __weakref__
>>> type(inspect.getattr_static(tuple, '__getattribute__'))
<class 'wrapper_descriptor'>

>>> type(inspect.getattr_static((), '__mro__'))
Traceback (most recent call last):
    ...
AttributeError: __mro__
>>> type(inspect.getattr_static((), '__dict__'))
Traceback (most recent call last):
    ...
AttributeError: __dict__
>>> type(inspect.getattr_static((), '__weakref__'))
Traceback (most recent call last):
    ...
AttributeError: __weakref__
>>> type(inspect.getattr_static((), '__getattribute__'))
<class 'wrapper_descriptor'>

>>> type(inspect.getattr_static(set(), '__mro__'))
Traceback (most recent call last):
    ...
AttributeError: __mro__
>>> type(inspect.getattr_static(set(), '__dict__'))
Traceback (most recent call last):
    ...
AttributeError: __dict__
>>> type(inspect.getattr_static(set(), '__weakref__'))
Traceback (most recent call last):
    ...
AttributeError: __weakref__
>>> type(inspect.getattr_static(set(), '__getattribute__'))
<class 'wrapper_descriptor'>





>>> class B:
...     __slots__ = ('x',)
>>> class C(B):
...     pass

>>> type(inspect.getattr_static(C(), '__mro__'))
Traceback (most recent call last):
    ...
AttributeError: __mro__
>>> type(inspect.getattr_static(C(), '__dict__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(C(), '__weakref__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(C(), '__getattribute__'))
<class 'wrapper_descriptor'>
>>> type(inspect.getattr_static(C(), '__class__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(C(), 'x'))
<class 'member_descriptor'>



>>> type(inspect.getattr_static(C, 'x'))
<class 'member_descriptor'>
>>> type(inspect.getattr_static(C, '__getattribute__'))
<class 'wrapper_descriptor'>
>>> type(inspect.getattr_static(C, '__weakref__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(C, '__dict__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(C, '__class__'))
<class 'getset_descriptor'>
>>> type(inspect.getattr_static(C, '__mro__'))
<class 'member_descriptor'>


>>> B().x = 4
>>> C().x = 4
>>> C.x = 4
>>> del C.x
>>> C.x.__objclass__ is B
True
>>> C.x.__objclass__ = C
Traceback (most recent call last):
    ...
AttributeError: readonly attribute
>>> type(inspect.getattr_static(C.x, '__objclass__'))
<class 'member_descriptor'>

>>> C.__mro__ = ()
Traceback (most recent call last):
    ...
AttributeError: readonly attribute
>>> C.__dict__ = {}
Traceback (most recent call last):
    ...
AttributeError: attribute '__dict__' of 'type' objects is not writable
>>> C.__class__ = C
Traceback (most recent call last):
    ...
TypeError: __class__ assignment only supported for heap types or ModuleType subclasses


#>>> C.__dict__
mappingproxy({'__module__': '__main__', '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None})
>>> C().__dict__
{}
>>> C().__dict__ = {}
>>> type(C.__dict__['__dict__'])
<class 'getset_descriptor'>
>>> (C.__dict__['__dict__']) is (inspect.getattr_static(C, '__dict__'))
True
>>> (C.__dict__['__dict__']) is (inspect.getattr_static(C(), '__dict__'))
True




>>> from types import MappingProxyType
>>> from types import GetSetDescriptorType
>>> from types import MemberDescriptorType
>>> from types import WrapperDescriptorType

#>>> help(GetSetDescriptorType)
#>>> help(MemberDescriptorType)
#>>> help(WrapperDescriptorType)

>>> GetSetDescriptorType()
Traceback (most recent call last):
    ...
TypeError: cannot create 'getset_descriptor' instances
>>> MemberDescriptorType()
Traceback (most recent call last):
    ...
TypeError: cannot create 'member_descriptor' instances
>>> WrapperDescriptorType(1, 1, 1)
Traceback (most recent call last):
    ...
TypeError: cannot create 'wrapper_descriptor' instances





#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''

    '''.split()

#################################
#HHHHH
#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):



