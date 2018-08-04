

__all__ = '''
    SimpleDFA2FSM
    SimpleNDFA2FSM
    fsm2dfa
'''.split()
from .FSM_prime import *
from .FSM_ex import *
from .FA_prime import *

from .Maybe import *
from .FA_transform import rename_dfa_states


class SimpleDFA2FSM(DFABufferedFSM_ABC):
    def __init__(self, dfa):
        self.dfa = dfa
        self.dfa_from_fsm = self._calc_dfa()
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        return self.dfa.maybe_initial
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        # union or intersection or should be equal??
        # since I donot known universal set, so, union...
        return self.dfa.alphabet
    def step(self, state, symbol):
        ''':: FSM -> FSM State -> Symbol -> FSM State'''
        return self.dfa.goto(state, symbol)
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        return self.dfa.is_final(state)
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        return self.dfa.is_error(state)

    def _calc_dfa(self):
        old2new = {old: just(old) for old in self.dfa.all_states}
        return rename_dfa_states(self.dfa, old2new)
    def get_dfa(self):
        return self.dfa_from_fsm

    
    

class SimpleNDFA2FSM(RawFSM_ABC):
    def __init__(self, ndfa):
        self.ndfa = ndfa
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        return self.ndfa.calc_initials()
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        # union or intersection or should be equal??
        # since I donot known universal set, so, union...
        return self.ndfa.alphabet
    def step(self, state, symbol):
        ''':: FSM -> FSM State -> Symbol -> FSM State'''
        # bug: return self.ndfa.goto(state, symbol)
        #      without "just"
        return self.ndfa.goto(state, just(symbol))
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        return self.ndfa.is_final(state)
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        return self.ndfa.is_error(state)



def fsm2dfa(fsm):
    assert isinstance(fsm, RawFSM_ABC)
    fsm = BasicBufferedFSM(fsm)
    fsm = DFABufferedFSM(fsm)
    return fsm.get_dfa()











