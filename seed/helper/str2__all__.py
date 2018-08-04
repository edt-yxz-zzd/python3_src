
"""
usage:
    __all__ = str2__all__('''
        str2__all__ # str -> [word]
        xxx, xxx
        yyy  zzz
        XXX
            YYY;
                ,UUU # xxxalaj afd
            ZZZ:
        KKK(XXX,YYY)
        ''')
"""

__all__ = '''
    str2__all__
    '''.split()
from io import StringIO
import re

#nonword1s_re = re.compile('[^a-zA-Z0-9_]+')
word1s_re = re.compile('[a-zA-Z0-9_]+')
def str2__all__(s):
    '''str -> [word]

def str2__all__(s)
    lines = io.StringIO(s)
    for line in lines:
        line, _, _ = line.lpartition('#')
        line.replace_nonword(' ')
        new_lines.append(line)
    s = ' '.join(new_lines)
    return list(set(s.split()))
'''
    lines = StringIO(s)
    all_words = []
    for line in lines:
        line, _, _ = line.partition('#')
        #words = nonword1s_re.split(line)
        #all_words.extend(filter(None, words))
        words = word1s_re.findall(line)
        all_words.extend(words)
    all_words = list(set(all_words))
    if not all(map(str.isidentifier, all_words)):
        bad_words = [w for w in all_words if not w.isidentifier()]
        raise ValueError(f'not identifier: {bad_words} @str2__all__')
    return all_words


def _t():
    s = '''
    xxx yyy,zzz # ooo1
    # ooo2
    x1#
    x2
        x3:
      x4@%$%&&x5%&%*x6
      ,x6

'''
    R = ['x3', 'x2', 'x1', 'x4', 'yyy', 'x5', 'xxx', 'zzz', 'x6']
    #print(str2__all__(s))
    r = str2__all__(s)
    assert type(r) is list # not tuple
    assert len(R) == len(r)
    assert set(R) == set(r)


if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()
