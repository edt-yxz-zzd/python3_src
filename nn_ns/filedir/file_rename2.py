
'''

ls -c -r -1 | py -m nn_ns.filedir.file_rename2 3 .


1) list and sort and filter filenames
ls -c -r -1
    last time first!!! so, we need "-r"
-c
    sort by change time
    ctime - change_time - time of last status change
    ????????? sort by create time ?????????? NO
        ctime is not creation_time
-t
    sort by modification time
-u
    sort by last access time
-r
    reverse order while sorting
-1
    list one file per line
'''



from .file_rename import rename_to
import argparse
import os.path as os_path


def split_tuples(length, tuples):
    def mk_iter():
        return range(length)
    lsls = tuple([] for _ in mk_iter())
    for t in tuples:
        for i in mk_iter():
            lsls[i].append(t[i])
    return lsls

def split_fname(fname):
    folder, name = os_path.split(fname)
    base_name, ext_name = os_path.splitext(name)
    return folder, base_name, ext_name


def split_fnames(fnames):
    folders, base_names, ext_names = split_tuples(3, map(split_fname, fnames))
    return folders, base_names, ext_names


def file_rename2(old_fnames, new_basename_width = 3, new_folder = None
    , *, offset = 0, prefix = '', suffix = ''):
    '''\
if new_folder is None, then use original folder
'''
    old_fnames, new_fnames = rename_prepare(
        old_fnames, new_basename_width, new_folder
        , offset = offset, prefix = prefix, suffix = suffix)
    rename_to(old_fnames, new_fnames)
def rename_prepare(old_fnames, new_basename_width = 3, new_folder = None
    , *, offset = 0, prefix = '', suffix = ''):
    old_fnames = list(old_fnames)
    folders, base_names, ext_names = split_fnames(old_fnames)
    if new_folder is not None:
        folders = [new_folder] * len(folders)

    # ignore base_name
    new_fnames = to_new_fnames(ext_names
                            , new_basename_width = new_basename_width
                            , offset = offset
                            , prefix = prefix
                            , suffix = suffix)
    new_fnames = [os_path.join(folder, new_fname)
                    for folder, new_fname in zip(folders, new_fnames)]
    return old_fnames, new_fnames


def to_new_fnames(ext_names, *, new_basename_width, offset, prefix='', suffix=''):
    new_fnames = []
    # ignore base_name
    fmt = '{{:0>{width}d}}'.format(width = new_basename_width)
    f = fmt.format
    for idx, ext_name in enumerate(ext_names, offset):
        new_base_name = f(idx)
        new_fname = ''.join([prefix, new_base_name, suffix, ext_name])
        new_fnames.append(new_fname)

    return new_fnames





class IntegerGE:
    def __init__(self, min):
        assert isinstance(min, int)
        self.min = min
    def __call__(self, string):
        try:
            i = int(string)
        except:
            raise argparse.ArgumentTypeError("{!r} is not integer"
                        .format(string))
        if i >= self.min:
            return i
        raise argparse.ArgumentTypeError("{!r} is not integer great than {}"
                        .format(string, self.min))
def integer_ge(min):
    return IntegerGE(min)
def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='rename file names')
    parser.add_argument('width', type=IntegerGE(1)
                        , help = 'new file base name width: 4 => 0000.jpg'
                        )
    parser.add_argument('output_dir', type=str, nargs='?', default = None
                        , help = 'if not given, use the original folder'
                        )
    parser.add_argument('--offset', type=IntegerGE(0), default=0
                        , help='the begin number'
                        )
    parser.add_argument('--prefix', type=str, default=''
                        , help='the prefix of new file names'
                        )
    parser.add_argument('--suffix', type=str, default=''
                        , help='the suffix of new file names'
                        )
    parser.add_argument('--dry_run', action='store_true', default = False
                        , help='show what name each file be renamed to'
                        )

    args = parser.parse_args(args)
    with sys.stdin as fin:
        old_fnames = [line.strip() for line in fin]

    old_fnames, new_fnames =\
        rename_prepare(old_fnames, args.width, args.output_dir
            , offset = args.offset
            , prefix = args.prefix
            , suffix = args.suffix
            )
    if not args.dry_run:
        rename_to(old_fnames, new_fnames)
    else:
        for old_fname, new_fname in zip(old_fnames, new_fnames):
            print(old_fname)
            print('=> ', new_fname)

if __name__ == '__main__':
    main()

