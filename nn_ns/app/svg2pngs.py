
# diff svg2png.py: batch handle
from cairosvg import svg2png

def main(argv=None):
    import argparse, glob, os.path
    #from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description="convert svg files to png files"
        )
    parser.add_argument('input_path_patterns', type=str
                        , nargs = '*'
                        , default = []
                        #bug: , action='append'
                        #   will lead to [[pattern]]
                        , help='input file paths (glob pattern)')
    parser.add_argument('-o', '--output_dir', type=str
                        , default = '.'
                        , help='output dir')
    parser.add_argument('-pre', '--output_prefex', type=str
                        , default = ''
                        , help='output file basename prefix')
    parser.add_argument('-suf', '--output_suffex', type=str
                        , default = ''
                        , help='output file basename suffix (file suffix will be ".png")')
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


    def iter_ifnames(patterns):
        for ifname_pattern in patterns:
            yield from glob.iglob(ifname_pattern, recursive=True)

    input_path_patterns = args.input_path_patterns
    for ifname in iter_ifnames(input_path_patterns):
        with open(ifname, 'rt', encoding=encoding) as fin:
            svg_content = fin.read()

        output_dir = args.output_dir
        output_prefex = args.output_prefex
        output_suffex = args.output_suffex
        ibasename, _svg = os.path.splitext(os.path.basename(ifname))
        obasename_ext = f'{output_prefex}{ibasename}{output_suffex}.png'
        ofname = os.path.join(output_dir, obasename_ext)
        with open(ofname, omode, encoding=None) as fout:
            svg2png(svg_content, write_to=fout, **kwargs)

if __name__ == "__main__":
    main()



