

from .to_DFA_Args import union_states

class To_DFA_ARGs_INTERFACE:
    def get_initial(self):raise NotImplementedError()
    def get_default(self, q):raise NotImplementedError()
    def get_transition_symbols(self, q):raise NotImplementedError()
    def get_next(self, q, sym):raise NotImplementedError()
    def get_state(self):raise NotImplementedError()
    def state_key(self, q):raise NotImplementedError()

    def to_DFA_Args(self):
        t = type(self)
        return union_states(self, t.get_initial, t.get_default,
                            t.get_transition_symbols, t.get_next,
                            t.get_state, state_key = self.state_key)
    pass


class FA2DFA_ARGs_INTERFACE(To_DFA_ARGs_INTERFACE):
    def __init__(self, fa):
        self.fa = fa
        super().__init__()
        pass

    def get_FA(self):
        return self.fa

    pass

class FAs2DFA_ARGs_INTERFACE(To_DFA_ARGs_INTERFACE):
    def __init__(self, fa_ls):
        assert len(fa_ls)
        
        self.fa_ls = fa_ls
        super().__init__()
        pass

    def get_FAs(self):
        return self.fa_ls
    pass



