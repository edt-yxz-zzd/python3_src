
from unicodedata import category
import os.path

L = 0x110000
def iter_chars():
    for i in range(L):
        ch = chr(i)
        yield ch

def iter_chars_of_category(cat):
    return (ch for ch in iter_chars() if category(ch) == cat)

def show_category(file, cat):
    for ch in iter_chars_of_category(cat):
        i = ord(ch)
        hex = f'{i:X}'
        print(f'U+{hex}', f'&#x{hex};', ch, file=file)


html_begin_tpl = r'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>unicode category {category}</title>
</head>
<body><pre>
'''
html_end = r'''
</pre></body>
</html>
'''

def do_output(fname_tpl, cat, *, force:bool=...):
    if not (force is ... or type(force) is bool): raise TypeError

    fname = fname_tpl.format(category=cat)
    html_begin = html_begin_tpl.format(category=cat)

    if force is ...:
        omode = 'w'
        if os.path.exists(fname):
            while True:
                s = input(f'{fname!r} exists, overwrite it? (Y/N): ')
                s = s.lower()
                if 'y' == s: break
                elif 'n' == s: return
                else:
                    continue
        pass
    else:
        omode = 'w' if force else 'x'

    with open(fname, omode, encoding='utf8') as fout:
        print(html_begin, file=fout)
        show_category(fout, cat)
        print(html_end, file=fout)

def _t():
    fname_tpl = 'unicode category {category}.html'
    cat = 'So'
    do_output(fname_tpl, cat)



def main(argv=None):
    import argparse
    #from seed.io.may_open import may_open_stdout

    parser = argparse.ArgumentParser(
        description='generate html to show unicode category'
        )
    parser.add_argument('category', type=str
                        , help='unicode category, e.g. "So"'
                        )
    parser.add_argument('-o', '--output', type=str
                        , default = 'unicode category {category}.html'
                        , help='output file path format string: {category}')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(argv)

    fname_tpl = args.output
    cat = args.category
    do_output(fname_tpl, cat, force=args.force)
    #may_ofname = args.output
    #with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:


if __name__ == "__main__":
    main()





