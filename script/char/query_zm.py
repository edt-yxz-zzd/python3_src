
'''
rem query zeng ma
rem grep %* E:\my_data\program_output\py3\nn_ns\char\char2zm\str_char2zm_ls.txt
rem cat E:\my_data\program_output\py3\nn_ns\char\char2zm\str_char2zm_ls.txt | grep %* -
grep: writing output: Invalid argument
grep: writing output: No space left on device
'''


import re

def find_re_in_lines(rex, file, beg_line_no):
    return [line for line in enumerate(file, beg_line_no)
                    if rex.search(line)]

def find(hanzi_list, file):
    s = set(hanzi_list)
    ls = [line for line in file if line and line[0] in s]
    founds = set(line[0] for line in ls)
    not_founds = s - founds
    return ls, founds, not_founds
def main(argv=None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='query hanzi zengma')
    parser.add_argument('hanzi_list', type=str,
                        help='each hanzi in hanzi list will be queried')
    parser.add_argument('-e', '--encoding', type=str, default='utf8',
                        help='encoding of the dict txt')
    parser.add_argument('-d', '--dict', type=str, default=None
                        , help='the dict txt file')

    args = parser.parse_args(argv)

    if args.dict is not None:
        file = open(args.dict, encoding = args.encoding)
    else:
        file = sys.stdin

    try:
        lines, founds, not_founds = find(args.hanzi_list, file)
        # for line in lines: print(line)
        print(''.join(lines))
        tail = '  founds {}:{!r}; not_founds {}:{!r}'.format(
            len(founds), ''.join(sorted(founds)),
            len(not_founds), ''.join(sorted(not_founds))
            )
        print(tail)
    finally:
        if args.dict is not None:
            with file: pass

if __name__ == '__main__':
    main()


