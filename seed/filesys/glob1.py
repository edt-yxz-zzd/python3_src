
__all__ = ['glob1', 'globN']


import glob
#import itertools


def globN(fname, N):
    # fnames = itertools.islice(glob.iglob(fname), 2)
    fnames = glob.glob(fname)
    L = len(fnames)
    if L == N:
        return fnames
    elif L > N:
        raise ValueError('too many file matched: len({}) > {}'.format(fnames, N))
    else:
        raise ValueError('too few file matched: len({}) < {}'.format(fnames, N))

def glob1(fname):
    fname, = globN(fname, 1)
    return fname

