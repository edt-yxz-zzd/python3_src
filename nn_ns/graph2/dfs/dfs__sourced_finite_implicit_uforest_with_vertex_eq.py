'''
see: "def - 2.1. infinite implicit graph.txt"
    implicit graph
        * finite out_rooted utree with vertex_eq
            # need vertex_eq to avoid parent since undirected
'''

__all__ = '''
    DFS_Case
    dfs__sourced_finite_implicit_uforest_with_vertex_eq
    '''.split()

from ..stack.ICompleteMutableStack import ICompleteMutableStack
from ..stack.INearlyCompleteMutableStack import INearlyCompleteMutableStack
from ..stack.SeqAsCompleteMutableStack import SeqAsCompleteMutableStack
from ..stack.NearlyCompleteMutableStack import NearlyCompleteMutableStack

from .dfs__finite_explicit_ugraph__two_color import (
    dfs__finite_explicit_ugraph__two_color
    ,DFS_Case as _DFS_Case
    )
from .Vertex2TwoColor.Vertex2TwoColor__no_effect import the_vertex2two_color__no_effect

import enum
DFS_Case = enum.Enum('DFS_Case', '''
    DFS_EnterVertex
    DFS_ExitVertex
    '''.split()
    )


"""
DFS_Case = enum.Enum('DFS_Case', '''
    DFS_EnterRootVertex
    DFS_ExitRootVertex
    DFS_EnterTreeHEdge
    DFS_ExitTreeHEdge
    '''.split()
    )
DFS_Case = enum.Flag('DFS_Case', '''
    DFS_Exit
    DFS_TreeHEdge
    '''.split()
    )
class DFS_Case(enum.Flag):
    DFS_EnterTreeHEdge = enum.auto()
    DFS_ExitRootVertex = enum.auto()

    DFS_Exit = DFS_ExitRootVertex
    DFS_TreeHEdge = DFS_EnterTreeHEdge

    DFS_EnterRootVertex = DFS_Exit & DFS_TreeHEdge
    DFS_ExitTreeHEdge = DFS_Exit | DFS_TreeHEdge
"""


'''
def _dfs__sourced_finite_implicit_uforest_with_hedge_eq(*
    ,source_vertices

    # for root_vertex
    ,vertex2unstable_iter_hedges

    # for nonroot_vertex
    ,hedge2next_hedge_in_cycle_around_vertex
    ,hedge2another_hedge
    ,hedge_eq

    ,hedge2vertex
    ):
'''

def dfs__sourced_finite_implicit_uforest_with_vertex_eq(*
    ,source_vertices
    ,vertex_eq
    ,vertex2unstable_iter_hedges
    ,hedge2another_vertex

    ,maybe_ancestor_hedge_stack = None
    ,maybe_ancestor_vertex_stack = None
    ):
    '''

do not color vertices in this function

input:
    source_vertices :: Iter Vertex
        # dfs roots
        # if donot want to visit vertex more than once
        #   should select one vertex per connected component
    vertex_eq :: Vertex -> Vertex -> Bool
        # to avoid parent vertex
        #   [uforest is ugraph]
        #   [iter hedges around vertex will visit parent vertex]
        # if we can avoid parent vertex when iter hedges around vertex
        #   then we should use dfs__sourced_finite_implicit_DAG_as_compact_forest
        #
        # uforest ==>> need vertex_eq only, need not hedge_eq
    vertex2unstable_iter_hedges :: Vertex -> Iter HEdge
    hedge2another_vertex :: HEdge -> Vertex

inout:
    maybe_ancestor_hedge_stack :: None|INearlyCompleteMutableStack
        NearlyCompleteMutableStack
    maybe_ancestor_vertex_stack :: None|ICompleteMutableStack
        SeqAsCompleteMutableStack


output:
    #push before yield DFS_EnterXXX
    #pop after yield DFS_ExitXXX
    # uforest ==>> only tree_edge, no back_edge

    Iter (DFS_Case, Vertex)
        (DFS_EnterVertex, Vertex)
        (DFS_ExitVertex, Vertex)
            # to access hedge, use maybe_ancestor_hedge_stack
            # to tell whether is root, use maybe_ancestor_vertex_stack


        # ??Iter simple_path?? too heavy
        simple_path = (ancestor_hedges, end_vertex) :: ([HEdge], Vertex)
            may be empty
            dfs_tree_arcs from root to curr vertex


example:
    >>> this = dfs__sourced_finite_implicit_uforest_with_vertex_eq
    >>> source_vertices = '0a1'
    >>> vertex_eq = lambda a, b: a == b
    >>> d = {'a':'bc', 'b':'a', 'c':'ad', 'd':'c', '0':'1', '1':'0'}
    >>> vertex2unstable_iter_hedges = lambda v:iter(d[v])
    >>> hedge2another_vertex = lambda a:a
    >>> it = this(source_vertices=source_vertices, vertex_eq=vertex_eq, vertex2unstable_iter_hedges=vertex2unstable_iter_hedges, hedge2another_vertex=hedge2another_vertex)
    >>> list(it)
    [(<DFS_Case.DFS_EnterVertex: 1>, '0'), (<DFS_Case.DFS_EnterVertex: 1>, '1'), (<DFS_Case.DFS_ExitVertex: 2>, '1'), (<DFS_Case.DFS_ExitVertex: 2>, '0'), (<DFS_Case.DFS_EnterVertex: 1>, 'a'), (<DFS_Case.DFS_EnterVertex: 1>, 'b'), (<DFS_Case.DFS_ExitVertex: 2>, 'b'), (<DFS_Case.DFS_EnterVertex: 1>, 'c'), (<DFS_Case.DFS_EnterVertex: 1>, 'd'), (<DFS_Case.DFS_ExitVertex: 2>, 'd'), (<DFS_Case.DFS_ExitVertex: 2>, 'c'), (<DFS_Case.DFS_ExitVertex: 2>, 'a'), (<DFS_Case.DFS_EnterVertex: 1>, '1'), (<DFS_Case.DFS_EnterVertex: 1>, '0'), (<DFS_Case.DFS_ExitVertex: 2>, '0'), (<DFS_Case.DFS_ExitVertex: 2>, '1')]


'''
    if maybe_ancestor_hedge_stack is None:
        ancestor_hedges = NearlyCompleteMutableStack()
    else:
        ancestor_hedges = maybe_ancestor_hedge_stack
        if not isinstance(ancestor_hedges, INearlyCompleteMutableStack): raise TypeError
        if not ancestor_hedges.is_empty(): raise ValueError

    if maybe_ancestor_vertex_stack is None:
        ancestor_vertices = SeqAsCompleteMutableStack([])
    else:
        ancestor_vertices = maybe_ancestor_vertex_stack
        if not isinstance(ancestor_vertices, ICompleteMutableStack): raise TypeError
        if not ancestor_vertices.is_empty(): raise ValueError

    #f = _dfs__sourced_finite_implicit_uforest_with_vertex_eq__basic_ver2
    f = _dfs__sourced_finite_implicit_uforest_with_vertex_eq__basic_ver1
    return f(source_vertices = source_vertices
            ,vertex_eq = vertex_eq
            ,vertex2unstable_iter_hedges = vertex2unstable_iter_hedges
            ,hedge2another_vertex = hedge2another_vertex
            ,ancestor_hedges = ancestor_hedges
            ,ancestor_vertices = ancestor_vertices
            )


def _dfs__sourced_finite_implicit_uforest_with_vertex_eq__basic_ver2(*
    ,source_vertices
    ,vertex_eq
    ,vertex2unstable_iter_hedges
    ,hedge2another_vertex

    ,ancestor_hedges
    ,ancestor_vertices
    ):
    # hedge__new = (vertex, hedge)
    #   where vertex == hedge2vertex(hedge)

    def hedge2another_vertex__new(hedge__new):
        vertex, hedge = hedge__new
        return hedge2another_vertex(hedge)
    def vertex2unstable_iter_hedges__new(vertex):
        for hedge in vertex2unstable_iter_hedges(vertex):
            yield vertex, hedge
    def hedge2unstable_iter_other_hedges_around_another_vertex__new(hedge__new):
        vertex, hedge = hedge__new
        # vertex == hedge2vertex(hedge)
        another_vertex = hedge2another_vertex(hedge)
        for other_hedge in vertex2unstable_iter_hedges(another_vertex):
            vertex_ = hedge2another_vertex(other_hedge)
            if not vertex_eq(vertex_, vertex):
                yield another_vertex, other_hedge

    class AncestorHedges__new(INearlyCompleteMutableStack):
        def __init__(self, ancestor_hedges):
            self.ancestor_hedges = ancestor_hedges
        def is_empty(self):
            return self.ancestor_hedges.is_empty()
        def pop_None(self):
            self.ancestor_hedges.pop_None()
        def push(self, hedge__new):
            vertex, hedge = hedge__new
            self.ancestor_hedges.push(hedge)
    ancestor_hedges__new = AncestorHedges__new(ancestor_hedges)

    it__new = dfs__finite_explicit_ugraph__two_color.via_source_vertices(
        source_vertices=source_vertices
        ,vertex2color=the_vertex2two_color__no_effect
        ,vertex2unstable_iter_hedges=vertex2unstable_iter_hedges__new
        ,hedge2another_vertex=hedge2another_vertex__new
        ,hedge2unstable_iter_other_hedges_around_another_vertex
            =hedge2unstable_iter_other_hedges_around_another_vertex__new
        ,maybe_ancestor_vertex_stack=ancestor_vertices
        ,maybe_ancestor_hedge_stack=ancestor_hedges__new
        )
    for case, payload in it__new:
        if case == _DFS_Case.DFS_EnterRootVertex:
            vertex = payload
            yield DFS_Case.DFS_EnterVertex, ancestor_vertices.get_top()
        elif case == _DFS_Case.DFS_ExitRootVertex:
            vertex = payload
            yield DFS_Case.DFS_ExitVertex, ancestor_vertices.get_top()
        elif case == _DFS_Case.DFS_EnterTreeHEdge:
            hedge, vertex = payload
            yield DFS_Case.DFS_EnterVertex, ancestor_vertices.get_top()
        elif case == _DFS_Case.DFS_ExitTreeHEdge:
            assert payload is None
            yield DFS_Case.DFS_ExitVertex, ancestor_vertices.get_top()
        elif case == _DFS_Case.DFS_EnterExitBackHEdge:
            raise logic-error or not uforest
        else:
            raise unknown-case

def _dfs__sourced_finite_implicit_uforest_with_vertex_eq__basic_ver1(*
    ,source_vertices
    ,vertex_eq
    ,vertex2unstable_iter_hedges
    ,hedge2another_vertex

    ,ancestor_hedges
    ,ancestor_vertices
    ):
    def iter_child_pairs__root(root_vertex):
        for hedge in vertex2unstable_iter_hedges(root_vertex):
            child_vertex = hedge2another_vertex(hedge)
            yield hedge, child_vertex
    def iter_child_pairs(parent_vertex, vertex):
        for hedge in vertex2unstable_iter_hedges(vertex):
            child_vertex = hedge2another_vertex(hedge)
            if not vertex_eq(parent_vertex, child_vertex):
                yield hedge, child_vertex




    iterator_stack = []

    for root_vertex in source_vertices:
        assert not iterator_stack
        assert ancestor_vertices.is_empty()
        assert ancestor_hedges.is_empty()

        iterator_stack.append(iter_child_pairs__root(root_vertex))
        ancestor_vertices.push(root_vertex)
        # len(ancestor_hedges) + 1 == len(ancestor_vertices) == len(iterator_stack)
        yield DFS_Case.DFS_EnterVertex, root_vertex

        while True:
            #assert len(iterator_stack) == len(ancestor_vertices) == len(ancestor_hedges) + 1

            for hedge, vertex in iterator_stack[-1]:
                break
            else:
                if ancestor_hedges.is_empty():
                    break
                else:
                    vertex = ancestor_vertices.get_top()
                    yield DFS_Case.DFS_ExitVertex, vertex
                    iterator_stack.pop()
                    ancestor_vertices.pop_None()
                    ancestor_hedges.pop_None()
                    continue

            parent_vertex = ancestor_vertices.get_top()
            iterator_stack.append(iter_child_pairs(parent_vertex, vertex))
            ancestor_vertices.push(vertex)
            ancestor_hedges.push(hedge)
            yield DFS_Case.DFS_EnterVertex, vertex

        yield DFS_Case.DFS_ExitVertex, root_vertex
        iterator_stack.pop()
        ancestor_vertices.pop_None()

if __name__ == "__main__":
    import doctest
    doctest.testmod()




