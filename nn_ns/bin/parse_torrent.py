
r'''
# http://www.bittorrent.org/beps/bep_0003.html
# All strings in a .torrent file that contains text must be UTF-8 encoded.
# below example 'path' is MD5 # may not be MD5
# 'piece' must be SHA1
# 'path' = [dir, subdir, subsubdir, ..., basename] # must nonempty!

convert torrent file to dict:
{'announce': 'udp://tracker.openbittorrent.com:80',
 'announce-list': [['udp://tracker.openbittorrent.com:80'],
                   ...
                  ],
 'creation date': 1525087424,
 'info': {'files': [{'length': 3627254,
                     'path': ['00adeb502fd2f3f80b113ade57191167']},
                     ...
                   ],
          'name': '2213000',
          'piece length': 4194304,
          'pieces': ['dd9972a6ee393d2b54abe373bac0ae02e64a8d13',
                     ...
                    ]
 'nodes': [['router.bittorrent.com', 6881],
           ...
          ]
}

example:
    py -m nn_ns.bin.parse_torrent r_2213000.torrent -pp > r_2213000.torrent.txt
'''
epilog_str = __doc__

__all__ = '''
    parse_torrent
    parse_torrent__file
    '''.split()

from torrent_parser import TorrentFileParser
from seed.io.may_open import may_open_stdout
from pprint import pprint
import sys
from seed.math.floor_ceil import ceil_div

def print_err(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def parse_torrent__file(fin, *, encoding):
    # -> ordered_dict_
    return TorrentFileParser(fin, use_ordered_dict=True).parse()
def parse_torrent(path_or_fin, *, encoding):
    # -> ordered_dict_
    # path_or_fin is a binary file
    # but string inside it need a encoding to decode
    # default: utf8
    if hasattr(path_or_fin, 'readable'):
        fin = path_or_fin
        ordered_dict_ = parse_torrent__file(fin, encoding=encoding)
    else:
        path = path_or_fin
        with open(path, 'rb') as fin:
            ordered_dict_ = parse_torrent__file(fin, encoding=encoding)

    info = ordered_dict_['info']
    total_bytes = sum(file_info['length'] for file_info in info['files'])
    piece_length = info['piece length']
    num_pieces = len(info['pieces'])
    #fake_num_pieces = sum(ceil_div(file_info['length'], piece_length) for file_info in info['files'])
    try:
        #assert fake_num_pieces == num_pieces
        assert ceil_div(total_bytes, piece_length) == num_pieces
        '''
        r_2213000.torrent
        http://libgen.io/libgen/repository_torrent/r_2213000.torrent
        #############
        total = 21526239267
        ceil_div(total, piece_length) = 5133
        num_pieces = 5133
        fake_num_pieces = 5682
        '''
    except:
        print_err('total_bytes =', total_bytes)
        print_err('ceil_div(total_bytes, piece_length) =', ceil_div(total_bytes, piece_length))
        print_err('num_pieces =', num_pieces)
        print_err('fake_num_pieces =', fake_num_pieces)
        raise
    return ordered_dict_



def main(argv=None):
    import argparse
    import sys

    parser = argparse.ArgumentParser(
                description='convert torrent file to dict'
                , epilog=epilog_str
                , formatter_class=argparse.RawDescriptionHelpFormatter
                )
    parser.add_argument('input', type=str
                        , help='path to the input torrent file')
    parser.add_argument('-ie', '--input_encoding', type=str
                        , default='utf8'
                        , help='encoding to strings in input file')
    parser.add_argument('-pp', '--pretty_print', action='store_true'
                        , default=False
                        , help='pretty print output')

    parser.add_argument('-o', '--output', type=str
                        , default=None
                        , help='output file path')
    parser.add_argument('-oe', '--output_encoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('--mode', choices='exclusive append overwrite'.split()
                        , default='exclusive'
                        , help='mode for open output file')

    args = parser.parse_args()
    iencoding = args.input_encoding
    result = parse_torrent(args.input, encoding=iencoding)
    #print_err('piece length =', result['info']['piece length'])
    #print_err('len(pieces) =', len(result['info']['pieces']))


    if args.pretty_print:
        # pprint
        def xprint(obj, *, file):
            pprint(obj, stream=file)
    else:
        # print
        def xprint(obj, *, file):
            print(obj, file=file)

    oencoding = args.output_encoding
    mode = {'exclusive':'x', 'append':'a', 'overwrite':'w'}[args.mode]
    with may_open_stdout(args.output, mode+'t', encoding=oencoding) as fout:
        xprint(result, file=fout)

    parser.exit(0)
    return 0

if '__main__' == __name__:
    main()

