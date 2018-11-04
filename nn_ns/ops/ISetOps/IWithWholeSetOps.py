
__all__ = '''
    IWithWholeSetOps
    '''.split()

from .abc import not_implemented, override
from .ISetOps import ISetOps



class IWithWholeSetOps(ISetOps):
    '''
may has no len since whole_set may be infinite large
'''
    __slots__ = ()

    @not_implemented
    @override
    def contains(ops, self, elem):
        # raise TypeError | return bool
        # when elem not in whole set, raise TypeError
        pass

