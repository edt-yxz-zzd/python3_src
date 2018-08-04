

import os
from datetime import datetime
from seed.special_funcs import identity as eye_func
from seed.debug.print_err import print_err
from sand import get_pylike_encoding_from_path, \
     FormatError
from .zip_by_7z import zip_by_7z


default_txtname = 'path.txt'
def folder2iter_folder_backup_paths_warnings_ls(
    path, pred:'lambda folder: True'=None,
    *, txtname = default_txtname):
    '''yield folder, backup_paths, warnings

if not pred(folder):
    skip folder

detect "path.txt" in each folder

encoding is utf-8 or using python encoding declarations
    # -*- coding: <encoding-name> -*-
    encoding has to be compatible with ascii


each line should be:
    begin with '#' is comment
    or begin with '!' is reserved
        begin with '!#' is a warning
    or empty line
    or a path of file required to backup
'''
    if pred is None:
        pred = lambda folder: True
    if txtname is None:
        txtname = default_txtname

    false_prefix = None
    for dirpath, dirnames, filenames in os.walk(path):
        if false_prefix:
            if dirpath.startswith(false_prefix):
                print('how to skip folder??')
                yeah, skipped
                continue
            else:
                false_prefix = None
        if not pred(dirpath):
            dirnames.clear()
            false_prefix = dirpath
            continue

        ### real work
        txtpath = os.path.join(dirpath, txtname)
        folder = dirpath
        backup_paths, warnings = [], []
        if os.path.isfile(txtpath):
            encoding = get_pylike_encoding_from_path(txtpath)
            with open(txtpath) as fin:
                for line in fin:
                    if not line[-1] == '\n':
                        #print(repr(line))
                        line += '\n' # last line
                    assert line[-1] == '\n'
                    if line.startswith('#'):
                        continue
                    elif line.startswith('!'):
                        if line.startswith('!#'):
                            warnings.append(line[2:-1])
                        else:
                            raise FormatError('unknown line startswith {!r} ...'
                                              .format(line[:20]))
                    else:
                        backup_paths.append(line[:-1])
        # even not exists txtpath !!
        yield folder, backup_paths, warnings 
    return


def backup_tofrom_pairs(tofrom_pairs, extend=None, mode='x', exe7z_path=None):
    'to_path = to + extend if extend'
    for to_path, from_path in tofrom_pairs:
        if extend:
            to_path += extend

        if os.path.exists(to_path):
            print_err('skip since to_path exists : {} :<-: {}'
                      .format(to_path, from_path))
            continue
        try:
            zip_by_7z(to_path, from_path, mode='x', exe7z_path=exe7z_path)
        except:
            if __name__ == '__main__':
                to_path, from_path = map(os.path.abspath, [to_path, from_path])
                print_err('zip_by_7z raise:')
                print_err('\tto_path :', to_path)
                print_err('\tfrom_path :', from_path)
            raise
        
    return
##
##t = datetime.today()
##print('{:%Y%m%d}'.format(t))

default_print_warning = print_err
null_print_warning = lambda *args, **kwargs: None
default_basename_fmt = '[{date:%Y%m%d}]{basename}'
default_warning_prefix = 'warning from path.txt'
def iter_tofrom_pairs_from_iter_folder_backup_paths_warnings_ls(
    folder_backup_paths_warnings_iterable,
    # for store_path not backup_path
    basename_fmt = default_basename_fmt,
    basename_transform:'lambda x:x' = eye_func,
    folder_transform:'lambda x:x' = eye_func,
    path_transform:'lambda x:x' = eye_func,
    print_warning:'noprint if None' = default_print_warning,
    warning_prefix = default_warning_prefix,
    **fmt_kwargs):
    '''yield store_path, backup_path

fmt_kwargs:
    note {date} and {basename} are available
    {date} can be overwrite but {basename} cannot
'''
    args = basename_fmt, basename_transform, folder_transform, path_transform, warning_prefix
    defaults = [default_basename_fmt, eye_func, eye_func, eye_func, default_warning_prefix]
    args = (default if arg is None else arg for arg, default in zip(args, defaults))
    basename_fmt, basename_transform, folder_transform, path_transform, warning_prefix = args

    if 'date' not in fmt_kwargs:
        fmt_kwargs['date'] = datetime.today()

    # since user can provide basename_fmt
    # date can be of any type
##    if not isinstance(fmt_kwargs['date'], datetime):
##        raise TypeError("not isinstance(fmt_kwargs['date'], datetime)")

    for folder, backup_paths, warnings in folder_backup_paths_warnings_iterable:
        if print_warning is not None:
            for warning in warnings:
                print_warning(warning_prefix, ':', folder, ':', warning)

        folder = folder_transform(folder)
        for backup_path in backup_paths:
            basename = os.path.basename(backup_path)
            basename = basename_transform(basename)
            basename = basename_fmt.format(basename=basename, **fmt_kwargs)
            
            store_path = os.path.join(folder, basename)
            store_path = path_transform(store_path)
            yield store_path, backup_path
    return



def auto_backup(path, extend='.7z', mode='x', exe7z_path=None):
    if not extend:
        extend = '.7z'
    it = folder2iter_folder_backup_paths_warnings_ls(path)
    tofrom_pairs = iter_tofrom_pairs_from_iter_folder_backup_paths_warnings_ls(it)
    backup_tofrom_pairs(tofrom_pairs, extend=extend, mode=mode, exe7z_path=exe7z_path)
    
    
if 0:
    _path = r'E:\my_data\program_config'
    def _t(show=True, path=_path):
        from pprint import pprint
        ls = list(folder2iter_folder_backup_paths_warnings_ls(path))
        if show: pprint(ls)
        return ls
    #_t()
    def _t2(show=True, path=_path):
        from pprint import pprint
        *ls, = iter_tofrom_pairs_from_iter_folder_backup_paths_warnings_ls(_t(show=False))
        if show: pprint(ls)
        return ls
    #_t2()
    def _t3(show=True, path=_path):
        from pprint import pprint
        # bug: backup_to_from_pairs(_t2(show=False), extend=None)
        backup_tofrom_pairs(_t2(show=False), extend='.7z')
    #_t3()
    auto_backup(_path)


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='auto backup to the given storing path')
    parser.add_argument('storing_path', type=str,
                        help = ('the storing path '
                                'which "path.txt" will be search in '
                                'and archive files will be stored to')
                        )
    args = parser.parse_args()
    auto_backup(args.storing_path)


if __name__ == "__main__":
    main()











        

