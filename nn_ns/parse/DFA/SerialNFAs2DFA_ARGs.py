
from .To_DFA_ARGs_INTERFACE import FAs2DFA_ARGs_INTERFACE

def _none_or_call(func, none):
    if none == None:
        return None
    return func(none)

class SerialNFAs2DFA_ARGs(FAs2DFA_ARGs_INTERFACE):
    def __init__(self, fa_ls):
        assert len(fa_ls)
        assert all(isinstance(fa, NFA) for fa in fa_ls)
        
        super().__init__(fa_ls)
        
        N = len(fa_ls)
        self.__first_ls = tuple((fa_ls[0] if i == 0 else None) for i in range(N))
        pass

    def get_initial(self):
        q0 = tuple(_none_or_call(lambda fa:fa.get_initial(), fa)
                   for fa in self.__first_ls)
        return q0
    def get_default(self, q):
        FA_ls = self.get_FAs()
        fail = tuple(_none_or_call(fa.get_default, qx) for fa, qx in zip(FA_ls, q))
        return fail
    def get_transition_symbols(self, q):
        FA_ls = self.get_FAs()
        syms = set().union(_none_or_call(fa.get_transition_symbols, qx)
                           for fa, qx in zip(FA_ls, q))
        return syms

    
    def get_next(self, q, sym):
        FA_ls = self.get_FAs()
        next_ = list(_none_or_call(lambda qx:fa.next(qx, sym), qx)
                     for fa, qx in zip(FA_ls, q))
        
        for i in range(len(next_) - 1):
            nfa = NFA_ls[i]
            qx = next_[i]

            # i.final -> zero move to -> i+1.initial
            if nfa.is_final(qx):
                nfa_right = NFA_ls[i+1]
                q0_right = nfa_right.get_initial()
                
                q_right = next_[i+1]
                if q_right == None:
                    q_right = frozenset()

                q_right = q_right | q0_right
                next_[i+1] = q_right
                
        return tuple(next_)

    

    def get_state(self):
        FA_ls = self.get_FAs()
        state = tuple(_none_or_call(lambda fa:fa.get_state(), fa)
                      for fa in self.__first_ls)
        return state

    def state_key(self, q):
        FA_ls = self.get_FAs()
        assert len(FA_ls) == len(q)
        
        return tuple(_none_or_call(fa.state_key, qx) for fa, qx in zip(FA_ls, q))
    pass

