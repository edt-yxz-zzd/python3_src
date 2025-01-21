
r'''
===
@20250118: ++kw:using_extended_globals

===
why not _builtins['eval'] = safe_eval??
    safe_eval needs __globals__ to access builtins.eval
    if pass safe_eval as eval to the call, builtins.eval is passed too.
    hence, user can asscess builtins.eval
    ##_builtins['eval'] = safe_eval
    ##safe_eval.__globals__

safe_eval/safe_exec vs eval/exec:
    forbid import_stmt, ie __import__()
safe_eval vs data_eval(===ast.literal_eval):
    diff when eval('set(frozenset())')


py -m seed.helper.safe_eval
from seed.helper.safe_eval import safe_eval, safe_exec, data_eval
from seed.helper.safe_eval import safe_eval_ex, safe_exec_ex
from seed.helper.safe_eval import safe_eval_ex as safe_eval, safe_exec_ex as safe_exec

use-scene:
    # see: seed.io.savefile.SaveFile
    #
    * safe_eval:
        whole text file store repr of single unnamed object
        cooperate with stable_repr
        example file content:
            {'a': set()
            ,'b': MkXXX(...)
            }
    #
    * safe_exec:
        whole text file store assignment_stmts of ordered named objects
        example file content:
            a = set()
            b = MkXXX(...)



[[[begin-doctest_examples
#>>> from seed.helper.safe_eval import safe_eval, safe_exec
#   since see below: this_module.__builtins__ := _builtins

#################################
# data_eval
>>> data_eval is literal_eval
True
>>> data_eval("[1, {2: 3}, {4}, (), '', b'']")
[1, {2: 3}, {4}, (), '', b'']
>>> data_eval('set()') #doctest: +ELLIPSIS
set()

py3_?:Traceback (most recent call last):
    ...
ValueError: malformed node or string: <_ast.Call object at ...
py3_10_5:set()
>>> data_eval('max(1,2)') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
ValueError: malformed node or string...

py3_?:ValueError: malformed node or string: <_ast.Call object at ...
py3_10_5:ValueError: malformed node or string on line 1: <ast.Call object at ...>
>>> data_eval('import sys')
Traceback (most recent call last):
    ...
SyntaxError: invalid syntax
>>> data_eval('a=1')
Traceback (most recent call last):
    ...
SyntaxError: invalid syntax


#################################
# safe_eval
>>> safe_eval("[1, {2: 3}, {4}, (), '', b'']")
[1, {2: 3}, {4}, (), '', b'']
>>> safe_eval('set()')
set()
>>> safe_eval('max(1,2)')
2
>>> safe_eval('import sys')
Traceback (most recent call last):
    ...
SyntaxError: invalid syntax
>>> safe_eval('a=1')
Traceback (most recent call last):
    ...
SyntaxError: invalid syntax
>>> safe_eval('f(1,2)', locals=dict(f=max))
2
>>> safe_eval('f(1,2)', nonlocals=dict(f=max))
2
>>> safe_eval('f(1,2)', locals=dict(f=min), nonlocals=dict(f=max))
1


#################################
# safe_exec
>>> safe_exec("[1, {2: 3}, {4}, (), '', b'']")
{}
>>> safe_exec('set()')
{}
>>> safe_exec('max(1,2)')
{}
>>> safe_exec('import sys') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
_ImportError__forbid_import_stmt: forbid calling __import__('sys', globals={'__builtins__': [{...}]}, fromlist=None, level=0)

old-result-above:
    SystemError: ...: bad argument to internal function

>>> safe_exec('a=1')
{'a': 1}
>>> safe_exec("a=[1, {2: 3}, {4}, (), '', b'']")
{'a': [1, {2: 3}, {4}, (), '', b'']}
>>> safe_exec('a=set()')
{'a': set()}
>>> safe_exec('a=max(1,2)')
{'a': 2}
>>> safe_exec('a=f(1,2)', locals=dict(f=max)) == dict(f=max, a=2)
True
>>> safe_exec('a=f(1,2)', nonlocals=dict(f=max))
{'a': 2}
>>> safe_exec('a=f(1,2)', locals=dict(f=min), nonlocals=dict(f=max)) == dict(f=min, a=1)
True

>>> safe_exec('a=max(1,2)\nb={3};c=[4]\nd=(5,)') == dict(a=2, b={3}, c=[4], d=(5,))
True


]]]end-doctest_examples









from collections import ChainMap
import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))



chang API-of-safe_eval:
    old-def safe_eval(expression, locals=None):
    new-def safe_eval(expression, /,*, locals=None, nonlocals=None):
    =======src-code: move safe_eval(x,y) to safe_eval(x, locals=y)
    $ echo $my_tmp
    /sdcard/0my_files/tmp/
    $ mkdir $my_tmp/out4grep/
    $ cd $my_git_py
    $ pwd
    /sdcard/0my_files/git_repos/python3_src
    $ grep safe_eval -r . > $my_tmp/out4grep/safe_eval.txt
    $
    view /sdcard/0my_files/tmp/out4grep/safe_eval.txt
    only-one-place-required-fixed:
        ./nn_ns/regex/Simple/string_regex_pattern.py:    regex = safe_eval(py_expr_str, locals)



kw: global, nonlocal

py_help collections@UserDict
UserDict.data

[[[begin-doctest_examples:lambda
>>> _locals = {}
>>> _locals is safe_exec('f=lambda:1', locals=_locals)
True
>>> _locals is safe_exec('g=lambda:1+f()', locals=_locals)
True
>>> sorted(_locals)
['f', 'g']
>>> safe_eval('f()', locals=_locals)
1
>>> safe_eval('g()', locals=_locals)
Traceback (most recent call last):
    ...
NameError: name 'f' is not defined
>>> safe_eval('g()', locals=_locals, nonlocals=_locals) #??? NameError: name 'f' is not defined
Traceback (most recent call last):
    ...
NameError: name 'f' is not defined
>>> _global_eval('g()', _locals, _locals) #???
Traceback (most recent call last):
    ...
NameError: name 'f' is not defined

>>> h = _locals['g']

#>>> dir(h)
__closure__
__defaults__
__kwdefaults__
__globals__
>>> h.__kwdefaults__
>>> h.__defaults__
>>> h.__closure__ is None #??? why ???
True
>>> h.__globals__ #doctest: +ELLIPSIS
ChainMap({}, mappingproxy({...}))
>>> type(h.__globals__) is _pseudo_py_dict
True


>>> _locals = {}
>>> _locals is safe_exec('def f():return 1', locals=_locals)
True
>>> _locals is safe_exec('def g():return 1+f()', locals=_locals)
True
>>> sorted(_locals)
['f', 'g']
>>> safe_eval('f()', locals=_locals)
1
>>> _global_eval('g()', _locals, _locals) #???
Traceback (most recent call last):
    ...
NameError: name 'f' is not defined
>>> h = _locals['g']
>>> h.__closure__ is None #??? why ???
True
>>> def h():return h
>>> h.__closure__ is None #??? why ???
True



>>> _locals = {}
>>> _locals is safe_exec('f=lambda:1', locals=_locals, nonlocals=_locals)
True
>>> _locals is safe_exec('g=lambda:1+f()', locals=_locals, nonlocals=_locals)
True
>>> sorted(_locals)
['f', 'g']
>>> safe_eval('f()', locals=_locals)
1
>>> safe_eval('g()', locals=_locals)
2
>>> h = _locals['g']
>>> h.__closure__ is None #??? why ???
True



]]]end-doctest_examples:lambda
#'''


__all__ = ('literal_eval', 'data_eval', 'safe_eval', 'safe_exec', 'safe_eval_ex', 'safe_exec_ex')

#from .. import get_keys_and_gettor_of_module_or_dict
from ast import literal_eval
#from collections import Mapping
from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttrAndAsMapping
from types import MappingProxyType as _MappingProxyType
from collections import ChainMap as _ChainMap
from collections import UserDict as _UserDict
import builtins
# NOTE: <built-in function __import__>

def _vars5module(qnm4mdl, nms4check, /):
    import importlib
    mdl = importlib.import_module(qnm4mdl)
    assert mdl.__name__ == qnm4mdl
    nm2v = {nm:v for nm in dir(mdl) if not nm[:1] == '_' for v in [getattr(mdl, nm)] if v.__module__ == qnm4mdl}
    assert sorted(nm2v) == sorted(nms4check), set(nm2v) ^ set(nms4check)
    return nm2v#vars(mdl)

def _vars5math():
    qnm4mdl = 'math'
    nms4check = ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
    return _vars5module(qnm4mdl, nms4check)
def _vars5cmath():
    qnm4mdl = 'cmath'
    nms4check = ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'cos', 'cosh', 'e', 'exp', 'inf', 'infj', 'isclose', 'isfinite', 'isinf', 'isnan', 'log', 'log10', 'nan', 'nanj', 'phase', 'pi', 'polar', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau']
    return _vars5module(qnm4mdl, nms4check)
def _vars5itertools():
    qnm4mdl = 'itertools'
    nms4check = ['accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'filterfalse', 'groupby', 'islice', 'pairwise', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee', 'zip_longest']
    return _vars5module(qnm4mdl, nms4check)
    #.import itertools
    #.nm2v = {nm:v for nm in dir(itertools) if not nm[:1] == '_' for v in [getattr(itertools, nm)] if v.__module__ == 'itertools'}
    #.assert (__:=sorted(nm2v)) == nms4check, __
    #.return nm2v#vars(itertools)

from ._safe_eval__details import allows as _allows, forbids as _forbids
class _pseudo_py_dict(_UserDict, dict):
    # <<== TypeError: exec() globals must be a dict, not ChainMap
    def __init__(sf, d, /):
        assert not hasattr(sf, 'data')
        _UserDict.__init__(sf)
        assert sf.data == {}
        assert not sf.data is d
        sf.data = d
            # donot 『_UserDict.__init__(sf, d)』, since .data={**d}
        assert sf.data is d
    def __missing__(sf, k, /, *, _null={}):
        #@20250118:++__missing__
        d = sf.data
        assert not k in d
        _d = d.get('__builtins__', _null)#if not k in d else d
        return _d[k]
        print('__missing__', k)
        return sf.data[k]


literal_eval = literal_eval
data_eval = literal_eval
_global_eval = eval
_global_exec = exec

def _test4_pseudo_py_dict():
    d = dict(x=999)
    assert 999 == _global_eval('x', d)
    _d = _pseudo_py_dict(_ChainMap({}, d))
    assert 999 == _global_eval('x', dict(_d))
    assert 999 == _global_eval('x', _d)
    g = dict(__builtins__=d)
    assert 999 == _global_eval('x', g)
    _g = _pseudo_py_dict(_ChainMap({}, g))
    assert 999 == _global_eval('x', dict(_g))
    assert 999 == _global_eval('x', _g)
        # NameError: name 'x' is not defined
        # why only this line fail???
        # => @20250118:++__missing__
_test4_pseudo_py_dict(); del _test4_pseudo_py_dict


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

class _ImportError__forbid_import_stmt(BaseException):pass
def _4__import__(*args, **kwargs):
    raise _ImportError__forbid_import_stmt(*args, **kwargs)

_allowed_modules = frozenset({'unicodedata'})
_saved__import__ = __import__
def _4__import__(name, globals=None, locals=None, fromlist=(), level=0, **kwargs) -> 'module':
    if name in _allowed_modules and level==0:
        #requured 'unicodedata' when identifier/string_literal contains hz(Chinese character)
        return _saved__import__(name, globals=None, locals=None, fromlist=(), level=0, **kwargs)
    if globals is not None:
        recur = []
        globals = dict.fromkeys(iter(globals), recur)
        recur.append(globals)
    del locals
    if kwargs:
        raise _ImportError__forbid_import_stmt(fr'forbid calling __import__({name!r}, globals={globals!r}, fromlist={fromlist!r}, level={level!r}, **{kwargs!r})')
    else:
        raise _ImportError__forbid_import_stmt(fr'forbid calling __import__({name!r}, globals={globals!r}, fromlist={fromlist!r}, level={level!r})')
    raise _ImportError__forbid_import_stmt(name, globals=globals, fromlist=fromlist, level=level, **kwargs)
r'''
Help on built-in function __import__ in module builtins:

__import__(...)
    __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module

    Import a module. Because this function is meant for use by the Python interpreter and not for general use, it is better to use importlib.import_module() to programmatically import a module.

    The globals argument is only used to determine the context; they are not modified.
        The locals argument is unused.
        The fromlist should be a list of names to emulate ``from name import ...'', or an empty list to emulate ``import name''.
            When importing a module from a package, note that __import__('A.B', ...) 
                returns package A when fromlist is empty
                , but its submodule B when fromlist is not empty.
        The level argument is used to determine whether to perform absolute or relative imports:
            0 is absolute
            , while a positive number is the number of parent directories to search relative to the current module.
(END)
:
#'''

_builtins = {name : getattr(builtins, name) for name in _allows}
#_builtins = dict(__import__=_4__import__, **_builtins)
_builtins.update(__import__=_4__import__)
#_builtins.update(**_vars5itertools())

_builtins_ex = {**_vars5itertools(), **_builtins}
    # @20250118: ++_vars5itertools()
    # @20250118: ++_builtins_ex
    # @20250118: ++_globals_ex
    # @20250118: ++kw:using_extended_globals
    # @20250118: ++safe_eval_ex(), safe_exec_ex()
    # for 『py_adhoc_call   aaa.bbb   ,stable_repr.f ='range(1,10)' ='count(4)'』

_builtins = _MappingProxyType(_builtins)
#_builtins = DictKeyAsObjAttrAndAsMapping(_MappingProxyType(_builtins))
_builtins_ex = _MappingProxyType(_builtins_ex)
#_builtins_ex = DictKeyAsObjAttrAndAsMapping(_MappingProxyType(_builtins_ex))

_globals = {'__builtins__' : _builtins}
_globals = _MappingProxyType(_globals)
_globals_ex = {'__builtins__' : _builtins_ex}
_globals_ex = _MappingProxyType(_globals_ex)
assert 'count' in _globals_ex['__builtins__']
#assert hasattr(_globals_ex['__builtins__'], 'count')

_global_print = print
_global_eval
_global_exec
_pseudo_py_dict
_UserDict
#del _MappingProxyType
del builtins, _allows
del _4__import__
del DictKeyAsObjAttrAndAsMapping
del _builtins_ex, _vars5itertools
del _vars5module, _vars5math, _vars5cmath
_globals
_globals_ex
_ImportError__forbid_import_stmt
_allowed_modules
_saved__import__
_MappingProxyType
_ChainMap
_global_print
#rint(list(globals()))
__builtins__ = _builtins; del _builtins
    #now, exec cannot be used in this module
    #now, print cannot be used in this module
    #using _global_print instead





assert ...
__builtins__, _global_eval, _global_eval
def _std4args(locals, nonlocals, /, *, readonly, using_extended_globals):
    # ??? globals is used to be bound to func ???
    # ??? locals is used to lookup vats (?hence should _ChainMap globals?) ???
    if locals is None:
        locals = {}
    #type(locals).__getitem__
    if nonlocals is ...:
        nonlocals = locals
    elif nonlocals is None:
        nonlocals = {}

    same = nonlocals is locals
    if readonly:
        locals = _MappingProxyType(locals)
        nonlocals = _MappingProxyType(nonlocals)
    if same:
        nonlocals = locals
    if same or not nonlocals:

        locals_nonlocals = locals
    else:
        locals_nonlocals = _ChainMap(locals, nonlocals)

    xglobals = _globals if not using_extended_globals else _globals_ex
    assert len(xglobals) == 1
        # only "__builtins__"
    ######################
    ######################
    if 1:
        #@20250118
        locals_nonlocals_globals = _ChainMap(locals_nonlocals, xglobals)
        locals_nonlocals = _pseudo_py_dict(locals_nonlocals_globals)
            # ok
    else:
        #@20250118
        locals_nonlocals = _pseudo_py_dict(locals_nonlocals)
            # fail
        # ??? globals is used to be bound to func ???
        # ??? locals is used to lookup vats (?hence should _ChainMap globals?) ???
    ######################
    ######################
    #.if 1:
    #.    #@20250118
    #.    locals_nonlocals_globals = _ChainMap(locals_nonlocals, xglobals)
    #.    nonlocals_globals = _pseudo_py_dict(locals_nonlocals_globals)
    #.    locals_nonlocals = nonlocals_globals
    #.        #ok
    #.    locals_nonlocals = locals_nonlocals_globals
    #.        #fail
    #.    return (locals, nonlocals, locals_nonlocals, nonlocals_globals)
    #.if 1:
    #.    #@20250118
    #.    locals_nonlocals = _ChainMap(locals_nonlocals, xglobals)
    #.    nonlocals_globals = {**xglobals}
    #.    assert len(nonlocals_globals) == 1
    #.    #return (locals, nonlocals, locals_nonlocals, nonlocals_globals)
    #.    gd = _ChainMap(xglobals, nonlocals) # @20250118:override "__builtins__"
    #.    #gd = _ChainMap(nonlocals, xglobals)
    #.    nonlocals_globals = _pseudo_py_dict(gd)
    #.    return (locals, nonlocals, locals_nonlocals, nonlocals_globals)

    gd = _ChainMap(nonlocals, xglobals)
        # <<== proof from `kw:global`
        #
        #
        #result = _global_eval(expression, gd, locals_nonlocals)
            # TypeError: globals must be a real dict; try eval(expr, {}, mapping)
        #_global_exec(script, gd, locals_nonlocals)
            #TypeError: exec() globals must be a dict, not ChainMap
    nonlocals_globals = _pseudo_py_dict(gd)
    assert nonlocals_globals.data is gd

    return (locals, nonlocals, locals_nonlocals, nonlocals_globals)
def _test4_std4args(locals, nonlocals):
    (_locals, _nonlocals, locals_nonlocals, nonlocals_globals) = _std4args(locals, nonlocals, readonly=True, using_extended_globals=True)
    #_global_print(nonlocals_globals)
    #_global_print(type(nonlocals_globals))
    #_global_print(nonlocals_globals.data)
    #import itertools
    itertools = _saved__import__('itertools')
    assert nonlocals_globals.data['__builtins__']['count'] is itertools.count

    assert 'count' in nonlocals_globals['__builtins__']
    #assert hasattr(nonlocals_globals['__builtins__'], 'count')

    assert nonlocals_globals['__builtins__']['count'] is itertools.count
    #assert nonlocals_globals['__builtins__'].count is itertools.count

    assert _global_eval('count', dict(__builtins__=_globals_ex['__builtins__'])) is itertools.count
    assert _global_eval('count', dict(_globals_ex)) is itertools.count

    assert _global_eval('count', dict(nonlocals_globals)) is itertools.count
    assert _global_eval('count', nonlocals_globals) is itertools.count
    assert _global_eval('round', nonlocals_globals, locals_nonlocals) is round
    assert _global_eval('round', nonlocals_globals, {}) is round
    assert _global_eval('count', nonlocals_globals, _ChainMap(locals_nonlocals, nonlocals_globals)) is itertools.count
    assert _global_eval('count', nonlocals_globals, None) is itertools.count
        # ok
    if 0:
        #fail
        assert _global_eval('count', nonlocals_globals, {}) is itertools.count
        assert _global_eval('count', nonlocals_globals, {**_globals_ex}) is itertools.count
    if 0:
        #fail
        assert _global_eval('count', nonlocals_globals, locals_nonlocals) is itertools.count
            # why only this line fail???

_test4_std4args({}, {})
_test4_std4args(None, None)
del _test4_std4args

#def safe_eval(expression, locals=None):
#def safe_eval(expression, locals=None, /):
#def safe_eval(expression, /,*, locals=None, nonlocals=None):
#def safe_eval(expression, /, locals=None):
#def safe_eval(expression, /, locals=None, *, nonlocals=None):
def safe_eval(expression, /,*, locals=None, nonlocals=None, using_extended_globals=False):
    return safe_eval_ex(expression, locals=locals, nonlocals=nonlocals, using_extended_globals=using_extended_globals)
def safe_eval_ex(expression, /,*, locals=None, nonlocals=None, using_extended_globals=True):
    # assume expression cannot setitem in locals
    # but expression can getitem in locals and update it
    #
    (_locals, _nonlocals, locals_nonlocals, nonlocals_globals) = _std4args(locals, nonlocals, readonly=True, using_extended_globals=using_extended_globals)
        #although nonlocals is useless, here to match API-of-safe_eval with safe_exec


    #if 0b0: return _global_eval(expression, dict(xglobals), locals_nonlocals)

    result = _global_eval(expression, nonlocals_globals, locals_nonlocals)
        # TypeError: globals must be a real dict; try eval(expr, {}, mapping)
    return result
r'''
Help on built-in function eval in module builtins:

eval(source, globals=None, locals=None, /)
    Evaluate the given source in the context of globals and locals.

    The source may be a string representing a Python expression or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping, defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
(END)
#'''

# safe_eval needs __globals__ to access eval
# if pass safe_eval as eval to the call, eval is passed too.
##safe_eval.__globals__
##_builtins['eval'] = safe_eval

assert safe_eval_ex('count', locals={}, nonlocals={})
assert safe_eval_ex('count')

def safe_exec(script, /,*, locals=None, nonlocals=None, using_extended_globals=False):
    return safe_exec_ex(script, locals=locals, nonlocals=nonlocals, using_extended_globals=using_extended_globals)
def safe_exec_ex(script, /,*, locals=None, nonlocals=None, using_extended_globals=True):
    # assume script cannot setitem in nonlocals
    # but script can getitem in nonlocals and update it
    #
    #forbidden __import__

    #bug:result = locals
    #   locals may be None
    (_locals, _nonlocals, locals_nonlocals, nonlocals_globals) = _std4args(locals, nonlocals, readonly=False, using_extended_globals=using_extended_globals)
    result = _locals

    #if 0b0: _global_exec(script, dict(xglobals), locals_nonlocals) return result

    _global_exec(script, nonlocals_globals, locals_nonlocals)
        #TypeError: exec() globals must be a dict, not ChainMap
    return result
r'''
Help on built-in function exec in module builtins:

exec(source, globals=None, locals=None, /)
    Execute the given source in the context of globals and locals.

    The source may be a string representing one or more Python statements or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping, defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
(END)
#'''





if 1:
    __nms4globals4this_module = {'__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', '__all__', 'literal_eval', 'data_eval', '_global_eval', '_global_exec', '_globals', '_globals_ex', 'safe_eval', 'safe_eval_ex', 'safe_exec', 'safe_exec_ex', '_ImportError__forbid_import_stmt', '_allowed_modules', '_saved__import__', '_MappingProxyType', '_ChainMap', '_global_print', '_pseudo_py_dict', '_UserDict', '_std4args', '__nms4globals4this_module'}
    assert set(globals()) ^ __nms4globals4this_module <= {'__annotations__'}, set(globals()) ^ __nms4globals4this_module



assert safe_eval('{max(1,2)}') == {2}
assert safe_exec('{max(1,2)};[a]=[1]\nb=2') == {'a':1,'b':2}, repr(safe_exec('{max(1,2)};[a]=[1]\nb=2'))

def _test_safe_eval(exp, name_for_NameError, /):
    err = "name '{}' is not defined".format(name_for_NameError)
    try:
        safe_eval(exp)
    except NameError as e:
        assert str(e) == err
    else:
        raise Exception('fail _test_safe_eval')
    return
def _test_safe_exec():
    script = 'import sys'
    try:
        exec('import sys', {}, {})
    except NameError:
        # NameError: name 'exec' is not defined
        #   <<== [__builtins__ := _builtins]
        pass
    else:
        raise Exception('fail _test_safe_exec')

    try:
        _global_exec('import sys', {}, {})
    except _ImportError__forbid_import_stmt:
    #except SystemError:
        #forbidden __import__
        pass
    else:
        raise Exception('fail _test_safe_exec')

    try:
        #safe_exec(script)
        safe_exec('import sys')
    except _ImportError__forbid_import_stmt:
    #except SystemError:
        # SystemError: /home/builder/.termux-build/python/src/Objects/dictobject.c:1434: bad argument to internal function
        #forbidden __import__
        pass
    else:
        raise Exception('fail _test_safe_exec')
    return


if __name__ == '__main__':
    #assert eval is getattr(safe_eval.__globals__['__builtins__'], 'eval')
    assert safe_eval('(max(1+2, abs(-53), *iter(list(range(57)))),)') == (56,)

    _test_safe_eval("(eval('(print(1),)'),)", 'eval')
    _test_safe_eval('(print(''),)', 'print')
    _test_safe_eval('(exec(''),)', 'exec')
    _test_safe_exec()



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):



from seed.helper.safe_eval import safe_eval, safe_exec, data_eval
from seed.helper.safe_eval import safe_eval_ex, safe_exec_ex
if 0:from seed.helper.safe_eval import safe_eval_ex as safe_eval, safe_exec_ex as safe_exec
from seed.helper.safe_eval import *
