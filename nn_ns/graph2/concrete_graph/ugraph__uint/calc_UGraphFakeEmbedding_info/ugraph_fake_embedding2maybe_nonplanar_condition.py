r'''
see:
    "planar/algo - is fake_embedding relax_planar[ver4].txt"
        use dfs to detect ugraph_fake_embedding nonplanar_condition
    "def - 3.4. simple clockwise path cycle.txt"
        for simple_nonemtpy_path, simple_path
    "def - 3.5. nonplanar_condition.txt"
        for ugraph_fake_embedding nonplanar_condition

xcycle =[def]= simple_nonemtpy_path__left_biased s.t. last hedge is back_hedge
    i.e. the path's tail is a cycle



nonplanar_condition
    detected at the begin_vertex of 3-paths
        # B
    detected on rback_hedge
        # when revisit back_hedge hedgeX
        #
        # B<-[hedgeX]-+-[back]-*-C
        #   where preorder[hedgeX] < preorder[hedgeY]
        #         C-*-[back]-+-[hedgeY]->A
                                     <-\
         /-<-[hedgeX]-+-[back]-*-C      |
...A-*->B-*->C-*-[back]-+-[hedgeY]->A   |
             \-*-[back]-+-[hedgeX]->B  /
                                      /  direction of dfs visit hedges around vertex
    # min low_pt[C.tree_hedge that lead to hedgeX] may lower than A
    #   hence can not be detected by rtree_hedge at C



'''

__all__ = '''
    ugraph_fake_embedding2maybe_nonplanar_condition
    '''.split()

from seed.tiny import print_err
from .dfs__ugraph_fake_embedding import (
    dfs__ugraph_fake_embedding
    ,DFS_Case
    ,DFS_CaseParts
    )
from .imports import (
    the_left_biased_list_as_stack_ops
    ,LeftBiasedListAsAsCompleteMutableStack
    )
from ..NonEmptyPathOps import (
    NonEmptyPathOps
    ,is_connected_hedges1__prime
    ,reverse_nonempty_path__basic
    )
from .verify_ugraph_fake_embedding_nonplanar_condition import check_ugraph_fake_embedding_nonplanar_condition


def ugraph_fake_embedding2maybe_nonplanar_condition(ugraph_fake_embedding):
    '''
input:
    ugraph_fake_embedding :: UGraphFakeEmbedding
output:
    maybe_nonplanar_condition = () | nonplanar_condition
        ()
            planar fake_embedding
        (simple_nonemtpy_path, simple_path, simple_nonemtpy_path)
            non-planar fake_embedding
            simple_path may be empty, only a fvertex

            3 paths have same (begin_fvertex, end_fvertex)
            any 2 paths donot shared any middle fvertex

            if simple_path is not empty:
                3 first_hedges and 3 reversed_last_hedges are in same clockwise-direction
            else:
                (first_hedgeX, first_hedgeY, reversed_last_hedgeX, reversed_last_hedgeY) in one clockwise-direction
'''
    try:
        _mk_maybe_nonplanar_condition_impl(ugraph_fake_embedding)
    except _NonPlanarConditionException as e:
        return _handle_nonplanar_condition(e)
    return ()

class _NonPlanarConditionException(BaseException):
    def __init__(self, *
        , ugraph_fake_embedding, early_pair, later_pair
        ):
        self.ugraph_fake_embedding = ugraph_fake_embedding
        #self.fork_depth = fork_depth
        self.early_pair = early_pair
        self.later_pair = later_pair
def _handle_nonplanar_condition(e):
    ugraph_fake_embedding = e.ugraph_fake_embedding
    #fork_depth = e.fork_depth
    pair0 = early_pair = e.early_pair
    pair1 = later_pair = e.later_pair

    ((depth0, local_idx0), xcycle0__left_biased) = pair0
    #depth1 = fork_depth
    ((depth2, local_idx2), xcycle2__left_biased) = pair1
    assert depth0 >= depth2

    xcycle0 = _left_biased_list_to_seq(xcycle0__left_biased)
    xcycle2 = _left_biased_list_to_seq(xcycle2__left_biased)
    for fork_depth in range(depth0, min(len(xcycle0), len(xcycle2))):
        if xcycle0[fork_depth] != xcycle2[fork_depth]: break
    else:
        raise logic-error
    depth1 = fork_depth

    # key1 > key0 > key2
    assert depth1 >= depth0 >= depth2

    assert len(xcycle0) >= depth1+1
    assert len(xcycle2) >= depth1+1

    #               /----<-------------------------------
    #        /-<----| --------------------------------\  |
    # depth2.A -> depth0.B -> depth1.C -[fork]-> ... -[back]->(A|B)
    #

    # fork
    assert xcycle0[depth1] != xcycle2[depth1]
    #assert xcycle0[:depth1] == xcycle2[:depth1]
    assert xcycle0[depth1-1:depth1] == xcycle2[depth1-1:depth1]



    path_ops = NonEmptyPathOps(ugraph_fake_embedding)
    def is_back_to(depth, xcycle):
        middle_first_hedge = xcycle[depth]
        last_hedge = xcycle[-1]
        path = (last_hedge, middle_first_hedge)
        return is_connected_hedges1__prime(ugraph_fake_embedding, path)
    assert is_back_to(depth0, xcycle0)
    assert is_back_to(depth2, xcycle2)

    # arc0_XXX - may empty
    # arc1_XXX - nonempty
    arc0_A2B = xcycle0[depth2:depth0] # may empty
    arc0_B2C = xcycle0[depth0:depth1] # may empty
    arc1_C2A = xcycle2[depth1:] # nonempty
    arc1_C2B = xcycle0[depth1:] # nonempty

    arc1_C2A2B = arc1_C2A + arc0_A2B # nonempty

    arc1_B2A2C = path_ops.reverse_nonempty_path__basic(arc1_C2A2B)
    arc1_B2C__from_C2B = path_ops.reverse_nonempty_path__basic(arc1_C2B)

    C = path_ops.begin_fvertex_of__basic(arc1_C2A)
    path0_B2C = (arc0_B2C, C)
    nonplanar_condition = (arc1_B2A2C, path0_B2C, arc1_B2C__from_C2B)

    assert check_ugraph_fake_embedding_nonplanar_condition(ugraph_fake_embedding, nonplanar_condition) or True
    return nonplanar_condition

def _left_biased_list_to_seq(left_biased_list):
    it = the_left_biased_list_as_stack_ops.reversed(left_biased_list)
    ls = list(it)
    ls.reverse()
    return tuple(ls)


def _mk_maybe_nonplanar_condition_impl(ugraph_fake_embedding):
    ancestor_hedges = LeftBiasedListAsAsCompleteMutableStack()
    it = dfs__ugraph_fake_embedding(
        ugraph_fake_embedding=ugraph_fake_embedding
        ,is_clockwise_around_fvertex=False
            # dfs visit fvertices in "counterclockwise"
            #
            # hence clockwise around fface
            # assume tree hedge comes down
            #   then child tree hedges from left to right
        ,maybe_ancestor_hedge_stack = ancestor_hedges
        ,maybe_ancestor_vertex_stack = None
        )

    fvertex2depth = [None]*ugraph_fake_embedding.num_fvertices
    hedge2local_idx = [None]*ugraph_fake_embedding.num_hedges
        # local idx around fvertex in "clockwise"
        #   NOTE: dfs visit fvertices in counterclockwise
        # start from the another_hedge of income tree hedge
        #

    rback_hedge2pair = [None]*ugraph_fake_embedding.num_hedges
    hedge2preorder = [None]*ugraph_fake_embedding.num_hedges
    global_hedge_preorder = 0
    global_depth = -1
    pair_stack = []
        # a stack<pair>
        # pair = keyed_may_min_xcycle
        # pair = (key, None|simple_nonemtpy_xcycle__left_biased)
        # None - for root/income hedge
        # simple_nonemtpy_xcycle__left_biased :: LeftBiasedListAsAsCompleteMutableStack
        # back_hedge = simple_nonemtpy_xcycle__left_biased.get_top()
        # key = (depth-of-end_fvertex, local_idx-of-reversed-back_hedge)

    def hedge2another_fvertex(hedge):
        other = ugraph_fake_embedding.hedge2another_hedge(hedge)
        return ugraph_fake_embedding.hedge2fvertex[other]
    def hedge2key(hedge):
        fvertex = ugraph_fake_embedding.hedge2fvertex[hedge]
        key = (fvertex2depth[fvertex], hedge2local_idx[hedge])
        return key
    def xcycle2key(simple_nonemtpy_xcycle__left_biased):
        last_hedge = back_hedge = \
            simple_nonemtpy_xcycle__left_biased[1]
        reversed_last_hedge = reversed_back_hedge = \
            ugraph_fake_embedding.hedge2another_hedge(back_hedge)
        key = hedge2key(reversed_back_hedge)
        return key
    def min_pair(pair1, pair2):
        return min(pair1, pair2, key=lambda pair:pair[0])
    def update_last_pair(global_depth, hedge, pair):
        fvertex = ugraph_fake_embedding.hedge2fvertex[hedge]
        depth = fvertex2depth[fvertex]
        assert depth == global_depth

        last_pair = pair_stack[-1]
        pair_stack[-1] = min_pair(last_pair, pair)
        return
    def detect_nonplanar_condition(global_depth, rback_hedge):
        fvertex = ugraph_fake_embedding.hedge2fvertex[rback_hedge]
        depth = fvertex2depth[fvertex]
        assert depth == global_depth

        last_pair = pair_stack[-1]
        last_key = last_pair[0]
        # since we have revisit a back_hedge, last_key cannot be the default one
        assert last_key != (global_depth+1, -1)
        assert last_key != make_default_key_at(global_depth)
        assert last_key[0] == global_depth
        assert last_key[1] >= 0

        rback_pair = rback_hedge2pair[rback_hedge]
        rback_hedge2pair[rback_hedge] = ()#del
        rback_key = rback_pair[0]

        if rback_key <= last_key:
            return

        assert last_key < rback_key # last_key goto outside back_hedge
        back_hedge = rback_pair[1][1]
        assert back_hedge == ugraph_fake_embedding.hedge2another_hedge(rback_hedge)
        back_order = hedge2preorder[back_hedge]
        last_order = hedge2preorder[last_pair[1][1]]

        assert back_order != last_order
        if back_order > last_order: return
        assert back_order < last_order # rback_pair is early

        last_depth = last_key[0]
        rback_depth = rback_key[0]
        assert last_depth <= rback_depth
        #for fork_depth in range(rback_depth, len()):
        # nonplanar_condition
        raise _NonPlanarConditionException(
                ugraph_fake_embedding=ugraph_fake_embedding
                #, fork_depth=fork_depth
                , early_pair=rback_pair, later_pair=last_pair
                )

    def make_default_pair_at(global_depth):
        return (make_default_key_at(global_depth), None)
    def make_default_key_at(global_depth):
        key = (global_depth+1, -1)
            # > (global_depth, 0..?)
            # < (global_depth+1, 0..?)
        return key

    # len(ancestor_hedges) == len(pair_stack) == global_depth+1 == 0

    for case, payload in it:
        # update global_depth
        #   NOTE: DFS_EnterExitBackOrRBackHEdge
        '''
        print_err(case._value_)
        if False and not ancestor_hedges.is_empty():
            h = ancestor_hedges.get_top()
            o = ugraph_fake_embedding.hedge2another_hedge(h)
            print_err(f'{h}-><-{o}')
            del h,o
        '''

        if DFS_CaseParts.Enter in case._value_:
            global_depth += 1
        ###not elif
        if DFS_CaseParts.Exit in case._value_:
            global_depth -= 1



        '''
        (DFS_EnterRootVertex, Vertex)
        (DFS_ExitRootVertex, Vertex)
        (DFS_EnterTreeHEdge, (HEdge, Vertex))
        (DFS_ExitTreeHEdge, None)
        (DFS_EnterExitBackOrRBackHEdge, (HEdge, Vertex))
        '''

        # len(ancestor_hedges)
        #   == len(pair_stack) + [0/1]
        #   == global_depth + [0/1]
        if case == DFS_Case.DFS_EnterTreeHEdge:
            # len(ancestor_hedges)
            #   == len(pair_stack) + 0
            #   == global_depth + 0
            #
            hedge, fvertex = payload
            # fill fvertex2depth
            # fill hedge2local_idx
            # append pair_stack
            #
            hedge2preorder[hedge] = global_hedge_preorder
            global_hedge_preorder += 1

            fvertex2depth[fvertex] = global_depth
            other = ugraph_fake_embedding.hedge2another_hedge(hedge)
            it = ugraph_fake_embedding.hedge2iter_fake_clockwise_hedges_around_vertex(other)
            for local_idx, hedge in enumerate(it):
                hedge2local_idx[hedge] = local_idx

            #hedge = other
            #local_idx = 0 # other is root/income hedge
            pair = make_default_pair_at(global_depth)
            pair_stack.append(pair)
            # len(ancestor_hedges) == len(pair_stack)-1 == global_depth
        elif case == DFS_Case.DFS_EnterRootVertex:
            # len(ancestor_hedges)
            #   == len(pair_stack) + 0
            #   == global_depth + 0
            #
            assert global_depth == 0
            fvertex = payload
            # fill hedge2local_idx
            # fill fvertex2depth
            # init pair_stack

            first_child_hedge_of_root = ugraph_fake_embedding.fvertex2arbitrary_hedge[fvertex]
            last_child_hedge_of_root = ugraph_fake_embedding.hedge2fake_clockwise_next_hedge_around_vertex[first_child_hedge_of_root]
            it = ugraph_fake_embedding.hedge2iter_fake_clockwise_hedges_around_vertex(last_child_hedge_of_root)
            for local_idx, hedge in enumerate(it):
                hedge2local_idx[hedge] = local_idx

            fvertex2depth[fvertex] = global_depth
            pair = make_default_pair_at(global_depth)
            pair_stack.append(pair)
            # len(ancestor_hedges) == len(pair_stack)-1 == global_depth
        elif case == DFS_Case.DFS_ExitTreeHEdge:
            # len(ancestor_hedges)
            #   == len(pair_stack) + -1
            #   == global_depth + 1
            #
            # pop and update top pair_stack
            assert payload is None
            hedge = ancestor_hedges.get_top()

            hedge2preorder[ugraph_fake_embedding.hedge2another_hedge(hedge)] = global_hedge_preorder
            global_hedge_preorder += 1

            pair = pair_stack.pop()
            update_last_pair(global_depth, hedge, pair)
            # len(ancestor_hedges) == len(pair_stack)+0 == global_depth+1
            # will ancestor_hedges.pop_None()
            # len(ancestor_hedges) == len(pair_stack)-1 == global_depth
        elif case == DFS_Case.DFS_ExitRootVertex:
            # len(ancestor_hedges)
            #   == len(pair_stack) + -1
            #   == global_depth + 1
            #
            assert global_depth == -1
            assert len(pair_stack) == 1
            assert ancestor_hedges.is_empty()
            pair_stack.pop()
            # len(ancestor_hedges) == len(pair_stack)+0 == global_depth+1
            # will ancestor_hedges.pop_None()
            # len(ancestor_hedges) == len(pair_stack)-1 == global_depth
        elif case == DFS_Case.DFS_EnterExitBackOrRBackHEdge:
            # len(ancestor_hedges)
            #   == len(pair_stack) + 0
            #   == global_depth + 1
            #
            hedge, fvertex = payload

            hedge2preorder[hedge] = global_hedge_preorder
            global_hedge_preorder += 1

            # to test whether a back_hedge
            other = ugraph_fake_embedding.hedge2another_hedge(hedge)
            begin_key = hedge2key(hedge)
            end_key = hedge2key(other)
            assert begin_key != end_key
            if end_key < begin_key:
                # back_hedge
                back_hedge = hedge
                simple_nonemtpy_xcycle__left_biased = \
                    ancestor_hedges.underlying_left_biased_list
                key = xcycle2key(simple_nonemtpy_xcycle__left_biased)
                pair = (key, simple_nonemtpy_xcycle__left_biased)
                assert key == end_key
                update_last_pair(global_depth, back_hedge, pair)

                rback_hedge = ugraph_fake_embedding.hedge2another_hedge(back_hedge)
                rback_hedge2pair[rback_hedge] = pair
            else:
                # rback_hedge
                rback_hedge = hedge
                detect_nonplanar_condition(global_depth, rback_hedge)
            # len(ancestor_hedges) == len(pair_stack)+0 == global_depth+1
            # will ancestor_hedges.pop_None()
            # len(ancestor_hedges) == len(pair_stack)-1 == global_depth
        else:
            raise unknown-case
        # len(ancestor_hedges) == len(pair_stack) == global_depth


