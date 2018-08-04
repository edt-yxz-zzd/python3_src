

'''
FSM - total # i.e. include error_state
DFA/NDFA - partial # i.e. exclude error_state

'''

__all__ = '''
    SimpleDFA
    SimpleNDFA

    collect_symbols_from_dfa_transition
    collect_maybe_symbols_from_ndfa_transition
'''.split()

from collections import defaultdict
from sand.types.ToProcess import FILOOnce, FIFOOnce
from sand.types.MultiIndicesSet import PairSet
from sand import repr_helper, nub
from .Maybe import *
from .Set_Dict_Pair import *
from .Dgraph import *




def is_NDFA_transition_key_type(obj):
    return is_Pair(obj) and is_Maybe(obj[1])
def is_NDFA_transition_key(obj, all_states, alphabet):
    return is_NDFA_transition_key_type(obj) and\
           obj[0] in all_states and is_Maybe_a(obj[1], alphabet)



            

class SimpleNDFA:
    '''

terms:
    SimpleNDFA Symbol State
    alphabet :: Set Symbol
    data Maybe a = () | (a,)
    transition :: Map (State, Maybe Symbol) (Set State)
    all_states, initials, finals :: Set State

'''
    def __init__(self, alphabet, all_states, initials, finals, transition):
        self.alphabet = alphabet
        self.all_states = all_states
        self._initials = initials
        self.finals = finals
        self.transition = transition

        assert initials <= all_states
        assert finals <= all_states
        assert all(map(is_NDFA_transition_key_type, transition.keys()))
        assert all(map(is_Set, transition.values()))

        is_key = lambda key: is_NDFA_transition_key(key, all_states, alphabet)
        assert all(val <= all_states for val in transition.values())
        assert all(map(is_key, transition.keys()))
        

    def shift_onestep(self, state, maybe_symbol):
        return self.transition.get((state, maybe_symbol), empty_set)
    def goto_onestep(self, current_states, maybe_symbol):
        assert current_states <= self.all_states
        im_states = set_union( # bug: "empty_set.union(" without "*"
            self.shift_onestep(state, maybe_symbol)
            for state in current_states)
        assert im_states <= self.all_states
        return im_states
    
    def complete_states(self, current_states):
        new_states = current_states
        while new_states:
            new_states = self.goto_onestep(new_states, ()) - current_states
            current_states = new_states | current_states
        return current_states
    def calc_initials(self):
        s = self.complete_states(self._initials)
        assert is_Set(s)
        return s

    def completed_goto(self, completed_current_states, maybe_symbol):
        'assume current_states == self.complete_states(current_states)'
        current_states = completed_current_states
        assert is_Maybe_a(maybe_symbol, self.alphabet)
        #assert current_states <= self.all_states

        # assert current_states == self.complete_states(current_states)
        if maybe_symbol == nothing:
            return current_states
        next_states = self.goto_onestep(current_states, maybe_symbol)
        next_states = self.complete_states(next_states)
        return next_states
    def goto(self, current_states, maybe_symbol):
        '''goto :: (Set State, Maybe Symbol) -> Set State

NOTE:
    current_states may not be complete
    e.g.
        when this ndfa was a elem of a ConcatFSM,
            if [final prev_elem] ==>>
                new_current_state = ndfa.calc_initials() | completed_prev_states
'''
        assert current_states <= self.all_states

        current_states = self.complete_states(current_states)
        return self.completed_goto(current_states, maybe_symbol)


    def is_final(self, current_states):
        return not self.finals.isdisjoint(current_states)

    def is_error(self, current_states):
        return not current_states

    def __repr__(self):
        return repr_helper(self, self.alphabet,
                           self.all_states, self._initials, self.finals,
                           self.transition)



def collect_key_states_from_ndfa_transition(ndfa_transition):
    ':: ndfa_transition -> Set State which present in keys'
    return frozenset(nd_state for (nd_state, _) in ndfa_transition.keys())

def collect_maybe_symbols_from_ndfa_transition(ndfa_transition):
    ':: Map (State, Maybe Symbol) (Set State) -> Map State (Set (Maybe Symbol))'
    return group_pairs2dict(ndfa_transition.keys())

def collect_symbols_from_dfa_transition(dfa_transition):
    ':: Map (State, Symbol) State -> Map State (Set Symbol)'
    return group_pairs2dict(dfa_transition.keys())

    
    
class SimpleDFA:
    '''

terms:
    SimpleDFA Symbol State
    alphabet :: Set Symbol
    data Maybe a = () | (a,)
    transition :: Map (State, Symbol) State
    all_states, finals :: Set State
    maybe_initial :: Maybe State
'''
    
    def __init__(self, alphabet, all_states, maybe_initial, finals, transition):
        self.alphabet = alphabet
        self.all_states = all_states
        self.maybe_initial = maybe_initial
        self.finals = finals
        self.transition = transition

        assert is_Maybe_a(maybe_initial, all_states)
        assert finals <= all_states


        def is_key(key):
            return is_Pair(key) and\
                   key[0] in all_states and\
                   key[1] in alphabet
        def is_val(val):
            return val in all_states
        assert all(map(is_key, transition.keys()))
        assert all(map(is_val, transition.values()))


    def calc_num_states(self):
        'NOTE: finals may not present in transitions'
        # bug: return len(self.transition)
        # bug: return len(set(self.transition) | self.finals)
        #      since tr.keys() is not states!!
        return len(set(s for s, _ in self.transition) | self.finals)

    def shift_onestep(self, curr_state, symbol):
        is_nothing = []
        next_state = self.transition.get((curr_state, symbol), is_nothing)
        if next_state is is_nothing:
            maybe_next_state = nothing
        else:
            maybe_next_state = (next_state,)
        return maybe_next_state
        
    def goto(self, maybe_state, symbol):
        'goto :: (Maybe State, Symbol) -> Maybe State'
        assert is_Maybe_a(maybe_state, self.all_states)
        assert symbol in self.alphabet

        if maybe_state == nothing:
            return nothing
        curr_state = unjust(maybe_state)
        return self.shift_onestep(curr_state, symbol)


    def is_final(self, maybe_state):
        assert is_Maybe(maybe_state)
        return maybe_state != nothing and maybe_state[0] in self.finals

    def is_error(self, maybe_state):
        return maybe_state == nothing

    def _get_args(self):
        return (self.alphabet,
                self.all_states, self.maybe_initial, self.finals,
                self.transition)
    def __repr__(self):
        return repr_helper(self, *self._get_args())









if __name__ == "__main__":
    import doctest
    doctest.testmod()

