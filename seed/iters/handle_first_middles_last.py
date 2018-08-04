
__all__ = ['handle_first_middles_last']

def handle_first_middles_last(iterable
    , handle_first, handle_middle, handle_last, handle_the_only_one
    , handle_empty=None):
    '''
input:
    # Handler = None | (a -> Iterable b)
    iterable :: Iterable a
    handle_first :: Handler
    handle_middle :: Handler
    handle_last :: Handler
    handle_the_only_one :: Handler
        all above: default = lambda a: []

    handle_empty :: None | (() -> Iterable b)
        default = lambda: []
        why not (Iterable b) directly?
            since reusable handle_empty is better
output:
    output :: Iterator b


example:
    >>> this = handle_first_middles_last
    >>> list_this = lambda *args: list(this(*args))
    >>> one_iter = lambda f: lambda a: [f(a)]
    >>> hfirst = one_iter(len)
    >>> hmiddle = one_iter(str)
    >>> hlast = one_iter(type)
    >>> honly = one_iter(repr)
    >>> hempty = lambda: ({},)

    >>> list_this([], hfirst, hmiddle, hlast, honly, hempty)
    [{}]
    >>> list_this([], hfirst, hmiddle, hlast, honly)
    []

    >>> list_this([''], hfirst, hmiddle, hlast, honly, hempty)
    ["''"]
    >>> list_this([''], hfirst, hmiddle, hlast, None, hempty)
    []

    >>> list_this(['abc', ()], hfirst, hmiddle, hlast, honly, hempty)
    [3, <class 'tuple'>]
    >>> list_this(['abc', ()], None, hmiddle, hlast, honly, hempty)
    [<class 'tuple'>]
    >>> list_this(['abc', ()], hfirst, hmiddle, None, honly, hempty)
    [3]
    >>> list_this(['abc', ()], None, hmiddle, None, honly, hempty)
    []

    >>> list_this(['abc', 1, 2, ()], hfirst, hmiddle, hlast, honly, hempty)
    [3, '1', '2', <class 'tuple'>]
    >>> list_this(['abc', 1, ()], hfirst, hmiddle, hlast, honly, hempty)
    [3, '1', <class 'tuple'>]
    >>> list_this(['abc', 1, ()], None, hmiddle, hlast, honly, hempty)
    ['1', <class 'tuple'>]
    >>> list_this(['abc', 1, ()], hfirst, None, hlast, honly, hempty)
    [3, <class 'tuple'>]
    >>> list_this(['abc', 1, ()], hfirst, hmiddle, None, honly, hempty)
    [3, '1']
    >>> list_this(['abc', 1, ()], hfirst, None, None, honly, hempty)
    [3]
    >>> list_this(['abc', 1, ()], None, hmiddle, None, honly, hempty)
    ['1']
    >>> list_this(['abc', 1, ()], None, None, hlast, honly, hempty)
    [<class 'tuple'>]
    >>> list_this(['abc', 1, ()], None, None, None, honly, hempty)
    []

'''
    it = iter(iterable); del iterable

    for first_or_the_only_one in it:
        break
    else:
        # empty
        if handle_empty is not None:
            yield from handle_empty()
        return # yield nothing

    for maybe_last in it:
        first = first_or_the_only_one
        if handle_first is not None:
            yield from handle_first(first)
        break
    else:
        the_only_one = first_or_the_only_one
        if handle_the_only_one is not None:
            yield from handle_the_only_one(the_only_one)
        return


    if handle_middle is not None:
        maybe_middle = maybe_last
        for maybe_last in it:
            middle = maybe_middle
            yield from handle_middle(middle)
            maybe_middle = maybe_last
    else:
        for maybe_last in it: pass

    last = maybe_last
    if handle_last is not None:
        yield from handle_last(last)
    return

if __name__ == "__main__":
    import doctest
    doctest.testmod()

