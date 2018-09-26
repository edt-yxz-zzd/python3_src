
'''
cmd.exe encoding:
    chcp 936    # gbk
    chcp 65001  # utf8
    chcp 54936  # gb18030


as_file
    import argparse, sys
    from seed.io.as_file import as_file, curry_file
    from seed.for_libs.parent_argparser import \
        input_file_parent_argparser, input_encoding_parent_argparser \
        , output_file_parent_argparser, output_encoding_parent_argparser
        , output_open_mode_parent_argparser, open_mode_to_pyopen_arg

    parents = [input_file_parent_argparser, input_encoding_parent_argparser
            , output_file_parent_argparser, output_encoding_parent_argparser
            , output_open_mode_parent_argparser
            ]
    obinary = ...
    ibinary = ...
    parser = argparse.ArgumentParser(parents=parents)
    parser.add_argument(...)
    args = parser.parse_args()


    omode = open_mode_to_pyopen_arg(args.output_open_mode, binary=obinary)
    imode = 'rb' if ibinary else 'r'
    def do(fin):
        def do(fout):
            ...
        return do
    fi = curry_file(args.input_file, imode)
    fo = curry_file(args.output_file, omode)
    fo(fi(do))
    parser.exit(0)

    def read_fin(fin):
        def write_fout(fout):
            ...
        as_file(write_fout, args.output_file, omode, encoding=args.output_encoding)
    as_file(read_fin, args.input_file, 'r', encoding=args.input_encoding)
    parser.exit(0)

'''

import argparse, sys
from abc import abstractmethod
class MakeParentArgParser:
    @abstractmethod
    def __add_argument__(self, parser):
        # return None
        # modify parser
        raise NotImplementedError
    def __new_argparser__(self):
        # create new parser
        parser = argparse.ArgumentParser(add_help=False)
        return parser
    def new(self):
        parser = type(self).__new_argparser__(self)
        r = type(self).__add_argument__(self, parser)
        if r is not None:
            raise TypeError('MakeParentArgParser.__add_argument__'
                            ' should return None instead of {}'
                            .format(type(r)))
        return parser

class AddOutputFile(MakeParentArgParser):
    def __add_argument__(self, parser):
        parser.add_argument('-o', '--output_file', type=str
                            , default = sys.stdout
                            , help='output file name')
output_file_parent_argparser = AddOutputFile().new()


class AddOutputEncoding(MakeParentArgParser):
    def __add_argument__(self, parser):
        parser.add_argument('-oe', '--output_encoding', type=str
                            , default = 'utf-8'
                            , help='output file encoding')
output_encoding_parent_argparser = AddOutputEncoding().new()

# OpenMode
APPENDING = 'APPENDING'
EXCLUSIVE = 'EXCLUSIVE'
TRUNCATING = 'TRUNCATING'
OpenModes = (EXCLUSIVE, APPENDING, TRUNCATING)
_open_mode2pyopen_arg = dict(APPENDING='a', EXCLUSIVE='x', TRUNCATING='w')
def open_mode_to_pyopen_arg(mode, binary=False):
    tail = 'b' if binary else ''
    mode = _open_mode2pyopen_arg[mode] + tail
    return mode
class AddOutputOpenMode(MakeParentArgParser):
    def __add_argument__(self, parser):
        parser.add_argument('-oom', '--output_open_mode', choices=OpenModes
                            , default = EXCLUSIVE
                            , help='output file open mode')
output_open_mode_parent_argparser = AddOutputOpenMode().new()




class AddInputFilePlc(MakeParentArgParser):
    def __add_argument__(self, parser):
        parser.add_argument('input_file', type=str
                            , default = sys.stdin
                            , help='input file name')
input_file_plc_parent_argparser = AddInputFilePlc().new()



class AddInputFile(MakeParentArgParser):
    def __add_argument__(self, parser):
        parser.add_argument('-i', '--input_file', type=str
                            , default = sys.stdin
                            , help='input file name')
input_file_parent_argparser = AddInputFile().new()


class AddInputEncoding(MakeParentArgParser):
    def __add_argument__(self, parser):
        parser.add_argument('-ie', '--input_encoding', type=str
                            , default = 'utf-8'
                            , help='input file encoding')
input_encoding_parent_argparser = AddInputEncoding().new()




