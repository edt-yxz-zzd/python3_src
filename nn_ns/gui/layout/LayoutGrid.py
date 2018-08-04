
from .LayoutChildren import LayoutChildren
from .LayoutBox import LayoutBox, C, getSize, sizeSub, sizeLessOrEqual
from functools import reduce
from itertools import accumulate, islice, groupby
from root.math.math_func import vsub, rproduct, gcd, vmap, numv_product
from .layoutGridLinearProgramming import layoutGridLinearProgramming
from sand import project
import fractions



'''
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

''

def layouts2xysizes(layouts):
    sizes = tuple(map(lambda layout: layout.getSize(), layouts))
    xsizes = tuple(x for x,y in sizes)
    ysizes = tuple(y for x,y in sizes)
    return xsizes, ysizes'''

        
    
    
class XGrid:
    def getOutSpanLengths(self):
        return self.outSpanLengths

    def __setLength(self, length):
        self.length = length
        return
    def setOutSpanLengths(self, outSpanLengths=None, indices=None):
        if indices == None:
            indices = range(self.ngrid)
        indices = list(indices)

        if outSpanLengths == None:
            outSpanLengths = (self.outSpans[i].minLength for i in indices)
        outSpanLengths = list(outSpanLengths)

        _outSpanLengths = list(self.outSpanLengths)
        for i, spanLen in zip(indices, outSpanLengths):
            _outSpanLengths[i] = spanLen
            self.outSpans[i].setLength(spanLen)
        self.outSpanLengths = tuple(_outSpanLengths)

        length = sum(self.outSpanLengths)
        self.__setLength(length)
        return
            
    def setOutSpans(self, outSpanArgs_ls):
        spans = []
        start = 0
        gridMinlengths = self.gridMinlengths
        for nspan, wme, gridWeights in outSpanArgs_ls:
            end = start + span
            minLengths = gridMinlengths[start : end]
            start = end
            
            span = Span(nspan, minLengths, wme, gridWeights)
            spans.append(span)
        
        assert self.ngrid == start
        self.outSpans = spans
        self.outSpanLengths = (None,)*ngrid
        self.setOutSpanLengths()
        return
    

    def __init__(self, ngrid=0, \
                 childGridLocationSpans_ls:\
                 '[(child, gridx, [ncolumnspan,]),]'=(), \
                 outSpanArgs_ls:\
                 '[(nspan, [weightWeight, minSizeWeight, evenWeight], [gridWeight,])]'=None,\
                 outSpanLengths = None):
        assert allUint((ngrid,))
        if outSpanArgs_ls == None:
            outSpanArgs_ls = [(ngrid, [0, 1, 0], [0,]*ngrid),]

        
        ls = tuple(childGridxSpanMinlengths_ls)
        gridWeights = tuple(gridWeights)
        assert ngrid == len(gridWeights)
        assert allUint(gridWeights)
        assert allUint(spanArgs_ls)
        

        rngLen = []
        gridx2children = 
        for child, gridx, ncolumnspans in ls:
            assert 0 <= gridx <= ngrid
            childOutSpans = child.outSpans
            assert len(ncolumnspans) == len(childOutSpans)
            childOutSpanMinlengths = [span.minLength for span in childOutSpans]
            for nspan, minLength in zip(ncolumnspans, childOutSpanMinlengths):
                end = gridx + nspan
                assert gridx <= end <= ngrid
                rng = (gridx, end)
                rngLen.append((rng, minLength))
                gridx = end
                
        gridMinlengths = calcMinlengths(ngrid, rngLen)
        minLength = sum(gridMinlengths)

        self.childGridxSpanMinlengths_ls = ls
        self.ngrid, self.gridMinlengths, self.minLength = ngrid, gridMinlengths, minLength
        self.outSpans = None
        self.outSpanLengths = None
        self.length = None
        self.setOutSpans(outSpanArgs_ls)
        return
    
        
        


def _standardizeLayoutGridArgs(gridSize, childGridLocationSpanWeight_ls):
    gridSize = getSize(gridSize)

    r = []
    for e in childGridLocationSpanWeight_ls:
        child, gridLocation, gridSpan, gridWeight = e
        gridLocation = getSize(gridLocation)
        gridSpan = getSize(gridSpan)
        gridWeight = getSize(gridWeight)
        assert sizeLessOrEqual(vadd(gridLocation+gridSpan), gridSize)

        r.append(tuple(child, minSize, gridLocation, gridSpan, gridWeight)))
    return gridSize, r


def _split_argls(gridSize, childGridLocationSpanWeight_ls):
    r = []
    for e in childGridLocationSpanWeight_ls:
        child, gridLocation, gridSpan, gridWeight = e
        minSize = child.getMinsize()
        gridLocation = getSize(gridLocation)
        gridSpan = getSize(gridSpan)
        gridWeight = getSize(gridWeight)
        assert sizeLessOrEqual(vadd(gridLocation+gridSpan), gridSize)

        r.append(tuple(zip(minSize, gridLocation, gridSpan, gridWeight)))
            
    return r
def calcMinLengths(n, minLengthLocationSpanWeights):
    ls = minLengthLocationSpanWeights
    L = len(ls)
    A = []
    b = []
    for minLength, loc, span, _ in ls:
        b.append(minLength)
        row = [0]*loc + [1]*span + [0]*(n - loc - span)
        A.append(row)
    x = layoutGridLinearProgramming(A, b)
    return x




class LayoutGrid(LayoutChildren):
    def __init__(self, gridSize=(0,0), \
                 childGridLocationSpanWeight_ls:\
                 '[(child,(gridx,gridy),(columnspan, rowspan), (weightx, weighty)),]'=(), \
                 wweight:\
                 'realWeight='\
                     '(wweight*(weight/totalWeight) + '\
                     '(1-wweight)*(minLength/totalMinLength)) '\
                     'if totalMinLength and totalWeight'\
                     'else ...'=0,\
                 outAlign=C, outFill='', outSize=None):
        r, c = gridSize = getSize(gridSize)
        ls = tuple(childGridLocationSpanWeight_ls)
        L = len(ls)
        assert L <= r * c

        gridSize, ls = _standardizeLayoutGridArgs(gridSize, ls)

        children, childMinsizes, gridXYs, gridSpans, gridWeights = \
                  project(ls, range(5), type=tuple)

        self.childMinsizeGridLocationSpanWeight_ls = ls
        self.gridSize, self.childMinsizes, self.gridXYs, self.gridSpans, self.gridWeights = \
                       gridSize, childMinsizes, gridXYs, gridSpans, gridWeights

        self.minWidths, self.minHeights = self.__calcRCMinsize(\
            gridSize, childMinsizes, gridXYs, gridSpans)
        super().__init__(children, outAlign, outFill, outSize)
        

    def _calcMinsize(self, children):
        column_xsizes, row_ysizes = self.__getRCMinsize()
        x = sum(column_xsizes, 0)
        y = sum(row_ysizes, 0)
        minSize = (x, y)
        return minSize
    def __getRCMinsize(self):
        return self.column_xsizes, self.row_ysizes
    
    def __calcRCMinsize(self, gridSize, ls):
        minWidths, minHeights = \
                   (calcMinLengths(minsizeGridLocationSpanWeights) \
                    for minsizeGridLocationSpanWeights in _split_argls(gridSize, ls))
                      
        return minWidths, minHeights


    
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
    
    
