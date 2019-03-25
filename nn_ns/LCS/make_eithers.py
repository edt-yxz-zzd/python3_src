
__all__ = '''
    make_eithers
    '''.split()

#from seed.io.iter_reads import iter_reads
#from nn_ns.LCS.longest_common_subsequence_problem import LCS_RowByRow__common_elements
from nn_ns.LCS.longest_common_subsequence_problem__O_NNlogN import calc_LCS__OlogNRlogN


def make_eithers(txt1, txt2):
    eithers = [] # [diff|same] # [Either (str, str) str]
    lcs = calc_LCS__OlogNRlogN(txt1, txt2)
    def push(sames, diff):
        same = ''.join(sames)
        sames.clear()
        if same: eithers.append(same)
        eithers.append(diff)
    i1 = i2 = 0
    sames = []
    for ch in lcs:
        i1_ = txt1.index(ch, i1)
        i2_ = txt2.index(ch, i2)
        if i1 == i1_ and i2 == i2_:
            pass
        else:
            diff = (txt1[i1:i1_], txt2[i2:i2_])
            push(sames, diff)
        sames.append(ch)
        i1 = i1_+1
        i2 = i2_+1
    else:
        diff = (txt1[i1:], txt2[i2:])
        push(sames, diff)
        if diff == ('', ''):
            _diff = eithers.pop()
            assert diff is _diff
    return eithers

def main0():
    fname1 = '东周列国志.txt'
    encoding1 = 'gb18030'
    fname2 = '东周列国志 (2).txt'
    encoding2 = 'utf8'


    with open(fname1, encoding=encoding1) as fin1, open(fname2, encoding=encoding2) as fin2:
        txt1 = fin1.read()
        txt2 = fin2.read()
    eithers = make_eithers(txt1, txt2)
    for either in eithers:
        print(repr(either))


def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='compare 2 files, like cmp/diff'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str
                        , nargs=2, required=True
                        , help='the 2 input file paths')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--default_encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default=None
                        , help='output file encoding')
    parser.add_argument('-ie1', '--iencoding1', type=str
                        , default=None
                        , help='1st input file encoding')
    parser.add_argument('-ie2', '--iencoding2', type=str
                        , default=None
                        , help='2nd input file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    default_encoding = args.default_encoding
    omode = 'wt' if args.force else 'xt'

    def f(e):
        return default_encoding if e is None else e
    oencoding = f(args.oencoding)
    iencoding1 = f(args.iencoding1)
    iencoding2 = f(args.iencoding2)

    ifname1, ifname2 = args.input
    with open(ifname1, 'rt', encoding=iencoding1) as fin1, open(ifname2, 'rt', encoding=iencoding2) as fin2:
        txt1 = fin1.read()
        txt2 = fin2.read()

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        eithers = make_eithers(txt1, txt2)
        for either in eithers:
            print(repr(either), file=fout)


if __name__ == "__main__":
    main()


