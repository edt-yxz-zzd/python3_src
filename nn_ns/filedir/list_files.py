

__all__ = '''
    list_files
    list_folders
    '''.split()

import os

def list_files(path): # -> [file_names]
    ls = os.listdir(path)
    return [fn for fn in ls if os.path.isfile(os.path.join(path, fn))]


def list_folders(path): # -> [folder_names]
    ls = os.listdir(path)
    return [fn for fn in ls if os.path.isdir(os.path.join(path, fn))]


