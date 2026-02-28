#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/count_each_chars.py

nn_ns.app.count_each_chars
py -m nn_ns.app.debug_cmd   nn_ns.app.count_each_chars -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.count_each_chars:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



[[
echo 'abbbcc' | count_each_chars
    <==>:
echo 'abbbcc' | py -m nn_ns.app.count_each_chars
    =>:
    ,'\n':1
    ,'a':1
    ,'b':3
    ,'c':2
]]
[[
count_each_chars -ie ascii -i /sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt
    ,'\n':7320000
    ,'0':672651
    ,'1':5349930
    ,'2':1297218
    ,'3':201
]]

py_adhoc_call   nn_ns.app.count_each_chars   @f
from nn_ns.app.count_each_chars import *
]]]'''#'''
__all__ = r'''
count_each_chars5file_
count_each_chars5path_
main
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

def count_each_chars5file_(ifile, /):
    from collections import Counter
    d = Counter(ch for line in ifile for ch in line)
    return dict(d)
def count_each_chars5path_(ipath, /, *, encoding):
    with open(ipath, 'rt', encoding=encoding) as ifile:
        return count_each_chars5file_(ifile)

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='count_each_chars'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
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
    with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:
        d = count_each_chars5file_(fin)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        #from seed.helper.stable_repr import stable_repr
        for ch, count in sorted(d.items()):
            print(f',{ch!r}:{count}', file=fout)

if __name__ == "__main__":
    main()


__all__
from nn_ns.app.count_each_chars import *
