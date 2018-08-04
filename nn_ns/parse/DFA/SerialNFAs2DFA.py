
from .SerialNFAs2DFA_ARGs import SerialNFAs2DFA_ARGs, _none_or_call
from .FAs2DFA_BASE import FAs2DFA_BASE

class SerialNFAs2DFA(FAs2DFA_BASE):
    def __init__(self, nfa_ls, final_NFA_indices):
        self.final_NFA_indices = tuple(final_NFA_indices)
        super().__init__(nfa_ls, SerialNFAs2DFA_ARGs)
        pass
    def get_final_NFA_indices(self):
        return self.final_NFA_indices

    def is_final_substates(self, substates):
        fa_ls = self.get_FAs()
        final_NFA_indices = self.get_final_NFA_indices()

        return any(_none_or_call(fa_ls[idx].is_final, states[idx])
                   for idx in final_NFA_indices)

    pass

class CONCAT_NFAs_FinalFromIdx(SerialNFAs2DFA):
    def __init__(self, nfa_ls, final_from_idx):
        N = len(nfa_ls)
        assert -N <= final_from_idx < N

        
        if final_from_idx < 0:
            final_from_idx += N
        assert 0 <= final_from_idx < N
        
        final_NFA_indices = range(final_from_idx, len(nfa_ls))
        super().__init__(nfa_ls, final_NFA_indices)
        
        pass
    
    pass



class CONCAT_NFAs_FinalAll(CONCAT_NFAs_FinalFromIdx):
    def __init__(self, nfa_ls):
        super().__init__(nfa_ls, 0)
        pass
    pass


class CONCAT_NFAs_FinalLast(CONCAT_NFAs_FinalFromIdx):
    def __init__(self, nfa_ls):
        super().__init__(nfa_ls, -1)
        pass
    pass









        
        
