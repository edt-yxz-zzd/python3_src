
r'''
see also:
    nn_ns.txt.MergeContentOfWebpages

=====
tag ==>> iter_XXX
filter
    tag.find_XXX(SoupStrainer(name, attrs, string))
第一/唯一
=====

from seed.internet.html_ast import HtmlAstOps, MarkupLang

ops = HtmlAstOps()
obj = ops.建('<p>xxx</p>', markup_lang=MarkupLang.HTML)
ops.得文本(obj)
ops.得件名(obj)
ops.得属性值(obj, 'id')

# 类别举 = 后代|子女|祖先|弟妹|兄姐|序后|序前|文本|简报
# 类别搜 = 后代|子女|祖先|弟妹|兄姐|序后|序前
ops.枚举后代(obj)
ops.举得第一后代(obj)
ops.举得唯一后代(obj)
ops.搜索后代(obj, ['div', 'span'], 属性过滤={'class':'xxx yyy'}, 文本过滤=re.compile(...), 前几个=4)
ops.搜得第一后代(obj, ['div', 'span'], 属性过滤={'class':'xxx yyy'}, 文本过滤=re.compile(...))
ops.搜得唯一后代(obj, ['div', 'span'], 属性过滤={'class':'xxx yyy'}, 文本过滤=re.compile(...))


枚举序后文本
枚举此后文本
枚举此后
    # obj not in descendants/next_elements
    # descendants == next_elements[:L]
    # [document]需特别对待


py -m seed.internet.html_ast

>>> ops = HtmlAstOps()
>>> obj = ops.建('<p>xxx<span>sss</span><br/><img><div>yyy</div></p>', markup_lang=MarkupLang.HTML)

>>> obj
<p>xxx<span>sss</span><br/><img/><div>yyy</div></p>

#注意: obj是[document]，因此 此后 含obj+<p>
>>> for x in ops.枚举此后(obj): print(x)
<p>xxx<span>sss</span><br/><img/><div>yyy</div></p>
<p>xxx<span>sss</span><br/><img/><div>yyy</div></p>
xxx
<span>sss</span>
sss
<br/>
<img/>
<div>yyy</div>
yyy

#注意: obj是[document]，因此 序后 含<p>
>>> for x in ops.枚举序后(obj): print(x)
<p>xxx<span>sss</span><br/><img/><div>yyy</div></p>
xxx
<span>sss</span>
sss
<br/>
<img/>
<div>yyy</div>
yyy

#注意: obj是[document]，因此 后代 含<p>
>>> for x in ops.枚举后代(obj): print(x)
<p>xxx<span>sss</span><br/><img/><div>yyy</div></p>
xxx
<span>sss</span>
sss
<br/>
<img/>
<div>yyy</div>
yyy


>>> span = ops.搜得唯一后代(obj, 'span')
>>> span
<span>sss</span>

>>> sss = ops.举得唯一后代(span)
>>> str(sss)
'sss'

>>> for x in ops.枚举此后(span): print(x)
<span>sss</span>
sss
<br/>
<img/>
<div>yyy</div>
yyy

>>> for x in ops.枚举序后(span): print(x)
sss
<br/>
<img/>
<div>yyy</div>
yyy

>>> for x in ops.枚举后代(span): print(x)
sss


#'''



__all__ = '''
    MarkupLang
        default_markup_lang
    HtmlAstOps
    '''.split()


from bs4 import BeautifulSoup, Tag, NavigableString
from bs4 import SoupStrainer
import bs4
_bs4__element__ResultSet = bs4.element.ResultSet
del bs4
import enum
import re


@enum.unique
class MarkupLang(enum.Enum):
    HTML = enum.auto()
    HTML5 = enum.auto()
    XML = enum.auto()
default_markup_lang = MarkupLang.HTML
MarkupProxy = BeautifulSoup
MarkupTag = Tag
# BeautifulSoup <: Tag



隔串动作 = r'枚举|搜索'
隔单动作 = r'举得|搜得'
隔要求 = r'第一|唯一' #单动作 要求
隔类别共享 = '后代|子女|祖先|弟妹|兄姐|序后|序前'
隔类别举 = fr'{隔类别共享}|文本|简报'
隔类别搜 = fr'{隔类别共享}'

名单动作举 = r'(?P<单动作举>举得)'
名单动作搜 = r'(?P<单动作搜>搜得)'
名单动作 = fr'(?P<单动作>{名单动作举}|{名单动作搜})'

名类别举 = fr'(?P<类别举>{隔类别举})'
名类别搜 = fr'(?P<类别搜>{隔类别搜})'
名类别 = fr'(?P<类别>(?(单动作举){名类别举}|{名类别搜}))'


名要求 = fr'(?P<要求>{隔要求})'
式单方法名 = re.compile(fr'{名单动作}{名要求}{名类别}')
隔类别列表 = [隔类别举, 隔类别搜]

if 1:
    #print(式单方法名.pattern)
    assert 式单方法名.fullmatch('举得唯一后代')
    assert 式单方法名.fullmatch('搜得唯一后代')

def _cut(s):
    i = s.index('>')
    j = s.index(')')
    t = s[i+1:j]
    return t
def _ls(s):
    return (s).split('|')
    return _cut(s).split('|')
def _iter_nm3_011(隔类别):
    for b in _ls(隔要求):
      for c in _ls(隔类别):
        yield b+c
def _iter_dir3():
    # 枚举 单方法名
    for a, 隔类别 in zip(_ls(隔单动作), 隔类别列表):
      for bc in _iter_nm3_011(隔类别):
        nm = a+bc
        yield nm
def _iter_dir2():
    # 枚举 串方法名
    for a, 类别 in zip(_ls(隔串动作), 隔类别列表):
      for c in _ls(隔类别):
        nm = a+c
        yield nm


def _iter_fmt_f3():
    # 枚举 单方法名 定义
    [I, S] = _ls(隔单动作)

    fmt_I = """\
    def {nm}(ops, obj):
        check_tag(obj)
        return ops._{nm}(obj)
        #"""

    fmt_S = """\
    def {nm}(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={{}}):
        check_tag(obj)
        return ops._{nm}(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #"""

    yield from _iter_fmt_f3_X(I, fmt_I)
    yield from _iter_fmt_f3_X(S, fmt_S)

def _iter_fmt_f3_X(X, fmt):
    for nm in _iter_dir3():
        if not nm.startswith(X): continue
        yield fmt.format(nm=nm)
def _print_f3():
    for s in _iter_fmt_f3():
        print(s)

_iter = iter




def is_bs4_doc(obj):
    return type(obj) is BeautifulSoup and obj.name == '[document]'

def check_iterator(iterator):
    if iter(iterator) is not iterator:
        # TypeError: <class 'bs4.element.ResultSet'> is not iterator
        raise TypeError(fr'{type(iterator)!r} is not iterator')
def check_tag(obj):
    if not isinstance(obj, (MarkupTag, MarkupProxy)):
        raise TypeError(fr"{type(obj)!r} is not {MarkupTag!r} or {MarkupProxy!r}")
def check_str(obj):
    if not isinstance(obj, str):
        raise TypeError(fr"{type(obj)!r} is not str")

class _HtmlAstOpsAid0:
    # 类别举 = 后代|子女|祖先|弟妹|兄姐|序后|序前|文本|简报
    # 类别搜 = 后代|子女|祖先|弟妹|兄姐|序后|序前
    # 全部/第一/唯一 (枚举搜索结果)
    # 举得/搜得 * 第一/唯一 * <类别举/类别搜>
    def __getattr__(ops, _name):
        #print(f'{name}')

        m = None
        if _name.startswith('_'):
            name = _name[1:]
            m = 式单方法名.fullmatch(name)

        if m is None:
            name = _name
            #print(f'{name}')
            #AttributeError: 'super' object has no attribute '__getattr__'
            #说明真的没有name! 不是bug!
            return super().__getattr__(name)
            return super(__class__, type(ops)).__getattr__(ops, name)
            return super(__class__, ops).__getattr__(name)
        单动作 = m['单动作']
        要求 = m['要求']
        类别 = m['类别']

        if 1:
            f2 = getattr(ops, 要求)
        else:
            _f2 = getattr(ops, 要求)
            def f2(x):
                try:
                    return _f2(x)
                except TypeError:
                    print(x)
                    print(type(x))
                    #<class 'bs4.element.ResultSet'>
                    raise
        #end-def f2

        if 单动作 == '举得':
            method_name = fr'枚举{类别}'
            f1 = getattr(ops, method_name)
            def f(obj):
                check_tag(obj)
                return f2(f1(obj))
        elif 单动作 == '搜得':
            method_name = fr'搜索{类别}'
            f1 = getattr(ops, method_name)
            def f(obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
                check_tag(obj)
                return f2(f1(obj, 件名过滤, 文本过滤=文本过滤, 前几个=2, 属性过滤=属性过滤))
        else:
            raise logic-error
        return f

    @classmethod
    def _check_iterator(cls, iterator):
        check_iterator(iterator)
    #may be <class 'bs4.element.ResultSet'>
    @classmethod
    def 全部(cls, iterator):
        if type(iterator) is _bs4__element__ResultSet:
            iterator = iter(iterator)
        cls._check_iterator(iterator)
        return iterator
    @classmethod
    def 第一(cls, iterator):
        if type(iterator) is _bs4__element__ResultSet:
            iterator = iter(iterator)
        cls._check_iterator(iterator)
        for head in iterator:
            return head
        else:
            raise ValueError('空序列@求第一元素')
    @classmethod
    def 唯一(cls, iterator):
        if type(iterator) is _bs4__element__ResultSet:
            iterator = iter(iterator)
        cls._check_iterator(iterator)
        for head in iterator:
            break
        else:
            raise ValueError('空序列@求唯一元素')
        for _ in iterator:
            raise ValueError('序列长度大于一@求唯一元素')

        return head










class _HtmlAstOpsAid1(_HtmlAstOpsAid0):
    #自动生成: py -m seed.internet.html_ast > ~/tmp/ha_t0.txt
    ##================================
    ##================================
    ##================================
    #[
    def 举得第一后代(ops, obj):
        check_tag(obj)
        return ops._举得第一后代(obj)
        #
    def 举得第一子女(ops, obj):
        check_tag(obj)
        return ops._举得第一子女(obj)
        #
    def 举得第一祖先(ops, obj):
        check_tag(obj)
        return ops._举得第一祖先(obj)
        #
    def 举得第一弟妹(ops, obj):
        check_tag(obj)
        return ops._举得第一弟妹(obj)
        #
    def 举得第一兄姐(ops, obj):
        check_tag(obj)
        return ops._举得第一兄姐(obj)
        #
    def 举得第一序后(ops, obj):
        check_tag(obj)
        return ops._举得第一序后(obj)
        #
    def 举得第一序前(ops, obj):
        check_tag(obj)
        return ops._举得第一序前(obj)
        #
    def 举得第一文本(ops, obj):
        check_tag(obj)
        return ops._举得第一文本(obj)
        #
    def 举得第一简报(ops, obj):
        check_tag(obj)
        return ops._举得第一简报(obj)
        #
    def 举得唯一后代(ops, obj):
        check_tag(obj)
        return ops._举得唯一后代(obj)
        #
    def 举得唯一子女(ops, obj):
        check_tag(obj)
        return ops._举得唯一子女(obj)
        #
    def 举得唯一祖先(ops, obj):
        check_tag(obj)
        return ops._举得唯一祖先(obj)
        #
    def 举得唯一弟妹(ops, obj):
        check_tag(obj)
        return ops._举得唯一弟妹(obj)
        #
    def 举得唯一兄姐(ops, obj):
        check_tag(obj)
        return ops._举得唯一兄姐(obj)
        #
    def 举得唯一序后(ops, obj):
        check_tag(obj)
        return ops._举得唯一序后(obj)
        #
    def 举得唯一序前(ops, obj):
        check_tag(obj)
        return ops._举得唯一序前(obj)
        #
    def 举得唯一文本(ops, obj):
        check_tag(obj)
        return ops._举得唯一文本(obj)
        #
    def 举得唯一简报(ops, obj):
        check_tag(obj)
        return ops._举得唯一简报(obj)
        #
    def 搜得第一后代(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得第一后代(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得第一子女(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得第一子女(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得第一祖先(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得第一祖先(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得第一弟妹(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得第一弟妹(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得第一兄姐(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得第一兄姐(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得第一序后(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得第一序后(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得第一序前(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得第一序前(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得唯一后代(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得唯一后代(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得唯一子女(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得唯一子女(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得唯一祖先(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得唯一祖先(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得唯一弟妹(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得唯一弟妹(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得唯一兄姐(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得唯一兄姐(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得唯一序后(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得唯一序后(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #
    def 搜得唯一序前(ops, obj, 件名过滤=True, *, 文本过滤=None, 属性过滤={}):
        check_tag(obj)
        return ops._搜得唯一序前(obj, 件名过滤, 文本过滤=文本过滤, 属性过滤=属性过滤)
        #


    #]
    ##================================
    ##================================
    ##================================















class HtmlAstOps(_HtmlAstOpsAid1):
    def 建(ops, markup_doc, *, markup_lang=default_markup_lang):
        if markup_lang is None:
            markup_lang = default_markup_lang
        if type(markup_lang) is not MarkupLang:
            raise TypeError(fr"{type(markup_lang)!r} is not {MarkupLang!r}")

        if markup_lang is MarkupLang.HTML:
            wk = "html.parser"
        elif markup_lang is MarkupLang.HTML5:
            wk = "html5lib"
        elif markup_lang is MarkupLang.XML:
            wk = "lxml-xml"
        else:
            raise NotImplementedError(fr"unknown case: {markup_lang!r}")

        obj = MarkupProxy(markup_doc, wk, multi_valued_attributes=None)
        check_tag(obj)
        return obj
    def 得文本(ops, obj):
        check_tag(obj)
        return obj.get_text()
    def 得件名(ops, obj):
        check_tag(obj)
        return obj.name
    def 得属性值(ops, obj, 属性名):
        check_tag(obj)
        check_str(属性名)
        return obj[属性名]

    #举/搜:不含自己
    #####搜 * 全/首/独
    # 类别举 = 后代|子女|祖先|弟妹|兄姐|序后|序前|文本|简报
    # 类别搜 = 后代|子女|祖先|弟妹|兄姐|序后|序前
    # 枚举/搜索 * <类别举/类别搜>
    # 举得/搜得 * 第一/唯一 * <类别举/类别搜>
    def 枚举后代(ops, obj):
        check_tag(obj)
        return obj.descendants
    def 枚举子女(ops, obj):
        check_tag(obj)
        return obj.children
    def 枚举祖先(ops, obj):
        check_tag(obj)
        return obj.parents
    def 枚举弟妹(ops, obj):
        check_tag(obj)
        return obj.next_siblings
    def 枚举兄姐(ops, obj):
        check_tag(obj)
        return obj.previous_siblings
    def 枚举序后(ops, obj):
        check_tag(obj)
        if is_bs4_doc(obj):
            return obj.descendants
        else:
            return obj.next_elements
    def 枚举序前(ops, obj):
        check_tag(obj)
        return obj.previous_elements
    def 枚举文本(ops, obj):
        check_tag(obj)
        #print(obj)
        #return obj.strings #？只有『子女』，非所有『后代』？
        it = ops.枚举后代(obj)
        return ops._过滤文本(it)
    def _过滤文本(ops, objs):
        #T = bs4.element.NavigableString
        T = NavigableString
        for x in objs:
            #print(type(x))
            if isinstance(x, T):
                yield str(x)
    def 枚举简报(ops, obj):
        check_tag(obj)
        return obj.stripped_strings
    def 枚举序后文本(ops, obj):
        check_tag(obj)
        if 0:
            print(obj.children)
            print(len([*obj.children]))
            print([*map(type, obj.children)])
            print([*obj.children][2].name)
        if 0:
            it = ops.枚举序后(obj)
            ls = [*it]
            print(len(ls))
        it = ops.枚举序后(obj)
        return ops._过滤文本(it)
    def 枚举此后文本(ops, obj):
        check_tag(obj)
        it = ops.枚举此后(obj)
        return ops._过滤文本(it)
    def 枚举此后(ops, obj):
        check_tag(obj)
        #print(type(obj), obj.name, len([*obj.children]))
        # obj not in descendants/next_elements
        # descendants == next_elements[:L]
        yield obj
        yield from ops.枚举序后(obj)




    def 搜索后代(ops, obj, 件名过滤=True, *, 文本过滤=None, 前几个=None, 属性过滤={}):
        check_tag(obj)
        return _iter(obj.find_all(name=件名过滤, attrs=属性过滤, recursive=True, string=文本过滤, limit=前几个))

    def 搜索子女(ops, obj, 件名过滤=True, *, 文本过滤=None, 前几个=None, 属性过滤={}):
        check_tag(obj)
        return _iter(obj.find_all(name=件名过滤, attrs=属性过滤, recursive=False, string=文本过滤, limit=前几个))

    def 搜索祖先(ops, obj, 件名过滤=True, *, 文本过滤=None, 前几个=None, 属性过滤={}):
        check_tag(obj)
        return obj.find_parents(name=件名过滤, attrs=属性过滤, string=文本过滤, limit=前几个)

    def 搜索弟妹(ops, obj, 件名过滤=True, *, 文本过滤=None, 前几个=None, 属性过滤={}):
        check_tag(obj)
        return obj.find_next_siblings(name=件名过滤, attrs=属性过滤, string=文本过滤, limit=前几个)

    def 搜索兄姐(ops, obj, 件名过滤=True, *, 文本过滤=None, 前几个=None, 属性过滤={}):
        check_tag(obj)
        return obj.find_previous_siblings(name=件名过滤, attrs=属性过滤, string=文本过滤, limit=前几个)

    def 搜索序后(ops, obj, 件名过滤=True, *, 文本过滤=None, 前几个=None, 属性过滤={}):
        check_tag(obj)
        return _iter(obj.find_all_next(name=件名过滤, attrs=属性过滤, string=文本过滤, limit=前几个))

    def 搜索序前(ops, obj, 件名过滤=True, *, 文本过滤=None, 前几个=None, 属性过滤={}):
        check_tag(obj)
        return _iter(obj.find_all_previous(name=件名过滤, attrs=属性过滤, string=文本过滤, limit=前几个))














r"""

class HtmlTag:
    def __init__(sf, ops, obj):
        check_tag(obj)
        sf._ops = ops
        sf._obj = obj
    def get_text():
#"""



if __name__ == '__main__':
    _print_f3()

if __name__ == "__main__":
    import doctest
    doctest.testmod()



