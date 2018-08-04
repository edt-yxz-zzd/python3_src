

from nn_ns.char.unifont import gbk_rng, gbk_hanzi_rng
from sand import default_fix_paths
gbk_txt_path = 'gbk.txt'
default_fix_paths('output', __name__, 'gbk_txt_path')

def g1():
    with open(gbk_txt_path, 'xb') as fout:
        for i in range(128+1, 256-1):
            for j in range(128, 256-1):
                fout.write(bytes((i,j)))
            fout.write(b'\n')

def t(s = '一︰亐亖亗亙亜亝亞亣亪'):
    for c in s:
        i = ord(c)
        print(c, i, i.to_bytes(4, byteorder='big'))

def ls_short_gbk_rng():
    ls = []
    for i, j in gbk_rng:
        if j-i<20:
            print(''.join(chr(k) for k in range(i,j)))
        else:
            ls.append((i,j))
    print(ls)
def g2():
    with open(gbk_txt_path, 'x', encoding='gbk') as fout:
        for i, j in gbk_rng:
            fout.write(''.join(chr(k) for k in range(i,j)))
            fout.write('\n')
t()
