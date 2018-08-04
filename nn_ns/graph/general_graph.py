
'''
general_graph
self-loop
multi-edge
undirected-edge
directed-edge

but no color, no label
'''

'''
one directed-edge = two half-edges = src-edge + dst-edge = outgo-edge + income-edge
dedge = oedge + iedge
iedge = -(1+oedge) = o2iedge(oedge)

oedge in range(noe)


one undirected-edge = two directed-edge = oedge + redge
redge is a oedge               # reversed
for undirected-loop, oedge == redge

uedge = min(oedge, redge)      # undirected/unique
vedge is a uedge or it's redge # virtual



GG = (v2ioedges, oedge2redge)
= (v2ioedges, oedge2redge, oedge2src, oedge2dst, uv2ioedges)


oedge2redge[oedge] = None or redge
oedge2uv(oedge) = (oedge2src[oedge], oedge2dst[oedge])


1
== sum(v2ioedges[v].count(oedge) for any v) for any oedge
== v2ioedges[oedge2src[oedge]].count(oedge) for any oedge
== sum(v2ioedges[v].count(iedge) for any v) for any iedge
== v2ioedges[oedge2dst[i2oedge(iedge)]].count(iedge) for any iedge

oedge2uv(oedge) == reversed(oedge2uv(redge)) and oedge2redge[redge] == oedge
for any uedge let oedge = uedge, redge = oedge2redge[oedge]

is_loop(oedge) = oedge2src[oedge] == oedge2dst[oedge]
is_vedge(oedge) = oedge2redge[oedge] != None
is_uedge(oedge) = is_vedge(oedge) and oedge <= oedge2redge[oedge]
is_uloop(oedge) = oedge == oedge2redge[oedge]
is_dedge(oedge) = not is_vedge(oedge)

nv = len(v2ioedges)
nie = noe = len(oedge2redge) = len(oedge2src) = len(oedge2dst)
nue_loop = sum(is_uloop(oedge) for any oedge)
nue = sum(is_uedge(oedge) for any oedge)
ne = noe - nue
nde = ne - nue
ne_loop = sum(is_loop(oedge) for any oedge)
nde_loop = ne_loop - nue_loop

'''

def is_vertex(v, nv):
    return type(v) is int and 0 <= v < nv

def is_oedge(oedge, noe):
    return type(oedge) is int and 0 <= oedge < noe
def is_iedge(iedge, noe):
    oedge = i2oedge(iedge)
    return is_oedge(oedge, noe)
def is_ioedge(ioedge, noe):
    return is_oedge(ioedge, noe) or is_iedge(ioedge, noe)


def o2iedge(oedge):
    iedge = -(1+oedge)
    return iedge

def i2oedge(iedge):
    oedge = -(1+iedge)
    return oedge


####
is_loop = lambda oedge, oedge2src, oedge2dst : oedge2src[oedge] == oedge2dst[oedge]
is_vedge = lambda oedge, oedge2redge : oedge2redge[oedge] != None
is_uedge = lambda oedge, oedge2redge : is_vedge(oedge, oedge2redge) and oedge <= oedge2redge[oedge]
is_uloop = lambda oedge, oedge2redge : oedge == oedge2redge[oedge]
is_dedge = lambda oedge, oedge2redge : not is_vedge(oedge, oedge2redge)
oedge2uv = lambda oedge, oedge2src, oedge2dst : (oedge2src[oedge], oedge2dst[oedge])
iedge2ruv = lambda iedge, oedge2src, oedge2dst : tuple(reversed(oedge2uv(i2oedge(iedge))))
def ioedge2xuv(ioedge, oedge2src, oedge2dst):
    noe = len(oedge2src)
    if is_oedge(ioedge, noe):
        return oedge2uv(ioedge)
    elif is_iedge(ioedge, noe):
        return iedge2ruv(ioedge)
    else:
        raise ValueError('ioedge or len(oedge2src) @ioedge2xuv')
####



def check_v2ioedges_bound(v2ioedges, noe):
    assert all(is_ioedge(ioe, noe) for ios in v2ioedges for ioe in ios)
    return
def check_oedge2redge_bound(oedge2redge, noe):
    assert all(r == None or is_oedge(r, noe) for r in oedge2redge)
    return

def tuple_v2ioedges(v2ioedges):
    return tuple(tuple(ios) for ios in v2ioedges)

def build_oe2src_dst(v2ioedges, noe):
    nv = len(v2ioedges)
    oedge2src = [None] * noe
    oedge2dst = [None] * noe

    for v, ios in enumerate(v2ioedges):
        for ioe in ios:
            if is_oedge(ioe):
                ls = oedge2src
                oe = ioe
            elif is_iedge(ioe):
                ls = oedge2dst
                oe = i2oedge(ioe)
            else:
                raise ValueError('v2ioedges @build_oe2src_dst')
            
            assert ls[oe] == None
            ls[oe] = v

    return oedge2src, oedge2dst

def check_vs_ls_bound(nv, *vs_ls):
    assert all(is_vertex(v, nv) for v in itertools.chain.from_iterable(vs_ls))
    return

def check_args(v2ioedges, oedge2redge, oedge2src, oedge2dst):
    nv = len(v2ioedges)
    noe = len(oedge2redge)
    assert len(oedge2redge) == len(oedge2src) == len(oedge2dst)
    
    check_v2ioedges_bound(v2ioedges, noe)
    check_oedge2redge_bound(oedge2redge, noe)
    check_vs_ls_bound(nv, oedge2src, oedge2dst)

    for oe in range(noe):
        ie = o2iedge(oe)

        assert 1 == sum(v2ioedges[v].count(oe) for v in range(nv))
        assert 1 == sum(v2ioedges[v].count(ie) for v in range(nv))
        
        assert 1 == v2ioedges[oedge2src[oe]].count(oe)
        assert 1 == v2ioedges[oedge2dst[i2oedge(ie)]].count(ie)


    _oedge2uv = lambda oedge: oedge2uv(oedge, oedge2src, oedge2dst)
    for oe in range(noe):
        if not is_uedge(oe, oedge2redge): continue
        r = oedge2redge[oe]

        assert oedge2redge[r] == oe
        assert _oedge2uv(oe) == tuple(reversed(_oedge2uv(r)))
    return

    
class general_graph:
    def __init__(v2ioedges, oedge2redge):
        v2ioedges = tuple_v2ioedges(v2ioedges)
        oedge2redge = tuple(oedge2redge)
        
        nv = len(v2ioedges)
        noe = len(oedge2redge)
        check_v2ioedges_bound(v2ioedges, noe)
        check_oedge2redge_bound(oedge2redge, noe)

        oedge2src, oedge2dst = build_oe2src_dst(v2ioedges, noe)
        check_args(v2ioedges, oedge2redge, oedge2src, oedge2dst)
        

        
        d = collections.defaultdict(list)
        for ios in v2ioedges:
            for ioe in ios:
                u, v = ioedge2xuv(ioedge, oedge2src, oedge2dst)
                d[(u,v)].append(ioe)

        uv2ioedges = collections.defaultdict(
            tuple, (key, tuple(value)) for key, value in d.items())


        self.v2ioedges = v2ioedges
        self.oedge2redge = oedge2redge
        self.oedge2src = oedge2src
        self.oedge2dst = oedge2dst
        self.uv2ioedges = uv2ioedges

        self._nue_loop = sum(self.is_uloop(oedge) for oedge in range(noe))
        self._nue = sum(self.is_uedge(oedge) for oedge in range(noe))
        self._ne_loop = sum(self.is_loop(oedge) for oedge in range(noe))
        pass
    def is_loop(self, oedge):
        return is_loop(oedge, self.oedge2src, self.oedge2dst)
    def is_vedge(self, oedge):
        return is_vedge(oedge, self.oedge2redge)
    def is_uedge(self, oedge):
        return is_uedge(oedge, self.oedge2redge)
    def is_uloop(self, oedge):
        return is_uloop(oedge, self.oedge2redge)
    def is_dedge(self, oedge):
        return is_dedge(oedge, self.oedge2redge)




    def nv(self):
        return len(self.v2ioedges)
    def nie(self):
        return self.noe()
    def noe(self):
        return len(self.oedge2redge)
    
    def nue_loop(self):
        return self._nue_loop
    def nue(self):
        return self._nue
    def ne_loop(self):
        return self._ne_loop
    
    def ne(self):
        return self.noe() - self.nue()
    def nde(self):
        return self.ne() - self.nue()
    def nde_loop(self):
        return self.ne_loop() - self.nue_loop()



    def is_vertex(self, v):
        return is_vertex(v, self.nv())

    def is_oedge(self, oedge):
        noe = self.noe()
        return is_oedge(oedge, noe)
    def is_iedge(self, iedge):
        noe = self.noe()
        return is_iedge(iedge, noe)
    def is_ioedge(self, ioedge):
        noe = self.noe()
        return is_ioedge(ioedge, noe)

    @staticmethod
    def o2iedge(oedge):
        return o2iedge(oedge)
    @staticmethod
    def i2oedge(iedge):
        return i2oedge(iedge)

    def oedge2uv(self, oedge):
        return oedge2uv(oedge, self.oedge2src, self.oedge2dst)
    def iedge2ruv(self, iedge):
        return iedge2ruv(iedge, self.oedge2src, self.oedge2dst)
    def ioedge2xuv(self, ioedge):
        return ioedge2xuv(ioedge, self.oedge2src, self.oedge2dst)


    ################
    def oedges(self, u, v=None):
        return filter(self.is_oedge, self.ioedges(u, v))
    def iedges(self, u, v=None):
        return filter(self.is_iedge, self.ioedges(u, v))
    
    def ioedges(self, u, v=None):
        if v == None:
            return self._v2ioedges(u)
        return self._uv2ioedges(u, v)
    
    def _v2ioedges(self, v):
        return self.v2ioedges[v]
    def _uv2ioedges(self, u, v):
        assert all(map(self.is_vertex, (u,v)))
        return self.uv2ioedges[(u,v)]

    def vedge2redge(self, vedge):
        assert self.is_vedge(vedge)
        return self.oedge2redge[vedge]
    
####







