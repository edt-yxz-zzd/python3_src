

__all__ = '''
    ComplementFSM
    NullFSM
    null_fsm
    
    ToNFSM
    UnionFSM
    ConcatFSM
'''.split()


from .FSM_prime import *
from Set_Dict_Pair import empty_set, set_union


class ComplementFSM(WrapFSM):
    'State = UnderlyState'
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        return not self.fsm.is_final(state)
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        return False



class NullFSM(RawFSM_ABC):
    def __init__(self):
        pass
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        return 0
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        # union or intersection or should be equal??
        # since I donot known universal set, so, union...
        return empty_set
    def step(self, state, symbol):
        ''':: FSM -> FSM State -> Symbol -> FSM State'''
        return 1
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        return state == 0
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        return state != 0

null_fsm = NullFSM()




class ToNFSM(RawFSM_ABC):
    'State = Set UnderlyState; used in ConcatFSM'
    def __init__(self, fsm):
        self.fsm = fsm
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        return frozenset([self.fsm.calc_initial()])
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        return self.fsm.calc_alphabet()
    def step(self, state, symbol):
        ''':: FSM -> FSM State -> Symbol -> FSM State'''
        assert is_Set(state)
        return frozenset(self.fsm.step(q, symbol) for q in state)
    
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        assert is_Set(state)
        return any(self.fsm.is_final(q) for q in state)
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        assert is_Set(state)
        return all(self.fsm.is_error(q) for q in state)





    
class UnionFSM(RawFSM_ABC):
    @classmethod
    def __count_total2final__(cls, count, total):
        assert 0 <= count <= total
        return bool(count)
    @classmethod
    def __count_total2error__(cls, count, total):
        assert 0 <= count <= total
        return bool(count == total)
    def __init__(self, fsms, *, count_total2final = None, count_total2error = None):
        'count_total2final :: Integer -> Integer -> Bool'
        if count_total2final is None:
            count_total2final = type(self).__count_total2final__
        if count_total2error is None:
            count_total2error = type(self).__count_total2error__
        self.fsms = tuple(fsms)
        self.count_total2final = count_total2final
        self.count_total2error = count_total2error
        
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        return tuple(fsm.calc_initial() for fsm in self.fsms)
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        # union or intersection or should be equal??
        # ConcatFSM([]) ==>> alphabet == {}, so...
        return set_union(fsm.calc_alphabet() for fsm in self.fsms)
    def step(self, state, symbol):
        ''':: FSM -> FSM State -> Symbol -> FSM State'''
        assert len(state) == len(self.fsms)
        return tuple(fsm.step(q, symbol) for q, fsm in zip(state, self.fsms))
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        assert len(state) == len(self.fsms)
        total = len(state)
        count = sum(fsm.is_final(q) for q, fsm in zip(state, self.fsms))
        return bool(self.count_total2final(count, total))
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        assert len(state) == len(self.fsms)
        total = len(state)
        count = sum(fsm.is_error(q) for q, fsm in zip(state, self.fsms))
        return bool(self.count_total2error(count, total))

    

def get_args(*args):
    return args


class ConcatFSM(RawFSM_ABC):
    'State == (fsms[0].state...)'
    def __init__(self, fsms):
        f = ToNFSM
        self.nfsms = tuple(map(f, get_args(null_fsm, *fsms)))
        assert self.nfsms
        
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        state = [empty_set]*len(self.nfsms)
        state[0] = self.nfsms[0].calc_initial()
        return tuple(state)
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        # union or intersection or should be equal??
        return set_union(fsm.calc_alphabet() for fsm in self.nfsms)
    def step(self, state, symbol):
        ''':: FSM -> FSM State -> Symbol -> FSM State'''
        assert len(state) == len(self.nfsms)
        ls = []
        prev_finals = False
        for q, nfsm in zip(state, self.nfsms):
            if prev_finals:
                q |= nfsm.calc_initial()
            q = nfsm.step(q, symbol)
            ls.append(q)

            prev_finals = nfsm.is_final(q)

        state = tuple(ls)
        assert len(state) == len(self.nfsms)
        return state
    
                
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        assert len(state) == len(self.nfsms)
        
        return self.nfsms[-1].is_final(state[-1])
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        return all(nfsm.is_error(q) for q, nfsm in zip(state, self.nfsms))
    
    
    
