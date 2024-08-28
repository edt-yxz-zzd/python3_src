#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/IScene.py

seed.recognize.recognizer_LLoo_.IScene
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.IScene -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.IScene:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.IScene   @f
#]]]'''
__all__ = r'''
KindError
LookupError__circle_ref
IWithScene
IScene
    IScene__register
INamed
IWrapper
    ILazyWrapper
IDependentTreeNode
    IDependentTreeNode__no_ref
    IDependentTreeNode__no_children
        IDependentTreeNode__leaf
    IDependentTreeNode__wrapper
    IDependentTreeNode__ref

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.recognizer_LLoo_._common import (
null_iter
,check_type_le#,check_type_is
,abstractmethod, override, ABC, ABC__no_slots
)

from seed.types.StackStyleSet import StackStyleSet
from seed.tiny_.dict_op__add import dict_add, set_add
from itertools import count as count_

___end_mark_of_excluded_global_names__0___ = ...

#class KindError(Exception):pass
class KindError(TypeError):pass
class LookupError__circle_ref(LookupError):pass



class IWithScene(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def scene(sf, /):
        '-> IScene'

class IScene(ABC):
    r'''[[[
    'factory4combinators&&closure4ref&&register4ref&&global_setting'

    global_recur_break vs local_recur_break
    named_recur_break vs unamed_recur_break
        * global_recur_break:using:
            IDependentTreeNode__ref
            IScene.dereference()
            +++
            IScene.register()
            #xxx:IScene.register__named()
        * local_recur_break:using:
            ILazyWrapper
                .unlazy()
            ######
            xxx = mk_Xxx(..., lazy_wrapper4xxx:=XxxLazyWrapper(lazy_xxx:=lambda:xxx), ...)
            yyy = lazy_wrapper4xxx.unlazy()
            assert xxx is yyy
            ######
            ??weakref??
            ######


    #]]]'''#'''
    __slots__ = ()
    @abstractmethod
    def check_kinded_name(sf, kinded_name, /):
        '-> None | ^TypeError'
    @abstractmethod
    def _lookup_(sf, kinded_name, /):
        '-> obj | ^KeyError'
    @abstractmethod
    def _iter_all_registered_kinded_names_(sf, /):
        '-> Iter kinded_name'
    ######################
    def dereference(sf, kinded_name, /):
        '-> obj | ^KeyError | ^LookupError__circle_ref # until not ref/IDependentTreeNode__ref'
        sf.check_kinded_name(kinded_name)
        knm = kinded_name
        s = StackStyleSet()
        for sz in count_(1):
            s.add(knm)
            if not len(s) == sz:
                ls = [*s]
                j = ls.index(knm)
                ls.append(knm)
                leadings = ls[:j]
                circle = ls[j:]
                raise LookupError__circle_ref(leadings, circle)
            obj = sf._lookup_(knm)
                # ^KeyError
            if not isinstance(obj, IDependentTreeNode__ref):
                break
            ref = obj
            knm = ref.its_kinded_name
        return obj
    ######################
    def iter_all_registered_objs(sf, /):
        '-> Iter obj # [maybe not unique]'
        knms = sf.iter_all_registered_kinded_names()
        objs = map(sf._lookup_, knms)
        return objs
    ######################
    def iter_all_registered_kinded_names(sf, /):
        '-> Iter kinded_name # [unique]'
        s = set()
        knms = sf._iter_all_registered_kinded_names_()
        for knm in knms:
            if set_add(s, knm):
                yield knm
        return

    ######################
    def detect_circle_ref(scene, /):
        '-> None | ^LookupError__circle_ref'
        known_knms = {*scene.iter_all_registered_kinded_names()}
        for kinded_name in known_knms:
            scene.dereference(kinded_name)
                # ^LookupError__circle_ref
        return
    ######################
    def findout_all_missing_kinded_names(scene, /):
        'IScene -> Iter kinded_name #but not detect circle_ref, see:.detect_circle_ref()'
        objs = scene.iter_all_registered_objs()
        addr2node = {id(obj):obj for obj in objs if isinstance(obj, IDependentTreeNode)}
            # unique&&filter
        ls = [*addr2node.values()]
        def put(node, /):
            if dict_add(addr2node, id(node), node):
                ls.append(node)
        while ls:
            node = ls.pop()
            for child_node in node.iter_direct_child_dependent_tree_nodes():
                put(child_node)
        ######################
        nodes = addr2node.values()
        used_knms = {knm for node in nodes for knm in node.iter_directly_used_kinded_names()}
        known_knms = {*scene.iter_all_registered_kinded_names()}
        missing_knms = used_knms -known_knms
        return missing_knms

    ######################
    ######################
#end-class IScene(ABC):

class IScene__register(IScene):
    __slots__ = ()
    @abstractmethod
    def get_kind(sf, kinded_name, /):
        'knm -> kind'
    @abstractmethod
    def check_kind(sf, kind, /):
        '-> None | ^KindError'
    @abstractmethod
    def check_kind_of_obj(sf, kind, obj, /):
        '-> None | ^KindError'
    @abstractmethod
    def _register_(sf, kinded_name, obj, /):
        '-> None | ^KeyError'
    ######################
    def register(sf, kinded_name, obj, /):
        '-> None | ^KeyError | ^KindError'
        sf.check_kinded_name(kinded_name)
        kind = sf.get_kind(kinded_name)
        sf.check_kind(kind)
        sf.check_kind_of_obj(kind, obj)
            # ^KindError

        try:
            sf._lookup_(kinded_name)
        except KeyError:
            pass
        else:
            raise KeyError(kinded_name)
        sf._register_(kinded_name, obj)
            # ^KeyError
    ######################


class IDependentTreeNode(ABC):
    #class IRequiredSceneAsClosure(ABC):
    '[kinded_name <: Hashable] # [kinded_name =?= (kind, name)]'
    __slots__ = ()
    #@abstractmethod
    def check_kinded_name(sf, kinded_name, /):
        '-> None | ^TypeError'
        pass#hash(kinded_name)
    @abstractmethod
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
    @abstractmethod
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'


    def iter_directly_used_kinded_names(sf, /):
        '-> Iter knm/kinded_name'
        for knm in sf._iter_directly_used_kinded_names_():
            sf.check_kinded_name(knm)
            yield knm
        return

    def iter_direct_child_dependent_tree_nodes(sf, /):
        '-> Iter IDependentTreeNode'
        for x in sf._iter_direct_child_dependent_tree_nodes_():
            check_type_le(IDependentTreeNode, x)
            yield x



class INamed(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def my_name(sf, /):
        '-> nm/(hashable&&immutable)'
class IWrapper(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def the_wrapped_obj(sf, /):
        '-> wrapped_obj'
    _base_type4wrapped_obj_ = object
    @property
    @abstractmethod
    def _base_type4wrapped_obj_(sf, /):
        '-> typ # [wrapped_obj <: typ]'
    def _check_wrapped_obj_(sf, wrapped_obj, /):
        check_type_le(type(sf)._base_type4wrapped_obj_, wrapped_obj)
class ILazyWrapper(IWrapper):
    'to break local recur/unamed recur'
    __slots__ = ()
    @abstractmethod
    def unlazy(sf, /):
        '-> the_wrapped_obj # get or (make and cache)'
    @property
    @override
    def the_wrapped_obj(sf, /):
        '-> wrapped_obj'
        return sf.unlazy()







class IDependentTreeNode__no_ref(IDependentTreeNode):
    __slots__ = ()
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kinded_name)'
        return null_iter
class IDependentTreeNode__no_children(IDependentTreeNode):
    __slots__ = ()
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        return null_iter
class IDependentTreeNode__leaf(IDependentTreeNode__no_children, IDependentTreeNode__no_ref):
    __slots__ = ()

class IDependentTreeNode__wrapper(IDependentTreeNode, IWrapper):
    __slots__ = ()
class IDependentTreeNode__ref(ILazyWrapper, IDependentTreeNode__no_children, IDependentTreeNode__wrapper, IWithScene):
    #IDependentTreeNode__wrapper<<==『+IDependentTreeNode』『+IWrapper』to avoid:『order (MRO) for bases IDependentTreeNode, IWrapper, object』<<==『class RecognizerLLoo__ref(IRecognizerLLoo__wrapper_base, IDependentTreeNode__ref, _Base4repr):』
    #class IRequiredSceneAsClosure__ref(IRequiredSceneAsClosure):
    __slots__ = ()
    @property
    @abstractmethod
    def its_kinded_name(sf, /):
        '-> knm/kinded_name/(hashable&&immutable)'
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter (kinded_name)'
        yield sf.its_kinded_name
        return
    #@override
    #def _iter_direct_child_dependent_tree_nodes_(sf, /):
    #    '-> Iter IDependentTreeNode'
    #    return null_iter
    @override
    def unlazy(sf, /):
        '-> the_wrapped_obj # get or (make and cache)'
        the_wrapped_obj = sf.scene.dereference(sf.its_kinded_name)
        return the_wrapped_obj





__all__
from seed.recognize.recognizer_LLoo_.IScene import \
(KindError
,LookupError__circle_ref
,IWithScene
,IScene
,    IScene__register
,INamed
,IWrapper
,    ILazyWrapper
,IDependentTreeNode
,    IDependentTreeNode__no_ref
,    IDependentTreeNode__no_children
,        IDependentTreeNode__leaf
,    IDependentTreeNode__wrapper
,    IDependentTreeNode__ref
)

from seed.recognize.recognizer_LLoo_.IScene import *
