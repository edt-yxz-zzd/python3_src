
__all__ = ['bisearch']


import operator
from seed.tiny import echo

def bisearch(x, array, begin=None, end=None
        , *, key=None, __lt__=None, result_case=2):
    '''see also : bisect

bisearch(x, a) == bisect_left(a, x), bisect_right(a, x)
bisearch(x, a, result_case=2) == bisect_left(a, x), bisect_right(a, x)
bisearch(x, a, result_case=0) == bisect_left(a, x)
bisearch(x, a, result_case=1) == bisect_right(a, x)

input:
    x :: k
    array :: Seq a
    begin, end :: None | UInt
        0 <= begin <= end <= len(array)
        default (begin, end) = (0, len(array))
    key :: None | (a -> k)
        default = echo
    __lt__ :: None | (k -> k -> bool)
        default = operator.__lt__
    result_case :: UInt = 2
        result_case = -1 | 0 | 1 | 2
        affect the output

        -1 - arbitrary_middle
            arbitrary_middle = arbitrary index in [middle_begin..middle_end]
            i.e. in range(middle_begin, middle_end+1)
            [arbitrary_middle == middle_end] <==> [x not in array]
        0 - lower_end == middle_begin
        1 - middle_end == upper_begin
        2 - (middle_begin, middle_end)

output:
    result :: UInt | (UInt, UInt)
        if result_case == -1:
            result = arbitrary_middle
            arbitrary_middle = arbitrary index in [middle_begin..middle_end]
            if arbitrary_middle == end or array[arbitrary_middle] != x:
                ==>> [x not in array]

        if result_case == 0:
            result = middle_begin
        if result_case == 1:
            result = middle_end
        if result_case == 2:
            result = (middle_begin, middle_end)

example:
    >>> test_bisearch()
    >>> test_bisearch2()

    >>> this = bisearch
    >>> this(-1, [])
    (0, 0)
    >>> this(-1, [6])
    (0, 0)
    >>> this(-1, [5,6])
    (0, 0)

    >>> this(3, [-1])
    (1, 1)
    >>> this(3, [-1,1])
    (2, 2)

    >>> this(1, ['123', [1], ''], key=len, __lt__=operator.__gt__)
    (1, 2)
    >>> this(5, [-6,6])
    (1, 1)
    >>> this(5, [-6,5,6])
    (1, 2)
    >>> this(5, [-6,5,6], result_case=-1)
    1
    >>> this(5, [-6,5,6], result_case=0)
    1
    >>> this(5, [-6,5,6], result_case=1)
    2
    >>> this(5, [-6,5,6], result_case=2)
    (1, 2)
    >>> this(5, [-6,5,5,6])
    (1, 3)
    >>> this(5, [-6,-6,5,5,6,6])
    (2, 4)
    >>> this(5, [-6,-6,5,5,6,6],1)
    (2, 4)
    >>> this(5, [-6,-6,5,5,6,6],2)
    (2, 4)
    >>> this(5, [-6,-6,5,5,6,6],3)
    (3, 4)
    >>> this(5, [-6,-6,5,5,6,6],4)
    (4, 4)
    >>> this(5, [-6,-6,5,5,6,6],5)
    (5, 5)
    >>> this(5, [-6,-6,5,5,6,6],1,6)
    (2, 4)
    >>> this(5, [-6,-6,5,5,6,6],1,5)
    (2, 4)
    >>> this(5, [-6,-6,5,5,6,6],1,4)
    (2, 4)
    >>> this(5, [-6,-6,5,5,6,6],1,3)
    (2, 3)
    >>> this(5, [-6,-6,5,5,6,6],1,2)
    (2, 2)
    >>> this(5, [-6,-6,5,5,6,6],1,1)
    (1, 1)
'''
    if key is None:
        key = echo
    if __lt__ is None:
        __lt__ = operator.__lt__
    if begin is None:
        begin = 0
    if end is None:
        end = len(array)

    if result_case not in (-1,0,1,2):
        raise ValueError(f'result_case == {result_case} not in [-1,0,1,2]')
    if not 0 <= begin <= end <= len(array):
        raise ValueError('not 0 <= begin <= end <= len(array)')


    def get_key(i):
        return key(array[i])

    old_begin = begin
    old_end = end

    # find middle, such that:
    #   * array[middle] <> x
    #   * or array[middle] > x if x not in array
    while begin < end:
        middle = (begin+end)//2
        y = get_key(middle)
        if __lt__(x, y):
            end = middle        # x < array[end]
        elif __lt__(y, x):
            begin = middle + 1  # array[begin-1] < x
        else:
            # assert array[middle] <> x
            # array[begin-1] < x == array[middle] < array[end]
            lower_end = middle
            upper_begin = middle + 1
            done = False
            break
    else:
        # array[begin-1] < x  < array[begin] is array[end]
        middle = begin
        # array[begin-1] < x  < array[begin] is array[middle] is array[end]
        assert begin == middle == end

        lower_end = upper_begin = middle
        lower = lower_end
        upper = upper_begin
        done = True

    # array[begin-1] < x  < array[end]
    # begin <= end
    arbitrary_middle = middle
    try:
      if __debug__:
        assert (arbitrary_middle == old_end
            or not __lt__(get_key(arbitrary_middle), x)
            )
        assert (arbitrary_middle == old_begin
            or not __lt__(x, get_key(arbitrary_middle-1))
            )
        assert (arbitrary_middle in [old_begin, old_end]
            or not __lt__(x, get_key(arbitrary_middle))

            # now, x < get_key(arbitrary_middle)
            # assert x not in array
            or __lt__(get_key(arbitrary_middle-1), x)
            )
    except:
        print(x, array, old_begin, old_end)
        raise
    if result_case == -1:
        return arbitrary_middle

    #print('begin, middle, end', begin, middle, end)
    lower_begin, upper_end = begin, end


    if not done and result_case != 1:
        # find lower bound
        begin, end = lower_begin, lower_end
        while begin < end:
            middle = (begin+end)//2
            y = get_key(middle)
            if __lt__(y, x):
                begin = middle + 1
            else:
                end = middle
        lower = end


    if not done and result_case != 0:
        # find upper bound
        begin, end = upper_begin, upper_end
        while begin < end:
            middle = (begin+end)//2
            y = get_key(middle)
            if __lt__(x, y):
                end = middle
            else:
                begin = middle + 1
        upper = begin

    if result_case == 0: return lower
    if result_case == 1: return upper
    if result_case == 2: return lower, upper
    raise ValueError(f'result_case == {result_case} not in [-1,0,1,2]')




def test_bisearch():
    data = [
        # [[(x, ans)...], array]
        [[(-1, (0, 0)), (0, (0, 0))], list(range(0))],
        [[(-1, (0, 0)), (0, (0, 1)), (1, (1, 1))], list(range(1))],
        [[(-1, (0, 0)), (0, (0, 1)), (1, (1, 2)), (2, (2, 2))], list(range(2))],
        [[(-1, (0, 0)), (0, (0, 1)), (1, (1, 2)), (2, (2, 3)), (3, (3, 3))], list(range(3))],
        ]

    for x_ans_ls, array in data:
        for x, ans in x_ans_ls:
            #print(array, x, ans, bisearch(x, array))
            assert ans == bisearch(x, array)
def test_bisearch2():
    import random
    from bisect import bisect_left, bisect_right
    minN, maxN = 0, 20
    for _ in range(10):
        a = [random.randrange(minN, maxN) for _ in range(30)]
        a.sort()
        for x in range(minN-1, maxN+1):
            assert bisearch(x, a) == (bisect_left(a, x), bisect_right(a, x))

this = bisearch
this(5, [-6,-6,5,5,6,6],4)
this(5, [-6,-6,5,5,6,6],5)
this(5, [-6,-6,5,5,6,6],1,1)



if __name__ == '__main__':
    test_bisearch()
    test_bisearch2()


if __name__ == "__main__":
    import doctest
    doctest.testmod()


















