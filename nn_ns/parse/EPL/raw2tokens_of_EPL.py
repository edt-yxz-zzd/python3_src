
from MyLL1L.raw2tokens import *

def raw2tokens_of_EPL(raw_tokens, source_string):
    type_map = {
        'word': 'w',
        'string': 's',
        'spaces': ' ',
        'comment': '#',
        'group': ',',
    }

    tokens = raw2tokens(raw_tokens, source_string)
    tokens = discardFalseType(tokens)
    convert_type(tokens, type_map)
    #insert_token(tokens, ',')

    assert all(len(t.type) == 1 for t in tokens)

    string = ''.join(t.type for t in tokens)
    tokens, string = discardTokens(tokens, string, r'[ #]+') # remove spaces and comment



    for t in tokens:
        if t.type == ',':
            t.type = t.value

    assert all(len(t.type) == 1 for t in tokens)     
    assert all(t.type in 'ws[]' for t in tokens)
    return tokens



if __name__ == '__main__':
    print('test: to try tokenize_of_EPL')
            
