from .get_list_in_html_txt import get_html
from sand import write_bin, write_txt, internet_except
import os
from sand.ptask import *

#from breakpoint_continuingly_multithreaded_download import get_head
from .http_do import http_do#, _request_headers



_max_workers = 10



def fname_url_list_filter(fname_url_list):
    ls = []
    for fname_url in fname_url_list:
        fname = fname_url[0]
        if not os.path.exists(fname):
            ls.append(fname_url)

    return ls




def download_html(fname, url, encoding):
    if os.path.exists(fname):
        raise Exception('{fname} already exists'.format(fname = fname))

    write_txt(fname, get_html(url), encoding)





def download_files(fname_url_list, download_file_f):
    worker = download_file_f
    task_info = (((worker, fname_url[0], fname_url[1]), fname_url)\
                 for fname_url in fname_url_list)
    for branch, info_ in ptask(task_info, max_workers=_max_workers):
        if branch == except_branch:
            info, exc = info_
            print('{!r} generated an exception: {!s}'.format(info, exc))
        elif branch == except_else_branch:
            info, data = info_
            pass
        elif branch == finally_branch:
            pass
        else:
            raise unknown_case_except('ptask branch', \
                'func@download_files')
    
    return

def download_htmls(fname_url_list, encoding):
    download_file_f = lambda fname, url: download_html(fname, url, encoding)
    download_files(fname_url_list, download_file_f)





def download_image(fname, url):
    if os.path.exists(fname):
        raise Exception('{fname} already exists'.format(fname = fname))

    r = http_do(url, 'GET', timeout=60*2)
    if r.reason != 'ok':
        raise internet_except('http_do GET fail: url = {}'.format(url))

    write_bin(fname, r.data)
    
'''
url = r'http://ww1.sinaimg.cn/mw600/789dfeffjw1eekgxcxp2wj20dc0hs0vf.jpg'
fname = r'tmp.jpg'
download_image(fname, url)'''


def download_images(fname_url_list):
    download_files(fname_url_list, download_image)












