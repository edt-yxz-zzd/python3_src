
#from .to_container import to_container


def project_key(iterable, key):
    '''item:tail -> item[key] : project_key tail

example:
    >>> list(project_key(([1,2], [3,5]), 1))
    [2, 5]
'''
    return (ls[key] for ls in iterable)

def element_project_keys(elem, keys):
    return (elem[key] for key in keys)
def project_keys(iterable, keys):
    '''deep_map_funcs([list, list], project_keys([(0, 1), (2, 3), (4, 5)], [1,0])) == [[1,0], [3,2], [5,4]]'''
    keys = tuple(keys)
    return (element_project_keys(ls, keys) for ls in iterable)

assert list(project_key(([1,2], [3,5]), 1)) == [2,5]
assert list(element_project_keys(list(range(5)), [2,3])) == [2,3]
assert list(map(list, project_keys([(0, 1), (2, 3), (4, 5)], [1,0]))) == [[1,0], [3,2], [5,4]]


            


if 0:
    def project(key2value_iterable, keys, type=list):
        '''
    project_iterable_keys(iterable, keys)

    example:
        >>> list(map(list, project(([1,2], [3,4], [5,6]), keys=[1,0])))
        [[2, 4, 6], [1, 3, 5]]
    '''

        key2value_ls = tuple(key2value_iterable)
        
        for key in keys:
            yield type(d[key] for d in key2value_ls)


if __name__ == "__main__":
    import doctest
    doctest.testmod()




