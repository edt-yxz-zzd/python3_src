
r'''
under same dir

example:
    # rename xx.svg to xx.svg.png
    file_rename_cmd svg_as_png "^.*\.svg$" ".*" "r""\g<0>.png"""
example:
    # offset
    py -m nn_ns.filedir.file_rename_cmd --dry_run . "chapter\d+.html" "\d+" "lambda m: '{:0>4}'.format(int(m.group(0))+757)"
    py -m nn_ns.filedir.file_rename_cmd . "chapter\d+.html" "\d+" "offset_number(4,0,757)" --dry_run

    # fill width
    py -m nn_ns.filedir.file_rename_cmd . "chapter\d+.html" "\d+" "offset_number(4,0,0)" --dry_run

    # partial offset
    py -m nn_ns.filedir.file_rename_cmd . "chapter\d+.html" "\d+" "offset_number(4,0, 1, min=767)" --dry_run
    py -m nn_ns.filedir.file_rename_cmd . "chapter\d+.html" "\d+" "offset_number(4,0, 1, min=759)" --dry_run
'''

__all__ = '''
    file_rename
    '''.split()

from .reorder_src_dst_pairs import reorder_src_dst_pairs
from .rename_under_same_folder import rename_under_same_folder
from .list_files import list_files, list_folders
import os, re


# rename_case
RenameFileOnly = 1
RenameFolderOnly = 2
RenameBoth = 3

rename_case2listdir =\
    { RenameBoth: os.listdir
    , RenameFolderOnly: list_folders
    , RenameFileOnly: list_files
    }
def get_listdir(rename_case):
    return rename_case2listdir[rename_case]
def file_rename(folder, regex_for_filter, regex_for_sub, matchobj2str
        , rename_case, *, recursive, pseudo_rename):
    listdir = get_listdir(rename_case)
    if not recursive:
        _file_rename(folder, regex_for_filter, regex_for_sub, matchobj2str
            , listdir, pseudo_rename=pseudo_rename)
        return

    def this_func(folder):
        subfolders = list_folders(folder)
        for subfolder in subfolders:
            this_func(subfolder)

        # post_ordering since maybe dry_run
        _file_rename(folder, regex_for_filter, regex_for_sub, matchobj2str
            , listdir, pseudo_rename=pseudo_rename)
    this_func(folder)


def _file_rename(folder, regex_for_filter, regex_for_sub, matchobj2str
        , listdir, *, pseudo_rename):
    basenames = listdir(folder)
    match = regex_for_filter.fullmatch
    basenames = filter(match, basenames)
    src_dst_basename_pairs = iter_src_dst_pairs(basenames, regex_for_sub, matchobj2str)
    rename_under_same_folder(folder, src_dst_basename_pairs, pseudo_rename=pseudo_rename)

def iter_src_dst_pairs(srcs, regex, matchobj2str):
    for src in srcs:
        dst = regex.sub(matchobj2str, src)
        yield src, dst



"lambda m: '{:0>4}'.format(int(m.group(0))+757)"
"lambda m: '{{:0>{fill_width}}}'.format(int(m.group({group}))+{offset})"
def offset_number(fill_width, group, offset, *, min=None, max=None):
    '''
e.g.
    fill_width = "4"
    group = "0" or "'xxx'"
    offset = "757"
    "offset_number(4, 0, 757)"
    "offset_number(4, 'xxx', 757)"
'''
    if min is None:
        min = float('-inf')
    if max is None:
        max = float('inf')
    fmt = f'{{:0>{fill_width}}}'
    def matchobj2str(m):
        s = m.group(group)
        i = int(s)
        if min <= i <= max:
            return fmt.format(i+offset)
        else:
            return s
    return matchobj2str
    return eval(f"lambda m: '{{:0>{fill_width}}}'.format(int(m.group({group}))+{offset})")
    return lambda m: '{{:0>{fill_width}}}'.format(fill_width).format(int(m.group(group))+offset)


def main(argv=None):
    '''
'''
    import argparse, sys

    parser = argparse.ArgumentParser(description='rename_under_same_folder'
        , epilog='''if matchobj2str_case==ReplPyObj:
    # example
    matchobj2str = "lambda m: '{:0>4}'.format(int(m.group(0))+757)"
    ###############################4######################0###757#
    matchobj2str = "offset_number(4, 0, 757)"
'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )

    add_argument = parser.add_argument

    add_argument('folder', type=str
        , help='the folder; src and dst are all under the same folder')
    add_argument('regex_pattern_for_filter', type=str
        , help='regex_pattern used to list basenames')
    add_argument('regex_pattern_for_sub', type=str
        , help='regex_pattern used to yield new basename')
    add_argument('matchobj2str', type=str
        , help='matchobj2str used to yield new basename')

    add_argument('--matchobj2str_case'
        , choices = 'ReplStr ReplPyObj'.split()
        , default='ReplPyObj'
        , help='matchobj2str case: direct_repl_str or python_repl_str or python_repl_func')
    add_argument('--rename_case'
        , choices = 'RenameFileOnly RenameFolderOnly RenameBoth'.split()
        , default='RenameFileOnly'
        , help='rename files or rename folders or rename both')

    add_argument('-r', '--recursive', action='store_true'
        , default=False
        , help='recursively rename')
    add_argument('--dry_run', action='store_true'
        , default=False
        , help='dry_run rename')

    args = parser.parse_args(argv)

    folder = args.folder
    regex_for_filter = re.compile(args.regex_pattern_for_filter)
    regex_for_sub = re.compile(args.regex_pattern_for_sub)
    recursive = args.recursive

    pseudo_rename = None
    if args.dry_run:
        def pseudo_rename(src, dst):
            print((src, dst))

    matchobj2str = args.matchobj2str
    if args.matchobj2str_case == 'ReplPyObj':
        matchobj2str = eval(matchobj2str)
        assert type(matchobj2str) is str or callable(matchobj2str)

    rename_case = args.rename_case
    d = \
        { 'RenameFileOnly': RenameFileOnly
        , 'RenameBoth': RenameBoth
        , 'RenameFolderOnly': RenameFolderOnly
        }
    rename_case = d[rename_case]

    file_rename(folder, regex_for_filter, regex_for_sub, matchobj2str
        , rename_case, recursive=recursive, pseudo_rename=pseudo_rename)



    #parser.exit()
    return


if __name__ == '__main__':
    main()


