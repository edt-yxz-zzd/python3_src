
__all__ = 'txt_open  bin_open'.split()
def bin_open(file, mode, **kwargs):
    return open(file, mode+'b', **kwargs)
def txt_open(file, mode, **kwargs):
    return open(file, mode+'t', **kwargs)

from seed.io.xopen import txt_open, bin_open
