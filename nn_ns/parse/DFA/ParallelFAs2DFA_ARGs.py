
from .To_DFA_ARGs_INTERFACE import FAs2DFA_ARGs_INTERFACE

class ParallelFAs2DFA_ARGs(FAs2DFA_ARGs_INTERFACE):
    def get_initial(self):
        FA_ls = self.get_FAs()
        q0 = tuple(fa.get_initial() for fa in FA_ls)
        return q0
    def get_default(self, q):
        FA_ls = self.get_FAs()
        fail = tuple(fa.get_default(qx) for fa, qx in zip(FA_ls, q))
        return fail
    def get_transition_symbols(self, q):
        FA_ls = self.get_FAs()
        syms = set().union(fa.get_transition_symbols(qx) for fa, qx in zip(FA_ls, q))
        return syms
    def get_next(self, q, sym):
        FA_ls = self.get_FAs()
        next_ = tuple(fa.next(qx, sym) for fa, qx in zip(FA_ls, q))
        return next_

    def get_state(self):
        FA_ls = self.get_FAs()
        state = tuple(fa.get_state() for fa in FA_ls)
        return state

    def state_key(self, q):
        FA_ls = self.get_FAs()
        state_tuple = q
        assert len(FA_ls) == len(state_tuple)
        
        return tuple(fa.state_key(state) for fa, state in zip(FA_ls, state_tuple))
    pass
