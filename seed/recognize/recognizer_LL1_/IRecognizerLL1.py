#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LL1_/IRecognizerLL1.py


seed.recognize.recognizer_LL1_.IRecognizerLL1
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LL1_.IRecognizerLL1 -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LL1_.IRecognizerLL1:__doc__ -ht


[[
TODO:
    ===
    ???TODO:++mk_eresult8null()@IRecognizerLL1
        允空式-空分支-结果

    ===
    DONE:++deep_verify(sf, addr_set4acc)@IRecognizerLL1

    ===
    DONE:++nonterminal_symbol@RecognizerLL1__ref8fwd_decl.__init__
        rule-lhs
            ref8fwd_decl
    ===
    ???DONE:++may_node_tag/may_nonterminal_symbol@rule-rhs-IRecognizerLL1.mk_gi8rgnr
        rule-rhs
            parallel
            serial
            alias
            xxx:tkey
            xxx:array
            xxx:constant_loader
        default-oresult:
            parallel - (NodeTag.NP, nonterminal_symbol, Cased branch_tag child_oresult)
                RecognizerLL1__parallel
            serial - (NodeTag.NS, nonterminal_symbol, tuple<child_oresult>)
                RecognizerLL1__serial
            alias - (NodeTag.NA, nonterminal_symbol, child_oresult)
                RecognizerLL1__alias__pick_one
                xxx:RecognizerLL1__alias__only_one
            tkey - (NodeTag.TK, terminal_symbol/tkey, oresult/tdat)
                RecognizerLL1__tkey
    ===
    DONE:++branch_tag@rule-rhs-RecognizerLL1__parallel.__init__#tag_rgnr_pairs
        rule-rhs-parallel

    ===
    DONE:++env/global_env@IRecognizerLL1.mk_gi8rgnr#used in RecognizerLL1__ref8fwd_decl.mk_gi8rgnr
        postprocess6ok
            env.symbol2may_postprocess6ok_ex
                {nonterminal_symbol:(may_postprocess6ok, {branch_tag, may_postprocess6ok})}
                -->:
                {symbol:(may_postprocess6ok, may {branch_tag, may_postprocess6ok})}

    ===
    DONE:++RecognizerLL1__alias__pick_one@IRecognizerLL1
        别名式-取一
        RecognizerLL1__alias__pick_one
        xxx:RecognizerLL1__alias__only_one

    ===
    DONE:++RecognizerLL1__array
        <<==:
        xxx:++RecognizerLL1__array__indefinite@IRecognizerLL1
            诡复式<非空式冃体式>
        xxx:++RecognizerLL1__array__definite@IRecognizerLL1
            bug:庸复式<任意式冃体式>
            庸复式<非空式冃体式|必空式冃体式>
    ===
]]


#]]]'''
__all__ = r'''
IRecognizerLL1
parse_via_rgnrLL1
    RecognizerLL1__constant_loader
    RecognizerLL1__tkey
    RecognizerLL1__array
    RecognizerLL1__ref8fwd_decl
        GlobalEnvironment4LL1
            Symbol4postprocess
        NodeTag
            RecognizerLL1__parallel
            RecognizerLL1__serial
            RecognizerLL1__alias__pick_one


















OtherError
    Error__property_existed
    Error__property_not_existed

LL1GrammarError
    LL1GrammarError__conflict_FIRST_x_NON_FOLLOW__siblings
    LL1GrammarError__conflict_FIRST__branches
    LL1GrammarError__conflict_FIRST__siblings
    LL1GrammarError__multi_nullable_branches
    LL1GrammarError__array__more_than_one_nullable_but_not_always_null_item
    LL1GrammarError__conflict_FIRST_x_NON_FOLLOW__definite_array
    LL1GrammarError__array__indefinite_nullable

NodeTag

Symbol4postprocess
GlobalEnvironment4LL1


IRecognizerLL1
    IRecognizerLL1__init_properties
        RecognizerLL1__ref8fwd_decl

    IRecognizerLL1__always_dead
    IRecognizerLL1__always_null
        RecognizerLL1__constant_loader

    IRecognizerLL1__tkey_query_set
        RecognizerLL1__tkey

    IRecognizerLL1__serial_framework
        _RecognizerLL1__serial

    IRecognizerLL1__serial__init
        RecognizerLL1__serial

    IRecognizerLL1__wrapper
        RecognizerLL1__alias__pick_one

    RecognizerLL1__array
    RecognizerLL1__parallel

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...


from seed.types.Symbol import public_symbol5cls
from seed.iters.duplicate_elements import iter_duplicate_representative_elements
from seed.iters.count_ import count_
from seed.tiny_.oo8inf import oo

from seed.tiny_.funcs import echo, unbox, fst, snd
from seed.tiny_.dict__add_fmap_filter import fmap4dict_value
from seed.tiny_.dict_op__add import set_add
from seed.tiny_.containers import null_frozenset, null_iter, mk_frozenset, mk_tuple
from seed.types.IToken import IToken
from seed.types.IToken import IPositionInfo4Gap
from seed.types.Either import Cased, Either
from seed.types.Either import mk_Left, mk_Right

from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_uint_lt
from seed.tiny_.check import check_may_, check_callable, check_pair, check_smay_pseudo_qual_name







from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper

from enum import Enum
from collections import defaultdict


___end_mark_of_excluded_global_names__0___ = ...












class OtherError(Exception):pass
class Error__property_existed(OtherError):pass
class Error__property_not_existed(OtherError):pass



class LL1GrammarError(Exception):pass
class LL1GrammarError__conflict_FIRST_x_NON_FOLLOW__siblings(LL1GrammarError):pass
class LL1GrammarError__conflict_FIRST__branches(LL1GrammarError):pass
class LL1GrammarError__conflict_FIRST__siblings(LL1GrammarError):pass
class LL1GrammarError__multi_nullable_branches(LL1GrammarError):pass

class LL1GrammarError__array__more_than_one_nullable_but_not_always_null_item(LL1GrammarError):pass
class LL1GrammarError__conflict_FIRST_x_NON_FOLLOW__definite_array(LL1GrammarError):pass
class LL1GrammarError__array__indefinite_nullable(LL1GrammarError):pass



class NodeTag(Enum):
    TK = 0 #terminal_symbol/tkey
    NA = 1 #nonterminal_symbol.alias
    NS = 2 #nonterminal_symbol.serial
    NP = 3 #nonterminal_symbol.parallel
    #repetition/array: inner_expr not nonterminal_symbol
    #tag/constant_loader: immediate operand : not symbol
assert len(NodeTag) == 4, sorted(NodeTag)




@public_symbol5cls
class Symbol4postprocess:
    'key to (symbol2may_postprocess6ok_ex :: {symbol:(may_postprocess6ok, may {branch_tag, may_postprocess6ok})})'
    pass



if 0:
  class GlobalEnvironment4LL1:
    'global_env'
    def __init__(sf, symbol2may_postprocess6ok_ex, /):
        sf[Symbol4postprocess] = symbol2may_postprocess6ok_ex
    def __getitem__(sf, k, /):
        return vars(sf)[k]
    def __setitem__(sf, k, v, /):
        vars(sf)[k] = k
GlobalEnvironment4LL1 = dict#Mapping
    #[global_env :: {Symbol:obj}]

class IRecognizerLL1(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def always_dead(sf, /):
        '-> bool #[min_oolen == +oo]'
    @property
    @abstractmethod
    def always_null(sf, /):
        '-> bool #[max_oolen == 0]'
    @property
    @abstractmethod
    def nullable(sf, /):
        '-> bool #[min_oolen == 0]'
    @property
    @abstractmethod
    def FIRST(sf, /):
        '-> head_first_terminal_symbol_set/{terminal_symbol}'
    @property
    @abstractmethod
    def NON_FOLLOW(sf, /):
        '-> tail_nonfollowed_terminal_symbol_set/tail_lookahead_terminal_symbol_set/{terminal_symbol}'

    @abstractmethod
    def mk_gi8rgnr(sf, global_env, /, *args):
        '-> gi8rgnr/IGeneratorIterator/GI<[yield peek1_vs_read1/bool --> may token][yield rgnr_ex/(child_rgnr/IRecognizerLL1|child_rgnr_with_args/(child_rgnr,*args)/tuple) --> oresult][return eresult/(Either errmsg oresult)]>'

    @abstractmethod
    def iter_direct_children(sf, /):
        '-> Iter IRecognizerLL1'

    def shallow_verify(sf, /):
        '-> None|^Exception'
        always_dead = sf.always_dead
        always_null = sf.always_null
        nullable = sf.nullable
        FIRST = sf.FIRST
        NON_FOLLOW = sf.NON_FOLLOW
        check_type_is(bool, always_dead)
        check_type_is(bool, always_null)
        check_type_is(bool, nullable)
        check_type_is(frozenset, FIRST)
        check_type_is(frozenset, NON_FOLLOW)
        #####
        assert not (always_dead and always_null)

        #####
        assert not (always_dead and nullable)

        #####
        assert not always_null or nullable

        #####
        assert not (always_null and FIRST)
        assert not (always_dead and FIRST)
        assert FIRST or always_null or always_dead

        #####
        assert not (always_null and NON_FOLLOW)
        assert not (always_dead and NON_FOLLOW)
        #bug:assert NON_FOLLOW or always_null or always_dead
            #还有大量:非空内敛式

        #####
        assert not nullable or (FIRST <= NON_FOLLOW)
        return
    def deep_verify(sf, /):
        '-> None|^Exception'
        addr_set = set()
        ls = []
        def put(rgnr, /):
            if set_add(addr_set, id(rgnr)):
                ls.append(rgnr)
        put(sf)
        while ls:
            rgnr = ls.pop()
            rgnr.shallow_verify()
            for _ in map(put, rgnr.iter_direct_children()):pass
#end-class IRecognizerLL1(ABC):

def parse_via_rgnrLL1(global_env, prev_tgend_or_token, tokens, rgnrLL1, /, *args):
    'global_env/GlobalEnvironment4LL1 -> (IPositionInfo4Gap|IToken) -> Iter IToken -> IRecognizerLL1 -> (*args{IRecognizerLL1.mk_gi8rgnr}) -> (eresult, eof, tgend6halt_or_token, iter_tokens)/(Either errmsg oresult, bool, (IPositionInfo4Gap|IToken), Iter IToken)'
    def _0init():
        if isinstance(IToken, prev_tgend_or_token):
            head_token = prev_tgend_or_token
            #prev_tgend = head_token.token_begin_position_info
            emm = head_token
            prev_tgend = head_token.token_end_position_info
                #asif-_0feed()
        else:
            prev_tgend = prev_tgend_or_token
            emm = ...
        return (emm, prev_tgend)
    del prev_tgend_or_token
    (emm, prev_tgend) = _0init()

    check_type_le(IPositionInfo4Gap, prev_tgend)
    check_type_le(IRecognizerLL1, rgnrLL1)
    tokens = iter_tokens = iter(tokens)

    #nonlocal:
    emm
    prev_tgend
    args
    lnkls = ()
    gi = ...
    i4send = ...
    eresult = ...

    def _put():
        '(rgnrLL1, args) -> ...'
        nonlocal lnkls, gi, rgnrLL1, args, i4send
        gi = rgnrLL1.mk_gi8rgnr(global_env, *args)
        lnkls = (lnkls, gi)
        777;    rgnrLL1 = args = ...
        i4send = None
        return _send
    def _pop():
        'eresult -> ...'
        nonlocal eresult, gi, lnkls
        assert gi is lnkls[-1]
        lnkls, _ = lnkls
        777;    gi = ...
        if eresult.is_left:
            return None
        if not lnkls:
            return None
        gi = lnkls[-1]
        i4send = oresult = eresult.right
        777;    eresult = ...
        return _send
    def _send():
        '(gi,i4send) -> ...'
        nonlocal eresult, i4send, rgnrLL1, args
        try:
            r = gi.send(i4send)
        except StopIteration as e:
            eresult = e.value
            check_type_is(Either, eresult)
            eresult
            return _pop
        finally:
            777;    i4send = ...

        T = type(r)
        if T is bool:
            #peek1_vs_read1
            return _0feed(r)
        if T is tuple:
            (rgnrLL1, *args) = r
        else:
            (rgnrLL1, *args) = [r]
        check_type_le(IRecognizerLL1, rgnrLL1)
        (rgnrLL1, args)
        return _put
    def _0feed(r, /):
        #peek1_vs_read1
        nonlocal i4send, emm, prev_tgend
        if emm is ...:
            emm = next(tokens, None)
            emm # is may_token
            if not emm is None:
                token = emm
                check_type_le(IToken, token)
                prev_tgend = token.token_end_position_info
            else:
                prev_tgend # @eof
            emm # is may_token
        else:
            emm # is may_token
        #
        may_token = emm
        if r:
            #read1
            emm = ... #consume
        else:
            #peek1
            pass
        i4send = may_token
        return _send

    (rgnrLL1, args)
    def _0mainloop():
        (rgnrLL1, args)
        f = _put
        while f:
            f = f()
    _0mainloop()
    assert not eresult is ...
    assert not lnkls or eresult.is_left
    eresult
    def _0mk_result():
        eresult
        emay_may_token = emm
        (eresult, emay_may_token, prev_tgend, iter_tokens)

        if emay_may_token is ...:
            x = tgend6halt = prev_tgend
            eof = False #unknown yet
        elif emay_may_token is None:
            # eof
            x = tgend6halt = prev_tgend
            eof = True #known eof
        else:
            x = token = emay_may_token
            tgend6halt = token.token_begin_position_info
            eof = False #known not eof
        tgend6halt
        tgend6halt_or_token = x
        eof

        (eresult, tgend6halt, emay_may_token, prev_tgend, iter_tokens)
            #order
        (eresult, eof, tgend6halt_or_token, iter_tokens)
        return (eresult, eof, tgend6halt_or_token, iter_tokens)
    return _0mk_result()
#end-def parse_via_rgnrLL1(prev_tgend_or_token, tokens, rgnrLL1, /, *args):

class IRecognizerLL1__wrapper(IRecognizerLL1):
    __slots__ = ()
    @property
    @override
    def _the_wrapped_rgnr_(sf, /):
        '-> IRecognizerLL1'
    @override
    def mk_gi8rgnr(sf, global_env, /, *args):
        '-> gi8rgnr/IGeneratorIterator'
        return sf._the_wrapped_rgnr_.mk_gi8rgnr(global_env, *args)


    @property
    @override
    def always_dead(sf, /):
        '-> bool #[min_oolen == +oo]'
        return sf._the_wrapped_rgnr_.always_dead
    @property
    @override
    def always_null(sf, /):
        '-> bool #[max_oolen == 0]'
        return sf._the_wrapped_rgnr_.always_null
    @property
    @override
    def nullable(sf, /):
        '-> bool #[min_oolen == 0]'
        return sf._the_wrapped_rgnr_.nullable
    @property
    @override
    def FIRST(sf, /):
        '-> head_first_terminal_symbol_set/{terminal_symbol}'
        return sf._the_wrapped_rgnr_.FIRST
    @property
    @override
    def NON_FOLLOW(sf, /):
        '-> tail_nonfollowed_terminal_symbol_set/tail_lookahead_terminal_symbol_set/{terminal_symbol}'
        return sf._the_wrapped_rgnr_.NON_FOLLOW

#end-class IRecognizerLL1__wrapper(IRecognizerLL1):



class IRecognizerLL1__init_properties(IRecognizerLL1):
    ___no_slots_ok___ = True
    def __init__(sf, always_dead, always_null, nullable, FIRST, NON_FOLLOW, /):
        check_type_is(bool, always_dead)
        check_type_is(bool, always_null)
        check_type_is(bool, nullable)
        check_type_is(frozenset, FIRST)
        check_type_is(frozenset, NON_FOLLOW)
        sf._dd = always_dead
        sf._nn = always_null
        sf._nb = nullable
        sf._hf = FIRST
        sf._tl = NON_FOLLOW
    @property
    @override
    def always_dead(sf, /):
        '-> bool #[min_oolen == +oo]'
        return sf._dd
    @property
    @override
    def always_null(sf, /):
        '-> bool #[max_oolen == 0]'
        return sf._nn
    @property
    @override
    def nullable(sf, /):
        '-> bool #[min_oolen == 0]'
        return sf._nb
    @property
    @override
    def FIRST(sf, /):
        '-> head_first_terminal_symbol_set/{terminal_symbol}'
        return sf._hf
    @property
    @override
    def NON_FOLLOW(sf, /):
        '-> tail_nonfollowed_terminal_symbol_set/tail_lookahead_terminal_symbol_set/{terminal_symbol}'
        return sf._tl
class RecognizerLL1__ref8fwd_decl(IRecognizerLL1__init_properties):
    'ref<nonterminal_symbol>++fwd_decl<nonterminal_symbol>'
    ___no_slots_ok___ = True
    @override
    def iter_direct_children(sf, /):
        '-> Iter IRecognizerLL1'
        if not None is sf.may_rgnr:
            yield sf.may_rgnr

    def __init__(sf, smay_qname4repr, nonterminal_symbol, always_dead, always_null, nullable, FIRST, NON_FOLLOW, may_rgnr, /):
        check_smay_pseudo_qual_name(smay_qname4repr)
        if not may_rgnr is None:
            rgnr = may_rgnr
            check_type_le(IRecognizerLL1, rgnr)
            if not type(rgnr) in _TYPES4ref:raise TypeError(type(rgnr))

        FIRST = mk_frozenset(FIRST)
        NON_FOLLOW = mk_frozenset(NON_FOLLOW)

        sf._sqnm = smay_qname4repr
        sf._nt = nonterminal_symbol
        sf._mr = may_rgnr
        sf._args4repr = (smay_qname4repr, nonterminal_symbol, always_dead, always_null, nullable, FIRST, NON_FOLLOW, may_rgnr)
        super().__init__(always_dead, always_null, nullable, FIRST, NON_FOLLOW)
        sf.shallow_verify()

    def __repr__(sf, /):
        if (qnm := sf._sqnm):
            return qnm
        return str(sf)
    def __str__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def smay_qname(sf, /):
        '-> str'
        return sf._sqnm
    @property
    def nonterminal_symbol(sf, /):
        '-> nonterminal_symbol'
        return sf._nt
    @property
    def may_rgnr(sf, /):
        '-> may IRecognizerLL1'
        return sf._mr
    @may_rgnr.setter
    def may_rgnr(sf, rgnr, /):
        'IRecognizerLL1 -> None'
        if not sf._mr is None:
            raise Error__property_existed('RecognizerLL1__ref8fwd_decl.may_rgnr')
        check_type_le(IRecognizerLL1, rgnr)
        if not type(rgnr) in _TYPES4ref:raise TypeError(type(rgnr))
        if rgnr is sf:raise TypeError
        if isinstance(rgnr, __class__):raise TypeError

        sf._mr = rgnr
        try:
            sf.shallow_verify()
        except:
            sf._mr = None
            raise
        sf._args4repr = (*sf._args4repr[:-1], rgnr)
        return


    @override
    def mk_gi8rgnr(sf, global_env, /, *args):
        '-> gi8rgnr/IGeneratorIterator'
        if None is (rgnr := sf._mr):
            raise Error__property_not_existed('RecognizerLL1__ref8fwd_decl.may_rgnr')
        rgnr
        #return rgnr.mk_gi8rgnr(global_env, sf._nt, *args)
        oresult = yield (rgnr, sf.nonterminal_symbol, *args)
        oresult = _apply_postprocess6ok(global_env, sf.nonterminal_symbol, oresult)
        return mk_Right(oresult)

    @override
    def shallow_verify(sf, /):
        '-> None|^Exception'
        super().shallow_verify()
        check_smay_pseudo_qual_name(sf.smay_qname)

        may_rgnr = sf.may_rgnr
        if may_rgnr is None:
            return
        rgnr = may_rgnr

        check_type_le(IRecognizerLL1, rgnr)
        if not type(rgnr) in _TYPES4ref:raise TypeError(type(rgnr))
        if rgnr is sf:raise TypeError
        if isinstance(rgnr, __class__):raise TypeError
        assert sf.always_dead == rgnr.always_dead
        assert sf.always_null == rgnr.always_null
        assert sf.nullable == rgnr.nullable
        assert sf.FIRST == rgnr.FIRST
        assert sf.NON_FOLLOW == rgnr.NON_FOLLOW
        return

def _apply_postprocess6ok(global_env, nonterminal_symbol, oresult, /):
    '[used in RecognizerLL1__ref8fwd_decl][assume oresult come from:RecognizerLL1__parallel,RecognizerLL1__serial,RecognizerLL1__alias__pick_one]'
    if not None is (pair := global_env[Symbol4postprocess].get(nonterminal_symbol)):
        (may_postprocess6ok, may__branch_tag2postprocess6ok) = pair
        (node_tag, _symbol, payload) = oresult
        assert _symbol is nonterminal_symbol
        if not may__branch_tag2postprocess6ok is None:
            branch_tag2postprocess6ok = may__branch_tag2postprocess6ok
            assert node_tag is NodeTag.NP
            check_type_is(Cased, payload)
            cased = payload
            branch_tag = cased.case
            f = branch_tag2postprocess6ok.get(branch_tag, echo)
            oresult = f(oresult)
        oresult #updated
        if not may_postprocess6ok is None:
            postprocess6ok = may_postprocess6ok
            oresult = postprocess6ok(oresult)
        oresult #updated
    oresult #updated
    return oresult
#end-class RecognizerLL1__ref8fwd_decl(IRecognizerLL1):


class IRecognizerLL1__always_dead(IRecognizerLL1):
    __slots__ = ()
    #@override
    always_dead = True
    #@override
    always_null = False
    #@override
    nullable = False
    #@override
    FIRST = null_frozenset
    #@override
    NON_FOLLOW = null_frozenset

class IRecognizerLL1__always_null(IRecognizerLL1):
    __slots__ = ()
    #@override
    always_dead = False
    #@override
    always_null = True
    #@override
    nullable = True
    #@override
    FIRST = null_frozenset
    #@override
    NON_FOLLOW = null_frozenset

class RecognizerLL1__constant_loader(IRecognizerLL1__always_null):
    'oresult/tag/constant_loader: immediate operand : not symbol'
    ___no_slots_ok___ = True
    @override
    def iter_direct_children(sf, /):
        '-> Iter IRecognizerLL1'
        return null_iter
    def __init__(sf, oresult, /):
        sf._or = oresult
        sf._er = eresult = mk_Right(oresult)
    def __repr__(sf, /):
        return repr_helper(sf, sf._or)
    @property
    def oresult(sf, /):
        '-> oresult'
        return sf._or

    @override
    def mk_gi8rgnr(sf, global_env, /):
        '-> gi8rgnr/IGeneratorIterator'
        return sf._er
        777;    yield
class IRecognizerLL1__tkey_query_set(IRecognizerLL1):
    __slots__ = ()
    #@override
    always_dead = False
    #@override
    always_null = False
    #@override
    nullable = False
    #@override
    NON_FOLLOW = null_frozenset
class RecognizerLL1__tkey(IRecognizerLL1__tkey_query_set):
    ___no_slots_ok___ = True
    @override
    def iter_direct_children(sf, /):
        '-> Iter IRecognizerLL1'
        return null_iter
    def __init__(sf, tkey, /):
        sf._x = tkey
        sf._xs = mk_frozenset([tkey])
    def __repr__(sf, /):
        return repr_helper(sf, sf._x)
    @property
    def tkey(sf, /):
        '-> tkey/terminal_symbol'
        return sf._x
    @property
    @override
    def FIRST(sf, /):
        '-> head_first_terminal_symbol_set/{terminal_symbol}'
        return sf._xs
    @override
    def mk_gi8rgnr(sf, global_env, /):
        '-> gi8rgnr/IGeneratorIterator'
        may_token = yield False # peek1
        if may_token is None:
            return mk_Left(errmsg:=('eof', sf.tkey))
        token = may_token
        if not token.token_key == sf.tkey:
            return mk_Left(errmsg:=('neq', sf.tkey, token.token_key))
        yield True # read1
        tkey = sf.tkey
        tdat = token.token_data
        oresult = (NodeTag.TK, tkey, tdat)
        return mk_Right(oresult)

class IRecognizerLL1__serial_framework(IRecognizerLL1):
    __slots__ = ()
    @abstractmethod
    def mk_gi4child_ex(sf, nonterminal_symbol, /, *args):
        '-> gi4child_ex/IGeneratorIterator/GI<[yield (case4unpack/(0|1|2),rgnr_ex/(rgnr|(rgnr,*args))) --> oresult][return may_postprocess6ok/(may (oresult->oresult))]>'
    @override
    def mk_gi8rgnr(sf, global_env, nonterminal_symbol, /, *args):
        '-> gi8rgnr/IGeneratorIterator'
        gi = sf.mk_gi4child_ex(nonterminal_symbol, *args)
        ls = []
        i4send = None
        while 1:
            try:
                x = gi.send(i4send)
                777;    i4send = ...
            except StopIteration as e:
                may_postprocess6ok = e.value
                break
            (case4unpack, rgnr_ex) = x
            check_uint_lt(3, case4unpack)
            oresult = yield rgnr_ex
            if case4unpack == 1:
                ls.append(oresult)
            elif case4unpack == 0:
                pass
            elif case4unpack == 2:
                ls.extend(oresult)
            else:
                raise 000
            i4send = oresult
        #end-while
        ls, may_postprocess6ok
        check_may_(check_callable, may_postprocess6ok)

        #xxx:oresult = (NodeTag.NS, nonterminal_symbol, mk_tuple(ls))
        oresult = child_oresults = mk_tuple(ls)

        if not may_postprocess6ok is None:
            postprocess6ok = may_postprocess6ok
            oresult = postprocess6ok(oresult)
        oresult
        return mk_Right(oresult)

class IRecognizerLL1__serial__init(IRecognizerLL1__init_properties):
    '[cased_rgnrs :: [Cased case4unpack/(0|1|2) IRecognizerLL1]]'
    ___no_slots_ok___ = True
    @override
    def iter_direct_children(sf, /):
        '-> Iter IRecognizerLL1'
        return map(snd, sf.cased_rgnrs)
    ##def __init__(sf, cased_rgnrs, may_postprocess6ok=None, /):
    ##    check_may_(check_callable, may_postprocess6ok)
    def __init__(sf, cased_rgnrs, /):

        cs = cased_rgnrs = mk_tuple(cased_rgnrs)
        for c in cs:
            check_type_is(Cased, c)
            check_uint_lt(3, c.case)
            check_type_le(IRecognizerLL1, c.payload)
        rs = [c.payload for c in cs]


        always_dead = any(r.always_dead for r in rs)
        always_null = not always_dead and all(r.always_null for r in rs)
        nullable = always_null or (not always_dead and all(r.nullable for r in rs))

        FIRST = set()
        NON_FOLLOW = set()
        if not (always_null or always_dead):
            for r in rs:
                FIRST |= r.FIRST
                if not r.nullable:break

            for r in reversed(rs):
                NON_FOLLOW |= r.NON_FOLLOW
                if not r.nullable:break
        FIRST = mk_frozenset(FIRST)
        NON_FOLLOW = mk_frozenset(NON_FOLLOW)

        ######################
        ######################
        #DONE:允空区间
        ######################
        ######################
        if not always_dead:
            # [g means j4gap not j4rgnr]
            prev = null_frozenset
            g2NON_FOLLOW = [prev]
            for r in rs:
                s = r.NON_FOLLOW
                prev = (prev | s) if r.nullable else s
                g2NON_FOLLOW.append(prev)
            g2NON_FOLLOW

            prev = null_frozenset
            rev__g2FIRST = [prev]
            #for r in reversed(rs):
            for j in reversed(range(len(rs))):
                r = rs[j]
                s = r.FIRST
                if r.nullable and (common := prev & s):raise LL1GrammarError__conflict_FIRST__siblings(common, rs[j:], cased_rgnrs)
                prev = (prev | s) if r.nullable else s
                rev__g2FIRST.append(prev)
            rev__g2FIRST
            if 1:
                rev__g2FIRST.reverse()
                g2FIRST = rev__g2FIRST
                del rev__g2FIRST

            g2FIRST
            g2NON_FOLLOW

            assert len(g2FIRST) == len(g2NON_FOLLOW) == 1+len(rs)
            assert g2FIRST[-1] == null_frozenset
            assert g2NON_FOLLOW[0] == null_frozenset

            for g, (FIRST4g, NON_FOLLOW4g) in enumerate(zip(g2FIRST, g2NON_FOLLOW)):
                if (common := FIRST4g & NON_FOLLOW4g):raise LL1GrammarError__conflict_FIRST_x_NON_FOLLOW__siblings(common, rs[:g], rs[g:], cased_rgnrs)

            #####
            may__g2FIRST = mk_tuple(g2FIRST)
            may__g2NON_FOLLOW = mk_tuple(g2NON_FOLLOW)
        else:
            may__g2FIRST = None
            may__g2NON_FOLLOW = None
        may__g2FIRST
        may__g2NON_FOLLOW
        ######################
        ######################



        ##if not always_dead:
        ##    # [g means group not j4gap not j4rgnr]
        ##    j2n = [r.nullable for r in rs]
        ##    j2g = []
        ##    g2js = []
        ##    prev = ...
        ##    for j, n4j in enumerate(j2n):
        ##        if n4j is not prev:
        ##            g = len(g2js)
        ##            g2js.append([])
        ##            prev = n4j
        ##        j2g.append(g)
        ##        g2js[-1].append(j)

        sf._cs = cs
        ##sf._mf = may_postprocess6ok
        sf._mHs = may__g2FIRST
        sf._mTs = may__g2NON_FOLLOW


        super().__init__(always_dead, always_null, nullable, FIRST, NON_FOLLOW)
        sf.shallow_verify()


    def __repr__(sf, /):
        return repr_helper(sf, sf._cs)
        ##if sf._mf is None:
        ##    return repr_helper(sf, sf._cs)
        ##return repr_helper(sf, sf._cs, sf._mf)
    @property
    def cased_rgnrs(sf, /):
        '-> [Cased case4unpack/(0|1|2) IRecognizerLL1]'
        return sf._cs
    ##@property
    ##def may_postprocess6ok(sf, /):
    ##    '-> may (oresult->oresult)'
    ##    return sf._mf



    @override
    def shallow_verify(sf, /):
        '-> None|^Exception'
        super().shallow_verify()
        ##check_may_(check_callable, sf.may_postprocess6ok)

        #####
        cs = sf.cased_rgnrs
        check_type_is(tuple, cs)
        for c in cs:
            check_type_is(Cased, c)
            check_uint_lt(3, c.case)
            check_type_le(IRecognizerLL1, c.payload)

        #####
        rs = [c.payload for c in cs]
        always_dead = sf.always_dead
        always_null = sf.always_null
        nullable = sf.nullable
        FIRST = sf.FIRST
        NON_FOLLOW = sf.NON_FOLLOW

        may__g2FIRST = sf._mHs
        may__g2NON_FOLLOW = sf._mTs

        #####
        assert always_dead is any(r.always_dead for r in rs)
        assert always_null is all(r.always_null for r in rs)
        assert nullable is all(r.nullable for r in rs)


        #####
        assert (FIRST == null_frozenset) is (always_null or always_dead)
        if (always_null or always_dead):
            assert FIRST == null_frozenset
            assert NON_FOLLOW == null_frozenset
        else:
            assert FIRST
            for r in rs:
                assert FIRST >= r.FIRST
                if not r.nullable:break

            for r in reversed(rs):
                assert NON_FOLLOW >= r.NON_FOLLOW
                if not r.nullable:break
        #####
        if always_dead:
            assert may__g2FIRST is None
            assert may__g2NON_FOLLOW is None
        else:
            g2FIRST = may__g2FIRST
            g2NON_FOLLOW = may__g2NON_FOLLOW
            assert not g2FIRST is None
            assert not g2NON_FOLLOW is None
            assert len(g2FIRST) == len(g2NON_FOLLOW) == 1+len(rs)
            assert g2FIRST[-1] == null_frozenset
            assert g2NON_FOLLOW[0] == null_frozenset
            for j, r in enumerate(rs):
                H4j = g2FIRST[j]
                T4j = g2NON_FOLLOW[j]
                H4j1 = g2FIRST[j+1]
                T4j1 = g2NON_FOLLOW[j+1]
                if r.nullable:
                    assert H4j == (r.FIRST | H4j1)
                    assert len(H4j) == len(r.FIRST) + len(H4j1)
                    assert (T4j | r.NON_FOLLOW) == T4j1
                else:
                    assert H4j == r.FIRST
                    assert r.NON_FOLLOW == T4j1

            for g, (FIRST4g, NON_FOLLOW4g) in enumerate(zip(g2FIRST, g2NON_FOLLOW)):
                assert not (common := FIRST4g & NON_FOLLOW4g), common

#end-class IRecognizerLL1__serial__init(IRecognizerLL1__init_properties):

class _RecognizerLL1__serial(IRecognizerLL1__serial__init, IRecognizerLL1__serial_framework):
    '[cased_rgnrs :: [Cased case4unpack/(0|1|2) IRecognizerLL1]]'
    ___no_slots_ok___ = True
    @override
    def mk_gi4child_ex(sf, nonterminal_symbol, /):
        '-> gi4child_ex/IGeneratorIterator/GI<[yield (case4unpack/(0|1|2),rgnr_ex/(rgnr|(rgnr,*args))) --> oresult][return may_postprocess6ok/(may (oresult->oresult))]>'
        yield from sf.cased_rgnrs
        ##return sf._mf
        return None
#end-class _RecognizerLL1__serial(IRecognizerLL1__serial__init, IRecognizerLL1__serial_framework):
_RecognizerLL1__serial([])

class RecognizerLL1__serial(IRecognizerLL1__serial__init):
    '[cased_rgnrs :: [Cased case4unpack/(0|1|2) IRecognizerLL1]]'
    ___no_slots_ok___ = True
    @override
    def mk_gi8rgnr(sf, global_env, nonterminal_symbol, /):
        '-> gi8rgnr/IGeneratorIterator'
        ls = []
        for (case4unpack, rgnr_ex) in sf.cased_rgnrs:
            child_oresult = yield rgnr_ex
            if case4unpack == 1:
                ls.append(child_oresult)
            elif case4unpack == 0:
                pass
            elif case4unpack == 2:
                ls.extend(child_oresult)
            else:
                raise 000
        #end-for
        ls
        child_oresults = mk_tuple(ls)

        oresult = (NodeTag.NS, nonterminal_symbol, child_oresults)

        return mk_Right(oresult)
#end-class RecognizerLL1__serial(IRecognizerLL1__serial__init):
RecognizerLL1__serial([])


class RecognizerLL1__alias__pick_one(IRecognizerLL1__wrapper):
    ___no_slots_ok___ = True
    @override
    def iter_direct_children(sf, /):
        '-> Iter IRecognizerLL1'
        yield sf._the_wrapped_rgnr_
    def __init__(sf, head_rgnrs, main_rgnr, tail_rgnrs, /):
        head_rgnrs = mk_tuple(head_rgnrs)
        tail_rgnrs = mk_tuple(tail_rgnrs)
        rgnrs = (*head_rgnrs, main_rgnr, *tail_rgnrs)

        j = len(head_rgnrs)
        assert rgnrs[j] is main_rgnr

        cased_rgnrs = (Cased(int(i==j), r) for i, r in enumerate(rgnrs))
        _the_wrapped_rgnr_ = RecognizerLL1__serial(cased_rgnrs)

        sf._args4repr = (head_rgnrs, main_rgnr, tail_rgnrs)
        sf._j = j
        sf._w = _the_wrapped_rgnr_

    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)

    @property
    @override
    def _the_wrapped_rgnr_(sf, /):
        '-> IRecognizerLL1'
        return sf._w
    @override
    def mk_gi8rgnr(sf, global_env, nonterminal_symbol, /, *args):
        '-> gi8rgnr/IGeneratorIterator'
        (_node_tag, _None, child_oresults) = _oresult = yield (sf._the_wrapped_rgnr_, None, *args)
        assert _node_tag is NodeTag.NS
        assert _None is None # [nonterminal_symbol:=None]
        main_child_oresult = child_oresults[sf._j]
        oresult = (NodeTag.NA, nonterminal_symbol, main_child_oresult)
        return mk_Right(oresult)

#end-class RecognizerLL1__alias__pick_one(IRecognizerLL1__wrapper):
RecognizerLL1__alias__pick_one([], RecognizerLL1__serial([]), [])


class RecognizerLL1__array(IRecognizerLL1__init_properties):
    ___no_slots_ok___ = True
    @override
    def iter_direct_children(sf, /):
        '-> Iter IRecognizerLL1'
        yield sf.rgnr
    def __init__(sf, min_len, may_max_len, rgnr, args4rgnr, /):
        args4rgnr = mk_tuple(args4rgnr)

        check_int_ge(0, min_len)
        check_may_([check_int_ge, min_len], may_max_len)
        check_type_le(IRecognizerLL1, rgnr)

        max_oolen = +oo if may_max_len is None else may_max_len
        assert max_oolen >= min_len

        relaxation = max_oolen -min_len
        definite = not relaxation
        indefinite = not definite




        if (indefinite and rgnr.nullable):raise LL1GrammarError__array__indefinite_nullable(rgnr)
        # [indefinite -> [not rgnr.nullable]]
        if (max_oolen>=2 and rgnr.nullable and not rgnr.always_null):raise LL1GrammarError__array__more_than_one_nullable_but_not_always_null_item(rgnr)
        # [indefinite -> [not rgnr.nullable]]
        # [[max_oolen>=2] -> [not rgnr.always_null] -> [not rgnr.nullable]]
        #
        if max_oolen >= 2 and not rgnr.always_dead and (common:=rgnr.NON_FOLLOW & rgnr.FIRST):raise LL1GrammarError__conflict_FIRST_x_NON_FOLLOW__definite_array(common, rgnr)
        # [[max_oolen >= 2] -> [not rgnr.always_dead] -> [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]]



        # [indefinite -> [not rgnr.nullable]]
        # [[max_oolen>=2] -> [not rgnr.always_null] -> [not rgnr.nullable]]
        # [[max_oolen >= 2] -> [not rgnr.always_dead] -> [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]]
        #
        if max_oolen == 0 or (rgnr.always_dead and min_len == 0) or rgnr.always_null:
            #always_null: x[0] or always_null[min_len]
            #IRecognizerLL1__always_null
            if rgnr.always_null:
                assert not indefinite
            if indefinite:
                assert rgnr.always_dead
            always_dead = False
            always_null = True
            nullable = True
            FIRST = null_frozenset
            NON_FOLLOW = null_frozenset
        # [not rgnr.always_null]
        # !! [[max_oolen>=2] -> [not rgnr.always_null] -> [not rgnr.nullable]]
        #  [[max_oolen>=2] -> [not rgnr.nullable]]
        # !! [indefinite -> [not rgnr.nullable]]
        # [[[max_oolen>min_len]or[max_oolen>1]] -> [not rgnr.nullable]]
        # [[not [min_len==max_oolen<=1]] -> [not rgnr.nullable]]
        # [[not [(min_len,max_oolen) <- {(0,0),(1,1)}]] -> [not rgnr.nullable]]

        elif rgnr.always_dead:
            assert min_len > 0
            #always_dead
            #IRecognizerLL1__always_dead
            always_dead = True
            always_null = False
            nullable = False
            FIRST = null_frozenset
            NON_FOLLOW = null_frozenset
        #
        # [[not [(min_len,max_oolen) <- {(0,0),(1,1)}]] -> [not rgnr.nullable]]
        # [max_oolen >= 1][not rgnr.always_dead][not rgnr.always_null]
        elif max_oolen == 1:
            # [max_oolen == 1][not rgnr.always_dead][not rgnr.always_null]
            if definite:
                #x[1]
                # [min_len == 1][max_oolen == 1][not rgnr.always_dead][not rgnr.always_null]
                always_dead = rgnr.always_dead
                always_null = rgnr.always_null
                nullable = rgnr.nullable
                FIRST = rgnr.FIRST
                NON_FOLLOW = rgnr.NON_FOLLOW
            else:
                #optional: x?
                # [not rgnr.nullable]
                # [min_len == 0][max_oolen == 1][not rgnr.always_dead][not rgnr.always_null]
                #
                # =>[not sf.always_null]
                always_dead = False
                always_null = False
                nullable = True
                FIRST = rgnr.FIRST
                NON_FOLLOW = rgnr.NON_FOLLOW | rgnr.FIRST
        # [max_oolen >= 2][not rgnr.always_dead][not rgnr.always_null]
        # !! [[not [(min_len,max_oolen) <- {(0,0),(1,1)}]] -> [not rgnr.nullable]]
        # [not rgnr.nullable]
        # !! [[max_oolen >= 2] -> [not rgnr.always_dead] -> [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]]
        # [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]
        elif definite:
            # x[min_len]{min_len>=2}
            # [max_oolen >= 2][not rgnr.always_dead]
            # [not rgnr.nullable]
            # [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]
            assert not rgnr.nullable
            always_dead = False
            always_null = False
            nullable = False
            FIRST = rgnr.FIRST
            NON_FOLLOW = rgnr.NON_FOLLOW
        else:
            # x[min_len] + x{0..=relaxation}{min_len+relaxation>=2}
            # [max_oolen >= 2][not rgnr.always_dead]
            # [not rgnr.nullable]
            # [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]
            assert not rgnr.nullable
            always_dead = False
            always_null = False
            nullable = min_len == 0
            FIRST = rgnr.FIRST
            NON_FOLLOW = rgnr.NON_FOLLOW | rgnr.FIRST
        (always_dead, always_null, nullable, FIRST, NON_FOLLOW)



        sf._args4repr = (min_len, may_max_len, rgnr, args4rgnr)
        sf._m = min_len
        sf._M = may_max_len
        sf._r = rgnr
        sf._xs = args4rgnr
        sf._zs = rgnr_ex = (rgnr, *args4rgnr)
        super().__init__(always_dead, always_null, nullable, FIRST, NON_FOLLOW)
        sf.shallow_verify()

    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    @property
    def min_len(sf, /):
        '-> uint'
        return sf._m
    @property
    def may_max_len(sf, /):
        '-> may uint'
        return sf._M
    @property
    def rgnr(sf, /):
        '-> IRecognizerLL1'
        return sf._r
    @property
    def args4rgnr(sf, /):
        '-> tuple'
        return sf._xs
    @override
    def shallow_verify(sf, /):
        '-> None|^Exception'
        super().shallow_verify()
        # .,.+3s/\(sf\S*\) = \(\S*\)/\2 = \1
        min_len = sf._m
        may_max_len = sf._M
        rgnr = sf._r

        always_dead = sf.always_dead
        always_null = sf.always_null
        nullable = sf.nullable
        FIRST = sf.FIRST
        NON_FOLLOW = sf.NON_FOLLOW



        #####
        check_int_ge(0, min_len)
        check_may_([check_int_ge, min_len], may_max_len)
        check_type_le(IRecognizerLL1, rgnr)

        max_oolen = +oo if may_max_len is None else may_max_len
        assert max_oolen >= min_len

        relaxation = max_oolen -min_len
        definite = not relaxation
        indefinite = not definite




        #####
        assert not (indefinite and rgnr.nullable)
        # [indefinite -> [not rgnr.nullable]]
        assert not (max_oolen>=2 and rgnr.nullable and not rgnr.always_null)
        # [[max_oolen>=2] -> [not rgnr.always_null] -> [not rgnr.nullable]]
        #
        assert not (max_oolen >= 2 and not rgnr.always_dead and (rgnr.NON_FOLLOW & rgnr.FIRST))
        # [[max_oolen >= 2] -> [not rgnr.always_dead] -> [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]]



        #####
        #####
        #####
        #####
        #####
        if max_oolen == 0 or (rgnr.always_dead and min_len == 0) or rgnr.always_null:
            #always_null: x[0] or always_null[min_len]
            assert always_dead == False
            assert always_null == True
            assert nullable == True
            assert FIRST == null_frozenset
            assert NON_FOLLOW == null_frozenset
        # [not rgnr.always_null]
        # [[not [(min_len,max_oolen) <- {(0,0),(1,1)}]] -> [not rgnr.nullable]]

        elif rgnr.always_dead:
            assert min_len > 0
            #always_dead
            assert always_dead == True
            assert always_null == False
            assert nullable == False
            assert FIRST == null_frozenset
            assert NON_FOLLOW == null_frozenset
        #
        # [[not [(min_len,max_oolen) <- {(0,0),(1,1)}]] -> [not rgnr.nullable]]
        # [max_oolen >= 1][not rgnr.always_dead][not rgnr.always_null]
        elif max_oolen == 1:
            if definite:
                #x[1]
                # [min_len == 1][max_oolen == 1][not rgnr.always_dead][not rgnr.always_null]
                assert always_dead == rgnr.always_dead
                assert always_null == rgnr.always_null
                assert nullable == rgnr.nullable
                assert FIRST == rgnr.FIRST
                assert NON_FOLLOW == rgnr.NON_FOLLOW
            else:
                #optional: x?
                # [not rgnr.nullable]
                # [min_len == 0][max_oolen == 1][not rgnr.always_dead][not rgnr.always_null]
                #
                # =>[not sf.always_null]
                assert always_dead == False
                assert always_null == False
                assert nullable == True
                assert FIRST == rgnr.FIRST
                assert NON_FOLLOW == rgnr.NON_FOLLOW | rgnr.FIRST
        # [max_oolen >= 2][not rgnr.always_dead][not rgnr.always_null]
        # [not rgnr.nullable]
        # [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]
        elif definite:
            # x[min_len]{min_len>=2}
            # [max_oolen >= 2][not rgnr.always_dead]
            # [not rgnr.nullable]
            # [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]
            assert not rgnr.nullable
            assert always_dead == False
            assert always_null == False
            assert nullable == False
            assert FIRST == rgnr.FIRST
            assert NON_FOLLOW == rgnr.NON_FOLLOW
        else:
            # x[min_len] + x{0..=relaxation}{min_len+relaxation>=2}
            # [max_oolen >= 2][not rgnr.always_dead]
            # [not rgnr.nullable]
            # [{} == rgnr.NON_FOLLOW /-\ rgnr.FIRST]
            assert not rgnr.nullable
            assert always_dead == False
            assert always_null == False
            assert nullable is (min_len == 0)
            assert FIRST == rgnr.FIRST
            assert NON_FOLLOW == rgnr.NON_FOLLOW | rgnr.FIRST
        return


    @override
    def mk_gi8rgnr(sf, global_env, /):
        '-> gi8rgnr/IGeneratorIterator'
        rgnr_ex = sf._zs # = (rgnr, *args4rgnr)
        rgnr = rgnr_ex[0]
        min_len = sf.min_len
        may_max_len = sf.may_max_len
        ls = []
        _nullable = rgnr.nullable
        _FIRST = rgnr.FIRST
        it = count_(0, may_max_len)
        for j in it:
            if not _nullable:
                may_token = yield False # peek1
                if may_token is None:
                    if len(ls) < min_len:
                        return mk_Left(errmsg:=('eof', sf))
                    # [len(ls) >= min_len]
                    break
                else:
                    token = may_token
                    tkey = token.token_key
                    if not tkey in _FIRST:
                        if len(ls) < min_len:
                            return mk_Left(errmsg:=('not_meet', sf, tkey))
                        # [len(ls) >= min_len]
                        break
                    # [tkey in _FIRST]
                    pass
                # [next-tkey in rgnr.FIRST]
                pass
            else:
                # [rgnr.nullable]
                pass
            # [[rgnr.nullable]or[next-tkey in rgnr.FIRST]]
            child_oresult = yield rgnr_ex
            ls.append(child_oresult)
        else:
            assert len(ls) == may_max_len >= min_len
            # [len(ls) >= min_len]
        #end-for
        # [len(ls) >= min_len]
        ls
        child_oresults = mk_tuple(ls)

        oresult = (child_oresults)
            # without:NodeTag

        return mk_Right(oresult)
#end-class RecognizerLL1__array(IRecognizerLL1__init_properties):
RecognizerLL1__array(0, None, RecognizerLL1__tkey('...'), [])



class RecognizerLL1__parallel(IRecognizerLL1__init_properties):
    ___no_slots_ok___ = True
    @override
    def iter_direct_children(sf, /):
        '-> Iter IRecognizerLL1'
        return map(snd, sf.tag_rgnr_pairs)
    def __init__(sf, tag_rgnr_pairs, /):
        tag_rgnr_pairs = mk_tuple(tag_rgnr_pairs)

        for pair in tag_rgnr_pairs:
            check_pair(pair)
        for tag, rgnr in tag_rgnr_pairs:
            check_type_le(IRecognizerLL1, rgnr)

        tag2rgnr = dict(tag_rgnr_pairs)
        if not len(tag2rgnr) == len(tag_rgnr_pairs):raise KeyError([*iter_duplicate_representative_elements(tag_rgnr_pairs, key=fst)])

        rs = [rgnr for tag, rgnr in tag_rgnr_pairs]
        ts = [tag for tag, rgnr in tag_rgnr_pairs]
        def _js2tags(js, /):
            return [ts[j] for j in js]

        js4living = mk_tuple(j for j,r in enumerate(rs) if not r.always_dead)
        always_dead = not js4living
        always_null = len(js4living) == 1 and rs[js4living[0]].always_null
        js4nullable = mk_tuple(j for j,r in enumerate(rs) if r.nullable)
        if len(js4nullable) > 1: raise LL1GrammarError__multi_nullable_branches(_js2tags(js4nullable), tag_rgnr_pairs)

        nullable = bool(js4nullable)
        if nullable:
            [may_j4nullable] = js4nullable
        else:
            [], may_j4nullable = js4nullable, None
        may_j4nullable



        tkey2js8FIRST = defaultdict(list)
        ##tkey2js8NON_FOLLOW = defaultdict(list)
        def _update(j, tkeys, tkey2js, /):
            for tkey in tkeys:
                tkey2js[tkey].append(j)
        def _find_bads(tkey2js, /):
            return {k:_js2tags(js) for k,js in tkey2js.items() if not 1==len(js)}

        for j in js4living:
            r = rs[j]
            _update(j, r.FIRST, tkey2js8FIRST)
            ##_update(j, r.NON_FOLLOW, tkey2js8NON_FOLLOW)
        if (bads := _find_bads(tkey2js8FIRST)):raise LL1GrammarError__conflict_FIRST__branches(bads, tag_rgnr_pairs)
        ##if (bads := _find_bads(tkey2js8NON_FOLLOW)):raise LL1GrammarError__conflict_NON_FOLLOW__branches(bads, tag_rgnr_pairs)
            #bug! NON_FOLLOW need only simply union

        FIRST = mk_frozenset(tkey2js8FIRST)
        ##NON_FOLLOW = mk_frozenset(tkey2js8NON_FOLLOW)
        NON_FOLLOW = mk_frozenset(tkey for j in js4living for tkey in rs[j].NON_FOLLOW)
        if nullable:
            NON_FOLLOW |= FIRST

        tkey2j8FIRST = fmap4dict_value(unbox, tkey2js8FIRST)
        ##tkey2j8NON_FOLLOW = fmap4dict_value(unbox, tkey2js8NON_FOLLOW)


        j2tagged_rgnr = tag_rgnr_pairs
        js4living
        may_j4nullable
        tkey2j8FIRST
        ##tkey2j8NON_FOLLOW#used in shallow_verify only

        sf._ps = tag_rgnr_pairs
        sf._js = js4living
        sf._mjn = may_j4nullable
        sf._k2j4H = tkey2j8FIRST
            #head
        ##sf._k2j4T = tkey2j8NON_FOLLOW
            #tail

        super().__init__(always_dead, always_null, nullable, FIRST, NON_FOLLOW)
        sf.shallow_verify()


    def __repr__(sf, /):
        return repr_helper(sf, sf._ps)
    @property
    def tag_rgnr_pairs(sf, /):
        '-> [(tag, IRecognizerLL1)]'
        return sf._ps
    @override
    def shallow_verify(sf, /):
        '-> None|^Exception'
        super().shallow_verify()
        # .,.+5s/\(sf\S*\) = \(\S*\)/\2 = \1
        tag_rgnr_pairs = sf._ps
        js4living = sf._js
        may_j4nullable = sf._mjn
        tkey2j8FIRST = sf._k2j4H
        ##tkey2j8NON_FOLLOW = sf._k2j4T

        always_dead = sf.always_dead
        always_null = sf.always_null
        nullable = sf.nullable
        FIRST = sf.FIRST
        NON_FOLLOW = sf.NON_FOLLOW


        #####
        tag_rgnr_pairs
        check_type_is(tuple, tag_rgnr_pairs)

        for pair in tag_rgnr_pairs:
            check_pair(pair)
        for tag, rgnr in tag_rgnr_pairs:
            check_type_le(IRecognizerLL1, rgnr)
        assert len(dict(tag_rgnr_pairs)) == len(tag_rgnr_pairs)

        #####
        rs = [rgnr for tag, rgnr in tag_rgnr_pairs]
        ts = [tag for tag, rgnr in tag_rgnr_pairs]


        #####
        js4living
        i = -1
        for j in js4living:
            assert i < j
            for r in rs[i+1:j]:
                assert r.always_dead
            assert not rs[j].always_dead
            ###
            i = j
        assert i < len(rs)
        #####
        may_j4nullable
        for j, r in enumerate(rs):
            assert r.nullable is (j == may_j4nullable)
        #####
        tkey2j8FIRST
        ##tkey2j8NON_FOLLOW
        def _test(sz4acc, j, tkeys, tkey2j, /):
            for tkey in tkeys:
                assert tkey2j[tkey] == j
            return sz4acc+len(tkeys)
        sz4T = sz4H = 0
        for j in js4living:
            r = rs[j]
            sz4H = _test(sz4H, j, r.FIRST, tkey2j8FIRST)
            ##sz4T = _test(sz4T, j, r.NON_FOLLOW, tkey2j8NON_FOLLOW)
        assert sz4H == len(tkey2j8FIRST)
        ##assert sz4T == len(tkey2j8NON_FOLLOW)

        #####
        assert always_dead is (not js4living)
        assert always_null is (len(js4living) == 1 and rs[js4living[0]].always_null), (always_null, (len(js4living) == 1, rs[js4living[0]].always_null))
        #bug:assert always_null is (not may_j4nullable is None and rs[may_j4nullable].always_null), (always_null, (not may_j4nullable is None, rs[may_j4nullable].always_null))
                #必须是:唯一活分支 才有效
        assert nullable is (not may_j4nullable is None and rs[may_j4nullable].nullable)
        assert FIRST == tkey2j8FIRST.keys()
        ##assert NON_FOLLOW == tkey2j8NON_FOLLOW.keys()
        assert NON_FOLLOW == {tkey for j in js4living for tkey in rs[j].NON_FOLLOW} | (FIRST if nullable else {*[]})
        #####

        return

    @override
    def mk_gi8rgnr(sf, global_env, nonterminal_symbol, /, *args):
        '-> gi8rgnr/IGeneratorIterator'
        may_token = yield False # peek1
        if may_token is None:
            if not sf.nullable:
                return mk_Left(errmsg:=('eof', nonterminal_symbol))
            j = may_j4nullable = sf._mjn
        else:
            token = may_token
            tkey = token.token_key
            tkey2j8FIRST = sf._k2j4H
            if None is (j := tkey2j8FIRST.get(tkey)):
                if not sf.nullable:
                    return mk_Left(errmsg:=('not_meet', nonterminal_symbol, tkey))
                j = may_j4nullable = sf._mjn
            else:
                j
            j
        j
        #xxx:yield True # read1
        tag_rgnr_pairs = sf._ps
        (branch_tag, child_rgnr) = tag_rgnr_pairs[j]
        child_oresult = yield child_rgnr
        oresult = (NodeTag.NP, nonterminal_symbol, Cased(branch_tag, child_oresult))
        return mk_Right(oresult)
#end-class RecognizerLL1__parallel(IRecognizerLL1__init_properties):
RecognizerLL1__parallel([])




_TYPES4ref = \
(RecognizerLL1__parallel
,RecognizerLL1__serial
,RecognizerLL1__alias__pick_one
)



def __():
    r0 = RecognizerLL1__constant_loader('ooo')
    r1 = RecognizerLL1__tkey('...')
    r2 = RecognizerLL1__array(0, None, r1, [])


    r3 = RecognizerLL1__alias__pick_one([r0], r1, [r2])
    r4 = RecognizerLL1__serial([Cased(0, r0), Cased(1, r1), Cased(2, r2)])
    r5 = RecognizerLL1__parallel([(0, r0), (1, r1)])


    #RecognizerLL1__ref8fwd_decl(smay_qname4repr, nonterminal_symbol, always_dead, always_null, nullable, FIRST, NON_FOLLOW, may_rgnr, /):
    r6 = RecognizerLL1__ref8fwd_decl('', 'nnn', False, False, True, {'...'}, {'...'}, r5)

    r0.deep_verify()
    r1.deep_verify()
    r2.deep_verify()
    r3.deep_verify()
    r4.deep_verify()
    r5.deep_verify()
    r6.deep_verify()
__()

__all__
from seed.recognize.recognizer_LL1_.IRecognizerLL1 import \
(IRecognizerLL1
,parse_via_rgnrLL1
,    RecognizerLL1__constant_loader
,    RecognizerLL1__tkey
,    RecognizerLL1__array
,    RecognizerLL1__ref8fwd_decl
,        GlobalEnvironment4LL1
,            Symbol4postprocess
,        NodeTag
,            RecognizerLL1__parallel
,            RecognizerLL1__serial
,            RecognizerLL1__alias__pick_one
)




from seed.recognize.recognizer_LL1_.IRecognizerLL1 import *
