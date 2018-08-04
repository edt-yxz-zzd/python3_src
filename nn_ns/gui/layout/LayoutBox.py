
from root.math.math_func import vsub
import operator

ALIGN = 'NW N NE W C E SW S SE'
FILL = 'X Y XY L' # and ''. 'L' means 'lock width/height'

ALIGN_STRS = ALIGN.split()
FILL_STRS = [''] + FILL.split()

CONSTSTR = '{} {}'.format(ALIGN, FILL)
CONSTSTRS = CONSTSTR.split()
for _CONST in CONSTSTRS:
    exec('{0} = {0!r}'.format(_CONST))




def getSize(size):
    size = tuple(size)
    assert len(size) == 2
    for i in size:
        assert isinstance(i, int)
        assert i >= 0
    return size

def getAlign(align):
    assert align in ALIGN_STRS
    return align
def getFill(fill):
    if fill not in FILL_STRS:
        print('{!r} {}'.format(fill, FILL_STRS))
    
    assert fill in FILL_STRS
    return fill

def sizeSub(lhs, rhs):
    assert sizeLessOrEqual(rhs, lhs)
    r = vsub(lhs, rhs)
    return getSize(r)

def sizeLessOrEqual(lhs, rhs):
    r = all(map(operator.le, lhs, rhs))
    return r
class LayoutBox:
    def __init__(self, minSize=(0,0), outAlign=C, outFill='', outSize=None):
        outAlign = getAlign(outAlign)
        outFill = getFill(outFill)
        minSize = getSize(minSize)
        
        self.minSize = minSize
        self.outAlign = outAlign
        self.outFill = outFill
        
        self.size = None
        self.offset = None
        self.outSize = None
        self.setOutsize(outSize) # may not call _update

        self._update() # for subclass
        return

    
    def setOutsize(self, outSize):
        if outSize == None:
            outSize = self.minSize
        else:
            outSize = getSize(outSize)
            
        if outSize == self.outSize:
            return
        
        self.__setOutsize(outSize)
        self._update()
        return
    
    def __setOutsize(self, outSize):
        assert sizeLessOrEqual(self.minSize, outSize)
        self.outSize = outSize
        return
    
    def _update(self):
        self.size = self.__calcSize()
        self.offset = self.__calcOffset()
        return
    
    def getMinsize(self):
        return self.minSize
    def getOutsize(self):
        return self.outSize
    def getSize(self):
        return self.size
    def __calcSize(self):
        if not self.outSize:
            return self.minSize
        f = lambda fill, length, outlength: outlength if fill in self.outFill else length
        size = map(f, (X, Y), self.getMinsize(), self.getOutsize())
        return getSize(size)
    
    def getChildern(self):
        return ()

    def getoutAlignXY(self):
        align = self.outAlign
        i = ALIGN_STRS.index(align)
        r, c = divmod(i, 3)
        x = r - 1
        y = c - 1
        return x, y
    
    @staticmethod
    def __calcOneOffset(align, length, outlength):
        pad = outlength - length
        offsets = [0, pad//2, pad]
        return offsets[align+1]
    def getOffset(self):
        return self.offset
    def __calcOffset(self):
        align = self.getoutAlignXY()
        size = self.getSize()
        outSize = self.getOutsize()
        offset = map(self.__calcOneOffset, align, size, outSize)
        return getSize(offset)






NullLayout = LayoutBox()
PointLayout = LayoutBox((1,1))

