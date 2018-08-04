'''
graph requirement like graph.py
Orientation preserved

enter_tree_edge(G, edge_idx, parent, v)
exit_tree_edge(G, edge_idx, parent, v)
visit_back_edge(G, edge_idx, curr_node, ancester)
revisit_back_edge(G, edge_idx, curr_node, prev_back_src)
enter_tree(G, root)
exit_tree(G, root)

dir_root(G, root)      #list neighbors and incident_edge_indices, let user to control the orientation
dir_node(G, parent, v) #list neighbors except parent and incident_edge_indices,

roots # they should connecte to all vertices
what_color(G, edge_idx, from, to) - white:tree edge, black:rback_edge, gray:back_edge
what_color_mayroot(G, mayroot) - white:root, black:not a root
'''

from .fake_face import fake_face
from itertools import chain

enter_tree = 0
exit_tree = 1
enter_tree_edge = 2
exit_tree_edge = 3
visit_back_edge = 4
revisit_back_edge = 5

root_parent = -1
init_parent = None
'''
white = 0
gray = -1
black = 1
_idx_edge_idx = 0
_idx_node = 1
_idx_neighbors = 2
_idx_edge_idcs = 3



def _r_dir_root(G, r):
    ns = list(G.neighbors(r))
    ns.reverse()
    es = list(G.incident_edge_indices(r))
    es.reverse()

    assert len(ns) == len(es)
    return ns, es

def _r_dir_node(G, parent, v):
    ns, es =_r_dir_root(G, v)
    #bug: loc = search(ns, parent)
    loc = ns.index(parent)
    def cyclic_shift(ls, loc):
        ls = ls[loc+1:] + ls[:loc] # orientation preserved
        ls.reverse() # pop out
        return ls
    ns = cyclic_shift(ns, loc)
    es = cyclic_shift(es, loc)
    return ns, es



def _reverse(ls):
    ls.reverse()
    return ls


def _color_before_enter_tree_edge(v, color):
    assert color[v] == white
    color[v] = gray
    
def _color_after_exit_tree_edge(v, color):
    assert color[v] == gray
    color[v] = black
    

def _color_before_enter_tree(root, color):
    assert color[root] == white
    color[root] = gray
    
    
def _color_after_exit_tree(root, color):
    assert color[root] == gray
    color[root] = black


class DFS:
    def __init__(self, g, root = None):
        self.roots = None
        self.root = root
        self.g = g
    def __iter__(self):
        G = self.g
        n = G.order()
        root = self.root

        roots = G.vertices()
        if root:
            assert root < n
            roots = itertools.chain([root], roots)
            
        color = [white]*n
        what_color_mayroot = lambda G,r: color[r]
        what_color = lambda G, i, f, t: color[t]
        dir_root = _r_dir_root
        dir_node = _r_dir_node
        color_before_enter_tree_edge = lambda v: _color_before_enter_tree_edge(v, color)
        color_after_exit_tree_edge = lambda v: _color_after_exit_tree_edge(v, color)
        color_before_enter_tree = lambda r: _color_before_enter_tree(r, color)
        color_after_exit_tree = lambda r: _color_after_exit_tree(r, color)
        _roots = []
        for r in roots: 
            if what_color_mayroot(G,r) != white:
                assert what_color_mayroot(G,r) == black
                continue
            _roots.append(r)
            ns, es = dir_root(G, r)
            stack = [(None, r, ns, es)]
            #enter_tree(G, r)
            color_before_enter_tree(r)
            yield enter_tree, (G, r)
            while len(stack) > 0:
                idx, v, ns, es = stack[-1]
                if len(ns) == 0:
                    # exit
                    if len(stack) > 1:
                        p = stack[-2][_idx_node]
                        #exit_tree_edge(G, p, v)
                        yield exit_tree_edge, (G, idx, p, v)
                        color_after_exit_tree_edge(v)
                    else:
                        assert r == v
                        #exit_tree(G, r)
                        yield exit_tree, (G, r)
                        color_after_exit_tree(r)
                    stack.pop()
                    continue

                # downward
                son = ns.pop()
                to_son = es.pop()
                c = what_color(G, to_son, v, son)
                if c == white:
                    son_ns, son_es = dir_node(G, v, son)
                    stack.append((to_son, son, son_ns, son_es))
                    #enter_tree_edge(G, to_son, v, son)
                    color_before_enter_tree_edge(son)
                    yield enter_tree_edge, (G, to_son, v, son)
                elif c == black:
                    #(son, v) should be a visited back edge
                    #graph is undirected, cannot contain forward edges or cross edge
                    #revisit_back_edge(G, to_son, v, son)
                    yield revisit_back_edge, (G, to_son, v, son)
                else:# c == gray
                    #visit_back_edge(G, to_son, v, son)
                    yield visit_back_edge, (G, to_son, v, son)

                

        assert color == [black]*n
        self.roots = _roots


'''


class partial_DFS:
    def __init__(self, g, roots):
        n = g.nv()
        self.graph = g
        self.roots = roots
        self.parent = [init_parent]*n
        self.active_flag = [False]*n
        self.faces = fake_face(g)
        self._reenter_flag = False


    def _color_v(self, p, v):
        assert not self.active_flag[v]
        self.active_flag[v] = True
        assert self.parent[v] == init_parent
        self.parent[v] = p
    def _uncolor_v(self, p, v):
        assert self.active_flag[v]
        self.active_flag[v] = False
        assert self.parent[v] != init_parent
    def _ent_tree(self, r):
        self._color_v(root_parent, r)
    def _ent_edge(self, p, v):
        self._color_v(p, v)
    def _ext_tree(self, r):
        self._uncolor_v(root_parent, r)
    def _ext_edge(self, p, v):
        self._uncolor_v(p, v)
    def _visited(self, v):
        return self.parent[v] != init_parent
    def _back(self, p, v):pass
    def _re_back(self, p, v):pass
        
    def __iter__(self):
        if self._reenter_flag: raise 'forbidden reenter'
        self._reenter_flag = True

        g = self.graph
        n = g.nv()
        rs = self.roots
        
        self.roots = roots = []
        parent = self.parent
        faces = self.faces
        active_flag = self.active_flag

        for r in rs:
            if parent[r] != init_parent: continue
            roots.append(r)

            
            yield enter_tree, (g, r)
            self._ent_tree(r)
            
            if g.degree(r) == 0:
                yield exit_tree, (g, r)
                self._ext_tree(r)
                continue

            de0 = g.dedges(r)[0]
            dedge = de0
            while True:
                p, v = g.dedge2edge(dedge)
                idx = g.to_uedge(dedge)
                if not self._visited(v):
                    yield enter_tree_edge, (g, idx, p, v)
                    self._ent_edge(p, v)
                elif active_flag[v]:
                    if v == parent[p]:
                        p,v = v,p ##v, p#########################
                        yield exit_tree_edge, (g, idx, p, v) 
                        self._ext_edge(p, v)
                    else:
                        yield visit_back_edge, (g, idx, p, v)
                        self._back(p, v)
                        dedge = g.flip_dedge(dedge)
                else:
                    yield revisit_back_edge, (g, idx, p, v)
                    self._re_back(p, v)
                    dedge = g.flip_dedge(dedge)
                dedge = faces.next_dedge(dedge)
                if dedge == de0: break

            yield exit_tree, (g, r)
            self._ext_tree(r)
        self._reenter_flag = False
        self.roots = tuple(roots)
        
def DFS(G, root = None):
    roots = G.vertices()
    if root:
        assert 0 <= root < n
        roots = itertools.chain([root], roots)
    return partial_DFS(G, roots)


def is_connected(G):
    count = 0
    for action, argv in DFS(G):
        if action == enter_tree:
            if count:
                return False
            count = 1
    return True

def is_biconnected(G):
    count = 0
    lowpt = [None]*G.order()
    order = [None]*G.order()
    curr = 0
    for action, argv in DFS(G):
        if action == enter_tree:
            G, r = argv
            if count > 0: return False
            else: count += 1
            lowpt[r] = curr
            order[r] = curr
            curr += 1
    
        elif action == exit_tree:
            G, r = argv
        elif action == enter_tree_edge:
            G, idx, p, v = argv
            lowpt[v] = curr
            order[v] = curr
            curr += 1
        elif action == exit_tree_edge:
            G, idx, p, v = argv
            if lowpt[v] >= order[p]:
                if p != r: return False
                elif count > 1: return False
                else: count += 1
                    
            if lowpt[p] > lowpt[v]:
                lowpt[p] = lowpt[v]
        elif action == visit_back_edge:
            G, idx, p, v = argv
            if lowpt[p] > order[v]:
                lowpt[p] = order[v]
        elif action == revisit_back_edge:
            G, idx, p, v = argv
        else:
            raise 'unknown'

    return True



def DFS_lowpt(G, root = None):
    n = G.order()
    lowpt = [None]*n
    order = [None]*n
    cut_vertices = []
    dfs_forest = [[] for i in range(n)]
    dfs_roots = []
    dfs_parent = [None]*n
    curr = 0
    for action, argv in DFS(G, root):
        if action == enter_tree:
            G, r = argv
            lowpt[r] = curr
            order[r] = curr
            curr += 1
            dfs_roots.append(r)
    
        elif action == exit_tree:
            G, r = argv
            cut_vertices.pop()
        elif action == enter_tree_edge:
            G, idx, p, v = argv
            lowpt[v] = curr
            order[v] = curr
            curr += 1
            dfs_parent[v] = (p, len(dfs_forest[p]))
            dfs_forest[p].append((idx, v))
        elif action == exit_tree_edge:
            G, idx, p, v = argv
            if lowpt[v] >= order[p]:
                cut_vertices.append(p)
            if lowpt[p] > lowpt[v]:
                lowpt[p] = lowpt[v]
        elif action == visit_back_edge:
            G, idx, p, v = argv
            if lowpt[p] > order[v]:
                lowpt[p] = order[v]
        elif action == revisit_back_edge:
            G, idx, p, v = argv
        else:
            raise 'unknown'

    cut_vertices_flag = [False]*n
    for v in cut_vertices: cut_vertices_flag[v] = True
    cut_vertices = (v for v in G.vertices() if cut_vertices_flag[v])
    return lowpt, order, cut_vertices, dfs_roots, dfs_parent, dfs_forest


'''

import bisect
search = bisect.bisect_left

def _null_f(a,b,c=None): return
#_enter_tree_edge = lambda G, parent, v: pass
_enter_tree_edge = _null_f
_exit_tree_edge = _enter_tree_edge
_visit_back_edge = _enter_tree_edge
_revisit_back_edge = _enter_tree_edge
#_enter_tree = lambda G, root: pass
_enter_tree = _null_f
_exit_tree = _enter_tree

def _r_dir_root(G, v):
    ls = list(G.neighbors(v))
    ls.reverse()
    return ls

def _r_dir_node(G, parent, v):
    ls = list(G.neighbors(v))
    #bug: loc = search(ls, parent)
    loc = ls.index(parent)
    ls = ls[loc+1:] + ls[:loc] # orientation preserved
    ls.reverse() # pop out
    return ls

def _reverse(ls):
    ls.reverse()
    return ls


def _color_enter_tree_edge(G, parent, v, color, user_func):
    assert color[v] == white
    color[v] = gray
    user_func(G, parent, v)
    
def _color_exit_tree_edge(G, parent, v, color, user_func):
    assert color[v] == gray
    user_func(G, parent, v)
    color[v] = black
    

def _color_enter_tree(G, root, color, user_func):
    assert color[root] == white
    color[root] = gray
    user_func(G, root)
    
    
def _color_exit_tree(G, root, color, user_func):
    assert color[root] == gray
    user_func(G, root)
    color[root] = black
    

def _DFS(G, \
        enter_tree = None, exit_tree = None,\
        enter_tree_edge = None, exit_tree_edge = None, \
        visit_back_edge = None, revisit_back_edge = None,\
        dir_root = None, dir_node = None, \
        roots = None, what_color = None, what_color_mayroot = None):
    
    if enter_tree_edge == None: enter_tree_edge = _enter_tree_edge
    if exit_tree_edge == None: exit_tree_edge = _exit_tree_edge
    if visit_back_edge == None: visit_back_edge = _visit_back_edge
    if revisit_back_edge == None: revisit_back_edge = _revisit_back_edge
    if enter_tree == None: enter_tree = _enter_tree
    if exit_tree == None: exit_tree = _exit_tree
    
    if dir_root == None:
        dir_root = _r_dir_root
    else:
        dir_root = lambda G, r: _reverse(list(dir_root(G,r)))
    if dir_node == None:
        dir_node = _r_dir_node
    else:
        dir_node = lambda G, p, r: _reverse(list(dir_node(G,p,r)))

    roots = roots
    if roots == None: roots = G.vertices()
    
    n = G.order()
    assert (what_color == None) == (what_color_mayroot == None)
    if what_color == None:
        color = [white]*n
        what_color = lambda G, f, t: color[t]
        what_color_mayroot = lambda G, r: color[r]
        def _f3(f, c, u):
            return lambda G, p, v: f(G, p, v, color, u)
        def _f2(f, c, u):
            return lambda G, v: f(G, v, color, u)

        enter_tree_edge = _f3(_color_enter_tree_edge, color, enter_tree_edge)
        exit_tree_edge = _f3(_color_exit_tree_edge, color, exit_tree_edge)
        enter_tree = _f2(_color_enter_tree, color, enter_tree)
        exit_tree = _f2(_color_exit_tree, color, exit_tree)


    _roots = []
    for r in roots: 
        if what_color_mayroot(G,r) != white:
            assert what_color_mayroot(G,r) == black
            continue
        _roots.append(r)
        stack = [(r, dir_root(G, r))]
        enter_tree(G, r)
        while len(stack) > 0:
            v, ns = stack[-1]
            if len(ns) == 0:
                # exit
                if len(stack) > 1:
                    exit_tree_edge(G, stack[-2][idx_node], v)
                else:
                    exit_tree(G, v)
                stack.pop()
                continue

            # downward
            son = ns.pop()
            c = what_color(G, v, son)
            if c == black:
                # raise 'graph format is unsported'
                #(son, v) should be a visited back edge
                #graph is undirected, cannot contain forward edges or cross edge
                revisit_back_edge(G, v, son)
                continue
            elif c == gray:
                visit_back_edge(G, v, son)
                continue

            son_ns = dir_node(G, v, son)
            stack.append((son, son_ns))
            enter_tree_edge(G, v, son)

    assert color == [black]*n
    return _roots

'''




def _t():
    import simple_undirected_graph
    g = simple_undirected_graph.graph
    def _f(G, p, v=None):print('({}, {})'.format(p, v))

    data = [\
        (10, [(1,2), (3,4), (1,8), (9,5), (6,7), (5,8), (2,5), (9,7)]),\
        ]
    for n, es in data:
        G = g(n, es)
        #DFS(G,_f,lambda G,p:print('end'),_f,_f,_f,_f)
        #for a in DFS(G): print(a)
        depth = 0
        h = '\t'
        for action, argv in DFS(G):
            if action == enter_tree:
                assert depth == 0
                G, r = argv
                print('root {}'.format(r))
            elif action == exit_tree:
                assert depth == 0
                G, r = argv
                print('quit {}'.format(r))
            elif action == enter_tree_edge:
                depth += 1
                G, idx, p, v = argv
                print(h*depth + '{}->{}'.format(p,v))
            elif action == exit_tree_edge:
                G, idx, p, v = argv
                print(h*depth + '{}<-{}'.format(p,v))
                depth -= 1
            elif action == visit_back_edge:
                G, idx, p, v = argv
                print(h*(depth+1) + '{1}<~{0}'.format(p,v))
            elif action == revisit_back_edge:
                G, idx, p, v = argv
                print(h*(depth+1) + '{}~>{}'.format(p,v))
            else:
                raise 'unknown'

            
        
if __name__ == "__main__":
    _t()


