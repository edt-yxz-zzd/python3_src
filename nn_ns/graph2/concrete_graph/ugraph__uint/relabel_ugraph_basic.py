
__all__ = '''
    relabel_ugraph_basic
    '''.split()

from .UGraphBasic import UGraphBasic
from .UGraphLabelling import UGraphLabelling
from .relabel_ugraph__prime import relabel_ugraph__prime

def relabel_ugraph_basic(*
    ,ugraph_basic__old
    ,ugraph_labelling__old2new
    ):
    '''UGraphBasic -> UGraphLabelling -> UGraphBasic
ugraph_basic__old -> ugraph_labelling__old2new -> ugraph_basic__new
'''
    assert isinstance(ugraph_basic__old, UGraphBasic)
    assert isinstance(ugraph_labelling__old2new, UGraphLabelling)
    if ugraph_basic__old.num_vertices != ugraph_labelling__old2new.num_vertices: raise ValueError
    if ugraph_basic__old.num_aedges != ugraph_labelling__old2new.num_aedges: raise ValueError
    if ugraph_basic__old.num_hedges != ugraph_labelling__old2new.num_hedges: raise ValueError

    (new_hedge2new_vertex, new_hedge2new_aedge
    ) = relabel_ugraph__prime(
        old_hedge2old_vertex=ugraph_basic__old.hedge2vertex
        ,old_hedge2old_aedge=ugraph_basic__old.hedge2aedge

        ,new_hedge2old_hedge=ugraph_labelling__old2new.old_hedge2new_hedge.backward_mapping
        ,old_vertex2new_vertex=ugraph_labelling__old2new.old_vertex2new_vertex.forward_mapping
        ,old_aedge2new_aedge=ugraph_labelling__old2new.old_aedge2new_aedge.forward_mapping
        )

    ugraph_basic__new = UGraphBasic.make_UGraphBasic__simplest(
        ,num_vertices = ugraph_basic__old.num_vertices
        ,hedge2vertex = new_hedge2new_vertex
        ,hedge2aedge = new_hedge2new_aedge
        )
    return ugraph_basic__new

