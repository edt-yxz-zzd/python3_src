
__all__ = '''
    get_may_longest_prefix_idx_in_sorted_prefixes
    get_may_longest_prefix_in_sorted_prefixes
    contains_any_prefix_in_sorted_prefixes
    '''.split()

from bisect import bisect_right
import warnings

warnings.warn('get_may_longest_prefix_idx_in_sorted_prefixes is inefficient, use nn_ns.Trie instead')
def __ver1__get_may_longest_prefix_idx_in_sorted_prefixes(s, sorted_prefixes):
    insert_point = bisect_right(sorted_prefixes, s)
    if insert_point and s.startswith(sorted_prefixes[insert_point-1]):
        return insert_point-1
    return None
assert __ver1__get_may_longest_prefix_idx_in_sorted_prefixes('2', ['', '1']) is None



def get_may_longest_prefix_idx_in_sorted_prefixes(s, sorted_prefixes):
    '''String -> sorted[String] -> (None|UInt)

inefficient
O(N)
consider to use Trie

example:
    >>> this = get_may_longest_prefix_idx_in_sorted_prefixes
    >>> sorted_prefixes = ["1", "2", "23", "234", "5"]
    >>> this("", sorted_prefixes) is None
    True
    >>> this("3", sorted_prefixes) is None
    True
    >>> this("6", sorted_prefixes) is None
    True
    >>> this("1", sorted_prefixes)
    0
    >>> this("2", sorted_prefixes)
    1
    >>> this("22", sorted_prefixes)
    1
    >>> this("23", sorted_prefixes)
    2
    >>> this("24", sorted_prefixes)
    1
    >>> this('2', ['', '1'])
    0

bug of version1:
    def get_may_longest_prefix_idx_in_sorted_prefixes(s, sorted_prefixes):
        insert_point = bisect_right(sorted_prefixes, s)
        if insert_point and s.startswith(sorted_prefixes[insert_point-1]):
            return insert_point-1
        return None
    fail at:
        get_may_longest_prefix_idx_in_sorted_prefixes('2', ['', '1'])

'''
    #raise NotImplementedError
    insert_point = bisect_right(sorted_prefixes, s)
    while insert_point:
        # assert sorted_prefixes

        insert_point -= 1
        prefix = sorted_prefixes[insert_point]
        if s.startswith(prefix):
            return insert_point

        # assert s
        if s[0] != prefix[0]:
            if not sorted_prefixes[0]:
                return 0
            break
    return None

def contains_any_prefix_in_sorted_prefixes(s, sorted_prefixes):
    may_idx = get_may_longest_prefix_idx_in_sorted_prefixes(
                s, sorted_prefixes)
    return may_idx is not None
def get_may_longest_prefix_in_sorted_prefixes(s, sorted_prefixes):
    may_idx = get_may_longest_prefix_idx_in_sorted_prefixes(
                s, sorted_prefixes)
    if may_idx is not None:
        idx = may_idx
        return sorted_prefixes[idx]
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()


