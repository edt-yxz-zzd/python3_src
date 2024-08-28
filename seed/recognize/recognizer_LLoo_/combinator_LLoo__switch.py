#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__switch.py

if_then_else
switch_branches
dependent_pair


seed.recognize.recognizer_LLoo_.combinator_LLoo__switch
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__switch -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__switch:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.combinator_LLoo__switch   @f
#]]]'''
__all__ = r'''
mk_LLoo__dependent_pair
mk_LLoo__switch_branches
mk_LLoo__if_then_else

IRecognizerLLoo__switch
    RecognizerLLoo__switch
        IMaker4RecognizerLLoo__5oresult
        RecognizerLLoo__switch_branches
            Maker4RecognizerLLoo__5oresult__4switch_branches
            RecognizerLLoo__if_then_else

IMaker4RecognizerLLoo__5oresult
    Maker4RecognizerLLoo__5oresult__4switch_branches
    Maker4RecognizerLLoo__5oresult__constant_rgnr


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.recognizer_LLoo_._common import (IForkable__stamp
,Cased, Either# mk_Left, mk_Right
,check_non_ABC
,check_type_is, check_type_le
,mk_tuple, null_iter
,abstractmethod, override, ABC
,repr_helper, _Base4repr
)
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, IDependentTreeNode, Signal__HeaderCompleted

from seed.tiny_.check import check_int_ge_lt

from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import IRecognizerLLoo__serial_framework
from seed.tiny_.CompactData import mk_CompactDataType

from operator import __index__

from seed.recognize.recognizer_LLoo_.IMaker4RecognizerLLoo import IMaker4RecognizerLLoo__5args_ex, IMaker4RecognizerLLoo__5args

___end_mark_of_excluded_global_names__0___ = ...

_Ctx = mk_CompactDataType(__slots__='may_either_oresult', __module__=__name__, __qualname__='_Ctx')



class IRecognizerLLoo__switch(IRecognizerLLoo__serial_framework):
    'switch/~=dependent_pair  #assume[inputter contains global runtime info...]#'
    __slots__ = ()
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend

    @abstractmethod
    def _be_dependent_pair_(sf, /):
        '-> bool'
    @abstractmethod
    def _get_uhidx4hdr_(sf, /):
        '-> uhidx4hdr/uint%5'
    @abstractmethod
    def _get_rgnr4case_(sf, /):
        '-> rgnr4case/IRecognizerLLoo'
    @abstractmethod
    def _mk_rgnr4body_(sf, oresult4rgnr4case, inputter, /):
        'oresult4rgnr4case/oresult<rgnr4case> -> inputter.fork() -> rgnr4body/IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'


    @override
    def _iter_child_items4serial4LLoo_(sf, /):
        '-> Iter child_item'
        yield False#0
        yield True#1
        return
    @override
    def _initialize_context4serial4LLoo_(sf, inputter4whole, /):
        'inputter4whole.fork() -> ctx' ' #assume[inputter contains global runtime info...]'
        return _Ctx(may_either_oresult=None)
    @override
    def _is_stopped4serial4LLoo_(sf, ctx, inputter, /):
        'ctx -> inputter.fork() -> stopped/bool' ' #assume[inputter contains global runtime info...]'
        return False
    @override
    def _mk_child_recognizer_ex4serial4LLoo_(sf, ctx, child_item, inputter, /):
        'ctx -> child_item -> inputter.fork() -> (child_rgnr/IRecognizerLLoo, ctx)' ' #assume[inputter contains global runtime info...]'
        if child_item is False:
            assert None is ctx.may_either_oresult
            return sf._get_rgnr4case_()
        elif child_item is True:
            oresult4rgnr4case = ctx.may_either_oresult.left
            return sf._mk_rgnr4body_(oresult4rgnr4case, inputter)
        raise 000
    @override
    def _update_context4serial4LLoo_(sf, child_item, child_rgnr, ctx, result6ok4child, inputter, /):
        'child_item -> child_rgnr -> ctx -> result6ok4child -> inputter.fork() -> ctx' ' #assume[inputter contains global runtime info...]'
        if child_item is True and sf._be_dependent_pair_():
            oresult4fst = ctx.may_either_oresult.left
            oresult4snd = result6ok4child
            pair = (oresult4fst, oresult4snd)
            right = pair
        else:
            right = result6ok4child
        right
        ctx.may_either_oresult = Either(child_item, right)
        return ctx
    @override
    def _finalize_oresult4serial4LLoo_(sf, ctx, inputter, /):
        'ctx -> inputter.fork() -> result6ok4whole_LLoo' ' #assume[inputter contains global runtime info...]'
        oresult4rgnr4body_or_pair = ctx.may_either_oresult.right
        oresult4rgnr4whole = oresult4rgnr4body_or_pair
        return oresult4rgnr4whole
    @override
    def _mk_may_header_signal_at_child_beginning_(sf, child_item, child_rgnr, ctx, consumed0, inputter, /):
        '-> may Signal__HeaderCompleted'
        uhidx4hdr = sf._get_uhidx4hdr_()
        #if not uhidx4hdr == (0 if child_item is False else 2):
        if not (child_item is False and uhidx4hdr == 0):
            return None
        #hdr_sgnl = Signal__HeaderCompleted(inputter, ctx.may_either_oresult)
        hdr_sgnl = Signal__HeaderCompleted(inputter, None)
        return hdr_sgnl
    @override
    def _mk_may_header_signal5header_signal_(sf, child_item, child_rgnr, ctx, consumed0, consumed, hdr_sgnl, /):
        '-> may Signal__HeaderCompleted'
        uhidx4hdr = sf._get_uhidx4hdr_()
        if not uhidx4hdr == (1 if child_item is False else 3):
            return None
        return hdr_sgnl
    @override
    def _mk_may_header_signal5ok_reply_(sf, child_item, child_rgnr, reply4LLoo, consumed0, consumed, ctx, /):
        '-> may Signal__HeaderCompleted'
        uhidx4hdr = sf._get_uhidx4hdr_()
        if not uhidx4hdr == (2 if child_item is False else 4):
            return None
        hdr_sgnl = reply4LLoo.to_Signal__HeaderCompleted()
        return hdr_sgnl





class IMaker4RecognizerLLoo__5oresult(IMaker4RecognizerLLoo__5args_ex):
    #class IMaker4RecognizerLLoo__5oresult(IDependentTreeNode):
    'oresult/result6ok:oresult4rgnr4case/[#see:switch#]'
    __slots__ = ()
    @abstractmethod
    def _mk_recognizer_LLoo5oresult_(sf, oresult4rgnr4case, inputter, /):
        'oresult<rgnr4case> -> inputter.fork() -> rgnr4body/IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
    def mk_recognizer_LLoo5oresult(sf, oresult4rgnr4case, inputter, /):
        'oresult<rgnr4case> -> inputter.fork() -> rgnr4body/IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        check_type_le(IForkable__stamp, inputter)
        rgnr = sf._mk_recognizer_LLoo5oresult_(oresult4rgnr4case, inputter.fork())
        check_type_le(IRecognizerLLoo, rgnr)
        return rgnr


    #@override
    num_args4mkr4LLoo = 1

    @override
    def _mk_recognizer_LLoo5args_ex_(sf, inputter, /, *args):
        'inputter.fork() -> (*args){len=.num_args4mkr4LLoo} -> IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        rgnr = sf._mk_recognizer_LLoo5oresult_(*args, inputter) #.fork()
        return rgnr
IMaker4RecognizerLLoo__5oresult

class RecognizerLLoo__switch(IRecognizerLLoo__switch, _Base4repr):
    'switch/dependent_pair'
    ___no_slots_ok___ = True
    def __init__(sf, switch_vs_pair, uhidx4hdr, rgnr4case, mkr4body, /):
        check_type_is(bool, switch_vs_pair)
        check_int_ge_lt(0, 5, uhidx4hdr)
        check_type_le(IRecognizerLLoo, rgnr4case)
        check_type_le(IMaker4RecognizerLLoo__5oresult, mkr4body)
        sf._b = switch_vs_pair
        sf._u = uhidx4hdr
        sf._r = rgnr4case
        sf._k = mkr4body
        sf._args4repr = (switch_vs_pair, uhidx4hdr, rgnr4case, mkr4body)

    @override
    def _be_dependent_pair_(sf, /):
        '-> bool'
        switch_vs_pair = sf._b
        return switch_vs_pair
    @override
    def _get_uhidx4hdr_(sf, /):
        '-> uhidx4hdr/uint%5'
        uhidx4hdr = sf._u
        return uhidx4hdr
    @override
    def _get_rgnr4case_(sf, /):
        '-> rgnr4case/IRecognizerLLoo'
        rgnr4case = sf._r
        return rgnr4case
    @override
    def _mk_rgnr4body_(sf, oresult4rgnr4case, inputter, /):
        'oresult4rgnr4case/oresult<rgnr4case> -> inputter.fork() -> rgnr4body/IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        mkr4body = sf._k
        rgnr4body = mkr4body.mk_recognizer_LLoo5oresult(oresult4rgnr4case, inputter)
        return rgnr4body

    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        rgnr4case = sf._r
        yield rgnr4case
        mkr4body = sf._k
        yield mkr4body
        return
check_non_ABC(RecognizerLLoo__switch)





class Maker4RecognizerLLoo__5oresult__constant_rgnr(IMaker4RecognizerLLoo__5oresult):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._r)
    def __init__(sf, rgnr, /):
        check_type_le(IRecognizerLLoo, rgnr)
        sf._r = rgnr
    @override
    def _mk_recognizer_LLoo5oresult_(sf, oresult4rgnr4case, inputter, /):
        'oresult<rgnr4case> -> inputter.fork() -> rgnr4body/IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        rgnr = sf._r
        return rgnr
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        rgnr = sf._r
        yield rgnr
        return
check_non_ABC(Maker4RecognizerLLoo__5oresult__constant_rgnr)




class Maker4RecognizerLLoo__5oresult__4switch_branches(IMaker4RecognizerLLoo__5oresult):
    '[oresult/cased_oresult4branch :: Cased<idx/ibranch,payload8oresult>] #see:switch_branches'
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._mkrs)
    def __init__(sf, mkrs4branches, /):
        mkrs4branches = mk_tuple(mkrs4branches)
        for mkr4branch in mkrs4branches:
            check_type_le(IMaker4RecognizerLLoo__5oresult, mkr4branch)
        sf._mkrs = mkrs4branches
    @override
    def _mk_recognizer_LLoo5oresult_(sf, oresult4rgnr4case, inputter, /):
        'oresult<rgnr4case> -> inputter.fork() -> rgnr4body/IRecognizerLLoo' ' #assume[inputter contains global runtime info...]'
        check_type_le(Cased, oresult4rgnr4case)
        cased_oresult4branch = oresult4rgnr4case
        case = cased_oresult4branch.case
            # (int|bool)
        ibranch = __index__(case)
        mkrs4branches = sf._mkrs
        L = len(mkrs4branches)
        check_int_ge_lt(0, L, ibranch)
        mkr4branch = mkrs4branches[ibranch]

        oresult4branch = cased_oresult4branch.payload
        return mkr4branch.mk_recognizer_LLoo5oresult(oresult4branch, inputter)
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        mkrs4branches = sf._mkrs
        return iter(mkrs4branches)
check_non_ABC(Maker4RecognizerLLoo__5oresult__4switch_branches)

class RecognizerLLoo__switch_branches(RecognizerLLoo__switch):
    'switch_branches:[oresult<rgnr4case>/cased_oresult4branch :: Cased<idx/ibranch,payload8oresult>]'
    ___no_slots_ok___ = True
    def __init__(sf, switch_vs_pair, uhidx4hdr, rgnr4case, mkrs4branches, /):
        mkrs4branches = mk_tuple(mkrs4branches)
        mkr4body = Maker4RecognizerLLoo__5oresult__4switch_branches(mkrs4branches)
        super().__init__(switch_vs_pair, uhidx4hdr, rgnr4case, mkr4body)
        777;    sf._args4repr = (switch_vs_pair, uhidx4hdr, rgnr4case, mkrs4branches)
check_non_ABC(RecognizerLLoo__switch_branches)





class RecognizerLLoo__if_then_else(RecognizerLLoo__switch_branches):
    ' if_then_else:[oresult<rgnr4case>/cased_oresult4branch :: Either/Cased<ibranch/uint%2/bool,payload8oresult>]'
    ___no_slots_ok___ = True
    def __init__(sf, switch_vs_pair, uhidx4hdr, rgnr4if, mkr4then, mkr4else, /):
        mkrs4branches = (mkr4then, mkr4else)
        super().__init__(switch_vs_pair, uhidx4hdr, rgnr4if, mkrs4branches)
        777;    sf._args4repr = (switch_vs_pair, uhidx4hdr, rgnr4if, mkr4then, mkr4else)
check_non_ABC(RecognizerLLoo__if_then_else)


def _mkr5or_rgnr_(rgnr_or_mkr, /):
    '-> IMaker4RecognizerLLoo__5oresult'
    if isinstance(rgnr_or_mkr, IRecognizerLLoo):
        rgnr = rgnr_or_mkr
        mkr = Maker4RecognizerLLoo__5oresult__constant_rgnr(rgnr)
    else:
        mkr = rgnr_or_mkr
    mkr
    return mkr

def mk_LLoo__dependent_pair(rgnr4fst, rgnrXmkr4snd, /):
    'IRecognizerLLoo -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> IRecognizerLLoo{dependent_pair}'#RecognizerLLoo__switch
    mkr4snd = _mkr5or_rgnr_(rgnrXmkr4snd)
    return RecognizerLLoo__switch(switch_vs_pair:=True, uhidx4hdr:=1, rgnr4fst, mkr4snd)
def mk_LLoo__switch_branches(rgnr4case, rgnrXmkr_ls4branches, /):
    'IRecognizerLLoo{oresult/Cased} -> [(IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult)] -> IRecognizerLLoo'#RecognizerLLoo__switch_branches
    mkrs4branches = map(_mkr5or_rgnr_, rgnrXmkr_ls4branches)
    return RecognizerLLoo__switch_branches(switch_vs_pair:=False, uhidx4hdr:=3, rgnr4case, mkrs4branches)
def mk_LLoo__if_then_else(rgnr4if, rgnr_or_mkr4then, rgnr_or_mkr4else, /):
    'IRecognizerLLoo{oresult/Either} -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> (IRecognizerLLoo|IMaker4RecognizerLLoo__5oresult) -> IRecognizerLLoo'#RecognizerLLoo__if_then_else
    mkr4then = _mkr5or_rgnr_(rgnr_or_mkr4then)
    mkr4else = _mkr5or_rgnr_(rgnr_or_mkr4else)
    return RecognizerLLoo__if_then_else(switch_vs_pair:=False, uhidx4hdr:=3, rgnr4if, mkr4then, mkr4else)



__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__switch import mk_LLoo__dependent_pair, mk_LLoo__switch_branches, mk_LLoo__if_then_else
from seed.recognize.recognizer_LLoo_.combinator_LLoo__switch import *
