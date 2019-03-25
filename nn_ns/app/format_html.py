

from bs4 import BeautifulSoup
import lxml
import re

rex_indent_spaces = re.compile(r'(?m)^ +')
def replace_indent_spaces(indent_width, txt):
    assert indent_width >= 0
    if indent_width == 1:
        return txt

    def repl(m):
        return m.group(0) * indent_width
        begin = m.start()
        end = m.end()
        L = end - begin
        return ' '*(indent_width*L)
    return rex_indent_spaces.sub(repl, txt)
assert replace_indent_spaces(2, ' a\n  b') == '  a\n    b'

def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='format html/xml by well indent'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-iw', '--indent_width', type=int
                        , default = 1
                        , help='the number of indent spaces for children')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        soup = BeautifulSoup(fin, 'lxml')

    txt = soup.prettify()
    txt = replace_indent_spaces(args.indent_width, txt)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        fout.write(txt)

if __name__ == "__main__":
    main()


