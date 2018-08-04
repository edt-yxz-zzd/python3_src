
'''
slice twice will yield two different object!!
does these object use the same original tuple? no
but will they reference to the same original memory area?
since tuple may need to calculate the hash key or likes, time spent grows.
why the time of list slice vivi that of tuple, growing but not o(n)?
'''

from sys import getrefcount
from timeit import timeit

from sand import is_main

def throw_if_not_tuple(t):
    if not isinstance(t, tuple):
        raise ValueError('not tuple')
    return

def is_slice_all_self(t):
    throw_if_not_tuple(t)

    L = len(t)
    return t is t[0:L]

def are_slice_twice_results_the_same(t, *slice_args):
    throw_if_not_tuple(t)
    
    return t[slice(*slice_args)] is t[slice(*slice_args)]

def does_slice_use_old_tuple(t, *slice_args):
    throw_if_not_tuple(t)
    
    old = getrefcount(t)
    s = t[slice(*slice_args)]
    new = getrefcount(t)
    del s
    if old != getrefcount(t):
        raise logic-error

    if new != old and new != old+1:
        raise logic-error

    return new == old+1
    
def does_slice_use_old_memory_data(t, *, number=10, max_step = 10):
    throw_if_not_tuple(t)
    ls = list(t)
    
    ft = lambda: t[sl]
    fls = lambda : ls[sl]
    ftg = lambda: tuple(x for x in tsl)
    flsg = lambda: list(x for x in tsl)

    steps = list(range(max_step, 0, -1))

    fs = [ft, fls, ftg, flsg]
    rs = []
    for step in steps:
        sl = slice(None, None, -step)
        tsl = t[sl]
        r = tuple(timeit(f, number=number) for f in fs)
        rs.append(r)
        
    print('1/step: tuple[slice], list[slice], tuple(iterable), list(iterable)')
    if rs:
        base = rs[0][0]
        print('base =', base)
    for n, r in zip(steps, rs):
        print(1/n, tuple(x/base for x in r))

    return
    


def main():
    t = (1, 2, [], {})
    slice_args_ls = [(None, None), (1, 2), (None, -2), (2, None), (None, None, -2)]
    
    print('is_slice_all_self', is_slice_all_self(t))
    
    for slice_args in slice_args_ls:
        print('are_slice_twice_results_the_same',
              are_slice_twice_results_the_same(t, *slice_args))
    
    for slice_args in slice_args_ls:
        print('does_slice_use_old_tuple',
              does_slice_use_old_tuple(t, *slice_args))

    t = tuple(range(1000000))
    print('does_slice_use_old_memory_data')
    does_slice_use_old_memory_data(t)
    return

if is_main(__name__):
    main()
    pass







    
