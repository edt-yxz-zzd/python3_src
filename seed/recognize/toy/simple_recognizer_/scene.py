#__all__:goto
r'''[[[

seed.recognize.toy.simple_recognizer_.scene
py -m nn_ns.app.debug_cmd   seed.recognize.toy.simple_recognizer_.scene -x
py -m nn_ns.app.doctest_cmd seed.recognize.toy.simple_recognizer_.scene:__doc__
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.register:魖工厂场景@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.scene:魖解码场景@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.toy.simple_recognizer_.scene:乸解码场景@T    =T      ++exclude_prefixes:_       +exclude_attrs5listed_in_cls_doc

#]]]'''
__all__ = r'''
魖工厂场景
魖解码场景
    乸解码场景
        构造冫解码场景扌

乸可变真值
乸私用空间
乸具名私用空间
乸私钥
乸具名私钥

构造冫解码器巛名扌
    注册冫解码器名纟公用扌
    注册冫解码器名纟私用扌

魖注册处
    乸具名注册处
    乸具名注册处暨用户数据
    构造冫具名注册处扌

构造冫具名对象乊缺省扌
    构造冫具名注册处乊缺省扌
    构造冫解码场景乊缺省扌

取冫变量值扌
    注册冫变量名纟公用扌
    注册冫变量名纟私用扌
具名扌
    注册冫变换结果函数纟具名解码器扌
    取冫变换结果函数纟具名解码器扌

'''.split()#'''
__all__

___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.toy.simple_recognizer_._common import abstractmethod, override, ABC
from seed.recognize.toy.simple_recognizer_._common import _4repr, _4repr_named, _巛彧
from seed.recognize.toy.simple_recognizer_._common import check_type_le, check_type_is, ifNone, ifNonef
from seed.tiny_.check import check_callable
from seed.tiny_.check import check_may_
from seed.tiny_.check import check_pseudo_qual_name
from seed.tiny import curry1
___end_mark_of_excluded_global_names__0___ = ...


from seed.recognize.toy.simple_recognizer_.register import 乸可变真值
from seed.recognize.toy.simple_recognizer_.register import 乸私用空间,乸具名私用空间,乸私钥,乸具名私钥
from seed.recognize.toy.simple_recognizer_.register import 魖注册处,乸具名注册处,乸具名注册处暨用户数据
from seed.recognize.toy.simple_recognizer_.register import 构造冫具名对象乊缺省扌,构造冫具名注册处乊缺省扌,构造冫具名注册处扌
from seed.recognize.toy.simple_recognizer_.register import 魖工厂场景,注册冫变量名纟公用扌,注册冫变量名纟私用扌,取冫变量值扌
__all__












if 1:
    #用于:调试
    ######################
    #def 包装灬扌(sf, 乊起始扌, 乊锁定扌, 乊失败扌, 乊匹配扌, 乊结束扌, 解码器名, /, *, 鬽名):
    def _名凵乊起始扌(名, 包装解码器, 全文暨起讫讫, /):
        '包装解码器 -> 全文暨起讫讫 -> None'
        print('进入:', 名, 全文暨起讫讫.起地址)
        return None
    def _名凵乊结束扌(名, 包装解码器, 全文暨起讫讫, 讫错果, /):
        '包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果'
        print('退出:', 名, 全文暨起讫讫.起地址, 讫错果[:2])
        print()
        return 讫错果


######################
######################
######################
def _构造冫鬽解码器巛名扌(sf, 解码器名, /, *, 仅测试):
    '-> 鬽 魖解码器 if not 仅测试 else 欤已注册/bool'
    if callable(解码器名):
        #魖辅助构造表达式
        if 仅测试: return True
        f = 解码器名
        场景 = sf
        #bug:解码器 = f(解码器名)
        解码器 = f(场景)
    elif hasattr(解码器名, '场景') and isinstance(解码器名, 魖解码器):
        if 仅测试: return True
        解码器 = 解码器名
    else:
        return sf.罓注册处纟解码器.取冫目标值扌(解码器名, 鬽槑目标值:=lambda:None, 仅测试=仅测试)
    if 仅测试: raise 000
    return 解码器
######################
######################
######################
def _检查冫场景纟解码器扌(场景, 解码器, /):
    if not 解码器.场景 is 场景: raise TypeError('场景 必须 一致')
def _检查冫解码器扌(场景, 解码器, /):
    check_type_le(魖解码器, 解码器)
    _检查冫场景纟解码器扌(场景, 解码器)
def 构造冫解码器巛名扌(场景, 解码器名, /):
    r'''
:: 场景/魖解码场景 -> 解码器名/??? -> 解码器/魖解码器

解码器名 =:
    * :: (魖解码场景 -> 魖解码器)
        用户自定义
        [魖辅助构造表达式 <: (魖解码场景 -> 魖解码器)]
    * :: 魖解码器
        立即值
    * 场景.欤已注册冫解码器名扌(解码器名)
        未来值=>解决循环引用
            [引用式 <: 魖辅助构造表达式]
        注册冫解码器名纟公用扌
        注册冫解码器名纟私用扌

    '''#'''
    解码器 = 场景.构造冫解码器巛名扌(解码器名)
    return 解码器
def 注册冫解码器名纟公用扌(场景, 解码器名纟公用, 解码器, /):
    ':: 场景/魖解码场景 -> 解码器名纟公用/hashable -> 解码器 -> None'
    场景.注册冫解码器名纟公用扌(解码器名纟公用, 解码器)
def 注册冫解码器名纟私用扌(场景, 解码器名纟私用, 私用空间, /):
    ':: 场景/魖解码场景 -> 解码器名纟私用{eq==is} -> 私用空间/weakable_mapping<解码器名纟私用,解码器> -> None #参见:乸私用空间,乸具名私用空间,乸私钥,乸具名私钥'
    场景.注册冫解码器名纟私用扌(解码器名纟私用, 私用空间)



def 具名扌(sf, 鬽名, 解码器名, /):
    if 鬽名:
        名 = 鬽名
        check_pseudo_qual_name(名)
        #
        预处理器纟构造冫具名解码器 = sf.预处理器纟构造冫具名解码器
        后处理器纟构造冫具名解码器 = sf.后处理器纟构造冫具名解码器
        解码器名 = 预处理器纟构造冫具名解码器(sf, 名,解码器名)
        debug = sf.欤调试纟构造冫具名解码器
        if debug:
            解码器名 = sf.包装灬扌(乊起始扌:=curry1(_名凵乊起始扌,名), 乊锁定扌:=None, 乊失败扌:=None, 乊匹配扌:=None, 乊结束扌:=curry1(_名凵乊结束扌,名), 解码器名, 鬽名=None)
        #
        欤自动注册冫具名解码器 = sf.欤自动注册冫具名解码器
        欤自动变换结果冫具名解码器 = sf.欤自动变换结果冫具名解码器
        #
            #更新:expr.py
        if 欤自动注册冫具名解码器:
            if sf.欤已注册冫解码器名扌(名):
                sf.注册冫解码器名纟公用扌(名, sf.零解码器扌()) #^异常
                raise 000
        if 欤自动变换结果冫具名解码器:
            #由 乸具名解码器 负责？还是 再加一个 乸变换结果解码器？
            #   ...
            #   区别在于 设定 [欤自动变换结果冫具名解码器:=True] 前后不同:
            #       已注册 具名解码器 还要不要 响应 这一变动？？
            #
            # [函数名 not 名]
            鬽变换结果扌 = sf.取冫变换结果函数纟具名解码器扌(名, lambda:None)
            if not (变换结果扌:=鬽变换结果扌) is None:
                解码器 = sf.变换结果解码器扌(None, 变换结果扌, 解码器名)
                解码器名 = 解码器
            解码器名
        解码器名
    解码器名
    具名解码器 = sf.罓具名扌(鬽名, 解码器名)
    if 鬽名:
        if 欤自动注册冫具名解码器:
            sf.注册冫解码器名纟公用扌(名, 具名解码器)
        后处理器纟构造冫具名解码器(sf, 具名解码器)
    return 具名解码器
class 魖解码场景(魖工厂场景):
    r'''[[[
######################
news:
    ++公钥纟欤调试纟构造冫具名解码器
######################
news:
    ++公钥纟预处理器纟构造冫具名解码器
    ++公钥纟后处理器纟构造冫具名解码器
######################
news:
    意图:避免 表达式 多次重复求值:树->DAG复用构造结果
    ++公钥纟欤自动注册冫具名解码器
        注册处纟解码器
        欤自动注册冫具名解码器
    ++公钥纟欤自动变换结果冫具名解码器
        注册处纟变量
        欤自动变换结果冫具名解码器
    ++罓构造冫变量名纟变换结果函数纟具名解码器扌
        注册冫变换结果函数纟具名解码器扌
        取冫变换结果函数纟具名解码器扌

######################
######################
######################
######################
魖工厂场景:
new_abstract_methods:
    `罓注册处纟变量
new_concrete_methods:
    罓检查冫变量值扌
    匞参数配置包
    欤已注册冫变量名扌
    注册冫变量名纟公用扌
    注册冫变量名纟私用扌
    取冫变量值扌
===
魖解码场景:
new_abstract_methods:
    `罓构造冫解码器纟并联扌
    `罓注册处纟解码器
    `罓注册处纟变量
new_concrete_methods:
    罓构造冫解码器巛名扌
    欤已注册冫解码器名扌
    注册冫解码器名纟公用扌
    注册冫解码器名纟私用扌
    构造冫解码器巛名扌
    构造冫解码器纟并联扌
    兼顾灬扌
    兼顾扌
    互斥并联灬扌
    互斥并联扌
    优先并联灬扌
    优先并联扌
    串联灬扌
    串联扌
    串联时忽略结果扌
    序列解码器扌
    码元集合匹配解码器扌
    码元串常量匹配解码器扌
    码元串定长读取解码器扌
    失败零解码器扌
    恒果零解码器扌
    直达终点解码器扌
    前瞻零解码器扌
    逆转成败解码器扌
    变换讫错果解码器扌
    变换结果解码器扌
    结尾限长序列解码器扌
    间隙锁定串联扌
    元素锁定串联扌
    首非零锁定串联扌
    首锁定串联扌
    尾锁定串联扌
    实心锁定串联扌
    零解码器扌
    具名扌
    引用扌
    包装灬扌
    包装扌
    #]]]'''#'''
    __slots__ = ()
    def 罓构造冫变量名纟变换结果函数纟具名解码器扌(sf, 名纟具名解码器, /):
        '名<具名解码器> -> 函数名<变换结果扌> #配合:欤自动变换结果冫具名解码器'
        return f'变换结果扌:{名纟具名解码器!s}'

    #@abstractmethod
    def 罓构造冫解码器巛名扌(sf, 解码器名, /):
        '-> 魖解码器 | ^LookupError'
        raise LookupError(解码器名)

    @abstractmethod
    def 罓构造冫解码器纟并联扌(sf, 并联解码器, 索引号冃分支, 结果冃锁定, 部分构造参数冃后续, /):
        '-> 魖解码器'



    @property
    @abstractmethod
    def 罓注册处纟解码器(sf, /):
        r'''
        :: -> 注册处纟解码器/解码区/魖注册处<解码器名,解码器>
         #用于 构造冫解码器巛名扌/乸引用解码器 解引用
        .公用区/{解码器名纟公用:解码器}
        .私用区/WeakValueDictionary<解码器名纟私用/AddrAsHash, 私用空间/weakable_mapping<解码器名纟私用,解码器> >
        '''#'''
    @property
    @abstractmethod
    @override
    def 罓注册处纟变量(sf, /):
        r'''
        :: -> 注册处纟变量/变量区/魖注册处<变量名,变量值>
        主要配合 变果式+乸具名引用函数 解引用
        '''#'''

    #####
    公钥纟欤调试纟构造冫具名解码器 = 乸具名私钥('公钥纟欤调试纟构造冫具名解码器')
    #####
    公钥纟预处理器纟构造冫具名解码器 = 乸具名私钥('公钥纟预处理器纟构造冫具名解码器')
    公钥纟后处理器纟构造冫具名解码器 = 乸具名私钥('公钥纟后处理器纟构造冫具名解码器')
    #####
    公钥纟欤自动注册冫具名解码器 = 乸具名私钥('公钥纟欤自动注册冫具名解码器')
    公钥纟欤自动变换结果冫具名解码器 = 乸具名私钥('公钥纟欤自动变换结果冫具名解码器')
    #####
    @property
    def 欤调试纟构造冫具名解码器(sf, /):
        '-> bool #简化访问:公钥纟欤调试纟构造冫具名解码器'
        #乸可变真值
        真值丷可变真值 = sf.取冫变量值扌(sf.公钥纟欤调试纟构造冫具名解码器, lambda:False)
        return bool(真值丷可变真值)
    @欤调试纟构造冫具名解码器.setter
    def 欤调试纟构造冫具名解码器(sf, 欤调试纟构造冫具名解码器, /):
        'bool -> None # 简化访问:公钥纟欤调试纟构造冫具名解码器'
        check_type_is(bool, 欤调试纟构造冫具名解码器)
        真值丷可变真值 = sf.取冫变量值扌(sf.公钥纟欤调试纟构造冫具名解码器, lambda:False)
        if bool(真值丷可变真值) is 欤调试纟构造冫具名解码器:
            return
        if 真值丷可变真值 is False:
            #未初始化
            可变真值 = 乸可变真值(欤调试纟构造冫具名解码器)
            sf.注册冫变量名纟公用扌(sf.公钥纟欤调试纟构造冫具名解码器, _欤调试纟构造冫具名解码器:=可变真值)
        else:
            可变真值 = 真值丷可变真值
            可变真值 <<= 欤调试纟构造冫具名解码器
        assert sf.欤调试纟构造冫具名解码器 is 欤调试纟构造冫具名解码器
        return

    #####
    @property
    def 预处理器纟构造冫具名解码器(sf, /):
        '-> (场景->名->解码器名->解码器名) #简化访问:公钥纟预处理器纟构造冫具名解码器'
        return sf.取冫变量值扌(sf.公钥纟预处理器纟构造冫具名解码器, lambda:lambda 场景,名,解码器名:解码器名)
    @预处理器纟构造冫具名解码器.setter
    def 预处理器纟构造冫具名解码器(sf, 预处理器纟构造冫具名解码器, /):
        '(场景->名->解码器名->解码器名) -> None # 简化访问:公钥纟预处理器纟构造冫具名解码器'
        sf.注册冫变量名纟公用扌(sf.公钥纟预处理器纟构造冫具名解码器, 预处理器纟构造冫具名解码器)
    #####
    @property
    def 后处理器纟构造冫具名解码器(sf, /):
        '-> (场景->具名解码器->None) #简化访问:公钥纟后处理器纟构造冫具名解码器'
        return sf.取冫变量值扌(sf.公钥纟后处理器纟构造冫具名解码器, lambda:lambda 场景,具名解码器:None)
    @后处理器纟构造冫具名解码器.setter
    def 后处理器纟构造冫具名解码器(sf, 后处理器纟构造冫具名解码器, /):
        '(场景->具名解码器->None) -> None #简化访问:公钥纟后处理器纟构造冫具名解码器'
        sf.注册冫变量名纟公用扌(sf.公钥纟后处理器纟构造冫具名解码器, 后处理器纟构造冫具名解码器)
    #####
    #####
    @property
    def 欤自动注册冫具名解码器(sf, /):
        '简化访问:公钥纟欤自动注册冫具名解码器'
        return sf.取冫变量值扌(sf.公钥纟欤自动注册冫具名解码器, lambda:False)
    @欤自动注册冫具名解码器.setter
    def 欤自动注册冫具名解码器(sf, 欤自动注册冫具名解码器, /):
        '简化访问:公钥纟欤自动注册冫具名解码器'
        sf.注册冫变量名纟公用扌(sf.公钥纟欤自动注册冫具名解码器, 欤自动注册冫具名解码器)
    #####
    @property
    def 欤自动变换结果冫具名解码器(sf, /):
        '简化访问:公钥纟欤自动变换结果冫具名解码器'
        return sf.取冫变量值扌(sf.公钥纟欤自动变换结果冫具名解码器, lambda:False)
    @欤自动变换结果冫具名解码器.setter
    def 欤自动变换结果冫具名解码器(sf, 欤自动变换结果冫具名解码器, /):
        '简化访问:公钥纟欤自动变换结果冫具名解码器'
        sf.注册冫变量名纟公用扌(sf.公钥纟欤自动变换结果冫具名解码器, 欤自动变换结果冫具名解码器)
    #####
    def 注册冫变换结果函数纟具名解码器扌(sf, 名纟具名解码器, 变换结果扌, /):
        '名<具名解码器> -> 变换结果扌/(果->果) -> None #配合:欤自动变换结果冫具名解码器 #实际允许类型:见:变换结果解码器扌:鬽变换结果扌丨变换讫错果扌丨两段式篡改器'
        check_callable(变换结果扌)
        函数名 = sf.罓构造冫变量名纟变换结果函数纟具名解码器扌(名纟具名解码器)
        sf.注册冫变量名纟公用扌(函数名, 变换结果扌)
    def 取冫变换结果函数纟具名解码器扌(sf, 名纟具名解码器, 槑变换结果函数, /):
        '名<具名解码器> -> 槑变换结果函数/(() -> (果->果)) -> 变换结果扌/(果->果) #配合:欤自动变换结果冫具名解码器 #实际允许类型:见:变换结果解码器扌:鬽变换结果扌丨变换讫错果扌丨两段式篡改器'
        函数名 = sf.罓构造冫变量名纟变换结果函数纟具名解码器扌(名纟具名解码器)
        return sf.取冫变量值扌(函数名, 槑变换结果函数)
    #####


    r'''[[[

    @abstractmethod
    def 罓构造冫新解码场景扌(sf, 注册处纟解码器, 注册处纟变量, /):
        '-> 场景/魖解码场景'
    def 更新冫注册处纟解码器扌(sf, 彧注册处纟解码器, /):
        '-> 场景#彧:『...』非『None』'
        return sf.构造冫新场景扌(彧注册处纟解码器, 彧注册处纟变量:=...)
    def 更新冫注册处纟变量扌(sf, 彧注册处纟变量, /):
        '-> 场景#彧:『...』非『None』'
        return sf.构造冫新场景扌(彧注册处纟解码器:=..., 彧注册处纟变量)
    def 构造冫新场景扌(sf, 彧注册处纟解码器, 彧注册处纟变量, /):
        '-> 场景#彧:『...』非『None』'
        def f(彧新值, 旧值, /):
            '-> (欤新, 值)'
            if 彧新值 is ... or 彧新值 is 旧值:
                欤新 = False
                值 = 旧值
            else:
                欤新 = True
                值 = 彧新值
            return (欤新, 值)
        (欤新纟解码器, 注册处纟解码器) = f(彧注册处纟解码器, sf.罓注册处纟解码器)
        (欤新纟变量, 注册处纟变量) = f(彧注册处纟变量, sf.罓注册处纟变量)
        if not (欤新纟解码器 or 欤新纟变量):
            return sf
        return sf.罓构造冫新解码场景扌(注册处纟解码器, 注册处纟变量)
    #]]]'''#'''















    ######################

    def 欤已注册冫解码器名扌(sf, 解码器名, /):
        '-> 欤已注册/bool'
        欤已注册 = _构造冫鬽解码器巛名扌(sf, 解码器名, 仅测试=True)
        return 欤已注册

    def 注册冫解码器名纟公用扌(sf, 解码器名纟公用, 解码器, /):
        '解码器名纟公用/hashable -> 解码器 -> None'
        if 1:
            _检查冫解码器扌(sf, 解码器)
        sf.罓注册处纟解码器.注册纟公用扌(解码器名纟公用, 解码器)
        return
    def 注册冫解码器名纟私用扌(sf, 解码器名纟私用, 私用空间, /):
        '解码器名纟私用{eq==is} -> 私用空间/weakable_mapping<解码器名纟私用,解码器> -> None #参见:乸私用空间,乸具名私用空间,乸私钥,乸具名私钥'
        if 1:
            解码器 = 私用空间[解码器名纟私用]
            _检查冫解码器扌(sf, 解码器)
        sf.罓注册处纟解码器.注册纟私用扌(解码器名纟私用, 私用空间)
        return


    def 构造冫解码器巛名扌(sf, 解码器名, /):
        '-> 魖解码器'
        鬽解码器 = _构造冫鬽解码器巛名扌(sf, 解码器名, 仅测试=False)
        if 鬽解码器 is None:
            解码器 = sf.罓构造冫解码器巛名扌(解码器名)
                # ^LookupError
        else:
            解码器 = 鬽解码器
        #_检查冫解码器扌(sf, 解码器)
        _检查冫场景纟解码器扌(sf, 解码器)
        return 解码器
    ######################
    def 构造冫解码器纟并联扌(sf, 并联解码器, 索引号冃分支, 结果冃锁定, 部分构造参数冃后续, /):
        '-> 魖解码器'
        #_检查冫解码器扌(sf, 并联解码器)
        _检查冫场景纟解码器扌(sf, 并联解码器)
        if 部分构造参数冃后续 is ...:
            #尾递归
            部分构造参数冃后续 = 并联解码器
        ######################

        if 部分构造参数冃后续 is None:
            #now:两段式宽解码扌
            #None => 实心锁定
            #两段式宽解码扌 => 『[(x,y)] --> [((x,y)|z)]』
            #xxx#raise TypeError('now:using:两段式宽解码扌')
            #需求源自:魖辅助构造表达式._call2_
            解码器冃后续 = sf.恒果零解码器扌(结果冃锁定)
        elif callable(部分构造参数冃后续):
            f = 部分构造参数冃后续
            #无需:场景 = sf
            解码器冃后续 = f(并联解码器, 索引号冃分支, 结果冃锁定)
        elif hasattr(部分构造参数冃后续, '场景') and isinstance(部分构造参数冃后续, 魖解码器):
            解码器冃后续 = 部分构造参数冃后续
            _检查冫场景纟解码器扌(sf, 解码器冃后续)
            解码器冃后续 = sf.串联扌([sf.恒果零解码器扌(结果冃锁定), 解码器冃后续])
                #需求源自:乸结尾限长序列解码器
        else:
            解码器冃后续 = sf.罓构造冫解码器纟并联扌(并联解码器, 索引号冃分支, 结果冃锁定, 部分构造参数冃后续)
        _检查冫场景纟解码器扌(sf, 解码器冃后续)
        return 解码器冃后续
    ######################
    ######################
    ######################

    #####
    def 兼顾灬扌(sf, /, *列表纟解码器名):
        '-> 乸定域解码器|解码器乊唯一'
        if len(列表纟解码器名) == 1:
            return sf.串联扌(列表纟解码器名)
        return sf.兼顾扌(限制冫步进丷前瞻:=False, 保底索引号:=0, 列表纟解码器名)
    def 兼顾扌(sf, 限制冫步进丷前瞻, 保底索引号, 列表纟解码器名, /):
        '-> 乸定域解码器'
        return 乸定域解码器(sf, 限制冫步进丷前瞻, 保底索引号, 列表纟解码器名)
    def 互斥并联灬扌(sf, /, *列表纟丮锁定丶动态厈):
        '-> 乸互斥并联解码器'
        if len(列表纟丮锁定丶动态厈) == 1 and type(列表纟丮锁定丶动态厈[0]) is not tuple:
            return sf.串联扌(列表纟丮锁定丶动态厈)
        return sf.互斥并联扌(鬽错误乊无锁定:=None, 彧鬽错误乊多锁定:=None, 列表纟丮锁定丶动态厈)
    def 互斥并联扌(sf, 鬽错误乊无锁定, 彧鬽错误乊多锁定, 列表纟丮锁定丶动态厈, /):
        '-> 乸互斥并联解码器'
        return 乸互斥并联解码器(sf, 鬽错误乊无锁定, 彧鬽错误乊多锁定, 列表纟丮锁定丶动态厈)
    def 优先并联灬扌(sf, /, *列表纟丮锁定丶动态厈):
        '-> 乸优先并联解码器'
        if len(列表纟丮锁定丶动态厈) == 1 and type(列表纟丮锁定丶动态厈[0]) is not tuple:
            return sf.串联扌(列表纟丮锁定丶动态厈)
        return sf.优先并联扌(鬽错误乊无锁定:=None, 鬽解码器名乊无锁定:=None, 列表纟丮锁定丶动态厈)
    def 优先并联扌(sf, 鬽错误乊无锁定, 鬽解码器名乊无锁定, 列表纟丮锁定丶动态厈, /):
        '-> 乸优先并联解码器'
        return 乸优先并联解码器(sf, 鬽错误乊无锁定, 鬽解码器名乊无锁定, 列表纟丮锁定丶动态厈)
    def 串联灬扌(sf, /, *列表纟解码器名):
        '-> 乸串联解码器|解码器乊唯一'
        return sf.串联扌(列表纟解码器名)
    def 串联扌(sf, 列表纟解码器名, /):
        '-> 乸串联解码器|解码器乊唯一'
        if len(列表纟解码器名) == 1:
            [解码器名] = 列表纟解码器名
            return sf.构造冫解码器巛名扌(解码器名)
        return 乸串联解码器(sf, 列表纟解码器名)
    def 串联时忽略结果扌(sf, 解码器名, /):
        '-> 乸收集时忽略结果解码器'
        return 乸收集时忽略结果解码器(sf, 解码器名)
    def 序列解码器扌(sf, 最小数目, 鬽最大数目, 解码器名, /):
        '-> 乸序列解码器'
        return 乸序列解码器(sf, 最小数目, 鬽最大数目, 解码器名)
    def 码元集合匹配解码器扌(sf, 码元集, /):
        '-> 乸码元集合匹配解码器'
        return 乸码元集合匹配解码器(sf, 码元集)
    def 码元串常量匹配解码器扌(sf, 码元串, /):
        '-> 乸码元串常量匹配解码器'
        return 乸码元串常量匹配解码器(sf, 码元串)
    def 码元串定长读取解码器扌(sf, 鬽长度, /):
        '-> 乸码元串定长读取解码器'
        return 乸码元串定长读取解码器(sf, 鬽长度)
    def 失败零解码器扌(sf, 错误, /):
        '-> 乸失败零解码器'
        return 乸失败零解码器(sf, 错误)
    def 恒果零解码器扌(sf, 结果, /):
        '-> 乸恒果零解码器'
        return 乸恒果零解码器(sf, 结果)
    def 直达终点解码器扌(sf, 解码器名, /):
        '-> 乸直达终点解码器'
        return 乸直达终点解码器(sf, 解码器名)
    def 前瞻零解码器扌(sf, 解码器名, /):
        '-> 乸前瞻零解码器'
        return 乸前瞻零解码器(sf, 解码器名)
    def 逆转成败解码器扌(sf, 解码器名, /):
        '-> 乸逆转成败解码器'
        return 乸逆转成败解码器(sf, 解码器名)
    #def 欤是冫讫错果变换器扌(sf, x, /):
    #    'x?讫错果变换器 -> [x :: 魖讫错果变换器]'
    #    return isinstance(x, 魖讫错果变换器)
    def 变换讫错果解码器扌(sf, 鬽变换讫错果扌丨讫错果变换器, 解码器名, /):
        '-> 乸变换讫错果解码器'
        return 乸变换讫错果解码器(sf, 鬽变换讫错果扌丨讫错果变换器, 解码器名)

    #def 变换结果解码器扌(sf, 变换错误扌, 变换结果扌, 解码器名, /):
    def 变换结果解码器扌(sf, 鬽变换错误扌, 鬽变换结果扌丨变换讫错果扌丨两段式篡改器, 解码器名, /):
        '-> 乸变换结果解码器'
        #return 乸变换结果解码器(sf, 变换错误扌, 变换结果扌, 解码器名)
        return 乸变换结果解码器(sf, 鬽变换错误扌, 鬽变换结果扌丨变换讫错果扌丨两段式篡改器, 解码器名)
    #def 惑构造冫变换结果解码器扌(sf, 鬽变换错误扌, 变换结果扌丨变换讫错果扌丨讫错果变换器, 解码器名, /):
    #    '-> 乸变换结果解码器|乸变换讫错果解码器'
    #    return 惑构造冫变换结果解码器扌(sf, 鬽变换错误扌, 变换结果扌丨变换讫错果扌丨讫错果变换器, 解码器名)
    def 结尾限长序列解码器扌(sf, 鬽错误乊无锁定, 欤去除结果冃结尾, 解码器名冃结尾, 解码器名冃元素, /):
        '-> 乸结尾限长序列解码器'
        return 乸结尾限长序列解码器(sf, 鬽错误乊无锁定, 欤去除结果冃结尾, 解码器名冃结尾, 解码器名冃元素)

    def 间隙锁定串联扌(sf, 鬽索引号纟间隙, 列表纟解码器名, /):
        '-> 乸间隙锁定串联解码器~~~锁定式'
        return 乸间隙锁定串联解码器(sf, 鬽索引号纟间隙, 列表纟解码器名)
    def 元素锁定串联扌(sf, 鬽索引号纟间隙, 列表纟解码器名, /):
        '-> 乸元素锁定串联解码器===细胞锁定式'
        return 乸元素锁定串联解码器(sf, 鬽索引号纟间隙, 列表纟解码器名)
    def 首非零锁定串联扌(sf, 列表纟解码器名, /):
        '-> 乸首非零锁定串联解码器=[def]=串联式/乸串联解码器'
        return 乸首非零锁定串联解码器(sf, 列表纟解码器名)
    def 首锁定串联扌(sf, 列表纟解码器名, /):
        '-> 乸首锁定串联解码器===乸元素锁定串联解码器@0'
        return 乸首锁定串联解码器(sf, 列表纟解码器名)
    def 尾锁定串联扌(sf, 列表纟解码器名, /):
        '-> 乸尾锁定串联解码器===乸元素锁定串联解码器@-1'
        return 乸尾锁定串联解码器(sf, 列表纟解码器名)
    def 实心锁定串联扌(sf, 列表纟解码器名, /):
        '-> 乸实心锁定串联解码器===乸元素锁定串联解码器@None===乸间隙锁定串联解码器@None'
        return 乸实心锁定串联解码器(sf, 列表纟解码器名)
    def 零解码器扌(sf, 鬽名=None, /):
        if 鬽名 is None:
            return 乸零解码器(sf)
        名 = 鬽名
        return 乸具名零解码器(sf, 名)
    def 具名扌(sf, 鬽名, 解码器名, /):
        return 具名扌(sf, 鬽名, 解码器名)
    def 罓具名扌(sf, 鬽名, 解码器名, /):
        return 乸具名解码器(sf, 鬽名, 解码器名)
    def 引用扌(sf, 解码器名, /):
        return 乸引用解码器(sf, 解码器名)
    def 包装灬扌(sf, 乊起始扌, 乊锁定扌, 乊失败扌, 乊匹配扌, 乊结束扌, 解码器名, /, *, 鬽名):
        两段式篡改器 = 乸两段式篡改器(鬽名, 乊起始扌, 乊锁定扌, 乊失败扌, 乊匹配扌, 乊结束扌)
        return sf.包装扌(两段式篡改器, 解码器名)
    def 包装扌(sf, 两段式篡改器, 解码器名, /):
        r'''
见:乸包装解码器,乸两段式篡改器
提供完整信息:
乊锁定扌,乊失败扌,乊匹配扌,乊结束扌 :: 包装解码器 -> 全文暨起讫讫 -> 讫错果 -> 讫错果
包装解码器:
    .场景
    .解码器名
    .两段式篡改器
        .乊锁定扌
        .乊失败扌
        .乊匹配扌
        .乊结束扌

    '''#'''
        return 乸包装解码器(sf, 两段式篡改器, 解码器名)
#end-class 魖解码场景(ABC):
注册冫变换结果函数纟具名解码器扌=魖解码场景.注册冫变换结果函数纟具名解码器扌
取冫变换结果函数纟具名解码器扌=魖解码场景.取冫变换结果函数纟具名解码器扌

__all__
def 构造冫解码场景乊缺省扌(鬽乸解码场景, 鬽名丨解码场景, /):
    解码场景 = 构造冫具名对象乊缺省扌(lambda 鬽名:构造冫解码场景扌(鬽乸解码场景,鬽名=鬽名), 鬽名丨解码场景)
    return 解码场景
def 构造冫解码场景扌(cls=None, /, *, 鬽名=None, 用户数据纟场景固化=None, 鬽构造冫解码器纟并联扌=None, 鬽名丨注册处纟解码器=None, 鬽名丨注册处纟变量=None, 鬽乸具名注册处=None):
    #乸解码场景,乸具名注册处
    注册处纟解码器 = 构造冫具名注册处乊缺省扌(None, 鬽名丨注册处纟解码器)
    注册处纟变量 = 构造冫具名注册处乊缺省扌(None, 鬽名丨注册处纟变量)
    cls = ifNone(cls, 乸解码场景)
    return cls(鬽名, 用户数据纟场景固化, 鬽构造冫解码器纟并联扌, 注册处纟解码器, 注册处纟变量)
class 乸解码场景(_4repr_named, 魖解码场景):
    '乸解码场景(鬽名, 用户数据纟场景固化, 鬽构造冫解码器纟并联扌, 注册处纟解码器, 注册处纟变量)'
    ___no_slots_ok___ = True
    def __init__(sf, 鬽名, 用户数据纟场景固化, 鬽构造冫解码器纟并联扌, 注册处纟解码器, 注册处纟变量, /):
        '为何 __init__ 不能用『鬽名丨注册处纟...』而改用『构造冫解码场景扌』？<<==因为 _4repr_named.__new__保存._args'
        sf._鬽名 = 鬽名
        sf._用户数据纟场景固化 = 用户数据纟场景固化
        #
        sf._鬽构造冫解码器纟并联扌 = 鬽构造冫解码器纟并联扌
        sf._注册处纟解码器 = 注册处纟解码器
        sf._注册处纟变量 = 注册处纟变量
        ######################
        check_may_(check_callable, 鬽构造冫解码器纟并联扌)
        check_type_le(魖注册处, 注册处纟解码器)
        check_type_le(魖注册处, 注册处纟变量)

    #@override
    #def 罓构造冫解码器巛名扌(sf, 解码器名, /):
    #    '-> 魖解码器 | ^LookupError'
    #    #兜底|fallback
    #    return sf._解码器名讠解码器[解码器名]
    #        #^LookupError

    @override
    def 罓构造冫解码器纟并联扌(sf, 并联解码器, 索引号冃分支, 结果冃锁定, 部分构造参数冃后续, /):
        '-> 魖解码器'
        #已知:并联解码器.场景 一致，可省略
        m = sf._鬽构造冫解码器纟并联扌
        if m is None:
            raise NotImplementedError
        f = m
        return f(并联解码器, 索引号冃分支, 结果冃锁定, 部分构造参数冃后续)



    @property
    @override
    def 罓注册处纟解码器(sf, /):
        '-> 注册处纟解码器/{解码器名:解码器}'
        return sf._注册处纟解码器
    @property
    @override
    def 罓注册处纟变量(sf, /):
        '-> 注册处纟变量/WeakValueDictionary{解码器名纟私用/AddrAsHash:私用解释器/私用空间}'
        return sf._注册处纟变量

    @property
    @override
    def 匞参数配置包(sf, /):
        '-> 用户数据纟场景固化'
        return sf._用户数据纟场景固化
    用户数据纟场景固化 = 匞参数配置包


    r'''[[[
    @property
    @override
    def 用户数据纟场景固化(sf, /):
        '-> 用户数据纟场景固化'
        return sf._用户数据纟场景固化

    @override
    def 罓构造冫新解码场景扌(sf, 注册处纟解码器, 注册处纟变量, /):
        return type(sf)(鬽名:=None, sf.用户数据纟场景固化, sf._鬽构造冫解码器纟并联扌, 注册处纟解码器, 注册处纟变量)
    def 更新冫用户数据纟场景固化(sf, 用户数据纟场景固化, /, *, 鬽名=None):
        '-> 场景/魖解码场景'
        if 用户数据纟场景固化 is sf.用户数据纟场景固化:
            return sf
        return type(sf)(鬽名, 用户数据纟场景固化, sf._鬽构造冫解码器纟并联扌, sf._注册处纟解码器, sf._注册处纟变量)
        构造冫解码场景扌
    #]]]'''#'''



___begin_mark_of_excluded_global_names__9___ = ...
from seed.recognize.toy.simple_recognizer_.decoder import \
(筐简化锁定况型
,魖解码器
,魖解码器冫侧重两段式
,魖解码器冫侧重单段式冫实心锁定
,乸优先并联解码器
,乸互斥并联解码器
,乸码元集合匹配解码器
,乸码元串常量匹配解码器
,乸间隙锁定串联解码器
,乸元素锁定串联解码器
,乸串联解码器
,乸首非零锁定串联解码器
,乸首锁定串联解码器
,乸尾锁定串联解码器
,乸实心锁定串联解码器
,乸序列解码器
,乸失败零解码器
,乸恒果零解码器
,乸零解码器
,乸具名零解码器
,乸具名解码器
,乸引用解码器
,乸收集时忽略结果解码器
,乸前瞻零解码器
,乸逆转成败解码器
,乸变换讫错果解码器
,乸变换结果解码器
,乸结尾限长序列解码器
,乸直达终点解码器
,乸码元串定长读取解码器
,乸定域解码器
#乸变换讫错果解码器:
    #,魖讫错果变换器
    #,乸讫错果变换器
    #,惑构造冫讫错果变换器扌
#乸变换讫错果解码器:
    #,魖错果变换器
    #,乸错果变换器
    #,乸结果变换器
    #,惑构造冫结果变换器扌
,乸包装解码器
    ,乸两段式篡改器
)
___end_mark_of_excluded_global_names__9___ = ...

from seed.recognize.toy.simple_recognizer_.scene import 具名扌,注册冫变换结果函数纟具名解码器扌,取冫变换结果函数纟具名解码器扌

from seed.recognize.toy.simple_recognizer_.scene import 魖解码场景, 乸解码场景, 构造冫解码场景扌
from seed.recognize.toy.simple_recognizer_.scene import 乸私用空间,乸具名私用空间,乸私钥,乸具名私钥
from seed.recognize.toy.simple_recognizer_.scene import 构造冫解码器巛名扌,注册冫解码器名纟公用扌,注册冫解码器名纟私用扌

from seed.recognize.toy.simple_recognizer_.scene import 取冫变量值扌,注册冫变量名纟公用扌,注册冫变量名纟私用扌

from seed.recognize.toy.simple_recognizer_.scene import 魖注册处,乸具名注册处,乸具名注册处暨用户数据
from seed.recognize.toy.simple_recognizer_.scene import 构造冫具名注册处扌

from seed.recognize.toy.simple_recognizer_.scene import 构造冫具名对象乊缺省扌,构造冫具名注册处乊缺省扌,构造冫解码场景乊缺省扌


from seed.recognize.toy.simple_recognizer_.scene import *
