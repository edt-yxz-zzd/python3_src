
r'''
there are bugs in python!
    when parse .py include all_similar_chars.u8 as str, decode fail!
now I have to read from file

'''

def _make():
    return ''.join(_make_iter())
def _make_iter():
    with open('similar-chars-html.txt', encoding='utf-8') as fin:
        lines = iter(fin)
        # skip first 3 line
        list(zip(range(3), lines))
        for line in lines:
            if not line or line.isspace():
                continue
            ch = line[0]
            if ch == 'n':
                ch = '\U0002FA1A'
            yield ch

output_filename = 'all_similar_chars.u8'
oencoding = 'utf-8'

if 0:
    all_similar_chars = _make()
    L = len(all_similar_chars)
    print(L)
    from seed.io.read_txt import write_txt
    #print(all_similar_chars)
    write_txt(output_filename, all_similar_chars, encoding=oencoding)
elif 0:
    L = 593
    all_similar_chars = '<output_filename>'
    # parse fail at above line

from seed.io.read_txt import read_or_calc_xwrite__txt
all_similar_chars = \
    read_or_calc_xwrite__txt(output_filename, _make, encoding=oencoding)

L = 593
assert len(all_similar_chars) == L





