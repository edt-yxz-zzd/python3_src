#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/show_chars5block.py


nn_ns.app.show_chars5block
py -m nn_ns.app.debug_cmd   nn_ns.app.show_chars5block -x
py -m nn_ns.app.doctest_cmd nn_ns.app.show_chars5block:__doc__
py_adhoc_call   nn_ns.app.show_chars5block   @f
from nn_ns.app.show_chars5block import *
py -m nn_ns.app.show_chars5block 16 "0x30:0x3A;0x41:0x5B,0x61:0x7B"
py -m nn_ns.app.show_chars5block 16 "0x3400:0xA000"
py -m nn_ns.app.show_chars5block 16 "0x3400:0x4DC0;0x4DC0:0x4E00;0x4E00:0xA000" -o /sdcard/0my_files/tmp/out4py/nn_ns.app.show_chars5block..0x3400-0xA000.out.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.app.show_chars5block..0x3400-0xA000.out.txt

view ../../python3_src/nn_ns/CJK/cjk_subsets/hanzi.py
view ../../python3_src/seed/text/charset_filter.py
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__Blocks_txt.py.out.ver13_0.txt
#基本面:汉字区:归并区/归一区/统一区
,(0x3400, 0x4dc0)
: 'CJK Unified Ideographs Extension A'
,(0x4e00, 0xa000)
: 'CJK Unified Ideographs'

#基本面:汉字区:兼容区
,(0x3300, 0x3400)
: 'CJK Compatibility'
,(0xf900, 0xfb00)
: 'CJK Compatibility Ideographs'
,(0xfe30, 0xfe50)
: 'CJK Compatibility Forms'

#高位面:汉字区:归并区
,(0x20000, 0x2a6e0)
: 'CJK Unified Ideographs Extension B'
,(0x2a700, 0x2b740)
: 'CJK Unified Ideographs Extension C'
,(0x2b740, 0x2b820)
: 'CJK Unified Ideographs Extension D'
,(0x2b820, 0x2ceb0)
: 'CJK Unified Ideographs Extension E'
,(0x2ceb0, 0x2ebf0)
: 'CJK Unified Ideographs Extension F'
,(0x30000, 0x31350)
: 'CJK Unified Ideographs Extension G'

#高位面:汉字区:兼容区
,(0x2f800, 0x2fa20)
: 'CJK Compatibility Ideographs Supplement'


#]]]'''
__all__ = r'''
main
    show_chars5block
    parse_str2rngss_
        parse_str2rngs_

'''.split()#'''
__all__
from seed.data_funcs.rngs import make_Ranges
from seed.tiny_.check import check_int_ge
from itertools import islice
from ast import literal_eval

def show_chars5block(fout, num_chars_per_line, rngs, /):
    check_int_ge(1, num_chars_per_line)
    it = make_Ranges(rngs).iter_ints()
    it = map(chr, it)
    while 1:
        s = islice(it, num_chars_per_line)
        s = ''.join(s)
        if not s:
            break
        print(s, file=fout)

def parse_str2rngss_(s, /):
    return [parse_str2rngs_(t) for t in s.split(';')]
def parse_str2rngs_(s, /):
    def __():
        for t in s.split(','):
            begin, sep, end = t.partition(':')
            if not sep: raise ValueError('bad format')
            begin = literal_eval(begin)
            end = literal_eval(end)
            check_int_ge(0, begin)
            check_int_ge(begin, end)
            yield (begin, end)
    return [*__()]
################8*2
################################16*2
def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='show chars in given rngs'
        , epilog=r'''
py -m nn_ns.app.show_chars5block 16 "0x30:0x3A;0x41:0x5B,0x61:0x7B"
py -m nn_ns.app.show_chars5block 16 "0x3400:0xA000"
py -m nn_ns.app.show_chars5block 16 "0x3400:0x4DC0;0x4DC0:0x4E00;0x4E00:0xA000" -o /sdcard/0my_files/tmp/out4py/nn_ns.app.show_chars5block..0x3400-0xA000.out.txt

'''#'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('num_chars_per_line', type=int
                        , default=16
                        , help='max size per line')
    parser.add_argument('rngss', type=str
                        #, required=True
                        , help='=>[[(begin,end)]] #e.g: "0x30:0x3A,0x41:0x5B,0x61:0x7B;0x3400:0xA000" #";"=>sepline')
    parser.add_argument('-sl', '--sepline', type=str
                        , default='#'*8
                        , help='sepline per ";"')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    force = args.force
    omode = 'wt' if args.force else 'xt'
    oencoding = args.oencoding
    oencoding = 'utf8' if not oencoding else oencoding
    num_chars_per_line = args.num_chars_per_line
    check_int_ge(1, num_chars_per_line)
    sepline = args.sepline

    rngss = parse_str2rngss_(args.rngss)
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        for rngs in rngss:
            if not rngs is rngss[0]:
                print(sepline, file=fout)
            show_chars5block(fout, num_chars_per_line, rngs)
if __name__ == "__main__":
    main()


__all__
from nn_ns.app.show_chars5block import *
