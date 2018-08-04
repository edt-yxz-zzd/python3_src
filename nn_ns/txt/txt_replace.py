

from seed.io.read_txt import read_txt
from seed.filesys.file_rename import write_force
from os import remove, path

import re # sub split


def replace_str_str(string, str_find, str_replace):
    r = string.replace(str_find, str_replace)
    return r

def replace_re_str(string, re_pattern, str_replace):
    ls = re.split(re_pattern, string)
    r = str_replace.join(ls)
    return r

def replace_re_re(string, re_pattern, re_str_replace):
    r = re.sub(re_pattern, re_str_replace, string)
    return r

    

def txt_replace_f(src, dst, encoding, transform):
    txt = read_txt(src, encoding)
    txt = transform(txt)
    write_force(dst, txt, encoding)
    return




def main(args = None):
    method_choices = ['ss', 'rs', 'rr']
    
    import argparse, sys

    parser = argparse.ArgumentParser(description='txt replace')
    parser.add_argument('source', type=str, help='source')

    parser.add_argument('destination', type=str,
                        nargs='?', default=None,
                        help='destination (default to <source>)')
    
    parser.add_argument('-f', '--find', type=str, required=True,
                        help='finding string')
    parser.add_argument('-r', '--replace', type=str,
                        default='',
                        help='replacing string')
    
    parser.add_argument('-m', '--method', type=str,
                        choices=method_choices,
                        default=method_choices[0],
                        help='use the finding|replacing string as string or regular expression')
    parser.add_argument('-e', '--encoding', type=str,
                        default='utf8',
                        help='encoding of source and destination')
    

    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)


    src = args.source
    dst = args.destination
    if dst == None:
        dst = src

    method = args.method
    d = {'s':'str', 'r':'re'}
    types = [d[m] for m in method]
    method_name = 'replace_{}_{}'.format(*types)
    
    replace_x_x = eval(method_name)
    f = lambda string: replace_x_x(string, args.find, args.replace)

    encoding = args.encoding
    txt_replace_f(src, dst, encoding, f)
    return

    


if __name__ == "__main__":
    main()

    

