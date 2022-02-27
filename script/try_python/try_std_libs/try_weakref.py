#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
e ../../python3_src/script/try_python/try_std_libs/try_weakref.py

script.try_python.try_std_libs.try_weakref
py -m    script.try_python.try_std_libs.try_weakref
py -m nn_ns.app.debug_cmd   script.try_python.try_std_libs.try_weakref

from script.try_python.try_std_libs.try_weakref import ...

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto


#[[[doctest_examples:begin
#>>> weakref.ref()
>>> import weakref
>>> weakref.ref(None)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'NoneType' object
>>> weakref.ref(True)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'bool' object
>>> weakref.ref(...)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'ellipsis' object
>>> weakref.ref(NotImplemented)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'NotImplementedType' object
>>> weakref.ref(())
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'tuple' object
>>> weakref.ref([])
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'list' object
>>> weakref.ref({})
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'dict' object
>>> weakref.ref(object())
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'object' object
>>> _ = weakref.ref(set())
>>> _ = weakref.ref(frozenset())

>>> class C:
...     __slots__ = ()
>>> weakref.ref(C())
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'C' object
>>> class C:
...     __slots__ = ('__weakref__',)
>>> _ = weakref.ref(C())
>>> c = C()
>>> None is c.__weakref__
True
>>> w1 = weakref.ref(c)
>>> w1 is weakref.ref(c) is c.__weakref__ is not None
True
>>> w1() is c
True
>>> weakref.ref(w1)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'weakref' object

#>>> import sys
#>>> sys.stderr = sys.stdout
#>>> w2 = weakref.ref(c, lambda *args, **kwargs:print('del c'))
>>> ls = []
>>> w2 = weakref.ref(c, lambda x:ls.append(id(x)))
>>> w2 == w1
True
>>> w2 is w1
False
>>> w2 is not w1 is c.__weakref__
True
>>> w2() is c is w1()
True
>>> id_w1 = id(w1)
>>> id_w2 = id(w2)
>>> id_c = id(c)
>>> id_w2 != id_w1
True
>>> del w1
>>> c.__weakref__ is None
False
>>> w2 is c.__weakref__ is not None
True
>>> id(c.__weakref__) == id_w2
True
>>> del w2
>>> c.__weakref__ is None
True
>>> ls
[]
>>> del c #w2 deleted, no callback!
>>> ls
[]

>>> c = C()
>>> f = lambda x:ls.append([id(x), x()])
>>> w3 = weakref.ref(c, f)
>>> w3 is c.__weakref__ is not None
True
>>> w4 = weakref.ref(c)
>>> w3 is not c.__weakref__ is w4 is not None
True
>>> w4 == w3
True
>>> w4() is c is w3() is not None #alive
True
>>> w4.__callback__ is None
True
>>> w3.__callback__ is f
True
>>> ls
[]
>>> del c #w3 exists!
>>> ls == [[id(w3), None]]
True
>>> w4.__callback__ is None is w3.__callback__
True
>>> w4() is None is w3() #dead
True
>>> w3 == w3 != w4
True
>>> w3.xxx = 1
Traceback (most recent call last):
    ...
AttributeError: 'weakref' object has no attribute 'xxx'



#WeakKeyDictionary by eq not by id
>>> class C:
...     __slots__ = ('__weakref__',)
...     __hash__ = None
>>> _ = weakref.ref(C())
>>> c = C()
>>> d = weakref.WeakKeyDictionary()
>>> d[c] = 1
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'C'
>>> class C:
...     __slots__ = ('__weakref__',)
...     __eq__ = None
...     __ne__ = None
...     __hash__ = object.__hash__
>>> _ = weakref.ref(C())
>>> c = C()
>>> d = weakref.WeakKeyDictionary()
>>> d[c] = 1
>>> d[c] = 2
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object is not callable

>>> class C:
...     __slots__ = ('__weakref__',)
...     def __eq__(a, b): return True
...     def __hash__(_): return 0
>>> c1 = C()
>>> c2 = C()
>>> c1 is not c2
True
>>> weakref.ref(c1) == weakref.ref(c2)
True
>>> d = weakref.WeakKeyDictionary()
>>> d[c1] = 1
>>> d[c2] = 2
>>> d[c1]
2
>>> d[c2]
2
>>> [k] = d
>>> k is c1
True









>>> weakref.ref({})
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'dict' object
>>> class D(dict):
...     __slots__ = ('__weakref__',)
>>> d = D()
>>> w_d = weakref.ref(d)
>>> class T(tuple):
...     __slots__ = ('__weakref__',)
Traceback (most recent call last):
    ...
TypeError: nonempty __slots__ not supported for subtype of 'tuple'
>>> class T(tuple):pass
>>> t = T()
>>> w_t = weakref.ref(t)
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'T' object
>>> class X(list):
...     __slots__ = ('__weakref__',)
>>> x = X()
>>> w_x = weakref.ref(x)
>>> class X(str):
...     __slots__ = ('__weakref__',)
>>> x = X()
>>> w_x = weakref.ref(x)
>>> class X(bytes):
...     __slots__ = ('__weakref__',)
Traceback (most recent call last):
    ...
TypeError: nonempty __slots__ not supported for subtype of 'bytes'
>>> class X(int):
...     __slots__ = ('__weakref__',)
Traceback (most recent call last):
    ...
TypeError: nonempty __slots__ not supported for subtype of 'int'
>>> class X(bool):
...     __slots__ = ('__weakref__',)
Traceback (most recent call last):
    ...
TypeError: type 'bool' is not an acceptable base type


>>> class X:pass
>>> x = X()
>>> w_x = weakref.ref(x)
>>> x.__weakref__ = 1
Traceback (most recent call last):
    ...
AttributeError: attribute '__weakref__' of 'X' objects is not writable
>>> del x.__weakref__
Traceback (most recent call last):
    ...
AttributeError: attribute '__weakref__' of 'X' objects is not writable
>>> x.__dict__ = {} # ok
>>> del x.__dict__ # ok
>>> x.__dict__ = 1
Traceback (most recent call last):
    ...
TypeError: __dict__ must be set to a dictionary, not a 'int'

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



