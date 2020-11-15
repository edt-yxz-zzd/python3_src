r"""
async_vs_recur

does async have max depth stack call limit?


py script/try_python/try_std_libs/try_async/async_vs_recur.py

#"""


class Int:
    def __init__(sf, i):
        sf.i = i
    def __iadd__(sf, j):
        sf.i += j
        return sf
    def __repr__(sf):
        return f"Int({sf.i!r})"

def recur(depth):
    #print(depth)
    depth += 1
    recur(depth)


def main_recur():
    i = Int(0)
    try:
        recur(i)
    except Exception as e:
        return i.i
        print(e)
        input(Exception)
        raise
    except BaseException as e:
        print(e)
        input(BaseException)
        raise

############################
############################
############################
############################
############################


async def arecur(depth):
    #print(depth)
    depth += 1
    await arecur(depth)


def main_arecur():
    i = Int(0)
    c = arecur(i)
    ############################
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(c)
    except Exception as e:
        return i.i
        print(e)
        input(Exception)
        raise
    except BaseException as e:
        print(e)
        input(BaseException)
        raise
    finally:
        loop.close()

i = main_recur()
print(i)
i = main_arecur()
print(i)


r"""
collections.abc.Generator
6.2.9.1. Generator-iterator methods
#"""

from collections.abc import Generator
def flatten_recur(g, *, value=None):
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
i = main_bin_recur(2**13, 2**16)
print(i)

