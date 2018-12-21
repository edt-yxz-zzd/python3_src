
'''
dfs__finite_explicit_ugraph
    common from:
        dfs__finite_explicit_xgraph
        dfs__sourced_finite_implicit_uforest_with_vertex_eq


expected:
    vs dfs__finite_explicit_xgraph
        donot treat hedge2another_hedge[back_hedge] as forward_hedge
but actually:
    since using only 2 colors!
    has forward_hedge
    weired dfs:
        hedge2another_hedge[tree_hedge] is not back_hedge
        back_hedge pair with forward_hedge
'''


__all__ = '''
    DFS_Case
    DFS_CaseParts

    IVertex2TwoColor
    dfs__finite_explicit_ugraph

    Vertex2TwoColor__no_effect
    Vertex2TwoColor__seq
    Vertex2TwoColor__set
    the_vertex2two_color__no_effect
    make_hedge2unstable_iter_other_hedges_around_another_vertex
    '''.split()


from .make_hedge2unstable_iter_other_hedges_around_another_vertex \
    import make_hedge2unstable_iter_other_hedges_around_another_vertex

#from ..stack.ICompleteMutableStack import ICompleteMutableStack
from ..stack.INearlyCompleteMutableStack import INearlyCompleteMutableStack
#from ..stack.SeqAsCompleteMutableStack import SeqAsCompleteMutableStack
from ..stack.NearlyCompleteMutableStack import NearlyCompleteMutableStack
from .abc import ABC, abstractmethod, override

import enum
from .Enum__NoShowValue import Enum__NoShowValue

"""
DFS_Case = enum.Enum('DFS_Case', '''
    DFS_EnterRootVertex
    DFS_ExitRootVertex

    DFS_EnterTreeHEdge
    DFS_ExitTreeHEdge

    DFS_EnterExitBackOrForwardHEdge
    '''.split()
    )
"""

def _mk_frozenset(s):
    for name in s.split():
        assert name == getattr(DFS_CaseParts, name)
    return frozenset(s.split())

class DFS_CaseParts:pass
def _fill_DFS_CaseParts():
    #DFS_CaseParts.__dict__.update (name, name) for name in '''
    attrs = '''
    DFS
    Enter
    Exit
    Root
    Vertex
    RootVertex
    Tree
    HEdge
    TreeHEdge
    EnterExit
    Back
    Forward
    BackHEdge
    ForwardHEdge
    '''.split()
    for name in attrs:
        setattr(DFS_CaseParts, name, name)
_fill_DFS_CaseParts()

class DFS_Case(Enum__NoShowValue):
    DFS_EnterRootVertex = _mk_frozenset('DFS Enter Root Vertex RootVertex')
    DFS_ExitRootVertex = _mk_frozenset('DFS Exit Root Vertex RootVertex')

    DFS_EnterTreeHEdge = _mk_frozenset('DFS Enter Tree HEdge TreeHEdge')
    DFS_ExitTreeHEdge = _mk_frozenset('DFS Exit Tree HEdge TreeHEdge')

    DFS_EnterExitBackOrForwardHEdge = _mk_frozenset('DFS Enter Exit EnterExit Back Forward HEdge BackHEdge ForwardHEdge')


class IVertex2TwoColor(ABC):
    @abstractmethod
    def is_vertex_colored_WHITE(self, vertex):
        # vertex -> bool
        pass
    @abstractmethod
    def set_vertex_color_WHITE(self, vertex):
        # vertex -> None
        pass


class Vertex2TwoColor__no_effect(IVertex2TwoColor):
    @override
    def is_vertex_colored_WHITE(self, vertex):
        return False
    @override
    def set_vertex_color_WHITE(self, vertex):
        pass
the_vertex2two_color__no_effect = Vertex2TwoColor__no_effect()

class Vertex2TwoColor__seq(IVertex2TwoColor):
    def __init__(self, underlying_seq, WHITE):
        self.underlying_seq = underlying_seq
        self.WHITE = WHITE
    @override
    def is_vertex_colored_WHITE(self, vertex):
        return self.underlying_seq[vertex] is self.WHITE
    @override
    def set_vertex_color_WHITE(self, vertex):
        self.underlying_seq[vertex] = self.WHITE


class Vertex2TwoColor__set(IVertex2TwoColor):
    def __init__(self, underlying_set):
        self.underlying_set = underlying_set
    @override
    def is_vertex_colored_WHITE(self, vertex):
        return vertex in self.underlying_set
    @override
    def set_vertex_color_WHITE(self, vertex):
        self.underlying_set.add(vertex)

def dfs__finite_explicit_ugraph(*
    ,source_vertices
    ,vertex2color
    ,vertex2unstable_iter_hedges
    ,hedge2another_vertex
    ,hedge2unstable_iter_other_hedges_around_another_vertex

    ,maybe_ancestor_hedge_stack = None
    ,maybe_ancestor_vertex_stack = None
    ):
    '''
ugraph ==>> tree_edge|back_edge|forward_edge
    no cross_edge...
    # deprecated: no forward_edge/cross_edge...

    hedge2another_hedge[back_hedge] == forward_hedge
    use only 2-colors: BLACK/WHITE

input:
    source_vertices :: Iter Vertex
        possible roots
        allow duplicated
        allow missing
            if donot want to dfs whole graph
            or known vertex in same connected component is chosen
    vertex2color :: IVertex2TwoColor
        {.set_vertex_color_WHITE :: Vertex -> None
        ,.is_vertex_colored_WHITE :: Vertex -> Bool
        }

        allow no-effect set_vertex_color_WHITE
            for uforest:
                vertex2color.set_vertex_color_WHITE(vertex)
                neednot: vertex2color.is_vertex_colored_WHITE(vertex)

        allow some vertex with WHITE color
            as-if colored by prev dfs

        allow partial_mapping
            missing ==>> BLACK
        allow full_mapping

        neednot have 'len'

    vertex2unstable_iter_hedges :: Vertex -> Iter HEdge
    hedge2another_vertex :: HEdge -> Vertex
    hedge2unstable_iter_other_hedges_around_another_vertex
        :: HEdge -> Iter HEdge
        impl:
            * may use vertex_eq/hedge_eq in impl
            * may be a ???dgraph???
        set(hedge2unstable_iter_other_hedges_around_another_vertex(hedge)) == set(vertex2unstable_iter_hedges(hedge2another_vertex(hedge))) - {hedge2another_hedge(hedge)}

inout:
    maybe_ancestor_hedge_stack :: None|INearlyCompleteMutableStack
    maybe_ancestor_vertex_stack :: None|INearlyCompleteMutableStack
        NearlyCompleteMutableStack
        SeqAsCompleteMutableStack

output:
    Iter (DFS_Case, payload)
        (DFS_EnterRootVertex, Vertex)
        (DFS_ExitRootVertex, Vertex)
        (DFS_EnterTreeHEdge, (HEdge, Vertex))
        (DFS_ExitTreeHEdge, None)
        (DFS_EnterExitBackOrForwardHEdge, (HEdge, Vertex))
            where pair s.t. vertex = hedge2another_vertex(hedge)


example:
    vertex2unstable_iter_hedges :: Vertex -> Iter HEdge
    hedge2another_vertex :: HEdge -> Vertex
    hedge2unstable_iter_other_hedges_around_another_vertex
    >>> this = dfs__finite_explicit_ugraph
    >>> source_vertices = '0a1'
    >>> vertex2color = Vertex2TwoColor__no_effect()
    >>> d = {'a':'bc', 'b':'a', 'c':'ad', 'd':'c', '0':'1', '1':'0'}#tree
    >>> vertex2unstable_iter_hedges = lambda v:((v,u) for u in d[v])
    >>> hedge2another_vertex = lambda pair:pair[-1]
    >>> hedge2unstable_iter_other_hedges_around_another_vertex = lambda pair:((pair[-1], u) for u in d[pair[-1]] if u != pair[0])
    >>> it = this(source_vertices=source_vertices, vertex2color=vertex2color, vertex2unstable_iter_hedges=vertex2unstable_iter_hedges, hedge2another_vertex=hedge2another_vertex, hedge2unstable_iter_other_hedges_around_another_vertex=hedge2unstable_iter_other_hedges_around_another_vertex)
    >>> list(it)
    [(<DFS_Case.DFS_EnterRootVertex>, '0'), (<DFS_Case.DFS_EnterTreeHEdge>, (('0', '1'), '1')), (<DFS_Case.DFS_ExitTreeHEdge>, None), (<DFS_Case.DFS_ExitRootVertex>, '0'), (<DFS_Case.DFS_EnterRootVertex>, 'a'), (<DFS_Case.DFS_EnterTreeHEdge>, (('a', 'b'), 'b')), (<DFS_Case.DFS_ExitTreeHEdge>, None), (<DFS_Case.DFS_EnterTreeHEdge>, (('a', 'c'), 'c')), (<DFS_Case.DFS_EnterTreeHEdge>, (('c', 'd'), 'd')), (<DFS_Case.DFS_ExitTreeHEdge>, None), (<DFS_Case.DFS_ExitTreeHEdge>, None), (<DFS_Case.DFS_ExitRootVertex>, 'a'), (<DFS_Case.DFS_EnterRootVertex>, '1'), (<DFS_Case.DFS_EnterTreeHEdge>, (('1', '0'), '0')), (<DFS_Case.DFS_ExitTreeHEdge>, None), (<DFS_Case.DFS_ExitRootVertex>, '1')]


'''
    assert isinstance(vertex2color, IVertex2TwoColor)

    if maybe_ancestor_hedge_stack is None:
        ancestor_hedges = NearlyCompleteMutableStack()
    else:
        ancestor_hedges = maybe_ancestor_hedge_stack
        if not isinstance(ancestor_hedges, INearlyCompleteMutableStack): raise TypeError
        if not ancestor_hedges.is_empty(): raise ValueError

    if maybe_ancestor_vertex_stack is None:
        ancestor_vertices = NearlyCompleteMutableStack()
    else:
        ancestor_vertices = maybe_ancestor_vertex_stack
        if not isinstance(ancestor_vertices, INearlyCompleteMutableStack): raise TypeError
        if not ancestor_vertices.is_empty(): raise ValueError









    iterator_stack = []
    #ancestor_hedges = []
    #ancestor_vertices = []

    for root_vertex in source_vertices:
        assert not iterator_stack
        assert ancestor_vertices.is_empty()
        assert ancestor_hedges.is_empty()

        if vertex2color.is_vertex_colored_WHITE(root_vertex): continue
        vertex2color.set_vertex_color_WHITE(root_vertex)

        iterator_stack.append(vertex2unstable_iter_hedges(root_vertex))
        ancestor_vertices.push(root_vertex)
        yield DFS_Case.DFS_EnterRootVertex, root_vertex

        while True:
            #assert len(iterator_stack) == len(ancestor_vertices) == len(ancestor_hedges)+1
            for hedge in iterator_stack[-1]:
                break
            else:
                if ancestor_hedges.is_empty():
                    break
                else:
                    yield DFS_Case.DFS_ExitTreeHEdge, None
                    iterator_stack.pop()
                    ancestor_vertices.pop_None()
                    ancestor_hedges.pop_None()
                    continue

            vertex = hedge2another_vertex(hedge)
            if vertex2color.is_vertex_colored_WHITE(vertex):
                # back_edge
                ancestor_hedges.push(hedge)
                ancestor_vertices.push(vertex)
                yield DFS_Case.DFS_EnterExitBackOrForwardHEdge, (hedge, vertex)
                ancestor_hedges.pop_None()
                ancestor_vertices.pop_None()
                continue

            # tree_edge
            vertex2color.set_vertex_color_WHITE(vertex)
            ancestor_hedges.push(hedge)
            ancestor_vertices.push(vertex)
            iterator_stack.append(hedge2unstable_iter_other_hedges_around_another_vertex(hedge))
            yield DFS_Case.DFS_EnterTreeHEdge, (hedge, vertex)

        yield DFS_Case.DFS_ExitRootVertex, root_vertex
        iterator_stack.pop()
        ancestor_vertices.pop_None()





if __name__ == "__main__":
    import doctest
    doctest.testmod()




