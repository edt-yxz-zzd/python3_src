

def nub(iterable):
    '''removes duplicate elements. keeps only the first occurrence of each element.'''
    s = set()
    for x in iterable:
        if x not in s:
            s.add(x)
            yield x

assert list(nub([1,0,1])) == [1,0]
