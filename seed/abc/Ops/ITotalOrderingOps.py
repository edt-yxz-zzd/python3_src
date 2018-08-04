
__all__ = '''
    ITotalOrderingOps
    '''.split()

from .abc import not_implemented, abstractmethod, override
#from ..TreeNodeOps.ITreeNodeRelated import ITreeNodeRelated
from .IEqOps import IEqOps



class ITotalOrderingOps(IEqOps):
    __slots__ = ()

    @not_implemented
    def le(ops, lkey, rkey):
        return lkey <= rkey

    @abstractmethod
    @override
    def eq(ops, lkey, rkey):
        return ops.le(lkey, rkey) and ops.le(lkey, rkey)



    def lt(ops, lkey, rkey):
        return not ops.le(rkey, lkey)
        return ops.le(lkey, rkey) and not ops.le(lkey, rkey)

    #def ne(ops, lkey, rkey):
    #    return not ops.eq(lkey, rkey)
    def ge(ops, lkey, rkey):
        return ops.le(rkey, lkey)
    def gt(ops, lkey, rkey):
        return ops.lt(rkey, lkey)

