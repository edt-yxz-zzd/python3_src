
'''
Trie - prefix tree
    is a kind of search tree -- an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings.


mkTrie :: Iter ([a], v) -> Trie a v
    like _mkTrie
    but handle ([], v) directly in Trie object instead of Trie.Node object
_mkTrie :: Iter (NonEmpty[a], v) -> Trie a v
    why the key should be nonempty?
        to simplify Trie.Node datastructure
'''


class NonLeafNode:
    '''


################# version2
Node a v = {common_prefix :: 

################# version1
Node a v = Either (NonLeafNode a v) (LeafNode a v)
NonLeafNode a v = NonLeafNode
                {common_prefix :: NonEmpty[a]
                ,children :: NonEmpty(Map (Maybe a) (Node a v))
                # at least 2 children
                }
LeafNode a v = LeafNode
                {suffix :: [a]
                ,value :: v
                }

'''
    def __init__(self, may_children=None):
        self.may_common_prefix = None
        self.may_children = None
class Trie:
    def __init__(self, immutable_array_value_pairs=()):
        '''Hashable a => ([a], v) -> Trie a v
use seq as key, which should be immutable

usually, Trie Char v
'''
        ...
        for immutable_seq, value in immutable_array_value_pairs:
            self[immutable_seq] = value
        return
    def __



