#__all__:goto
#[forkable is bad idea][there should be only one input_stream and many snapshot]
#   <<== old discarded istream will still remain in parent func stack frame therefore never be destroyed and release memory...
#
#to protect istream monotonic_idx, now ISnapshot is no more subclass of IUnlocker
#
#now cancel auto release:unlocker_release() <<== [@fail:not reply.ok: (unlocker>>snapshot) should not unlocker_release()!]
#
#
r'''[[[
e ../../python3_src/seed/types/stream/IRecoverableInputStream.py
view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/IRecognizerLLoo.py
view ../../python3_src/seed/types/Deque.py
view ../../python3_src/seed/types/view/View.py
view ../../python3_src/seed/types/view/SeqTransformView.py


seed.types.stream.IRecoverableInputStream
py -m nn_ns.app.debug_cmd   seed.types.stream.IRecoverableInputStream -x
py -m nn_ns.app.doctest_cmd seed.types.stream.IRecoverableInputStream:__doc__ -ht

#]]]'''
__all__ = r'''
Error
    InputStreamError__eof
    ReleasedError
    NotSameStreamError
        NotSameStreamNameError

IBasicMonotonicIndex
    IMonotonicIndex
    IMonotonicIndex__flow_identifier
        MonotonicIndex

ExtPositionInfo
IBaseInputStream
    IRecoverableInputStream
        IPlainRecoverableInputStream
            PlainRecoverableInputStream5token_seq
        RecoverableInputStream9LazyList
ISnapshot
    ISnapshot4RecoverableInputStream__clean
        ISnapshot4RecoverableInputStream__clean__init

IUnlocker
    DummyUnlocker
        dummy_unlocker
    DetectionUnlocker
    AddUnlocker
    Unlocker5ISnapshot

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from weakref import ref as wref_# WeakKeyDictionary as WkeyD, WeakValueDictionary as WvalD



from seed.types.IToken import IBaseToken, IToken, BaseToken
from seed.types.IToken import IBasePositionInfo, IPositionInfo4Gap, IPositionInfo4Span
###########
##if 0:
    ##from seed.types.Deque import Deque
    ##from seed.types.view.View import SeqView
###########
from seed.types.LazyList import LazyList, LazyListError
from seed.types.LazyList import to_LazyList, to_LazyListIter

from seed.tiny import null_tuple, fst
from seed.tiny_.check import check_type_is, check_type_le, check_non_ABC, check_int_ge, check_int_ge_lt, check_int_ge_le
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.tiny_._Base4repr import _Base4repr

___end_mark_of_excluded_global_names__0___ = ...

class Error(Exception):pass
class InputStreamError__eof(Error):pass
#class InputStreamError__has_been_read(Error):pass
class ReleasedError(Error):pass
class NotSameStreamError(Error):pass
class NotSameStreamNameError(NotSameStreamError):pass

class ExtPositionInfo(tuple):
    '[ext_info/ExtPositionInfo ~=~ (monotonic_idx, gap_info)]'
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf, *sf)
    def __new__(cls, /, monotonic_idx, gap_info):
        #check_type_is(int, monotonic_idx)
        return tuple.__new__(cls, [monotonic_idx, gap_info])
    @property
    def monotonic_idx(sf, /):
        return sf[0]
    @property
    def gap_info(sf, /):
        return sf[1]

#class ISnapshot(IUnlocker):
class ISnapshot(ABC):
    #to protect istream monotonic_idx, now ISnapshot is no more subclass of IUnlocker
    #   ==>>Unlocker5ISnapshot
    'snapshot'
    __slots__ = ()
    @abstractmethod
    def restore_(sf, istream, /, *, hold_vs_release):
        'IRecoverableInputStream -> (None|^ReleasedError) #if hold_vs_release then finally release'
        #istream.restore5snapshot_(sf, copy_vs_move=hold_vs_release)
        raise ReleasedError

    @property
    @abstractmethod
    def snapshot_released(sf, /):
        '-> bool #[#return True iff called .snapshot_release()]'
    @abstractmethod
    def snapshot_release(sf, /):
        '-> None'


    def __del__(sf, /):
        sf.snapshot_release()

    def restore_and_hold(sf, istream, /):
        'IRecoverableInputStream -> (None|^ReleasedError) #not release'
        return sf.restore_(istream, hold_vs_release=False)
    def restore_and_release(sf, istream, /):
        'IRecoverableInputStream -> (None|^ReleasedError) #finally release'
        return sf.restore_(istream, hold_vs_release=True)
#end-class ISnapshot(ABC):

class ISnapshot4RecoverableInputStream__clean(ISnapshot):
    'usage: __init__():sf._??? = wref_(istream, sf._clean)'
    __slots__ = ()
    @abstractmethod
    def _semi_snapshot_release(sf, /):
        'release but not mark known-snapshot_release'
    @property
    def _clean(wsf, /):
        wsf = wref_(wsf)
        def _clean(istream, /, *, wsf=wsf):
            #semi-release by _clean
            m = wsf()
            if not m is None:
                sf = m
                sf._semi_snapshot_release()
        try:
            return _clean
        finally:
            del _clean
            del wsf
#end-class ISnapshot4RecoverableInputStream__clean(ISnapshot):
class ISnapshot4RecoverableInputStream__clean__init(ISnapshot4RecoverableInputStream__clean):
    ___no_slots_ok___ = True
    def __init__(sf, istream, st4istream, /):
        sf._x = False#is_released
            # [snapshot_released =[def]= sf._x]
        sf._w = wref_(istream, sf._clean)
            # :: may weakref<istream>
            # [semi_snapshot_released =[def]= (sf._w is None)]
            #   semi-release by _clean
            #   see:_semi_snapshot_release()
        sf._st = st4istream
        # invariant:[[snapshot_released] -> [semi_snapshot_released]]
    @abstractmethod
    def _raw_restore_(sf, istream, st4istream, /):
        '[not snapshot_released][same istream]=>IRecoverableInputStream -> st4istream -> None'
    @override
    def restore_(sf, istream, /, *, hold_vs_release):
        'IRecoverableInputStream -> (None|^ReleasedError) #if hold_vs_release then finally release'
        #istream.restore5snapshot_(sf, copy_vs_move=hold_vs_release)
        check_type_is(bool, hold_vs_release)
        if sf.snapshot_released:
            # [snapshot_released]
            raise ReleasedError
        # [not snapshot_released]

        if sf._w is None:
            # [semi_snapshot_released]
            raise NotSameStreamError
        m = sf._w()
        if m is None:
            raise 000-'if istream dead, sf._semi_snapshot_release() should be called, hence cannot come here'
            raise NotSameStreamError
        if not m is istream:
            raise NotSameStreamError
        # [same istream]


        ###########
        # [not snapshot_released]
        # [same istream]
        sf._raw_restore_(istream, sf._st)
        ###########
        if hold_vs_release:
            sf.snapshot_release()
    @property
    @override
    def snapshot_released(sf, /):
        '-> bool #[#return True iff called .snapshot_release()]'
        return sf._x#is_released
    @override
    def snapshot_release(sf, /):
        '-> None'
        if sf._x:
            # [snapshot_released]
            return
        # [not snapshot_released]

        # !! [[snapshot_released] -> [semi_snapshot_released]]
        sf._semi_snapshot_release()
        # [not snapshot_released]
        # [semi_snapshot_released]
        sf._x = True#is_released
            # [snapshot_released]
        ######################
        # [semi_snapshot_released]
        # [snapshot_released]
        # hold:invariant:[[snapshot_released] -> [semi_snapshot_released]]
        ######################
    @override
    def _semi_snapshot_release(sf, /):
        'release but not mark known-snapshot_release'
        if sf._x:
            # [snapshot_released]
            # !! [[snapshot_released] -> [semi_snapshot_released]]
            # [semi_snapshot_released]
            return
        # [not snapshot_released]
        if sf._w is None:
            # [semi_snapshot_released]
            return
        ######################
        del sf._st
        sf._w = None
            # [semi_snapshot_released]
        ######################
        #no:sf._x = True#is_released
        ######################
        # [not snapshot_released]
        # [semi_snapshot_released]
        ######################
        return
#end-class ISnapshot4RecoverableInputStream__clean__init(ISnapshot4RecoverableInputStream__clean):



class IBaseInputStream(ABC):
    'base_istream/base_input_stream'
    __slots__ = ()
    ######################
    @abstractmethod
    def tell_ext_info(sf, /):
        '-> ext_info/ext_position_info/ExtPositionInfo'
        return ExtPositionInfo(sf.tell_monotonic_idx(), sf.tell_gap_info())
    @abstractmethod
    def peek_ext_iter(sf, /):
        '-> Iter token_ext/(token, ext_info)'
    @abstractmethod
    def read1_ext(sf, /):
        '-> token_ext/(token, ext_info) | ^InputStreamError__eof'

    ######################
    #@abstractmethod
    def tell_gap_info(sf, /):
        '-> gap_info/gap_info8begin/prev_gap_info'
        return sf.tell_ext_info().gap_info
    #@abstractmethod
    def tell_monotonic_idx(sf, /):
        '-> monotonic_idx/TotalOrderingType #monotonic - the clock cannot go backward #distinguish each token position'
        return sf.tell_ext_info().monotonic_idx
    #@abstractmethod
    def read1(sf, /):
        '-> token | ^InputStreamError__eof'
        return fst(sf.read1_ext())
    #@abstractmethod
    def peek_iter(sf, /):
        '-> Iter token'
        return map(fst, sf.peek_ext_iter())
    @property
    def may_head_ext(sf, /):
        '-> may token_ext/(token, ext_info)'
        for token_ext in sf.peek_ext_iter():
            return token_ext
        return None
    @property
    def head_ext(sf, /):
        '-> (token_ext/(token, ext_info) | ^InputStreamError__eof)'
        for token_ext in sf.peek_ext_iter():
            return token_ext
        raise InputStreamError__eof(sf.tell_gap_info())
    @property
    def head(sf, /):
        '-> (token | ^InputStreamError__eof)'
        for token in sf.peek_iter():
            return token
        raise InputStreamError__eof(sf.tell_gap_info())
    @property
    def eof(sf, /):
        '-> bool'
        ####################
        for _ in sf.peek_iter():
            return False
        return True
        ####################
        try:
            sf.head
        except InputStreamError__eof:
            return True
        return False
        ####################
    def read_ext_iter(sf, /):
        '-> Iter token_ext/(token, ext_info)'
        try:
            while 1:
                yield sf.read1_ext()
        except InputStreamError__eof:
            return

    def read_iter(sf, /):
        '-> Iter token'
        try:
            while 1:
                yield sf.read1()
        except InputStreamError__eof:
            return

    def peek_ext_le(sf, sz, /):
        '-> [token_ext/(token, ext_info)]'
        return tuple(islice(sf.peek_ext_iter(), sz))
    def read_ext_le(sf, sz, /):
        '-> [token_ext/(token, ext_info)]'
        return tuple(islice(sf.read_ext_iter(), sz))

    def peek_le(sf, sz, /):
        '-> [token]'
        return tuple(islice(sf.peek_iter(), sz))
    def read_le(sf, sz, /):
        '-> [token]'
        return tuple(islice(sf.read_iter(), sz))
    ######################


class IRecoverableInputStream(IBaseInputStream):
    'istream/input_stream'
    __slots__ = ()
    @property
    @abstractmethod
    def max_num_tokens6backward(sf, /):
        '-> uint#limit4back_cache'
        #IRecognizerLLoo.required_num_tokens6backward6env_(env)
    #@abstractmethod
    #def view_tokens6backward(sf, /):
    #    '-> view [token]'
    #   cancel <<== !! snapshot copy to much...
    @abstractmethod
    def list_tokens6backward(sf, sz=-1, /):
        '-> tuple#tokens6backward/[token] if sz < 0 else tokens6backward[:sz]'
        #hold two tails of one LazyList
    @abstractmethod
    def save2snapshot(sf, /):
        '-> snapshot/ISnapshot'
    #@abstractmethod
    def restore5snapshot_(sf, snapshot, /, *, copy_vs_move:bool):
        'snapshot/ISnapshot -> (None|^ReleasedError) #[if copy_vs_move then finally call snapshot.snapshot_release()]'
        return snapshot.restore_(sf, hold_vs_release=copy_vs_move)
        ISnapshot.restore_
    def restore5snapshot__copy(sf, snapshot, /):
        'snapshot/ISnapshot -> None|^ReleasedError #not call snapshot.snapshot_release()'
        sf.restore5snapshot_(snapshot, copy_vs_move=False)
    def restore5snapshot__move(sf, snapshot, /):
        'snapshot/ISnapshot -> None|^ReleasedError #finally call snapshot.snapshot_release()'
        sf.restore5snapshot_(snapshot, copy_vs_move=True)
    ######################
    ##@property
    ##@abstractmethod
    ##def boxed_istream(sf, /):
    ##    '-> IBoxedInputStream'
##class IForkableInputStream(IRecoverableInputStream):
##    __slots__ = ()
##    @abstractmethod
##    def fork(sf, /):
##        '-> new-IForkableInputStream'
##    @override
##    def save2snapshot(sf, /):
##        '-> snapshot/ISnapshot'
##        return Snapshot4IForkableInputStream(sf)

class IUnlocker(ABC):
    'unlocker'
    __slots__ = ()
    @property
    @abstractmethod
    def known_released(sf, /):
        '-> bool #[#return True iff called .unlocker_release()]'
    @abstractmethod
    def unlocker_release(sf, /):
        '-> None'
    if 0:
        #now cancel auto release:unlocker_release() <<== [@fail:not reply.ok: (unlocker>>snapshot) should not unlocker_release()!]
        def __del__(sf, /):
            sf.unlocker_release()
        def close(sf, /):
            sf.unlocker_release()
    def __rshift__(sf, snapshot, /):
        'sf >> snapshot'
        return sf + Unlocker5ISnapshot(snapshot)
    def __add__(sf, ot, /):
        'sf + ot'
        return AddUnlocker(sf, ot)
        if ot.known_released:return sf
        if sf.known_released:return ot
    def __enter__(sf, /):
        return sf
    def __exit__(sf, exc_type, exc_value, traceback, /):
        sf.unlocker_release()
class DummyUnlocker(IUnlocker):
    'dummy_unlocker'
    ___no_slots_ok___ = True
    #@override
    known_released = True

    @override
    def unlocker_release(sf, /):
        '-> None'
dummy_unlocker = DummyUnlocker()

class DetectionUnlocker(IUnlocker):
    'detection_unlocker'
    ___no_slots_ok___ = True
    def __init__(sf, /):
        sf._x = False
    @property
    @override
    def known_released(sf, /):
        '-> bool #[#return True iff called .unlocker_release()]'
        return sf._x
    @override
    def unlocker_release(sf, /):
        '-> None'
        sf._x = True
_detection_unlocker = DetectionUnlocker()


class AddUnlocker(IUnlocker):
    ___no_slots_ok___ = True
    def __new__(cls, lhs, rhs, /):
        if rhs.known_released:
            if lhs.known_released:
                return dummy_unlocker
            return lhs
        if lhs.known_released:
            return rhs
        sf = super(__class__, cls).__new__(cls)
        sf._m = [lhs, rhs]
        return sf

    @property
    @override
    def known_released(sf, /):
        '-> bool'
        #return True iff called .unlocker_release()
        return not sf._m
        ######################
        ######################
        ######################
        ######################

        ##m = sf._m
        ##if not m:
        ##    return True
        ########################
        ##ls = m
        ##while ls:
        ##    #reversed() <<== "unlocker >> snapshot"
        ##    if not ls[-1].released:
        ##        return False
        ##    ls.pop()
        ##sf._m = None
        ##return True
        ########################
        ##if all(unlocker.released for unlocker in reversed(ls)):
        ##    #reversed() <<== "unlocker >> snapshot"
        ##    sf._m = None
        ##    return True
        ##return False
    @override
    def unlocker_release(sf, /):
        '-> None'
        if not (ls:=sf._m):
            return
        while ls:
            #reversed() <<== "unlocker >> snapshot"
            #ls.pop().unlocker_release()
            ls[-1].unlocker_release()
                #??^Exception??
            ls.pop()
        sf._m = None
        return
        ######################
        ######################
        ######################

        for unlocker in ls:
            unlocker.unlocker_release()
        sf._m = None

class Unlocker5ISnapshot(IUnlocker):
    ___no_slots_ok___ = True
    def __new__(cls, snapshot, /):
        if snapshot is None:
            return dummy_unlocker
        #check_type_le(ISnapshot, snapshot)
        if snapshot.snapshot_released:
            return dummy_unlocker
        sf = super(__class__, cls).__new__(cls)
        sf._m = snapshot
        return sf

    @property
    @override
    def known_released(sf, /):
        '-> bool'
        #return True iff called .unlocker_release()
        return sf._m is None
        ######################
        ######################
        ######################
        ######################
        m = sf._m
        if m is None:
            return True
        snapshot = m
        b = snapshot.snapshot_released
        if b:
            sf._m = None
        return b
    @override
    def unlocker_release(sf, /):
        '-> None'
        m = sf._m
        if m is None:
            return
        snapshot = m
        snapshot.snapshot_release()
        sf._m = None




class IBasicMonotonicIndex(ABC):
    'monotonic_idx can be of arbitrary TotalOrderingType'
    __slots__ = ()
    @abstractmethod
    def __hash__(sf, /):
        '-> int'
    @abstractmethod
    def __eq__(sf, ot, /):
        '-> bool|NotImplemented|^NotSameStreamNameError'
    @abstractmethod
    def __lt__(sf, ot, /):
        '-> bool|NotImplemented|^NotSameStreamNameError'
    @abstractmethod
    def __le__(sf, ot, /):
        '-> bool|NotImplemented|^NotSameStreamNameError'
    def __ne__(sf, ot, /):
        return not sf == ot
    def __ge__(sf, ot, /):
        return not sf < ot
    def __gt__(sf, ot, /):
        return not sf <= ot
class IMonotonicIndex(IBasicMonotonicIndex):
    __slots__ = ()
    @abstractmethod
    def __sub__(sf, ot, /):
        '-> int/+-num_tokens|NotImplemented|^NotSameStreamNameError'
class IMonotonicIndex__flow_identifier(IMonotonicIndex):
    __slots__ = ()
    @property
    @abstractmethod
    def flow_name(sf, /):
        '-> identifier<stream>/hashable #neednot be str'
    @property
    @abstractmethod
    def flow_idx(sf, /):
        '-> uint/num_tokens'
    @abstractmethod
    def next(sf, /):
        '-> IMonotonicIndex'
    ###########
    ##if 0:
    ##    def __iadd__(sf, j, /):
    ##        #check_int_ge(0, j)
    ##        return type(sf)(sf.flow_name, sf.flow_idx+j)
    ###########

    ###########
    #IMonotonicIndex
    ###########
    @override
    def __sub__(sf, ot, /):
        '-> int/+-num_tokens|NotImplemented|^NotSameStreamNameError'
        return _idx_op_(sf, ot, 0, '__sub__')
    ###########
    #IBasicMonotonicIndex
    ###########
    @override
    def __hash__(sf, /):
        return hash((id(type(sf)), sf.flow_name, sf.flow_idx))
    @override
    def __eq__(sf, ot, /):
        return _idx_op_(sf, ot, True, '__eq__')
        if sf is ot:
            return True
        return type(sf) is type(ot) and sf.flow_name == ot.flow_name and sf.flow_idx == ot.flow_idx
    @override
    def __le__(sf, ot, /):
        return _idx_op_(sf, ot, True, '__le__')
    @override
    def __lt__(sf, ot, /):
        return _idx_op_(sf, ot, False, '__lt__')

def _idx_op_(sf, ot, r4is, op, /):
    'IMonotonicIndex__flow_identifier -> IMonotonicIndex__flow_identifier -> r -> str -> r|NotImplemented|^NotSameStreamNameError'
    if sf is ot:
        return r4is
    if not type(sf) is type(ot):
        return NotImplemented
    if not sf.flow_name == ot.flow_name:
        raise NotSameStreamNameError(sf.flow_name, ot.flow_name)
    return getattr(int, op)(sf.flow_idx, ot.flow_idx)


class MonotonicIndex(IMonotonicIndex__flow_identifier):
    'just a example class, monotonic_idx can be of arbitrary TotalOrderingType'
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._nm, sf._j)
    def __init__(sf, nm, idx, /):
        sf._nm = nm #object() if may_nm is None else may_nm
        sf._j = idx
    ###########
    #IMonotonicIndex__flow_identifier
    ###########
    @property
    @override
    def flow_name(sf, /):
        '-> identifier<stream> #neednot be str'
        return sf._nm
    @property
    @override
    def flow_idx(sf, /):
        '-> uint/num_tokens'
        return sf._j
    @override
    def next(sf, /):
        '-> MonotonicIndex'
        return type(sf)(sf._nm, sf._j+1)
#.    ###########
#.    #IMonotonicIndex
#.    ###########
#.    @override
#.    def __sub__(sf, ot, /):
#.        '-> int/+-num_tokens'
#.
#.    ###########
#.    #IBasicMonotonicIndex
#.    ###########
#.    @override
#.    def __hash__(sf, /):
#.        return hash((id(type(sf)), sf._nm, sf._j))
#.    @override
#.    def __eq__(sf, ot, /):
#.        return _hcmp_(sf, ot, True, '__eq__')
#.        if sf is ot:
#.            return True
#.        return type(sf) is type(ot) and sf._nm == ot._nm and sf._j == ot._j
#.    @override
#.    def __le__(sf, ot, /):
#.        return _hcmp_(sf, ot, True, '__le__')
#.    @override
#.    def __lt__(sf, ot, /):
#.        return _hcmp_(sf, ot, False, '__lt__')
#.def _hcmp_(sf, ot, r4eq, op, /):
#.    if sf is ot:
#.        return r4eq
#.    if not type(sf) is type(ot):
#.        return NotImplemented
#.    if not sf._nm == ot._nm:
#.        raise NotSameStreamNameError(sf._nm, ot._nm)
#.    return getattr(int, op)(sf._j, ot._j)
check_non_ABC(MonotonicIndex)

class IPlainRecoverableInputStream(IRecoverableInputStream):
    'plain <<== seekable'
    ___no_slots_ok___ = True
    @abstractmethod
    def seek_monotonic_idx(sf, monotonic_idx, /):
        'monotonic_idx -> None'
    @override
    def save2snapshot(sf, /):
        '-> snapshot/ISnapshot'
        return _Snapshot4IPlainRIStream(sf)
_IPRIStream = IPlainRecoverableInputStream
class _Snapshot4IPlainRIStream(ISnapshot4RecoverableInputStream__clean__init):
    'snapshot<IPlainRecoverableInputStream>#eg:PlainRecoverableInputStream5token_seq'
    ___no_slots_ok___ = True
    def __init__(sf, istream, /):
        #check_type_is(_RIStream5token_seq, istream)
        check_type_le(_IPRIStream, istream)
        monotonic_idx = istream.tell_monotonic_idx()
        st4istream = monotonic_idx
        super().__init__(istream, st4istream)
        return
        # ######################
        # ######################
        # max_num_tokens6backward = istream._max
        # offset = istream._j
        # token_seq = istream._ts
        # eof_gap_position_info = istream._g8eof
        # ######################
        # st4istream = (max_num_tokens6backward, offset, token_seq, eof_gap_position_info)
        # super().__init__(istream, st4istream)
    @override
    def _raw_restore_(sf, istream, st4istream, /):
        '[not snapshot_released][same istream]=>IRecoverableInputStream -> st4istream -> None'
        monotonic_idx = st4istream
        istream.seek_monotonic_idx(monotonic_idx)
        return
        # ######################
        # ######################
        # (max_num_tokens6backward, offset, token_seq, eof_gap_position_info) = st4istream
        # ######################
        # istream._max = max_num_tokens6backward
        # istream._j = offset
        # istream._ts = token_seq
        # istream._g8eof = eof_gap_position_info
        # ######################
        # return
check_non_ABC(_Snapshot4IPlainRIStream)
#end-class _Snapshot4IPlainRIStream(ISnapshot4RecoverableInputStream__clean__init):



class PlainRecoverableInputStream5token_seq(IPlainRecoverableInputStream):
    '[PlainRecoverableInputStream5token_seq ~=~ (max_num_tokens6backward, offset, token_seq/[IToken], eof_gap_position_info)] # [used as pseudo-IRecoverableInputStream for testing]'
    'PlainRecoverableInputStream5token_seq :: uint -> may IPositionInfo4Gap -> uint -> [token] -> PlainRecoverableInputStream5token_seq'
    ___no_slots_ok___ = True
    def __init__(sf, max_num_tokens6backward, may_prev_token_end_gap_position_info, offset, token_seq, /):
        'uint -> may IPositionInfo4Gap -> uint -> [token] -> None'
        check_int_ge(0, max_num_tokens6backward)
        check_int_ge_le(0, len(token_seq), offset)
        if not token_seq and may_prev_token_end_gap_position_info is None:raise TypeError
        if not token_seq:
            prev_token_end_gap_position_info = may_prev_token_end_gap_position_info
            eof_gap_position_info = prev_token_end_gap_position_info
        else:
            eof_gap_position_info = token_seq[-1].token_end_position_info
        eof_gap_position_info

        ######################
        sf._max = max_num_tokens6backward
        sf._j = offset
        sf._ts = token_seq
        sf._g8eof = eof_gap_position_info
        ######################
    def __repr__(sf, /):
        ######################
        max_num_tokens6backward = sf._max
        may_prev_token_end_gap_position_info = None if sf._ts else sf._g8eof
        offset = sf._j
        token_seq = sf._ts
        #eof_gap_position_info = sf._g8eof
        ######################
        return repr_helper(sf, max_num_tokens6backward, may_prev_token_end_gap_position_info, offset, token_seq)
    ######################
    @override
    def seek_monotonic_idx(sf, monotonic_idx, /):
        'monotonic_idx -> None'
        offset = monotonic_idx
        check_int_ge_le(0, len(sf._ts), offset)
        sf._j = offset
    @override
    def tell_monotonic_idx(sf, /):
        '-> monotonic_idx/TotalOrderingType #monotonic - the clock cannot go backward #distinguish each token position'
        monotonic_idx = offset = sf._j
        return monotonic_idx
    ######################
    @override
    def tell_gap_info(sf, /):
        '-> gap_info/gap_info8begin/prev_gap_info'
        offset = sf._j
        return sf._tell_gap_info6offset(offset)
    @override
    def tell_ext_info(sf, /):
        '-> ext_info/ext_position_info/ExtPositionInfo'
        offset = sf._j
        return sf._tell_ext_info6offset(offset)
        return ExtPositionInfo(sf.tell_monotonic_idx(), sf.tell_gap_info())
    def _tell_gap_info6offset(sf, offset, /):
        'offset -> gap_info/gap_info8begin/prev_gap_info'
        token_seq = sf._ts
        return token_seq[offset].token_begin_position_info if not offset == len(token_seq) else sf._g8eof
    def _tell_ext_info6offset(sf, offset, /):
        'offset -> ext_info/ext_position_info/ExtPositionInfo'
        return ExtPositionInfo(offset, sf._tell_gap_info6offset(offset))
    @override
    def peek_ext_iter(sf, /):
        '-> Iter token_ext/(token, ext_info)'
        offset = sf._j
        token_seq = sf._ts
        return map(sf._peek_ext6offset, range(offset, len(token_seq)))
        ##for offset in range(offset, len(token_seq)):
        ##    token_ext = sf._peek_ext6offset(offset)
        ##    yield token_ext
    @override
    def read1_ext(sf, /):
        '-> token_ext/(token, ext_info) | ^InputStreamError__eof'
        offset = sf._j
        token_ext = sf._peek_ext6offset(offset)
        sf._j += 1
        return token_ext
    def _peek_ext6offset(sf, offset, /):
        'offset -> token_ext/(token, ext_info) | ^InputStreamError__eof'
        token_seq = sf._ts
        try:
            token = token_seq[offset]
        except IndexError:
            raise InputStreamError__eof(sf._g8eof)
        ext_info = sf._tell_ext_info6offset(offset+1)
        token_ext = (token, ext_info)
        return token_ext

    ######################
    @property
    @override
    def max_num_tokens6backward(sf, /):
        '-> uint#limit4back_cache'
        #IRecognizerLLoo.required_num_tokens6backward6env_(env)
        return sf._max
    #@abstractmethod
    #def view_tokens6backward(sf, /):
    #    '-> view [token]'
    #   cancel <<== !! snapshot copy to much...
    @override
    def list_tokens6backward(sf, sz=-1, /):
        '-> tuple#tokens6backward/[token] if sz < 0 else tokens6backward[:sz]'
        #hold two tails of one LazyList
        check_type_is(int, sz)
        if sz < 0:
            sz = sf.max_num_tokens6backward
        else:
            sz = min(sz, sf.max_num_tokens6backward)
        sz
        offset = sf._j
        token_seq = sf._ts
        sz = min(sz, offset)
        return tuple(token_seq[offset-sz:offset])

    ######################
check_non_ABC(PlainRecoverableInputStream5token_seq)
_RIStream5token_seq = PlainRecoverableInputStream5token_seq
#end-class PlainRecoverableInputStream5token_seq(IPlainRecoverableInputStream):


class RecoverableInputStream9LazyList(IRecoverableInputStream):
    '[RecoverableInputStream9LazyList ~=~ (max_num_tokens6backward,?view4tokens6backward?,ExtPositionInfo/(MonotonicIndex,IPositionInfo4Gap),LazyList<(IToken{.token_end_position_info},MonotonicIndex)>)]'
    'RecoverableInputStream9LazyList :: uint -> IPositionInfo4Gap -> Iter token -> RecoverableInputStream9LazyList'
    ___no_slots_ok___ = True
    def _iter_check_input_iter6init_(sf, nonlazylist_iter_tokens8istream, /):
        assert nonlazylist_iter_tokens8istream is iter(nonlazylist_iter_tokens8istream) #to avoid cache LazyList
        for token in nonlazylist_iter_tokens8istream:
            check_type_le(IToken, token)
            yield token
        return#to_LazyListIter(nonlazylist_iter_tokens8istream)
    def _check_prev_token_end_gap_position_info6init_(sf, prev_token_end_gap_position_info, /):
        check_type_le(IPositionInfo4Gap, prev_token_end_gap_position_info)
    def _get_end_gap_position_info5token_(sf, token, /):
        'token -> token_end_position_info'
        del sf
        return token.token_end_position_info
    if 1:
        #neednot be staticmethod:
        #   not part of API
        #   just impl details to better used with _0_mk_LazyList4stream()
        @staticmethod
        def _get_end_gap_position_info5token_(token, /):
            'token -> token_end_position_info'
            return token.token_end_position_info
    def __init__(sf, max_num_tokens6backward, prev_token_end_gap_position_info, nonlazylist_iter_tokens8istream, /):
        'uint -> IPositionInfo4Gap -> Iter token -> None'
        check_int_ge(0, max_num_tokens6backward)
        sf._check_prev_token_end_gap_position_info6init_(prev_token_end_gap_position_info)
        nonlazylist_iter_tokens8istream = iter(nonlazylist_iter_tokens8istream) #to avoid cache LazyList
        nonlazylist_iter_tokens8istream = sf._iter_check_input_iter6init_(nonlazylist_iter_tokens8istream)
        nm = object()
        monotonic_idx = MonotonicIndex(nm, 0)
        #lazylist_iter
        #check_type_is(_LazyListIter, lazylist_iter)

        lazylist = _0_mk_LazyList4stream(sf._get_end_gap_position_info5token_, monotonic_idx, nonlazylist_iter_tokens8istream)
        check_type_is(LazyList, lazylist)
        ext = ExtPositionInfo(monotonic_idx, prev_token_end_gap_position_info)

        #sf._g = prev_token_end_gap_position_info
        sf._ext = ext
        sf._ly = lazylist
            # :: LazyList token_ext/(token, ext_info)
        sf._max = max_num_tokens6backward
        if sf._max:
            sf._ext4prev = ext
            sf._ly4prev = lazylist
            sf._nroom4prev = sf._max
        return
        ###########
        ##if 0:
        ##    if sf._max:
        ##        dq = Deque() #view4tokens6backward
        ##            # :: [(ext_info, token)]{len<=max_num_tokens6backward}
        ##        sf._vw = SeqView(dq)
        ##        # !! sf._dq may be omitted
        ##        # !! py.dict.impl.split_table
        ##        sf._dq = dq
        ##    else:
        ##        sf._vw = null_tuple
        ###########

    ######################
    ######################
    ######################
    @override
    def tell_ext_info(sf, /):
        '-> ext_position_info/ExtPositionInfo'
        return sf._ext
    @override
    def peek_ext_iter(sf, /):
        '-> Iter token_ext/(token, ext_info)'
        return iter(sf._ly) #to avoid cache LazyList
    @override
    def read1_ext(sf, /):
        '-> token_ext/(token, ext_info) | ^InputStreamError__eof'
        m = sf._ly.may_unpack()
        if not m:
            raise InputStreamError__eof(sf.tell_ext_info())
        (token_ext, tail_ly) = m
        (token, ext_info) = token_ext
        # token, ext_info, tail_ly
        ###########
        ##if 0:
        ##    if sf._max:
        ##        dq = sf._dq
        ##        if len(dq) == sf._max:
        ##            dq.pop_left()
        ##        dq.append_right((sf._ext, token))
        ##    #above:use sf._ext
        ###########
        if sf._max:
            if not sf._nroom4prev:
                #full:
                (token_ext4prev, tail_ly4prev) = sf._ly4prev.may_unpack()
                (token4prev, ext_info4prev) = token_ext4prev
                # token4prev, ext_info4prev, tail_ly4prev
                del token4prev
                sf._ext4prev = ext_info4prev
                sf._ly4prev = tail_ly4prev
                #sf._nroom4prev -= 0
            else:
                sf._nroom4prev -= 1
        # token, ext_info, tail_ly
        del token
        sf._ext = ext_info
        sf._ly = tail_ly
        return token_ext

    ######################
    ######################
    ######################
    @property
    @override
    def max_num_tokens6backward(sf, /):
        '-> uint#limit4back_cache'
        return sf._max
    #@override
    #def view_tokens6backward(sf, /):
    #    '-> view [token]'
    #    return sf._vw
    @override
    def list_tokens6backward(sf, sz=-1, /):
        '-> tuple#tokens6backward/[token] if sz < 0 else tokens6backward[:sz]'
        #hold two tails of one LazyList
        n = sf._max -sf._nroom4prev
        if sz < 0:
            sz = n
        else:
            sz = min(sz, n)
        sz
        if not sz:
            return null_tuple
        it = iter(sf._ly4prev) #to avoid cache LazyList
        it = map(fst, it) # :: Iter token
        return tuple(islice(it, sz))
    @override
    def save2snapshot(sf, /):
        '-> snapshot/ISnapshot'
        return _Snapshot4RIStream5LazyList(sf)

    ######################
    ######################
    ######################

def _0_mk_LazyList4stream(get_, monotonic_idx, nonlazylist_iter_tokens8istream, /):
    '(token->token_end_position_info) -> Iter token -> LazyList token_ext/(token, ext_info)'
    assert nonlazylist_iter_tokens8istream is iter(nonlazylist_iter_tokens8istream) #to avoid cache LazyList
    return to_LazyList(_1_mk_pairs4stream(get_, monotonic_idx, nonlazylist_iter_tokens8istream))
def _1_mk_pairs4stream(get_, monotonic_idx, nonlazylist_iter_tokens8istream, /):
    for token in nonlazylist_iter_tokens8istream:
        monotonic_idx = monotonic_idx.next()
        token_end_position_info = get_(token)
        ext_info = ExtPositionInfo(monotonic_idx, token_end_position_info)
        yield (token, ext_info)
check_non_ABC(RecoverableInputStream9LazyList)
_RIStream5LazyList = RecoverableInputStream9LazyList
#end-class RecoverableInputStream9LazyList(IRecoverableInputStream):

class _Snapshot4RIStream5LazyList(ISnapshot4RecoverableInputStream__clean__init):
    #class _Snapshot4RIStream5LazyList(ISnapshot):
    'snapshot<RecoverableInputStream9LazyList>'
    ___no_slots_ok___ = True
    def __init__(sf, istream, /):
        check_type_is(_RIStream5LazyList, istream)
        _2 = (istream._ext, istream._ly)
        if istream._max:
            _03 = (istream._ext4prev, istream._ly4prev, istream._nroom4prev)
            st4istream = _2, _03
        else:
            st4istream = _2
        st4istream
        super().__init__(istream, st4istream)
        ###########
        ##if 0:
        ##    if istream._max:
        ##        sf._01 = istream._dq.to_list()
        ###########
    @override
    def _raw_restore_(sf, istream, st4istream, /):
        '[not snapshot_released][same istream]=>IRecoverableInputStream -> st4istream -> None'
        ###########
        ##if 0:
        ##    if istream._max:
        ##        dq = istream._dq
        ##        dq.clear()
        ##        dq.extend_right(sf._01)
        ###########
        if istream._max:
            _2, _03 = st4istream
            (istream._ext4prev, istream._ly4prev, istream._nroom4prev) = _03
        else:
            _2 = st4istream
        _2
        (istream._ext, istream._ly) = _2
        return
check_non_ABC(RecoverableInputStream9LazyList)
check_non_ABC(_Snapshot4RIStream5LazyList)
#end-class _Snapshot4RIStream5LazyList(ISnapshot4RecoverableInputStream__clean__init):


##class ISnapshot(IUnlocker):
##    'snapshot'
##    __slots__ = ()
##    @abstractmethod
##    def restore_(sf, /, *, hold_vs_release):
##        '-> (IRecoverableInputStream|^ReleasedError) # boxed_istream8begin keep unchanged if not hold_vs_release else  may changed'
##    def restore_and_hold(sf, /):
##        '-> (IRecoverableInputStream|^ReleasedError) # boxed_istream8begin keep unchanged'
##        return sf.restore_(hold_vs_release=False)
##        raise ReleasedError
##    def restore_and_release(sf, /):
##        '-> (IRecoverableInputStream|^ReleasedError) # boxed_istream8begin may unchanged'
##        return sf.restore_(hold_vs_release=True)
##        try:
##            return sf.restore_and_hold()
##        finally:
##            sf.unlocker_release()
##class Snapshot4IForkableInputStream(IUnlocker):
##    ___no_slots_ok___ = True
##    def __init__(sf, may_forkable_istream:'may IForkableInputStream', /):
##        sf._m = None if may_forkable_istream is None else may_forkable_istream.fork()
##    @override
##    @override
##    def restore_(sf, /, *, hold_vs_release):
##        '-> (IRecoverableInputStream|^ReleasedError) # boxed_istream8begin keep unchanged if not hold_vs_release else  may changed'
##        m = sf._m
##        if m is None:
##            raise ReleasedError
##        forkable_istream = m
##        if hold_vs_release:
##            #release
##            sf.snapshot_release()
##            return forkable_istream
##        #hold
##        return forkable_istream.fork()
##    @property
##    @override
##    def known_released(sf, /):
##        '-> bool'
##        return sf._m is None
##    @override
##    def snapshot_release(sf, /):
##        '-> None'
##        sf._m = None
##check_non_ABC(Snapshot4IForkableInputStream)

##class IBoxedInputStream(ABC):
##    'boxed_istream'
##    __slots__ = ()
##    @property
##    @abstractmethod
##    def gap_info(sf, /):
##        '-> gap_info'
##    @property
##    @abstractmethod
##    def monotonic_idx(sf, /):
##        '-> TotalOrderingType'
##    @abstractmethod
##    def unbox(sf, /):
##        '-> istream|^InputStreamError__has_been_read'
##    @property
##    @abstractmethod
##    def changed(sf, /):
##        '-> bool'
##        try:
##            sf.unbox()
##        except InputStreamError__has_been_read:
##            return True
##        return False
##    def __bool__(sf, /):
##        '-> not_input_stream_has_been_read/bool'
##        return not sf.changed
##class IBoxedInputStream__accesss_may_invalid_istream(IBoxedInputStream):
##    __slots__ = ()
##    @abstractmethod
##    def _get_may_invalid_istream_(sf, /):
##        '-> may <maybe-invalid-istream>'
##    @abstractmethod
##    def _del_invalid_istream_(sf, /):
##        '-> None'
##    def _get_may_valid_istream_(sf, /):
##        '-> may <valid-istream>'
##        m = sf._get_may_invalid_istream_()
##        if m is None:
##            return None
##        xvalid_istream = m
##        if not xvalid_istream.tell_monotonic_idx() == sf.monotonic_idx:
##            invalid_istream = xvalid_istream
##            sf._del_invalid_istream_()
##            return sf._get_may_valid_istream_()
##        istream = xvalid_istream
##        return istream
##    @override
##    def unbox(sf, /):
##        '-> istream|^InputStreamError__has_been_read'
##        m = sf._get_may_valid_istream_()
##        if m is None:
##            raise InputStreamError__has_been_read
##        istream = m
##        return istream
##    @property
##    @override
##    def changed(sf, /):
##        '-> bool'
##        m = sf._get_may_valid_istream_()
##        return m is None

#class ISnapshot(IUnlocker):


__all__
from seed.types.stream.IRecoverableInputStream import \
(    InputStreamError__eof
,    ReleasedError
,    NotSameStreamError
,        NotSameStreamNameError
#
,MonotonicIndex
,ExtPositionInfo
,IBaseInputStream
,    IRecoverableInputStream
,        PlainRecoverableInputStream5token_seq
,        RecoverableInputStream9LazyList
,ISnapshot
#
,IUnlocker
,    DummyUnlocker
,        dummy_unlocker
,    DetectionUnlocker
,    AddUnlocker
,    Unlocker5ISnapshot
)

#for_rarely_subclassing:
from seed.types.stream.IRecoverableInputStream import IUnlocker

#for_subclassing:
from seed.types.stream.IRecoverableInputStream import IRecoverableInputStream, IPlainRecoverableInputStream, ISnapshot, ISnapshot4RecoverableInputStream__clean__init
from seed.types.stream.IRecoverableInputStream import ExtPositionInfo, MonotonicIndex
from seed.types.stream.IRecoverableInputStream import InputStreamError__eof, ReleasedError, NotSameStreamError, NotSameStreamNameError

#utilities:
from seed.types.stream.IRecoverableInputStream import dummy_unlocker, DetectionUnlocker
from seed.types.stream.IRecoverableInputStream import PlainRecoverableInputStream5token_seq, RecoverableInputStream9LazyList

from seed.types.stream.IRecoverableInputStream import *
