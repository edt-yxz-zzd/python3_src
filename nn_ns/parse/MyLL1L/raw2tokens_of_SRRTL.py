
from .raw2tokens import *

def raw2tokens_of_SRRTL(raw_tokens, source_string):
    type_map = {
        'idstring': 'd',
        'id': 'i',
        'string': 's',
        'spaces': ' ',
        'comment': '#',
        'newlines': '\n',
        'indent': '\t', 
        "'='": '='
    }

    tokens = raw2tokens(raw_tokens, source_string)
    tokens = discardFalseType(tokens)
    convert_type(tokens, type_map)
    tokens = addNewLine(tokens)

    for t in tokens: assert len(t.type) == 1

    string = ''.join(t.type for t in tokens)
    tokens, string = discardTokens(tokens, string, '[ #]+') # remove spaces and comment
    tokens, string = mergeTokens(tokens, string, '[\t\n]*\n', '\n')
    tokens, string = discardTokens(tokens, string, r'^\n+')
    
    tokens, string = insert_indents(tokens, string)
    if string: assert string[0] != '\n'

    for k in ['newlines', 'indent', "'='"]:
        del type_map[k]
    type_map = reverseDict(type_map)
    convert_type_default(tokens, type_map)
    
    newType = set('otherwise return if goto call error ='.split())
    for t in tokens:
        if t.type == 'id':
            if t.value in newType:
                t.type = t.value
        elif t.type == "'='":
            raise
    return tokens



if __name__ == '__main__':
    print('test: to try tokenize_of_SRRTL')
    
