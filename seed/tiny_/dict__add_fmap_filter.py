r'''
py -m nn_ns.app.debug_cmd   seed.tiny_.dict__add_fmap_filter
seed.tiny_.dict__add_fmap_filter
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, dict_add__new, group4dict_value
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value_with_key, filter4dict_value_with_key, group4dict_value_with_key, filter4dict_item, group4dict_item

see:
    from seed.mapping_tools.dict_op import inv__k2v_to_v2k, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks



#'''

__all__ = '''
    fmap4dict_value
    filter4dict_value
    group4dict_value

    fmap4dict_value_with_key
    filter4dict_value_with_key
    group4dict_value_with_key
        filter4dict_item
        group4dict_item

    dict_add__is
    dict_add__eq
    dict_add__new
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
            raise ValueError((k, _v, v))
    else:
        if not (_v is v): raise ValueError((k, _v, v))
    return
def dict_add__eq(d, k, v, /):
    _v = d.setdefault(k, v)
    if not (_v is v or _v == v): raise ValueError((k, _v, v))
    return
def dict_add__new(d, k, v, /):
    sz = len(d)
    _v = d.setdefault(k, v)
    if not (sz+1 == len(d)): raise ValueError((k, _v, v))
    return

assert expectError(ValueError, lambda:dict_add__eq({1: 2}, 1, 3))
assert not expectError(ValueError, lambda:dict_add__eq({1: []}, 1, []))

assert expectError(ValueError, lambda:dict_add__is({1: 2}, 1, 3))
assert expectError(ValueError, lambda:dict_add__is({1: []}, 1, []))
assert not expectError(ValueError, lambda:dict_add__is({1: True}, 1, True))

assert expectError(ValueError, lambda:dict_add__new({1: 2}, 1, 3))
assert expectError(ValueError, lambda:dict_add__new({1: []}, 1, []))
assert expectError(ValueError, lambda:dict_add__new({1: True}, 1, True))
assert not expectError(ValueError, lambda:dict_add__new({1: True}, 0, True))
assert not expectError(ValueError, lambda:dict_add__new({1: True}, 0, 0))




def group4dict_value(f, d, /):
    #partition4dict_value??
    g2k2v = group2part = {}
    for k, v in d.items():
        g = f(v)
        k2v = g2k2v.setdefault(g, {})
        k2v[k] = v
    return g2k2v

assert group4dict_value(len, {-1:'', -2:'', -3:'a', -4:'xx', -5:'b'}) == {0:{-1:'', -2:''}, 1:{-3:'a', -5:'b'}, 2:{-4:'xx'}}

def fmap4dict_value_with_key(f, d, /):
    return {k:f(k,v) for k, v in d.items()}
def group4dict_value_with_key(f, d, /):
    #partition4dict_value??
    g2k2v = group2part = {}
    for k, v in d.items():
        g = f(k,v)
        k2v = g2k2v.setdefault(g, {})
        k2v[k] = v
    return g2k2v
group4dict_item = group4dict_value_with_key

def filter4dict_value_with_key(f, d, /):
    return {k:v for k, v in d.items() if f(k,v)}
filter4dict_item = filter4dict_value_with_key

