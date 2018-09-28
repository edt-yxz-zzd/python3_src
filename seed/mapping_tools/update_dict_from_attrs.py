
__all__ = '''
    update_dict_from_attrs
    '''.split()

def update_dict_from_attrs(mapping, obj, attrs, *, getattr=getattr):
    '''Map k v -> obj -> Iter k -> (getattr=obj->k->v) -> Map k v

example:
    >>> this = update_dict_from_attrs

    >>> from fractions import Fraction
    >>> obj = Fraction(3, 5)
    >>> attrs = 'numerator denominator'.split()
    >>> result = dict(numerator=3, denominator=5)
    >>> this({}, obj, attrs) == result
    True

    >>> d = dict(numerator=0, denominator=0, xxxx=0)
    >>> d2 = d.copy()
    >>> d2.update(result)
    >>> d2 != d
    True
    >>> this(d, obj, attrs) is d == d2
    True

    >>> this({}, d, d.keys(), getattr=dict.__getitem__) == d2
    True
'''
    for attr in attrs:
        mapping[attr] = getattr(obj, attr)

    return mapping

if __name__ == "__main__":
    import doctest
    doctest.testmod()



