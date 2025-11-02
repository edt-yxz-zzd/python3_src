#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/copy6root_cmd.py

nn_ns.app.copy6root_cmd
py -m nn_ns.app.debug_cmd   nn_ns.app.copy6root_cmd -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.copy6root_cmd:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py -m nn_ns.app.copy6root_cmd   -to script/png/   -from /sdcard/0my_files/tmp/out4py/py_src/  -v -ig  --  site-packages/PIL/_binary.py site-packages/PIL/PngImagePlugin.py site-packages/png/

e ../../python3_src/bash_script/app/copy6root

copy6root   -to script/png/   -from /sdcard/0my_files/tmp/out4py/py_src/  -v -ig  --  site-packages/PIL/_binary.py site-packages/PIL/PngImagePlugin.py site-packages/png/




py_adhoc_call   nn_ns.app.copy6root_cmd   @f
from nn_ns.app.copy6root_cmd import *
]]]'''#'''
__all__ = r'''
main
'''.split()#'''
__all__






def main(args=None, /):
    from seed.filesys.copy6root import copy6root
    #def copy6root(dst_root_dir, src_root_dir, relative_paths4both_src_dst, /, *, dst_root_dir_nonexist_ok=False, skip_when_dst_file_exist=False, overwrite_when_dst_file_exist=False, interactive_when_dst_file_exist=False, verbose=False):
    import argparse

    parser = argparse.ArgumentParser(
        description='copy with whole local path i.e. keep the tree struct'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-to', '--dst_root_dir', type=str, required=True
                        , help='target root path')
    parser.add_argument('-from', '--src_root_dir', type=str, required=True
                        , help='source root path')
    parser.add_argument('relative_paths4both_src_dst', type=str, nargs='+'
                        , help='relative paths for both src,dst')

    parser.add_argument('--dst_root_dir_nonexist_ok', action='store_true'
                        , default = False
                        , help='auto create dst_root_dir')
    parser.add_argument('-ig', '--skip_when_dst_file_exist', action='store_true'
                        , default = False
                        , help='ignore/skip when dst_file exists')
    parser.add_argument('-fc', '--overwrite_when_dst_file_exist', action='store_true'
                        , default = False
                        , help='overwrite when dst_file exists')
    parser.add_argument('-i', '--interactive_when_dst_file_exist', action='store_true'
                        , default = False
                        , help='ask when dst_file exists')
    parser.add_argument('-v', '--verbose', action='store_true'
                        , default = False
                        , help='verbose')
    #.parser.add_argument('-f', '--force', action='store_true'
    #.                    , default = False
    #.                    , help='open mode for output file')

    args = parser.parse_args(args)
    #force = args.force
    dst_root_dir = args.dst_root_dir
    src_root_dir = args.src_root_dir
    relative_paths4both_src_dst = args.relative_paths4both_src_dst
    dst_root_dir_nonexist_ok = args.dst_root_dir_nonexist_ok
    skip_when_dst_file_exist = args.skip_when_dst_file_exist
    overwrite_when_dst_file_exist = args.overwrite_when_dst_file_exist
    interactive_when_dst_file_exist = args.interactive_when_dst_file_exist
    verbose = args.verbose
    #######
    copy6root(dst_root_dir, src_root_dir, relative_paths4both_src_dst, dst_root_dir_nonexist_ok=dst_root_dir_nonexist_ok, skip_when_dst_file_exist=skip_when_dst_file_exist, overwrite_when_dst_file_exist=overwrite_when_dst_file_exist, interactive_when_dst_file_exist=interactive_when_dst_file_exist, verbose=verbose)
    #######

if __name__ == "__main__":
    main()












__all__
from nn_ns.app.copy6root_cmd import *
