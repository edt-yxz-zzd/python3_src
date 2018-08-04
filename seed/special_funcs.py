

empty_set = frozenset() # used in set_union
identity_func = identity = lambda x:x # bug: once named as "identify"
set_union = lambda iterables: empty_set.union(*iterables)


def iempty():
    'iter_empty ::= iter("")'
    return
    yield
assert list(iempty()) == []
assert list(iempty()) == []


# null_iterable == iempty()
