
__all__ = '''
    default_iter_read_a_d

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

hanzi_or_num_pattern = r'(?:\D|\d{5})' # num is not unicode!!!!!
a_d_line_pattern = fr'(?P<key>{hanzi_or_num_pattern}):(?P<case>a|d)\((?P<components>{hanzi_or_num_pattern}(?:,{hanzi_or_num_pattern})+)\)'
a_d_line_rex = re.compile(a_d_line_pattern)
def hanzi_or_num_str2hanzi_or_num(hanzi_or_num_str):
    # -> (hanzi|int)
    assert len(hanzi_or_num_str) in (1,5)
    if len(hanzi_or_num_str) == 1:
        hanzi = hanzi_or_num_str
        hanzi_or_num = hanzi
    else:
        num_str = hanzi_or_num_str
        num = int(num_str)
        #bug!: hanzi = chr(num)
        hanzi_or_num = num
    return hanzi_or_num

def iter_read_a_d(ifile):
    '-> Iter (hanzi|int, ("a"|"d", [(hanzi|int)]))'
    f = hanzi_or_num_str2hanzi_or_num
    for line in ifile:
        line = line.strip()
        m = a_d_line_rex.fullmatch(line)
        if m:
            key = f(m['key'])
            case = m['case']
            components_str = m['components']
            components = components_str.split(',')
            components = list(map(f, components))
            yield key, (case, components)

def default_iter_read_a_d():
    '-> Iter (hanzi|int, ("a"|"d", [(hanzi|int)]))'
    with open(Global.ipath, encoding=Global.iencoding) as fin:
        yield from iter_read_a_d(fin)


