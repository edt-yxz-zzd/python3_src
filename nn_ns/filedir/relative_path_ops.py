
r"""
py -m nn_ns.filedir.relative_path_ops
from nn_ns.filedir.relative_path_ops import relative_path_ops, check_relative_path, is_relative_path_empty, relative_path2parts, empty_relative_path, str2relative_path, relative_path2str, check_relative_path__str, parts2relative_path, part2relative_path
#"""

__all__ = '''
    relative_path_ops
        empty_relative_path
        check_relative_path
        is_relative_path_empty
        relative_path2parts
        parts2relative_path
            part2relative_path
        str2relative_path
        relative_path2str
        check_relative_path__str
    '''.split()


from pathlib import PurePosixPath#, Path
from seed.helper.check.checkers import check_str, check_all, check_tuple


def _check_relative_path__type__relative(relative_path, /):
    if not type(relative_path) is PurePosixPath: raise TypeError
    if relative_path.is_absolute(): raise ValueError

def check_relative_path(relative_path, /,*, empty_ok:bool=True):
    'relative_path :: PurePosixPath & not .is_absolute() # .as_posix()->str'
    _check_relative_path__type__relative(relative_path)
    parts = relative_path2parts(relative_path)
        #check inside has no '..'
    if not empty_ok and not parts: raise ValueError
    return None

empty_relative_path = PurePosixPath('.')
def is_relative_path_empty(relative_path, /):
    _check_relative_path__type__relative(relative_path)
    return relative_path == empty_relative_path
    return relative_path.as_posix() == '.'
    return relative_path.as_posix() in ('', '.')
def relative_path2parts(relative_path, /):
    'relative_path -> tuple<basename>'
    _check_relative_path__type__relative(relative_path)
    #if is_relative_path_empty(relative_path): return ()
    parts = relative_path.parts
    #if any(basename in ('/', '//', '.', '..') for basename in parts): raise ValueError
    if '..' in parts: raise ValueError
    return parts

def part2relative_path(*parts):
    return parts2relative_path(parts)
def parts2relative_path(parts, /):
    check_tuple(parts)
    check_all(check_str, parts)
    relative_path = PurePosixPath(*parts)
    if relative_path2parts(relative_path) != parts: raise ValueError(f'not std relative_path__parts: {parts!r}, std = {relative_path2parts(relative_path)!r}')
    return relative_path

def str2relative_path(s, /):
    if type(s) is not str: raise TypeError
    relative_path = PurePosixPath(s)
    if relative_path2str(relative_path) != s: raise ValueError(f'not std relative_path__str: {s!r}, std = {relative_path2str(relative_path)!r}')

    #!!!
    if 0:
        #since checked inside relative_path2str
        check_relative_path(relative_path)

    return relative_path
def relative_path2str(relative_path, /):
    check_relative_path(relative_path)
    relative_path__str = relative_path.as_posix()
    return relative_path__str
def check_relative_path__str(s, /,*, empty_ok:bool=True):
    relative_path = str2relative_path(s)
        #check inside
    if not empty_ok and relative_path == empty_relative_path: raise ValueError

class relative_path_ops:
    'relative_path :: PurePosixPath & not .is_absolute() # .as_posix()->str'
    empty = empty_relative_path

    @classmethod
    def check(cls, relative_path, /,*, empty_ok:bool=True):
        return check_relative_path(relative_path, empty_ok=empty_ok)
    @classmethod
    def is_empty(cls, relative_path, /):
        return is_relative_path_empty(relative_path)
    @classmethod
    def to_parts(cls, relative_path, /):
        return relative_path2parts(relative_path)
    @classmethod
    def to_str(cls, relative_path, /):
        return relative_path2str(relative_path)
    @classmethod
    def from_parts(cls, relative_path__parts, /):
        return parts2relative_path(relative_path__parts)
    @classmethod
    def from_part(cls, /, *relative_path__parts):
        return part2relative_path(relative_path__parts)
    @classmethod
    def check_str(cls, relative_path__str, /,*, empty_ok:bool=True):
        return check_relative_path__str(relative_path__str, empty_ok=empty_ok)
















assert PurePosixPath().as_posix() == '.'
assert PurePosixPath('').as_posix() == '.'
assert PurePosixPath('x').as_posix() == 'x'
assert PurePosixPath('./x').as_posix() == 'x'
assert PurePosixPath('./x/../x').as_posix() == 'x/../x'
assert PurePosixPath('./x/../x/.').as_posix() == 'x/../x'
assert PurePosixPath('./x/./../x/.').as_posix() == 'x/../x'
assert PurePosixPath('./x/./../x/./y/.').as_posix() == 'x/../x/y'

if __name__ == '__main__':
    assert PurePosixPath() == PurePosixPath('') == PurePosixPath('.')
    ss = r'''
        .
        ./x/../t/./../y/./z/.
        /
        /x//y///../t
        //x/./y/.
        ///x/./y/.
        ////x/./y/.
        c:/y
        file:///y
        '''.split()
    for s in ['', *ss]:
        x = PurePosixPath(s)
        print(f'{s!r}')
        print(f'    {x!r}')
        print(f'    {x.as_posix()!r}')
        print(f'    {x.parts!r}')
        print(f'    {x.is_absolute()!r}')

