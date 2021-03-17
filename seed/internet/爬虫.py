
r'''
website = regex'//{url_char}+'
incomplete_href = regex'(/{url_char}+)+/?'
complete_href = regex'{website}{incomplete_href}?'
href = complete_href | incomplete_href
website <: complete_href
final_href <: complete_href
    href may jump/redirect

html_doc <: text
bs4_doc <- html_doc


#'''

import re


from urllib.parse import urlparse


class 爬虫:
    def get_bs4_ops(sf):
        '-> bs4_ops'
    def get_website2handler(sf):
        '-> (website -> 爬虫)'
        #重点1
    def get_maybe_base_websitw(sf):
        '-> website'
    def get_download_dir(sf):
        '-> download_dir'
    def get_database_dir(sf):
        '-> database_dir'
    def 网址补全(sf, href):
        '(incomplete_href|complete_href) -> complete_href'
    def 读取或下载(sf, href):
        'href -> raise|(final_href, fname, maybe_encoding)'
    def 读取(sf, href):
        'href -> ()|(final_href, fname, maybe_encoding)'
    def 直接下载(sf, href):
        'href -> raise|(final_href, fname, maybe_encoding)'
    def 分支(sf, html_doc):
        'html_doc -> Iter (file_type, href)'
    def 分支__bs4(sf, bs4_doc):
        'bs4_doc -> Iter bs4_href_tag #<a><img>...'
        #重点2

    def 爬(sf, href):
        'href -> None'







