r'''[[[
e ../../python3_src/nn_ns/app/char5hex.py

py -m nn_ns.app.char5hex
py -m nn_ns.app.debug_cmd   nn_ns.app.char5hex -x


py -m nn_ns.app.char5hex 4E00,3000,6211  4E8C
4E00,3000,6211
    一　我
    一0x4E00　0x3000我0x6211

4E8C
    二
    二0x4E8C

#]]]'''

def main(args=None):
    import sys
    if args is None:
        args = sys.argv

    #s = ' '.join(args[1:])
    for s in args[1:]: # skip script name
        _s = s.replace(',', ' ')
        ls = _s.split()
        us = [int(t, 16) for t in ls]
        cs = ''.join(chr(u) for u in us)
        print(s)
        print('   ', cs)
        print('   ', ''.join(f'{ch}0x{ord(ch):0>4X}' for ch in cs))
        print()

    return 0

if __name__ == '__main__':
    main()

