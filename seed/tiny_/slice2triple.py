#from seed.tiny_.slice2triple import slice2triple, slice2item, slices2iter_items, slices2items, slices2dict, items2dict__reject_duplicates
#from seed.tiny_.slice2triple import slice2triple, fix_slice_by_len, fix_slice_by_len_of
#from seed.tiny_.slice2triple import slice2triple_, fix_slice_by_len_, fix_slice_by_len_of_
#from seed.tiny_.slice2triple import slice2triple, range2triple, convert_triple_as_, range2triple_, slice2triple_



__all__ = '''
    slice2triple
    range2triple
    convert_triple_as_
        range2triple_
        slice2triple_

    slice2item
    slices2iter_items
    slices2items
    slices2dict
    items2dict__reject_duplicates

    echo_key
    fix_slice_by_len
    fix_slice_by_len_of

    fix_slice_by_len_
    fix_slice_by_len_of_
    '''.split()

from seed.tiny_.echo_key import echo_key
from seed.tiny_.funcs import echo_args
from seed.debug.expectError import expectError

def range2triple(range_, /):
    'range -> (.start, .stop, .step)  #range is both immutable and hashable, diff slice'
    #check_type_is(range_, range)
    assert type(range_) is range
    return range_.start, range_.stop, range_.step
assert range2triple(range(3, 9, 2)) == (3, 9, 2)


hash(range(5))
assert expectError(TypeError, lambda:hash(slice(1,5)))


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

#slice.indices(len) -> (start, stop, stride)
def fix_slice_by_len(length, slice_, /):
    return fix_slice_by_len_(None, length, slice_)
def fix_slice_by_len_of(seq, slice_, /):
    return fix_slice_by_len_of_(None, seq, slice_)



_output_type2mk = {
    tuple: echo_args
    ,range: range
    ,slice: slice
    }
_output_type2mk[None] = _output_type2mk[tuple]

def convert_triple_as_(may_output_type, triple, /):
    (start, stop, stride) = triple
    mk = _output_type2mk[may_output_type]
    return mk(start, stop, stride)

def range2triple_(may_output_type, range_, /):
    triple = range2triple(range_)
    return convert_triple_as_(may_output_type, triple)
def slice2triple_(may_output_type, slice_, /):
    triple = slice2triple(slice_)
    return convert_triple_as_(may_output_type, triple)
def fix_slice_by_len_(may_output_type, length, slice_, /):
    triple = slice_.indices(length)
    return convert_triple_as_(may_output_type, triple)

def fix_slice_by_len_of_(may_output_type, seq, slice_, /):
    return fix_slice_by_len_(may_output_type, len(seq), slice_)

fix_slice_by_len
fix_slice_by_len_of

slice2triple_
fix_slice_by_len_
fix_slice_by_len_of_


assert (0,4,1) == fix_slice_by_len(4, echo_key[:])
assert (4-1,-1,-1) == fix_slice_by_len(4, echo_key[::-1])
assert (4-1,-1,-1) == fix_slice_by_len_of(range(4), echo_key[::-1])



