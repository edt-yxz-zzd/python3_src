

'''
ctrl+D or ctrl+Z to EOF stdin
    before and after it should have no chars
    or <Enter>+<Ctrl_Z>+<Enter>
'''


import hashlib

'''
hashlib.new(name)

hashlib.algorithms_guaranteed
hashlib.algorithms_available
hash.update(arg)
hash.hexdigest()
'''

def hash_file(name, fin):
    m = hashlib.new(name)
    sz = max(m.block_size, 1024)
    while True:
        bs = fin.read(sz)
        if not bs: break
        #rint(bs)
        m.update(bs)
    return m.hexdigest()


def main(argv=None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='hash file')
    parser.add_argument('-n', '--algorithm_name', type=str
                        , help='name of algorithm used to hash')
    parser.add_argument('-i', '--input', type=str
                        , help='input file to hash')
    parser.add_argument('-E', '--expected_result', type=str
                        , help='compare with expected hexdigest result')
    parser.add_argument('-g', '--algorithms_guaranteed'
                        , action='store_true'
                        , help='show guaranteed algorithm names')
    parser.add_argument('-a', '--algorithms_available'
                        , action='store_true'
                        , help='show available algorithm names')
    args = parser.parse_args()
    if args.algorithms_guaranteed:
        print(sorted(hashlib.algorithms_guaranteed))
    if args.algorithms_available:
        print(sorted(hashlib.algorithms_available))

    if args.algorithms_available or args.algorithms_guaranteed:
        result = None
    else:
        name = args.algorithm_name
        if name is None:
            raise Exception('should offer algorithm_name')

        if args.input is None:
            fin = sys.stdin.buffer
            result = hash_file(name, fin)
        else:
            with open(args.input, 'rb') as fin:
                result = hash_file(name, fin)

    if result is not None:
        if args.expected_result is None:
            print(result)
        elif result == args.expected_result:
            pass
        else:
            print('E:', args.expected_result)
            print('O:', result)

if __name__ == "__main__":
    main()

