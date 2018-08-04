from math import isnan
from itertools import accumulate, chain
from fractions import Fraction
from RexParser import RexParser

music_score_language = r'''
简谱文本　=　BEGIN 简谱 END
简谱　=　小节*
小节　_SPACES_ =　拍+　'|'
拍　=　连音+
连音　_NOSPACES_ =　连音记号始? 音高 时长? 连音记号末? 延长*
音高　_NOSPACES_ =　变化? 音符 八度偏移?
时长　_NOSPACES_ =　时值倍数记号+
变化　_NOSPACES_ =　'#' | 'b' | 'X' | 'bb' | '&'
音符 _NOSPACES_ = rex'[0-7]' # 0 是休止符
八度偏移 _NOSPACES_ = 八度升偏移　|　八度降偏移
八度升偏移　_NOSPACES_ =　八度升+
八度升　_NOSPACES_ =　'^'
八度降偏移　_NOSPACES_ =　八度降+
八度降　_NOSPACES_ =　'v'
时值倍数记号 _NOSPACES_ = '_' | '=' | '.'
延长　=　'-'
连音记号始 = '('
连音记号末 = ')'


NEWLINE = '\n'
BEGIN _SPACES_ = rrex'^'
END = rrex'$'
'''

if 0:
    p = RexParser()
    r = p.parser(music_score_language)
    assert r != None
    from ParserResultWalk import ParserResultWalk
    str_parser, _ = ParserResultWalk().process(r, mainID='简谱文本', parsername='简谱parser')
    print(str_parser)
    exec(str_parser)


from MatchPattern import *
class 简谱parser:
    def __init__(self):
        d = {'_NOSPACES_':MatchString,
             '_SPACES_BUT_NEWLINE_':MatchString,
             '_SPACES_':MatchString,
             '简谱文本':MatchSequence,\
            '简谱':MatchStar,\
            '小节':MatchSequence,\
            '拍':MatchPlus,\
            '连音':MatchSequence,\
            '音高':MatchSequence,\
            '时长':MatchPlus,\
            '变化':MatchChoices,\
            '音符':MatchRex,\
            '八度偏移':MatchChoices,\
            '八度升偏移':MatchPlus,\
            '八度升':MatchString,\
            '八度降偏移':MatchPlus,\
            '八度降':MatchString,\
            '时值倍数记号':MatchChoices,\
            '延长':MatchString,\
            '连音记号始':MatchString,\
            '连音记号末':MatchString,\
            'NEWLINE':MatchString,\
            'BEGIN':MatchRex,\
            'END':MatchRex
             }

        o = {name:type.default_factory() for name, type in d.items()}

        a = {'_NOSPACES_': ((r'_NOSPACES_',), {'name':'_NOSPACES_'}),
             '_SPACES_BUT_NEWLINE_': ((r'_SPACES_BUT_NEWLINE_',), {'name':'_SPACES_BUT_NEWLINE_'}),
             '_SPACES_': ((r'_SPACES_',), {'name':'_SPACES_'}),
             '简谱文本':(([o['BEGIN'], o['简谱'], o['END']],), {'name': '简谱文本'}),\
            '简谱':((o['小节'],), {'name': '简谱'}),\
            '小节':(([MatchPlus(o['拍']), MatchString('|')],), {'name': '小节', 'follow': '\\s*'}),\
            '拍':((o['连音'],), {'name': '拍'}),\
            '连音':(([MatchOptional(o['连音记号始']), o['音高'], MatchOptional(o['时长']), MatchOptional(o['连音记号末']), MatchStar(o['延长'])],), {'name': '连音', 'follow': ''}),\
            '音高':(([MatchOptional(o['变化']), o['音符'], MatchOptional(o['八度偏移'])],), {'name': '音高', 'follow': ''}),\
            '时长':((o['时值倍数记号'],), {'name': '时长', 'follow': ''}),\
            '变化':(([MatchString('#'), MatchString('b'), MatchString('X'), MatchString('bb'), MatchString('&')],), {'name': '变化', 'follow': ''}),\
            '音符':(('[0-7]',), {'name': '音符', 'follow': ''}),\
            '八度偏移':(([o['八度升偏移'], o['八度降偏移']],), {'name': '八度偏移', 'follow': ''}),\
            '八度升偏移':((o['八度升'],), {'name': '八度升偏移', 'follow': ''}),\
            '八度升':(('^',), {'name': '八度升', 'follow': ''}),\
            '八度降偏移':((o['八度降'],), {'name': '八度降偏移', 'follow': ''}),\
            '八度降':(('v',), {'name': '八度降', 'follow': ''}),\
            '时值倍数记号':(([MatchString('_'), MatchString('='), MatchString('.')],), {'name': '时值倍数记号', 'follow': ''}),\
            '延长':(('-',), {'name': '延长'}),\
            '连音记号始':(('(',), {'name': '连音记号始'}),\
            '连音记号末':((')',), {'name': '连音记号末'}),\
            'NEWLINE':(('\n',), {'name': 'NEWLINE'}),\
            'BEGIN':((r'^',), {'name': 'BEGIN', 'follow': '\\s*'}),\
            'END':((r'$',), {'name': 'END'})
             }

        assert len(o) == len(a)

        for name, obj in o.items():
            args, kwargs = a[name]
            obj.__init__(*args, **kwargs)

        self.lang = o
        return
    def parser(self, string):
        if not string.endswith('\n'):
            string = string + '\n'
        r = self.lang['简谱文本'].match(string, 0, len(string))
        return r
    

if '简谱parser' not in globals():
    p = RexParser()
    r = p.parser(music_score_language)
    assert r != None
    from ParserResultWalk import ParserResultWalk
    str_parser, _ = ParserResultWalk().process(r, mainID='简谱文本', parsername='简谱parser')
    print(str_parser)
    exec(str_parser)




    
    
class 简谱ParserResultProcess:
    def __init__(self):
        self.每拍时长 = None
        self.每节时长 = None
        self.连音记号始减末 = None
    def process(self, parserResult, 每拍时长, 每节时长):
        assert isinstance(每拍时长, Fraction)
        assert isinstance(每节时长, Fraction)
        
        self.每拍时长 = 每拍时长
        self.每节时长 = 每节时长
        self.连音记号始减末 = 0
        
        self.process简谱文本(parserResult)
        return parserResult.data
    
    def process八度升偏移(self, node):
        node.data = len(node.children)
        return
    def process八度降偏移(self, node):
        node.data = -len(node.children)
        return
    def process八度偏移(self, node):
        i = node.data
        if i == 0:
            self.process八度升偏移(node[i])
        elif i == 1:
            self.process八度降偏移(node[i])
        else:
            raise
        node.data = node[i].data
        return

    def _node2substr(self, node):
        s = node.string[node.start : node.org_end]
        return s
    def process音符(self, node):
        s = self._node2substr(node)
        
        if s == '0':
            node.data = float('NaN')
        else:
            i = int(s)
            assert 0 < i < 8
            node.data = i
            
        return

    
    def process变化(self, node):
        s = self._node2substr(node)
        node.data = s
            
        return
    def process时长(self, node):
        for c in node.children:
            self.process时值倍数记号(c)

        times = 1
        for c in node.children:
            times *= c.data
        node.data = times
        return
    def process时值倍数记号(self, node):
        one = Fraction(1,1)
        times = [one/2, one/4, 3*one/2, ]
        i = node.data
        node.data = times[i]
        return

    def _process_node(self, name, node):
        process = eval('self.process' + name)
        process(node)
        return node.data
    
    def _process_opt(self, name, node, default):
        if node.children:
            node = node[0]
            return self._process_node(name, node)
        else:
            return default
        
    def process音高(self, node):
        one = Fraction(1,1)
        变化 = self._process_opt('变化', node[0], '')
        八度偏移 = self._process_opt('八度偏移', node[2], 0)
        音符 = self._process_node('音符', node[1])
        #print(repr(音符), repr(八度偏移))
        音符 += 7 * 八度偏移
        
        node.data = 变化, 音符
        return

    def process连音记号始(self, node):
        s = self._node2substr(node)
        node.data = s
        self.连音记号始减末 += 1
        return

    def process连音记号末(self, node):
        s = self._node2substr(node)
        node.data = s
        self.连音记号始减末 -= 1
        assert self.连音记号始减末 >= 0
        return
    def process连音(self, node):
        one = Fraction(1,1)
        连音记号始 = self._process_opt('连音记号始', node[0], '')
        连音记号末 = self._process_opt('连音记号末', node[3], '')
        
        延长 = len(node[-1].children)
        时长 = self._process_opt('时长', node[2], one)
        
        时长 += 延长
        时长 *= self.每拍时长
        
        变化, 音符 = 音高 = self._process_node('音高', node[1])
        node.data = 变化, 音符, 时长, 连音记号始, 连音记号末
        return
    
    def process拍(self, node):
        for c in node.children:
            self.process连音(c)

        ls = []
        time = 0
        for c in node.children:
            ls.append(c.data)
            time += c.data[2]
        node.data = ls, time
        return

    def process小节(self, node):
        nodes = node[0]
        for c in nodes.children:
            self.process拍(c)

        ls = []
        time = 0
        for c in nodes.children:
            ls.append(c.data[0])
            time += c.data[-1]

        #print(time, self.每节时长, self.每拍时长)
        assert time == self.每节时长
        node.data = ls
        return

    def process简谱(self, node):
        for c in node.children:
            self.process小节(c)

        ls = []
        for c in node.children:
            ls.append(c.data)
            
        node.data = ls
        return

    def process简谱文本(self, node):
        self.process简谱(node[1])
        node.data = node[1].data
        return



def _名2位置when0eqc1(名表, 名, 切分点, 名caseHeadLen=1):
    L = len(名表)
    head = 名[:切分点]
    num = 名[切分点:]
    
    if num:
        num = int(num)
    else:
        num = 0

    case = head[:名caseHeadLen] # 'F#' -> 'F'
    if case.isupper():
        i = 名表.index(head) - L
        i -= num * L
    else:
        head_upper = case.upper() + head[名caseHeadLen:]
        i = 名表.index(head_upper)
        i += num * L
    return i-L

def _位置2名when0eqc1(名表, 位置, 名caseHeadLen=1):
    L = len(名表)

    i = 位置 + L
    q, r = divmod(i, L)
    assert 0 <= r < L
    name = 名表[r]
    
    if i < 0:
        assert q < 0
        q += 1
        q = -q
    else:
        head = name[:名caseHeadLen]
        head = head.lower()
        name = head + name[名caseHeadLen:]

    assert q >= 0
    sn = q if q else ''
    return '{}{}'.format(name, sn)

_键名升2位置表 = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
_键名降2位置表 = ('C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B')



def _升降2位置表(升降='#'):
    i = '#b'.index(升降)
    return [_键名升2位置表, _键名降2位置表][i]

def 键名2切分点位置表(键名, 升降='#'):
    pos = 1
    name = 键名

    L = len(name)
    if L > 1 and name[1] in '#b':
        升降 = name[1]
        pos = 2

    return pos, _升降2位置表(升降)

    
def 键名2位置when0eqc1(键名):
    pos, 位置表 = 键名2切分点位置表(键名)
    i = _名2位置when0eqc1(位置表, 键名, 切分点=pos)
    return i

def 位置2键名when0eqc1(位置, 升降='#'):
    name = _位置2名when0eqc1(_升降2位置表(升降), 位置)
    return name


def 生成键名表(升降='#'):
    start = 键名2位置when0eqc1('A2')
    end = 键名2位置when0eqc1('c5') + 1

    ls = tuple(位置2键名when0eqc1(i, 升降=升降) for i in range(start, end))
    assert len(ls) == 88

    idx_c1 = ls.index('c1')
    for 位置, 键名 in enumerate(ls, -idx_c1):
        assert 位置 == 键名2位置when0eqc1(键名)
        assert 键名 == 位置2键名when0eqc1(位置, 升降=升降)

    return ls

键名升表 = 生成键名表(升降='#')
键名降表 = 生成键名表(升降='b')

#音名表 = [] 'A2 B2 C1..G1 A1 B1..B c..g a b c1..c5'
def 音名2音值when0eqc1(音名):
    '不含半#/b'
    assert isinstance(音名, str)
    C2B = 'CDEFGAB'

    i = _名2位置when0eqc1(C2B, 音名, 切分点=1)
    return i

def 音值2音名when0eqc1(音值):
    '不含半#/b'
    C2B = 'CDEFGAB'
    name = _位置2名when0eqc1(C2B, 音值)
    return name


音名2音值when0eqc1_test_data = [
    ('c', -7),
    ('C', -14),
    ('c1', 0),
    ('C1', -21),
    ]
for _音名, _音值 in 音名2音值when0eqc1_test_data:
    assert 音名2音值when0eqc1(_音名) == _音值
    assert 音值2音名when0eqc1(_音值) == _音名


    
def 生成音名表():
    start = 音名2音值when0eqc1('A2')
    end = 音名2音值when0eqc1('c5') + 1

    ls = tuple(音值2音名when0eqc1(i) for i in range(start, end))
    assert len(ls) == 2 + 7*7 + 1

    idx_c1 = ls.index('c1')
    for 音值, 音名 in enumerate(ls, -idx_c1):
        assert 音值 == 音名2音值when0eqc1(音名)
        assert 音名 == 音值2音名when0eqc1(音值)

    return ls

音名表 = 生成音名表()

自然大调式音程间隔 = '全—全—半—全—全—全—半'
自然小调式音程间隔 = '全—半—全—全—半—全—全'
和声小调式音程间隔 = '全—半—全—全—半—增—半'
#?旋律小调式音程间隔 = '全—半—全—全—全—全—半'

def 音程间隔str2tuple(音程间隔):
    n2idx = '半全增'
    r = tuple((n2idx.index(n) + 1) for n in 音程间隔.split('—'))
    return r

def 调号音程间隔2调式(主音高度, 调式音程间隔):
    ls = 音程间隔str2tuple(调式音程间隔)
    assert sum(ls) == 12
    
    start = 键名2位置when0eqc1(主音高度)
    ls = accumulate(chain([start], ls[:-1]))
    ls = tuple(map(位置2键名when0eqc1, ls))
    return ls
assert 调号音程间隔2调式('C', 自然大调式音程间隔) == ('C', 'D', 'E', 'F', 'G', 'A', 'B')
assert 调号音程间隔2调式('G', 自然大调式音程间隔) == ('G', 'A', 'B', 'c', 'd', 'e', 'f#')





where_G谱号高音谱号_2线g1_when_1eqG_一线音高 = 13 #1=G 1^=g 1^^=g1=15@2线 14@1间 13@1线
where_F谱号低音谱号_4线f_when_1eqG_一线音高 = 1 #1=G 1^=g f=7@4线 1@1线
where_C谱号中音谱号_3线c1_when_1eqG_一线音高 = 7 #1=G 1^=g c1=11@3线 7@1线
where_C谱号活动谱号_X线c1_when_1eqG_一线音高 = lambda x: 13-2*x #1=G 1^=g c1=11@X线 13-2X@1线

def X线间2diffX线间1线(X线间):
    "X线间2subX线间1线('1线') == 0"
    "X线间2subX线间1线('1间') == 1"
    "X线间2subX线间1线('2线') == 2"
    "X线间2subX线间1线('2间') == 3"
    
    num = X线间[:-1]
    线间 = X线间[-1]

    num = int(num)
    num -= 1
    num *= 2

    i = '线间'.index(线间)
    diff = num + i
    return diff

def diffX线间1线2X线间(diffX线间1线):
    d = diffX线间1线
    if d & 1:
        n = d + 1
        n >>= 1
        return '{}间'.format(n)
    else:
        n = d + 2
        n >>= 1
        return '{}线'.format(n)

diffX线间1线2X线间_test_data = [
    (0, '1线'),
    (1, '1间'),
    (2, '2线'),
    (3, '2间'),
    ]
for _diff, _name in diffX线间1线2X线间_test_data:
    assert _name == diffX线间1线2X线间(_diff)
    assert _diff == X线间2diffX线间1线(_name)

def 计算一线音高(where_X线间音名, when_简谱音值eq音名):
    X线间, where音名 = where_X线间音名
    简谱音值, when音名 = when_简谱音值eq音名
    简谱音高 = 简谱音值 - 音名2音值when0eqc1(when音名) +\
           音名2音值when0eqc1(where音名) - X线间2diffX线间1线(X线间)
    return 简谱音高

计算一线音高_test_data = [
    (('2线', 'g1'), (1, 'G'), where_G谱号高音谱号_2线g1_when_1eqG_一线音高),
    (('4线', 'f'), (1, 'G'), where_F谱号低音谱号_4线f_when_1eqG_一线音高),
    (('3线', 'c1'), (1, 'G'), where_C谱号中音谱号_3线c1_when_1eqG_一线音高),
    ]
for _where, _when, _r in 计算一线音高_test_data:
    assert _r == 计算一线音高(_where, _when)
    

assert where_C谱号活动谱号_X线c1_when_1eqG_一线音高(3) == \
       计算一线音高(('3线', 'c1'), (1, 'G')) == \
       where_C谱号中音谱号_3线c1_when_1eqG_一线音高


def 音高转化(简谱音高, 一线音高):
    d = 简谱音高 - 一线音高
    return diffX线间1线2X线间(d)





简谱_仙剑一_雨 = r'''
3^_ 2^ 2^_1^_ 6. | 2^_ 1^ 2^_1^_ 6. | 2^_ 1^ 5^_2^_ 3^. | 2^_1^_ 1^_7_ 1^_7_ 6_5_ |

3^_ 2^ 2^_1^_ 6. | 2^_ 1^ 2^_1^_ 6. | 2^_ 1^ 5^_2^_ 3^. | 2^_1^_ 1^_7_ 1^_7_ 6_5_ |

4_6_ 4_6_ 4_6_ 4_6_ | 4_6_ 3^_2^_ 1^_7_ 6_5_ | 5_7_ 5_7_ 5_7_ 5_7_ | 5_7_ 5^_4^_ 3^_2^_ 1^_2^_ |

3^_3^_ 3^_3^_ 3^_3^_ 3^_3^_ | 3^_3^_ 3^_3^_ 3^_3^_ 4^_5^_ | 6^_6^_ 6^_6^_ 6^_6^_ 6^_1^^_ | 7^_7^_ 7^_7^_ 7^_7^_ 7^_2^^_ |

1^^_1^^_ 1^^_1^^_ 1^^_1^^_ 7^_1^^_ | 6^_6^_ 6^_6^_ 6^_6^_ 6^ | 6^_6^_ 6^_6^_ 6^_6^_ 6^_1^^_ | 7^_7^_ 7^_7^_ 7^_7^_ 6^_5^_ |

3^_#5^_ 3^_6^_ 3^_7^_ 3^_3^^_ | 3^_#5^_ 3^_6^_ 3^_7^_ 3^^_2^^_ | 6^_6^_ 6^_6^_ 6^_6^_ 6^_1^^_ | 7^_7^_ 7^_7^_ 7^_7^_ 7^_2^^_ |

1^^_1^^_ 1^^_1^^_ 1^^_1^^_ 7^ | 6^_6^_ 6^_6^_ 6^ 5^ | 6^_6^_ 6^_6^_ 6^_6^_ 6^_1^^_ | 7^_7^_ 7^_7^_ 7^_7^_ 6^_5^_ |

3^_#5^_ 3^_6^_ 3^_7^_ 3^_3^^_ | 3^_#5^_ 3^_6^_ 3^_7^_ 2^^_3^^_ |


'''

简谱_仙剑三_玉满堂 = r'''
0 0 0_5v_ 5_2_ | 3 3_4_ 2 2_3_ | 2--- | 3 3_2_ 3 5_6_ | 5-- 3_5_ | 

6 6_1^_ 6 5_3_ | 5-- 5_6_ | 1^ 1^_2^_ 3^ 2^_1^_ | 2^--- | 3^- 5_6_ 1^_2^_ | 

3^ 3^_2^_ 1^. 1^_ | 6 6_1^_ 6 3 | 5--- | 6 6_1^_ 6 1^_2^_ | 3^ 3^_2^_ 1^. 1^_ | 

6_1^_ 6_1^_ 2^_3^_ 5^_3^_ | 2^-- 1^_2^_ | 3^- 5_6_ 1^_2^_ | 3^ 3^_2^_ 1^. 1^_ | 6 6_1^_ 6_1^_ 5_3_ |

5-- 3_5_ | 6 6_1^_ 6 6_1^_ | 2^ 2^_3^_ 2^ 2^_3^_ | 5^_6^_ 3^_5^_ 2^_3^_ 1^_6_ | 1^--- |

'''

简谱_仙剑问情第一页 = r'''
1=C
4/4

start:
0 0 0 3_2_ | 3._0= 3_2_ 3._0= 3_2_ | 3_6_ 5_3_ 2._0= 1_2_ | 

3._0= 3_2_ 3._0= 3_2_ | 3_1^_ 6_5_ 3._0= 3_5_ | 6._0= 6_1^_ 6._0= 5_(3_ | 


3_) 2- 0_ 1_2_ | 3._0= 3_5_ 3._0= 3_(1_ | 1_) 2- 0_ 3_2_ | 

3._0= 3_2_ 3._0= 3_2_ | 3_6_ 5_3_ 2._0= 3_5_ | 6. 1^_ 6. 1^_ | 5_6_ 1^_7_ 6_5_ 3_5_ | 

(6- 6_)0_ 3_5_ | (6- 6_)0_ 3_5_ | 6_1^_ 6-- | (5- 5_)0_ 3_5_ | 6 6_1^_ 5. 3_ | 2. 0_ 5 2 | 

3. 6_ 5 2 | 3. 0_ 2 3_2_ | (1- 1_)0_ 2_1_ | 6v 1 2 3 | (5 5.=)0=_6_ 3 1 | 

(2 2.=)0_0=_ 3 5 | 6. 1^_ 5 3 | 2- 5 2 | 3. 6_ 5 3 | 5- 6 1^ | 2^- 6- | 

(5. 5=_)0=. 6 1^ | 3^ 2^ 1^ 5 | 6--- | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | 


'''


############################################################

def 比str(n, d):
    return '{}/{}'.format(n, d)

def 时长2str(时长):
    n = 时长.numerator
    d = 时长.denominator
    return 比str(n, d)

def parser简谱(简谱, *, 谱表=('2线', 'g1'), 大调简谱1键名=(1, 'c1'), \
             几拍每全音符=4, 几拍每节=4, 几拍每分钟=120):
    简谱 = 简谱.split('\nstart:')[-1]
    r = 简谱parser().parser(简谱)
    assert r != None
    data = 简谱ParserResultProcess().\
           process(r, Fraction(1, 几拍每节), Fraction(几拍每全音符, 几拍每节))

    一线音高 = 计算一线音高(谱表, 大调简谱1键名)

    str_ls = []
    for 小节 in data:
        ls = []
        for 拍 in 小节:
            for 连音 in 拍:
                变化, 音符, 时长, 连音记号始, 连音记号末 = 连音
                if isnan(音符):
                    音符 = '$$'
                else:
                    音符 = 音高转化(音符, 一线音高)
                时长 = 时长2str(时长)
                r = 变化, 音符, 时长, 连音记号始, 连音记号末
                r = ''.join(r)
                ls.append(r)
        str_ls.append(repr(ls))

    调性 = '{}大调'.format(大调简谱1键名[1][0].upper())
    比 = 比str(几拍每全音符, 几拍每节)
    速度 = '速度 = {}'.format(几拍每分钟)
    节数 = '节数 = {}'.format(len(str_ls))
    谱表 = ''.join(谱表)
    info = '\n'.join([调性, 比, 速度, 节数, 谱表])
    return str_ls, info

def _print(parser简谱_result):
    str_ls, info = parser简谱_result
    ms = '\n'.join(str_ls)
    print(info)
    print(ms)
    
    return

def test_简谱_仙剑三_玉满堂():
    r = parser简谱(简谱_仙剑三_玉满堂, 谱表=('2线', 'g1'), \
                      大调简谱1键名=(1, 'c1'),\
                      几拍每全音符=4, 几拍每节=4)
    _print(r)
    
    return


def test_简谱_仙剑问情第一页():
    r = parser简谱(简谱_仙剑问情第一页, 谱表=('1线', 'c1'), \
                      大调简谱1键名=(1, 'c1'),\
                      几拍每全音符=4, 几拍每节=4)
    _print(r)
    
    return


test_简谱_仙剑问情第一页()
    







