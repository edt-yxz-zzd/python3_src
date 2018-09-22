
import sys
from glob import iglob
import os.path

def iter_paths(patterns):
    for pattern in patterns:
        yield from iglob(pattern, recursive=True)

def test_encoding(path, *, encoding):
    try:
        with open(path, encoding=encoding) as fin:
            while fin.read(1024):pass
    except UnicodeError:
        return False
    return True

def read_txt(path, *, encoding):
    with open(path, encoding=encoding) as fin:
        return fin.read()
def may_read_txt(path, *, encoding):
    try:
        return read_txt(path, encoding=encoding)
    except UnicodeError:
        return None

def err_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)



def write_txt(*, text, input_path, output_dir, iencoding, oencoding, force):
    fname = os.path.basename(input_path)
    output_path = os.path.join(output_dir, fname)
    if not force and os.path.exists(output_path):
        err_print(f'x input_path={input_path!r}: file exists: {output_path!r}')

    try:
        bs = text.encode(encoding=oencoding)
    except UnicodeError:
        err_print(f'x input_path={input_path!r}: cannot encoded by {oencoding!r}')

    omode = 'wb' if force else 'xb'
    with open(output_path, omode) as fout:
        fout.write(bs)
    err_print(f'o input_path={input_path!r}, iencoding={iencoding!r}, oencoding={oencoding!r} => opath={output_path!r}')

def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='re_encode text by a fix encoding'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input_path_patterns', type=str
                        , action='append'
                        , default=[]
                        , help='input text glob patterns')
    parser.add_argument('-ie', '--input_encodings', type=str
                        , action='append'
                        , default=[]
                        #['gb18030', 'utf_8', 'utf_16_le', 'utf_16_be', 'utf_32_le', 'utf_32_be']
                        , help='input file encodings')
    parser.add_argument('-od', '--output_folder', type=str
                        , required=True
                        , help='output directory')
    parser.add_argument('-oe', '--output_encoding', type=str
                        , required=True
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(argv)
    force = args.force

    input_patterns = args.input_path_patterns
    input_encodings = args.input_encodings
    oencoding = args.output_encoding
    output_dir = args.output_folder
    err_print(f're_encode input_path_patterns={input_patterns!r} input_encodings={input_encodings!r} output_folder={output_dir!r} output_encoding={oencoding!r}')
    err_print('=============================')
    for input_path in iter_paths(input_patterns):
        if test_encoding(input_path, encoding=oencoding):
            err_print(f'= input_path={input_path!r}')
            continue
        for iencoding in input_encodings:
            may_txt = may_read_txt(input_path, encoding=iencoding)
            if may_txt is not None:
                txt = may_txt
                write_txt(text=txt, input_path=input_path, output_dir=output_dir
                        , iencoding=iencoding, oencoding=oencoding, force=force)
                break
        else:
            err_print(f'x input_path={input_path!r}: cannot decoded by {input_encodings!r}')


if __name__ == "__main__":
    main()


