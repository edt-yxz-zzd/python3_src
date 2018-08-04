

import ast
import io
import glob
import itertools
import os.path


'''
def sources2ifnames(srcs):
    return itertools.chain.from_iterable(glob.iglob(src) for src in srcs)

def sources2fnames(srcs):
    fnames = set(os.path.abspath(path) for path in sources2ifnames(srcs))
    ls = list(fnames)
    ls.sort()
    return ls
'''

def sources2ifnames(srcs):
    return itertools.chain.from_iterable(
        sorted(glob.iglob(src)) for src in srcs)

def sources2fnames(srcs):
    return list(sources2ifnames(srcs))



def con_txts2bin(fnames, in_encoding, fout, out_encoding):
    for fname in fnames:
        with open(fname, encoding=in_encoding) as fin:
            txt = fin.read()
        fout.write(txt.encode(out_encoding))
    return


def write_bytes2txt(fout, bs):
    txt = bs.decode(fout.encoding)
    fout.write(txt)
def write_bytes2bin(fout, bs):
    fout.write(bs)


def con_bins2bin(fnames, fout, head=b'', tail=b'', join=b''):

    write_f = write_bytes2txt if isinstance(fout, io.TextIOBase) \
              else write_bytes2bin

    is_first = True
    write_f(fout, head)
    for fname in fnames:
        with open(fname, 'rb') as fin:
            bs = fin.read()
        assert type(bs) is bytes
        
        if is_first:
            is_first = False
        else:
            write_f(fout, join)
        write_f(fout, bs)

    
    write_f(fout, tail)
    return


def literal2bytes(s):
    bs = ast.literal_eval("b'{}'".format(s))
    return bs

def main(args=None):
    
    import argparse, sys, os.path
    

    parser = argparse.ArgumentParser(description='concate files into one file')
    parser.add_argument('-m', '--mode', type=str, default='x',
                        choices=['w', 'x', 'a'],
                        help='open mode of output file')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='output file name')
    parser.add_argument('-S', '--start_of_all', type=str, default='',
                        help='head of each src')
    parser.add_argument('-s', '--start', type=str, default='',
                        help='head of all')
    parser.add_argument('-t', '--tail', type=str, default='',
                        help='tail of each src')
    parser.add_argument('-T', '--tail_of_all', type=str, default='',
                        help='tail of all')
    parser.add_argument('-j', '--join', type=str, default='',
                        help='bytes between srcs')
    parser.add_argument('sources', type=str, nargs='+',
                        help='binary file names')

    args = parser.parse_args(args)
    mode = args.mode + 'b'
    fnames = sources2fnames(args.sources)

    headall = literal2bytes(args.start_of_all)
    head = literal2bytes(args.start)
    tail = literal2bytes(args.tail)
    tailall = literal2bytes(args.tail_of_all)
    join = literal2bytes(args.join)

    join = tail + join + head
    head = headall + head
    tail = tail + tailall
    if args.output:
        fout = open(args.output, mode)
        with fout:
            con_bins2bin(fnames, fout, head=head, tail=tail, join=join)
    else:
        fout = sys.stdout
        con_bins2bin(fnames, fout, head=head, tail=tail, join=join)

    return


if '__main__' == __name__:
    main()
    pass














    
