#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/check_container.py


seed.tiny_.check_container
py -m nn_ns.app.debug_cmd   seed.tiny_.check_container -x
py -m nn_ns.app.doctest_cmd seed.tiny_.check_container:__doc__ -ht
py_adhoc_call   seed.tiny_.check_container   @f
from seed.tiny_.check_container import *
#]]]'''
__all__ = r'''
is_mapping
    check_mapping
'''.split()#'''
__all__



from collections.abc import Mapping

def is_mapping(d, /):
    return isinstance(d, Mapping)
def check_mapping(d, /):
    if not is_mapping(d):raise TypeError(type(d))

__all__
from seed.tiny_.check_container import is_mapping, check_mapping
from seed.tiny_.check_container import *
