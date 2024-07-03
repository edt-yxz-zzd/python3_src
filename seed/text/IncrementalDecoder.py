#__all__:goto
r'''[[[
e ../../python3_src/seed/text/IncrementalDecoder.py
view ../../python3_src/seed/types/StreamPosition.py
    AutoPruneStream
vs:
    view ../../python3_src/seed/text/IncrementalDecoder.py
    view ../../python3_src/seed/text/StepDecoder.py


seed.text.IncrementalDecoder
py -m nn_ns.app.debug_cmd   seed.text.IncrementalDecoder -x
py -m nn_ns.app.doctest_cmd seed.text.IncrementalDecoder:__doc__ -ht
py_adhoc_call   seed.text.IncrementalDecoder   @f


#]]]'''
__all__ = r'''
Error
    DecodeFail
        DecodeFail__feed_with_final_state
        DecodeFail__non_accepted_when_stop

IncrementalDecoderState
IIncrementalDecoder
    IncrementalDecoder5IIncrementalDecoderOps
    IncrementalDecoder5encoding

IIncrementalDecoderOps
    IncrementalDecoderOps5IIncrementalDecoder

'''.split()#'''
__all__
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_may_, check_int_ge_le
from seed.types.LazyList import LazyList# LazyListError

import codecs
    #codecs.getincrementaldecoder(encoding)->codecs.IncrementalDecoder
#class codecs.IncrementalDecoder
#    decode(object[, final])
#    reset()
#    getstate()->(buffered_input, additional_state_info)
#    setstate(state)

class Error(Exception):pass
class DecodeFail(Error):pass
class DecodeFail__feed_with_final_state(DecodeFail):pass
class DecodeFail__non_accepted_when_stop(DecodeFail):pass

class IIncrementalDecoder(ABC):
    r'''[[[
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.text.IncrementalDecoder:IIncrementalDecoder@T    =T    +exclude_attrs5listed_in_cls_doc
new_abstract_methods:
    `begin_position
    `end_position
    `get_state
    `set_state
    `reset
    `accepted
    `final
    `feed
    `detect
new_concrete_methods:
    reset_then_decode__ifile
    reset_then_decode
    reset_then_decode1

    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def begin_position(sf, /):
        '-> begin_position'
    @property
    @abstractmethod
    def end_position(sf, /):
        '-> end_position'
    @abstractmethod
    def get_state(sf, /):
        '-> st'
    @abstractmethod
    def set_state(sf, st, /):
        '-> None'
    @abstractmethod
    def reset(sf, begin_position, /):
        '-> None'
    @property
    @abstractmethod
    def accepted(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def final(sf, /):
        '-> bool'
    @abstractmethod
    def feed(sf, x, post_position, /):
        '-> None|^DecodeFail__feed_with_final_state'
    @abstractmethod
    def detect(sf, /, *, eof):
        '-> emay (is_ok, (err_msg|(result, accepted_end_position, accepted_st))) # [[not eof][not final] <==> [return ...]] # [MAYBE [accepted_end_position{result} is not sf.end_position]]'
    def reset_then_decode__ifile(sf, ifile, /):
        ''
        def __(ifile, /):
            while 1:
                s = ifile.read(1)
                if not s:
                    break
                yield s, ifile.tell()
        sf.reset(ifile.tell())
        st = sf.get_state()
        return sf.reset_then_decode(st, 0, *__(ifile), to_finalize=True)
    def reset_then_decode(sf, st, offset, pairs, /, *, to_finalize=False, imay_accepted_end=-1):
        '-> Iter (emay_ok, ???)/Iter ((False,((st, offset, pairs, imay_accepted_end), (end, err_msg, end_position, end_st, eof)))|(True,(result, accepted_end, accepted_end_position, accepted_st, tail, end, end_position, end_st, eof))|(...,(st:=end_st, offset:=end, imay_accepted_end, end_position))) # [[emay_ok is ...] <==> [[eof][not to_finalize]]] # [[emay_ok{@j} is not True] <==> [emay_ok{@j} is the last one]]'
        #see:reset_then_decode
        #see:reset_then_decode1
        #see:decode1
        #see:decode
        #
        #
        check_int_ge(0, offset)
        #xxx:pairs = LazyList(iter(pairs))
        check_type_is(LazyList, pairs)
        def _is_st0(sf, /):
            begin_position = sf.begin_position
            end_st = sf.get_state()
            sf.reset(begin_position)
            st0 = sf.get_state()
            sf.set_state(end_st)
            return end_st==st0
        #while pairs.is_empty__hardwork():
        while 1:
            (emay_ok, xx) = sf.reset_then_decode1(st, offset, pairs, to_finalize=to_finalize, imay_accepted_end=imay_accepted_end)
            end_position = sf.end_position
            if emay_ok is ...:
                #eof and not to_finalize
                eof = True
                assert not to_finalize
                break
            elif emay_ok is False:
                #err or to_finalize
                (end, err_msg, eof) = xx
                if (eof and to_finalize) and offset == end and imay_accepted_end==-1 and _is_st0(sf):
                    #complete
                    return
                yield (emay_ok, ((st, offset, pairs, imay_accepted_end), (end, err_msg, end_position, end_st, eof)))
                return
            elif emay_ok is True:
                #ok # to_finalize
                (accepted_end, result, accepted_end_position, accepted_st, end, eof) = xx
                sz = accepted_end -offset
                (zs, tail) = pairs.extract_prefix_with_tail__le(sz, relax=True)
                assert len(zs) == sz
                pairs = tail
                yield (emay_ok, (result, accepted_end, accepted_end_position, accepted_st, tail, end, end_position, end_st, eof))
                #pairs = tail
                sf.reset(end_position)
                st = sf.get_state()
                offset = accepted_end
                imay_accepted_end = -1
                continue
            raise 000
        #eof and not to_finalize
        (imay_accepted_end, end) = xx
        if offset == end and imay_accepted_end==-1 and _is_st0(sf):
            # complete
            return
        # incomplete
        end_st = sf.get_state()
        #begin_position = sf.begin_position
        end_position
        #yield (emay_ok, ((st, offset, pairs), (imay_accepted_end, end, end_position, end_st)))
        yield (emay_ok, (st:=end_st, offset:=end, imay_accepted_end, end_position))
        return

    def reset_then_decode1(sf, st, offset, pairs, /, *, to_finalize=False, imay_accepted_end=-1):
        '-> (emay_ok, ???)/((False, (end, err_msg, eof))|(True, (accepted_end, result, accepted_end_position, accepted_st, end, eof))|(..., (imay_accepted_end, end))) # [[emay_ok is ...] <==> [[eof][not to_finalize]]]'
        #see:reset_then_decode
        #see:reset_then_decode1
        #see:decode1
        #see:decode
        #
        #
        #sf.reset(begin_position)
        sf.set_state(st)
        check_type_is(bool, to_finalize)
        check_int_ge(0, offset)
        if 0:
            imay_accepted_end = -1
            #may_accepted_st = None
        else:
            check_int_ge(-1, imay_accepted_end)
            check_int_ge_le(-1, offset, imay_accepted_end)
            #if not (imay_accepted_end==offset) is (may_accepted_st == st):raise 000
            #if not (imay_accepted_end==-1) is (may_accepted_st is None):raise 000
        it = enumerate(pairs:=iter(pairs), offset+1)
        eof = False
        end = offset
        while 1:
            if sf.accepted:
                imay_accepted_end = end
                #may_accepted_st = sf.get_state()
            if sf.final:
                # [final_st]
                # [not eof]
                break
            # [nonfinal_st]
            for end, (x, post_position) in it:
                sf.feed(x, post_position)
                break
            else:
                # [nonfinal_st]
                # [eof]
                eof = True
                break
        assert eof is (not sf.final)
        # [[[not eof][final_st]]xor[[eof][nonfinal_st]]]
        end
        imay_accepted_end
        #may_accepted_st
        eof
        #sf
        end_st = sf.get_state()
        end_position = sf.end_position
        if eof:
            nonfinal_st = end_st
            if to_finalize:
                pseudo_final_st = nonfinal_st
        else:
            final_st = end_st
            pseudo_final_st = final_st

        if eof and not to_finalize:
            #nonfinal_st = end_st
            #return (emay_ok:=..., (imay_accepted_end, nonfinal_st, end_position, end))
            return (emay_ok:=..., (imay_accepted_end, end))
        # [[not eof]or[to_finalize]]
        # !! [[[not eof][final_st]]xor[[eof][nonfinal_st]]]
        # [[[not eof][final_st]]xor[[eof][nonfinal_st][to_finalize]]]
        # [[final_st]xor[[eof][to_finalize]]]
        pseudo_final_st

        if not imay_accepted_end >= 0:
            non_accepted_st = pseudo_final_st
            if sf.accepted:raise 000
        else:
            #xxx:if not sf.accepted:raise 000
            accepted_end = imay_accepted_end

        gl_eof = eof and to_finalize
        assert gl_eof is (not sf.final)
        em = sf.detect(eof=gl_eof)
            # !! [[final_st]xor[[eof][to_finalize]]]
            # [[final_st]xor[gl_eof]]
            # !! detect():[[not eof:=gl_eof][not final]] <==> [return ...]]
            # [not$ [detect():return ...]]
        if em is ...:raise 000
        (is_ok, xx) = em
        if is_ok:
            (result, accepted_end_position, accepted_st) = xx
            #return (emay_ok:=True, (accepted_end, result, accepted_end_position, accepted_st, pseudo_final_st, end_position, end, eof))
            return (emay_ok:=True, (accepted_end, result, accepted_end_position, accepted_st, end, eof))
        else:
            err_msg = xx
            #return (emay_ok:=False, (pseudo_final_st, end_position, end, err_msg, eof))
            return (emay_ok:=False, (end, err_msg, eof))



#end-class IIncrementalDecoder(ABC):

class IIncrementalDecoderOps(ABC):
    r'''[[[
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.text.IncrementalDecoder:IIncrementalDecoderOps@T    =T      +exclude_attrs5listed_in_cls_doc
new_abstract_methods:
    `initial_state
    `is_accepted_state
    `is_final_state
    `feed__nonfinal
    `non_accepted_state2err_msg
    `accepted_state2result
new_concrete_methods:
    decode
    decode1

    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def initial_state(ops, /):
        '-> st'
    @abstractmethod
    def is_accepted_state(ops, st, /):
        '-> bool'
    @abstractmethod
    def is_final_state(ops, st, /):
        '-> bool'
    @abstractmethod
    def feed__nonfinal(ops, nonfinal_st, x, /):
        '-> st'
    @abstractmethod
    def non_accepted_state2err_msg(ops, non_accepted_st, /):
        '-> err_msg'
    @abstractmethod
    def accepted_state2result(ops, accepted_st, /):
        '-> result'
    def decode(ops, st, offset, xs, /, *, to_finalize=False, imay_accepted_end=-1, may_accepted_st=None):
        '-> Iter (emay_ok, ???)/Iter ((False,((st, offset, xs, imay_accepted_end, may_accepted_st),(pseudo_final_st, end, err_msg, eof)))|(True,(result, accepted_end, accepted_st, tail, pseudo_final_st, end, eof))|(...,(st:=nonfinal_st, offset:=end, imay_accepted_end, may_accepted_st))) # [[emay_ok is ...] <==> [[eof][not to_finalize]]] # [[emay_ok{@j} is not True] <==> [emay_ok{@j} is the last one]]'
        #see:reset_then_decode
        #see:reset_then_decode1
        #see:decode1
        #see:decode
        #
        #
        check_int_ge(0, offset)
        #xxx:xs = LazyList(iter(xs))
        check_type_is(LazyList, xs)
        #while xs.is_empty__hardwork():
        while 1:
            (emay_ok, xx) = ops.decode1(st, offset, xs, to_finalize=to_finalize, imay_accepted_end=imay_accepted_end, may_accepted_st=may_accepted_st)
            if emay_ok is ...:
                #eof and not to_finalize
                eof = True
                assert not to_finalize
                break
            elif emay_ok is False:
                #err or to_finalize
                (pseudo_final_st, end, err_msg, eof) = xx
                if (eof and to_finalize) and offset == end and imay_accepted_end==-1 and nonfinal_st==ops.initial_state:
                    #complete
                    return
                yield (emay_ok, ((st, offset, xs, imay_accepted_end, may_accepted_st), xx))
                return
            elif emay_ok is True:
                #ok # to_finalize
                (result, accepted_end, accepted_st, pseudo_final_st, end, eof) = xx
                sz = accepted_end -offset
                (zs, tail) = xs.extract_prefix_with_tail__le(sz, relax=True)
                assert len(zs) == sz
                xs = tail
                yield (emay_ok, (result, accepted_end, accepted_st, tail, pseudo_final_st, end, eof))
                #xs = tail
                st = ops.initial_state
                offset = accepted_end
                imay_accepted_end = -1
                may_accepted_st = None
                continue
            raise 000
        #eof and not to_finalize
        (imay_accepted_end, may_accepted_st, nonfinal_st, end) = xx
        if offset == end and imay_accepted_end==-1 and nonfinal_st==ops.initial_state:
            # complete
            return
        # incomplete
        #yield (emay_ok, ((st, offset, xs), xx))
        yield (emay_ok, (st:=nonfinal_st, offset:=end, imay_accepted_end, may_accepted_st))
        return
    def decode1(ops, st, offset, xs, /, *, to_finalize=False, imay_accepted_end=-1, may_accepted_st=None):
        '-> (emay_ok, ???)/((False,(pseudo_final_st, end, err_msg, eof))|(True,(result, accepted_end, accepted_st, pseudo_final_st, end, eof))|(...,(imay_accepted_end, may_accepted_st, nonfinal_st, end))) # [[emay_ok is ...] <==> [[eof][not to_finalize]]]'
        #see:reset_then_decode
        #see:reset_then_decode1
        #see:decode1
        #see:decode
        #
        #
        #check_type_is(LazyList, xs)
        check_type_is(bool, to_finalize)
        check_int_ge(0, offset)
        if 0:
            imay_accepted_end = -1
            may_accepted_st = None
        else:
            check_int_ge(-1, imay_accepted_end)
            check_int_ge_le(-1, offset, imay_accepted_end)
            if not (imay_accepted_end==offset) is (may_accepted_st == st):raise 000
            if not (imay_accepted_end==-1) is (may_accepted_st is None):raise 000
        it = enumerate(xs:=iter(xs), offset+1)
        eof = False
        end = offset
        while 1:
            if ops.is_accepted_state(st):
                imay_accepted_end = end
                may_accepted_st = st
            if ops.is_final_state(st):
                # [final_st]
                # [not eof]
                break
            # [nonfinal_st]
            for end, x in it:
                st = ops.feed__nonfinal(st, x)
                break
            else:
                # [nonfinal_st]
                # [eof]
                eof = True
                break
        assert eof is (not ops.is_final_state(st))
        imay_accepted_end
        may_accepted_st
        end
        eof
        st
        if eof:
            nonfinal_st = st
            if to_finalize:
                pseudo_final_st = nonfinal_st
        else:
            final_st = st
            pseudo_final_st = final_st

        if eof and not to_finalize:
            #nonfinal_st = st
            return (emay_ok:=..., (imay_accepted_end, may_accepted_st, nonfinal_st, end))
        # [[not eof]or[to_finalize]]
        pseudo_final_st

        if not imay_accepted_end >= 0:
            err_msg = ops.non_accepted_state2err_msg(non_accepted_st:=pseudo_final_st)
            return (emay_ok:=False, (pseudo_final_st, end, err_msg, eof))

        accepted_end = imay_accepted_end
        accepted_st = may_accepted_st
        result = ops.accepted_state2result(accepted_st)
        return (emay_ok:=True, (result, accepted_end, accepted_st, pseudo_final_st, end, eof))
#end-class IIncrementalDecoderOps(ABC):

class IncrementalDecoderState:
    def __init__(sf, begin_position, state4ops, end_position, may_prev_accepted_state, accepted, /):
        check_type_is(bool, accepted)
        check_may_([check_type_is, IncrementalDecoderState], may_prev_accepted_state)
        if accepted:
            may_prev_accepted_state = None
                #break-chain=>auto-prune:see:AutoPruneStream
        sf._args = (begin_position, state4ops, end_position, may_prev_accepted_state, accepted)

    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not type(ot) is type(sf):
            #if not isinstance(ot, type(sf)):
            return NotImplemented
        return sf.args == ot.args
    @property
    def args(sf, /):
        return sf._args
    @property
    def begin_position(sf, /):
        return sf._args[0]
    @property
    def state4ops(sf, /):
        return sf._args[1]
    @property
    def end_position(sf, /):
        return sf._args[2]
    @property
    def may_prev_accepted_state(sf, /):
        return sf._args[3]
    @property
    def may_prev_accepted_state4next(sf, /):
        m = sf.may_prev_accepted_state
        if sf.accepted:
            if not m is None:raise 000
            m = sf
        if not m is None:
            if not m.may_prev_accepted_state is None:raise 000
        return m
    @property
    def accepted(sf, /):
        '-> bool'
        return sf._args[4]
    def mk_next_state(sf, new_st4ops, post_position, accepted, /):
        m = None if accepted else sf.may_prev_accepted_state4next
        return type(sf)(sf.begin_position, new_st4ops, post_position, m, accepted)

#end-class IncrementalDecoderState:
class IncrementalDecoder5IIncrementalDecoderOps(IIncrementalDecoder):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf.incremental_decoder_ops, sf.begin_position)
    def __init__(sf, ops, begin_position, /):
        check_type_le(IIncrementalDecoderOps, ops)
        sf._ops = ops
        sf.reset(begin_position)
        sf._st
        sf._st4ops
    @property
    def incremental_decoder_ops(sf, /):
        return sf._ops
    @property
    def _st4ops(sf, /):
        return sf._st.state4ops
    ######################
    ######################
    ######################
    @property
    @override
    def begin_position(sf, /):
        '-> begin_position'
        return sf._st.begin_position
    @property
    @override
    def end_position(sf, /):
        '-> end_position'
        return sf._st.end_position
    @override
    def get_state(sf, /):
        '-> st'
        return sf._st
    @override
    def set_state(sf, st, /):
        '-> None'
        check_type_is(IncrementalDecoderState, st)
        sf._st = st
    @override
    def reset(sf, begin_position, /):
        '-> None'
        ops = sf._ops
        st4ops = ops.initial_state
        accepted = ops.is_accepted_state(st4ops)
        sf._st = IncrementalDecoderState(begin_position, st4ops, begin_position, None, accepted)
    @property
    @override
    def accepted(sf, /):
        '-> bool'
        st4ops = sf._st4ops
        return st4ops.accepted
        ops = sf._ops
        st4ops = sf._st4ops
        return ops.is_accepted_state(st4ops)

    @property
    @override
    def final(sf, /):
        '-> bool'
        ops = sf._ops
        st4ops = sf._st4ops
        return ops.is_final_state(st4ops)

    @override
    def feed(sf, x, post_position, /):
        '-> None|^DecodeFail__feed_with_final_state'
        ops = sf._ops
        st4ops = sf._st4ops
        if ops.is_final_state(st4ops):
            raise DecodeFail__feed_with_final_state(ops, st4ops)
        nonfinal_st4ops = st4ops
        new_st4ops = ops.feed__nonfinal(nonfinal_st4ops, x)

        sf._st = sf._st.mk_next_state(new_st4ops, post_position, ops.is_accepted_state(new_st4ops))
        return None
    @override
    def detect(sf, /, *, eof):
        '-> emay (is_ok, (err_msg|(result, accepted_end_position, accepted_st))) # [[not eof][not final] <==> [return ...]] # [MAYBE [accepted_end_position{result} is not sf.end_position]]'
        check_type_is(bool, eof)
        ops = sf._ops
        st4ops = sf._st4ops
        if not (eof or ops.is_final_state(st4ops)):
            # [nonfinal][not eof]
            return ...
        # [[final]or[eof]]
        st = sf._st
        m = st.may_prev_accepted_state4next
        if m is None:
            # [[final]or[eof]][no accepted]
            non_accepted_st4ops = st4ops
            err_msg = ops.non_accepted_state2err_msg(non_accepted_st4ops)
            return (is_ok:=False, err_msg)
            raise DecodeFail__non_accepted_when_stop(err_msg)
        # [[final]or[eof]][had accepted]
        accepted_st = m
        accepted_st4ops = accepted_st.state4ops
        result = ops.accepted_state2result(accepted_st4ops)
        return (is_ok:=True, (result, accepted_end_position:=accepted_st.end_position, accepted_st))
        return (result, accepted_st.end_position)

#end-class IncrementalDecoder5IIncrementalDecoderOps(IIncrementalDecoder):

class IncrementalDecoderOps5IIncrementalDecoder(IIncrementalDecoderOps):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        #return repr_helper(sf, sf._may_mk_next, sf.incremental_decoder)
        return repr_helper(sf, sf.incremental_decoder)
    def __init__(sf, incremental_decoder, /):
        #def __init__(sf, may_mk_next_position, incremental_decoder, /):
        check_type_le(IIncrementalDecoder, incremental_decoder)
        sf._dcdr = incremental_decoder
        #sf._may_mk_next = may_mk_next_position
    @property
    def incremental_decoder(sf, /):
        return sf._dcdr
    ######################
    ######################
    ######################
    @property
    @override
    def initial_state(ops, /):
        '-> st'
        dcdr = ops._dcdr
        dcdr.reset(dcdr.begin_position)
        return dcdr.get_state()
    @override
    def is_accepted_state(ops, st, /):
        '-> bool'
        dcdr = ops._dcdr
        dcdr.set_state(st)
        return dcdr.accepted
    @override
    def is_final_state(ops, st, /):
        '-> bool'
        dcdr = ops._dcdr
        dcdr.set_state(st)
        return dcdr.final
    @override
    def feed__nonfinal(ops, nonfinal_st, big_x, /):
        '-> st'
        dcdr = ops._dcdr
        dcdr.set_state(nonfinal_st)
        if dcdr.final:raise 000
        #dcdr.feed(x, post_position:=ops._may_mk_next(dcdr.end_position))
        (x, post_position) = big_x
        dcdr.feed(x, post_position)
        return dcdr.get_state()
    @override
    def non_accepted_state2err_msg(ops, non_accepted_st, /):
        '-> err_msg'
        dcdr = ops._dcdr
        dcdr.set_state(non_accepted_st)
        if dcdr.accepted:raise 000
        (is_ok, either) = dcdr.detect(eof=True)
        if is_ok:raise 000
        err_msg = either
        return err_msg
    @override
    def accepted_state2result(ops, accepted_st, /):
        '-> result'
        dcdr = ops._dcdr
        dcdr.set_state(accepted_st)
        if not dcdr.accepted:raise 000
        (is_ok, either) = dcdr.detect(eof=True)
        if not is_ok:raise 000
        big_result = (result, accepted_end_position, accepted_st) = either
        return big_result
        assert accepted_end_position == dcdr.end_position
        return result


#end-class IncrementalDecoderOps5IIncrementalDecoder(IIncrementalDecoderOps):


def _find_input_kinds(std_dcdr, /):
    (buffered_input, additional_state_info) = std_dcdr.get_state()
    s = buffered_input[:0]
    return [s]
    ...
    ss = [b'', '']
    ss = [s for s in ss if _try_input(std_dcdr, s)]
    return ss
def _try_input(std_dcdr, s, /):
    st4std = std_dcdr.getstate()
    try:
        std_dcdr.decode(s, final=True)
    except ValueError:
        r = True
    except TypeError:
        r = False
    else:
        r = True
    std_dcdr.setstate(st4std)
    return r
def _is_accepted(sf, /):
    'precondition:[nonempty-input]'
    #(buffered_input, additional_state_info) = std_dcdr.get_state()
    #return not buffered_input
    #...
    s = sf._empty
    std_dcdr = sf._std_dcdr
    st4std = std_dcdr.getstate()
    try:
        std_dcdr.decode(s, final=True)
    except ValueError:
        r = False
    else:
        r = True
    std_dcdr.setstate(st4std)
    return r
class IncrementalDecoder5encoding(IIncrementalDecoder):
    'encoding->py_codecs_IncrementalDecoder'
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf.encoding, sf.begin_position)
    def __init__(sf, encoding, begin_position, /):
        std_dcdr = sf._std_dcdr = codecs.getincrementaldecoder(encoding)
        ss = _find_input_kinds(std_dcdr)
        if not len(ss)==1: raise Exception(f'unknown input type:{encoding}')
        [sf._empty] = ss
        sf._encoding = encoding
        sf.reset(begin_position)
        sf._e_se_st
        sf._e_se
        sf._st
        sf._st4std
    @property
    def encoding(sf, /):
        return sf._encoding
    @property
    def py_codecs_incremental_decoder(sf, /):
        return sf._std_dcdr
    @property
    def _s(sf, /):
        (is_err, s_or_err_msg) = sf._e_se
        if is_err:raise 000
        s = s_or_err_msg
        return s
    @property
    def _e_se(sf, /):
        return sf._e_se_st[:2]
    @property
    def _st(sf, /):
        return sf._e_se_st[2]
    @property
    def _st4std(sf, /):
        return sf._st.state4ops
    ######################
    ######################
    ######################
    @property
    @override
    def begin_position(sf, /):
        '-> begin_position'
        return sf._st.begin_position
    @property
    @override
    def end_position(sf, /):
        '-> end_position'
        return sf._st.end_position
    @override
    def get_state(sf, /):
        '-> st'
        return sf._st
    @override
    def set_state(sf, st, /):
        '-> None'
        check_type_is(IncrementalDecoderState, st)
        sf._st = st
    @override
    def reset(sf, begin_position, /):
        '-> None'
        std_dcdr = sf._std_dcdr
        std_dcdr.reset()
        st4std = std_dcdr.getstate()
        #accepted = _is_accepted(sf)
        accepted = False#no_input
        s = sf._empty
            #=>final
        is_err = False
        s_or_err_msg = s
        sf._e_se_st = (is_err, s_or_err_msg, IncrementalDecoderState(begin_position, st4std, begin_position, None, accepted))
    @property
    @override
    def accepted(sf, /):
        '-> bool'
        st4std = sf._st4std
        return st4std.accepted
    @property
    @override
    def final(sf, /):
        '-> bool'
        (is_err, s_or_err_msg) = sf._e_se
        return is_err or bool(s:=s_or_err_msg)
        return sf.accepted

    @override
    def feed(sf, x, post_position, /):
        '-> None|^DecodeFail__feed_with_final_state'
        check_type_is(type(sf._empty), x)
        if not len(x) == 1:raise TypeError

        std_dcdr = sf._std_dcdr
        st4std = sf._st4std
        if sf.final:
            (is_err, s_or_err_msg) = sf._e_se
            raise DecodeFail__feed_with_final_state(sf.encoding, (is_err, s_or_err_msg))
            raise DecodeFail__feed_with_final_state(sf.encoding, st4std)
        try:
            s = std_dcdr.decode(x)
        except ValueError as e:
            err_msg = e.args
            e_se = (is_err:=True, err_msg)
        else:
            e_se = (is_err:=False, s)
        e_se
        new_st4std = std_dcdr.getstate()

        accepted = _is_accepted(new_st4std) # [nonempty-input]
        st = sf._st.mk_next_state(new_st4std, post_position, accepted)
        sf._e_se_st = (*e_se, st)
        return None
    @override
    def detect(sf, /, *, eof):
        '-> emay (is_ok, (err_msg|(result, accepted_end_position, accepted_st))) # [[not eof][not final] <==> [return ...]] # [MAYBE [accepted_end_position{result} is not sf.end_position]]'
        check_type_is(bool, eof)
        if not (eof or sf.final):
            # [nonfinal][not eof]
            return ...
        # [[final]or[eof]]
        if not sf.final:
            # [eof]
            assert eof
            std_dcdr = sf._std_dcdr
            try:
                s = std_dcdr.decode(sf._empty, final=True)
            except ValueError as e:
                err_msg = e.args
                e_se = (is_err:=True, err_msg)
            else:
                e_se = (is_err:=False, s)
            e_se
        else:
            # [final]
            e_se = sf._e_se
            e_se
        e_se
        (is_err, s_or_err_msg) = e_se
        if is_err:
            err_msg = s_or_err_msg
            return (is_ok:=False, err_msg)
        s = s_or_err_msg
        if not s:
            return (is_ok:=False, 'no-input')
        result = s
        accepted_st = sf.getstate()
        accepted_end_position = accepted_st.end_position
        return (is_ok:=True, (result, accepted_end_position, accepted_st))

#end-class IncrementalDecoder5encoding(IIncrementalDecoder):



__all__
from seed.text.IncrementalDecoder import DecodeFail
from seed.text.IncrementalDecoder import IIncrementalDecoder, IIncrementalDecoderOps
from seed.text.IncrementalDecoder import IncrementalDecoder5IIncrementalDecoderOps, IncrementalDecoder5encoding, IncrementalDecoderOps5IIncrementalDecoder

from seed.text.IncrementalDecoder import *
