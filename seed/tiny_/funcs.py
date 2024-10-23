

__all__ = '''
    no_op
    echo_args_kwargs
    echo_kwargs
    echo_args
    echo

    unbox_
    unbox
    fst
    snd
    const
    lazy
    lazy_raise_v
    lazy_raise_f
    eq
    not_eq
    is_
    not_is
    in_
    not_in

    flip
    neg_flip

    xor
    xnor
    not_

    with_key
    mk_fprint
    fprint
    py_cmp
    int2cmp
    '''.split()


no_op = lambda *args, **kwargs:None
echo_args_kwargs = lambda *args, **kwargs:(args, kwargs)
echo_kwargs = lambda **kwargs:kwargs
echo_args = lambda *args: args
echo = lambda x,/:x

def unbox_(default, it01, /):
    it01 = iter(it01)
    x = next(it01, default)
    [] = it01
    return x
def unbox(it1, /):
    [x] = it1
    return x
def fst(seq, /): return seq[0]
def snd(seq, /): return seq[1]
def const(a, /): return lambda _,/:a
def lazy(a, /): return lambda:a
def lazy_raise_v(exc, /): raise exc
def lazy_raise_f(mk_exc, /): raise mk_exc()
def eq(a, /): return lambda b,/: a==b
def not_eq(a, /): return lambda b,/: a!=b
def is_(a, /): return lambda b,/: a is b
def not_is(a, /): return lambda b,/: a is not b
#def contains(c, /): return lambda x,/: x in c
#def not_contains(c, /): return lambda x,/: x not in c
def in_(c, /): return lambda x,/: x in c
def not_in(c, /): return lambda x,/: x not in c

def flip(op, /): return lambda a,b,/: op(b, a)
def neg_flip(cmp, /): return lambda a,b,/: -cmp(b, a)


def xor(a, b, /):
    return bool(a) != bool(b)
def xnor(a, b, /):
    return bool(a) == bool(b)
def not_(b, /): return not b

def with_key(key, iterable, /):
    '''with_key=map_with_input :: (a->k) -> Iter a -> Iter (k, a)'''
    # key at first as dict(...)
    for x in iterable:
        yield key(x), x


def mk_fprint(file):
    def fprint(*args, **kw):
        print(*args, file=file, **kw)
    return fprint
def fprint(*args, file, **kw):
    print(*args, file=file, **kw)

def py_cmp(a, b, /):
    # Ord a => a -> a -> -> (-1|0|+1)
    if a == b: return 0
    return -1 if a < b else +1

def int2cmp(i, /):
    # int -> (-1|0|+1)
    if not i:
        return 0
    return -1 if i < 0 else +1


from seed.tiny_.funcs import no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, unbox_, unbox, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, not_, with_key, mk_fprint, fprint, py_cmp, int2cmp
from seed.tiny_.funcs import *
