
'''
unicodedata.category(char) in ('Ps', 'Pe', 'Pi', 'Pf')
or unicodedata.mirrored(char)
'''

import unicodedata
CHAR_ORD_UPPER = 0x110000

def iter_open_close_info4s():
    for i in range(CHAR_ORD_UPPER):
        char = chr(i)
        category = unicodedata.category(char)
        name = unicodedata.name(char, '')
        if (category in ('Ps', 'Pe', 'Pi', 'Pf')
            or unicodedata.mirrored(char)
            #or 'bracket' in name.lower() or 'paren' in name.lower()
            ):
            #print(i, name, '#', char)
            yield i, name, char, category
        #if unicodedata.bidirectional(char):
        #   print(i, unicodedata.bidirectional(char))

def list_open_close(fout):
    for i, name, char, category in iter_open_close_info4s():
        print('U+{:0>6X}'.format(i), '#', name, '#', char, file=fout)
def show_open_close_numbers(fout):
    f = lambda head: print(head, '0x{:0>6X}'.format(i), '#', name, '#', char, file=fout)
    it = iter_open_close_info4s()
    for i, name, char, category in it:
    #bug:for i, name, char, category in iter_open_close_info4s():
        f('(')
        break
    for i, name, char, category in it:
    #bug:for i, name, char, category in iter_open_close_info4s():
        f(',')
    #bug:print(')')
    print(')', file=fout)

def main(argv=None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='show open/close bracket/quot')
    parser.add_argument('-o', '--output', type=str, help='output file name')
    parser.add_argument('-f', '--force', action='store_true', help='overwrite output file if exists')
    parser.add_argument('-e', '--encoding', type=str, default='utf8'
                        , help='output encoding')
    parser.add_argument('--format', choices='list numbers'.split()
                        , default='list'
                        , help='output format')

    args = parser.parse_args()
    f = list_open_close if args.format == 'list' else show_open_close_numbers

    may_ofname = args.output
    if may_ofname is None:
        fout = sys.stdout
        f(fout)
    else:
        ofname = may_ofname
        mode = 'w' if args.force else 'x'
        with open(ofname, mode, encoding=args.encoding) as fout:
            f(fout)


if __name__ == '__main__':
    main()


