
'''
Windows only

why?
    I found it was hard to identify the absolute path of a selected file in Windows.
    so I decide to register a command into right-click menu.

'''
from seed.windows.windows_clipboard import set_Windows_clipboard

def main(argv=None):
    import argparse, os.path

    parser = argparse.ArgumentParser(
        description='save_input_path_to_clipboard'
        )
    parser.add_argument('input_path', type=str
                        , help='input file path')

    args = parser.parse_args(argv)
    input_path = args.input_path
    input_path = os.path.abspath(input_path)
    set_Windows_clipboard(input_path)
    parser.exit(0)

if __name__ == "__main__":
    main()


