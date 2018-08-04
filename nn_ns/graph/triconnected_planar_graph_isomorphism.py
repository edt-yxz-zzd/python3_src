'''
A V log V algorithm for isomorphism of triconnected planar graphs
'''


'''
suppose we want to canonize SPQR-tree
we need to weight the edges of R
if we want to canonize BC-tree,
we need to color vertices of B
so the vertices of SPQR is colored

'''

from data_structure import OneTimeSet, OneTimeMap, Partition, OrderedSet
from .bucket_sort import group, bucket_sorts, is_sorted
from .simple_undirected_graph import graph
from .fake_face import fake_face
from .planar_embedding import planar_embedding, reverse_embedding, \
     is_planar_embedding, is_planar
from .multi_graph import make_mgraph, make_mgraph_from_simple_graph, \
     enter_edge, back_edge, dead_edge, exit_edge, \
     enter_root, exit_root, loop_edge

__all__ = ('canonize_triconnected_planar_simple_graph',)



planar_dt = 0
find_root_edge_dt = 0
relabel_dt = 0
covert_weight_dt = 0
mgraph_dfs_canon_dt = [0]*4
refine_loop_dt = 0
time_perf_counter = lambda:0
USING_C_EXTEND = True


def canonize_simple_planar_graph_by_given_root_dedge_and_embedding(
    simple_graph_with_embedding, root_dedge):
    t0 = time_perf_counter()
    G = simple_graph_with_embedding
    G_dedge = root_dedge
    mgraph = make_mgraph_from_simple_graph(G)
    t1 = time_perf_counter()
    
    if G.is_uedge(G_dedge):
        mgraph_start_edge = G_dedge
    else:
        medge = G.flip_dedge(G_dedge)
        mgraph_start_edge = mgraph.flip(medge)
    assert G.dedge2edge(G_dedge) == mgraph.edge2ends(mgraph_start_edge)

    t2 = time_perf_counter()
    DFS = mgraph.DFS(start_vtc_or_edges=[('e', mgraph_start_edge)])
    old_vertices_ordering, old_edges_ordering, new_mg = \
        canonize_graph_by_given_DFS(mgraph, DFS)
    t3 = time_perf_counter()
    

    # this adjacence list is a planar embedding too
    adj_ls = tuple(tuple(new_mg.edge2end(vu)
                         for vu in new_mg.outgoings(v)
                         )
                   for v in new_mg.vertices()
                   )
    assert sum(map(len, adj_ls)) == 2*G.ne()
    canon_label = adj_ls, old_vertices_ordering
    t4 = time_perf_counter()

    ts = [t0, t1, t2, t3, t4]
    global mgraph_dfs_canon_dt
    for i, (tx, tx1) in enumerate(zip(ts, ts[1:])):
        mgraph_dfs_canon_dt[i] += tx1-tx
    return canon_label

    
def canonize_graph_by_given_DFS(mgraph, DFS):
    g = mgraph
    n = g.nv()
    ordering = old_vertices_ordering = new_vtx2old_vtx = []
    old_vtx2new_vtx = [None]*n
    old_edges_ordering = []
    old_vtx2enterorstart_edge_loc = [None]*n
    new_vtx_cases = {enter_root, enter_edge}
    new_edge_cases = {enter_edge, loop_edge, back_edge, dead_edge}
    for case, edges, v in DFS:
        if case in new_vtx_cases:
            new = len(ordering)
            ordering.append(v)
            old_vtx2new_vtx[v] = new
        if case in new_edge_cases:
            e = edges[-1]
            for u, u_loc in g.edge2locs(e):
                if old_vtx2enterorstart_edge_loc[u] is None:
                    old_vtx2enterorstart_edge_loc[u] = u_loc
                    
            if case == dead_edge:
                if not g.is_directed(e):
                    # undirected edge has been treated as back edge
                    #
                    continue
            elif case == back_edge:
                if not g.is_directed(e):
                    if g.flip(e) == edges[-2]:
                        # back to parent
                        # it has been taken as a tree edge
                        continue
            old_edges_ordering.append(e)
            
    if not len(ordering) == n:
        raise ValueError('not visit all vertices')
    if not len(old_edges_ordering) == g.ne():
        print('len(old_edges_ordering) != g.ne()',
              len(old_edges_ordering), g.ne())
        print('old_edges_ordering', old_edges_ordering)
        
    assert len(old_edges_ordering) == g.ne()

##    new_edge2info = new_edge2directed_N_vtx_loc_pair_ls = tuple(
##        (g.is_directed(old_edge),
##         tuple((new_end, new_loc)
##               for old_end, old_loc in g.edge2locs(old_edge)
##               for new_end in [old_vtx2new_vtx[old_end]]
##               for loc_offset in [old_vtx2enterorstart_edge_loc[old_end]]
##               for loc_mod in [g.num_edge_ends(old_end)]
##               for new_loc in [(old_loc - loc_offset)%loc_mod]
##               )
##         )
##        for new_edge in range(g.ne())
##        for old_edge in [old_edges_ordering[new_edge]]
##        )

    new_edge2info = new_edge2directed_N_vtx_loc_pair_ls = []
    for new_edge in range(g.ne()):
        old_edge = old_edges_ordering[new_edge]
        new_locs = []
        for old_end, old_loc in g.edge2locs(old_edge):
            new_end = old_vtx2new_vtx[old_end]
            loc_offset = old_vtx2enterorstart_edge_loc[old_end]
            loc_mod = g.num_edge_ends(old_end)
            new_loc = (old_loc - loc_offset)%loc_mod
            new_locs.append((new_end, new_loc))
        info = [g.is_directed(old_edge), new_locs]
        new_edge2info.append(info)
            
        
    new_mg = make_mgraph(n, new_edge2info)
    return old_vertices_ordering, old_edges_ordering, new_mg



def canonize_triconnected_planar_simple_graph(simple_graph,
                                              e2weight=None,
                                              v2color=None):
    '''return ordering of vertices and edges

space: O(E) = O(V)
time:  O(ElogE) = O(VlogV)

input:
    g : simple_graph
    e2weight[uedge] = weight : 0 <= weight < g.ne()
    v2color[vtx] = color : 0 <= color < g.nv()

output:
    adj_ls : adjacency list of the canon graph (also a planar embedding)
    ordering: a map such that ordering[new_vtx] = old_vtx
'''

    g = simple_graph
    if e2weight == None:
        e2weight = [0]*g.ne()
    if v2color == None:
        v2color = [0]*g.nv()
        

    assert max(map(abs, v2color)) < g.nv()
    assert max(map(abs, e2weight)) < g.ne()

    t0 = time_perf_counter()
    embedding = planar_embedding(g)
    rembedding = reverse_embedding(embedding)
    t1 = time_perf_counter()
    global planar_dt
    planar_dt += t1 - t0
    results = []
    newgs = []

    def convert_e2weight(old_g, old_e2weight, new_g):
        # with same vertices
        # but edge number may be different
        new_e2weight = [None]*new_g.ne()
        for old_ue, weight in enumerate(old_e2weight):
            u,v = old_g.dedge2edge(old_ue)
            new_ue = new_g.edge2uedge((u,v))
            new_e2weight[new_ue] = weight
        return new_e2weight
    
    for em in [embedding, rembedding]:
        # for each embedding, find out a canon start dedge
        
        t0 = time_perf_counter()
        G = graph(em)
        new_e2weight = convert_e2weight(g, e2weight, G)
        t1 = time_perf_counter()
        global covert_weight_dt
        covert_weight_dt += t1-t0

        t0 = time_perf_counter()
        G_dedge = __canonize_triconnected_planar_simple_graph__one_embedding(
            G, new_e2weight, v2color)
        t1 = time_perf_counter()
        #print('dt=', t1-t0)
        global find_root_edge_dt
        find_root_edge_dt += t1-t0


        t0 = time_perf_counter()
        # generate canon label
        canon_label = adj_ls, old_vertices_ordering = \
            canonize_simple_planar_graph_by_given_root_dedge_and_embedding(
                G, G_dedge)
        results.append(canon_label)
        t1 = time_perf_counter()
        global relabel_dt
        relabel_dt += t1-t0 
        #print('adj_ls for an embedding', adj_ls)


    canon_label = adj_ls, old_vertices_ordering = \
                  min(results)
    return canon_label

def __canonize_triconnected_planar_simple_graph__one_embedding(
    g_with_planar_embedding, e2weight, v2color):
    g = g_with_planar_embedding
    ff = fake_face(g)

    # dedge(A->B), its neighbor (B->X) X!=A
    # assume ff.next_edge(dedge)->rightmost_neighbor
    # ==>> face that contains dedge is its right face
    def calc_dedge2rightmost_outgoing_neighbor(dedge):
        return ff.next_dedge(dedge)
    def calc_dedge2leftmost_outgoing_neighbor(dedge):
        return g.flip_dedge(ff.prev_dedge(g.flip_dedge(dedge)))
    def calc_dedge2info(dedge):
        right_face = ff.dedge2face[dedge]
        left_face = ff.dedge2face[g.flip_dedge(dedge)]
        num_edges_of_right_face = len(ff.face2dedges[right_face])
        num_edges_of_left_face = len(ff.face2dedges[left_face])
        
        head, tail = g.dedge2edge(dedge)
        head_degree = g.degree(head)
        tail_degree = g.degree(tail)
        
        edge_weight = e2weight[g.to_uedge(dedge)]
        head_color = v2color[head]
        tail_color = v2color[tail]
        info = ((num_edges_of_left_face, num_edges_of_right_face),
                (head_degree, tail_degree),
                (edge_weight, head_color, tail_color))
        return info

    num_dedges = 2*g.ne()
    dedge2info = [None]*num_dedges
    dedge2rightmost_outgoing_neighbor = [None]*num_dedges
    dedge2leftmost_outgoing_neighbor = [None]*num_dedges
    for dedge in g.dedges():
        assert 0 <= dedge < num_dedges
        dedge2info[dedge] = calc_dedge2info(dedge)
        dedge2rightmost_outgoing_neighbor[dedge] = \
            calc_dedge2rightmost_outgoing_neighbor(dedge)
        dedge2leftmost_outgoing_neighbor[dedge] = \
            calc_dedge2leftmost_outgoing_neighbor(dedge)
    assert all(left != right for left, right in
               zip(dedge2leftmost_outgoing_neighbor,
                   dedge2rightmost_outgoing_neighbor))
    assert sorted(dedge2leftmost_outgoing_neighbor) ==\
           sorted(dedge2rightmost_outgoing_neighbor) == \
           list(range(num_dedges))
        
    # bucket sort, initial partition dedges by info
    max_degree = max(g.degree(v) for v in g.vertices())
    max_num_face_edges = max(map(len, ff.face2dedges))
    ls = list((dedge2info[dedge], dedge) for dedge in g.dedges())
    assert is_sorted((g.dedges()))
    
    N = g.nv()
    M = g.ne()
    ls = bucket_sorts(ls, lambda i,e: e[0][2][i], [2,1,0], [N,N,M])
    
    N = max_degree+1
    ls = bucket_sorts(ls, lambda i,e: e[0][1][i], [1,0], [N,N])
    
    N = max_num_face_edges+1
    ls = bucket_sorts(ls, lambda i,e: e[0][0][i], [1,0], [N,N])
    assert is_sorted(ls)
    assert is_sorted(ls, key=lambda e:e[0])

    blocks = group(ls, key=lambda e:e[0])
    dedge_partition = [ls[k][1] for i,j in blocks for k in range(i,j)]
    

    
    

    # refine partition


    # initial dedge_partition
    block_sizes = (end-begin for begin, end in blocks)
    block_indices = range(len(blocks))
    buffer_dedge2block_idx = [None]*num_dedges
    dedge_partition = Partition(
        dedge_partition, block_sizes, block_indices, buffer_dedge2block_idx)
    
    buffer_block2idx = [None]*num_dedges # num_blocks at most num_dedges
    block2count = OneTimeMap(buffer_block2idx)

    
    
    LEFTMOST = 0
    RIGHTMOST = 1
    leftorright2dedge2neighbor = [None]*2
    leftorright2dedge2neighbor[LEFTMOST] = dedge2leftmost_outgoing_neighbor
    leftorright2dedge2neighbor[RIGHTMOST] = dedge2rightmost_outgoing_neighbor


    t0 = time_perf_counter()
    if USING_C_EXTEND:
        root_dedge = __canonize_triconnected_planar_simple_graph__refinement_c(
            dedge_partition, block2count, leftorright2dedge2neighbor,
            LEFTMOST, RIGHTMOST)
    ##########################################
    else:
        root_dedge, __num_steps, __num_loops = \
            __canonize_triconnected_planar_simple_graph__refinement(
                dedge_partition, block2count, leftorright2dedge2neighbor,
                LEFTMOST, RIGHTMOST)

        assert __canonize_triconnected_planar_simple_graph__refinement_check(
            dedge_partition, block2count, leftorright2dedge2neighbor,
            LEFTMOST, RIGHTMOST, dedge2info, g, __num_steps, __num_loops)

    t1 = time_perf_counter()
    global refine_loop_dt
    refine_loop_dt += t1 - t0
    return root_dedge

def __canonize_triconnected_planar_simple_graph__refinement_c(
        dedge_partition, block2count, leftorright2dedge2neighbor,
        LEFTMOST, RIGHTMOST):
    import graph._refinement as c_r
    import array
    f = c_r._refinement
    ints = array.array('i') # int []

    num_dedges = len(leftorright2dedge2neighbor[LEFTMOST])
    num_blocks = dedge_partition.num_blocks()
    dedge2loc = array.array('i', dedge_partition.element2loc)
    loc2dedge = array.array('i', dedge_partition.elements)
    loc2block = array.array('i', dedge_partition.loc2block)
    block2range = array.array('i',
        (loc for rng in dedge_partition.block_idx2range for loc in rng))
    block2range.extend([0]*(2*num_dedges - len(block2range)))
    assert len(block2range) == 2*num_dedges # int[num_dedges][2]
    assert len(dedge2loc) == len(loc2dedge) == len(loc2block) == num_dedges
    
    py_leftorright2dedge2neighbor = \
            array.array('i', leftorright2dedge2neighbor[LEFTMOST])
    py_leftorright2dedge2neighbor.extend(leftorright2dedge2neighbor[RIGHTMOST])
    assert len(py_leftorright2dedge2neighbor) == 2*num_dedges # int [2][num_dedges]
    
    root_dedge = c_r._refinement(num_dedges, num_blocks,
            dedge2loc, loc2dedge, loc2block, block2range,
            py_leftorright2dedge2neighbor)
    return root_dedge
    
    
def __canonize_triconnected_planar_simple_graph__refinement(
        dedge_partition, block2count, leftorright2dedge2neighbor,
        LEFTMOST, RIGHTMOST):
    num_dedges = len(leftorright2dedge2neighbor[LEFTMOST])
    
    # initial process
    def encode(block_idx, leftorright):
        assert 0 <= leftorright < 2
        begin, end = dedge_partition.block_range(block_idx)
        # bug:
        #      Once I use which_block(which now named as element2block_idx)
        #      as location2block_idx
        assert block_idx == dedge_partition.location2block_idx(begin)
        key = 2*begin + leftorright
        if not decode(key) == (block_idx, leftorright):
            print('decode(key) != (block_idx, leftorright)',
                  decode(key), (block_idx, leftorright))
        assert decode(key) == (block_idx, leftorright)
        return key
    
    def decode(key):
        begin, leftorright = divmod(key, 2)
        block_idx = dedge_partition.location2block_idx(begin)
        return block_idx, leftorright
        
    #process = OneTimeSet([None]*(2*num_dedges))
    process = OrderedSet()
    def add_to_process(block_idx, on_block_leftorright):
        key = encode(block_idx, on_block_leftorright)
        assert key not in process
        process.add(key)
    def not_processed(block_idx, on_block_leftorright):
        key = encode(block_idx, on_block_leftorright)
        return key in process
    def pop_from_process():
        return decode(process.pop_left())
    
    
    for block_idx in dedge_partition.iter_blocks():
        for on_block_leftorright in ([LEFTMOST, RIGHTMOST]):
            add_to_process(block_idx, on_block_leftorright)

    # after all I have switched to a more complex implement
##    process = [None]*(2*len(blocks))
##    __process_idx = -1
##    def add_to_process(block_idx, on_block_leftorright):
##        key = 2*block_idx + on_block_leftorright
##        if not key > __process_idx:
##            print('not key > __process_idx', key, __process_idx)
##        assert key > __process_idx # otherwise will not be process
##        process[key] = value
##    
##    def not_processed(block_idx, on_block_leftorright):
##        key = 2*block_idx + on_block_leftorright
##        return key > __process_idx and process[key] != None
##    for block_idx in range(len(blocks)):
##        for i, on_block_leftorright in enumerate([LEFTMOST, RIGHTMOST]):
##            value = (block_idx, on_block_leftorright)
##            assert i == on_block_leftorright
##            add_to_process(block_idx, on_block_leftorright)

    def print_lrface_edges_N_block_size_ls():
    
        lrface_edges_N_block_size_ls = [(face_edges, block_size)
            for block, dedge in zip(dedge_partition.iter_blocks(),
                                    dedge_partition.first_elements_by_block_idx())
            for face_edges in [dedge2info[dedge][0]]
            for block_size in [dedge_partition.block_size(block)]]
        print('lrface_edges_N_block_size_ls', lrface_edges_N_block_size_ls)

##    print('\n'*5)
##    print_lrface_edges_N_block_size_ls()
##    print([(dedge, g.dedge2edge(dedge)) for dedge in dedge_partition.iter_elements_by_location()])
##    print('dedge2leftmost_outgoing_neighbor', list(enumerate(dedge2leftmost_outgoing_neighbor)))
##    print('process', process)
    
    # main loop
    # before or eq __process_idx, has been processed
    __num_steps = 0
    __num_loops = 0
##    for __process_idx in range(2*num_dedges):
##        if __process_idx == len(process): break
##        data = process[__process_idx]
##        if data == None: continue
    while process:
        #data = decode(process.pop()) # FILO
        # using sorted set
        # since only O(E) blocks, each push/pop once, O(ElogE), too
        data = pop_from_process() # min out
        #print('process', process)
        
        block2count.clear()
        __num_loops += 1
        
        
        (block_idx, on_block_leftorright) = data
        # steps 'loop' body spent = O(block_size)
        __num_steps += dedge_partition.block_size(block_idx)
        # all dedges on current block's left/right
        moving = [] 

        dedge2neighbor = leftorright2dedge2neighbor[on_block_leftorright]
##        print('block', block_idx)
##        print('left/right', on_block_leftorright)
##        print('dedge2neighbor', dedge2neighbor)
        for dedge in dedge_partition.iter_block_elements(block_idx):
            moving.append(dedge2neighbor[dedge])
            #print('dedge2moving[{}]={}'.format(dedge, dedge2neighbor[dedge]))
            



        
        for dedge in moving:
            block = dedge_partition.element2block_idx(dedge)
            block2count.setdefault(block, 0)
            block2count[block] += 1
            #print('dedge2block[{}]={}'.format(dedge, block))
        
##        if any(count > 1 for count in block2count.values()):
##            print(list(block2count.items()))
        
        for block, count in block2count.items():
            block_size = dedge_partition.block_size(block)
            assert 0 < count <= block_size
            if count == block_size:
                # this block is a subset of moving
                # we can't split this block
                block2count[block] = -1
                continue


        # move edges
        # split blocks
        # NOTE:
        #    order of dedges in 'moving' determine
        #    1) order of block_idc
        #       which affect the order how we put data into process
        #    2) 1) will affect the split order of a block
        #    we should control dedge order in 'moving'(hard) AND
        #    control the element order in 'process'
        #    now I use begin_location of block to identify block
        #
        #    Once I used OneTimeSet for 'process'
        #    but it failed, so I switched to SortedSet
        for dedge in moving:
            block = dedge_partition.element2block_idx(dedge)
            # count = -1/0/>0
            # if -1: block is subset of moving, can't split
            # if 0: we have created a new block next to it
            # if >0: we have to create a new block
            count = block2count[block]
            if count < 0:
                continue

            #print('split block', block)
            if count > 0:
                dedge_partition.move_element_to_end(dedge)
                new_block = dedge_partition.split_tail(block, 1)
                assert new_block == dedge_partition.next_block(block)
                #assert new_block * 2 == len(process) > __process_idx
                #process.extend([None]*2)
                block2count[block] = 0
            else:
                dedge_partition.move_element_to_next(dedge)
            next_block = dedge_partition.element2block_idx(dedge)
            assert next_block == dedge_partition.next_block(block)
            begin, end = dedge_partition.block_range(next_block)
            assert dedge_partition.element2location(dedge) == begin
            _, _end = dedge_partition.block_range(block)
            assert _end == begin


        # new created blocks require 'process'
        for block, count in (list(block2count.items())):
            if count < 0: continue
            assert 0 == count
            
            new_block = dedge_partition.next_block(block)
            #assert __process_idx < 2*new_block
            for leftorright in ([LEFTMOST, RIGHTMOST]):
                if (not not_processed(block, leftorright)) and \
                   dedge_partition.block_size(block) < \
                   dedge_partition.block_size(new_block):
                    add_to_process(block, leftorright)
                else:
                    add_to_process(new_block, leftorright)
        while 0:
            print_lrface_edges_N_block_size_ls()
            break

            #######################################
            # 2333333333333333333333333333333333
            # drop...................
            continue
            if dedge_partition.block_size(block) < \
               dedge_partition.block_size(new_block):
                # 1 bug: we have to swap the block idx
                # since 'block' was passed
                # 2 bug: even swapped, bug too.
                # (block, L) processed but (block, R) not yet
                # we can't swap them!!!!
                dedge_partition.swap_block_idx(block, new_block)


            #########################################
            # drop below code.........
            continue
            for leftorright in [LEFTMOST, RIGHTMOST]:
                if not_processed(block, leftorright):
                    add_to_process(new_block, leftorright)
                elif dedge_partition.block_size(block) < \
                     dedge_partition.block_size(new_block):
                    # bug: we have to swap the block idx
                    # since 'block' was passed
                    
                    # 233333333333333333333333333333
                    # we are in a loop
                    # can't change 'block' and 'new_block', like below:
##                    dedge_partition.swap_block_idx(block, new_block)
##                    assert __process_idx < 2*new_block
##                    block, new_block = new_block, block
##                    assert __process_idx < 2*block
##                    add_to_process(block, leftorright)
                    # 233333333333333333333333333333
                    add_to_process(new_block, leftorright)
                    # after loop, we swap these two block
                else:
                    add_to_process(new_block, leftorright)
    return dedge_partition.location2element(0), __num_steps, __num_loops


def __canonize_triconnected_planar_simple_graph__refinement_check(
        dedge_partition, block2count, leftorright2dedge2neighbor,
        LEFTMOST, RIGHTMOST, dedge2info, g, __num_steps, __num_loops):
    num_dedges = len(leftorright2dedge2neighbor[LEFTMOST])
    
    # check: is stable now?
    for leftorright in [LEFTMOST, RIGHTMOST]:
        for block in dedge_partition.iter_blocks():
            block2count.clear()
            
            for dedge in dedge_partition.iter_block_elements(block):
                testing_block = dedge_partition.element2block_idx(dedge)
                block2count.setdefault(testing_block, 0)
                block2count[testing_block] += 1
            for dedge in dedge_partition.iter_block_elements(block):
                testing_block = dedge_partition.element2block_idx(dedge)
                assert block2count[testing_block] == \
                       dedge_partition.block_size(testing_block)
            
##    assert __process_idx == len(process) or len(process) == 2*num_dedges
##    assert len(process) <= 2*num_dedges
    block_sizes = list(dedge_partition.block_size(block)
                       for block in dedge_partition.iter_blocks())
    assert num_dedges == sum(block_sizes)
    assert all(all(info == dedge2info[dedge]
                   for dedge in dedge_partition.iter_block_elements(block))
               for block in dedge_partition.iter_blocks()
               for begin, end in [dedge_partition.block_range(block)]
               for info in [dedge2info[dedge_partition.\
                                       location2element(begin)]])
    if 0:
        block0 = dedge_partition.location2block_idx(0)
        assert block0 == 0
        print('block_sizes', block_sizes)
        print('blocks[0]->info', list(dedge2info[dedge]
            for dedge in dedge_partition.iter_block_elements(block0)))

    # for V=24 cubic graph, E=3V/2=36
    # 4Elog4E = 1152 # too large!
    E = 4*g.ne() # undirected->directed and L/R; 4 times
    assert E*E.bit_length() >= __num_steps
    assert __num_loops == dedge_partition.num_blocks() * 2 <= E
    return True




def test(N = 6):
    from .some_triconnected_cubic_planar_graphs import \
         get_planar_embeddings
    import random
    from .decompose import is_connect3

    def test_g(old_g, adj_ls, old2new):
        
        new_g = old_g.relabel(old2new)
        assert old_g == new_g.relabel_back(old2new)
        if 0:
            assert is_planar(new_g)
            new_mg = make_mgraph_from_simple_graph(new_g)
            assert is_connect3(new_mg, new_mg.DFS())
        
        _canon = canonize_triconnected_planar_simple_graph(new_g)
        _adj_ls, _ = _canon
        if not _adj_ls == adj_ls:
            print('i=', i)
            print('old canon:', adj_ls)
            print('new canon:', _adj_ls)
            print('old g:', old_g)
            print('new g:', new_g)
            print('old2new:', old2new)
        assert _adj_ls == adj_ls

    begin_at = 0
    for i,em in enumerate(get_planar_embeddings()):
        if i < begin_at: continue
        old_g = graph(em)
        canon = canonize_triconnected_planar_simple_graph(old_g)
        adj_ls, ordering = canon
        #print(adj_ls)
        if i == 6:
            old2new = [1, 8, 9, 4, 2, 0, 3, 5, 6, 7]
            test_g(old_g, adj_ls, old2new)
            
        old2new = list(range(old_g.nv()))
        for _ in range(N):
            random.shuffle(old2new)
            test_g(old_g, adj_ls, old2new)
    return 
            


if __name__ == '__main__':
    import time
    time_perf_counter = time.perf_counter
    t0 = time_perf_counter()
    test(1)
    t1 = time_perf_counter()
    total_dt = t1-t0
    tpl = '{}/{} = {:.5}/{:.5} = {:.5}'
    def show(dt_name, total_name):
        dt = globals()[dt_name]
        tt = globals()[total_name]
        s = tpl.format(dt_name, total_name,
                       dt, tt, dt/tt)
        
        print(s)

    print('USING_C_EXTEND:', USING_C_EXTEND)
    for dt_name in 'planar_dt covert_weight_dt find_root_edge_dt relabel_dt'.split():
        show(dt_name, 'total_dt')
    show('refine_loop_dt', 'find_root_edge_dt')

    mgraph_dfs_canon_dt_all = sum(mgraph_dfs_canon_dt)
    dt1, dt2, dt3, dt4 = mgraph_dfs_canon_dt
    show('mgraph_dfs_canon_dt_all', 'relabel_dt')
    
    for i in range(1,5):
        show('dt'+str(i), 'mgraph_dfs_canon_dt_all')
    # print('dt/total', total_dt, '/', (t1-t0), '=', total_dt/(t1-t0))
    # ---when using C for core loop
    ##planar_dt/total_dt = 7.188573849783089/14.463644089705753 = 0.4970098686885853
    ##covert_weight_dt/total_dt = 0.7091263272767284/14.463644089705753 = 0.049028192541147826
    ##find_root_edge_dt/total_dt = 2.71369088374012/14.463644089705753 = 0.18762151964673565
    ##relabel_dt/total_dt = 2.4573612269762286/14.463644089705753 = 0.1698991769802475
    # ---pure python implement:
    ##planar_dt/total_dt = 7.166468494541814/25.37807527217512 = 0.28238818025728024
    ##covert_weight_dt/total_dt = 0.7097015395848114/25.37807527217512 = 0.027965144400171994
    ##find_root_edge_dt/total_dt = 13.584114659312569/25.37807527217512 = 0.5352696969185202
    ##relabel_dt/total_dt = 2.5232745952133184/25.37807527217512 = 0.09942734301761144

    '''why planar-embedding took so many times???
a check 'is_planar_embedding' in Boyer_Myrvold_planarity_test
is expensive.
remove it:
planar_dt/total_dt = 1.48681678877099/8.751148103241079 = 0.16989962588112661
covert_weight_dt/total_dt = 0.7077310586789926/8.751148103241079 = 0.08087293807961918
find_root_edge_dt/total_dt = 2.716208231742618/8.751148103241079 = 0.3103830719921929
relabel_dt/total_dt = 2.4496694117537743/8.751148103241079 = 0.2799254889591588

why is relabel so timeconsume??

'''










