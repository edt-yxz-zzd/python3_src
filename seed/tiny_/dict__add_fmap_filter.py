r'''
py -m nn_ns.app.debug_cmd   seed.tiny_.dict__add_fmap_filter
seed.tiny_.dict__add_fmap_filter
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, group4dict_value



#'''

__all__ = '''
    fmap4dict_value
    filter4dict_value
    group4dict_value

    dict_add__is
    dict_add__eq
    '''.split()

from seed.debug.expectError import expectError



def fmap4dict_value(f, d, /):
    return {k:f(v) for k, v in d.items()}
def filter4dict_value(f, d, /):
    return {k:v for k, v in d.items() if f(v)}
assert fmap4dict_value(bool, {0: 0, 1: 1}) == {0: False, 1: True}
assert filter4dict_value(bool, {0: 0, 1: 1}) == {1: 1}

def dict_add__is(d, k, v, /):
    _v = d.setdefault(k, v)
    if 0b00:
        if not (_v is v):
            print(v)
            print(_v)
            raise ValueError
    else:
        if not (_v is v): raise ValueError
    return
def dict_add__eq(d, k, v, /):
    _v = d.setdefault(k, v)
    if not (_v is v or _v == v): raise ValueError
    return
assert expectError(ValueError, lambda:dict_add__eq({1: 2}, 1, 3))
assert not expectError(ValueError, lambda:dict_add__eq({1: []}, 1, []))

assert expectError(ValueError, lambda:dict_add__is({1: 2}, 1, 3))
assert expectError(ValueError, lambda:dict_add__is({1: []}, 1, []))
assert not expectError(ValueError, lambda:dict_add__is({1: True}, 1, True))




def group4dict_value(f, d, /):
    #partition4dict_value??
    g2k2v = group2part = {}
    for k, v in d.items():
        g = f(v)
        k2v = g2k2v.setdefault(g, {})
        k2v[k] = v
    return g2k2v

assert group4dict_value(len, {-1:'', -2:'', -3:'a', -4:'xx', -5:'b'}) == {0:{-1:'', -2:''}, 1:{-3:'a', -5:'b'}, 2:{-4:'xx'}}


