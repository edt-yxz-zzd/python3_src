
import re
from sand import re_partition_to_head_bodyls
from sand import raw_text2html_content, \
     read_txt, write_txt, zh_cn_encoding, is_main

from sand import literal_eval, safe_eval, replace_substrings


'''
novel.txt:
----------------------------------------
head...
vol. 1
v1head...
chapter. 1
chapter1txt...
----------------------------------------

err: re_seps = [r'(?m)^vol. \d+$', r'(?m)^chapter. \d+$']
re_seps = [r'(?m)(^vol. \d+\s*\n)', r'(?m)(^chapter. \d+\s*\n)']
result = list of (path_parts, txt)
= [
    ((), head...),
    (('vol. 1',), v1head...),
    (('vol. 1', 'chapter. 1'), chapter1txt...),
]
'''




def _novel_split(path_parts, re_seps, re_sep_idx, txt):
    if re_sep_idx == len(re_seps):
        return [(path_parts, txt)]
    
    sep = re_seps[re_sep_idx]
    re_sep_idx += 1
    

    head, bodyls = re_partition_to_head_bodyls(sep, txt)
    result = [(path_parts, head)]

    for path_part, sub_txt in bodyls:
        sub_path_parts = path_parts + (path_part,)
        sub_result = _novel_split(sub_path_parts, re_seps, re_sep_idx, sub_txt)
        result.extend(sub_result)
        
    return result


def novel_split(re_seps, txt):
    ls = [re.compile(sep) for sep in re_seps]
    re_seps = ls
    
    return _novel_split((), re_seps, 0, txt)





class Node:
    __slots__ = ('id', 'path', 'head', 'subnodes')
    def __init__(self, id, path, head, subnodes):
        self.id = id
        self.path = path
        #self.num_path = num_path
        self.head = head
        self.subnodes = subnodes
        return
    def to_tuple(self):
        return (self.id, self.path, self.head, self.subnodes)
    def get_args(self):
        return self.to_tuple()
    def __repr__(self):
        return 'Node' + repr(self.get_args())

    def __eq__(self, other):
        return (self is other) or (self.get_args() == other.get_args())
    def __ne__(self, other):
        return not (self == other)
    pass


##class _novel_split_ls2tree:
##    def __init__(self, novel_split_ls, path_parts2title):
##        self.ls = novel_split_ls
##        self.path2title = path_parts2title
##        pass
##    def to_tree(self, idx, node):
##        path_parts, txt = self.ls[idx]
##        title = self.path2title(path_parts)


def _novel_split_ls2tree(ls, idx):
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
    assert ls
    assert ls[0][0] == ()

    tree, next_idx = _novel_split_ls2tree(ls, 0)
    assert next_idx == len(ls)
    return tree


html_tpl = r'''
<!DOCTYPE html>
<html>
<head>
    <meta charset={encoding!r}/>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href={style_css_fname!r} />
    <style type="text/css">
        {styles}
    </style>
</head>
<body>
{body}
</body>
</html>
'''
labelcontent_tpl = r'''
<span {action}>{title}</span>
{radio}
<div>
<p>{content}</p>
{subnodes}
</div>
'''

subnode_radio_tpl = r'''<input type="radio" name="radio-{sublevel}"/>'''
subnode_li_tpl = r'''
<li><label id="{id}" {action}>{radio}
    <a href="#{id}">{labelcontent}</a>
</label></li>
'''
subnode_li_tpl = r'''
<li><label id="{id}">{radio}
    {labelcontent}
</label></li>
'''
subnode_li_tpl = r'''
<li><label id="{id}">
    {labelcontent}
</label></li>
'''

subnodes_ol_tpl = r'''
<ol>
{subnode_list}
</ol>
'''

def _node2li(node, path2title, radio):
    labelcontent = novel_split_node2labelcontent(node, path2title, radio)
    li = subnode_li_tpl.format(id=node.id,
                               #radio=radio,
                               labelcontent=labelcontent)
    return li
    
def novel_split_node2labelcontent(node, path2title, radio):
    level = len(node.path)
    title = raw_text2html_content(path2title(node.path))
    content = raw_text2html_content(node.head)
    
    sublevel = level + 1
    subnode_radio = subnode_radio_tpl.format(sublevel=sublevel)

    ls = []
    for subnode in node.subnodes:
        li = _node2li(subnode, path2title, subnode_radio)
        ls.append(li)
    ol = subnodes_ol_tpl.format(subnode_list='\n'.join(ls))
    labelcontent = labelcontent_tpl.format(title=title,
                                           radio=radio,
                                           content=content,
                                           subnodes=ol,
                                           action='onclick="this.focus();"')
    
    #labelcontent = labelcontent.format(radio=radio)
    return labelcontent

def novel_split_tree2html_body(tree, path2title):
    content = novel_split_node2labelcontent(tree, path2title, radio='')
    body = '<div>{content}</div>'.format(content=content)
    return body


def novel2html_body(txt, re_seps, path2title):
    ls = novel_split(re_seps, txt)
    tree = novel_split_ls2tree(ls)
    body = novel_split_tree2html_body(tree, path2title)
    return body

def novel2html(txt, re_seps, path2title, title, encoding = 'utf-8',
               style_css_fname='style.css', styles = ''):
    body = novel2html_body(txt, re_seps, path2title)
    
    return html_tpl.format(encoding=encoding,
                           title=title,
                           style_css_fname=style_css_fname,
                           styles=styles,
                           body=body)

def novel2htm(txt_fname, htm_fname, re_seps, path2title, *,
              iencoding, oencoding, title, 
              style_css_fname='style.css', styles = ''):
    txt = read_txt(txt_fname, iencoding)
    htm = novel2html(txt, re_seps, path2title,
                     title, oencoding,
                     style_css_fname, styles)
    write_txt(htm_fname, htm, oencoding)
    return

re_zh_cn_digits = '零一二三四五六七八九十百千万'
re_zh_cn_digit = '[{}]'.format(re_zh_cn_digits)
re_zh_cn_num = re_zh_cn_digit + '+'


def replace_re_digit(re_str):
    return replace_substrings(re_str, [(r"[:数:]", re_zh_cn_digits)])
def replace_re_seps(re_seps):
    return [replace_re_digit(re_str) for re_str in re_seps]


def main(args=None):
    import argparse, sys, os.path

    path2title = 'lambda path: "" if not path else path[-1].strip()'
    parser = argparse.ArgumentParser(description='convert novel text to html',
             epilog=r'Note: r"[:数:]" in <re_seps> will be replaced by '\
             r'"零一二三四五六七八九十百千万". '\
             r'You may want to use r"[[:数:]\d]" instead of r"\d".')
    parser.add_argument('source', type=str, \
                        help='text file name')
    parser.add_argument('destination', type=str, \
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
    
    parser.add_argument('-p2t', '--path2title', type=str, \
                        default = path2title,
                        help='covert subtitle-path to htm radio label')

    parser.add_argument('-rs', '--re_seps', type=str, \
                        nargs = '+',
                        help='regular-expression list to identify subtitle-path')

    args = parser.parse_args(args)
    if args.title == None:
        args.title = os.path.basename(args.destination)

    if args.iencoding == None:
        args.iencoding = args.encoding

    if args.oencoding == None:
        args.oencoding = args.encoding

    args.path2title = safe_eval(args.path2title)
    args.re_seps = replace_re_seps(args.re_seps)
    
    novel2htm(args.source, args.destination,
            title=args.title,
            iencoding=args.iencoding, oencoding = args.oencoding,
            re_seps=args.re_seps, path2title=args.path2title,
            style_css_fname=args.style_css_fname, styles=args.styles)
    
    



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



r'''
py -m novel_split E:\book\novel\华武\西游日记[今何在].txt E:\temp_output\西游.htm
 -e gbk -rs "(?m)(^第[[:数:]]+本\s+第[[:数:]]+天～第[[:数:]]+天\s*\n)"
 "(?m)(^【第[[:数:]]+天】\s*\n)"
 -s "body, ol { padding:0; background-color: #eee; list-style-type: none; }
 label > div { display: none; } input:checked + span + div { display: block; }"
'''
if is_main(__name__):
    main()



