
r'''
e ../../python3_src/seed/algo/closure.py
loop until result unchanged
#'''
from seed.abc.abc__ver1 import ABC, abstractmethod
from seed.tiny import check_type_is

class IClosureAlgorithm(ABC):
    r'''
    state may be mutable
    snapshot shiuld? be immutable?
    eg.
        mutable state==growonly dict
        immutable snapshot==len of state
    #'''
    __slots__ = ()


    @abstractmethod
    def _step4closure_(sf, st, /):
        'st -> st'
    @abstractmethod
    def _state2snapshot_(sf, st, /):
        'st -> snapshot'
    @abstractmethod
    def _eq4snapshot_(sf, lhs_snapshot, rhs_snapshot, /):
        'snapshot -> snapshot -> bool '


    def check_state(sf, st, /):
        'st -> None'
    def check_snapshot(sf, snapshot, /):
        'snapshot -> None'

    def step4closure(sf, st, /):
        'st -> st'
        sf.check_state(st)
        st = sf._step4closure_(st)
        sf.check_state(st)
        return st

    def state2snapshot(sf, st, /):
        'st -> snapshot'
        sf.check_state(st)
        snapshot = sf._state2snapshot_(st)
        sf.check_snapshot(snapshot)
        return snapshot

    def eq4snapshot(sf, lhs_snapshot, rhs_snapshot, /):
        'snapshot -> snapshot -> bool '
        sf.check_snapshot(lhs_snapshot)
        sf.check_snapshot(rhs_snapshot)
        r = sf._eq4snapshot_(lhs_snapshot, rhs_snapshot)
        check_type_is(bool, r)
        return r




    def __call__(sf, st, /):
        'st -> st'
        snapshot = sf.state2snapshot(st)
        while 1:
            st_ = sf._step4closure_(st)
            snapshot_ = sf.state2snapshot(st_)
            if sf._eq4snapshot_(snapshot, snapshot_): break
            st = st_
            snapshot = snapshot_
        return st


