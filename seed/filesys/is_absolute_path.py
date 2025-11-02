#__all__:goto
r'''
e ../../python3_src/seed/filesys/is_absolute_path.py


NOTE:!!!result is platform-dependent!!!'



seed.filesys.is_absolute_path
py -m nn_ns.app.debug_cmd   seed.filesys.is_absolute_path -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.filesys.is_absolute_path:__doc__ -ht # -ff -df

>>> is_relative_path('')
True
>>> is_relative_path('.')
True
>>> is_relative_path('..')
True
>>> is_relative_path('./aaa')
True
>>> is_relative_path('aaa/bbb')
True
>>> is_relative_path('aaa')
True

>>> is_relative_path('/')
False
>>> is_relative_path('/aaa')
False
>>> is_relative_path('c:/aaa') # !!! PurePosixPath
True
>>> is_relative_path('c:/') # !!! PurePosixPath
True
>>> is_relative_path('c:') # !!! PurePosixPath
True





>>> is_absolute_path('/')
True
>>> is_absolute_path('a')
False

>>> check_absolute_path('/')
>>> check_absolute_path('a')
Traceback (most recent call last):
    ...
seed.filesys.is_absolute_path.NotAnAbsolutePathError: a

>>> is_relative_path('/')
False
>>> is_relative_path('a')
True

>>> check_relative_path('/')
Traceback (most recent call last):
    ...
seed.filesys.is_absolute_path.NotARelativePathError: /
>>> check_relative_path('a')





>>> from pathlib import PurePosixPath as Path
>>> Path('aaa') / 'c:'
PurePosixPath('aaa/c:')
>>> Path('aaa') / 'c:/'
PurePosixPath('aaa/c:')
>>> Path('aaa') / 'c:/bbb'
PurePosixPath('aaa/c:/bbb')
>>> Path('aaa') / '/bbb'
PurePosixPath('/bbb')
>>> Path('aaa') / 'bbb'
PurePosixPath('aaa/bbb')

>>> from pathlib import PureWindowsPath as Path
>>> Path('aaa') / 'c:'
PureWindowsPath('c:')
>>> Path('aaa') / 'c:/'
PureWindowsPath('c:/')
>>> Path('aaa') / 'c:/bbb'
PureWindowsPath('c:/bbb')
>>> Path('aaa') / '/bbb'
PureWindowsPath('/bbb')
>>> Path('aaa') / 'bbb'
PureWindowsPath('aaa/bbb')






'''#'''

__all__ = r'''
is_relative_path
    check_relative_path
        NotARelativePathError

is_absolute_path
    check_absolute_path
        NotAnAbsolutePathError

'''.split()#'''
from pathlib import Path as _Path

class NotARelativePathError(OSError):pass
class NotAnAbsolutePathError(OSError):pass

def check_relative_path(path, /):
    if not is_relative_path(path):
        raise NotARelativePathError(path)
def check_absolute_path(path, /):
    if not is_absolute_path(path):
        raise NotAnAbsolutePathError(path)

def is_relative_path(path, /):
    '-> bool # NOTE:!!!result is platform-dependent!!!'
    path = _Path(path)
    return not (path.anchor)
def is_absolute_path(path, /):
    '-> bool # NOTE:!!!result is platform-dependent!!!'
    return not is_relative_path(path)

from seed.filesys.is_absolute_path import is_relative_path, is_absolute_path, check_relative_path, check_absolute_path, NotARelativePathError, NotAnAbsolutePathError

