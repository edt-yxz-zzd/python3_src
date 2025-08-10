#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/_Base4repr.py

seed.tiny_._Base4repr
py -m nn_ns.app.debug_cmd   seed.tiny_._Base4repr -x
#]]]'''
__all__ = r'''
_Base4repr
'''.split()#'''
    #_Base4repr_ex
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from seed.helper.repr_input import repr_helper
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
___end_mark_of_excluded_global_names__0___ = ...

class _Base4repr:
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr, **getattr(sf, '_kwds4repr', {}))
    def __init__(sf, /, *_args4repr, **_kwds4repr):
        sf._reset4repr(_args4repr, _kwds4repr)
        #subclass:
        #_Base4repr.__init__(sf, ...)
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
        ######################
        # !! ++ _Base4repr._kwds4repr:should overwrite both at once
        #below deprecated:
        #   #sf._args4repr = (...)
        #   #if 0:sf._kwds4repr = {...}
        ######################
    def _init4repr(sf, /, *_args4repr, **_kwds4repr):
        sf._reset4repr(_args4repr, _kwds4repr)
    def _reset4repr(sf, may_args4repr, may_kwds4repr=None, /):
        _args4repr = null_tuple if may_args4repr is None else may_args4repr
        _kwds4repr = {} if may_kwds4repr is None else may_kwds4repr

        _args4repr[:0]
        _kwds4repr.items

        _args4repr = null_tuple if not _args4repr else _args4repr
        sf._args4repr = _args4repr
        sf._kwds4repr = _kwds4repr
        if not _kwds4repr:
            del sf._kwds4repr
null_tuple = ()
#.class _Base4repr_ex:
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *sf._args4repr_ex, **sf._kwds4repr_ex)
#.    def __init__(sf, /, *args, **kwds):
#.        sf._args4repr_ex = args
#.        sf._kwds4repr_ex = kwds
#.        #subclass:
#.        #_Base4repr_ex.__init__(sf, ...)
#.        #sf._args4repr_ex = (...)
#.        #sf._kwds4repr_ex = {...}
#.

#from seed.tiny_._Base4repr import _Base4repr_ex
        #sf._args4repr_ex = (...)
        #sf._kwds4repr_ex = {...}

assert repr(_Base4repr()) == '_Base4repr()'
assert repr(_Base4repr(1)) == '_Base4repr(1)'
assert repr(_Base4repr(1, 2)) == '_Base4repr(1, 2)'
assert repr(_Base4repr(a = 1)) == '_Base4repr(a = 1)'
assert repr(_Base4repr(a = 1, b = 2)) == '_Base4repr(a = 1, b = 2)'
__all__
from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
from seed.tiny_._Base4repr import *
