r'''[[[
[[
gbk vs utf8
===
py -m nn_ns.CJK.CJK_pinyin__ucd.normal_pinyin_prime2full_pinyin_prime > /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_pinyin__ucd.normal_pinyin_prime2full_pinyin_prime..out.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_pinyin__ucd.normal_pinyin_prime2full_pinyin_prime..out.txt
    utf8
view ++enc=gbk ../../python3_src/nn_ns/CJK/CJK_pinyin__ucd/normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair.py
    gbk
diff ../../python3_src/nn_ns/CJK/CJK_pinyin__ucd/normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair.py  /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_pinyin__ucd.normal_pinyin_prime2full_pinyin_prime..out.txt
< # -*- coding: gbk -*-
422c421
<  '��': ('E', ('', '', 'E'))}
---
>  'ê': ('E', ('', '', 'E'))}
    ## not bug, gbk but `diff` read as utf8
]]



[[
bug?:miss: tei1,fiao4,  r5,ging1
unicode::unihan never complete
===
view ../../python3_src/nn_ns/CJK/CJK_pinyin__cedict/read_cedict_1_0_ts.py
□ □ [ging1] /uptight/obstinate/to awkwardly force oneself to do sth/(Taiwanese, POJ pr. [gēng], often written as ㄍㄧㄥ, no generally accepted hanzi form)/
兒 儿 [r5] /non-syllabic diminutive suffix/retroflex final/
忒 忒 [tei1] /(dialect) too/very/also pr. [tui1]/
覅 覅 [fiao4] /(fanqie contraction of 勿 and 要)/
]]


[[
ucd X cedict_1_0_ts
===
py_adhoc_call nn_ns.CJK.CJK_pinyin__ucd.normal_pinyin_prime2full_pinyin_prime  @main --extra_normal_pinyin_primes='["fiao", "tei", "ging", "r"]'
 'er': ('er', ('', '', 'er')),
 'ri': ('r', ('', '', 'R')),
 'r': ('r', ('', '', 'R')),
    bug!
         expect? 'r': ('er', ('', '', 'er')),
    normal_pinyin_prime2full_pinyin_prime only work correctly on GOOD pinyin_prime
    bad input ==>> undefined behavior

py_adhoc_call nn_ns.CJK.CJK_pinyin__ucd.normal_pinyin_prime2full_pinyin_prime  @main --extra_normal_pinyin_primes='["fiao", "tei", "ging"]'  --nm4varable:normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair____ucdXcedict  --header:'# -*- coding: utf-8 -*-' > ../../python3_src/nn_ns/CJK/CJK_pinyin__ucd/normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair____ucdXcedict.py
view ../../python3_src/nn_ns/CJK/CJK_pinyin__ucd/normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair____ucdXcedict.py
diff ../../python3_src/nn_ns/CJK/CJK_pinyin__ucd/normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair.py  ../../python3_src/nn_ns/CJK/CJK_pinyin__ucd/normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair____ucdXcedict.py
< # -*- coding: gbk -*-
< normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair = \
---
> # -*- coding: utf-8 -*-
> normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair____ucdXcedict = \
93a94
>  'fiao': ('fiao', ('f', '', 'iao')),
105a107
>  'ging': ('ging', ('g', '', 'ing')),
332a335
>  'tei': ('tei', ('t', '', 'ei')),
422c425
<  '��': ('E', ('', '', 'E'))}
---
>  'ê': ('E', ('', '', 'E'))}
]]




######################
######################prev doc
######################
#python3_src\script\char\韵\std_pinyin.py
#   modified

normal_pinyin = normal_pinyin_prime + pinyin_number
full_pinyin = full_pinyin_prime + pinyin_number


normal_pinyin -> full_pinyin
    B = '(b|p|m|f|d|t|n|l|g|k|h|)'
    R = '(r|zh|ch|sh)'
    Z = '(z|c|s)'
    Q = '(j|q|x)'
    W = 'w'
    Y = 'y'
    M = RZQB # except 'WY'
    E = ê
    1) [Qy]u.* -> [Qy]v.*
       wu?.* -> u.*
       [RZ]i -> [RZ]
    2) yv.* -> v.*
    3) yi?.* -> i.*
    4) .*[iv]e -> .*[iv]E
    5) iu,ui,un,vn,vE -> iou,uei,uen,vin,viE
    // iou ??
    M?a M?ia M?ua           M?an M?ian M?van M?uan      7
    M?o M?e M?io M?uo       M?u?en M?v?in               6
    M?v?iE                  M?ang M?iang M?uang         4
    M?ai M?uai              M?eng M?ing M?ong M?iong    6
    M?ei M?uei              [BQ]?i  er [BQ]?v           5
    M?ao M?iao              R   Z                       4
    M?ou M?iou              M?u                         3
    hng m n ng E                                        5
                                                        total: 40
M?u?en M?v?in M?v?iE
R Z er hng m n ng E
#]]]'''


__all__ = '''
    normal_pinyin_prime2full_pinyin_prime
    classify_full_pinyin_prime2ym_cls
    classify_full_pinyin_prime2ym_cls_ex

    split_normal_pinyin
    normal_pinyin2full_pinyin_pair
    '''.split()

import re
B = '(?:b|p|m|f|d|t|n|l|g|k|h|)'
R = '(?:r|zh|ch|sh)'
Z = '(?:z|c|s)'
Q = '(?:j|q|x)'
W = 'w'
Y = 'y'
M = f'(?:{R}|{Z}|{Q}|{B})'


#0
_E_ = 'ê', 'E'
#1
Qy_u_ = f'({Q}|y)u', r'\1v'
W_u_ = f'wu?', r'u'
RZ_i = f'({R}|{Z})i', r'\1'
# _E_, Qy_u_, W_u_, RZ_i

#2
y_v_ = 'yv', 'v'
#3
y_i_ = 'yi?', 'i'
#4
_iv_e = '([iv])e', r'\1E'
# y_v_, y_i_, _iv_e
#5) iu,ui,un,vn,vE -> iou,uei,uen,vin,viE
_iu = 'iu', 'iou'
_ui = 'ui', 'uei'
_un = 'un', 'uen' # no ung/vng
_vn = 'vn', 'vin' # but result will have ueng: weng -> ueng
_vE = 'vE', 'viE'
# _vE, _vn, _un, _ui, _iu



pattern_pairs = _E_, Qy_u_, W_u_, RZ_i, y_v_, y_i_, _iv_e, _vE, _vn, _un, _ui, _iu
rex_repl_pairs = tuple((re.compile(p), r) for p, r in pattern_pairs)

def normal_pinyin_prime2full_pinyin_prime(normal_pinyin_prime):
    r'normal_pinyin_prime -> full_pinyin_prime'
    if normal_pinyin_prime=='r': raise ValueError(f'ri or er?: normal_pinyin=="r"')

    xxx_pinyin = normal_pinyin_prime
    for rex, repl in rex_repl_pairs:
        xxx_pinyin = rex.sub(repl, xxx_pinyin)
    full_pinyin_prime = xxx_pinyin
    return full_pinyin_prime


normal_pinyin_rex = re.compile(r'(?P<prime>[a-zê]+)(?P<number>\d*)')
def split_normal_pinyin(normal_pinyin):
    r'normal_pinyin -> (normal_pinyin_prime, pinyin_number)'
    m = normal_pinyin_rex.match(normal_pinyin)
    if not m: raise ValueError(f'{normal_pinyin!r} is not normal_pinyin')
    normal_pinyin_prime = m['prime']
    pinyin_number = m['number']
    if not pinyin_number:
        pinyin_number = 0
    else:
        pinyin_number = int(pinyin_number)
    return normal_pinyin_prime, pinyin_number

r = normal_pinyin_prime2full_pinyin_prime('yin')
#print(r)
assert r == 'in'

test_data = \
    [ ('qu', 'qv')
    , ('yu', 'v')
    , ('wan', 'uan')
    , ('wu', 'u')
    , ('ri', 'r')
    , ('zi', 'z')
    , ('chi', 'ch')

    , ('yuan', 'van')
    , ('yin', 'in')
    , ('que', 'qviE')
    , ('tie', 'tiE')
    , ('liu', 'liou')
    , ('tui', 'tuei')
    , ('kun', 'kuen')
    , ('qun', 'qvin')
    , ('jue', 'jviE')
    , ('X', 'X')
    , ('X', 'X')
    ]
for normal_pinyin_prime, ans__full_pinyin_prime in test_data:
    #rint(normal_pinyin_prime, ans__full_pinyin_prime)
    assert normal_pinyin_prime2full_pinyin_prime(normal_pinyin_prime) == ans__full_pinyin_prime

def is_rex(rex, s):
    return re.fullmatch(rex, s) is not None
__rex__sm_ym = f'(?P<sm>{M})(?P<ym>.*)' #声母、韵母
def classify_full_pinyin_prime2ym_cls(full_pinyin_prime):
    'full_pinyin_prime -> ym_cls'
    (may_sm, may_half_sm, ym_cls
    ) = classify_full_pinyin_prime2ym_cls_ex(full_pinyin_prime)
    return ym_cls

def classify_full_pinyin_prime2ym_cls_ex(full_pinyin_prime):
    r'''full_pinyin_prime -> ym_cls_ex
    ym_cls_ex = (may_sm, may_half_sm, ym_cls)
    may_half_sm = ''|'u'|'v'
'''

    ym_cls = None
    # R Z er hng m n ng E
    if is_rex(R, full_pinyin_prime):
        ym_cls = 'R'
    elif is_rex(Z, full_pinyin_prime):
        ym_cls = 'Z'
    elif full_pinyin_prime in 'er hng m n ng E'.split():
        ym_cls = full_pinyin_prime
    if ym_cls is not None:
        may_sm = may_half_sm = ''
        return (may_sm, may_half_sm, ym_cls)

    # M?u?en M?v?in M?v?iE
    m = re.match(__rex__sm_ym, full_pinyin_prime)
    if not m: raise ValueError(f'{full_pinyin_prime!r} is not a full_pinyin_prime')
    sm = m['sm']
    full_ym = m['ym']
    d = {'uen':'en', 'ueng':'eng'
        ,'vin':'in', 'ving':'ing'
        ,'viE':'iE'
        }
    end_ym = d.get(full_ym, full_ym)
    may_half_sm = '' if end_ym == full_ym else full_ym[0]
    assert may_half_sm + end_ym == full_ym

    may_sm = sm
    ym_cls = end_ym
    return (may_sm, may_half_sm, ym_cls)


def normal_pinyin2full_pinyin_pair(normal_pinyin):
    r'normal_pinyin -> (full_pinyin_prime, pinyin_number)'
    (normal_pinyin_prime, pinyin_number
    ) = split_normal_pinyin(normal_pinyin)

    (full_pinyin_prime
    ) = normal_pinyin_prime2full_pinyin_prime(normal_pinyin_prime)

    return full_pinyin_prime, pinyin_number


def __():
  if 1:
    #from collections import defaultdict
    from pprint import pprint
    from pathlib import PurePath as Path
    from itertools import chain
  def iter_read__normal_pinyin_primes(ifname):
    '-> Iter normal_pinyin_prime'
    with open(ifname, encoding = 'utf8') as fin:
        for i, line in enumerate(fin):
            # once omit encoding=utf8!!! cause using gbk!!!
            #   if '锚' in line: print(i, line)
            normal_pinyin_prime = line.strip()
            yield normal_pinyin_prime
  def mk__normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair(normal_pinyin_primes):
    '-> {normal_pinyin_prime:(full_pinyin_prime,ym_cls_ex/(may_sm, may_half_sm, ym_cls))}'
    #ym_cls2normal_pinyin_primes = defaultdict(list)
    normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair = {}

    for normal_pinyin_prime in normal_pinyin_primes:
        full_pinyin_prime = normal_pinyin_prime2full_pinyin_prime(normal_pinyin_prime)
        (may_sm, may_half_sm, ym_cls
        ) = classify_full_pinyin_prime2ym_cls_ex(full_pinyin_prime)
        #print(ym_cls)
        #ym_cls2normal_pinyin_primes[ym_cls].append(normal_pinyin_prime)
        normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair[normal_pinyin_prime] = full_pinyin_prime, (may_sm, may_half_sm, ym_cls)

    return normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair

    #ym_cls2normal_pinyin_primes = dict(ym_cls2normal_pinyin_primes)
    # print('cls2HanyuPinyinPrimes = \\'); pprint(ym_cls2normal_pinyin_primes)
    #assert '锚' not in ym_cls2normal_pinyin_primes


    '''
    normal_pinyin_prime2ym_cls = {
        normal_pinyin_prime : ym_cls
        for ym_cls, normal_pinyin_primes
            in ym_cls2normal_pinyin_primes.items()
        for normal_pinyin_prime in normal_pinyin_primes
        }
    '''
  def main(*, ipath=None, extra_normal_pinyin_primes=(), nm4varable=None, header=None):
    if not ipath:
        this_folder = Path(__file__).parent
        ifname = this_folder / 'allHanyuPinyinPrime_list.txt'
    else:
        ifname = ipath
    normal_pinyin_primes = iter_read__normal_pinyin_primes(ifname)
    if extra_normal_pinyin_primes:
        normal_pinyin_primes = chain(extra_normal_pinyin_primes, normal_pinyin_primes)
    if not nm4varable:
        nm4varable = 'normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair'

    normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair = mk__normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair(normal_pinyin_primes)
    #print('HanyuPinyinPrime2cls = \\'); pprint(normal_pinyin_prime2ym_cls)
    if header:
        print(header)
    print(f'{nm4varable} = \\'); pprint(normal_pinyin_prime2full_pinyin_prime_ym_cls_ex_pair)
  if 1:
    return main
main = __()


if __name__ == '__main__':
    main()

