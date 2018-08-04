
__all__ = ['shell_copy']

import os.path, shutil

def shell_copy(src, dst):
    '''it seems shutil.copy2 does not call os.makedirs'''
    dst = os.path.abspath(dst)
    folder = os.path.dirname(dst)
    os.makedirs(folder, exist_ok=True)
    shutil.copy2(src, dst)
    return
