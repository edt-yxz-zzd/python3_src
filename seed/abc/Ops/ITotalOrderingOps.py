
#e ../../python3_src/seed/abc/Ops/ITotalOrderingOps.py
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
        return ops.cmp(lkey, rkey) == 0
        return ops.le(lkey, rkey) and ops.le(rkey, lkey)



    def lt(ops, lkey, rkey):
        return not ops.le(rkey, lkey)

    #def ne(ops, lkey, rkey):
    #    return not ops.eq(lkey, rkey)
    def ge(ops, lkey, rkey):
        return ops.le(rkey, lkey)
    def gt(ops, lkey, rkey):
        return ops.lt(rkey, lkey)

    #@abstractmethod
    def cmp(ops, lkey, rkey, /):
        '-> k -> k -> int/[-1,0,+1]'
        if not ops.le(lkey, rkey):
            # [lkey > rkey]
            return +1
        if not ops.le(rkey, lkey):
            # [lkey < rkey]
            return -1
        return 0

class ITotalOrderingOps__via_cmp(ITotalOrderingOps):
    __slots__ = ()
    @abstractmethod
    def cmp(ops, lkey, rkey, /):
        '-> k -> k -> int/[-1,0,+1]'
    @override
    def le(ops, lkey, rkey):
        return ops.cmp(lkey, rkey) <= 0
    @override
    def eq(ops, lkey, rkey):
        return ops.cmp(lkey, rkey) == 0

from seed.abc.Ops.ITotalOrderingOps import ITotalOrderingOps
from seed.abc.Ops.ITotalOrderingOps import ITotalOrderingOps__via_cmp
