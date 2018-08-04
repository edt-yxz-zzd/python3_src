

# BT - B:BNF-like; T:template
# BCT - B:BNF-like; C:constructor; T:template


GrammarBT_in_GrammarBT = '''
# this is a comment
# every Nonterminal should be defined
# null rule : "A := ;"
# dead rule : "A : ;"

@start_symbol GrammarBT
@terminals:
    at_start_symbol # @start_symbol
    at_terminals    # @terminals
    rule_body_begin # =
    body_begin      # :
    body_end        # ;
    symbol          # r"\w+"
    call_begin      # (
    call_end        # )
    args_sep        # ,
    ;


GrammarBT := Star(Statement) ;

Statement:
    = at_start_symbol StartSymbol
    = at_terminals body_begin Star(Terminal) body_end
    = TemplateDecl body_begin Star(RuleBody) body_end
    ;

RuleBody := rule_body_begin Star(ESymbol) ;
TemplateDecl:
    = Template call_begin StarArgs(Symbol, args_sep) call_end
    = Nonterminal
    ;

ESymbol:
    = Symbol
    = Template call_begin StarArgs(Star(ESymbol), args_sep) call_end
    ;

StartSymbol := Nonterminal ;
Nonterminal := Symbol ;
Terminal := Symbol ;
Template := Symbol ;
Symbol := symbol ;

Star(a):
    = a Star(a)
    =
    ;


StarArgs(a, sep):
    = a Star(sep a)
    =
    ;
'''




GrammarBT_AST_in_Haskell = '''
-- AbstractSyntaxTree of GrammarBT
---- not DerivationTree
type GrammarBT_AST a = [GrammarBT_Stmt a]
data GrammarBT_Stmt a = GrammarBT_StartSymbol a
                      | GrammarBT_Terminals (Set a)
                      | GrammarBT_Rule (GrammarBT_TemplateDecl a) (Set [GrammarBT_TemplateCall a])
GrammarBT_TemplateDecl a = GrammarBT_TemplateDecl a (Maybe [a])
GrammarBT_TemplateCall a = GrammarBT_TemplateCall a (Maybe [[GrammarBT_TemplateCall a]])

'''

GrammarBT_SemanticObj_in_Haskell = '''
-- SemanticObj = parse result
data GrammarBT_SemanticObj a = GrammarBT_SemanticObj {
                                    start_symbol :: a, -- (a, 0)
                                    # (a, Int) -- num_args::Int
                                    symbol2rule :: Map (a, Int) (Maybe (Set [GrammarBT_TemplateCall_SemanticObj a]))
                                }
GrammarBT_TemplateCall_SemanticObj a = (Either a Int, [[GrammarBT_TemplateCall_SemanticObj (Either a Int)]])

'''



