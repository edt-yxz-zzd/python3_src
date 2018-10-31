
'''

'''

__all__ = '''
    discard_keys__inplace
    remove_keys__inplace
    subtract_keys__inplace

    subtract_keys__immutable
    add_dict__immutable
    subset_keys__immutable
    intersect_keys__immutable
    sum_dicts__immutable
    '''.split()


#from functools import reduce


def discard_keys__inplace(dict_, keys):
    for key in keys:
        dict_.pop(key, None) # nothrow
def remove_keys__inplace(dict_, keys):
    for key in keys:
        dict_.pop(key) # raise
def subtract_keys__inplace(dict_, keys):
    discard_keys__inplace(dict_, keys)



#################################

def subtract_keys__immutable(dict_, keys):
    keys = frozenset(dict_) - frozenset(keys)
    return subset_keys__immutable(dict_, keys)


def add_dict__immutable(lhs, rhs):
    d = dict(lhs)
    d.update(rhs)
    return d

def subset_keys__immutable(dict_, keys):
    'assert set(keys) <= set(dict_)'
    return {k:dict_[k] for k in frozenset(keys)}
def intersect_keys__immutable(dict_, keys):
    keys = frozenset(dict_) & frozenset(keys)
    return subset_keys__immutable(dict_, keys)

def sum_dicts__immutable(dicts):
    # bug: since update()->None not a dict
    return reduce(dict.update, dicts, {})


def sum_dicts__immutable(dicts):
    d = {}
    for x in dicts:
        d.update(x)
    return d


