#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.hierarchy.symbol.PrivateSymbol
py -m    seed.hierarchy.symbol.PrivateSymbol
py -m nn_ns.app.debug_cmd   seed.hierarchy.symbol.PrivateSymbol


mkdir ../../python3_src/seed/hierarchy/symbol/
py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/hierarchy/symbol/PrivateSymbol.py
e ../../python3_src/seed/hierarchy/symbol/PrivateSymbol.py


from seed.hierarchy.symbol.PrivateSymbol import PrivateSymbol

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    PrivateSymbol

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById # BaseAddrAsHash, le_AddrAsHash
from seed.helper.repr_input import repr_helper
r"""
import ...
#"""
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#PrivateSymbol:goto
#zzzwww:goto

#[[[PrivateSymbol:begin

class PrivateSymbol(EqById, str):
    r'''
>>> import weakref

>>> PrivateSymbol('xxx')
PrivateSymbol('xxx')
>>> PrivateSymbol('xxx') is PrivateSymbol('xxx')
False
>>> PrivateSymbol('xxx') == PrivateSymbol('xxx')
False

>>> ('xxx') == PrivateSymbol('xxx')
False
>>> PrivateSymbol('xxx') == ('xxx')
False
>>> str(PrivateSymbol('xxx'))
'xxx'

>>> hash(PrivateSymbol('xxx')) is not None
True
>>> weakref.ref(PrivateSymbol('xxx')) is not None
True
>>> PrivateSymbol('xxx').kkk = 1
>>> xxx = PrivateSymbol('xxx', b=1, a=2)
>>> xxx.c = -3
>>> xxx.a = -2
>>> str(xxx)
'xxx'
>>> xxx
PrivateSymbol('xxx', a = -2, b = 1, c = -3)

#if 0: PrivateSymbol('xxx', a = 2, b = 1)

>>> xxx.a
-2
>>> xxx.b
1
>>> xxx.c
-3
>>> setattr(PrivateSymbol, xxx, 333)
>>> getattr(PrivateSymbol, 'xxx', 222)
333
>>> xxx in (PrivateSymbol.__dict__)
False
>>> 'xxx' in (PrivateSymbol.__dict__)
True

#>>> sorted(PrivateSymbol.__dict__)
['__abstractmethods__', '__dict__', '__doc__', '__module__', '__new__', '__repr__', '__slots__', '__weakref__', '_abc_impl', 'xxx']

>>> class XXX(EqById):
...     __slots__ = ()
...     def __str__(sf, /):
...         return 'xxx'
>>> xxx2 = XXX()
>>> str(xxx2)
'xxx'
>>> hash(xxx2) == hash(hash(xxx2))
True
>>> xxx2.__hash__() == (id(xxx2))
False
>>> xxx2.__hash__() == object.__hash__(xxx2)
True
>>> setattr(PrivateSymbol, xxx2, 333)
Traceback (most recent call last):
    ...
TypeError: attribute name must be string, not 'XXX'

>>> class YYY(EqById, str):
...     __slots__ = ()
...     def __str__(sf, /):
...         return 'xxx'
>>> yyy = YYY('yyy')
>>> str(yyy)
'xxx'
>>> setattr(PrivateSymbol, yyy, 333)
>>> yyy in PrivateSymbol.__dict__
False
>>> 'yyy' in PrivateSymbol.__dict__
True

>>> class Z:
...     def __getattribute__(sf, attr, /):
...         return attr
>>> z = Z()
>>> getattr(z, 999, 111)
Traceback (most recent call last):
    ...
TypeError: getattr(): attribute name must be string
>>> getattr(z, xxx, 111) is xxx #not check is_str but isinstance<str>
True
>>> str(xxx) == xxx
False
>>> xxx == str(xxx)
False
>>> zzz = PrivateSymbol(' ')
>>> getattr(z, zzz, 111) is zzz #not check isidentifier
True


>>> PrivateSymbol('description', __doc__ = '???', __isabstractmethod__ = True)
PrivateSymbol('description', __doc__ = '???', __isabstractmethod__ = True)


    #'''
    __slots__ = ('__weakref__', '__dict__')
    def __new__(cls, description, /, **kwargs):
        if not type(description) is str: raise TypeError
        sf = super(__class__, cls).__new__(cls, description)
        if 0:
            if kwargs:
                sf.__dict__[_symbol4kwargs4PrivateSymbol] = kwargs
        else:
            sf.__dict__.update(kwargs)
        return sf
    if 0:
        def __getattr__(sf, attr, /):
            kwargs = sf.__dict__.get(_symbol4kwargs4PrivateSymbol, {})
            if attr in kwargs:
                return kwargs[attr]
            return super().__getattr__(sf, attr)
        def __setattr__(sf, attr, x, /):
            kwargs = sf.__dict__.get(_symbol4kwargs4PrivateSymbol, {})
            if attr in kwargs:
                kwargs[attr] = x
                return
            else:
                return super().__setattr__(sf, attr, x)
    def __repr__(sf, /):
        if 0:
            kwargs = sf.__dict__.get(_symbol4kwargs4PrivateSymbol, {})
        else:
            kwargs = {k:v for k, v in sf.__dict__.items() if type(k) is str and k.isidentifier()}
        return repr_helper(sf, str(sf), **kwargs)
        return (f'{type(sf).__name__!s}({str(sf)!r})')
_symbol4kwargs4PrivateSymbol = PrivateSymbol('symbol4kwargs4PrivateSymbol')

#]]]PrivateSymbol:end

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


