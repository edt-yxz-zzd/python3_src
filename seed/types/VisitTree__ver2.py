#__all__:goto
r'''[[[
e ../../python3_src/seed/types/VisitTree__ver2.py
view ../../python3_src/seed/recognize/tree/parse_tree.py
view ../../python3_src/seed/types/VisitTree.py

seed.types.VisitTree__ver2
py -m nn_ns.app.debug_cmd   seed.types.VisitTree__ver2 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.VisitTree__ver2:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.types.VisitTree__ver2:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
源起:
    view ../../python3_src/seed/recognize/tree/parse_tree.py
对 无限制深度的树 作变换
flatten_recur
]]


'#'; __doc__ = r'#'
>>> from seed.types.Either import mk_Left,mk_Right, Either,Cased
>>> tree = Either(True, (('(', ')'), (Either(True, (('(', ')'), (Either(False, '1'), Either(True, (('(', ')'), (Either(False, '2'), Either(False, '3')))), Either(True, (('(', ')'), ())), Either(True, (('(', ')'), (Either(False, '4'),))), Either(False, '5'), Either(False, '6'), Either(False, '7'), Either(True, (('(', ')'), (Either(True, (('(', ')'), ())),)))))),)))

>>> visitor = VisitTree__dfs__print()
>>> visitor.visit_(env:={}, ctx:=999, st:=333, root:=tree)
_setup_
_enter_node_
_visit_nonleaf__6pre_ ('(', ')')
_enter_node_
_visit_nonleaf__6pre_ ('(', ')')
_enter_node_
_visit_leaf_ 1
_exit_node_
_enter_node_
_visit_nonleaf__6pre_ ('(', ')')
_enter_node_
_visit_leaf_ 2
_exit_node_
_enter_node_
_visit_leaf_ 3
_exit_node_
_visit_nonleaf__6post_ ('(', ')')
_exit_node_
_enter_node_
_visit_nonleaf__6pre_ ('(', ')')
_visit_nonleaf__6post_ ('(', ')')
_exit_node_
_enter_node_
_visit_nonleaf__6pre_ ('(', ')')
_enter_node_
_visit_leaf_ 4
_exit_node_
_visit_nonleaf__6post_ ('(', ')')
_exit_node_
_enter_node_
_visit_leaf_ 5
_exit_node_
_enter_node_
_visit_leaf_ 6
_exit_node_
_enter_node_
_visit_leaf_ 7
_exit_node_
_enter_node_
_visit_nonleaf__6pre_ ('(', ')')
_enter_node_
_visit_nonleaf__6pre_ ('(', ')')
_visit_nonleaf__6post_ ('(', ')')
_exit_node_
_visit_nonleaf__6post_ ('(', ')')
_exit_node_
_visit_nonleaf__6post_ ('(', ')')
_exit_node_
_visit_nonleaf__6post_ ('(', ')')
_exit_node_
_result5state_
_teardown_
333

py_adhoc_call   seed.types.VisitTree__ver2   @f
from seed.types.VisitTree__ver2 import *
]]]'''#'''
__all__ = r'''
IVisitTree__dfs__ver2
    VisitTree__dfs__print


'''.split()#'''
    #ITree4Visit
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from functools import cached_property
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from abc import update_abstractmethods
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
flatten_recur = lazy_import4func_('seed.iters.flatten_recur', 'flatten_recur', __name__)
#.repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
#.
#.lazy_import4funcs_('seed.tiny_.containers', 'mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_', __name__)
#.if 0:from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_ #xxx:null_tuple
#.lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
#.if 0:from seed.debug.print_err import print_err
#.lazy_import4funcs_('seed.helper.ifNone', 'ifNone,ifNonef', __name__)
#.if 0:from seed.helper.ifNone import ifNone,ifNonef
#.lazy_import4funcs_('seed.tiny_.funcs', 'echo,fst,snd', __name__)
#.if 0:from seed.tiny_.funcs import echo,fst,snd
#.lazy_import4funcs_('seed.types.Either', 'mk_Left,mk_Right', __name__)
#.if 0:from seed.types.Either import mk_Left,mk_Right #Either,Cased
#.echo_or_mk_PeekableIterator = lazy_import4func_('seed.iters.PeekableIterator', 'echo_or_mk_PeekableIterator', __name__)
#.
#.
#.
#.
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args4env, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

#.class ITree4Visit(ABC):
#.    '(tree|tree_node_ops) # only used in IVisitTree__dfs__ver2._node2may_iter_children_().default_impl'
#.    __slots__ = ()
#.    @abstractmethod
#.    def node2may_iter_children_(sf, node, /):
#.        'node -> may (Iter node)'
#.    def is_leaf_(sf, node, /):
#.        'node -> bool'
#.        return None is sf.node2may_iter_children_(node)
class IVisitTree__dfs__ver2(ABC):
    r'''[[[
    [visitor :: IVisitTree__dfs__ver2]

    [wstN :: ((+1|0|-1|-2|-3),(result,st))]
    [wstN == (1/return_immediately,result)|(0/normal,st)|(-1/skip_subtree,st)|(-2/skip_subtree_and_post,st)|(-3/skip_subtree_and_post_and_sibling,st)]
        -1/skip@pre => skip subtree/(leaf|children)# but will still call post to check whether skip later sibling
        post may be skipped: +1,-2,-3
    [wstX :: ((+1|0|+2),(result,st))]
    [wstX == (1/return_immediately,result)|(0/normal,st)|(+2/skip_sibling,st)]
        +2/skip@post => skip later sibling
    [wstN == wst{pre}]
    [wstX == wst{post}]

    [env :: immutable-background-config]
    [ctx :: strict-stack operated via enter&exit pairs]
    [st :: varable operated via visit (pre&post donot form strict pair, i.e. pre run but post skipped)]
    [wst :: wrapped/cased st]

    [_setup_ :: *args -> **kwds -> (env, ctx, st, root)]
    [_teardown_ :: env -> ctx -> root -> None]
        #without st
    [_enter_node_ :: env -> ctx -> st -> node -> (ctx, st)]
        #with st
        # enter required succ st
    [_exit_node_ :: env -> ctx -> node -> ctx]
        #without st
        # cleanup without st when return result immediately # [wstX==(1,result)]

    [_visit_nonleaf__6pre_ :: env -> ctx -> st -> nonleaf -> wstN]
        #not affect ctx
    [_visit_nonleaf__6post_ :: env -> ctx -> st -> nonleaf -> wstX]
        #not affect ctx
        post may be skipped if wstN.case<-{+1,-2,-3}
            but exit never be skipped
    [_visit_leaf_ :: env -> ctx -> st -> leaf -> wstX]
        #not affect ctx

    #]]]'''#'''
    __slots__ = ()
    def visit_(sf, /, *args4setup, **kwds4setup):
        '-> result'
        (env, ctx, st, root) = sf._setup_(args4setup, kwds4setup)
        try:
            gi = _gi_visit_root_(sf, env, ctx, st, root)
            (ctx, result) = flatten_recur(gi)
        finally:
            sf._teardown_(env, ctx, root)
        return result

    ######################
    @abstractmethod
    def is_leaf_(sf, env, node, /):
        'env -> bool'
        return None is sf._node2may_iter_children_(env, node)
    @abstractmethod
    def _node2may_iter_children_(sf, env, node, /):
        '-> may (Iter node) # [None <==> (node is leaf){!!!not means skipped!!!}]'
        #.return tree.node2may_iter_children_(node)
    ######################
    @abstractmethod
    def _setup_(sf, args4setup, kwds4setup, /):
        '[_setup_ :: args4setup -> kwds4setup -> (env, ctx, st, root)]'
        if kwds4setup:
            raise TypeError
        (env, ctx, st, root) = args4setup
        return (env, ctx, st, root)
    @abstractmethod
    def _teardown_(sf, env, ctx, root, /):
        '[_teardown_ :: env -> ctx -> root -> None]'
        #without st
        return None
    @abstractmethod
    def _result5state_(sf, env, ctx, st, root, /):
        '[_result5state_ :: env -> ctx -> st -> root -> result] # after _exit_node_{root} # before _teardown_()'
        result = st
        return result
    @abstractmethod
    def _enter_node_(sf, env, ctx, st, node, /):
        '[_enter_node_ :: env -> ctx -> st -> node -> (ctx, st)]'
        #with st
        # enter required succ st
        return (ctx, st)
    @abstractmethod
    def _exit_node_(sf, env, ctx, node, /):
        '[_exit_node_ :: env -> ctx -> node -> ctx]'
        #without st
        # cleanup without st when return result immediately # [wstX==(1,result)]
        return ctx

    @abstractmethod
    def _visit_nonleaf__6pre_(sf, env, ctx, st, nonleaf, /):
        '[_visit_nonleaf__6pre_ :: env -> ctx -> st -> nonleaf -> wstN] #just after _enter_node_{nonleaf}'
        #not affect ctx
        return (wstN := (0, st))
    @abstractmethod
    def _visit_nonleaf__6post_(sf, env, ctx, st, nonleaf, /):
        '[_visit_nonleaf__6post_ :: env -> ctx -> st -> nonleaf -> wstX] #just before _exit_node_{nonleaf}'
        #not affect ctx
        #post may be skipped if wstN.case<-{+1,-2,-3}
        #   but exit never be skipped
        return (wstX := (0, st))
    @abstractmethod
    def _visit_leaf_(sf, env, ctx, st, leaf, /):
        '[_visit_leaf_ :: env -> ctx -> st -> leaf -> wstX] #just between _enter_node_{leaf} _exit_node_{leaf}'
        #not affect ctx
        return (wstX := (0, st))
    ######################

#end-class IVisitTree__dfs__ver2(ABC):
def _gi_visit_root_(sf, env, ctx, st, root, /):
    'GI:-> (ctx, result)'
    (ctx, wstX) = yield _gi_visit_node_(sf, env, ctx, st, root)
    match wstX:
        case (1, result):
            # return_immediately
            pass
        case (0|2, st):
            # normal | skip_sibling
            result = sf._result5state_(env, ctx, st, root)
        case (bad_case, _):
            raise ValueError(bad_case)
        case _:
            raise TypeError(type(wstX))
    result
    return (ctx, result)
def _gi_visit_node_(sf, env, ctx, st, node, /):
    'GI:-> (ctx, wstX)'
    (ctx, st) = sf._enter_node_(env, ctx, st, node)
    try:
        (ctx, wstX) = yield _gi_visit_node_inner_(sf, env, ctx, st, node)
    finally:
        ctx = sf._exit_node_(env, ctx, node)
    return (ctx, wstX)
def _gi_visit_node_inner_(sf, env, ctx, st, node, /):
    'GI:-> (ctx, wstX)'
    #.m = sf._node2may_iter_children_(env, node)
    #.b_leaf = m is None
    b_leaf = sf.is_leaf_(env, node)
    if b_leaf:
        leaf = node
        wstX = sf._visit_leaf_(env, ctx, st, leaf)
    else:
        nonleaf = node
        #.children = m
        children = sf._node2may_iter_children_(env, node)
        iter(children)
        wstN = sf._visit_nonleaf__6pre_(env, ctx, st, nonleaf)
        match wstN:
            case (0, st):
                # normal
                st
                # into children
                (ctx, wstX) = yield _gi_visit_children_(sf, env, ctx, st, children)
                # ?del wstX? No! ==>>: _post4visit_children_()
                wstX = _post4visit_children_(sf, env, ctx, wstX, nonleaf)
                    #will:call post{if not wstX.case==1}
                    #.wstX = sf._visit_nonleaf__6post_(env, ctx, st, nonleaf)
            case (-1, st):
                # skip_subtree
                st
                # not into children
                #call post
                wstX = sf._visit_nonleaf__6post_(env, ctx, st, nonleaf)
            case (-2, st):
                # skip_subtree_and_post
                # not into children
                # not call post
                wstX = (0, st)
                    #normal#continue:sibling
            case (-3, st):
                # skip_subtree_and_post_and_sibling
                # not into children
                # not call post
                wstX = (2, st)
                    #skip_sibling
            case (1, result):
                # return_immediately
                wstX = wstN
            case (bad_case, _):
                raise ValueError(bad_case)
            case _:
                raise TypeError(type(wstN))
    ctx, wstX #updated
    return (ctx, wstX)
def _gi_visit_children_(sf, env, ctx, st, children, /):
    'GI:-> (ctx, wstX)'
    wstX = (0, st) # for empty children
    for child in children:
        st
        (ctx, wstX) = yield _gi_visit_node_(sf, env, ctx, st, child)
        match wstX:
            case (0, st):
                # normal
                st
                continue
            case (1, result):
                # return_immediately
                wstX
                #return (ctx, wstX)
                break
            case (2, st):
                # skip_sibling
                wstX = (0, st)
                break
            case (bad_case, _):
                raise ValueError(bad_case)
            case _:
                raise TypeError(type(wstX))
    wstX
    return (ctx, wstX)

def _post4visit_children_(sf, env, ctx, wstX, nonleaf, /):
    '-> wstX'
    #will:call post{if not wstX.case==1}
    #.wstX = sf._visit_nonleaf__6post_(env, ctx, st, nonleaf)
    match wstX:
        case (0|-1, st):
            # normal | skip_sibling
            # skip_sibling@children-level, but now all children processed, hence no child to be skipped
            777;wstX = (0, st)
            wstX = sf._visit_nonleaf__6post_(env, ctx, st, nonleaf)
        case (1, result):
            # return_immediately
            wstX
            pass
        case (bad_case, _):
            raise ValueError(bad_case)
        case _:
            raise TypeError(type(wstX))

    wstX
    return wstX
class VisitTree__dfs__print(IVisitTree__dfs__ver2):
    '[Tree a b = Either a (b, [Tree a b])]'
    ___no_slots_ok___ = True
    ######################
    @override
    def is_leaf_(sf, env, node, /):
        'env -> bool'
        return not node[0]
    @override
    def _node2may_iter_children_(sf, env, node, /):
        '-> may (Iter node) # [None <==> (node is leaf){!!!not means skipped!!!}]'
        match node:
            case (False, payload4leaf):
                return None
            case (True, (payload4noleaf, children)):
                return iter(children)
        raise TypeError(node)
    ######################
    @override
    def _setup_(sf, args4setup, kwds4setup, /):
        '[_setup_ :: args4setup -> kwds4setup -> (env, ctx, st, root)]'
        if kwds4setup:
            raise TypeError
        (env, ctx, st, root) = args4setup
        print('_setup_')
        return (env, ctx, st, root)
    @override
    def _teardown_(sf, env, ctx, root, /):
        '[_teardown_ :: env -> ctx -> root -> None]'
        #without st
        print('_teardown_')
        return None
    @override
    def _result5state_(sf, env, ctx, st, root, /):
        '[_result5state_ :: env -> ctx -> st -> root -> result] # after _exit_node_{root} # before _teardown_()'
        print('_result5state_')
        result = st
        return result
    @override
    def _enter_node_(sf, env, ctx, st, node, /):
        '[_enter_node_ :: env -> ctx -> st -> node -> (ctx, st)]'
        #with st
        # enter required succ st
        print('_enter_node_')
        return (ctx, st)
    @override
    def _exit_node_(sf, env, ctx, node, /):
        '[_exit_node_ :: env -> ctx -> node -> ctx]'
        #without st
        # cleanup without st when return result immediately # [wstX==(1,result)]
        print('_exit_node_')
        return ctx

    @override
    def _visit_nonleaf__6pre_(sf, env, ctx, st, nonleaf, /):
        '[_visit_nonleaf__6pre_ :: env -> ctx -> st -> nonleaf -> wstN] #just after _enter_node_{nonleaf}'
        #not affect ctx
        print('_visit_nonleaf__6pre_', nonleaf[1][0])
        return (wstN := (0, st))
    @override
    def _visit_nonleaf__6post_(sf, env, ctx, st, nonleaf, /):
        '[_visit_nonleaf__6post_ :: env -> ctx -> st -> nonleaf -> wstX] #just before _exit_node_{nonleaf}'
        #not affect ctx
        #post may be skipped if wstN.case<-{+1,-2,-3}
        #   but exit never be skipped
        print('_visit_nonleaf__6post_', nonleaf[1][0])
        return (wstX := (0, st))
    @override
    def _visit_leaf_(sf, env, ctx, st, leaf, /):
        '[_visit_leaf_ :: env -> ctx -> st -> leaf -> wstX] #just between _enter_node_{leaf} _exit_node_{leaf}'
        #not affect ctx
        print('_visit_leaf_', leaf[1])
        return (wstX := (0, st))
    ######################
print

__all__
#[f,g] = lazy_import4funcs_('seed.types.VisitTree__ver2', 'f,g', __name__)
from seed.types.VisitTree__ver2 import *
