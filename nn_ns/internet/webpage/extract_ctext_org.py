
'''

why fail?
    1. <form action=action_url, method='post'>...</form>
        POST to action_url
            with data={soup['name']:soup['value']
                for soup in form_soup.find_all(hasattr 'name'&'value')}
                # hence not include 'submit'
            with headers.referrer = ...
    2. allow_redirects=True
        should use requests instead of urllib
    3. need session to hold cookies
        should use requests instead of urllib

https://ctext.org/
https://ctext.cn/

https://ctext.org/fengshen-yanyi/
https://ctext.org/fengshen-yanyi/1
https://ctext.org/fengshen-yanyi/zh
https://ctext.org/fengshen-yanyi/1/zh
    漢代之後 -> 宋明 -> 封神演義 -> 紂王女媧宮進香
    <meta property="og:title" content="紂王女媧宮進香"/>
    class="ctext opt"
        text in this class should be removed
    class="ctext"
        extract text in this class

https://ctext.org/quantangshi/900/zh
    <tr>
    <td><h2>《<a href="text.pl?node=108542&amp;if=gb" class="popup">帝京篇十首</a>》</h2></td>
    <td><span class="etext opt"><b> 李世民著</b></span></td>
    <td align='right'> ... </td>
    </tr>


http://ctext.org/guo-yu/zh
    <head>
        <base href="https://ctext.org/"/>
        ...
        <meta content="book" property="og:type"/>
        <meta content="國語" property="og:title"/>
        <meta content="http://ctext.org/guo-yu/zh" property="og:url"/>
        <title>國語 - 中國哲學書電子化計劃</title>
        ...
    </head>
    <body ...>
        ...
        <div id="menubar">...<div id="menu">
            ...
            <span class="menuitem container"><a class="menuitem" href="guo-yu/zh" id="m24449">國語</a><br/><span class="subcontents">
                <a class="menuitem" href="guo-yu/zhou-yu-shang/zh" id="m24451">周語上</a><br/>
                <a class="menuitem" href="guo-yu/zhou-yu-zhong/zh" id="m24481">周語中</a>
                ...
            </span></span>
            ...
        </div>...</div>
        <div id="content">...</div>
    </body>



https://ctext.org/wiki.pl?if=gb&res=115079
    <div class="ctext" style="margin: 10px; float: left;">
        <a href="wiki.pl?if=gb&amp;chapter=797963">第一卷</a>
            <a href="wiki.pl?if=gb&amp;chapter=797963#考城隍">考城隍</a>
            <a href="wiki.pl?if=gb&amp;chapter=797963#耳中人">耳中人</a>
    </div>
https://ctext.org/wiki.pl?if=gb&chapter=797963
    維基 -> 聊齋誌異 -> 第一卷

https://ctext.org/wiki.pl?if=gb&res=47184

example:
    $ pym extract_ctext_org.py -url https://ctext.org/fengshen-yanyi/1
    $ pym extract_ctext_org.py -url https://ctext.org/fengshen-yanyi/ -rng 1 100 -o 封神演義[ctext.org].txt -e utf8 --verbose --timeout=10 --time_sep=10

https://ctext.org/xiyouji/ch1
    $ pym extract_ctext_org.py -url https://ctext.org/xiyouji/ -rng 1 100 -o 西遊記[ctext.org].txt -e utf8 --verbose --timeout=10 --time_sep=1 --index_format=ch{} --without_book_title --append

https://ctext.org/sanguo-yanyi/ch33/zh
    $ pym extract_ctext_org.py -url https://ctext.org/sanguo-yanyi/ -rng 1 2 -o 三國演義[ctext.org].txt -e utf8 --verbose --timeout=10 --time_sep=1 --index_format="ch{}/zh"
    $ pym extract_ctext_org.py -url https://ctext.org/sanguo-yanyi/ -rng 3 120 -o 三國演義[ctext.org].txt -e utf8 --verbose --timeout=10 --time_sep=1 --index_format="ch{}/zh" --without_book_title --append

https://ctext.org/jinpingmei/ch1
    $ pym extract_ctext_org.py -url https://ctext.org/jinpingmei/ -rng 1 100 -o 金瓶梅[ctext.org].txt -e utf8 --verbose --timeout=10 --time_sep=1 --index_format="ch{}"
    $ pym extract_ctext_org.py -url https://ctext.org/jinpingmei/ -rng 21 100 -o 金瓶梅[ctext.org].txt -e utf8 --verbose --timeout=10 --time_sep=1 --index_format="ch{}" --without_book_title --append

'''


'''
#####################https://www.w3schools.com/html/html_forms.asp
##################### xxxx ?? will post {'message'=???, 'submit'='OK'} to "https://ctext.org/unban.pl"
##################### xxxx ?? will get "https://ctext.org/unban.pl?message=???"
##################### yes ?? will post {'message'=???} to "https://ctext.org/unban.pl"
#####################
<form action="https://ctext.org/unban.pl" method="post">
<table><tr><td>Validation image:<br />認證圖案：</td><td><span id="imageholder"></span></td></tr>
<tr><td>Type the letters in the above image:<br />輸入上述認證圖案中的字：</td><td><input type="text" name="message" /></td></tr>
<tr><td></td><td><input type="submit" value="OK" /></td></table>
</form>

<script>
window.onload = function() {
  document.getElementById('imageholder').innerHTML = "<img src='https://ctext.org/captcha.pl?random=" + Math.floor(Math.random()*100000) + "' />";
}
</script>
'''

#from .fetch_webpage import open_webpage, fetch_webpage
#from .download import download_file_from_url_ex
from . import _configure_
from seed.tiny import print_err
from seed.for_libs.for_tkinter.ask_maybe_input import ask_maybe_input
from seed.types.pair_based_leftward_list import iter_leftward_list

import requests
import PIL.Image, PIL.ImageTk
from bs4 import BeautifulSoup

import traceback
import io
import random
import time
import socket
import re
import shelve
import itertools
#from collections import OrderedDict


#from pathlib import PurePosixPath as Path
#import os.path

def show_session(session):
    return
    attrs = type(session).__attrs__
    print_err('show_session')
    for attr in attrs:
        value = getattr(session, attr, None)
        print_err(f'\t{attr}={value!r}')

TimeoutErrors = (TimeoutError, socket.timeout)
class CTextOrgConfirmError(Exception):
    def __init__(self, *args, action_url, text_field_name, **kwargs):
        self.action_url = action_url
        self.text_field_name = text_field_name
        super().__init__(*args, **kwargs)
    pass

def swap_to_last(ls, i):
    ls[i], ls[-1] = ls[-1], ls[i]
def swap_to_last_and_pop(ls, i):
    swap_to_last(ls, i)
    ls.pop()
def get_tag__lower(soup):
    return str(soup.name).lower()
def get_classes__lower(soup):
    if not soup.has_attr('class'): return set()
    return {cls.lower() for cls in soup['class']}
def has_html_class(soup, cls):
    return cls.lower() in get_classes__lower(soup)
def assert_html_class_single(soup):
    clss = get_classes__lower(soup)
    if not len(clss) == 1: raise Exception(clss)
    return True
def get_text_prime(soup):
    return soup.get_text().strip()

class Global:
    captcha_url_random_range = 100000
    captcha_url_fmt = 'https://ctext.org/captcha.pl?random={}'
    re_newline = re.compile(r'(?:\n\r|\r\n|\n|\r)')
    new_line = '\n'
    escaped_new_line = f'{new_line}#'


class ExtractCTextOrgBase:
    def pred_ver1(self, soup):
        #ver1: ctexts = soup.find_all(attrs={'class': 'ctext'})
        #   has not 'opt'
        clss = get_classes__lower(soup)
        if 'ctext' in clss:
            if 'opt' in clss:
                assert len(clss) == 2
                return False
            else:
                assert len(clss) == 1
                return True
        return False

    def _pred_ver2(self, soup):
        #ver2: +<h2>
        return get_tag__lower(soup) == 'h2'
    def pred_ver2(self, soup):
        return self._pred_ver2(soup) or self.pred_ver1(soup)
    def _pred_ver3(self, soup):
        #ver3: +<td><span class="etext opt"><b> 李世民著</b></span></td>
        return get_classes__lower(soup) == {'etext', 'opt'}
    def pred_ver3(self, soup):
        return self._pred_ver3(soup) or self.pred_ver2(soup)
    def get_text_ver1(self, soup):
        return self.escape_per_line(get_text_prime(soup))
    def _get_text_ver2(self, soup):
        section_title = get_text_prime(soup)
        return f'[h2]:{section_title!r}'
    def get_text_ver2(self, soup):
        if self._pred_ver2(soup):
            return self._get_text_ver2(soup)
        return self.get_text_ver1(soup)
    def _get_text_ver3(self, soup):
        author = get_text_prime(soup)
        return f'[etext opt]:{author!r}'
    def get_text_ver3(self, soup):
        if self._pred_ver3(soup):
            return self._get_text_ver3(soup)
        return self.get_text_ver2(soup)
    pred_ver_LAST = pred_ver3
    get_text_ver_LAST = get_text_ver3


    def extract_ctext_org__subcontents(self, html_file, *, verbose:bool):
        # -> ((title, url), [(subtitle, sub_url)])
        soup = BeautifulSoup(html_file, 'lxml')
        verbose = bool(verbose)

        (base_url, type, title, url
        ) = self.extract_ctext_org__step1_base_type_title_url(soup, verbose=verbose)
        assert type.lower() == 'book'
        (middle_titles_subtitle_url_triples
        ) = self.extract_ctext_org__step2_iter_middle_titles_subtitle_url_triples(soup, title, base_url, verbose=verbose)
        subtitle_url_pairs = (
            (repr((*middle_titles, subtitle)), sub_url)
            for middle_titles, subtitle, sub_url
            in middle_titles_subtitle_url_triples
            )
        return (title, url), tuple(subtitle_url_pairs)

    def extract_ctext_org__text(self, html_file, *, verbose:bool):
        soup = BeautifulSoup(html_file, 'lxml')
        verbose = bool(verbose)

        title = self.extract_ctext_org__step1_title(soup, verbose=verbose)
        txt = self.extract_ctext_org__step2_ctext(soup, verbose=verbose)
        if verbose: print_err('extract_ctext_org__text done!')
        return title, txt
    def extract_ctext_org__step1_base_type_title_url(self, soup, *, verbose:bool):
        # -> (str, str, str, str)
        # -> (base_url, type, title, url)
        #<meta content="book" property="og:type"/>
        #<meta content="國語" property="og:title"/>
        #<meta content="http://ctext.org/guo-yu/zh" property="og:url"/>
        verbose = bool(verbose)

        _title = self.extract_ctext_org__step1_title(soup, verbose=verbose)
        soup = soup.head
        [base_url_soup] = soup.find_all(name='base')
        base_url = str(base_url_soup['href'])

        names = ('type', 'title', 'url')
        def get(name):
            property = f"og:{name}"
            meta_soup = soup.find(name='meta', property=property)
            if meta_soup is None: raise ValueError(f'not found: {property!r}')
            value = str(meta_soup['content'])
            if verbose: print_err(f'{name}: {value!r}')
            return value
        return (base_url, *map(get, names))

    def extract_ctext_org__step1_title(self, soup, *, verbose:bool):
        # html_file -> title
        # html_file may be BytesIO/StringIO?
        verbose = bool(verbose)

        title_soup = soup.find('meta', property="og:title")
        if title_soup is None:
            [form_soup] = soup.find_all('form', method='post')
            [text_field_soup] = form_soup.find_all('input', type='text')
            text_field_name = str(text_field_soup['name'])
            action_url = form_soup['action']
            raise CTextOrgConfirmError(
                action_url=action_url, text_field_name=text_field_name
                )

        title = title_soup['content']
        if verbose: print_err(f'title: {title!r}')
        return title

    def extract_ctext_org__step2_iter_middle_titles_subtitle_url_triples(self, soup, title, base_url, *, verbose:bool):
        # -> Iter (middle_titles, subtitle, sub_href)
        # middle_titles = [middle_title]
        #
        #.find_all(string=re.compile('\s*{}\s*'.format(re.escape('title'))))
        '''
        span menuitem_container
            a menuitem_href
                #href, title
            span subcontents
                [(menuitem_href | menuitem_container)
        '''
        #subcontents
        #tree structure
        #   many middle parents...
        #   so search the first title that match
        main_menuitem_href_soup = (soup.body
                                .find('div', id='menubar')
                                .find('div', id='menu')
                                .find(name='a'
                                    , attrs={'class':'menuitem'}
                                    , string=title)
                                )
        '''
        url = url.lower()
        this_href = str(main_menuitem_href_soup['href']).lower()
        url.endswith(this_href)
        url_root = url[:-len(this_href)]
        assert url_root and url_root[-1] == '/'
        '''
        url_root = base_url
        assert url_root and url_root[-1] == '/'

        topmost_span_container_soup = main_menuitem_href_soup.parent

        #<span class="menuitem container"><a class="menuitem" href="guo-yu/zh" id="m24449">國語</a><br/><span class="subcontents">

        # visit_(soup):
        # -> Iter (middle_titles, subtitle, sub_href)
        # middle_titles = () | (middle_title, middle_titles)
        def visit_menuitem_href(menuitem_href_soup):# is_topmost:bool:
            #leaf
            subtitle = str(menuitem_href_soup.string)
            #bug: sub_href = menuitem_href_soup.href
            sub_href = str(menuitem_href_soup['href'])
            assert sub_href and sub_href[0] != '/'
            sub_href = url_root + sub_href
            yield (), subtitle, sub_href

        def pred(soup):
            if has_html_class(soup, 'subcontents'):
                return False
            if soup.name.lower() == 'span':
                return has_html_class(soup, 'container')
            return True
        def visit_subcontents(span_subcontents_soup):# is_topmost:bool:
            it = span_subcontents_soup.find_all(
                                name=['a', 'span']
                                , attrs={'class':'menuitem'}
                                , recursive=False
                                )
            children = list(filter(pred, it))
            for child in children:
                if child.name.lower() == 'a':
                    visit = visit_menuitem_href
                else:
                    visit = visit_container
                yield from visit(child)

        def visit_container(span_container_soup):# is_topmost:bool:
            #tree structure
            #   many subcontents if children is a tree too
            #   so, recursive=False
            [menuitem_href_soup
            ] = (span_container_soup
                    .find_all(name='a'
                            , attrs={'class':'menuitem'}
                            , recursive=False
                            )
                )
            [span_subcontents_soup
            ] = (span_container_soup
                    .find_all(name='span'
                            , attrs={'class':'subcontents'}
                            , recursive=False
                            )
                )
            #menuitem_href_soup['href']
            middle_title = str(menuitem_href_soup.string)
            it = visit_subcontents(span_subcontents_soup)
            for middle_titles, subtitle, sub_href in it:
                yield (middle_title, middle_titles), subtitle, sub_href

        it = visit_container(topmost_span_container_soup)
        for middle_titles, subtitle, sub_href in it:
            middle_titles = list(iter_leftward_list(middle_titles))
            yield (middle_titles, subtitle, sub_href)

    def extract_ctext_org__step2_ctext(self, soup, *, verbose:bool):
        verbose = bool(verbose)
        #ver1: ctexts = soup.find_all(attrs={'class': 'ctext'})
        #ls = [ctext.get_text().strip()
        #       for ctext in ctexts
        #       if not has_html_class(ctext, 'opt')
        #           and assert_html_class_single(ctext)
        #   ]
        #ver2: +<h2>
        #ver3: +class='etext opt'
        pred = self.pred_ver_LAST
        get_text = self.get_text_ver_LAST
        ctexts = soup.find_all(pred)
        ls = [get_text(ctext) for ctext in ctexts]

        txt = Global.new_line.join(ls)
        return txt
    def escape_per_line(self, txt):
        # '{line}' -> '#{line}'
        txt = '#' + Global.re_newline.sub(Global.escaped_new_line, txt)
        return txt


class ExtractCTextOrg(ExtractCTextOrgBase):
    def __init__(self, *, cache_fname, captcha_image_db_fname):
        self.cache_fname = cache_fname
        self.cache = shelve.open(cache_fname)
        self.session = requests.Session()
        self.captcha_image_db = shelve.open(captcha_image_db_fname)
        show_session(self.session)
    def close(self):
        self.cache.close()
        self.captcha_image_db.close()
    def save_captcha(self, *, image_bytes, captcha:str, correct:bool):
        if type(image_bytes) is not bytes: raise TypeError
        if type(captcha) is not str: raise TypeError
        if type(correct) is not bool: raise TypeError
        L = len(self.captcha_image_db)
        for i in itertools.count(L):
            key = f'{i}_{captcha}'
            if key in self.captcha_image_db: continue
            self.captcha_image_db[key] = (correct, image_bytes)
            break
        return
    def make_headers(self, *, referrer):
        headers = {'User-Agent': _configure_.UserAgent, 'Referer': referrer}
        if referrer is None:
            del headers['Referer']
        return headers

    def fetch_webpage(self, url, *, timeout, referrer):
        # -> page_bytes
        return self.download_file_from_url(url
            , timeout=timeout, referrer=referrer)
    def download_file_from_url(self, url, *, timeout, referrer):
        # -> content_data
        headers =self.make_headers(referrer=referrer)
        r = self.session.get(url, timeout=timeout, headers=headers)
        show_session(self.session)
        data = r.content
        assert type(data) is bytes
        return data

    def fecth_captcha_image__bytes(self, *, referrer, timeout, **kwargs):
        i = random.randrange(Global.captcha_url_random_range)
        #print_err(f"random i for captcha_url_fmt: {i}={i:x}")
        image_url = Global.captcha_url_fmt.format(i)
        content_data = self.download_file_from_url(image_url
            , referrer=referrer, timeout=timeout, **kwargs)

        if False:
            print_err(f'captcha image content_type:{content_type!r}')
            print_err(type(content_data))
            print_err(content_data)
            #assert content_type.lower().startswith('image')
        return content_data


    def ask_maybe_captcha_ex(self, *, title, referrer, timeout, **kwargs):
        # -> ()|(image_bytes:bytes, captcha:str)
        image_bytes = self.fecth_captcha_image__bytes(
            referrer=referrer, timeout=timeout, **kwargs)
        image_file = io.BytesIO(image_bytes)
        image_PIL = PIL.Image.open(image_file)
        maybe_captcha = ask_maybe_input(title=title, prompt='', image_PIL=image_PIL)
        if maybe_captcha:
            [captcha] = maybe_captcha
            captcha_ex = image_bytes, captcha
            maybe_captcha_ex = captcha_ex
        else:
            maybe_captcha_ex = ()
        del maybe_captcha
        return maybe_captcha_ex

    def post_captcha(self, *, referrer, action_url, text_field_name, captcha
        , timeout, **kwargs):
        data = {text_field_name: captcha}
        headers =self.make_headers(referrer=referrer)
        print_err(f'data={data}; headers={headers}')
        r = self.session.post(action_url, headers=headers, data=data
            , allow_redirects=True, timeout=timeout)
        show_session(self.session)
        data = r.content # read but discard
        return data
        return
        print_err(data)
        if input('(input yes to continue)>>>') != 'yes':
            raise KeyboardInterrupt
        return
        ######### fail
        self.fetch_webpage(action_url, referrer=referrer
            , data=data, timeout=timeout, **kwargs)

    def cached_extract_ctext_org__url(self, url
        , *, verbose:bool, timeout, referrer, subcontents:bool, **kwargs):
        # url -> (title, txt)
        verbose = bool(verbose)
        subcontents = bool(subcontents)

        fetch = lambda: self.bare_extract_ctext_org__url(url
                , referrer=referrer
                ,verbose=verbose, timeout=timeout
                ,subcontents=subcontents
                , **kwargs
                )
        if not subcontents:
            key = url
        else:
            key = '[subcontents]'+url

        def result2title(result):
            if not subcontents:
                title, txt = result
            else:
                ((title, _url), subtitle_url_pairs) = result
            return title

        if verbose:
            str_may_subcontents = '[subcontents]' if subcontents else ''
        if key not in self.cache:
            result = fetch()
            self.cache[key] = result
            title = result2title(result)

            if verbose: print_err(f'store title{str_may_subcontents!s}: {title!r}')

        if verbose: print_err(f'read cached webpage: {url!r}')
        result = self.cache[key]
        title = result2title(result)
        if verbose: print_err(f'read title{str_may_subcontents!s}: {title!r}')
        return result

    def bare_extract_ctext_org__url(self, url
        , *, verbose:bool, timeout, referrer, subcontents:bool, **kwargs):
        # url -> (title, txt)
        verbose = bool(verbose)
        try:
            if verbose: print_err(f'fetch webpage: {url!r}')
            page_bytes = self.fetch_webpage(url
                , timeout=timeout, referrer=referrer, **kwargs)

            if verbose: print_err(f'extracting webpage...: {url!r}')
            if not subcontents:
                title, txt = self.extract_ctext_org__text(page_bytes, verbose=verbose)
                result = title, txt
            else:
                ((title, url), subtitle_url_pairs
                ) = self.extract_ctext_org__subcontents(page_bytes, verbose=verbose)
                subtitle_url_pairs = tuple(subtitle_url_pairs)
                result = (title, url), subtitle_url_pairs
            if verbose: print_err(f'extract webpage done: {url!r}')
            return result
        except (CTextOrgConfirmError, *TimeoutErrors):
            if verbose: print_err(f'extract webpage timeout: {url!r}')
            raise
        except Exception as e:
            if verbose: print_err(f'extract webpage error: {url!r}')
            raise Exception(f'url={url!r}', e)
    def ordered_iter_extract_ctext_org__url_rng__cache_only(self
        , base_url, indices, index_format
        ):
        # -> Iter (title, txt)
        referrer_url_pairs = self.make_referrer_url_pairs__url_rng(
                base_url, indices, index_format)
        for referrer, url in referrer_url_pairs:
            title, txt = self.cache[url]
            yield title, txt
    def unordered_iter_extract_ctext_org__url_rng(self
        , base_url, indices, index_format, *
        , verbose:bool, timeout, time_sep, **kwargs
        ):
        # url -> begin -> end -> Iter (title, txt)
        #base_url = Path(base_url)
        verbose = bool(verbose)
        if verbose: print_err(f'fetch&extract webpages from: {base_url!r}')
        referrer_url_pairs = self.make_referrer_url_pairs__url_rng(
                base_url, indices, index_format)
        return self.unordered_iter_extract_ctext_org__referrer_url_pairs(
            referrer_url_pairs
            , verbose=verbose, timeout=timeout, time_sep=time_sep
            , **kwargs
            )

    def make_referrer_url_pairs__url_rng(self
        , base_url, indices, index_format):
        if base_url[-1:] == '/':
            base_url = base_url[:-1]
        referrer = base_url
        base_fmt = f'{base_url}/{index_format}'
        referrer_url_pairs = [
            (referrer, base_fmt.format(i))
            for i in indices
            ]
        return referrer_url_pairs

    def unordered_iter_extract_ctext_org__referrer_url_pairs(self
        , referrer_url_pairs, *
        , verbose:bool, timeout, time_sep, **kwargs
        ):
        # referrer_url_pairs :: [(referrer, url)]
        # -> Iter (referrer, url, title, txt)
        verbose = bool(verbose)
        referrer_url_pairs = list(referrer_url_pairs)

        while referrer_url_pairs:
            i = random.randrange(len(referrer_url_pairs))
            referrer, url = referrer_url_pairs[i]
            if verbose: print_err(f'to fetch&extract webpage {url!r} from: {referrer!r}')

            if url not in self.cache:
                t = random.randrange(time_sep, 2*time_sep)
                if verbose: print_err(f'sleep {t}s before fetch&extract webpage')
                time.sleep(t)

            try:
                title, txt = self.cached_extract_ctext_org__url(url
                    , referrer=referrer
                    , verbose=verbose, timeout=timeout
                    , subcontents=False
                    , **kwargs)
            except CTextOrgConfirmError as e:
                #input('ctext.org requires confirm')
                self.handle_captcha_confirm(
                    from_url = url
                    , action_url = e.action_url
                    ,text_field_name = e.text_field_name
                    ,verbose=verbose
                    ,timeout=timeout, **kwargs
                    )
                continue
            except KeyboardInterrupt:
                raise
            except (Exception, OSError, *TimeoutErrors) as e:
                self.handle_exc(e)
                continue
            yield url, referrer, title, txt

            L = len(referrer_url_pairs)
            swap_to_last_and_pop(referrer_url_pairs, i)
            assert len(referrer_url_pairs) == L-1


    def handle_captcha_confirm(self, *
        , from_url, action_url, text_field_name
        , verbose, timeout, **kwargs):
        verbose = bool(verbose)

        if verbose: print_err(f'text_field_name={text_field_name!r}; action_url={action_url!r}; from_url={from_url!r}')

        while True:
            try:
                maybe_captcha_ex = self.ask_maybe_captcha_ex(
                        title='ctext.org requires confirm'
                        ,referrer=from_url
                        ,timeout=max(10, timeout)
                        ,**kwargs
                        )
                if not maybe_captcha_ex:
                    raise KeyboardInterrupt
                [image_bytes, captcha] = maybe_captcha_ex

                if not captcha: raise logic-error
                if verbose: print_err(f'input captcha = {captcha!r}')
                data = self.post_captcha(
                    action_url=action_url
                    , text_field_name=text_field_name
                    , referrer=from_url
                    , captcha=captcha
                    , timeout=timeout, **kwargs)

                try:
                    self.extract_ctext_org__text(data, verbose=False)
                except CTextOrgConfirmError:
                    # input wrong captcha
                    self.save_captcha(image_bytes=image_bytes, captcha=captcha, correct=False)
                except Exception as e:
                    # unknown error
                    self.handle_exc(e)
                else:
                    # input correct captcha
                    self.save_captcha(image_bytes=image_bytes, captcha=captcha, correct=True)

            except KeyboardInterrupt:
                raise
            except Exception as e:
                self.handle_exc(e)
                continue
            else:
                break
        #end while
        return
    def handle_exc(self, e):
        # requests.exceptions.ConnectionError
        print_err(repr(type(e)))
        print_err(repr(e))
        if input('(input nothing to quit) >>>'):
            traceback.print_exc()
            return None
        else:
            raise


def _test_file():
    fname = r'E:\download\novel_new\novel_20170808\小说\https _ctext.cn_fengshen-yanyi_1.htm'
    self = ExtractCTextOrgBase()
    with open(fname, encoding='utf8') as fin:
        print(self.extract_ctext_org__text(fin, verbose=False))

def _test_url():
    url = r'https://ctext.org/fengshen-yanyi/1'
    print(self.cached_extract_ctext_org__url(url, subcontents=False, verbose=False))
def _test_url_rng():
    base_url = r'https://ctext.org/fengshen-yanyi'
    for title, txt in self.unordered_iter_extract_ctext_org__url_rng(base_url, range(1,100+1), verbose=False):
        print(title)
        print(txt)
        break

def _t():
    sep = '='*20
    print(sep, '_test_file', sep)
    _test_file()
    print(sep, '_test_url', sep)
    _test_url()
    print(sep, '_test_url_rng', sep)
    _test_url_rng()


def main(argv=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout


    parser = argparse.ArgumentParser(
        description='extract text on ctext.org or ctext.cn'
        )
    parser.add_argument('-e', '--encoding', type=str, default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-i', '--input', type=str, default = None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default = None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('--append', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-V', '--verbose', action='store_true'
                        , default = False
                        , help='show path/url that opened')
    parser.add_argument('-url', '--url', type=str, default = None
                        , help='input webpage url')
    parser.add_argument('-rng', '--range', type=int, default = None
                        , nargs = 2
                        , help='input webpage url range (first, last); {url}/{i} for i in range')
    parser.add_argument('-ifmt', '--index_format', type=str
                        , default = '{}'
                        , help='index python format for webpage url; base_url/{fmt}')
    parser.add_argument('--timeout', type=int, default=10
                        , help='timeout for urllib')
    parser.add_argument('--time_sep', type=int, default=1
                        , help='time space between two downloads')
    parser.add_argument('--without_book_title', action='store_true'
                        , default = False
                        , help='not show book_title')
    parser.add_argument('--book_title_at', type=str
                        , default = None
                        , help='extended url for book_title; {base_url}{book_title_at}')

    parser.add_argument('--cache_fname', type=str
                        , required = True
                        , help='cache file name; to store middle extract data; Map url (title, txt)')
    parser.add_argument('--captcha_image_db_fname', type=str
                        , required = True
                        , help='cache file name; to store (correct or wrong) captcha string and its image bytes; Map "{i}_{captcha}" (correct, image_bytes)')


    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'
    if args.append:
        omode = 'at'

    if args.input is not None and args.url is not None:
        raise ValueError('input both file and url at same time')

    if args.url is not None:
        self = ExtractCTextOrg(
            cache_fname=args.cache_fname
            , captcha_image_db_fname=args.captcha_image_db_fname
            )
        if args.range is None:
            title, txt = self.cached_extract_ctext_org__url(args.url
                    , referrer=None
                    , verbose=args.verbose
                    , subcontents=False
                    , timeout=args.timeout
                    )
            may_book_title = None
            begin = 0
            result = (may_book_title, begin, [(title, txt)])
        elif 0:
            first, last = args.range
            begin, end = first, last+1
            rng = range(begin, end)

            base_url = args.url
            index_format = args.index_format
            it = self.unordered_iter_extract_ctext_org__url_rng(
                    base_url, rng, index_format
                    , verbose=args.verbose
                    , timeout=args.timeout
                    , time_sep=args.time_sep
                    )

            if args.without_book_title:
                may_book_title = None
            else:
                if args.book_title_at is None:
                    book_title_url = base_url
                else:
                    book_title_url = f'{base_url}{args.book_title_at}'

                book_title, _ = self.cached_extract_ctext_org__url(
                        book_title_url
                        , referrer=None
                        , verbose=args.verbose
                        , subcontents=False
                        , timeout=args.timeout
                        )
                may_book_title = book_title

            for _ in it:pass
            it = self.ordered_iter_extract_ctext_org__url_rng__cache_only(
                    base_url, rng, index_format
                    )
            begin = begin
            #result = (may_book_title, begin, list(it))
            result = (may_book_title, begin, iter(it))
        else:
            first, last = args.range
            if (first, last) == (0, 0):
                first, last = 1, None
                begin, end = None, None
            else:
                assert first >= 1
                begin, end = first-1, last
                #rng = range(begin, end)

            base_url = args.url
            if args.book_title_at is None:
                book_title_url = base_url
            else:
                book_title_url = f'{base_url}{args.book_title_at}'

            ((book_title, book_url), subtitle_url_pairs
            ) = self.cached_extract_ctext_org__url(
                    book_title_url
                    , referrer=None
                    , verbose=args.verbose
                    , subcontents=True
                    , timeout=args.timeout
                    )
            if args.without_book_title:
                may_book_title = None
            else:
                may_book_title = book_title

            subtitle_url_pairs = subtitle_url_pairs[begin:end]
            referrer_url_pairs = [(book_url, sub_url)
                        for subtitle, sub_url in subtitle_url_pairs]
            it = self.unordered_iter_extract_ctext_org__referrer_url_pairs(
                        referrer_url_pairs
                        , verbose=args.verbose
                        , timeout=args.timeout
                        , time_sep=args.time_sep
                        )



            for _ in it:pass

            def tmp__ordered_iter_extract_ctext_org__url_rng__cache_only():
                for (referrer, url), (subtitle, _) in zip(referrer_url_pairs, subtitle_url_pairs):
                    title, txt = self.cache[url]
                    #yield title, txt
                    yield subtitle, txt
            it = tmp__ordered_iter_extract_ctext_org__url_rng__cache_only()
            begin = first
            #result = (may_book_title, begin, list(it))
            result = (may_book_title, begin, iter(it))

    else:
        self = ExtractCTextOrgBase()
        may_ifname = args.input
        try:
            # open as text file
            with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
                title, txt = self.extract_ctext_org__text(fin
                    , verbose=args.verbose
                    , timeout=args.timeout
                    )
        except UnicodeError:
            assert may_ifname is not None
            ifname = may_ifname
            # open as binary file
            with open(ifname, 'rb') as fin:
                title, txt = self.extract_ctext_org__text(fin
                    , verbose=args.verbose
                    , timeout=args.timeout
                    )
        may_book_title = None
        begin = 0
        result = (may_book_title, begin, [(title, txt)])

    #result :: (may_book_title, begin, [(title, txt)])
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        def fprint(*args, **kwargs):
            print(*args, file=fout, **kwargs)

        may_book_title, begin, title_txt_pairs = result
        if not args.without_book_title:
            fprint(f'[book]:{may_book_title}')
        for i, (title, txt) in enumerate(title_txt_pairs, begin):
            fprint(f'[chapter{i}]:{title}')
            fprint(txt)

    if hasattr(self, 'close'):
        self.close()
    parser.exit(0)
    return 0


if __name__ == "__main__":
    #_t()
    #_test_file()
    pass
if __name__ == "__main__":
    main()


