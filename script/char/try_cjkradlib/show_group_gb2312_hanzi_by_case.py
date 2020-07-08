
# set PYTHONIOENCODING=utf8

#from nn_ns.CJK.CJK_struct.make_simple_decomposed_chars3980 import \
#    iter_simple_decomp_chars

from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import \
    (default_iter_read_a_d
    ,default_iter_read_cjk_decomp
    )
from nn_ns.CJK.iter_gb2312_hanzi import iter_gb2312_hanzi
from collections import defaultdict

_ad = dict(default_iter_read_a_d())
_cjk = dict(default_iter_read_cjk_decomp())
def iter_gb2312_hanzi_not_decomposed():
    return (char for char in iter_gb2312_hanzi() if char not in _ad)

#def find_gb2312_not_decomposed():
def generate_gb2312_hanzi_not_decomposed():
    for i, char in enumerate(iter_gb2312_hanzi_not_decomposed()):
        print(i, char, _cjk[char])
#generate_gb2312_hanzi_not_decomposed()
# 993 麟 ('stl', ['鹿', '粦'])
# total 994 in 6763

def classify_gb2312_hanzi_by_case():
    d = defaultdict(list)
    for char in iter_gb2312_hanzi():
        case, components = x = _cjk[char]
        d[case].append((char, x))
    return d
def show_group_gb2312_hanzi_by_case():
    d = classify_gb2312_hanzi_by_case()
    items = sorted(d.items())
    i = 0
    for case, pairs in items:
        for i, (char, x) in enumerate(pairs, i):
            print(i, case, char, x)
show_group_gb2312_hanzi_by_case()

