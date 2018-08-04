


'''
normal_pinyin = pinyin_prime + pinyin_number
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
'''



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
_un = 'un', 'uen'
_vn = 'vn', 'vin'
_vE = 'vE', 'viE'
# _vE, _vn, _un, _ui, _iu



pattern_pairs = _E_, Qy_u_, W_u_, RZ_i, y_v_, y_i_, _iv_e, _vE, _vn, _un, _ui, _iu
rex_repl_pairs = tuple((re.compile(p), r) for p, r in pattern_pairs)

def std_pinyin(pinyin):
    # pinyin_prime -> full_pinyin_prime
    for rex, repl in rex_repl_pairs:
        pinyin = rex.sub(repl, pinyin)
    return pinyin


pinyin_rex = re.compile(r'(?P<prime>[a-zê]+)(?P<number>\d*)')
def split_pinyin(pinyin):
    # pinyin -> (prime, number)
    m = pinyin_rex.match(pinyin)
    if not m: raise ValueError(f'{pinyin!r} is not pinyin')
    prime = m['prime']
    number = m['number']
    if not number:
        number = 0
    else:
        number = int(number)
    return prime, number

r = std_pinyin('yin')
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
for pinyin, ans in test_data:
    #rint(pinyin, ans)
    assert std_pinyin(pinyin) == ans

def is_rex(rex, s):
    return re.fullmatch(rex, s) is not None
def classify_std_pinyin(std_pinyin):
    # full_pinyin_prime -> ym_cls

    # R Z er hng m n ng E
    if is_rex(R, std_pinyin):
        return 'R'
    elif is_rex(Z, std_pinyin):
        return 'Z'
    elif std_pinyin in 'er hng m n ng E'.split():
        return std_pinyin

    # M?u?en M?v?in M?v?iE
    m = re.match(f'(?P<sm>{M})(?P<ym>.*)', std_pinyin)
    if not m: raise ValueError(f'{std_pinyin!r} is not a std_pinyin')
    ym = m['ym']
    d = {'uen':'en', 'vin':'in', 'viE':'iE'}
    return d.get(ym, ym)


from collections import defaultdict
from pprint import pprint
ifname = 'allHanyuPinyinPrime_list.txt'
cls2pinyins = defaultdict(list)
with open(ifname, encoding = 'utf8') as fin:
    for i, line in enumerate(fin):
        # once omit encoding=utf8!!! cause using gbk!!!
        #   if '锚' in line: print(i, line)
        pinyin = line.strip()
        std = std_pinyin(pinyin)
        cls = classify_std_pinyin(std)
        #print(cls)
        cls2pinyins[cls].append(pinyin)

cls2pinyins = dict(cls2pinyins)
# print('cls2HanyuPinyinPrimes = \\'); pprint(cls2pinyins)
assert '锚' not in cls2pinyins


pinyin2cls = {pinyin : cls for cls, pinyins in cls2pinyins.items()
                for pinyin in pinyins
                }
print('HanyuPinyinPrime2cls = \\'); pprint(pinyin2cls)

