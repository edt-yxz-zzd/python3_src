


#import http
from .http_do import http_do
from html.parser import HTMLParser
import io
import re
from html.entities import name2codepoint
from sand import internet_except
from .max_tag_match import max_tag_match, tags2ints
from sand import read_txt, write_txt


#import httplib2


# http.client.HTTPConnection(host)


'''
# GZ Archive gz;tgz 0x1F8B08
gz_header = b'\x1F\x8B'
def decode(data):
    try:
        if data[:len(gz_header)] == gz_header:
            data = gzip.decompress(data)
    except:
        pass

    txt = data.decode('utf-8')
    return txt
'''




#'Content-Type' 'text/html;charset=utf-8'
content_type_charset_pattern = re.compile('(.*;)?\s*charset\s*=\s*(\S+)\s*(;.*)?')
def get_charset_from_content_type(content_type, default = 'utf-8'):
    m = content_type_charset_pattern.match(content_type)
    if m != None:
        #print(m.group(2))
        return m.group(2)
    return default
def get_html(url):
    r = http_do(url, 'GET')
    if r.reason != 'ok':
        raise internet_except('get_html fail: url = {}'.format(url))
    encoding = get_charset_from_content_type(r.head['content-type'])
    txt = r.data.decode(encoding)
    return txt


class get_tags_HTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self, strict=False)
        self.tags = []
    def handle_startendtag(self, tag, attrs):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        pass
    def handle_starttag(self, tag, attrs):
        self.tags.append((True, tag))
    def handle_endtag(self, tag):
        self.tags.append((False, tag))
    def pop(self):
        t = self.tags
        self.tags = []
        return t
    
class max_tag_match_HTMLParser(HTMLParser):
    #get_tags = get_tags_HTMLParser()
    def __init__(self):
        HTMLParser.__init__(self, strict=False)
        self.match_map = ()
        self.tag_idx = 0
        self.get_tags = get_tags_HTMLParser()
    def feed(self, txt):
        self.get_tags.feed(txt)
        tags = self.get_tags.pop()
        
        ints, tag2int = tags2ints(tags)
        self.match_map = max_tag_match(len(tag2int), ints)
        self.tag_idx = 0
        HTMLParser.feed(self, txt)



class stack_HTMLParser(max_tag_match_HTMLParser):
    def __init__(self):
        max_tag_match_HTMLParser.__init__(self)
        self.stack = []
        self.idc = []
        self.ls = []

    def _handle_startendtag_start(self, tag, attrs):
        self.stack.append((tag, attrs))
        return True
    def _handle_startendtag_end(self, tag, attrs):
        self.stack.pop()
    def handle_startendtag(self, tag, attrs):
        if not stack_HTMLParser._handle_startendtag_start(self, tag, attrs): return
        self._handle_startendtag(tag, attrs)
        stack_HTMLParser._handle_startendtag_end(self, tag, attrs)
    def handle_starttag(self, tag, attrs):
        #rint('handle_starttag', tag)
        if not stack_HTMLParser._handle_starttag(self, tag, attrs): return
        self._handle_starttag(tag, attrs)
    def handle_endtag(self, tag):
        #rint('handle_endtag', tag)
        if not stack_HTMLParser._handle_endtag_ask(self, tag): return
        self._handle_endtag(tag)
        stack_HTMLParser._handle_endtag_impl(self, tag)
    def handle_data(self, data):
        if not stack_HTMLParser._handle_data(self, data): return
        self._handle_data(data)
    
    def _handle_starttag(self, tag, attrs):
        #rint('handle_starttag', tag)
        if self.match_map[self.tag_idx] != -1:
            if not self.match_map[self.tag_idx] > self.tag_idx:
                print(self.tag_idx, self.match_map[self.tag_idx])
                print(self.match_map)
            assert self.match_map[self.tag_idx] > self.tag_idx
            
        self.ls.append(tag)
        self.tag_idx += 1
        assert len(self.ls) == self.tag_idx
        if self.match_map[self.tag_idx-1] == -1:
            # an error
            self.handle_startendtag(tag, attrs)
            return False
        self.stack.append((tag, attrs))
        self.idc.append(self.tag_idx-1)
        return True

    def _handle_endtag_impl(self, tag):
        self.stack.pop()
    def _handle_endtag_ask(self, tag):
        #rint('handle_endtag', tag)
        if self.match_map[self.tag_idx] != -1:
            assert self.match_map[self.tag_idx] < self.tag_idx
            assert tag == self.ls[self.match_map[self.tag_idx]]
        self.ls.append(tag)
        self.tag_idx += 1
        assert len(self.ls) == self.tag_idx
        _t, _a = self.stack[-1]
        #error : assert (self.match_map[self.tag_idx] == -1) == (_t != tag)
        
        if self.match_map[self.tag_idx-1] != -1:
            assert _t == tag
            i = self.idc.pop()
            assert self.match_map[self.tag_idx-1] == i
            return True
        else:
            print('error: mismatch (starttag, endtag) in stack_HTMLParser.handle_endtag')
            print('\t(starttag, endtag) == ({}, {})'.format(_t, tag))
            print('\tself.stack of starttags = {}'.format(self.stack))
            
            #forgot endtag
            return False

    def _handle_data(self, data):
        return True
'''
startendtag_list = {'img', 'link', 'meta', 'input'}
class stack_HTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self, strict=False)
        self.stack = []

    def _handle_startendtag_start(self, tag, attrs):
        self.stack.append((tag, attrs))
        return True
    def _handle_startendtag_end(self, tag, attrs):
        self.stack.pop()
    def handle_startendtag(self, tag, attrs):
        if not stack_HTMLParser._handle_startendtag_start(self, tag, attrs): return
        self._handle_startendtag(tag, attrs)
        stack_HTMLParser._handle_startendtag_end(self, tag, attrs)
    def handle_starttag(self, tag, attrs):
        if not stack_HTMLParser._handle_starttag(self, tag, attrs): return
        self._handle_starttag(tag, attrs)
    def handle_endtag(self, tag):
        if not stack_HTMLParser._handle_endtag_ask(self, tag): return
        self._handle_endtag(tag)
        stack_HTMLParser._handle_endtag_impl(self, tag)
    def handle_data(self, data):
        if not stack_HTMLParser._handle_data(self, data): return
        self._handle_data(data)
    
    def _handle_starttag(self, tag, attrs):
        if tag in startendtag_list:
            # an error
            self.handle_startendtag(tag, attrs)
            return False
        self.stack.append((tag, attrs))
        return True

    def _handle_endtag_impl(self, tag):
        self.stack.pop()
    def _handle_endtag_ask(self, tag):
        #print('handle_endtag')
        _t, _a = self.stack[-1]
        if _t == tag: return True
        if _t != tag:
            print('error: mismatch (starttag, endtag) in stack_HTMLParser.handle_endtag')
            print('\t(starttag, endtag) == ({}, {})'.format(_t, tag))
            print('\tself.stack of starttags = {}'.format(self.stack))
            stack = self.stack
            last_n = 2
            last_n = min(len(stack), last_n)
            
            if tag in list(k for k, _a in stack[-last_n:]):
                while tag != _t:
                    _t, _a = stack.pop()
                stack.append((_t, _a))
            else:
                #forgot tag
                return False
                    
        _t, _a = self.stack[-1]
        assert _t == tag
        return True
    def _handle_data(self, data):
        return True
'''


class format_HTMLParser(stack_HTMLParser):
    def __init__(self):
        stack_HTMLParser.__init__(self)
        self.txt = []
    def pop(self):
        txt = self.txt
        self.txt = []
        return txt
    def _handle_startendtag(self, tag, attrs):
        strs = ['\t'*(len(self.stack) - 1), repr(tag), ', ', dict(attrs), '\n']
        self.txt.append(strs)
    def _handle_starttag(self, tag, attrs):
        strs = ['\t'*(len(self.stack) - 1), repr(tag), ', ', dict(attrs), '\n']
        self.txt.append(strs)
    def _handle_endtag(self, tag):
        strs = ['\t'*(len(self.stack) - 1), repr(tag), '\n']
        self.txt.append(strs)
    def _handle_data(self, data):
        strs = ['\t'*len(self.stack), repr(data), '\n']
        self.txt.append(strs)
        

def format_html(html_txt):
    p = format_HTMLParser()
    try:
        p.feed(html_txt)
    except:
        raise internet_except(p.txt)
    return ''.join(str(e) for strs in p.txt for e in strs)

def html_url2format2file(url, out_fname, encoding='utf-8'):
    html_txt = get_html(url)
    txt = format_html(html_txt)
    write_txt(out_fname, txt, encoding)

'''
def read_txt(txt_file, encoding='utf-8'):
    with io.FileIO(txt_file, 'rb') as fin:
        data = fin.readall()

    return data.decode(encoding)

def write_txt(txt, out_file, encoding='utf-8'):
    data = txt.encode(encoding)
    with open(out_file, 'xb') as fout:
        fout.write(data)



def format_html_file(input_html_file, out_file, encoding='utf-8'):
    txt = read_txt(input_html_file, encoding)
    txt = format_html(txt)
    write_txt(txt, out_file, encoding)
'''



'''
match_to_bilibili_list_root = (\
    (tag_p, dict(attrs_p), [get_item_info]),\
)


#example:
match_to_bilibili_list_root = [\
    ('div', dict([('class', 'vd_list_cnt')])),\
    ('ul', dict([('class', 'vd_list')])),\
    ('li', dict([('class', 'l1')])),\
    ]

'''

def do_string_match(string, pattern):
    if pattern == None:
        r = True
    elif type(pattern) == str:
        r = pattern == string
    else:
        r = pattern.match(string)

    return r

def do_attrs_match(attrs, attrs_pattern):
    #print(attrs_pattern)
    assert isinstance(attrs_pattern, dict)
    if not attrs_pattern.keys() <= attrs.keys():
        return False

    for k, p in attrs_pattern.items():
        s = attrs[k]
        if not do_string_match(s, p):
            return False

    return True

def do_tag_match(tag, tag_pattern):
    return do_string_match(tag, tag_pattern)

def do_tagattrs_match(tagattrs, tagattrs_pattern):
    #print(tagattrs_pattern)
    tag, attrs = tagattrs
    tag_pattern, attrs_pattern = tagattrs_pattern
    return do_tag_match(tag, tag_pattern) and do_attrs_match(attrs, attrs_pattern)


class list_HTMLParser(stack_HTMLParser):
    def __init__(self, match_to_list_root):
        stack_HTMLParser.__init__(self)
        self.blist = []
        self.to_list = match_to_list_root
        self.to_list_depth = []
        self.tree = []
        self._path = [self.tree]

    def pop(self):
        t = self.tree
        self.blist = []
        self.to_list_depth = []
        self.tree = []
        self._path = [self.tree]
        return t
    def _handle_startendtag(self, tag, attrs):
        attrs = dict(attrs)
        list_HTMLParser._handle_starttag_part1(self, tag, attrs)
        if len(self.to_list_depth) == len(self.to_list):
            if tag == 'br':
                data = '\n'
                curr = ((data,),)
            else:
                curr = ((tag, attrs,),)
            self._path[-1].append(curr)

        list_HTMLParser._handle_endtag_part2(self)
        
    def _handle_starttag_part1(self, tag, attrs):
        if len(self.to_list_depth) < len(self.to_list):
            pattern = self.to_list[len(self.to_list_depth)]
            if do_tagattrs_match((tag, attrs), pattern[:2]):
                self.to_list_depth.append(len(self.stack) - 1)
    def _handle_endtag_part2(self):
        if len(self._path) == 1:
            if len(self.to_list_depth) and self.to_list_depth[-1] == len(self.stack) -1:
                self.to_list_depth.pop()
    def _handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        list_HTMLParser._handle_starttag_part1(self, tag, attrs)

        if len(self.to_list_depth) == len(self.to_list):
            curr = ((tag, attrs), [])
            self._path[-1].append(curr)
            self._path.append(curr[-1])
            assert len(self._path) > 1

            
    def _handle_endtag(self, tag):            
        if len(self._path) > 1:
            self._path.pop()

        list_HTMLParser._handle_endtag_part2(self)
        

        
    def _handle_data(self, data):
        if len(self.to_list_depth) == len(self.to_list):
            curr = ((data,),)
            self._path[-1].append(curr)

    def handle_entityref(self, name):
        if name in name2codepoint:
            c = chr(name2codepoint[name])
        else:
            c = '&{};'.format(name)
            print('error: handle_entityref - entityref name {!r} not in name2codepoint'.format(c))
            
        self.handle_data(c)
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        self.handle_data(c)

    def feed(self, html_txt):
        stack_HTMLParser.feed(self, html_txt)
        for idc, node in walk_tree_list(self.tree):
            if walk_tree_list_is_leaf(node):
                continue
            children = []
            tmp = []
            def flush_tmp():
                if tmp:
                    data = ''.join(tmp)
                    children.append( ((data,),) )
                    tmp.clear()
                    
            for c in walk_tree_list_get_children(node):
                assert 1 <= len(c) < 3
                assert 1 <= len(c[0]) < 3
                if len(c) == 1 and len(c[0]) == 1:
                    tmp.append(c[0][0])
                else:
                    flush_tmp()
                    children.append(c)
            else:
                flush_tmp()
            node[-1][:] = children




walk_tree_list_is_leaf = lambda node: len(node) < 2
def walk_tree_list_get_children(node):
    assert not walk_tree_list_is_leaf(node)
    assert len(node) == 2
    return node[-1]
def walk_tree_list(tree_list, \
                   is_leaf=walk_tree_list_is_leaf, \
                   get_children=walk_tree_list_get_children):
    stack = [iter(tree_list)]
    idc = [-1]
    while stack:
        try:
            n = next(stack[-1])
        except StopIteration:
            stack.pop()
            idc.pop()
            continue
        idc[-1] += 1
        yield idc, n
        
        if not is_leaf(n):
            stack.append(iter(get_children(n)))
            idc.append(-1)



'''
def flat_tree_list(tree_list_walk_iter, flat_node):
    ls = []
    for idc, data in tree_list_walk_iter:
        ls += flat_node(data)



'''

'''
match_list_info = (\
    (tag_p, dict(attrs_p)), 'data'|None, set(attrs_to_get)\
)

#example:
match_bilibili_list_info = [\
    (None, dict([('href', None), ('class', 'title')]), 'data', {'href', 'class'}),\
    (None, dict([('class', 'gk'), ('title', '观看')]), 'data', {'class'}),\
    (None, dict([('class', 'sc'), ('title', '收藏')]), 'data', {'class'}),\
    (None, dict([('class', 'dm'), ('title', '弹幕')]), 'data', {'class'}),\
    (None, dict([('class', 'date'), ('title', '日期')]), 'data', {'class'}),\
    (None, dict([('class', 'info')]), 'data', {'class'}),\
    ]
'''



def get_data_attrs_from_tree_list(tree_list, match_list_info, get_data):
    #print(tree_list)
    stack = [tuple([] for _ in match_list_info)]
    empty = tuple([] for _ in match_list_info)
    for idc, node in walk_tree_list(tree_list):
        if len(idc) == 1:
            if stack[-1] != empty:
                stack.append(tuple([] for _ in match_list_info))
        n = len(node)
        '''
        if not 1 <= n < 3 or not 1 <= len(node[0]) < 3 or \
           not (n == 1 or len(node[1]) == 1):
            print(node)'''
        assert 1 <= n < 3 # ((tag, attrs),) or ((tag, attrs),(data,)) or ((data,)) or ((tag, attrs),[...])
        assert 1 <= len(node[0]) < 3
        #assert n == 1 or len(node[1]) == 1 error
        
        if len(node[0]) == 1: continue
        for i, p in enumerate(match_list_info):
            if not do_tagattrs_match(node[0], p[:2]):
                continue
            tag, attrs = node[0]
            attrs = dict((k, attrs[k]) for k in p[3])
            if p[2] == 'data':
                data = get_data(node)
                stack[-1][i].append((tag, attrs, data))
            else:
                stack[-1][i].append((tag, attrs))
    if stack[-1] == empty:
        stack.pop()

    return stack

def get_the_exact_only_one_data_from_tree_list_node(node):
    #print(node)
    try:
        if node[-1]:
            data, = node[-1]
            data, = data
            data, = data
            assert type(data) == str
        else:
            data = ''
    except:
        raise internet_except(node)
    return data

get_nothing_from_tree_list_node = lambda node:None

#example:
#get_data_from_bilibili_tree_list_node = get_the_exact_only_one_data_from_tree_list_node





def get_info_from_url(url, info_obj):
    html_txt = get_html(url)
    return get_info_from_html_txt(html_txt, info_obj)


def get_info_from_html_txt(html_txt, info_obj):
    return _get_info_from_html_txt(html_txt, \
                                   info_obj.match_to_list_root, \
                                   info_obj.match_to_info, \
                                   info_obj.get_data_from_tree_list_node)

def _get_info_from_html_txt(html_txt, match_to_list_root, match_to_info, \
                      get_data_from_tree_list_node):
    p = list_HTMLParser(match_to_list_root)
    p.feed(html_txt)
    
    page_info = get_data_attrs_from_tree_list(p.tree, match_to_info, get_data_from_tree_list_node)

    for slot_idx, one_matched_info_slot in enumerate(page_info):
        for pattern_idx, (matched_info_ls, info_pattern) in \
            enumerate(zip(one_matched_info_slot, match_to_info)):
            try:
                for t2_or_t3 in matched_info_ls: # (tag, attrs) or (tag, attrs, data)
                    yield t2_or_t3, (slot_idx, pattern_idx, info_pattern)
            except StopIteration:
                raise
            except GeneratorExit:
                raise
            except:
                raise internet_except('error: "for t2_or_t3 in matched_info_ls:"',\
                                      one_matched_info_slot=one_matched_info_slot,\
                                      matched_info_ls=matched_info_ls)



_test_html_txt_data = '<html><img src="a.gif" /><a href="/path/to"><img src="b.jpg"></a><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>'
	
def _test_format_html():
    ans = "'html', {}\n\t'img', {'src': 'a.gif'}\n\t'a', {'href': '/path/to'}\n\t\t'img', {'src': 'b.jpg'}\n\t'a'\n\t'head', {}\n\t\t'title', {}\n\t\t\t'Test'\n\t\t'title'\n\t'head'\n\t'body', {}\n\t\t'h1', {}\n\t\t\t'Parse me!'\n\t\t'h1'\n\t'body'\n'html'\n"
    
    fh = format_html(_test_html_txt_data)
    if ans != fh: print(fh)
    assert ans == fh


def _test_format_html_file():
    path = r'C:/Users/Administrator/Desktop/tmp/'
    format_html_file(path+'h.txt', path+'fh.txt', encoding='GBK')



def _t1():
    _test_format_html()
    _test_format_html_file()






    
if __name__ == "__main__":
    path = r'C:/Users/Administrator/Desktop/tmp/'
    format_html_file(path+'file.html', path+'out_file.html', encoding='gbk')
    _t1()
    
    
    
    
    
    


    
