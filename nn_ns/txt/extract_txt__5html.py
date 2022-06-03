r'''
see:
    seed.internet.html_ast

e ../../python3_src/nn_ns/txt/extract_txt__5html.py
py -m nn_ns.txt.extract_txt__5html   -i /sdcard/0my_files/tmp/wget_/CPython-guide/CPython-guide.html  -o /sdcard/0my_files/tmp/wget_/CPython-guide.txt -f

#'''



from bs4 import BeautifulSoup

def extract_txt(fout, fin, /):
    html_doc = fin
    soup = BeautifulSoup(html_doc, 'html.parser')
    def oprint(s):
        print(s, file=fout)

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


def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

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

    args = parser.parse_args(args)
    iencoding = args.iencoding
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:
        txt = fin.read()

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        extract_txt(fout, txt)
if __name__ == "__main__":
    main()


