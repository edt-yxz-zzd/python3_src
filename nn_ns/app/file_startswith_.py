#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/file_startswith_.py

py -m nn_ns.app.file_startswith_
py -m nn_ns.app.debug_cmd   nn_ns.app.file_startswith_ -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.file_startswith_:__doc__ -ht # -ff -df

[[
]]

py -m nn_ns.app.file_startswith_  /sdcard/0my_files/tmp/0tmp /sdcard/0my_files/tmp/0tmp2
file_startswith_  /sdcard/0my_files/tmp/0tmp script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺深一.out.txt
e ../../python3_src/bash_script/app/file_startswith_


py_adhoc_call   nn_ns.app.file_startswith_   @f
from nn_ns.app.file_startswith_ import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

BLOCK_SIZE = 256
def main(args=None, /):
    import argparse
    import os.path
    from os.path import samefile
    from os import SEEK_END
    parser = argparse.ArgumentParser(
        description='is first file a prefix bytes of second file'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('fpath8prefix', type=str, default=None
                        , help='prefix file path')
    parser.add_argument('fpath8whole', type=str, default=None
                        , help='whole file path')
    parser.add_argument('-at', '--offset', type=int
                        , default=0
                        , help='offset for prefix file')

    args = parser.parse_args(args)

    path1 = args.fpath8prefix
    path2 = args.fpath8whole
    offset = args.offset
    check_int_ge(0, offset)
    def fail():
        print('diff')
    def succ():
        print('same')
    if samefile(path1, path2):
        return succ() if offset==0 else fail()
    with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
        f1.seek(0, SEEK_END)
        sz1 = f1.tell()
        f1.seek(0)

        f2.seek(0, SEEK_END)
        sz2 = f2.tell()
        f2.seek(0)
        if not sz1 <= sz2-offset:
            return fail()
        f2.seek(offset)
        while 1:
            bs1 = f1.read(BLOCK_SIZE)
            if not bs1:break
            bs2 = f2.read(len(bs1))
            if not bs1==bs2:
                return fail()
        return succ()

if __name__ == "__main__":
    main()


__all__
from nn_ns.app.file_startswith_ import *
