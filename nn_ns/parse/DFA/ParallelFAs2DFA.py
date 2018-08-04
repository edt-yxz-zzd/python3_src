
from .ParallelFAs2DFA_ARGs import ParallelFAs2DFA_ARGs
from .FAs2DFA_BASE import FAs2DFA_BASE

class ParallelFAs2DFA(FAs2DFA_BASE):
    def __init__(self, fa_ls):
        super().__init__(fa_ls, ParallelFAs2DFA_ARGs)
        pass
    pass

class OR_FAs(ParallelFAs2DFA):
    def is_final_substates(self, substates):
        fa_ls = self.get_FAs()
        return any(fa_ls(idx).is_final(state) for idx, state in enumerate(substates))

    pass

class AND_FAs(ParallelFAs2DFA):
    def is_final_substates(self, substates):
        fa_ls = self.get_FAs()
        return all(fa_ls(idx).is_final(state) for idx, state in enumerate(substates))

    pass
