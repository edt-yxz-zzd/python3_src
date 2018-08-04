
# ETSA - E:extended; T:terminal_rule; S:seq_nonterminal_rule; A:alt_nonterminal_rule
GrammarETSA_in_GrammarETSA = '''
# this is a comment
# every Nonterminal should be defined
# GrammarETSA will allow Symbol[+*?]; @Null; @Dead

@start_symbol GrammarETSA # the first one wins; follows are ignored
@terminals {
    at_start_symbol # @start_symbol
    at_terminals    # @terminals
    seq_begin       # =
    seq_end         # ;
    alt_begin       # {
    alt_end         # }
    symbol          # r"\w+|@Null|@Dead"
    star            # * 
    cross           # +
    option          # ?
}

GrammarETSA { Statement* }

Statement {
    SetStartSymbolStmt
    ImportTerminals
    DefineSeqRule
    DefineAltRule
}

SetStartSymbolStmt = at_start_symbol StartSymbol ;
ImportTerminals = at_terminals alt_begin Terminal* alt_end ;
DefineSeqRule = Nonterminal seq_begin ESymbol* seq_end ;
DefineAltRule = Nonterminal alt_begin ESymbol* alt_end ;

StartSymbol { Nonterminal }
Nonterminal { Symbol }
Terminal { Symbol }
Symbol { symbol }
ESymbol = Symbol ExtendMark* ;
ExtendMark {
    star            # * 
    cross           # +
    option          # ?
}


'''


GrammarETSA_AST_in_Haskell = '''
-- AbstractSyntaxTree of GrammarETSA
---- not DerivationTree
data ESymbol a  = Plain a
                | Star (ESymbol a)
                | Cross (ESymbol a)
                | Option (ESymbol a)

type GrammarETSA_AST a = GrammarTSA_AST (ESymbol a)

'''

GrammarETSA_SemanticObj_in_Haskell = '''
-- SemanticObj = parse result
type GrammarETSA_SemanticObj a = GrammarTSA_SemanticObj (ESymbol a)

'''





