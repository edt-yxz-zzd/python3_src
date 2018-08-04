
# v.s. project_keys

from itertools import islice as _islice
def unzip(n, iterable):
    '''inverse of zip()

unzip(n, iterable) -> n lists
assert all(len(list(e)) == n for e in iterable)
'''
    if not n >= 0:
        raise ValueError('not n >= 0')

    lsls = tuple([] for _ in range(n))
    for xs in iterable:
        xs = _islice(xs, n+1)
        xs = tuple(xs)
        if not len(xs) == n:
            raise ValueError('not all(len(list(e)) == n for e in iterable)')
        for x, ls in zip(xs, lsls):
            ls.append(x)
    return lsls

assert unzip(3, [(1,2,4), (1,3,9)]) == ([1,1], [2,3], [4,9])



def unzip_keys(keys, iterable):
    'keys is a seq in concept; order is important'
    keys = tuple(keys)
    n = len(keys)
    lsls = tuple([] for _ in range(n))
    for d in iterable:
        for key, ls in zip(keys, lsls):
            ls.append(d[key])
    return lsls
assert unzip_keys(range(3), [(1,2,4), (1,3,9)]) == ([1,1], [2,3], [4,9])
assert unzip_keys(range(2), [(1,2,4), (1,3,9)]) == ([1,1], [2,3])



        
    
    



