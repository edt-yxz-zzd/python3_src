#__all__:goto
r'''[[[
e ../../python3_src/seed/graph/DGraph4GrowingOnly.py

used in:
    view ../../python3_src/seed/algo/computing_network.py

seed.graph.DGraph4GrowingOnly
py -m nn_ns.app.debug_cmd seed.graph.DGraph4GrowingOnly
py -m seed.graph.DGraph4GrowingOnly


from seed.graph.DGraph4GrowingOnly import DGraph4GrowingOnly, explain_pn_idx



#]]]'''
__all__ = r'''
    DGraph4GrowingOnly
    explain_pn_idx
'''.split()#'''
__all__


from seed.tiny import null_iter #null_tuple, 
from seed.tiny import check_uint
from seed.tiny_.mk_fdefault import mk_default
#def mk_default(imay_xdefault_rank, xdefault, /,*args4xdefault):


class _Data:
    __slots__ = ()
    def __init__(sf, /, **kw):
        for nm, v in sorted(kw.items()):
            #sorted() to shared keys
            setattr(sf, nm, v)
class Data4Vtx(_Data):
    __slots__ = r'''
    node
    outgo_dedges
    income_dedges
    vtx_st
    '''.split()#'''
    #Data4Vtx(node=,outgo_dedges=,income_dedges=,vtx_st=)
    #_on_new_vtx


class Data4DEdge(_Data):
    __slots__ = r'''
    uv
    param2pdedges
    dedge_st
    '''.split()#'''
    #Data4DEdge(uv=,param2pdedges=,dedge_st=)
    #_on_new_dedge
class Data4PDEdge(_Data):
    __slots__ = r'''
    dedge_param
    pdedge_st
    '''.split()#'''
    #Data4PDEdge(dedge_param=,pdedge_st=)
    #_on_new_pdedge

class DGraph4GrowingOnly:
    r'''directed_edge&multi_dedge&selfloop_dedge; node,vtx,uv/(src,dst),dedge,vtx_st,dedge_st

parametric dedge
    uv_param :: (src,dst,param)
    pdedge :: uint
    dedge -> uv
    uv -> [dedge]
    pdedge -> (dedge, param)
    (dedge, param) -> [pdedge]
pdedge2dedge_param :: [(dedge,param)]
dedge2param2pdedges :: [{(param,):[pdedge]}]


input:
    allow_multi_dedge :: bool
    allow_multi_pdedge :: bool

    #====
    # vtx_st := mk_default(sf.imay_xdefault_rank4vtx_st, sf.xdefault4vtx_st, sf, node, vtx)
    #====
    imay_xdefault_rank4vtx_st <- [-1..=3]
    xdefault4vtx_st :: vtx_st if imay_xdefault_rank4vtx_st==-1 else (sf, node, vtx)[3-imay_xdefault_rank4vtx_st:] -> vtx_st


    #====
    # dedge_st := mk_default(sf.imay_xdefault_rank4dedge_st, sf.xdefault4dedge_st, sf, src, dst, dedge)
    #====
    imay_xdefault_rank4dedge_st <- [-1..=4]
    xdefault4dedge_st :: dedge_st if imay_xdefault_rank4dedge_st==-1 else (sf, src, dst, dedge)[4-imay_xdefault_rank4dedge_st:] -> dedge_st


    #====
    # pdedge_st := mk_default(sf.imay_xdefault_rank4pdedge_st, sf.xdefault4pdedge_st, sf, dedge, param, pdedge)
    #====
    imay_xdefault_rank4pdedge_st <- [-1..=4]
    xdefault4pdedge_st :: pdedge_st if imay_xdefault_rank4pdedge_st==-1 else (sf, src, dst, pdedge)[4-imay_xdefault_rank4pdedge_st:] -> pdedge_st




new_concrete_methods:
__init__
num_vertices
num_dedges
num_pdedges
get_num_vertices
get_num_dedges
get_num_pdedges
_on_new_vtx
_on_new_dedge
_on_new_pdedge
numbers_node
numbers_node_ex
numbers_uv
numbers_uv_ex
numbers_dedge_param
numbers_dedge_param_ex
add_dedge
add_pdedge
vtx2node
vtx2vtx_st
src2dedges
dst2dedges
dedge2uv
dedge2param2pdedges
dedge2dedge_st
dedge2src
dedge2dst
dedge_param2pdedges
pdedge2dedge_param
pdedge2pdedge_st
pdedge2dedge
pdedge2param
pdedge2uv
pdedge2src
pdedge2dst
uv2iter_pdedges
src2iter_pdedges
dst2iter_pdedges
dedge2iter_pdedges
auto_extend_graph
auto_extend_graph__pdedge
    '''#'''
    def __init__(sf, /, *, allow_multi_dedge, allow_multi_pdedge, imay_xdefault_rank4vtx_st, xdefault4vtx_st, imay_xdefault_rank4dedge_st, xdefault4dedge_st, imay_xdefault_rank4pdedge_st, xdefault4pdedge_st):
        sf.node2vtx = {} #{node:vtx}
        sf.uv2dedges = {} #{(src,dst):[dedge]}
        sf.pdedge2pdedge_ns = []
        sf.dedge2dedge_ns = []
        sf.vtx2vtx_ns = []

        if 0:
            #####
            sf.vtx2node = []
            sf.node2vtx = {} #{node:vtx}
            #####
            sf.dedge2uv = [] #[(src,dst)]
            sf.uv2dedges = {} #{(src,dst):[dedge]}
            sf.src2dedges = [] #[[dedge]]
            sf.dst2dedges = [] #[[dedge]]
            #####
            sf.dedge2param2pdedges = [] # [{(param,):[pdedge]}]
            sf.pdedge2dedge_param = [] # [(dedge,param)]
            #####
            sf.pdedge2pdedge_st = []
            sf.dedge2dedge_st = []
            sf.vtx2vtx_st = []
        #####
        sf.allow_multi_dedge = bool(allow_multi_dedge)
        sf.allow_multi_pdedge = bool(allow_multi_pdedge)

        sf.imay_xdefault_rank4vtx_st = imay_xdefault_rank4vtx_st
        sf.xdefault4vtx_st = xdefault4vtx_st

        sf.imay_xdefault_rank4dedge_st = imay_xdefault_rank4dedge_st
        sf.xdefault4dedge_st = xdefault4dedge_st

        sf.imay_xdefault_rank4pdedge_st = imay_xdefault_rank4pdedge_st
        sf.xdefault4pdedge_st = xdefault4pdedge_st


    @property
    def num_vertices(sf, /):
        return sf.get_num_vertices()
    @property
    def num_dedges(sf, /):
        return sf.get_num_dedges()
    @property
    def num_pdedges(sf, /):
        return sf.get_num_pdedges()

    def get_num_vertices(sf, /):
        return len(sf.vtx2vtx_ns)
        return len(sf.vtx2node)
    def get_num_dedges(sf, /):
        return len(sf.dedge2dedge_ns)
        return len(sf.dedge2uv)
    def get_num_pdedges(sf, /):
        return len(sf.pdedge2pdedge_ns)
        return len(sf.pdedge2dedge_param)


    def _on_new_vtx(sf, vtx, node, vtx_st, /):
        sf.node2vtx[node] = vtx
        vtx_ns = Data4Vtx(node=node,outgo_dedges=[],income_dedges=[],vtx_st=vtx_st)
        sf.vtx2vtx_ns.append(vtx_ns)
        assert len(sf.node2vtx) == sf.num_vertices
        return
        sf.node2vtx[node] = vtx
        sf.vtx2node.append(node)
        sf.vtx2vtx_st.append(vtx_st)
        sf.src2dedges.append([])
        sf.dst2dedges.append([])
        assert len(sf.node2vtx) == len(sf.vtx2node) == len(sf.vtx2vtx_st) == len(sf.src2dedges) == len(sf.dst2dedges) == sf.num_vertices


    def _on_new_dedge(sf, dedge, src, dst, dedge_st, /):
        uv = src, dst
        dedges4uv = sf.uv2dedges.setdefault(uv, [])
        dedges4uv.append(dedge)
        dedge_ns = Data4DEdge(uv=uv,param2pdedges={},dedge_st=dedge_st)
        sf.dedge2dedge_ns.append(dedge_ns)
        sf.src2dedges(src).append(dedge)
        sf.dst2dedges(dst).append(dedge)
        assert sf.num_dedges >= len(sf.uv2dedges)
        assert sf.allow_multi_dedge or sf.num_dedges == len(sf.uv2dedges)
        return
        uv = src, dst
        dedges4uv = sf.uv2dedges.setdefault(uv, [])
        dedges4uv.append(dedge)
        sf.dedge2uv.append(uv)
        sf.src2dedges[src].append(dedge)
        sf.dst2dedges[dst].append(dedge)
        sf.dedge2dedge_st.append(dedge_st)
        sf.dedge2param2pdedges.append({})
        assert len(sf.dedge2uv) == len(sf.dedge2dedge_st) == len(sf.dedge2param2pdedges) == sf.num_dedges >= len(sf.uv2dedges)
        assert sf.allow_multi_dedge or sf.num_dedges == len(sf.uv2dedges)



    def _on_new_pdedge(sf, pdedge, dedge, param, pdedge_st, /):
        pdedges = sf.dedge2param2pdedges(dedge).setdefault(param, [])
        pdedges.append(pdedge)
        pdedge_ns = Data4PDEdge(dedge_param=(dedge,param),pdedge_st=pdedge_st)
        sf.pdedge2pdedge_ns.append(pdedge_ns)
        return
        pdedges = sf.dedge2param2pdedges[dedge].setdefault(param, [])
        pdedges.append(pdedge)
        sf.pdedge2dedge_param.append((dedge,param))
        sf.pdedge2pdedge_st.append(pdedge_st)
        assert len(sf.pdedge2dedge_param) == len(sf.pdedge2pdedge_st) == sf.num_pdedges







    def numbers_node(sf, node, /):
        'node -> vtx #old | new'
        (is_new, vtx) = sf.numbers_node_ex(node)
        return vtx
    def numbers_node_ex(sf, node, /):
        'node -> (is_new, vtx)'
        assert len(sf.node2vtx) == sf.num_vertices
        L = sf.num_vertices
        vtx = sf.node2vtx.get(node, L)
        is_new = vtx == L
        if is_new:
            #new
            vtx_st = mk_default(sf.imay_xdefault_rank4vtx_st, sf.xdefault4vtx_st, sf, node, vtx)
            sf._on_new_vtx(vtx, node, vtx_st)
        assert len(sf.node2vtx) == sf.num_vertices
        return (is_new, vtx)

    def numbers_uv(sf, src, dst, /):
        'src -> dst -> dedge #old | new'
        (is_new, dedge) = sf.numbers_uv_ex(src, dst)
        return dedge
    def numbers_uv_ex(sf, src, dst, /):
        'src -> dst -> (is_new, dedge)'
        if sf.allow_multi_dedge: raise TypeError
        pn_dedge = sf.add_dedge(src, dst, donot_raise_on_multi_dedge=True)
        (is_new, dedge) = explain_pn_idx(pn_dedge)
        return (is_new, dedge)
    def numbers_dedge_param(sf, dedge, param, /):
        'dedge -> param -> pdedge #old | new'
        (is_new, pdedge) = sf.numbers_dedge_param_ex(dedge, param)
        return pdedge
    def numbers_dedge_param_ex(sf, dedge, param, /):
        'dedge -> param -> (is_new, pdedge)'
        if sf.allow_multi_pdedge: raise TypeError
        pn_pdedge = sf.add_pdedge(dedge, param, donot_raise_on_multi_pdedge=True)
        (is_new, pdedge) = explain_pn_idx(pn_pdedge)
        return (is_new, pdedge)

    def add_dedge(sf, src, dst, /, *, donot_raise_on_multi_dedge):
        '-> pn_dedge (dedge | not sf.allow_multi_dedge&occur multi_dedge ==>> (-1-dedge if donot_raise_on_multi_dedge else raise ValueError))'
        dedge = sf.num_dedges
        uv = src, dst
        may_dedges4uv = sf.uv2dedges.get(uv)
        if may_dedges4uv and not sf.allow_multi_dedge:
            [dedge] = may_dedges4uv
            if donot_raise_on_multi_dedge:
                pn_dedge = -1-dedge
                return pn_dedge
            raise ValueError('not allow_multi_dedge')

        dedge_st = mk_default(sf.imay_xdefault_rank4dedge_st, sf.xdefault4dedge_st, sf, src, dst, dedge)
        sf._on_new_dedge(dedge, src, dst, dedge_st)

        pn_dedge = dedge
        return pn_dedge

    def add_pdedge(sf, dedge, param, /, donot_raise_on_multi_pdedge):
        '-> pn_pdedge (pdedge | not sf.allow_multi_pdedge&occur multi_pdedge ==>> (-1-pdedge if donot_raise_on_multi_pdedge else raise ValueError))'
        pdedge = sf.num_pdedges
        #may_pdedges = sf.dedge2param2pdedges[dedge].get(param)
        dedge_ns = sf.dedge2dedge_ns[dedge]
        may_pdedges = dedge_ns.param2pdedges.get(param)
        if may_pdedges and not sf.allow_multi_pdedge:
            [pdedge] = may_pdedges
            if donot_raise_on_multi_pdedge:
                pn_pdedge = -1-pdedge
                return pn_pdedge
            raise ValueError('not allow_multi_pdedge')

        pdedge_st = mk_default(sf.imay_xdefault_rank4pdedge_st, sf.xdefault4pdedge_st, sf, dedge, param, pdedge)
        sf._on_new_pdedge(pdedge, dedge, param, pdedge_st)

        pn_pdedge = pdedge
        return pn_pdedge


    ########
    def vtx2node(sf, vtx, /):
        return sf.vtx2vtx_ns[vtx].node
    def vtx2vtx_st(sf, vtx, /):
        return sf.vtx2vtx_ns[vtx].vtx_st
    def src2dedges(sf, src, /):
        return sf.vtx2vtx_ns[src].outgo_dedges
    def dst2dedges(sf, dst, /):
        return sf.vtx2vtx_ns[dst].income_dedges
    ########
    ########
    def dedge2uv(sf, dedge, /):
        return sf.dedge2dedge_ns[dedge].uv
    def dedge2param2pdedges(sf, dedge, /):
        return sf.dedge2dedge_ns[dedge].param2pdedges
    def dedge2dedge_st(sf, dedge, /):
        return sf.dedge2dedge_ns[dedge].dedge_st
    def dedge2src(sf, dedge, /):
        return sf.dedge2dedge_ns[dedge].uv[0]
    def dedge2dst(sf, dedge, /):
        return sf.dedge2dedge_ns[dedge].uv[1]
    def dedge_param2pdedges(sf, dedge, param, /):
        return sf.dedge2dedge_ns[dedge].param2pdedges[param]
    ########
    ########
    def pdedge2dedge_param(sf, pdedge, /):
        return sf.pdedge2pdedge_ns[pdedge].dedge_param
    def pdedge2pdedge_st(sf, pdedge, /):
        return sf.pdedge2pdedge_ns[pdedge].pdedge_st
    def pdedge2dedge(sf, pdedge, /):
        return sf.pdedge2pdedge_ns[pdedge].dedge_param[0]
    def pdedge2param(sf, pdedge, /):
        #bug:return sf.pdedge2pdedge_ns[pdedge].dedge_param[1:]
        return sf.pdedge2pdedge_ns[pdedge].dedge_param[1]

    def pdedge2uv(sf, pdedge, /):
        return sf.dedge2uv(sf.pdedge2dedge(pdedge))
    def pdedge2src(sf, pdedge, /):
        return sf.dedge2src(sf.pdedge2dedge(pdedge))
    def pdedge2dst(sf, pdedge, /):
        return sf.dedge2dst(sf.pdedge2dedge(pdedge))

    def uv2iter_pdedges(sf, uv, /):
        for dedge in sf.uv2dedges.get(uv, null_iter):
            yield from sf.dedge2iter_pdedges(dedge)

    def src2iter_pdedges(sf, src, /):
        for dedge in sf.src2dedges(src):
            yield from sf.dedge2iter_pdedges(dedge)
    def dst2iter_pdedges(sf, dst, /):
        for dedge in sf.dst2dedges(dst):
            yield from sf.dedge2iter_pdedges(dedge)
    def dedge2iter_pdedges(sf, dedge, /):
        param2pdedges = sf.dedge2param2pdedges(dedge)
        for pdedges in param2pdedges.values():
            yield from pdedges
    ########

    def auto_extend_graph(sf, begin_vtx, src_node_src_st2iter_dst_nodes, /, *, donot_raise_on_multi_dedge):
        'src_node_src_st2iter_dst_nodes :: node -> vtx_st -> Iter node'
        check_uint(begin_vtx)
        donot_raise_on_multi_dedge = bool(donot_raise_on_multi_dedge)
        src = begin_vtx
        while src < sf.num_vertices:
            src_node = sf.vtx2node(src)
            src_st = sf.vtx2vtx_st(src)
            for dst_node in src_node_src_st2iter_dst_nodes(src_node, src_st):
                dst = sf.numbers_node(dst_node)
                sf.add_dedge(src, dst, donot_raise_on_multi_dedge=donot_raise_on_multi_dedge)

            src += 1


    def auto_extend_graph__pdedge(sf, begin_dedge, dedge_st_src_node_src_st_dst_node_dst_st2iter_param4pdedge, /, *, donot_raise_on_multi_pdedge):
        'dedge_st_src_node_src_st_dst_node_dst_st2iter_param4pdedge :: dedge_st -> src_node -> src_st -> dst_node -> dst_st -> Iter param4pdedge'
        check_uint(begin_dedge)
        donot_raise_on_multi_dedge = bool(donot_raise_on_multi_dedge)
        dedge = begin_dedge
        while dedge < sf.num_dedges:
            dedge_st = sf.dedge2dedge_st(dedge)
            src = sf.dedge2src(dedge)
            src_node = sf.vtx2node(dedge)
            src_st = sf.vtx2vtx_st(dedge)
            dst = sf.dedge2dst(dedge)
            dst_node = sf.vtx2node(dedge)
            dst_st = sf.vtx2vtx_st(dedge)
            for param in dedge_st_src_node_src_st_dst_node_dst_st2iter_param4pdedge(dedge_st, src_node, src_st, dst_node, dst_st):
                sf.add_pdedge(dedge, param, donot_raise_on_multi_pdedge=donot_raise_on_multi_pdedge)

            dedge += 1

def explain_pn_idx(pn_idx, /):
    'pn_idx -> (is_new, idx)'
    is_new = pn_idx >= 0
    if is_new:
        idx = pn_idx
    else:
        idx = -1-pn_idx
    return (is_new, idx)

#end-class DGraph4GrowingOnly:

if 0:
    def add_dedge5node(sf, src_node, dst_node, /, *, donot_raise_on_multi_dedge):
        '-> pn_dedge (dedge | not sf.allow_multi_dedge&occur multi_dedge ==>> (-1-dedge if donot_raise_on_multi_dedge else raise ValueError))'
        src = sf.numbers_node(src_node)
        dst = sf.numbers_node(dst_node)
        return sf.add_dedge(src, dst, donot_raise_on_multi_dedge=donot_raise_on_multi_dedge)

from seed.graph.DGraph4GrowingOnly import DGraph4GrowingOnly, explain_pn_idx

if __name__ == '__main__':
    XXX = DGraph4GrowingOnly

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)


