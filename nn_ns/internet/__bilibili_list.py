# -*- coding: gbk -*-

from get_list_in_html_txt import *
from my_exception import internet_except

host = r'http://www.bilibili.com'
url = r'http://www.bilibili.com/video/tv-drama-cn-41.html'


match_to_bilibili_list_root = [\
    ('div', dict([('class', 'vd_list_cnt')])),\
    ('ul', dict([('class', 'vd_list')])),\
    ('li', dict([('class', 'l1')])),\
    ]

get_data_from_bilibili_tree_list_node = get_the_exact_only_one_data_from_tree_list_node


match_bilibili_list_info = [\
    (None, dict([('href', None), ('class', 'title')]), 'data', {'href', 'class'}),\
    (None, dict([('class', 'gk'), ('title', '观看')]), 'data', {'class'}),\
    (None, dict([('class', 'sc'), ('title', '收藏')]), 'data', {'class'}),\
    (None, dict([('class', 'dm'), ('title', '弹幕')]), 'data', {'class'}),\
    (None, dict([('class', 'date'), ('title', '日期')]), 'data', {'class'}),\
    (None, dict([('class', 'info')]), 'data', {'class'}),\
    ]

def get_bilibili_tree_list(html_txt):
    p = list_HTMLParser(match_to_bilibili_list_root)
    p.feed(html_txt)
    return p.tree


def get_data_attrs_from_bilibili_tree_list(bilibili_tree_list):
    ls = get_data_attrs_from_tree_list(bilibili_tree_list, match_bilibili_list_info, get_data_from_bilibili_tree_list_node)
    stack = []
    
    for (tag, attrs, data), _ in get_info_from_url(\
        url, match_to_bilibili_list_root, match_bilibili_list_info, \
        get_data_from_bilibili_tree_list_node):
        tmp = {}
        stack.append(tmp)
        t = attrs.pop('class')
        tmp[t] = data
        tmp.update(attrs)

    '''
    for item in ls:
        if len(item[0]) == 0: continue
        tmp = {}
        stack.append(tmp)
        for (tag, attrs, data), in item:
            t = attrs.pop('class')
            tmp[t] = data
            tmp.update(attrs)'''
        
    return stack

def _test_get_data_attrs_from_bilibili_tree_list():
    path = r'C:/Users/Administrator/Desktop/tmp/'
    bilibili_tree_list = get_bilibili_tree_list(read_txt(path+'h.txt', 'gbk'))
    get_data_attrs_from_bilibili_tree_list(bilibili_tree_list)
    return
    
        



def get_bilibili_list_item_from_urls(urls):
    ls = []
    for url in urls:
        print('get_bilibili_list_item_from_urls: {}'.format(url))
        txt = get_html(url)
        bilibili_tree_list = get_bilibili_tree_list(txt)
        ls += get_data_attrs_from_bilibili_tree_list(bilibili_tree_list)

    return ls

def get_bilibili_page_num_from_url_fmt(bilibili_list_url_fmt, pattern = re.compile('.*共 *(\d+) *页.*')):
    url = bilibili_list_url_fmt.format(1)
    match_to_bilibili_list_pagebox_root = [\
        ('div', dict([('class', 'pagelistbox')])),\
        ('span', {}),\
        ]
    match_bilibili_pagenum_info = [\
        ('span', {}, 'data', {}),\
    ]

    for (tag, attrs, data), _ in get_info_from_url(\
        url, match_to_bilibili_list_pagebox_root, match_bilibili_pagenum_info, \
        get_data_from_bilibili_tree_list_node):
        m = pattern.match(data)
        if m:
            page_num = int(m.group(1))
            return page_num

def get_bilibili_all_list_item_from_url_fmt(bilibili_list_url_fmt):
    max_n = get_bilibili_page_num_from_url_fmt(bilibili_list_url_fmt)
    min_n = 1
    urls = tuple(bilibili_list_url_fmt.format(i) for i in range(min_n, max_n+1))
    return get_bilibili_list_item_from_urls(urls)

def unify_bilibili_list_items(bilibili_item_ls):
    d = dict((item['href'], item) for item in bilibili_item_ls)
    return list(d.values())


bilibili_tv_drama_cn_fmt = r'http://www.bilibili.com/video/tv-drama-cn-{}.html'
bilibili_list_video_music_dance_url_fmt = r'http://www.bilibili.com/video/music-dance-{}.html'



def _test_get_bilibili_page_num_from_url_fmt():
    get_bilibili_page_num_from_url_fmt(bilibili_tv_drama_cn_fmt)
def _test_get_bilibili_list_item_from_urls():
    bilibili_list_url_fmt = bilibili_tv_drama_cn_fmt
    max_n = get_bilibili_page_num_from_url_fmt(bilibili_list_url_fmt)
    min_n = 1
    begin = max(min_n, max_n-1)
    end = max_n + 1
    urls = tuple(bilibili_list_url_fmt.format(i) for i in range(begin, end))
    return get_bilibili_list_item_from_urls(urls)


def calc_range_for_bilibili_list(bilibili_list_url_fmt, begin=None, end=None):
    max_n = get_bilibili_page_num_from_url_fmt(bilibili_list_url_fmt)
    min_n = 1
    N = max_n + 1
    
    def _f(idx, default, N):
        if idx == None:
            idx = default
        elif idx < 0:
            idx += N
        return idx
        
    begin = _f(begin, min_n, N)
    end = _f(end, N, N)
    assert min_n <= begin <= end <= N
    return begin, end

def get_bilibili_list_items_and_write_to_file(fname, bilibili_list_url_fmt, begin=None, end=None):
    begin, end = calc_range_for_bilibili_list(bilibili_list_url_fmt, begin, end)
    urls = tuple(bilibili_list_url_fmt.format(i) for i in range(begin, end))
    
    try:
        with open(fname, 'xb') as fout:
            ls = get_bilibili_list_item_from_urls(urls)
            ls = unify_bilibili_list_items(ls)
            data = str(ls).encode(encoding='gbk')
            fout.write(data)
    except BaseException as e:
        print("error!!")
        return e
    return ls

def download_bilibili_html(fname_fmt, bilibili_list_url_fmt, begin=None, end=None, encoding='utf-8'):
    begin, end = calc_range_for_bilibili_list(bilibili_list_url_fmt, begin, end)
    urls = tuple(bilibili_list_url_fmt.format(i) for i in range(begin, end))
    fs = tuple(fname_fmt.format(i) for i in range(begin, end))
    try:
        for fname, url in zip(fs, urls):
            txt = get_html(url)
            write_txt(txt, out_file=fname, encoding=encoding)
    except BaseException as e:
        print("error!!")
        return e

def extract_info_from_bilibili_html_txt(out_file, fname_fmt, begin, end, encoding='utf-8'):
    head_fmt = '# -*- coding: {} -*-\n\nls = '
    fs = tuple(fname_fmt.format(i) for i in range(begin, end))
    txts = (read_txt(fname, encoding) for fname in fs)
    ls = []
    for txt, fn in zip(txts, fs):
        try:
            bilibili_tree_list = get_bilibili_tree_list(txt)
            ls += get_data_attrs_from_bilibili_tree_list(bilibili_tree_list)
        except:
            raise internet_except(fn)
    ls = unify_bilibili_list_items(ls)
    txt = head_fmt.format(encoding) + str(ls)

    try:
        write_txt(txt, out_file, encoding=encoding)
    except BaseException as e:
        print("error!!")
        return ls, e
    return ls



def _t1():
    _test_get_data_attrs_from_bilibili_tree_list()
    _test_get_bilibili_list_item_from_urls()
    _test_get_bilibili_page_num_from_url_fmt()

def _t3(begin=-2):
    path = r'C:/Users/Administrator/Desktop/tmp/'
    fname = path + 'tmp.txt'
    ls = get_bilibili_list_items_and_write_to_file(fname, bilibili_list_video_music_dance_url_fmt, begin)
    return ls
    
def _t4(begin=-2, encoding='utf-8'):
    path = r'C:/Users/Administrator/Desktop/tmp/'
    fname_fmt = path + 'music_dance_utf8_{}.txt'
    r = download_bilibili_html(fname_fmt, bilibili_list_video_music_dance_url_fmt, begin, encoding=encoding)
    return r


def _t5(begin, end, encoding='utf-8'):
    path = r'C:/Users/Administrator/Desktop/tmp/'
    fname_fmt = path + 'music_dance_utf8_{}.txt'
    out_file = path + 'music_dance_utf8.py'
    r = extract_info_from_bilibili_html_txt(out_file, fname_fmt, begin, end)
    return r

def _int(s):
    try:
        return int(s)
    except:
        return -1
def _str1(e):
    key = [('title', 'href'), ('info',), ('sc', 'dm', 'gk', 'date')]
    _f = lambda k,v: '{0!r}:{1!r}, '.format(k,v)
    stack = ['{']
    for ks in key:
        for k in ks:
            stack.append(_f(k, e[k]))
        stack.append('\\\n')
    stack.append('}')
    return ''.join(stack)


def _print_sort(ls, key, n):
    k = key
    key = lambda k:lambda e: _int(e[k])
    ls.sort(key=key(k))
    for e in (ls[:n]+ls[-n:]):
        print(_str1(e), ',\\')

        
def _t6(ls, n=50, k='sc'):
    _print_sort(ls, k, n)

def _t7(n=50, k='sc'):
    import bilibili_list_example_data as dlib
    for ls in [dlib.tv_drama_cn_ls, dlib.music_dance_ls]:
        _t6(ls, n, k)

def _t8():
    url = bilibili_tv_drama_cn_fmt.format(1)
    html_txt = get_html(url)
    bilibili_tree_list = get_bilibili_tree_list(html_txt)
    ls = get_data_attrs_from_bilibili_tree_list(bilibili_tree_list)
    return ls
    
if __name__ == "__main__":
    print(_t8())
