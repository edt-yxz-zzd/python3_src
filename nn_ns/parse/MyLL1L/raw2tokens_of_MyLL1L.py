
from .raw2tokens import *

def raw2tokens_of_MyLL1L(raw_tokens, source_string):
    type_map = {
        'block': 'b',
        'string': 's',
        'spacesButNewline': ' ',
        'comment': '#',
        'newlines': '\n',
        'indent': '\t'
    }

    tokens = raw2tokens(raw_tokens, source_string)
    tokens = discardFalseType(tokens)
    convert_type(tokens, type_map)
    tokens = addNewLine(tokens)

    for t in tokens: assert len(t.type) == 1

    string = ''.join(t.type for t in tokens)
    tokens, string = mergeTokens(tokens, string, r'[bs]+', 'B')
    tokens, string = discardTokens(tokens, string, r'(?<=\n)[\t #\n]*\n') # empty line except BEGIN
    tokens, string = discardTokens(tokens, string, r'[ #]+') # remove spaces and comment
    tokens, string = discardTokens(tokens, string, r'^\n+')

    tokens, string = insert_indents(tokens, string)
    if string: assert string[0] != '\n'

    newType = set('is = , ? * + { }'.split())
    for t in tokens:
        if t.type == 'B':
            if t.value in newType:
                t.type = t.value
    return tokens



if __name__ == '__main__':
    print('test: to try tokenize_of_MyLL1L')
            
