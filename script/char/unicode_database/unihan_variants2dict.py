
from seed.io.iter_line_contents import filter_py_line_contents
from seed.io.RCXW import make_rcxw__pickle
import re
from collections import defaultdict
from pprint import pprint
from itertools import chain


input_fname = 'Unihan_Variants_9_0.txt'
output_fname = 'han2variant2vtype2srcs.py.obj'

variant_types = '''
    kSemanticVariant
    kSimplifiedVariant
    kSpecializedSemanticVariant
    kTraditionalVariant
    kZVariant
    '''.split()









unicode_rex = re.compile(r'U\+(?P<unicode>[0-9A-F]+)')
def _repl_unicode(m):
    return chr(int(m.group('unicode'), base=16))

def replace_unicode(s, rex = unicode_rex):
    return rex.sub(_repl_unicode, s)
assert replace_unicode(' U+0 ') == ' \0 '

def parse_line_content(line):
    r'''covert line to value
line -> (han, variant_type, variant_srcs_pairs)
String -> (Char, str, [(Char, [String])])

line format:
    line = han "\t" variant_type "\t" variant_srcs_pairs
    han = <Han-Char>
    variant_type = re'[^\t]+'
    variant_srcs_pairs = variant_srcs (" " variant_srcs)*
    variant_srcs = variant ("<" srcs)?
    srcs = src ("," src)*
    src = re"[^\t ,<]"
    variant = han
'''
    han, variant_type, variant_srcs_pairs = line.split('\t')
    assert len(han) == 1
    assert variant_type in variant_types
    variant_srcs_pairs = variant_srcs_pairs.split()
    variant_srcs_pairs = map(parse_variant_srcs_pair, variant_srcs_pairs)
    variant_srcs_pairs = tuple(variant_srcs_pairs)
    return han, variant_type, variant_srcs_pairs
def parse_variant_srcs_pair(variant_srcs_pair):
    L = len(variant_srcs_pair)
    variant, srcs = variant_srcs_pair.split('<') if L > 2 else \
                    (variant_srcs_pair, '')
    assert len(variant) == 1
    srcs = tuple(srcs.split(','))
    return variant, srcs
def unihan_variants2dict(fname, encoding='utf-8'):
    # d :: han -> variant -> variant_type -> [src]
    d = defaultdict(lambda:defaultdict(dict))
    with open(fname, encoding=encoding) as fin:
        for line in filter_py_line_contents(fin):
            line = replace_unicode(line)
            han, variant_type, variant_srcs_pairs = parse_line_content(line)
            dh = d[han]
            for variant, srcs in variant_srcs_pairs:
                dhv = dh[variant]
                assert variant_type not in dhv
                dhv[variant_type] = srcs

    d = {k:dict(v) for k,v in d.items()}
    han2variant2vtype2srcs = d
    return han2variant2vtype2srcs

if 0:
    d = unihan_variants2dict(input_fname)
    pprint(d)

rcxw = make_rcxw__pickle(lambda:unihan_variants2dict(input_fname)
                        , output_fname)
han2variant2vtype2srcs = rcxw()
#print(len(han2variant2vtype2srcs))
assert 9980 == len(han2variant2vtype2srcs)


def filter_by_variant_type(han2variant2vtype2srcs, variant_type):
    # return han2variants
    assert variant_type in variant_types
    d = defaultdict(list)
    for han, variant2vtype2src2 in han2variant2vtype2srcs.items():
        for variant, vtype2src2 in variant2vtype2src2.items():
            if variant_type in vtype2src2:
                d[han].append(variant)
    han2variants = {han:''.join(variants) for han, variants in d.items()}
    return han2variants

def classify_by_variant_type(han2variant2vtype2srcs):
    # return vtype2han2variants
    k2v = lambda variant_type:\
            filter_by_variant_type(han2variant2vtype2srcs, variant_type)
    vtype2han2variants = {vtype: k2v(vtype) for vtype in variant_types}
    return vtype2han2variants

def calc_vtype2han2variants():
    vtype2han2variants = classify_by_variant_type(han2variant2vtype2srcs)
    vtype2size = {vtype:len(han2_) for vtype, han2_ in vtype2han2variants.items()}
    #print(vtype2size)
    assert vtype2size == \
        { 'kSemanticVariant': 3232, 'kSpecializedSemanticVariant': 498
        , 'kSimplifiedVariant': 3048, 'kTraditionalVariant': 3018
        , 'kZVariant': 2559}
    #print(sum(vtype2size.values()))
    assert sum(vtype2size.values()) == 12355
    return vtype2han2variants




def find_multi_values(k2vs):
    return ''.join(k for k,vs in k2vs.items() if len(vs)>1)
def has_multi_variants(vtype2han2variants, vtype):
    return find_multi_values(vtype2han2variants[vtype])
def has_multi_simplifieds(vtype2han2variants):
    return has_multi_variants(vtype2han2variants, 'kSimplifiedVariant')
def has_multi_traditionals(vtype2han2variants):
    return has_multi_variants(vtype2han2variants, 'kTraditionalVariant')



def iter_all_chars(ch2str):
    for ch, s in ch2str.items():
        assert len(ch)==1
        yield from ch
        yield from s

def iter_all_chars_from_dicts(dicts):
    return chain.from_iterable(map(iter_all_chars, dicts))

def chars2unique_sorted_str(chars):
    return ''.join(sorted(set(chars)))


def _calc_charss():
    vtype2han2variants = calc_vtype2han2variants()
    t_of_ms = has_multi_simplifieds(vtype2han2variants)
    s_of_mt = has_multi_traditionals(vtype2han2variants)
    #print(t_of_ms, s_of_mt)
    chars_with_multi_ST = t_of_ms + s_of_mt

    other_dicts = [d for vt,d in vtype2han2variants.items() if vt not in
                    ('kSimplifiedVariant', 'kTraditionalVariant')]
    all_chars_exclude_ST = chars2unique_sorted_str(
                            iter_all_chars_from_dicts(other_dicts))

    assert len(all_chars_exclude_ST) == 5356


    vary_chars = chars_with_multi_ST + all_chars_exclude_ST
    vary_chars = chars2unique_sorted_str(vary_chars)
    all_chars_with_variant = chars2unique_sorted_str(
                iter_all_chars_from_dicts(vtype2han2variants.values()))

    assert len(vary_chars) == 5361
    assert len(all_chars_with_variant) == 10068

    return chars_with_multi_ST, vary_chars, all_chars_with_variant

rcxw = make_rcxw__pickle(_calc_charss, '__vary_charss.py.obj')
chars_with_multi_ST, vary_chars, all_chars_with_variant = rcxw()
assert len(vary_chars) == 5361
assert len(all_chars_with_variant) == 10068

make_vary_charss = lambda: dict(
                    chars_with_multi_ST=chars_with_multi_ST
                    , vary_chars = vary_chars
                    , all_chars_with_variant=all_chars_with_variant
                    )
rcxw = make_rcxw__pickle(make_vary_charss, 'vary_charss.py.obj')
vary_charss = rcxw()





