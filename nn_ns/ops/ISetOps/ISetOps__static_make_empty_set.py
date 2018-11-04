
__all__ = '''
    ISetOps__static_make_empty_set
    '''.split()

from .abc import not_implemented, define
from .ISetOps import ISetOps

class ISetOps__static_make_empty_set(ISetOps):
    __slots__ = ()
    @define
    @not_implemented
    def static_make_empty_set(ops):
        # return the immutable empty_set
        #       or make a new immutable/mutable empty_set
        pass



