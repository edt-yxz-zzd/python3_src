#__all__:goto
r'''[[[
e ../../python3_src/seed/filesys/relative_to.py

seed.filesys.relative_to
py -m nn_ns.app.debug_cmd   seed.filesys.relative_to -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.filesys.relative_to:__doc__ -ht # -ff -df
#######

[[
----
#!Deprecated since version 3.12, will be removed in version 3.14:
PurePath.relative_to(self, *other)
             Return the relative path to another path identified by the passed
             arguments.  If the operation is not possible (because this is not
             a subpath of the other path), raise ValueError.
----
]]
[[
view ../../python3_src/bash_script/app/relative_to_if_under_rootdir_
realpath -m -L --relative-base "$@"
]]



'#'; __doc__ = r'#'
>>> relative_to('/aaa/bbb', '/aaa/bbb')
PosixPath('.')
>>> relative_to('/aaa/bbb', '/aaa/bbb/ccc')
PosixPath('ccc')
>>> relative_to('/aaa/bbb', '/aaa/bbbxxx')
Traceback (most recent call last):
    ...
seed.filesys.relative_to.NotUnderRootDirError: ('/aaa/bbb', '/aaa/bbbxxx')

>>> relative_to('aaa/bbb', 'aaa/bbb')
PosixPath('.')
>>> relative_to('aaa/bbb', 'aaa/bbb/ccc')
PosixPath('ccc')
>>> relative_to('aaa/bbb', 'aaa/bbbxxx')
Traceback (most recent call last):
    ...
seed.filesys.relative_to.NotUnderRootDirError: ('aaa/bbb', 'aaa/bbbxxx')


>>> relative_to('aaa/../bbb', 'aaa/../bbb')
PosixPath('.')
>>> relative_to('aaa/../bbb', 'aaa/../bbb/ccc')
PosixPath('ccc')
>>> relative_to('aaa/../bbb', 'aaa/../bbbxxx')
Traceback (most recent call last):
    ...
seed.filesys.relative_to.NotUnderRootDirError: ('aaa/../bbb', 'aaa/../bbbxxx')


>>> relative_to('aaa/../bbb', 'aaa/../bbb')
PosixPath('.')
>>> relative_to('bbb', 'aaa/../bbb')
PosixPath('.')
>>> relative_to('aaa/../bbb', 'bbb')
PosixPath('.')



py_adhoc_call   seed.filesys.relative_to   @f

]]]'''#'''
__all__ = r'''
relative_to
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from pathlib import Path
___end_mark_of_excluded_global_names__0___ = ...


class NotUnderRootDirError(Exception):pass
    #ValueError
def relative_to(rootdir, path, /):
    if not None is (r:=may_relative_to(rootdir, path)):
        return r
    raise NotUnderRootDirError(rootdir, path)
def may_relative_to(rootdir, path, /):
    rootdir = Path(rootdir)
    path = Path(path)
    if not None is (r:=_relative_to(rootdir, path)):
        return r
    rootdir = rootdir.resolve()
    path = path.resolve()
    return _relative_to(rootdir, path)
def _relative_to(rootdir, path, /):
    ls0 = rootdir.parts
    ls1 = path.parts
    if len(ls0) <= len(ls1) and ls1[:len(ls0)] == ls0:
        return Path(*ls1[len(ls0):])
    return None


__all__
from seed.filesys.relative_to import relative_to
from seed.filesys.relative_to import *
