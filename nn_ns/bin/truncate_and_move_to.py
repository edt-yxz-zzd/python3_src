

__all__ = '''
    truncate_and_move_to
    '''.split()


from nn_ns.filedir.get_file_size import get_file_size


def truncate_and_move_to(length, src, dst, dst_mode):
    # last_block = src[length:]
    # dst += last_block
    # del src[length:]

    if not (length >= 0): raise ValueError(length)
    if not (dst_mode in 'xaw' and len(dst_mode)==1): raise ValueError(f'dst_mode={dst_mode!r} not in "xaw"')
    dst_mode = dst_mode+'b'

    src_size = get_file_size(src)
    with open(dst, dst_mode) as fout, open(src, 'rb') as fin:
        if length < src_size:
            fin.seek(length)
            copyfileobj(fin, fout)

    if length < src_size:
        os.truncate(src, length)
    return



def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='truncate src and append to dst')
    parser.add_argument('new_src_max_size', type=int
                        , help='max file size of input file after this cmd')
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
    length = args.new_src_max_size

    truncate_and_move_to(length, ifname, ofname, mode)


if __name__ == "__main__":
    main()

