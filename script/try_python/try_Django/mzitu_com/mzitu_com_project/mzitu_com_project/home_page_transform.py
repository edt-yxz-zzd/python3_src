

__all__ = '''
    home_page_transform__url

    home_page_transform__page
    extract_mzitu_com__the_all_or_old_page
    '''.split()
    #NotFoundError
    #find

from nn_ns.internet.webpage.fetch_webpage import fetch_webpage
from seed.helper.repr_input import repr_helper
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urlunparse
from pathlib import PurePosixPath as Path
from .DATA import project_per_page_url_route


r'''
def make_project_per_page_url_base(new_url):
    parse_result = urlparse(new_url)
    parts = (parse_result.scheme, parse_result.netloc, project_per_page_url_route, '', '', '')
    project_per_page_url_base = urlunparse(parts)
    return project_per_page_url_base
'''

r'''
def home_page_transform__url(old_url, new_project_website):
    # .DATA.website_all_old/website_all_new
    # e.g. home_page_transform__url(.DATA.website_all_old, 'http://127.0.0.1:8000/')
    # e.g. home_page_transform__url('https://www.mzitu.com/old/', 'http://127.0.0.1:8000/')
    # e.g. home_page_transform__url('https://www.mzitu.com/all/', 'http://127.0.0.1:8000/')
    #
    assert new_project_website[-1:] == '/'
'''


project_per_page_url_relative_base = Path(project_per_page_url_route)

def home_page_transform__url(old_url):
    # .DATA.website_all_old/website_all_new
    # e.g. home_page_transform__url(.DATA.website_all_old)
    # e.g. home_page_transform__url('https://www.mzitu.com/old/')
    # e.g. home_page_transform__url('https://www.mzitu.com/all/')
    #
    html_page = fetch_webpage(old_url)

    #project_per_page_url_base = make_project_per_page_url_base(new_url)
    assert project_per_page_url_route[:1] == '/'

    #project_per_page_url_base = new_project_website + project_per_page_url_route[1:]
    #project_per_page_url_base = Path(new_project_website, project_per_page_url_route)

    project_per_page_url_base = project_per_page_url_relative_base
    return home_page_transform__page(html_page, project_per_page_url_base)

class NotFoundError(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def __repr__(self):
        return repr_helper(self, *self.args, **self.kwargs)

def find(soup_find, *args, **kwargs):
    may_r = soup_find(*args, **kwargs)
    if may_r is None: raise NotFoundError(*args, **kwargs)
    r = may_r
    return r

def extract_mzitu_com__the_all_or_old_page(html_page):
    # html_page of .../all/ or .../old/
    #
    # html_page -> (html_title, [((year::str, month::str), [(old_url::str, title::str)])])
    #
    soup = BeautifulSoup(html_page, 'lxml')
    [html_title] = soup.head.find_all('title')
    html_title = html_title.get_text()

    [class_main] = soup.find_all('div', {'class': 'main'})
    [class_all] = class_main.find_all('div', {'class': 'all'})
    class_years = class_all.find_all('div', {'class': 'year'})

    #what's the name of tail-string?#?No such name in bs4?
    #print(dir(class_main))
    #import sys; sys.exit()


    year_month__url_title_pairs__pairs = []
    for class_year in class_years:
        year = class_year.get_text()
        class_archives = find(class_year.find_next_sibling, 'ul', {'class':'archives'})
        class_monthes = class_archives.find_all('p', {'class': 'month'})
        for class_month in class_monthes:
            month = class_month.get_text()
            class_url = find(class_month.find_next_sibling, 'p', {'class':'url'})
            href_children = class_url.find_all('a')

            year_month = year, month
            url_title_pairs = []
            for href_child in href_children:
                url = href_child['href']
                title = href_child.get_text()
                url_title_pairs.append((url, title))
            year_month__url_title_pairs__pairs.append((year_month, url_title_pairs))
    return html_title, year_month__url_title_pairs__pairs


new_html_begin = r'''
<!DOCTYPE html>
<html>
<head> <title></title> </head>
<body>
    <ul>
    </ul>
</body>
</html>
'''

body_tpl = r'''
{year} {month} {new_url} {title}
'''

def old_url2new_url(old_url, project_per_page_url_base:Path):
    project_per_page_url = project_per_page_url_base / Path(old_url).name
    new_url = project_per_page_url
    return new_url
def home_page_transform__page(html_page, project_per_page_url_base:Path):
    (html_title, year_month__url_title_pairs__pairs
    ) = extract_mzitu_com__the_all_or_old_page(html_page)

    new_soup = BeautifulSoup(new_html_begin, 'lxml')
    [new_title_tag] = new_soup.find_all('title')
    new_title_tag.append(html_title)
    [new_ul_tag] = new_soup.find_all('ul')

    for (year, month), url_title_pairs in year_month__url_title_pairs__pairs:
        new_li_tag = new_soup.new_tag('li')
        new_ul_tag.append(new_li_tag)

        fst_new_p_tag = new_soup.new_tag('p')
        new_li_tag.append(fst_new_p_tag)
        fst_new_p_tag.string = f'{year} {month}'

        snd_new_p_tag = new_soup.new_tag('p')
        new_li_tag.append(snd_new_p_tag)
        for old_url, title in url_title_pairs:
            new_url = old_url2new_url(old_url, project_per_page_url_base)
            new_href_tag = new_soup.new_tag('a', href=new_url, target="_blank")
            new_href_tag.string = title
            new_br_tag = new_soup.new_tag('br')

            snd_new_p_tag.append(new_href_tag)
            snd_new_p_tag.append(new_br_tag)

    #new_html_page = new_soup.encode('gb18030')
    new_html_page = str(new_soup)
    return new_html_page


