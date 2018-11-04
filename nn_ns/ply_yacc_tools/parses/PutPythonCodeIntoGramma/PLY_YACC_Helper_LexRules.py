


__all__ = '''
    PLY_YACC_Helper_LexRules
    terminals
    lex_postprocessor
    '''.split()


from .imports import (
    let_be_all_staticmethods
    ,LexPostprocessor
    ,lex_error_handle, token_error_handle
    )

import re

regex_flags = re.MULTILINE|re.VERBOSE



raw_tokens_only = '''
    CommentLine
    Newline
    '''.split()
terminals_only = []
common_of_terminals_and_raw_tokens = '''
    RuleName
    RuleBody
    PythonLine
    '''.split()
raw_tokens = raw_tokens_only + common_of_terminals_and_raw_tokens
terminals = terminals_only + common_of_terminals_and_raw_tokens




@let_be_all_staticmethods('t_')
class PLY_YACC_Helper_LexRules:
    START_STATE = 'INITIAL'
    tokens = raw_tokens
    states = ()
    def t_error(t):
        return lex_error_handle(t, '')

    def t_Newline(t):
        r'[\r\n]+'
        t.lexer.lineno += len(t.value)
        return None
    def t_CommentLine(t):
        r'^(?:[ ]{4})?(?:[#].*)$'
        return None
    def t_RuleName(t):
        r'^(?P<name>\w+)[ ]*(?:[#].*)?$'
        t.value = t.lexer.lexmatch.group('name')
        return t
    def t_RuleBody(t):
        r'^[ ]{4}(?=\S)(?P<body><>|(?=\S)[\w |]+)[ ]*(?:[#].*)?$'
        body = t.lexer.lexmatch.group('body').strip()
        if body == '<>':
            body = ''
        namess = eval_rule_body(body)
        t.value = namess # [[name]]
        return t
    def t_PythonLine(t):
        r'^[ ]{8}(?P<python>.*)$'
        t.value = t.lexer.lexmatch.group('python')
        return t
PLY_YACC_Helper_LexRules.regex_flags = regex_flags

lex_postprocessor = LexPostprocessor(
            PLY_YACC_Helper_LexRules
            , regex_flags=...
            , START_STATE=...
            , lex_postprocess_filter='echo'
            )

def eval_rule_body(body:str):
    # str -> [[name]]
    return [s.split() for s in body.split('|')]

if __name__ == '__main__':
    from .example import example
    tokenize = lex_postprocessor.tokenize
    print(tokenize(example))


