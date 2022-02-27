#from seed.tiny_.slice2triple import slice2triple, slice2item, slices2iter_items, slices2items, slices2dict, items2dict__reject_duplicates

__all__ = '''
    slice2triple

    slice2item
    slices2iter_items
    slices2items
    slices2dict
    items2dict__reject_duplicates
    '''.split()

def slice2triple(slice_, /):
    'slice -> (.start, .stop, .step)  #slice is immutable but unhashable, to be used as special-key for __getitem__'
    #check_type_is(slice_, slice)
    assert type(slice_) is slice
    return slice_.start, slice_.stop, slice_.step
assert slice2triple(slice(3, 9, 2)) == (3, 9, 2)


def slice2item(kv, /):
    if not type(kv) is slice: raise TypeError
    k, v, xxx = slice2triple(kv)
    if not xxx is None: raise TypeError
    return k, v
def slices2iter_items(slices, /):
    return map(slice2item, slices)
def slices2items(slices, /):
    return tuple(slices2iter_items(slices))
def slices2dict(slices, /):
    return items2dict__reject_duplicates(slices2iter_items(slices))

assert dict([(1,1)]*2) == {1: 1}
assert {1:2, 1:3} == {1: 3}
    #accept duplicates!!
#reversed({1:2, 1:3}) #ok??

def items2dict__reject_duplicates(pairs, /):
    d = {}
    for sz, (k, v) in enumerate(pairs, 1):
        d[k] = v
        if not len(d) == sz: raise KeyError(k)
    return d



