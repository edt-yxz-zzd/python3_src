
'''
单字－郑码

先由char2count找出高频字
再由‘极点郑码’码表作映射
最后结果是‘str_char2zm_ls_small.txt’
'''


__all__ = ['char2zm_ls']

import configparser
from collections import defaultdict
from sand import skip_BOM_for_TextIO, write_txt, intersect_keys, read_txt,\
     is_CJK_char, escape_char
import os



#this_dir = os.path.dirname(__file__) + '/'
output_dir = '.' # will append to real output_path
char2count_file = r'char2count__from_novel__L0.txt'
zm_path = r'E:\book\数据' '\\'
zm_file = zm_path + r'极点郑码7格式吴准少大字集词库_err.utf_16_le'
zm_encoding = 'utf_16_le'
first_line = '\ufeff[Description]\n' # not skip BOM

char2zm_ls_objs_file = 'char2zm_ls.objs.py'
str_char2zm_ls_txt_file = 'str_char2zm_ls.txt'
str_char2zm_ls_small_txt_file = 'str_char2zm_ls_small.txt'
zhcn_e = 'gb18030'

from sand import default_WorkingPath
default_WorkingPath.fix_paths('output', globals(),
                              '''
    output_dir
    char2count_file
    char2zm_ls_objs_file
    str_char2zm_ls_txt_file
    str_char2zm_ls_small_txt_file
''')
joiner = default_WorkingPath.joiner__variables(output_dir) # exported
#joiner(globals(), 'char2count_file')



def get_char2zm_ls(zm_file):
    config = configparser.ConfigParser(delimiters=('=', ':', ' '),
                                       comment_prefixes=('#', ';', '----', '★★★'))

    with open(zm_file, encoding=zm_encoding) as fin:
        config.read_file(skip_BOM_for_TextIO(fin))
    ##    for line in skip_BOM_for_TextIO(fin):
    ##        print(repr(line))
    ##        break
    ##raise


    char2zm_ls = defaultdict(list)
    for zm, words in config['Text'].items():
        words = words.split()
        words = [word for word in words
                 if len(word)==1 or (len(word) == 2 and word.startswith('~'))]
        
        for word in words:
            char = word[-1]
            char2zm_ls[char].append(zm)
    if '?' in char2zm_ls:
        del char2zm_ls['?']
    return dict(char2zm_ls)
#print(len(char2zm_ls)) # 21751






def write_obj_repr(fname, obj_name, obj_repr, encoding=None):
    txt = '{} = {}'.format(obj_name, obj_repr)
    bs = txt.encode(encoding = encoding)
    with open(fname, 'xb') as fout:
        fout.write(bs)
def read_objs_file(fname, encoding=None):
    with open(fname, 'r', encoding = encoding) as fin:
        src = fin.read()
    globals = {}
    exec(src, globals, globals)
    return globals


def char_zm_ls_pairs_to_str(char_zm_ls_pairs):
    lines = []
    for char, zm_ls in char_zm_ls_pairs:
        line = '{}={}'.format(char, ' '.join(zm_ls))
        lines.append(line)

    str_char2zm_ls = '\n'.join(lines)
    return str_char2zm_ls

if 0:
    char2zm_ls = get_char2zm_ls(zm_file)
    str_char2zm_ls = char_zm_ls_pairs_to_str(char2zm_ls.items())
    


if 0:
    write_obj_repr(char2zm_ls_objs_file, 'char2zm_ls', repr(char2zm_ls),
                   encoding=zhcn_e)
if 0:
    write_txt(str_char2zm_ls_txt_file, str_char2zm_ls, zhcn_e)


try:
    char2zm_ls = read_objs_file(char2zm_ls_objs_file, zhcn_e)['char2zm_ls']
    if '?' in char2zm_ls:
        del char2zm_ls['?']
    str_char2zm_ls = read_txt(str_char2zm_ls_txt_file, zhcn_e)
except Exception as e:
    print(str(e)[:1000])





def get_frequent_chars(char2count_file, encoding='gb18030'):
    with open(char2count_file, encoding=encoding) as fin:
        chars = (line[0] for line in fin)
        chars = ''.join(filter(is_CJK_char, chars))
    return chars



def char2count_file_to_frequent_chars(char2count_file, *, oprint = print):
    import io
    output = io.StringIO()
    def print(*args, **kwargs):
        oprint(*args, file=output, **kwargs)
    chars = get_frequent_chars(char2count_file)
    #chars = ''.join(chars)
    L = len(chars)
    N = 25
    for i in range(0, L, N):
        try:
            if i == 6550:
                raise ValueError
            print(chars[i:i+N])
        except:
            #print(i)
            assert i == 6550
            cs = chars[i:i+N]
            oprint(escape_char(cs[16]))
            assert escape_char(cs[16]) == r'\U00020131'
            print(cs[:16], escape_char(cs[16]), cs[17:], sep='')
            pass
    #print(repr(chars))
    print = oprint
    s = output.getvalue()
    assert len(s) == len(chars) + 2+8-1 + (L+N-1)//N
    ss = "{} = ''.join('''\n{}'''.split())".format('frequent_chars__from_novel__L0', s)
    return ss


if 0:
    print('get_frequent_chars from {!r}'.format(char2count_file))
    ss = char2count_file_to_frequent_chars(char2count_file)
    print(ss)
    raise

    #chars = '，的。 一\u3000了是不“”这我人有在他道来大个你就着…到上也那？说下然：出么之子看时！可地要们没过后为都她自中还天心小得去对和只能里以头会起想手身好如而无面些声眼事李什笑却己知前多已真经现但将意开气力生—张点样所情白此话方.间让被两军见家很女清才神又回当发于、再明动从风老正三长成年几把十法打实星少色口主本光用向死定其太最听问给次王边住~门觉走便脸战原何行种进果等高重儿分直怎全衣水公外山啊候做同杀更微相'
    from frequent_chars__from_novel__L0 import frequent_chars__from_novel__L0 as chars
    # before 擞, count>=100, after/include 擞, count<100
    assert 4209 == chars.index('擞')


    char2zm_ls_small = intersect_keys(char2zm_ls, chars)
    str_char2zm_ls_small = char_zm_ls_pairs_to_str(sorted(char2zm_ls_small.items()))

    write_txt(str_char2zm_ls_small_txt_file, str_char2zm_ls_small, zhcn_e)































