
r"""

py -m nn_ns.app.hex2char 4E00 5143 65E6 541E 528D 9582 98A8 885E
一u4E00h,元u5143h,旦u65E6h,吞u541Eh,劍u528Dh,閂u9582h,風u98A8h,衞u885Eh

echo 2007 3007 | py -m nn_ns.app.hex2char 4E5B 86CB -si
 u2007h,〇u3007h
乛u4E5Bh,蛋u86CBh

#"""

def hex2char(hexdigits):
    u = int(hexdigits, base=16)
    c = chr(u)
    return c


def hex2char_ex(hexdigits):
    c = hex2char(hexdigits)
    return f"{c}u{ord(c):X}h"


def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description="hex to char"
        , epilog=__doc__
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('hex', type=str, default=[], nargs='*'
                        , help='input hexdigits')
    parser.add_argument('-i', '--input', type=str, default=[], nargs="*"
                        , help='input file')
    parser.add_argument('-si', '--stdin', action='store_true'
                        , default = False
                        , help='using stdin')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    def h(hexdigits_ls):
        return ','.join(map(hex2char_ex, hexdigits_ls))
    def f(hexdigits_ls, fout):
        s = h(hexdigits_ls)
        print(s, file=fout)
    def fs(may_ifnames, fout):
        for may_ifname in may_ifnames:
            with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
                for line in fin:
                    hexdigits_ls = line.split()
                    try:
                        f(hexdigits_ls, fout)
                    except Exception:
                        print(line, file=fout, end='')
                        continue


    h(args.hex) #check

    ifnames = args.input
    if args.stdin:
        may_ifnames = [None, *ifnames]
    else:
        may_ifnames = [*ifnames]
    del ifnames

    may_ifnames
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        fs(may_ifnames, fout)
        hexdigits_ls = args.hex
        if hexdigits_ls:
            f(hexdigits_ls, fout)

if __name__ == "__main__":
    main()



