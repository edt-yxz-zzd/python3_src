
from .unifont import font_file, read, print_char


uint16_to_mx = read(font_file)
#print_char(uint16_to_mx, 'A')


def main(args = None):
    import sys
    for line in sys.stdin:
        for c in line:
            print_char(uint16_to_mx, c)



if __name__ == "__main__":
    main()
