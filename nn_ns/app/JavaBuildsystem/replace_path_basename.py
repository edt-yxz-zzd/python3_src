
r'''
replace_path_basename("path/file.ext", "xxx.txt") == "path/xxx.txt"

'''

__all__ = ['replace_path_basename']

import os.path

def replace_path_basename(path, basename):
    return os.path.join(os.path.dirname(path), basename)

