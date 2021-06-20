
'''
from seed.mapping_tools.dict_op import partition_by_keyss__immutable
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

    partition_by_keyss__immutable
    iter_partition_by_keyss__immutable
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

def partition_by_keyss__immutable(dict_, keyss):
    return list(iter_partition_by_keyss__immutable(dict_, keyss))
def iter_partition_by_keyss__immutable(dict_, keyss):
    s = set()
    for keys in keyss:
        d = {}
        for key in keys:
            if key in d:
                pass
            elif key in s:
                raise KeyError(f'keyss not partition: duplicate key: {key!r}')
            else:
                d[key] = dict_[key]
                s.add(key)
        yield d
    if len(s) != len(dict_):
        diff = s^set(dict_)
        raise KeyError(f'keyss not partition of the input mapping: diff={diff!r}')
    return
