

import re
#from LL1V2.MyLL1L.RawTokenizer_SRRTL_of_XL import RawTokenizer_SRRTL_of_XL

re_char = re.compile('[;{}"\']')


js_token_type_pattern_ls = (
    ('multiline_comment', r'/\*([^*]|\*(?!/))*\*/'),
    ('singleline_comment', r'//.*(\n|(?!\n)$)'),
    ('spaces', r'\s+'),
    
    ('sep', r'[,;:]'),
    #('pair', r'[(){}\[\]]'),
    ('open', r'[(\[{]'),
    ('close', r'[\]})]'),
    ('keyword', r'return|typeof|function|var'),

    ('rex', r"/([^/\\]|\\.)*/\w*"),
    ('string', r"\w*'([^'\\]|\\.)*'" '|' r'\w*"([^"\\]|\\.)*"'),
    ('id', r'[\$\w]+'),
    ('op', r'/?[-+*%=\.!~^&\|<>\?]+|/'),
)


js_include_all = tuple(range(len(js_token_type_pattern_ls)))
js_exclude_rex = tuple(i for i in js_include_all
                       if js_token_type_pattern_ls[i][0] != 'rex')

js_init_state = not_after_object = 'not_after_object'
after_object = 'after_object'
js_state_type_to_next_state = {
    not_after_object: {
        'id': after_object,
        'string': after_object,
        'rex': after_object,
        'close': after_object,
    },
    after_object: {
        'keyword': not_after_object,
        'op': not_after_object,
        'sep': not_after_object,
        'pair': not_after_object,
        'open': not_after_object,
    }
}

js_state_to_indices = {
    not_after_object: js_include_all,
    after_object: js_exclude_rex,
}




#js_token_re_ls = tuple((type, re.compile(str)) for type, str in token_type_pattern_ls)

def tokenize(src,
             token_type_pattern_ls,
             init_state,
             state_to_indices,
             state_type_to_next_state,
             start = None, end = None):
    if start == None: start = 0
    if end == None: end = len(src)

    t_re_ls = tuple((t, re.compile(p)) for t, p in token_type_pattern_ls)

    state = init_state
    indices = state_to_indices[state]
    ls = []
    while start < end:
        #for token_type, pattern in re_token_ls:
        for i in indices:
            token_type, pattern = t_re_ls[i]
            
            m = pattern.match(src, start, end)
            if not m: continue
            if m.start() == m.end():
                raise ValueError('token_type:{} is nullable?'.format(token_type))

            
            break
        else:
            print(ls[-21:])
            pre = src[max(0,start-10):start+10]
            curr = src[start:start+20]
            raise ValueError(
                'state: {state}. failed at position: {pos}. '\
                'src=...{pre!r}...{curr!r}...'
                .format(state=state, pos=start, pre=pre, curr=curr))
        
        start = m.end()
        ls.append((token_type, m.group(0), m.start(), m.end()))
        next_state = state_type_to_next_state[state].get(token_type, state)
        if next_state == state:
            continue

        state = next_state
        indices = state_to_indices[state]
        
    return ls
        
            
def js_format(js):
    level = 0
    ls = []
    js = tokenize(js,
                  js_token_type_pattern_ls,
                  js_init_state,
                  js_state_to_indices,
                  js_state_type_to_next_state)
    for token in js:
        level = _js_format(token, level, ls)
    return ''.join(ls)



def _js_format(token, level, ls):
    def newline():
        ls.append('\n')
        ls.append(' ' * (4*level))
        return
    
    t, s, beg, end = token
    if t in {'multiline_comment', 'singleline_comment', 'spaces'}:
        pass

    elif t in {'string', 'id', 'op', 'keyword', 'rex'}:
        ls.append(s)
        ls.append(' ')
        


    elif t == 'sep':
        if s in ',:':
            ls.append(s)
            ls.append(' ')
        elif s == ';':
            ls.append(s)
            newline()
        else:
            raise never-here
        
    elif t in {'open', 'close'}:
    #elif t == 'pair':
        if s in '()[]':
            ls.append(s)
            
        elif s == '{':
            ls.append(s)
            level += 1
            newline()
        elif s == '}':
            level -= 1
            newline()
            ls.append(s)
            newline()
        else:
            raise never-here
    else:
        print(t, s)
        raise never-here

            
    return level

from sand import read_txt, write_txt

js_fname = r'E:/temp_output/jquery-1.4.2.min.js'
js = read_txt(js_fname, 'utf-8')
js = js_format(js)
write_txt(js_fname + '.txt', js, 'utf-8')


