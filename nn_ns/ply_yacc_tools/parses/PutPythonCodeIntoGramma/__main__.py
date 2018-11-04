

__all__ = '''
    main
    '''.split()


from .example import __doc__ as example_doc
from .PLY_YACC_Helper_YaccRules import parse_ex
__doc__ = example_doc

def main(argv=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='parse pythoncoded_rules_in_str'
        , epilog=example_doc
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

    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        pythoncoded_rules_in_str = fin.read()

    python_code_str_ex = parse_ex(pythoncoded_rules_in_str
        , name2count = None
        , the_input_parameter_name = 'p'
        , with_class_keyword = False
        )
    head_str, tail_str, name2count = python_code_str_ex

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        fout.write(head_str)
        fout.write(tail_str)

if __name__ == "__main__":
    main()


