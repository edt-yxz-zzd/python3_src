
#copy from:from seed.io.savefile__str_tuple import iter_split_ex_by_
def iter_split_ex_by_(substr, s, /):
    '-> Iter (gap, smay substr)  # str | bytes'
    if not len(substr): raise ValueError
    L = len(substr)
    i = 0
    while 1:
        j = s.find(substr, i)
        if j == -1:break
        gap = s[i:j]
        yield gap, substr
        i = j+L
    gap = s[i:]
    yield gap, substr[:0]
    return

from seed.str_tools.iter_split_ex_by_ import iter_split_ex_by_

