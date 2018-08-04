r'''
glob_cmd | line_filter_cmd | sort_lines_cmd
#unique/reverse

input:
    [line] | [((keys...), repr(line))]

example:
    > py sort_lines_cmd.py
    134235
    53453
    4564
    4645
    ^Z
    134235
    4564
    4645

> ls . | py line_filter_cmd.py "f(.+)(\..+)" --group_names 1 2 | py sort_lines_cmd.py

> ls . | py line_filter_cmd.py "f(.+)(\..+)" --group_names 1 2 | py sort_lines_cmd.py
(('ile_filter', '.py'), 'file_filter.py')
(('ile_rename', '.py'), 'file_rename.py')
(('ile_rename2', '.py'), 'file_rename2.py')
(('ile_rename_example', '.py'), 'file_rename_example.py')
(('ile_tree', '.py'), 'file_tree.py')
(('ilter_cmd', '.py'), 'line_filter_cmd.py')
(('rename', '.py'), 'frename.py')



# --reverse
> ls . | py line_filter_cmd.py "f(.+)(\..+)" --group_names 1 2 | py sort_lines_cmd.py --reverse
(('rename', '.py'), 'frename.py')
(('ilter_cmd', '.py'), 'line_filter_cmd.py')
(('ile_tree', '.py'), 'file_tree.py')
(('ile_rename_example', '.py'), 'file_rename_example.py')
(('ile_rename2', '.py'), 'file_rename2.py')
(('ile_rename', '.py'), 'file_rename.py')
(('ile_filter', '.py'), 'file_filter.py')


# KEY_LINE
> ls . | py line_filter_cmd.py "f(.+)(\..+)" --group_names 1 2 | py sort_lines_cmd.py --reverse --line_type=KEY_LINE
frename.py
line_filter_cmd.py
file_tree.py
file_rename_example.py
file_rename2.py
file_rename.py
file_filter.py





'''


import ast
#import re
#from glob import iglob
from itertools import groupby # chain
from seed.io.may_open import may_open_stdout, may_open_stdin


class Globals:
    output_file_encoding = 'utf8'
    input_file_encoding = 'utf8'



RAW_LINE = 'RAW_LINE'
KEY_LINE = 'KEY_LINE'
def main(argv=None):
    '''
'''
    import argparse, sys

    parser = argparse.ArgumentParser(description='stable sort lines')
    add_argument = parser.add_argument


    add_argument('--line_type', choices='RAW_LINE KEY_LINE'.split()
        , default=RAW_LINE
        , help='type of input lines')
    add_argument('--unique', action='store_true'
        , default=False
        , help='remove duplicate lines')
    add_argument('--reverse', action='store_true'
        , default=False
        , help='stable sort by reverse ordering')


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

    if args.line_type == RAW_LINE:
        def input_line2val(input_line):
            val = org_line = input_line
            return val
        def val2org_line(val):
            return val
    elif args.line_type == KEY_LINE:
        def input_line2val(input_line):
            assert input_line[-1:] != '\n'
            try:
                keys, org_line = ast.literal_eval(input_line)
            except:
                print(input_line)
                print(repr(input_line))
                raise
            assert type(keys) is tuple
            return keys, org_line
        def val2org_line(val):
            keys, org_line = val
            return org_line



    vals = [] # [org_line] | [(keys, org_line)]
    with may_open_stdout(args.output_file, 'xt'
            , encoding=args.output_encoding) as fout\
        , may_open_stdin(args.input_file, 'rt'
            , encoding=args.input_encoding) as fin:
        EOF = False
        for line in fin:
            #print(repr(line))
            #bug:
            #   xxx.bat xxx | this_cmd
            #   xxx.bat should be:
            #       @xxx_cmd args
            #       @yyy_cmd args
            if EOF:
                raise logic-error
            if line == '':
                # EOF?
                EOF = True
                continue
            if line[-1:] == '\n':
                line = line[:-1]
            input_line = line
            vals.append(input_line2val(input_line))

        vals.sort(reverse=args.reverse)
        if args.unique:
            vals = [unique_line for unique_line, _ in groupby(vals)]

        for val in vals:
            org_line = val2org_line(val)
            print(org_line, file=fout)

    #parser.exit()
    return


if __name__ == '__main__':
    main()


