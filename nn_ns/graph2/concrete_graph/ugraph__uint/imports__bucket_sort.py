

#imports__bucket_sort

__all__ = '''
    bucket_sort
    radix_sort
    bucket_sort4uint_seq
    '''.split()

from nn_ns.graph2.bucket_sort.UIntSeqSort import UIntSeqSort
from seed.algo.bucket_sort.bucket_sort_with_table import bucket_sort_with_table__easy
from seed.algo.bucket_sort.radix_sort_with_table import radix_sort_with_table

def radix_sort(alphabet_sizes, iterable, *, key):
    alphabet_sizes = tuple(alphabet_sizes)
    L = max(alphabet_sizes, default=0)
    table = tuple([] for _ in range(L))
    return radix_sort_with_table(alphabet_sizes, iterable, table, key=key)
def bucket_sort(alphabet_size, iterable, *, key):
    return bucket_sort_with_table__easy(alphabet_size, iterable, None, [], key=key)

def bucket_sort4uint_seq(upper_bound, iterable, *, key):
    return UIntSeqSort(upper_bound, key=key).sort__uintss(iterable)


