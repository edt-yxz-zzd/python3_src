
r'''
tokenize - split by line first:
begin = r'\\begin'
end = r'\\end'
newline = r'\n'

comment = r'\#.*'
num_children = r'\\\d+'
node_value = r'(?[^\\]).*' # not start with '\'
node_value = r'\\\\.*'     # starts with '\'
node_value = '\\' py single line string
node_value = '\\' py raw single line string


# each multiline block will be treated as 'node_value'
multiline_begin = r'\:.*'
multiline_continue_startswith_newline = r'\|.*'
multiline_continue_without_newline = r'\-.*'

'''

r'''
grammar:
tree = begin newline prefix_tree end newline
prefix_tree = leaf | num_children newline prefix_tree[num_children]
leaf = node_value newline | multiline_block
multiline_block = multiline_begin newline multiline_continue*
multiline_continue = multiline_continue_startswith_newline newline
    | multiline_continue_without_newline newline


'''


'''
evalue token:
num_children::int
node_value::str
'''
'''
parse:
<< tokens, values
# each tree is a string that is a leaf or a list of subtrees.
stack = []
for token, value in reversed(zip(tokens, values)):
    if token == 'num_children':
        num_children = value
        assert len(stack) >= num_children
        subtree = stack[-1:len(stack) - num_children - 1:-1]
        del stack[len(stack) - num_children:]
        stack.append(subtree)
    else:
        leaf = substring = value
        stack.append(leaf)
stack.reverse()
assert len(stack) == 1 # one tree
tree = stack[0]
>> tree
'''

from ast import literal_eval

num_children = 'num_children'
node_value = 'node_value'
mcontinue = 'mcontinue'
mbegin = 'mbegin'
BEGIN = 'begin'
END = 'end'
COMMENT = 'comment'



def tokenize_to_lines_without_newline(s):
    return s.splitlines()

def _tokenize_parse_string(s):
    
    if s[:2] == '\\\\':
        return s[1:]
    if s[:1] != '\\':
        return s

    s1 = s[1:]
    first = s[1:2]
    if any(s1.startswith(prefix) for prefix in '\' " r\' r"'.split()):
        value = literal_eval(s1)
        if type(value) is not str:
            raise ValueError('tokenize string fail: {}'.format(type(value)))
        
        return value
    return None


def tokenize_to_tokens(lines):
    tokens = []
    for line in lines:
        s = _tokenize_parse_string(line)
        if s is not None:
            tokens.append((node_value, s))
            
        elif line[:1] != '\\':
            raise logic - error
        else:
            line1 = line[1:]
            first = line1[:1]
            line2 = line[2:]
            if line1.isdigit():
                tokens.append((num_children, int(line1)))
            elif first in ':|-#':
                if first == ':':
                    tokens.append((mbegin, line2))
                elif first == '|':
                    tokens.append((mcontinue, '\n'+line2))
                elif first == '-':
                    tokens.append((mcontinue, line2))
                elif first == '#':
                    tokens.append((COMMENT, line2))
                else:
                    raise logic-error
            elif line1 == 'begin':
                tokens.append((BEGIN, None))
            elif line1 == 'end':
                tokens.append((END, None))
            else:
                raise ValueError('tokenize fail: {}'.format(line[:30]))

    return tokens



def tokenize_merge_mline(tokens):
    merged_tokens = []
    for token, value in tokens:
        if token == mbegin:
            merged_tokens.append([value])
        elif token == mcontinue:
            if type(merged_tokens[-1]) is not list:
                raise ValueError(
                    'bad format: multiline-continue not in multiline-block')
            merged_tokens[-1].append(value)
        else:
            merged_tokens.append((token, value))
    for i, e in enumerate(merged_tokens):
        if type(e) is list:
            s = ''.join(e)
            value = _tokenize_parse_string(s)
            if value is None:
                raise ValueError('multiline-block cannot convert to string: {}'\
                                 .format(s[:39]))
            merged_tokens[i] = (node_value, value)
    return merged_tokens

def tokenize_remove_comment(tokens):
    return [(token, value) for token, value in tokens if token != COMMENT]



def parse(merged_tokens):
    # each tree is a string that is a leaf or a list of subtrees.
    merged_tokens = list(merged_tokens)
    if len(merged_tokens) < 2 \
       or merged_tokens[0] != (BEGIN, None)\
       or merged_tokens[-1] != (END, None):
        raise ValueError('bad format: not enclosed in BEGIN/END')
    if len(merged_tokens) == 2:
        raise ValueError('bad format: tree should have at least one node.')
    
    stack = []
    NUM_CHILDREN = num_children
    for token, value in reversed(merged_tokens[1:-1]):
        if token == NUM_CHILDREN:
            num_children_ = value
            L = len(stack)
            if L < num_children_:
                raise ValueError('bad format: no num_children subtrees')
            
            subtree = stack[L - num_children_:]
            subtree.reverse()
            del stack[L - num_children_:]
            assert len(subtree) == num_children_
            assert len(stack) + num_children_ == L
            
            stack.append(subtree)
        else:
            leaf = substring = value
            stack.append(leaf)
    stack.reverse()
    if len(stack) != 1: # one tree
        raise ValueError('not exactly one tree')
    tree = stack[0]
    return tree


def parse_txt(txt):
    lines = tokenize_to_lines_without_newline(txt)
    tokens = tokenize_to_tokens(lines)
    tokens = tokenize_remove_comment(tokens)
    merged_tokens = tokenize_merge_mline(tokens)
    tree = parse(merged_tokens)
    return tree

txt = r'''\begin
\4
\2
\#comment
first grandson
\0
\:multiline
\|nextline
\-, 2ndline
\|3rd line
2th/3rd children
\r'\afsfafass'
\end'''
print(parse_txt(txt))
print(repr(parse_txt('\\begin\n\0\n\\end\n')))
print(repr(parse_txt('\\begin\n\\0\n\\end\n')))








        
    

    









