
r'''
to genenerate some dicts in color_names.py from <PY_HOME>/Tools/pynche
'''

__all__ = ()

import sys, os.path
from collections import OrderedDict
from pprint import pprint
from seed.iters.duplicate_elements import iter_duplicate_representative_elements
from seed.tiny import fst


def _read_name_color_pairs(fin):
    # fin -> Iter name color
    # namedcolors.txt and html40colors.txt and webcolors.txt
    # line format: r"\s*(#.*)?\n|(.+)\b\s+#\w+\n"
    pattern = r"\s*(#.*)?|(.+)\b\s+#\w+"
    for line in fin:
        line = line.strip()
        if not line or line[0] == '#': continue
        i = line.rfind('#')
        if i == -1: raise Exception(f'line format error: {line}')
        name = line[:i].strip()
        color = line[i:].strip() # '#[0-9a-fA-F]+'
        assert len(color.split()) == 1
        name = ' '.join(name.split())
        yield name, color


def _read_R_G_B_name_tuples(fin):
    # fin -> Iter name color
    # X/rgb.txt
    # line format: r"\s*(!.*)?\n|(\d+\s+){3}.+\n"
    pattern = r"\s*(!.*)?|(\d+\s+){3}.+"
    def to_hex(u):
        return f'{u:0>2X}'
    for line in fin:
        line = line.strip()
        if not line or line[0] == '!': continue
        words = line.split()
        if len(words) < 4:
            raise Exception(f'line format error: {line}')

        i = 3
        name = ' '.join(words[i:])
        R,G,B = map(int, words[:i])
        RGB = R,G,B
        assert all(0<=x<0x100 for x in RGB)
        color = '#' + ''.join(map(to_hex, RGB)) # '#[0-9a-fA-F]+'
        yield name, color


def _get_pynche_folder():
    prefixes = [sys.prefix, sys.exec_prefix]
    for prefix in prefixes:
        path = os.path.join(prefix, 'Tools', 'pynche')
        if os.path.isdir(path):
            break
    else:
        raise FileNotFoundError('cannot found "sys.prefix/Tools/pynche"')
    pynche_folder = path
    return pynche_folder

def _iter_read_pynche_files(pynche_folder):
    # pynche_folder -> Iter (fname, Map name color)
    def pairs2dict(pairs):
        pairs = list(pairs)
        d = OrderedDict(pairs)
        if len(d) != len(pairs):
            names = iter_duplicate_representative_elements(pairs, key=fst)
            names = list(names)
            raise Exception(f'duplicate names: {names}')
        return d
    def read(fname, iter_pair_from_file):
        path = os.path.join(pynche_folder, fname)
        with open(path, 'rt', encoding='ascii') as fin:
            pairs = iter_pair_from_file(fin)
            d = pairs2dict(pairs)
        return d

    for fname in ['namedcolors.txt', 'html40colors.txt', 'webcolors.txt']:
        d = read(fname, _read_name_color_pairs)
        yield fname, d
    fname = 'X/rgb.txt'
    d = read(fname, _read_R_G_B_name_tuples)
    yield fname, d

_print = print
def _show_pynche_files(fout=None):
    if fout is None:
        #fout = sys.stdout
        print = _print
    else:
        def print(*args, **kwargs):
            _print(*args, file=fout, **kwargs)

    pynche_folder = _get_pynche_folder()
    it = _iter_read_pynche_files(pynche_folder)
    for fname, name2color in it:
        size = len(name2color)
        print(f'fname={fname}')
        print(f'size={size}')
        pprint(dict(name2color), stream=fout)
        it = iter(name2color.items())
        print('{', end='')
        for name, color in it:
            print(f'{name!r}: {color!r}')
            break
        for name, color in it:
            print(f',{name!r}: {color!r}')
        print('}')


if __name__ == "__main__":
    _show_pynche_files()



