
'''
see:
    "planar/algo - is fake_embedding relax_planar[ver2].txt"
    "def - relax biconnected.txt"


(1 old hedge, 1 old fvertex) -> (6 new hedges, 3 new aedges, 2 new fvertices)

(v)-[h]->{e}<-[o]<-(u)
h is hedge
let v = hedge2fvertex[h]
    o = hedge2another_hedge[h]
    e = hedge2aedge[h]
    n = hedge2fake_clockwise_next_hedge_around_vertex[v]
    p = hedge2fake_clockwise_prev_hedge_around_vertex[v]

    #hedge2fake_clockwise_next_hedge_around_fface

# old -> NEW...
v -> VP, VN
    # V: new fvertex
    # P/N fake clockwise prev/next
h -> HPP, HPM, HPN, HNP, HNM, HNN
    # H: new hedge
    # P/N: from VP, VN
    # P/M/N fake clockwise prev/next
h -> ES, EI, EE
    # E: new aedge
    # S/I/E - self, internal, external


(v)-[h]->{e}
==>>
                                 (VN(o))-...............-(VP(o))
                                   |                       |
                                 [HNM(o)]                [HPM(o)]
                                   |                       |
                                   v                       v
                                  {ES}                    {ES(o)}
                                   ^                       ^
                                   |                       |
                                 [HPM]                   [HNM]
                                   |                       |
(VN(p))-[HNN(p)]->{EE(p)}<-[HPP]-(VP)-[HPN]->{EI}<-[HNP]-(VN)-[HNN]->{EE}<-[HPP(n)]-(VP(n))

# X=P/N, Y=P/M/N, Z=S/I/E, W=F/E/V
    # VX, EZ, HXY

    #VX
    VP(h) = 2*h
    VN(h) = VP(h)+1

    #EZ
    ES(h) = 3*hedge2aedge[h]
    EI(h) = ES(h)+1
    EE(h) = ES(h)+2

    #HXY
    HPP(h) = 6*h
    HPM(h) = HPP+1
    HPN(h) = HPP+2
    HNP(h) = HPP+3
    HNM(h) = HPP+4
    HNN(h) = HPP+5

    #FW
    #new fface
    num_ffaces__new = num_ffaces + num_aedges + num_fvertices
    from old fface:
        FF = new_fface = old_fface
    from aedge:
        FE = new_fface = num_ffaces + aedge
    from fvertex:
        FV = new_fface = num_ffaces + num_aedges + fvertex
'''

__all__ = '''
    ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex
    '''.split()
from ..UGraphFakeEmbedding import UGraphFakeEmbedding


# VX
# HXY
# EZ
class Global:
    Xs = 'PN'
    Ys = 'PMN'
    Zs = 'SIE'
    #Ws = 'FEV'
    num_VXs = len(Xs)
    num_EZs = len(Zs)
    num_HXYs = len(Xs)*len(Ys)

    assert num_HXYs == 6

class MkHXY:
    # HXY: X=P/N, Y=P/M/N
    def __init__(self, hedge):
        self._HPP = Global.num_HXYs * hedge

    @property
    def HPP(self): return self._HPP+0
    @property
    def HPM(self): return self._HPP+1
    @property
    def HPN(self): return self._HPP+2
    @property
    def HNP(self): return self._HPP+3
    @property
    def HNM(self): return self._HPP+4
    @property
    def HNN(self): return self._HPP+5
class MkVX:
    def __init__(self, hedge):
        self._VP = Global.num_VXs * hedge
    @property
    def VP(self): return self._VP+0
    @property
    def VN(self): return self._VP+1
class MkEZ:
    def __init__(self, aedge):
        self._ES = Global.num_EZs * aedge
    @property
    def ES(self): return self._ES+0
    @property
    def EI(self): return self._ES+1
    @property
    def EE(self): return self._ES+2
class MkFW:
    def __init__(self, num_ffaces, num_aedges, num_fvertices):
        self.offset__fface = 0
        self.offset__aedge = num_ffaces
        self.offset__fvertex = num_ffaces + num_aedges
        self.num_ffaces__new = num_ffaces + num_aedges + num_fvertices

    def from_fface(self, fface): return self.offset__fface + fface
    def from_aedge(self, aedge): return self.offset__aedge + aedge
    def from_fvertex(self, fvertex): return self.offset__fvertex + fvertex



def HXY2delta_HPP(HXY):
    return HXY % Global.num_HXYs
def HXY2HPP(HXY):
    return HXY - HXY2delta_HPP(HXY)
def new_HXY2old_hedge(HXY):
    return HXY // Global.num_HXYs

def ugraph_fake_embedding2relax_biconnected_ugraph_fake_embedding_ex(*
    ,ugraph_fake_embedding, hedge2aedge):
    # -> (ugraph_fake_embedding__new, hedge2aedge__new)
    hedge2another_hedge = ugraph_fake_embedding.hedge2another_hedge
        # method, not array
    hedge2fake_clockwise_next_hedge_around_vertex = \
        ugraph_fake_embedding.hedge2fake_clockwise_next_hedge_around_vertex

    num_ffaces = ugraph_fake_embedding.num_ffaces
    num_hedges = ugraph_fake_embedding.num_hedges
    num_fvertices = ugraph_fake_embedding.num_fvertices

    num_aedges = num_hedges//2
    assert num_hedges == 2*num_aedges

    mkF = MkFW(num_ffaces=num_ffaces
            , num_aedges=num_aedges
            , num_fvertices=num_fvertices
            )

    num_ffaces__new = mkF.num_ffaces__new
    num_hedges__new = Global.num_HXYs*num_hedges
    num_fvertices__new = Global.num_VXs*num_hedges

    hedge2another_hedge__new = [None]*num_hedges__new
    hedge2aedge__new = [None]*num_hedges__new
    hedge2fake_clockwise_next_hedge_around_vertex__new = [None]*num_hedges__new

    fface2arbitrary_hedge__new = [None]*num_ffaces__new
    fvertex2arbitrary_hedge__new = [None]*num_fvertices__new

    #for hedge in range(num_hedges):
    for hedge, aedge in enumerate(hedge2aedge):
        #fvertex = ugraph_fake_embedding.hedge2fvertex
        other_hedge = hedge2another_hedge(hedge) # method
        next_hedge = hedge2fake_clockwise_next_hedge_around_vertex[hedge]

        mkH = MkHXY(hedge)
        mkH_o = MkHXY(other_hedge)
        mkH_n = MkHXY(next_hedge)
        mkE = MkEZ(aedge)
        mkV = MkVX(hedge)

        HPM = mkH.HPM
        HNM_o = mkH_o.HNM
        ES = mkE.ES

        HPN = mkH.HPN
        HNP = mkH.HNP
        EI = mkE.EI

        HNN = mkH.HNN
        HPP_n = mkH_n.HPP
        EE = mkE.EE

        triples = [(HPM, HNM_o, ES), (HPN, HNP, EI), (HNN, HPP_n, EE)]
        for H,O,E in triples:
            hedge2another_hedge__new[H] = O
            hedge2another_hedge__new[O] = H
            hedge2aedge__new[H] = E
            hedge2aedge__new[O] = E

        HPP = mkH.HPP
        HNM = mkH.HNM
        hedgess_around_vertex__new = [(HPP, HPM, HPN), (HNP, HNM, HNN)]
        for hedges in hedgess_around_vertex__new:
            prev = hedges[-1]
            for curr in hedges:
                hedge2fake_clockwise_next_hedge_around_vertex__new[prev] = curr
                prev = curr

        FE = mkF.from_aedge(aedge)
        fface2arbitrary_hedge__new[FE] = HPM # assign twice!!

        fvertex2arbitrary_hedge__new[mkV.VP] = HPM
        fvertex2arbitrary_hedge__new[mkV.VN] = HNM

    for fface, hedge in enumerate(ugraph_fake_embedding.fface2arbitrary_hedge):
        mkH = MkHXY(hedge)

        HNM = mkH.HNM
        FF = mkF.from_fface(fface)
        fface2arbitrary_hedge__new[FF] = HNM

    for fvertex, hedge in enumerate(ugraph_fake_embedding.fvertex2arbitrary_hedge):
        mkH = MkHXY(hedge)

        HPN = mkH.HPN
        FV = mkF.from_fvertex(fvertex)
        fface2arbitrary_hedge__new[FV] = HPN

    (ugraph_fake_embedding__new
    ) = UGraphFakeEmbedding.make_UGraphFakeEmbedding__simplest(
        hedge2fake_clockwise_next_hedge_around_vertex
            = hedge2fake_clockwise_next_hedge_around_vertex__new
        ,hedge2another_hedge
            = hedge2another_hedge__new
        ,fface2arbitrary_hedge
            = fface2arbitrary_hedge__new
        ,fvertex2arbitrary_hedge
            = fvertex2arbitrary_hedge__new
        )
    return ugraph_fake_embedding__new, hedge2aedge__new


