
__all__ = '''
    RawFSM_ABC
    WrapFSM
    BasicBufferedFSM
    DFABufferedFSM_ABC
    DFABufferedFSM

'''.split()

from sand.types.ToProcess import FILOOnce
from sand import unsafe_last
from abc import ABCMeta, abstractmethod
from .Maybe import *
from .FA_prime import SimpleDFA


class RawFSM_ABC(metaclass=ABCMeta):
    '''FSM State = DFA (Maybe State) | NDFA (Set State) # completed ndfa states
'''
    @abstractmethod
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        raise NotImplementedError
    @abstractmethod
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        raise NotImplementedError
    @abstractmethod
    def step(self, state, symbol):
        ''':: FSM -> FSM State -> Symbol -> FSM State'''
        raise NotImplementedError
    @abstractmethod
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        raise NotImplementedError
    @abstractmethod
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        raise NotImplementedError

    
    #@abstractmethod
    def _state2symbols(self, state):
        ''':: FSM -> FSM State -> Iter Symbol'''
        yield from self.calc_alphabet() # may filter out those lead to error
    def _state2iter_symbol_states(self, state):
        ''':: FSM -> FSM State -> Iter (Symbol, FSM State)
-- for all symbols s.t. not is_error(step(state, symbol))'''
        for symbol in self._state2symbols(state):
            next_state = self.step(state, symbol)
            if not self.is_error(next_state):
                yield symbol, next_state
    def _state2symbol_states(self, state):
        ''':: FSM -> FSM State -> Set (Symbol, FSM State)
-- for all symbols s.t. not is_error(step(state, symbol))'''
        return frozenset(self._state2iter_symbol_states(state))
    

    def _state2next_states(self, state):
        ''':: FSM -> FSM State -> Set (FSM State) -- may not error next_state'''
        return frozenset(s for _, s in self._state2iter_symbol_states(state))
    def _make_reachable_dedges(self, states):
        states = (s for s in states if not self.is_error(s)) # bug: "if not is_error" without calling
        dedges = set()
        def to_nexts(state):
            nexts = self._state2next_states(state)
            dedges.update((state, n) for n in nexts)
            return nexts
        to_process = FILOOnce(states)
        to_process.apply(to_nexts)
        return dedges
        
        
    def _calc_reachable_states(self, states = None):
        if states is None:
            initial = self.calc_initial()
            states = [initial]

        states = frozenset(s for s in states if not self.is_error(s))
        #print(states, self.calc_initial())
        dedges = self._make_reachable_dedges(states)
        # bug: without "| states" ; if exists state in states s.t. no jumps
        return frozenset(v for d in dedges for v in d) | states
    

    def calc_all_states(self):
        return self._calc_reachable_states()
    def calc_finals(self):
        all_states = self.calc_all_states()
        return frozenset(filter(self.is_final, all_states)) # bug: once used "map" instead of "filter"
    def calc_partial_transition(self):
        all_states = self.calc_all_states()
        return {(state, symbol): next_state
                for state in all_states
                for symbol, next_state in self._state2iter_symbol_states(state)}
    def calc_dfa(self):
        initial = self.calc_initial()
        
        alphabet = self.calc_alphabet()
        all_states = self.calc_all_states()
        maybe_initial = just(initial) if initial in all_states else nothing
        finals = self.calc_finals()
        transition = self.calc_partial_transition()
        return SimpleDFA(alphabet, all_states, maybe_initial, finals, transition)
        
    def symbols2accepteds(self, symbols):
        alphabet = self.calc_alphabet()
        q = self.calc_initial()
        yield self.is_final(q)
        for symbol in symbols:
            assert symbol in alphabet
            q = self.step(q, symbol)
            yield self.is_final(q)

    def accepted(self, symbols):
        return unsafe_last(self.symbols2accepteds(symbols))




class WrapFSM(RawFSM_ABC):
    def __init__(self, fsm):
        self.fsm = fsm
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        return self.calc_initial()
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        return self.calc_alphabet()
    def step(self, state, symbol):
        ''':: FSM -> FSM State -> Symbol -> FSM State'''
        return self.fsm.step(state, symbol)
    def is_final(self, state):
        ''':: FSM -> FSM State -> Bool'''
        return self.fsm.is_final(state)
    def is_error(self, state):
        ''':: FSM -> FSM State -> Bool -- error if True else maybe_not_error'''
        return self.fsm.is_error(state)
        
class BasicBufferedFSM(WrapFSM):
    def __init__(self, fsm):
        self.fsm = fsm
        self.initial = fsm.calc_initial()
        self.alphabet = fsm.calc_alphabet()
    def calc_initial(self):
        ''':: FSM -> FSM State'''
        return self.initial
    def calc_alphabet(self):
        ':: FSM -> Set Symbol'
        return self.alphabet
        


class DFABufferedFSM_ABC(WrapFSM):
    @abstractmethod
    def get_dfa(self):
        raise NotImplementedError
    
    def calc_all_states(self):
        return self.get_dfa().all_states
    def calc_finals(self):
        return self.get_dfa().finals
    def calc_partial_transition(self):
        return self.get_dfa().transition
    def calc_dfa(self):
        return self.get_dfa()
    

class DFABufferedFSM(DFABufferedFSM_ABC):
    def __init__(self, fsm):
        self.fsm = fsm
        self.dfa = self.fsm.calc_dfa()
    def get_dfa(self):
        return self.dfa













