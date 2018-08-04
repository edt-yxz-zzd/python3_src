

r'''
a msgid line is:
    rex'^msgid\s*".*"\s*$'
a msgstr line is:
    rex'^msgstr\s*".*"\s*$'
extended lines:
    <xxx line>(\n\s*".*"\s*)*

given a zh_CN.po and a google translated translated.txt
assume number of msgstr lines in zh_CN.po == number of msgid lines in translated.txt
using translated.txt version to replace zh_CN.po ones
'''
import re
import json
import ast

def repr_str_in_c_literal(s):
    # i.e. double-quot, ascii
    return json.JSONEncoder().encode(s)#.decode('ascii')
def repr_str_in_double_quot_literal(s):
    # i.e. double-quot, unicode
    return json.JSONEncoder(ensure_ascii=False).encode(s)


def find_lines(rex, lines):
    return list(iter_find_lines(rex, lines))
def iter_find_lines(rex, lines):
    for i, line in enumerate(lines):
        m = rex.match(line)
        if m:
            yield (i, m)
msgstr_line_rex = re.compile(r'^msgstr\s*"(?P<to>.*)"\s*$')
msgid_line_rex = re.compile(r'^msgid\s*[“"](?P<from>.*)["”]\s*$')
extended_line_rex = re.compile(r'^\s*[“"](?P<unquot>.*)["”]\s*$')
def quot_and_eval(s):
    s = '"'+s+'"'
    try:
        s = ast.literal_eval(s)
    except:
        print(s)
        raise
    return s
def file2lines(fname, encoding):
    with open(fname, encoding=encoding) as fin:
        return list(fin)
def replace(from_lines, to_lines):
    from_indices = find_lines(msgid_line_rex, from_lines)
    to_indices = find_lines(msgstr_line_rex, to_lines)
    if len(from_indices) != len(to_indices):
        tostr_indices = find_lines(msgid_line_rex, to_lines)
        assert len(tostr_indices) == len(to_indices)
        to_indices = tostr_indices
        print(len(from_indices), len(to_indices))
        L = max(len(from_indices), len(to_indices))
        pad = -1, re.match('', '<none>')
        from_indices += [pad]*(L - len(from_indices))
        to_indices += [pad]*(L - len(to_indices))
        get_str = lambda i_m: i_m[1].group(0)
        it = zip(map(get_str, from_indices), map(get_str, to_indices))
        print(*tuple(it), sep='\n')
        raise ValueError('len(from_indices) != len(to_indices)')
    for (i_from, m_from), (i_to, m_to) in zip(from_indices, to_indices):
        # msgstr = 'msgstr {!r}\n'.format(m_from.group('from'))
        msg = quot_and_eval(m_from.group('from'))
        msgstr = 'msgstr {!s}\n'.format(
            #repr_str_in_c_literal(m_from.group('from')))
            repr_str_in_double_quot_literal(msg))
        to_lines[i_to] = msgstr

        # Note:
        #   maybe a extended line
        i = i_from
        for i in range(i_from+1, len(from_lines)):
            extended_line = from_lines[i]
            m = extended_line_rex.match(extended_line)
            if not m: break
        to_lines[i_to] += ''.join(from_lines[i_from+1 : i])


    #return to_lines
    return None

def replace_msgstr_lines(
        from_fname, to_fname
        , from_encoding='utf8', to_encoding='utf8'):
    from_lines = file2lines(from_fname, from_encoding)
    from_lines = tuple(from_lines)
    to_lines = file2lines(to_fname, to_encoding)
    replace(from_lines, to_lines)
    return ''.join(to_lines)
    return '\n'.join(to_lines)

def main():
    out_fname = 'zh_CN-new.po'
    out_encoding = 'utf8'
    to_fname = 'zh_CN.po'
    from_fname = 'translated.txt'
    out_mode = 'x'
    txt = replace_msgstr_lines(from_fname, to_fname)
    with open(out_fname, 'x', encoding=out_encoding) as fout:
        fout.write(txt)
main()



