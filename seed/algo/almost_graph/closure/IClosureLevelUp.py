#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/almost_graph/closure/IClosureLevelUp.py

seed.algo.almost_graph.closure.IClosureLevelUp
py -m nn_ns.app.debug_cmd   seed.algo.almost_graph.closure.IClosureLevelUp -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.almost_graph.closure.IClosureLevelUp:__doc__ -ht # -ff -df
#######

[[
源起:
view script/helper4Framework4Translation__ver5__api_only.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.algo.almost_graph.closure.IClosureLevelUp   @f
]]]'''#'''
__all__ = r'''
IClosureLevelUp
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
from seed.abc.abc__ver1 import abstractmethod, override, ABC

from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
lazy_import4funcs_('seed.tiny_.types5py', 'mk_MapView', __name__)
if 0:from seed.tiny_.types5py import mk_MapView#curry1,kwargs2Attrs #,MapView

___end_mark_of_excluded_global_names__0___ = ...


__all__



class IClosureLevelUp(ABC):
    'mimic:bfs/(breadth-first-search)'
    r'''
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.algo.almost_graph.closure.IClosureLevelUp:IClosureLevelUp@T    =T   +exclude_attrs5listed_in_cls_doc

new_abstract_methods:
    `_iter_derive_child_vertices_when_new_vtx_induced_
new_concrete_methods:
    ___no_slots_ok___
    on_vertex_added_
    on_vertex_processed_
    __init__
    inflate_closure__via_progressively_levelup_
    _add_vtx_to_be_processed
    vertex2level_
    is_processed_vtx_
    iter_processed_vtc_now_
    iter_processed_vtc_at_level_

    '''#'''
    ___no_slots_ok___ = True
    @abstractmethod
    def _iter_derive_child_vertices_when_new_vtx_induced_(sf, lvl, v, processed_vtc, /):
        'lvl/level{v}/uint -> v/vtx/vertex -> Iter vtx -> (Iter vtx){expect generate vertices of next level; but arbitrary vertices are ok}'
    def on_vertex_added_(sf, lvl, v, /):
        'lvl/level{v}/uint -> v/vtx/vertex -> None'
    def on_vertex_processed_(sf, lvl, v, /):
        'lvl/level{v}/uint -> v/vtx/vertex -> None'
    def __init__(sf, src_vtc, /):
        #sf._vs = iter(src_vtc)
        sf._lvl2vtc = [[]]
        sf._vtx2lvl = {}
        sf._processed_vtc = set()
        sf._lvl = 0
            # min lvl for unprocessed_vtc
        sf._j = 0
            # begin idx for unprocessed_vtc@sf._lvl2vtc[sf._lvl]

        lvl = 0
        for v in src_vtc:
            sf._add_vtx_to_be_processed(lvl, v)

    def inflate_closure__via_progressively_levelup_(sf, /):
        '-> (lvl2vtc, vtx2lvl)/([[vtx]], {vtx:lvl}) #donot run twice #mimic:bfs/(breadth-first-search)'
        vss = sf._lvl2vtc
        lvl = sf._lvl
        if not lvl == len(vss)-1: raise 000
        if not sf._j == 0: raise 000
        while vss[-1]:
            assert sf._j == 0
            vs = vss[-1]
            vss.append([])
            _lvl = lvl+1
            if not _lvl == len(vss)-1: raise 000
            for sf._j, v in enumerate(vs):
                processed_vtc = sf.iter_processed_vtc_now_()
                for _v in sf._iter_derive_child_vertices_when_new_vtx_induced_(lvl, v, processed_vtc):
                    sf._add_vtx_to_be_processed(_lvl, _v)
                v
                sf._processed_vtc.add(v)
                sf.on_vertex_processed_(lvl, v)
            sf._lvl = lvl = _lvl
            sf._j = 0
        if not sf._lvl == len(vss)-1: raise 000
        if not sf._j == 0: raise 000
        lvl2vtc = tuple(map(tuple, vss))
        vtx2lvl = mk_MapView(sf._vtx2lvl)
        sf._lvl2vtc = lvl2vtc
        sf._vtx2lvl = vtx2lvl
        return (lvl2vtc, vtx2lvl)
    def _add_vtx_to_be_processed(sf, lvl, v, /):
        vss = sf._lvl2vtc
        d = sf._vtx2lvl
        if not lvl == len(vss)-1: raise 000
        if v in d:
            if not d[v] <= lvl: raise 000
            return
        d[v] = lvl
        vss[-1].append(v)
        sf.on_vertex_added_(lvl, v)
    def vertex2level_(sf, v, /):
        return sf._vtx2lvl[v]
    def is_processed_vtx_(sf, v, /):
        return v in sf._processed_vtc
    def iter_processed_vtc_now_(sf, /):
        #bug:return iter(sf._processed_vtc)
        vss = sf._lvl2vtc
        lvl = sf._lvl
        j = sf._j
        # snapshot: lvl,j
        for vs in islice(vss, 0, lvl):
            yield from vs
        vs = vss[lvl]
        return islice(vs, 0, j)

    def iter_processed_vtc_at_level_(sf, lvl, /):
        check_int_ge(0, lvl)
        vs = sf._lvl2vtc[lvl]
        if lvl < sf._lvl:
            return iter(vs)
        elif lvl > sf._lvl:
            #return null_iter
            return iter('')
        return islice(vs, 0, sf._j)
#end-class IClosureLevelUp(ABC):

















__all__
from seed.algo.almost_graph.closure.IClosureLevelUp import IClosureLevelUp
from seed.algo.almost_graph.closure.IClosureLevelUp import *
