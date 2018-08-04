from itertools import accumulate, groupby
from abc import abstractmethod, ABCMeta



from WeightLengths import WeightLengths
from util import *

class WeightLengthsChild(metaclass=ABCMeta):    
    def __init__(self, minLength, length=None):
        assert self.minLength >= 0
        self.minLength = minLength
        
        self.length = None
        self.setLength(length)
        return
    def setLength(self, length = None):
        minLength = self.minLength
        if length == None:
            length = minLength
        assert length >= minLength

        if length == self.length:
            return
        self._setLength(length)
        return

    @abstractmethod
    def _setLength(self, length):
        assert length >= self.minLength
        self.length = length
        

        
class _WeightLengthsChildren(WeightLengths):
    def _updateLengths(self, length, lengths):
        if self.lengths == None:
            # init
            self.lengths = [-1] * len(lengths)

        self.__updateChildLengths(length, lengths)
        super()._updateLengths(length, lengths)
        return
    def __updateChildLengths(self, length, lengths):
        #print(self.lengths, lengths)

        
        gridxUpdated = []
        for gridx, old, new in zip(range(len(lengths)), self.lengths, lengths):
            if old != new:
                gridxUpdated.append(gridx)

        childUpdatingIndices = set()
        for gridx in gridxUpdated:
            childIndices = self.gridx2childIndices[gridx]
            childUpdatingIndices.update(childIndices)

        for i in childUpdatingIndices:
            child, rng = self.childRngs[i]
            begin, end = rng
            old = sum(self.lengths[begin : end])
            new = sum(lengths[begin : end])

            if old != new:
                child.setLength(new)
        return
    
    def __init__(self, wlChildGridxNgrid, ngrid, *argsOfWeightLengths):
        
        gridx2childIndices = [[] for _ in range(ngrid)]
        childRngs = []
        for child, start, childNgrid in wlChildGridxNgrid:
            end = start + childNgrid
            assert 0 <= start <= end <= ngrid
            idx = len(childRngs)
            for gridx in range(start, end):
                gridx2childIndices[gridx].append(idx)
            childRngs.append((child, (start, end)))

        self.childRngs = childRngs
        self.gridx2childIndices = gridx2childIndices

        super().__init__(ngrid, *argsOfWeightLengths)
        return







def checkMinlengths(rngLen, minLengths):
    for idx, (rng, L) in enumerate(rngLen):
        i, j = rng
        assert sum(minLengths[i:j], 0) >= L

def calcMinlengths(ngrid, rngLen):
    gridx2rngidc = [[] for _ in range(ngrid)]
    for idx, (rng, _) in enumerate(rngLen):
        i, j = rng
        for gridx in range(i,j):
            gridx2rngidc[gridx].append(idx)

    blockGridLens = []
    blockKeys = []
    for k, g in groupby(gridx2rngidc):
        ls = list(g)
        blockGridLens.append(len(ls))
        blockKeys.append(k)

    blockBegins = [0]
    blockBegins.extend(list(accumulate(blockGridLens))[:-1])
    assert len(blockBegins) == len(blockGridLens) == len(blockKeys)

    
    rngidx2rngMinlen = [minLen for _, minLen in rngLen]
    gridx2rngBeginIdc = [[] for _ in range(ngrid)]
    for idx, (rng, _) in enumerate(rngLen):
        begin, end = rng
        gridx = begin
        gridx2rngBeginIdc[gridx].append(idx)
    
    minLengths = [0] * ngrid
    for i in reversed(range(len(blockBegins))):
        blockBegin = blockBegins[i]
        rngBeginIdc = gridx2rngBeginIdc[blockBegin]
        if not rngBeginIdc:
            # the minLengths of grid in this block set to 0 as default
            continue

        minLengthOfThisBlock = max(rngidx2rngMinlen[idx] for idx in rngBeginIdc)
        assert minLengthOfThisBlock >= 0

        minLengths[blockBegin] = minLengthOfThisBlock
        
        rngidc = gridx2rngidc[blockBegin]
        for idx in rngidc:
            rngidx2rngMinlen[idx] -= min(rngidx2rngMinlen[idx], minLengthOfThisBlock)
            
    assert not any(rngidx2rngMinlen)
    assert allUint(minLengths)

    checkMinlengths(rngLen, minLengths)
    return minLengths


class WeightLengthsChildren(_WeightLengthsChildren):
    def __init__(self, wlChildGridxNgrid, ngrid, *argsOfWeightLengths):
        # to calc minLengths

        
        wlChildGridxNgrid = list(wlChildGridxNgrid)
        
        rngLen = []
        for child, start, childNgrid in wlChildGridxNgrid:
            end = start + childNgrid
            assert 0 <= start <= end <= ngrid
            
            minLength = child.minLength
            rng = (start, end)
            rngLen.append((rng, minLength))
            
        minLengths = calcMinlengths(ngrid, rngLen)
        #minLength = sum(gridMinlengths)
        super().__init__(wlChildGridxNgrid, ngrid, minLengths, *argsOfWeightLengths)
        return


def test():
    w = (1,0,0)
    m = (0,1,0)
    e = (0,0,1)
    childrenData = [
        # WeightLengthsArgs, (gridx, ngrid)
        [(3, [1, 2, 3], (1, 3, 7), w, 17), (1,2)],
        [(3, [1, 2, 3], (1, 3, 7), m, 12), (1,3)],
        [(3, [1, 2, 3], (1, 3, 7), e, 9), (2,2)],
        ]
    data = [
        # args, minLengths, [(length,[child[i].length]),]
        [(4, (1, 3, 7, 10), w, ), (0,0,6,0), [(27, [16, 26, 23]), (7, [6,7,7])]],

        ]

    for args, minLengths, lcls in data:
        wlChildGridxNgrid = [(WeightLengths(*args), gridx, ngrid) for args, (gridx, ngrid) in childrenData]
        #print(args)
        
        wlc = WeightLengthsChildren(wlChildGridxNgrid, *args)
        assert wlc.minLengths == minLengths
        for length, childLengths in lcls:
            wlc.setLength(length)
            for childLength, (child, _, _) in zip(childLengths, wlChildGridxNgrid):
                assert child.length == childLength


    return

if __name__ == '__main__':
    test()











