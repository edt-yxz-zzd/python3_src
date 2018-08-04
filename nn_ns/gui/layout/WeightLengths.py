import operator
import fractions

from root.math.math_func import vsub, gcd, vmap, numv_product, vadd
from util import *


class WeightLengths:    
    def __init__(self, ngrid, minLengths, gridWeights = None, \
                 wme:'(weightWeight, minSizeWeight, evenWeight)' = None, \
                 length=None):
        if gridWeights == None:
            gridWeights = (0,) * ngrid
        if wme == None:
            wme = (0, 1, 0)
            
        minLengths, wme, gridWeights = tuple(minLengths), tuple(wme), tuple(gridWeights)

        assert ngrid >= 0
        assert len(wme) == 3
        assert len(gridWeights) == ngrid == len(minLengths)
        assert allUint(minLengths)
        assert allUint(wme)
        assert allUint(gridWeights)

        wme = self.standardizeWME(wme)
        gridWeights = self.standardizeGridWeights(gridWeights)
        totalWeight = sum(gridWeights)
        minLength = sum(minLengths)
        padWeights = self.calcPadWeight(minLengths, gridWeights, wme)

        

        self.ngrid, self.minLengths, self.wme, self.gridWeights, \
                    self.totalWeight, self.minLength, self.padWeights = \
                    ngrid, minLengths, wme, gridWeights, totalWeight, minLength, padWeights

        self.length = None
        self.lengths = None
        self.setLength(length)
        return
    @staticmethod
    def standardizeVector(v, when0=None):
        g = gcd(v)
        if g:
            f = lambda x:operator.__floordiv__(x,g)
            v = vmap(f, v)
        elif when0 == None:
            v = (0,)* len(v)
        else:
            v = WeightLengths.standardizeVector(when0)
        return v
    
    @staticmethod
    def standardizeWME(wme):
        wme = WeightLengths.standardizeVector(wme, (0,0,1))
        #wme = (weightWeight, minSizeWeight, evenWeight) = 
        return wme
    @staticmethod
    def standardizeGridWeights(ws):
        ws = WeightLengths.standardizeVector(ws, (1,)*len(ws))
        return ws
    
    def setLength(self, length = None):
        minLength = self.minLength
        if length == None:
            length = minLength
        assert length >= minLength

        if length == self.length:
            return
        self.__setLength(length)

    @staticmethod
    def calcPadWeight(minLengths, gridWeights, wme):
        ngrid = len(minLengths)
        if ngrid == 0:
            return ()
        
        def v2fv(v):
            d = sum(v)
            assert d
            f = lambda x:fractions.Fraction(x, d)
            fv = vmap(f, v)
            return fv

        assert any(wme)
        assert any(gridWeights)
        fwme = v2fv(wme)
        fgridWeights = v2fv(gridWeights)
        feven = (fractions.Fraction(1, ngrid),) * ngrid
        fminLengths = feven if sum(minLengths) == 0 else v2fv(minLengths)

        fw = lambda w: numv_product(w, fgridWeights)
        fm = lambda m: numv_product(m, fminLengths)
        fe = lambda e: numv_product(e, feven)

        _3vs = (fww(ww) for ww, fww in zip(wme, [fw, fm, fe]))
        padWeights = vadd(*_3vs)
        assert sum(padWeights) == 1
        return padWeights

    def __setLength(self, length):
        
        
        ngrid, minLength, minLengths, wme, gridWeights, padWeights = \
               self.ngrid, self.minLength, self.minLengths, \
               self.wme, self.gridWeights, self.padWeights

        assert length >= minLength

        '''
        if ngrid == 0:
            lengths = ()
            self._updateLengths(length, lengths)
            return'''
        
        pad = length - minLength
        tail_lengths = numv_product(pad, padWeights)
        lengths = vmap(int, tail_lengths)
        tail_lengths = vsub(tail_lengths, lengths)
        lengths = list(vadd(lengths, minLengths))

        n = length - sum(lengths)
        assert ngrid == 0 or n == sum(tail_lengths)

        tail_lengths = [(-t, i) for i, t in enumerate(tail_lengths)]
        tail_lengths.sort()
        for _, i in tail_lengths[:n]:
            lengths[i] += 1

        if not(ngrid == 0 or sum(lengths) == length):
            print(ngrid, length, lengths)
            
        assert ngrid == 0 or sum(lengths) == length
        lengths = tuple(lengths)
        self._updateLengths(length, lengths)
        return
    
    def _updateLengths(self, length, lengths):
        self.length = length
        self.lengths = lengths
        return



def test():
    w = (1,0,0)
    m = (0,1,0)
    e = (0,0,1)

    data =[
        # args, minLength, lengths
        [(0, [], None, None, 12), 0, ()],
        
        [(1, [1], None, None, 12), 1, (12,)],
        [(1, [1], None, w, 12), 1, (12,)],
        [(1, [1], None, m, 12), 1, (12,)],
        [(1, [1], None, e, 12), 1, (12,)],

        
        [(3, [1, 2, 3], (1, 3, 7), w, 17), 6, (2, 5, 10)],
        [(3, [1, 2, 3], (1, 2, 3), m, 12), 6, (2, 4, 6)],
        [(3, [1, 2, 3], (1, 2, 3), e, 9), 6, (2, 3, 4)],

        [(3, [1, 2, 3], (1, 3, 7), w, 17+1), 6, (2, 5, 11)],
        [(3, [1, 2, 3], (1, 2, 3), m, 12+1), 6, (2, 4, 7)],
        [(3, [1, 2, 3], (1, 2, 3), e, 9+1), 6, (3, 3, 4)],
        ]

    for args, minLength, lengths in data:
        wl = WeightLengths(*args)
        assert wl.minLength == minLength
        if not wl.lengths == lengths:
            print(wl.lengths, lengths)
        assert wl.lengths == lengths

    return



if __name__ == '__main__':
    test()




















