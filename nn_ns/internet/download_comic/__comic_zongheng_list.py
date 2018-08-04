from get_list_in_html_txt import get_html, list_HTMLParser, \
     get_the_exact_only_one_data_from_tree_list_node,\
     get_nothing_from_tree_list_node, \
     get_info_from_html_txt, write_txt, read_txt

import os
import re
from my_exception import internet_except, unknown_case_except
from urllib.parse import urlparse, unquote
from ptask import *

from save_value import write_value, read_value, read_or_calc_xwrite

_max_workers = 10




def database(*args, **keys):
    return args, keys


get_data_from_zongheng_tree_list_node = get_nothing_from_tree_list_node
_tmp_path = r'E:/my_data/program_source/python3_src/internet/'

def _pr_r(*arg, **ks):
    print(*arg)
    print(ks)

def _pr_d(*arg, **ks):
    pass

_pr = _pr_d



def get_zongheng_image_url(zongheng_image_page_html_txt):
    _pr(get_zongheng_image_url='')
    #'img', {'title': '点击进入下一页。', 'id': 'disp', 'onmousedown': 'imageMouseDown(this,event)', 'onclick': 'doAfterPage();', 'src': 'http://img1.comic.zongheng.com/comic/series/2013/4/xiefengmanhua/15/svol_20130506094345270440.jpg'}
    #<img id="disp" src="http://img1.comic.zongheng.com/comic/series/2013/4/xiefengmanhua/15/svol_20130506115801444503.jpg" onclick="doAfterPage();" onMouseDown="imageMouseDown(this,event)" title="点击进入下一页。"/>

    match_to_zongheng_image_root = [\
        ('img', {'title': '点击进入下一页。', 'id': 'disp', \
                'onclick': 'doAfterPage();', 'src': None}),\
        ]
    match_zongheng_image_info = [\
        ('img', {'src':None}, None, {'src'}),\
    ]

    for (tag, attrs), _ in get_info_from_html_txt(\
        zongheng_image_page_html_txt, \
        match_to_zongheng_image_root, match_zongheng_image_info, \
        get_data_from_zongheng_tree_list_node):
        return attrs['src']

    print(zongheng_image_page_html_txt.find('点击进入下一页。'))
    write_txt(zongheng_image_page_html_txt, _tmp_path+'out.html', 'gbk')
    raise internet_except(get_zongheng_image_url, zongheng_image_page_html_txt)

def _t():
    zongheng_image_page_html_txt = read_txt(_tmp_path+'out.html', 'gbk')
    match_to_zongheng_image_root = [\
        ('img', {'title': '点击进入下一页。', 'id': 'disp', \
                'onclick': 'doAfterPage();', 'src': None}),\
        ]
    match_zongheng_image_info = [\
        ('img', {'src':None}, None, {'src'}),\
    ]

    for (tag, attrs), _ in get_info_from_html_txt(\
        zongheng_image_page_html_txt, \
        match_to_zongheng_image_root, match_zongheng_image_info, \
        get_data_from_zongheng_tree_list_node):
        print(tag, attrs)
        return attrs['src']
    raise internet_except('')


def get_zongheng_image_page_idx_list(zongheng_image_page_html_txt):
    #afterPageUrl = "http://comic.zongheng.com/seriesShow/m0/c31513/i281147.html"
    '''
    'select', {'onchange': 'doRedirect()', 'id': 'imagePageNum', 'style': 'margin:0 10px 3px 10px'}
            ' \t\t\t\t \t\t\t\t'
            'option', {'value': '281145'}
                    ' \t\t\t\t\t第1页 \t\t\t\t
    '''

    match_to_zongheng_image_page_idx_list_root = [\
        ('select', {'id': 'imagePageNum'}),\
        ('option', {'value': None}),\
        ]
    match_to_zongheng_image_page_idx_list_info = [\
        ('option', {'value': None}, None, {'value'}),\
    ]

    ls = []
    for (tag, attrs), _ in get_info_from_html_txt(\
        zongheng_image_page_html_txt, \
        match_to_zongheng_image_page_idx_list_root, \
        match_to_zongheng_image_page_idx_list_info, \
        get_data_from_zongheng_tree_list_node):
        idx = attrs['value']
        if ls and idx == ls[0]:
            break
        ls.append(idx)

    assert get_num_zongheng_image_page_idx_list_size(zongheng_image_page_html_txt) \
           == len(ls)
    return ls


def get_num_zongheng_image_page_idx_list_size(zongheng_image_page_html_txt, \
                                              pattern = re.compile('总页\s*(\d+)')):
    #'[当前 2 | 总页36]'
    return int(pattern.search(zongheng_image_page_html_txt).group(1))


def get_zongheng_chapter_list(zongheng_chapter_list_html_txt):
    '''
    <div class="chapterli">

        <ul>

            <li>

                <a  href="http://comic.zongheng.com/seriesShow/c31513.html" target="_blank" title="">1</a>

    '''
    
    match_to_zongheng_chapter_list_root = [\
        ('div', {'class' : "chapterli"}),\
        ('ul', {}),\
        ('li', {}),\
        ('a', {'href':None, 'title':None}),\
        ]
    match_zongheng_chapter_list_info = [\
        ('a', {'href':None}, 'data', {'href'}),\
    ]

    ls = []
    for (tag, attrs, data), _ in get_info_from_html_txt(\
        zongheng_chapter_list_html_txt, \
        match_to_zongheng_chapter_list_root, match_zongheng_chapter_list_info, \
        get_the_exact_only_one_data_from_tree_list_node):
        chapter_name = data
        ls.append((attrs['href'], chapter_name))
    return ls

def zongheng_chapter_url_to_zongheng_image_page_url_fmt(zongheng_chapter_url, \
                                              pattern = re.compile('(.*\D)(\d+)(\D*)')):
    a,b,c = pattern.search(zongheng_chapter_url).group(*range(1,4))
    return a+b+'/i{}'+c
    
def get_zongheng_chapter_url_list_from_work_page_url(\
        zongheng_chapter_list_url, \
        first_chapter_name = None, \
        last_chapter_name = None):
    _pr(get_zongheng_chapter_url_list_from_work_page_url=zongheng_chapter_list_url)
    zongheng_chapter_list_html_txt = get_html(zongheng_chapter_list_url)
    ls = get_zongheng_chapter_list(zongheng_chapter_list_html_txt)

    def find_index(ls, chapter_name):
        if type(chapter_name) == str:
            for i, (url, name) in enumerate(ls):
                if name == chapter_name:
                    return i
            else:
                raise internet_except(get_zongheng_chapter_url_list_from_work_page_url, \
                                      find_index, 'not found')
        else:
            return chapter_name # should be int

    begin = 0 if first_chapter_name == None else find_index(ls, first_chapter_name)
    end = len(ls) if last_chapter_name == None else 1+find_index(ls, last_chapter_name)
    return ls[begin:end], (begin, end)


def get_zongheng_work_image_page_url_list_from_chapter_url(zongheng_chapter_url):
    _pr(get_zongheng_work_image_page_url_list_from_chapter_url=zongheng_chapter_url)
    fmt = zongheng_chapter_url_to_zongheng_image_page_url_fmt(zongheng_chapter_url)
    zongheng_image_page_html_txt = get_html(zongheng_chapter_url)
    idc = get_zongheng_image_page_idx_list(zongheng_image_page_html_txt)
    ls = []
    for idx in idc:
        url = fmt.format(idx)
        ls.append(url)

    return ls





              
def get_zongheng_work_image_page_url_lists_from_chapter_url_list(zongheng_chapter_url_list):
    _pr(get_zongheng_work_image_page_url_lists_from_chapter_url_list=zongheng_chapter_url_list)
    '''
    ls = []
    for zongheng_chapter_url in zongheng_chapter_url_list:
        urls = get_zongheng_work_image_page_url_list_from_chapter_url(zongheng_chapter_url)
        ls.append(urls)'''
    
    worker = get_zongheng_work_image_page_url_list_from_chapter_url
    task_info = tuple(((worker, zongheng_chapter_url), \
                  (idx, zongheng_chapter_url)\
                  )\
                 for idx, zongheng_chapter_url in \
                 enumerate(zongheng_chapter_url_list))
    n = len(task_info)
    ls = [None]*n
    for branch, info_ in ptask(task_info, max_workers=_max_workers):
        if branch == except_branch:
            info, exc = info_
            idx, _ = info
            print('{} generated an exception: {}'.format(info, exc))
            ls[idx] = []
        elif branch == except_else_branch:
            (idx, _), urls = info_
            ls[idx] = urls
        elif branch == finally_branch:
            pass
        else:
            raise unknown_case_except('ptask branch', \
                'func@get_zongheng_work_image_page_url_lists_from_chapter_url_list')


    return ls
  
def get_zongheng_work_image_page_url_list_from_work_page_url(\
        zongheng_chapter_list_url, \
        first_chapter_name = None, \
        last_chapter_name = None):
    ls, (begin, end) = get_zongheng_chapter_url_list_from_work_page_url(\
        zongheng_chapter_list_url, first_chapter_name, last_chapter_name)
    _pr(get_zongheng_work_image_page_urls_list_from_work_page_url=zongheng_chapter_list_url)

    chapter_names = tuple(name for url, name in ls)
    chapter_urls = (url for url, name in ls)

    image_page_urls_ls = get_zongheng_work_image_page_url_lists_from_chapter_url_list(chapter_urls)

    # flatten
    image_page_url_ls = tuple(url for urls in image_page_urls_ls for url in urls)
    chapter_idx_name_image_idx_ls = \
        tuple((ch_name_idx+begin, chapter_names[ch_name_idx], img_idx) \
              for ch_name_idx, urls in enumerate(image_page_urls_ls)\
              for img_idx, url in enumerate(urls))
    return image_page_url_ls, chapter_idx_name_image_idx_ls

def get_zongheng_work_image_url_list_from_image_page_url_ls(\
    image_page_url_ls):
    
    # one html to one img_url
    '''
    image_urls_ls = []
    for image_page_urls in image_page_urls_ls:
        image_urls = []
        image_urls_ls.append(image_urls)
        for image_page_url in image_page_urls:
            html_txt = get_html(image_page_url)
            image_url = get_zongheng_image_url(html_txt)
            image_urls.append(image_url)'''

    n = len(image_page_url_ls)
    image_url_ls = [None]*n
    worker = get_html
    task_info = (((worker, image_page_url), idx)\
                 for idx, image_page_url in enumerate(image_page_url_ls))
    for branch, info_ in ptask(task_info, max_workers=_max_workers):
        if branch == except_branch:
            info, exc = info_
            print('{!r} generated an exception: {!s}'.format(info, exc))
        elif branch == except_else_branch:
            info, data = info_
            idx = info
            html_txt = data
            image_url = get_zongheng_image_url(html_txt)
            
            image_url_ls[idx] = image_url
        elif branch == finally_branch:
            pass
        else:
            raise unknown_case_except('ptask branch', \
                'func@down_load_using_chapter_idx_name_and_image_idx_url_list')
    
    return image_url_ls


def get_zongheng_work_image_url_list_from_work_page_url(\
        zongheng_chapter_list_url, \
        first_chapter_name = None, \
        last_chapter_name = None):
    image_page_url_ls, chapter_idx_name_image_idx_ls = \
        get_zongheng_work_image_page_url_list_from_work_page_url(\
            zongheng_chapter_list_url, first_chapter_name, last_chapter_name)
    image_url_ls = \
        get_zongheng_work_image_url_list_from_image_page_url_ls(\
            image_page_url_ls)

    chapter_idx_name_and_image_idx_url_list = tuple(\
        ((chapter_idx, chapter_name), (image_idx, image_url))\
        for image_url, (chapter_idx, chapter_name, image_idx) in \
              zip(image_url_ls, chapter_idx_name_image_idx_ls))

    return chapter_idx_name_and_image_idx_url_list
    '''
    # flat
    chapter_idx_name_and_image_idx_url_list = tuple(\
        ((chapter_idx, chapter_name), (image_idx, image_url))\
        for chapter_idx, chapter_name, image_urls in \
              zip(range(begin, end), chapter_names, image_urls_ls) \
        for image_idx, image_url in enumerate(image_urls))
    
    return chapter_idx_name_and_image_idx_url_list'''

def get_download_chapter_dirname(chapter_idx, chapter_name):
    return '{:0>4}_{}'.format(chapter_idx, chapter_name)

def get_download_filename(chapter_idx_name, image_idx_url, url_encoding):
    image_idx, image_url = image_idx_url
    data = split_file_url(image_url, url_encoding)
    ext = data['url_filename_ext']
    return '{:0>4}{}'.format(image_idx, ext)

def split_file_url(file_url, url_encoding):
    r = urlparse(file_url)
    path = unquote(r.path, encoding=url_encoding)
    url_dirpath, url_filename = os.path.split(path)
    url_filename_base, url_filename_ext = os.path.splitext(url_filename)
    return dict(file_url = file_url, \
                url_dirpath = url_dirpath,\
                url_filename_base = url_filename_base,\
                url_filename_ext = url_filename_ext)
    




def down_load_using_chapter_idx_name_and_image_idx_url(\
    path, chapter_idx_name_and_image_idx_url, url_encoding,\
    get_download_chapter_dirname=get_download_chapter_dirname,\
    get_download_filename=get_download_filename):
    #assert os.path.isdir(path)
    ch_i_n, img_i_u = chapter_idx_name_and_image_idx_url
        
    (chapter_idx, chapter_name), (image_idx, image_url) = ch_i_n, img_i_u
    ch_dir = get_download_chapter_dirname(chapter_idx, chapter_name)
    ch_dir = os.path.join(path, ch_dir)
    if not os.path.exists(ch_dir):
        try:
            os.makedirs(ch_dir)
        except OSError:
            if not os.path.exists(ch_dir):
                return ('skip', ch_dir, image_url, ch_i_n, img_i_u)
                #raise
                

    img_name = get_download_filename(ch_i_n, img_i_u, url_encoding)
    fname = os.path.join(ch_dir, img_name)
    fmt = 'download={} fname={}\n\turl={}'
    if os.path.exists(fname):
        #print(fmt.format('skip', fname, image_url))
        return ('skip', fname, image_url, ch_i_n, img_i_u)
        
    
    print(fmt.format('start', fname, image_url))
    try:
        down_load(fname, image_url)
    except:
        end_state = 'fail'
        #raise
    else:
        end_state = 'success'
        return ('success', fname, image_url, ch_i_n, img_i_u)
    finally:
        #print(fmt.format('end:'+end_state, fname, image_url))
        pass

    return (end_state, fname, image_url, ch_i_n, img_i_u)



def down_load_using_chapter_idx_name_and_image_idx_url_list(\
    path, chapter_idx_name_and_image_idx_url_list, url_encoding,\
    max_workers = 10, \
    get_download_chapter_dirname=get_download_chapter_dirname,\
    get_download_filename=get_download_filename):
    assert os.path.isdir(path)
    
    worker = lambda ch_img_info: down_load_using_chapter_idx_name_and_image_idx_url(\
        path, ch_img_info, url_encoding=url_encoding,\
        get_download_chapter_dirname=get_download_chapter_dirname,\
        get_download_filename=get_download_filename)

    cs = dict(skip = 0, fail = 0, success = 0)


    task_info = (((worker, ch_img_info), ch_img_info)\
                 for ch_img_info in chapter_idx_name_and_image_idx_url_list)
    for branch, info_ in ptask(task_info, max_workers=max_workers):
        if branch == except_branch:
            info, exc = info_
            print('{!r} generated an exception: {!s}'.format(info, exc))
        elif branch == except_else_branch:
            info, data = info_
            (state, fname, image_url,) = data[:3]
            print('state={}, \n\tfname={}, \n\turl={}'.format(state, fname, image_url))
            cs[state] += 1
        elif branch == finally_branch:
            pass
        else:
            raise unknown_case_except('ptask branch', \
                'func@down_load_using_chapter_idx_name_and_image_idx_url_list')


    '''
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_info = {executor.submit(worker, ch_img_info): ch_img_info \
                         for ch_img_info in chapter_idx_name_and_image_idx_url_list}
        for future in concurrent.futures.as_completed(future_to_info):
            info = future_to_info[future]
            try:
                data = future.result()
            except Exception as exc:
                print('{!r} generated an exception: {!s}'.format(info, exc))
            else:
                (state, fname, image_url,) = data[:3]
                print('state={}, \n\tfname={}, \n\turl={}'.format(state, fname, image_url))
                cs[state] += 1'''

    print('finish: {}'.format(cs))

def down_load_if_not_exist(fname, url):
    if not os.path.exists(fname):
        down_load(fname, url)

                  
def down_load(fname, url):
    import urllib.request
    #local_filename, headers = urllib.request.urlretrieve('http://python.org/')
    data = urllib.request.urlopen(url)
    buffer = bytearray(2**20) #1M Byte
    with open(fname, "xb") as fout:
        while True:
            n = data.readinto(buffer)
            fout.write(buffer[:n])
            if n < len(buffer):
                break

def _test_down_load():
    path = r'E:/my_data/program_source/python3_src/internet/'
    fout = path+'tmp.jpg'
    url = 'http://img1.comic.zongheng.com/comic/series/2013/4/xiefengmanhua/15/svol_20130506094345270440.jpg'
    down_load(fout, url)

def _test_get_zongheng_work_image_url_list_from_work_page_url(first_ch=None, last_ch='2'):
    print('_test_get_zongheng_work_image_url_list_from_work_page_url')
    url = r'http://comic.zongheng.com/series/15.html'
    img_urls_ls = get_zongheng_work_image_url_list_from_work_page_url(\
        url, first_chapter_name=first_ch, last_chapter_name=last_ch)
    return img_urls_ls


if __name__ == "__main__":
    fn = _tmp_path+'urls.zlib'
    #ls = _test_get_zongheng_work_image_urls_list_from_work_page_url()
    #ls = eval(read_txt(_tmp_path+'urls.txt'))
    #write_value(ls, fn)
    #down_load_using_chapter_idx_name_and_image_idx_url_list(_tmp_path, ls, 'gbk')
    calc_f = lambda:_test_get_zongheng_work_image_url_list_from_work_page_url()
    print('test')
    ls = read_or_calc_xwrite(fn, calc_f)
    down_load_using_chapter_idx_name_and_image_idx_url_list(\
        _tmp_path, ls, 'gbk')
    


