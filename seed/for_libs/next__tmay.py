
def next__tmay(iterator, /):
    try:
        return (next(iterator),)
    except StopIteration:
        return ()
    Nothing = []
    m = next(iterator, Nothing)
    if m is Nothing:
        tmay = ()
    else:
        value = m
        tmay = (value,)
    return tmay
head__tmay = next__tmay
safe_head = head__tmay

assert () == next__tmay(iter([]))
assert (9,) == next__tmay(iter([9,5]))



