
from util import *

class LayoutBase:
    def __init__(self, minSize=(0,0), size=None):
        minSize = getSize(minSize)
        self.minSize = minSize
        self.size = None
        self.setSize(size) # may not call _update

        self._update() # for subclass
        return

    
    def setSize(self, size):
        if size == None:
            size = self.minSize
        else:
            size = getSize(size)
            
        if size == self.size:
            return
        
        self.__setSize(size)
        self._update()
        return
    
    def __setSize(self, size):
        assert sizeLessOrEqual(self.minSize, size)
        self.size = size
        return
    
    def _update(self):
        return
    
    def getMinsize(self):
        return self.minSize
    def getSize(self):
        return self.size



NullLayout = LayoutBase()
PointLayout = LayoutBase((1,1))
