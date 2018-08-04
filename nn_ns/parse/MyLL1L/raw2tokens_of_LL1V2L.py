
from .raw2tokens import *

def raw2tokens_of_LL1V2L(raw_tokens, source_string):
    type_map = {
        'block': 'b',
        'string': 's',
        'spacesButNewline': ' ',
        'comment': '#',
        'newlines': '\n',
        'indent': '\t',
        'del_prev_newlines': '\\',
        
    }

    tokens = raw2tokens(raw_tokens, source_string)
    tokens = discardFalseType(tokens)
    convert_type(tokens, type_map)

    for t in tokens: assert len(t.type) == 1

    string = ''.join(t.type for t in tokens)
    tokens, string = mergeTokens(tokens, string, r'[bs]+', 'B')
    tokens, string = discardTokens(tokens, string, r'[ #]+') # remove spaces and comment
    tokens, string = discardTokens(tokens, string, r'[\t\n\\]*\\')
    tokens, string = discardTokens(tokens, string, r'^\n+')

    tokens, string = insert_indents(tokens, string)
    if string: assert string[0] != '\n'


    newType = set('concept is = , ? * + { } <- -> . :'.split())
    for t in tokens:
        if t.type == 'B':
            t.type = 'id'
            if t.value in newType:
                t.type = t.value
            elif t.value[:2] == '--':
                t.type = '--'

    return tokens

    
