
from .GrammarETSA_def import GrammarETSA_in_GrammarETSA

# CNDFA - C:complex ; NDFA:nondeterministic finite automaton
GrammarCNDFA_in_GrammarETSA = '''
# state is PartialState
# type TotalState = Set PartialState
# CompleteState is TotalState which is a fix point under null-transitions
# not allow undefined states
@start_symbol GrammarCNDFA
@terminals {
    at_start_states # @start_states
    at_final_states # @final_states
    # seq_begin       # =
    seq_end         # ;
    alt_begin       # {
    alt_end         # }
    symbol          # r"\w+"
}

GrammarNDFA = SetStartStates SetFinalStates Rule* ;
SetStartStates = at_start_states StateSet ;
SetFinalStates = at_final_states StateSet ;
Rule = State RuleBodySet ;

RuleBody = EitherElemOrSet__Terminal? EitherElemOrSet__State seq_end ;

EitherElemOrSet__State {
    State
    StateSet
}
EitherElemOrSet__Terminal {
    Terminal
    TerminalSet
}


State { symbol }
Terminal { symbol }

RuleBodySet = alt_begin RuleBody* alt_end ;
StateSet = alt_begin State* alt_end ;
TerminalSet = alt_begin Terminal* alt_end ;

'''


GrammarCNDFA_AST_in_Haskell = '''
data GrammarCNDFA_AST s t = GrammarCNDFA_AST { start_states :: Set s
                                             , final_states :: Set s
                                             , uni_transition :: Map s (Set GrammarCNDFA_RuleBody)
                                             }
type GrammarCNDFA_RuleBody s t  = (Maybe (GrammarCNDFA_ETerminal t), GrammarCNDFA_EState s)
type EitherElemOrSet a = Either a (Set a)
type GrammarCNDFA_ETerminal = EitherElemOrSet
type GrammarCNDFA_EState = EitherElemOrSet

'''

GrammarCNDFA_SemanticObj_in_Haskell = '''
type GrammarCNDFA_SemanticObj = GrammarNDFA_SemanticObj

'''


