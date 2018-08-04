
'''
why not _builtins['eval'] = safe_eval??
    safe_eval needs __globals__ to access builtins.eval
    if pass safe_eval as eval to the call, builtins.eval is passed too.
    hence, user can asscess builtins.eval
    ##_builtins['eval'] = safe_eval
    ##safe_eval.__globals__
'''

__all__ = ('literal_eval', 'safe_eval', 'data_eval')

#from .. import get_keys_and_gettor_of_module_or_dict
from ast import literal_eval
#from collections import Mapping
from types import MappingProxyType
import builtins
# NOTE: <built-in function __import__>
from ._safe_eval__details import allows as _allows, forbids as _forbids


literal_eval = literal_eval
data_eval = literal_eval
_global_eval = eval



forbid___bs__ = \
    {'__build_class__'  # remove
    ,'__import__'       # remove
    ,'__loader__'       # remove
    ,'__spec__'         # remove
    }

forbid_bs_callables = \
    {'compile'      # remove
    ,'copyright'    # remove
    ,'credits'      # remove
    ,'delattr'      # remove
    ,'eval'         # remove
    ,'exec'         # remove
    ,'exit'         # remove
    ,'getattr'      # remove
    ,'globals'      # remove
    ,'help'         # remove
    ,'input'        # remove
    ,'license'      # remove
    ,'locals'       # remove
    ,'open'         # remove
    ,'print'        # remove
    ,'quit'         # remove
    ,'setattr'      # remove
    }

_constant_forbids = forbid___bs__ | forbid_bs_callables
if not (_constant_forbids <= _forbids): raise Exception
if _constant_forbids & _allows: raise Exception
del _constant_forbids, forbid___bs__, forbid_bs_callables
del _forbids # use _allows only







#  define  '_globals'
# __builtins__ # sometimes 'dict', sometimes 'module'


_builtins = {name : getattr(builtins, name) for name in _allows}
_builtins = MappingProxyType(_builtins)
_globals = {'__builtins__' : _builtins}
_globals = MappingProxyType(_globals)
del MappingProxyType, builtins, _allows
_globals
#rint(list(globals()))
__builtins__ = _builtins; del _builtins





__builtins__, _global_eval, _global_eval
def safe_eval(expression, locals=None):
    # assume expression cannot setitem in locals
    # but expression can getitem in locals and update it
    #
    if locals is None:
        locals = {}
    return _global_eval(expression, dict(_globals), locals)

# safe_eval needs __globals__ to access eval
# if pass safe_eval as eval to the call, eval is passed too.
##safe_eval.__globals__
##_builtins['eval'] = safe_eval


assert safe_eval('{max(1,2)}') == {2}
assert set(globals()) == {'__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', '__all__', 'literal_eval', 'data_eval', '_global_eval', '_globals', 'safe_eval'}

def _test_safe_eval(exp, name_for_NameError):
    err = "name '{}' is not defined".format(name_for_NameError)
    try:
        safe_eval(exp)
    except NameError as e:
        assert str(e) == err
    else:
        raise Exception('fail _test_safe_eval')
    return

if __name__ == '__main__':
    #assert eval is getattr(safe_eval.__globals__['__builtins__'], 'eval')
    assert safe_eval('(max(1+2, abs(-53), *iter(list(range(57)))),)') == (56,)

    _test_safe_eval("(eval('(print(1),)'),)", 'eval')
    _test_safe_eval('(print(''),)', 'print')
    _test_safe_eval('(exec(''),)', 'exec')


