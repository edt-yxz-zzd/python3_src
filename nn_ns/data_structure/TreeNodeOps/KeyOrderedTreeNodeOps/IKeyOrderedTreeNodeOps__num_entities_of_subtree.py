
__all__ = '''
    IKeyOrderedTreeNodeOps__num_entities_of_subtree
    '''.split()

from .abc import not_implemented, override, abstractmethod
from .IKeyOrderedTreeNodeOps import IKeyOrderedTreeNodeOps
from ..UnbalancedMultiWayTreeNodeOps.IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree import \
    IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree

class IKeyOrderedTreeNodeOps__num_entities_of_subtree(
        IKeyOrderedTreeNodeOps
        , IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree
        ):
    '''
IUnbalancedMultiWayTreeNodeOps__num_entities_of_subtree's methods:
    `get_num_entities_of_subtree
    `index_nonleaf_entity_position_ex_at

    index_entity_at

new_methods:
    index_key_at
'''
    __slots__ = ()

    def index_key_at(ops, self, idx):
        entity = ops.index_entity_at(self, idx)
        return ops.entity2key(entity)



if __name__ == '__main__':
    XXX = IKeyOrderedTreeNodeOps__num_entities_of_subtree

    from seed.helper.print_methods import print_methods
    print_methods(XXX)




