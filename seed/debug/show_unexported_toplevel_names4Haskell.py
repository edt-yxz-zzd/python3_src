#__all__:goto
r'''[[[
e ../../python3_src/seed/debug/show_unexported_toplevel_names4Haskell.py

假设:
    + [所有 {- -} 要么 起始符,结束符 之前 只有前缀空格 要么 只内嵌于单行内]
        注意:特殊情况:
        {-
            class ... where
                -- {-# LANGUAGE ExplicitForAll #-}
        -}
    + [字符串 单行]
    + [类型构造器指令 只有:data,newtype,type,class]
        type-family??
        ??[类型构造器指令 与 类型构造器 之间 只有空格(没有 注释/换行)]
            但是class/data都可有 约束
    + [类型构造器指令,顶层变量 位于 行首]
        之前 没有 注释
    + [顶层变量 必须 声明 类型]
    + [顶层变量声明,类型构造器指令-标识名 位于 同一行]
    + [库包输出声明 -- 位于 行首]
    + 未考虑 操作符
    + 未考虑 转发性输出

seed.debug.show_unexported_toplevel_names4Haskell
py -m nn_ns.app.debug_cmd   seed.debug.show_unexported_toplevel_names4Haskell -x
py -m nn_ns.app.doctest_cmd seed.debug.show_unexported_toplevel_names4Haskell:__doc__ -ht
py_adhoc_call   seed.debug.show_unexported_toplevel_names4Haskell   @f
from seed.debug.show_unexported_toplevel_names4Haskell import *


py_adhoc_call   seed.debug.show_unexported_toplevel_names4Haskell   ,iter_toplevel_names4Haskell__5path  --encoding:utf8   :../../python3_src/haskell_src/Framework4Translation.hs
py_adhoc_call   seed.debug.show_unexported_toplevel_names4Haskell   ,iter_exported_names4Haskell__5path  --encoding:utf8   :../../python3_src/haskell_src/Framework4Translation.hs
py_adhoc_call   seed.debug.show_unexported_toplevel_names4Haskell   @show_unexported_toplevel_names4Haskell__5path  --encoding:utf8   :../../python3_src/haskell_src/Framework4Translation.hs

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from pathlib import Path
from itertools import chain
import re
re4comment_sep = re.compile(r'(?:[{]-|-[}])')

#re4toplevel_var_decl = re.compile(r'(?:^(\w+)\s*(?:[@(,.!)\w\s]*(?<=[\w\s])=|::)(?:\s|[\(\{\[]|$|\w))') #--\]\}\)
    # 太麻烦:f (D {a=x})
    #   只保留声明+极简函数定义(小写首字母 避免 类型构造器)
re4toplevel_var_decl = re.compile(r'(?:^(\w+)\s*(?:(?:[_a-z]\w*\b\s*)*(?<=[\w\s])=|::)(?:\s|[\(\{\[]|$|\w))') #--\]\}\)

#re4toplevel_typ_def = re.compile(r'(?:^\<(?:data|newtype|type|class)\>\s*(?:(?:[(][^()=]*[)]\s*|[^()=]*)=>\s*)?\<(\w+)\>)')
re4toplevel_typ_def = re.compile(r'(?:^\b(?:data|newtype|type|class)\b\s*(?:(?:[(][^()=]*[)]\s*|[^()=]*)=>\s*)?\b(\w+)\b)')

re469 = re.compile(r'[()]')
re4where = re.compile(r'(?:\bwhere\b)')
def _test():
    s0 = 'class (A a, B b) => C c where'
    m0 = re4toplevel_typ_def.match(s0).group(1)
    assert m0 == 'C', m0
    ps = (
        [('C', 'class (A a, B b) => C c where')
        ,('C', 'class A a => C c where')
        ,('C', 'class C c where')
        ])
    for ans, s in ps:
        m = re4toplevel_typ_def.match(s).group(1)
        assert m == ans, (m, ans)
_test()

def _skip_multiline_comment_and_line_tail(j, line, s, it, /):
    assert s.startswith('{-')
    begin = line.index('{-')
    prefix = line[:begin]
    j0 = j
    acc = 0
    for j, line, s in chain([(j, line, s)], it):
        for m in re4comment_sep.finditer(line):
            t = m.group(0)
            #if 0b000:print(f'{j0}:{j}:{line!r}:{s!r}:{t!r}:{acc}')
            if t == '{-':
                acc += 1
                continue
            if t == '-}':
                acc -= 1
                if acc > 0:
                    continue
                if acc == 0:
                    #break#必须处理完整行
                    end = m.end(0)
                    suffix = line[end:]
                    line = prefix + suffix
                    continue
                raise Exception(j0, j, line, s, acc)
                raise 000
            raise 000
        ##已处理完整行
        if acc == 0:
            ##忽略行尾 <<== 不在行首/不是顶层对象
            jt = j
            line
            break
    else:
        raise 000#不完整的注释
    return (j, line, s)
def _iter_xxx_(lines, /):
    it = iter(lines)
    for j, line in enumerate(it):
        s = line.strip()
        yield j, line, s
def iter_lines_without_comment4Haskell__5lines(lines, /):
    it = _iter_xxx_(lines)
    for j, line, s in it:
        if s.startswith('--'):
            #skip-singleline-comment
            continue
        if s.startswith('{-'):
            #skip multiline-comment+line_tail
            (j, line, s) = _skip_multiline_comment_and_line_tail(j, line, s, it)
            #continue#ignore line_tail(!!after comment==>>not toplevel entry)
        if s:
            yield (j, line, s)

def iter_exported_names4Haskell__5lines(lines, /):
    it = iter_lines_without_comment4Haskell__5lines(lines)
    for j, line, s in it:
        if line.startswith('module '):
            break
    else:
        return
    ls = []
    for j, line, s in chain([(j, line, s)], it):
        ls.append(s)
        #if 'where' in s:
        if re4where.search(s):
            assert s.endswith('where'), s
            break
    s = ' '.join(ls)
    assert s.endswith(' where'), s
    assert s.startswith('module '), s
    try:
        i = s.index('(')
        j = s.rindex(')')
    except IndexError:
        return
    def _ignore_inner_69(s, i, j, /):
        #ignore (.*)
        acc = 0
        for k in range(i+1, j):
            c = s[k]
            if c == '(':
                acc += 1
            elif c == ')':
                acc -= 1
            elif acc == 0:
                yield c
    t = ''.join(_ignore_inner_69(s, i, j))
    r = re.sub('\s', '', t)
    if not r:
        return
    nms = r.split(',')
    assert all(nm.isidentifier() for nm in nms)
    yield from nms
    return
    r'''
    acc46 = 0
    acc49 = 0
        acc46 += s.count('(')
        acc49 += s.count(')')
    #'''


def iter_toplevel_names4Haskell__5lines(lines, /, *, nms4yielded=None):
    if nms4yielded is None:
        nms4yielded = set()
    re_ls = (re4toplevel_var_decl, re4toplevel_typ_def)

    it = iter_lines_without_comment4Haskell__5lines(lines)
    for j, line, s in it:
        for re4xxx in re_ls:
            m = re4xxx.match(line)
            if m:
                break
        if m:
            nm = m.group(1)
            if not nm in nms4yielded:
                nms4yielded.add(nm)
                yield nm
                continue
def lines5path_(path, /, *, encoding):
    txt = Path(path).read_text(encoding)
    lines = txt.replace('\r', '\n').split('\n')
    return lines
def iter_exported_names4Haskell__5path(path, /, *, encoding):
    lines = lines5path_(path, encoding=encoding)
    return iter_exported_names4Haskell__5lines(lines)
def iter_toplevel_names4Haskell__5path(path, /, *, encoding):
    lines = lines5path_(path, encoding=encoding)
    return iter_toplevel_names4Haskell__5lines(lines, nms4yielded=set())
def show_unexported_toplevel_names4Haskell__5path(path, /, *, encoding):
    (unexported_toplevel_names, exported_nontoplevel_names) = collect_ex__unexported_toplevel_names4Haskell__5path(path, encoding=encoding)
    for nm in unexported_toplevel_names:
        print(nm)
    if exported_nontoplevel_names:
        print('===bug?:')
    for nm in exported_nontoplevel_names:
        print(nm)

def collect_ex__unexported_toplevel_names4Haskell__5path(path, /, *, encoding):
    lines = lines5path_(path, encoding=encoding)
    return collect_ex__unexported_toplevel_names4Haskell__5lines(lines)
def collect_ex__unexported_toplevel_names4Haskell__5lines(lines, /):
    toplevel_names = set(iter_toplevel_names4Haskell__5lines(lines, nms4yielded=set()))
    exported_names = set(iter_exported_names4Haskell__5lines(lines))
    unexported_toplevel_names = toplevel_names -exported_names
    exported_nontoplevel_names = exported_names -toplevel_names
    return (unexported_toplevel_names, exported_nontoplevel_names)



__all__
from seed.debug.show_unexported_toplevel_names4Haskell import *
