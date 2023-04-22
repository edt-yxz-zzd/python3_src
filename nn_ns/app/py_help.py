#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/py_help.py
    view ../../python3_src/seed/for_libs/for_builtins/py_help.py

help(math)
    交互对话式，太长就难以复制
    py -c 'import math;help(math)' | cat
      #输出到文件




nn_ns.app.py_help
xxx py -m nn_ns.app.py_help  -qnm4mdl nn_ns.app.py_help -qnm4obj py_help_
py -m nn_ns.app.py_help  nn_ns.app.py_help:py_help_
py_help  nn_ns.app.py_help:py_help_

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from warnings import warn
from seed.for_libs.for_builtins.py_help import py_help_, py_help
    # 'py_help(may_qname4module, may_qname4obj) -> help_str4obj'

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    #from seed.io.savefile.unbuffered_growonly_dict_in_file import tabular_cached_calc

    parser = argparse.ArgumentParser(
        description='py.help(xxx.yyy.CCC.fff)'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    r'''
    parser.add_argument('-qnm4mdl', '--smay_qname4module', type=str, default=None
                        , help='qual_name to module for target obj; default="builtins"')
    parser.add_argument('-qnm4obj', '--smay_qname4obj', type=str, default=None
                        , help='qual_name to target obj; default=module_obj')
    '''#'''
    parser.add_argument('smay_qname4module_and_obj', type=str, default=''
                        , help='qual_name to module and target obj; fmt=regex"({qnm4mdl}?(:{qnm4obj}?)?)?" e.g. "xxx.yyy:CCC.MMM.fff"; default<qnm4mdl>="builtins"; default<target_obj>=module_obj')

    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'

    #may_smay_qname4module = args.smay_qname4module
    #may_smay_qname4obj = args.smay_qname4obj
    #help_str4obj = py_help(may_smay_qname4module, may_smay_qname4obj)

    if '@' in args.smay_qname4module_and_obj:
        #Deprecated:
        warn('nn_ns.app.py_help:Deprecated:『"xxx.yyy@CCC.MMM.fff"』 --> 『"xxx.yyy:CCC.MMM.fff"』')
        smay_qname4module, _, smay_qname4obj = args.smay_qname4module_and_obj.partition('@')
    else:
        smay_qname4module, _, smay_qname4obj = args.smay_qname4module_and_obj.partition(':')

    help_str4obj = py_help(smay_qname4module, smay_qname4obj)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        print(help_str4obj, end='', file=fout)
    return
if __name__ == "__main__":
    main()

