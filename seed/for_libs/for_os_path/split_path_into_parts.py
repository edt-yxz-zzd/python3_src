

r'''
split path into parts
https://stackoverflow.com/questions/3167154/how-to-split-a-dos-path-into-its-components-in-python


py -m seed.for_libs.for_os_path.split_path_into_parts
'''

__all__ = '''
    split_path_into_parts

    split_path_into_parts__by_split
    split_path_into_parts__by_parts
    '''.split()

from pathlib import Path
import os.path

def split_path_into_parts__by_split(path):
    ls = os.path.normpath(path).split(os.path.sep)
    if len(ls) >= 2 and not ls[-1]: ls.pop()
    assert ls
    return ls
assert split_path_into_parts__by_split('/') == ['']

def split_path_into_parts__by_parts(path):
    return list(Path(path).parts)
assert split_path_into_parts__by_parts('/') == ['/']


split_path_into_parts = split_path_into_parts__by_parts


from seed.for_libs.for_os_path.split_path_into_parts import split_path_into_parts
from seed.for_libs.for_os_path.split_path_into_parts import split_path_into_parts__by_split, split_path_into_parts__by_parts

from seed.for_libs.for_os_path.split_path_into_parts import *

