
'''wrapper for nauty. keyword: isomorphism, canonize, graph.

nauty (no automorphisms, yes?) is a set of procedures for determining the
automorphism group of a vertex-coloured graph. It provides this information
in the form of a set of generators, the size of the group, and the orbits
of the group. It is also able to produce a canonically-labelled isomorph of
the graph, to assist in isomorphism testing.


NOTE: can't not re-entrance!
1) it seems nauty use global valuables.
2) since the callback can't hold data and nauty can't be cancelled by callback
and I don't know wether safe to throw exception or longjmp to stop it, we have
to store the py-exception info to some a global valuable to prevent successive
calls to python if py-exception occured.

TAKE CARE when using 'userautomproc' or using multi-threads.

term:
    n                   - graph order, nauty require: n > 0
    v, u, vtx           - vertex, 0 <= v < n
    vtc, vtcs           - vertices
    ns, neighbors       - neighbors of some a vertex, or
                          end-vtcs of out-edges in directed-graph
    ne, nde, num_edges  - number of edges; nonloop nondirected edges count twice.
    g,v2neighbors,graph - a py graph
    dg, digraph         - directed graph
    cg, cpacked_graph          - a c graph
    dcg                 - directed c graph
    cpacked_graph       - c graph in packed form, adjacency matrix;
                          one bit to represent whether two vtcs're connected
    csparse_graph       - c graph in sparse form, 
    rng                 - range = (begin, end) 0 <= begin <= end
    directed            - flag to indicate whether the graph is a digraph
    setword             - c unsigned-int-type
    WORDSIZE            - bit length of setword = 8*sizeof(setword)
    set                 - a row in adjacency matrix = setword[m]
    m                   - number of setword per row = (WORDSIZE-1+n) //WORDSIZE



data-struct:
    py graph            - list of list of int = list of neighors
    cpacked_graph       - (n, adjacency-matrix);
                          not allow multiedges; 1-loop is ok.
    adjacency-matrix    - array('setword') of length n*m at least;
                          edge (v->u) can be set by:
                          M[v*m + u//WORDSIZE] |= 1<<(WORDSIZE-1-u%WORDSIZE)
    csparse_graph       - (cout_neighbors, v2neighbor_rng)
    cout_neighbors      - array('c int') of length num_edges at least
    v2neighbor_rng      - list of rng; let (begin,end) = v2neighbor_rng[v],
                          then cout_neighbors[begin:end] are neighbors of v
    coloring            - list of list of vertex;
                          vertices with same color were grouped together.
    canon_vtx2old_vtx   - list of original graph vertex;the indices of this
                          list are vertices of the canonical graph
    leveled_partition   - may contain NAUTY_INFINITY
    orbits              - orbits of the automorphism group


function:
    graph -> cgraph
        graph2cpacked_graph
        multi_graph2csparse_graph
    cgraph -> graph
        graph2cpacked_graph
        multi_graph2csparse_graph
    
    call nauty using py-graph
        nauty_packed
        nauty_sparse
    call nauty using c-graph
        cnauty_packed
        cnauty_sparse
'''
import array, itertools, collections
import call_cnauty


#from sys import byteorder 

CHAR_BIT = 8
c_CHAR_BIT = call_cnauty.get_CHAR_BIT()
c_INT_BIT = call_cnauty.get_INT_BIT()
nauty_WORDSIZE = call_cnauty.get_nauty_WORDSIZE()
nauty_VERSION_ID = call_cnauty.get_NAUTYVERSIONID()
nauty_INFINITY = call_cnauty.get_NAUTY_INFINITY()

WORDSIZE2WORD_FMT = {16: '=H', 32:'=I', 64:'=Q'}
INT_BIT2INT_FMT = {16: '=h', 32:'=i', 64:'=q'}
WORD_FMT = WORDSIZE2WORD_FMT[nauty_WORDSIZE]
INT_FMT = INT_BIT2INT_FMT[nauty_INT_BIT]
py_INT_FMT = 'i'
py_WORD_FMT = 'I'

INT_ARRAY = array.array(py_INT_FMT)     # for int[]
GRAPH = array.array(py_WORD_FMT)         # setword[][]
SETWORD_ARRAY = array.array(py_WORD_FMT) # for setword[]
if INT_ARRAY.itemsize * CHAR_BIT != c_INT_BIT:
    raise TypeError('INT_ARRAY.itemsize * CHAR_BIT != c_INT_BIT')
if CHAR_BIT != c_CHAR_BIT:
    raise TypeError('CHAR_BIT != c_CHAR_BIT')
if SETWORD_ARRAY.itemsize * CHAR_BIT != nauty_WORDSIZE:
    raise TypeError('SETWORD_ARRAY.itemsize * CHAR_BIT != nauty_WORDSIZE')


INT_ARRAY_t = type(INT_ARRAY)
GRAPH_t = type(GRAPH)
SETWORD_ARRAY_t = type(SETWORD_ARRAY)

INT_ARRAY_new = lambda *args: INT_ARRAY_t(INT_ARRAY.typecode, *args)
GRAPH_new = lambda *args: GRAPH_t(GRAPH.typecode, *args)
SETWORD_ARRAY_new = GRAPH_new

def is_of_same_arraytype(obj, array_obj):
    return isinstance(obj, type(array_obj)) and obj.typecode == array_obj.typecode
def is_cpacked_graph(obj):
    return is_of_same_arraytype(obj, GRAPH)
def is_cvertices(obj):
    return is_of_same_arraytype(obj, INT_ARRAY)


WORDSIZE = CHAR_BIT * GRAPH.itemsize # bitsizeof int
m_from_n = lambda n: (WORDSIZE-1+n)//WORDSIZE
WORKSIZE_SCALE = 600 # this value in dreadnaut is 120; recommended > 50
packed_form_cpacked_graph_size_from_n = lambda n: n*m_from_n(n)*WORDSIZE//8
pyarray_size_from_n = lambda n: n*m_from_n(n)







_masks = [1 << (WORDSIZE-1 - i) for i in range(WORDSIZE)]
def _ls2row(n, m, vtx, neighbors):
    row = [0] * m
    for v in neighbors:
        assert 0 <= v < n
        assert v != vtx
        i, j = divmod(v, WORDSIZE)
        assert 0 <= i < m
        assert not row[i] & _masks[j]
        row[i] |= _masks[j]
    return row


def check_nonzero_graph_order(v2neighbors):
    if not len(v2neighbors):
        raise ValueError('empty graph')
    return True

def check_nonzero_cpacked_graph_order(n):
    if n <= 0:
        raise ValueError('empty graph')
    return True


def check_multi_digraph(v2neighbors):
    n = len(v2neighbors)
    for v, neighbors in enumerate(v2neighbors):
        if not all(0 <= u < n for u in neighbors):
            raise ValueError('out vertex range: not all(0 <= u < n for u in neighbors)')
        
    return True

def check_simple_digraph_oneloop(v2neighbors):
    check_multi_digraph(v2neighbors)
    for neighbors in v2neighbors:
        if not len(set(neighbors)) == len(neighbors):
            raise ValueError('not allowed: multi-edges')
        
    return True
        

def check_graph_symmetry(v2neighbors):
    edges = set()
    for v, neighbors in enumerate(v2neighbors):
        for u in neighbors:
            if v == u:
                continue
            edge = tuple(sorted([v, u]))
            if edge in edges:
                edges.remove(edge)
            else:
                edges.add(edge)
    if edges:
        raise ValueError('not symmetry: {}'.format(edges.pop()))
    return True


def check_multi_graph(v2neighbors, directed=False):
    check_multi_digraph(v2neighbors)
    if directed:
        return True
    return check_graph_symmetry(v2neighbors)
def check_simple_graph_oneloop(v2neighbors, directed=False):
    check_simple_digraph_oneloop(v2neighbors)
    if directed:
        return True
    return check_graph_symmetry(v2neighbors)



def graph2cpacked_graph(v2neighbors, directed=False):
    cg = _graph2cpacked_graph(v2neighbors, directed)
    g = cpacked_graph2graph(len(v2neighbors), cg, directed)
    cg2 = _graph2cpacked_graph(g, directed)
    assert cg == cg2
    return cg

def _graph2cpacked_graph(v2neighbors, directed=False):
    check_simple_graph_oneloop(v2neighbors, directed)
    cg = digraph2cpacked_graph(v2neighbors)
    return cg
    
def cpacked_graph2graph(n, cpacked_graph, directed=False):
    v2neighbors = cpacked_graph2digraph(n, cpacked_graph)
    check_simple_graph_oneloop(v2neighbors, directed)
    return v2neighbors
    
def digraph2cpacked_graph(v2neighbors):
    check_simple_digraph_oneloop(v2neighbors)
    g = v2neighbors
    n = order = len(g)
    assert n

    m = m_from_n(n)
    cpacked_graph = GRAPH_new()
    for v, ns in enumerate(v2neighbors):
        row = _ls2row(n, m, v, ns)
        cpacked_graph.extend(row)

##    if sys.byteorder == 'little':
##        cpacked_graph.byteswap()
        
    return cpacked_graph

def cpacked_graph2digraph(n, cpacked_graph):
    begin, end = get_rng_of_cpacked_graph(n, cpacked_graph)
    m = m_from_n(n)
    assert begin + m * n == end

##    if sys.byteorder == 'little':
##        cpacked_graph.byteswap()
    try:
        v2neighbors = [
            [col for col in range(n)
                     if cpacked_graph[begin+m*row + col//WORDSIZE] & \
                          _masks[col%WORDSIZE]]
            for row in range(n)]
        check_simple_digraph_oneloop(v2neighbors)
        return v2neighbors
    finally:
##        if sys.byteorder == 'little':
##            cpacked_graph.byteswap()
        pass
    





def get_info_of_csparse_graph(cout_neighbors, v2neighbor_rng):
    rng, begins, ends, sizes = get_info_of_v2neighbor_rng(v2neighbor_rng)
    check_cout_neighbors(cout_neighbors, rng, begins, ends)
    n = len(begins)
    assert len(begins) == len(ends) == len(sizes)
    return n, rng, begins, ends, sizes


def multi_digraph2csparse_graph(v2neighbors):
    check_multi_digraph(v2neighbors)
    n = len(v2neighbors)
    sizes = [0]
    sizes.extend(itertools.accumulate(len(ns) for ns in v2neighbors))
    v2neighbor_rng = tuple(zip(sizes[:-1], sizes[1:]))
    assert n == len(sizes) - 1 == len(v2neighbor_rng)
    
    cout_neighbors = INT_ARRAY_new(itertools.chain.from_iterable(v2neighbors))
    nedges = len(cout_neighbors)
    assert nedges == sum(map(len, v2neighbors), 0)
    assert n == 0 or nedges == v2neighbor_rng[-1][-1]
    return cout_neighbors, v2neighbor_rng

def csparse_graph2multi_digraph(cout_neighbors, v2neighbor_rng):
    n, rng, begins, ends, sizes = get_info_of_csparse_graph(cout_neighbors, v2neighbor_rng)
    nedges = sum(sizes, 0)
    assert nedges <= len(cout_neighbors)
    v2neighbors = [list(cout_neighbors[begin, end]) for begin, end in zip(begins, ends)]
    check_multi_digraph(v2neighbors)
    return v2neighbors

        
def multi_graph2csparse_graph(v2neighbors, directed=False):
    check_multi_graph(v2neighbors, directed)
    return multi_digraph2csparse_graph(v2neighbors)
def csparse_graph2multi_graph(cout_neighbors, v2neighbor_rng, directed=False):
    v2neighbors = csparse_graph2multi_digraph(cout_neighbors, v2neighbor_rng)
    check_multi_graph(v2neighbors, directed)
    return v2neighbors

    



def nauty_packed(graph, coloring = None, userautomproc=None, directed = False):
    '''wrapper for nauty_packed. using packed form graph.

args:
    graph is a simple graph.
        no multi-edges are allowed. (1-loop is fine)
        struct of graph is vertex2neighbors, that is list of list of int.
        n = order(graph) == len(graph)
        assert all(0 <= vtx < n for neighbors in graph for vtx in neighbors)

    coloring is groups of vertices with same color.
        struct of coloring is list of list of int.
        assert set(range(n)) == set(vtcs for vtcs in coloring)

    userautomproc -> void (dict);

requirement:
    since the underlying c library not allow re-entrance,
    so raise RuntimeError if more than one call at same time.

    memory used ~n*n/8 (Byte)
    n = 100000 ~ 1192.5 MB
'''
    n, cpacked_graph = len(graph), graph2cpacked_graph(graph, directed)
    
    return cnauty_packed(n, cpacked_graph, coloring, userautomproc, directed)

def nauty_sparse(graph, coloring = None, userautomproc=None, directed = False):
    '''like nauty_packed, but underlying graph using sparse form

args:
    graph is a multi-edges graph.
        struct of graph is vertex2neighbors, that is list of list of int.
        n = order(graph) == len(graph)
        assert all(0 <= vtx < n for neighbors in graph for vtx in neighbors)

    coloring is groups of vertices with same color.
        struct of coloring is list of list of int.
        assert set(range(n)) == set(vtcs for vtcs in coloring)

    userautomproc -> void (dict);

requirement:
    since the underlying c library not allow re-entrance,
    so raise RuntimeError if more than one call at same time.

    memory used ~(2*n + num_edges)*sizeof(int) (Byte)
    
'''

    cout_neighbors, v2neighbor_rng = multi_graph2csparse_graph(graph, directed)
    
    return cnauty_sparse(cout_neighbors, v2neighbor_rng, coloring, userautomproc, directed)



# userautomproc (count , perm , orbits , numorbits , stabvertex , n )


def get_rng_of_cpacked_graph(n, cpacked_graph, offset = 0):
    
    if not n >= 1: # required by nauty.c !!!
        raise ValueError('not n >= 1')
    if not is_cpacked_graph(cpacked_graph):
        raise ValueError('not is_cpacked_graph(cpacked_graph)')
    if not offset >= 0:
        raise ValueError('not offset >= 1')

    L = pyarray_size_from_n(n)
    if not L + offset <= len(cpacked_graph):
        raise ValueError('not pyarray_size_from_n(n) <= len(cpacked_graph)')

    return offset, offset + L

def get_info_of_v2neighbor_rng(v2neighbor_rng):
    v2neighbor_rng = list(v2neighbor_rng)
    
    n = len(v2neighbor_rng)
    if not n > 0:
        raise ValueError('not n > 0')
    if not all(len(rng) == 2 for rng in v2neighbor_rng):
        raise ValueError('not all(len(rng) == 2 for rng in v2neighbor_rng)')
    begins = [rng[0] for rng in v2neighbor_rng]
    ends = [rng[1] for rng in v2neighbor_rng]
    begin = min(begins)
    end = max(ends)
    if not 0 <= begin <= end:
        raise ValueError('not 0 <= begin <= end')

    sizes = [end-begin for begin, end in zip(begins, ends)]
    if not min(sizes) >= 0:
        raise ValueError('not min(size) >= 0')

    v2neighbor_rng.sort()
    for rng0, rng1 in zip(v2neighbor_rng[:-1], v2neighbor_rng[1:]):
        assert rng0[0] <= rng1[0]
        if not rng0[1] <= rng1[0]:
            raise ValueError('rng overlap')

    return (begin, end), begins, ends, sizes
    
def check_cout_neighbors(cout_neighbors, rng, begins, ends):
    begin, end = rng
    n = len(begins)
    
    if not is_cvertices(cout_neighbors):
        raise ValueError('not is_cvertices(cout_neighbors)')
    if not 0 <= begin <= end <= len(cout_neighbors):
        raise ValueError('not 0 <= begin <= end <= len(cout_neighbors)')
    for begin, end in zip(begins, ends):
        for i in range(begin, end):
            if not 0 <= cout_neighbors[i] < n:
                raise ValueError('not 0 <= cout_neighbors[i] < n')
    return True
    

def bytes_as_int_ls(bs):
    ls = INT_ARRAY_new()
    ls.frombytes(bs)
    return list(ls)

def userautomproc_wrapper(userautomproc):
    def wrapper(d):
        assert len(d) == 6
        for k in ['perm', 'orbits']:
            d[k] = bytes_as_int_ls(d[k])
        userautomproc(d)
        return None
    return wrapper

def _cnauty_args_init(n, coloring, userautomproc):
    if coloring is None:
        coloring = [list(range(n))]
    if userautomproc is not None:
        if not callable(userautomproc):
            raise ValueError('userautomproc not callable')
        userautomproc = userautomproc_wrapper(userautomproc)
    return coloring, userautomproc

def _cnauty_coloring2lab_ptn(n, coloring):

    # vtc may be []
    lab = INT_ARRAY_new(v for vtc in coloring for v in vtc)
    if not list(range(n)) == sorted(lab):
        raise ValueError('bad coloring')
    
    ptn = INT_ARRAY_new(1 for _ in range(n))
    _s = set(itertools.accumulate(len(vtc) for vtc in coloring))
    _s.discard(0)
    for i in _s:
        ptn[i-1] = 0
    del i, _s
    return lab, ptn
def _cnauty_n2other_args(n):
    # set m, worksize
    m = m_from_n(n)
    worksize = WORKSIZE_SCALE * m

    # init workspace buf
    workspace = SETWORD_ARRAY_new(0 for _ in range(worksize))

    # init orbits buf
    orbits = INT_ARRAY_new(3000 for _ in range(n))

    return m, worksize, workspace, orbits

def _cnauty_args_init2(n, coloring, userautomproc):
    coloring, userautomproc = _cnauty_args_init(n, coloring, userautomproc)
    
    # labels, partition
    lab, ptn = _cnauty_coloring2lab_ptn(n, coloring)
    m, worksize, workspace, orbits = _cnauty_n2other_args(n)
    return coloring, userautomproc, lab, ptn, m, worksize, workspace, orbits
    

def _cnauty_results(errstatus, lab, ptn, orbits):
    if errstatus:
        raise RuntimeError('nauty stats.errstatus != 0: {!r}'.format(errstatus))
    

    #orbits = list(orbits)
    d = collections.defaultdict(list)
    for i, orbit_idx in enumerate(orbits):
        d[orbit_idx].append(i)
    orbits = list(d[key] for key in sorted(d.keys()))

    #assert all(not c for c in ptn)
    canon_vtx2old_vtx = tuple(lab)
    leveled_partition = tuple(ptn)
    
    return canon_vtx2old_vtx, leveled_partition, orbits


def cnauty_sparse(cout_neighbors, v2neighbor_rng,
                  coloring = None, userautomproc=None, directed = False):
    check_nonzero_cpacked_graph_order(len(v2neighbor_rng))
    directed = bool(directed)
    
    n, rng, begins, ends, sizes = get_info_of_csparse_graph(cout_neighbors, v2neighbor_rng)
    coloring, userautomproc, lab, ptn, m, worksize, workspace, orbits\
          = _cnauty_args_init2(n, coloring, userautomproc)

    nv = n
    nde = sum(sizes, 0)  # undirected-edge count twice except loop count 1
    begins = INT_ARRAY_new(begins)  # int* v
    sizes = INT_ARRAY_new(sizes)    # int* d
    cout_neighbors = cout_neighbors # int* e
    if len(cout_neighbors) < nde:
        raise ValueError('len(cout_neighbors) < nde')
    
    errstatus = call_cnauty.call_cnauty_sparse(
        nv, nde, begins, sizes, cout_neighbors,
        lab, ptn, workspace, orbits, userautomproc, directed,
        m, WORDSIZE # just for checking
        )
    return _cnauty_results(errstatus, lab, ptn, orbits)
    
    
def cnauty_packed(n, cpacked_graph,
                  coloring = None, userautomproc=None, directed = False):
    check_nonzero_cpacked_graph_order(n)
    directed = bool(directed)
    begin, end = get_rng_of_cpacked_graph(n, cpacked_graph) # check args inside, not nonmeaning
    coloring, userautomproc, lab, ptn, m, worksize, workspace, orbits\
          = _cnauty_args_init2(n, coloring, userautomproc)
    

##    if byteorder == 'little':
##        lab.byteswap()
##        ptn.byteswap()
    errstatus = call_cnauty.call_cnauty_packed(
                n, cpacked_graph, lab, ptn, workspace, orbits,
                userautomproc, directed,
                m, WORDSIZE # just for checking
                )
##    if byteorder == 'little':
##        lab.byteswap()
##        ptn.byteswap()
##        orbits.byteswap()
    return _cnauty_results(errstatus, lab, ptn, orbits)
    

def to_old_vtx2canon_vtx(canon_vtx2old_vtx):
    ls = [None]*len(canon_vtx2old_vtx)
    for new_v, old_v in enumerate(canon_vtx2old_vtx):
        ls[old_v] = new_v
    return ls

def to_canonical_graph(v2neighbors, canon_vtx2old_vtx):
    n = len(v2neighbors)
    old_vtx2canon_vtx = to_old_vtx2canon_vtx(canon_vtx2old_vtx)
    ls = [[old_vtx2canon_vtx[old_neighbor]
               for old_neighbor in v2neighbors[old_v]]
          for new_v, old_v in enumerate(canon_vtx2old_vtx)]
    for row in ls:
        row.sort()
    return ls

            
    

def __test_cpacked_graph2graph():
    g = [[1,2,], [2,0,3], [1,3,0], [2,1], []]
    n, cg = len(g), graph2cpacked_graph(g)
    
    for ls in g:
        ls.sort()
    if not g == cpacked_graph2graph(n, cg):
        raise logic-error

    try:
        dg = [[1,2,], [2,0,3], [1,3,], [2,1], []]
        graph2cpacked_graph(dg)
        raise logic-error
    except ValueError:
        pass

    
    n, dcg = len(dg), digraph2cpacked_graph(dg)
    for ls in dg:
        ls.sort()
    if not dg == cpacked_graph2digraph(n, dcg):
        raise logic-error

    try:
        cpacked_graph2graph(n, dcg)
        raise logic-error
    except ValueError:
        pass
    
    try:
        mdg = [[1,1,], [2,], [], [2,1], []]
        digraph2cpacked_graph(mdg)
        raise logic-error
    except ValueError:
        pass
    try:
        not_g = [[1,5,], [2,], [], [2,1], []]
        digraph2cpacked_graph(not_g)
        raise logic-error
    except ValueError:
        pass
    return
__test_cpacked_graph2graph()

