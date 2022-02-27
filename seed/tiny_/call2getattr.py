
r'''
seed.tiny_.call2getattr
py -m seed.tiny_.call2getattr
py -m nn_ns.app.debug_cmd   seed.tiny_.call2getattr
e ../../python3_src/seed/tiny_/call2getattr.py

from seed.tiny_.call2getattr import get5cls, call5cls, get5cls_, call5cls_, Call2GetAttrs, IGetAttr8Call, Call2GetAttr, interpreter4Call2GetAttr__unpack_and_call, interpreter4Call2GetAttr__MethodType

>>> get5cls.__getitem__([1])(0)
1
>>> call5cls.__getitem__([1], 0)
1
>>> get5cls_('__getitem__', [1])(0)
1
>>> call5cls_('__getitem__', [1], 0)
1


>>> class List(list):pass
>>> ls = List([1])
>>> ls.__getitem__ = -1
>>> get5cls.__getitem__(ls)(0)
1
>>> call5cls.__getitem__(ls, 0)
1
>>> get5cls_('__getitem__', ls)(0)
1
>>> call5cls_('__getitem__', ls, 0)
1

#'''

__all__ = r'''
    get5cls
    call5cls
        get5cls_
        call5cls_

    Call2GetAttrs
    IGetAttr8Call
        Call2GetAttr
            interpreter4Call2GetAttr__unpack_and_call
            interpreter4Call2GetAttr__MethodType
    '''.split()

from types import MethodType


_oget = object.__getattribute__
class Call2GetAttrs:
    r'''
    call :: args4temple -> [name] -> args4call -> kwargs4call -> result
    deepL_names = ()|(deepL_names, name)
    #'''
    def __init__(sf, call, args4temple, deepL_names, /):
        assert callable(call)
        assert type(args4temple) is tuple
        assert type(deepL_names) is tuple
        sf._f = call
        sf._t = args4temple
        sf._p = deepL_names
        #sf._s = names

    def _get_names(sf, /):
        #bug:s = _oget(sf, '_s', None)
        try:
            s = _oget(sf, '_s')
        except AttributeError:
            ls = []
            p = _oget(sf, '_p')
            while p:
                p, x = p
                ls.append(x)
            sf._s = (*reversed(ls),)
            s = _oget(sf, '_s')
        assert type(s) is tuple
        return s

    def __getattribute__(sf, name, /):
        f = _oget(sf, '_f')
        t = _oget(sf, '_t')
        p = _oget(sf, '_p')
        return __class__(f, t, (p, name))
    def __call__(sf, /, *args4call, **kwargs4call):
        f = _oget(sf, '_f')
        t = _oget(sf, '_t')
        s = _oget(sf, '_get_names')()
        return f(t, s, args4call, kwargs4call)
def _echo4Call2GetAttrs(args4temple, names, args4call, kwargs4call):
    return (args4temple, names, args4call, kwargs4call)
assert Call2GetAttrs(_echo4Call2GetAttrs, (99, 88), ((), 'd')).c.b(77, a=66) == ((99, 88), ('d', 'c', 'b'), (77,), {'a': 66})

class IGetAttr8Call:
    __slots__ = ()
    def __getattribute__(sf, name, /):
        return sf(name)
    def __call__(sf, name, /):
        raise NotImplementedError


class Call2GetAttr(IGetAttr8Call):
    r'''
    call :: args4temple -> name -> result
    #'''

    def __init__(sf, call, args4temple, /):
        assert callable(call)
        assert type(args4temple) is tuple
        sf._f = call
        sf._t = args4temple

    def __call__(sf, name, /):
        f = _oget(sf, '_f')
        t = _oget(sf, '_t')
        return f(t, name)

def _flip_MethodType(name, f, /):
    return MethodType(f, name)
def interpreter4Call2GetAttr__unpack_and_call(args4temple, name, /):
    [f, *ls] = args4temple
    return f(*ls, name)
def interpreter4Call2GetAttr__MethodType(args4temple, name, /):
    [f] = args4temple
    return MethodType(f, name)

def get5cls_(name, sf, /, *tmay_default):
    r''' only for special instance method
        #avoid classmethod/staticmethod

    call5cls.__xxx__(sf, *args, **kwargs)
    get5cls.__xxx__(sf, *tmay_default)(*args, **kwargs)

    #'''
    f = getattr(type(sf), name, *tmay_default)
    return MethodType(f, sf)
def call5cls_(name, sf, /, *args, **kwargs):
    f = getattr(type(sf), name)
    return f(sf, *args, **kwargs)
    return get5cls_(name, sf)(*args, **kwargs)
#get5cls = Call2GetAttr(get5cls_, ())
#get5cls = Call2GetAttr(MethodType, (get5cls_,))
#get5cls = Call2GetAttr(_flip_MethodType, (get5cls_,))
get5cls = Call2GetAttr(interpreter4Call2GetAttr__MethodType, (get5cls_,))
#call5cls = Call2GetAttr(call5cls_, ())
#call5cls = Call2GetAttr(_flip_MethodType, (call5cls_,))
call5cls = Call2GetAttr(interpreter4Call2GetAttr__MethodType, (call5cls_,))


assert get5cls.__getitem__([1])(0) == 1
assert call5cls.__getitem__([1], 0) == 1
assert get5cls_('__getitem__', [1])(0) == 1
assert call5cls_('__getitem__', [1], 0) == 1


from seed.tiny_.call2getattr import get5cls, call5cls, get5cls_, call5cls_, Call2GetAttrs, IGetAttr8Call, Call2GetAttr, interpreter4Call2GetAttr__unpack_and_call, interpreter4Call2GetAttr__MethodType
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


