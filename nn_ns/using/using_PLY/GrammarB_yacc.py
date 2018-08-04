

from .defs import GrammarB_in_GrammarB
from sand import CompileError

# Get the token map from the lexer.  This is required.
from .GrammarB_lex import tokens
from .parse_common import *






# main should be first or using start=...
start = 'GrammarB'
def p_GrammarB(p):
    'GrammarB : StatementStar'
    nonterminal2right_parts = set_defaultfactory_attr(p.parser, 'nonterminal2right_parts', dict)
    terminals = set_defaultfactory_attr(p.parser, 'terminals', set)
    start_symbol = set_default_attr(p.parser, 'start_symbol')
    p[0] = start_symbol, terminals, nonterminal2right_parts

    if terminals & set(nonterminal2right_parts):
        raise CompilerError('both terminal/nonterminal : {}'
                            .format(terminals & set(nonterminal2right_parts)))

    


def p_SetStartSymbolStmt(p):
    'Statement : AT_START_SYMBOL StartSymbol'
    set_default_attr(p.parser, 'start_symbol', p[2])
    p[0] = None

def p_ImportTerminals(p):
    'Statement : AT_TERMINALS BODY_BEGIN TerminalStar BODY_END'
    terminals = set_defaultfactory_attr(p.parser, 'terminals', set)
    terminals.update(iter_leftward_list(p[3]))
    p[0] = None



def p_RuleBody(p):
    'RuleBody : RULE_BODY_BEGIN SymbolStar'
    p[0] = tuple(leftward_list2list(p[2]))
def p_DefineRule(p):
    'Statement : Nonterminal BODY_BEGIN RuleBodyStar BODY_END'
    terminals = set_defaultfactory_attr(p.parser, 'terminals', set)
    nonterminal2right_parts = set_defaultfactory_attr(p.parser, 'nonterminal2right_parts', dict)
    nonterminal = p[1]
    right_parts = set(leftward_list2list(p[3]))
    if nonterminal in nonterminal2right_parts:
        raise CompileError('multi definitions : {}'.format(nonterminal))
    elif nonterminal in terminals:
        raise CompileError('redefine terminal to a nonterminal: {}'.format(nonterminal))
    nonterminal2right_parts[nonterminal] = right_parts
    p[0] = None
















def p_copy_rule(p):
    '''
StartSymbol : Nonterminal
Nonterminal : Symbol
Terminal : Symbol

Symbol : SYMBOL
'''
    return handle_alt_rule(p)



SCO_basics = 'Statement Symbol Terminal RuleBody'.split()
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
    import nn_ns.using.using_PLY.GrammarB_lex as lex_module
    source = GrammarB_in_GrammarB
    return parse(lex_module, __name__, source)

def test_parser_error():
    source = ('''
A:= B ;
 =
''')
    import nn_ns.using.using_PLY.GrammarB_lex as lex_module
    try:
        parse(lex_module, __name__, source)
    except Exception as e:
        try:
            assert str(e) == "fail at line:3, column:2, lexpos:10, total:12, token:LexToken(RULE_BODY_BEGIN,'=',1,10)"
        except:
            print(e)
            raise
    else:
        raise logic-error
    
def test_parser_error_EOF():
    source = ('''
A:= B ;
 A
''')
    import nn_ns.using.using_PLY.GrammarB_lex as lex_module
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
    



