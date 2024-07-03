#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/unique_and_sort_chars.py


py -m nn_ns.app.debug_cmd   nn_ns.app.unique_and_sort_chars -x

py -m nn_ns.app.unique_and_sort_chars -t 987abcA
789Aabc

py -m nn_ns.app.unique_and_sort_chars -t 卝一我
一卝我
py -m nn_ns.app.unique_and_sort_chars -t 卝一我 -by gbk
卝我一

#]]]'''
__all__ = r'''
'''.split()#'''
__all__


def main(args=None, /):
    import argparse
    from io import StringIO
    from seed.io.may_open import may_open_stdin, may_open_stdout
    #from seed.io.savefile.unbuffered_growonly_dict_in_file import tabular_cached_calc
    from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
    from seed.io.may_open import open4w, open4w_err, open4r

    parser = argparse.ArgumentParser(
        description=''
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )

    parser.add_argument('-by', '--encoding4sort', type=str, default=None
            , help='sorted via bytes encoded: eg:gbk')


    parser.add_argument('-t', '--text', type=str, default=None
                        , help='used as input text directly')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    force = args.force
    iencoding = args.iencoding
    oencoding = args.oencoding
    iencoding = 'utf8' if not iencoding else iencoding
    oencoding = 'utf8' if not oencoding else oencoding

    may_ifname = args.input
    may_text = args.text
    if not may_text is None:
        txt0 = may_text
    else:
        txt0 = ''
    if (may_text is None or not may_ifname is None):
        with open4r(may_ifname, xencoding=iencoding) as fin:
            txt1 = fin.read()
    else:
        txt1 = ''
    txt = txt0 + txt1
    by = args.encoding4sort
    if by is None:
        _2 = ord
        _5 = chr
    else:
        def _2(ch, /):
            return ch.encode(by)
        def _5(bs, /):
            return bs.decode(by)
    s = ''.join(map(_5, sorted(set(map(_2, txt)))))

    may_ofname = args.output
    with open4w(may_ofname, force=force, xencoding=oencoding) as fout:
        print(s, file=fout)
if __name__ == "__main__":
    main()



__all__
