
from glob import iglob
from seed.io.may_open import may_open_stdout


class Globals:
    output_file_encoding = 'utf8'

def main(argv=None):
    '''
'''
    import argparse, sys

    parser = argparse.ArgumentParser(description='list paths')
    add_argument = parser.add_argument

    add_argument('glob_patterns', type=str
        , nargs='+'
        , metavar='GLOB_PATTERN'
        , help='glob_patterns for list paths')
    add_argument('-r', '--recursive', action='store_true'
        , default=False
        , help='recursive search')
    add_argument('-o', '--output_file', type=str
        , default=None
        , help='the output file')
    add_argument('-oe', '--output_encoding', type=str
        , default = Globals.output_file_encoding
        , help='the encoding of output file')

    args = parser.parse_args(argv)
    with may_open_stdout(args.output_file, 'xt'
            , encoding=args.output_encoding) as fout:
        for glob_pattern in args.glob_patterns:
            for path in iglob(glob_pattern, recursive=args.recursive):
                print(path, file=fout)

    #parser.exit()
    return


if __name__ == '__main__':
    main()


