r'''[[[
e ../../python3_src/nn_ns/app/char2hex.py


nn_ns.app.char2hex
py -m nn_ns.app.char2hex

also:
    view others/app/gvim/call_function_and_show_result.txt
    vim:
    :echo printf('0x%X', char2nr('一'))
    0x4E00

#]]]'''#'''

def main(args=None):
    import sys
    if args is None:
        args = sys.argv

    for s in args[1:]: # skip script name
        cs = ''.join(sorted({*s}))
        print(s)
        print('   ', cs)
        print('   ', ''.join(f'{ch}0x{ord(ch):0>4X}' for ch in cs))
        print()

    return 0

if __name__ == '__main__':
    main()







