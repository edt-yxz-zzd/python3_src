
r'''
from seed.tiny_.get_mro import get_mro4cls, get_dict4cls, get_dict4obj, iter_cls_member_pairs_in_mro_at

e ../../python3_src/seed/tiny_/get_mro.py
e ../../python3_src/seed/lang/apply_descriptor_protocol.py
#'''

__all__ = '''
    get_mro4cls
    get_dict4cls
    get_dict4obj
    iter_cls_member_pairs_in_mro_at
    '''.split()

_tget = type.__getattribute__
_oget = object.__getattribute__
def get_mro4cls(cls, /):
    return _tget(cls, '__mro__')
def get_dict4cls(cls, /):
    return _tget(cls, '__dict__')
def get_dict4obj(obj, /):
    return _oget(obj, '__dict__')

def _g(C, x, /):
    return x
def _h(C, x, /):
    cls = type(x)
    try:
        f = cls.__get__
    except AttributeError:
        #x is not descriptor
        pass #return x
    else:
        #x is descriptor
        x = f(x, None, C)
    return x

def iter_cls_member_pairs_in_mro_at(cls, name, /, *, apply_descriptor_protocol:bool):
    '-> iter (Type, member)'
    if (apply_descriptor_protocol):
        f = _h
    else:
        f = _g
    mro = get_mro4cls(cls)
    for C in mro:
        d = get_dict4cls(C)
        if name in d:
            member = d[name]
            member = f(C, member)
            yield C, member



from seed.tiny_.get_mro import get_mro4cls, get_dict4cls, get_dict4obj, iter_cls_member_pairs_in_mro_at

