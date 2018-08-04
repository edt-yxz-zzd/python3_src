

__all__ = '''
    novel_split_tree2html
    Node
'''.split()

from .novel_split_html_tpl import dt_dd_tpl, content_dl_tpl, html_tpl
from seed.text.raw_text2html_content import raw_text2html_content
    # previous assume Node.head (head_txt) is raw
    # now treat it may be escaped, so we pass
    #   is_head_raw/raw_text2html_content as argument


echo = lambda x:x
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

def novel_split_node2content_dl(node, path2title, raw_text2html_content):
    level = len(node.path)
    #title = raw_text2html_content(path2title(node.path))
    content = raw_text2html_content(node.head)

    sublevel = level + 1
    ls = []
    for subnode in node.subnodes:
        id = 'a{}'.format(subnode.id)
        path = subnode.path
        subtitle = raw_text2html_content(path2title(path))
        sub_content_dl = novel_split_node2content_dl(
                    subnode, path2title, raw_text2html_content)
        dt_dd = dt_dd_tpl.format(id=id,
                                 title=subtitle,
                                 level=sublevel,
                                 content_dl=sub_content_dl
                                 )
        ls.append(dt_dd)
    content_dl = content_dl_tpl.format(dt_dd_ls='\n'.join(ls), content=content)

    return content_dl

def novel_split_tree2html_body(tree, path2title, is_head_raw):
    # novel_split_tree2html_body
    #       :: Node -> ([title]->final_title)->bool->html_body
    #
    # tree :: Node
    # path2title :: [title] -> final_title
    # Node = Node {id :: uint, path :: [title], head :: str, subnodes :: [Node]}
    # title :: str
    __raw_text2html_content = raw_text2html_content if is_head_raw else echo
    content_dl = novel_split_node2content_dl(tree, path2title
                                , __raw_text2html_content)
    body = content_dl
    return body



def novel_split_tree2html(tree, path2title, is_head_raw
                , title, encoding = 'utf-8'
                , style_css_fname='style.css'
                , styles = ''
                , action_js_fname='action.js'
                , jscript = ''):
    body = novel_split_tree2html_body(tree, path2title, is_head_raw)

    return html_tpl.format(encoding=encoding,
                           title=title,
                           content_dl=body,
                           style_css_fname=style_css_fname,
                           styles=styles,
                           action_js_fname=action_js_fname,
                           jscript = jscript)




