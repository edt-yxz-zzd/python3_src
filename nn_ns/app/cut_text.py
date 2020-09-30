
r"""

mkdir ~/tmp/笔顺码分解
py -m nn_ns.app.cut_text -n 500 -re '^\s*$' -cs tail -ofmt '{0:0>4}.txt' -od ~/tmp/笔顺码分解 -i /storage/emulated/0/0my_files/笔顺码分解.txt

e ../../python3_src/nn_ns/app/cut_text.py
#"""


import re
from pathlib import PurePath, Path
from seed.iters.PeekableIterator import PeekableIterator

def cut_text(fin, *
        , force:bool, oencoding, odir, ofname_number_offset, ofname_fmt
        , max_sep_lines_per_ofile, sep_line_regex, sep_line_case:'head|tail'
        ):
    omode = 'wt' if force else 'xt'
    del force

    if type(max_sep_lines_per_ofile) is not int: raise TypeError
    elif not max_sep_lines_per_ofile >= 1: raise ValueError

    if sep_line_case == 'head':
        is_head_rex = True
    elif sep_line_case == 'tail':
        is_head_rex = False
    else:
        assert sep_line_case not in ('head', 'tail')
        raise ValueError(f"sep_line_case=={sep_line_case!r} not in ('head', 'tail')")
    assert hasattr(sep_line_regex, 'match')

    is_head_rex
    it = PeekableIterator(fin)
    assert ofname_fmt.format(0) != ofname_fmt.format(1)
    assert ofname_number_offset+1 != ofname_number_offset
    odir = Path(odir)
    if not odir.is_dir():
        raise NotADirectoryError(odir)


    if is_head_rex:
        #head rex
        def f(fout, it):
            w = fout.write
            number_of_sep_lines = 0
            line = it.read1()
            w(line)
            number_of_sep_lines += 1
            for line in it:
                assert number_of_sep_lines <= max_sep_lines_per_ofile
                if sep_line_regex.match(line):
                    #line is head of next file
                    number_of_sep_lines += 1
                    if number_of_sep_lines > max_sep_lines_per_ofile:
                        it.append_left(line)
                        break
                w(line)
    else:
        #tail rex
        def f(fout, it):
            w = fout.write
            number_of_sep_lines = 0
            for line in it:
                assert number_of_sep_lines < max_sep_lines_per_ofile
                w(line)
                if sep_line_regex.match(line):
                    #line is tail
                    number_of_sep_lines += 1
                    if number_of_sep_lines >= max_sep_lines_per_ofile:
                        break

    while not it.is_empty():
        ofname = ofname_fmt.format(ofname_number_offset)
        ofname_number_offset += 1
        ofpath = odir / ofname
        with open(ofpath, omode, encoding=oencoding) as fout:
            f(fout, it)


def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='cut text file into many text files by detect head/tail line for each output files'
        , epilog=r"""
usiing python.re.match #not search/fullmatch
    for search:
        r".*?{pattern}"
    for fullmatch:
        r"^{pattern}$"
#"""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-re', '--sep_line_regex', type=str, required=True
                        , help='python regex pattern for input line')
    parser.add_argument('-cs', '--sep_line_case', choices='head tail'.split(), required=True
                        , help='input line which match sep_line_regex is head/tail')

    parser.add_argument('-od', '--output_dir', type=str, required=True
                        , help='output dir path')
    parser.add_argument('-ofmt', '--output_file_name_fmt', type=str, default='{0}.txt'
                        , help="python str format of output file name; {0} for number_offset; eg, -ofmt '{0:0>4}.txt'")
    parser.add_argument('-oi', '--output_file_name_number_offset', type=str, default=0
                        , help='number_offset of output file name')
    parser.add_argument('-n', '--max_sep_lines_per_ofile', type=int, required=True
                        , help='max number of sep_lines per output_file')

    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        cut_text(fin
        , force=args.force
        , oencoding=encoding
        , odir=args.output_dir
        , ofname_number_offset=args.output_file_name_number_offset
        , ofname_fmt=args.output_file_name_fmt
        , sep_line_regex=re.compile(args.sep_line_regex)
        , sep_line_case=args.sep_line_case
        , max_sep_lines_per_ofile=args.max_sep_lines_per_ofile
        )

if __name__ == "__main__":
    main()


