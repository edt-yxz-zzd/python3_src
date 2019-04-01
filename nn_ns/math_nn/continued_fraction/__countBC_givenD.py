
r'''

------------------
result:
    D with max ratio_total/ratio_small:
    for D <= 1000:
        3 > 7 > 13 > ...
        * ratio_small:
            3 > 7 > 13 > 19 > 21 > 22 > 46 > 61 > 94 > 109 > ...
        * ratio_total:
            3 > 7 > 13 > 21 > 24 > 34 > 37 > 46 > 76 > 97 > 109 > ...
    for 800 <= D <= 2000:
        * ratio_small:
            919 > 991 > 1039 > ...
        * ratio_total:
            889 > 1009 > ...
------------------

refine [C>0][B>0][C+B > floor_sqrt(D) >= B][floor_sqrt(D) >= C-B]
    by [C `divs` D - B^2]!

see:
    continued_fraction_digits_of_quadratic_surd.py
    "NOTE/math/continued fractoin/[20190331]compute_about_continued_fraction_of_quadratic_irrational.txt"
    "NOTE/math/continued fractoin/[20190331]proof_about_continued_fraction_of_quadratic_irrational.txt"

[[sqrt(D) is irrational][x = (B+sqrt(D))/C][x is reduced_quadratic_surd
][C `divs` D - B^2]]:
    [C>0][B>0][C+B > floor_sqrt(D) >= B][floor_sqrt(D) >= C-B]!
    [C `divs` D - B^2]!
    [D' == D]
    [0 < B <= R]:
        [C-B <= R < C+B]
        [R-B < C <= R+B]
        [total C = 2*B]
    [total (B,C) = SUM total C {B<-1..R} = SUM 2*B {B<-1..R} = R*(1+R)]

    draw on x=B-y=C-plane
    let R = floor_sqrt(D) # the "*" point on C-axis and B-axis
    all possibles (B,C) are in the triangle area:
        total (B,C) == R*(R+1)
        len(periodic_digits)
            <= total (B,C)
            <= R*(R+1)
        len(periodic_digits) <= floor_sqrt(D)*(floor_sqrt(D)+1)

    C
    ^
    |
    |
    |   C-B=R/
    |       /
    |      /
    |     /|
    |    / | B=R
    |   /  |
    |  /   |
    | /    |
    |/     |
    * HERE |
    |\     |
    | \    |
    |  \   |
    |   \  |
    |    \ |
    |     \|
    -------*-------------------------------------> B
    |       \
    |        \
    |         \C+B == R






'''


from fractions import Fraction
from collections import namedtuple, OrderedDict
from ..floor_sqrt import floor_sqrt
from .continued_fraction_digits_of_quadratic_surd import (
    list_split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ
    ,_split_iter_cut_maybes
    ,_iter_cut_maybe_continued_fraction_digits_of_quadratic_surd_withBC__BCD
    )




def iter_Ds2iter_D_BCs(iter_Ds):
    'Iter D -> Iter (D, [(B,C)])'
    for D in iter_Ds:
        floor_sqrtD = floor_sqrt(D)
        if floor_sqrtD**2 == D:
            continue
        BCs = tuple(iter_BCs(D=D, floor_sqrtD=floor_sqrtD))
        yield (D, BCs)
def iter_BCs(*, D, floor_sqrtD):
    '''D -> floor_sqrtD -> Iter (B,C)
precondition:
    [D>0][sqrt(D) is irrational]
'''
    assert floor_sqrtD**2 < D < (floor_sqrtD+1)**2

    R = floor_sqrtD
    #[0 < B <= R][R-B < C <= R+B]
    _remain = R*(R+1)
    for B in range(0+1, R+1):
        for C in range(R-B+1, R+B+1):
            _remain -= 1
            if (D-B**2)%C == 0:
                yield (B, C)
    assert _remain == 0
    return

def iter_BCs_in_same_period(*, B, D, C, floor_sqrtD):
    it = _iter_cut_maybe_continued_fraction_digits_of_quadratic_surd_withBC__BCD(B=B,D=D,C=C, floor_sqrtD=floor_sqrtD)
    _, it = _split_iter_cut_maybes(it)
    for B, C, d in it:
        yield B, C
def length_of_period__BDC(*, B, D, C):
    (non_periodic_digits, periodic_digits
    ) = list_split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ(
            P=B, N=D, Q=C)
    return len(periodic_digits)

def split_BCs(D, BCs):
    floor_sqrtD = floor_sqrt(D)
    BCs = set(BCs)
    BCss = []
    while BCs:
        B, C = BC = BCs.pop()
        L = length_of_period__BDC(B=B, D=D, C=C)
        it = iter_BCs_in_same_period(B=B, D=D, C=C, floor_sqrtD=floor_sqrtD)
        ls = list(it)
        assert ls
        try:
            assert ls[0] == BC
        except:
            print(ls[0], BC)
            print(ls)
            raise
        for BC in ls[1:]:
            BCs.remove(BC)

        i = ls.index(min(ls))
        ls = ls[i:] + ls[:i]
        assert len(ls) == L
        BCss.append(ls)

    BCss.sort()
    return BCss


D_totalBCs_BCss_Triple = namedtuple('D_totalBCs_BCss_Triple', 'D totalBCs BCss'.split())
Info = namedtuple('Info', '''
        D_totalBCs_BCss_triple
        sort_keys
    '''.split()
    )
SortKeys = namedtuple('SortKeys', '''
        ratio_total
        ratio_small
        ratio_total_floor_sqrt
        ratio_small_floor_sqrt
    '''.split()
    )

def show_info(info, *, print):
    triple = info.D_totalBCs_BCss_triple
    D, totalBCs, BCss = (triple.D, triple.totalBCs, triple.BCss)
    sort_keys = info.sort_keys
    ratio_total = sort_keys.ratio_total
    ratio_small = sort_keys.ratio_small
    ratio_total_floor_sqrt = sort_keys.ratio_total_floor_sqrt
    ratio_small_floor_sqrt = sort_keys.ratio_small_floor_sqrt

    print(f'D={D}, total={totalBCs}, ratio_total={ratio_total}, ratio_small={ratio_small}, ratio_total_floor_sqrt={ratio_total_floor_sqrt}, ratio_small_floor_sqrt={ratio_small_floor_sqrt}:')
    #print(f'    {sort_keys!r}')

    for i, small_BCs in enumerate(BCss):
        L = len(small_BCs)
        print(f'    len={L}, BCss[{i}]={small_BCs}')
    print()

def noshow_info(triple, *, print):
    pass

def eval_info_forDs(iter_Ds, show_eachD:bool):
    # -> [Info]
    #print('see: continued_fraction_digits_of_quadratic_surd.py')
    it = iter_Ds2iter_D_BCs(iter_Ds)

    maybe_show_info = show_info if show_eachD else noshow_info

    # infos :: [((D, BCs, BCss), (ratio_total, ratio_small))]
    infos = []
    for D, BCs in it:
        #print(f'D={D}, total={len(BCs)}:')
        #print(f'    BCs={BCs}')

        BCss = split_BCs(D, BCs)
        total = len(BCs)
        small = max(map(len, BCss))
        floor_sqrtD = floor_sqrt(D)

        ratio_total = Fraction(total, D)
        ratio_small = Fraction(small, D)
        ratio_total_floor_sqrt = Fraction(total, floor_sqrtD)
        ratio_small_floor_sqrt = Fraction(small, floor_sqrtD)

        triple = D_totalBCs_BCss_Triple(D=D, totalBCs=len(BCs), BCss=BCss)
        #ratios = ratio_total, ratio_small
        sort_keys = SortKeys(ratio_total=ratio_total
                            ,ratio_small=ratio_small
                            ,ratio_total_floor_sqrt=ratio_total_floor_sqrt
                            ,ratio_small_floor_sqrt=ratio_small_floor_sqrt
                            )
        info = Info(D_totalBCs_BCss_triple=triple, sort_keys=sort_keys)
        infos.append(info)
        #maybe_show_triple(triple)
        maybe_show_info(info, print=print)
    return infos

def sort_then_show_infos(infos, *
    , sort_attrs:[str], maybe_show_first_n_infos:int, print):
    infos = list(infos)
    def show_infos(infos):
        #for _ in map(show_info, infos): pass
        infos = infos[:maybe_show_first_n_infos]

        Ds = [info.D_totalBCs_BCss_triple.D for info in infos]
        print(f'    Ds={Ds}')
        print()

        for info in infos:
            show_info(info, print=print)

    sep = '='*60
    for sort_attr in sort_attrs:
        print(sep)
        print(f'max {sort_attr} first')
        infos.sort(key=lambda info:-getattr(info.sort_keys, sort_attr))
        show_infos(infos)
        print()
    return

    sep = '='*60
    print(sep)
    print(f'max ratio_small first')
    infos.sort(key=lambda info:-info.ratio_small)
    show_infos(infos)

    print(sep)
    print(f'max ratio_total first')
    infos.sort(key=lambda info:-info.ratio_total)
    show_infos(infos)


def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='show D, [BCs]'
        , epilog='''
B,D,C
    see: continued_fraction_digits_of_quadratic_surd.py

#choices
ratio_small
    =max{len(BC_orbit)}=max{len(periodic_digits)}/D
ratio_total
    =len(all_BCs)/D
ratio_small_floor_sqrt
    =max{len(periodic_digits)}/floor_sqrt(D)
ratio_total_floor_sqrt
    =len(all_BCs)/floor_sqrt(D)'
'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )

    choices = '''
        ratio_small
        ratio_total
        ratio_small_floor_sqrt
        ratio_total_floor_sqrt
        '''.split()
    parser.add_argument('sort_attrs', choices=choices
                        , default=['ratio_small']
                        , nargs='*'
                        , help='sorted by this attr; see whole help'
                        )
    parser.add_argument('-Ds', '--input_Ds_directly'
                        , type=int
                        , default=None
                        , nargs='+'
                        , help='input Ds directly; override from/to/step (firstD/lastD/stepD)'
                        )
    parser.add_argument('--exprD', type=str, default=None
                        , help='python expr for D: lambda n:{exprD}; range of n = input_Ds_directly or range(from, to, step); override them')
    parser.add_argument('-to', '--lastD', type=int, default=30
                        , help='last D')
    parser.add_argument('-from', '--firstD', type=int, default=2
                        , help='first D')
    parser.add_argument('-step', '--stepD', type=int, default=1
                        , help='step for D: D <- range(firstD, lastD, stepD)')
    parser.add_argument('-N', '--show_first_n_infos', type=int
                        , default=None
                        , help='show first n infos for each sort')
    parser.add_argument('--show_eachD', action='store_true'
                        , default = False
                        , help='show info for each D'
                        )


    args = parser.parse_args(args)
    #print(args.__dict__)
    print('args=', (sorted(args.__dict__.items())))

    if args.input_Ds_directly is not None:
        iter_Ds = iter(args.input_Ds_directly)
    else:
        firstD = args.firstD
        lastD = args.lastD
        stepD = args.stepD
        iter_Ds = range(firstD, lastD, stepD)

    if args.exprD is not None:
        exprD = args.exprD
        exprD = eval(f'lambda n: {exprD!s}', {}, {})
        iter_ns = iter_Ds
        iter_Ds = map(exprD, iter_ns)

    show_eachD = args.show_eachD
    infos = eval_info_forDs(iter_Ds, show_eachD=show_eachD)
    sort_then_show_infos(infos
                        ,sort_attrs=args.sort_attrs
                        ,maybe_show_first_n_infos=args.show_first_n_infos
                        ,print=print
                        )

if __name__ == "__main__":
    main()


r'''
list:
    # p= 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271
    2^p-1
        # p=2, 3, 5, 7, 11, 13
        3, 7, 31, 127, 2047, 8191, 131071, 524287
        #3, 7, 31, 127, 8191, 131071, 524287 # Mersenne
    2^p+1
        5, 9, 33, 129, 2049, 8193, 131073, 524289
    2^n-1
        3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535
    2^n+1
        3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535
    n^2-1
        3 8 15 24 35
        3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195, 224, 255, 288, 323, 360, 399, 440, 483, 528, 575, 624, 675, 728, 783, 840, 899, 960, 1023, 1088, 1155, 1224, 1295, 1368, 1443, 1520, 1599, 1680, 1763, 1848, 1935, 2024, 2115, 2208, 2303, 2400, 2499, 2600
    n^2+1
        5 10 17 26 37
        5, 10, 17, 26, 37, 50, 65, 82, 101, 122, 145, 170, 197, 226, 257, 290, 325, 362, 401, 442, 485, 530, 577, 626, 677, 730, 785, 842, 901, 962, 1025, 1090, 1157, 1226, 1297, 1370, 1445, 1522, 1601, 1682, 1765, 1850, 1937, 2026, 2117, 2210, 2305, 2402, 2501
    n^2+n-1
        5 11 19 29 41 55 71
    n^2+n
        6 12 20 30 42 56 72
    n^2+n+1
        7 13 21 31 43 57 73

pym __countBC_givenD.py -to 1000 -from 0 -N 40 > "__countBC_givenD.output[N=40][2to1000].txt"
pym __countBC_givenD.py -to 1000 -from 0 -N 40 ratio_small_floor_sqrt > "__countBC_givenD.output[N=40][2to1000][ratio_small_floor_sqrt].txt"

pym __countBC_givenD.py -Ds 3 7 31 127 8191 > "__countBC_givenD.output[3 7 31 127 8191].txt"

pym __countBC_givenD.py -Ds 2 3 5 7 11 13 --exprD "2**n-1" > "__countBC_givenD.output[2^p-1][2to13].txt"
pym __countBC_givenD.py -Ds 2 3 5 7 11 13 --exprD "2**n+1" > "__countBC_givenD.output[2^p+1][2to13].txt"
pym __countBC_givenD.py -from 2 -to 13 --exprD "2**n-1" > "__countBC_givenD.output[2^n-1][2to13].txt"
pym __countBC_givenD.py -from 2 -to 13 --exprD "2**n+1" > "__countBC_givenD.output[2^n+1][2to13].txt"
pym __countBC_givenD.py -from 2 -to 50 --exprD "n**2-1" > "__countBC_givenD.output[n^2-1][2to50].txt"
pym __countBC_givenD.py -from 2 -to 50 --exprD "n**2+1" > "__countBC_givenD.output[n^2+1][2to50].txt"
pym __countBC_givenD.py -from 2 -to 50 --exprD "n**2+n-1" > "__countBC_givenD.output[n^2+n-1][2to50].txt"
pym __countBC_givenD.py -from 2 -to 50 --exprD "n**2+n+1" > "__countBC_givenD.output[n^2+n+1][2to50].txt"
pym __countBC_givenD.py -from 2 -to 50 --exprD "n**2+n" > "__countBC_givenD.output[n^2+n][2to50].txt"

pym __countBC_givenD.py -to 3000 -from 2 > "__countBC_givenD.output[2to3000].txt"




A000668 Mersenne primes (of form 2^p - 1 where p is a prime).
3, 7, 31, 127, 8191, 131071, 524287, 2147483647, 2305843009213693951, 618970019642690137449562111, 162259276829213363391578010288127, 170141183460469231731687303715884105727

D=3, total=2, ratio_total=2/3, ratio_small=2/3:
    len=2, BCss[0]=[(1, 1), (1, 2)]

D=7, total=4, ratio_total=4/7, ratio_small=4/7:
    len=4, BCss[0]=[(1, 2), (1, 3), (2, 1), (2, 3)]

D=31, total=8, ratio_total=8/31, ratio_small=8/31:
    len=8, BCss[0]=[(1, 5), (4, 3), (5, 2), (5, 3), (4, 5), (1, 6), (5, 1), (5, 6)]

D=127, total=12, ratio_total=12/127, ratio_small=12/127:
    len=12, BCss[0]=[(6, 7), (8, 9), (10, 3), (11, 2), (11, 3), (10, 9), (8, 7), (6, 13), (7, 6), (11, 1), (11, 6), (7, 13)]
#12 = 2^2 * 3
D=8191, total=164, ratio_total=164/8191, ratio_small=164/8191:
#164 = 2^2 * 41
'''
