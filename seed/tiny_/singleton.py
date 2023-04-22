#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/singleton.py

py -m nn_ns.app.debug_cmd seed.tiny_.singleton
py -m seed.tiny_.singleton
py -m nn_ns.app.debug_cmd

from seed.tiny_.singleton import mk_SingletonClass, mk_existing_type_singleton
from seed.tiny_.singleton import __newobj__, __new4singleton__

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL
#]]]'''
__all__ = r'''
mk_SingletonClass
mk_existing_type_singleton
__newobj__
__new4singleton__

'''.split()#'''
__all__


if __name__ == "__main__":
    from seed.tiny_.singleton import mk_SingletonClass, mk_existing_type_singleton
    from seed.tiny_.singleton import __newobj__, __new4singleton__
    #####
    #from seed.tiny_.singleton import __name__
    #import __main__
    #assert __main__.__name__ == __name__
    #del __main__


from seed.tiny import null_frozenset
from seed.helper.repr_input import repr_helper
from seed.debug.expectError import expectError
import pickle
from seed.tiny_.check import check_type_le, check_type_is
__newobj__ = None.__reduce_ex__(2)[0]
def mk_SingletonClass(module_qname, type_qname, /, *bases, **kw):
    check_type_is(str, module_qname)
    check_type_is(str, type_qname)
    class Singleton(*bases, **kw):
        __slots__ = ()
            #data_on_cls_instead_sf
        def __repr__(sf, /):
            return repr_helper(sf)
        def __reduce__(sf, /):
            #pickle
            cls = type(sf)
            return (__newobj__, (cls,))
        __eq__ = object.__eq__
        __ne__ = object.__ne__
        __hash__ = object.__hash__
        def __new__(cls, /):
            return __new4singleton__(__class__, cls)
        def __init_subclass__(cls, /):
            raise TypeError(cls)
    Singleton.__module__ = module_qname
    Singleton.__qualname__ = type_qname
    (_,_,Singleton.__name__) = type_qname.rpartition('.')
    return Singleton

def __new4singleton__(__class__, cls, /):
    r'''
usage:see:mk_SingletonClass, mk_existing_type_singleton
    '''#'''
    if cls is not __class__: raise TypeError((__class__, cls))
    try:
        return cls.__dict__['__sf']
        return cls.__sf
    #except AttributeError:
    except KeyError:
        sf = super(__class__, cls).__new__(cls)
        if not type(sf) is cls: raise TypeError((type(sf), cls))
        cls.__sf = sf
        try:
            _sf = cls()
            if not _sf is sf: raise TypeError(cls)
        except:
            del cls.__sf
            raise

        cls.__abstractmethods__ = (1,)
        return cls()
from seed.tiny_.singleton import mk_SingletonClass
from seed.tiny_.singleton import __newobj__, __new4singleton__
_C = mk_SingletonClass('pkg.mm', 'xxx.C', dict)
assert _C.__module__ == 'pkg.mm'
assert _C.__qualname__ == 'xxx.C'
assert _C.__name__ == 'C'
assert repr(_C()) == 'C()', repr(_C())
assert _C.__eq__ is object.__eq__
assert _C.__ne__ is object.__ne__
assert _C.__hash__ is object.__hash__
try:
    assert pickle.dumps(_C()) == b'', pickle.dumps(_C())
except pickle.PicklingError as e:
    assert e.args == ("Can't pickle <class 'pkg.mm.xxx.C'>: import of module 'pkg.mm' failed",)
    pass
_C = mk_SingletonClass(__name__, 'xxx.C', dict)
try:
    assert pickle.dumps(_C()) == b'', pickle.dumps(_C())
except pickle.PicklingError as e:
    assert e.args == ("Can't pickle <class '__main__.xxx.C'>: attribute lookup xxx.C on __main__ failed".replace('__main__', __name__),), e.args
    pass
if not __name__ == "__main__":
    class xxx:
        C = _C
    assert pickle.dumps(_C()) == b'\x80\x04\x95%\x00\x00\x00\x00\x00\x00\x00\x8c\x14seed.tiny_.singleton\x94\x8c\x05xxx.C\x94\x93\x94)\x81\x94.'
    del xxx
_C()
assert _C() is _C()
assert expectError(TypeError, lambda:object.__new__(_C))
try:
    object.__new__(_C)
except TypeError:
    pass
else:
    raise logic-err
_C #used in mk_existing_type_singleton
assert sorted(_C.__dict__) == ['__abstractmethods__', '__doc__', '__eq__', '__hash__', '__init_subclass__', '__module__', '__ne__', '__new__', '__reduce__', '__repr__', '__sf', '__slots__'], sorted(_C.__dict__)
_nms4singleton = ('__eq__', '__hash__', '__init_subclass__', '__ne__', '__reduce__', '__repr__')
_spec_nms4singleton = ('__abstractmethods__', '__new__', '__sf')
_ot_nms = ('__doc__', '__module__', '__slots__')
assert {*_C.__dict__} == {*_nms4singleton, *_spec_nms4singleton, *_ot_nms}
assert len(_C.__dict__) == len(_nms4singleton) + len(_spec_nms4singleton) + len(_ot_nms)
def mk_existing_type_singleton(__class__, /):
    check_type_le(type, __class__)
    if __class__.__slots__: raise TypeError(__class__)
    if __class__.__dict__['__slots__']: raise TypeError(__class__)
    __abstractmethods__ = getattr(__class__, '__abstractmethods__', set())
    if __abstractmethods__:
        if not __abstractmethods__ <= {*_nms4singleton}: raise TypeError((__class__, __abstractmethods__))
        __class__.__abstractmethods__ = null_frozenset

    def _():
        for nm in _nms4singleton:
            #bug:setattr(__class__, nm, _C.__dict__[nm])
            #   __class__() ==>> TypeError: sequence item 0: expected str instance, int found
            #       descriptor bug? No, cause by __abstractmethods__!!!
            #
            if not nm == '__abstractmethods__':
                setattr(__class__, nm, getattr(_C, nm))
    #__class__.__sf = __class__() #before _()~__abstractmethods__ setted
    _()
    del _
    #__class__.__repr__ = _C.__repr__
        #fail if only update __dict__
        #   repr() bypass _C.__dict__

    #using:__class__
    def __new__(cls, /):
        return __new4singleton__(__class__, cls)
    __class__.__new__ = __new__
    assert _spec_nms4singleton == ('__abstractmethods__', '__new__', '__sf')
    #del __class__.__abstractmethods__
    assert not getattr(__class__, '__abstractmethods__', 0)
    __class__()
    assert getattr(__class__, '__abstractmethods__', 0)
    __class__.__new__(__class__)
    __new__(__class__)
    __class__.__new__(__class__)
    assert __class__() is __class__() is __class__.__sf
    assert expectError(TypeError, lambda:object.__new__(__class__))
from seed.tiny_.singleton import mk_existing_type_singleton


class _D:
    __slots__ = ()
_D()
mk_existing_type_singleton(_D)

assert _D.__module__ == __name__
assert _D.__qualname__ == '_D'
assert _D.__name__ == '_D'
assert repr(_D()) == '_D()', repr(_D())
if not __name__ == "__main__":
    assert pickle.dumps(_D()) == b'\x80\x04\x95"\x00\x00\x00\x00\x00\x00\x00\x8c\x14seed.tiny_.singleton\x94\x8c\x02_D\x94\x93\x94)\x81\x94.', pickle.dumps(_D())
_D()
assert _D() is _D()
assert expectError(TypeError, lambda:object.__new__(_D))
try:
    object.__new__(_D)
except TypeError:
    pass
else:
    raise logic-err

from seed.tiny_.singleton import mk_SingletonClass, mk_existing_type_singleton
from seed.tiny_.singleton import __newobj__, __new4singleton__

