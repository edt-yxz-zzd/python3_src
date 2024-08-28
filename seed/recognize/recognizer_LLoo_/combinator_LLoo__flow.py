#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/combinator_LLoo__flow.py

seed.recognize.recognizer_LLoo_.combinator_LLoo__flow
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.combinator_LLoo__flow -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.combinator_LLoo__flow:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.combinator_LLoo__flow   @f
#]]]'''
__all__ = r'''
mk_LLoo__flow


IRecognizerLLoo__flow
    IRecognizerLLoo__flow__using_containers4instructions
        RecognizerLLoo__flow

IInstruction4flow4LLoo
    Instruction4flow4LLoo__wrapper
        Instruction4flow4LLoo__hdr_sgnl
    Instruction4flow4LLoo__return
    Instruction4flow4LLoo__goto
    Instruction4flow4LLoo__switch

    Instruction4flow4LLoo__exec
    Instruction4flow4LLoo__del_nms6ctx
    Instruction4flow4LLoo__mkr4rgnr7ctx
        ICtxUpdater__5oresult

ICtxUpdater__5oresult
    CtxUpdater__5oresult__assign_nm6ctx
    CtxUpdater__5oresult__assign_nms6ctx
    CtxUpdater__5oresult__no_update
        no_op_updater


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.recognizer_LLoo_._common import (IForkable__stamp
#mk#_gi4either8xresult
,BoxedFinalResult, BoxedHalfwayResult
,Cased, Either, mk_Left, mk_Right
,check_non_ABC
,check_type_is, check_type_le, check_int_ge
,mk_tuple, null_iter
,abstractmethod, override, ABC
,repr_helper, _Base4repr
)
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo, IDependentTreeNode



from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import recognizer_LLoo__ignore#recognizer_LLoo__pass
from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import IRecognizerLLoo__flow_framework
from seed.recognize.recognizer_LLoo_.combinator_LLoo__serial import IMaker4RecognizerLLoo__5ctx, rgnr_or2mkr4rgnr7ctx
from seed.tiny_.types5py import MapView
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IWrapper

from seed.tiny_.check import check_pseudo_identifier

from collections.abc import Mapping, Hashable
from types import CodeType

from seed.tiny_.containers import null_mapping_view
___end_mark_of_excluded_global_names__0___ = ...


class IInstruction4flow4LLoo(IDependentTreeNode):
    __slots__ = ()
    @abstractmethod
    def is_instruction4hdr_sgnl(sf, /):
        '-> bool'
    @abstractmethod
    def mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(sf, ctx, inputter, /):
        'ctx/dict -> inputter.fork() -> child_rgnr/IRecognizerLLoo # [inplace update ctx/dict]' ' #assume[inputter contains global runtime info...]'
    @abstractmethod
    def mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(sf, idx4instruction, child_rgnr, ctx, oresult4child, inputter, /):
        'idx4instruction/uint -> child_rgnr/IRecognizerLLoo -> ctx/dict -> oresult4child -> inputter.fork() -> Either<oresult4return,next_addr_label4instruction> # [inplace update ctx/dict] #[addr_label :: (int|label)]'


def _tmay_addr_label2may_idx4instruction_(sf, tmay_addr_label4instruction, /):
    '-> may_idx4instruction'
    if tmay_addr_label4instruction:
        [addr_label4instruction] = tmay_addr_label4instruction
        if type(addr_label4instruction) is int:
            idx4instruction = addr_label4instruction
        else:
            idx4instruction = sf._addr_label2idx4instruction_(addr_label4instruction)
        idx4instruction
        may_idx4instruction = idx4instruction
    else:
        may_idx4instruction = None
    may_idx4instruction
    if not may_idx4instruction is None:
        idx4instruction = may_idx4instruction
        check_int_ge(0, idx4instruction)
    may_idx4instruction
    return may_idx4instruction


class IRecognizerLLoo__flow(IRecognizerLLoo__flow_framework):
    'flow#assume[inputter contains global runtime info...]'
    __slots__ = ()

    @abstractmethod
    def _idx2instruction_(sf, idx4instruction, /):
        '-> instruction/IInstruction4flow4LLoo | ^LookupError'
    @abstractmethod
    def _addr_label2idx4instruction_(sf, addr_label4instruction, /):
        '-> idx4instruction/uint'

    @override
    def _initialize_state_context4flow4LLoo_(sf, inputter4whole, /):
        'inputter4whole.fork() -> (state4flow, ctx)' ' #assume[inputter contains global runtime info...]'
        state4flow = idx4instruction = 0
        ctx = {}
        return (state4flow, ctx)
    @override
    def _next_child_item_ex4flow4LLoo_(sf, state4flow, ctx, /):
        'state4flow -> ctx -> (child_item, ctx) | ^StopIteration' '  ###[no StopIteration:MUST use return_instruction] ### fatal-fault:^LookupError'
        idx4instruction = state4flow
        check_int_ge(0, idx4instruction)
        instruction = sf._idx2instruction_(idx4instruction)
            # ^LookupError
        check_type_le(IInstruction4flow4LLoo, instruction)
        child_item = instruction
        return (child_item, ctx)
    @override
    def _is_stopped4flow4LLoo_(sf, state4flow, ctx, inputter, /):
        'state4flow -> ctx -> inputter.fork() -> stopped/bool' ' #assume[inputter contains global runtime info...]'
        may_idx4instruction = state4flow
        return may_idx4instruction is None
    @override
    def _mk_child_recognizer_ex4flow4LLoo_(sf, state4flow, ctx, child_item, inputter, /):
        'state4flow -> ctx -> child_item -> inputter.fork() -> (child_rgnr/IRecognizerLLoo, ctx)' ' #assume[inputter contains global runtime info...]'
        instruction = child_item
        child_rgnr = instruction.mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(ctx, inputter)
        return (child_rgnr, ctx)
    @override
    def _update_state_context4flow4LLoo_(sf, state4flow, child_item, child_rgnr, ctx, result6ok4child, inputter, /):
        'state4flow -> child_item -> child_rgnr -> ctx -> result6ok4child -> inputter.fork() -> (state4flow, ctx)' ' #assume[inputter contains global runtime info...]'
        check_type_is(dict, ctx)
        idx4instruction = state4flow
        instruction = child_item
        oresult4child = result6ok4child
        tmay_next_addr_label4instruction
        either_ores_or_next = instruction.mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(idx4instruction, child_rgnr, ctx, oresult4child, inputter)
        check_type_is(Either, either_ores_or_next)
        tmay_next_addr_label4instruction = either_ores_or_next.to_tmay_right()
        may_idx4instruction = _tmay_addr_label2may_idx4instruction_(sf, tmay_next_addr_label4instruction)
        state4flow = may_idx4instruction
        ######################
        #if instruction.is_instruction4return():
        if may_idx4instruction is None:
            #stop/return
            #is:return_instruction
            oresult4return = either_ores_or_next.left
            ctx = (ctx, oresult4return)
        ######################
        return (state4flow, ctx)
        ######################
    @override
    def _finalize_oresult4flow4LLoo_(sf, state4flow, ctx, inputter, /):
        'state4flow -> ctx -> inputter.fork() -> result6ok4whole_LLoo' ' #assume[inputter contains global runtime info...]'
        check_type_is(tuple, ctx)
        (ctx, oresult4return) = ctx
        return oresult4return

    ######################
    ######################
    @override
    def _mk_may_header_signal_at_child_beginning_(sf, child_item, child_rgnr, ctx, consumed0, inputter, /):
        '-> may Signal__HeaderCompleted'
        return None
    @override
    def _mk_may_header_signal5header_signal_(sf, child_item, child_rgnr, ctx, consumed0, consumed, hdr_sgnl, /):
        '-> may Signal__HeaderCompleted'
        instruction = child_item
        if instruction.is_instruction4hdr_sgnl():
            return hdr_sgnl
        return None
    @override
    def _mk_may_header_signal5ok_reply_(sf, child_item, child_rgnr, reply4LLoo, consumed0, consumed, ctx, /):
        '-> may Signal__HeaderCompleted'
        instruction = child_item
        if instruction.is_instruction4hdr_sgnl():
            hdr_sgnl = reply4LLoo.to_Signal__HeaderCompleted()
            return hdr_sgnl
        return None











class IRecognizerLLoo__flow__using_containers4instructions(IRecognizerLLoo__flow):
    'flow#assume[inputter contains global runtime info...]'
    __slots__ = ()
    @abstractmethod
    def _get_instructions_(sf, /):
        '-> instructions/j2instruction/[instruction]'
    @abstractmethod
    def _get_label2idx4instruction_(sf, /):
        '-> label2idx4instruction/{label4instruction:idx4instruction}'

    @override
    def _idx2instruction_(sf, idx4instruction, /):
        '-> instruction/IInstruction4flow4LLoo | ^LookupError'
        j2instruction = sf._get_instructions_()
        instruction = j2instruction[idx4instruction]
            # ^LookupError
        return instruction
    @override
    def _addr_label2idx4instruction_(sf, addr_label4instruction, /):
        '-> idx4instruction/uint'
        if type(addr_label4instruction) is int:raise TypeError
        label2idx4instruction = sf._get_label2idx4instruction_()
        idx4instruction = label2idx4instruction[addr_label4instruction]
        return idx4instruction

    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        j2instruction = sf._get_instructions_()
        j2instruction[:0] #check seq
        return iter(j2instruction)









class RecognizerLLoo__flow(IRecognizerLLoo__flow__using_containers4instructions, _Base4repr):
    'flow#assume[inputter contains global runtime info...]'
    ___no_slots_ok___ = True
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend

    def __init__(sf, instructions, label2idx4instruction, /):
        check_type_le(Mapping, label2idx4instruction)
        for idx4instruction in label2idx4instruction.values():
            check_int_ge(0, idx4instruction)

        instructions = mk_tuple(instructions)
        for instruction in instructions:
            check_type_le(IInstruction4flow4LLoo, instruction)

        sf._j2op = instructions
        sf._nm2j = label2idx4instruction
        _Base4repr.__init__(sf, instructions, label2idx4instruction)

    @override
    def _get_instructions_(sf, /):
        '-> instructions/j2instruction/[instruction]'
        return sf._j2op
    @override
    def _get_label2idx4instruction_(sf, /):
        '-> label2idx4instruction/{label4instruction:idx4instruction}'
        return sf._nm2j
check_non_ABC(RecognizerLLoo__flow)











class _IInstruction4flow4LLoo__no_ref(IInstruction4flow4LLoo, _Base4repr):
    ___no_slots_ok___ = True
    @override
    def is_instruction4hdr_sgnl(sf, /):
        '-> bool'
        return False
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        return null_iter











class Instruction4flow4LLoo__wrapper(_IInstruction4flow4LLoo__no_ref, IWrapper):

    @property
    @override
    def the_wrapped_obj(sf, /):
        '-> wrapped_obj'
        return sf._op
    #@override
    _base_type4wrapped_obj_ = IInstruction4flow4LLoo


    def __init__(sf, instruction, /):
        #check_type_le(IInstruction4flow4LLoo, instruction)
        sf._check_wrapped_obj_(instruction)
        sf._op = instruction
        _Base4repr.__init__(sf, instruction)

    @override
    def is_instruction4hdr_sgnl(sf, /):
        '-> bool'
        instruction = sf._op
        return instruction.is_instruction4hdr_sgnl()
    @override
    def mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(sf, ctx, inputter, /):
        'ctx/dict -> inputter.fork() -> child_rgnr/IRecognizerLLoo # [inplace update ctx/dict]' ' #assume[inputter contains global runtime info...]'
        instruction = sf._op
        return instruction.mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(ctx, inputter)
    @override
    def mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(sf, idx4instruction, child_rgnr, ctx, oresult4child, inputter, /):
        'idx4instruction/uint -> child_rgnr/IRecognizerLLoo -> ctx/dict -> oresult4child -> inputter.fork() -> Either<oresult4return,next_addr_label4instruction> # [inplace update ctx/dict] #[addr_label :: (int|label)]'
        instruction = sf._op
        return instruction.mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(idx4instruction, child_rgnr, ctx, oresult4child, inputter)
check_non_ABC(Instruction4flow4LLoo__wrapper)

class Instruction4flow4LLoo__hdr_sgnl(Instruction4flow4LLoo__wrapper):
    @override
    def is_instruction4hdr_sgnl(sf, /):
        '-> bool'
        return True
check_non_ABC(Instruction4flow4LLoo__hdr_sgnl)










class Instruction4flow4LLoo__return(_IInstruction4flow4LLoo__no_ref):
    def __init__(sf, nm6ctx, /):
        check_type_le(Hashable, nm6ctx)
        sf._k = nm6ctx
        _Base4repr.__init__(sf, nm6ctx)
    @override
    def mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(sf, ctx, inputter, /):
        'ctx/dict -> inputter.fork() -> child_rgnr/IRecognizerLLoo # [inplace update ctx/dict]' ' #assume[inputter contains global runtime info...]'
        raise 000
    @override
    def mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(sf, idx4instruction, child_rgnr, ctx, oresult4child, inputter, /):
        'idx4instruction/uint -> child_rgnr/IRecognizerLLoo -> ctx/dict -> oresult4child -> inputter.fork() -> Either<oresult4return,next_addr_label4instruction> # [inplace update ctx/dict] #[addr_label :: (int|label)]'
        nm6ctx = sf._k
        oresult4return = ctx[nm6ctx]
        return mk_Left(oresult4return)
check_non_ABC(Instruction4flow4LLoo__return)














class Instruction4flow4LLoo__goto(_IInstruction4flow4LLoo__no_ref):
    'Either<relative4next_addr,next_addr_label4instruction>'
    def __init__(sf, either_relative4next_addr_or_next_addr_label4instruction, /):
        either_rel_or_nm = sf._x = either_relative4next_addr_or_next_addr_label4instruction
        _check__either_rel_or_nm(either_rel_or_nm)
        _Base4repr.__init__(sf, either_rel_or_nm)
    @override
    def mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(sf, ctx, inputter, /):
        'ctx/dict -> inputter.fork() -> child_rgnr/IRecognizerLLoo # [inplace update ctx/dict]' ' #assume[inputter contains global runtime info...]'
        return recognizer_LLoo__ignore

    @override
    def mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(sf, idx4instruction, child_rgnr, ctx, oresult4child, inputter, /):
        'idx4instruction/uint -> child_rgnr/IRecognizerLLoo -> ctx/dict -> oresult4child -> inputter.fork() -> Either<oresult4return,next_addr_label4instruction> # [inplace update ctx/dict] #[addr_label :: (int|label)]'
        either_rel_or_nm = sf._x
        either_ores_or_next = _mk__either_ores_or_next__5__either_rel_or_nm(idx4instruction, either_rel_or_nm)
        return either_ores_or_next
check_non_ABC(Instruction4flow4LLoo__goto)







def _check__either_rel_or_nm(either_rel_or_nm, /):
    check_type_is(Either, either_rel_or_nm)
    if either_rel_or_nm.is_left:
        relative4next_addr = either_rel_or_nm.left
        check_type_is(int, relative4next_addr)
    elif type(next_addr:=either_rel_or_nm.right) is int:
        idx4next_instruction = next_addr
        check_int_ge(0, idx4next_instruction)
    else:
        label4next_instruction = next_addr
        check_type_le(Hashable, label4next_instruction)
def _mk__either_ores_or_next__5__either_rel_or_nm(idx4instruction, either_rel_or_nm, /):
    'idx4instruction -> either_rel_or_nm -> either_ores_or_next{.is_right}'
    if either_rel_or_nm.is_right:
        either_ores_or_next = either_rel_or_nm
    else:
        relative4next_addr = either_rel_or_nm.left
        next_addr_label4instruction = relative4next_addr + idx4instruction
        either_ores_or_next = mk_Right(next_addr_label4instruction)
    #assert either_ores_or_next.is_right
    check_int_ge(0, either_ores_or_next.right)
    return either_ores_or_next
def _mk__either_ores_or_next__5__idx4instruction__plus1(idx4instruction, /):
    'idx4instruction -> either_ores_or_next{.is_right} # [idx4instruction+=1]'
    next_addr_label4instruction = 1 + idx4instruction
    either_ores_or_next = mk_Right(next_addr_label4instruction)
    return either_ores_or_next







class Instruction4flow4LLoo__switch(_IInstruction4flow4LLoo__no_ref):
    def __init__(sf, nm4case6ctx, ls4either_rel_or_nm, /):
        check_type_le(Hashable, nm4case6ctx)
        ls4either_rel_or_nm = mk_tuple(ls4either_rel_or_nm)
        for either_rel_or_nm in ls4either_rel_or_nm:
            _check__either_rel_or_nm(either_rel_or_nm)

        sf._k = nm4case6ctx
        sf._xs = ls4either_rel_or_nm
        _Base4repr.__init__(sf, nm4case6ctx, ls4either_rel_or_nm)

    @override
    def mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(sf, ctx, inputter, /):
        'ctx/dict -> inputter.fork() -> child_rgnr/IRecognizerLLoo # [inplace update ctx/dict]' ' #assume[inputter contains global runtime info...]'
        return recognizer_LLoo__ignore
    @override
    def mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(sf, idx4instruction, child_rgnr, ctx, oresult4child, inputter, /):
        'idx4instruction/uint -> child_rgnr/IRecognizerLLoo -> ctx/dict -> oresult4child -> inputter.fork() -> Either<oresult4return,next_addr_label4instruction> # [inplace update ctx/dict] #[addr_label :: (int|label)]'
        nm4case6ctx = sf._k
        ls4either_rel_or_nm = sf._xs
        case4switch = ctx[nm4case6ctx]
        either_rel_or_nm = ls4either_rel_or_nm[case4switch]
        either_ores_or_next = _mk__either_ores_or_next__5__either_rel_or_nm(idx4instruction, either_rel_or_nm)
        return either_ores_or_next
check_non_ABC(Instruction4flow4LLoo__switch)















class ICtxUpdater__5oresult(IDependentTreeNode):
    __slots__ = ()
    @abstractmethod
    def inplace_update_ctx5oresult(sf, ctx, oresult4child, /):
        'ctx/dict -> oresult<child_rgnr> -> None'
class Instruction4flow4LLoo__mkr4rgnr7ctx(IInstruction4flow4LLoo, _Base4repr):
    'using:IMaker4RecognizerLLoo__5ctx,ICtxUpdater__5oresult'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr_or_mkr4rgnr7ctx, ctx_updater7oresult, /):
        mkr4rgnr7ctx = rgnr_or2mkr4rgnr7ctx(rgnr_or_mkr4rgnr7ctx)
        check_type_le(ICtxUpdater__5oresult, ctx_updater7oresult)
        sf._mkr = mkr4rgnr7ctx
        sf._upt = ctx_updater7oresult
        _Base4repr.__init__(sf, rgnr_or_mkr4rgnr7ctx, ctx_updater7oresult)

    @override
    def mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(sf, ctx, inputter, /):
        'ctx/dict -> inputter.fork() -> child_rgnr/IRecognizerLLoo # [inplace update ctx/dict]' ' #assume[inputter contains global runtime info...]'
        mkr4rgnr7ctx = sf._mkr
        ctx_view = MapView(ctx)
        rgnr = mkr4rgnr7ctx.mk_recognizer_LLoo5ctx(ctx_view, inputter)
        return rgnr
    @override
    def mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(sf, idx4instruction, child_rgnr, ctx, oresult4child, inputter, /):
        'idx4instruction/uint -> child_rgnr/IRecognizerLLoo -> ctx/dict -> oresult4child -> inputter.fork() -> Either<oresult4return,next_addr_label4instruction> # [inplace update ctx/dict] #[addr_label :: (int|label)]'
        ctx_updater7oresult = sf._upt
        ctx_updater7oresult.inplace_update_ctx5oresult(ctx, oresult4child)
        either_ores_or_next = _mk__either_ores_or_next__5__idx4instruction__plus1(idx4instruction)
        return either_ores_or_next
    @override
    def is_instruction4hdr_sgnl(sf, /):
        '-> bool'
        return False
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        mkr4rgnr7ctx = sf._mkr
        yield mkr4rgnr7ctx
        ctx_updater7oresult = sf._upt
        yield ctx_updater7oresult
        return

check_non_ABC(Instruction4flow4LLoo__mkr4rgnr7ctx)










class _ICtxUpdater__5oresult__no_ref(ICtxUpdater__5oresult, _Base4repr):
    __slots__ = ()
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        return null_iter
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        return null_iter









class CtxUpdater__5oresult__assign_nm6ctx(_ICtxUpdater__5oresult__no_ref):
    ___no_slots_ok___ = True
    def __init__(sf, nm6ctx, /):
        check_type_le(Hashable, nm6ctx)
        sf._k = nm6ctx
        _Base4repr.__init__(sf, nm6ctx)
    @override
    def inplace_update_ctx5oresult(sf, ctx, oresult4child, /):
        'ctx/dict -> oresult<child_rgnr> -> None'
        nm6ctx = sf._k
        ctx[nm6ctx] = oresult4child
        return
check_non_ABC(CtxUpdater__5oresult__assign_nm6ctx)








class CtxUpdater__5oresult__assign_nms6ctx(_ICtxUpdater__5oresult__no_ref):
    ___no_slots_ok___ = True
    def __init__(sf, nms6ctx, /):
        nms6ctx = mk_tuple(nms6ctx)
        for nm6ctx in nms6ctx:
            check_type_le(Hashable, nm6ctx)
        sf._ks = nms6ctx
        _Base4repr.__init__(sf, nms6ctx)
    @override
    def inplace_update_ctx5oresult(sf, ctx, oresult4child, /):
        'ctx/dict -> oresult<child_rgnr> -> None'
        nms6ctx = sf._ks
        vs = mk_tuple(oresult4child)
        if not len(nms6ctx) == len(vs):raise TypeError((len(nms6ctx), len(vs)))
        for nm6ctx, v in zip(nms6ctx, vs):
            ctx[nm6ctx] = v
        return
check_non_ABC(CtxUpdater__5oresult__assign_nms6ctx)











class CtxUpdater__5oresult__no_update(_ICtxUpdater__5oresult__no_ref):
    ___no_slots_ok___ = True
    def __init__(sf, /):
        _Base4repr.__init__(sf)
    @override
    def inplace_update_ctx5oresult(sf, ctx, oresult4child, /):
        'ctx/dict -> oresult<child_rgnr> -> None'
        return
check_non_ABC(CtxUpdater__5oresult__no_update)
no_op_updater = CtxUpdater__5oresult__no_update()









class Instruction4flow4LLoo__del_nms6ctx(_IInstruction4flow4LLoo__no_ref):
    ___no_slots_ok___ = True
    def __init__(sf, nms6ctx, /):
        nms6ctx = mk_tuple(nms6ctx)
        for nm6ctx in nms6ctx:
            check_type_le(Hashable, nm6ctx)
        sf._ks = nms6ctx
        _Base4repr.__init__(sf, nms6ctx)

    @override
    def mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(sf, ctx, inputter, /):
        'ctx/dict -> inputter.fork() -> child_rgnr/IRecognizerLLoo # [inplace update ctx/dict]' ' #assume[inputter contains global runtime info...]'
        return recognizer_LLoo__ignore

    @override
    def mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(sf, idx4instruction, child_rgnr, ctx, oresult4child, inputter, /):
        'idx4instruction/uint -> child_rgnr/IRecognizerLLoo -> ctx/dict -> oresult4child -> inputter.fork() -> Either<oresult4return,next_addr_label4instruction> # [inplace update ctx/dict] #[addr_label :: (int|label)]'
        nms6ctx = sf._ks
        for nm6ctx in nms6ctx:
            del ctx[nm6ctx]
        either_ores_or_next = _mk__either_ores_or_next__5__idx4instruction__plus1(idx4instruction)
        return either_ores_or_next
check_non_ABC(Instruction4flow4LLoo__del_nms6ctx)













def _compile(src_or_code, /, *, fname='<IInstruction4flow4LLoo-ICtxUpdater__5oresult>'):
    '(str|bytes|AST|code) -> code'
    if type(src_or_code) is CodeType:
        code = src_or_code
    else:
        src = src_or_code
        code = compile(src, fname, 'exec')
    code
    return code



class Instruction4flow4LLoo__exec(IInstruction4flow4LLoo, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, src_or_code, may_globals, used_kinded_names, used_dependent_tree_nodes, /):
        ######################
        used_kinded_names = mk_tuple(used_kinded_names)
        used_dependent_tree_nodes = mk_tuple(used_dependent_tree_nodes)
        ######################
        for kinded_name in used_kinded_names:
            check_type_le(Hashable, kinded_name)
        for dependent_tree_node in used_dependent_tree_nodes:
            check_type_le(IDependentTreeNode, dependent_tree_node)
        ######################
        globals = {} if None is may_globals else may_globals
        check_type_is(dict, globals)
        ######################
        code = _compile(src_or_code)
        ######################
        sf._c = code
        sf._g = globals
        sf._knms = used_kinded_names
        sf._nds = used_dependent_tree_nodes
        _Base4repr.__init__(sf, src_or_code, may_globals, used_kinded_names, used_dependent_tree_nodes)

    @override
    def mk_child_recognizer_ex4flow4LLoo__and__inplace_update_ctx(sf, ctx, inputter, /):
        'ctx/dict -> inputter.fork() -> child_rgnr/IRecognizerLLoo # [inplace update ctx/dict]' ' #assume[inputter contains global runtime info...]'
        return recognizer_LLoo__ignore

    @override
    def mk_either_oresult4return_or_next_addr_label4instruction__and__inplace_update_ctx(sf, idx4instruction, child_rgnr, ctx, oresult4child, inputter, /):
        'idx4instruction/uint -> child_rgnr/IRecognizerLLoo -> ctx/dict -> oresult4child -> inputter.fork() -> Either<oresult4return,next_addr_label4instruction> # [inplace update ctx/dict] #[addr_label :: (int|label)]'
        globals = sf._g
        code = sf._c
        exec(code, globals, ctx)
        either_ores_or_next = _mk__either_ores_or_next__5__idx4instruction__plus1(idx4instruction)
        return either_ores_or_next
    @override
    def is_instruction4hdr_sgnl(sf, /):
        '-> bool'
        return False
    @override
    def _iter_directly_used_kinded_names_(sf, /):
        '-> Iter knm/kinded_name'
        used_kinded_names = sf._knms
        return iter(used_kinded_names)
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        used_dependent_tree_nodes = sf._nds
        return iter(used_dependent_tree_nodes)
check_non_ABC(Instruction4flow4LLoo__exec)

















def mk_LLoo__flow(instructions, may__label2idx4instruction, /):
    r'[IInstruction4flow4LLoo]{len==L} -> may {label/(Hashable\-\int):uint%L} -> IRecognizerLLoo'
    label2idx4instruction = null_mapping_view if None is may__label2idx4instruction else may__label2idx4instruction
    return RecognizerLLoo__flow(instructions, label2idx4instruction)






__all__
from seed.recognize.recognizer_LLoo_.combinator_LLoo__flow import mk_LLoo__flow
from seed.recognize.recognizer_LLoo_.combinator_LLoo__flow import (mk_LLoo__flow
,IRecognizerLLoo__flow
,    IRecognizerLLoo__flow__using_containers4instructions
,        RecognizerLLoo__flow
#
,IInstruction4flow4LLoo
,    Instruction4flow4LLoo__wrapper
,        Instruction4flow4LLoo__hdr_sgnl
,    Instruction4flow4LLoo__return
,    Instruction4flow4LLoo__goto
,    Instruction4flow4LLoo__switch
#
,    Instruction4flow4LLoo__exec
,    Instruction4flow4LLoo__del_nms6ctx
,    Instruction4flow4LLoo__mkr4rgnr7ctx
,        ICtxUpdater__5oresult
#
,ICtxUpdater__5oresult
,    CtxUpdater__5oresult__assign_nm6ctx
,    CtxUpdater__5oresult__assign_nms6ctx
,    CtxUpdater__5oresult__no_update
,        no_op_updater
)
from seed.recognize.recognizer_LLoo_.combinator_LLoo__flow import *
