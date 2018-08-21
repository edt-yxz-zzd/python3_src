

from cairosvg import svg2png

def main(argv=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description="convert svg to png"
        , epilog="<==> cairosvg -f png <input> -o <output>"
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default = None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default = None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-D', '--dpi', type=float
                        , default = None
                        , help='dpi of output png')
    parser.add_argument('-S', '--scale', type=float
                        , default = None
                        , help='scale of output png')
    parser.add_argument('-W', '--parent_width', type=float
                        , default = None
                        , help='parent_width of output png')
    parser.add_argument('-H', '--parent_height', type=float
                        , default = None
                        , help='parent_height of output png')

    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wb' if args.force else 'xb'

    kwargs = dict(
        dpi = args.dpi
        ,scale = args.scale
        ,parent_width = args.parent_width
        ,parent_height = args.parent_height
        )
    kwargs = {k:v for k,v in kwargs.items() if v is not None}

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        svg_content = fin.read()

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=None) as fout:
        svg2png(svg_content, write_to=fout, **kwargs)

if __name__ == "__main__":
    main()



