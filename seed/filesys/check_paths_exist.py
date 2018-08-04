

__all__ = ['check_paths_exist']

import os.path
from itertools import filterfalse
from seed.types.to_container import is_reiterable


def list_filter(pred, iterable, *, not_pred=False):
    return list(filter_ex(pred, iterable, not_pred=not_pred))
def filter_ex(pred, iterable, *, not_pred=False):
    f = filterfalse if not_pred else filter
    return f(pred, iterable)



def check_paths_exist(paths, *, all_files=False, all_folders=False):
    #paths = tuple(paths)
    if not is_reiterable(paths): raise TypeError

    not_exists = list_filter(os.path.exists, paths, not_pred=True)
    if not_exists:
        raise FileNotFoundError(not_exists)

    if all_files:
        folders = list_filter(os.path.isdir, paths)
        if folders:
            raise IsADirectoryError(folders)
    ###
    if all_folders:
        files = list_filter(os.path.isfile, paths)
        if files:
            raise NotADirectoryError(files)
    return

