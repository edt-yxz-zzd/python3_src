

import unicodedata as U


def char2info(ch):
    name = U.name(ch, None)
    decimal = U.decimal(ch, None)
    digit = U.digit(ch, None)
    numeric = U.numeric(ch, None)

    category = U.category(ch)
    bidirectional = U.bidirectional(ch)
    combining = U.combining(ch)
    east_asian_width = U.east_asian_width(ch)
    mirrored = U.mirrored(ch)
    decomposition = U.decomposition(ch)

    unicode = ord(ch)
    unicode_hex = hex(unicode)
    return dict(locals())

def iter_to_char_names(string):
    return map(char2info, string)
    return map(U.name, string)

def to_char2name_dict(s):
    return dict(zip(s, iter_to_char_names(s)))

def main(args=None):
    import sys
    try:
        from seed.helper.stable_repr import stable_repr_print__expand_all_layer
    except ImportError:
        from pprint import pprint
    else:
        def pprint(x, /, *, file=None):
            stable_repr_print__expand_all_layer(file, x)

    if args is None:
        args = sys.argv

    for s in args[1:]: # skip script name
        if 1:
            pprint((s, to_char2name_dict(s)))
        else:
            print(s)
            pprint(to_char2name_dict(s))
        print()

    return 0

if __name__ == '__main__':
    main()







