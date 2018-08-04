

__all__ = ['rename']
from os import rename as _rename, replace as _replace
def rename(src, dst):
    open(dst, 'xb')
    _replace(src, dst)

