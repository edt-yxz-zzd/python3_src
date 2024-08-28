#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/_Base4repr.py

seed.tiny_._Base4repr
py -m nn_ns.app.debug_cmd   seed.tiny_._Base4repr -x
#]]]'''
__all__ = r'''
_Base4repr
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

class _Base4repr:
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    def __init__(sf, /, *_args4repr):
        sf._args4repr = _args4repr
        #subclass:
        #_Base4repr.__init__(sf, ...)
        #sf._args4repr = (...)



__all__
from seed.tiny_._Base4repr import _Base4repr #sf._args4repr = (...)
from seed.tiny_._Base4repr import *
