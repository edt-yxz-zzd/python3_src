#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree2/scene_role.py
    匞场景包++圁角色名++注册处


seed.data_funcs.finger_tree2.scene_role
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree2.scene_role -x
#]]]'''
__all__ = r'''
魖场景包暨角色名注册处
    乸场景包暨角色名注册处
'''.split()#'''
__all__


from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

#class 魖场景包(ABC):
class 魖场景包暨角色名注册处(ABC):
    r'''[[[

对象可能不存在，需要构造器
    匞场景包.构造囗算子包扌(圁角色名,算子包模板参数...).对象构造器(...)
    构造囗算子包扌 :: 匞场景包->圁角色名->(*算子包模板参数...) -> 匴算子包<算子包模板参数...>
此前需要 绑定/注册:
    指派囗角色扌/绑定囗算子包囗构造器扌:: 匞场景包->圁角色名-> 乸算子包 -> None
    #]]]'''#'''
    __slots__ = ()

    @abstractmethod
    def 指派囗角色扌(匞场景包, 圁角色名, 乸算子包, /):
        ':: 匞场景包 -> 圁角色名 -> 乸算子包/(匞场景包 -> 圁角色名 -> (*算子包模板参数...)-> 匴算子包<匞场景包;圁角色名;算子包模板参数>) -> None'
    @abstractmethod
    def 构造囗算子包扌(匞场景包, 圁角色名, /, *算子包模板参数冖冖位次, **算子包模板参数冖冖具名):
        '-> 匴算子包<匞场景包;圁角色名;算子包模板参数>'

class 乸场景包暨角色名注册处(魖场景包暨角色名注册处):
    __slots__ = ()

    @override
    def 指派囗角色扌(匞场景包, 圁角色名, 乸算子包, /):
        ':: 匞场景包 -> 圁角色名 -> 乸算子包/(匞场景包 -> 圁角色名 -> (*算子包模板参数...)-> 匴算子包<匞场景包;圁角色名;算子包模板参数>) -> None'
        角色名讠乸算子包 = vars(匞场景包).setdefault(__class__, {})
        角色名讠乸算子包[圁角色名] = 乸算子包

    @override
    def 构造囗算子包扌(匞场景包, 圁角色名, /, *算子包模板参数冖冖位次, **算子包模板参数冖冖具名):
        '-> 匴算子包<匞场景包;圁角色名;算子包模板参数>'
        角色名讠乸算子包 = vars(匞场景包)[__class__]
        return 角色名讠乸算子包[圁角色名](匞场景包, 圁角色名, *算子包模板参数冖冖位次, **算子包模板参数冖冖具名)


__all__


from seed.data_funcs.finger_tree2.scene_role import 魖场景包暨角色名注册处, 乸场景包暨角色名注册处
from seed.data_funcs.finger_tree2.scene_role import *
