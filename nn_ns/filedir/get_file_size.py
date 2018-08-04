
'''
os.stat(path).st_size
'''
__all__ = '''
    get_file_size
    '''.split()

import os.path

def get_file_size(fname):
    if os.path.isdir(fname): raise IsADirectoryError(fname)
    return os.stat(fname).st_size

