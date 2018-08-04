

'''
SuffixTreeData
    = (whole_isuffix,)
    | (begin_isuffix, size, children::[SuffixTreeData])

    0) len(children) >= 2
    1) size == 0 ==>> the node is root
        but root may be a leaf
    2) size is as max as possible
        at most one of children is empty
        nonempty children cannot have same head char
    3) whole_suffix
        = array[whole_isuffix:]
        | ancestor_prefix... + array[begin_isuffix:begin_isuffix+size] + ...
'''

__all__ = '''
    make_suffix_tree_data
    make_suffix_tree_data_from_uint_array
    '''.split()

from .suffix_tree.SuffixTree import SuffixTree
def make_suffix_tree_data(SA, LCP):
    '''
example:
    >>> make_suffix_tree_data([6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4], [6, 1, 5, 0, 4, 1, 3, 0, 1, 1, 2])
    (0, 0, [(12,), (6, 1, [(7, 5, [(6,), (0,)]), (8, 4, [(7,), (1,)])]), (8, 1, [(9, 3, [(8,), (2,)]), (10, 2, [(9,), (3,)])]), (11, 1, [(11,), (5,), (11, 1, [(10,), (4,)])])])
'''
    return SuffixTree(SA, LCP).to_data()
def make_suffix_tree_data_from_uint_array(array):
    '''
example:
    >>> make_suffix_tree_data_from_uint_array(b'112233112233')
    (0, 0, [(12,), (6, 1, [(7, 5, [(6,), (0,)]), (8, 4, [(7,), (1,)])]), (8, 1, [(9, 3, [(8,), (2,)]), (10, 2, [(9,), (3,)])]), (11, 1, [(11,), (5,), (11, 1, [(10,), (4,)])])])
'''
    return SuffixTree.from_uint_array(array).to_data()

if __name__ == "__main__":
    import doctest
    doctest.testmod()



