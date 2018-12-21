
__all__ = '''
    group_by
    '''.split()
from itertools import groupby
def group_by(iterable, *, key=None, container=tuple):
    for k, g in groupby(iterable, key=key):
        yield k, container(g)


