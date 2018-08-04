
'''
time O(n)

see: canonical_Cartesian_tree_definition.py :: "Right Open"
see: ballot_number.py :: "encode canonical_Cartesian_tree" :: [(append|pop)]

array2CanonicalCartesianRightOpenTreeRootRights_append_pop_ls

'''

__all__ = '''
    canonical_Cartesian_tree_of_array_to_balanced_Dyck_word
    array2CanonicalCartesianRightOpenTreeRootRights_append_pop_ls
    '''.split()

def canonical_Cartesian_tree_of_array_to_balanced_Dyck_word(iterable):
    '''canonical_Cartesian_tree_of_array  TO  balanced_Dyck_word
    :: Ord a => Iter a -> Iter bool

see: array2CanonicalCartesianRightOpenTreeRootRights_append_pop_ls
'''
    return array2CanonicalCartesianRightOpenTreeRootRights_append_pop_ls(iterable)
def array2CanonicalCartesianRightOpenTreeRootRights_append_pop_ls(iterable):
    ''':: Ord a => Iter a -> Iter bool


time O(n)
time O(len input)


:: Ord a => [a] -> [(append|pop)]
    append is True is open
    pop is False is close

output:
    balanced_Dyck_word :: [bool]
        len output == 2 * len input
        output is balanced, i.e. num_appends == num_pops
        output is balanced_Dyck_word

used to encode canonical_Cartesian_tree of array

see: ballot_number.py :: "encode canonical_Cartesian_tree" :: [(append|pop)]
see: canonical_Cartesian_tree_definition.py :: "Right Open"
    see:
        FreeCanonicalCartesianRightOpenReverseTree.py
        or: CanonicalCartesianRightOpenTree.py
        for how right_open_trees are constructed

example:
    >>> this = canonical_Cartesian_tree_of_array_to_balanced_Dyck_word
    >>> f = lambda iterable: list(this(iterable))
    >>> f([])
    []
    >>> f([1])
    [True, False]
    >>> f([1,2])
    [True, True, False, False]
    >>> f([1,1])
    [True, True, False, False]
    >>> f([1,0])
    [True, False, True, False]
    >>> f([2,1,0])
    [True, False, True, False, True, False]
    >>> f([1,2,0])
    [True, True, False, False, True, False]
'''

    POP = False
    APPEND = True

    stack = root_temp_right_descendants = []
    for x in iterable:
        while stack and x < stack[-1]:
            yield POP; stack.pop()
        yield APPEND; stack.append(x)
    while stack:
        yield POP; stack.pop()



canonical_Cartesian_tree_of_array_to_balanced_Dyck_word.__doc__ +=\
    array2CanonicalCartesianRightOpenTreeRootRights_append_pop_ls.__doc__




if __name__ == "__main__":
    import doctest
    doctest.testmod()



