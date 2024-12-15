#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/lineno.py
e ../../python3_src/bash_script/app/lineno

[[
seperated from:『py_adhoc_call { +lineno }』

源起:
    view script/搜索冫乘积加一型素数乊上界.py
        有序结果冫八七九一牜无重复十进制位数字

usage:
cat /sdcard/0my_files/tmp/0tmp | py -m nn_ns.app.lineno
cat /sdcard/0my_files/tmp/0tmp | lineno
lineno < /sdcard/0my_files/tmp/0tmp

===
发现cat,grep,awk/gawk也有类似功能:
===
echo -e -n 'abc\n123\n...\n' | cat -n
     1  abc
     2  123
     3  ...
echo -e -n 'abc\n123\n...\n' | lineno
1:abc
2:123
3:...

===
echo $'aaa\n777\n...' | gawk 'BEGIN { OFS = ":" } { print FNR, $0 }'
1:aaa
2:777
3:...

===
echo $'aaa\n777\n...' | grep '' -n
1:aaa
2:777
3:...

===

]]


py -m nn_ns.app.lineno
py -m nn_ns.app.debug_cmd   nn_ns.app.lineno -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.lineno:__doc__ -ht # -ff -df


py_adhoc_call   nn_ns.app.lineno   @f
from nn_ns.app.lineno import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    #from seed.io.savefile.unbuffered_growonly_dict_in_file import tabular_cached_calc
    from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
    from seed.io.may_open import open4w, open4w_err, open4r

    parser = argparse.ArgumentParser(
        description='label lineno to each line'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-fmt', '--format4lineno', type=str, default=(default_format4lineno:='{0}:')
            , help=f'format<lineno>: [default:={default_format4lineno!r}]')
    parser.add_argument('-s', '--lineno_offset', type=int, default=1
                        , help='lineno for first line: [default:=1]')
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

    may_ifname = args.input
    #with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:
    #with open_under_pkg_('seed.pkg_tools', 'xxx.dat', xencoding='u8' or None) as fin:
    #dat = read_under_pkg_('seed.pkg_tools', 'xxx.dat', xencoding='u8' or None)

    may_ofname = args.output
    #with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
    lineno_offset = args.lineno_offset
    format4lineno = args.format4lineno
    with open4r(may_ifname, xencoding=iencoding) as fin:
        with open4w(may_ofname, force=force, xencoding=oencoding) as fout:
          for lineno, line in enumerate(fin, lineno_offset):
              #print(lineno, ':', line, sep='', end='')
              print(format4lineno.format(lineno), line, sep='', end='')

if __name__ == "__main__":
    main()


__all__
from nn_ns.app.lineno import *
