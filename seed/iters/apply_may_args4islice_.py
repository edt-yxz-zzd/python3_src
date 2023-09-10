
#e ../../python3_src/seed/iters/apply_may_args4islice_.py
#seed.iters.apply_may_args4islice_
__all__ = '''
    apply_may_args4islice_

    list_islice_
    show_islice_
    stable_show_islice_
    stable_list_islice_

    '''.split()#'''

from itertools import islice

def list_islice_(sz, iterable, /):
    return [*islice(iterable, sz)]
def show_islice_(sz, iterable, /):
    for x in islice(iterable, sz):
        print(repr(x)) #stable_repr?
    return
def stable_show_islice_(sz, iterable, /):
    from seed.helper.stable_repr import stable_repr
    for x in islice(iterable, sz):
        print(stable_repr(x))
    return
def stable_list_islice_(sz, iterable, /):
    from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
    print(stable_repr__expand_top_layer(list_islice_(sz, iterable)))
    return
def apply_may_args4islice_(may_args4islice, iterable, /):
    it = iter(iterable)
    if not may_args4islice is None:
        args4islice = may_args4islice
        try:
            args4islice = iter(args4islice)
        except TypeError:
            #int??
            sz = args4islice
            args4islice = [sz]
        it = islice(it, *args4islice)
    return it

from seed.iters.apply_may_args4islice_ import apply_may_args4islice_
from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_
from seed.iters.apply_may_args4islice_ import *

