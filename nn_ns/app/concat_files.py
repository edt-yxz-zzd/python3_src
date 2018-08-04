
'''
see also:
    nn_ns.bin.concat_files
    nn_ns.app.concat_files
    nn_ns.fileformat.zip.move_last_zip_to
'''

from nn_ns.bin.concat_files import concat_files

def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='concat files')
    parser.add_argument('fnames', type=str, nargs='*'
                        , help='input file paths')
    parser.add_argument('-o', '--output', type=str, required=True
                        , help='output file path')
    parser.add_argument('--mode', choices='exclusive append overwrite'.split()
                        , default='exclusive'
                        , help='mode for open output file')

    args = parser.parse_args()
    mode = args.mode
    mode = {'exclusive':'x', 'append':'a', 'overwrite':'w'}[mode]
    ofname = args.output
    ifnames = args.fnames

    concat_files(ofname, ifnames, mode=mode)




if __name__ == "__main__":
    main()

