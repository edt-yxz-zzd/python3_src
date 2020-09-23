
r"""
$ pwd
/sdcard/0my_files/git_repos/python3_src
$ py -m nn_ns.app.count_identifiers -i . -g '**/*.py' -o ~/tmp/tmp.txt

$ py -m nn_ns.app.count_identifiers -i /sdcard/0my_files/unzip/py_doc/python-3.8.1-docs-html/ -g '**/*.html' -o ~/tmp/py_doc_381_words.txt  -f
#"""

import re
import pathlib
from seed.tiny import print_err

word_rex = re.compile(r"\w+")

def _add(d, k):
    d.setdefault(k, 0)
    d[k] += 1

def feed(d, txt):
    for m in word_rex.finditer(txt):
        w = m.group(0)
        _add(d, w)

def lst(d):
    def f(kv):
        k, i = kv
        return -i, k
    return sorted(d.items(), key=f)

def show(file, ls):
    for word, count in ls:
        print(word, count, file=file)

def iter_files(path, glob):
    root = pathlib.Path(path)
    for path in root.glob(glob):
        if path.is_file():
            yield path



def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='count identifiers'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-g', '--glob_pattern', type=str, default=None
                        , help='treat <input> as folder path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    d = {}
    def f(fin):
        for line in fin:
            feed(d, line)

    may_glob_pattern = args.glob_pattern
    if may_glob_pattern is None:
        may_ifname = args.input
        with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
            f(fin)
    else:
        glob_pattern = may_glob_pattern
        may_root = args.input
        root = '.' if not may_root else may_root
        for path in iter_files(root, glob_pattern):
            try:
                with open(path, 'rt', encoding=encoding) as fin:
                    f(fin)
            except UnicodeDecodeError:
                print_err(path)
                continue
            except:
                print_err(path)
                raise

    ls = lst(d)
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        show(fout, ls)

if __name__ == "__main__":
    main()



