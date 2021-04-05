r'''
bucket_sort__plain - plain old bucket_sort
#'''

__all__ = '''
    bucket_sort__plain
        bucket_sort
    '''.split()

from seed.algo.bucket_sort.bucket_sort_with_table import bucket_sort_with_table__easy

def bucket_sort__plain(alphabet_size, iterable, *, key):
    'may uint -> Iter a -> (key::may (a->uint)) -> [a]'
    return bucket_sort_with_table__easy(alphabet_size, iterable, None, [], key=key)
bucket_sort = bucket_sort__plain


