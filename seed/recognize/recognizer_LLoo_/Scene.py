#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/Scene.py

seed.recognize.recognizer_LLoo_.Scene
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.Scene -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.Scene:__doc__ -ht
#]]]'''
__all__ = r'''
mk_Scene_ex
SceneView
Scene
    Scene__register
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.recognizer_LLoo_._common import (
null_iter
,check_type_le, check_type_is
,abstractmethod, override, ABC, ABC__no_slots
,_Base4repr#_args4repr
, KindedName #,Cased # Either
)


from seed.recognize.recognizer_LLoo_.IScene import IScene , IScene__register
from collections.abc import Hashable as IHashable, Mapping as IMapping
from seed.tiny_.dict_op__add import dict_add, set_add
___end_mark_of_excluded_global_names__0___ = ...


class Scene(IScene, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, knm2obj, /):
        check_type_le(IMapping, knm2obj)
        sf._d = knm2obj
        sf._args4repr = (knm2obj,)
            #_Base4repr
    @override
    def check_kinded_name(sf, kinded_name, /):
        '-> None | ^TypeError'
        check_type_is(KindedName, kinded_name)
        if 0:
            kind, nm = kinded_name
            check_type_le(type, kind)
            #check_type_le(kind, obj)
            check_type_le(IHashable, nm)
    @override
    def _lookup_(sf, kinded_name, /):
        '-> obj | ^KeyError'
        return sf._d[kinded_name]
    @override
    def _iter_all_registered_kinded_names_(sf, /):
        '-> Iter kinded_name'
        return iter(sf._d)

#class IScene__wraper(IScene):
class SceneView(IScene, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, scene, /):
        check_type_le(IScene, scene)
        sf._sc = scene
        sf._args4repr = (scene,)
            #_Base4repr
    @override
    def check_kinded_name(sf, kinded_name, /):
        '-> None | ^TypeError'
        scene = sf._sc
        scene.check_kinded_name(kinded_name)
    @override
    def _lookup_(sf, kinded_name, /):
        '-> obj | ^KeyError'
        scene = sf._sc
        return scene._lookup_(kinded_name)
    @override
    def _iter_all_registered_kinded_names_(sf, /):
        '-> Iter kinded_name'
        scene = sf._sc
        return scene._iter_all_registered_kinded_names_()



class Scene__register(Scene, IScene__register, _Base4repr):
    ___no_slots_ok___ = True
    def view_scene(sf, /):
        '-> IScene'
        return Scene(sf._d)

    @override
    def get_kind(sf, kinded_name, /):
        'knm -> kind'
        check_type_is(KindedName, kinded_name)
        return kinded_name.case
    @override
    def check_kind(sf, kind, /):
        '-> None | ^KindError'
        check_type_le(type, kind)
    @override
    def check_kind_of_obj(sf, kind, obj, /):
        '-> None | ^KindError'
        check_type_le(kind, obj)
    @override
    def _register_(sf, kinded_name, obj, /):
        '-> None | ^KeyError'
        if not dict_add(sf._d, kinded_name, obj):
            raise KeyError(kinded_name)


def mk_Scene_ex(knm2obj=None, /):
    '-> (register4scene, view4scene)/(IScene__register, IScene)'
    if knm2obj is None:
        knm2obj = {}
    register4scene = Scene__register(knm2obj)
    view4scene = register4scene.view_scene()
    return (register4scene, view4scene)

__all__
from seed.recognize.recognizer_LLoo_.Scene import SceneView, Scene, Scene__register
from seed.recognize.recognizer_LLoo_.Scene import mk_Scene_ex
from seed.recognize.recognizer_LLoo_.Scene import *
