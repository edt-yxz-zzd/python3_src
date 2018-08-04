# -*- coding: gb18030 -*-

from sand import zh_cn_encoding
from ..get_list_in_html_txt import *

comic_url = r'http://comic.zongheng.com/series/15.html'

'''
html_url2format2file(comic_url, 'tmp.html', zh_cn_encoding)


<div class="chapterli">
    <ul>
        <li>
            <a  href=... target="_blank" title="">
                1
            </a>

'''


class comic2chapters:
    match_to_list_root = [\
        ('div', {'class' : "chapterli"}),\
        ('ul', {}),\
        ('li', {}),\
        ('a', {'href':None, 'title':None}),\
        ]

    match_to_info = [\
        ('a', {'href':None}, 'data', {'href'}),\
        ]

    get_data_from_tree_list_node = get_the_exact_only_one_data_from_tree_list_node


def comic_url2chapter_urls(comic_url):
    g = get_info_from_url(comic_url, comic2chapters)
    
    ls = []
    for t2_or_t3, (slot_idx, pattern_idx, info_pattern) in g:
        tag, attrs, data = t2_or_t3
        chapter_name = data
        url = attrs['href']
        ls.append((chapter_name, url))
        
    return ls


#print(comic_url2chapter_urls(comic_url))

chapter_url = r'http://comic.zongheng.com/seriesShow/c31513.html'

'''
html_url2format2file(chapter_url, 'tmp.html', zh_cn_encoding)

'select', {'onchange': 'doRedirect()', 'id': 'imagePageNum', 'style': 'margin:0 10px 3px 10px'}
    ' \t\t\t\t \t\t\t\t'
    'option', {'value': '281145'}
            ' \t\t\t\t\t第1页 \t\t\t\t

'''



class chapter2image_pages:
    match_to_list_root = [\
        ('select', {'id': 'imagePageNum'}),\
        ('option', {'value': None}),\
        ]

    match_to_info = [\
        ('option', {'value': None}, None, {'value'}),\
        ]

    get_data_from_tree_list_node = None


def _image_page_idx2url_fmt(chapter_url, pattern = re.compile('(.*\D)(\d+)(\D*)')):
    a,b,c = pattern.search(chapter_url).group(*range(1,4))
    return a+b+'/i{}'+c
    image_page_url = r'http://comic.zongheng.com/seriesShow/c31513/i281145.html'
    
def chapter_url2image_page_urls(chapter_url):
    g = get_info_from_url(chapter_url, chapter2image_pages)

    ls = []
    for t2_or_t3, (slot_idx, pattern_idx, info_pattern) in g:
        tag, attrs = t2_or_t3
        idx = attrs['value']
        if ls and idx == ls[0]:
            break
        ls.append(idx)

    fmt = _image_page_idx2url_fmt(chapter_url)
    ls = tuple(fmt.format(idx) for idx in ls)
        
    return ls


#print(chapter_url2image_page_urls(chapter_url))

image_page_url = r'http://comic.zongheng.com/seriesShow/c31513/i281145.html'

'''
html_url2format2file(image_page_url, 'tmp.html', zh_cn_encoding)

'img', {
         'title': '点击进入下一页。',
         'id': 'disp',
         'onmousedown': 'imageMouseDown(this,event)',
         'onclick': 'doAfterPage();',
         'src': '...jpg'}

'''

class image_page2image:
    match_to_list_root = [\
        ('img', {'title': '点击进入下一页。', 'id': 'disp', \
                'onclick': 'doAfterPage();', 'src': None}),\
        ]

    match_to_info = [\
        ('img', {'src':None}, None, {'src'}),\
        ]

    get_data_from_tree_list_node = None


def image_page_url2image_url(image_page_url):
    g = get_info_from_url(image_page_url, image_page2image)

    ls = []
    for t2_or_t3, (slot_idx, pattern_idx, info_pattern) in g:
        tag, attrs = t2_or_t3
        url = attrs['src']
        ls.append(url)

    assert len(ls) == 1
    return ls[0]

#print(image_page_url2image_url(image_page_url))


class download_funcs:pass

download_funcs.comic_url2chapter_urls = comic_url2chapter_urls
download_funcs.chapter_url2image_page_urls = chapter_url2image_page_urls
download_funcs.image_page_url2image_url = image_page_url2image_url

def _t():
    from .download_chapters import download_chapters
    download_chapters('./gw', comic_url, 0, 1, download_funcs)
 
