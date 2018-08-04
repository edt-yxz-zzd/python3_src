
__all__ = '''
    file2all_char_set
    file2unique_sorted_char_string
    '''.split()
from seed.io.may_open import may_open_stdin, may_open_stdout
from seed.text.repr_string_as_unicode import repr_string_as_unicode
#from .file2all_char_set import file2all_char_set

def file2all_char_set(fin):
    # -> Set char
    all_chars = set()
    # bug: for block in fin.read(1024):
    while True:
        block = fin.read(1024)
        if not block: break

        all_chars.update(block)
    return all_chars

def chars2sorted_char_string(chars):
    # -> String
    return ''.join(sorted(chars))
def file2unique_sorted_char_string(fin):
    # -> String
    return chars2sorted_char_string(file2all_char_set(fin))



#sort and unique chars
def main(argv=None):
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='sort and unique chars in text.')
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
    parser.add_argument('-u', '--repr_as_unicode', action='store_true'
                            , default = False
                            , help='output char in format \\UXXXXXXXX')


    args = parser.parse_args(argv)

    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        #all_chars = file2unique_sorted_char_string(fin)
        all_chars = file2all_char_set(fin)
    #txt = chars2sorted_char_string(all_chars)

    s = chars2sorted_char_string(all_chars)
    if args.repr_as_unicode:
        s = repr_string_as_unicode(s)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        print(s, file=fout)

if __name__ == '__main__':
    main()



