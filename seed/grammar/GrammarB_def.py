

# B - BNF-style

GrammarB_in_GrammarB = '''
# this is a comment
# every Nonterminal should be defined
# null rule : "A := ;"
# dead rule : "A : ;"

@start_symbol GrammarB
@terminals:
    at_start_symbol # @start_symbol
    at_terminals    # @terminals
    rule_body_begin # =
    body_begin      # :
    body_end        # ;
    symbol          # r"\w+"
    ;


GrammarB := StatementStar ;

Statement:
    = at_start_symbol StartSymbol
    = at_terminals body_begin TerminalStar body_end
    = Nonterminal body_begin RuleBodyStar body_end
    ;

RuleBody := rule_body_begin SymbolStar ;

StartSymbol := Nonterminal ;
Nonterminal := Symbol ;
Terminal := Symbol ;
Symbol := symbol ;

StatementStar:
    = Statement StatementStar
    =
    ;
SymbolStar:
    = Symbol SymbolStar
    =
    ;
RuleBodyStar:
    = RuleBody RuleBodyStar
    =
    ;
TerminalStar:
    = Terminal TerminalStar
    =
    ;

'''




GrammarB_AST_in_Haskell = '''
-- AbstractSyntaxTree of GrammarB
---- not DerivationTree
type GrammarB_AST a = [GrammarB_Stmt a]
data GrammarB_Stmt a = GrammarB_StartSymbol a
                     | GrammarB_Terminals (Set a)
                     | GrammarB_Rule a (Set [a])
'''

GrammarB_SemanticObj_in_Haskell = '''
-- SemanticObj = parse result
data GrammarB_SemanticObj a = GrammarB_SemanticObj {
                                    start_symbol :: a,
                                    symbol2rule :: Map a (Maybe (Set [a]))
                                }


'''

'''
NonterminalRule = (Nonterminal, Set [Symbol]) = (LeftPart, RightPart)
TotalRule = (Symbol, Maybe (Set [Symbol]))

start_symbol :: a
terminals :: Set a
nonterminal2rules :: Map a (Set [a])
'''















