
from .GrammarETSA_def import GrammarETSA_in_GrammarETSA

# NDFA - nondeterministic finite automaton
GrammarNDFA_in_GrammarETSA = '''
# state is PartialState
# type TotalState = Set PartialState
# CompleteState is TotalState which is a fix point under null-transitions
# allow undefined states which are dead states
@start_symbol GrammarNDFA
@terminals {
    at_start_states # @start_states
    seq_begin       # =
    seq_end         # ;
    alt_begin       # {
    alt_end         # }
    symbol          # r"\w+"
}

GrammarNDFA = SetStartStates Rule* ;
SetStartStates = at_start_states alt_begin State* alt_end ;

Rule {
    NullTransitionRule
    TransitionRule
    FinalRule
}


NullTransitionRule = State seq_begin State seq_end ;
TransitionRule = State seq_begin Terminal State seq_end ;
FinalRule = State seq_begin seq_end ;
State { symbol }
Terminal { symbol }

'''


GrammarNDFA_AST_in_Haskell = '''
data GrammarNDFA_AST s t = GrammarNDFA_AST { start_states :: Set s
                                           , rules :: Set (GrammarNDFA_Rule s t)}
data GrammarNDFA_Rule s t   = GrammarNDFA_NullTransitionRule s s
                            | GrammarNDFA_TransitionRule s t s
                            | GrammarNDFA_FinalRule s

'''

GrammarNDFA_SemanticObj_in_Haskell = '''
data GrammarNDFA_SemanticObj s t = GrammarNDFA_SemanticObj {
                                        start_states :: Set s,
                                        final_states :: Set s,
                                        transition :: Map s (Map t (Set s)),
                                        null_transition :: Map s (Set s)}

'''


