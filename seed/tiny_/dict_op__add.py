#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/dict_op__add.py

seed.tiny_.dict_op__add
py -m nn_ns.app.debug_cmd   seed.tiny_.dict_op__add -x
py -m nn_ns.app.doctest_cmd seed.tiny_.dict_op__add:__doc__ -ht

>>> d = {}
>>> dict_add(d, 333, 666)
True
>>> dict_add(d, 333, 666)
False
>>> dict_add(d, 222, 555)
True
>>> dict_add(d, 222, 444)
False
>>> dict_add(d, 222, 444)
False
>>> dict_add(d, 333, 666)
False

>>> s = {333}
>>> set_add(s, 333)
False
>>> set_add(s, 666)
True
>>> set_add(s, 666)
False

>>> d = {}
>>> dict_update(d, {})
True
>>> dict_update(d, {})
True
>>> dict_update(d, {222:111,333:444})
True
>>> dict_update(d, {555:111,666:444})
True
>>> dict_update(d, {555:111,777:444})
False
>>> dict_update(d, {777:444})
False


>>> s = {444}
>>> set_update(s, {})
True
>>> set_update(s, {})
True
>>> set_update(s, {222,333})
True
>>> set_update(s, {555,666})
True
>>> set_update(s, {555,777})
False
>>> set_update(s, {777})
False
>>> set_update(s, {444,111})
False




#]]]'''
__all__ = r'''
dict_add
set_add

dict_update
set_update
'''.split()#'''
__all__

def dict_add(d, k, v, /):
    '-> is_new_key/bool'
    sz = len(d)
    #x = d.setdefault(k, v)
    d[k] = v
    return not sz == len(d)
def set_add(s, k, /):
    '-> is_new_key/bool'
    sz = len(s)
    s.add(k)
    return not sz == len(s)


def dict_update(d, d2, /):
    '-> are_all_new_keys/bool'
    sz = len(d)
    sz2 = len(d2)
    d.update(d2)
    return sz+sz2 == len(d)
def set_update(s, s2, /):
    '-> are_all_new_keys/bool'
    sz = len(s)
    sz2 = len(s2)
    s.update(s2)
    return sz+sz2 == len(s)

__all__
from seed.tiny_.dict_op__add import dict_add, set_add, dict_update, set_update
from seed.tiny_.dict_op__add import *
