

from nn_ns.filedir.touch_file_time_pair__ns import touch_as



def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description="touch to_path's (atime, mtime) as from_path"
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-to', '--to_path', type=str
                        , required=True
                        , help='path to set (atime, mtime)')
    parser.add_argument('-from', '--from_path', type=str
                        , required=True
                        , help='path to get (atime, mtime)')

    args = parser.parse_args(args)
    to_path = args.to_path
    from_path = args.from_path
    touch_as(to_path=to_path, from_path=from_path)




if __name__ == "__main__":
    main()



