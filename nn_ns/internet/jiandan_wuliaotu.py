
from .get_list_in_html_txt import *
from sand import internet_except, format_output, zh_cn_encoding
import os
from sand.ptask import *
from sand.save_value import *

from .download_small_file import download_htmls, download_images, fname_url_list_filter
from sand import list_split

host = r'http://jandan.net/'

class jandan_info_t:
    page_file_name_fmt = r'{}.html'
    encoding = zh_cn_encoding
    image_file_name_fmt = r'{}_{}.jpg'
    
    def __init__(self, url, out_path, begin, end):
        self.url = url
        self.out_path = out_path
        self.begin = begin
        self.end = end
        self.page_out_path = os.path.join(out_path, 'html')
        self.image_out_path = os.path.join(out_path, 'image')
        self.img_info_fname = os.path.join(out_path, 'img_info_file')
        self.page_url_fmt = url + r'/page-{}'
        

jandan_wuliaotu = jandan_info_t(\
    url = r'http://jandan.net/pic',\
    out_path = r'./jandan_wuliao/',\
    begin = 4000, \
    end = 5207)


jandan_meizitu = jandan_info_t(\
    url = r'http://jandan.net/ooxx',\
    out_path = r'./jandan_meizi/',\
    begin = 900, \
    end = 1214)



def download_pages(path, file_name_fmt, begin, end, page_url_fmt, encoding):

    if not os.path.exists(path):
        os.makedirs(path)

    assert os.path.isdir(path)
    
    fname_url_list = []
    for i in range(begin, end):
        fname = os.path.join(path, file_name_fmt.format(i))
        url = page_url_fmt.format(i)
        fname_url_list.append((fname, url))

    fname_url_list = fname_url_list_filter(fname_url_list)
    
    download_htmls(fname_url_list, encoding)
    return


#download_pages(path = page_out_path)


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
'img', {'src': 'http://ww4.sinaimg.cn/mw600/e0dab130gw1eds4tqhca7j20cm0j9myp.jpg',
        #'org_src':...sometime}
'span', {'id': 'cos_support-2378453'}
        '113'
'span'
'span', {'id': 'cos_unsupport-2378453'}
        '42'
'span'
'''

class page2img:
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
def get_img_info_from_html_txt(html_txt):
    g = get_info_from_html_txt(html_txt, page2img)

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

def get_img_info_from_html_files(path, file_name_fmt, begin, end, encoding):

    assert os.path.isdir(path)
    
    fname_list = []
    for i in range(begin, end):
        fname = os.path.join(path, file_name_fmt.format(i))
        if not os.path.exists(fname):
            raise Exception('{!r} not exist'.format(fname))

        fname_list.append(fname)

    info = {}
    for fname in fname_list:
        _info = get_img_info_from_html_txt(read_txt(fname, encoding))
        info.update(_info)

    return info


def image_info2fname_url_oo_xx_list(path, image_info, file_name_fmt):
    fname_url_oo_xx_list = []
    for k, oo_xx_imgurls in image_info.items():
        oo, xx = oo_xx_imgurls[:2]
        for i, url in enumerate(oo_xx_imgurls[-1]):
            fname = file_name_fmt.format(k, i)
            fname = os.path.join(path, fname)
            fname_url_oo_xx_list.append(((fname, url), (oo, xx)))

    return fname_url_oo_xx_list

def download_jandan_images(path, image_info, file_name_fmt):
    fname_url_oo_xx_list = image_info2fname_url_oo_xx_list(path, image_info, file_name_fmt)
    fname_url_list = list(fname_url for fname_url, _ in fname_url_oo_xx_list)
    fname_url_list = fname_url_list_filter(fname_url_list)
    
    if not os.path.exists(path):
        os.makedirs(path)
    assert os.path.isdir(path)
    
    download_images(fname_url_list)

        
    
def build_calc_f(page_out_path, page_url_fmt, page_file_name_fmt, \
                 begin, end, encoding):
    def calc_f():
        download_pages(path = page_out_path, file_name_fmt = page_file_name_fmt, \
                       begin = begin, end = end, \
                       page_url_fmt = page_url_fmt, encoding = encoding)

        return get_img_info_from_html_files(\
            page_out_path, file_name_fmt = page_file_name_fmt, \
            begin = begin, end = end, encoding = encoding)
    return calc_f

def main(download_info_obj):
    calc_f = build_calc_f(download_info_obj.page_out_path, \
                          download_info_obj.page_url_fmt, \
                          download_info_obj.page_file_name_fmt, \
                          download_info_obj.begin, \
                          download_info_obj.end, \
                          download_info_obj.encoding)
    image_info = (read_or_calc_xwrite(download_info_obj.img_info_fname, calc_f))

    download_jandan_images(download_info_obj.image_out_path, \
                           image_info, \
                           download_info_obj.image_file_name_fmt)

def _t1():
    main(jandan_wuliaotu)
    return 
    download_info_obj = jandan_wuliaotu
    ls = [\
        "img_info_file_0_300",\
        "img_info_file_300_600",\
        "img_info_file_600_750",\
        "img_info_file_750_800",\
        "img_info_file_800_801",\
        "img_info_file_801_802",\
        "img_info_file_802_",\
        ]

    info = {}
    for fn in ls:
        fn = os.path.join(download_info_obj.out_path, fn)
        info.update(read_value(fn))

    write_value(info, download_info_obj.img_info_fname)

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


