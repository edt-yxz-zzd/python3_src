
'''
pprint depth 1

example:
    >>> pprint1({2:1, 1:(1,2)})
    {1
    : (1, 2)
    ,2
    : 1
    }


'''

__all__ = '''
    pprint1
    '''.split()

from seed.helper.stable_repr import stable_repr_print
import sys

def pprint1(obj, *, file=None):
    ofile = sys.stdout if file is None else file
    del file
    stable_repr_print(ofile, obj
        , indent='', depth=0, maybe_max_depth=1
        , has_head_eol_when_indent=False
        )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


