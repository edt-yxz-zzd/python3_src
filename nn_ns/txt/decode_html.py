
'''
entityref  &name; (e.g. &gt;), 
charref &#NNN; &#xNNN;
    the decimal equivalent for &gt; is &#62;, whereas the hexadecimal is &#x3E;; 
'''


'''
# not a bug
py.re.bugs from decode_html
p = re.compile('((\s)|(\d))')
assert p.split(' -1') == ['', ' ', ' ', None, '-', '1', None, '1', '']
# all capturing parentheses !!!!!!!!!!
'''



import re
from html.entities import name2codepoint, html5 as html5_name2char

__all__ = ('decode_html decode_html_ref re_html_ref_tpl'.split())

tpl_head = '(?ai)'
entityref_tpl = '&\w+;'
charref_dec_tpl = '&#\d+;'
charref_hex_tpl = '&#x[0-9a-f]+;'
html_ref_tpls = [entityref_tpl, charref_dec_tpl, charref_hex_tpl]
html_ref_tpl = '|'.join(html_ref_tpls)

to_re_tpl = lambda tpl: re.compile('{}({})'.format(tpl_head, tpl))
re_html_ref_tpl = to_re_tpl(html_ref_tpl)
re_entityref_tpl = to_re_tpl(entityref_tpl)
re_charref_dec_tpl = to_re_tpl(charref_dec_tpl)
re_charref_hex_tpl = to_re_tpl(charref_hex_tpl)

def decode_html(html_txt):
    words = re_html_ref_tpl.split(html_txt)
    #print(words)
    for i in range(1, len(words), 2):
        ref = words[i]
        c = decode_html_ref(ref)
        words[i] = c
    return ''.join(words)

def decode_html_ref(ref):
    assert len(ref) >= 3
    assert ref[0] == '&'
    assert ref[-1] == ';'

    if ref[1] == '#':
        s = ref[2:-1].lower()
        if s[0] == 'x':
            s = s[1:]
            base = 16
        else:
            base = 10
        c = chr(int(s, base))
    else:
        name = ref[1:] # include ";"
        c = html5_name2char[name]
    return c

assert '>' == decode_html_ref('&gt;') == \
       decode_html_ref('&#62;') == decode_html_ref('&#x3E;')

assert decode_html('> &gt; &#62; &#x3E;') == '> > > >'




def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='covert htmlref to char')
    
    parser.add_argument('-f', '--file', type=str, default=None,
                        help='source; default <stdin>')
    parser.add_argument('-o', '--output', type=str, default=None,
                        help='destination; default <stdout>')
    
    parser.add_argument('-e', '--encoding', type=str,
                        default='utf8',
                        help='encoding of source and destination; default utf8')
    

    args = parser.parse_args(args)


    src = args.file
    dst = args.output
    encoding = args.encoding
    
    if src is None:
        src = sys.stdin
    else:
        src = open(src, 'r', encoding=encoding)
        
    if dst is None:
        dst = sys.stdout
    else:
        dst = open(dst, 'x', encoding=encoding)

    with src, dst:
        # close stdin/out ??

        for line in src:
            dst.write(decode_html(line))

    parser.exit(0)
    return

    


if __name__ == "__main__":
    main()

    
