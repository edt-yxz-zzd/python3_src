

'''
bug if BOM exists
    utf_16_le BOM == '\ufeff'
    unicodedata.category('\ufeff') == 'Cf' # format characters (General_Category=Cf )
    unicodedata.category(' ') == 'Zs'

    if we try to match "^\s*\w{,40}$" we'll fail
    # "(^|\A\ufeff?).*($|\Z)"
    "(^\ufeff?).*($)"
'''

import re, sys
from seed.text.re_partition_all import re_partition_to_head_bodyls
from seed.text.raw_text2html_content import raw_text2html_content
from seed.text.replace_substrings import replace_substrings
#from seed.io.read_txt import read_txt, write_txt
from seed.text.encodings import python_encoding2html_encoding
from seed.helper.safe_eval import literal_eval, safe_eval
from .novel_split_tree2html import novel_split_tree2html, Node


zh_cn_encoding = 'gb18030'

#print(replace_substrings, safe_eval)
#print(zh_cn_encoding)

# -----------------------------------------------------------------------------



# ------------------------novel_split----------------------------------------



def _novel_split(path_parts, re_seps, re_sep_idx, txt):
    # path_parts :: tuple<title>
    # re_seps :: [regex]
    # re_sep_idx :: uint
    # txt :: str
    # head :: str
    # result :: [([title], head_txt)]
    if re_sep_idx == len(re_seps):
        return [(path_parts, txt)]

    sep = re_seps[re_sep_idx]
    re_sep_idx += 1


    # re_partition_to_head_bodyls :: (regex, str) -> (str, [(title, whole_txt)])
    head, bodyls = re_partition_to_head_bodyls(sep, txt)
    result = [(path_parts, head)]
    if False and re_sep_idx == 1:
        print(len(head))
        print(sep.pattern)
        first_line = txt[:txt.index('\n')]
        print(first_line)

    for path_part, sub_txt in bodyls:
        sub_path_parts = path_parts + (path_part,)
        sub_result = _novel_split(sub_path_parts, re_seps, re_sep_idx, sub_txt)
        result.extend(sub_result)

    return result


def novel_split(re_seps, txt):
    # novel_split :: ([regex], str) -> [([title], head_txt)]
    # re_seps :: [regex]
    # txt :: str
    # title :: str
    # output:
    #   path_parts_txt_pairs :: [([title], head_txt)]
    #print(re_seps)
    re_seps = [re.compile(sep) for sep in re_seps]

    path_parts_txt_pairs = _novel_split((), re_seps, 0, txt)
    try:
        assert len(txt) == sum(len(path_parts[-1] if path_parts else '') +
                               len(txt) for path_parts, txt in path_parts_txt_pairs)
    except:
        print(len(txt))
        print(sum(len(txt) for path_parts, txt in path_parts_txt_pairs))
        print(path_parts_txt_pairs)
        raise
    return path_parts_txt_pairs



# -------------------------novel_split_ls2tree--------------------------------



def _novel_split_ls2tree(ls, idx):
    # ls :: [([title], head_txt)]
    # idx :: uint # begin_idx
    # postcondition:
    #   next_idx == len(ls) or ls[next_idx][0] is not startswith ls[idx][0]
    #   i.e. _novel_split_ls2tree group all children of ls[idx]
    path_parts, txt = ls[idx]
    subnodes = []
    next_idx = idx + 1
    while next_idx < len(ls):
        next_path_parts, _ = ls[next_idx]
        if len(next_path_parts) > len(path_parts):
            if len(next_path_parts) != len(path_parts) + 1:
                raise logic-error or value-error
            subnode, next_idx = _novel_split_ls2tree(ls, next_idx)
            subnodes.append(subnode)
        else:
            break
    node = Node('id{}'.format(idx), path_parts, txt, subnodes)
    return node, next_idx

def novel_split_ls2tree(ls):
    # ls :: [([title], head_txt)]
    assert ls
    assert ls[0][0] == ()

    tree, next_idx = _novel_split_ls2tree(ls, 0)
    assert next_idx == len(ls)
    return tree



# ------------------------novel2html----------------------------------------



def novel2html(txt, re_seps, path2title, title, encoding='utf-8',
               style_css_fname='style.css', styles = '',
               action_js_fname='action.js', jscript = '',
               is_head_raw=True):
    # txt :: str
    # re_seps :: [regex]
    # path2title :: [title] -> final_title
    ls = novel_split(re_seps, txt)
    # ls :: [([title], head_txt)]
    tree = novel_split_ls2tree(ls)

    return novel_split_tree2html(
                    tree, path2title, is_head_raw=is_head_raw
                    , title=title, encoding=encoding
                    , style_css_fname=style_css_fname
                    , styles = styles
                    , action_js_fname=action_js_fname
                    , jscript = jscript)




# ------------------------------main---------------------------------------

def read_txt(txt_fname, encoding, newline_convert=True):
    if newline_convert:
        with open(txt_fname, encoding=encoding) as fin:
            return fin.read()
    else:
        with open(txt_fname, 'rb') as fin:
            bs = fin.read()
        return bs.decode(encoding)

def write_txt(txt_fname, txt, encoding, newline_convert=True, force=False):
    open_mod = 'w' if force else 'x'
    # txt_fname maybe None
    if txt_fname is None:
        if True:
            fout = sys.stdout
            fout.write(txt)
        return

    elif newline_convert:
        with open(txt_fname, open_mod, encoding=encoding) as fout:
            fout.write(txt)
    else:
        bs = txt.encode(encoding)
        with open(txt_fname, open_mod+'b') as fout:
            fout.write(bs)


def novel2htm(txt_fname, htm_fname, re_seps, path2title, *,
              iencoding, oencoding, title,
              style_css_fname='style.css', styles = '',
              action_js_fname='action.js', jscript = '',
              force=False, is_head_raw=True,
              newline_convert=True):
    txt = read_txt(txt_fname, iencoding
                , newline_convert=newline_convert)
    htm = novel2html(txt, re_seps, path2title,
                     title, oencoding,
                     style_css_fname, styles,
                     action_js_fname, jscript,
                     is_head_raw=is_head_raw,
                     )
    write_txt(htm_fname, htm, oencoding, force=force
                , newline_convert=newline_convert)
    return

#万、亿、兆、京、垓、秭、穰、沟、涧、正、载、极
re_zh_cn_num_group = r"[:数:]"
zh_cn_digits = ('〇一二三四五六七八九' '十百千万亿兆吉太拍艾'
                   '零壹贰叁肆伍陆柒捌玖' '拾佰仟萬' '两倆'
                   '万亿兆京垓秭穰沟涧正载极'
                   '０１２３４５６７８９')
#re_zh_cn_digit = '[{}]'.format(zh_cn_digits)
#re_zh_cn_num = re_zh_cn_digit + '+'

re_zh_cn_numth_group = r"[:序:]"
zh_ch_numth = '''
ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ
ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ
①②③④⑤⑥⑦⑧⑨⑩
⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇
⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛
㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩
甲乙丙丁戊己庚辛壬癸
子丑寅卯辰巳午未申酉戌亥
天地玄黄宇宙洪荒日月盈昃辰宿列张寒来暑往秋收冬藏闰余成岁律吕调阳
'''
zh_ch_numth = ''.join(zh_ch_numth.split())
#re_zh_ch_numth = '[{}]'.format(zh_ch_numth)

def replace_re_digit(re_str):
    return replace_substrings(
        re_str,
        [(re_zh_cn_num_group, zh_cn_digits),
         (re_zh_cn_numth_group, zh_ch_numth)])
def replace_re_seps(re_seps):
    return [replace_re_digit(re_str) for re_str in re_seps]


NOTE = '''Note:
    r"{re_zh_cn_num_group}" in <re_seps> will be replaced by r"{zh_cn_digits}". '\
    You may want to use r"[{re_zh_cn_num_group}\d]" instead of r"\d".
    r"{re_zh_cn_numth_group}" in <re_seps> will be replaced by r"{zh_ch_numth}".
    usage: r"[{re_zh_cn_numth_group}]"
'''.format(re_zh_cn_num_group=re_zh_cn_num_group,
           zh_cn_digits=zh_cn_digits,
           re_zh_cn_numth_group=re_zh_cn_numth_group,
           zh_ch_numth=zh_ch_numth)
def main(args=None):
    import argparse, sys, os.path

    path2title = 'lambda path: "" if not path else path[-1].strip()'
    parser = argparse.ArgumentParser(
        description='convert novel text to html',
        epilog=NOTE)
    parser.add_argument('input_fname', type=str, \
                        help='text file name')
    parser.add_argument('output_fname', type=str, \
                        nargs = '?',
                        default = None,
                        help='html file name')

    parser.add_argument('-t', '--title', type=str, \
                        default = None,
                        help='title of html file')

    parser.add_argument('-e', '--encoding', type=str, \
                        default = 'utf-8',
                        help='encoding of both text/html file')

    parser.add_argument('-ie', '--iencoding', type=str, \
                        default = None,
                        help='encoding of the input text file')

    parser.add_argument('-oe', '--oencoding', type=str, \
                        default = None,
                        help='encoding of the output html file')



    parser.add_argument('-css', '--style_css_fname', type=str, \
                        default = 'style.css',
                        help='css fname')

    parser.add_argument('-s', '--styles', type=str, \
                        default = '',
                        help='inline css')

    parser.add_argument('-js', '--action_js_fname', type=str, \
                        default = 'action.js',
                        help='javascript fname')

    parser.add_argument('-j', '--jscript', type=str, \
                        default = '',
                        help='inline javascript')




    parser.add_argument('-p2t', '--path2title', type=str, \
                        default = path2title,
                        help='covert subtitle-path to htm radio label')

    parser.add_argument('-rs', '--re_seps', type=str, \
                        nargs = '+',
                        help='regular-expression list to identify subtitle-path')
    parser.add_argument('-f', '--force', action='store_true',
                        default=False,
                        help='overwrite output file if it exists')
    parser.add_argument('-H', '--HTML', action='store_true',
                        default=False,
                        help='is the input_file contains valid html node? if "-H" then the text will not be escaped in the output html.')
    parser.add_argument('-D', '--DisableUniversalNewlinesMode', action='store_true',
                        default=False,
                        help='to disable universal newlines mode')

    # args.output_fname may be None
    args = parser.parse_args(args)
    if args.title is None:
        title = args.output_fname
        if title is None:
            title = args.input_fname
        args.title = os.path.basename(title)
        del title

    if args.iencoding is None:
        args.iencoding = args.encoding

    if args.oencoding is None:
        args.oencoding = args.encoding

    args.oencoding = python_encoding2html_encoding(args.oencoding)

    args.path2title = safe_eval(args.path2title)
    args.re_seps = replace_re_seps(args.re_seps)

    novel2htm(args.input_fname, args.output_fname,
              title=args.title,
              iencoding=args.iencoding, oencoding = args.oencoding,
              re_seps=args.re_seps, path2title=args.path2title,
              style_css_fname=args.style_css_fname, styles=args.styles,
              action_js_fname=args.action_js_fname, jscript=args.jscript,
              force=args.force, is_head_raw=not args.HTML,
              newline_convert=not args.DisableUniversalNewlinesMode
              )



r'''
py -m novel_split E:\book\novel\华武\西游日记[今何在].txt E:\temp_output\西游.htm
 -e gbk -rs "(?m)(^第[[:数:]]+本\s+第[[:数:]]+天～第[[:数:]]+天\s*\n)"
 "(?m)(^【第[[:数:]]+天】\s*\n)"
'''
if __name__ == '__main__':
    main()
    pass


# ------------------------------test--------------------------------------



def get_txt_仙道求索():
    fname = r'E:/download/novel/仙道求索[虫豸].txt'
    txt = read_txt(fname, encoding = zh_cn_encoding)
    return txt
def get_txt_仙道求索test():
    txt = 'nhead\n第一卷 偶得仙缘始觉寒\nvolhead\n第一章 精怪\nchaptertxt'
    return txt

def re_seps_for_仙道求索():
    '第一卷 偶得仙缘始觉寒 | 第一章 精怪'
    re_zh_cn_num = re_zh_cn_digit + '+'
    re_volume = '第' + re_zh_cn_num + '卷'
    re_chapter = '第' + re_zh_cn_num + '章'
    re_title = '\w+'


    # If capturing parentheses are used in pattern,
    # then the text of all groups in the pattern are also
    # returned as part of the resulting list.
    re_seps_tpl = r'(?m)(^\s*' + '{index}' + r'\s+' + '{title}' + r'\s*\n)'
    re_seps = [
        re_seps_tpl.format(index = re_volume, title = re_title),
        re_seps_tpl.format(index = re_chapter, title = re_title),
        ]
    return re_seps

def split_仙道求索(txt):
    re_seps = re_seps_for_仙道求索()
    result = novel_split(re_seps, txt)
    return result


def test_split仙道求索():
    txt = get_txt_仙道求索test()
    r = split_仙道求索(txt)
    assert r == [((), 'nhead\n'),
                 (('第一卷 偶得仙缘始觉寒\n',), 'volhead\n'),
                 (('第一卷 偶得仙缘始觉寒\n', '第一章 精怪\n'), 'chaptertxt')]
    return r

def test_split2tree仙道求索():
    txt = get_txt_仙道求索test()
    ls = split_仙道求索(txt)
    assert ls == [((), 'nhead\n'),
                 (('第一卷 偶得仙缘始觉寒\n',), 'volhead\n'),
                 (('第一卷 偶得仙缘始觉寒\n', '第一章 精怪\n'), 'chaptertxt')]

    r = novel_split_ls2tree(ls)
    assert r == Node((),
                     'nhead\n',
                     [
                         Node(
                             ('第一卷 偶得仙缘始觉寒\n',),
                             'volhead\n',
                             [
                                 Node(
                                     ('第一卷 偶得仙缘始觉寒\n', '第一章 精怪\n'),
                                     'chaptertxt',
                                     []
                                 )
                             ]
                         )
                    ]
                )
    return r

def t():
    print(test_split2tree仙道求索())






