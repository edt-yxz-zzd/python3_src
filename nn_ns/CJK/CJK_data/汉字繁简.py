#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/CJK_data/汉字繁简.py

py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_data.汉字繁简 -x
py -m   nn_ns.CJK.CJK_data.汉字繁简 -sz 16
py -m   nn_ns.CJK.CJK_data.汉字繁简 -sz 16 -py
py -m   nn_ns.CJK.CJK_data.汉字繁简 -sz 16 -py -o ../../python3_src/nn_ns/CJK/CJK_data/汉字繁简囗囗平凡自反囗唯一可逆.py
view  ../../python3_src/nn_ns/CJK/CJK_data/汉字繁简囗囗平凡自反囗唯一可逆.py
py -m   nn_ns.CJK.CJK_data.汉字繁简 -sz 16 -py -o ../../python3_src/nn_ns/CJK/CJK_data/汉字繁简囗囗平凡自反囗唯一可逆囗囗打完补丁囗简繁字对囗补丁囗㝉宁相关.py
view  ../../python3_src/nn_ns/CJK/CJK_data/汉字繁简囗囗平凡自反囗唯一可逆囗囗打完补丁囗简繁字对囗补丁囗㝉宁相关.py

py -m nn_ns.CJK.CJK_data.汉字繁简囗囗平凡自反囗唯一可逆囗囗打完补丁囗简繁字对囗补丁囗㝉宁相关
from nn_ns.CJK.CJK_data.汉字繁简囗囗平凡自反囗唯一可逆囗囗打完补丁囗简繁字对囗补丁囗㝉宁相关 import 汉字列表囗繁简囗平凡自反, 繁简字对列表囗繁简囗唯一可逆
deprecated:
    py -m nn_ns.CJK.CJK_data.汉字繁简囗囗平凡自反囗唯一可逆
    from nn_ns.CJK.CJK_data.汉字繁简囗囗平凡自反囗唯一可逆 import 汉字列表囗繁简囗平凡自反, 繁简字对列表囗繁简囗唯一可逆


from nn_ns.CJK.CJK_data.汉字繁简 import 简繁字对集, 繁体字到简体字串, 简体字到繁体字串
from nn_ns.CJK.CJK_data.汉字繁简 import 生成囗汉字列表囗繁简囗平凡自反囗, 生成囗繁简字对列表囗繁简囗唯一可逆囗


######################
######################
######################
######################
######################
######################
######################
######################
######################

给定一份文本，未知其简繁状态或其中字符简繁状态不一致，要求能够准确转化为繁体文本、简体文本，则需要什么条件？
[z :: 汉字]:
    [ok z =[def]= [汉字z满足上述要求]]

用箭头表示繁简关系:
    #繁-->简
    [[a-->b] =[def]= [(a,b)是繁简字对]]

#同向囗在左
[[z-->b] -> [z-->q] -> [b =/= q] -> [not [ok z]]]
    [[proof:
        要求z转化为简体时，有b,q两种译法，出现歧义
    ]]

#同向囗在右
[[b-->z] -> [q-->z] -> [b =/= q] -> [not [ok z]]]
    [[proof:
        要求z转化为繁体时，有b,q两种译法，出现歧义
    ]]

#异向囗不等
[[z-->b] -> [q-->z] -> [b =/= q] -> [not [ok z]]]
    [[proof:
        要求z转化为简体时，有b,z(不变)两种译法，出现歧义
        要求z转化为繁体时，有z(不变),q两种译法，出现歧义
    ]]

#异向囗相等
[[z-->b] -> [b-->z] -> [b =/= z] -> [not [ok z]]]
    [[proof:
        要求z转化为简体时，有b,z(不变)两种译法，出现歧义
        要求z转化为繁体时，有z(不变),b两种译法，出现歧义
    ]]

#异向囗全同
[[z-->b] -> [q-->z] -> [not [b == q == z]] -> [not [ok z]]]
    [[proof:
    #异向囗不等
    !! [[z-->b] -> [q-->z] -> [b =/= q] -> [not [ok z]]]
    #异向囗相等
    !! [[z-->b] -> [b-->z] -> [b =/= z] -> [not [ok z]]]
    [[z-->b] -> [q-->z] -> [[b =/= q]or[b == q =/= z]] -> [not [ok z]]]
    ]]

#异向囗全同囗逆否
[[z-->b] -> [q-->z] -> [ok z] -> [b == q == z]]
    [[proof:
    #异向囗全同
    !! [[z-->b] -> [q-->z] -> [not [b == q == z]] -> [not [ok z]]]
    ]]

#同向囗在左囗逆否
[[z-->b] -> [z-->q] -> [ok z] -> [b == q]]
    [[proof:
    #同向囗在左
    !! [[z-->b] -> [z-->q] -> [b =/= q] -> [not [ok z]]]
    ]]

#同向囗在右囗逆否
[[b-->z] -> [q-->z] -> [ok z] -> [b == q]]
    [[proof:
    #同向囗在右
    !! [[b-->z] -> [q-->z] -> [b =/= q] -> [not [ok z]]]
    ]]

#公理囗繁简至少居一
[[?b. [z-->b]] or [?q. [q-->z]]]
    汉字不可能既不是简体字又不是繁体字

[ok z]:
    #公理囗繁简至少居一
    !! [[?b. [z-->b]] or [?q. [q-->z]]]
    [z-->b][q-->z]:
        #异向囗全同囗逆否
        !! [[z-->b] -> [q-->z] -> [ok z] -> [b == q == z]]
        [b == q == z]
    #繁体简体不并存或自反
    [@[b,q] -> [not [q==b==z]] -> [not [[z-->b][q-->z]]]]

    [b-->z][q-->z]:
        #同向囗在右囗逆否
        !! [[b-->z] -> [q-->z] -> [ok z] -> [b == q]]
        [b == q]
    #繁体囗不存在或唯一
    [@[b,q] -> [b=/=q] -> [not [[b-->z][q-->z]]]]

    [z-->b][z-->q]:
        #同向囗在左囗逆否
        !! [[z-->b] -> [z-->q] -> [ok z] -> [b == q]]
        [b == q]
    #简体囗不存在或唯一
    [@[b,q] -> [b=/=q] -> [not [[z-->b][z-->q]]]]

#繁体简体不并存或自反
[[ok z] -> [not [q==b==z]] -> [not [[z-->b][q-->z]]]]
#繁体囗不存在或唯一
[[ok z] -> [b=/=q] -> [not [[b-->z][q-->z]]]]
#简体囗不存在或唯一
[[ok z] -> [b=/=q] -> [not [[z-->b][z-->q]]]]

[平凡自反 z =[def]= [[z-->z][@[b-->z] -> [b==z]][@[z-->q] -> [q==z]]]]
[繁简居一不兼职 z =[def]= [[?b.[b-->z]]xor[?q.[q-->z]]]]
[简体唯一 z =[def]= [[?q.[z-->q]][@b.[z-->b] -> [b==q]]]]
[繁体唯一 z =[def]= [[?b.[b-->z]][@q.[q-->z] -> [q==b]]]]
[唯一繁简字对 t s =[def]= [[繁简居一不兼职 t][繁简居一不兼职 s][简体唯一 t][繁体唯一 s]]]

[唯一可逆 z =[def]= [?n. [[唯一繁简字对 n z]or[唯一繁简字对 z n]]]]

[[ok z] <-> [[平凡自反 z]or[唯一可逆 z]]]


[ok z]:
    * [z-->z]:
    * [z-->b][b=/=z]:
    * [q-->z][q=/=z]:

    ######################
    * [z-->z]:
        [[z-->b] -> [q-->z] -> [not [b == q == z]] -> [not [ok z]]]
        [x=/=z]:
            [z-->x]:
                !! [[z-->b] -> [q-->z] -> [b =/= q] -> [not [ok z]]]
                [not [ok z]]
                _L
            [not [z-->x]]
            [x-->z]:
                !! [[z-->b] -> [q-->z] -> [b =/= q] -> [not [ok z]]]
                [not [ok z]]
                _L
            [not [x-->z]]
        [[x=/=z] -> [[not [z-->x]][not [x-->z]]]]

    * [z-->b][b=/=z]:
        [z-->x]:
            [x=/=b]:
                !! [[z-->b] -> [z-->q] -> [b =/= q] -> [not [ok z]]]
                [not [ok z]]
                _L
            [x==b]
        [x-->z]:
[[z-->b] -> [q-->z] -> [b =/= q] -> [not [ok z]]]
    * [q-->z][q=/=z]:

#]]]'''


__all__ = '''
简繁字对集
    繁体字到简体字串
    简体字到繁体字串

LookupError__unknown_TS_info4hz
    类囗囗三值判别汉字囗繁简囗囗相关

对象囗囗三值判别汉字囗繁简囗囗相关
    三值判别汉字囗繁简囗平凡自反囗
    三值判别汉字囗繁简囗唯一可逆囗
    生成囗汉字列表囗繁简囗平凡自反囗
    生成囗繁简字对列表囗繁简囗唯一可逆囗
main
    '''.split()#'''

from functools import cache

from nn_ns.CJK.CJK_data.raw.汉字繁简 import (
    简繁字对集
        ,繁体字到简体字串
        ,简体字到繁体字串
    )
from seed.text.print_txt_as_multilines import print_txt_without_space_as_py_src_varable_, print_txt_as_multilines_
from seed.tiny import check_type_is, mk_fprint#, ifNone
from seed.text.pack_char_set import pack_char_set_, pack_char_sets_, pack_char_setvary_depth_
from seed.text.pack_char_set import pack_ordered_strs_, pack_ordered_strss_, pack_ordered_strsvary_depth_

class LookupError__unknown_TS_info4hz(Exception):pass


class 类囗囗三值判别汉字囗繁简囗囗相关:
  def __init__(sf, /, *, 繁体字到简体字串, 简体字到繁体字串):
    sf.繁体字到简体字串 = 繁体字到简体字串
    sf.简体字到繁体字串 = 简体字到繁体字串

  def 囗取囗汉字繁简信息囗(sf, may_fdefault, hz, /):
    'may fdefault -> hz -> (is_info, (fdefault()|(may_Ts, may_Ss))) | ^LookupError__unknown_TS_info4hz'
    may_Ss = sf.繁体字到简体字串.get(hz)
    may_Ts = sf.简体字到繁体字串.get(hz)
    #if may_Ts is None is may_Ss:
    if not (may_Ts or may_Ss):
        #smay?
        #raise
        if not may_fdefault is None:
            fdefault = may_fdefault
            default = fdefault()
            return False, default
        raise LookupError__unknown_TS_info4hz(hz)
    return True, (may_Ts, may_Ss)

  def 三值判别汉字囗繁简囗平凡自反囗(sf, may_fdefault, hz, /):
    'may fdefault -> hz -> bool | fdefault() | ^LookupError__unknown_TS_info4hz'
    (is_info, x) = sf.囗取囗汉字繁简信息囗(may_fdefault, hz)
    if not is_info:
        default = x
        return default
    (may_Ts, may_Ss) = x
    return may_Ts == hz == may_Ss

  def 囗取囗单向囗唯一繁简字对囗(sf, may_fdefault, hz, /):
    'may fdefault -> hz -> (is_right, (fdefault()|may (T, S))) | ^LookupError__unknown_TS_info4hz'
    (is_info, x) = sf.囗取囗汉字繁简信息囗(may_fdefault, hz)
    if not is_info:
        default = x
        return False, default
    (may_Ts, may_Ss) = x
    may_ts = None
    if not may_Ts:
        t = hz
        Ss = may_Ss
        if len(Ss) == 1:
            [s] = Ss
            may_ts = t,s
            ot = s
        else:
            #非 可逆
            pass
    elif not may_Ss:
        s = hz
        Ts = may_Ts
        if len(Ts) == 1:
            [t] = Ts
            may_ts = t,s
            ot = t
        else:
            #非 可逆
            pass
    else:
        #非 唯一 <<== 身兼繁简
        pass
    return True, may_ts

  def 三值判别汉字囗繁简囗唯一可逆囗(sf, may_fdefault, hz, /, *, return_TS_if_True=False):
    'may fdefault -> hz -> bool | fdefault() | ^LookupError__unknown_TS_info4hz  #唯一:指不能身兼简繁两职:避免[[A-->B][B-->C]]'
    (is_right, x) = sf.囗取囗单向囗唯一繁简字对囗(may_fdefault, hz)
    if not is_right:
        default = x
        return default
    may_ts = x
    if may_ts:
        #单向 唯一繁简字对
        ts = may_ts
        ([t],[s]) = ts
        if not t==s:
            ot = t if hz==s else s
            assert not ot == hz
            (is_right, x) = sf.囗取囗单向囗唯一繁简字对囗(may_fdefault, ot)
            if not is_right:
                default = x
                return default
            may_ts4ot = x
            if may_ts4ot == ts:
                #双向 唯一繁简字对
                if return_TS_if_True:
                    return t+s
                return True
        else:
            #平凡自反
            pass
    else:
        #非 唯一 或 非 可逆
        pass
    return False
  @cache
  def 生成囗汉字列表囗繁简囗平凡自反囗(sf, /):
    hzs = pack_char_set_(sf.繁体字到简体字串.keys() & sf.简体字到繁体字串.keys())
        # /-\ # &
        #
    fdefault = lambda:False
    pred = lambda hz:sf.三值判别汉字囗繁简囗平凡自反囗(fdefault, hz)
    汉字列表囗繁简囗平凡自反 = hzs = pack_ordered_strs_(filter(pred, hzs))
    return 汉字列表囗繁简囗平凡自反


  @cache
  def 生成囗繁简字对列表囗繁简囗唯一可逆囗(sf, /):
    'bug:包含:  ․˙‥¨′＇═〓「“」”『‘』’〞″䊷䌶'
    if all(sf.简体字到繁体字串.values()):
        hzs = pack_char_set_(sf.繁体字到简体字串.keys() - sf.简体字到繁体字串.keys())
            # \-\ # -
            #
    else:
        hzs = pack_char_sets_([sf.繁体字到简体字串.keys(), sf.简体字到繁体字串.keys()])
            # \-/ # |
            #
    fdefault = lambda:False
    ps = set()
    for hz in hzs:
        x = sf.三值判别汉字囗繁简囗唯一可逆囗(fdefault, hz, return_TS_if_True=True)
        if x:
            ts = x
            check_type_is(str, ts)
            assert len(ts) == 2
            ([t],[s]) = ts
            ps.add(ts)
    繁简字对列表囗繁简囗唯一可逆 = pairs_str = pack_ordered_strs_(sorted(ps))
    return 繁简字对列表囗繁简囗唯一可逆



对象囗囗三值判别汉字囗繁简囗囗相关 = 类囗囗三值判别汉字囗繁简囗囗相关(繁体字到简体字串=繁体字到简体字串, 简体字到繁体字串=简体字到繁体字串)
三值判别汉字囗繁简囗平凡自反囗 = 对象囗囗三值判别汉字囗繁简囗囗相关.三值判别汉字囗繁简囗平凡自反囗
三值判别汉字囗繁简囗唯一可逆囗 = 对象囗囗三值判别汉字囗繁简囗囗相关.三值判别汉字囗繁简囗唯一可逆囗
生成囗汉字列表囗繁简囗平凡自反囗 = 对象囗囗三值判别汉字囗繁简囗囗相关.生成囗汉字列表囗繁简囗平凡自反囗
生成囗繁简字对列表囗繁简囗唯一可逆囗 = 对象囗囗三值判别汉字囗繁简囗囗相关.生成囗繁简字对列表囗繁简囗唯一可逆囗




def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
    from seed.io.may_open import open4wt, open4wt_err, open4rt

    parser = argparse.ArgumentParser(
        description='列出 平凡自反囗汉字、唯一可逆囗繁简字对'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-sz', '--sz4row', type=int
                        , default = 0
                        , help='output sz4row chars per row if sz4row > 0')
    parser.add_argument('-py', '--as_py_src', action='store_true'
                        , default = False
                        , help='output as *.py file')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    sz4row = args.sz4row
    as_py_src = args.as_py_src
    force = args.force
    oencoding = args.oencoding
    oencoding = 'utf8' if not oencoding else oencoding

    #with open_under_pkg_('seed.pkg_tools', 'xxx.dat', xencoding='u8' or None) as fin:
    #dat = read_under_pkg_('seed.pkg_tools', 'xxx.dat', xencoding='u8' or None)
    if as_py_src:
        def show_x(d, nm, /):
            print_txt_without_space_as_py_src_varable_(ofile, sz4row, d, nm)
            return
            x = d[nm]
            fprint(f"{nm} = r'''")
            print_txt_as_multilines_(ofile, sz4row, x)
            fprint(f"'''#'''")
            fprint(f"{nm} = ''.join({nm}.split())\n\n")
    else:
        def show_x(d, nm, q, /):
            x = d[nm]
            Lq = len(x)
            L,r = divmod(Lq, q)
            if r: raise logic-err
            tail = '' if q == 1 else f'*{q}'
            fprint(f'{nm}:{L}{tail}')
            print_txt_as_multilines_(ofile, sz4row, 汉字列表囗繁简囗平凡自反)
            fprint('='*22)
    if as_py_src:
        def fff(d, /):
            mdl = 类囗囗三值判别汉字囗繁简囗囗相关.__module__
            fprint(f'#generated by {mdl}\n')
            show_x(d, '汉字列表囗繁简囗平凡自反')
            show_x(d, '繁简字对列表囗繁简囗唯一可逆')
    else:
        def fff(d, /):
            fprint('='*22)
            show_x(d, '汉字列表囗繁简囗平凡自反', 1)
            show_x(d, '繁简字对列表囗繁简囗唯一可逆', 2)





    汉字列表囗繁简囗平凡自反 = 生成囗汉字列表囗繁简囗平凡自反囗()
    繁简字对列表囗繁简囗唯一可逆 = 生成囗繁简字对列表囗繁简囗唯一可逆囗()
    may_ofname = args.output
    with open4wt(may_ofname, force=force, encoding=oencoding) as ofile:
        fprint = mk_fprint(ofile)
        fff({**locals()})
        r'''
===起始:
汉字列表囗繁简囗平凡自反:14520
㓟㕕㕭㕸㖠㗅㗆㗎㞗㤻㦴㧵㨘㨢㩒㩧㩻㱦㹃

繁简字对列表囗繁简囗唯一可逆:1966*2
䊷䌶䋙䌺䝼䞍丟丢亂乱亙亘來来侶侣俁

===打补丁-简繁字对囗补丁囗㝉宁相关:之后:
汉字列表囗繁简囗平凡自反:14517
汉字列表囗繁简囗平凡自反:14513
繁简字对列表囗繁简囗唯一可逆:1965*2

'''#'''

from nn_ns.CJK.CJK_data.汉字繁简 import (
简繁字对集
,    繁体字到简体字串
,    简体字到繁体字串
)

from nn_ns.CJK.CJK_data.汉字繁简 import (
LookupError__unknown_TS_info4hz
,    类囗囗三值判别汉字囗繁简囗囗相关
,对象囗囗三值判别汉字囗繁简囗囗相关
,    三值判别汉字囗繁简囗平凡自反囗
,    三值判别汉字囗繁简囗唯一可逆囗
,    生成囗汉字列表囗繁简囗平凡自反囗
,    生成囗繁简字对列表囗繁简囗唯一可逆囗
,main
)
from nn_ns.CJK.CJK_data.汉字繁简 import *
if __name__ == "__main__":
    main()
