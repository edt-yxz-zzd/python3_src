
#e ../../python3_src/seed/iters/iter_with.py

def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_callable
    def iter_funcs5may_funcs_(may_funcs, /):
        for m in may_funcs:
            f = ifNone(m, echo)
            check_callable(f)
            yield f

    def iter_with_(may_funcs, iterable, /):
        'Iter (may (x->y)) -> Iter x -> Iter tuple<y>'
        funcs = iter_funcs5may_funcs_(may_funcs)
        funcs = tuple(funcs)
        for x in iterable:
            ts = tuple(f(x) for f in funcs)
            yield ts

    return iter_with_

iter_with_ = __()


from seed.iters.iter_with import iter_with_


