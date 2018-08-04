
from root.henzi_used import isChineseChar, num2hz_int2gb, hz2num_gb2int

zmlsfname = 'zmls.txt'
hz_zms_fname = 'hz_zms.txt'
fname = '极点郑码词库gb18030.txt'
encoding = 'gb18030'

special_prefix = '!~^'

def jdzmck2zmls(fname=fname, encoding=encoding, special_prefix=special_prefix):
    ls = []
    with open(fname, encoding=encoding) as fin:
        ifin = iter(fin)
        for line in ifin:
            if line == '[Text]\n':
                break
        for line in ifin:
            line = line[:-1]
            words = line.split(' ')
            
            zm = words[0]
            words = [(word[1:], word[0]) if len(word) > 1 and word[0] in special_prefix
                     else (word, '') for word in words[1:]]
            
            chars = [(word, pre) for word, pre in words if len(word) == 1 and isChineseChar(word)]
            if chars:
                ls.append((zm, chars))



    d = dict(ls)
    assert len(d) == len(ls)

    return ls

def gen_zmls_file(ofname=zmlsfname):
    zmls = jdzmck2zmls()

    with open(ofname, 'x', encoding=encoding) as fout:
        for zm, chars in zmls:
            s = '{} {!r}\n'.format(zm, chars)
            fout.write(s)


def read_zmls_file(fname=zmlsfname):
    zmls = []

    with open(fname, encoding=encoding) as fin:
        for line in fin:
            line = line[:-1]
            zm, chars = line.split(' ', 1)
            chars = eval(chars)
            zmls.append((zm, chars))
    return zmls







zmls = read_zmls_file()

        
        

