

r'''
input unicode points
append characters to file

'''
def word2cp__default_hex(word):
    # hex | U+hex
    return word2cp__default(word, hex2int)
def word2cp__default_dec(word):
    # dec | U+hex
    return word2cp__default(word, dec2int)
def word2cp__default(word, to_int):
    if word.startswith('U+'):
        word = word[2:]
        return hex2int(word)
    else:
        return to_int(word)
def hex2int(hex):
    return int(hex, base=16)
def dec2int(dec):
    return int(dec, base=10)
def main(argv=None):
    import argparse, sys
    from seed.io.as_file import as_file, curry_file
    from seed.for_libs.parent_argparser import \
        input_file_parent_argparser, input_encoding_parent_argparser \
        , output_file_parent_argparser, output_encoding_parent_argparser \
        , output_open_mode_parent_argparser, open_mode_to_pyopen_arg

    parents = [input_file_parent_argparser, input_encoding_parent_argparser
            , output_file_parent_argparser, output_encoding_parent_argparser
            , output_open_mode_parent_argparser
            ]
    obinary = False
    ibinary = False

    parser = argparse.ArgumentParser(parents=parents
        , description = 'code point to character')
    parser.add_argument('--dec', action='store_false', dest='hex')
    parser.add_argument('--hex', action='store_true', dest='hex')
    parser.set_defaults(hex=True)



    args = parser.parse_args(argv)
    word2cp = word2cp__default_hex if args.hex else word2cp__default_dec
    def word2char(word):
        return chr(word2cp(word.upper()))


    omode = open_mode_to_pyopen_arg(args.output_open_mode, binary=obinary)
    imode = 'rb' if ibinary else 'r'
    def do(fin):
        def do(fout):
            for line in fin:
                s = ''.join(map(word2char, line.split()))
                fout.write(s)
                fout.write('\n')
        return do

    input_file = args.input_file
    output_file = args.output_file
    iencoding = args.input_encoding
    oencoding = args.output_encoding

    fi = curry_file(input_file, imode, encoding=iencoding)
    fo = curry_file(output_file, omode, encoding=oencoding)
    fo(fi(do))
    parser.exit(0)


    def read_fin(fin):
        def write_fout(fout):
            for line in fin:
                s = ''.join(map(word2char, line.split()))
                fout.write(s)
                fout.write('\n')
        as_file(write_fout, args.output_file, 'x', encoding=args.output_encoding)

    as_file(read_fin, args.input_file, 'r', encoding=args.input_encoding)
    parser.exit(0)

if __name__ == '__main__':
    main()


