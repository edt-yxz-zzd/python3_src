
from seed.text.make_strings_pattern import make_chars_pattern
from nn_ns.txt.find_nonGBK_chars import find_nonGBK_chars_ex, find_nonGBK_chars
from nn_ns.txt.file2all_char_set import file2all_char_set
from seed.io.may_open import may_open_stdin, may_open_stdout
from seed.text.repr_string_as_unicode import \
    repr_string_as_unicode, repr_char_as_unicode
import re


def main(argv=None):
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='find(and replace) non gbk char in novel text.')
    parser.add_argument('-e', '--encoding', type=str
                            , default='utf8'
                            , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                            , default = False
                            , help='open mode for output file')
    parser.add_argument('-i', '--input', type=str
                            , help='path to the input novel text file')
    parser.add_argument('-o', '--output', type=str
                            , help='path to the output file')
    parser.add_argument('-r', '--replace', action='store_true'
                            , default = False
                            , help='output replaced file instead of sorted non-gbk chars')


    args = parser.parse_args(argv)

    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    #all_chars = set()
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        if not args.replace:
            all_chars = file2all_char_set(fin)
        else:
            txt = fin.read()
            all_chars = set(txt)

    chars = find_nonGBK_chars(all_chars)
    #chars.update(ch for ch in all_chars if not ch.isprintable())
    #chars.update(ch for ch in all_chars if ord(ch) < 0x100 and (ord(ch) > 0x7F or not ch.isalnum()))

    if not chars:
        print('no nonGBK chars at all', file=sys.stderr)
        return

    assert chars
    if not args.replace:
        s = repr_string_as_unicode(sorted(chars))
    else:
        txt
        #bug:pattern = '[' + '|'.join(map(repr_char_as_unicode, chars)) + ']'
        #pattern = '[' + ''.join(map(repr_char_as_unicode, chars)) + ']'
        pattern = make_chars_pattern(chars)

        def replace(m):
            char = m.group(0)
            return repr_char_as_unicode(char) # \Uxxxxxxxx ; no ""
        s = re.sub(pattern, replace, txt)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        print(s, file=fout)

    '''
    may_ifname = args.input
    may_ofname = args.output
    with (may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin
        , may_open_stdout(may_ofname, omode, encoding=encoding) as fout):
        def fout_print(*args, **kwargs):
            print(*args, file=fout, **kwargs)

        for lineno, line in enumerate(fin):
            char2columns = find_nonGBK_chars_ex(line)
            if not char2columns: continue
            fout_print(char2columns, 
    '''
if __name__ == '__main__':
    main()


