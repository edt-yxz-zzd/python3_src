
from .MKUL_in_SRRTL import named_b_string_pattern_MKUL, \
     call_on_b_string_pattern_MKUL
from MyLL1L.ProcessMatchResult_MyLL1L import ProcessMatchResult_MyLL1L
from ast import literal_eval
import re



def _esc_named_str2esc_str_find(s, t, chars='\'"'):
    assert len(s) == len(t)
    ls = []
    for i, c in enumerate(s):
        if c in chars:
            if t[i] == c:
                ls.append(i)
    return ls

def esc_named_b_str2str(s, byte_esc):
    if 'e' in byte_esc:
        r = esc_named_str2esc_str(s)
        prefix = 'b' if 'b' in byte_esc else ''
        r = literal_eval("{prefix}'''{content}'''"\
                         .format(prefix=prefix, content=r))
        pass

    elif 'b' in byte_esc:
        r = s.encode('ascii')
    else:
        r = s
    return r


def esc_named_str2str(s):
    r = esc_named_str2esc_str(s)
    r = literal_eval("'''{}'''".format(r))
    return r

def esc_named_bstr2bstr(s):
    r = esc_named_str2esc_str(s)
    r = literal_eval("b'''{}'''".format(r))
    return r

def esc_named_str2esc_str(s):
    t = re.sub(r'(?s)\\.', r'xx', s)
    assert len(t) == len(s)

    if '\\' in t:
        raise ValueError(r'tail "\" exists.')


    ls = _esc_named_str2esc_str_find(s, t)
    
    begins = [0]
    begins.extend(i+1 for i in ls)
    ends = list(ls)
    ends.append(len(s))

    assert len(ls) + 1 == len(begins) == len(ends)
    strs = []
    for i, begin, end in zip(ls, begins, ends):
        strs.append(s[begin:end])
        strs.append('\\' + s[i]) # escape ' to \' and " to \"
        
    begin = begins[-1]
    end = ends[-1]
    strs.append(s[begin:end])
    r = ''.join(strs)
    assert len(r) >= len(s)

    
    _ = literal_eval("'''{}'''".format(r))
    return r

    
class ProcessMatchResult_MyLL1L_of_MKUL(ProcessMatchResult_MyLL1L):
    
    def _pre_process(self, match_result):pass
    def _process_leaf(self, match_result):pass

    
    def _get_result(self, match_result):
        ns = match_result[-1]
        normal_node = ns.data
        assert type(normal_node) == tuple

        return normal_node

            
    def _post_process(self, match_result):
        explain = self.explain
        e = self.explain(match_result)

        tID = e.tID
        ID, *rID = tID
        ns = e.ns
        case = e.define_type
        #print('case={} , tID={}'.format(case, tID))

        self.gen_ns_data(e)
        self.outbox_optional_Item(e)

        if case == 'Token':
            if len(tID) == 1:
                s = ns.data
                if ID in {'str-', 'bstr-'}:
                    assert ns.data[-1] == '-'
                    ns.data = literal_eval(s[:-1])
                elif ID in {'str', 'bstr'}:
                    ns.data = literal_eval(s)
                elif ID in {'int', 'tfloat', 'timag', 'tcomplex'}:
                    d = {'int':int, 'tfloat':float, 'timag':complex, 'tcomplex':complex}
                    ns.data = d[ID](s)
                elif ID in {'0float', '0timag', '0complex'}:
                    d = {'0float':float, '0imag':complex, '0complex':complex}
                    assert s[0] == '0'
                    ns.data = d[ID](s[1:])
                elif ID in {'0none', '0bool', '0complex'}:
                    d = {'0none':None, '0true':True, '0false':False}
                    assert s[0] == '0'
                    ns.data = d[s]
                elif ID in {'named_str', 'named_str-',
                            'named_bstr', 'named_bstr-'}:
                    m = named_b_string_pattern_MKUL.match(s)
                    assert m
                    assert m.end() == len(s)
                    assert m.start() == 0
                    byte_esc = m.group('byte_esc')
                    tag = m.group('tag')
                    content = m.group('content')
                    tail = m.group('tail')
                    #print('len(m.groups()) =', len(m.groups()), m.groups())

                    ns.xdata = (s, byte_esc, tag, content, tail)

                    content = esc_named_b_str2str(content, byte_esc)
                    ns.data = content
                    #print(content)
                    
                elif ID in {'hashable_call_on_bytes',
                            'hashable_call_on_string',
                            'nonhashable_call_on_bytes',
                            'nonhashable_call_on_string'}:
                    
                    m = call_on_b_string_pattern_MKUL.match(s)
                    assert m
                    assert m.end() == len(s)
                    assert m.start() == 0
                    byte_esc = m.group('byte_esc')
                    tag = m.group('tag')
                    content = m.group('content')
                    rtype = m.group('rtype')
                    func = m.group('func')

                    ns.xdata = (s, byte_esc, func, tag, rtype, content)

                    content = esc_named_b_str2str(content, byte_esc)
                    t = list if rtype == ']' else tuple
                    ns.data = t([func, content])
                    

                    
                    
            return

        elif case == 'Item':
            pass
        elif case == 'Block':
            pass

        elif ID == 'normal_node':
            _, tag , _id , _type , args , kwargs , subnodes, _ = ns.data

            if not _id: _id = None
            if not _type: _type = frozenset()
            if not args: args = ()
            if not kwargs: kwargs = {}
            if not subnodes: subnodes = []
            
            ns.data = (tag , _id , _type , args , kwargs , subnodes)
        elif ID in {'subnodes', 'list'}:
            _, ls, _ = ns.data
            ns.data = ls
        elif ID in {'hashable_tuple', 'tuple'}:
            _, ls, _ = ns.data
            ns.data = tuple(ls)
        elif ID in {'set', 'frozenset', 'dict'}:
            _, ls, _ = ns.data
            ns.data = eval(ID)(ls)
        elif ID == 'key=value':
            key, _, value = ns.data
            ns.data = (key, value)
        elif ID in {'string', 'bytes'}:
            s_, st = ns.data
            ss = list(s_)
            ss.append(st)
            ns.data = type(st)().join(ss)
        elif ID == '==key=value':
            _, _, ls = ns.data
            kwargs = dict(ls)
            
            if len(kwargs) < len(ls):
                raise SyntaxError(
                    'keyword argument repeated: begin, end = {}, {}'\
                    .format(e.begin, e.end))
            
            ns.data = kwargs
            
        elif ID in {'hashable_call_on_args', 'nonhashable_call_on_args'}:
            func, args, kwargs, _ = ns.data
            if kwargs == None: kwargs = {}
            ns.data = repr((func, args, kwargs))

            ns.data = (func, repr(args), repr(kwargs))
            if ID == 'nonhashable_call_on_args':
                ns.data = list(ns.data)

            if ID == 'hashable_call_on_args':
                hash(ns.data)
                
        else:
            pass
            #raise ValueError('else:', tID)
        return
    


        
