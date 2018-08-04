
from .LayoutBox import LayoutBox, C
from abc import abstractmethod, ABCMeta


class LayoutChildren(LayoutBox, metaclass=ABCMeta):
    @abstractmethod
    def _calcMinsize(self, children):
        return
        return minSize
    
    @abstractmethod
    def _calcChildrenOffsetOutsizes(self, minSize, outSize, children):
        return ((offset, outSize),) * n

    def __updateChildrenOffsetOutsizes(self):
        self.offsetOutSizes = self._calcChildrenOffsetOutsizes(self.minSize, self.outSize, self.children)
        for child, (_offset, outSize) in zip(self.children, self.offsetOutSizes):
            child.setOutsize(outSize)
        return
    
    def __setChildrenParent(self):
        for child in self.children:
            child.setParent(self)
        return
    def __init__(self, children=(), outAlign=C, outFill='', outSize=None):
        self.children = tuple(children)
        #self.__setChildrenParent()
        
        minSize = self._calcMinsize(children)
        self.offsetOutSizes = None
        super().__init__(minSize, outAlign, outFill, outSize)
        return

    def _update(self):
        super()._update()
        self.__updateChildrenOffsetOutsizes()

    def getChildren(self):
        return self.children
    def getChildrenOffsetOutsizes(self):
        return self.offsetOutSizes

