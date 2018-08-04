
'''

zip_me v.s. icut_to/icut_seq_to
    zip_me iter overlap blocks
    icut_to iter nonoverlap blocks

zip_me v.s. zip_meN
    zip_me will use zip_me2/zip_me1 for N = 2/1
        so, the result type are different
    zip_meN's result is a ZipMe
        so, user can access to the remains data after loop
        zip_meN.tail #####################################




########################## example:
    ########## zip_me/zip_me2
        >>> diff = lambda it: (b-a for a, b in zip_me2(it))
        >>> [*diff([1,2,5,12,6])]
        [1, 3, 7, -6]

    ########## zip_meN
        >>> it = zip_meN(2, [1,2,-1,0,3])
        >>> iter(it) is it
        True
        >>> type(it) is ZipMe
        True
        >>> list(it)
        [(1, 2), (2, -1), (-1, 0), (0, 3)]
        >>> it.tail
        (3,)




##################
for a, b in zip(ls, ls[1:]):
    ...
compare with icut

it seems previous version like icut,
    this version cause a bug in novel_split<-re_partition_to_head_bodyls<-zip_me
    replace it by icut_seq_to


'''


__all__ = '''
    zip_me2
    zip_me
    zip_meN
    '''.split()

from collections import deque
#from .head import take_lt
import itertools


class ZipMe:
    def __init__(self, n, iterable):
        if n < 1:
            raise ValueError('n < 1')



        self.__itI = iter(iterable)
        self.__tail = None
        self.__itO = self.__make_itO(n)

    @property
    def tail(self):
        'after iter all tuples, tail gives the remain elements'
        if self.__itI is not None:
            raise TypeError('not yet StopIteration')
        assert type(self.__tail) is tuple
        return self.__tail

    def __iter__(self):
        return self
    def __next__(self):
        return next(self.__itO)
    def __make_itO(self, N):
        assert N >= 1
        first_n = itertools.islice(self.__itI, N)
        dq = deque(first_n, N)
        assert len(dq) <= N
        assert N == dq.maxlen
        del first_n

        if len(dq) == N:
            yield tuple(dq)
            for x in self.__itI:
                dq.append(x)
                yield tuple(dq)
            else:
                dq.popleft()

        assert len(dq) < N
        self.__itI = None # to notify self.tail the end of iter
        self.__tail = tuple(dq)
        return

def zip_me(N, iterable):
    '''zip(ls, ls[1:]) <==> zip_me(2, ls); N >= 1'''
    if N <= 2:
        if N == 2: return zip_me2(iterable)
        elif N == 1: return zip_me1(iterable)
        assert N <= 0
        pass # use zip_meN to raise
    return zip_meN(N, iterable)
def zip_meN(N, iterable):
    '''zip(ls, ls[1:]) <==> zip_me(2, ls); N >= 1'''
    return iter(ZipMe(N, iterable))

def zip_me1(iterable):
    '''zip(ls) <==> zip_me1(ls)'''
    return zip(iterable)
def zip_me2(iterable):
    '''zip(ls, ls[1:]) <==> zip_me2(ls)'''
    it = iter(iterable); del iterable
    for fst in it:
        break
    else:
        return
    for snd in it:
        yield fst, snd
        fst = snd
    return


def _test():
    assert list(zip(range(5))) == list(zip_me(1, range(5)))
    assert list(zip(range(5), range(1,5))) == list(zip_me(2, range(5)))
    assert list(zip(range(5), range(1,5), range(2,5))) == list(zip_me(3, range(5)))


    assert list(zip(range(5), range(1,5))) == list(zip_me2(range(5)))

    assert list(zip(range(5))) == list(zip_meN(1, range(5)))
    assert list(zip(range(5), range(1,5))) == list(zip_meN(2, range(5)))
    assert list(zip(range(5), range(1,5), range(2,5))) == list(zip_meN(3, range(5)))


if __name__ == "__main__":
    _test()
    import doctest
    doctest.testmod()




