#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/almost_graph/tree/conformal_transformation.py

seed.algo.almost_graph.tree.conformal_transformation
py -m nn_ns.app.debug_cmd   seed.algo.almost_graph.tree.conformal_transformation -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.almost_graph.tree.conformal_transformation:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.algo.almost_graph.tree.conformal_transformation:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.algo.almost_graph.tree.conformal_transformation:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
源起:
平行识别器/投喂型识别器
输出类型 只能是 特定某些封装类型
    基础型:Raw/LazyRaw
    结构型:Tuple/Array/Union/...
后处理:
    * 用户外赋后处理:可忽略，不影响成败流程，用户自定义，保形变换
    * 释义内禀后处理:可忽略，不影响成败流程，语义相关，保形变换
    * 流程内禀后处理:不可忽略，影响成败流程，语法相关，非保形变换
保形变换:
    基础型 -> 基础型
    结构型 -> (基础型|结构型{保持原先结构})

]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.algo.almost_graph.tree.conformal_transformation   @f
]]]'''#'''
__all__ = r'''
IOps4ConformalTransformation
    conformal_transformation_
        std_conformal_transformation_
            gi_std_conformal_transformation_


ISemiOps4ConformalTransformation__part_ops7tree_struct
ISemiOps4ConformalTransformation__part_ops7transform

IOps4ConformalTransformation
    IOps4ConformalTransformation__wrapped_part_ops7transform
    IOps4ConformalTransformation__wrapped_part_ops7tree_struct
    IOps4ConformalTransformation__impl_part_ops7tree_struct__via_IFoldableFunctor

IFoldableFunctor
    IFoldableFunctor__mixins4seq
    IFoldableFunctor__mixins4mapping
    IFoldableFunctor__mixins4cased_union




Error__not_either
    Error__bad_type4either
    Error__bad_payload4either
    Error__bad_type4case4either

Error__not_node
Error__wrong_node_type
    Error__leaf
    Error__fork




mk_exc5bad_either_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.iters.flatten_recur import flatten_recur
    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__


class Error__not_either(Exception):pass
class Error__bad_type4either(Error__not_either):pass
class Error__bad_type4case4either(Error__not_either):pass
class Error__bad_payload4either(Error__not_either):pass

class Error__not_node(Exception):pass
# no:[Error__wrong_node_type <: Error__not_node]
class Error__wrong_node_type(Exception):pass
class Error__fork(Error__wrong_node_type):pass
class Error__leaf(Error__wrong_node_type):pass


class ISemiOps4ConformalTransformation__part_ops7tree_struct(ABC):
    __slots__ = ()
    #########
    @abstractmethod
    def gi_fmap4fork_(sf, env, gi_f, wst, fork, /):
        'GI:env -> gi_f/(GI:wst -> a -> (b, wst)) -> wst -> fork/node{a} -> (fork7new/node{b}, wst) # NOTE:[if all children unchanged and the fork node is immutable then fork7new SHOULD-BEST-BE the old fork node]'
        return; yield
    @abstractmethod
    def is_leaf_node_(sf, env, node, /):
        'env -> node -> bool|^Error__not_node'
    #########
    def is_fork_node_(sf, env, node, /):
        'env -> node -> bool|^Error__not_node'
        return not sf.is_leaf_node_(env, node)
    #########
class ISemiOps4ConformalTransformation__part_ops7transform(ABC):
    __slots__ = ()
    #########
    @abstractmethod
    def gi_fmap4leaf_(sf, env, ctx, st, leaf, /):
        'GI:env -> ctx -> st -> leaf/node -> (leaf7new, st7new) # NOTE:[if leaf payload unchanged and the leaf node is immutable then leaf7new SHOULD-BEST-BE the old leaf node]'
        return; yield
    #########
    @abstractmethod
    def gi_enter4fmap4fork_(sf, env, ctx, st, fork, /):
        'GI:env -> ctx -> st -> fork/node -> Either (leaf7new, st7new) (ctx7deeper, st7deeper)'
        return; yield
    @abstractmethod
    def gi_exit4fmap4fork_(sf, env, ctx, st, fork, fork7new, ctx7deeper, st7deeper7new, /):
        'GI:env -> ctx -> st -> fork/node -> fork7new -> ctx7deeper -> st7deeper7new -> Either (leaf7new, st7new) st7new'
        return; yield
    #########
class IOps4ConformalTransformation(ISemiOps4ConformalTransformation__part_ops7transform, ISemiOps4ConformalTransformation__part_ops7tree_struct):
    r'''
    [GI:generator_iterator:see flatten_recur()]

    [node == (leaf|fork)]

    [env unchanged at all levels]
    [ctx unchanged for children node of same parent node]
    [st changed when visit{leaf}/enter{fork}/exit{fork}]

    [env used as background global setting]
    [ctx used as stacked local setting]
    [st used as accumulating state or intermediate result for final output]'

    '''#'''
    __slots__ = ()
    #########
    def gi_conformal_transformation_(sf, env, ctx, st, node, /):
        'GI:env -> ctx -> st -> node -> (node7new, st7new)'
        return gi_std_conformal_transformation_(sf, env, ctx, st, node)
    #########
    def conformal_transformation_(sf, env, ctx, st, node, /):
        'env -> ctx -> st -> node -> (node7new, st7new) # override .gi_std_conformal_transformation_() insted this method/.conformal_transformation_()'
        gi = sf.gi_conformal_transformation_(env, ctx, st, node)
        return flatten_recur(gi)
    #########
#end-class IOps4ConformalTransformation(ABC):



def conformal_transformation_(ops, env, ctx, st, node, /):
    'ops -> env -> ctx -> st -> node -> (node7new, st7new) # [ops :: IOps4ConformalTransformation]'
    return ops.conformal_transformation_(env, ctx, st, node)
def std_conformal_transformation_(ops, env, ctx, st, node, /):
    'ops -> env -> ctx -> st -> node -> (node7new, st7new) # [ops :: IOps4ConformalTransformation]'
    gi = gi_std_conformal_transformation_(ops, env, ctx, st, node)
    return flatten_recur(gi)
def _gi_f(wst, node, /):
    'GI:(wst -> node -> (node7new, wst7new))'
    (header, st) = wst
    (ops, env, ctx) = header
    (node7new, st7new) = yield gi_std_conformal_transformation_(ops, env, ctx, st, node)
    wst7new = (header, st7new)
    return (node7new, wst7new)
    777; yield
def gi_std_conformal_transformation_(ops, env, ctx, st, node, /):
    'GI:ops -> env -> ctx -> st -> node -> (node7new, st7new) # [ops :: IOps4ConformalTransformation]'
    if ops.is_leaf_node_(env, node):
        leaf = node
        (leaf7new, st7new) = yield ops.gi_fmap4leaf_(env, ctx, st, leaf)
        is_new_node_leaf = True
    else:
        fork = node
        x = yield ops.gi_enter4fmap4fork_(env, ctx, st, fork)
            # Either (leaf7new, st7new) (ctx7deeper, st7deeper)
        match x:
            case (False, (leaf7new, st7new)):
                is_new_node_leaf = True
            case (True, (ctx7deeper, st7deeper)):
                wst = (header:=(ops, env, ctx7deeper), st7deeper)
                #_gi_f
                (fork7new, wst7new) = yield ops.gi_fmap4fork_(env, _gi_f, wst, fork)
                (_header, st7deeper7new) = wst7new
                y = yield ops.gi_exit4fmap4fork_(env, ctx, st, fork, fork7new, ctx7deeper, st7deeper7new)
                    #Either (leaf7new, st7new) st7new
                match y:
                    case (False, (leaf7new, st7new)):
                        del fork7new
                        is_new_node_leaf = True
                    case (True, st7new):
                        fork7new
                        is_new_node_leaf = False
                    case _:
                        raise mk_exc5bad_either_(y)
            case _:
                raise mk_exc5bad_either_(x)

    st7new
    if is_new_node_leaf:
        node7new = leaf7new
        if not ops.is_leaf_node_(env, node7new):raise Error__fork
    else:
        node7new = fork7new
        if ops.is_leaf_node_(env, node7new):raise Error__leaf
    node7new
    return (node7new, st7new)

def mk_exc5bad_either_(x, /):
    match x:
        case (case, payload):
            if not type(case) is bool:
                return Error__bad_type4case4either(type(case))
            return Error__bad_payload4either(payload)
        case _:
            return Error__bad_type4either(type(x))
    raise 000






class IOps4ConformalTransformation__wrapped_part_ops7transform(IOps4ConformalTransformation):
    __slots__ = ()
    #########
    @property
    @abstractmethod
    def part_ops7transform(sf, /):
        '-> ISemiOps4ConformalTransformation__part_ops7transform'
    #########
    @override
    def gi_fmap4leaf_(sf, env, ctx, st, leaf, /):
        'GI:env -> ctx -> st -> leaf/node -> (leaf7new, st7new) # NOTE:[if leaf payload unchanged and the leaf node is immutable then leaf7new SHOULD-BEST-BE the old leaf node]'
        return sf.part_ops7transform.gi_fmap4leaf_(env, ctx, st, leaf)
    #########
    @override
    def gi_enter4fmap4fork_(sf, env, ctx, st, fork, /):
        'GI:env -> ctx -> st -> fork/node -> Either (leaf7new, st7new) (ctx7deeper, st7deeper)'
        return sf.part_ops7transform.gi_enter4fmap4fork_(env, ctx, st, fork)
    @override
    def gi_exit4fmap4fork_(sf, env, ctx, st, fork, fork7new, ctx7deeper, st7deeper7new, /):
        'GI:env -> ctx -> st -> fork/node -> fork7new -> ctx7deeper -> st7deeper7new -> Either (leaf7new, st7new) st7new'
        return sf.part_ops7transform.gi_exit4fmap4fork_(env, ctx, st, fork, fork7new, ctx7deeper, st7deeper7new)
    #########

class IOps4ConformalTransformation__wrapped_part_ops7tree_struct(IOps4ConformalTransformation):
    __slots__ = ()
    #########
    @property
    @abstractmethod
    def part_ops7tree_struct(sf, /):
        '-> ISemiOps4ConformalTransformation__part_ops7tree_struct'
    #########
    @override
    def gi_fmap4fork_(sf, env, gi_f, wst, fork, /):
        'GI:env -> gi_f/(GI:wst -> a -> (b, wst)) -> wst -> fork/node{a} -> (fork7new/node{b}, wst) # NOTE:[if all children unchanged and the fork node is immutable then fork7new SHOULD-BEST-BE the old fork node]'
        return sf.part_ops7tree_struct.gi_fmap4fork_(env, gi_f, wst, fork)
    @override
    def is_leaf_node_(sf, env, node, /):
        'env -> node -> bool|^Error__not_node'
        return sf.part_ops7tree_struct.is_leaf_node_(env, node)
    #########



class IOps4ConformalTransformation__impl_part_ops7tree_struct__via_IFoldableFunctor(IOps4ConformalTransformation):
    '[fork :: IFoldableFunctor]'
    __slots__ = ()
    #########
    @override
    def gi_fmap4fork_(sf, env, gi_f, wst, fork, /):
        'GI:env -> gi_f/(GI:wst -> a -> (b, wst)) -> wst -> fork/node{a} -> (fork7new/node{b}, wst) # NOTE:[if all children unchanged and the fork node is immutable then fork7new SHOULD-BEST-BE the old fork node]'
        return fork.gi_fmap_(gi_f, wst)
    #########

class IFoldableFunctor(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def whether_immutable(sf, /):
        '-> bool'
    @abstractmethod
    def _from_ordered_iterable4fmap_(sf, iterable, /):
        '(#sf -> #)Iter x -> __class__  # [not classmethod]'
    @abstractmethod
    def _to_ordered_iterable4fmap_(sf, /):
        '(#sf -> #)Iter x'
    #foldl
    #@abstractmethod
    def gi_fmap_(sf, gi_f, wst, /):
        'GI:(#sf/fork/node{a} -> #)gi_f/(GI:wst -> a -> (b, wst)) -> wst -> (fork7new/node{b}, wst) # NOTE:[if all children unchanged and the fork node is immutable then fork7new SHOULD-BEST-BE the old fork node]'
        it = iter(sf._to_ordered_iterable4fmap_())
        same = True
        ys = []
        for x in it:
            (y, wst) = yield gi_f(wst, x)
            ys.append(y)
            same = same and x is y
        same, ys, wst
        if same and sf.whether_immutable:
            ot = sf
        else:
            ot = sf._from_ordered_iterable4fmap_(ys)
        ot, wst
        return (ot, wst)
    #########

class IFoldableFunctor__mixins4seq(IFoldableFunctor):
    __slots__ = ()
    @override
    def _to_ordered_iterable4fmap_(sf, /):
        '(#sf -> #)Iter x'
        return iter(sf)
class IFoldableFunctor__mixins4mapping(IFoldableFunctor):
    __slots__ = ()
    @abstractmethod
    def _from_ordered_items4fmap_(sf, iterable, /):
        '(#sf -> #)Iter x -> __class__  # [not classmethod]'
    #@abstractmethod
    def _to_ordered_keys4fmap_(sf, /):
        '(#sf -> #)Iter k'
        return reversed(sf)
    @override
    def _from_ordered_iterable4fmap_(sf, iterable, /):
        '(#sf -> #)Iter x -> __class__  # [not classmethod]'
        return sf._from_ordered_items4fmap_(zip(sf._to_ordered_keys4fmap_(), iterable))
    @override
    def _to_ordered_iterable4fmap_(sf, /):
        '(#sf -> #)Iter x'
        for k in sf._to_ordered_keys4fmap_():
            yield sf[k]
        return
class IFoldableFunctor__mixins4cased_union(IFoldableFunctor):
    __slots__ = ()
    @abstractmethod
    def _from_payload4fmap_(sf, payload, /):
        '(#sf -> #)payload -> __class__  # [not classmethod]'
    @override
    def _from_ordered_iterable4fmap_(sf, iterable, /):
        '(#sf -> #)Iter x -> __class__  # [not classmethod]'
        [payload] = iterable
        return sf._from_payload4fmap_(payload)
    @override
    def _to_ordered_iterable4fmap_(sf, /):
        '(#sf -> #)Iter x'
        #yield sf.payload
        match sf:
            case (case, payload):
                yield payload
                return
        raise 000


__all__
from seed.algo.almost_graph.tree.conformal_transformation import IOps4ConformalTransformation, conformal_transformation_
from seed.algo.almost_graph.tree.conformal_transformation import std_conformal_transformation_, gi_std_conformal_transformation_

from seed.algo.almost_graph.tree.conformal_transformation import \
(IOps4ConformalTransformation
,    IOps4ConformalTransformation__wrapped_part_ops7transform
,    IOps4ConformalTransformation__wrapped_part_ops7tree_struct
,    IOps4ConformalTransformation__impl_part_ops7tree_struct__via_IFoldableFunctor
,IFoldableFunctor
,    IFoldableFunctor__mixins4seq
,    IFoldableFunctor__mixins4mapping
,    IFoldableFunctor__mixins4cased_union
,Error__not_either
,    Error__bad_type4either
,    Error__bad_payload4either
,    Error__bad_type4case4either
,Error__not_node
,Error__wrong_node_type
,    Error__leaf
,    Error__fork
)



from seed.algo.almost_graph.tree.conformal_transformation import *
