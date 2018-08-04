

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
from seed.io.read_txt import read_txt, write_txt
from seed.text.encodings import python_encoding2html_encoding

from seed.helper.safe_eval import literal_eval, safe_eval


zh_cn_encoding = 'gb18030'

#print(replace_substrings, safe_eval)
#print(zh_cn_encoding)

# -----------------------------------------------------------------------------



r'''
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

r'''
<!DOCTYPE html>
<html>
<head>
    <meta charset={encoding!r}/>
    <title>{title}</title>


    <link rel="stylesheet" type="text/css" href={style_css_fname!r} />
    <style type="text/css">
        {styles}
    </style>

    <script src="jquery-1.4.2.min.js"></script>
    <!-- <script src="http://code.jquery.com/jquery-1.4.2.min.js"></script> -->
</head>


<body>
<p>c</p>
<dl>
<dt level=1><a id="a1" href="#a1">1</a></dt>
<dd>
    <p>c1</p>
    <dl>
    <dt level=2>1.1</dt>
    <dd>
        <p>c1.1</p>
    </dd>


    <dt level=2>1.2</dt>
    <dd>
        <p>c1.2</p>
    </dd>
    </dl>
</dd>


<dt level=1><a href="#">2</a></dt>
<dd>
    <p>c2</p>
    <dl>
    <dt level=2>2.1</dt>
    <dd>
        <p>c2.1</p>
    </dd>


    <dt level=2>2.2</dt>
    <dd>
        <p>c2.2</p>
    </dd>
    </dl>
</dd>
</dl>

</body>


<script src={action_js_fname!r}></script>
<script type="text/javascript">
{jscript}
</script>

</html>
'''



style_css = r'''
dd { display: none; }
body, dl { padding:0; background-color: #eee; list-style-type: none; }
'''

action_js = r'''
elems = [null];

function get_elem(level){
    if (level < elems.length){
        return elems[level];
    }
    alert("error: index outside array");
    return null;
}

function _hide_elem(level){
    elem = get_elem(level);
    if (elem) $(elem).hide();
}

function _show_elem(level){
    elem = get_elem(level);
    if (elem) $(elem).slideDown();
}

function _toggle_elem(level){
    elem = get_elem(level);
    if (elem) $(elem).toggle();
}

function set_elem(level, elem){
    clear_elems_to(level);
    if (elem && (elem === get_elem(level))){
        clear_elems_to(level-1);
    }
    else{
        _hide_elem(level);
        elems[level] = elem;
        _show_elem(level);
    }
}

function clear_elems_to(level){
    while (!(level < elems.length)){
        elems.push(null);
    }

    while ((level+1) < elems.length){
        _hide_elem(elems.length-1);
        elem = elems.pop();
    }
}


function next_elem(curr){
    var next = curr;
    if (next === null) alert("error: next == null");
    for (next = next.nextSibling; next; next = next.nextSibling){
        if (next.nodeType === 1) break;
    }
    return next;
}

$('dt').click(
        function(){
            var level = parseInt(this.getAttribute("level"));
            var next = next_elem(this);
            set_elem(level, next);
            //this.focus();
        }
    );
'''

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

    <script src="jquery-1.4.2.min.js"></script>
    <!-- <script src="http://code.jquery.com/jquery-1.4.2.min.js"></script> -->
</head>


<body>
{content_dl}
</body>

<script src={action_js_fname!r}></script>
<script type="text/javascript">
{jscript}
</script>

</html>
'''



content_dl_tpl = r'''
<p>{content}</p>
<dl>
{dt_dd_ls}
</dl>
'''
dt_dd_tpl = r'''
<dt level={level}><a id="{id!s}" href="#{id!s}">{title}</a></dt>
<dd>
{content_dl}
</dd>
'''


def novel_split_node2content_dl(node, path2title):
    level = len(node.path)
    #title = raw_text2html_content(path2title(node.path))
    content = raw_text2html_content(node.head)

    sublevel = level + 1
    ls = []
    for subnode in node.subnodes:
        id = 'a{}'.format(subnode.id)
        path = subnode.path
        subtitle = raw_text2html_content(path2title(path))
        sub_content_dl = novel_split_node2content_dl(subnode, path2title)
        dt_dd = dt_dd_tpl.format(id=id,
                                 title=subtitle,
                                 level=sublevel,
                                 content_dl=sub_content_dl
                                 )
        ls.append(dt_dd)
    content_dl = content_dl_tpl.format(dt_dd_ls='\n'.join(ls), content=content)

    return content_dl

def novel_split_tree2html_body(tree, path2title):
    # tree :: Node
    # path2title :: [title] -> final_title
    # Node = Node {id :: uint, path :: [title], head :: str, subnodes :: [Node]}
    content_dl = novel_split_node2content_dl(tree, path2title)
    body = content_dl
    return body


def novel2html_body(txt, re_seps, path2title):
    # txt :: str
    # re_seps :: [regex]
    # path2title :: [title] -> final_title
    ls = novel_split(re_seps, txt)
    # ls :: [([title], head_txt)]
    tree = novel_split_ls2tree(ls)
    body = novel_split_tree2html_body(tree, path2title)
    return body

def novel2html(txt, re_seps, path2title, title, encoding = 'utf-8',
               style_css_fname='style.css', styles = '',
               action_js_fname='action.js', jscript = ''):
    body = novel2html_body(txt, re_seps, path2title)

    return html_tpl.format(encoding=encoding,
                           title=title,
                           content_dl=body,
                           style_css_fname=style_css_fname,
                           styles=styles,
                           action_js_fname=action_js_fname,
                           jscript = jscript)





# ------------------------------main---------------------------------------

def novel2htm(txt_fname, htm_fname, re_seps, path2title, *,
              iencoding, oencoding, title, 
              style_css_fname='style.css', styles = '',
              action_js_fname='action.js', jscript = '',
              force=False):
    txt = read_txt(txt_fname, iencoding)
    htm = novel2html(txt, re_seps, path2title,
                     title, oencoding,
                     style_css_fname, styles,
                     action_js_fname, jscript)
    if False:
        write_txt(htm_fname, htm, oencoding)
        return

    bin_htm = htm.encode(oencoding)
    open_mod = 'w' if force else 'x'
    if htm_fname is None:
        if True:
            fout = sys.stdout
            fout.write(htm)
            #fout.write(htm)
    elif True:
        # to avoid \r\n \n\r
        bin_open_mod = open_mod + 'b'
        with open(htm_fname, bin_open_mod) as fout:
            fout.write(bin_htm)
    else:
        with open(htm_fname, open_mod, encoding=oencoding) as fout:
            fout.write(htm)
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
              force=args.force)



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






