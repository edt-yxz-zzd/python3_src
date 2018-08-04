


import re
from .EPL_in_SRRTL import word_pattern_EPL

_re_word_pattern_EPL = re.compile(word_pattern_EPL + '$')
def is_word_EPL(s):
    m = _re_word_pattern_EPL.match(s)
    return bool(m)

def repr_item_EPL(s):
    if is_word_EPL(s):
        return s
    return repr(s)

    


'''
    name_type = tag_type = tuple of str
    result_type = item_type = (name_type, tag_type, list of item_type)
'''


def is_tuple_of_str(r):
    return isinstance(r, tuple) and \
           all(is_str(v) for v in r)
is_name_type = is_tag_type = is_tuple_of_str


def is_str(r):
    return isinstance(r, str)

def is_list_of_item_type(r):
    return isinstance(r, list) and \
           all(is_item_type(v) for v in r)

def is_item_type(r):
    if not isinstance(r, tuple) and len(r) == 3:
        return False
    
    name, tag, ls = r
    return is_name_type(name) and is_tag_type(tag) and \
           is_list_of_item_type(ls)

def is_parse_result_EPL(r):
    return is_item_type(r)



def _strs_to_str(strs):
    return ' '.join(repr_item_EPL(s) for s in strs)

def _parse_result2EPL(r):

    name, tag, ls = r
    name = _strs_to_str(name)
    tag = _strs_to_str(tag)
    ls = ' '.join(_parse_result2EPL(item)[-1] for item in ls)
    src = '[{name} {ls}] {tag}'.format(name=name, tag=tag, ls=ls)
    return r, src
        

def parse_result2EPL(r):
    if not is_parse_result_EPL(r):
        raise ValueError('not is_parse_result_EPL')
    
    _, src = _parse_result2EPL(r)
    return src









##############################



def _parse_result2indent_lines_EPL(r, depth):
    this_f = _parse_result2indent_lines_EPL

    name, tag, ls = r
    name = _strs_to_str(name)
    tag = _strs_to_str(tag)

    indent = '\t' * depth
    head = '{indent}[{name}'.format(indent=indent, name=name)
    tail = '{indent}]  {tag}\n'.format(indent=indent, tag=tag)
    
    lines = [head]
    lines.extend(line for item in ls for line in this_f(item, depth+1))
    lines.append(tail)
    return lines

def parse_result2indent_EPL(r):
    if not is_parse_result_EPL(r):
        raise ValueError('not is_parse_result_EPL')
    
    lines = _parse_result2indent_lines_EPL(r, depth=0)
    src = '\n'.join(lines)
    return src






