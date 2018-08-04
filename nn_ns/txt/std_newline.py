

from io import StringIO
def std_newline(bin_fout, txt_fin, oencoding):
    txt = txt_fin.read() # newline to '\n'
    bs = txt.encode(oencoding) # '\n' to '\n' not newline
    bin_fout.write(bs)


def main(argv=None):
    import argparse, sys

    parser = argparse.ArgumentParser(description=r'remove "\r" from newline')
    add_argument = parser.add_argument

    add_argument('input_fname', type=str
        , help='the input file name')
    add_argument('output_fname', type=str
        , help='the output file')
    add_argument('-ie', '--input_encoding', type=str
        , default = 'utf8'
        , help='the encoding of input html files')
    add_argument('-oe', '--output_encoding', type=str
        , default = 'utf8'
        , help='the encoding of output file')
    add_argument('-f', '--force', action='store_true'
        , default=False
        , help='overwrite output file if it exists')

    args = parser.parse_args(argv)
    with open(args.input_fname, 'r', encoding=args.input_encoding) as txt_fin\
        , open(args.output_fname, 'xb' if not args.force else 'wb') as bin_fout:
        std_newline(bin_fout, txt_fin, args.output_encoding)
    #parser.exit()
    return

if __name__ == '__main__':
    main()
