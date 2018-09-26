
r'''
see: parse_torrent.py

# below 'file_path' means 'files::path' inside torrent file
convert torrent file to another torrent file with selected file_paths only

useless?
    https://superuser.com/questions/483285/how-to-edit-the-list-of-files-to-download-in-a-torrent-file
    http://torrenteditor.com/faq.php

    change 'info' ==>> change 'info_hash'
        This makes it a different .torrent file
    'info_hash' is used to identify .torrent file
        if 'info_hash' not matched, file/piece are not matched, too.
'''

__all__ = '''
    filter_torrent_ex
    '''.split()
from torrent_parser import BEncoder #, TorrentFileCreator
from .parse_torrent import parse_torrent
from seed.for_libs.for_os_path.split_path_into_parts import \
    split_path_into_parts
#from seed.io.may_open import may_open_stdout
from logging import warning
warning(DeprecationWarning, 'the module is useless, since change the info_hash; but we can use it to detect which file_paths are not in the input torrent file')

def filter_torrent_ex(path_or_fin, selected_file_paths, *, encoding):
    # -> (bytes, file_paths_inside_output_torrent::set<str>)
    # input selected_file_paths :: Iter str
    # encoding - used to decode/encode string inside torrent file
    selected_file_paths = {tuple(split_path_into_parts(path)) : path
                            for path in selected_file_paths}
    #now selected_file_paths :: Set<Tuple<str>>
    file_paths_inside_output_torrent = set()

    dict_ = parse_torrent(path_or_fin, encoding=encoding) # ordered dict
    '''
 'info': {'files': [{'length': 3627254,
                     'path': ['00adeb502fd2f3f80b113ade57191167']},
                     ...
                   ],
    '''
    file_infos = dict_['info']['files']
    #new_file_infos = []
    for i in range(len(file_infos)):
        file_info = file_infos[i]
        assert len(file_info) == 2
        file_path = tuple(file_info['path'])
        if file_path in selected_file_paths:
            #new_file_infos.append(file_info)
            file_paths_inside_output_torrent.add(selected_file_paths[file_path])
            file_info['path'].insert(0, 'selected')
        else:
            file_info['path'].insert(0, 'not_selected')

    #dict_['info']['files'] = new_file_infos
    result = BEncoder(dict_, encoding=encoding).encode()
    assert type(result) is bytes
    return result, file_paths_inside_output_torrent


def main(argv=None):
    import argparse, sys

    parser = argparse.ArgumentParser(
                description='filter torrent file with selected file_paths only'
                , epilog='''
classify files:
    selected files inside subfolder "selected"
    others files inside subfolder "not_selected"
example:
    py -m nn_ns.bin.parse_torrent r_2213000.torrent -pp > r_2213000.torrent.txt
    py -m nn_ns.bin.filter_torrent -i r_2213000.torrent -o selected.torrent -ps db8a8ec0aac7b304567aa68775f613b0 102d4e981ef87ad6e3b77d8ef854d3f2
    py -m nn_ns.bin.parse_torrent selected.torrent -pp > selected.torrent.txt
'''
                , formatter_class=argparse.RawDescriptionHelpFormatter
                )
    parser.add_argument('-i', '--input', type=str
                        , required=True
                        , help='path to the input torrent file')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='encoding to strings in input/output file')
    parser.add_argument('-o', '--output', type=str
                        , required=True
                        , help='path to output torrent file')
    parser.add_argument('--mode', choices='exclusive append overwrite'.split()
                        , default='exclusive'
                        , help='mode for open output file')

    parser.add_argument('-ps', '--file_paths', type=str
                        , nargs='*'
                        , required=True
                        , default=[]
                        , help='selected file paths to export to the output torrent file')


    args = parser.parse_args()
    encoding = args.encoding
    paths = set(args.file_paths)
    result, output_paths = filter_torrent_ex(args.input, paths, encoding=encoding)
    assert type(result) is bytes
    assert type(output_paths) is set
    path_not_inside = paths - output_paths
    if path_not_inside:
        print(path_not_inside, file=sys.stderr)


    mode = {'exclusive':'x', 'append':'a', 'overwrite':'w'}[args.mode]
    #with may_open_stdout(args.output, mode+'b', encoding=None) as fout:
    with open(args.output, mode+'b', encoding=None) as fout:
        fout.write(result)

    parser.exit(0)
    return 0

if '__main__' == __name__:
    main()

