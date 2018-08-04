


def len_lcp(*iterables):
    '''Eq a => Iter a -> Iter a -> UInt

length of longest common prefix of input
'''
    if not iterables: raise TypeError
    i = -1
    for i, ls in enumerate(zip(*iterables)):
        a = ls[0]
        if not all(a == b for b in ls[1:]):
            return i
    return i+1

