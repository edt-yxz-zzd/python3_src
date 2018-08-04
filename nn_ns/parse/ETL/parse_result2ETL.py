

import re
from .ETL_in_SRRTL import word_pattern_ETL

_re_word_pattern_ETL = re.compile(word_pattern_ETL + '$')
def is_word_ETL(s):
    m = _re_word_pattern_ETL.match(s)
    return bool(m)

def repr_item_ETL(s):
    if is_word_ETL(s):
        return s
    return repr(s)

        
    



def is_list_of_tuple_of_str(r):
    return isinstance(r, list) and \
           all(is_tuple_of_str(v) for v in r)

def is_tuple_of_str(r):
    return isinstance(r, tuple) and \
           all(is_str(v) for v in r)

def is_str(r):
    return isinstance(r, str)

def is_parse_result_ETL(r):
    return len(r) and is_list_of_tuple_of_str(r)

def iterable2list(r):
    if isinstance(r, list):
        return r
    else:
        return list(r)


def _parse_result2ETL(r):
    r = iterable2list(r)
    if not is_parse_result_ETL(r):
        raise ValueError('not is_parse_result_ETL')

    ls = []
    for strs in r:
        tokens = ' '.join(repr_item_ETL(s) for s in strs)
        ls.append(tokens + ',')

    assert ls
    src = ' '.join(ls)
    return r, src
        

def parse_result2ETL(r):
    _, src = _parse_result2ETL(r)
    return src



