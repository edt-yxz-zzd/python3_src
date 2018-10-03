from abc import ABC, abstractmethod
from collections import namedtuple
class ITrieNode(ABC):
    __slots__ = ()
    @abstractmethod
    def is_leaf(self):
        raise NotImplementedError
try:
    ITrieNode()
except TypeError:
    #TypeError: Can't instantiate abstract class ITrieNode with abstract methods is_leaf
    pass
else:
    raise Exception

TrieLeafNodeBase = namedtuple('TrieLeafNodeBase', 'suffix value'.split())
class TrieLeafNode(TrieLeafNodeBase, ITrieNode):
    def __new__(cls, suffix, value):
        len(suffix)
        self = super().__new__(cls, suffix, value)
        return self
assert TrieLeafNode.__abstractmethods__ == {'is_leaf'}
node = TrieLeafNode('', 0) # ??????????no TypeError??????????
assert node.suffix == ''
assert node.value == 0
try:
    node.is_leaf()
except NotImplementedError:
    pass
else:
    raise Exception



