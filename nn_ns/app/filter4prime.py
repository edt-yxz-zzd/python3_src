#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/filter4prime.py

源起:
    view script/搜索冫某进制表达数乊多种进制解读皆为素数.py
        十进制表达，高进制解读为素数，但 十进制解读不一定为素数


py -m nn_ns.app.filter4prime
py -m nn_ns.app.debug_cmd   nn_ns.app.filter4prime -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.filter4prime:__doc__ -ht # -ff -df



py -m nn_ns.app.filter4prime
    ^D
    # Ctrl+D => EOF
py -m nn_ns.app.filter4prime  -s
    <None>
py -m nn_ns.app.filter4prime  -s -1 0 1 2 3 4 5 6 7 8 9 10
2
3
5
7
echo -1 0 1 2 3 4 5 6 7 8 9 10 | py -m nn_ns.app.filter4prime
2
3
5
7
echo -1 0 1 2 3 4 5 6 7 8 9 10 | py -m nn_ns.app.filter4prime -s
    <None>
echo -1 0 1 2 3 4 5 6 7 8 9 10 | py -m nn_ns.app.filter4prime -s -i ''
2
3
5
7
echo -1 0 1 2 3 4 5 6 7 8 9 10 | py -m nn_ns.app.filter4prime -s 11 12 13 14 -i ''
11
13
2
3
5
7
filter4prime  -s -1 0 1 2 3 4 5 6 7 8 9 10
2
3
5
7


py_adhoc_call   nn_ns.app.filter4prime   @f
from nn_ns.app.filter4prime import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_
_max1 = is_prime__using_A014233_.upperbound
___end_mark_of_excluded_global_names__0___ = ...

def main(args=None, /):
    import argparse
    from seed.io.may_open import open4w, open4w_err, open4r

    parser = argparse.ArgumentParser(
        description='filter out nonprime numbers'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-s', '--ints', type=int, default=None, nargs='*'
                        , help='input ints via args instead of input_file')
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
    omode = 'wt' if args.force else 'xt'
    iencoding = args.iencoding
    oencoding = args.oencoding
    iencoding = 'utf8' if not iencoding else iencoding
    oencoding = 'utf8' if not oencoding else oencoding

    may_ints = args.ints

    may_ifname = args.input
    may_ofname = args.output

    def ints5ints_may_ipath_(may_ints, may_ifname, /):
        if may_ints:
            ints = may_ints
            yield from ints
        if may_ints is not None and may_ifname is None:
            return
        if may_ifname == '':
            may_ifname = None
        with open4r(may_ifname, xencoding=iencoding) as ifile:
            yield from ints5ifile_(ifile)
        return
    def ints5ifile_(ifile, /):
        for lineno, line in enumerate(ifile, 1):
            #print(lineno, ':', line, sep='', end='')
            yield from map(int, line.split())
    with open4w(may_ofname, force=force, xencoding=oencoding) as ofile:
        _ints = ints5ints_may_ipath_(may_ints, may_ifname)
        primes = filter(is_prime__using_A014233_, _ints)
        for p in primes:
            print(p, file=ofile)

if __name__ == "__main__":
    main()




__all__
from nn_ns.app.filter4prime import *
