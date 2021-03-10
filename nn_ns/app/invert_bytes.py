
r'''

py -m nn_ns.app.invert_bytes
e ../../python3_src/nn_ns/app/invert_bytes.py


py -m nn_ns.app.invert_bytes -a -i 王京示申一乂彐水.7z
py -m nn_ns.app.invert_bytes -a -i 王京示申一乂彐水.7z.inv
#'''



BLOCK_SIZE = 2**20
def mk_invert_bytes_table():
    msk = (2**8)-1
    bs1 = bytes(msk^i for i in range(2**8))
    bs2 = bytes(msk-i for i in range(2**8))
    bs3 = bytes(msk&~i for i in range(2**8))
    assert bs1 == bs2
    assert bs1 == bs3

    return bs1
TABLE = mk_invert_bytes_table()
assert TABLE[0] == 2**8-1
assert TABLE[1] == 2**8-2



def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='invert bytes of file'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-a', '--auto_name_output', action='store_true'
                        , default = False
                        , help='add/remove ".inv" to input fname for output fname')

    args = parser.parse_args(args)
    omode = 'wb' if args.force else 'xb'

    may_ifname = args.input
    may_ofname = args.output
    if (args.auto_name_output
        and may_ofname is None
        and may_ifname is not None
        ):
        ext = '.inv'
        if may_ifname.endswith(ext):
            #bug:may_ofname = may_ifname[-len(ext):]
            may_ofname = may_ifname[:-len(ext)]
        else:
            may_ofname = may_ifname + ext

    with may_open_stdin(may_ifname, 'rb', encoding=None) as fin:
        with may_open_stdout(may_ofname, omode, encoding=None) as fout:
            while 1:
                bs = fin.read(BLOCK_SIZE)
                if not bs: break
                bs = bs.translate(TABLE)
                fout.write(bs)

if __name__ == "__main__":
    main()






