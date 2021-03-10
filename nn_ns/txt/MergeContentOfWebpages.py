
r'''
e ../../python3_src/nn_ns/txt/MergeContentOfWebpages.py


from nn_ns.txt.MergeContentOfWebpages import MergeContentOfWebpages, MergeContentOfWebpages__枚举此后文本
class MergeContentOfWebpages4XXX(MergeContentOfWebpages__枚举此后文本):
    def 是否除去文本的空白前后缀(sf):
        '-> bool'
        return False
    def 构造可选的结束文本(sf):
        '-> may_end_str'
        return ''
    def 构造搜索参数(sf):
        '-> (args, kwargs) #for bs4_ops.搜得第一后代()'
        return ['body'], {}
    def 构造章节标题(sf, idx, usrdata, html_fname):
        'idx -> usrdata -> html_fname -> title'
        return f'\n\n第{idx+1}章 【【【【{usrdata!r}】】】】\n\n'

class MergeContentOfWebpages4XXX(MergeContentOfWebpages):
    def iter_usrdata_htmlpath_pairs(sf):
        '-> Iter (usrdata, html_fname)'
    def output(sf, bs4_ops, bs4_obj, idx, usrdata, html_fname):
        'bs4_ops::HtmlAstOps -> bs4_obj::BeautifulSoup -> idx -> usrdata -> html_fname::Path -> IO ()'
    def skip(sf, idx, usrdata, html_fname):
        'idx -> usrdata -> html_fname::Path -> bool'
    def __init__(sf, may_ofname, *, force, iencoding, oencoding):
        super().__init__(may_ofname, force=force, iencoding=iencoding, oencoding=oencoding)

if __name__ == "__main__":
    sf = MergeContentOfWebpages4XXX(may_ofname, force=force, iencoding=iencoding, oencoding=oencoding)
    sf.main()


#'''


__all__ = '''
    MergeContentOfWebpages
    MergeContentOfWebpages__枚举此后文本
    '''
from seed.internet.html_ast import HtmlAstOps, MarkupLang
from seed.io.may_open import may_open_stdin, may_open_stdout
import bs4
import re
from pathlib import Path
from abc import ABC, abstractmethod

_ops = HtmlAstOps()
class MergeContentOfWebpages:
    r'''
to be overrided:
    iter_usrdata_htmlpath_pairs
    output
    skip
    pre_break
    post_break
    #'''
    def __init__(sf, may_ofname, *, force, iencoding, oencoding):
        omode = 'wt' if force else 'xt'
        sf.may_ofname = may_ofname
        sf.omode = omode
        sf.iencoding = iencoding
        sf.oencoding = oencoding
        sf._ops = _ops
        sf.fout = None
    def oprint(__sf, *args, **kw):
        return print(*args, **kw, file=__sf.fout)
    def main(sf):
        bs4_ops = sf._ops
        oprint = sf.oprint
        #with open(sf.may_ofname, sf.omode, encoding=sf.oencoding) as fout:
        with may_open_stdout(sf.may_ofname, sf.omode, encoding=sf.oencoding) as fout:
            sf.fout = fout
            for idx, (usrdata, path) in enumerate(sf.iter_usrdata_htmlpath_pairs()):
                html_fname = Path(path)
                if sf.pre_break(idx, usrdata, html_fname): break
                if sf.skip(idx, usrdata, html_fname): continue
                html_doc = html_fname.read_text(encoding=sf.iencoding)
                bs4_obj = bs4_ops.建(html_doc, markup_lang=MarkupLang.HTML)
                sf.output(bs4_ops, bs4_obj, idx, usrdata, html_fname)
                if sf.post_break(idx, usrdata, html_fname): break




    @abstractmethod
    def iter_usrdata_htmlpath_pairs(sf):
        '-> Iter (usrdata, html_fname)'
    def skip(sf, idx, usrdata, html_fname):
        'idx -> usrdata -> html_fname::Path -> bool'
        return False
    def pre_break(sf, idx, usrdata, html_fname):
        'idx -> usrdata -> html_fname::Path -> bool'
        return False
    def post_break(sf, idx, usrdata, html_fname):
        'idx -> usrdata -> html_fname::Path -> bool'
        return False
    def output(sf, bs4_ops, bs4_obj, idx, usrdata, html_fname):
        'bs4_ops::HtmlAstOps -> bs4_obj::BeautifulSoup -> idx -> usrdata -> html_fname::Path -> IO ()'
        oprint = sf.oprint
        ####
        if 0:
            ch, pg = usrdata
            oprint(f'\n\n第{ch}章 第{pg}页【【【【{ch}-{pg}】】】】\n\n')
            div = bs4_ops.搜得唯一后代(obj, 'div', 属性过滤={'id':'content'})
        else:
            pass
        oprint(f'\n\n第{idx+1}章 【【【【{usrdata!r}】】】】\n\n')
        body = bs4_ops.搜得第一后代(bs4_obj, 'body')
        sf.output__此后文本(bs4_ops, body, '', stripped=False)


    def output__此后文本(sf, bs4_ops, bs4_obj, may_end_str, *, stripped):
        'bs4_ops::HtmlAstOps -> bs4_obj::BeautifulSoup -> may_end_str -> IO ()'
        oprint = sf.oprint
        ####
        it = bs4_ops.枚举此后文本(bs4_obj)
        for txt in it:
            if may_end_str and may_end_str in txt: break
            if stripped:
                txt = txt.strip()
            oprint(txt)




class MergeContentOfWebpages__枚举此后文本(MergeContentOfWebpages):
    r'''
to be overrided:
    iter_usrdata_htmlpath_pairs
    构造章节标题
    构造搜索参数
    构造可选的结束文本
    是否除去文本的空白前后缀
    skip
    pre_break
    post_break
    #'''
    def 是否除去文本的空白前后缀(sf):
        '-> bool'
        return False
    def 构造可选的结束文本(sf):
        '-> may_end_str'
        return ''
    def 构造搜索参数(sf):
        '-> (args, kwargs) #for bs4_ops.搜得第一后代()'
        return ['body'], {}
    def 构造章节标题(sf, idx, usrdata, html_fname):
        'idx -> usrdata -> html_fname -> title'
        return f'\n\n第{idx+1}章 【【【【{usrdata!r}】】】】\n\n'
    def output(sf, bs4_ops, bs4_obj, idx, usrdata, html_fname):
        'bs4_ops::HtmlAstOps -> bs4_obj::BeautifulSoup -> idx -> usrdata -> html_fname::Path -> IO ()'
        oprint = sf.oprint
        ####
        title = sf.构造章节标题(idx, usrdata, html_fname)
        oprint(title)
        (args, kwargs) = sf.构造搜索参数()
        bs4_obj = bs4_ops.搜得第一后代(bs4_obj, *args, **kwargs)
        may_end_str = sf.构造可选的结束文本()
        sf.output__此后文本(bs4_ops, bs4_obj, may_end_str, stripped=sf.是否除去文本的空白前后缀())


