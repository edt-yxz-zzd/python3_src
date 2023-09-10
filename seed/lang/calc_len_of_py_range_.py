r'''[[[
e ../../python3_src/seed/lang/calc_len_of_py_range_.py

#]]]'''#'''



def calc_len_of_py_range_(array, /):
    r'''see:seed.seq_tools.bisearch

# e ../lots/NOTE/Python/python-bug/len-bug.txt
>>> len(range(2**80))
Traceback (most recent call last):
    ...
OverflowError: Python int too large to convert to C ssize_t
>>> range(2**80).__len__()
Traceback (most recent call last):
    ...
OverflowError: Python int too large to convert to C ssize_t

'''#'''

    (start, stop, step) = (array.start, array.stop, array.step)

    if step < 0:
        (start, stop, step) = (-start, -stop, -step)

    return max(0, 1+ (stop -start -1) // step)



assert calc_len_of_py_range_(__ := range(6)) == len(__)
assert calc_len_of_py_range_(__ := range(0)) == len(__)
assert calc_len_of_py_range_(__ := range(-1)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, -1)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, 1)) == len(__)

assert calc_len_of_py_range_(__ := range(3, 7, 1)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 2)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 3)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 4)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 5)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 6)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 7)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 8)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -1)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -2)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -3)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -4)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -5)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -6)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -7)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -8)) == len(__)


from seed.lang.calc_len_of_py_range_ import calc_len_of_py_range_
