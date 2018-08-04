
from MyLL1L.raw2tokens import *

def raw2tokens_of_ETL(raw_tokens, source_string):
    type_map = {
        'word': 'w',
        'string': 's',
        'spaces': ' ',
        'comment': '#',
        'separator': ',',
        'EOF': '$',
    }

    tokens = raw2tokens(raw_tokens, source_string)
    tokens = discardFalseType(tokens)
    convert_type(tokens, type_map)
    #insert_token(tokens, ',')

    assert all(len(t.type) == 1 for t in tokens)

    string = ''.join(t.type for t in tokens)
    tokens, string = discardTokens(tokens, string, r'[ #]+') # remove spaces and comment


    assert all(len(t.type) == 1 for t in tokens)
    assert all(t.type in 'ws,$' for t in tokens)
    assert tokens and tokens[-1].type == '$'
    assert all(t.type != '$' for t in tokens[:-1])
    return tokens



if __name__ == '__main__':
    print('test: to try tokenize_of_ETL')
            
