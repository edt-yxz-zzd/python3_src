

def is_file_prefix(fname_prefix, fname_large, N=2**20):
    with open(fname_prefix, 'rb') as fpre, open(fname_large, 'rb') as flg:
        while fpre:
            prefix = fpre.read(N)
            if not prefix:
                return True
            other = flg.read(len(prefix))
            if other != prefix:
                return False

            #xxxxxxxxxxxx assert fpre.tell() == flg.tell()
        

def main(args=None):
    import argparse
    parser = argparse.ArgumentParser(description='test whether file1 is prefix of file2')
    parser.add_argument('file1', type=str,
                        help='file may be prefix')
    parser.add_argument('file2', type=str,
                        help='base file')
    

    args = parser.parse_args()
    r = is_file_prefix(args.file1, args.file2)
    print(repr(r))
    parser.exit(0)

if '__main__' == __name__:
    main()











    
