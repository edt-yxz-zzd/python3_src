#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/append_eof.py
see:
    view ../../python3_src/nn_ns/app/append_eof.py
    view ../../python3_src/seed/io/continue_io.py
    view ../../python3_src/seed/io/continue_io__folder.py

nn_ns.app.append_eof
py -m nn_ns.app.debug_cmd   nn_ns.app.append_eof -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.append_eof:__doc__ -ht # -ff -df

[[
源起:
py_adhoc_call   script.搜索冫某进制表达数乊多种进制解 读皆为素数   ,str.搜索冫某进制表达数乊多种进制解读皆为素数扌 ="[17,19,23,29,31]" =16     ="0x00*16**6"  ="0x01*16**6" --imay_radix4beyond=-1 +int_vs_str +str_with_int +to_swap_fmt4str_with_int | lineno  | append_eof  >  /sdcard/0my_files/tmp/out多种进制解读皆为素数/16_56_00tmp
一共分割为256行命令(5分钟以内/命令)
append_eof 用于确认命令正常结束
]]


echo xxx | append_eof
xxx
<eof>

echo $'xxx\nyyy\nzzz' | append_eof --prolog $'666\n' --epilog $'999\n'
666
xxx
yyy
zzz
999
echo $'xxx\nyyy\nzzz' | append_eof --prolog $'666' --epilog $'999' | append_eof --prolog $'666' --epilog $'999' | append_eof
666666xxx
yyy
zzz
999999<eof>
    # !! "echo" append '\n'

help echo
    -n        do not append a newline
    -e        enable interpretation of the following backslash escapes
    -E        explicitly suppress interpretation of backslash escapes

echo -e -n 'xxx\nyyy\nzzz' | append_eof --prolog $'666' --epilog $'999' | append_eof --prolog $'666' --epilog $'999' | append_eof
666666xxx
yyy
zzz999999<eof>


py_adhoc_call   nn_ns.app.append_eof   @f
from nn_ns.app.append_eof import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='append lines to file'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--prolog', type=str, default=''
                        , help="prolog (default:=$'')")
    parser.add_argument('--epilog', type=str, default='<eof>\n'
                        , help="epilog (default:=$'<eof>\n')")
    parser.add_argument('-io', '--iopath', type=str, default=None
                        , help='input&output file path')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    force = args.force
    omode = 'wt' if args.force else 'xt'
    iencoding = args.iencoding
    oencoding = args.oencoding
    iencoding = 'utf8' if not iencoding else iencoding
    oencoding = 'utf8' if not oencoding else oencoding

    may_iofname = args.iopath
    if not may_iofname is None: raise NotImplementedError

    may_ifname = args.input
    may_ofname = args.output
    if may_ofname is may_ifname is not None: raise NotImplementedError
    prolog = args.prolog
    epilog = args.epilog

    with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin, may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        fout.write(prolog)
        for line in fin:
            fout.write(line)
        fout.write(epilog)


if __name__ == "__main__":
    main()


__all__
from nn_ns.app.append_eof import *
