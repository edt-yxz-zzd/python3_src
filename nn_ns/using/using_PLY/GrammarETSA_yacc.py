
#from sand.grammar.GrammarETSA_def import GrammarETSA_in_GrammarETSA
from .defs import GrammarETSA_in_GrammarETSA
from sand import CompileError
from .GrammarETSA_lex import tokens
from .parse_common import *
from sand.types.ToProcess import UnorderedSetOnce
from itertools import chain

##to_SCO = ToStarCrossOptionRule__PLY(Star='*', Cross='+', Option='?')
##set_PLY_star_doc = SetDocFrom(to_SCO.basics2star_rules)
##set_PLY_cross_doc = SetDocFrom(to_SCO.basics2cross_rules)
##set_PLY_option_doc = SetDocFrom(to_SCO.basics2option_rules)
##set_PLY_optioncross_rules = SetDocFrom(to_SCO.basics2optioncross_rules)
##



def is_plain_symbol(plain_or_extended_symbol):
    return plain_or_extended_symbol[-1:] not in '*+?'
def check_extended_symbol(extended_symbol):
    if is_plain_symbol(extended_symbol):
        raise ValueError('plain symbol not extended')
    
def extended_symbol2depends(extended_symbol):
    check_extended_symbol(extended_symbol)
    mark = extended_symbol[-1]
    ref = extended_symbol[:-1]
    if mark == '?':
        marks = []
    elif mark == '*':
        marks = ['+?']
    elif mark == '+':
        marks = ['*']
    else:
        raise logic-error

    if not is_plain_symbol(ref):
        yield ref
    for mark in marks:
        yield ref + mark

def extended_symbol2rule_body(extended_symbol, NullName):
    check_extended_symbol(extended_symbol)
    
    mark = extended_symbol[-1]
    ref = extended_symbol[:-1]
    if mark == '?':
        rule = frozenset([ref, NullName])
    elif mark == '*':
        rule = frozenset([ref + '+?'])
    elif mark == '+':
        rule = (ref, ref + '*')
    else:
        raise logic-error
    return rule


def inplace_complete_extended_gram_info(incomplete_gram_info, NullName):
    if not all(map(is_plain_symbol, incomplete_gram_info)):
        raise ValueError('has defined some non plain symbols!')

    undefined_extended_symbols = set()
    for rule in incomplete_gram_info.values():
        if rule is None:
            continue
        undefined_extended_symbols.update(
            extended_symbol
            for extended_symbol in rule
            if not is_plain_symbol(extended_symbol)
            )

    esym2rule = incomplete_gram_info
    def update(extended_symbol):
        assert extended_symbol not in esym2rule
        esym2rule[extended_symbol] = \
            extended_symbol2rule_body(extended_symbol, NullName)
        return extended_symbol2depends(extended_symbol)
        
    to_proc = UnorderedSetOnce(undefined_extended_symbols)
    to_proc.apply(update)

def to_all_symbols(symbol2rule, start_symbol=None):
    all_symbols = set() if start_symbol is None else {start_symbol}
    all_symbols.update(symbol2rule)
    all_symbols.update(chain.from_iterable(filter(None, symbol2rule.values())))
    return all_symbols

def insert_builtin_rules(builtin2rule, symbol2rule, start_symbol=None):
    all_symbols = to_all_symbols(symbol2rule, start_symbol)
    for builtin, rule in builtin2rule.items():
        if builtin in all_symbols:
            symbol2rule[builtin] = rule
    return

builtin_null = '@Null'
builtin_dead = '@Dead'
builtin2rule = {builtin_null: (), builtin_dead: frozenset()}
def inplace_complete_ETSA_symbol2rule(symbol2rule, start_symbol=None):
    inplace_complete_extended_gram_info(symbol2rule, builtin_null)
    insert_builtin_rules(builtin2rule, symbol2rule, start_symbol)
    
# main should be first or using start=...
start = 'GrammarETSA' # since Null above
def p_GrammarETSA(p):
    'GrammarETSA : StatementStar'
    # Illegal name 'Statement*' in rule 'GrammarETSA'
    symbol2rule = set_defaultfactory_attr(p.parser, 'symbol2rule', dict)
    start_symbol = set_default_attr(p.parser, 'start_symbol')
    inplace_complete_ETSA_symbol2rule(symbol2rule, start_symbol)
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
    'DefineSeqRule : Nonterminal SEQ_BEGIN ESymbolStar SEQ_END'
    handle_DefineRule(p, tuple)
def p_DefineAltRule(p):
    'DefineAltRule : Nonterminal ALT_BEGIN ESymbolStar ALT_END'
    handle_DefineRule(p, frozenset)

def p_ESymbol(p):
    'ESymbol : Symbol ExtendMarkStar'
    p[0] = p[1] + ''.join(leftward_list2list(p[2]))














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

ExtendMark  : STAR
            | CROSS
            | OPTION

'''
    return handle_alt_rule(p)





SCO_basics = 'Statement Terminal ESymbol ExtendMark'.split()
@set_PLY_star_doc(SCO_basics)
def p_star_rule(p):
    '''
Statement* : Statement+?
'''
    return handle_alt_rule(p)

@set_PLY_cross_doc(SCO_basics)
def p_cross_rule(p):
    '''
Statement+ : Statement Statement*
'''
    p[0] = (p[1], p[2])
@set_PLY_optioncross_doc(SCO_basics)
def p_optioncross_rule(p):
    '''
Statement+? : Statement+
    | Null
'''
    return handle_alt_rule(p)









def test_parser():
    import nn_ns.using.using_PLY.GrammarETSA_lex as lex_module
    source = GrammarETSA_in_GrammarETSA
    return parse(lex_module, __name__, source)

if __name__ == '__main__':
    from pprint import pprint
    pprint(test_parser())










