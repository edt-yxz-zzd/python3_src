

r'''
translate lower characters in input to upper characters in output

lower cmd:
    vs "tr A-Z a-z <ifname"
    vs "tr [:upper:] [:lower:] <ifname"

source:
    http://libgen.io/book/index.php?md5=1C5C744850AF249F0A5BE6E956D84FB2
    http://libgen.io/libgen/repository_torrent/r_1467000.torrent
    md5 value in url is upper case.
    but lower case of md5 value was used as 'info::files::path' in .torrent file
    I want to translate upper case to lower case:
        input file:
            LINE1
            LINE2
        1) output file:
            # 2 columes
            LINE1<sep>line1
            LINE2<sep>line2
        2) output file:
            line1
            line2
'''

__all__ = '''
    lower_file
    '''.split()

from seed.text.split_newlines import split_newlines
from seed.io.may_open import may_open_stdin, may_open_stdout


def lower_file(fout, fin, *, upper=False, sep=None):
    r'''translate lower characters in input to upper characters in output

assume fout/fin are openned with (newline="")

upper :: bool
    if upper:
        lower2upper
    else:
        upper2lower

sep :: None | str
    if None:
        #translate
        output file:
            line1
            line2
    else:
        #2 columes
        output file:
            LINE1<sep>line1
            LINE2<sep>line2


example:
    >>> from io import StringIO
    >>> string = '\n\r\nabc\n123\r\nXYZ'
    >>> this = lower_file

    >>> fout = StringIO(newline='')
    >>> fin = StringIO(string, newline='')
    >>> this(fout, fin)
    >>> fout.getvalue()
    '\n\r\nabc\n123\r\nxyz'

    >>> fout = StringIO(newline='')
    >>> fin = StringIO(string, newline='')
    >>> this(fout, fin, upper=True)
    >>> fout.getvalue()
    '\n\r\nABC\n123\r\nXYZ'

    >>> fout = StringIO(newline='')
    >>> fin = StringIO(string, newline='')
    >>> this(fout, fin, upper=True, sep=':')
    >>> fout.getvalue()
    ':\n:\r\nabc:ABC\n123:123\r\nXYZ:XYZ'

    >>> fout = StringIO(newline='')
    >>> fin = StringIO(string, newline='')
    >>> this(fout, fin, sep='%')
    >>> fout.getvalue()
    '%\n%\r\nabc%abc\n123%123\r\nXYZ%xyz'

'''
    translate = str.upper if upper else str.lower
    write = fout.write
    if sep is None:
        #translate
        while True:
            s = fin.readline(1024)
            if not s: break
            t = translate(s)
            write(t)
    else:
        #2 columes
        for line in fin:
            content, newlines = split_newlines(line)
            t = translate(content)
            #line = f'{content}{sep}{t}{newlines}'
            #write(line)
            write(content)
            write(sep)
            write(t)
            write(newlines)
    return



if __name__ == "__main__":
    import doctest
    doctest.testmod()

def main(argv = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='translate characters from lower to upper case')
    parser.add_argument('-i', '--input', type=str
                        , default=None
                        , help='input file name')
    parser.add_argument('-o', '--output', type=str
                        , default=None
                        , help='output file name')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='encoding of input/output file')
    parser.add_argument('-f', '--force', action='store_true'
                        , default=False
                        , help='open mode for output file')

    parser.add_argument('-s', '--sep', type=str
                        , default=None
                        , help='seperator string of output file which has 2 columes')
    parser.add_argument('-u', '--upper', action='store_true'
                        , default=False
                        , help='lower2upper instead of upper2lower')

    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    may_ofname = args.output
    with may_open_stdin(may_ifname, 'rt', encoding=encoding, newline='')\
        as fin\
        , may_open_stdout(may_ofname, omode, encoding=encoding, newline='')\
        as fout:
        lower_file(fout, fin, upper=args.upper, sep=args.sep)

    parser.exit(0)
    return 0

if __name__ == "__main__":
    main()


