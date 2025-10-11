#__all__:goto
#TODO:visit_tree_
r'''[[[
e ../../python3_src/seed/recognize/tree/parse_tree.py
view ../../python3_src/seed/types/VisitTree.py
view ../../python3_src/seed/types/VisitTree__ver2.py

seed.recognize.tree.parse_tree
py -m nn_ns.app.debug_cmd   seed.recognize.tree.parse_tree -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.tree.parse_tree:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.recognize.tree.parse_tree:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
源起:
    嵌套
    无限深嵌套
假设:
    整树使用一致的词法分析
fully parenthesized notation
全括号表示法
]]
[[

TODO:函数参数数量固化:
Polish notation
波兰表示法
reversed Polish notation
逆波兰表示法

但是 无法 迭代读取 reversed_Polish_notation，因为 不论读多少，都可能是 后面函数的操作数
]]



'#'; __doc__ = r'#'

>>> _g = {'(':1,')':2,'.':3}.get
>>> def case5token_(c, /): return _g(c,0)
>>> it = echo_or_mk_PeekableIterator('((1(23)()(4)567(())))8.9')
>>> [*iter_parse_trees_(case5token_, it)]
[Either(True, (('(', ')'), (Either(True, (('(', ')'), (Either(False, '1'), Either(True, (('(', ')'), (Either(False, '2'), Either(False, '3')))), Either(True, (('(', ')'), ())), Either(True, (('(', ')'), (Either(False, '4'),))), Either(False, '5'), Either(False, '6'), Either(False, '7'), Either(True, (('(', ')'), (Either(True, (('(', ')'), ())),)))))),))), Either(False, '8')]

>>> [*it]
['.', '9']

>>> it = echo_or_mk_PeekableIterator('(8.9)')
>>> [*iter_parse_trees_(case5token_, it)]
Traceback (most recent call last):
    ...
seed.recognize.tree.parse_tree.Error__missing_close_token: (3, '.')
>>> it.peek_relax()
('.',)








>>> def xnum_fanins5token_(c, /):
...     if c.isdigit():
...         #op
...         num_fanins = int(c)
...         return num_fanins
...     elif c.isalpha():
...         #value
...         return -1
...     else:
...         return -2
>>> it = echo_or_mk_PeekableIterator('31a3b2c0111d010111a.9')
>>> [*iter_parse_trees__plain_Polish_notation_(xnum_fanins5token_, it)]
[Either(True, ('3', (Either(True, ('1', (Either(False, 'a'),))), Either(True, ('3', (Either(False, 'b'), Either(True, ('2', (Either(False, 'c'), Either(True, ('0', ()))))), Either(True, ('1', (Either(True, ('1', (Either(True, ('1', (Either(False, 'd'),))),))),)))))), Either(True, ('0', ()))))), Either(True, ('1', (Either(True, ('0', ())),))), Either(True, ('1', (Either(True, ('1', (Either(True, ('1', (Either(False, 'a'),))),))),)))]
>>> it.peek_relax()
('.',)
>>> [*it]
['.', '9']







py_adhoc_call   seed.recognize.tree.parse_tree   @f
]]]'''#'''
__all__ = r'''
iter_parse_trees_
    mkr4iter_parse_trees_

iter_parse_trees__plain_Polish_notation_
    mkr4iter_parse_trees__plain_Polish_notation_

BaseError__parse_tree
    Error__missing_close_token
    Error__mismatch_open_close_token
    Error__missing_child
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from functools import cached_property
from seed.tiny_.check import check_type_is, check_int_ge
#.
from abc import update_abstractmethods
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
#.repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
#.
#.lazy_import4funcs_('seed.tiny_.containers', 'mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_', __name__)
#.if 0:from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_
lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
if 0:from seed.debug.print_err import print_err
lazy_import4funcs_('seed.helper.ifNone', 'ifNone,ifNonef', __name__)
if 0:from seed.helper.ifNone import ifNone,ifNonef
lazy_import4funcs_('seed.tiny_.funcs', 'echo,fst,snd', __name__)
if 0:from seed.tiny_.funcs import echo,fst,snd
lazy_import4funcs_('seed.types.Either', 'mk_Left,mk_Right', __name__)
if 0:from seed.types.Either import mk_Left,mk_Right
#.from seed.types.Either import Cased, Either
flatten_recur = lazy_import4func_('seed.iters.flatten_recur', 'flatten_recur', __name__)
echo_or_mk_PeekableIterator = lazy_import4func_('seed.iters.PeekableIterator', 'echo_or_mk_PeekableIterator', __name__)

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
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

if 0:
  def visit_tree_(tree, enter_root_):
    r'''[[[
class???
view ../../python3_src/seed/types/VisitTree.py
view ../../python3_src/seed/types/VisitTree__ver2.py


    [enter_root_ :: whole_tree -> wst]
    [enter_node_ :: may (tree -> st -> wst)]
    [enter_fork_ :: may (fork -> st -> wst)]
    [visit_leaf_ :: may (leaf -> st -> wst)]
    [exit_fork_ :: may (fork -> st -> wst)]
    [exit_node_ :: may (tree -> st -> wst)]
    [exit_root_ :: whole_tree -> st -> result]
    [wst == (1,result)|(0,st/into)|(-1,st/skip)]
        skip@exit => skip later sibling
        skip@enter => skip children# but will still call exit to check whether skip later sibling
    #]]]'''#'''

def iter_parse_trees_(case5token_, tokens, /, *, data5token_=None, match_=None, key=None, Leaf=None, Fork=None, Children=None, nonpeekable_ok=False):
    ':: (tkn -> uint%3) -> PeekableIterator token -> Iter (Tree dat)  #see:mkr4iter_parse_trees_.__doc__'
    iter_parse_trees_ = mkr4iter_parse_trees_(case5token_, data5token_=data5token_, match_=match_, key=key, Leaf=Leaf, Fork=Fork, Children=Children)
    return iter_parse_trees_(tokens, nonpeekable_ok=nonpeekable_ok)

class _IToken__with_LazyProperties(ABC):
    ___no_slots_ok___ = True
    @property
    @abstractmethod
    def key(sf, /):
        ''
    @property
    @abstractmethod
    def case5token_(sf, /):
        ''
    @property
    @abstractmethod
    def data5token_(sf, /):
        ''
    @property
    @abstractmethod
    def _match_(sf, /):
        ''

    def __init__(sf, token, /):
        sf.token = token
    @cached_property
    def tkn(sf, /):
        return sf.key(sf.token)
    @cached_property
    def case(sf, /):
        #bug:return sf.case5token_(sf.token)
        return sf.case5token_(sf.tkn)
    @cached_property
    def dat(sf, /):
        #bug:return sf.data5token_(sf.token)
        return sf.data5token_(sf.tkn)
    def match_(sf, ot, /):
        #bug:return sf._match_(sf.token, ot.token)
        return sf._match_(sf.tkn, ot.tkn)
#_Token__with_LazyProperties(key, case5token_, data5token_, match_, token)
def _mk_subclass4Token__with_LazyProperties_(key, case5token_, data5token_, match_):
    class _Token__with_LazyProperties(_IToken__with_LazyProperties):
        #key = key
            #NameError: name 'key' is not defined
        pass
    T = _Token__with_LazyProperties
    #@override
    T.key = staticmethod(key)
    #@override
    T.case5token_ = staticmethod(case5token_)
    #@override
    T.data5token_ = staticmethod(data5token_)
    #@override
    T._match_ = staticmethod(match_)
    update_abstractmethods(T)
    return _Token__with_LazyProperties

class _ITokenII__with_LazyProperties(ABC):
    ___no_slots_ok___ = True
    @property
    @abstractmethod
    def key(sf, /):
        ''
    @property
    @abstractmethod
    def xnum_fanins5token_(sf, /):
        ''
    @property
    @abstractmethod
    def data5token_(sf, /):
        ''
    def __init__(sf, token, /):
        sf.token = token
    @cached_property
    def tkn(sf, /):
        return sf.key(sf.token)
    @cached_property
    def xnum_fanins(sf, /):
        return sf.xnum_fanins5token_(sf.tkn)
    @cached_property
    def dat(sf, /):
        return sf.data5token_(sf.tkn)
#_TokenII__with_LazyProperties(key, xnum_fanins5token_, data5token_, token)
def _mk_subclass4TokenII__with_LazyProperties_(key, xnum_fanins5token_, data5token_):
    class _TokenII__with_LazyProperties(_ITokenII__with_LazyProperties):
        pass
    T = _TokenII__with_LazyProperties
    #@override
    T.key = staticmethod(key)
    #@override
    T.xnum_fanins5token_ = staticmethod(xnum_fanins5token_)
    #@override
    T.data5token_ = staticmethod(data5token_)
    update_abstractmethods(T)
    return _TokenII__with_LazyProperties




class _PeekableIterator__over_PeekableIterator:
    def __init__(sf, f, it, /):
        sf._f = f
        sf._it = it
        sf._tm = []
    @property
    def the_peekable_iterator(sf, /):
        return sf._it
    @property
    def head(sf, /):
        tm = sf._tm
        if not tm:
            _h = sf._it.head
            h = sf._f(_h)
            tm.append(h)
        [h] = tm
        return h
    def is_empty(sf, /):
        return sf._it.is_empty()
    def read1(sf, /):
        h = sf.head
        #if 0b0000:print_err(h)
        sf._it.read1()
        sf._tm.clear()
        return h

class BaseError__parse_tree(Exception):pass
#class Error__bad_head_token(BaseError__parse_tree):pass
class Error__missing_close_token(BaseError__parse_tree):pass
class Error__mismatch_open_close_token(BaseError__parse_tree):pass
class Error__missing_child(BaseError__parse_tree):pass

_x2y2True = lambda x,y:True
def mkr4iter_parse_trees_(case5token_, /, *, data5token_=None, match_=None, key=None, Leaf=None, Fork=None, Children=None):
    r'''[[[
    :: case5token_ -> iter_parse_trees_

    ######################
    #output:
    [iter_parse_trees_ :: PeekableIterator token -> Iter (Tree dat)]

    ######################
    #throw:
    ^Error__missing_close_token
    ^Error__mismatch_open_close_token

    ######################
    #args:
    [case5token_ :: tkn -> case/uint%3]
        case:
            0 - leaf
            1 - open
            2 - close
            _ - external data

    ######################
    #kwds:
    [Children :: may ([Tree dat] -> Seq (Tree dat))]
        default:tuple
    [Fork :: may (((open/dat, close/dat), children/[Tree dat]) -> Fork dat)]
        default:mk_Right
    [Leaf :: may (dat -> Leaf dat)]
        default:mk_Left
    [key :: may (token -> tkn)]
        default:echo
    [match_ :: may (tkn{open} -> tkn{close} -> bool)]
        default:\_ _->True
        used to distinguish parentheses:『()』『[]』『{}』
    [data5token_ :: may (tkn -> dat)]
        default:echo

    default:[Tree a =[def]= Either a ((open/a, close/a), children/[Tree a])]
    <<==:
    data Tree a
        = Leaf a
        | Fork ((a, a), Children (Tree a))
    data Children a ~= [a] # userdefined
    <<==:
    [Tree a b = Either a (b, [Tree a b])]


    #]]]'''#'''

    data5token_ = ifNone(data5token_, echo)
    match_ = ifNone(match_, _x2y2True)
    key = ifNone(key, echo)
    Leaf = ifNone(Leaf, mk_Left)
    Fork = ifNone(Fork, mk_Right)
    Children = ifNone(Children, tuple)
    _Token__with_LazyProperties = _mk_subclass4Token__with_LazyProperties_(key, case5token_, data5token_, match_)

    def iter_parse_trees_(peekable_tokens, /, *, nonpeekable_ok=False):
        '[iter_parse_trees_ :: PeekableIterator token -> Iter (Tree dat)] #see:mkr4iter_parse_trees_.__doc__'
        it = echo_or_mk_PeekableIterator(peekable_tokens)
        if not (nonpeekable_ok or it is peekable_tokens):raise TypeError(type(peekable_tokens))
        777;del peekable_tokens
        it = _PeekableIterator__over_PeekableIterator(_Token__with_LazyProperties, it)

        while 1:
            tm = _main4read_tmay_tree(depth:=0, it)
            if not tm:
                break
            [tree] = tm
            yield tree
        return it.the_peekable_iterator

    def _main4read_tmay_tree(depth, it, /):
        'uint -> _PeekableIterator__over_PeekableIterator token -> tmay (Tree dat)'
        gi = _mk_gi4read_tmay_tree(depth, it)
        return flatten_recur(gi)

    def _mk_gi4read_tmay_tree(depth, it, /):
        'GI:uint -> _PeekableIterator__over_PeekableIterator token -> tmay (Tree dat)'
        if it.is_empty():
            return ()
        _wtkn = it.head
        _case = _wtkn.case
        match _case:
            case 0:
                # leaf
                wtkn8leaf = _wtkn
                777;it.read1()
                777;del _wtkn, _case
                dat8leaf = wtkn8leaf.dat
                leaf = Leaf(dat8leaf)
                tree = leaf
            case 1:
                # open
                wtkn8open = _wtkn
                777;it.read1()
                777;del _wtkn, _case
                dat8open = wtkn8open.dat
                children = yield _mk_gi4read_children(depth, it)
                _wtkn = it.head
                _case = _wtkn.case
                if not _case in (2,):
                    #.raise Error__missing_close_token(_case)
                    raise Error__missing_close_token((_case, it.head.token))
                if not wtkn8open.match_(_wtkn):
                    raise Error__mismatch_open_close_token((wtkn8open, _wtkn))
                wtkn8close = _wtkn
                777;it.read1()
                777;del _wtkn, _case
                dat8close = wtkn8close.dat
                dat4node = (dat8open, dat8close)
                fork = Fork((dat4node, children))
                tree = fork
            case _:
                # close | external data...
                return ()
        tree
        return (tree,)
    def _mk_gi4read_children(depth, it, /):
        'GI:uint -> _PeekableIterator__over_PeekableIterator token -> Children (Tree dat)'
        depth += 1
        ls = []
        while 1:
            tm = yield _mk_gi4read_tmay_tree(depth, it)
            if not tm:
                break
            [tree] = tm
            ls.append(tree)
        ls
        return Children(ls)
    return iter_parse_trees_
#end-def mkr4iter_parse_trees_(case5token_, /, *, data5token_=None, match_=None, key=None, Leaf=None, Fork=None, Children=None):




def iter_parse_trees__plain_Polish_notation_(xnum_fanins5token_, peekable_tokens, /, *, data5token_=None, key=None, Leaf=None, Fork=None, Children=None, nonpeekable_ok=False):
    '[iter_parse_trees__plain_Polish_notation_ :: PeekableIterator token -> Iter (Tree dat)] #see:mkr4iter_parse_trees__plain_Polish_notation_.__doc__'
    iter_parse_trees__plain_Polish_notation_ = mkr4iter_parse_trees__plain_Polish_notation_(xnum_fanins5token_, data5token_=data5token_, key=key, Leaf=Leaf, Fork=Fork, Children=Children)
    return iter_parse_trees__plain_Polish_notation_(peekable_tokens, nonpeekable_ok=nonpeekable_ok)
def mkr4iter_parse_trees__plain_Polish_notation_(xnum_fanins5token_, /, *, data5token_=None, key=None, Leaf=None, Fork=None, Children=None):
    r'''
    :: xnum_fanins5token_ -> iter_parse_trees__plain_Polish_notation_
        # plain_Polish_notation vs reversed_Polish_notation
        # unable to iter_parse{reversed_Polish_notation} since cannot stop until end-of-stream or external data

    ######################
    #output:
    [iter_parse_trees__plain_Polish_notation_ :: PeekableIterator token -> Iter (Tree dat)]

    ######################
    #throw:
    ^Error__missing_child

    ######################
    #args:
    [xnum_fanins5token_ :: tkn -> xnum_fanins/int{>=-2}]
        xnum_fanins:
            -2 - external data
            -1 - value/leaf
            num_fanins/uint - op/fork

    ######################
    #kwds:
    [Children :: may ([Tree dat] -> Seq (Tree dat))]
        default:tuple
    [Fork :: may ((op/dat, children/[Tree dat]) -> Fork dat)]
        default:mk_Right
    [Leaf :: may (dat -> Leaf dat)]
        default:mk_Left
    [key :: may (token -> tkn)]
        default:echo
    [data5token_ :: may (tkn -> dat)]
        default:echo

    default:[Tree a =[def]= Either a (op/a, children/[Tree a])]
    <<==:
    data Tree a
        = Leaf a
        | Fork (a, Children (Tree a))
    data Children a ~= [a] # userdefined
    <<==:
    [Tree a b = Either a (b, [Tree a b])]



    '''#'''
    xnum_fanins5token_ = ifNone(xnum_fanins5token_, _x2y2True)
    data5token_ = ifNone(data5token_, echo)
    key = ifNone(key, echo)

    Leaf = ifNone(Leaf, mk_Left)
    Fork = ifNone(Fork, mk_Right)
    Children = ifNone(Children, tuple)
    _TokenII__with_LazyProperties = _mk_subclass4TokenII__with_LazyProperties_(key, xnum_fanins5token_, data5token_)

    def iter_parse_trees__plain_Polish_notation_(peekable_tokens, /, *, nonpeekable_ok=False):
        '[iter_parse_trees__plain_Polish_notation_ :: PeekableIterator token -> Iter (Tree dat)] #see:mkr4iter_parse_trees__plain_Polish_notation_.__doc__'
        it = echo_or_mk_PeekableIterator(peekable_tokens)
        if not (nonpeekable_ok or it is peekable_tokens):raise TypeError(type(peekable_tokens))
        777;del peekable_tokens
        it = _PeekableIterator__over_PeekableIterator(_TokenII__with_LazyProperties, it)

        while 1:
            tm = _main4read_tmay_tree(depth:=0, it)
            if not tm:
                break
            [tree] = tm
            yield tree
        return it.the_peekable_iterator

    def _main4read_tmay_tree(depth, it, /):
        'uint -> _PeekableIterator__over_PeekableIterator token -> tmay (Tree dat)'
        gi = _mk_gi4read_tmay_tree(depth, it)
        return flatten_recur(gi)

    def _mk_gi4read_tmay_tree(depth, it, /):
        'GI:uint -> _PeekableIterator__over_PeekableIterator token -> tmay (Tree dat)'
        if it.is_empty():
            return ()
        _wtkn = it.head
        _xnum_fanins = _wtkn.xnum_fanins
        check_type_is(int, _xnum_fanins)
        match _xnum_fanins:
            case -1:
                # value/leaf
                wtkn8leaf = _wtkn
                777;it.read1()
                777;del _wtkn, _xnum_fanins
                dat8leaf = wtkn8leaf.dat
                leaf = Leaf(dat8leaf)
                tree = leaf
            case num_fanins if num_fanins >= 0:
                # op/fork
                wtkn8op = _wtkn
                777;it.read1()
                777;del _wtkn, _xnum_fanins
                dat8op = wtkn8op.dat
                children = yield _mk_gi4read_children(depth, num_fanins, it)
                fork = Fork((dat8op, children))
                tree = fork
            case -2:
                # external data...
                return ()
            case bad_xnum_fanins:
                raise ValueError(bad_xnum_fanins)
        tree
        return (tree,)
    def _mk_gi4read_children(depth, num_fanins, it, /):
        'GI:uint -> _PeekableIterator__over_PeekableIterator token -> num_fanins -> Children (Tree dat)'
        depth += 1
        num_children = num_fanins
        check_int_ge(0, num_children)
        ls = []
        for _ in range(num_children):
            tm = yield _mk_gi4read_tmay_tree(depth, it)
            if not tm:
                raise Error__missing_child
            [tree] = tm
            ls.append(tree)
        ls
        return Children(ls)
    return iter_parse_trees__plain_Polish_notation_
#end-def mkr4iter_parse_trees__plain_Polish_notation_(xnum_fanins5token_, /, *, data5token_=None, key=None, Leaf=None, Fork=None, Children=None):




__all__
#[iter_parse_trees_,mkr4iter_parse_trees_] = lazy_import4funcs_('seed.recognize.tree.parse_tree', 'iter_parse_trees_,mkr4iter_parse_trees_', __name__)
#[iter_parse_trees__plain_Polish_notation_,mkr4iter_parse_trees__plain_Polish_notation_] = lazy_import4funcs_('seed.recognize.tree.parse_tree', 'iter_parse_trees__plain_Polish_notation_,mkr4iter_parse_trees__plain_Polish_notation_', __name__)
from seed.recognize.tree.parse_tree import iter_parse_trees_,mkr4iter_parse_trees_
from seed.recognize.tree.parse_tree import iter_parse_trees__plain_Polish_notation_,mkr4iter_parse_trees__plain_Polish_notation_
from seed.recognize.tree.parse_tree import BaseError__parse_tree, Error__missing_close_token, Error__mismatch_open_close_token, Error__missing_child
from seed.recognize.tree.parse_tree import *
