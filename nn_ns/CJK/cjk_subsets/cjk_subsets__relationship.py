
r"""

py -m seed.text.charset_filter -o ~/tmp/cjk_d.txt -f > ~/tmp/cjk_pr2.txt
py -m nn_ns.CJK.cjk_subsets.cjk_subsets__relationship -i ~/tmp/cjk_d.txt -o  ~/tmp/cjk_rel.txt -f -o2  ~/tmp/cjk_rel_more.txt -f2 > ~/tmp/cjk_rel_more__le.txt
#"""

from io import StringIO
from seed.text.charset_filter import CharsetCharFilter
from seed.data_funcs.rngs import (
        NonTouchRanges
        ,subset_relation_ex__xtouch_ranges
        )
from seed.helper.safe_eval import safe_eval
from pathlib import Path
from itertools import combinations
from seed.iters.iter_subsets_of import iter_subsets_of__sorted_by_len_first

def path2cjk_d(cjk_d_txt_path):
    path = Path(cjk_d_txt_path)
    txt = path.read_text(encoding='utf8')
    return txt2cjk_d(txt)

def txt2cjk_d(cjk_d_txt):
    cjk_d = safe_eval(cjk_d_txt, locals=dict(CharsetCharFilter=CharsetCharFilter))
    return cjk_d

def subset_relation_of_encoding2cjk_part_rngs(encoding2cjk_part_rngs):
    r"""
    input:
        encoding2cjk_part_rngs :: {encoding:CharsetCharFilter}
    output:
        encoding2relation2encodings :: {encoding:{relation:[encoding]}}
    where:
        relation <- "!<>="
        encoding :: str
    #"""
    cjk_d = encoding2cjk_part_rngs
    encodings = sorted(encoding2cjk_part_rngs)
    def f(ccf):
        return NonTouchRanges(ccf.ranges)
    def cmp(lhs, rhs):
        # -> rel
        r = subset_relation_ex__xtouch_ranges(lhs.ranges, rhs.ranges, lhs_maynot_be_nontouch_ranges=False, rhs_maynot_be_nontouch_ranges=False, faster_return_not_le=False, faster_return_not_ge=False)
        return relations[r]

    relations = "!<>="
    encoding2relation2encodings = {}
    for lhs_encoding in encodings:
        lhs = f(cjk_d[lhs_encoding])
        relation2encodings = {rel:[] for rel in relations}
        encoding2relation2encodings[lhs_encoding] = relation2encodings
        for rhs_encoding in encodings:
            rhs = f(cjk_d[rhs_encoding])
            rel = cmp(lhs, rhs)
            relation2encodings[rel].append(rhs_encoding)
    return encoding2relation2encodings


def handle_encoding2relation2encodings(encoding2relation2encodings):
    #cjk part eq class
    encoding_cjk_part_eq_class_set = set()
    for relation2encodings in encoding2relation2encodings.values():
        ls = relation2encodings['=']
        ts = tuple(sorted(ls))
        encoding_cjk_part_eq_class_set.add(ts)
    assert sum(map(len, encoding_cjk_part_eq_class_set)) == len(encoding2relation2encodings)
    encoding_cjk_part_eq_classes = sorted(encoding_cjk_part_eq_class_set)

    encoding2std_cjk_eq_encoding = {}
    std_cjk_eq_encodings = set()
    for ts in encoding_cjk_part_eq_classes:
        std_cjk_eq_encoding = ts[0]
        std_cjk_eq_encodings.add(std_cjk_eq_encoding)
        for encoding in ts:
            encoding2std_cjk_eq_encoding[encoding] = std_cjk_eq_encoding
    assert encoding2std_cjk_eq_encoding.keys() == encoding2relation2encodings.keys()

    def to_std_encodings(encodings):
        return sorted(set(encoding2std_cjk_eq_encoding[encoding] for encoding in encodings))

    new_encoding2relation2encodings = {}
    std_cjk_eq_encoding_lt_pair_set = set()
    _std_cjk_eq_encoding_lt_pair_set__from_gt = set()
    for std_cjk_eq_encoding in std_cjk_eq_encodings:
        relation2encodings = encoding2relation2encodings[std_cjk_eq_encoding]
        new_relation2encodings = {k:to_std_encodings(v) for k,v in relation2encodings.items()}
        del new_relation2encodings['!']
        del new_relation2encodings['=']
        new_encoding2relation2encodings[std_cjk_eq_encoding] = new_relation2encodings

        for rhs_encoding in new_relation2encodings["<"]:
            std_cjk_eq_encoding_lt_pair_set.add((std_cjk_eq_encoding, rhs_encoding))
        for lhs_encoding in new_relation2encodings[">"]:
            _std_cjk_eq_encoding_lt_pair_set__from_gt.add((lhs_encoding, std_cjk_eq_encoding))
    assert std_cjk_eq_encoding_lt_pair_set == _std_cjk_eq_encoding_lt_pair_set__from_gt

    encoding2relation2encodings__std_cjk_eq = new_encoding2relation2encodings
    std_cjk_eq_encoding_lt_pairs = sorted(std_cjk_eq_encoding_lt_pair_set)

    std_cjk_eq_encoding_atomic_lt_pair_set = set()
    for lhs_encoding, rhs_encoding in std_cjk_eq_encoding_lt_pairs:
        llts = encoding2relation2encodings__std_cjk_eq[lhs_encoding]["<"]
        rgts = encoding2relation2encodings__std_cjk_eq[rhs_encoding][">"]
        middles = set(llts) & set(rgts)
        assert lhs_encoding not in middles
        assert rhs_encoding not in middles
        assert all((lhs_encoding, mid_encoding) in std_cjk_eq_encoding_lt_pair_set for mid_encoding in middles)
        assert all((mid_encoding, rhs_encoding) in std_cjk_eq_encoding_lt_pair_set for mid_encoding in middles)
        if not middles:
            std_cjk_eq_encoding_atomic_lt_pair_set.add((lhs_encoding, rhs_encoding))
    std_cjk_eq_encoding_atomic_lt_pairs = sorted(std_cjk_eq_encoding_atomic_lt_pair_set)

    #atomic buttomup
    encoding2encodings__std_cjk_eq__atomic_lt = {lhs:[] for lhs in std_cjk_eq_encodings}
    #atomic topdown
    encoding2encodings__std_cjk_eq__atomic_gt = {rhs:[] for rhs in std_cjk_eq_encodings}
    for lhs_encoding, rhs_encoding in std_cjk_eq_encoding_atomic_lt_pairs:
        #rhss = encoding2encodings__std_cjk_eq__atomic_lt.setdefault(lhs_encoding, [])
        #lhss = encoding2encodings__std_cjk_eq__atomic_gt.setdefault(rhs_encoding, [])
        rhss = encoding2encodings__std_cjk_eq__atomic_lt[lhs_encoding]
        lhss = encoding2encodings__std_cjk_eq__atomic_gt[rhs_encoding]
        lhss.append(lhs_encoding)
        rhss.append(rhs_encoding)
    tops = sorted({lhs for lhs, rhss in encoding2encodings__std_cjk_eq__atomic_lt.items() if not rhss})
    buttoms = sorted({rhs for rhs, lhss in encoding2encodings__std_cjk_eq__atomic_gt.items() if not lhss})
    encoding2encodings__std_cjk_eq__atomic_lt[""] = buttoms
    encoding2encodings__std_cjk_eq__atomic_gt[""] = tops
    atomic_buttomup = encoding2encodings__std_cjk_eq__atomic_lt
    atomic_topdown = encoding2encodings__std_cjk_eq__atomic_gt



    #encoding_cjk_part_eq_classes__txt
    #std_cjk_eq_encoding_lt_pairs__txt
    #std_cjk_eq_encoding_atomic_lt_pairs__txt
    #atomic_buttomup__txt
    #atomic_topdown__txt
    sout = StringIO()
    for ts in encoding_cjk_part_eq_classes:
        print(' = '.join(ts), file=sout)
    encoding_cjk_part_eq_classes__txt = sout.getvalue()

    sout = StringIO()
    for lhs_encoding, rhs_encoding in std_cjk_eq_encoding_lt_pairs:
        print(f'{lhs_encoding!s} < {rhs_encoding!s}', file=sout)
    std_cjk_eq_encoding_lt_pairs__txt = sout.getvalue()

    sout = StringIO()
    for lhs_encoding, rhs_encoding in std_cjk_eq_encoding_atomic_lt_pairs:
        print(f'{lhs_encoding!s} *<* {rhs_encoding!s}', file=sout)
    std_cjk_eq_encoding_atomic_lt_pairs__txt = sout.getvalue()


    sout = StringIO()
    show_forest_from_DAG(atomic_buttomup
            ,roots=[""]
            ,node2str=lambda me: me if me else "<"
            ,level2indent=lambda u: " "*(2*u)
            ,fout=sout
            )
    atomic_buttomup__txt = sout.getvalue()

    sout = StringIO()
    show_forest_from_DAG(atomic_topdown
            ,roots=[""]
            ,node2str=lambda me: me if me else ">"
            ,level2indent=lambda u: " "*(2*u)
            ,fout=sout
            )
    atomic_topdown__txt = sout.getvalue()


    return dict(
            encoding_cjk_part_eq_classes
            =encoding_cjk_part_eq_classes
            ,std_cjk_eq_encodings
            =std_cjk_eq_encodings
            ,encoding2std_cjk_eq_encoding
            =encoding2std_cjk_eq_encoding
            ,encoding2relation2encodings__std_cjk_eq
            =encoding2relation2encodings__std_cjk_eq
            ,std_cjk_eq_encoding_lt_pairs
            =std_cjk_eq_encoding_lt_pairs
            ,std_cjk_eq_encoding_atomic_lt_pairs
            =std_cjk_eq_encoding_atomic_lt_pairs
            ,atomic_buttomup
            =atomic_buttomup
            ,atomic_topdown
            =atomic_topdown
            #############
            #############
            ,encoding_cjk_part_eq_classes__txt
            =encoding_cjk_part_eq_classes__txt
            ,std_cjk_eq_encoding_lt_pairs__txt
            =std_cjk_eq_encoding_lt_pairs__txt
            ,std_cjk_eq_encoding_atomic_lt_pairs__txt
            =std_cjk_eq_encoding_atomic_lt_pairs__txt
            ,atomic_buttomup__txt
            =atomic_buttomup__txt
            ,atomic_topdown__txt
            =atomic_topdown__txt
            )
def show_forest_from_DAG(forest_from_DAG, *, roots, node2str, level2indent, fout):
    def show_tree(node, level):
        indent = level2indent(level)
        head = node2str(node)
        print(f'{indent!s}{head!s}', file=fout)
        level += 1
        for child in forest_from_DAG[node]:
            show_tree(child, level)
    level = 0
    for root in roots:
        show_tree(root, level)


def size_of_encoding_cjk_part(encodings, encoding2cjk_part_rngs):
    #encoding2cjk_part_size = {k:v.len() for k,v in encoding2cjk_part_rngs.items()}
    d = encoding2cjk_part_rngs
    encoding2cjk_part_size = {k:d[k].len() for k in encodings}
    return encoding2cjk_part_size
def intersection_of_subsets_of_encoding_cjk_part_rngs_of(encodings, encoding2cjk_part_rngs):
    d = {}
    s = {}
    def f(encoding):
        rngs = NonTouchRanges(encoding2cjk_part_rngs[encoding].ranges)
        return rngs
    for subset in iter_subsets_of__sorted_by_len_first(encodings):
        if not subset:
            pass
        elif len(subset)==1:
            [encoding] = subset
            rngs = f(encoding)
            d[subset] = rngs
        else:
            L = len(subset)//2
            assert 0 < L < len(subset)
            left = subset[:L]
            right = subset[L:]
            if left in s or right in s:
                s.add(subset)
            else:
                common_rngs = d[left] & d[right]
                if common_rngs.len_ints():
                    d[subset] = common_rngs
                else:
                    s.add(subset)
    encodings2nonempty_common_rngs = d
    encodings_with_empty_common_rngs = s
    return encodings2nonempty_common_rngs, encodings_with_empty_common_rngs



def intersection_of_pairwise_encoding_cjk_part_rngs(encodings, encoding2cjk_part_rngs):
    d = {}
    s = {}
    def f(encoding):
        rngs = NonTouchRanges(encoding2cjk_part_rngs[encoding].ranges)
        return rngs
    for lhs, rhs in combinations(encodings, 2):
        lrngs = f(lhs)
        rrngs = f(rhs)
        common = lrngs & rrngs
        k = lhs, rhs
        if common.len_ints():
            d[k] = common
        else:
            s.add(k)
    encoding_pair2nonempty_common_rngs = d
    encoding_pairs_of_empty_common_rngs = s
    return encoding_pair2nonempty_common_rngs, encoding_pairs_of_empty_common_rngs
del intersection_of_pairwise_encoding_cjk_part_rngs


def handle_more_result(more_result, encoding2cjk_part_rngs):
    std_cjk_eq_encoding2cjk_part_size = size_of_encoding_cjk_part(more_result['std_cjk_eq_encodings'], encoding2cjk_part_rngs)

    def get_snd_buttoms(more_result):
        _d = more_result['atomic_buttomup']
        [_e] = _d[""]
        snd_buttoms = _d[_e]
        return snd_buttoms
    snd_buttoms = get_snd_buttoms(more_result)
    [
    snd_buttom_subset2nonempty_common_rngs
    ,snd_buttom_subsets_with_empty_common_rngs
    ] = intersection_of_subsets_of_encoding_cjk_part_rngs_of(snd_buttoms, encoding2cjk_part_rngs)

    #std_cjk_eq_encoding2cjk_part_size__txt
    #snd_buttoms__txt
    #snd_buttom_subset2nonempty_common_rngs__txt
    #snd_buttom_subsets_with_empty_common_rngs__txt
    sout = StringIO()
    for encoding, cjk_size in sorted(std_cjk_eq_encoding2cjk_part_size.items()):
        print(f'{encoding!s}.cjk_size = {cjk_size}', file=sout)
    std_cjk_eq_encoding2cjk_part_size__txt = sout.getvalue()

    sout = StringIO()
    for encoding in snd_buttoms:
        print(encoding, file=sout)
    snd_buttoms__txt = sout.getvalue()

    sout = StringIO()
    for encodings, common_rngs in sorted(snd_buttom_subset2nonempty_common_rngs.items()):
        encodings = sorted(encodings)
        assert encodings
        and_expr = "&".join(encodings)
        cjk_size = common_rngs.len_ints()
        print(f'cjk_part of ({and_expr!s})\n    # {cjk_size}\n    = {common_rngs!r}', file=sout)
    snd_buttom_subset2nonempty_common_rngs__txt = sout.getvalue()

    sout = StringIO()
    for encodings in sorted(snd_buttom_subsets_with_empty_common_rngs):
        encodings = sorted(encodings)
        assert encodings
        and_expr = "&".join(encodings)
        print(f'cjk_part of ({and_expr!s}) = {{}}', file=sout)
    snd_buttom_subsets_with_empty_common_rngs__txt = sout.getvalue()



    more_result2 = {**more_result
        ,**dict(
            std_cjk_eq_encoding2cjk_part_size
            =std_cjk_eq_encoding2cjk_part_size
            ,snd_buttoms
            =snd_buttoms
            ,snd_buttom_subset2nonempty_common_rngs
            =snd_buttom_subset2nonempty_common_rngs
            ,snd_buttom_subsets_with_empty_common_rngs
            =snd_buttom_subsets_with_empty_common_rngs
            ########
            ########
            ,std_cjk_eq_encoding2cjk_part_size__txt
            =std_cjk_eq_encoding2cjk_part_size__txt
            ,snd_buttoms__txt
            =snd_buttoms__txt
            ,snd_buttom_subset2nonempty_common_rngs__txt
            =snd_buttom_subset2nonempty_common_rngs__txt
            ,snd_buttom_subsets_with_empty_common_rngs__txt
            =snd_buttom_subsets_with_empty_common_rngs__txt
            )
        }

    return more_result2



def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    from pprint import pprint

    parser = argparse.ArgumentParser(
        description="find out relationship of cjk part of encodings (postprocess of charset_filter.py)"
        , epilog=""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-o2', '--output2', type=str, default=None
                        , help='output2 file path')
    parser.add_argument('-f2', '--force2', action='store_true'
                        , default = False
                        , help='open mode for output2 file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'
    omode2 = 'wt' if args.force2 else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        txt = fin.read()
    cjk_d = txt2cjk_d(txt)

    encoding2cjk_part_rngs = cjk_d
    encoding2relation2encodings = subset_relation_of_encoding2cjk_part_rngs(encoding2cjk_part_rngs)
    more_result = handle_encoding2relation2encodings(encoding2relation2encodings)
    more_result2 = handle_more_result(more_result, encoding2cjk_part_rngs)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        pprint(encoding2relation2encodings, stream=fout)

    may_ofname2 = args.output2
    with may_open_stdout(may_ofname2, omode2, encoding=encoding) as fout2:
        pprint(more_result, stream=fout2)

    ks = r"""
    encoding_cjk_part_eq_classes__txt
    std_cjk_eq_encoding_lt_pairs__txt
    std_cjk_eq_encoding_atomic_lt_pairs__txt
    atomic_buttomup__txt
    atomic_topdown__txt

    std_cjk_eq_encoding2cjk_part_size__txt
    snd_buttoms__txt
    snd_buttom_subset2nonempty_common_rngs__txt
    snd_buttom_subsets_with_empty_common_rngs__txt
    """.split()
    show_more_result2(ks, more_result2)


def show_more_result2(ks, more_result2):
    sep = '#'*10
    for k in ks:
        print(f'{sep!s} begin: {k!s} {sep!s}')
        print(more_result2[k])
        print(f'{sep!s} end: {k!s} {sep!s}')

if __name__ == "__main__":
    main()


