
'''
RIX是《仙剑奇侠传DOS版》的音乐格式，它采用小尾数法存储。


RIX格式 - 格式 

1.头结构
偏移长度描述
0x000x02标识码(0x55AA) // little-endian: "AA 55 ..." in file
0x020x01是否保留打击乐器(0-全乐音,1-保留打击乐)
0x080x02乐器块偏移(不过我怀疑是4字节的.不过我还没找到证据)
0x0C0x02音乐块偏移(同样怀疑是4字节)

2.乐器块结构
乐器块是以乐器为单位，每个乐器为INS格式的0x02-0x41，共0x40字节合成起来的。
INS格式是ADLIB公司BNK格式的前身(至今仍有INS编辑器)。
具体格式，有ADLIB声卡开发包的可以看一下。

3.音乐块结构
音乐块是以2字节为单位的，每一个单位都有两种状态：
(1)普通状态
低字节设定值
高字节
高4位命令码
低4位通道号
(2)延时状态
当普通状态的命令码不是合法的(即不为"命令一览"中的值之一)，即为延时值，其大小为两个字节。
音乐块以双字节魔数0x8000结尾(碰到它，千万不要以为是延时了!!)，一般也是整个文件的结尾。

说明1：乐器通道
当打击乐器标志==0,0-8全为乐音。
当打击乐器标志==1,0-6为乐音,7-A为打击乐器(BD,SD,TT,CY,HH);
说明2:命令一览
(1)设定乐器
命令码0x9
设定值乐器块内的乐器号
(2)频率微调
命令码0xA
设定值频率调整值(0x00-低半音,0xFF-高半音)
(3)音量调整
命令码0xB
设定值音量值(0x00-最小,0x7F-最大[默认7F])
(4)设定音符
命令码0xC
设定值音符号码(0x3C是中央C,半音为单位[0x00为禁止通道发声,也就是静音])注意，必须有延时才能放出音来，两个通道可以同时延时形成和音。


'''



from collections import defaultdict
from struct import *

head_st = Struct('<2s1B5s2L')

def readHead(fin):
    assert fin.tell() == 0

    size = head_st.size
    bs = fin.read(size)
    magic, 是否保留打击乐器, others, 乐器块偏移, 音乐块偏移 = head_st.unpack(bs)
    assert magic == b'\xAA\x55'
    assert others == b'\x00\x00\x00\x00\x00'
    assert 是否保留打击乐器 in (0, 1)
    return 是否保留打击乐器, 乐器块偏移, 音乐块偏移



def readRIX(fname):
    结束码 = b'\x00\x80'
    命令码集 = (0x9, 0xA, 0xB, 0xC, )
    with open(fname, 'rb') as fin:
        是否保留打击乐器, 乐器块偏移, 音乐块偏移 = readHead(fin)
        fin.seek(音乐块偏移)
        #ls = ['默认音量0x7F(最大);音符0=中央C(半音为单位)']
        flist = lambda: ['首延时值{}'.format(总延时值)]
        d = defaultdict(flist)
        总延时值 = 0
        while True:
            bs = fin.read(2)
            if bs == 结束码:
                break
            设定值, 命令码通道号 = bs
            命令码 = 命令码通道号 >> 4
            通道号 = 命令码通道号 & 0x0F
            if 命令码 in 命令码集:
                通道, r = 处理命令码(命令码, 通道号, 设定值)
                d[通道].append(r)
            else:
                延时值, r = 处理延时值(bs)
                总延时值 += 延时值
                for k in d:
                    ls = d[k]
                    t = 合并延时值(ls[-1], 延时值)
                    if t == None:
                        ls.append(延时值)
                    else:
                        ls[-1] = t
                
            #ls.append(r)
    return d

def 合并延时值(或是延时值, 延时值):
    if isinstance(或是延时值, int):
        return 或是延时值 + 延时值
    else:
        return None
def 处理延时值(bs):
    延时值, = unpack('<H', bs)
    #assert 延时值 == 256
    #if 延时值 != 256: print(延时值)
    r = '延时值{}'.format(延时值)
    return 延时值, r

def 处理命令码(命令码, 通道号, 设定值):
    通道 = '通道{}'.format(通道号)
    if 命令码 == 0x9:
        assert 0 <= 设定值 < 0xB
        r = '乐器{}'.format(设定值)
    elif 命令码 == 0xA:
        设定值 -= 128
        r = '频率微调{}/128半音'.format(设定值)
    elif 命令码 == 0xB:
        #assert 0 <= 设定值 <= 0x7F
        #if not (0 <= 设定值 <= 0x7F): print(设定值)
        r = '音量{}/{}'.format(设定值, 0xFF)
    elif 命令码 == 0xC:
        if 设定值 == 0x0:
            r = '音符<通道静音>'
        else:
            设定值 -= 0x3C
            r = '音符c1{:+}'.format(设定值)
    else:
        raise
    return 通道, r


def 找调号(某通道ls):
    ls = 某通道ls
    ls = [int(e[4:]) for e in ls if isinstance(e, str) if e[:4] == '音符c1']
    ls = [i%12 for i in ls]
    s = set(ls)
    assert len(s) <= 7

    
    assert len(s) == 7 # 不是7个音,　比较难算,　下面按7个来算
    f = lambda i: (i-1)% 12 in s and (i+5)% 12 in s
    for i in s:
        if f(i):
            break
    else:
        assert len(s) < 7
        raise

    for j in s:
        if j != i:
            assert not f(j)

    k = i
    主音表 = 'C D EF G A B'
    assert len(主音表)
    主音 = 主音表[k]
    assert 主音 != ' '

    简谱表 = (1, None, 2, None, 3, 4, None, 5, None, 6, None, 7,)
    ls = [(i-k)%12 for i in ls]
    ls = [简谱表[i] for i in ls]

    return i, '{}大调'.format(主音), ls


    



d = readRIX('MUSIC_67.RIX')
for k in d:
    print(k)
    print(d[k])
    


s = 找调号(d['通道0'])
print(s)


    
    
