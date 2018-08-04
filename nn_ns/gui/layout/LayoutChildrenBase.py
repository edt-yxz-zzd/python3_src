
from abc import abstractmethod, ABCMeta

from util import *
from LayoutBase import LayoutBase


class LayoutChildrenBase(LayoutBase):pass

class LayoutChildrenBaseImpl(LayoutChildrenBase, metaclass=ABCMeta):
    @abstractmethod
    def _calcMinsize(self, minSize, children):
        return
        return minSize
    
    @abstractmethod
    def _calcChildrenOffsetSizes(self, minSize, size, children):
        return ((offset, size),) * n

    def __updateChildrenOffsetSizes(self):
        self.offsetSizes = self._calcChildrenOffsetSizes(self.minSize, self.size, self.children)
        for child, (_offset, size) in zip(self.children, self.offsetSizes):
            child.setSize(size)
        return
    
    def __init__(self, children=(), minSize=None, size=None):
        self.children = tuple(children)
        
        minSize = self._calcMinsize(minSize, children)
        self.offsetSizes = None
        super().__init__(minSize, size)
        return

    def _update(self):
        super()._update()
        self.__updateChildrenOffsetSizes()

    def getChildren(self):
        return self.children
    def getChildrenOffsetSizes(self):
        return self.offsetSizes

