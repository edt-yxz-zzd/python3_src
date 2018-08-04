
from char2zm import char2zm_ls, joiner
from pprint import pprint
import io
from sand import read_or_calc_xwrite__txt, gb18030


fmt_char2splits_path = 'fmt_char2splits.gb'
joiner(globals(), 'fmt_char2splits_path')

zhengma_roots = '''
A AI
B BD BI BK BM BO BZ
C CD CC CE CH CI CK CO CU  CS
D DS
E ED EA EB EC EE EH
F FD FB FJ FK FV
G GD GG GH GI GL GM GO GQ GR
H HD HB HE HI HM HS
I ID IH II IO
J JD JI
K KD KC KI KJ KO KU KV  KIA KIB KIC
L LD LC LI LJ LK LL LO LR LW  LKA
M MA MB MC MD ME MF MH MI MO MY
N ND NB NC NI NJ NK NL NX
O OD OI OS OX  ODA
P PD PF PQ PS PV PY  PDA
Q QD QI QM QX QY  QDA QYA
R RD RH RO RR RS RY RZ  RZA
S SE SH SI SK SO SU SY
T TD TG TI TL TX
U UD UA UB UC UF UO
V VD
W WD WM WO WS WT WW WX WZ
X XD XB XI XK XM XO XS  XMA
Y YD YDA YA YI YM YT YY YZ  YYA YYB YIA
Z ZD ZI ZM ZS ZY
'''

roots = sorted(zhengma_roots.split())
rN = lambda n: set(r for r in roots if len(r) == n)
r1 = rN(1)
r2 = rN(2)
r3 = rN(3)
r2_from_2_3 = r2 | set(zm[:2] for zm in r3)

grammar = '''
zm = zm2 | zm3 | zm4
zm2 = 2 | 1A | 1D
zm3 = 21 | 12 | 111 | 3 | 1AA | 2A
zm4 = 3.1 | 2.11 | 22 | 11.11 | 112 | 1AAA | 2AA | 3A | 11VV

'''


def fmt_rN(rN):
    sep = '\n' + ' '*4
    return sep+sep.join(sorted(rN))
grammar = '''
zm :
    zm2
    zm3
    zm4
zm2 :
    2
    1A = 1 A
    1D = 1 D
zm3 :
    21 = 2 1
    12 = 1 2'
    111 = 1 1 1
    3 = 3
    1AA = 1 A A
    2A = 2 A
zm4 :
    31 = 3 1
    211 = 2 1 1
    22 = 2 2
    1111 = 1 1 1 1
    112 = 1 1 2'
    1AAA = 1 A A A
    2AA = 2 A A
    3A = 3 A
    11VV = 1 1 V V

1 : {}
2 : {}
3 : {}


'''.format(*map(fmt_rN, [r1, r2, r3]))

if 0:
    ss = main_ref, nontoken_ref2rule_ids, rule_id2refs, token_refs = \
         ('zm', {'zm4': [12, 13, 14, 15, 16, 17, 18, 19, 20], 'zm2': [3, 4, 5], 'zm3': [6, 7, 8, 9, 10, 11], '1': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46], '3': [198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211], '2': [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197], 'zm': [0, 1, 2]}, {0: ['zm2'], 1: ['zm3'], 2: ['zm4'], 3: ['2'], 4: ['1', 'A'], 5: ['1', 'D'], 6: ['2', '1'], 7: ['1', '2'], 8: ['1', '1', '1'], 9: ['3'], 10: ['1', 'A', 'A'], 11: ['2', 'A'], 12: ['3', '1'], 13: ['2', '1', '1'], 14: ['2', '2'], 15: ['1', '1', '1', '1'], 16: ['1', '1', '2'], 17: ['1', 'A', 'A', 'A'], 18: ['2', 'A', 'A'], 19: ['3', 'A'], 20: ['1', '1', 'V', 'V'], 21: ['A'], 22: ['B'], 23: ['C'], 24: ['D'], 25: ['E'], 26: ['F'], 27: ['G'], 28: ['H'], 29: ['I'], 30: ['J'], 31: ['K'], 32: ['L'], 33: ['M'], 34: ['N'], 35: ['O'], 36: ['P'], 37: ['Q'], 38: ['R'], 39: ['S'], 40: ['T'], 41: ['U'], 42: ['V'], 43: ['W'], 44: ['X'], 45: ['Y'], 46: ['Z'], 47: ['AI'], 48: ['BD'], 49: ['BI'], 50: ['BK'], 51: ['BM'], 52: ['BO'], 53: ['BZ'], 54: ['CC'], 55: ['CD'], 56: ['CE'], 57: ['CH'], 58: ['CI'], 59: ['CK'], 60: ['CO'], 61: ['CS'], 62: ['CU'], 63: ['DS'], 64: ['EA'], 65: ['EB'], 66: ['EC'], 67: ['ED'], 68: ['EE'], 69: ['EH'], 70: ['FB'], 71: ['FD'], 72: ['FJ'], 73: ['FK'], 74: ['FV'], 75: ['GD'], 76: ['GG'], 77: ['GH'], 78: ['GI'], 79: ['GL'], 80: ['GM'], 81: ['GO'], 82: ['GQ'], 83: ['GR'], 84: ['HB'], 85: ['HD'], 86: ['HE'], 87: ['HI'], 88: ['HM'], 89: ['HS'], 90: ['ID'], 91: ['IH'], 92: ['II'], 93: ['IO'], 94: ['JD'], 95: ['JI'], 96: ['KC'], 97: ['KD'], 98: ['KI'], 99: ['KJ'], 100: ['KO'], 101: ['KU'], 102: ['KV'], 103: ['LC'], 104: ['LD'], 105: ['LI'], 106: ['LJ'], 107: ['LK'], 108: ['LL'], 109: ['LO'], 110: ['LR'], 111: ['LW'], 112: ['MA'], 113: ['MB'], 114: ['MC'], 115: ['MD'], 116: ['ME'], 117: ['MF'], 118: ['MH'], 119: ['MI'], 120: ['MO'], 121: ['MY'], 122: ['NB'], 123: ['NC'], 124: ['ND'], 125: ['NI'], 126: ['NJ'], 127: ['NK'], 128: ['NL'], 129: ['NX'], 130: ['OD'], 131: ['OI'], 132: ['OS'], 133: ['OX'], 134: ['PD'], 135: ['PF'], 136: ['PQ'], 137: ['PS'], 138: ['PV'], 139: ['PY'], 140: ['QD'], 141: ['QI'], 142: ['QM'], 143: ['QX'], 144: ['QY'], 145: ['RD'], 146: ['RH'], 147: ['RO'], 148: ['RR'], 149: ['RS'], 150: ['RY'], 151: ['RZ'], 152: ['SE'], 153: ['SH'], 154: ['SI'], 155: ['SK'], 156: ['SO'], 157: ['SU'], 158: ['SY'], 159: ['TD'], 160: ['TG'], 161: ['TI'], 162: ['TL'], 163: ['TX'], 164: ['UA'], 165: ['UB'], 166: ['UC'], 167: ['UD'], 168: ['UF'], 169: ['UO'], 170: ['VD'], 171: ['WD'], 172: ['WM'], 173: ['WO'], 174: ['WS'], 175: ['WT'], 176: ['WW'], 177: ['WX'], 178: ['WZ'], 179: ['XB'], 180: ['XD'], 181: ['XI'], 182: ['XK'], 183: ['XM'], 184: ['XO'], 185: ['XS'], 186: ['YA'], 187: ['YD'], 188: ['YI'], 189: ['YM'], 190: ['YT'], 191: ['YY'], 192: ['YZ'], 193: ['ZD'], 194: ['ZI'], 195: ['ZM'], 196: ['ZS'], 197: ['ZY'], 198: ['KIA'], 199: ['KIB'], 200: ['KIC'], 201: ['LKA'], 202: ['ODA'], 203: ['PDA'], 204: ['QDA'], 205: ['QYA'], 206: ['RZA'], 207: ['XMA'], 208: ['YDA'], 209: ['YIA'], 210: ['YYA'], 211: ['YYB']}, frozenset({'NL', 'NI', 'NJ', 'NK', 'ND', 'NB', 'NC', 'VD', 'NX', 'FD', 'FB', 'FJ', 'FK', 'FV', 'PF', 'KC', 'RH', 'KD', 'KJ', 'KI', 'KO', 'ZS', 'KV', 'KU', 'LK', 'J', 'N', 'CS', 'B', 'CU', 'F', 'CK', 'CI', 'CH', 'CO', 'SU', 'CC', 'R', 'CE', 'CD', 'ODA', 'HD', 'HE', 'HB', 'HM', 'HI', 'HS', 'YDA', 'X', 'Z', 'T', 'UO', 'ZI', 'UD', 'UF', 'UA', 'UC', 'UB', 'I', 'M', 'EH', 'XMA', 'EE', 'ED', 'PD', 'EA', 'EC', 'EB', 'Y', 'MD', 'XD', 'MF', 'MA', 'MC', 'MB', 'PV', 'XO', 'MO', 'V', 'U', 'PS', 'PQ', 'JD', 'JI', 'QYA', 'YY', 'YIA', 'BZ', 'YZ', 'KIC', 'YT', 'YI', 'BI', 'BK', 'YM', 'BM', 'BO', 'YA', 'QDA', 'BD', 'YD', 'PDA', 'WW', 'WT', 'WS', 'OI', 'OD', 'WZ', 'WX', 'WD', 'OX', 'WO', 'WM', 'OS', 'XS', 'GG', 'H', 'GD', 'L', 'RO', 'GO', 'ZY', 'GM', 'LKA', 'RD', 'D', 'GI', 'GH', 'RY', 'RZ', 'ZD', 'GR', 'GQ', 'P', 'RR', 'RS', 'ZM', 'TX', 'E', 'TI', 'XK', 'TL', 'TG', 'TD', 'LR', 'ME', 'SI', 'SH', 'SO', 'LW', 'SE', 'LC', 'SY', 'LD', 'LJ', 'DS', 'GL', 'LO', 'LL', 'YYA', 'IH', 'YYB', 'RZA', 'IO', 'QY', 'QX', 'PY', 'ID', 'Q', 'QD', 'MY', 'QI', 'QM', 'KIB', 'KIA', 'K', 'XM', 'II', 'O', 'AI', 'MI', 'C', 'A', 'G', 'MH', 'SK', 'LI', 'XB', 'S', 'XI', 'W'}))

    from nn_ns.parse.choice_concat_parser import compile as compile_cc
    from sand import get_attrs__str
    print('compile...')
    parser_cc = compile_cc(grammar, 'zm')
    attrs = 'main_ref, nontoken_ref2rule_ids, rule_id2refs, token_refs'
    print('get_attrs__str...')
    s = main_ref, nontoken_ref2rule_ids, rule_id2refs, token_refs = get_attrs__str(attrs, parser_cc)
    #print(s)
    assert s == ss

    

def parse_zm(zm):
    L = len(zm)
    if not 0 < L < 5:
        raise ValueError('not 0 < len(zm) < 5')
    if any(ch not in r1 for ch in zm):
        raise ValueError('any(ch not in [A-Z])')
    if L == 1:
        return []

    L2parser = {2: parse_zm2, 3: parse_zm3, 4: parse_zm4}
    return L2parser[L](zm)



def parse_zm2(zm):
    '''
zm2 :
    2
    1A = 1 A
    1D = 1 D
'''
    
    if len(zm) != 2:
        return []
    
    ch = zm[-1]
    if ch == 'A':
        return ['1A']
    if ch == 'D':
        return ['1D']
    if zm in r2:
        return ['2']
    return []



def parse_zm3(zm):
    '''
zm3 :
    21 = 2 1
    12 = 1 2
    111 = 1 1 1
    3 = 3
    1AA = 1 A A
    2A = 2 A
'''
    
    if len(zm) != 3:
        return []

    ls = []
    if zm[:2] in r2:
        ls.append('21')
        if zm[-1] == 'A':
            ls.append('2A')
    
    if zm[-2:] in r2:
        ls.append('12')
    ls.append('111')
    if zm in r3:
        ls.append('3')

    if zm[-2:] == 'AA':
        ls.append('1AA')
    return ls
def parse_zm4(zm):
    '''
zm4 :
    31 = 3 1
    211 = 2 1 1
    22 = 2 2'
    1111 = 1 1 1 1
    112 = 1 1 2'
    1AAA = 1 A A A
    2AA = 2 A A
    3A = 3 A
    11VV = 1 1 V V
'''
    
    if len(zm) != 4:
        return []

    ls = []
    if zm[:3] in r3:
        ls.append('31')
        if zm[-1] == 'A':
            ls.append('3A')
    if zm[:2] in r2:
        ls.append('211')
        if zm[-2:] == 'AA':
            ls.append('2AA')
    if zm[-2:] == 'VV':
        ls.append('11VV')
    
    if zm[-2:] in r2_from_2_3:
        ls.append('112')
        if zm[:2] in r2:
            ls.append('22')
    ls.append('1111')

    if zm[-3:] == 'AAA':
        ls.append('1AAA')
    return ls

def union(iters):
    return set().union(*iters)

def calc_char2splits():
    char2splits = {}
    for ch, ls in char2zm_ls.items():
        L = max(map(len, ls))
        ls = [zm.upper() for zm in ls if len(zm) == L]
        #print(ls)
        s = union(parse_zm(zm) for zm in ls)
        char2splits[ch] = sorted(s)
        #print(ch, s)
        #break
    return char2splits

def fmt_char2splits(char2splits):
    sout = io.StringIO()
    pprint(char2splits, stream=sout)
    data_str = sout.getvalue()
    return data_str

calc_data_str = lambda: fmt_char2splits(calc_char2splits())
data_str = read_or_calc_xwrite__txt(fmt_char2splits_path, calc_data_str, gb18030)










