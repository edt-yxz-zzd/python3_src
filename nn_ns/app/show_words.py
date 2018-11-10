
'''
why?
    to comment all words in a package
    e.g. to write: "def - XXX.txt"

usage:
    py -m nn_ns.app.show_words ./**/*.py
'''

import argparse
import glob
from pathlib import Path
import re
import os.path

class Global:
    block_size = 1024
#space_regex = re.compile(r'\s')
nonalpha_regex = re.compile(r'[^a-zA-Z_0-9]+')

def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='show all words in a package (once per word)'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('input_glob_pattern', type=str
                        , help='input file path glob pattern')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')

    args = parser.parse_args(args)
    encoding = args.encoding

    block_size = Global.block_size
    assert block_size >= 1
    prev_remains = [] # contain non-empty parts of a word
    def put(s):
        if s: prev_remains.append(s)

    words = set()
    def show(word):
        if not word:
            return
            raise logic-error
        L = len(words)
        words.add(word)
        if L < len(words):
            #new
            print(word)

    for path in glob.iglob(args.input_glob_pattern, recursive=True):
        if os.path.isdir(path): continue
        with open(path, encoding=encoding) as fin:
            while True:
                s = fin.read(block_size)
                if not s:
                    break
                ls = nonalpha_regex.split(s)
                if not ls: raise logic-error

                if len(ls) == 1:
                    [s] = ls
                    put(s)
                else:
                    put(ls[0])
                    ls[0] = ''.join(prev_remains)
                    prev_remains.clear()
                    put(ls[-1])
                    for word in ls[:-1]:
                        show(word)
            #end-while
            if prev_remains:
                word = ''.join(prev_remains)
                show(word)
    return
if __name__ == "__main__":
    main()


