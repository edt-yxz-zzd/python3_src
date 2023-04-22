
__all__ = '''
    group_by

    xs_to_k2vs_
        xs_to_vss_
            partition_xs_by_bool_
    '''.split()

from itertools import groupby

def group_by(iterable, *, key=None, container=tuple):
    for k, g in groupby(iterable, key=key):
        yield k, container(g)

from seed.tiny_.group__partition import partition_xs_by_bool_, xs_to_vss_, xs_to_k2vs_

from seed.iters.group_by import group_by
from seed.iters.group_by import xs_to_k2vs_, xs_to_vss_, partition_xs_by_bool_
from seed.iters.group_by import *

