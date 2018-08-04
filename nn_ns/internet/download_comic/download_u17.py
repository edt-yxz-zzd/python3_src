# -*- coding: gb18030 -*-

import base64, re

from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor

from sand import zh_cn_encoding
from ..get_list_in_html_txt import *


comic_url = r'http://www.u17.com/comic/42730.html'

'''
html_url2format2file(comic_url, 'tmp.html', zh_cn_encoding)

'div', {'class': 'chapterlist_box'}
    'ul', {'class': 'cf', 'id': 'chapter'}
            '\r\n                                                                                                                        '
            'li', {'id': 'cpt_read_188735'}
                    '\r\n                    '
                    'a', {'id': 'cpt_188735', 'target': '_blank', 'title': '006 孙悟空？孙悟空！ 2013-04-22', 'href': 'http://www.u17.com/chapter/188735.html'}
'''

class comic2chapters:
    match_to_list_root = [\
        ('div', {'class': 'chapterlist_box'}),\
        ('ul', {'class': 'cf', 'id': 'chapter'}),\
        ('li', {'id': None}),\
        ]

    match_to_info = [\
        ('a', {'id': None, 'target': '_blank', 'title': None, 'href': None}, None, {'title', 'href'}),\
        ]

    get_data_from_tree_list_node = None


def comic_url2chapter_urls(comic_url):
    g = get_info_from_url(comic_url, comic2chapters)

    ls = []
    for t2_or_t3, (slot_idx, pattern_idx, info_pattern) in g:
        tag, attrs = t2_or_t3
        title = attrs['title']
        href = attrs['href']
        ls.append((title, href))
        
    return ls

#print(comic_url2chapter_urls(comic_url))

chapter_url = r'http://www.u17.com/chapter/188735.html'

'''
html_url2format2file(chapter_url, 'tmp.html', zh_cn_encoding)

'html', {}
    '\r\n'
    'head', {}
        'script', {}
            '...;var image_config = {
                comic: $.evalJSON(\'{...}\'),
                chapter: $.evalJSON(\'{...}\'),
                ...,
                image_list: $.evalJSON(\'{
                    "1":{"src":"...",...},...
                    }

                ...
                }
                ...
        'script'
#'''



class chapter2images:
    match_to_list_root = [\
        ('html', {}),\
        ('head', {}),\
        ('script', {}),\
        ]

    match_to_info = [\
        ('script', {}, 'data', {}),\
        ]

    def get_data_from_tree_list_node(node):
        try:
            return get_the_exact_only_one_data_from_tree_list_node(node)
        except:
            return ''
    

_image_list_match_pattern = re.compile(r'image_list\s*:\s*\$\.evalJSON\((.*)\)')
def chapter_url2image_urls(chapter_url):
    g = get_info_from_url(chapter_url, chapter2images)

    p = Parser()
    for t2_or_t3, (slot_idx, pattern_idx, info_pattern) in g:
        tag, _, data = t2_or_t3
        #p = Parser()
        tree = p.parse(data)
        pre = None
        for node in nodevisitor.visit(tree):
            if isinstance(node, ast.Identifier) and node.value == 'image_list':
                break
            pre = node

    assert pre != None
    m = _image_list_match_pattern.match(pre.to_ecma())
    assert m != None
    image_list = eval(m.group(1))
    image_list = eval(image_list)

    ls = []
    for info in image_list.values():
        src = base64.b64decode(info['src']).decode('ascii')
        page = info['page']
        ls.append((page, src))

    ls.sort()
    ls = tuple(src for _, src in ls)
    
        
    return ls

#print(chapter_url2image_urls(chapter_url))



class download_funcs:pass

download_funcs.comic_url2chapter_urls = comic_url2chapter_urls
download_funcs.chapter_url2image_page_urls = chapter_url2image_urls
download_funcs.image_page_url2image_url = lambda x:x



def _t():
    from .download_chapters import download_chapters
    download_chapters('./wkz', comic_url, 0, 1, download_funcs)
    

