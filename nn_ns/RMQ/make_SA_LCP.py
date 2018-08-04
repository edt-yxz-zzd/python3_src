
__all__ = '''
    make_SA_LCP
    make_SA
    '''.split()

from .suffix_array.uint_array2suffix_array__ver5 import uint_array2suffix_array

from seed.algo.bucket_sort.compress import compress as global_compress
from seed.types.view.mkSubSeqTransformView import mkSubSeqTransformView_or_notView
#from seed.iters.minmax import minmax_default



def make_SA(array, *, alphabet_size=None, LCP=False
        , make_RMQ=None
        , table=None
        , handle_if_basic_case=None
        , compress=True
        , array_element_transform=None
        , array_slice_or_range=None
        ):
    '''see: make_SA_LCP

diff make_SA_LCP:
    LCP default to False
'''
    return make_SA_LCP(array
            , alphabet_size = alphabet_size
            , LCP=LCP
            , make_RMQ=make_RMQ
            , table=table
            , handle_if_basic_case=handle_if_basic_case
            , compress=compress
            , array_element_transform=array_element_transform
            , array_slice_or_range=array_slice_or_range
            )
def make_SA_LCP(array, *, alphabet_size=None, LCP=True
        , make_RMQ=None
        , table=None
        , handle_if_basic_case=None
        , compress=True
        , array_element_transform=None
        , array_slice_or_range=None
        ):
    r''':: [UInt] -> (SA, LCP)

SA - suffix array of input
LCP - lengths of longest common prefix of neighbor suffices in SA
see:
    uint_array2suffix_array__ver5
    diff at:
        using compress
        using mkSubSeqTransformView_or_notView

time:
    assume
        make_RMQ.'__init__' = O(n)*ops
        make_RMQ.'__call__' = O(1)*ops
    O(L+alphabet_size)

let L = len(array)
input:
    array :: [a]
    alphabet_size :: None | UInt
        alphabet_size >= max(array, default=-1)+1
    LCP :: bool
        affect output type

    make_RMQ
    table
    handle_if_basic_case
        see: uint_array2suffix_array__ver5.py ::
            UIntArray2SuffixArray__ver5.uint_array2suffix_array

    array_element_transform :: None | (a -> UInt)
    array_slice_or_range :: None | slice | range
        see: SeqSliceView::check_range
        see: mkSubSeqTransformView_or_notView

output:
    result :: (SA, LCP) | SA
        #if LCP=True, then (SA, LCP)
        #else: SA

        len(SA) == L
        len(LCP) == max(0, L-1)

SA<array> = sorted(range(len(array)), key=lambda isuffix:array[isuffix:])
LCP<array> = [len_lcp(suffices[i], suffices[i+1]) for i in range(L-1)]
    where suffices = [array[isuffix:] for isuffix in SA<array>]


example:
    >>> this = make_SA_LCP
    >>> this(b'')
    ([], [])
    >>> this(b'231')
    ([2, 0, 1], [0, 0])
    >>> this([1,1,1,0])
    ([3, 2, 1, 0], [0, 1, 2])
    >>> this(b'112233112233')
    ([6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4], [6, 1, 5, 0, 4, 1, 3, 0, 1, 1, 2])
    >>> this([1,1,1])
    ([2, 1, 0], [1, 2])

    >>> this(b'0120121')
    ([0, 3, 6, 1, 4, 2, 5], [3, 0, 1, 2, 0, 1])
    >>> this(b'100100100')
    ([8, 7, 4, 1, 5, 2, 6, 3, 0], [1, 2, 5, 1, 4, 0, 3, 6])
    >>> this(b'100100')
    ([5, 4, 1, 2, 3, 0], [1, 2, 1, 0, 3])

    # subarray transform
    >>> this('xxxx100100yyyy', array_element_transform=int, array_slice_or_range = slice(4, -4))
    ([5, 4, 1, 2, 3, 0], [1, 2, 1, 0, 3])


refs:
    [SA][LCP][2011]Inducing the LCP-Array (Johannes Fischer).pdf
    [SA][2009]Linear Suffix Array Construction by Almost Pure Induced-Sorting (Ge Nong).pdf
    [SA][2004]Space efficient linear time construction of suffix arrays (Pang Ko).pdf

see:
    mkSubSeqTransformView_or_notView
        SeqSliceView
        SeqTransformView
        mkSubSeqTransformView
        mk_slice
'''

    array = mkSubSeqTransformView_or_notView(
                array_element_transform, array, array_slice_or_range)

    L = len(array)
    if L == 0:
        alphabet_size = 0
    elif alphabet_size is None or L < alphabet_size:
        M = max(array)
        if alphabet_size is None:
            if not 0 <= M: raise ValueError
        else:
            if not 0 <= M < alphabet_size: raise ValueError
        alphabet_size = M + 1

    if compress and L < alphabet_size:
        # compress??
        #
        #m, M = minmax_default(None, array)
        M = M
        assert M+1 == alphabet_size
        m = min(array)

        if not 0 <= m <= M: raise ValueError # not all uints
        if L + 7 < alphabet_size and L*5//3 < alphabet_size:
            # compress??
            alphabet_size, array = global_compress(array, m, M)
            assert 0 < alphabet_size <= L

    return uint_array2suffix_array(alphabet_size, array
            , LCP=LCP
            , make_RMQ=make_RMQ
            , table=table
            , handle_if_basic_case=handle_if_basic_case
            )


if __name__ == "__main__":
    import doctest
    doctest.testmod()


