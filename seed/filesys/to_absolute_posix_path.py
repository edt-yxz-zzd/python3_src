

__all__ = '''
    to_absolute_posix_path
    '''.split()

from pathlib import Path

def to_absolute_posix_path(path):
    #bug:abs_path = PosixPath(path).resolve()
    abs_path = Path(path).resolve().as_posix()
    assert abs_path
    if abs_path[0] != '/':
        abs_path = '/' + abs_path
    #print_err(abs_path)
    assert abs_path and abs_path[0] == '/'
    return abs_path

