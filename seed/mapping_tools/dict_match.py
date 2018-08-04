

__all__ = '''
    dict_match
'''.split()

from operator import __eq__
def dict_match(a, b, *, common_keys = None, value_eq = __eq__):
    if value_eq is None: value_eq = __eq__

    keys = set(a) & set(b) if common_keys is None else common_keys
    # __getitem__ instead of get
    return all(value_eq(a[key], b[key]) for key in keys)
    keys = list(keys)
    u = map(a.__getitem__, keys)
    v = map(b.__getitem__, keys)
    return all(map(value_eq, u, v))
