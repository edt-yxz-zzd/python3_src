

'''
show class hierarchy

input:
    [(subclass, bases)]
output:
    class_forest : Forest = [(baseclass, [Forest])]


### output are ordered:
    A
        B
            C
        D
            E
                C

        C
            F
    G
        F
    F

input:
    B(A)
    D(A)
    E(D)
    C(E,B)
    G()
    F(G,C)
NOTE:
    C is under it min ancestor A (not under D)
        A is the finest class s.t.
            each path from DAG source to C must go through A
        F - assume a virtual root for DAG
    the last appear of C is not prec B/D, i.e. its parent
    subclasses (e.g. F) of C was present in the last appear of C
    unordered pair are sorted by input order
'''

from collections import defaultdict
from functools import cmp_to_key


def show_hierarchy(subclass_bases_pairs):
    # input:
    #   subclass_bases_pairs :: [(cls, [cls])]
    #   should be DAG
    # output:
    #   [Tree]
    #   where Tree = (cls, None) | (cls, [Tree])

    clss = [] # preorder2cls
    cls2input_order = {}
    def new_cls(cls):
        clss.append(cls)
        cls2input_order.setdefault(cls, len(clss))

    cls2bases = defaultdict(set)
    for cls, bases in subclass_bases_pairs:
        bases = list(bases)
        bases.reverse()
        for base in bases: new_cls(base)
        new_cls(cls)

        # cls may appear many times
        cls2bases[cls].update(bases)
    all_vertices = set(clss)
    for cls in all_vertices - set(cls2bases):
        cls2bases[cls]
    vtx2parents = dict(cls2bases); del cls2bases
    assert len(vtx2parents) == len(all_vertices)


    #find source
    sources = [vtx for vtx, parents in vtx2parents.items() if not parents]

    #in-DAG to out-DAG
    vtx2children = {v:set() for v in all_vertices}
    for vtx, parents in vtx2parents.items():
        for parent in parents:
            vtx2children[parent].add(vtx)

    topo_ordering = calc_topological_ordering__recur_dfs(sources, vtx2children)
    if len(topo_ordering) < len(vtx2children):
        raise Exception('non-DAG: root strong component')

    # vtx2ancestors include self
    # vtx2descendants not include self
    vtx2ancestors = {}
    vtx2descendants = {}
    for v in topo_ordering:
        parents = vtx2parents[v]
        ancestors = set(parents)
        ancestors.update(*(vtx2ancestors[parent] for parent in parents))
        ancestors.add(v)
        vtx2ancestors[v] = ancestors

    for v in reversed(topo_ordering):
        children = vtx2children[v]
        descendants = set(children)
        descendants.update(*(vtx2descendants[child] for child in children))
        vtx2descendants[v] = descendants


    # parents of v in final result
    #   iff p is in vtx2parents[v] & all(v not in sibling.descendants for sibling in p.children)
    #   and p is not v.last_parent # will removed below
    vtx2final_parents = {}
    for v, parents in vtx2parents.items():
        vtx2final_parents[v] = final_parents = set()
        for parent in parents:
            if all(v not in vtx2descendants[sibling]
                    for sibling in vtx2children[parent]):
                final_parents.add(parent)


    # last_parent of v in final result
    #   iff p is the finest ancestor in intersect(p.ancestors for p in v.final_parents)
    #   v.last_parent may be the virtual DAG root
    vtx2topo_ord = {v:idx for idx, v in enumerate(topo_ordering)}
    virtual_root = object()
    vtx2last_parent = {}
    for v, final_parents in vtx2final_parents.items():
        if not final_parents:
            # v is a source
            last_parent = virtual_root
            pass
        elif len(final_parents) == 1:
            # last_parent of v already in final_parents
            last_parent = final_parents.pop()
            pass
        else:
            common_ancestors = set.intersection(
                *(vtx2ancestors[parent] for parent in final_parents))
            if not common_ancestors:
                last_parent = virtual_root
            else:
                finest = sorted(common_ancestors, key=vtx2topo_ord.__getitem__)[-1]
                last_parent = finest
        vtx2last_parent[v] = last_parent
    pass
    assert len(vtx2last_parent) == len(all_vertices)
    # now we have
    #   vtx2final_parents, vtx2last_parent, virtual_root


    # p in v.final_parents should pointer to a leaf version of v
    # build a forest use big-vtx
    #   Node vtx = (Leaf, vtx) | (NonLeaf, vtx)
    Leaf = 0
    NonLeaf = 1

    final_forest_big_roots = []
    final_forest_big_vtx2children = {(NonLeaf, v): [] for v in all_vertices}
    for vtx, final_parents in vtx2final_parents.items():
        big_vtx = (Leaf, vtx)
        for parent in final_parents:
            big_parent = (NonLeaf, parent)
            final_forest_big_vtx2children[big_parent].append(big_vtx)
    for vtx, last_parent in vtx2last_parent.items():
        big_vtx = (NonLeaf, vtx) # even it has no children!
        if last_parent is virtual_root:
            final_forest_big_roots.append(big_vtx)
        else:
            big_parent = (NonLeaf, last_parent)
            final_forest_big_vtx2children[big_parent].append(big_vtx)
    pass

    # now we have
    #   final_forest_big_roots, final_forest_big_vtx2children
    def cmp_big_vtx(lhs, rhs):
        _, u = lhs
        _, v = rhs
        if u == v:
            raise logic-error # children of any big-vertex can not have duplicate vtx

        # descendant later/bigger
        if u in vtx2descendants[v]:
            # u > v
            return +1
        if v in vtx2descendants[u]:
            # u < v
            return -1
        return cls2input_order[u] - cls2input_order[v]
    key = cmp_to_key(cmp_big_vtx)
    final_forest_big_roots.sort(key=key)
    for big_children in final_forest_big_vtx2children.values():
        big_children.sort(key=key)

    #return final_forest_big_vtx2children, final_forest_big_roots
    def recur_tree_(big_vtx):
        # subtree[big_vtx] -> (vtx, ...)
        # subtree[(Leaf, vtx)] -> (vtx, None)
        # subtree[(NonLeaf, vtx)] -> (vtx, [...])
        case, vtx = big_vtx
        if case == Leaf:
            return (vtx, None)

        big_children = final_forest_big_vtx2children[big_vtx]
        out_children = []
        for big_c in big_children:
            out_children.append(recur_tree_(big_c))
        return (vtx, out_children)
    small_forest = list(map(recur_tree_, final_forest_big_roots))
    return small_forest

def print_output_tree(small_forest):
    # Forest v = [Tree v]
    # Tree v = (v, None) | (v, Forest v)
    def handle_forest(depth, forest):
        for tree in forest:
            handle_tree(depth, tree)
    def handle_tree(depth, tree):
        v, may_forest = tree
        print(' '*(4*depth), v, sep='')
        if may_forest is None:
            return

        forest = may_forest
        handle_forest(depth + 1, forest)
        return
    handle_forest(0, small_forest)
    return


def calc_topological_ordering__recur_dfs(roots, DAG_in_vtx2children):
    #calc topo_ordering
    # input:
    #   roots :: [vtx]
    #   DAG_in_vtx2children :: {vtx:Iter vtx} # DAG
    # output:
    #   [vtx] # [..., parent, ... child, ...]
    vtx2children = DAG_in_vtx2children
    visiting = set()
    visited = set()
    postordering = []
    def recur_dfs_(v):
        # generate postordering

        if v in visiting: raise Exception('non-DAG')
        if v in visited: return

        visiting.add(v)
        for c in vtx2children[v]:
            recur_dfs_(c)
        visiting.remove(v)
        visited.add(v)
        postordering.append(v) # output here
        return
    for v in roots: recur_dfs_(v)
    postordering.reverse(); topo_ordering = postordering; del postordering
    return topo_ordering


def t():
    A,B,C,D,E,F,G = 'ABCDEFG'

    input =\
        [(B,[A])
        ,(D,[A])
        ,(E,[D])
        ,(C,[E,B])
        ,(G,[])
        ,(F,[G,C])
        ]
    output = show_hierarchy(input)
    print_output_tree(output)
    from pprint import pprint
    pprint(output)

if __name__ == '__main__':
    t()

