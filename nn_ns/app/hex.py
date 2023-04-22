r'''
deprecated by new version py_eval:
    #py -m nn_ns.app.hex -i "$@"
    py -m nn_ns.app.py_eval --postprocess 'hex' -i "$@"

also:
    printf $'%x\n' $[0x8000-0x80]
    7f80
######################
py -c 'print(hex(333))'
0x14d

######################
py -m nn_ns.app.py_eval -i 'hex(333)' '3 + 7' '2 ** 3' '2 ^ 3'
0x14d
10
8
1

######################
py -m nn_ns.app.hex -i '333' '3 + 7' '2 ** 3' '2 ^ 3'
0x14d
0xa
0x8
0x1


#'''

from seed.helper.safe_eval import safe_eval

assert '0x14d' == hex(333)

def eval_then_show(expr, /, *, fout):
    print(hex(safe_eval(expr)), file=fout)

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='python eval then hex then print'
        , epilog=r'''
also:
    printf $'%x\n' $[0x8000-0x80]
    7f80
        '''#'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, nargs='*', default=[]
                        , help='input python expression')
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

    #may_ifname = args.input
    #with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:

    exprs = args.input
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        for expr in exprs:
            eval_then_show(expr, fout=fout)

if __name__ == "__main__":
    main()



