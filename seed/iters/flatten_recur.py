
r"""
see also:
    seed.iters.flatten_recur
        view ../../python3_src/seed/iters/flatten_recur.py
    seed.func_tools.recur5yield
        view ../../python3_src/seed/func_tools/recur5yield.py

flatten_recur

to avoid stack-overflow when calling recur func

from seed.iters.flatten_recur import flatten_recur


==========================
collections.abc.Generator
6.2.9.1. Generator-iterator methods

==========================
must start with g.send(None)
next(g) <==> g.send(None)
return_value is StopIteration.value

#"""

__all__ """
    flatten_recur
    """.split()

from collections.abc import Generator
def flatten_recur(g:Generator, /, *, value:object=None):
    assert isinstance(g, Generator)
    #assert iter(g) is g
    ls = [g]
    while ls:
        g = ls[-1]
        try:
            child_g = g.send(value)
        except StopIteration as e:
            #print(e)
            #raise
            value = e.value #return_value
            ls.pop()
        else:
            assert isinstance(child_g, Generator)
            ls.append(child_g)
            value = None
    return value

r"""#example

def bin_recur(max_depth, t, depth, d):
    #print(depth, d)
    if depth >= max_depth:
        return 1
        return depth
    depth += d
    a = yield bin_recur(max_depth, t, depth, d)
    b = yield bin_recur(max_depth, t, depth, d*t)
    return a+b
def main_bin_recur(max_depth=2**13, t=4, depth=0, d=1):
    return flatten_recur(bin_recur(max_depth, t, depth, d))
i = main_bin_recur(64, 2)
print(i)
assert i==27338
i = main_bin_recur(2**13, 2**16)
print(i)
assert i==2**14

#"""



