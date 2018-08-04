


'''
A = alphabet = [0..M-1]
L <- PInt
sep <- alphabet^L
avoid_substring :: UInt -> [alphabet]
    # sep is not a substring of result
UInts
    <-[sep.join(map(avoid_substring, uints))]-> [alphabet]
    <-[radix accumulate]-> UInt

'''

class AvoidSubstringCounter:
    def __init__(self, M:'>=2', sep:'array([0..M-1]){len>=1}'):
    # state -> char -> state
    def shift_state(self, state, char:'in [0..M-1]'):
    # state -> Map state char   # where exclude the 0-state in result Map
    def state_branches(self, nonfinal_state:'<len(sep)'):

    def total_avoid_of_len_L_if_after_state(self, state:'UInt{<=len(sep)}', L:'UInt'):
        this_func = self.total_avoid_of_len_L_if_after_state
        if state == len(self.sep):
            return 0
        if L == 0:
            return 1
        # assume cJrng = (rng, [(char, rng)])
        #   rng maybe empty
        #   continue, i.e. ((h0..t0-1), [(t0, (t0+1..t1-1)), (t1, (t1+1...])
        #   complete, i.e. cover [0..M-1]
        #   ch in rng, shift state to 0
        #   ch not in rng, shift state to non-0
        non0state2char = self.state_branches(state)
        return sum(this_func(state, L-1) for state in non0state2char)\
            + (M - len(non0state2char)) * this_func(0, L-1)
