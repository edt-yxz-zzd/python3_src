
from .DFS import *
from .bucket_sort import bucket_sorts, group_to_list, bucket_sort
from .simple_undirected_graph import graph
from .rooted_tree import *

from .planar_ordering import _make_connected

__all__ = ('is_planar, NonplanarError, Boyer_Myrvold_planarity_test, '
           'is_planar_embedding, planar_embedding_by_Boyer_Myrvold'\
           .split(', '))

DEBUG = 0

def planar_embedding_by_Boyer_Myrvold(G):
    try:
        embedding = Boyer_Myrvold_planarity_test(G)
        return embedding
    except NonplanarError:
        return None


def is_planar(G):
    try:
        Boyer_Myrvold_planarity_test(G)
        return True
    except NonplanarError:
        return False

class NonplanarError(Exception):pass

def _remove_edges(G):
    n = G.order()
    m = G.num_edges()
    # n-m+f=2
    # if n > 2, no multiedges, then 3f<=2m :
    #    2m/3>=f=2-n+m ~ m <= 3n-6
    if n > 2 and m > 3*n-6:
        if m > 3*n-5:
            edges = []
            for v in G.vertices():
                if len(edges) == 3*n-5: break
                for u in G.neighbors(v):
                    if v < u:
                        edges.append((v,u))
                        if len(edges) == 3*n-5: break
            G = graph(n, edges)

    return G, n


def _init_dfs(G):
    n = G.order()
    dfs_ord = [None]*n  # vertex to depth first indices (DFI)
    dfs_seq = []        # DFI2vtx
    low_pt = [None]*n   # ord
    self_low_pt = [None]*n
    tree_edge = [] # (p,v,v_low_pt)
    back_edge = [] # (v, ancester)
    roots = []
    def ent(v):
        v_ord = len(dfs_seq)
        dfs_ord[v] = v_ord
        low_pt[v] = v_ord
        self_low_pt[v] = v_ord
        dfs_seq.append(v)
        
    def ext(p,v):
        if low_pt[v] < low_pt[p]:
            low_pt[p] = low_pt[v]
    for action, argv in DFS(G):
        p = v = idx = a = None
        if action == enter_tree:
            G, v = argv
            ent(v)
            roots.append(v)
        elif action == exit_tree:
            G, v = argv
        elif action == enter_tree_edge:
            G, idx, p, v = argv
            ent(v)
        elif action == exit_tree_edge:
            G, idx, p, v = argv
            tree_edge.append((p,v,low_pt[v]))
            ext(p,v)
        elif action == visit_back_edge:
            G, idx, v, a = argv
            if dfs_ord[a] < low_pt[v]:
                low_pt[v] = dfs_ord[a]
        elif action == revisit_back_edge:
            G, idx, p, v = argv
            back_edge.append((p,v))
            if dfs_ord[p] < self_low_pt[v]:
                self_low_pt[v] = dfs_ord[p]
        else:
            raise 'unknown'

    #back_edge = bucket_sort(back_edge, lambda e: e[0], n)
    rback_edge = group_to_list(n, back_edge, lambda e: e[0], lambda e:e[1])
    del back_edge
    
    tree_edge = bucket_sorts(tree_edge, lambda i,e: e[i], [2,0], [n,n])
    dfs_children = group_to_list(n, tree_edge, lambda e: e[0], lambda e:e[1])
    tree_edge = tuple(e[:2] for e in tree_edge)

    return dfs_ord, dfs_seq, low_pt, self_low_pt, tree_edge, rback_edge, roots, dfs_children




#2333333333333333333333333333333333333333333



class _separated_dfs_child:
    def __init__(self, siblingL = None, siblingR = None, lowest_child = None):
        self.sL = siblingL
        self.sR = siblingR
        self.lC = lowest_child
    def __repr__(self):
        return '<separated_dfs_child:siblingL={}, siblingR={}, lowest_child={}>'\
               .format(self.sL, self.sR, self.lC)


class _Node:
    def __init__(self, parent, outerfaceL, outerfaceR):
        self.p = parent
        self.fL = [outerfaceL]
        self.fR = [outerfaceR]
    def __repr__(self):
        return '<Node:parent={}, outerfaceL={}, outerfaceR={}>'\
               .format(self.p, self.fL, self.fR)



def _virtual_parent(v, n): return n + v
def _rvirtual_parent(pv, n): return pv - n

def _make_separated_dfs_child_list(dfs_children, low_pt):
    n = len(low_pt)
    is_separated = [True]*n
    separated_dfs_child_list = [_separated_dfs_child() for i in range(n)]
    for p, children in enumerate(dfs_children):
        for v in reversed(children):
            lc = separated_dfs_child_list[p].lC
            if lc != None: assert low_pt[v] <= low_pt[lc]
            separated_dfs_child_list[v].sR = lc
            if lc != None: separated_dfs_child_list[lc].sL = v
            separated_dfs_child_list[p].lC = v
    return separated_dfs_child_list, is_separated


def _make_partial_graph(n, roots, tree_edge):
    g = [None]*(2*n)
    for v in roots:
        g[v] = _Node(v, v, v)
        g[v].fL.clear()
        g[v].fR.clear()  # law : real vertex incident to virtual's
    for p, v in tree_edge:
        pv = _virtual_parent(v, n)
        g[v] = _Node(pv, pv, pv)
        g[pv] = _Node(p, v, v)
    return g



def Boyer_Myrvold_planarity_test(G):
    bm = _Boyer_Myrvold(G)
    embedding = bm.test()
    if DEBUG and not is_planar_embedding(embedding):
        print(embedding)
        print(G)
        assert is_planar_embedding(embedding)
    return embedding

class _Boyer_Myrvold:
    def __init__(self, G):
        self.G, self.n = _remove_edges(G)
        self.dfs_ord, self.dfs_seq, \
                      self.low_pt, self.self_low_pt, \
                      self.tree_edge, self.rback_edge, \
                      self.roots, self.dfs_children\
                      = _init_dfs(G)

        self.separated_dfs_child_list, self.is_separated = \
                _make_separated_dfs_child_list(self.dfs_children, self.low_pt)
        self.g = _make_partial_graph(self.n, self.roots, self.tree_edge)
        del self.tree_edge


        #233333333333333333333333333333333333333333333333333333333333333
        n = self.n
        self._visited = [None]*(2*n)
        self._has_back_edge = [False]*n
        self._merging_children = [([], []) for i in range(n)]

        self.left = False
        self.right = True

        self.flips = [[] for i in range(n)]
        self.flip_flag = [None]*n
        return

    def add_flip(self, rup, rdown, s):# s == True means flip
        assert self.is_virtual_node(rup)
        assert self.is_virtual_node(rdown)
        iup = _rvirtual_parent(rup, self.n)
        idown = _rvirtual_parent(rdown, self.n)
        self.flips[iup].append((idown, s))
    def fill_flip_flag(self):
        for r in self.roots:
            self.flip_flag[r] = False

        for v, node in enumerate(self.separated_dfs_child_list):
            while node.lC != None:
                c = node.lC
                root = _virtual_parent(node.lC, self.n)
                self.delete_separated_child(v, root)
                self.g[v].fL.append(root)
                assert self.flip_flag[c] == None
                self.flip_flag[c] = False

        for v in self.dfs_seq:
            f = self.flip_flag[v]
            assert f != None
            for c, s in self.flips[v]:
                assert self.flip_flag[c] == None
                self.flip_flag[c] = f ^ s

        for f in self.flip_flag:
            assert f != None

    def test(self):
        for p in reversed(self.dfs_seq):
            for v in self.rback_edge[p]:
                self.walk_up(self.g, p, v)

            num_embedded = 0
            for c in self.dfs_children[p]:
                pc = _virtual_parent(c, self.n)
                num_embedded += self.walk_down(self.g, pc)

            if num_embedded != len(self.rback_edge[p]):
                raise NonplanarError('nonplanar') 


        embedding = self.recover_embedding(self.G, self.g)
        return embedding
    
    def walk_up(self, g, a, v):
        assert not self.is_virtual_node(a)
        assert not self.is_virtual_node(v)
        self._has_back_edge[v] = True
        r = None
        u = g[v].fL[-1]
        _v, _u = u, v
        while v != a and u != a:
            if self.has_visited(a,u,v):break
            self.visit(a, u, v)
            if self.is_component_root(v): r = v
            elif self.is_component_root(u): r = u
            if r == None:
                _v, v = self.move(_v, v)
                _u, u = self.move(_u, u)
                continue

            p = g[r].p
            if p == a: break
            extern = self.is_externally_active_component(a, r)
            self._merging_children[p][extern].append(r)
            #move up
            r = None
            v = p
            u = g[v].fL[-1]
            _v, _u = u, v

    def is_virtual_node(self, v): return v > self.n-1
    
    def is_separated_dfs_child(self, pv):
        assert self.is_virtual_node(pv)
        return self.is_separated[_rvirtual_parent(pv, self.n)]
    def is_component_root(self, v):
        return self.is_virtual_node(v) and self.is_separated_dfs_child(v)

    def lowpt_for_component(self, r):
        assert self.is_component_root(r)
        v = _rvirtual_parent(r, self.n)
        return self.low_pt[v]
    def is_externally_active_component(self, a, r):
        assert not self.is_virtual_node(a)
        assert self.is_component_root(r)
        return self.lowpt_for_component(r) < self.dfs_ord[a]

    def has_visited(self, a, u, v):
        return self._visited[v] == a or self._visited[u] == a
    def visit(self, a, u, v):
        self._visited[v] = a
        self._visited[u] = a

    def move(self, u, v):
        if self.g[v].fL[-1] == u:
            return v, self.g[v].fR[-1]
        return v, self.g[v].fL[-1]


    #23333333333333333333333333333333333333333
    def walk_down(self, g, pv):
        assert self.is_virtual_node(pv)
        L = g[pv].fL[-1]
        n = self.walk_down_one_side(g, pv, pv, L, self.left)
        R = g[pv].fR[-1]
        n += self.walk_down_one_side(g, pv, pv, R, self.right)
        return n


    
    def walk_down_one_side(self, g, r, up, down, side):
        #print('walk_down_one_side(g, r{}, up{}, down{}, side{})'.format(r, up, down, side))
        n = 0
        while down != r:
            if self.is_virtual_node(down):
                up, down = self.move(up, down)
                continue
            if self._has_back_edge[down]:
                self._has_back_edge[down] = False 
                self.add_edge(g, r, up, down, side)
                up = r
                n += 1

            if self.has_pertinent_roots(down):
                md = self._merging_children[down]
                mdex = md[1]
                mdex += md[0]
                md[0].clear()
                down_root = mdex.pop()
                w = self.flip(g, r, up, down, down_root, side)
                
                
                self.add_virtual_edge_passby_down_root(\
                    g, r, up, down, down_root, w, side) # r~w, down~root
                if self._has_back_edge[w]:
                    self._has_back_edge[w] = False 
                    n += 1
                self.delete_separated_child(down, down_root)
                up = r
                down = w
                continue

            if self.is_externally_active(r, down):
                self.add_virtual_edge_to_external_vertex(g, r, up, down, side)
                break

            up, down = self.move(up, down)

        return n


    def ord_for_virtual_node(self, pv):
        assert self.is_virtual_node(pv)
        p = self.g[pv].p
        return self.dfs_ord[p]
    def is_externally_active(self, r, v):
        assert self.is_component_root(r)
        assert not self.is_virtual_node(v)
        ord_r = self.ord_for_virtual_node(r)
        lowpt_v = self.low_pt[v]
        if lowpt_v < ord_r:
            if self.self_low_pt[v] < ord_r:
                return True
            elif self.separated_dfs_child_list[v].lC != None:
                c = self.separated_dfs_child_list[v].lC
                return self.low_pt[c] < ord_r

        return False


    def switch_to(self, a, b1, b2):# a~b1, aXb2 => a~b1, a~b2 on one side
        if self.g[a].fL[-1] == b1:
            self.g[a].fL.append(b2)
        else:
            self.g[a].fR.append(b2)
    def add_edge(self, g, r, up, down, side):
        if side == self.left:
            g[r].fL.append(down)
        else:
            g[r].fR.append(down)
        self.switch_to(down, up, r)
        
    def has_pertinent_roots(self, v):
        assert not self.is_virtual_node(v)
        md = self._merging_children[v]
        return len(md[0])+len(md[1])



    def rank(self, r, v):
        assert self.is_component_root(r)
        assert not self.is_virtual_node(v)
        n = 0
        if self.is_externally_active(r, v):
            n += 3
            if self.has_pertinent_roots(v):
                n -= 1
            if self._has_back_edge[v]:
                n -= 1
        return n
    def flip(self, g, r, up, down, down_root, side):
        s = False
        t = (g[down_root].fL, g[down_root].fR)
        fL = t[side]
        fR = t[1 - side]
        if self.rank(r, fL[-1]) > self.rank(r, fR[-1]):
            fL, fR = fR, fL
            s = not s
        self.add_flip(r, down_root, s)
        return fL[-1]

        
        w = g[down_root].fL  # w ~ up
        _m = g[down_root].fR #_m ~ down_root ~ down
        assert (not self.is_externally_active_component(\
            self.real_vertex(r), down_root)) \
            or self.rank(r, w[-1]) == 2 \
            or self.rank(r, _m[-1]) == 2
        if self.rank(r, w[-1]) > self.rank(r, _m[-1]):
            w, _m = _m, w
        if up == g[down].fL[-1]:
            # up @ down left
            # down_root @ down left
            # down @ down_root right
            # w @ down_root right
            g[down_root].flip = w is not g[down_root].fR
        else:
            g[down_root].flip = w is not g[down_root].fL

        return w[-1]
        

    def add_virtual_edge_passby_down_root(self, g, r, up, down, down_root, w, side):# r~w, down~root
        if side == self.left:
            g[r].fL.append(w)
        else:
            g[r].fR.append(w)
        self.switch_to(w, down_root, r)
        self.switch_to(down, up, down_root)
        self.switch_to(down_root, w, down)
    def add_virtual_edge_to_external_vertex(self, g, r, up, down, side):
        if r == up: return
        self.add_edge(g, r, up, down, side)


    def delete_separated_child(self, v, root):
        assert self.is_separated_dfs_child(root)
        c = _rvirtual_parent(root, self.n)
        self.is_separated[c] = False
        p = self.separated_dfs_child_list[v]
        node = self.separated_dfs_child_list[c]
        if node.sL == None:
            if p != None: p.lC = node.sR
        else:
            L = self.separated_dfs_child_list[node.sL]
            L.sR = node.sR
        if node.sR != None:
            R = self.separated_dfs_child_list[node.sR]
            R.sL = node.sL
        #self.separated_dfs_child_list[c] = None
        self.separated_dfs_child_list[c].sL = None
        self.separated_dfs_child_list[c].sR = None
        # but self.separated_dfs_child_list[c].lC is in use!!!!
        

    def recover_embedding(self, G, g):
        n = G.order()
        self.fill_flip_flag()
        neighbors = self.calc_neighbors(g)
    
        edges = []
        for v, ns in enumerate(neighbors):
            for u in ns:
                edges.append((v,u,len(edges)))

        m = len(edges)
        edges = bucket_sorts(edges, lambda i,e: e[i], [1,0], [n,n])

        G_es = []
        for v in G.vertices():
            for u in G.neighbors(v):
                G_es.append((v,u))
        G_es = bucket_sorts(G_es, lambda i,e: e[i], [1,0], [n,n])

        idx = 0
        ls = []
        for e in G_es:
            for u, v, i in edges[idx:]:
                idx += 1
                if (u, v) == e:
                    ls.append((u,v,i))
                    break
            else:
                raise 'error'
        assert len(ls) == len(G_es)
        edges = bucket_sort(ls, lambda e: e[2], m)
        adjecency_ls = group_to_list(n, edges, lambda e: e[0], lambda e:e[1])

        return adjecency_ls

    def dfs_parent(self, g, v):
        assert not self.is_virtual_node(v)
        return g[g[v].p].p
    def get_edges_for_virtual_vertex_face_parent(self, g, pv):
        assert self.is_virtual_node(pv)
        if self.flip_flag[_rvirtual_parent(pv, self.n)]:
            g[pv].fR.reverse()
            ls = g[pv].fR + g[pv].fL[1:]
        else:
            g[pv].fL.reverse()
            ls = g[pv].fL + g[pv].fR[1:]
        return ls
    def get_edges_for_real_vertex_face_parent(self, g, v):
        assert not self.is_virtual_node(v)
        is_flip = self.flip_flag[v]
        if self.is_dfs_root(v):
            if is_flip:
                g[v].fL.reverse()
                ls = g[v].fR + g[v].fL
            else:
                g[v].fR.reverse()
                ls = g[v].fL + g[v].fR
            return ls
        if is_flip:
            g[v].fL.reverse()
            ls = g[v].fR[1:] + g[v].fL[:-1]
        else:
            g[v].fR.reverse()
            ls = g[v].fL[1:] + g[v].fR[:-1]
        return ls


    def real_vertex(self, pv):
        assert self.is_virtual_node(pv)
        return self.g[pv].p

    def is_dfs_root(self, v):
        return self.g[v].p == v



    def calc_neighbors(self, g):
        for r in self.roots:
            for c in self.dfs_children[r]:
                vc = _virtual_parent(c, self.n)
                g[r].fL.append(vc)
        neighbors = [None]*self.n
        for v in self.dfs_seq:
            ls = self.get_edges_for_real_vertex_face_parent(g, v)
            ns = [self.dfs_parent(g, v)]
            for x in ls:
                assert self.is_virtual_node(x)
                real_vertex = self.real_vertex(x)
                if real_vertex == v: 
                    ns += self.get_edges_for_virtual_vertex_face_parent(g, x) #children
                else:
                    ns.append(real_vertex) # back to ancester
            neighbors[v] = ns
        return neighbors
    


def is_planar_embedding(embedding):
    g = graph(embedding)
    #print('g = {}'.format(g))
    n = g.nv()
    if n < 5: return True

    #assert is_connected(g)
    g = _make_connected(g)
        
    root = 0
    t = DFS_tree(root, g)
    t = t.parent2children()
    t = tuple(tuple(reversed(p2cs)) for p2cs in t)
    t = rooted_tree(root, t)
    #print(t)


    right_hidden = [False]*n
    back_from = [None]*n

    back_edges = list([] for _ in range(n))
    for action, argv in DFS(g):
        if action == enter_tree_edge:
            G, idx, p, v = argv
            back_edges[v].append([])
            
        elif action == exit_tree_edge:
            G, idx, p, v = argv
            back_edges[p].append([])
            
        elif action == visit_back_edge:
            G, idx, p, v = argv
            back_edges[p][-1].append(v)

    def go_up(s):
        if back_from[s] == None:
            s = t.parent(s)
        else:
            s = back_from[s]
        return s

    #print(back_edges)
    for updown, v in t:
        if updown == up_from:
            v = t.parent(v)
        bs = back_edges[v].pop()
        for u in reversed(bs):
            if right_hidden[u]: return False
            s = go_up(v)
            back_from[v] = u
            while s != u:
                if s == root: return False
                '''if right_hidden[s]: return False'''
                right_hidden[s] = True
                
                _s = go_up(s)
                back_from[s] = u
                s = _s

    assert back_edges == list([] for _ in range(n))
    return True

#23333333333333333333333333333333333333333333


_data = [\
    '4 bcd,adc,abd,acb',\
    '6 bcd,aef,afd,ace,bdf,bec',\
    '8 bcd,aef,afg,agh,bhf,bec,chd,dge',\
    '8 bcd,aef,afg,age,bdh,bhc,chd,egf',\
    '10 bcd,aef,afg,ahi,bjf,bec,cjh,dgi,dhj,eig',\
    '10 bcd,aef,afd,acg,bhi,bic,djh,egj,ejf,gih',\
    '10 bcd,aef,agd,ach,bif,beg,cfj,dji,ehj,gih',\
    '10 bcd,aef,afg,agh,bhi,bic,cjd,dje,ejf,gih',\
    '10 bcd,aef,agh,ahe,bdi,bjg,cfj,cid,ehj,fig',\
    '12 bcd,aef,afd,acg,bhi,bjc,djk,ekl,elj,fig,glh,hki',\
    '12 bcd,aef,agh,aij,bkl,blg,cfl,cki,dhj,dik,ejh,egf',\
    '12 bcd,aef,afg,ahi,bjf,bec,ckl,dli,dhj,eik,gjl,gkh',\
    '12 bcd,aef,afg,agh,bij,bjc,chd,dgk,ekl,elf,hli,ikj',\
    '12 bcd,aef,afg,agh,bij,bjc,ckd,dki,ehl,elf,glh,ikj',\
    '12 bcd,aef,agd,ach,bif,bej,cjk,dli,ehl,fkg,gjl,hki',\
    '12 bcd,aef,agd,ach,bij,bjg,cfk,dki,ehl,elf,glh,ikj',\
    '12 bcd,aef,agh,ahe,bdi,bjk,ckl,cid,ehj,fil,flg,gkj',\
    '12 bcd,aef,agh,ahe,bdi,bjg,cfj,ckd,ekl,flg,hli,ikj',\
    '12 bcd,aef,agh,aie,bdj,bkg,cfk,cli,dhl,elk,fjg,hji',\
    '12 bcd,aef,agh,aij,bjk,blg,cfl,cki,dhj,die,ehl,fkg',\
    '12 bcd,aef,agh,aie,bdj,bjg,cfk,cki,dhl,elf,glh,ikj',\
    '14 bcd,aef,agd,ach,bij,bjk,ckh,dgl,emn,enf,flg,hkm,iln,imj',\
    '14 bcd,aef,agd,ach,bij,bjg,cfh,dgk,ekl,emf,hni,inm,jln,kml',\
    '14 bcd,aef,agd,ach,bij,bjg,cfh,dgk,elm,enf,hnl,ikm,iln,jmk',\
    '14 bcd,aef,agd,ach,bij,bkg,cfh,dgl,emn,enk,fjl,hkm,iln,imj',\
    '14 bcd,aef,agd,ach,bif,bej,cjk,dlm,enj,fig,gnl,hkm,hln,imk',\
    '14 bcd,aef,agh,aij,bkl,bmn,cnl,cki,dhj,dik,ejh,egm,fln,fmg',\
    '14 bcd,aef,agd,ach,bif,bej,cjk,dkl,emn,fng,glh,hkm,iln,imj',\
    '14 bcd,aef,agd,ach,bij,bjg,cfk,dkl,emj,eif,gnh,hnm,iln,kml',\
    '14 bcd,aef,afg,ahi,bjf,bec,ckl,dli,dhj,eim,gmn,gnh,jnk,kml',\
    '14 bcd,aef,agh,aij,bkf,beg,cfh,cgl,dmj,dik,ejn,hnm,iln,kml',\
    '14 bcd,aef,afg,ahi,bjk,bkc,clm,dmi,dhn,enk,ejf,gnm,glh,ilj',\
    '14 bcd,aec,abf,afg,bhi,cjd,dkl,eli,ehm,fmn,gnl,gkh,inj,jmk',\
    '14 bcd,aef,afg,agh,bij,bjc,ckd,dkl,emn,enf,glh,hkm,iln,imj',\
    '14 bcd,aef,afg,agh,bij,bjc,ckd,dkl,elm,emf,gnh,hni,inj,kml',\
    '14 bcd,aef,agd,ach,bij,bjg,cfk,dkl,elm,emf,gnh,hni,inj,kml',\
    '14 bcd,aef,afg,ahi,bjk,bgc,cfl,dlm,dmj,ein,enl,gkh,hni,jmk',\
    '14 bcd,aec,abf,agh,bij,cjk,dkh,dgl,elm,emf,fng,hni,inj,kml',\
    '14 bcd,aef,agh,aij,bkf,beg,cfl,cmi,dhj,din,enl,gkm,hln,jmk',\
    '14 bcd,aef,afg,agh,bij,bkc,cld,dmi,ehj,eik,fjn,gnm,hln,kml',\
    '14 bcd,aef,afg,agh,bij,bkc,cld,dli,ehj,eim,fmn,gnh,jnk,kml',\
    '14 bcd,aef,agh,aij,bkl,bmg,cfh,cgi,dhn,dnk,ejl,ekm,fln,imj',\
    '14 bcd,aef,afg,agh,bij,bkc,cld,dmi,ehn,enk,fjl,gkm,hln,imj',\
    '14 bcd,aef,agh,ahe,bdi,bjk,clm,cid,ehj,fin,fnl,gkm,gln,jmk',\
    '14 bcd,aef,agh,aie,bdj,bkl,cmh,cgi,dhj,eik,fjn,fnm,gln,kml',\
    '14 bcd,aef,agh,ahe,bdi,bjk,clm,cid,ehn,fnk,fjl,gkm,gln,imj',\
    '14 bcd,aef,agh,ahe,bdi,bjk,ckl,cid,ehm,fmn,fng,gnm,ilj,jlk',\
    '14 bcd,aef,agh,ahe,bdi,bjg,cfk,cld,elm,fmk,gjn,hni,inj,kml',\
    '14 bcd,aef,agh,aie,bdj,bkg,cfk,clm,dmn,elk,fjg,hjn,hni,iml',\
    '14 bcd,aef,agh,aie,bdj,bkl,clh,cgm,dmn,enk,fjl,fkg,hni,imj',\
    '14 bcd,aef,agh,aij,bjk,blg,cfl,cmi,dhm,dke,ejn,fng,hni,kml',\
    '14 bcd,aef,agh,aij,bkl,bmg,cfh,cgi,dhm,dnk,ejl,ekn,fni,jml',\
    '14 bcd,aef,agh,aij,bjf,bek,ckl,cmi,dhm,dne,flg,gkn,hni,jml',\
    '14 bcd,aef,agh,aie,bdj,bjg,cfk,cli,dhm,emf,gnl,hkn,inj,kml',\
    '14 bcd,aef,agh,aie,bdj,bkg,cfl,cmi,dhn,enk,fjl,gkm,hln,imj',\
    ]


def _test_init_dfs():
    
    import graph_format_ascii_embedding
    _str2embedding = graph_format_ascii_embedding.str2embedding
    import simple_undirected_graph
    _graph = simple_undirected_graph.graph
    res = []
    for s in _data[:]:
        e = _str2embedding(s)
        G = _graph(e)
        e = _init_dfs(G)
        print('dfs_ord = {}\ndfs_seq = {}\nlow_pt = {}\n'\
              'self_low_pt = {}\ntree_edge = {}\nrback_edge = {}\nroots = {}\n'\
              .format(*e))
        input("enter: ")




#_test_init_dfs()

def _t():
    from planar_ordering import make_maximal_planar, planar_ordering, drawing_planar_graphs_on_a_grid
    import graph_format_ascii_embedding
    _str2embedding = graph_format_ascii_embedding.str2embedding
    from DFS import is_biconnected
    import simple_undirected_graph
    _graph = simple_undirected_graph.graph
    from simple_undirected_graph import union, K_n, K_n_m, G_0, G_1, \
         linear_graph, cycle_graph, star_graph, full_k_ary_tree, complete_k_ary_tree

    gx = [K_n(5), K_n_m(3,3), ]
    for G in gx:
        try:
            Boyer_Myrvold_planarity_test(G)
        except NonplanarError: pass
        else:
            print('error: nonplanar graph pass the test')


    
    gs = [G_0(), G_1(), K_n(0), K_n(1), K_n(2), K_n(3), K_n(4), \
          K_n_m(3,1), K_n_m(2,1), K_n_m(3,2), K_n_m(3,0), \
          linear_graph(0), linear_graph(1), linear_graph(2), linear_graph(18), \
          cycle_graph(3), cycle_graph(18), star_graph(1), star_graph(2), star_graph(18),\
          full_k_ary_tree(1, 0), full_k_ary_tree(1, 1), full_k_ary_tree(1, 2), \
          full_k_ary_tree(2, 0), full_k_ary_tree(2, 1), full_k_ary_tree(2, 2), \
          full_k_ary_tree(2, 6), full_k_ary_tree(3, 3), \
          complete_k_ary_tree(1, 1), complete_k_ary_tree(1, 2), complete_k_ary_tree(1, 3), \
          complete_k_ary_tree(2, 1), complete_k_ary_tree(2, 2), complete_k_ary_tree(2, 3), \
          complete_k_ary_tree(2, 4), complete_k_ary_tree(2, 5), complete_k_ary_tree(2, 100), \
          star_graph(1), star_graph(2), star_graph(3), star_graph(100), \
          ]
    
    
    
    for s in _data[:]:
        e = _str2embedding(s)
        gs.append(_graph(e))
    ugs = union(gs)
    gs.append(ugs)
    
    es = []
    for G in gs:
        e = Boyer_Myrvold_planarity_test(G)
        es.append(e)
    es.pop()
    
    res = []
    for i, e in enumerate(es):
        G = gs[i]
        #print(G)
        if G.num_edges() == 0: continue
        if not is_biconnected(G): continue
        me = make_maximal_planar(e)
        #print(me)
        o = planar_ordering(0, me[0][0], me)
        d = drawing_planar_graphs_on_a_grid(me, o)
        res.append((e,me,o,d))

    #return res
    #print(len(res))

    import matplotlib.pyplot as plt
    import networkx as nx
    for e,me,o,d in res:
        gx = nx.Graph
        g = graph(e)
        n = g.order()
        edges = g.edges()
        g = gx()
        g.add_nodes_from(range(n))
        g.add_edges_from(edges)
        pos = {i:p for i, p in enumerate(d)}
        nx.draw(g, pos)
        plt.show()

if __name__ == "__main__":
    e = [(3, 2, 1), (0, 5, 4), (3, 5, 0), (4, 2, 0), (1, 5, 3), (2, 4, 1)]
    assert is_planar_embedding(e)
    _t()







