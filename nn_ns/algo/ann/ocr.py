from backpropagation import 反向传播算法

import pickle # dump load
import sand

font8x8 = '8x8_font.txt'
训练集文件 = '训练集文件.8x8'
反向传播识字训练_txt = '反向传播识字训练.txt'
from sand import default_fix_paths
default_fix_paths('output', __name__, 'font8x8 训练集文件  反向传播识字训练_txt')
##
##print(font8x8)
##raise





def gen_8x8_font(fname=font8x8):
    from root.unifont import gbk_hanzi_rng, read as read_fontfile, font_file
    
    with open(fname, 'x') as fout:
        u16_to_mx = read_fontfile(font_file)
        for i,j in gbk_hanzi_rng:
            for k in range(i,j):
                mx = u16_to_mx[k]
                assert len(mx) == 16
                assert len(mx[0]) == 16
                mx_avg4 = [tuple(sum(mx[x][y]
                                     for x in range(2*u, 2*u+2)
                                     for y in range(2*v, 2*v+2))/4.0
                            for v in range(8))
                           for u in range(8)]
                record = (chr(k), k, bin(k), mx_avg4)
                fout.write(str(record))
                fout.write('\n')

def 生成训练集(fout_name=训练集文件, fin_name=font8x8):
    ls = []
    #pickle.dump(ls, fout_name)
    with open(fin_name) as fin:
        for line in fin:
            c, idx, bin_ord, mx_avg4 = eval(line)
            bin_ord = bin_ord[2:]
            bin_ord = '0' * (16-len(bin_ord)) + bin_ord
            vout = tuple(0 if c == '0' else 1 for c in bin_ord)
            assert len(vout) == 16
            vin = [x for row in mx_avg4 for x in row]
            ls.append((vin, vout))
    with open(fout_name, 'xb') as fout:
        pickle.dump(ls, fout)
            
def trans(n = 2, 训练集文件=训练集文件):
    各层结点数 = (8**2, 16, 16)
    with open(训练集文件, 'rb') as fin:
        训练集 = pickle.load(fin)
    #print(len(训练集))

    data = {
        '各层结点数':各层结点数,
        '训练集':训练集,
        '学习速率':0.3,
        '终止误差':0.3,
        '最大训练次数':n,
        '权冲量':0.3,
        }
    return 反向传播算法(**data)

def t():
    r = sand.dt(trans, n=1)
    with open(反向传播识字训练_txt, 'w') as fout:
        fout.write(str(r))
    
def gen_data_for_cpp(fout_name = 'trans_data_for_cpp.dat', 训练集文件=训练集文件):
    各层结点数 = (8**2, 16, 16)
    with open(训练集文件, 'rb') as fin:
        训练集 = pickle.load(fin)

    def to_vector_str(ls):
        s = ''.join(str(x) + ', ' for x in ls)
        return '[{}]'.format(s)
    def to_pair_str(i, o):
        return '({}, {}, )'.format(to_vector_str(i), to_vector_str(o))
    with open(fout_name, 'x') as fout:
        ls = [to_pair_str(输入, 输出) for 输入, 输出 in 训练集]
        fout.write(to_vector_str(ls))
            
gen_data_for_cpp()


