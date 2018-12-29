

__all__ = '''
    relabel_ugraph__prime
    '''.split()

from .relabel_XXX2YYY import relabel_XXX2YYY

def relabel_ugraph__prime(*
    #,num_vertices
    ,old_hedge2old_vertex
    ,old_hedge2old_aedge

    ,new_hedge2old_hedge
    ,old_vertex2new_vertex
    ,old_aedge2new_aedge
    ):
    '-> (new_hedge2new_vertex, new_hedge2new_aedge)'

    new_hedge2new_vertex = relabel_XXX2YYY(
        old_XXX2old_YYY=old_hedge2old_vertex
        ,new_XXX2old_XXX=new_hedge2old_hedge
        ,old_YYY2new_YYY=old_vertex2new_vertex
        )
    new_hedge2new_aedge = relabel_XXX2YYY(
        old_XXX2old_YYY=old_hedge2old_aedge
        ,new_XXX2old_XXX=new_hedge2old_hedge
        ,old_YYY2new_YYY=old_aedge2new_aedge
        )
    return new_hedge2new_vertex, new_hedge2new_aedge


