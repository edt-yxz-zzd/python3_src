#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/finger_tree__EPC__default.py


seed.data_funcs.finger_tree.finger_tree__EPC__default
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.finger_tree__EPC__default -x
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.finger_tree__EPC__default:__doc__
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.finger_tree__EPC__default:__doc__  -ff -v --ndiff
py_adhoc_call   seed.data_funcs.finger_tree.finger_tree__EPC__default   @f
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.finger_tree.finger_tree__EPC__default:魖双侧展翅树囗数据类型配置囗囗显式参数打包式囗囗面向组合式接口编程囗囗囗囗可优化方法缺省具象化@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc
from seed.data_funcs.finger_tree.finger_tree__EPC__default import *
#]]]'''
__all__ = r'''
魖双侧展翅树囗数据类型配置囗囗显式参数打包式囗囗面向组合式接口编程囗囗囗囗可优化方法缺省具象化
'''.split()#'''
__all__

#from seed.data_funcs.finger_tree.finger_tree__external_packed_config import 魖双侧展翅树囗数据类型配置囗囗显式参数打包式囗囗面向组合式接口编程囗囗囗囗基础
from seed.data_funcs.finger_tree.finger_tree__external_packed_config import 魖双侧展翅树囗数据类型配置囗囗显式参数打包式囗囗面向组合式接口编程囗囗囗囗部分可优化方法缺省具现囗囗下沉囗异心双翼
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import null_tuple# null_iter
from itertools import islice, chain


def __():
    #def _翅膀弹出节点兼后续囗(翅膀, **)
    ...

def _next(it, /):
    for x in it:
        return x
    raise 000

def _分裂成均衡双翼囗(sf, 长度, 节点序列, /, 左起丷右起, **kw2):
    kw3 = dict(左起丷右起=左起丷右起, **kw2)
    sz = 长度//2
    it = iter(节点序列)
    itR = it
    itL = islice(it, sz)
    it = None
    起翼 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(itL, 左翼丷右翼=左起丷右起, **kw3)
    讫翼 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(itR, 左翼丷右翼=not 左起丷右起, **kw3)
    左翼, 右翼 = _调整次序囗(起翼, 讫翼, 左起丷右起=左起丷右起)
    return 左翼, 右翼

#def _构造囗光杆树屮均衡双翼囗(长度, 节点序列, /, **kw3)
def _构造囗光杆树屮均衡双翼囗(sf, 长度, 节点序列, /, *, 左起丷右起, 参数配置, 深度):
    kw3 = _to_kw3(locals())
    if 长度 <= 参数配置.光杆树最大许可长度:
        光杆树 = sf.外参接口冖冖构造囗光杆树囗(节点序列, **kw3)
        return (False, 光杆树)
    均衡双翼 = _分裂成均衡双翼囗(sf, 长度, 节点序列, **kw3)
    return (True, 均衡双翼)


class 魖双侧展翅树囗数据类型配置囗囗显式参数打包式囗囗面向组合式接口编程囗囗囗囗可优化方法缺省具象化(魖双侧展翅树囗数据类型配置囗囗显式参数打包式囗囗面向组合式接口编程囗囗囗囗部分可优化方法缺省具现囗囗下沉囗异心双翼):
    __slots__ = ()
    ######################
    ######################
    # 可优化方法:here
    @override
    def 外参接口冖冖压入节点囗囗光杆树囗囗溢出时分裂成均衡双翼囗(sf, 光杆树, 节点, /, *, 左端丷右端, 参数配置, 深度):
        #可优化方法:底层接口
        '-> 光杆树屮均衡双翼/(光杆树丷均衡双翼, 光杆树丨均衡双翼) #均衡双翼/(左翼,右翼)'
        kw2 = dict(参数配置=参数配置, 深度=深度)
        左起丷右起 = 左端丷右端
        kw3 = dict(左起丷右起=左起丷右起, **kw2)
        it = sf.外参接口冖冖迭代囗子节点囗囗光杆树囗(光杆树, **kw3)
        it = chain([节点], it)

        L = sf.外参接口冖冖取囗长度囗囗光杆树囗(光杆树, **kw2)
        return _构造囗光杆树屮均衡双翼囗(sf, 1+L, it, **kw3)
    ######################
    @override
    def 外参接口冖冖巜外端压入节点囗囗翅膀囗囗溢出时异端弹出更深节点囗囗绝对定位囗(sf, 翅膀, 节点, /, *, 左翼丷右翼, 参数配置, 深度):
        '-> (翅膀<深度>, 魊 更深节点) #注意使用:更深节点最优许可长度'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        kw2 = dict(参数配置=参数配置, 深度=深度)
        kwA = dict(左翼丷右翼=左翼丷右翼, **kw2)
        左起丷右起 = 左翼丷右翼
        kw3A = dict(左起丷右起=左起丷右起, **kwA)

        it = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(翅膀, **kw3A)
        it = chain([节点], it)
        L = 1+sf.外参接口冖冖取囗长度囗囗翅膀囗囗绝对定位囗(翅膀, **kwA)
        if L <= 参数配置.翅膀最大许可长度:
            翅膀 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(it, **kw3A)
            return (翅膀, null_tuple)
        itR = it
        itL = islice(it, L -参数配置.更深节点最优许可长度)
        it = None
        翅膀 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(itL, **kw3A)
        kw3 = dict(左起丷右起=左起丷右起, **kw2)
        更深节点 = sf.外参接口冖冖构造囗更深节点囗(itR, **kw3)
        魊更深节点 = (更深节点,)
        return (翅膀, 魊更深节点)

    ######################
    @override
    def 外参接口冖冖巜弹出节点囗囗光杆树囗囗缺员时未定义囗(sf, 光杆树, /, *, 左端丷右端, 参数配置, 深度):
        #可优化方法:底层接口
        '-> (双侧展翅树<深度>, 节点)'
        kw2 = dict(参数配置=参数配置, 深度=深度)
        左起丷右起 = 左端丷右端
        kw3 = dict(左起丷右起=左起丷右起, **kw2)
        it = sf.外参接口冖冖迭代囗子节点囗囗光杆树囗(光杆树, **kw3)
        节点 = _next(it)
        光杆树 = sf.外参接口冖冖构造囗光杆树囗(it, **kw3)
        return (光杆树, 节点)
    ######################
    @override
    def 外参接口冖冖弹出节点囗空心树退化成光杆树囗囗绝对定位囗(sf, 左翼, 右翼, /, *, 左端丷右端, **kw2):
        '-> (光杆树<深度>, 节点)'
        左起丷右起 = 左端丷右端
        起翼, 讫翼 = _调整次序囗(左翼, 右翼, 左起丷右起=左起丷右起)

        #kwA = dict(左翼丷右翼=左翼丷右翼, **kw2)
        kw3 = dict(左起丷右起=左起丷右起, **kw2)
        it0 = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(起翼, 左翼丷右翼=左起丷右起, **kw3)
        it1 = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(讫翼, 左翼丷右翼=not 左起丷右起, **kw3)
        it = chain(it0, it1)
        节点 = _next(it)
        光杆树 = sf.外参接口冖冖构造囗光杆树囗(it, **kw3)
        return (光杆树, 节点)
    @override
    def 外参接口冖冖巜先内端压入更深节点再外端弹出节点囗囗翅膀囗囗临界缺员囗囗绝对定位囗(sf, 翅膀, 更深节点, /, *, 左翼丷右翼, **kw2):
        '-> (翅膀<深度>, 节点)'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        左起丷右起 = 左翼丷右翼
        kw3 = dict(左起丷右起=左起丷右起, **kw2)
        kw3A = dict(左翼丷右翼=左翼丷右翼, **kw3)
        it0 = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(翅膀, **kw3A)
        it1 = sf.外参接口冖冖迭代囗子节点囗囗更深节点囗(更深节点, **kw3)
        it = chain(it0, it1)
        节点 = _next(it)
        翅膀 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(it, **kw3A)
        return (翅膀, 节点)

    @override
    def 外参接口冖冖巜外端弹出节点囗囗翅膀囗囗缺员时未定义囗囗绝对定位囗(sf, 翅膀, /, *, 左翼丷右翼, **kw2):
        '-> (翅膀<深度>, 节点)'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        左起丷右起 = 左翼丷右翼
        kw3A = dict(左起丷右起=左起丷右起, 左翼丷右翼=左翼丷右翼, **kw2)
        it = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(翅膀, **kw3A)
        节点 = _next(it)
        翅膀 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(it, **kw3A)
        return (翅膀, 节点)


    ######################
    @override
    def 外参接口冖冖巜同端先弹出再压入节点囗囗光杆树囗(sf, 光杆树, 节点, /, *, 左端丷右端, **kw2):
        '-> (双侧展翅树, 节点)'
        左起丷右起 = 左端丷右端
        kw3 = dict(左起丷右起=左起丷右起, **kw2)
        it = sf.外参接口冖冖迭代囗子节点囗囗光杆树囗(光杆树, **kw3)
        节点囗囗出 = _next(it)
        it = chain([节点], it)
        光杆树 = sf.外参接口冖冖构造囗光杆树囗(it, **kw3)
        return (光杆树, 节点囗囗出)
    ######################
    @override
    def 外参接口冖冖巜外端先弹出再压入节点囗囗翅膀囗囗绝对定位囗(sf, 翅膀, 节点, /, *, 左翼丷右翼, **kw2):
        '-> (翅膀, 节点)'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        左起丷右起 = 左翼丷右翼
        kw3A = dict(左起丷右起=左起丷右起, 左翼丷右翼=左翼丷右翼, **kw2)
        it = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(翅膀, **kw3A)
        节点囗囗出 = _next(it)
        it = chain([节点], it)
        翅膀 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(it, **kw3A)
        return (翅膀, 节点囗囗出)
    ######################
    @override
    def 外参接口冖冖彳忄亍囗巜合并囗囗光杆树囗囗绝对定位囗(sf, 左囗光杆树, 右囗光杆树, /, *, 参数配置, 深度):
        '左/光杆树<深度> -> 右/光杆树<深度> -> (NotImplemented|(双侧展翅树<深度>, None))'
        return NotImplemented
        ####kw2 = dict(参数配置=参数配置, 深度=深度)
        ####左起丷右起 = False
        ####kw3 = dict(左起丷右起=左起丷右起, **kw2)
        ####it0 = sf.外参接口冖冖迭代囗子节点囗囗光杆树囗(左囗光杆树, **kw3)
        ####it1 = sf.外参接口冖冖迭代囗子节点囗囗光杆树囗(右囗光杆树, **kw3)
        ####it = chain(it0, it1)

        ####左长 = sf.外参接口冖冖取囗长度囗囗光杆树囗(左囗光杆树, **kw2)
        ####右长 = sf.外参接口冖冖取囗长度囗囗光杆树囗(右囗光杆树, **kw2)
        ####总长 = 左长 + 右长
        ####if 总长 <= 参数配置.光杆树最大许可长度:
        ####    光杆树 = sf.外参接口冖冖构造囗光杆树囗(it, **kw3)
        ####    return (光杆树, None)
        ####if not 总长 <= 2*参数配置.翅膀最大许可长度: raise NotImplementedError
        ####(左翼, 右翼) = 均衡双翼 = _分裂成均衡双翼囗(sf, 总长, it, **kw3)
        ####更深树 = 空心树囗囗更深 = 光杆树囗囗更深 = sf.外参接口冖冖构造囗光杆树囗('', **_更深囗(kw3))
        ####根深树 = sf.外参接口冖冖构造囗根深树囗囗绝对定位囗(左翼, 更深树, 右翼, **kw2)
        ####return (根深树, None)

    ######################
    ######################
    # 优化囗囗巨大囗最大许可长度:goto
    #
    # -> (魊囗焦点居前囗起半扇, 焦点居前囗累计值, 魊囗焦点诸后囗讫半扇, 魊囗焦点, 魊囗焦点居后囗讫半扇)
    @override
    def 外参接口冖冖示意分裂囗囗焦点不存在时未定义囗囗半扇版囗囗光杆树囗(sf, 光杆树, 初始累计值, 魊累积囗, /, *, 是否需囗焦点居前囗起半扇, 是否需囗焦点诸后囗讫半扇, 是否需囗焦点, 是否需囗焦点居后囗讫半扇, 左起丷右起, 参数配置, 深度):
        '-> (魊 焦点居前囗起半扇, 焦点居前囗累计值, 魊 焦点诸后囗讫半扇, 魊 焦点, 魊 焦点居后囗讫半扇)'
        kw = {**locals()}
        kw3 = _to_kw3(kw)
        kwm__kw3 = _to_kwm__kw3(kw)
        it = sf.外参接口冖冖迭代囗子节点囗囗光杆树囗(光杆树, **kw3)
        return _示意分裂囗囗依次一一搜索囗(sf, it, 初始累计值, 魊累积囗, **kwm__kw3)
    @override
    def 外参接口冖冖示意分裂囗囗焦点不存在时未定义囗囗半扇版囗囗翅膀囗囗绝对定位囗囗绝对定位囗(sf, 翅膀, 初始累计值, 魊累积囗, /, *, 是否需囗焦点居前囗起半扇, 是否需囗焦点诸后囗讫半扇, 是否需囗焦点, 是否需囗焦点居后囗讫半扇, 左翼丷右翼, 左起丷右起, 参数配置, 深度):
        '-> (魊 焦点居前囗起半扇, 焦点居前囗累计值, 魊 焦点诸后囗讫半扇, 魊 焦点, 魊 焦点居后囗讫半扇)'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        kw = {**locals()}
        kw3A = _to_kw3A(kw)
        kwm__kw3 = _to_kwm__kw3(kw)
        it = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(翅膀, **kw3A)
        return _示意分裂囗囗依次一一搜索囗(sf, it, 初始累计值, 魊累积囗, **kwm__kw3)
    @override
    def 外参接口冖冖示意分裂囗囗焦点不存在时未定义囗囗半扇版囗囗更深节点囗(sf, 更深节点, 初始累计值, 魊累积囗, /, *, 是否需囗焦点居前囗起半扇, 是否需囗焦点诸后囗讫半扇, 是否需囗焦点, 是否需囗焦点居后囗讫半扇, 左起丷右起, 参数配置, 深度):
        '-> (魊 焦点居前囗起半扇, 焦点居前囗累计值, 魊 焦点诸后囗讫半扇, 魊 焦点, 魊 焦点居后囗讫半扇)'
        kw = {**locals()}
        kw3 = _to_kw3(kw)
        kwm__kw3 = _to_kwm__kw3(kw)
        it = sf.外参接口冖冖迭代囗子节点囗囗更深节点囗(更深节点, **kw3)
        return _示意分裂囗囗依次一一搜索囗(sf, it, 初始累计值, 魊累积囗, **kwm__kw3)

    @override
    def 外参接口冖冖拼装巛光杆树半扇囗囗绝对定位囗(sf, 光杆树半扇, /, *, 左半扇丷右半扇, 参数配置, 深度):
        '-> 光杆树'
        kw2 = _to_kw2(locals())
        光杆树 = sf.外参接口冖冖构造囗光杆树囗(光杆树半扇, 左起丷右起=False, **kw2)
        return 光杆树
    @override
    def 外参接口冖冖拼装巛翅膀外端半扇囗囗绝对定位囗(sf, 翅膀外端半扇, /, *, 左翼丷右翼, 参数配置, 深度):
        '-> 光杆树屮均衡双翼 #MAY_BE 根深树/光杆树'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        # 外端 ==>> [起半扇丷讫半扇 == 起翼丷讫翼]
        # 外端 ==>> [左半扇丷右半扇 == 左翼丷右翼]
        kw2 = _to_kw2(locals())
        kw3 = dict(左起丷右起=False, **kw2)
        L = len(翅膀外端半扇)
        it = iter(翅膀外端半扇)
        return _构造囗光杆树屮均衡双翼囗(sf, L, it, **kw3)
        光杆树 = sf.外参接口冖冖构造囗光杆树囗(翅膀外端半扇, 左起丷右起=False, **kw2)
        return 光杆树


    #see: def 外参接口冖冖拼装巛翅膀内端半扇囗(sf, 翅膀内端半扇, 更深树, 异翅, /, *, 左翼丷右翼, 参数配置, 深度):
    @override
    def 外参接口冖冖取囗长度囗囗翅膀内端半扇囗囗绝对定位囗(sf, 翅膀内端半扇, /, *, 左翼丷右翼, 参数配置, 深度):
        '-> 长度'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        # 内端 ==>> [起半扇丷讫半扇 == not 起翼丷讫翼]
        # 内端 ==>> [左半扇丷右半扇 == not 左翼丷右翼]
        return len(翅膀内端半扇)

    @override
    def 外参接口冖冖拼装巛翅膀内端半扇囗囗足员囗囗绝对定位囗(sf, 翅膀内端半扇囗囗足员, /, *, 左翼丷右翼, 参数配置, 深度):
        '翅膀内端半扇<足员> -> 翅膀<同侧>'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        左起丷右起 = False
        kw3A = _to_kw3A(locals())
        翅膀 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(翅膀内端半扇囗囗足员, **kw3A)
        return 翅膀
    @override
    def 外参接口冖冖拼装巛翅膀内端半扇囗囗缺员囗囗厚势囗囗绝对定位囗(sf, 翅膀内端半扇囗囗缺员, 更深节点, /, *, 左翼丷右翼, 参数配置, 深度):
        '翅膀内端半扇<缺员> -> 更深节点 -> 翅膀<同侧>'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        #required:参数配置.缩水分裂#==>>断肢再造,滴血重生
        左起丷右起 = False
        it0 = iter(翅膀内端半扇囗囗缺员)
        kw3 = _to_kw3(locals())
        it1 = sf.外参接口冖冖迭代囗子节点囗囗更深节点囗(更深节点, **kw3)
        it0, it1 = _调整次序囗(it0, it1, 左起丷右起=左翼丷右翼)
        it = chain(it0, it1)
        kw3A = _to_kw3A(locals())
        翅膀 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(it, **kw3A)
        return 翅膀
    @override
    def 外参接口冖冖拼装巛翅膀内端半扇囗囗缺员囗囗空心囗囗绝对定位囗(sf, 翅膀内端半扇囗囗缺员, 异翅, /, *, 左翼丷右翼, **kw2):
        '翅膀内端半扇<缺员> -> 异翅 -> 光杆树屮均衡双翼/(光杆树丷均衡双翼, 光杆树丨均衡双翼)'   ' # 内端vs外端 为避免混乱 面向内外端的函数 没有 相对定位版'
        L0 = len(翅膀内端半扇囗囗缺员)
        左起丷右起 = False
        it0 = iter(翅膀内端半扇囗囗缺员)
            #左起
        L1 = sf.外参接口冖冖取囗长度囗囗翅膀囗囗绝对定位囗(异翅, 左翼丷右翼=not 左翼丷右翼, **kw2)
        kw3 = dict(左起丷右起=左起丷右起, **kw2)
        it1 = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(异翅, 左翼丷右翼=not 左翼丷右翼, **kw3)
        it0, it1 = _调整次序囗(it0, it1, 左起丷右起=左翼丷右翼)
        it = chain(it0, it1)
        L = L0 + L1
        return _构造囗光杆树屮均衡双翼囗(sf, L, it, **kw3)
    #####
    #see:def 外参接口冖冖拼装巛更深节点半扇囗(sf, 更深节点半扇, 外端囗更深树, 同侧浅翼, /, *, 左半扇丷右半扇, 参数配置, 深度):
    @override
    def 外参接口冖冖取囗长度囗囗更深节点半扇囗囗绝对定位囗(sf, 更深节点半扇, /, *, 左半扇丷右半扇, 参数配置, 深度):
        '更深节点半扇<左半扇丷右半扇> -> 长度'
        return len(更深节点半扇)
    @override
    def 外参接口冖冖拼装巛更深节点半扇囗囗足员囗囗绝对定位囗(sf, 更深节点半扇囗囗足员, /, *, 左半扇丷右半扇, 参数配置, 深度):
        '更深节点半扇<足员;左半扇丷右半扇> -> 异侧浅翼/翅膀<左翼丷右翼=not 左半扇丷右半扇>'
        左起丷右起 = False
        kw3 = _to_kw3(locals())
        异侧浅翼 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(更深节点半扇囗囗足员, 左翼丷右翼 = not 左半扇丷右半扇, **kw3)
        return 异侧浅翼
    @override
    def 外参接口冖冖拼装巛更深节点半扇囗囗缺员囗囗厚势囗囗绝对定位囗(sf, 更深节点半扇囗囗缺员, 外端囗更深节点, /, *, 左半扇丷右半扇, 参数配置, 深度):
        '更深节点半扇<缺员;左半扇丷右半扇> -> 外端囗更深节点/更深节点<原囗更深节点:外端> -> 异侧浅翼/翅膀<左翼丷右翼=not 左半扇丷右半扇>'
        #required:参数配置.缩水分裂#==>>断肢再造,滴血重生
        左起丷右起 = False
        kw3 = _to_kw3(locals())
        it0 = sf.外参接口冖冖迭代囗子节点囗囗更深节点囗(外端囗更深节点, **kw3)
        it1 = iter(更深节点半扇囗囗缺员)
        it0, it1 = _调整次序囗(it0, it1, 左起丷右起=左半扇丷右半扇)
        it = chain(it0, it1)
        kw3 = _to_kw3(locals())
        异侧浅翼 = sf.外参接口冖冖构造囗翅膀囗囗绝对定位囗(it, 左翼丷右翼 = not 左半扇丷右半扇, **kw3)
        return 异侧浅翼
    @override
    def 外参接口冖冖拼装巛更深节点半扇囗囗缺员囗囗空心囗囗绝对定位囗(sf, 更深节点半扇囗囗缺员, 同侧浅翼, /, *, 左半扇丷右半扇, 参数配置, 深度):
        '更深节点半扇<缺员;左半扇丷右半扇> -> 同侧浅翼/翅膀<左翼丷右翼=左半扇丷右半扇> -> 光杆树屮均衡双翼/(光杆树丷均衡双翼, 光杆树丨均衡双翼)'
        左起丷右起 = False
        kw3 = _to_kw3(locals())
        kw2 = _to_kw2(locals())
        L0 = sf.外参接口冖冖取囗长度囗囗翅膀囗囗绝对定位囗(同侧浅翼, 左翼丷右翼=左半扇丷右半扇, **kw2)
        it0 = sf.外参接口冖冖迭代囗子节点囗囗翅膀囗囗绝对定位囗(同侧浅翼, 左翼丷右翼=左半扇丷右半扇, **kw3)
        L1 = len(更深节点半扇囗囗缺员)
        it1 = iter(更深节点半扇囗囗缺员)
            #左起
        it0, it1 = _调整次序囗(it0, it1, 左起丷右起=左半扇丷右半扇)
        it = chain(it0, it1)
        L = L0 + L1
        return _构造囗光杆树屮均衡双翼囗(sf, L, it, **kw3)



def _示意分裂囗囗依次一一搜索囗(sf, 节点序列, 初始累计值, 魊累积囗, /, *, 是否需囗焦点居前囗起半扇, 是否需囗焦点诸后囗讫半扇, 是否需囗焦点, 是否需囗焦点居后囗讫半扇, 左起丷右起, **kw2):
    '-> (魊 焦点居前囗起半扇, 焦点居前囗累计值, 魊 焦点诸后囗讫半扇, 魊 焦点, 魊 焦点居后囗讫半扇)'
    ls = []
    累计值 = 初始累计值
    it = iter(节点序列)
    if 0:
        for i, 节点 in enumerate(it):
            缓存度量 = sf.外参接口冖冖取囗缓存度量囗囗节点囗(节点, **kw2)
            魊累计值 = 魊累积囗(累计值, 缓存度量)
            if not 魊累计值:
                break
            [累计值] = 魊累计值
            ls.append(节点)
        else:
            raise 000-'焦点不存在时未定义'
    else:
        #avoid last element
        ps = iter(enumerate(it))
        for x in ps:
            break
        else:
            raise 000-'焦点不存在时未定义:空序列'
        for y in ps:
            i, 节点 = x
            x = y
            缓存度量 = sf.外参接口冖冖取囗缓存度量囗囗节点囗(节点, **kw2)
            魊累计值 = 魊累积囗(累计值, 缓存度量)
            if not 魊累计值:
                j, z = x
                it = chain([z], it)
                break
            [累计值] = 魊累计值
            ls.append(节点)
        else:
            i, 节点 = x
                #last one

    焦点 = 节点
    ls, 累计值, 焦点, it
    if 是否需囗焦点诸后囗讫半扇 and 是否需囗焦点居后囗讫半扇:
        _ls = [*it]
    else:
        _ls = it

    if 左起丷右起:
        def 左右次序巛起讫囗(ls, /):
            return tuple(ls)[::-1]
    else:
        左右次序巛起讫囗 = tuple



    魊囗焦点居前囗起半扇 = _惰魊若囗(是否需囗焦点居前囗起半扇, lambda:左右次序巛起讫囗(ls))
    焦点居前囗累计值 = 累计值
    魊囗焦点诸后囗讫半扇 = _惰魊若囗(是否需囗焦点诸后囗讫半扇, lambda:左右次序巛起讫囗(chain([焦点],_ls)))
    魊囗焦点 = _惰魊若囗(是否需囗焦点, lambda:焦点)
    魊囗焦点居后囗讫半扇 = _惰魊若囗(是否需囗焦点居后囗讫半扇, lambda:左右次序巛起讫囗(_ls))
    return (魊囗焦点居前囗起半扇, 焦点居前囗累计值, 魊囗焦点诸后囗讫半扇, 魊囗焦点, 魊囗焦点居后囗讫半扇)




def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__


from seed.data_funcs.finger_tree.finger_tree__external_packed_config import _to_kw2, _to_kw3, _to_kw3A, _to_kwA, _to_kwm__kw3
from seed.data_funcs.finger_tree.finger_tree__external_packed_config import _调整次序囗, _更深囗, _惰魊若囗, _魊若囗, _魊变囗

from seed.data_funcs.finger_tree.finger_tree__EPC__default import 魖双侧展翅树囗数据类型配置囗囗显式参数打包式囗囗面向组合式接口编程囗囗囗囗可优化方法缺省具象化

from seed.data_funcs.finger_tree.finger_tree__EPC__default import *
