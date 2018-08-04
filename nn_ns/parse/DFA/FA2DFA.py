
from .FA2DFA_ARGs import FA2DFA_ARGs
from .To_DFA_BASE import FA2DFA_BASE

class FA2DFA(FA2DFA_BASE):
    def __init__(self, fa):
        super().__init__(FA2DFA_ARGs, fa)
        pass
    pass


