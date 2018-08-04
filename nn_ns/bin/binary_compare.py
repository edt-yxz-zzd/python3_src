
# import io
import filecmp

def binary_compare(fname1, fname2):
    # with open(fname1, 'rb') as fin1, open(fname2, 'rb') as fin2:
    return filecmp.cmp(fname1, fname2)

show = lambda b: 'same' if b else 'diff'
def main(args = None):
    import argparse

    parser = argparse.ArgumentParser(description='compare 2 files')
    parser.add_argument('file1', type=str, help='file name')
    parser.add_argument('file2', type=str, help='file name')

    args = parser.parse_args(args)
    print(show(binary_compare(args.file1, args.file2)))

if __name__ == '__main__':
    main()


    

