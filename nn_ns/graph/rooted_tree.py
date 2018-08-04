
from .simple_undirected_graph import graph
from .DFS import DFS_lowpt
from .bucket_sort import bucket_sorts



def is_vaild_parent_list(root, parent):
    r = _is_vaild_parent_list(root, parent)
    roots, to_root = search_parent(parent)
    r2 = len(roots) == 1 and parent[roots[0]] == None
    assert r == r2
    return r
    
def search_parent(parent): # list of int or None
    n = len(parent)
    to_root = down_to = [None]*n
    roots = []
    for v in range(n):
        if to_root[v] != None: continue
        p = v
        stack = []
        while p != None:
            if to_root[p] == None:
                # going up
                down_to[p] = v
                stack.append(p)
                p = parent[p]
            elif to_root[p] == v:
                # root circle
                idx = stack.index(p)
                root = min(stack[idx:])
                roots.append(root)
                break
            else:
                # this is a branch
                root = to_root[p]
                break
        else:
            # root
            root = stack[-1]
            roots.append(root)
        for v in stack:
            to_root[v] = root
    
    return roots, to_root

def parent2components(parent):
    n = len(parent)
    roots, to_root = search_parent(parent)
    #print(parent, roots, to_root)

    root2idx = [None] * n
    for i, root in enumerate(roots):
        root2idx[root] = i
        
    tree_vtc_ls = [[r] for r in roots]
    for v, root in enumerate(to_root):
        if root == None or root == v: # v or None ?? fixed it!!
            #v is root
            i = root2idx[v]
            assert i != None
            assert v == tree_vtc_ls[i][0]
            continue
        
        i = root2idx[root]
        vtc = tree_vtc_ls[i]

        vtc.append(v)

    return tree_vtc_ls
    
    
    
def _is_vaild_parent_list(root, parent):
    n = len(parent)
    if parent[root] != None: return False
    flag = [0]*n
    count = 0
    for v, p in enumerate(parent):
        if flag[v]: continue
        count += 1
        flag[v] = count
        tmp = v
        while p != v:
            if p == None:
                if tmp != root:
                    return False
                break
            if flag[p]:
                if flag[p] == flag[v]:
                    return False
                break
            flag[p] = flag[v]
            tmp = p
            p = parent[p]
        else:
            return False

    return True
    

def _make_rooted_tree_from_parent(parent):
    n = len(parent)
    to_son = tuple([] for i in range(n))
    root = None
    for v, p in enumerate(parent):
        if p == None:
            assert None == root
            root = v
        else:
            to_son[p].append(v)
    assert root != None and 0 <= root < n
    assert is_vaild_parent_list(root, parent)
    return _make_rooted_tree(root, to_son)

def _make_rooted_tree(root, parent2children):
    parent2children = tuple(tuple(children) for children in parent2children)
    n = len(parent2children)
    assert n >= 1
    assert 0 <= root < n

    parent = [None]*n
    location = [None]*n
    next_sibling = [None]*n
    v, son_loc = root, 0
    end = root, len(parent2children[root])
    pre_sibling = root
    while (v, son_loc) != end:
        if len(parent2children[v]) == son_loc:
            pre_sibling = v
            v, son_loc = parent[v], location[v]+1
            continue
        son = parent2children[v][son_loc]
        assert parent[son] == None
        parent[son] = v
        location[son] = son_loc
        next_sibling[pre_sibling] = son
        v, son_loc = son, 0
        pre_sibling = root
    next_sibling[root] = None

    edge_sons = []
    for v, p in enumerate(parent):
        assert (v == root) ^ (p != None)
        if v == root: continue
        son = v
        if v > p:
            v, p = p, v
        edge_sons.append((v, p, son))

    edge_sons = bucket_sorts(edge_sons, lambda i,e:e[i], (1,0), (n,n))
    vtx2dedge = [None]*n
    edges = []
    for uedge, (u, v, son) in enumerate(edge_sons):
        edges.append((u,v))
        if u == son:
            vtx2dedge[son] = uedge
        else:
            vtx2dedge[son] = uedge + n
    vtx2dedge = tuple(vtx2dedge)
    edges = tuple(edges)
    dedge2edge = tuple((v,u) for u,v in edges)
    dedge2edge = edges + dedge2edge

    return n, root, parent2children, \
           tuple(parent), tuple(location), tuple(next_sibling), \
           vtx2dedge, edges, dedge2edge
        
def _make_rooted_tree_from_edges(n, root, edges):
    assert root < n == len(edges) + 1
    g = graph(n, edges)
    to_sons = _nontree_graph2tree_ad_ls(root, g)
    return _make_rooted_tree(root, to_sons)
    



def _nontree_graph2tree_ad_ls(root, G):
    lowpt, order, cut_vertices, dfs_roots, dfs_parent, dfs_forest = DFS_lowpt(G, root)
    assert len(dfs_roots) == 1 and dfs_roots[0] == root
    to_sons = tuple(tuple(v for idx, v in sons) for sons in dfs_forest)
    return to_sons


def DFS_tree(root, G):
    to_sons = _nontree_graph2tree_ad_ls(root, G)
    return rooted_tree(root, to_sons)


up_from = 0
down_to = 1
class rooted_tree:
    #def __init__(parent):
    #def __init__(root, parent2children):
    #def __init__(n, root, edges):
    
    def __init__(self, root, parent2children = None, edges = None):
        if edges == None:
            if parent2children == None:
                parent = root
                t = _make_rooted_tree_from_parent(parent)
            else:
                t = _make_rooted_tree(root, parent2children)
        else:
            n, root, edges = root, parent2children, edges
            t = _make_rooted_tree_from_edges(n, root, edges)

        self._n, self._root, self._parent2children, \
                 self._parent, self._location, self._next_sibling, \
                 self._vtx2dedge, self._edges, self._dedge2edge = t
        self._hash = hash((self._root, self._parent2children))

    def root(self): return self._root
    def order(self): return self._n
    def parent2children(self): return self._parent2children
    def children(self, v): return self._parent2children[v]
    def child(self, v, loc): return self._parent2children[v][loc]
    def parent(self, v): return self._parent[v]
    def location(self, v): return self._location[v]
    def next_sibling(self, v): return self._next_sibling[v]
    def num_children(self, v): return len(self._parent2children[v])
    def num_edges(self): return self.nv() - 1
    def __repr__(self):
        return 'rooted_tree({}, {})'.format(self.root(), self.parent2children())
    def __hash__(self): return self._hash
    def __eq__(self, other):
        return (self.root(), self.parent2children()) == \
               (other.root(), other.parent2children())
    def __ne__(self, other): return not (self == other)
    def uedge2edge(self, uedge = None):
        if uedge == None: return self._edges
        return self._edges[uedge]
    def dedge2edge(self, dedge = None):
        if dedge == None: return self._dedge2edge
        return self._dedge2edge[dedge]
    def vtx2up_dedge(self, vtx = None):
        if vtx == None: return self._vtx2dedge
        return self._vtx2dedge[vtx]
    
    nc = num_children
    nv = order
    ne = num_edges


    
    def __iter__(self):
        root = self.root()
        return self(root)


    def __call__(self, subtree_root):
        root = subtree_root
        v, son_loc = root, 0
        end = root, self.nc(root)
        pre_sibling = root
        while (v, son_loc) != end:
            if self.nc(v) == son_loc:
                yield up_from, v
                v, son_loc = self.parent(v), self.location(v)+1
                continue
            son = self.child(v, son_loc)
            v, son_loc = son, 0
            yield down_to, v


def _test_rooted_tree():
    ps = [\
        [2,4,6,1,6,    3,12,5,7,2,  3,4,None],\
        [3,5,1,None,3,  4,9,2,6,2,  7,1],\
        ]
    ans = [\
            [\
                (1, 6), (1, 2), (1, 0), (0, 0), \
                (1, 9), (0, 9), (0, 2), \
                (1, 4), (1, 1), (1, 3), (1, 5), (1, 7), (1, 8), \
                (0, 8), (0, 7), (0, 5), \
                (1, 10), (0, 10), (0, 3), (0, 1), \
                (1, 11), (0, 11), (0, 4), (0, 6)],\
            [\
                (1, 0), (0, 0), \
                (1, 4), (1, 5), (1, 1), (1, 2), (1, 7), (1, 10), \
                (0, 10), (0, 7), \
                (1, 9), (1, 6), (1, 8), (0, 8), (0, 6), (0, 9), (0, 2), \
                (1, 11), (0, 11), (0, 1), (0, 5), (0, 4)],\
        ]
    for p, a in zip(ps, ans):
        tree = rooted_tree(p)
        t = list(tree)
        s = list(tree(tree.root()))
        assert t == a == s

if __name__ == "__main__":
    _test_rooted_tree()

