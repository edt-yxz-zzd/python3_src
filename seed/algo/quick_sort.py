

'''
unstable inplace quick sort
'''

__all__ = '''
    unstable_inplace_quick_sort
'''.split()

import random
import operator
from seed.algo.is_sorted import is_sorted
from seed.special_funcs import identity

class lt2key:
    @staticmethod
    def entity_lt(e0, e1):
        return e0 < e1
    def __init__(self, entity):
        self.entity = entity
    def __lt__(self, other):
        if type(other) is not type(self):
            return NotImplemented
        return type(self).entity_lt(self.entity, other.entity)
    
class key2lt:
    def __init__(self, key):
        if key is None:
            key = identity
        self.key = key
    def __call__(self, e0, e1):
        # __lt__
        return self.key(e0) < self.key(e1)
    
    
        

def stable_noninplace_quick_sort(array, *, __lt__=None):
    ':: Seq a -> (a->a->Bool) -> [a]'
    if __lt__ is None:
        __lt__ = operator.__lt__
    ls = _stable_noninplace_quick_sort(array, __lt__)
    assert type(ls) is list
    assert len(ls) == len(array)
    return ls


def _stable_noninplace_quick_sort(array, __lt__):
    if len(array) < 2:
        return list(array)
    
    # choose pivot
    begin = 0
    end = len(array)
    mid = random.randrange(begin, end)
    pivot = array[mid]

    left = []
    right = []
    
    for x in array[begin:mid]:
        if __lt__(pivot, x):
            # x gt pivot
            right.append(x)
        else:
            # x le pivot
            left.append(x)
    for x in array[mid+1:end]:
        if __lt__(x, pivot):
            # x lt pivot
            left.append(x)
        else:
            # x ge pivot
            right.append(x)
    left = _stable_noninplace_quick_sort(left, __lt__)
    right = _stable_noninplace_quick_sort(right, __lt__)
    ls = left; del left
    ls.append(pivot)
    ls.extend(right); del right
    assert len(ls) == len(array)
    return ls


    
    
    
def _swap(array, first, last):
    assert 0 <= first <= last < len(array)
    
    if first < last:
        array[first], array[last] = array[last], array[first]
    elif first == last:
        return
    else:
        raise ValueError('last > first')
    
def unstable_inplace_quick_sort(array, begin=None, end=None,
                                *, __lt__=None, swap=None):
    '''
unstable_inplace_quick_sort :: Array a -> Int -> Int
                                -> (a -> a -> Bool)
                                -> (Array a -> Int -> Int -> IO ())
                                -> IO ()
array :: Array a
__lt__ :: a -> a -> Bool
swap :: Array a -> Int -> Int -> IO ()
    # swap a i j : assert i <= j
'''
    if begin is None:
        begin = 0
    if end is None:
        end = len(array)
    if __lt__ is None:
        __lt__ = operator.__lt__
    if swap is None:
        swap = _swap
    assert 0 <= begin <= end <= len(array)

    #print(array)
    _unstable_inplace_quick_sort(array, begin, end, __lt__, swap)


def _unstable_inplace_quick_sort_ver1(array, begin, end, __lt__, swap):
    if end - begin < 2:
        return

    # choose pivot
    mid = random.randrange(begin, end)
    # pivot = array[mid]
    # begin  ...    mid    ...  end
    #       .(?).  pivot  .(?).
    
    swap(array, begin, mid); del mid
    pivot = array[begin]
    le_begin = le_end = begin + 1
    gt_begin = gt_end = end
    # begin le_begin     ...    le_end  ...  gt_begin    ...    gt_end==end
    # pivot          .(<=pivot).       .(?).          .(>pivot).
    while le_end < gt_begin:
        if __lt__(pivot, array[le_end]):
            # x gt pivot
            gt_begin -= 1
            swap(array, le_end, gt_begin)
        else:
            # x le pivot
            le_end += 1
    assert le_end == gt_begin
    # begin le_begin     ...    le_end==gt_begin    ...    gt_end==end
    # pivot          .(<=pivot).                .(>pivot).
    
    if le_begin < le_end:
        le_last = le_end - 1
        swap(array, begin, le_last)
    le_begin -= 1
    le_end -= 1
    # le_begin     ...      le_end gt_begin    ...    gt_end==end
    #          .(<=pivot).   pivot          .(>pivot).

    assert begin == le_begin <= le_end < le_end+1 == gt_begin <= gt_end == end
    assert (le_end - le_begin) + 1 + (gt_end - gt_begin) == end - begin
    _unstable_inplace_quick_sort(array, le_begin, le_end, __lt__, swap)
    _unstable_inplace_quick_sort(array, gt_begin, gt_end, __lt__, swap)


def _unstable_inplace_quick_sort(array, begin, end, __lt__, swap):
    if end - begin < 2:
        return

    # choose pivot
    mid = random.randrange(begin, end)
    # pivot = array[mid]
    # begin  ...    mid    ...  end
    #       .(?).  pivot  .(?).
    
    swap(array, begin, mid); del mid
    pivot = array[begin]
    le_begin = le_end = begin + 1
    ge_begin = ge_end = end
    # begin le_begin     ...    le_end  ...  ge_begin     ...    ge_end==end
    # pivot          .(<=pivot).       .(?).          .(>=pivot).
    while True:
        while le_end < ge_begin:
            if __lt__(pivot, array[le_end]):
                # x gt pivot
                break
            else:
                # x le pivot
                le_end += 1
        while le_end < ge_begin:
            if __lt__(array[ge_begin-1], pivot):
                # x lt pivot
                break
            else:
                # x ge pivot
                ge_begin -= 1
        if ge_begin - le_end >= 2:
            swap(array, le_end, ge_begin-1)
            le_end += 1
            ge_begin -= 1
        else:
            if le_end < ge_begin:
                assert le_end + 1 == ge_begin
                le_end += 1
            assert le_end == ge_begin
            break
    assert le_end == ge_begin
    # begin le_begin     ...    le_end==ge_begin    ...    ge_end==end
    # pivot          .(<=pivot).                .(>=pivot).
    
    if le_begin < le_end:
        le_last = le_end - 1
        swap(array, begin, le_last)
    le_begin -= 1
    le_end -= 1
    # le_begin     ...     le_end ge_begin    ...    ge_end==end
    #          .(<=pivot).  pivot         .(>=pivot).

    assert begin == le_begin <= le_end < le_end+1 == ge_begin <= ge_end == end
    assert (le_end - le_begin) + 1 + (ge_end - ge_begin) == end - begin
    _unstable_inplace_quick_sort(array, le_begin, le_end, __lt__, swap)
    _unstable_inplace_quick_sort(array, ge_begin, ge_end, __lt__, swap)


def test_unstable_inplace_quick_sort_1(ls):
    ans = sorted(ls)
    unstable_inplace_quick_sort(ls)
    assert is_sorted(ls)
    assert ls == ans
    return True
def test_stable_noninplace_quick_sort_1(ls):
    ans = sorted(ls)
    ls = stable_noninplace_quick_sort(ls)
    assert is_sorted(ls)
    assert ls == ans
    return True



def iter_test_lsls(N):
    test_lsls = [[], [None],
                 [1, 1], [1, 2], [2, 1],
                 [1, 1, 2], [1, 2, 2], [1, 2, 1]]
    yield from test_lsls
    from itertools import permutations
    for n in range(N):
        for p in permutations(range(n)):
            yield list(p)
test_qsort_1_ls = [test_stable_noninplace_quick_sort_1,
                   test_unstable_inplace_quick_sort_1]
    
def test_qsorts():
    for test_qsort_1 in test_qsort_1_ls:
        for ls in iter_test_lsls(5):
            assert test_qsort_1(ls)
    return True

assert test_qsorts()















