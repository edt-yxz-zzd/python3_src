'''remove line number'''
'''
1       package com.pulpfreepress.jfa.chapter1;
2
3       import java.util.*;
'''

import os.path as path
import io, os
import sand


def absPath(fname):
    fname = path.join('.', fname)
    fname = path.abspath(fname)
    return fname
def where(fname):
    return path.dirname(absPath(fname))

def _removeFirstChars(fin, fout, n):
    for line in fin:
        line = line[n:]
        if not line:
            line = '\n'
        fout.write(line)
        
def removeFirstChars(src, dst, n=8, open_mod='x'):
    assert open_mod in 'wx'
    
    with open(src) as fin:
        if isinstance(dst, io.IOBase):
            fout = dst
            _removeFirstChars(fin, fout, n)
        else:
            sand.makedirs(where(dst))
            with open(dst, open_mod) as fout:
                _removeFirstChars(fin, fout, n)


        


def main(args = None):
    import argparse, sys

    dst = '<sys.stdout>'
    parser = argparse.ArgumentParser(description='remove line number in source file')
    parser.add_argument('source', type=str, nargs=1,
                        help='source file name')

    parser.add_argument('destination', type=str, nargs='?', default=dst,
                        help='file name for output')
    '''
    parser.add_argument('destination', nargs='?', \
                        type=argparse.FileType('w'),\
                        default=sys.stdout, \
                        help='file name for output')'''
    
    parser.add_argument('length', type=int, nargs='?', default=8,
                        help='the length of string to remove from start of each line')
    
    parser.add_argument('-f', action='store_true',
                        help='overwrite file if destination file exists')

    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    
    args.source = args.source[0]
    if args.destination == dst:
        args.destination = sys.stdout
    
        
    open_mod = 'w' if args.f else 'x'
    removeFirstChars(args.source, args.destination, \
                     args.length, open_mod=open_mod)

    


if __name__ == "__main__":
    main()

