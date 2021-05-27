
def lookup__tmay(lookupable, key, /):
    try:
        return (lookupable[key],)
    except LookupError:
        return ()
assert () == lookup__tmay({}, 3)
assert (5,) == lookup__tmay({3:5}, 3)
assert () == lookup__tmay([2,3,5], 3)
assert (7,) == lookup__tmay([2,3,5,7], 3)


