
# TSA - T:terminal_rule; S:seq_nonterminal_rule; A:alt_nonterminal_rule
GrammarTSA_in_GrammarTSA = '''
# this is a comment
# every Nonterminal should be defined
# GrammarETSA will allow Symbol[+*?]; @Null; @Dead

@start_symbol GrammarTSA # the first one wins; follows are ignored
@terminals {
    at_start_symbol # @start_symbol
    at_terminals    # @terminals
    seq_begin       # =
    seq_end         # ;
    alt_begin       # {
    alt_end         # }
    symbol          # r"\w+"
}

GrammarTSA { StatementStar }
Null = ;

Statement {
    SetStartSymbolStmt
    ImportTerminals
    DefineSeqRule
    DefineAltRule
}

SetStartSymbolStmt = at_start_symbol StartSymbol ;
ImportTerminals = at_terminals alt_begin TerminalStar alt_end ;
DefineSeqRule = Nonterminal seq_begin SymbolStar seq_end ;
DefineAltRule = Nonterminal alt_begin SymbolStar alt_end ;

StartSymbol { Nonterminal }
Nonterminal { Symbol }
Terminal { Symbol }
Symbol { symbol }


SymbolCross = Symbol SymbolStar ;
SymbolStar { SymbolCrossOption }
SymbolCrossOption {
    Null
    SymbolCross
}



TerminalCross = Terminal TerminalStar ;
TerminalStar { TerminalCrossOption }
TerminalCrossOption {
    Null
    TerminalCross
}


StatementCross = Statement StatementStar ;
StatementStar { StatementCrossOption }
StatementCrossOption {
    Null
    StatementCross
}

'''


GrammarTSA_AST_in_Haskell = '''
-- AbstractSyntaxTree of GrammarTSA
---- not DerivationTree
type GrammarTSA_AST a = [GrammarTSA_Stmt a]
data GrammarTSA_Stmt a  = GrammarTSA_StartSymbol a
                        | GrammarTSA_Terminals (Set a)
                        | GrammarTSA_SeqRule a [a]
                        | GrammarTSA_AltRule a (Set a)
'''

GrammarTSA_SemanticObj_in_Haskell = '''
-- SemanticObj = parse result
data GrammarTSA_SemanticObj a = GrammarTSA_SemanticObj {
                                    start_symbol :: a,
                                    symbol2rule :: Map a (GrammarTSA_RuleBody a)
                                }
data GrammarTSA_RuleBody a  = GrammarTSA_TerminalRuleBody
                            | GrammarTSA_SeqRuleBody [a]
                            | GrammarTSA_AltRuleBody (Set a)


'''





