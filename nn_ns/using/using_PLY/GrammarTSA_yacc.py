
#from sand.grammar.GrammarTSA_def import GrammarTSA_in_GrammarTSA
from .defs import GrammarTSA_in_GrammarTSA
from sand import CompileError

# Get the token map from the lexer.  This is required.
from .GrammarTSA_lex import tokens
from .parse_common import *













# main should be first or using start=...
start = 'GrammarTSA' # since Null above
def p_GrammarTSA(p):
    'GrammarTSA : StatementStar'
    symbol2rule = set_defaultfactory_attr(p.parser, 'symbol2rule', dict)
    start_symbol = set_default_attr(p.parser, 'start_symbol')
    p[0] = start_symbol, symbol2rule


def p_SetStartSymbolStmt(p):
    'SetStartSymbolStmt : AT_START_SYMBOL StartSymbol'
    set_default_attr(p.parser, 'start_symbol', p[2])
    p[0] = None

def p_ImportTerminals(p):
    'ImportTerminals : AT_TERMINALS ALT_BEGIN TerminalStar ALT_END'
    symbol2rule = set_defaultfactory_attr(p.parser, 'symbol2rule', dict)
    terminals = set(leftward_list2list(p[3]))
    defineds = set(symbol2rule) - terminals
    pre_nonterminals = [symbol2rule[t] is not None for t in defineds]
    if pre_nonterminals:
        raise CompileError('nonterminals redefined to terminals : {}'.format(pre_nonterminals))
    
    symbol2rule.update((t, None) for t in terminals)
    p[0] = None


def handle_DefineRule(p, container):
    symbol2rule = set_defaultfactory_attr(p.parser, 'symbol2rule', dict)
    symbol = p[1]
    rule = leftward_list2list(p[3])
    if symbol in symbol2rule:
        raise CompileError('multi definitions : {}'.format(symbol))
    symbol2rule[symbol] = container(rule)
    p[0] = None
    
def p_DefineSeqRule(p):
    'DefineSeqRule : Nonterminal SEQ_BEGIN SymbolStar SEQ_END'
    handle_DefineRule(p, tuple)
def p_DefineAltRule(p):
    'DefineAltRule : Nonterminal ALT_BEGIN SymbolStar ALT_END'
    handle_DefineRule(p, frozenset)














def p_copy_rule(p):
    '''

StartSymbol : Nonterminal
Nonterminal : Symbol
Terminal : Symbol

Symbol : SYMBOL
'''
    return handle_alt_rule(p)


##def p_Symbol(p):
##    'Symbol : SYMBOL'
##    p[0] = p[1].value # p[1] is already token.value
    
def p_alt_rule(p):
    '''
Statement   : SetStartSymbolStmt
            | ImportTerminals
            | DefineSeqRule
            | DefineAltRule

'''
    return handle_alt_rule(p)





SCO_basics = 'Statement Symbol Terminal'.split()
@set_PLY_star_doc(SCO_basics)
def p_star_rule(p):
    '''
StatementStar : StatementCrossOption
'''
    return handle_alt_rule(p)
##    # Illegal name '|' in rule 'StatementStar'
##    '''
##StatementStar : Null | StatementCross
##'''
##    # Syntax error in rule 'StatementStar'
##    '''
##StatementStar
##    : Null
##    | StatementCross
##'''
@set_PLY_cross_doc(SCO_basics)
def p_cross_rule(p):
    '''
StatementCross : Statement StatementStar
'''
    p[0] = (p[1], p[2])
@set_PLY_optioncross_doc(SCO_basics)
def p_optioncross_rule(p):
    '''
StatementCrossOption : StatementCross
    | Null
'''
    return handle_alt_rule(p)










def test_parser():
    import nn_ns.using.using_PLY.GrammarTSA_lex as lex_module
    source = GrammarTSA_in_GrammarTSA
    return parse(lex_module, __name__, source)

def test_parser_error():
    source = ('''
A = B ;
 =
''')
    import nn_ns.using.using_PLY.GrammarTSA_lex as lex_module
    try:
        parse(lex_module, __name__, source)
    except Exception as e:
        try:
            assert str(e) == "fail at line:3, column:2, lexpos:10, total:12, token:LexToken(SEQ_BEGIN,'=',1,10)"
        except:
            print(e)
            raise
    else:
        raise logic-error
    
def test_parser_error_EOF():
    source = ('''
A = B ;
 A
''')
    import nn_ns.using.using_PLY.GrammarTSA_lex as lex_module
    try:
        parse(lex_module, __name__, source)
    except Exception as e:
        try:
            assert str(e) == 'end-of-file'
        except:
            print(e)
            raise
    else:
        raise logic-error

test_parser()
test_parser_error()
test_parser_error_EOF()

if __name__ == '__main__':
    from pprint import pprint
    pprint(test_parser())
    



