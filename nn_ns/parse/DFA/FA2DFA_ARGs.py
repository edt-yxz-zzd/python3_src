
from .To_DFA_ARGs_INTERFACE import FA2DFA_ARGs_INTERFACE

class FA2DFA_ARGs(FA2DFA_ARGs_INTERFACE):
    def get_initial(self):
        return self.get_FA().get_initial()
    def get_default(self, q):
        return self.get_FA().get_default(q)
    def get_transition_symbols(self, q):
        return self.get_FA().get_transition_symbols(q)
    def get_next(self, q, sym):
        return self.get_FA().get_next(q, sym)

    def get_state(self):
        return self.get_FA().get_state()

    def state_key(self, q):
        return self.get_FA().state_key(q)
    pass
