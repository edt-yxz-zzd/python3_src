#__all__:goto
r'''[[[
e ../../python3_src/seed/types/StreamPosition.py
[[
vs:
    ===
    view ../../python3_src/seed/types/StreamPosition.py
        AutoPruneStream:
            +automatically-prune via StrongStreamPosition.__del__
            +random-access as-if array
                +manually-fill via "std::next()"
    ===
    view ../../python3_src/seed/types/PruneableArray.py
        PruneableArray:
            +manually-prune via ".prune_lt_()"
            +random-access as-if array
                +manually-fill via ".append()"
    ===
    view ../../python3_src/seed/types/CuttableStream.py
        CuttableStream:
            +manually-prune via ".cut__position()"
            +random-access as-if seekable file
                +automatically-fill via ".read()/.peek()"
    ===
    view ../../python3_src/seed/iters/PeekableIterator.py
        PeekableIterator:
            +manually-prune via "std::next()/.read_le()"
            +sequential-access via ".peek_le()"
                +automatically-fill via ".peek_le()"
    ===
    view ../../python3_src/seed/types/LazyList.py
        LazyList:
            +automatically-prune via default::__del__
            +sequential-access via "std::next()"
                +automatically-fill via "std::next()"
    ===
    view ../../python3_src/seed/types/LazySeq.py
        LazySeq:
            +no-prune!!!
            +random-access as-if array
                +automatically-fill via ".__getitem__()"
    ===
]]


[[
intent:
    to use in parsing/decoding
    auto prune stream
===
stream.next(pure_addr)->strong_addr
strong_addr.weak_addr.pure_addr
weak_addr.may_strong_addr
strong_addr.__del__:stream.prune_lt_(pure_addr)
    not readable: strong_addr.tmay_read()
            #stream.read
    underlying stream is invisible
    strong_addr._invisible_stream
]]


seed.types.StreamPosition
py -m nn_ns.app.debug_cmd   seed.types.StreamPosition -x
py -m nn_ns.app.doctest_cmd seed.types.StreamPosition:__doc__
py_adhoc_call   seed.types.StreamPosition   @f



>>> a0 = PureStreamPosition(0, None)
>>> stream = AutoPruneStream('ap_stream', a0, ((111*(i+1),None) for i in range(9)))
>>> p0 = stream.tell()
>>> w0 = p0.weak_stream_position
>>> p0
StrongStreamPosition(ap_stream, PureStreamPosition(0, None))
>>> repr(p0) == repr(StrongStreamPosition(stream, a0))
True
>>> p0 == StrongStreamPosition(stream, a0) # [unique=>["eq" === "is"]]
False
>>> w0 #doctest: +ELLIPSIS
<seed.types.StreamPosition.WeakStreamPosition object at 0x...>
>>> a0
PureStreamPosition(0, None)
>>> a0 is p0.pure_stream_position
True
>>> a0 is w0.pure_stream_position
True
>>> a0 is a0.pure_stream_position
True
>>> stream._ls
PruneableArray(0, [])
>>> x0, p1 = next(stream) #test:fill-packet...
>>> x1, p2 = next(stream)
>>> x2, p3 = next(stream)
>>> stream._ls #doctest: +ELLIPSIS
PruneableArray(0, [(<seed.types.StreamPosition.WeakStreamPosition object at 0x...>, 111), (<seed.types.StreamPosition.WeakStreamPosition object at 0x...>, 222), (<seed.types.StreamPosition.WeakStreamPosition object at 0x...>, 333)])
>>> p1
StrongStreamPosition(ap_stream, PureStreamPosition(1, None))
>>> p2
StrongStreamPosition(ap_stream, PureStreamPosition(2, None))
>>> p3
StrongStreamPosition(ap_stream, PureStreamPosition(3, None))
>>> x0
111
>>> x1
222
>>> x2
333
>>> p0 is stream.tell()
False
>>> p3 is stream.tell()
True
>>> p3 is stream.end_position
True
>>> p0 is stream.begin_position
True
>>> stream[p0:p3] #test:read-packet...
[111, 222, 333]
>>> stream[p1:p2]
[222]
>>> stream[p2:p2]
[]
>>> del p1, p2
>>> w0 is p0.weak_stream_position
True
>>> w0.may_strong_stream_position is p0
True
>>> len(stream._ls)
3
>>> del p0 #test:auto-prune...
>>> w0.may_strong_stream_position is None
True
>>> len(stream._ls)
0
>>> stream._ls
PruneableArray(3, [])
>>> p3 is stream.end_position
True


>>> stream.read_at_le(None, -1)
[]
>>> stream.read_le(3)
[444, 555, 666]
>>> p6 = stream.tell()
>>> stream.read_at_le(p3, 3)
[444, 555, 666]
>>> [_p3, p4, p5] = stream.read_at_le(p3, 3, position_only=True)
>>> _p3 is p3
True
>>> [p3, p4, p5, p6] == stream.read_at_le(p3, 3, position_only=True, with_end_position=True)
True

>>> [(p3, 444, p4), (p4, 555, p5), (p5, 666, p6)] == stream.read_at_le(p3, 3, with_prev_position=True, with_post_position=True)
True

>>> [(444, p4), (555, p5), (666, p6)] == stream.read_at_le(p3, 3, with_prev_position=False, with_post_position=True)
True
>>> [(p3, 444), (p4, 555), (p5, 666)] == stream.read_at_le(p3, 3, with_prev_position=True, with_post_position=False)
True
>>> stream.read_at_le(p3, 3, with_prev_position=False, with_post_position=False)
[444, 555, 666]



>>> [p3, p4, p5] == stream.gets_between__position_only(p3, p6, with_end_position=False)
True
>>> [p3, p4, p5, p6] == stream.gets_between__position_only(p3, p6, with_end_position=True)
True

>>> [(p3, 444, p4), (p4, 555, p5), (p5, 666, p6)] == stream.gets_between__with_prev_and_post_position(p3, p6)
True

>>> [(444, p4), (555, p5), (666, p6)] == stream.gets_between__with_post_position(p3, p6)
True
>>> [(p3, 444), (p4, 555), (p5, 666)] == stream.gets_between__with_prev_position(p3, p6)
True
>>> stream.gets_between__without_position(p3, p6)
[444, 555, 666]




#]]]'''
__all__ = r'''
AutoPruneStream

IBaseStreamPosition
    IPureStreamPosition
        PureStreamPosition
    IStrongStreamPosition
        StrongStreamPosition
    IWeakStreamPosition
        WeakStreamPosition
Error
    Error__deref

'''.split()#'''
__all__

import weakref
from itertools import islice
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_may_, check_smay_pseudo_qual_name
from seed.tiny import fst, snd, ifNone
from seed.types.PruneableArray import PruneableArray
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper

class Error(Exception):pass
class Error__deref(Error):pass

class IBaseStreamPosition(ABC):
    '[non_readable][unique=>["eq" === "is"]]'
    __slots__ = ()
    @property
    @abstractmethod
    def pure_stream_position(sf, /):
        '-> IPureStreamPosition/opaque_address'
    if 0:
        @property
        @abstractmethod
        def may_strong_stream_position(sf, /):
            '-> may IStrongStreamPosition'
        @property
        @abstractmethod
        def weak_stream_position(sf, /):
            '-> IWeakStreamPosition'
    if 0:
        def __eq__(sf, ot, /):
            '"eq" === "is"'
            return sf is ot
        __eq__ = object.__eq__
class IPureStreamPosition(IBaseStreamPosition):
    __slots__ = ()
    '[non_readable][opaque_address]'
    @property
    @abstractmethod
    def toplevel_stream_position4pruning(sf, /):
        '-> opaque_address'
    @property
    @override
    def pure_stream_position(sf, /):
        '-> IPureStreamPosition/opaque_address'
        return sf

class IStrongStreamPosition(IBaseStreamPosition):
    '[non_readable][unique=>["eq" === "is"]][key_to_auto_prune][stored_by_prev_position_and_external_user]'
    __slots__ = ()
    @property
    @abstractmethod
    def weak_stream_position(sf, /):
        '-> IWeakStreamPosition'

    @classmethod
    @abstractmethod
    def _prune_lt_(cls, underlying_stream, pure_stream_position, /):
        '-> None'
    @property
    @abstractmethod
    def _invisible_stream(sf, /):
        '-> invisible underlying_stream'
    @property
    @abstractmethod
    def _emay_next_strong_stream_position(sf, /):
        '-> emay next_strong_stream_position'
    @abstractmethod
    def _set_once__invisible_next_strong_stream_position(sf, next_strong_stream_position, /):
        '-> None'

    def __del__(sf, /):
        em = sf._emay_next_strong_stream_position
        if em is ...:
            return
        next_position = em
        sf = next_position
        type(sf)._prune_lt_(sf._invisible_stream, sf.pure_stream_position)
class IWeakStreamPosition(IBaseStreamPosition):
    '[non_readable][unique=>["eq" === "is"]][store__pure_stream_position]'
    __slots__ = ()
    @property
    @abstractmethod
    def may_strong_stream_position(sf, /):
        '-> may IStrongStreamPosition'
    @property
    def strong_stream_position_or_raise(sf, /):
        '-> IStrongStreamPosition|^Error__deref'
        m = sf.may_strong_stream_position
        if m is None:
            raise Error__deref(sf.pure_stream_position)
        return (strong_stream_position := m)






















class PureStreamPosition(IPureStreamPosition):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._top, sf._low)
    def __init__(sf, toplevel_stream_position4pruning, may_lowlevel_pure_stream_position, /):
        check_may_([check_type_le, IPureStreamPosition], may_lowlevel_pure_stream_position)
        sf._top = toplevel_stream_position4pruning
        sf._low = may_lowlevel_pure_stream_position
    @property
    @override
    def toplevel_stream_position4pruning(sf, /):
        '-> opaque_address'
        return sf._top
class StrongStreamPosition(IStrongStreamPosition):
    '[unique=>["eq" === "is"]][underlying_stream::eg:AutoPruneStream,PruneableArray.prune_lt_]'
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._strm, sf._addr)
    def __init__(sf, underlying_stream, pure_stream_position, /):
        sf._strm = underlying_stream
        sf._addr = pure_stream_position
        sf._wpst = WeakStreamPosition(sf)
        sf._nxt = ...
    @property
    @override
    def pure_stream_position(sf, /):
        '-> IPureStreamPosition/opaque_address'
        return sf._addr
    @property
    @override
    def weak_stream_position(sf, /):
        '-> IWeakStreamPosition'
        return sf._wpst
    @override
    def _set_once__invisible_next_strong_stream_position(sf, next_strong_stream_position, /):
        '-> None'
        check_type_le(IStrongStreamPosition, next_strong_stream_position)
        assert not sf is next_strong_stream_position
        if not sf._nxt is ...: raise 000
        sf._nxt = next_strong_stream_position
    @property
    @override
    def _emay_next_strong_stream_position(sf, /):
        '-> emay next_strong_stream_position'
        return sf._nxt

    @classmethod
    @override
    def _prune_lt_(cls, underlying_stream, pure_stream_position, /):
        '-> None'
        underlying_stream.prune_lt_(pure_stream_position.toplevel_stream_position4pruning)
    @property
    @override
    def _invisible_stream(sf, /):
        '-> invisible underlying_stream'
        return sf._strm


class WeakStreamPosition(IWeakStreamPosition):
    ___no_slots_ok___ = True
    if 0:
        def __repr__(sf, /):
            return repr_helper(sf, sf.may_strong_stream_position, sf.pure_stream_position)
    def __init__(sf, strong_stream_position, /):
        check_type_le(IStrongStreamPosition, strong_stream_position)
        sf._addr = strong_stream_position.pure_stream_position
        sf._wref = weakref.ref(strong_stream_position)
        assert sf._wref() is strong_stream_position

    @property
    @override
    def pure_stream_position(sf, /):
        '-> IPureStreamPosition/opaque_address'
        return sf._addr
    @property
    @override
    def may_strong_stream_position(sf, /):
        '-> may IStrongStreamPosition'
        return sf._wref()





class AutoPruneStream:
    r'''[[[
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.types.StreamPosition:AutoPruneStream@T    =T      +exclude_attrs5listed_in_cls_doc
new_concrete_methods:
    __repr__
    __init__
    prune_lt_
    begin_position
    end_position
    tell
    __iter__
    __next__
    __getitem__
    read_le
    read_at_le
    fill_at_le
    gets_between
    gets_between__with_prev_and_post_position
    gets_between__with_post_position
    gets_between__without_position
    gets_between__with_prev_position
    gets_between__position_only

    #]]]'''#'''
    if 0:
        def __init__(sf, toplevel_idx, may_lowlevel_pure_stream_position, pairs, /):
            'uint -> may opaque_lowlevel_addr -> Iter (toplevel_packet, may_opaque_lowlevel_addr8end4packet)'
            addr = PureStreamPosition(toplevel_idx, may_lowlevel_pure_stream_position)
    def __repr__(sf, /):
        smay_qname = sf._snm
        if smay_qname:
            return smay_qname
        return super().__repr__()
    def __init__(sf, smay_qname, pure_stream_position, pairs, /):
        'PureStreamPosition<uint,?> -> Iter (toplevel_packet, may_opaque_lowlevel_addr8end4packet)'
        check_smay_pseudo_qual_name(smay_qname)
        toplevel_idx = pure_stream_position.toplevel_stream_position4pruning
        check_int_ge(0, toplevel_idx)
        sf._ls = PruneableArray(offset:=toplevel_idx, [])
            # offsetted[(weak_prev_position, packet)]
        sf._it = iter(pairs)
        addr = pure_stream_position
        sf._end = StrongStreamPosition(sf, addr)
        sf._snm = smay_qname
    def prune_lt_(sf, toplevel_idx, /):
        sf._ls.prune_lt_(toplevel_idx)
        return
    @property
    def begin_position(sf, /):
        '-> IStrongStreamPosition'
        #prune_lt_==>>begin_position changed unpredictable#dynamic determine
        if (ls := sf._ls):
            (weak_begin_position, packet) = ls[ls.begin]
            begin_position = weak_begin_position.strong_stream_position_or_raise
        else:
            begin_position = sf.end_position
        return begin_position
    @property
    def end_position(sf, /):
        '-> IStrongStreamPosition'
        return sf._end
    def tell(sf, /):
        return sf.end_position
    def __iter__(sf, /):
        '-> Iter (packet, end_position)'
        return sf
    def __next__(sf, /):
        '-> (packet, end_position)'
        (packet, low_end) = next(sf._it)
            #^StopIteration
        curr_position = sf.end_position
        offset = curr_position.pure_stream_position.toplevel_stream_position4pruning
        end_addr = PureStreamPosition(offset+1, low_end)
        end_position = StrongStreamPosition(sf, end_addr)
        curr_position._set_once__invisible_next_strong_stream_position(end_position)
        sf._ls.append((curr_position.weak_stream_position, packet))
        sf._end = end_position
        return (packet, end_position)
    def __getitem__(sf, k, /):
        check_type_is(slice, k)
        sl = k
        if not sl.step is None: raise TypeError
        return sf.gets_between__without_position(sl.start, sl.stop)
    def read_le(sf, size, /, **kwds4gets_between):
        check_int_ge(0, size)
        return sf.read_at_le(None, size, **kwds4gets_between)
    def read_at_le(sf, may_begin_position, imay_size, /, **kwds4gets_between):
        (begin_position, end_position) = sf.fill_at_le(may_begin_position, imay_size)
        return sf.gets_between(begin_position, end_position, **kwds4gets_between)
    def fill_at_le(sf, may_begin_position, imay_size, /):
        '-> (begin_position, end_position)'
        check_int_ge(-1, imay_size)
        _end_position = sf.end_position
        begin_position = ifNone(may_begin_position, _end_position)
        if imay_size == -1:
            end_position = _end_position
        else:
            ls = sf._ls
            begin_idx = _stream_position2offset(sf, begin_position)
            sz = imay_size
            end_idx = begin_idx + sz
            while 1:
                _end_idx = ls.end
                d = end_idx -_end_idx
                if not d > 0:
                    break
                for _ in islice(sf, d):pass
            if d == 0:
                end_position = sf.end_position
            else:
                (weak_end_position, _) = ls[end_idx]
                end_position = weak_end_position.strong_stream_position_or_raise
            assert end_position.pure_stream_position.toplevel_stream_position4pruning == end_idx
        end_position
        return (begin_position, end_position)

    def gets_between(sf, begin_position, end_position, /, *, with_prev_position=False, with_post_position=False, position_only=False, with_end_position=False):
        # [kwds4gets_between =[def]= {with_prev_position, with_post_position, position_only, with_end_position}]
        check_type_is(bool, with_prev_position)
        check_type_is(bool, with_post_position)
        check_type_is(bool, position_only)
        check_type_is(bool, with_end_position)
        if with_end_position and not position_only: raise TypeError
        if (with_prev_position or with_post_position) and (position_only or with_end_position): raise TypeError
        return _gets_between(**locals())
    def gets_between__with_prev_and_post_position(sf, begin_position, end_position, /):
        '-> [(prev_position, packet, post_position)]'
        return sf.gets_between(begin_position, end_position, with_prev_position=True, with_post_position=True)

    def gets_between__with_post_position(sf, begin_position, end_position, /):
        '-> [(packet, post_position)]'
        return sf.gets_between(begin_position, end_position, with_prev_position=False, with_post_position=True)
    def gets_between__without_position(sf, begin_position, end_position, /):
        '-> [packet]'
        return sf.gets_between(begin_position, end_position, with_prev_position=False, with_post_position=False)

    def gets_between__with_prev_position(sf, begin_position, end_position, /):
        '-> [(prev_position, packet)]'
        return sf.gets_between(begin_position, end_position, with_prev_position=True, with_post_position=False)

    def gets_between__position_only(sf, begin_position, end_position, /, *, with_end_position):
        return sf.gets_between(begin_position, end_position, position_only=True, with_end_position=with_end_position)



def _stream_position2offset(sf, strong_stream_position, /):
    check_type_is(StrongStreamPosition, strong_stream_position)
    idx = strong_stream_position.pure_stream_position.toplevel_stream_position4pruning
    if not strong_stream_position is sf.end_position:
        ls = sf._ls
        (weak_prev_position, packet) = ls[idx]
        prev_position = weak_prev_position.strong_stream_position_or_raise
        if not prev_position is strong_stream_position:raise ValueError
    return idx

def __():
  def _explain_stream_offset(sf, toplevel_idx, /):
    check_int_ge(0, toplevel_idx)
    end = sf.end_position
    end_addr = end.pure_stream_position
    end_offset = end_addr.toplevel_stream_position4pruning
    if not toplevel_idx <= end_offset:raise 000
    sf._ls[toplevel_idx]

def _gets_between__with_weak_prev_position(sf, begin_position, end_position, /):
    '-> [(weak_prev_position, packet)]'
    begin_idx = _stream_position2offset(sf, begin_position)
    end_idx = _stream_position2offset(sf, end_position)
    if not begin_idx <= end_idx: raise ValueError
    ps = sf._ls[begin_idx:end_idx]
    return ps
def _gets_between(*, sf, begin_position, end_position, with_prev_position, with_post_position, position_only, with_end_position):
    #gets_between::kwds4gets_between
    ps = _gets_between__with_weak_prev_position(sf, begin_position, end_position)
    ######################
    if not (with_prev_position or with_post_position or position_only or with_end_position):
        ls = [*map(snd, ps)]
        return ls
    ######################
    ps.append((end_position.weak_stream_position, None))
    it = iter((weak_prev_position.strong_stream_position_or_raise, packet) for weak_prev_position, packet in ps)
    if position_only:
        assert not (with_prev_position or with_post_position)
        ls = [*map(fst, it)]
        if not with_end_position:
            ls.pop()
        return ls
    assert not with_end_position
    ######################


    if with_prev_position and with_post_position:
        def mk(prev_position, packet, post_position, /):
            return (prev_position, packet, post_position)
    elif with_prev_position and not with_post_position:
        def mk(prev_position, packet, post_position, /):
            return (prev_position, packet)
    elif not with_prev_position and with_post_position:
        def mk(prev_position, packet, post_position, /):
            return (packet, post_position)
    else:
        raise 000

    def __(mk, prev_position, packet, /):
        for post_position, next_packet in it:
            yield mk(prev_position, packet, post_position)
            prev_position = post_position
            packet = next_packet
        return
    for prev_position, packet in it:
        break
    else:
        raise 000
    return [*__(mk, prev_position, packet)]
#end-def _gets_between(sf, begin_position, end_position, /, *, with_prev_position, with_post_position, position_only, with_end_position):

#end-class AutoPruneStream:







__all__
from seed.types.StreamPosition import AutoPruneStream
from seed.types.StreamPosition import PureStreamPosition, StrongStreamPosition, WeakStreamPosition

from seed.types.StreamPosition import *
