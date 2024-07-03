#__all__:goto
# [:综述冫各版本具象类纟展翅树]:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_trees.py
view ../../python3_src/seed/data_funcs/finger_tree__ABC.py
view ../../python3_src/seed/data_funcs/finger_tree__simple.py


seed.data_funcs.finger_trees
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_trees -x
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_trees:__doc__ -ht
py_adhoc_call   seed.data_funcs.finger_trees   @f
from seed.data_funcs.finger_trees import *
#]]]'''
__all__ = r'''
错误牜展翅树相关
    错误牜欤已知非超前进
    错误牜空树

Error4FingerTree
    Error__empty_tree
    Error__known_non_overflow

魖展翅树牜基本
    魖展翅树牜带总长
    魖展翅树
ISimpleFingerTree

SimpleFingerTree
    展翅树牜带总长
        匞展翅树爫元组爫最小极简


构造冫匞展翅树爫元组具现扌
    匞度量值爫自然数加法半群
    匞度量值爫无度量值
    匞展翅树牜一二三四四爫自然数加法半群
    匞展翅树牜一二三四四爫无度量值

魖元素容器爫展翅树
    魖元素容器爫展翅树牜带总长
    魖元素容器爫展翅树牜通用具现
    魖元素容器爫展翅树牜元组具现

IWithMeasurement
    IFingerTree
        IFingerTree__wrapper
            IFingerTree__wrapper__measurement_contains_len





IFingerTree__wrapper
    魖元素容器爫展翅树
        魖元素容器爫展翅树牜带总长
IFingerTree__wrapper__measurement_contains_len
    魖元素容器爫展翅树牜度量值含长度
FingerTree__measurement_is_len
    乸元素容器爫展翅树牜度量值为长度

'''.split()#'''
__all__



if 1:
    ######################
    ######################
    ######################
    from seed.data_funcs.finger_tree__errors import 错误牜展翅树相关,错误牜欤已知非超前进,错误牜空树
    from seed.data_funcs.finger_tree__errors import Error4FingerTree, Error__empty_tree, Error__known_non_overflow


    ######################
    ######################
    ######################
    #极简版:
    from seed.data_funcs.finger_tree__simple import 魖展翅树牜基本, 魖展翅树牜带总长
        # 极简版展翅树接口:中文版
        # 极简===无合并操作，无搜索操作, 无分裂操作
    from seed.data_funcs.finger_tree__simple import 魖展翅树
        # 极简+匞展翅树
    from seed.data_funcs.finger_tree__simple import ISimpleFingerTree
        # 极简版展翅树接口:英文版

    from seed.data_funcs.finger_tree__simple import 匞展翅树爫元组爫最小极简, 展翅树牜带总长
        # 极简+自计总长
        #   ++惰性散列
    from seed.data_funcs.finger_tree__simple import SimpleFingerTree
        # 包装:展翅树牜带总长:英文版



    ######################
    ######################
    ######################
    #度量版节点版
    from seed.data_funcs.finger_tree__ABC import 构造冫匞展翅树爫元组具现扌,匞度量值爫自然数加法半群,匞度量值爫无度量值
    from seed.data_funcs.finger_tree__ABC import 匞展翅树牜一二三四四爫自然数加法半群,匞展翅树牜一二三四四爫无度量值
        # 面向:节点{深度;}

    ######################
    ######################
    ######################
    #度量版元素版中文版
    from seed.data_funcs.finger_tree__ABC import 魖元素容器爫展翅树,魖元素容器爫展翅树牜带总长,魖元素容器爫展翅树牜度量值含长度,魖元素容器爫展翅树牜通用具现, 魖元素容器爫展翅树牜元组具现
        # 面向:元素
    from seed.data_funcs.finger_tree__ABC import 乸元素容器爫展翅树牜度量值为长度
        # 自带总长
        #   固化==>>不缓存散列



    ######################
    ######################
    ######################
    #度量版元素版英文版
    from seed.data_funcs.finger_tree__ABC import IWithMeasurement
    from seed.data_funcs.finger_tree__ABC import IFingerTree
    from seed.data_funcs.finger_tree__ABC import IFingerTree__wrapper
        # 包装:魖元素容器爫展翅树,魖元素容器爫展翅树牜带总长
        # 通用:自带散列
        # 通用:自计总长
        #   不一定能使用分裂操作
        # 分裂操作:要求:底层==魖元素容器爫展翅树牜带总长
    from seed.data_funcs.finger_tree__ABC import IFingerTree__wrapper__measurement_contains_len
        # 包装:魖元素容器爫展翅树牜度量值含长度
        # 通用:自带散列
        # 通用:自带总长<<==底层
        # 支持:分裂操作,__getitem__
    from seed.data_funcs.finger_tree__ABC import FingerTree__measurement_is_len
        # 包装:乸元素容器爫展翅树牜度量值为长度
        #   ++惰性散列


























__all__
################################
################################
################################
################################
################################
################################
################################
# [:综述冫各版本具象类纟展翅树]:here
展翅树牜带总长
    # 自带总长
    # 缓存散列==>>惰性散列
    # 极简:无合并，无搜索，无分裂
SimpleFingerTree
    # 包装==>>依赖底层:自带总长
    # 包装==>>依赖底层:缓存散列==>>惰性散列
    # 极简:无合并，无搜索，无分裂
乸元素容器爫展翅树牜度量值为长度
    # 自带总长
    # 固化==>>不缓存散列
    # 支持:合并，搜索，分裂{依长度}/取子串
    # 元组具现==>>不能篡改(或者说:麻烦):__getitem__
    # 元组具现==>>有一些无用的函数，易误用==>>使用包装器:FingerTree__measurement_is_len
    #
FingerTree__measurement_is_len
    # 包装==>>依赖底层:自带总长
    # 缓存散列==>>惰性散列
    # 包装==>>依赖底层:支持:合并，搜索，分裂{依长度}/取子串
    # 支持:__getitem__
    #


################################
#py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.finger_tree__simple:展翅树牜带总长@T    =T
#all_methods:
__ = 展翅树牜带总长
__.__eq__
__.__hash__
__.__init__
__.__iter__
__.__len__
__.__repr__
__.__reversed__
__.__str__
__.args
__.压入扌
__.取冫端点扌
__.同端弹压扌
__.展翅树牜无总长
__.异端压弹扌
__.异端压弹牜序列扌
__.弹出扌
__.总长
__.枚举冫节点扌
__.欤光杆
__.欤空树
################################
#py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.finger_tree__ABC:乸元素容器爫展翅树牜度量值为长度@T    =T
#all_methods:
__ = 乸元素容器爫展翅树牜度量值为长度
__.度量值讠长度
__.__add__
__.__bool__
__.__iter__
__.__len__
__.__new__
__.__repr__
__.__reversed__
__.__str__
__.分裂乊元素扌
__.分裂乊元素间隙扌
__.包装冫元素扌
__.包装冫展翅树乊底层扌
__.匞展翅树
__.压入冫元素序列扌
__.压入冫元素序列牜计长度扌
__.压入冫元素扌
__.取冫元素丶度量值巛路径扌
__.取冫元素巛路径扌
__.取冫端点元素扌
__.右端元素
__.合并扌
__.合并灬扌
__.同端弹压冫元素扌
__.展翅树乊底层
__.左端元素
__.度量值
__.度量值巛元素扌
__.异端压弹冫元素序列扌
__.异端压弹冫元素扌
__.弹出冫元素列表扌
__.弹出冫元素扌
__.总长
__.搜索定位冫元素扌
__.枚举冫元素丶度量值扌
__.枚举冫元素扌
__.枚举冫路径丶元素丶度量值扌
__.类忄合并牜序列扌
__.类忄构造冫展翅树丶总长扌
__.类忄构造冫空树扌
__.罒类忄包装冫展翅树乊底层扌
__.罒类忄取冫匞展翅树扌
__.罒类忄度量值巛元素扌
tuple.__ne__
tuple.__eq__
tuple.__hash__
tuple.__ge__
tuple.__le__
tuple.__lt__
tuple.__mul__
tuple.__rmul__
tuple.__contains__
tuple.__getitem__
tuple.count
tuple.index
################################
#py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.finger_tree__simple:SimpleFingerTree@T    =T
#all_methods:
__ = SimpleFingerTree
__.__eq__
__.__hash__
__.__init__
__.__iter__
__.__len__
__.__repr__
__.__reversed__
__.get_endpoint_
__.ipop_
__.ipop_then_ipush_on_same_endpoint_
__.ipush_
__.ipush_then_ipop_on_diff_endpoints_
__.ipushs_then_ipops_on_diff_endpoints_
__.iter_
################################
#py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.finger_tree__ABC:FingerTree__measurement_is_len@T    =T
#all_methods:
__ = FingerTree__measurement_is_len
__.__add__
__.__bool__
__.__eq__
__.__getitem__
__.__hash__
__.__iadd__
__.__init__
__.__iter__
__.__len__
__.__new__
__.__repr__
__.__reversed__
__.__str__
__.first
__.get_endpoint_
__.ipop_
__.ipop_then_ipush_on_same_endpoint_
__.ipops_le__
__.ipush_
__.ipush_then_ipop_on_diff_endpoints_
__.ipushs__
__.ipushs_then_ipops_on_diff_endpoints_
__.iter_
__.iter_path_value_measurement_triples_
__.iter_value_measurement_pairs_
__.join
__.joins
__.last
__.measurement
__.mk_empty_tree
__.path2reverse
__.path2value
__.path2value_measurement_pair
__.search_via_measurement___
__.slice_between
__.split4gap
__.split4value
__.split_at4gap
__.split_at4value
__.underlying_tree
__.__contains__
__.count
__.index
__.rindex
__.index_
__.__mul__
__.__rmul__
__.split_between

if 1:
    __._add_
    __._base_type4underlying_tree_
    __.accumulate4len
    __.measurement2len



################################
################################
################################
from seed.data_funcs.finger_trees import 错误牜展翅树相关,错误牜欤已知非超前进,错误牜空树
from seed.data_funcs.finger_trees import Error4FingerTree, Error__empty_tree, Error__known_non_overflow


######################
######################
######################
#极简版:
from seed.data_funcs.finger_trees import 魖展翅树牜基本, 魖展翅树牜带总长
    # 极简版展翅树接口:中文版
    # 极简===无合并操作，无搜索操作, 无分裂操作
from seed.data_funcs.finger_trees import 魖展翅树
    # 极简+匞展翅树
from seed.data_funcs.finger_trees import ISimpleFingerTree
    # 极简版展翅树接口:英文版

from seed.data_funcs.finger_trees import 匞展翅树爫元组爫最小极简, 展翅树牜带总长
    # 极简+自计总长
    #   ++惰性散列
from seed.data_funcs.finger_trees import SimpleFingerTree
    # 包装:展翅树牜带总长:英文版



######################
######################
######################
#度量版节点版
from seed.data_funcs.finger_trees import 构造冫匞展翅树爫元组具现扌,匞度量值爫自然数加法半群,匞度量值爫无度量值
from seed.data_funcs.finger_trees import 匞展翅树牜一二三四四爫自然数加法半群,匞展翅树牜一二三四四爫无度量值
    # 面向:节点{深度;}

######################
######################
######################
#度量版元素版中文版
from seed.data_funcs.finger_trees import 魖元素容器爫展翅树,魖元素容器爫展翅树牜带总长,魖元素容器爫展翅树牜度量值含长度,魖元素容器爫展翅树牜通用具现, 魖元素容器爫展翅树牜元组具现
    # 面向:元素
from seed.data_funcs.finger_trees import 乸元素容器爫展翅树牜度量值为长度
    # 自带总长
    #   固化==>>不缓存散列



######################
######################
######################
#度量版元素版英文版
from seed.data_funcs.finger_trees import IWithMeasurement
from seed.data_funcs.finger_trees import IFingerTree
from seed.data_funcs.finger_trees import IFingerTree__wrapper
    # 包装:魖元素容器爫展翅树,魖元素容器爫展翅树牜带总长
    # 通用:自带散列
    # 通用:自计总长
    #   不一定能使用分裂操作
    # 分裂操作:要求:底层==魖元素容器爫展翅树牜带总长
from seed.data_funcs.finger_trees import IFingerTree__wrapper__measurement_contains_len
    # 包装:魖元素容器爫展翅树牜度量值含长度
    # 通用:自带散列
    # 通用:自带总长<<==底层
    # 支持:分裂操作,__getitem__
from seed.data_funcs.finger_trees import FingerTree__measurement_is_len
    # 包装:乸元素容器爫展翅树牜度量值为长度
    #   ++惰性散列





__all__
from seed.data_funcs.finger_trees import *
