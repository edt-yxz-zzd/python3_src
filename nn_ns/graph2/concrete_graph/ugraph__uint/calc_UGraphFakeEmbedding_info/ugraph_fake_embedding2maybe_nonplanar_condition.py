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




how to find out nonplanar_condition of ugraph_fake_embedding?
    use dfs
    treat the whole dfs-tree as the only new super_vertex
    treat all back_hedge/rback_hedge as super_hedge of super_loop
    detect whether the new super_ugraph_fake_embedding is planar?

    detail:
        dfs:
            iter children tree_hedge/back_hedge by counterclockwise from the parent tree_hedge/rtree_hedge


            # number back_hedge/rback_hedge by postorder
            hedge2maybe_postorder
                # back_hedge/rback_hedge -> postorder
                # tree_hedge/rtree_hedge -> None
            postorder2hedge
                # postorder -> back_hedge/rback_hedge

            hedge2maybe_ancestor_hedges_of_another_hedge
                # rback_hedge -> back_hedge's ancestor_hedges # left_biased_list
                # non-rback_hedge -> None



        postorder2paired_postorder
            <<== postorder2hedge + hedge2another_hedge + hedge2maybe_postorder
            assert postorder2paired_postorder is a bijection without self-reflect

        use a stack to verify whether postorder2paired_postorder is well-parenthesis



'''

__all__ = '''
    ugraph_fake_embedding2maybe_nonplanar_condition
    '''.split()

from seed.tiny import print_err
from .dfs__ugraph_fake_embedding import (
    dfs__ugraph_fake_embedding
    ,DFS_Case
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
from .verify_ugraph_fake_embedding_nonplanar_condition import \
    check_ugraph_fake_embedding_nonplanar_condition


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
    return _mk_maybe_nonplanar_condition_impl(ugraph_fake_embedding)

'''
class _NonPlanarConditionException(BaseException):
    def __init__(self, *
        , ugraph_fake_embedding...
        ):
'''

def _handle_nonplanar_condition(
    ugraph_fake_embedding, ancestor_hedgesC, ancestor_hedgesD
    ):
    path_ops = NonEmptyPathOps(ugraph_fake_embedding)
    xcycleAC__left_biased = ancestor_hedgesC
    xcycleBD__left_biased = ancestor_hedgesD
    xcycleBD = _left_biased_list_to_seq(xcycleBD__left_biased)
    xcycleAC = _left_biased_list_to_seq(xcycleAC__left_biased)
    def find_depth(xcycle):
        end_fvertex = path_ops.end_fvertex_of__basic(xcycle)
        fvertices = path_ops.iter_fvertices_of__basic(xcycle)
        for depth, fvertex in enumerate(fvertices):
            if fvertex == end_fvertex:
                return depth
        raise logic-error(not xcycle)

    depthA = find_depth(xcycleAC)
    depthB = find_depth(xcycleBD)

    assert depthB >= depthA

    for fork_depth in range(depthB, min(len(xcycleBD), len(xcycleAC))):
        if xcycleBD[fork_depth] != xcycleAC[fork_depth]: break
    else:
        raise logic-error
    depthF = fork_depth

    assert depthA <= depthB <= depthF

    assert len(xcycleBD) >= depthF+1
    assert len(xcycleAC) >= depthF+1

    #               /----<-------------------------------
    #        /-<----| --------------------------------\  |
    # depthA.A -> depthB.B -> depthF.F -[fork]-> ... -[back]->(A|B)
    #

    # fork
    assert xcycleBD[depthF] != xcycleAC[depthF]
    #assert xcycleBD[:depthF] == xcycleAC[:depthF]
    assert xcycleBD[depthF-1:depthF] == xcycleAC[depthF-1:depthF]



    def is_back_to(depth, xcycle):
        middle_first_hedge = xcycle[depth]
        last_hedge = xcycle[-1]
        path = (last_hedge, middle_first_hedge)
        return is_connected_hedges1__prime(ugraph_fake_embedding, path)
    assert is_back_to(depthB, xcycleBD)
    assert is_back_to(depthA, xcycleAC)

    # arc0_XXX - may empty
    # arc1_XXX - nonempty
    arc0_A2B = xcycleBD[depthA:depthB] # may empty
    arc0_B2C = xcycleBD[depthB:depthF] # may empty
    arc1_C2A = xcycleAC[depthF:] # nonempty
    arc1_C2B = xcycleBD[depthF:] # nonempty

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
        ).more_dfs()

    # number back_hedge/rback_hedge by postorder
    hedge2maybe_postorder = [None]*ugraph_fake_embedding.num_hedges
        # back_hedge/rback_hedge -> postorder
        # tree_hedge/rtree_hedge -> None
    postorder2hedge = []
        # postorder -> back_hedge/rback_hedge

    hedge2maybe_ancestor_hedges_of_another_hedge = [None]*ugraph_fake_embedding.num_hedges
        # rback_hedge -> back_hedge's ancestor_hedges # left_biased_list
        # non-rback_hedge -> None



    for case, payload in it:
        '''
        (DFS_EnterRootVertex, Vertex)
        (DFS_ExitRootVertex, Vertex)
        (DFS_EnterTreeHEdge, (HEdge, Vertex))
        (DFS_ExitTreeHEdge, None)
        (DFS_EnterExitBackOrRBackHEdge, (HEdge, Vertex))
        '''
        if case == DFS_Case.DFS_EnterExitBackOrRBackHEdge:
            hedge, fvertex = payload
            postorder = len(postorder2hedge)

            hedge2maybe_postorder[hedge] = postorder
            postorder2hedge.append(hedge)

            another_hedge = ugraph_fake_embedding.hedge2another_hedge(hedge)
            if hedge2maybe_postorder[another_hedge] is None:
                # hedge is back_hedge
                back_hedge = hedge
                rback_hedge = another_hedge

                hedge2maybe_ancestor_hedges_of_another_hedge[rback_hedge] \
                    = ancestor_hedges_of_back_hedge \
                    = ancestor_hedges.underlying_left_biased_list
            else:
                # hedge is rback_hedge
                rback_hedge = hedge
                assert hedge2maybe_ancestor_hedges_of_another_hedge[rback_hedge] is not None
        '''
        elif case == DFS_Case.DFS_EnterTreeHEdge:
        elif case == DFS_Case.DFS_ExitTreeHEdge:
        elif case == DFS_Case.DFS_EnterRootVertex:
        elif case == DFS_Case.DFS_ExitRootVertex:
        else:
            raise BaseException('unknown-DFS_Case-case: {case!r}')
        '''

    postorder2paired_postorder = [
        hedge2maybe_postorder[another_hedge]
        for another_hedge in map(
            ugraph_fake_embedding.hedge2another_hedge
            , postorder2hedge
            )
        ]
    assert not any(x is None for x in postorder2paired_postorder)
    # postorder2paired_postorder is bijection without self-reflect
    for postorder, paired_postorder in enumerate(postorder2paired_postorder):
        assert postorder != paired_postorder
        assert postorder == postorder2paired_postorder[paired_postorder]

    stack = [len(postorder2paired_postorder)]
    for postorder, paired_postorder in enumerate(postorder2paired_postorder):
        if postorder < paired_postorder:
            if not paired_postorder < stack[-1]:
                # nonplanar_condition
                #
                #A B C D:
                #   A <-> C, B <-> D
                postorderC = postorder
                postorderA = paired_postorder
                postorderB = stack[-1]
                postorderD = postorder2paired_postorder[postorderB]
                assert postorderA > postorderB > postorderC > postorderD

                rback_hedgeA = postorder2hedge[postorderA]
                #back_hedgeC = postorder2hedge[postorderC]
                rback_hedgeB = postorder2hedge[postorderB]
                #back_hedgeD = postorder2hedge[postorderD]

                ancestor_hedgesC = hedge2maybe_ancestor_hedges_of_another_hedge[rback_hedgeA]
                ancestor_hedgesD = hedge2maybe_ancestor_hedges_of_another_hedge[rback_hedgeB]
                return _handle_nonplanar_condition(
                    ugraph_fake_embedding
                    ,ancestor_hedgesC, ancestor_hedgesD
                    )
            else:
                stack.append(paired_postorder)
        else:
            postorder_ = stack.pop()
            assert postorder_ == postorder
    assert stack == [len(postorder2paired_postorder)]

    # planar
    return ()



