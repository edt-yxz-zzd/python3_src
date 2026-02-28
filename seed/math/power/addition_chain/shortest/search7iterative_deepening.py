#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/search7iterative_deepening.py

seed.math.power.addition_chain.shortest.search7iterative_deepening
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.search7iterative_deepening -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.search7iterative_deepening:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.power.addition_chain.shortest.search7iterative_deepening   @f

]]]'''#'''
__all__ = r'''
魖匴渐深树搜索

追加冫异常信息扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.debug.print_err import print_err
___end_mark_of_excluded_global_names__0___ = ...

def 追加冫异常信息扌(exc, /, *args, **kwds):
    class Err(type(exc)):
        def __init__(sf, exc, /, *args, **kwds):
            sf._dat = (exc, args, kwds)
            #BaseException.__init__(sf, exc, *args, **kwds)
        def __repr__(sf, /):
            return f'Err{sf._dat}'
    return Err(exc, *args, **kwds)

#.class 魖匴修剪判定器纟渐深树搜索(ABC):
#.    __slots__ = ()
#.    @abstractmethod
#.    def 取冫下上界纟树深巛状态牜跨深扌(sf, 状态牜跨深, /):
#.        '状态牜跨深 -> 下上界纟树深/(下界纟树深, 上界纟树深)'
#.    @abstractmethod
#.     def 构造冫状态牜定深扌(sf, 状态牜跨深, 假想树深, /):
#.         '状态牜跨深 -> 假想树深 -> 状态牜定深 # [状态牜跨深.下界纟树深 <= 假想树深 <= 状态牜跨深.上界纟树深]'
#.

class 魖匴渐深树搜索(ABC):
    r'''[[[
    快照链vs搜索链vs重启链vs环节列表
    [搜索链 ~=~ 环节列表/[环节]]
    [重启链 :: 搜索链{冻结}]
    [快照链 ~=~ 重启链/搜索链{冻结}]
        # 一般来说:[快照链 不同于 重启链/搜索链]
        # 一般来说:[重启链 就是 搜索链]
    #]]]'''#'''
    __slots__ = ()
    def 渐深搜索扌(sf, /, *args, **kwds):
        '-> 鬽搜索链'
        匴 = sf#匴修剪判定器
        位置 = '起始时'
        try:
            规范参数 = (std_args, std_kwds) = 匴.规范冫参数纟渐深搜索扌(*args, **kwds)
            位置 = '已有冫规范参数'
            状态牜跨深 = 匴.乊搜索起始牜批量树深扌(*std_args, **std_kwds)
            位置 = '已有冫状态牜跨深'
            (下界纟树深, 上界纟树深) = 匴.取冫下上界纟树深巛状态牜跨深扌(状态牜跨深)
            起始链牜跨深 = 匴.取冫起始链巛状态牜跨深扌(状态牜跨深)
            if not None is (鬽:=匴.取冫鬽丮假想树深辻起始链厈牜重启巛状态牜跨深扌(状态牜跨深)):
                (假想树深牜重启, 起始链牜重启) = 鬽
                if not 假想树深牜重启 == 下界纟树深:raise Exception('重启:参数有毛病')
                if not 匴.欤搜索链内容前缀扌(起始链牜跨深, 起始链牜重启):raise Exception('not 起始链牜重启.startswith(起始链牜跨深)')
            else:
                (假想树深牜重启, 起始链牜重启) = (None, None)
            鬽搜索链 = 匴.求取冫鬽搜索链牜无需搜索巛状态牜跨深扌(状态牜跨深)
            欤成功 = not None is 鬽搜索链
            if not 欤成功:
                魊快照链 = []
                for 假想树深 in range(下界纟树深, 1+上界纟树深):
                    位置 = '已有冫假想树深'
                    assert not 魊快照链
                    #状态牜定深 = 匴.构造冫状态牜定深巛状态牜跨深扌(状态牜跨深, 假想树深)
                    状态牜定深 = 匴.乊搜索起始牜指定树深扌(状态牜跨深, 假想树深)
                    鬽搜索链 = 匴.求取冫鬽搜索链牜无需搜索巛状态牜定深扌(状态牜定深)
                    欤成功 = not None is 鬽搜索链
                    if 欤成功:break
                    重启链 = 起始链牜重启 if 假想树深 == 假想树深牜重启 else 起始链牜跨深
                    状态牜定深 = 匴.重置冫状态牜定深巛重启链扌(重启链, 状态牜定深)
                    鬽状态牜定深 = 匴.定深搜索扌(状态牜定深, 魊快照链)
                        #^Err{快照链}
                    假想树深牜延迟 = 假想树深
                    位置 = '已有冫鬽状态牜定深'
                    assert 魊快照链
                    魊快照链.clear()
                    欤成功 = not None is 鬽状态牜定深
                    if 欤成功:
                        状态牜定深 = 鬽状态牜定深
                        鬽搜索链 = 搜索链 = 匴.抽取冫搜索链巛状态牜定深扌(状态牜定深)
                        break
                #end-for 假想树深 in range(下界纟树深, 1+上界纟树深):
            #end-if not 欤成功:
            位置 = '结束时'
            鬽搜索链
            if not None is 鬽搜索链:
                搜索链 = 鬽搜索链
                #if 欤成功:
                匴.检查冫中靶搜索链扌(状态牜跨深, 搜索链)
                鬽搜索链 = 搜索链
            鬽搜索链
            return 鬽搜索链
        except BaseException as exc:
            raise 匴.乊异常扌(exc, **locals())
    def 定深搜索扌(sf, 状态牜定深, 魊快照链, /):
        '-> 鬽状态牜定深'
        匴 = sf#匴修剪判定器
        快照链 = 匴.快照冫搜索链扌(状态牜定深)
        assert not 魊快照链
        魊快照链.append(快照链)
        try:
            欤成功 = 匴.欤搜索链中靶扌(状态牜定深)
            if 欤成功:
                return 状态牜定深

            欤回溯 = False
            while 1:
                if 欤回溯:
                    #回溯...
                    欤不可回溯 = not 匴.欤搜索链可回溯扌(状态牜定深)
                    if 欤不可回溯:
                        return None
                    #状态牜定深 = 匴.出栈冫搜索链扌(状态牜定深)
                    状态牜定深 = 匴.减位冫搜索链扌(状态牜定深)
                    欤回溯 = False
                    continue
                else:
                    #深入...
                    欤无效 = not 匴.欤搜索链可能有效扌(状态牜定深)
                    if 欤无效:
                        欤回溯 = True
                        continue
                    #状态牜定深 = 匴.入栈冫搜索链扌(状态牜定深)
                    状态牜定深 = 匴.增位冫搜索链牜自动扌(状态牜定深)
                    魊快照链[0] = 快照链 = 匴.快照冫搜索链扌(状态牜定深)
                    欤成功 = 匴.欤搜索链中靶扌(状态牜定深)
                    if 欤成功:
                        return 状态牜定深
                    欤回溯 = False
                    continue
        except BaseException as exc:
            raise 追加冫异常信息扌(exc, 快照链=快照链)
    #@abstractmethod
    def 重置冫状态牜定深巛重启链扌(sf, 重启链, 状态牜定深, /):
        '重启链 -> 状态牜定深 -> 状态牜定深'
        匴 = sf#匴修剪判定器
        环节列表牜目标 = 匴.拆分冫环节列表巛重启链扌(重启链)
        _重启链 = 搜索链 = 匴.抽取冫搜索链巛状态牜定深扌(状态牜定深)
        环节列表牜起始 = 匴.拆分冫环节列表巛重启链扌(_重启链)
        if not 匴.欤搜索链内容前缀扌(_重启链, 重启链):raise Exception(_重启链, 重启链)#ValueError
        assert 环节列表牜起始 == 环节列表牜目标[:len(环节列表牜起始)]
        for 环节 in 环节列表牜目标[len(环节列表牜起始):]:
            状态牜定深 = 匴.增位冫搜索链牜指定扌(环节, 状态牜定深)
        状态牜定深
        _2重启链 = 搜索链 = 匴.抽取冫搜索链巛状态牜定深扌(状态牜定深)
        环节列表牜终止 = 匴.拆分冫环节列表巛重启链扌(_2重启链)
        if not 匴.欤搜索链内容前缀扌(_2重启链, 重启链):raise Exception(_2重启链, _重启链, 重启链)#ValueError
        assert 环节列表牜终止 == 环节列表牜目标
        return 状态牜定深

    def 构造冫输出器乊异常扌(sf, exc, /):
        'exc -> print6exc_/((**kwds)->None)'
        def print6exc_(**kwds):
            for nm, v in kwds.items():
                print_err(f'{nm!s}={v!r}')
        return print6exc_
    def 抛出异常巛输出器乊异常扌(sf, exc, print6exc_, /):
        'exc -> print6exc_ -> ^BaseException'
        raise
    def 乊异常扌(sf, exc, /, *, 位置, 规范参数=NotImplemented, 状态牜跨深=NotImplemented, 假想树深牜重启=NotImplemented, 起始链牜重启=NotImplemented, 起始链牜跨深=NotImplemented, 鬽搜索链=NotImplemented, 上界纟树深=NotImplemented, 假想树深=NotImplemented, 假想树深牜延迟=NotImplemented, 魊快照链=NotImplemented, 鬽状态牜定深=NotImplemented, **__):
        匴 = sf#匴修剪判定器
        print6exc_ = 匴.构造冫输出器乊异常扌(exc)
        match getattr(exc, '_dat', None):
            case (_exc, (), {'快照链':快照链}):
                位置 = '已有冫快照链'
                快照链
            #case
        位置
        if 位置 == '已有冫假想树深' and 魊快照链:
            [快照链] = 魊快照链
            位置 = '已有冫快照链'
        位置
        while 1:
            if 位置 == '起始时': break
            print6exc_(规范参数牜本次=规范参数)
            if 位置 == '已有冫规范参数': break
            重启信息牜本次起始 = 匴.抽取冫重启信息牜本次起始巛状态牜跨深扌(状态牜跨深)
            print6exc_(重启信息牜起始=重启信息牜本次起始)
            if 位置 == '已有冫状态牜跨深': break
            if (not None is 鬽搜索链):
                #况态{无需搜索}
                搜索链 = 鬽搜索链
                位置 = '结束时'
            elif 位置 == '已有冫鬽状态牜定深':
                假想树深 = 假想树深牜延迟
                魊快照链.clear()
                欤成功 = (not None is 鬽状态牜定深)
                if 欤成功:
                    状态牜定深 = 鬽状态牜定深
                    搜索链 = 匴.抽取冫搜索链巛状态牜定深扌(状态牜定深)
                    位置 = '结束时'
                elif 假想树深 == 上界纟树深:
                    位置 = '结束时'
                else:
                    假想树深 += 1
                    位置 = '已有冫假想树深'
                位置
            位置
            match 位置:
                case '结束时':
                    if 欤成功:
                        print6exc_(搜索链牜待检查=搜索链, 成功='待检查')
                    else:
                        #return 鬽搜索链
                        print6exc_(鬽搜索链=鬽搜索链, 失败=True)#失败
                    break
                case '已有冫假想树深':
                    假想树深
                    重启链 = 起始链牜重启 if 假想树深 == 假想树深牜重启 else 起始链牜跨深
                case '已有冫快照链':
                    假想树深
                    #重启链 = 匴.构造冫重启链巛状态牜跨深辻快照链扌(状态牜跨深, 快照链)
                    重启链 = 匴.构造冫重启链巛快照链扌(快照链)
                case _:
                    print6exc_(位置牜未知=位置, 理矩错误=True)
                #case
            重启链
            print6exc_(下界纟树深牜下次=假想树深)
            print6exc_(重启链牜下次=重启链)
            break
        #end-while 1:
        匴.抛出异常巛输出器乊异常扌(exc, print6exc_)
        print_err(f'理矩错误:{type(匴)}.抛出异常巛输出器乊异常扌():没有抛出异常')
        raise

    #@abstractmethod
    def 抽取冫搜索链巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 搜索链'
        匴 = sf
        快照链 = 匴.快照冫搜索链扌(状态牜定深)
        重启链 = 匴.构造冫重启链巛快照链扌(快照链)
        搜索链 = 重启链
        return 搜索链



    #grep '匴[.]\w\+' ../../python3_src/seed/math/power/addition_chain/shortest/search7iterative_deepening.py
    @abstractmethod
    def 规范冫参数纟渐深搜索扌(sf, /, *args, **kwds):
        '-> (std_args, std_kwds)'
        #eg:[None=>下上界纟最小显链长纟(靶值)]
        #eg:[None=>因数分解纟(靶值)]
        #eg:[None=>更小靶值讠最小显链长{靶值}]
        return (args, kwds)
    @abstractmethod
    def 乊搜索起始牜批量树深扌(sf, /, *std_args, **std_kwds):
        '-> 状态牜跨深{内含:靶值}{内含:下上界纟树深}{内含:重启信息牜本次起始}'
    @abstractmethod
    def 抽取冫重启信息牜本次起始巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 重启信息牜本次起始'
    @abstractmethod
    def 求取冫鬽搜索链牜无需搜索巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 鬽搜索链'
        #eg:无需搜索:[阳爻数{靶值}<=3]
    @abstractmethod
    def 取冫下上界纟树深巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 下上界纟树深/(下界纟树深, 上界纟树深)'
    @abstractmethod
    def 取冫鬽丮假想树深辻起始链厈牜重启巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 鬽 (假想树深牜重启, 起始链牜重启)'
    @abstractmethod
    def 取冫起始链巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 起始链牜跨深'
    @abstractmethod
    def 欤搜索链内容前缀扌(sf, 搜索链冃前缀, 搜索链冃全链, /):
        '搜索链冃前缀 -> 搜索链冃全链 -> 欤前缀/bool'
    @abstractmethod
    def 乊搜索起始牜指定树深扌(sf, 状态牜跨深, 假想树深, /):
        '状态牜跨深 -> 假想树深 -> 状态牜定深{内含:搜索链}{内含:假想树深}{内含:靶值}'
        #匴.构造冫状态牜定深巛状态牜跨深扌
    @abstractmethod
    def 求取冫鬽搜索链牜无需搜索巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 鬽搜索链'
        #eg:无需搜索:因数分解型、加一型
    @abstractmethod
    def 检查冫中靶搜索链扌(sf, 状态牜跨深, 搜索链, /):
        '状态牜跨深 -> 搜索链 -> None|^Exception'
    @abstractmethod
    def 快照冫搜索链扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 快照链{内含:搜索链}'
    @abstractmethod
    def 构造冫重启链巛快照链扌(sf, 快照链, /):
        '快照链{内含:搜索链} -> 重启链'
        #.def 构造冫重启链巛状态牜跨深辻快照链扌(sf, 状态牜跨深, 快照链, /):
        #.    '状态牜跨深 -> 快照链{内含:搜索链} -> 重启链'
    @abstractmethod
    def 欤搜索链中靶扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 欤成功/bool'
    @abstractmethod
    def 欤搜索链可回溯扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 欤可回溯/欤可减位/bool'
    @abstractmethod
    def 欤搜索链可能有效扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链}{内含:假想树深}{内含:靶值} -> 欤有效/欤可增位/bool #[未超长{假想树深}][未中靶][未判定必然无法中靶]'
    @abstractmethod
    def 减位冫搜索链扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 状态牜定深'
        #匴.出栈冫搜索链扌
    @abstractmethod
    def 增位冫搜索链牜自动扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 状态牜定深 #[以候选名单中下一个候选者作为末位环节]'
        #匴.入栈冫搜索链扌
    @abstractmethod
    def 增位冫搜索链牜指定扌(sf, 环节冃末位, 状态牜定深, /):
        '环节冃末位 -> 状态牜定深{内含:搜索链} -> 状态牜定深|^Exception{末位环节不在候选名单上}'
    @abstractmethod
    def 拆分冫环节列表巛重启链扌(sf, 重启链, /):
        '重启链 -> 环节列表/[环节]'





__all__
from seed.math.power.addition_chain.shortest.search7iterative_deepening import 魖匴渐深树搜索, 追加冫异常信息扌
from seed.math.power.addition_chain.shortest.search7iterative_deepening import *
