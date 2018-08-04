

'''
extract_data_cmd
    glob_cmd | line_filter_cmd | sort_lines_cmd | extract_data_cmd aaa.bbb.extract --kw=kkkk --kw2=wwww
        where aaa.bbb.extract :: (fout, path, *, encoding, kw=..., kw2=...)
            # need not "encoding", but extract can require it
'''


#import ast
#import re
#from glob import iglob
#from itertools import groupby # chain
from seed.io.may_open import may_open_stdout, may_open_stdin
from nn_ns.Import.import_object import import_object


class Globals:
    output_file_encoding = 'utf8'
    input_file_encoding = 'utf8'


def parse_unknown_args(unknown_args):
    # unknown_args = args kwargs
    # args = arg*
    # kwargs = kw args
    # arg = regex"[^-].*"
    # kw = regex"--[\w\d_]+"
    #
    # output:
    #   args :: [str]
    #   kwargs :: [(str, [str])]
    #   # f(*args:[str], **dict(kwargs):{str:[str]})

    kws = [None] # no leading kw
    argss = [[]]
    for string in unknown_args:
        if string.startswith('-'):
            # kw?
            if not string.startswith('--'):
                raise ValueError(f'kwarg should startswith "--": {string!r}')
            kw_may_arg = string[2:]
            if '=' in kw_may_arg:
                kw, arg = kw_may_arg.split('=')
            elif ':' in kw_may_arg:
                kw, arg = kw_may_arg.split(':')
            else:
                kw = kw_may_arg
                arg = None
            assert kw.isidentifier()
            kws.append(kw)
            argss.append([] if arg is None else [arg])
        else:
            # arg?
            argss[-1].append(string)
    args = argss[0]
    kwargs = zip(kws[1:], argss[1:])
    return args, kwargs




def main(argv=None):
    '''
'''
    import argparse, sys

    parser = argparse.ArgumentParser(description='extract info from files'
                                    , allow_abbrev=False
                                    , epilog = '''
    NOTE:
        extract_data_cmd -oe gbk -o ./1+2.txt -ie ascii -i ./paths.txt nn_ns.filedir._extractor_example.main --encoding=utf8
          where:
            -ie ascii
                the encoding of input file which contains paths to files from which data were extracted.
                arg of this program
            --encodinga utf8
                the encoding of all files from which data were extracted.
                arg of nn_ns.filedir._extractor_example

        glob_cmd ./*.html | line_filter_cmd chapter(\d+)\.html --group_names 1 --INT_GROUP | sort_lines_cmd --line_type=KEY_LINE | extract_data_cmd -oe gbk -o ./1+2.txt nn_ns.filedir._extractor_example.main --encoding=utf8
''')
    add_argument = parser.add_argument


    add_argument('extractor', type=str
        , help='fullname of a python function: e.g. math.log2')


    add_argument('-i', '--input_file', type=str
        , default=None
        , help='the input file which contains paths')
    add_argument('-ie', '--input_encoding', type=str
        , default = Globals.input_file_encoding
        , help='the encoding of input file')
    add_argument('-o', '--output_file', type=str
        , default=None
        , help='the output file')
    add_argument('-oe', '--output_encoding', type=str
        , default = Globals.output_file_encoding
        , help='the encoding of output file')

    args, unknown_args = parser.parse_known_args(argv)
    _args, _kwargs = parse_unknown_args(unknown_args)
    _kwargs = dict(_kwargs)

    extractor_qname = args.extractor
    extractor = import_object(extractor_qname)
    # extractor :: (fout, input_fname, **kwargs) -> None


    with may_open_stdout(args.output_file, 'xt'
            , encoding=args.output_encoding) as fout\
        , may_open_stdin(args.input_file, 'rt'
            , encoding=args.input_encoding) as fin:
        for line in fin:
            if line[-1:] == '\n':
                line = line[:-1]
            path = line
            extractor(fout, path, *_args, **_kwargs)

    #parser.exit()
    return


if __name__ == '__main__':
    main()


