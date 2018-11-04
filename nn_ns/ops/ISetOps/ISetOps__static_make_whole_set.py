
__all__ = '''
    ISetOps__static_make_whole_set
    '''.split()

from .abc import not_implemented, define
from .IWithWholeSetOps import IWithWholeSetOps

class ISetOps__static_make_whole_set(IWithWholeSetOps):
    __slots__ = ()

    @define
    @not_implemented
    def static_make_whole_set(ops):
        # return the immutable whole_set
        #       or make a new immutable/mutable whole_set
        pass



