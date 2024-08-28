#__all__:goto
r'''[[[
e ../../python3_src/seed/text/mk_char_pt_ranges5classifier.py
来源自脚本:
    view ../../python3_src/nn_ns/CJK/CJK_data/raw/U+FF00全角字符.txt
类似:
    view ../../python3_src/seed/text/mk_char_pt_ranges5predicator.py
缩写:ea,gc
    view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/PropertyValueAliases.txt
py-bug:
    view ../lots/NOTE/Python/python-bug/unicodedata-bug.txt


seed.text.mk_char_pt_ranges5classifier
py -m nn_ns.app.debug_cmd   seed.text.mk_char_pt_ranges5classifier -x
py -m nn_ns.app.doctest_cmd seed.text.mk_char_pt_ranges5classifier:__doc__ -ht
py_adhoc_call   seed.text.mk_char_pt_ranges5classifier   @f
from seed.text.mk_char_pt_ranges5classifier import *
#]]]'''
__all__ = r'''
mk_char_pt_ranges5classifier
    Name4region4char_pt
    classifier7ea_gc5ch
group_via_inv__j2kind_

mk_char_pt_ranges5rougher
    rougher7ea_gc05ea_gc
    rougher7ea5ea_gc

show__j2kind_
    show__kind2js_

'''.split()#'''
__all__
from seed.data_funcs.rngs import StackStyleSimpleIntSet, StackStyleSimpleIntMapping


import unicodedata as U
U.unidata_version
from enum import Enum
class Name4region4char_pt(Enum):
    unicode = (0, 0x11_00_00)
    ascii = (0, 0x80)
    BMP = (0, 0x1_00_00)
    r'''[[[
view ../lots/NOTE/unicode/BMP.txt
Plane 0 == Basic Multilingual Plane (BMP)
Plane 1 == Supplementary Multilingual Plane (SMP)
Plane 2 == Supplementary Ideographic Plane (SIP)
    #]]]'''#'''
assert Name4region4char_pt.unicode is Name4region4char_pt['unicode']
assert Name4region4char_pt['unicode'].value == (0, 0x11_00_00)

def mk_char_pt_ranges5classifier(classifier, /, *, nm4region='unicode'):
    'classifier/(char_pt->kind) -> j2kind/StackStyleSimpleIntMapping<char_pt,kind>'
    char_pt_rng = Name4region4char_pt[nm4region].value
    return _mk_char_pt_ranges5classifier(char_pt_rng, classifier)

def _mk_char_pt_ranges5classifier(char_pt_rng, classifier, /):
    (begin_char_pt, end_char_pt) = char_pt_rng
    j2kind = StackStyleSimpleIntMapping()
    for j in range(begin_char_pt, end_char_pt):
        j2kind[j] = kind = classifier(chr(j))
    return j2kind

def group_via_inv__j2kind_(j2kind, /):
    'j2kind/StackStyleSimpleIntMapping<char_pt,kind> -> kind2js/StackStyleSimpleIntMapping<kind,StackStyleSimpleIntSet<char_pt>>'
    kind2js = {}
    for rng, kind in j2kind.iter_rng_value_pairs_(reverse=False):
      js4kind = kind2js.setdefault(kind, StackStyleSimpleIntSet())
      js4kind.push_rng(rng)
    return kind2js

#def mk_char_pt_ranges5refiner(j2old_kind, refiner, /):
#generalizer,roughen,rougher
def mk_char_pt_ranges5rougher(j2old_kind, rougher, /):
    'j2old_kind/StackStyleSimpleIntMapping<char_pt,old_kind> -> rougher/(old_kind->new_kind) -> j2new_kind/StackStyleSimpleIntMapping<char_pt,new_kind>'
    j2new_kind = StackStyleSimpleIntMapping()
    for rng, old_kind in j2old_kind.iter_rng_value_pairs_(reverse=False):
        new_kind = rougher(old_kind)
        j2new_kind.push_rng_value(rng, new_kind)
    return j2new_kind


def classifier7ea_gc5ch(ch, /):
    'char -> (ea, gc)/(east_asian_width,category)'
    ea = U.east_asian_width(ch)
    gc = U.category
    return (ea, gc)
def rougher7ea_gc05ea_gc(ea_gc, /):
    '(ea, gc)/(east_asian_width,category) -> (ea,gc0/gc[0])'
    (ea, gc) = ea_gc
    gc0 = gc[0]
    return (ea, gc0)
def rougher7ea5ea_gc(ea_gc, /):
    '(ea, gc)/(east_asian_width,category) -> ea'
    (ea, gc) = ea_gc
    return ea

def show__kind2js_(repr4kind, kind2js, /):
    ls = []
    for kind, js in kind2js.items():
        h = repr(kind)
        for (i,j) in js.iter_rngs_(reverse=False):
            sz = j-i
            s = f'{h}@0x{i:X}+{sz}'
            k = (h, i)
            ls.append((k,s))

    ls.sort()
    for k,s in ls:print(s)


def show__j2kind_(repr4kind, j2kind, /):
    ls = []
    for (i,j), kind in j2kind.iter_rng_value_pairs_(reverse=False):
        h = repr(kind)
        sz = j-i
        s = f'{h}@0x{i:X}+{sz}'
        k = (h, i)
        ls.append((k,s))

    ls.sort()
    for k,s in ls:print(s)

    #len(ls)#
    #with open(r'/sdcard/0my_files/tmp/???-kind.begin.sz.txt', 'xt', encoding='ascii') as ofile:
    #    for k,s in ls:print(s, file=ofile)




__all__
from seed.text.mk_char_pt_ranges5classifier import *
