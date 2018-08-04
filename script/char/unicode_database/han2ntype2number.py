

from seed.io.iter_line_contents import filter_py_line_contents
from seed.io.RCXW import make_rcxw__pickle
from pprint import pprint
from replace_unicode import replace_unicode
from collections import defaultdict
from itertools import chain


ifname = 'Unihan_NumericValues_9_0.txt'
iencoding = 'utf8'
ofname = 'han2ntype2number.py.obj'


numeric_types = '''
    kAccountingNumeric
    kOtherNumeric
    kPrimaryNumeric
    '''.split()

def parse_line(line):
    han, numeric_type, num = line.split('\t')
    assert len(han) == 1
    assert numeric_type in numeric_types
    num = int(num)
    return han, numeric_type, num
def iter_parse_file(fin):
    for line in filter_py_line_contents(fin):
        line = replace_unicode(line)
        yield parse_line(line)

def _make():
    with open(ifname, encoding=iencoding) as fin:
        ls = list(iter_parse_file(fin))
    d = defaultdict(dict)
    for han, ntype, num in ls:
        dh = d[han]
        assert ntype not in dh
        dh[ntype] = num
    han2ntype2number = dict(d)
    return han2ntype2number


han2ntype2number = make_rcxw__pickle(_make, ofname)()
assert 73 == len(han2ntype2number)
all_numeric_han_chars = ''.join(sorted(han2ntype2number.keys()))

if 0:
    pprint(han2ntype2number)





