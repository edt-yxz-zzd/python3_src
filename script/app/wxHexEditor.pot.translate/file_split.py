


def file_split(file, num_char_per_split, max_num_char_per_line):
    if max_num_char_per_line < 0:
        raise ValueError('max_num_char_per_line < 0')
    if num_char_per_split < max_num_char_per_line:
        raise ValueError('num_char_per_split < max_num_char_per_line')
    '''
    def iter(file):
        for line in file:
            print(line)
            yield line
    '''
    it = iter(file)
    while True:
        yield file_split1(it, num_char_per_split, max_num_char_per_line)
def file_split1(iter_lines, num_char, max_num_char_per_line):
    num_char -= max_num_char_per_line
    ls = []
    it = iter_lines
    while num_char > 0:
        # bug: when raise the remain ls were not return yet!
        # line = next(it) # will raise StopIteration for file_split

        try:
            line = next(it)
        except StopIteration:
            if ls: return ls
            else: raise
        ls.append(line)
        num_char -= len(line)
    return ls

prefix_fmt = './po/{:0<2}.po'
with open('zh_CN.po', encoding='utf8') as fin:
    for i, lines in enumerate(file_split(fin, 5000, 100)):
        out_name = prefix_fmt.format(i*10)
        with open(out_name, 'w', encoding='utf8') as fout:
            for line in lines:
                fout.write(line)

