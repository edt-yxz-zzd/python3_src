
from util import *
from LayoutChildrenBase import LayoutChildrenBase
from sand import project
from WeightLengthsChildren import WeightLengthsChildren, WeightLengthsChild


def standardizeChildGridXYWH_ls(childGridXYWH_ls):
    g = ((child, getSize(gridxy), getSize(gridwh))
         for child, gridxy, gridwh in childGridXYWH_ls)

    return tuple(g)

class WeightLengthsChildLayoutX(WeightLengthsChild):
    def __init__(self, layout):
        x, y = layout.getMinsize()
        super().__init__(x)

        self.layout = layout
        return
    def _setLength(self, length):
        super()._setLength(length)
        x, y = layout.getSize()
        layout.setSize((length, y))
        return
class WeightLengthsChildLayoutY(WeightLengthsChild):
    def __init__(self, layout):
        x, y = layout.getMinsize()
        super().__init__(y)

        self.layout = layout
        return
    def _setLength(self, length):
        super()._setLength(length)
        x, y = self.layout.getSize()
        layout.setSize((x, length))
        return
    
        
class LayoutWeightGrid(LayoutChildrenBase):
    def __init__(self, gridSize, childGridXYWH_ls, WeightLengthsChildrenXYArgs):
        gridSize = getSize(gridSize)
        childGridXYWH_ls = standardizeChildGridXYWH_ls(childGridXYWH_ls)
        children, gridxys, gridwhs = project(childGridXYWH_ls, range(3))

        WeightLengthsChildren()
        ls = [[], []]
        for child, gridxy, gridwh in childGridXYWH_ls:
            for WLength, gridLoc, ngrid, als in \
                zip([WeightLengthsChildLayoutX, WeightLengthsChildLayoutY],
                    gridxy, gridwh, ls):
                als.append((WLength(child), gridLoc, ngrid))

        minSize = [0,0]
        size = [0,0]
        for i, args, childls in zip(range(2), args, ls):
            wlc = WeightLengthsChildren(childls, *args)
            ls[i] = wlc
            minSize[i] = wlc.minLength
            size[i] = wlc.length

        xyWeightLengthsChildren = tuple(ls)
        minSize = getSize(minSize)
        size = getSize(size)

        self.

        
        return
