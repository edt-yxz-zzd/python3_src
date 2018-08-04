
from functools import reduce
from itertools import accumulate, product, islice
from abc import abstractmethod, ABCMeta
import operator
from sand import Walk
from root.math.math_func import vadd

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
    r = tuple(map(operator.sub, lhs, rhs))
    return r

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



def scaleOneSize(minlength, total_minlength, total_outlength):
    assert 0 <= minlength <= total_minlength <= total_outlength
    if total_minlength == 0:
        return 0
    return total_outlength*minlength//total_minlength

def scaleOneSizesOffsets(minlengths, total_minlength, total_outlength):
    ls = [0]
    for minlength in minlengths:
        s = scaleOneSize(minlength, total_minlength, total_outlength)
        ls.append(s)
    offsets = list(accumulate(ls))
    endpad = total_outlength - offsets[-1]
    assert endpad >= 0

    ls[-1] += endpad
    sizes = ls[1:]
    offsets = offsets[:-1]
    assert len(sizes) == len(offsets)
    return sizes, offsets


def rproduct(*iterable):
    f = lambda t: tuple(reversed(t))
    return map(f, product(*reversed(iterable)))


def layouts2xysizes(layouts):
    sizes = tuple(map(lambda layout: layout.getSize(), layouts))
    xsizes = tuple(x for x,y in sizes)
    ysizes = tuple(y for x,y in sizes)
    return xsizes, ysizes

class LayoutGrid(LayoutChildren):
    def __init__(self, gridSize=(0,0), children=(), outAlign=C, outFill='', outSize=None):
        r, c = gridSize = getSize(gridSize)
        children = list(children)
        assert len(children) <= r * c
        
        self.gridSize = gridSize
        self.column_xsizes, self.row_ysizes = self.__calcRCMinsize(children)
        super().__init__(children, outAlign, outFill, outSize)
        

    def _calcMinsize(self, children):
        column_xsizes, row_ysizes = self.__getRCMinsize()
        x = sum(column_xsizes, 0)
        y = sum(row_ysizes, 0)
        minSize = (x, y)
        return minSize
    def __getRCMinsize(self):
        return self.column_xsizes, self.row_ysizes
    
    def __calcRCMinsize(self, children):
        xsizes, ysizes = layouts2xysizes(children)

        rowSize, columnSize = self.gridSize
        L = len(children)
        row_ysizes = tuple(
            reduce(max, ysizes[r*columnSize : (r+1)*columnSize], 0)
            for r in range(rowSize))
        column_xsizes = tuple(
            reduce(max, xsizes[c : L : columnSize], 0)
            for c in range(columnSize))
                      
        return column_xsizes, row_ysizes


    
    def _calcChildrenOffsetOutsizes(self, minSize, outSize, children):
        px, py = outSize
        pxm, pym = minSize
        column_xsizes, row_ysizes = self.__getRCMinsize()
        xsizes, xoffsets = scaleOneSizesOffsets(column_xsizes, pxm, px)
        ysizes, yoffsets = scaleOneSizesOffsets(row_ysizes, pym, py)

        L = len(children)
        assert L <= len(xsizes)*len(ysizes)
        outSizes = islice(rproduct(xsizes, ysizes), L)
        offsets = islice(rproduct(xoffsets, yoffsets), L)
        
        r = tuple(zip(offsets, outSizes))
        assert len(r) == L

        return r
    
    








class LayoutHBox(LayoutGrid):
    def __init__(self, children=(), outAlign=C, outFill='', outSize=None):
        children = tuple(children)
        gridSize = (1, len(children))
        super().__init__(gridSize, children, outAlign, outFill, outSize)
        

    
class LayoutVBox(LayoutGrid):
    def __init__(self, children=(), outAlign=C, outFill='', outSize=None):
        children = tuple(children)
        gridSize = (len(children), 1)
        super().__init__(gridSize, children, outAlign, outFill, outSize)
        



class Layout工(LayoutChildren):
    @staticmethod
    def _calcMinsize(children):
        assert len(children) == 5
        top, left, center, right, bottom = children
        hcenter = LayoutHBox([left, center, right])
        minLayout = LayoutVBox([top, hcenter, bottom])
        return minLayout.getMinsize()
    @staticmethod
    def _calcChildrenOffsetOutsizes(minSize, outSize, children):
        px, py = outSize
        top, left, center, right, bottom = children

        top_xsize = bottom_xsize = px
        _, top_ysize = top.getMinsize()
        _, bottom_ysize = bottom.getMinsize()
        
        left_ysize = center_ysize = right_ysize = py - top_ysize - bottom_ysize
        left_xsize, _ = left.getMinsize()
        right_xsize, _ = right.getMinsize()
        center_xsize = px - left_xsize - right_xsize

        top_offset = (0, 0)
        left_offset = (0, top_ysize)
        center_offset = (left_xsize, top_ysize)
        right_offset = (px - right_xsize, top_ysize)
        bottom_offset = (0, py - bottom_ysize)

        ls = []
        for name in 'top, left, center, right, bottom'.split(', '):
            name_xsize = eval('{}_xsize'.format(name))
            name_ysize = eval('{}_ysize'.format(name))
            name_size = name_xsize, name_ysize
            name_offset = eval('{}_offset'.format(name))
            ls.append((name_offset, name_size))

        return ls
            
        



class Layout井(LayoutChildren):
    @staticmethod
    def _calcMinsize(children):
        assert len(children) == 9
        minLayout = LayoutGrid((3,3), children)
        return minLayout.getMinsize()
    @staticmethod
    def _calcChildrenOffsetOutsizes(minSize, outSize, children):
        px, py = outSize
        minLayout = LayoutGrid((3,3), children)
        assert minLayout.getMinsize() == minSize
        
        minOffsetOutsizes = minLayout.offsetOutSizes
        _, outSizeNW = minOffsetOutsizes[0]
        _, outSizeSE = minOffsetOutsizes[8]
        center_size = sizeSub(outSize, outSizeNW)
        center_size = sizeSub(center_size, outSizeSE)

        children = list(children)
        children[4] = LayoutBox(center_size)
        maxLayout = LayoutGrid((3,3), children)
        assert maxLayout.getMinsize() == outSize

        
        maxOffsetOutsizes = maxLayout.offsetOutSizes
        return maxOffsetOutsizes

            
class LayoutUnion(LayoutChildren):
    # more last child, more front
    @staticmethod
    def _calcMinsize(children):
        if not children:
            return (0,0)
        xsizes, ysizes = layouts2xysizes(children)
        x = max(xsizes)
        y = max(ysizes)
        return x, y
    @staticmethod
    def _calcChildrenOffsetOutsizes(minSize, outSize, children):
        item = ((0,0), outSize)
        return (item,) * len(children)















def testLayout(constructor, args_outsize_ls):
    data = args_outsize_ls
    ls = []
    for args, outSize in data:
        layout = constructor(*args)
        assert layout.getOutsize() == outSize
        ls.append(layout)
        
    return ls

class __Data:
    dataLayoutGrid = [
        ([(3, 2), [LayoutBox(minSize=(i,i)) for i in range(3)]], (3, 3)),
        ([(2, 3), [LayoutBox(minSize=(i,i)) for i in range(3)]], (3, 2)),
        ([(0,0), []], (0, 0)),
        ]

    dataLayoutHBox = [
        ([[LayoutBox(minSize=(i,i)) for i in range(10)]], (45, 9)),
        ([[]], (0, 0)),
        ]

    dataLayoutVBox = [
        ([[LayoutBox(minSize=(i,i)) for i in range(10)]], (9, 45)),
        ([[]], (0, 0)),
        ]

    dataLayout工 = [
        ([[LayoutBox(minSize=(i,i)) for i in range(5)]], (6, 7)),
        ]

    dataLayout井 = [
        ([[LayoutBox(minSize=(i,i)) for i in range(9)]], (21, 15)),
        ]

    dataLayoutUnion = [
        ([[LayoutBox(minSize=(i,i)) for i in range(7)]], (6, 6)),
        ]


def test():
    dataLayoutClassNames = (key for key in dir(__Data) if key.startswith('dataLayout'))
        

    layouts = []
    for dataLayoutClassName in dataLayoutClassNames:
        className = dataLayoutClassName[4:]
        layoutClass = eval(className)
        
        data = getattr(__Data, dataLayoutClassName)
        r = testLayout(layoutClass, data)
        layouts.extend(r)

    v = LayoutVBox(layouts)
    return v


class DrawLayoutPath2Children:
    def __init__(self):pass
    def __call__(self, path):
        layout, childOffset = node = path[-1]
        if isinstance(layout, LayoutChildren):
            for child, (childOffset, _) in \
                zip(layout.getChildren(), \
                    layout.getChildrenOffsetOutsizes()):
                yield child, childOffset
                
        return None
    
        
def drawLayout(layout, background = ' '):
    L = len(background)
    c, r = outSize = layout.getOutsize()
    txt = [[0]*c for i in range(r)]

    def draw(txt, location, size):
        x0, y0 = location
        w, h = size
        for x in range(x0, x0+w):
            for y in range(y0, y0+h):
                try:
                    txt[y][x] += 1
                except:
                    print('r, c', r, c)
                    print('location, size', location, size)
                    print('x, y', x, y)
                    raise
                
    def to_txt(txt):
        ls = []
        for row in txt:
            for i in range(len(row)):
                if not row[i]:
                    row[i] = background
                else:
                    tpl = '{:*^' + str(L) +'}'
                    fg = tpl.format(row[i])
                    assert len(fg) == L # row[i] to big will cause error
                    row[i] = ''.join((b if f == '*' else f) for f, b in zip(fg, background))
            ls.append(''.join(row))
        
        return '\n'.join(ls)
    
                    

    root = layout, (0,0)
    location_stack = [(0,0)]
    for action, path, node in Walk(root, DrawLayoutPath2Children()):
        if action == Walk.ENTER:
            assert len(location_stack) == len(path)
            child, childOffset = node
            offset = child.getOffset()
            parent_location = location_stack[-1]
            location = vadd(parent_location, childOffset, offset)
            location_stack.append(location)
            size = child.getSize()
            
            draw(txt, location, size)
        elif action == Walk.EXIT:
            location_stack.pop()
            assert len(location_stack) == len(path)
            
    txt = to_txt(txt)
    return txt



            
        
        


if __name__ == '__main__':
    v = test()
    drawLayout(v)



        



