#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/check_path.py

seed.tiny_.check_path
py -m nn_ns.app.debug_cmd   seed.tiny_.check_path -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.tiny_.check_path:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.tiny_.check_path   @f
]]]'''#'''
__all__ = r'''
check_path_exists_
    check_path_not_exists_
check_file_path_
    check_not_file_path_
check_dir_path_
    check_not_dir_path_

check_same_path_
    check_not_same_path_
AreSameFileError
    NotSameFileError
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from pathlib import Path
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...
FileExistsError
FileNotFoundError
IsADirectoryError
NotADirectoryError

def check_path_exists_(path, /):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
def check_path_not_exists_(path, /):
    path = Path(path)
    if path.exists():
        raise FileExistsError(path)




def check_file_path_(path, /):
    path = Path(path)
    if not path.is_file():
        check_path_exists_(path)
        raise IsADirectoryError(path)

def check_dir_path_(path, /):
    path = Path(path)
    if not path.is_dir():
        check_path_exists_(path)
        raise NotADirectoryError(path)

def check_not_file_path_(path, /):
    path = Path(path)
    if path.is_file():
        raise NotADirectoryError(path)

def check_not_dir_path_(path, /):
    path = Path(path)
    if path.is_dir():
        raise IsADirectoryError(path)

class AreSameFileError(OSError):pass
class NotSameFileError(OSError):pass

def check_same_path_(path0, path1, /):
    path0 = Path(path0)
    if not path0.samefile(path1):
        raise NotSameFileError(path0, path1)


def check_not_same_path_(path0, path1, /):
    path0 = Path(path0)
    if path0.samefile(path1):
        raise AreSameFileError(path0, path1)





__all__
from seed.tiny_.check_path import check_path_exists_, check_path_not_exists_, check_file_path_, check_dir_path_, check_not_file_path_, check_not_dir_path_
from seed.tiny_.check_path import check_same_path_, check_not_same_path_, AreSameFileError, NotSameFileError
from seed.tiny_.check_path import *
