#__all__:goto
r'''
e ../../python3_src/seed/types/union_find_algo/DisjointSet.py
py -m seed.types.union_find_algo.DisjointSet
py -m nn_ns.app.debug_cmd   seed.types.union_find_algo.DisjointSet



from seed.types.union_find_algo.DisjointSet import UnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression


from seed.types.union_find_algo.DisjointSet import IUnionFindCtxOps, IUnionFindCtxOps__opaque_state4DisjointSet, IUnionFindCtxOps__opaque_state4DisjointSet__union_by_rank__path_compression, IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping, IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression






view others/数学/Disjoint-Set.txt
『Disjoint-Set data structure』/『union-find data structure』
  not 『Disjoint-Union』
view others/数学/Disjoint-Union.txt
view others/数学/Disjoint-Set.txt


view ../../python3_src/seed/types/ops/IEmplaceStackOps.py



https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
Union-Find Algorithm | Set 2 (Union By Rank and Path Compression)



[[[
>>> cls = UnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression
>>> ctxops = cls({})

>>> ctxops.union_find_algo__union(1, 2)
Traceback (most recent call last):
    ...
TypeError: raw: not inited
>>> ctxops.union_find_algo__union(1, 1)
Traceback (most recent call last):
    ...
TypeError: raw: not inited
>>> ctxops.union_find_algo__find_root(1)
Traceback (most recent call last):
    ...
TypeError: raw: not inited
>>> ctxops.union_find_algo__init_raw_element(1)
>>> ctxops.union_find_algo__find_root(1)
1
>>> ctxops.union_find_algo__union(1, 1)
1
>>> ctxops.union_find_algo__union(1, 2)
Traceback (most recent call last):
    ...
TypeError: raw: not inited
>>> ctxops.union_find_algo__init_raw_element(2)
>>> ctxops.union_find_algo__init_raw_element(1)
Traceback (most recent call last):
    ...
TypeError: inited: not raw
>>> ctxops.union_find_algo__eqv(1, 2)
False
>>> ctxops.union_find_algo__union(1, 2)
1
>>> ctxops.union_find_algo__eqv(1, 2)
True


>>> ctxops = ctxops.mk_ctxops__via_ireplace_mutable_context({})
>>> xs = range(10)
>>> ctxops.union_find_algo__init_raw_elements(xs)
>>> sorted(ctxops.get_mutable_context4ops().items())
[(0, (1, 0)), (1, (1, 1)), (2, (1, 2)), (3, (1, 3)), (4, (1, 4)), (5, (1, 5)), (6, (1, 6)), (7, (1, 7)), (8, (1, 8)), (9, (1, 9))]
>>> ctxops.union_find_algo__union_root1s(xs)
0
>>> sorted(ctxops.get_mutable_context4ops().items())
[(0, (10, 0)), (1, (1, 0)), (2, (1, 0)), (3, (1, 0)), (4, (1, 0)), (5, (1, 0)), (6, (1, 0)), (7, (1, 0)), (8, (1, 0)), (9, (1, 0))]


]]]


#'''
#HHHHH
__all__ = '''
IUnionFindCtxOps
    IUnionFindCtxOps__opaque_state4DisjointSet
        IUnionFindCtxOps__opaque_state4DisjointSet__union_by_rank__path_compression
        IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping
            IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression
                UnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import check_type_le, check_type_is, check_tmay, check_pair, check_uint
from seed.tiny import dict_add__is
from collections.abc import MutableMapping

from seed.abc.ICtxOps import ICtxOps
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH









#class DisjointSet:
class IUnionFindCtxOps(ICtxOps):
    __slots__ = ()
    #@abstractmethod
    def _sketchy_check__xelement_(ctxops, x, /):
        'xelement?/obj -> None|TypeError'
    #@abstractmethod
    def _sketchy_check__raw_element_(ctxops, x, /):
        'raw_element?/xelement -> None|TypeError'
    #@abstractmethod
    def _sketchy_check__inited_element_(ctxops, x, /):
        'element?/xelement -> None|TypeError'
    #@abstractmethod
    def _sketchy_check__root_element_(ctxops, x, /):
        'root_element?/element -> None|TypeError'

    @abstractmethod
    def _union_find_algo__init_raw_element_(ctxops, raw_x, /):
        'raw_element -> None #emplace become element'
    @abstractmethod
    def _union_find_algo__find_root_(ctxops, x, /):
        'element -> root_element'
    @abstractmethod
    def _union_find_algo__union_root_(ctxops, root_x, root_y, /):
        'root_element -> root_element -> root_element # [lhs is not rhs]' # [not eq(lhs, rhs)]
    @abstractmethod
    def _union_find_algo__eq_(ctxops, x, y, /):
        'element -> element -> bool # [lhs is not rhs]'


    def sketchy_check__xelement(ctxops, x, /):
        'xelement?/obj -> None|TypeError'
        ctxops._sketchy_check__xelement_(x)
    def sketchy_check__raw_element(ctxops, x, /):
        'raw_element?/obj -> None|TypeError'
        ctxops._sketchy_check__xelement_(x)
        ctxops._sketchy_check__raw_element_(x)
    def sketchy_check__inited_element(ctxops, x, /):
        'element?/obj -> None|TypeError'
        ctxops._sketchy_check__xelement_(x)
        ctxops._sketchy_check__inited_element_(x)
    def sketchy_check__root_element(ctxops, x, /):
        'root_element?/obj -> None|TypeError'
        ctxops.sketchy_check__inited_element(x)
        ctxops._sketchy_check__root_element_(x)

    def union_find_algo__init_raw_element(ctxops, raw_x, /):
        'raw_element -> None #emplace become element'
        ctxops.sketchy_check__raw_element(raw_x)
        ctxops._union_find_algo__init_raw_element_(raw_x)
        x = raw_x
        ctxops.sketchy_check__inited_element(x)
        return

    def union_find_algo__find_root(ctxops, x, /):
        'element -> root_element'
        ctxops.sketchy_check__inited_element(x)
        root_x = ctxops._union_find_algo__find_root_(x)
        ctxops.sketchy_check__root_element(root_x)
        return root_x
    def union_find_algo__union_root(ctxops, root_x, root_y, /):
        'root_element -> root_element -> root_element'
        ctxops.sketchy_check__root_element(root_x)
        if root_x is root_y: return root_x
        ctxops.sketchy_check__root_element(root_y)
        root_z = ctxops._union_find_algo__union_root_(root_x, root_y)
        ctxops.sketchy_check__root_element(root_z)
        return root_z

    def union_find_algo__eq(ctxops, x, y, /):
        'element -> element -> bool'
        ctxops.sketchy_check__inited_element(x)
        if x is y: return True
        ctxops.sketchy_check__inited_element(y)
        b = ctxops._union_find_algo__eq_(x, y)
        check_type_is(bool, b)
        return b









    def union_find_algo__eqv(ctxops, x, y, /):
        'element -> element -> bool'
        root_x = ctxops.union_find_algo__find_root(x)
        root_y = ctxops.union_find_algo__find_root(y)
        return ctxops.union_find_algo__eq(root_x, root_y)


    def union_find_algo__init_raw_elements(ctxops, raw_xs, /):
        'Iter raw_element -> None #emplace become elements'
        for _ in map(ctxops.union_find_algo__init_raw_element, raw_xs):pass

    def union_find_algo__union(ctxops, x, y, /):
        'element -> element -> root_element'
        root_x = ctxops.union_find_algo__find_root(x)
        root_y = ctxops.union_find_algo__find_root(y)
        root_z = ctxops.union_find_algo__union_root(root_x, root_y)
        return root_z
    def union_find_algo__union1s(ctxops, xs, /):
        'Iter element -> root_element'
        roots = map(ctxops.union_find_algo__find_root, xs)
        return ctxops.union_find_algo__union_root1s(roots)
    def union_find_algo__union_root1s(ctxops, roots, /):
        'Iter root_element -> root_element'
        for root_x in roots:
            break
        else:
            raise TypeError('empty-iter@union_find_algo__union1s')

        union_root = ctxops.union_find_algo__union_root
        for root_y in roots:
            root_x = union_root(root_x, root_y)
        return root_x
#class IUnionFindCtxOps(ICtxOps):






class IUnionFindCtxOps__opaque_state4DisjointSet(IUnionFindCtxOps):
    __slots__ = ()
    #@abstractmethod
    def _sketchy_check__opaque_state_(ctxops, opaque_state, /):
        'opaque_state?/obj -> None'
    @abstractmethod
    def _union_find__has_opaque_state_(ctxops, x, /):
        'xelement -> bool/(True@element, False@raw_element)'
    @abstractmethod
    def _union_find__set_opaque_state_(ctxops, x, opaque_state, /):
        'element -> opaque_state -> None'
    @abstractmethod
    def _union_find__get_opaque_state5inited_element_(ctxops, x, /):
        'element -> opaque_state'
    @abstractmethod
    def _union_find__mk_pseudo_opaque_state4raw_element_(ctxops, raw_x, /):
        'raw_element -> pseudo_opaque_state'
        #no union_find__mk_opaque_state4raw_element
        #   since pseudo_opaque_state may not pass sketchy_check__opaque_state until raw_element be inited!!



    def sketchy_check__opaque_state(ctxops, opaque_state, /):
        'opaque_state?/obj -> None'
        ctxops._sketchy_check__opaque_state_(opaque_state)
    def union_find__has_opaque_state(ctxops, x, /):
        'xelement -> bool'
        ctxops.sketchy_check__xelement(x)
        b = ctxops._union_find__has_opaque_state_(x)
        check_type_is(bool, b)
        return b
    def union_find__set_opaque_state(ctxops, x, opaque_state, /):
        'element -> opaque_state -> None'
        ctxops.sketchy_check__inited_element(x)
            #distinguish with: union_find_algo__init_raw_element
        ctxops.sketchy_check__opaque_state(opaque_state)
        ctxops._union_find__set_opaque_state_(x, opaque_state)
    def union_find__get_tmay_opaque_state(ctxops, x, /):
        'xelement -> tmay opaque_state'
        if ctxops.union_find__has_opaque_state(x):
            inited_x = x
            opaque_state = ctxops._union_find__get_opaque_state5inited_element_(x)
            return (opaque_state,)
        raw_x = x
        return ()



    def union_find__get_opaque_state(ctxops, x, /):
        'xelement -> opaque_state|raise LookupError'
        tm = ctxops.union_find__get_tmay_opaque_state(x)
        if tm:
            [opaque_state] = tm
            return opaque_state
        raise TypeError(r'raw_element@get opaque_state')


    @override
    def _sketchy_check__raw_element_(ctxops, x, /):
        'raw_element?/xelement -> None|TypeError'
        if ctxops.union_find__has_opaque_state(x):raise TypeError
    @override
    def _sketchy_check__inited_element_(ctxops, x, /):
        'element?/xelement -> None|TypeError'
        if not ctxops.union_find__has_opaque_state(x):raise TypeError
#class IUnionFindCtxOps__opaque_state4DisjointSet(IUnionFindCtxOps):










class IUnionFindCtxOps__opaque_state4DisjointSet__union_by_rank__path_compression(IUnionFindCtxOps__opaque_state4DisjointSet):
    r'''
    mutable_context :: ?
    opaque_state :: (tree_sz/rank/uint, parent_or_root/element)
    #'''
    __slots__ = ()
    @override
    def _union_find__mk_pseudo_opaque_state4raw_element_(ctxops, raw_x, /):
        'raw_element -> pseudo_opaque_state'
        #no union_find__mk_pseudo_opaque_state4raw_element
        #   since pseudo_opaque_state may not pass sketchy_check__opaque_state until raw_element be inited!!
        tree_sz = 1
        pseudo_root = raw_x
        pseudo__parent_or_root = pseudo_root
        pseudo_opaque_state = tree_sz, pseudo__parent_or_root
        return pseudo_opaque_state
    @override
    def _sketchy_check__opaque_state_(ctxops, opaque_state, /):
        'opaque_state?/obj -> None'
        check_pair(opaque_state)
        if 1:
            tree_sz, parent_or_root = opaque_state
            check_uint(tree_sz)
            ctxops.sketchy_check__inited_element(parent_or_root)

    @override
    def _sketchy_check__root_element_(ctxops, x, /):
        'root_element?/element -> None|TypeError'
        opaque_state = ctxops.union_find__get_opaque_state(x)
        tree_sz, parent_or_root = opaque_state
        if not ctxops.union_find_algo__eq(x, parent_or_root):raise TypeError

    @override
    def _union_find_algo__find_root_(ctxops, x, /):
        'element -> root_element #path_compression'

        get = ctxops.union_find__get_opaque_state
        eq = ctxops.union_find_algo__eq
        ls = []
        while 1:
            # x not in ls
            opaque_state = get(x)
            tree_sz, parent_or_root = opaque_state
            if 0:
              if eq(x, parent_or_root):
                # x == root
                # root not in ls
                root = parent_or_root
                    #not root = x
                break
            if x is parent_or_root:
                # x is root
                # root not in ls
                root = parent_or_root
                    #not root = x
                break
            parent = parent_or_root
            ####
            ls.append(x)
            x = parent
        # root not in ls
        if ls:
            ls.pop() # child of root
        if ls:
            #path_compression
            set_ = ctxops.union_find__set_opaque_state
            for z in ls:
                tree_sz, _ = get(z)
                opaque_state = tree_sz, root
                set_(z, opaque_state)

        return root

    @override
    def _union_find_algo__union_root_(ctxops, root_x, root_y, /):
        'root_element -> root_element -> root_element # [lhs is not rhs]' # [not eq(lhs, rhs)]
        eq = ctxops.union_find_algo__eq
        get = ctxops.union_find__get_opaque_state
        set_ = ctxops.union_find__set_opaque_state
        def root2true_root_ex(root, /):
            tree_sz, true_root = get(root)
            if not root is true_root:
                if not eq(root, true_root): raise TypeError
                _, _true_root = get(true_root)
                if not _true_root is true_root: raise logic-err
            return tree_sz, true_root

        if 1:
            # refresh root_x,root_y
            #   to be The True Root
            #   i.e. by "is" not by eq

            tree_sz_x, true_root_x = root2true_root_ex(root_x)
            tree_sz_y, true_root_y = root2true_root_ex(root_y)
            del root_x, root_y
            if true_root_x is true_root_y: return true_root_x
        true_root_x, true_root_y
        tree_sz_x, tree_sz_y

        #union_by_rank
        tree_sz_z = tree_sz_x + tree_sz_y
        if tree_sz_x < tree_sz_y:
            true_root_z = true_root_y
            child_w, tree_sz_w = true_root_x, tree_sz_x
        else:
            true_root_z = true_root_x
            child_w, tree_sz_w = true_root_y, tree_sz_y

        #bug:opaque_state_w = tree_sz_w, child_w
        opaque_state_w = tree_sz_w, true_root_z
        set_(child_w, opaque_state_w)

        opaque_state_z = tree_sz_z, true_root_z
        set_(true_root_z, opaque_state_z)

        return true_root_z
#class IUnionFindCtxOps__opaque_state4DisjointSet__union_by_rank__path_compression(IUnionFindCtxOps__opaque_state4DisjointSet):










class IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping(IUnionFindCtxOps__opaque_state4DisjointSet):
    r'''
    opaque_state :: ?
    mutable_context :: dict<element, opaque_state>
    #'''
    __slots__ = ()
    @override
    def _union_find__has_opaque_state_(ctxops, x, /):
        'xelement -> bool/(True@element, False@raw_element)'
        element2opaque_state = mutable_context = ctxops.get_mutable_context4ops()
        return x in element2opaque_state

    @override
    def _union_find__set_opaque_state_(ctxops, x, opaque_state, /):
        'element -> opaque_state -> None'
        element2opaque_state = mutable_context = ctxops.get_mutable_context4ops()
        if not x in element2opaque_state: raise TypeError('raw_element:not inited: use union_find_algo__init_raw_element instead')
        #overwrite
        element2opaque_state[x] = opaque_state

    @override
    def _union_find__get_opaque_state5inited_element_(ctxops, x, /):
        'element -> opaque_state'
        element2opaque_state = mutable_context = ctxops.get_mutable_context4ops()
        opaque_state = element2opaque_state[x]
        return opaque_state


    @override
    def _sketchy_check__xelement_(ctxops, x, /):
        'xelement?/obj -> None|TypeError'
        element2opaque_state = mutable_context = ctxops.get_mutable_context4ops()
        try:
            x in element2opaque_state
        except LookupError:
            raise TypeError
    @override
    def _sketchy_check__raw_element_(ctxops, x, /):
        'raw_element?/xelement -> None|TypeError'
        element2opaque_state = mutable_context = ctxops.get_mutable_context4ops()
        if x in element2opaque_state: raise TypeError('inited: not raw')
    @override
    def _sketchy_check__inited_element_(ctxops, x, /):
        'element?/xelement -> None|TypeError'
        element2opaque_state = mutable_context = ctxops.get_mutable_context4ops()
        if not x in element2opaque_state: raise TypeError('raw: not inited')

    @override
    def _union_find_algo__init_raw_element_(ctxops, raw_x, /):
        'raw_element -> None #emplace become element'
        element2opaque_state = mutable_context = ctxops.get_mutable_context4ops()
        pseudo_opaque_state = ctxops._union_find__mk_pseudo_opaque_state4raw_element_(raw_x)
        element2opaque_state[raw_x] = pseudo_opaque_state
        if 1:
            opaque_state = pseudo_opaque_state
            x = raw_x
            try:
                ctxops.sketchy_check__opaque_state(opaque_state)
                ctxops.sketchy_check__inited_element(x)
            except:
                del element2opaque_state[raw_x]
                raise
    @override
    def _union_find_algo__eq_(ctxops, x, y, /):
        'element -> element -> bool # [lhs is not rhs]'
        #hash mapping??
        return x == y

    @override
    def _sketchy_check__mutable_context_(ctxops, mutable_context, /):
        'ctxops -> mutable_context?/obj -> None|TypeError'
        element2opaque_state = mutable_context
        check_type_le(MutableMapping, element2opaque_state)



#class IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping(IUnionFindCtxOps__opaque_state4DisjointSet):


class IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression(IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping, IUnionFindCtxOps__opaque_state4DisjointSet__union_by_rank__path_compression):
    __slots__ = ()
    pass

class UnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression(IUnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression, ABC__no_slots):
    def __init__(sf, mutable_context, /):
        sf.sketchy_check__mutable_context(mutable_context)
        element2opaque_state = mutable_context
        sf._d = element2opaque_state


    @override
    def _get_mutable_context4ops_(ctxops, /):
        'ctxops -> mutable_context'
        return ctxops._d
    @override
    def _mk_ctxops__via_ireplace_mutable_context_(ctxops, mutable_context, /):
        'base_ctxops -> mutable_context -> new_ctxops'
        return type(ctxops)(mutable_context)
UnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression({})





if __name__ == "__main__":
    import doctest
    doctest.testmod()
