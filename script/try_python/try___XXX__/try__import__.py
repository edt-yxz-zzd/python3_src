#__all__:goto
r'''[[[
e ../../python3_src/script/try_python/try___XXX__/try__import__.py

script.try_python.try___XXX__.try__import__
py -m nn_ns.app.debug_cmd   script.try_python.try___XXX__.try__import__ -x # -off_defs
py -m nn_ns.app.doctest_cmd script.try_python.try___XXX__.try__import__:__doc__ -ht # -ff -df

[[
窜改__builtins__.__import__,globals()['__import__']都无用...
]]

py_adhoc_call   script.try_python.try___XXX__.try__import__   @f
from script.try_python.try___XXX__.try__import__ import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

__import__
_old_imp = __import__
assert _old_imp is __import__
def _new_imp(*args, **kwds):
    print((args, kwds))
    raise 000
__import__ = _new_imp
assert not _old_imp is __import__
import seed
    #无异常
    #=> 仍使用_old_imp
    #无用

#print(__builtins__)
_old_builtins = __builtins__
_vars4old_builtins = {**(_old_builtins if isinstance(_old_builtins, dict) else vars(_old_builtins))}
class _Builtins:
    __slots__ = ('__dict__', '_kw')
    def __init__(sf, /, **kwds):
        sf._kw = kwds
        #sf._vars = {**_vars4old_builtins, **kwds}
        d = vars(sf) #sf.__dict__
        assert not d
        d.update(_vars4old_builtins)
        d.update(kwds)
    def __dir__(sf, /):
        return sorted(vars(sf))
        return sorted(sf._vars)

#assert __builtins__.__import__ is _old_builtins
    #AttributeError: 'dict' object has no attribute '__import__'.
assert _vars4old_builtins['__import__'] is _old_imp
__builtins__ = _Builtins(__import__=__import__)
assert not __builtins__.__import__ is _old_imp
assert __builtins__.__import__ is __import__ is _new_imp

import seed
    #无异常
    #=> 仍使用_old_imp
    #无用



__all__
from script.try_python.try___XXX__.try__import__ import *
