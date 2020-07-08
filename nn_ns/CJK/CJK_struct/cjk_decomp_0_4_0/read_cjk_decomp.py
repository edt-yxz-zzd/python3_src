
__all__ = '''
    default_iter_read_cjk_decomp
    default_iter_read_a_d

    iter_read_cjk_decomp
    iter_read_a_d
    '''.split()

import re
from pathlib import PurePath as Path
this_file = Path(__file__)
this_folder = this_file.parent
this_file_name = this_file.name

class Global:
    ifname = 'cjk-decomp-0.4.0.txt'
    ipath = this_folder / ifname
    iencoding = 'utf8'

hanzi_or_num_pattern = r'(?:\D|\d+)' # num is not unicode!!!!!
line_pattern = fr'(?P<key>{hanzi_or_num_pattern}):(?P<case>[^(]+)\((?P<components>(?:{hanzi_or_num_pattern}(?:,{hanzi_or_num_pattern})*)?)\)'
line_rex = re.compile(line_pattern)
def hanzi_or_num_str2hanzi_or_num(hanzi_or_num_str):
    # -> (hanzi|int)
    try:
        assert len(hanzi_or_num_str) in (1,5)
    except:
        print(f'{hanzi_or_num_str!r}')
        raise
    if len(hanzi_or_num_str) == 1:
        hanzi = hanzi_or_num_str
        hanzi_or_num = hanzi
    else:
        num_str = hanzi_or_num_str
        num = int(num_str)
        #bug!: hanzi = chr(num)
        hanzi_or_num = num
    return hanzi_or_num

def iter_read_cjk_decomp(ifile):
    '-> Iter (hanzi|int, (case, [(hanzi|int)]))'
    f = hanzi_or_num_str2hanzi_or_num
    for line in ifile:
        line = line.strip()
        if not line: continue
        m = line_rex.fullmatch(line)
        if m:
            key = f(m['key'])
            case = m['case']
            components_str = m['components']
            components_str = components_str.strip()
            if not components_str:
                components = []
            else:
                components = components_str.split(',')
                components = list(map(f, components))
            yield key, (case, components)
        else:
            raise Exception(f'{line!r}')

_global_iter_read_cjk_decomp = iter_read_cjk_decomp
def default_iter_read_cjk_decomp(iter_read_cjk_decomp=None):
    '-> Iter (hanzi|int, (case, [(hanzi|int)]))'
    if iter_read_cjk_decomp is None:
        iter_read_cjk_decomp = _global_iter_read_cjk_decomp
    with open(Global.ipath, encoding=Global.iencoding) as fin:
        yield from iter_read_cjk_decomp(fin)

def iter_read_a_d_from_iter(iterable):
    return (x for x in iterable if x[1][0] in 'a(d')
def iter_read_a_d(ifile):
    return iter_read_a_d_from_iter(iter_read_cjk_decomp(ifile))
def default_iter_read_a_d():
    return default_iter_read_cjk_decomp(iter_read_a_d)
    return iter_read_a_d_from_iter(default_iter_read_cjk_decomp())




