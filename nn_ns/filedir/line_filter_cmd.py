

'''
filter lines and snap fields
    to use with glob_cmd:
        > glob_cmd | line_filter_cmd

example:
    > ls . | py line_filter_cmd.py s.*  f.*\.py
    sym_link.py
    file_filter.py
    file_rename.py
    file_rename2.py
    file_rename_example.py
    file_tree.py
    frename.py

    > ls . | py line_filter_cmd.py s(.*)  f(.*)\.py --group_names 1
    (('ym_link.py',), 'sym_link.py')
    (('ile_filter',), 'file_filter.py')
    (('ile_rename',), 'file_rename.py')
    (('ile_rename2',), 'file_rename2.py')
    (('ile_rename_example',), 'file_rename_example.py')
    (('ile_tree',), 'file_tree.py')
    (('rename',), 'frename.py')


    # convert '2' to 2
    > ls . | py line_filter_cmd.py (\d+)\.py --group_names 1
    (('2',), 'file_rename2.py')
    > ls . | py line_filter_cmd.py (\d+)\.py --group_names 1 --INT_GROUP
    ((2,), 'file_rename2.py')

    # named group "g" is group "1"
    > ls . | py line_filter_cmd.py "(?P<g>\d+)\.py" --group_names 1 --INT_GROUP
    ((2,), 'file_rename2.py')
    > ls . | py line_filter_cmd.py "(?P<g>\d+)\.py" --group_names g --INT_GROUP
    ((2,), 'file_rename2.py')
'''

#def line_filter_cmd

import re
#from glob import iglob
from itertools import chain
from seed.io.may_open import may_open_stdout, may_open_stdin


class Globals:
    output_file_encoding = 'utf8'
    input_file_encoding = 'utf8'

def main(argv=None):
    '''
'''
    import argparse, sys

    parser = argparse.ArgumentParser(description='filter lines')
    add_argument = parser.add_argument

    add_argument('regex_patterns', type=str
        , nargs='+'
        , metavar='REGEX_PATTERN'
        , help='regular expressions; if line match i-th regex, then put it into the i-th output slot; finally, all slots will be chained together')
    add_argument('--group_names', type=str
        , nargs='*'
        , metavar='NAME'
        , help='if group_names was set, then snap that named group of regex; each line will be output as ((groups...), repr(line))')

    '''#group name can not startswith digit...
    add_argument('--INT_NAME', action='store_true'
        , default=False
        , help='a group name is treated as integer if possible')
    '''
    add_argument('--INT_GROUP', action='store_true'
        , default=False
        , help='a named group is treated as integer if possible')


    add_argument('-i', '--input_file', type=str
        , default=None
        , help='the input file')
    add_argument('-ie', '--input_encoding', type=str
        , default = Globals.input_file_encoding
        , help='the encoding of input file')
    add_argument('-o', '--output_file', type=str
        , default=None
        , help='the output file')
    add_argument('-oe', '--output_encoding', type=str
        , default = Globals.output_file_encoding
        , help='the encoding of output file')

    args = parser.parse_args(argv)
    re_objs = list(map(re.compile, args.regex_patterns))
    def to_int_if_possible(s):
        try:
            return int(s)
        except:
            return s
    def to_ints_if_possible(strs):
        return list(map(to_int_if_possible, strs))
    def get_groups(m, group_names):
        # m.group(*group_names) will error if len <= 1
        return tuple(map(m.group, group_names))

    slots = [[] for _ in range(len(re_objs))]
    if args.group_names:# and args.INT_NAME:
        args.group_names = to_ints_if_possible(args.group_names)
    with may_open_stdout(args.output_file, 'xt'
            , encoding=args.output_encoding) as fout\
        , may_open_stdin(args.input_file, 'rt'
            , encoding=args.input_encoding) as fin:
        EOF = False
        for line in fin:
            if EOF:
                raise logic-error
            if line == '':
                # EOF?
                EOF = True
                continue
            if line[-1:] == '\n':
                line = line[:-1]
            for i, rex in enumerate(re_objs):
                #m = rex.match(line)
                m = rex.search(line)
                if m: break
            else:
                # no match
                # drop this line
                continue
            if args.group_names:
                # named_groups
                groups = get_groups(m, args.group_names)
                if args.INT_GROUP:
                    # convert to int
                    groups = to_ints_if_possible(groups)

                groups = tuple(groups)
                out_line = repr((groups, line))
            else:
                out_line = line # no repr!!
            #print(out_line, file=fout)
            slots[i].append(out_line)
        for out_line in chain.from_iterable(slots):
            print(out_line, file=fout)

    #parser.exit()
    return


if __name__ == '__main__':
    main()


