
r'''
try ascii|gb18030|utf8|utf_8_sig|utf_16_le|utf_16_be
xxx.txt ==>>
    xxx.ascii.text  # ascii
    xxx.many.text   # not asscii and more than one
    xxx.gb.text     # only gb18030
    xxx.u8.text     # only utf8 or utf_8_sig
    xxx.u16l.text   # only utf_16_le
    xxx.u16b.text   # only utf_16_be
    xxx.none.text   # none


'''
epilog_str = __doc__

import os.path
from seed.io.iter_reads import iter_reads
def _decode_file(fname, *, encoding):
    with open(fname, 'rt', encoding=encoding) as fin:
        for _ in iter_reads(fin): pass
def is_encoding_of_file_path(fname, *, encoding):
    try:
        _decode_file(fname, encoding=encoding)
    except UnicodeDecodeError:
        return False
    return True

def is_encoding_of_bytes(bs, *, encoding):
    try:
        bs.decode(encoding)
    except UnicodeDecodeError:
        return False
    return True

def split3_fname(fname):
    folder, basename = os.path.split(fname)
    bare, ext = os.path.splitext(basename)
    return folder, bare, ext

def fname_to_rename_class(fname):
    # fname -> ascii|gb|u8|both|none
    with open(fname, 'rb') as fin:
        bs = fin.read()

    ascii = 'ascii'
    if is_encoding_of_bytes(bs, encoding=ascii):
        result = ascii
    else:
        is_gb = is_encoding_of_bytes(bs, encoding='gb18030')
        is_u8 = is_encoding_of_bytes(bs, encoding='utf_8') \
                or is_encoding_of_bytes(bs, encoding='utf_8_sig')
        is_u16l = not is_u8 and is_encoding_of_bytes(bs, encoding='utf_16_le')
        is_u16b = not is_u8 and is_encoding_of_bytes(bs, encoding='utf_16_be')
        sum = is_gb + is_u8 + is_u16l + is_u16b
        if sum > 1:
            result = 'many'
        elif not sum:
            result = 'none'
        elif is_gb:
            result = 'gb'
        elif is_u8:
            result = 'u8'
        elif is_u16l:
            result = 'u16l'
        elif is_u16b:
            result = 'u16b'
        else:
            raise logic-error

        #i = is_gb*2+is_u8
        #result = ('none', 'u8', 'gb', 'both')[i]
    return result

def main(argv=None):
    import argparse, glob

    parser = argparse.ArgumentParser(
        description='detect file encoding and rename it'
        , epilog=epilog_str
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('input_pattern', type=str, default = None
                        , help='input file path glob pattern')
    parser.add_argument('-suf', '--suffix', type=str
                        , default = '/'
                        , help='new suffix of file; default="/" unchange')
    parser.add_argument('-nr', '--not_rename'
                        , choices='ascii|gb|u8|u16l|u16b|many|none'.split('|')
                        , nargs = '*'
                        , default = []
                        , help='not rename the class; ()')
    parser.add_argument('-sh', '--show', action='store_true'
                        , default = False
                        , help='show ascii|gb|u8|both|none, instead of rename')
    parser.add_argument('-dr', '--dry_run', action='store_true'
                        , default = False
                        , help='donot rename actually')



    args = parser.parse_args(argv)

    ifname_pattern = args.input_pattern
    not_rename_classes = frozenset(args.not_rename)
    dry_run = args.dry_run

    for ifname in glob.iglob(ifname_pattern, recursive=True):
        result = fname_to_rename_class(ifname)

        if args.show:
            print(result, ifname)
        elif result in not_rename_classes:
            pass
        else:
            path, bare, ext = split3_fname(ifname)
            suffix = args.suffix
            if suffix == '/':
                suffix = ext

            basename = f'{bare}.{result}{suffix}'
            if os.path.normpath(basename) == os.path.normpath(bare+ext):
                continue

            new_fname = os.path.join(path, basename)

            if dry_run:
                print(f'{ifname!r} ==>> {new_fname!r}')
            else:
                #with open(new_fname, 'xb'):pass
                if os.path.exists(new_fname):
                    raise FileExistsError(f'{ifname!r} ==>> {new_fname!r}')
                os.replace(src=ifname, dst=new_fname)
    return


if __name__ == "__main__":
    main()



