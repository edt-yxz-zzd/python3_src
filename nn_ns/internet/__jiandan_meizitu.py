
from .get_list_in_html_txt import *
from sand import internet_except, format_output
import os
from sand.ptask import *
from sand.save_value import *

from .download_small_file import download_htmls, download_images, fname_url_list_filter
from sand import list_split

host = r'http://jandan.net/'
url = r'http://jandan.net/ooxx'
jandan_ooxx_page_url_fmt = r'http://jandan.net/ooxx/page-{}' # 900-1214
jandan_ooxx_page_file_name_fmt = r'jandan_ooxx_page_{}.html'

_encoding = 'gbk'
_begin = 900
_end = 1214
out_path = r'./jandan_ooxx/'
img_info_fname = out_path + 'img_info_file'
jandan_ooxx_image_file_name_fmt = r'jandan_ooxx_image_{}_{}.jpg'


def down_load_jandan_ooxx_page(path, \
                               file_name_fmt = jandan_ooxx_page_file_name_fmt, \
                               begin = _begin, end = _end, \
                               jandan_ooxx_page_url_fmt = jandan_ooxx_page_url_fmt,
                               encoding = _encoding):

    if not os.path.exists(path):
        os.mkdir(path)

    assert os.path.isdir(path)
    
    fname_url_list = []
    for i in range(begin, end):
        fname = os.path.join(path, file_name_fmt.format(i))
        url = jandan_ooxx_page_url_fmt.format(i)
        fname_url_list.append((fname, url))

    fname_url_list = fname_url_list_filter(fname_url_list)
    
    download_htmls(fname_url_list, encoding)
    return


#down_load_jandan_ooxx_page(path = out_path)


################################3

'''
txt = format_html(html_txt)
write_txt(txt, out_file, encoding)
find the pattern to match...

'''

#'ol', {'class': 'commentlist', 'style': 'list-style-type: none;'}

'''
<li id="comment-2378453">
'img', {'src': 'http://ww4.sinaimg.cn/mw600/e0dab130gw1eds4tqhca7j20cm0j9myp.jpg',
        #'org_src':...sometime}
'span', {'id': 'cos_support-2378453'}
        '113'
'span'
'span', {'id': 'cos_unsupport-2378453'}
        '42'
'span'
'''

class ooxx2img:
    get_data_from_tree_list_node = lambda node: int('0'+get_the_exact_only_one_data_from_tree_list_node(node))#lambda node:node

    match_to_list_root = [\
        ('ol', {'class': 'commentlist'}),\
        ('li', {'id': None}),\
        ]
    match_to_info = [\
        ('li', {'id': None}, None, {'id'}),\
        ('img', {'org_src': None}, None, {'org_src'}),\
        ('img', {'src': None}, None, {'src'}),\
        ('span', {'id': None}, 'data', {'id'}),\
        ]


'result_type = {comment_id: (oo, xx, [img_url,...]),...}'
def get_jandan_ooxx_img_info_from_html_txt(html_txt):
    g = get_info_from_html_txt(html_txt, ooxx2img)

    ls = {}
    comment_id_prefix = 'comment-'
    oo_prefix = 'cos_support-'
    xx_prefix = 'cos_unsupport-'
    for t2_or_t3, (slot_idx, pattern_idx, info_pattern) in g:
        if pattern_idx == 0:
            s = t2_or_t3[1]['id']
            
            assert s.startswith(comment_id_prefix)
            comment_id = int(s[len(comment_id_prefix):])
            ls[comment_id] = [None, None, []]
        elif pattern_idx == 1:
            img_url = t2_or_t3[1]['org_src']
            ls[comment_id][-1].append(img_url)
            
        elif pattern_idx == 2:
            img_url = t2_or_t3[1]['src']
            ls[comment_id][-1].append(img_url)

        elif pattern_idx == 3:
            s = t2_or_t3[1]['id']

            for i, prefix in enumerate([oo_prefix, xx_prefix]):
                if s.startswith(prefix):
                    ooxx = t2_or_t3[2]
                    assert ls[comment_id][i] == None
                    ls[comment_id][i] = ooxx

    return ls

def get_jandan_ooxx_img_info_from_html_files(path, \
                               file_name_fmt = jandan_ooxx_page_file_name_fmt, \
                               begin = _begin, end = _end, \
                               encoding = _encoding):

    assert os.path.isdir(path)
    
    fname_list = []
    for i in range(begin, end):
        fname = os.path.join(path, file_name_fmt.format(i))
        if not os.path.exists(fname):
            raise Exception('{!r} not exist'.format(fname))

        fname_list.append(fname)


    info = {}
    for fname in fname_list:
        _info = get_jandan_ooxx_img_info_from_html_txt(read_txt(fname, encoding))
        info.update(_info)

    return info


def jandan_ooxx_image_info2fname_url_oo_xx_list(path, image_info, \
                                file_name_fmt = jandan_ooxx_image_file_name_fmt):
    fname_url_oo_xx_list = []
    for k, oo_xx_imgurls in image_info.items():
        oo, xx = oo_xx_imgurls[:2]
        for i, url in enumerate(oo_xx_imgurls[-1]):
            fname = file_name_fmt.format(k, i)
            fname = os.path.join(path, fname)
            fname_url_oo_xx_list.append(((fname, url), (oo, xx)))

    return fname_url_oo_xx_list

def download_jandan_ooxx_images(path, image_info, \
                                file_name_fmt = jandan_ooxx_image_file_name_fmt):
    fname_url_oo_xx_list = jandan_ooxx_image_info2fname_url_oo_xx_list(path, image_info, file_name_fmt)
    fname_url_list = list(fname_url for fname_url, _ in fname_url_oo_xx_list)
    fname_url_list = fname_url_list_filter(fname_url_list)
    
    if not os.path.exists(path):
        os.mkdir(path)
    assert os.path.isdir(path)
    
    download_images(fname_url_list)

        
    
def build_calc_f(path = out_path, file_name_fmt = jandan_ooxx_page_file_name_fmt, \
            begin = _begin, end = _end, encoding = _encoding):
    return lambda : get_jandan_ooxx_img_info_from_html_files(out_path, \
            file_name_fmt = jandan_ooxx_page_file_name_fmt, \
            begin = begin, end = end, encoding = encoding)

def _t1():
    image_info = (read_or_calc_xwrite(img_info_fname, build_calc_f()))

    download_jandan_ooxx_images(os.path.join(out_path, 'image'), image_info)

#format_html_file(r'C:/Users\Administrator\Desktop\tmp\oo.txt', r'C:/Users\Administrator\Desktop\tmp\xx.txt', 'gbk')
#p = (get_info_from_html_txt(html_txt, match_to_list_root, match_to_info, get_data_from_tree_list_node))
'''
p = (get_info_from_url(url, match_to_list_root, match_to_info, get_data_from_tree_list_node))
'
for t2_or_t3, (slot_idx, pattern_idx, info_pattern) in p:
    tag, attr, data = t2_or_t3
    if attr['id'].startswith('cos_unsupport-') or attr['id'].startswith('cos_support-'):
        data = get_the_exact_only_one_data_from_tree_list_node(data)
        data = int(data)
        print(attr['id'], data)
        break''
for t2_or_t3, (slot_idx, pattern_idx, info_pattern) in p:
    #if slot_idx > 0:break
    
    tag, attr = t2_or_t3[:2]
    #print(tag, attr)
    print(t2_or_t3)'''


def _t2():
    ipath = os.path.join(out_path, 'image')
    opath_fmt = 'image_oo_block_{}'
    block_size = 400
    #step = 30
    
    
    image_info = (read_or_calc_xwrite(img_info_fname, build_calc_f()))
    fname_url_oo_xx_list = jandan_ooxx_image_info2fname_url_oo_xx_list(\
        ipath, \
        image_info, \
        jandan_ooxx_image_file_name_fmt)

    fname_url_oo_xx_list.sort(key = lambda fu_ox: (fu_ox[-1][0] - fu_ox[-1][-1]//2))
    fname_url_oo_xx_block_list = list_split(fname_url_oo_xx_list, block_size)

    #for i, block in enumerate(fname_url_oo_xx_block_list):
    if True:
        i = len(fname_url_oo_xx_block_list)-1
        block = fname_url_oo_xx_block_list[-1]
        
        opath = opath_fmt.format(i)
        opath = os.path.join(out_path, opath)
        if not os.path.exists(opath):
            os.mkdir(opath)
        
        for (fname, _), (oo, _) in block:
            if os.path.exists(fname):
                ofname = os.path.join(opath, os.path.basename(fname))
                if os.path.exists(ofname):
                    raise Exception('{} exists!'.format(ofname))
                
                os.rename(fname, ofname)
                #break
            
                
_t = _t1


