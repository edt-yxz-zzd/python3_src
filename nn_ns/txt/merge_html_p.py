


r'''
<p></p>
<p>abc</p>
<p>defg</p>
<p></p>
==>> "\nabcdefg\n"

'''

import re
to_be_replace_re = re.compile(r'(?m)</p>\s*<p>(?!\s*</p>)')
repl = r'' # delete
def merge_html_p(pseudo_htm):
    return to_be_replace_re.sub(repl, pseudo_htm)













###################

def main(argv=None):
    import argparse, sys
    from seed.io.may_open import may_open_stdout, may_open_stdin
    class Globals:
        output_file_encoding = 'utf8'
        input_file_encoding = 'utf8'



    ###################
    parser = argparse.ArgumentParser(description='merge html <p>'
        , epilog='''
    <p></p> is the true seperator
    "<p>abc</p> <p>def</p>" ==>> "<p>abcdef</p>"

''')
    add_argument = parser.add_argument


    add_argument('-i', '--input_file', type=str
        , default=None
        , help='the input file')
    add_argument('-ie', '--input_encoding', type=str
        , default = Globals.input_file_encoding
        , help='the encoding of input file')
    add_argument('-o', '--output_file', type=str
        , default=None
        , help='the output file')
    add_argument('-oe', '--output_encoding', type=str
        , default = Globals.output_file_encoding
        , help='the encoding of output file')

    args = parser.parse_args(argv)
    with may_open_stdin(args.input_file, 'rt'
            , encoding=args.input_encoding) as fin:
        pseudo_htm = fin.read()
    txt = merge_html_p(pseudo_htm)
    if args.output_file is not None:
        # try output_encoding
        txt.encode(args.output_encoding)

    with may_open_stdout(args.output_file, 'xt'
            , encoding=args.output_encoding) as fout:
        fout.write(txt)
    #parser.exit(0)
    return 0

    ##########
    with may_open_stdout(args.output_file, 'xt'
            , encoding=args.output_encoding) as fout\
        , may_open_stdin(args.input_file, 'rt'
            , encoding=args.input_encoding) as fin:
        extract_fb_opf_items(fout, fin)

    #parser.exit(0)
    return 0


if __name__ == '__main__':
    main()



