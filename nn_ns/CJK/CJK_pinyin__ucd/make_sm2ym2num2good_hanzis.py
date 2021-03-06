
__all__ = '''
    sm2ym2num2good_hanzi_set
    sm2ym2num2good_hanzi_str
    '''.split()

from collections import defaultdict
from .hanzi2pinyins import hanzi2pinyins
from .normal_pinyin_prime2full_pinyin_prime import (
    normal_pinyin2full_pinyin_pair
    ,classify_full_pinyin_prime2ym_cls_ex
    )

__mk1 = lambda: defaultdict(set) # num2good_hanzis
__mk2 = lambda: defaultdict(__mk1) # ym2num2good_hanzis
def make_sm2ym2num2good_hanzis__where_exists_sm_but_no_half_sm(hanzi2pinyins):
    #-> sm2ym2num2good_hanzi_set
    #声母、韵母、声调
    sm2ym2num2good_hanzis = defaultdict(__mk2)
    for hanzi, pinyins in hanzi2pinyins.items():
        it = iter_good_pinyin_sm_ym_cls_pair(pinyins)
        for sm, ym, pinyin_number in it:
            sm2ym2num2good_hanzis[sm][ym][pinyin_number].add(hanzi)

    # defaultdict -> dict
    sm2ym2num2good_hanzi_set = sm2ym2num2good_hanzis__transform(
        sm2ym2num2good_hanzis, lambda hanzis:hanzis)
    return sm2ym2num2good_hanzi_set

def iter_good_pinyin_sm_ym_cls_pair(normal_pinyins):
    for normal_pinyin in normal_pinyins:
        (full_pinyin_prime, pinyin_number
        ) = normal_pinyin2full_pinyin_pair(normal_pinyin)

        (may_sm, may_half_sm, ym_cls
        ) = classify_full_pinyin_prime2ym_cls_ex(full_pinyin_prime)
        if may_sm and not may_half_sm:
            sm = may_sm
            ym = ym_cls
            assert sm+ym == full_pinyin_prime
            yield sm, ym, pinyin_number

def sm2ym2num2good_hanzis__transform(sm2ym2num2good_hanzis, hanzis2hanzis):
    sm2ym2num2good_hanzis = {
        sm:{ym:{num: hanzis2hanzis(hanzis) for num, hanzis in num2hanzis.items()}
            for ym, num2hanzis in ym2num2hanzis.items()
        }
        for sm, ym2num2hanzis in sm2ym2num2good_hanzis.items()
        }
    return sm2ym2num2good_hanzis


def sm2ym2num2good_hanzi_set2sm2ym2num2good_hanzi_str(sm2ym2num2good_hanzi_set):
    return sm2ym2num2good_hanzis__transform(
        sm2ym2num2good_hanzi_set
        , lambda hanzi_set: ''.join(sorted(hanzi_set))
        )
def sm2ym2num2good_hanzi_str2sm2ym2num2good_hanzi_set(sm2ym2num2good_hanzi_str):
    return sm2ym2num2good_hanzis__transform(sm2ym2num2good_hanzi_set, set)



(sm2ym2num2good_hanzi_set
) = make_sm2ym2num2good_hanzis__where_exists_sm_but_no_half_sm(hanzi2pinyins)
(sm2ym2num2good_hanzi_str
) = sm2ym2num2good_hanzi_set2sm2ym2num2good_hanzi_str(sm2ym2num2good_hanzi_set)



def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdout # may_open_stdin
    from pprint import pprint
    from pathlib import PurePath as Path
    this_file = Path(__file__)
    this_folder = this_file.parent
    this_file_name = this_file.name

    parser = argparse.ArgumentParser(
        description=f'show sm2ym2num2good_hanzis from hanzi2pinyins'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    '''
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-ie', '--input_encoding', type=str
                        , default=Global.encoding
                        , help='input file encoding')
    '''
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-oe', '--output_encoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-str', '--hanzi_str', action='store_true'
                        , default = False
                        , help='hanzis is hanzi_str instead of hanzi_set')


    args = parser.parse_args(args)
    #input_encoding = args.input_encoding
    output_encoding = args.output_encoding
    omode = 'wt' if args.force else 'xt'

    sm2ym2num2good_hanzis__name = (
        'sm2ym2num2good_hanzi_str' if args.hanzi_str else
        'sm2ym2num2good_hanzi_set'
        )
    sm2ym2num2good_hanzis = globals()[sm2ym2num2good_hanzis__name]

    '''
    may_ifname = args.input
    if may_ifname is None:
        this_folder = Path(__file__).parent
        ifname = this_folder / Global.ifname
    else:
        ifname = may_ifname
    with open(ifname, 'rt', encoding=input_encoding) as fin:
    '''

    may_ofname = args.output
    if may_ofname is None:
        may_ofname = this_folder / f'{sm2ym2num2good_hanzis__name}.py'
    with may_open_stdout(may_ofname, omode, encoding=output_encoding) as fout:
        print(f'#{sm2ym2num2good_hanzis__name} generated by {this_file_name}', file=fout);
        print(f'{sm2ym2num2good_hanzis__name} = \\', file=fout);
        pprint(sm2ym2num2good_hanzis, stream=fout)


if __name__ == '__main__':
    main()



