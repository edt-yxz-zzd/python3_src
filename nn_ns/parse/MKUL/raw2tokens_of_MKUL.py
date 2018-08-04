
from MyLL1L.raw2tokens import *

def raw2tokens_of_MKUL(raw_tokens, source_string):
    type_map = {
        'spaces': ' ',
        'word_comment': '#',
        'line_comment': '#',
        'multi_comment': '#',

        'hashable_call_on_bytes': 'H',
        'nonhashable_call_on_bytes': 'Q',
        'hashable_call_on_string': 'h',
        'nonhashable_call_on_string': '@',
        '{word[': '\\',
        '{word{': '"',
        
        'sep': ';',
        '{{': '`',
        '{[': '<',
        ']-': '>',
        '}-': '\'',

        'named_string': 'a',
        'named_str-' : '_',
        'named_bytes': 'A',
        'named_bstr-' : '^',
        'string': 's',
        'str-': '-',
        'bytes': '\0',
        'bstr-': '~',
        'word': 'w',
        
        'int': 'i',
        'float': 'f',
        'imag': 'm',
        'complex': 'c',
        '0none': 'n',
        '0bool': 'b',
        '0float': '!',
        '0imag': 'j',
        '0complex': 'C',
    }

    tokens = raw2tokens(raw_tokens, source_string)
    tokens = discardFalseType(tokens)

    for t in tokens:
        if t.type == 'sep' and len(t.value) > 1:
            t.type = t.value
    convert_type(tokens, type_map)
    for t in tokens:
        if t.type == ';':
            t.type = t.value

    assert all(len(t.type) == 1 for t in tokens)

    string = ''.join(t.type for t in tokens)
    tokens, string = discardTokens(tokens, string, r'[ #]+') # remove spaces and comment

    types = 'hH@Q_^-~aA\0swifmcnb!jC()[]{}="`\'\\<>'
    ts = set(types)
    assert len(types) == len(ts)
    assert all(len(t.type) == 1 for t in tokens)
    assert all(t.type in ts for t in tokens)
    return tokens



if __name__ == '__main__':
    print('test: to try tokenize_of_MKUL')
            
