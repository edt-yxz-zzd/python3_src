

'TODO: rewrite, replace ValueError'


__all__ = ('explain_node',)

def is_of_type(obj, type_):
    t = type_
    return t is None or type(obj) == t

##def is_of_type_or_None(obj, type_):
##    return obj is None or is_of_type(obj, type_)



def explain_node(node, types, *,
                 node_type=tuple, nrequired=0,
                 required_indices=(), is_of_type=is_of_type):
    r'''reposition the args. insert None if necessary


usage:
    1) multiple signature of a function
        f's signature: f(a, b) or f(a, c, b) or f(a, b, d)
        def f(a, b_or_c, void_or_b_or_d=None):...
        try to find out the proper signature
    2) node in tree of ast or HTML...
        ...
example:
    >>> types = [str, tuple, dict, list]
    >>> explain_node(('tag', {'kw':'args'}), types = types)
    ['tag', None, {'kw': 'args'}, None]
    >>> explain_node(('tag', ('arg',), ['child']), types = types)
    ['tag', ('arg',), None, ['child']]
    >>> explain_node(('tag',), types = types)
    ['tag', None, None, None]
    >>> explain_node((), types = types)
    [None, None, None, None]
    >>> explain_node((), types = types, nrequired=1)
    Traceback (most recent call last):
        ...
    ValueError: not 0 <= nrequired <= len(node) <= len(types)
    >>> explain_node(('tag',), types = types, required_indices=[1])
    Traceback (most recent call last):
        ...
    ValueError: node[1] missing.
    >>> explain_node([], types = types)
    Traceback (most recent call last):
        ...
    ValueError: unrecognize node type.
    >>> explain_node([], types = types, node_type=None)
    [None, None, None, None]

'''
    if not is_of_type(node, node_type):
        raise ValueError('unrecognize node type.')

    #types = list(types)
    if not 0 <= nrequired <= len(node) <= len(types): # not iter obj
        raise ValueError('not 0 <= nrequired <= len(node) <= len(types)')

    itypes = iter(types)
    inode = iter(node)
    r = [(t,x) for i, t, x in zip(range(nrequired), itypes, inode)]
    for t, x in r:
        if not is_of_type(x, t):
            raise ValueError('node required item of error type.')

    r = [x for t, x in r]
    got = [True] * len(r)
    for x in inode:
        for t in itypes:
            if not is_of_type(x, t):
                r.append(None)
                got.append(False)
            else:
                r.append(x)
                got.append(True)
                break
        else:
            raise ValueError('unrecognize type of node optional item.')

    assert len(r) == len(got)
    r.extend(None for _ in itypes)
    got += [False] * (len(r) - len(got))
    for i in required_indices:
        if not got[i]:
            raise ValueError('node[{}] missing.'.format(i))
    
    assert len(types) == len(r)
    for t, x in zip(types, r):
        #if not is_of_type_or_None(x, t): print(x, t)
        assert x == None or is_of_type(x, t)
    return r




if __name__ == "__main__":
    import doctest
    doctest.testmod()


