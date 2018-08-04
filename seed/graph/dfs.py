
__all__ = '''
    dfs
    ENTER
    EXIT
    BACK
    CROSS_OR_FORWARD
    
'''.split()



# dfs cases
from seed.cases.ENUM import ENTER, EXIT, BACK, CROSS_OR_FORWARD

def dfs(g, roots=None):
    '''yield (Case, Path)

output iterator about (Case, Path):
    Case = ENTER | EXIT | BACK | CROSS_OR_FORWARD
    Path = LeftwardList v = (v, LeftwardList v) | ()
        (curr_vtx, (parent, ...(root, ())...))

    if case == ENTER/EXIT:
        path == (fresh_vtx, ...)
    if case == BACK:
        path == (curr_vtx, ... curr_vtx ...)
    if case == CROSS_OR_FORWARD:
        path == (visited_vtx, ...)


input:
    graph g requirements:
        .iter_vertices()
        .make_vertex_map()
        .iter_neighbors(v)
    roots:
        default = g.iter_vertices()
        if provided:
            only descendants of roots will be visited
        
'''
    if roots is None:
        roots = g.iter_vertices()

    # 3 colors:
    #    unvisited : v not in processed
    #    visiting  : processed2is_ancestor[v]
    #    visited   : not processed2is_ancestor[v]
    processed = processed2is_ancestor = g.make_vertex_map()
    stack = [] # stack of remain neighors
    path = ()  # output leftward list, (me, ...(root, ()))
    
    def enter(v):
        nonlocal path
        if v in processed2is_ancestor:
            raise logic-error
        processed2is_ancestor[v] = True
        path = (v, path)
        stack.append(g.iter_neighbors(v))
    def exit():
        nonlocal path
        stack.pop()
        v, path = path
        processed2is_ancestor[v] = False

        
    for root in roots:
        if root in processed:
            continue
        
        enter(root) # enter before yield
        yield ENTER, path
        while stack:
            for v in stack[-1]:
                break
            else:
                yield EXIT, path
                exit() # exit after yield
                continue
            
            if v not in processed:
                enter(v)
                yield ENTER, path
                continue

            path = v, path # enter
            if processed2is_ancestor[v]:
                yield BACK, path
            else:
                yield CROSS_OR_FORWARD, path
            v, path = path # exit

















