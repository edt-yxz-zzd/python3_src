
r'''
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
Traceback (most recent call last):
    ...
ValueError: malformed node or string: <_ast.Call object at ...
>>> data_eval('max(1,2)') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
ValueError: malformed node or string: <_ast.Call object at ...
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

#'''


__all__ = ('literal_eval', 'safe_eval', 'data_eval', 'safe_exec')

#from .. import get_keys_and_gettor_of_module_or_dict
from ast import literal_eval
#from collections import Mapping
from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttrAndAsMapping
from types import MappingProxyType as _MappingProxyType
from collections import ChainMap as _ChainMap
import builtins
# NOTE: <built-in function __import__>
from ._safe_eval__details import allows as _allows, forbids as _forbids


literal_eval = literal_eval
data_eval = literal_eval
_global_eval = eval
_global_exec = exec




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
_builtins = dict(__import__=_4__import__, **_builtins)
_builtins = _MappingProxyType(_builtins)
_builtins = DictKeyAsObjAttrAndAsMapping(_MappingProxyType(_builtins))
_globals = {'__builtins__' : _builtins}
_globals = _MappingProxyType(_globals)
#del _MappingProxyType
del builtins, _allows
del _4__import__
del DictKeyAsObjAttrAndAsMapping
_globals
_ImportError__forbid_import_stmt
_allowed_modules
_saved__import__
_MappingProxyType
_ChainMap
#rint(list(globals()))
__builtins__ = _builtins; del _builtins





__builtins__, _global_eval, _global_eval
#def safe_eval(expression, locals=None):
#def safe_eval(expression, locals=None, /):
#def safe_eval(expression, /,*, locals=None, nonlocals=None):
#def safe_eval(expression, /, locals=None):
#def safe_eval(expression, /, locals=None, *, nonlocals=None):
def safe_eval(expression, /,*, locals=None, nonlocals=None):
    # assume expression cannot setitem in locals
    # but expression can getitem in locals and update it
    #
    if locals is None:
        locals = {}
    locals = _MappingProxyType(locals)

    if 1:
        #although nonlocals is useless, here to match API-of-safe_eval with safe_exec
        #r'''[[[
        if nonlocals:
            nonlocals = _MappingProxyType(nonlocals)
            locals_nonlocals = _ChainMap(locals, nonlocals)
        else:
            locals_nonlocals = locals
        #]]]'''
    else:
        locals_nonlocals = locals

    return _global_eval(expression, dict(_globals), locals_nonlocals)
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


def safe_exec(script, /,*, locals=None, nonlocals=None):
    # assume script cannot setitem in nonlocals
    # but script can getitem in nonlocals and update it
    #
    #forbidden __import__
    if locals is None:
        locals = {}
    result = locals

    if nonlocals:
        locals_nonlocals = _ChainMap(locals, nonlocals)
    else:
        locals_nonlocals = locals

    _global_exec(script, dict(_globals), locals_nonlocals)
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





try:
    assert set(globals()) ^ {'__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', '__all__', 'literal_eval', 'data_eval', '_global_eval', '_global_exec', '_globals', 'safe_eval', 'safe_exec', '_ImportError__forbid_import_stmt', '_allowed_modules', '_saved__import__', '_MappingProxyType', '_ChainMap'} <= {'__annotations__'}


except AssertionError:
    print(set(globals()) ^ {'__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', '__all__', 'literal_eval', 'data_eval', '_global_eval', '_global_exec', '_globals', 'safe_eval', 'safe_exec', '_ImportError__forbid_import_stmt', '_allowed_modules', '_saved__import__', '_MappingProxyType', '_ChainMap'})
    raise

assert safe_eval('{max(1,2)}') == {2}
try:
    assert safe_exec('{max(1,2)};[a]=[1]\nb=2') == {'a':1,'b':2}
except AssertionError:
    print(repr(safe_exec('{max(1,2)};[a]=[1]\nb=2')))
    raise
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
    exec('import sys', {}, {})
    try:
        #safe_exec(script)
        safe_exec('import sys')
    except SystemError:
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



