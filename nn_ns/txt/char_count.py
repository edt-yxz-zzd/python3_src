

'''
count char

output format:
    (last modified time + size + input file + newline)*
    <empty line>
    (total NNN + newline)?
    <empty line>
    (char count + newline)*

input text file
-a old_output file as input
-o output file
'''
__all__ = ('''
    calc_total total2str char2count_to_str
    record2str st_time2datetime
    fname2record fname_to_char2count
    fnames2output_head fnames_to_char2count
    main_impl1 main_impl2
    read_outputfile read_outputfiles
    char_count_rex is_emptyline read_char_count read_total total_rex
    path_patterns2iter_paths fname_patterns2iter_fnames
''').split()


from sand import fixed__package__
fixed__package__(globals())
from sand import top_level_import
assert top_level_import(__name__, 'import_main.forgot_import', args=('logic error',))
assert top_level_import(__name__, 'import_main.collect_globals',
        kwargs=dict(pred=None, include='', exclude='''
    main'''))


from collections import Counter
import os, re, glob
from datetime import datetime
from sand.big.makedirs import absPath
from sand import exc_addargs



##def count_char(char2count, txt):
##    for ch in txt:
##        char2count[ch] += 1

def st_time2datetime(st_time:'time in sec'):
    date_time = datetime.fromtimestamp(st_time)
    return date_time.replace(microsecond=0)
##def fname_to_char2count(fname, encoding):
##    try:
##        return _fname_to_char2count(fname, encoding)
##    except Exception as e:
##        raise Exception(fname, encoding, e)

@exc_addargs
def fname_to_char2count(fname, encoding):
    with open(fname, 'r', encoding=encoding) as fin:
        return Counter(fin.read())


def fnames_to_char2count(fnames, encoding, *, dels = '\n'):
    d = Counter()
    for fname in fnames:
        c2c = fname_to_char2count(fname, encoding)
        d.update(c2c)

    for ch in dels:
        if ch in d:
            del d[ch]
    return d

def calc_total(char2count):
    return sum(char2count.values())


def fname2record(fname):
    fname = absPath(fname)
    statinfo = os.stat(fname)
    fsize = statinfo.st_size
    fmtime = st_time2datetime(statinfo.st_mtime)
    return fmtime, fsize, fname

def char2count_to_str(c2c, length=None):
    return '\n'.join('{}:{}'.format(ch, n)
                     for ch, n in c2c.most_common()[:length])
char_count_rex = re.compile(r'(.):(\d+)\n?')

def read_char_count(char_count_str):
    m = re.match(char_count_rex, char_count_str)
    if m:
        ch, count = m.group(1, 2)
        count = int(count)
    else:
        raise ValueError('not (char:count) : {!r}'.format(char_count_str))
    return ch, count
    
def record2str(record):
    return '{} {}B {}'.format(*record)

def fnames2output_head(fnames):
    records = map(fname2record, fnames)
    return '\n'.join(map(record2str, records))

def total2str(total):
    return 'total {}'.format(total)

total_rex = re.compile(r'total (\d+)\n')
assert type(total_rex.pattern) is str
def read_total(total_num_str):
    m = re.match(total_rex, total_num_str)
    if m:
        total = int(m.group(1))
    else:
        raise ValueError('bad format: not {!r}'.format(total_rex.pattern))

    return total


def is_emptyline(line):
    return line.isspace() or not line
##
##def read_outputfile(fname, encoding):
##    try:
##        return _read_outputfile(fname, encoding)
##    except ValueError as e:
##        raise ValueError(fname, e)

@exc_addargs
def read_outputfile(fname, encoding):
    with open(fname, encoding=encoding) as fin:
        fin = iter(fin)
        # read head/records
        records = []
        for record in fin:
            if is_emptyline(record):
                break
            records.append(record)

        # read head/total
        total = None
        for total_num in fin:
            total = read_total(total_num)
            #print(repr(total_num))
            break
        if total is None:
            raise ValueError('bad format: no "total"')

        
        for emptyline in fin:
            if not is_emptyline(emptyline):
                raise ValueError('bad format: not emptyline follows "total"')
            break
        else:
            raise ValueError('bad format: no emptyline follows "total"')


        # read (char count)
        char_count_pairs = []
        for char_count in fin:
            ch, count = read_char_count(char_count)
            char_count_pairs.append((ch, count))


        c2c = dict(char_count_pairs)
        if not len(c2c) == len(char_count_pairs):
            raise ValueError('not len(c2c) == len(char_count_pairs)')

        if not calc_total(c2c) == total:
            raise ValueError('not sum(c2c.values()) == total')

        return records, c2c



def read_outputfiles(fnames, encoding):
    records = []
    c2c = Counter()
    for fname in fnames:
        records_, c2c_ = read_outputfile(fname, encoding)
        records.extend(records_)
        c2c.update(c2c_)

    return records, c2c




def main_impl1(outputfiles, oencoding, inputfiles, iencoding,
               no_head=False, length=None):
    records, c2c = read_outputfiles(outputfiles, oencoding)
    c2c.update(fnames_to_char2count(inputfiles, iencoding))
    head = ''.join(records)
    head += fnames2output_head(inputfiles)
    total = calc_total(c2c)

    total_str = total2str(total)
    c2c_str = char2count_to_str(c2c, length=length)

    emptyline = ''
    if no_head:
        return c2c_str
    return '\n'.join([head, emptyline, total_str, emptyline, c2c_str])


def main_impl2(output_txt, output_fname, encoding):
    with open(output_fname, 'x', encoding=encoding) as fout:
        fout.write(output_txt)


def path_patterns2iter_paths(path_patterns):
    for path_pattern in path_patterns:
        yield from glob.glob(path_pattern)
def fname_patterns2iter_fnames(fname_patterns):
    import sys
    for path in path_patterns2iter_paths(fname_patterns):
        if os.path.isdir(path):
            print('os.path.isdir(path): {!r}'.format(path), file=sys.stderr)
        else:
            yield path

def main(args=None):
    import argparse, sys
    from sand import text_encoding

    parser = argparse.ArgumentParser(description='count char')
    parser.add_argument('inputs', metavar='FILE_NAME',
                        type=str, nargs='+',
                        help='file to count')
    parser.add_argument('-a', '--append', type=str,
                        dest='appends', metavar='FILE_NAME',
                        action='append', default=[],
                        help='previous output file; append the counts')
    parser.add_argument('-o', '--output', type=str, 
                        default=sys.stdout,
                        help='output file')
    parser.add_argument('-oe', '--output_encoding', type=str, 
                        default=text_encoding,
                        help='encoding for output file')
    parser.add_argument('-ie', '--input_encoding', type=str, 
                        default=text_encoding,
                        help='encoding for input files')
    parser.add_argument('-f', '--force_write',
                        action='store_const', const='w',
                        default='x',
                        help='force to write to output file')
    parser.add_argument('-EH', '--exclude_head', dest = 'no_head',
                        action='store_true',
                        default=False,
                        help='not output head')
    parser.add_argument('-IH', '--include_head', dest = 'no_head',
                        action='store_false',
                        default=False,
                        help='output head')
    parser.add_argument('-L', '--length',
                        type=int,
                        default=None,
                        help='output first L chars; 0 stands for all')

    args = parser.parse_args(args)

    if args.length is not None and args.length == 0:
        args.length = None
        

    outputfiles = fname_patterns2iter_fnames(args.appends)
    inputfiles = fname_patterns2iter_fnames(args.inputs)
    iencoding = args.input_encoding
    oencoding = args.output_encoding
    txt = main_impl1(outputfiles, oencoding, inputfiles, iencoding,
                     no_head=args.no_head, length=args.length)
    if isinstance(args.output, str):
        fout = open(args.output, args.force_write,
                    encoding=args.output_encoding)
        with fout:
            fout.write(txt)
    else:
        args.output.write(txt)
    
    parser.exit(0)
    raise logic-error




    

if __name__ == "__main__":
    main()

    


















































        


















                    















        
















