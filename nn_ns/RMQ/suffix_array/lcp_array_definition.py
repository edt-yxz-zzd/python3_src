

from .len_lcp import len_lcp
def lcp_array_definition(array, SA):
    ''':: Ord a => [a] -> [ArrayIdx] -> [UInt]

LCP<array> = [len_lcp(suffices[i], suffices[i+1]) for i in range(L-1)]
    where suffices = [array[SA<array>[i]:] for i in range(L)]
          L = len(array)

len(LCP) + 1 == Len(array) == len(SA)
'''
    assert len(array) == len(SA)
    def suffix(i):
        return array[SA[i]:]
    L = len(array)
    suffices = [suffix(i) for i in range(L)]
    LCP = [len_lcp(suffices[i], suffices[i+1]) for i in range(L-1)]
    return LCP



