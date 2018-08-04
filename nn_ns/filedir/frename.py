
import file_rename



def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='rename files')
    parser.add_argument('source_txt', type=str, \
                        help='txt file whose line contains one old file name')
    parser.add_argument('destination_txt', type=str, \
                        help='txt file whose line contains one new file name')
    
    parser.add_argument('-p', '--path', type=str, \
                        default = '.',
                        help='path to all those file names')
    
    parser.add_argument('-e', '--encoding', type=str, \
                        default = None,
                        help='encoding of the input txt file')


    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)


    oldname_txtfn = args.source_txt
    newname_txtfn = args.destination_txt
    path = args.path
    encoding = args.encoding
    

    file_rename.rename_by_fname_from_txt(
        oldname_txtfn, newname_txtfn,
        path=path, encoding=encoding)
    return 0
    


if __name__ == "__main__":
    main()

    
