
'''
see also:
    nn_ns.bin.concat_files
    nn_ns.app.concat_files
    nn_ns.bin.truncate_and_move_to
    nn_ns.fileformat.zip.move_last_zip_to

    nn_ns.fileformat.zip.get_last_zip_begin
    nn_ns.fileformat.jpg.calc_first_jpg_size

'''

__all__ = '''
    move_last_zip_to
    '''.split()

import os
from shutil import copyfileobj

from nn_ns.filedir.get_file_size import get_file_size
from nn_ns.bin.truncate_and_move_to import truncate_and_move_to
from .get_last_zip_begin import get_last_zip_begin



def move_last_zip_to(src, dst, dst_mode):
    # src -= last_zip
    # dst += last_zip
    #
    #OR:
    # last_zip = src[last_zip_begin:]
    # dst += last_zip
    # del src[last_zip_begin:]

    last_zip_begin = get_last_zip_begin(src)
    truncate_and_move_to(last_zip_begin, src, dst, dst_mode)
    return

    if not (dst_mode in 'xaw' and len(dst_mode)==1): raise ValueError(f'dst_mode={dst_mode!r} not in "xaw"')
    dst_mode = dst_mode+'b'

    #last_zip_size = get_last_zip_size(src)
    #src_size = get_file_size(src)
    last_zip_begin = get_last_zip_begin(src)

    with open(dst, dst_mode) as fout, open(src, 'rb') as fin:
        #fin.seek(-last_zip_size, os.SEEK_END)
        fin.seek(last_zip_begin)
        copyfileobj(fin, fout)

    os.truncate(src, last_zip_begin)
    return


def _try():
    import os.path
    folder = r'E:\temp_output\concat files'
    a_jpg = folder + r'\a.jpg'
    a_zip = folder + r'\a.zip'
    jpg_zip = folder + r'\jpg+zip.jpg.zip'

    move_last_zip_to(jpg_zip, folder+r'\_a.zip')
    os.rename(jpg_zip, folder+r'\_a.jpg')
#_try()


def f():
    import os.path
    folder = r'E:\temp_output\concat files'
    a_jpg = folder + r'\a.jpg'
    a_zip = folder + r'\a.zip'
    jpg_zip = folder + r'\jpg+zip.jpg.zip'

    for fname in [a_jpg, a_zip, jpg_zip]:
        sz = get_file_size(fname)
        print(fname, sz)
    assert get_file_size(jpg_zip) == get_file_size(a_jpg) + get_file_size(a_zip)

    print(get_last_zip_size(jpg_zip))
    r'''
        E:\temp_output\concat files\a.jpg 32521
        E:\temp_output\concat files\a.zip 32797
        E:\temp_output\concat files\jpg+zip.jpg.zip 65318
        [b'PK\x05\x06', 0, 0, 2, 2, 183, 32592, 0, b'', 65296]
    '''




def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='move out last_zip and append to another file')
    parser.add_argument('-i', '--input', type=str, required=True
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, required=True
                        , help='output file path')
    parser.add_argument('--mode', choices='exclusive append overwrite'.split()
                        , default='exclusive'
                        , help='mode for open output file')

    args = parser.parse_args()
    mode = args.mode
    mode = {'exclusive':'x', 'append':'a', 'overwrite':'w'}[mode]
    ifname = args.input
    ofname = args.output

    move_last_zip_to(ifname, ofname, mode)


if __name__ == "__main__":
    main()

