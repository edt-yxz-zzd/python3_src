
r'''
1000^1 => KB - kilobyte
1000^2 => MB - megabyte
1000^3 => GB - gigabyte
1000^4 => TB - terabyte
1000^5 => PB - petabyte
1000^6 => EB - exabyte
1000^7 => ZB - zettabyte
1000^8 => YB - yottabyte

1024^1 => KiB - kibibyte
1024^2 => MiB - mebibyte
1024^3 => GiB - gibibyte
1024^4 => TiB - tebibyte
1024^5 => PiB - pebibyte
1024^6 => EiB - exbibyte
1024^7 => ZiB - zebibyte
1024^8 => YiB - yobibyte
'''
epilog_str = __doc__
from decimal import Decimal, getcontext
from fractions import Fraction
from math import ceil, log10

initials = 'KMGTPEZY'

def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(
                description='show KB KiB for <num> bytes'
                , epilog=epilog_str
                , formatter_class=argparse.RawDescriptionHelpFormatter
                )
    parser.add_argument('size', type=int
                        , help='size in bytes')
    '''
    parser.add_argument('-prec', '--precision', type=int
                        , default=None
                        , help='precision for float point computation')

    args = parser.parse_args()


    may_precision = args.precision
    if may_precision is not None:
        usr_precision = may_precision
        if usr_precision < 0: raise ValueError('precision < 0')
    else:
        usr_precision = getcontext().prec
    '''
    args = parser.parse_args()


    size = args.size
    if size < 0: raise ValueError('size < 0')
    # set usr_precision before Decimal(size)!!!
    #size = Decimal(size)
    #size = Fraction(size)
    assert type(size) is int and size >= 0

    base_XB = 10**3
    size_XB = size

    #base_XiB = 2**10
    #size_XiB = size

    base_N_XiB = 5**10
    base_D_XiB = 10**10
    size_N_XiB = size
    size_D_XiB = 1


    L = len(initials)
    eval_precision = ceil(log10(size_N_XiB * base_N_XiB ** L)) + 10*L + (50)
    getcontext().prec = eval_precision

    print(f'{size} B')
    for initial in initials:
        size_XB /= base_XB
        #size_XiB /= base_XiB
        size_N_XiB *= base_N_XiB
        size_D_XiB *= base_D_XiB
        size_XiB = Decimal(size_N_XiB)/size_D_XiB

        #getcontext().prec = usr_precision
        print()
        print(f'{size_XB} {initial}B')
        print(f'{size_XiB} {initial}iB')
        getcontext().prec = eval_precision

        #print(f'{Decimal(size_XB)} {initial}B')
        #print(f'{Decimal(size_XiB)} {initial}iB')

    return



if __name__ == "__main__":
    main()

