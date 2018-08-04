
def decompose_to_connected_components(g, roots=None):
    raise should-be-undirected-graph
    topological_ordering = reversed(list(iter_reversed_topological_ordering(g, roots)))
    root2connected_components
    for case, path in dfs(g, topological_ordering):raise
        
def decompose_to_strong_connected_components(g, roots=None):
    'return [[vertex]]'
    num2vtx = []
    vtx2num = g.make_vertex_map()
    vtx2low_num = g.make_vertex_map()
    components = []
    new_components = []

    def _exit():
        _from, (_to, _) = path
        vtx2low_num[_to] = min(vtx2low_num[_from], vtx2low_num[_to])
    for case, path in dfs(g, roots):
        if case == ENTER:
            n = len(num2vtx)
            v = path[0]
            num2vtx.append(v)
            vtx2num[v] = n
            vtx2low_num[v] = n
        elif case == EXIT:
            me = path[0]
            new_components.append(me)
            
            me_low = vtx2low_num[me]
            if me_low == vtx2num[me]:
                # a new complete scc
                components.append(new_components)
                new_components = []
                continue
            
            assert path[1] # cannot be root
            _exit()
        elif case == BACK:
            _exit()
            

    assert sum(map(len, components)) == g.num_vertices()
    assert all(components)
    return components

















            
