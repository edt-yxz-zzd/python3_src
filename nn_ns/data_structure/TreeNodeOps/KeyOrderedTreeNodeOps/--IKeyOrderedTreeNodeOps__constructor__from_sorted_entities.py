
__all__ = '''
    IKeyOrderedTreeNodeOps__constructor__from_sorted_entities
    '''.split()

from .abc import not_implemented, override, abstractmethod
from .IKeyOrderedTreeNodeOps import IKeyOrderedTreeNodeOps

class IKeyOrderedTreeNodeOps__constructor__from_sorted_entities(
        IKeyOrderedTreeNodeOps):
    __slots__ = ()

    @not_implemented
    def from_sorted_entities(ops, entities, reverse=False, strict=False):
        # [reverse==True][strict==False] ==>> entities[i] >= entities[i+1]
        # [reverse==False][strict==True] ==>> entities[i] < entities[i+1]
        ...


