
#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/check/ADT.py

seed.helper.check.ADT
py -m nn_ns.app.debug_cmd   seed.helper.check.ADT
py -m seed.helper.check.ADT
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.helper.check.ADT
#from seed.helper.check.ADT import ADT

from seed.helper.check.ADT import check_via_IADT_basic, check_via_IADT_advance, IADT_basic, IADT_advance

from seed.helper.check.ADT import IADT_advance__base_tuple, ADT_advance, IADT_basic__no_params, IADT_basic__dispatch__using_method_name_as_state

from seed.helper.check.ADT import ADT_basic__mapping__KV, ADT_basic__union__dispatch__using_type_le, ADT_basic__union__dispatch__using_type_eq, ADT_basic__pass_or_fail, ADT_basic__predicator

from seed.helper.check.ADT import ADT_basic__dispatch__using_method_name_as_state__no_params


data Tree a b = Leaf a | Fork b [Tree a]

tree = (a,) | (b, [tree])
see: _t3()

#]]]'''
__all__ = r'''
check_via_IADT_basic
check_via_IADT_advance
IADT_basic
IADT_advance


IADT_advance
    IADT_advance__base_tuple
        ADT_advance
IADT_basic
    IADT_basic__no_params
        ADT_basic__mapping__KV
        ADT_basic__union__dispatch__using_type_le
        ADT_basic__union__dispatch__using_type_eq
        ADT_basic__pass_or_fail
        ADT_basic__predicator

    IADT_basic__dispatch__using_method_name_as_state
        ADT_basic__dispatch__using_method_name_as_state__no_params

'''.split()#'''
    #ADT
__all__

from seed.tiny import check_type_is, check_type_le
from seed.types.FrozenDict import FrozenDict
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

from seed.tiny import BaseTuple


class IADT_basic(ABC):
    r'''
    triple4ADT_basic = (adt_basic, state_or_recur_group, template_params4adt_basic)
    ===
    triple4ADT_basic :: (IADT_basic, recur_group4adt, args4recur_group)
        :: (IADT_basic, [IADT_basic], [arg])
    triple4ADT_basic :: (IADT_basic, state/idx/name/method, template_params4adt_basic)
        :: (IADT_basic{.adt_seq::[IADT_basic]}, idx, [arg])
        :: (IADT_basic{.__dict__::{name->method}}, name, [arg])
        :: (IADT_basic{.__dict__::{name->method}}, method, [arg])
    '''#'''
    __slots__ = ()

    r'''
    @abstractmethod
    def _iter_check_basic_(sf, recur_group4sf, args4recur_group, obj, /):
        'IADT_basic -> recur_group4adt -> args4recur_group -> obj -> Iter (IADT_basic, recur_group4adt, args4recur_group, obj) | raise TypeError'
    '''#'''
    @abstractmethod
    def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
        'IADT_basic -> state_or_recur_group -> template_params4adt_basic -> obj -> Iter (IADT_basic, state_or_recur_group, template_params4adt_basic, obj) | raise TypeError'
    @abstractmethod
    def __eq__(sf, ot, /):
        pass
    @abstractmethod
    def __hash__(sf, /):
        pass
r'''[[[
class IADT_basic__dispatch(IADT_basic):
    __slots__ = ()
    @abstractmethod
    def _adt_dispatch_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
    @abstractmethod
    def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
#]]]'''

class IADT_advance(ABC):
    __slots__ = ()
    #check_via_IADT_advance
    @abstractmethod
    def _iter_check_advance_(sf, obj, /):
        'IADT_advance -> obj -> Iter (IADT_advance, obj) | raise TypeError'
    @abstractmethod
    def __eq__(sf, ot, /):
        pass
    @abstractmethod
    def __hash__(sf, /):
        pass

class IADT_advance__base_tuple(IADT_advance, BaseTuple):
    __slots__ = ()
    @override
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and tuple.__eq__(sf, ot)
    @override
    def __hash__(sf, /):
        return hash((type(sf), tuple.__hash__(sf)))
class ADT_advance(IADT_advance__base_tuple):
    __slots__ = ()
    def __init__(sf, adt_basic, state_or_recur_group, template_params4adt_basic, /):
        check_type_le(IADT_basic, adt_basic)
    @override
    def _iter_check_advance_(sf, obj, /):
        'IADT_advance -> obj -> Iter (IADT_advance, obj) | raise TypeError'
        (adt_basic, state_or_recur_group, template_params4adt_basic) = sf
        for (adt_basic, state_or_recur_group, template_params4adt_basic, obj) in adt_basic._iter_check_basic_(state_or_recur_group, template_params4adt_basic, obj):
            adt_advance = ADT_advance(adt_basic, state_or_recur_group, template_params4adt_basic)
            yield adt_advance, obj

def check_via_IADT_basic(adt_basic__recur_group__args__obj__4ples, obj_id2obj_adts=None, /):
    'Iter (IADT_basic, state_or_recur_group, template_params4adt_basic, obj) -> may {id<obj>:(obj, {ADT_advance})} -> None | raise TypeError'
    pairs = ((ADT_advance(adt_basic, state_or_recur_group, template_params4adt_basic), obj) for (adt_basic, state_or_recur_group, template_params4adt_basic, obj) in adt_basic__recur_group__args__obj__4ples)
    check_via_IADT_advance(pairs, obj_id2obj_adts)
def check_via_IADT_advance(adt_advance__obj__pairs, obj_id2obj_adts=None, /):
    'Iter (IADT_advance, obj) -> may {id<obj>:(obj, {IADT_advance})} -> None | raise TypeError'
    if obj_id2obj_adts is None:
        obj_id2obj_adts = {}
    ls = [iter(adt_advance__obj__pairs)]
        # :: [Iter (IADT_advance, object)]
    def put(sf, obj, /):
        try:
            check_type_le(IADT_advance, sf)
        except:
            raise TypeError(sf)
        (_obj, adt_set) = obj_id2obj_adts.setdefault(id(obj), (obj, set()))
        if _obj is not obj: raise ValueError('obj_id2obj_adts')
        if sf in adt_set:
            return
        adt_set.add(sf)
        it = iter(sf._iter_check_advance_(obj))
        ls.append(it)
        put(sf, obj)
    while ls:
        for adt_sf, obj in ls[-1]:
            put(adt_sf, obj)
            break
        else:
            ls.pop()






_the_ = '_the_'
class IADT_basic__no_params(IADT_basic):
    __slots__ = ()
    def __new__(cls, /):
        if not _the_ in cls.__dict__:
            sf = super(__class__, cls).__new__(cls)
            setattr(cls, _the_, sf)
        #sf = getattr(cls, _the_)
        sf = cls.__dict__[_the_]
        check_type_is(cls, sf)
        return sf

    @override
    def __eq__(sf, ot, /):
        return type(sf) is type(ot)
    @override
    def __hash__(sf, /):
        return hash(id(type(sf)))

class ADT_basic__mapping__KV(IADT_basic__no_params):
    r'''
    template_params4adt_basic :: (mapping_basecls, using_type_le/bool, triple4ADT_basic4key, triple4ADT_basic4val)
    state_or_recur_group :: ()
    '''#'''
    __slots__ = ()

    @override
    def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
        'IADT_basic -> state_or_recur_group -> template_params4adt_basic -> obj -> Iter (IADT_basic, state_or_recur_group, template_params4adt_basic, obj) | raise TypeError'
        [] = state_or_recur_group
        (mapping_basecls, using_type_le, triple4ADT_basic4key, triple4ADT_basic4val) = template_params4adt_basic
        check_ = check_type_le if using_type_le else check_type_is
        check_(mapping_basecls, obj)
        for k, v in obj.items():
            yield (*triple4ADT_basic4key, k)
            yield (*triple4ADT_basic4val, v)


class ADT_basic__union__dispatch__using_type_le(IADT_basic__no_params):
    r'''
    template_params4adt_basic :: ([(basecls, triple4ADT_basic)],)
    state_or_recur_group :: ()
    '''#'''
    __slots__ = ()

    @override
    def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
        'IADT_basic -> state_or_recur_group -> template_params4adt_basic -> obj -> Iter (IADT_basic, state_or_recur_group, template_params4adt_basic, obj) | raise TypeError'
        [] = state_or_recur_group
        [pairs] = template_params4adt_basic
        for basecls, triple4ADT_basic in pairs:
            if isinstance(obj, basecls):
                yield (*triple4ADT_basic, obj)
                return
        raise TypeError

class ADT_basic__union__dispatch__using_type_eq(IADT_basic__no_params):
    r'''
    template_params4adt_basic :: ({objcls, triple4ADT_basic},)
    state_or_recur_group :: ()
    '''#'''
    __slots__ = ()

    @override
    def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
        'IADT_basic -> state_or_recur_group -> template_params4adt_basic -> obj -> Iter (IADT_basic, state_or_recur_group, template_params4adt_basic, obj) | raise TypeError'
        [] = state_or_recur_group
        [ty2triple] = template_params4adt_basic
        ty = type(obj)
        if ty not in ty2triple:raise TypeError
        triple4ADT_basic = ty2triple[ty]
        yield (*triple4ADT_basic, obj)
        return



class ADT_basic__pass_or_fail(IADT_basic__no_params):
    r'''
    template_params4adt_basic :: (is_ok,)
    state_or_recur_group :: ()
    '''#'''
    __slots__ = ()

    @override
    def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
        'IADT_basic -> state_or_recur_group -> template_params4adt_basic -> obj -> Iter (IADT_basic, state_or_recur_group, template_params4adt_basic, obj) | raise TypeError'
        [] = state_or_recur_group
        [is_ok] = template_params4adt_basic
        if not is_ok: raise TypeError
        return;yield

class ADT_basic__predicator(IADT_basic__no_params):
    r'''
    template_params4adt_basic :: (predicator, post_args)
    state_or_recur_group = pre_args
    '''#'''
    __slots__ = ()

    @override
    def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
        'IADT_basic -> state_or_recur_group -> template_params4adt_basic -> obj -> Iter (IADT_basic, state_or_recur_group, template_params4adt_basic, obj) | raise TypeError'
        pre_args = state_or_recur_group
        (predicator, post_args) = template_params4adt_basic
        if not predicator(*pre_args, obj, *post_args): raise TypeError
        return;yield




class IADT_basic__dispatch__using_method_name_as_state(IADT_basic):
    r'''
    template_params4adt_basic :: ???
    state_or_recur_group = method_name
    '''#'''
    __slots__ = ()

    @override
    def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
        'IADT_basic -> state_or_recur_group -> template_params4adt_basic -> obj -> Iter (IADT_basic, state_or_recur_group, template_params4adt_basic, obj) | raise TypeError'
        method_name = state_or_recur_group
        check_type_is(str, method_name)
        handler = getattr(sf, method_name)
        yield from handler(template_params4adt_basic, obj)

class ADT_basic__dispatch__using_method_name_as_state__no_params(IADT_basic__dispatch__using_method_name_as_state, IADT_basic__no_params):
    __slots__ = ()



from seed.helper.check.ADT import check_via_IADT_basic, check_via_IADT_advance, IADT_basic, IADT_advance

from seed.helper.check.ADT import IADT_advance__base_tuple, ADT_advance, IADT_basic__no_params, IADT_basic__dispatch__using_method_name_as_state

from seed.helper.check.ADT import ADT_basic__mapping__KV, ADT_basic__union__dispatch__using_type_le, ADT_basic__union__dispatch__using_type_eq, ADT_basic__pass_or_fail, ADT_basic__predicator

from seed.helper.check.ADT import ADT_basic__dispatch__using_method_name_as_state__no_params

from seed.helper.check.ADT import *

def _mk_tree():
    class Leaf:
        def __init__(sf, a, /):
            sf.a = a
    class Fork:
        def __init__(sf, b, trees, /):
            sf.b = b
            sf.children = [*trees]
    # a = str
    # b = int
    leaf1 = Leaf('abc')
    leaf2 = Leaf('xyz')
    fork1 = Fork(6, [])
    fork2 = Fork(2, [leaf1])
    fork3 = Fork(4, [leaf2, fork2, fork1])
    fork4 = Fork(4, [leaf1, leaf2, fork3, fork2, fork1])
    tree = fork4
    triple4ADT_basic4pass = (ADT_basic__pass_or_fail(), (), (True,))
    triple4ADT_basic4a = (ADT_basic__union__dispatch__using_type_eq(), (), (FrozenDict({str:triple4ADT_basic4pass}),))
    #triple4ADT_basic4b = (ADT_basic__union__dispatch__using_type_eq(), (), (FrozenDict({int:triple4ADT_basic4pass}),))
    triple4ADT_basic4b = (ADT_basic__predicator(), (), (isinstance, (int,)))

    return (Leaf, Fork, tree, triple4ADT_basic4a, triple4ADT_basic4b)

def _t3():
    class ADT_basic__tree(ADT_basic__dispatch__using_method_name_as_state__no_params):
        r'''
        template_params4adt_basic :: (Leaf, Fork, triple4ADT_basic4a, triple4ADT_basic4b)
        state_or_recur_group :: (on_tree / on_fork / on_children / on_leaf)
        '''#'''
        __slots__ = ()

        def on_tree(sf, template_params4adt_basic, obj, /):
            [Leaf, Fork, triple4ADT_basic4a, triple4ADT_basic4b] = template_params4adt_basic
            ty = type(obj)
            if ty is Fork:
                yield (sf, 'on_fork', template_params4adt_basic, obj)
            elif ty is Leaf:
                yield (sf, 'on_leaf', template_params4adt_basic, obj)
            else:
                raise TypeError(ty)
        def on_fork(sf, template_params4adt_basic, obj, /):
            [Leaf, Fork, triple4ADT_basic4a, triple4ADT_basic4b] = template_params4adt_basic
            check_type_is(Fork, obj)
            yield (*triple4ADT_basic4b, obj.b)
            yield (sf, 'on_children', template_params4adt_basic, obj.children)
        def on_children(sf, template_params4adt_basic, obj, /):
            check_type_is(list, obj)
            for tree in obj:
                yield (sf, 'on_tree', template_params4adt_basic, tree)
        def on_leaf(sf, template_params4adt_basic, obj, /):
            [Leaf, Fork, triple4ADT_basic4a, triple4ADT_basic4b] = template_params4adt_basic
            check_type_is(Leaf, obj)
            yield (*triple4ADT_basic4a, obj.a)

    def main():
        (Leaf, Fork, tree, triple4ADT_basic4a, triple4ADT_basic4b) = _mk_tree()
        template_params4adt_basic = (Leaf, Fork, triple4ADT_basic4a, triple4ADT_basic4b)
        triple4ADT_basic4tree = (ADT_basic__tree(), 'on_tree', template_params4adt_basic)
        check_via_IADT_basic([(*triple4ADT_basic4tree, tree)])
    main()
if __name__ == "__main__":
    _t3()

def _t2():
    (Leaf, Fork, tree, triple4ADT_basic4a, triple4ADT_basic4b) = _mk_tree()

    class ADT_basic__leaf(IADT_basic__no_params):
        r'''
        template_params4adt_basic :: (triple4ADT_basic4a,)
        state_or_recur_group :: ()
        '''#'''
        __slots__ = ()

        @override
        def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
            [] = state_or_recur_group
            [triple4ADT_basic4a] = template_params4adt_basic
            check_type_is(Leaf, obj)
            yield (*triple4ADT_basic4a, obj.a)



    class ADT_basic__fork(IADT_basic__no_params):
        r'''
        template_params4adt_basic :: (triple4ADT_basic4a, triple4ADT_basic4b)
        state_or_recur_group :: (ADT_basic__tree, ADT_basic__fork, ADT_basic__children)
        '''#'''
        __slots__ = ()

        @override
        def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
            [adt_basic4tree, adt_basic4fork, adt_basic4children] = state_or_recur_group
            [triple4ADT_basic4a, triple4ADT_basic4b] = template_params4adt_basic
            check_type_is(Fork, obj)
            yield (*triple4ADT_basic4b, obj.b)
            yield (adt_basic4children, state_or_recur_group, template_params4adt_basic, obj.children)



    class ADT_basic__children(IADT_basic__no_params):
        __slots__ = ()

        @override
        def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
            [adt_basic4tree, adt_basic4fork, adt_basic4children] = state_or_recur_group
            [triple4ADT_basic4a, triple4ADT_basic4b] = template_params4adt_basic
            check_type_is(list, obj)
            for child in obj:
                yield (adt_basic4tree, state_or_recur_group, template_params4adt_basic, child)



    class ADT_basic__tree(IADT_basic__no_params):
        __slots__ = ()

        @override
        def _iter_check_basic_(sf, state_or_recur_group, template_params4adt_basic, obj, /):
            [adt_basic4tree, adt_basic4fork, adt_basic4children] = state_or_recur_group
            [triple4ADT_basic4a, triple4ADT_basic4b] = template_params4adt_basic
            yield (*triple4ADT_basic4tree__dispatch, obj)

    adt_basic4tree = ADT_basic__tree()
    adt_basic4fork = ADT_basic__fork()
    adt_basic4children = ADT_basic__children()
    state_or_recur_group = (adt_basic4tree, adt_basic4fork, adt_basic4children)

    template_params4adt_basic = (triple4ADT_basic4a, triple4ADT_basic4b)

    triple4ADT_basic4tree = (adt_basic4tree, state_or_recur_group, template_params4adt_basic)
    triple4ADT_basic4fork = (adt_basic4fork, state_or_recur_group, template_params4adt_basic)
    triple4ADT_basic4children = (adt_basic4children, state_or_recur_group, template_params4adt_basic)
    triple4ADT_basic4leaf = (ADT_basic__leaf(), (), (triple4ADT_basic4a,))
    args4recur_group4tree_dispatch = (FrozenDict({Leaf:triple4ADT_basic4leaf, Fork:triple4ADT_basic4fork}),)
    triple4ADT_basic4tree__dispatch = (ADT_basic__union__dispatch__using_type_eq(), (), args4recur_group4tree_dispatch)
        #not in recur_group4sf
    triple4ADT_basic4tree
        #in recur_group4sf

    tree
    check_via_IADT_basic([(*triple4ADT_basic4tree, tree)])

if __name__ == "__main__":
    _t2()





r'''[[[

class ADT:
    'iter_checker4ADT:: args4ADT -> ADT -> obj -> Iter (ADT, obj) | raise TypeError'
    def __init__(sf, type2iter_checker_args, /):
        d = dict(type2iter_checker_args)
        d = {ty:(iter_checker4ADT, (*args4ADT,)) for ty, (iter_checker4ADT, args4ADT) in d.items()}
        assert all(check_type_le(type, ty) for ty in d)
        assert all(callable(iter_checker4ADT) for (iter_checker4ADT, args4ADT) in d.values())
        sf._d = d
        sf._h = hash((type(sf), frozenset(d.items())))
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and sf._h==ot._h and len(sf._d)==len(ot._d) and (sf._d)==(ot._d)
    def __hash__(sf, /):
        return sf._h
    def type2iter_checker_args4ADT(sf, ty, /):
        'ty -> (iter_checker4ADT, args4ADT)'
        return sf._d[ty]
    def _iter_check_(sf, obj, /):
        ty = type(obj)
        try:
            (iter_checker4ADT, args4ADT) = sf.type2iter_checker_args4ADT(ty)
        except KeyError:
            raise TypeError((sf, ty))
        it = iter(iter_checker4ADT(args4ADT, sf, obj))
        return it
#end-class ADT:
def check_via_ADT(adt_x_pairs, obj_id2ADT_ids=None, /):
    if obj_id2ADT_ids is None:
        obj_id2ADT_ids = {}
    ls = [iter(adt_x_pairs)]
        # :: [Iter (ADT, object)]
    def put(sf, obj, /):
        check_type_le(ADT, sf)
        sf_ids = obj_id2ADT_ids.setdefault(id(obj), set())
        if id(sf) in sf_ids:
            return
        sf_ids.add(id(sf))
        it = iter(sf._iter_check_(obj))
        ls.append(it)
        put(sf, obj)
    while ls:
        for adt_sf, obj in ls[-1]:
            put(adt_sf, obj)
            break
        else:
            ls.pop()
#end-def check_via_ADT(sf, obj, /):


def _t():
    class Leaf:
        def __init__(sf, a, /):
            sf.a = a
    class Fork:
        def __init__(sf, b, trees, /):
            sf.b = b
            sf.children = [*trees]
    def on_a(args4ADT, adt, a, /):
        check_type_is(str, a)
        return; yield
    def on_b(args4ADT, adt, b, /):
        check_type_is(int, b)
        return; yield

    def on_leaf(args4ADT, adt, leaf, /):
        [adt4a, adt4b] = args4ADT
        yield (adt4a, leaf.a)
    def on_fork(args4ADT, adt, fork, /):
        [adt4a, adt4b] = args4ADT
        yield (adt4b, fork.b)
        for child in fork.children:
            yield (adt, child)

    adt4a = ADT({str:(on_a, ())})
    adt4b = ADT({int:(on_b, ())})
    args4adt4tree = (adt4a, adt4b)
    adt4tree = ADT({Leaf:(on_leaf, args4adt4tree), Fork:(on_fork, args4adt4tree)})




from seed.helper.check.ADT import ADT
#]]]'''

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

