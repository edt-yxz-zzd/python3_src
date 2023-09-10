r'''
see:
    seed.internet.html_ast

e ../../python3_src/nn_ns/txt/extract_txt__5html.py
py -m nn_ns.txt.extract_txt__5html   -i /sdcard/0my_files/tmp/wget_/CPython-guide/CPython-guide.html  -o /sdcard/0my_files/tmp/wget_/CPython-guide.txt -f

html2text -h

view ../../python3_src/seed/internet/html_ast.py

#'''



from bs4 import BeautifulSoup
from bs4 import BeautifulSoup, Tag, NavigableString, Doctype, Comment, Stylesheet, Script
from seed.internet.html_ast import HtmlAstOps, MarkupLang


ops = HtmlAstOps()
def extract_txt_(fout, fin, /, *, ver):
    html_doc = fin
    #soup = BeautifulSoup(html_doc, 'html.parser')
    soup = obj = ops.建(html_doc, markup_lang=MarkupLang.HTML)
    def oprint(s):
        print(s, file=fout)
    nm = f'extract_txt__ver_{ver!s}'
    extract_txt__ver_XXX = globals()[nm]
    extract_txt__ver_XXX(oprint, soup)

_ok_types = (Tag, BeautifulSoup)
_ignore_types = (Doctype, Comment, Stylesheet, Script)
def iter_extract_tags(soup, /):
    for obj in ops.枚举后代(soup):
        if type(obj) in _ok_types:
            yield ops.得件名(obj)
def extract_txt__ver_list_tags(oprint, soup, /):
    tags = iter_extract_tags(soup)
    tags = sorted({*tags})
    for tag in tags:
        oprint(tag)
def extract_txt__ver_get_text(oprint, soup, /):
    if 0:
        oprint('\n'*3)
        oprint('='*16)
        oprint(soup.title.string)
        #oprint(soup.h3)
        oprint('='*16)
    # for e in soup.find_all('p'): oprint(e.string)
    if 0:
        body = soup.body
        body.name = 'div'
        oprint(body)
    else:
        s = soup.get_text()
        oprint(s)

    if 0:
        oprint('\n'*3)



def extract_txt__ver_www_zhihu_com(oprint, soup, /):
    txt = ''.join(iter_extract_txt__ver_www_zhihu_com(soup))
    oprint(txt)
def iter_extract_txt__ver_www_zhihu_com(soup, /):
    unknowns = set()
    for obj in ops.枚举后代(soup):
        T = type(obj)
        if T in _ok_types:
            nm = ops.得件名(obj).lower()
            _nm_ = f' {nm!s} '
            if _nm_ in '   p h1 h2 h3 blockquote div title button a ':
                if nm == 'a':
                    href = obj['href']
                    yield '\n'
                    yield f'href="{href!s}"'
                    yield '\n'
                elif nm == 'p':
                    yield '\n\n'
                else:
                    yield '\n'
        elif T is NavigableString:
            yield str(obj)
        elif T in _ignore_types:
            pass
        else:
            #assert T is Doctype, T
            unknowns.add(T)
            pass
    if unknowns:
        print(unknowns)
        assert 0, unknowns


















def __():
    prefix = 'extract_txt__ver_'
    choices = set()
    for nm, f in globals().items():
        if type(nm) is str and nm.startswith(prefix) and callable(f):
            choices.add(nm[len(prefix):])
    choices = tuple(sorted(choices))
    return choices
choices = __()



def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    kkk = False

    parser = argparse.ArgumentParser(
        description='extract text from html'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    if kkk:
        parser.add_argument('-ls', '--list_all_tags', action='store_true'
                        , default = False
                        , help='list all tags in input html')
        parser.add_argument('-ln', '--tag8newline', type=str, action='append'
                        , default = []
                        , help='which tags convert to newline, eg. br,p,...')
        parser.add_argument('-txt', '--tag2txt', type=str, action='append'
                        , default = []
                        , help='which tags convert to text, eg. span,...')
    parser.add_argument('-ver', '--algo_version', choices=choices, type=str, default='get_text'
                        , help='choose diff extract method')


    args = parser.parse_args(args)
    iencoding = args.iencoding
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'
    if kkk:
        list_all_tags = args.list_all_tags
    ver = args.algo_version

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:
        txt = fin.read()

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        #if list_all_tags:
        #    extract_tags_(fout, txt)
        #else:
        extract_txt_(fout, txt, ver=ver)
if __name__ == "__main__":
    main()


