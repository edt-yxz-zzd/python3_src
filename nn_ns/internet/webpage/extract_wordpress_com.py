

from bs4 import BeautifulSoup
from .fetch_webpage import open_webpage
import re

p_or_footer = re.compile('^p|footer$')
def get_tag(soup):
    return str(soup.name).lower()
def extract_wordpress_com(html_file):
    # html_file may be BytesIO/StringIO?
    soup = BeautifulSoup(html_file, 'lxml')
    article = soup.article
    if article is None: raise NotFoundError('the first article')
    content_div = article.find('div', attrs={'class': "entry-content"})
    if content_div is None: raise NotFoundError('the first div(the content div)')
    #return content_div.get_text()
    #############

    # <br /> = '\n'*1
    # <p></p> = '\n'*2
    i = -1
    for i, c in enumerate(content_div.children):
        tag = get_tag(c)
        if tag == 'div': break
    else:
        i += 1
    #for node in content_div.contents[i:]: node.extract() # remove from its parent
    p = soup.new_tag('p')
    for _ in map(p.append, content_div.contents[:i]):pass
    txt = p.get_text()
    # &nbsp; indicates a non-breaking space character
    # U+A0 \xa0
    # which may occur in txt, but not in gbk
    txt = txt.replace('\xA0', ' ')
    return txt


    ls = []
    if True:
        for c in content_div.children:
            tag = get_tag(c)
            print(tag)
            if tag == 'none': print(type(c))
            if tag == 'footer': break
            ls.append(c)
    else:
        # fail when <pre> occur
        for p in content_div.find_all('p pre'.split()):
            ls.append(p)
    txt = '\n\n'.join(p.get_text() for p in ls)
    return txt



def main(argv=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout


    parser = argparse.ArgumentParser(
        description='extract first content_div of article on wordpress.com'
        )
    parser.add_argument('-e', '--encoding', type=str, default='utf8', help='input/output file encoding')
    parser.add_argument('-i', '--input', type=str, default = None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default = None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-url', '--url', type=str, default = None
                        , help='input webpage url')


    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    if args.input is not None and args.url is not None:
        raise ValueError('input both file and url at same time')
    if args.url is not None:
        with open_webpage(args.url) as fin:
            content_div = extract_wordpress_com(fin)
    else:
        may_ifname = args.input
        try:
            # open as text file
            with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
                content_div = extract_wordpress_com(fin)
        except UnicodeError:
            assert may_ifname is not None
            ifname = may_ifname
            # open as binary file
            with open(ifname, 'rb') as fin:
                content_div = extract_wordpress_com(fin)

    if 0:
        print(len(content_div))
        print(repr(content_div[5216:]))
        for i in range(len(content_div)):
            if ord(content_div[i]) > 0x7f:
                print(i)
                print(repr(content_div[i:]))
                break
        return
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        fout.write(content_div)

    parser.exit(0)
    return 0

'''
https://txt20180801.wordpress.com/2018/08/03/another-v3/
https://txt20180801.wordpress.com/2018/08/01/email-blog-psw/
https://bug20180101jieshenrenchong.wordpress.com/

'''

if __name__ == "__main__":
    main()

