
__all__ = '''
    INegableSetOps
    ISizedNegableSetOps
    '''.split()

from .abc import not_implemented, define
from .IWithWholeSetOps import IWithWholeSetOps
from .ISetOps__is_empty import ISetOps__is_empty

class INegableSetOps(IWithWholeSetOps):
    '''
two cases:
    * {a, b, c}
    * whole_set \-/ {a, b, c}

may has no len since whole_set may be infinite large
'''
    __slots__ = ()

    @define
    @not_implemented
    def inegative(ops, self):
        # "i" in "inegable" like __iadd__ in tupel or list
        #   may modify and return self
        #   or not modify self and return new one
        pass

class ISizedNegableSetOps(ISetOps__is_empty, INegableSetOps):
    '''
positive or negative size
    * +size
    * -size-1
'''
    __slots__ = ()
    @define
    @not_implemented
    def negable_size_of(ops, self):
        '-> Integer; +size | -size-1'
        pass


