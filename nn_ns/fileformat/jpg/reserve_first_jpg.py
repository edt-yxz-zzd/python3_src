
'''
see also:
    nn_ns.bin.concat_files
    nn_ns.app.concat_files
    nn_ns.bin.truncate_and_move_to
    nn_ns.fileformat.zip.move_last_zip_to
    nn_ns.fileformat.jpg.reserve_first_jpg

    nn_ns.fileformat.zip.get_last_zip_begin
    nn_ns.fileformat.jpg.calc_first_jpg_size

'''

__all__ = '''
    reserve_first_jpg
    '''.split()

import os
from nn_ns.filedir.get_file_size import get_file_size
from nn_ns.bin.truncate_and_move_to import truncate_and_move_to
from .calc_first_jpg_size import calc_first_jpg_size



def reserve_first_jpg(src, dst, dst_mode):
    # first_jpg = src[first_jpg_size:]
    # dst += first_jpg
    # del src[first_jpg_size:]

    first_jpg_size = calc_first_jpg_size(src)
    truncate_and_move_to(first_jpg_size, src, dst, dst_mode)
    return

def _try():
    import os.path
    folder = r'E:\temp_output\concat files'
    a_jpg = folder + r'\a.jpg'
    a_zip = folder + r'\a.zip'
    jpg_zip = folder + r'\jpg+zip.jpg.zip'

    reserve_first_jpg(jpg_zip, folder+r'\_a.zip')
    os.rename(jpg_zip, folder+r'\_a.jpg')
#_try()




def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='reserve first_jpg and append tail bytes to another file')
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

    reserve_first_jpg(ifname, ofname, mode)


if __name__ == "__main__":
    main()

