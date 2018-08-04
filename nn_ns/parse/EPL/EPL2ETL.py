

from MyLL1L.Token import Token
from ETL.parse_result2ETL import is_parse_result_ETL, parse_result2ETL, \
     is_tuple_of_str
from .parse_result2EPL import is_parse_result_EPL, parse_result2EPL
from .ToolChain_MyLL1L_of_EPL import toolchain_EPL

from .parse_EPL import parse_EPL
from ETL.parse_ETL import parse_ETL

from EPL_in_MyLL1L import example_EPL


def EPL2ETL(src):
    r = parse_EPL(src)
    r = parse_result_EPL2parse_result_ETL(r)
    return parse_result2ETL(r)

def ETL2EPL(src):
    r = parse_ETL(src)
    r = parse_result_ETL2parse_result_EPL(r)
    #print('parse_result_EPL', r)
    return parse_result2EPL(r)



_open = ('[',)
_close = (']',)
def _epl_strs2etl_tokens(strs):
    assert isinstance(strs,tuple)
    return (('w', s) for s in strs)
def parse_result_EPL2parse_result_ETL(r):
    if not is_parse_result_EPL(r):
        raise ValueError('not is_parse_result_EPL')

    this_f = parse_result_EPL2parse_result_ETL
    name, tag, subitems = r
    
    ls = [_open]
    ls.extend(_epl_strs2etl_tokens(name))
    
    for sub in subitems:
        ls.extend(this_f(sub))
        
    ls.append(_close)
    ls.extend(_epl_strs2etl_tokens(tag))

    return ls








############################################


def is_parse_item_ETL_of_token_EPL(t):
    if not is_tuple_of_str(t):
        return False
    if not (1 <= len(t) <= 2):
        return False
    
    if len(t) == 1:
        token_type, = t
        return len(token_type) == 1 and token_type in ['[', ']']
    elif len(t) == 2:
        token_type, value = t
        return token_type == 'w'
    
    raise never-here


def parse_item_ETL2token_EPL(t):
    if not is_parse_item_ETL_of_token_EPL(t):
        raise ValueError('not is_parse_item_ETL_of_token_EPL')
    if not (1 <= len(t) <= 2):
        return False
    
    if len(t) == 1:
        token_type, = t
        value = token_type
        assert token_type in ['[', ']']
    elif len(t) == 2:
        token_type, value = t
        assert token_type == 'w'

    return Token(token_type, begin = 0, end = 0, value = value)



def is_parse_result_ETL_of_tokens_EPL(r):
    if not is_parse_result_ETL(r):
        return False

    check = is_parse_item_ETL_of_token_EPL
    return all(check(t) for t in r)

def parse_result_ETL2tokens_EPL(r):
    if not is_parse_result_ETL_of_tokens_EPL(r):
        raise ValueError('not is_parse_result_ETL_of_tokens_EPL')

    T = parse_item_ETL2token_EPL
    return [T(t) for t in r]
    
def parse_result_ETL2parse_result_EPL(r):
    tokens_EPL = parse_result_ETL2tokens_EPL(r)
    #print('tokens_EPL', tokens_EPL)
    return toolchain_EPL.process_tokens(tokens_EPL)



def _test_EPL2ETL():
    for src0, ans0 in example_EPL:
        ans1 = parse_EPL(src0)
        assert ans1 == ans0
        
        etl_src = EPL2ETL(src0)
        src2 = ETL2EPL(etl_src)
        ans2 = parse_EPL(src2)
        
        if ans0 != ans2:
            print('etl',etl_src)
            print('src2', src2)
            print(ans0)
            print(ans2)
        assert ans0 == ans2
    pass

_test_EPL2ETL()

        
    

