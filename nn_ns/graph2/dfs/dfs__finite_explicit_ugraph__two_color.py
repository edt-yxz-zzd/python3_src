
'''
dfs__finite_explicit_ugraph__two_color
    common from:
        dfs__finite_explicit_xgraph
        dfs__sourced_finite_implicit_uforest_with_vertex_eq


NOTE: 4 hedge types
    rback_hedge = hedge2another_hedge[back_hedge]
        rback_hedge is not forward_hedge
    expected:
        vs dfs__finite_explicit_xgraph
            dfs__finite_explicit_xgraph:
                distinguish back_hedge and rback_hedge
                back_hedge - EnterBackHEdge
                rback_hedge in concept - ExitBackHEdge
                i.e. in "ONE" EnterExitBackHEdge
                    we visit both back_hedge and rback_hedge at same time
            dfs__finite_explicit_ugraph__two_color:
                donot distinguish back_hedge and rback_hedge
                    since using only 2 colors!
                back_hedge - DFS_EnterExitBackOrRBackHEdge
                rback_hedge - DFS_EnterExitBackOrRBackHEdge
                i.e. in "TWO" EnterExitBackOrRBackHEdge
                    we visit back_hedge and rback_hedge seperately

    weired dfs:
        hedge2another_hedge[tree_hedge] is not back_hedge/rback_hedge
            we may call it rtree_hedge
        back_hedge is paired with rback_hedge

    4 hedge types:
        tree_hedge - DFS_EnterTreeHEdge
        rtree_hedge in concept - DFS_ExitTreeHEdge
            actually ancestor_hedges.get_top() is tree_hedge
        back_hedge/rback_hedge - DFS_EnterExitBackOrRBackHEdge

'''


__all__ = '''
    DFS_Case
    DFS_CaseParts

    IVertex2TwoColor
    dfs__finite_explicit_ugraph__two_color

    dfs__finite_explicit_ugraph__two_color__basic
    dfs__finite_explicit_ugraph__two_color__source_vertex
    dfs__finite_explicit_ugraph__two_color__source_hedge
    dfs__finite_explicit_ugraph__two_color__source_either

    make_hedge2unstable_iter_other_hedges_around_another_vertex
    '''.split()

'''
    Vertex2TwoColor__no_effect
    Vertex2TwoColor__seq
    Vertex2TwoColor__set
    the_vertex2two_color__no_effect

'''

from .make_hedge2unstable_iter_other_hedges_around_another_vertex \
    import make_hedge2unstable_iter_other_hedges_around_another_vertex
from .Vertex2TwoColor.IVertex2TwoColor import IVertex2TwoColor
from .Vertex2TwoColor.Vertex2TwoColor__no_effect import Vertex2TwoColor__no_effect

#from ..stack.ICompleteMutableStack import ICompleteMutableStack
from ..stack.INearlyCompleteMutableStack import INearlyCompleteMutableStack
#from ..stack.SeqAsCompleteMutableStack import SeqAsCompleteMutableStack
from ..stack.NearlyCompleteMutableStack import NearlyCompleteMutableStack
from .abc import ABC, abstractmethod, override
from seed.tiny import echo

import enum
from .Enum__NoShowValue import Enum__NoShowValue

"""
DFS_Case = enum.Enum('DFS_Case', '''
    DFS_EnterRootVertex
    DFS_ExitRootVertex

    DFS_EnterTreeHEdge
    DFS_ExitTreeHEdge

    DFS_EnterExitBackOrRBackHEdge
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
    RBack
    BackHEdge
    RBackHEdge
    '''.split()
    for name in attrs:
        setattr(DFS_CaseParts, name, name)
_fill_DFS_CaseParts()

class DFS_Case(Enum__NoShowValue):
    DFS_EnterRootVertex = _mk_frozenset('DFS Enter Root Vertex RootVertex')
    DFS_ExitRootVertex = _mk_frozenset('DFS Exit Root Vertex RootVertex')

    DFS_EnterTreeHEdge = _mk_frozenset('DFS Enter Tree HEdge TreeHEdge')
    DFS_ExitTreeHEdge = _mk_frozenset('DFS Exit Tree HEdge TreeHEdge')

    DFS_EnterExitBackOrRBackHEdge = _mk_frozenset('DFS Enter Exit EnterExit Back RBack HEdge BackHEdge RBackHEdge')


def dfs__finite_explicit_ugraph__two_color__source_vertex(*
    ,source_vertices
    ,vertex2color
    ,vertex2unstable_iter_hedges
    ,hedge2another_vertex
    ,hedge2unstable_iter_other_hedges_around_another_vertex

    ,maybe_ancestor_hedge_stack = None
    ,maybe_ancestor_vertex_stack = None
    ):
    '''
ugraph ==>> tree_edge|rtree_hedge|back_edge|rback_hedge
    no forward_edge/cross_edge...

    hedge2another_hedge[back_hedge] == rback_hedge
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
        (DFS_EnterExitBackOrRBackHEdge, (HEdge, Vertex))
            where pair s.t. vertex = hedge2another_vertex(hedge)


example:
    vertex2unstable_iter_hedges :: Vertex -> Iter HEdge
    hedge2another_vertex :: HEdge -> Vertex
    hedge2unstable_iter_other_hedges_around_another_vertex
    >>> this = dfs__finite_explicit_ugraph__two_color__source_vertex
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
    return dfs__finite_explicit_ugraph__two_color__basic(
            sources = source_vertices
            ,source2vertex = echo
            ,source2unstable_iter_hedges
                = vertex2unstable_iter_hedges

            ,vertex2color
                = vertex2color
            ,hedge2another_vertex
                = hedge2another_vertex
            ,hedge2unstable_iter_other_hedges_around_another_vertex
                = hedge2unstable_iter_other_hedges_around_another_vertex

            ,maybe_ancestor_hedge_stack
                = maybe_ancestor_hedge_stack
            ,maybe_ancestor_vertex_stack
                = maybe_ancestor_vertex_stack
        )

class make_kwargs4dfs__finite_explicit_ugraph__two_color__basic:
    def from_kwargs__source_hedge(*
        ,hedge2another_hedge
        ,hedge2unstable_iter_other_hedges_around_another_vertex
        ,hedge2vertex
        ):
        # -> (hedge2another_vertex, hedge2unstable_iter_hedges)
        # for dfs__finite_explicit_ugraph__two_color__source_hedge
        def hedge2unstable_iter_hedges(hedge):
            yield hedge
            other = hedge2another_hedge(hedge)
            yield from hedge2unstable_iter_other_hedges_around_another_vertex(other)
        def hedge2another_vertex(hedge):
            other = hedge2another_hedge(hedge)
            return hedge2vertex(other)
        return hedge2another_vertex, hedge2unstable_iter_hedges
    def from_kwargs__source_either__less(*
        ,hedge2vertex
        ,vertex2unstable_iter_hedges
        ,hedge2unstable_iter_hedges
        ):
        # -> (either2vertex, either2unstable_iter_hedges)
        def either2vertex(either):
            is_vertex, hedge_or_vertex = either
            if is_vertex:
                vertex = hedge_or_vertex
            else:
                hedge = hedge_or_vertex
                vertex = hedge2vertex(hedge)
            return vertex
        def either2unstable_iter_hedges(either):
            is_vertex, hedge_or_vertex = either
            if is_vertex:
                vertex = hedge_or_vertex
                hedges = vertex2unstable_iter_hedges(vertex)
            else:
                hedge = hedge_or_vertex
                hedges = hedge2unstable_iter_hedges(hedge)
            return hedges
        return (either2vertex, either2unstable_iter_hedges)

    def from_kwargs__source_either(*
        ,hedge2vertex
        ,vertex2unstable_iter_hedges
        ,hedge2another_hedge
        ,hedge2unstable_iter_other_hedges_around_another_vertex
        ):
        # -> (either2vertex, either2unstable_iter_hedges, hedge2another_vertex)
        # for dfs__finite_explicit_ugraph__two_color__source_either

        def hedge2unstable_iter_hedges(hedge):
            yield hedge
            other = hedge2another_hedge(hedge)
            yield from hedge2unstable_iter_other_hedges_around_another_vertex(other)
        def hedge2another_vertex(hedge):
            other = hedge2another_hedge(hedge)
            return hedge2vertex(other)

        (either2vertex, either2unstable_iter_hedges
        ) = __class__.from_kwargs__source_either__less(
            hedge2vertex = hedge2vertex
            ,vertex2unstable_iter_hedges = vertex2unstable_iter_hedges
            ,hedge2unstable_iter_hedges = hedge2unstable_iter_hedges
            )
        return (either2vertex, either2unstable_iter_hedges, hedge2another_vertex)

def dfs__finite_explicit_ugraph__two_color__source_hedge(*
    #,source_vertices
    ,source_hedges
    ,vertex2color
    ,hedge2vertex
    ,hedge2another_hedge
    #,hedge2another_vertex
    ,hedge2unstable_iter_other_hedges_around_another_vertex

    ,maybe_ancestor_hedge_stack = None
    ,maybe_ancestor_vertex_stack = None
    ):
    '''
input:
    source_hedges :: Iter HEdge
        possible root_hedges
    hedge2vertex :: HEdge -> Vertex
    hedge2another_hedge :: HEdge -> HEdge
    ...other parameters
        see: dfs__finite_explicit_ugraph__two_color__source_vertex
'''
    (hedge2another_vertex, hedge2unstable_iter_hedges
    ) = make_kwargs4dfs__finite_explicit_ugraph__two_color__basic \
        .from_kwargs__source_hedge(
            hedge2another_hedge
                = hedge2another_hedge
            ,hedge2unstable_iter_other_hedges_around_another_vertex
                = hedge2unstable_iter_other_hedges_around_another_vertex
            ,hedge2vertex
                = hedge2vertex
            )

    return dfs__finite_explicit_ugraph__two_color__basic(
            sources = source_hedges
            ,source2vertex = hedge2vertex
            ,source2unstable_iter_hedges = hedge2unstable_iter_hedges
            ,hedge2another_vertex = hedge2another_vertex

            ,vertex2color
                = vertex2color
            ,hedge2unstable_iter_other_hedges_around_another_vertex
                = hedge2unstable_iter_other_hedges_around_another_vertex
            ,maybe_ancestor_hedge_stack
                = maybe_ancestor_hedge_stack
            ,maybe_ancestor_vertex_stack
                = maybe_ancestor_vertex_stack
            )


def dfs__finite_explicit_ugraph__two_color__source_either(*
    #,source_vertices
    ,source_eithers
    ,vertex2color
    ,vertex2unstable_iter_hedges
    ,hedge2vertex
    ,hedge2another_hedge
    #,hedge2another_vertex
    ,hedge2unstable_iter_other_hedges_around_another_vertex

    ,maybe_ancestor_hedge_stack = None
    ,maybe_ancestor_vertex_stack = None
    ):
    '''
input:
    source_eithers :: Iter ((False, HEdge)|(True, Vertex,))
        eithers of possible root_hedge or root_vertex
    hedge2vertex :: HEdge -> Vertex
    hedge2another_hedge :: HEdge -> HEdge
    ...other parameters
        see: dfs__finite_explicit_ugraph__two_color__source_vertex
'''
    (either2vertex
    ,either2unstable_iter_hedges
    ,hedge2another_vertex
    ) = make_kwargs4dfs__finite_explicit_ugraph__two_color__basic \
        .from_kwargs__source_either(
            hedge2vertex
                = hedge2vertex
            ,vertex2unstable_iter_hedges
                = vertex2unstable_iter_hedges
            ,hedge2another_hedge
                = hedge2another_hedge
            ,hedge2unstable_iter_other_hedges_around_another_vertex
                = hedge2unstable_iter_other_hedges_around_another_vertex
            )


    return dfs__finite_explicit_ugraph__two_color__basic(
            sources = source_eithers
            ,source2vertex = either2vertex
            ,source2unstable_iter_hedges = either2unstable_iter_hedges
            ,hedge2another_vertex = hedge2another_vertex

            ,vertex2color
                = vertex2color
            ,hedge2unstable_iter_other_hedges_around_another_vertex
                = hedge2unstable_iter_other_hedges_around_another_vertex
            ,maybe_ancestor_hedge_stack
                = maybe_ancestor_hedge_stack
            ,maybe_ancestor_vertex_stack
                = maybe_ancestor_vertex_stack
            )



def dfs__finite_explicit_ugraph__two_color__basic(*
    #,source_vertices
    ,sources
    ,vertex2color
    #,vertex2unstable_iter_hedges
    ,source2vertex
    ,source2unstable_iter_hedges
    ,hedge2another_vertex
    ,hedge2unstable_iter_other_hedges_around_another_vertex

    ,maybe_ancestor_hedge_stack
    ,maybe_ancestor_vertex_stack
    ):
    '''
input:
    sources :: Iter Source
        Source is opaque type
        why?
            to support root_hedge
    source2vertex :: Source -> Vertex
    source2unstable_iter_hedges :: Source -> Iter HEdge
    ...other parameters
        see: dfs__finite_explicit_ugraph__two_color__source_vertex
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

    #for root_vertex in source_vertices:
    for source in sources:
        assert not iterator_stack
        assert ancestor_vertices.is_empty()
        assert ancestor_hedges.is_empty()

        root_vertex = source2vertex(source)
        if vertex2color.is_vertex_colored_WHITE(root_vertex): continue
        vertex2color.set_vertex_color_WHITE(root_vertex)

        #hedges_around_root_vertex = vertex2unstable_iter_hedges(root_vertex)
        hedges_around_root_vertex = source2unstable_iter_hedges(source)
        iterator_stack.append(hedges_around_root_vertex)
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
                yield DFS_Case.DFS_EnterExitBackOrRBackHEdge, (hedge, vertex)
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


class dfs__finite_explicit_ugraph__two_color:
    '''
common:
    vertex2color
    hedge2unstable_iter_other_hedges_around_another_vertex
    maybe_ancestor_hedge_stack
    maybe_ancestor_vertex_stack

via_source_vertices:
    ,source_vertices
    ,vertex2unstable_iter_hedges
    ,hedge2another_vertex

via_source_hedges
    ,source_hedges
    ,hedge2vertex
    ,hedge2another_hedge

via_source_eithers
    ,source_eithers
    ,vertex2unstable_iter_hedges
    ,hedge2vertex
    ,hedge2another_hedge

via_opaque_sources
    ,sources
    ,source2vertex
    ,source2unstable_iter_hedges
    ,hedge2another_vertex

'''
    via_source_vertices = dfs__finite_explicit_ugraph__two_color__source_vertex
    via_source_hedges = dfs__finite_explicit_ugraph__two_color__source_hedge
    via_source_eithers = dfs__finite_explicit_ugraph__two_color__source_either
    via_opaque_sources = dfs__finite_explicit_ugraph__two_color__basic

    make_kwargs4via_opaque_sources = make_kwargs4dfs__finite_explicit_ugraph__two_color__basic



if __name__ == "__main__":
    import doctest
    doctest.testmod()




