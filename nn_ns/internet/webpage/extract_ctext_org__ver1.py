
'''

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
    <h2>《<a href="text.pl?node=277772&amp;if=gb" class="popup">西江月</a>》</h2>

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
##################### ?? will post {'message'=???, 'submit'='OK'} to "https://ctext.org/unban.pl"
##################### ?? will post {'message'=???} to "https://ctext.org/unban.pl"
##################### ?? will get "https://ctext.org/unban.pl?message=???"
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

from .fetch_webpage import open_webpage, fetch_webpage
from .download import download_file_from_url_ex
from seed.tiny import print_err
from seed.for_libs.for_tkinter.ask_input import ask_input

import requires
import PIL.Image, PIL.ImageTk
from bs4 import BeautifulSoup

import traceback
import io
import random
import time
import socket
if False:
    import tkinter
    # PIL.ImageTk.PhotoImage ==>> RuntimeError('Too early to create image',)
    # requires Tk() first
    #
    # but if Tk() then cause: _tkinter.TclError: image "pyimage1" doesn't exist
    #   since there should not be more than 1 Tk object!!!!
    ___donot_destroy_me = tkinter.Tk()
    del tkinter

#from pathlib import PurePosixPath as Path
#import os.path

TimeoutErrors = (TimeoutError, socket.timeout)
class CTextOrgConfirmError(Exception):
    def __init__(self, *args, action_url, text_field_name, **kwargs):
        self.action_url = action_url
        self.text_field_name = text_field_name
        super().__init__(*args, **kwargs)
    pass

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

def pred_ver1(soup):
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

def _pred_ver2(soup):
    #ver2: +<h2>
    return get_tag__lower(soup) == 'h2'
def pred_ver2(soup):
    return _pred_ver2(soup) or pred_ver1(soup)
def get_text_ver1(soup):
    return soup.get_text().strip()
def _get_text_ver2(soup):
    section_title = get_text_ver1(soup)
    return f'[h2]:{section_title}'
def get_text_ver2(soup):
    if _pred_ver2(soup):
        return _get_text_ver2(soup)
    return get_text_ver1(soup)

def fecth_captcha_image__PIL(*, referrer, timeout, **kwargs):
    i = random.randrange(100000)
    image_url = f'https://ctext.org/captcha.pl?random={i}'
    image_PIL = fecth_image__PIL(image_url
        , referrer=referrer, timeout=timeout, **kwargs)
    return image_PIL
def fecth_image__PIL(url, **kwargs):
    (content_type, content_data, url_info
    ) = download_file_from_url_ex(url, **kwargs)

    if False:
        print_err(f'captcha image content_type:{content_type!r}')
        print_err(type(content_data))
        print_err(content_data)

    assert content_type.lower().startswith('image')
    image_file = io.BytesIO(content_data)
    image_PIL = PIL.Image.open(image_file)
    #image_tk = PIL.ImageTk.PhotoImage(master=___donot_destroy_me, image=image_PIL)
        # RuntimeError('Too early to create image',)
        # see: ___donot_destroy_me
    return image_PIL

def ask_captcha(*, title, referrer, timeout, **kwargs):
    image_PIL = fecth_captcha_image__PIL(
        referrer=referrer, timeout=timeout, **kwargs)
    captcha = ask_input(title=title, prompt='', image_PIL=image_PIL)
    return captcha

def post_captcha(*, referrer, action_url, text_field_name, captcha
    , timeout, **kwargs):
    data = {text_field_name: captcha}
    r = requests.post(action_url, referrer=referrer
        , data=data, allow_redirects=True, timeout=timeout)
    r.content
    return
    ######### fail
    fetch_webpage(action_url, referrer=referrer
        , data=data, timeout=timeout, **kwargs)

def extract_ctext_org(html_file, *, verbose:bool):
    # html_file -> (title, txt)
    # html_file may be BytesIO/StringIO?
    verbose = bool(verbose)

    soup = BeautifulSoup(html_file, 'lxml')
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

    #ver1: ctexts = soup.find_all(attrs={'class': 'ctext'})
    #ls = [ctext.get_text().strip()
    #       for ctext in ctexts
    #       if not has_html_class(ctext, 'opt')
    #           and assert_html_class_single(ctext)
    #   ]
    #ver2: +<h2>
    pred = pred_ver2
    get_text = get_text_ver2
    ctexts = soup.find_all(pred)
    ls = [get_text(ctext) for ctext in ctexts]
    txt = '\n'.join(ls)

    if verbose: print_err('extract_ctext_org done!')
    return title, txt

def extract_ctext_org__url(url, *, verbose:bool, timeout, **kwargs):
    # url -> (title, txt)
    verbose = bool(verbose)
    try:
        if verbose: print_err(f'fetch webpage: {url!r}')
        page_bytes = fetch_webpage(url, timeout=timeout, **kwargs)

        if verbose: print_err(f'extracting webpage...: {url!r}')
        title, txt = extract_ctext_org(page_bytes, verbose=verbose)

        if verbose: print_err(f'extract webpage done: {url!r}')
        return title, txt
    except (CTextOrgConfirmError, *TimeoutErrors):
        if verbose: print_err(f'extract webpage timeout: {url!r}')
        raise
    except Exception as e:
        if verbose: print_err(f'extract webpage error: {url!r}')
        raise Exception(f'url={url!r}', e)
def iter_extract_ctext_org__url_rng(base_url, indices, index_format, *
    , verbose:bool, timeout, time_sep, **kwargs):
    # url -> begin -> end -> Iter (title, txt)
    #base_url = Path(base_url)
    verbose = bool(verbose)
    if verbose: print_err(f'fetch&extract webpages from: {base_url!r}')

    if base_url[-1:] == '/':
        base_url = base_url[:-1]
    referrer = base_url
    base_fmt = f'{base_url}/{index_format}'

    for i in indices:
        #str_i = str(i)
        #url = base_url / str_i; url = str(url)
        #url = os.path.join(base_url, str_i)
        #url = f'{base_url}/{i}'
        url = base_fmt.format(i)
        #print(url)
        while True:
            t = random.randrange(time_sep, 2*time_sep)
            if verbose: print_err(f'sleep {t}s before fetch&extract webpages from: {base_url!r}')
            time.sleep(t)
            try:
                title, txt = extract_ctext_org__url(url
                    , verbose=verbose, timeout=timeout, referrer=referrer
                    , **kwargs)
            except CTextOrgConfirmError as e:
                #input('ctext.org requires confirm')
                action_url = e.action_url
                text_field_name = e.text_field_name
                while True:
                    try:
                        captcha = ask_captcha(
                                title='ctext.org requires confirm'
                                ,referrer=url
                                ,timeout=max(10, timeout)
                                )
                        post_captcha(
                            action_url=action_url
                            , text_field_name=text_field_name
                            , referrer=url
                            , captcha=captcha, timeout=timeout)
                    except KeyboardInterrupt:
                        raise
                    except Exception as e2:
                        print_err(repr(e2))
                        if input('>>>'):
                            traceback.print_exc()
                            continue
                        else:
                            raise e2
                    else:
                        break
                continue
            except KeyboardInterrupt:
                raise
            except (Exception, OSError, *TimeoutErrors) as e:
                print_err(repr(e))
                continue
            break
        yield title, txt


def _test_file():
    fname = r'E:\download\novel_new\novel_20170808\小说\https _ctext.cn_fengshen-yanyi_1.htm'
    with open(fname, encoding='utf8') as fin:
        print(extract_ctext_org(fin, verbose=False))

def _test_url():
    url = r'https://ctext.org/fengshen-yanyi/1'
    print(extract_ctext_org__url(url, verbose=False))
def _test_url_rng():
    base_url = r'https://ctext.org/fengshen-yanyi'
    for title, txt in iter_extract_ctext_org__url_rng(base_url, range(1,100+1), verbose=False):
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


    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'
    if args.append:
        omode = 'at'

    if args.input is not None and args.url is not None:
        raise ValueError('input both file and url at same time')
    if args.url is not None:
        if args.range is None:
            title, txt = extract_ctext_org__url(args.url
                    , verbose=args.verbose
                    , timeout=args.timeout
                    )
            may_book_title = None
            begin = 0
            result = (may_book_title, begin, [(title, txt)])
        else:
            first, last = args.range
            begin, end = first, last+1
            rng = range(begin, end)

            base_url = args.url
            index_format = args.index_format
            it = iter_extract_ctext_org__url_rng(base_url, rng, index_format
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

                book_title, _ = extract_ctext_org__url(book_title_url
                        , verbose=args.verbose
                        , timeout=args.timeout
                        )
                may_book_title = book_title

            begin = begin
            #result = (may_book_title, begin, list(it))
            result = (may_book_title, begin, iter(it))
    else:
        may_ifname = args.input
        try:
            # open as text file
            with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
                title, txt = extract_ctext_org(fin
                    , verbose=args.verbose
                    , timeout=args.timeout
                    )
        except UnicodeError:
            assert may_ifname is not None
            ifname = may_ifname
            # open as binary file
            with open(ifname, 'rb') as fin:
                title, txt = extract_ctext_org(fin
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

    parser.exit(0)
    return 0


if __name__ == "__main__":
    #_t()
    pass
if __name__ == "__main__":
    main()


