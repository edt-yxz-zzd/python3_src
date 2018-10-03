
def calc_common_prefix_length(ls1, ls2):
    idx = -1
    for a, b, idx in zip(ls1, ls2, range(len(ls2))):
        if a != b:
            return idx
    else:
        return idx+1

assert calc_common_prefix_length([], []) == 0
assert calc_common_prefix_length([], [1]) == 0
assert calc_common_prefix_length([1], [1]) == 1
assert calc_common_prefix_length([1,3], [1,2]) == 1

