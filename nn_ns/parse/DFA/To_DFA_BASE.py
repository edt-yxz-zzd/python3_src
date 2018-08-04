
from .To_DFA_ARGs_INTERFACE import \
     To_DFA_ARGs_INTERFACE, FA2DFA_ARGs_INTERFACE, FAs2DFA_ARGs_INTERFACE
from .DFA import DFA


class To_DFA_BASE(DFA):
    def __init__(self, To_DFA_ARGs, *args):
        #assert issubclass(To_DFA_ARGs, To_DFA_ARGs_INTERFACE)
        assert type(args) == tuple
        
        transitions, defaults, state0, state, \
                     new_state2old_state, old_state2new_state\
                     = To_DFA_ARGs(*args).to_DFA_Args()

        

        self._args = (To_DFA_ARGs,) + args
        self.new_state2old_state = new_state2old_state
        self.old_state2new_state = old_state2new_state
        
        final = self.__calc_final_ls(new_state2old_state)
        super().__init__(transitions, defaults, state0, final)
        pass
    

    def get_args(self):
        return self._args
    def get_new_state2old_state(self):
        return self.new_state2old_state
    def get_old_state2new_state(self):
        return self.old_state2new_state
    def __calc_final_ls(self, old_states):
        final = tuple(self.is_final_old_state(q) for q in old_states)
        return final
    
    def is_final_old_state(self, old_state):
        args = self.get_args()
        raise NotImplementedError()

    pass



class FA2DFA_BASE(To_DFA_BASE):
    
    def __init__(self, FA2DFA_ARGs, fa):
        #assert issubclass(FA2DFA_ARGs, FA2DFA_ARGs_INTERFACE)
        self.fa = fa
        
        super().__init__(FA2DFA_ARGs, fa)
        pass
    

    def get_FA(self):
        return self.fa
    
    def is_final_old_state(self, old_state):
        fa = self.get_FA()
        return fa.is_final(old_state)

    pass

    
   
    
    
class FAs2DFA_BASE(To_DFA_BASE):
    
    def __init__(self, FAs2DFA_ARGs, fa_ls):
        #assert issubclass(FAs2DFA_ARGs, FAs2DFA_ARGs_INTERFACE)
        assert len(fa_ls) > 1
        self.fa_ls = fa_ls
        
        super().__init__(FAs2DFA_ARGs, fa_ls)
        pass
    

    def get_FAs(self):
        return self.fa_ls
    def get_substates2state(self):
        return self.get_old_state2new_state()
    def get_state2substates(self):
        return self.get_new_state2old_state()
    
    def is_final_old_state(self, old_state):
        return self.is_final_substates(old_state)
    
    def is_final_substates(self, substates):
        fa_ls = self.get_FAs()
        raise NotImplementedError()
    
   
