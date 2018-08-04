
from .LayoutChildren import LayoutChildren
from .LayoutBox import LayoutBox, C, getSize, sizeSub
from functools import reduce
from itertools import accumulate, islice
from root.math.math_func import vsub, rproduct

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





