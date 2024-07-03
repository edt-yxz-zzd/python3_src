#__all__:goto
# [:接口冫展翅树]:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree__simple.py

[[
展翅树牜极简:ISimpleFingerTree:
    只考虑:单元素:压入/弹出
        => 节点数纟更深节点:固化
        => [元素封包节点===元素]
    [:约束牜简化编程牜弹出乊临界缺员乊空心]:goto
]]


seed.data_funcs.finger_tree__simple
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree__simple -x
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree__simple:__doc__ -ht



######################
######################
######################
匞展翅树爫元组爫最小极简
######################
>>> 匞展翅树爫元组爫最小极简
乸匞展翅树爫元组爫最小极简()
>>> 匞 = 匞展翅树爫元组爫最小极简
>>> ee = 匞.构造冫空树扌()
>>> o = 匞.构造冫展翅树扌(range(1), 左起丷右起=False)
>>> oi = 匞.构造冫展翅树扌(range(2), 左起丷右起=False)
>>> oz = 匞.构造冫展翅树扌(range(3), 左起丷右起=False)
>>> o3 = 匞.构造冫展翅树扌(range(4), 左起丷右起=False)
>>> o4 = 匞.构造冫展翅树扌(range(5), 左起丷右起=False)
>>> o5 = 匞.构造冫展翅树扌(range(6), 左起丷右起=False)
>>> ee
{<乸光杆树爫元组爫最小极简()>}
>>> o
{<乸光杆树爫元组爫最小极简(0)>}
>>> oi
{<乸光杆树爫元组爫最小极简(0, 1)>}
>>> oz
{<乸光杆树爫元组爫最小极简(0, 1, 2)>}
>>> o3
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2, 3)>})>}
>>> o4
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2, 3, 4)>})>}
>>> o5
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>})>}, {<乸右翼爫元组爫最小极简(4, 5)>})>}


>>> og = 匞.构造冫展翅树扌(range(9), 左起丷右起=False)
>>> tuple(og.枚举冫节点扌(左起丷右起=False))
(0, 1, 2, 3, 4, 5, 6, 7, 8)
>>> og
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7, 8)>})>}
>>> go = 匞.构造冫展翅树扌(range(9), 左起丷右起=True)
>>> tuple(go.枚举冫节点扌(左起丷右起=False))
(8, 7, 6, 5, 4, 3, 2, 1, 0)
>>> go
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(8, 7, 6)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(5, 4)>}, {<乸更深节点爫元组爫最小极简(3, 2)>})>}, {<乸右翼爫元组爫最小极简(1, 0)>})>}

# [:接口冫展翅树]:here
>>> dir(魖匞展翅树) #doctest: +ELLIPSIS
[..., '匞光杆树', '匞更深节点', '匞根深树', '匞翅膀', '参数配置纟极简展翅树', '构造冫展翅树扌', '构造冫展翅树牜计总长扌', '构造冫空树扌']
>>> dir(魖展翅树) #doctest: +ELLIPSIS
[..., '匞展翅树', '压入扌', '取冫端点扌', '同端弹压扌', '异端压弹扌', '异端压弹牜序列扌', '弹出扌', '枚举冫节点扌', '欤光杆', '欤空树']

>>> ee.欤空树
True
>>> o.欤空树
False
>>> oi.欤空树
False
>>> oz.欤空树
False
>>> o3.欤空树
False
>>> o4.欤空树
False
>>> o5.欤空树
False
>>> og.欤空树
False


>>> ee.欤光杆
True
>>> o.欤光杆
True
>>> oi.欤光杆
True
>>> oz.欤光杆
True
>>> o3.欤光杆
False
>>> o4.欤光杆
False
>>> o5.欤光杆
False
>>> og.欤光杆
False

>>> og.取冫端点扌(左端丷右端=False)
0
>>> og.取冫端点扌(左端丷右端=True)
8
>>> o.取冫端点扌(左端丷右端=False)
0
>>> o.取冫端点扌(左端丷右端=True)
0
>>> ee.取冫端点扌(左端丷右端=False)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree__errors.错误牜空树
>>> ee.取冫端点扌(左端丷右端=True)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree__errors.错误牜空树


>>> og.同端弹压扌(999, 左端丷右端=False)
({<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(999, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7, 8)>})>}, 0)
>>> og.同端弹压扌(999, 左端丷右端=True)
({<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7, 999)>})>}, 8)
>>> o.同端弹压扌(999, 左端丷右端=False)
({<乸光杆树爫元组爫最小极简(999)>}, 0)
>>> o.同端弹压扌(999, 左端丷右端=True)
({<乸光杆树爫元组爫最小极简(999)>}, 0)
>>> ee.同端弹压扌(999, 左端丷右端=False)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree__errors.错误牜空树
>>> ee.同端弹压扌(999, 左端丷右端=True)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree__errors.错误牜空树

>>> og.异端压弹扌(999, 左出丷右出=False)
({<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>}, {<乸更深节点爫元组爫最小极简(6, 7)>})>}, {<乸右翼爫元组爫最小极简(8, 999)>})>}, 0)
>>> og.异端压弹扌(999, 左出丷右出=True)
({<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(999, 0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7)>})>}, 8)
>>> oi.异端压弹扌(999, 左出丷右出=False)
({<乸光杆树爫元组爫最小极简(1, 999)>}, 0)
>>> oi.异端压弹扌(999, 左出丷右出=True)
({<乸光杆树爫元组爫最小极简(999, 0)>}, 1)
>>> o.异端压弹扌(999, 左出丷右出=False)
({<乸光杆树爫元组爫最小极简(999)>}, 0)
>>> o.异端压弹扌(999, 左出丷右出=True)
({<乸光杆树爫元组爫最小极简(999)>}, 0)
>>> ee.异端压弹扌(999, 左出丷右出=False)
({<乸光杆树爫元组爫最小极简()>}, 999)
>>> ee.异端压弹扌(999, 左出丷右出=True)
({<乸光杆树爫元组爫最小极简()>}, 999)

>>> og.异端压弹牜序列扌(range(990,995), 左出丷右出=False)
({<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(5)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(6, 7)>}, {<乸更深节点爫元组爫最小极简(8, 990)>}, {<乸更深节点爫元组爫最小极简(991, 992)>})>}, {<乸右翼爫元组爫最小极简(993, 994)>})>}, [0, 1, 2, 3, 4])
>>> og.异端压弹牜序列扌(range(990,995), 左出丷右出=True)
({<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(994, 993, 992)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(991, 990)>}, {<乸更深节点爫元组爫最小极简(0, 1)>})>}, {<乸右翼爫元组爫最小极简(2, 3)>})>}, [8, 7, 6, 5, 4])
>>> oz.异端压弹牜序列扌(range(990,995), 左出丷右出=False)
({<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(992)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(993, 994)>})>}, [0, 1, 2, 990, 991])
>>> oz.异端压弹牜序列扌(range(990,995), 左出丷右出=True)
({<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(994, 993)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(992)>})>}, [2, 1, 0, 990, 991])
>>> o.异端压弹牜序列扌(range(990,995), 左出丷右出=False)
({<乸光杆树爫元组爫最小极简(994)>}, [0, 990, 991, 992, 993])
>>> o.异端压弹牜序列扌(range(990,995), 左出丷右出=True)
({<乸光杆树爫元组爫最小极简(994)>}, [0, 990, 991, 992, 993])
>>> ee.异端压弹牜序列扌(range(990,995), 左出丷右出=False)
({<乸光杆树爫元组爫最小极简()>}, [990, 991, 992, 993, 994])
>>> ee.异端压弹牜序列扌(range(990,995), 左出丷右出=True)
({<乸光杆树爫元组爫最小极简()>}, [990, 991, 992, 993, 994])




>>> ee.弹出扌(左端丷右端=False)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree__errors.错误牜空树
>>> ee.弹出扌(左端丷右端=True)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree__errors.错误牜空树
>>> o.弹出扌(左端丷右端=False)
({<乸光杆树爫元组爫最小极简()>}, 0)
>>> o.弹出扌(左端丷右端=True)
({<乸光杆树爫元组爫最小极简()>}, 0)
>>> oi.弹出扌(左端丷右端=False)
({<乸光杆树爫元组爫最小极简(1)>}, 0)
>>> oi.弹出扌(左端丷右端=True)
({<乸光杆树爫元组爫最小极简(0)>}, 1)

>>> sz4og = len(list(og.枚举冫节点扌(左起丷右起=True)))
>>> x = og
>>> for _ in range(sz4og):
...     (x, i) = x.弹出扌(左端丷右端=False)
...     print(i)
...     print(x)
0
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7, 8)>})>}
1
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(2, 3)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7, 8)>})>}
2
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(3)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7, 8)>})>}
3
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(4, 5)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(6, 7, 8)>})>}
4
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(5)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(6, 7, 8)>})>}
5
{<乸光杆树爫元组爫最小极简(6, 7, 8)>}
6
{<乸光杆树爫元组爫最小极简(7, 8)>}
7
{<乸光杆树爫元组爫最小极简(8)>}
8
{<乸光杆树爫元组爫最小极简()>}


>>> x = og
>>> for _ in range(sz4og):
...     (x, i) = x.弹出扌(左端丷右端=True)
...     print(i)
...     print(x)
8
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7)>})>}
7
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6)>})>}
6
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>})>}, {<乸右翼爫元组爫最小极简(4, 5)>})>}
5
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>})>}, {<乸右翼爫元组爫最小极简(4)>})>}
4
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2, 3)>})>}
3
{<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2)>})>}
2
{<乸光杆树爫元组爫最小极简(0, 1)>}
1
{<乸光杆树爫元组爫最小极简(0)>}
0
{<乸光杆树爫元组爫最小极简()>}



>>> x = og
>>> for _ in range(sz4og):
...     (x, i) = x.弹出扌(左端丷右端=False)
...     print(i)
...     print(list(x.枚举冫节点扌(左起丷右起=False)))
...     print(list(x.枚举冫节点扌(左起丷右起=True)))
0
[1, 2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2, 1]
1
[2, 3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3, 2]
2
[3, 4, 5, 6, 7, 8]
[8, 7, 6, 5, 4, 3]
3
[4, 5, 6, 7, 8]
[8, 7, 6, 5, 4]
4
[5, 6, 7, 8]
[8, 7, 6, 5]
5
[6, 7, 8]
[8, 7, 6]
6
[7, 8]
[8, 7]
7
[8]
[8]
8
[]
[]

>>> x = og
>>> for _ in range(sz4og):
...     (x, i) = x.弹出扌(左端丷右端=True)
...     print(i)
...     print(list(x.枚举冫节点扌(左起丷右起=False)))
...     print(list(x.枚举冫节点扌(左起丷右起=True)))
8
[0, 1, 2, 3, 4, 5, 6, 7]
[7, 6, 5, 4, 3, 2, 1, 0]
7
[0, 1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1, 0]
6
[0, 1, 2, 3, 4, 5]
[5, 4, 3, 2, 1, 0]
5
[0, 1, 2, 3, 4]
[4, 3, 2, 1, 0]
4
[0, 1, 2, 3]
[3, 2, 1, 0]
3
[0, 1, 2]
[2, 1, 0]
2
[0, 1]
[1, 0]
1
[0]
[0]
0
[]
[]


######################
######################
######################
展翅树牜带总长
######################
>>> 展翅树牜带总长()
展翅树牜带总长(0, {<乸光杆树爫元组爫最小极简()>})
>>> for sz in range(9):
...     t = 展翅树牜带总长(range(sz))
...     print(str(t))
...     print(repr(t))
展翅树牜带总长()
展翅树牜带总长(0, {<乸光杆树爫元组爫最小极简()>})
展翅树牜带总长([0])
展翅树牜带总长(1, {<乸光杆树爫元组爫最小极简(0)>})
展翅树牜带总长([0, 1])
展翅树牜带总长(2, {<乸光杆树爫元组爫最小极简(0, 1)>})
展翅树牜带总长([0, 1, 2])
展翅树牜带总长(3, {<乸光杆树爫元组爫最小极简(0, 1, 2)>})
展翅树牜带总长([0, 1, 2, 3])
展翅树牜带总长(4, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2, 3)>})>})
展翅树牜带总长([0, 1, 2, 3, 4])
展翅树牜带总长(5, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2, 3, 4)>})>})
展翅树牜带总长([0, 1, 2, 3, 4, 5])
展翅树牜带总长(6, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>})>}, {<乸右翼爫元组爫最小极简(4, 5)>})>})
展翅树牜带总长([0, 1, 2, 3, 4, 5, 6])
展翅树牜带总长(7, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>})>}, {<乸右翼爫元组爫最小极简(4, 5, 6)>})>})
展翅树牜带总长([0, 1, 2, 3, 4, 5, 6, 7])
展翅树牜带总长(8, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简({<乸更深节点爫元组爫最小极简(2, 3)>}, {<乸更深节点爫元组爫最小极简(4, 5)>})>}, {<乸右翼爫元组爫最小极简(6, 7)>})>})

>>> t = 展翅树牜带总长(range(5))
>>> for _ in range(len(t)):
...     (t, i) = t.弹出扌(左端丷右端=False)
...     print(i)
...     print(str(t))
...     print(repr(t))
0
展翅树牜带总长([1, 2, 3, 4])
展翅树牜带总长(4, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2, 3, 4)>})>})
1
展翅树牜带总长([2, 3, 4])
展翅树牜带总长(3, {<乸光杆树爫元组爫最小极简(2, 3, 4)>})
2
展翅树牜带总长([3, 4])
展翅树牜带总长(2, {<乸光杆树爫元组爫最小极简(3, 4)>})
3
展翅树牜带总长([4])
展翅树牜带总长(1, {<乸光杆树爫元组爫最小极简(4)>})
4
展翅树牜带总长()
展翅树牜带总长(0, {<乸光杆树爫元组爫最小极简()>})


>>> t = 展翅树牜带总长(range(5))
>>> for _ in range(len(t)):
...     (t, i) = t.弹出扌(左端丷右端=True)
...     print(i)
...     print(str(t))
...     print(repr(t))
4
展翅树牜带总长([0, 1, 2, 3])
展翅树牜带总长(4, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2, 3)>})>})
3
展翅树牜带总长([0, 1, 2])
展翅树牜带总长(3, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2)>})>})
2
展翅树牜带总长([0, 1])
展翅树牜带总长(2, {<乸光杆树爫元组爫最小极简(0, 1)>})
1
展翅树牜带总长([0])
展翅树牜带总长(1, {<乸光杆树爫元组爫最小极简(0)>})
0
展翅树牜带总长()
展翅树牜带总长(0, {<乸光杆树爫元组爫最小极简()>})



>>> t = 展翅树牜带总长(range(5))
>>> for _ in range(len(t)):
...     (t, i) = t.弹出扌(左端丷右端=True)
...     print(i)
...     print(t.欤空树)
...     print(t.欤光杆)
...     print(bool(t))
...     print(len(t))
...     print([*iter(t)])
...     print([*reversed(t)])
4
False
False
True
4
[0, 1, 2, 3]
[3, 2, 1, 0]
3
False
False
True
3
[0, 1, 2]
[2, 1, 0]
2
False
True
True
2
[0, 1]
[1, 0]
1
False
True
True
1
[0]
[0]
0
True
True
False
0
[]
[]

>>> t05 = 展翅树牜带总长(range(5))
>>> t50 = 展翅树牜带总长(range(5)[::-1], True)
>>> t05 == t05
True
>>> t05 == t50
True
>>> hash(t05) == hash(t05)
True
>>> hash(t05) == hash(t50)
True
>>> str(t05) == str(t50)
True
>>> repr(t05) == repr(t50)
False
>>> t05
展翅树牜带总长(5, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(2, 3, 4)>})>})
>>> t50
展翅树牜带总长(5, {<乸根深树爫元组爫最小极简({<乸左翼爫元组爫最小极简(0, 1, 2)>}, {<乸光杆树爫元组爫最小极简()>}, {<乸右翼爫元组爫最小极简(3, 4)>})>})



######################
######################
######################
SimpleFingerTree
######################
>>> sorted(set(dir(SimpleFingerTree)) -set(dir(ABC)))
['__dict__', '__iter__', '__len__', '__reversed__', '__weakref__', 'get_endpoint_', 'ipop_', 'ipop_then_ipush_on_same_endpoint_', 'ipush_', 'ipush_then_ipop_on_diff_endpoints_', 'ipushs_then_ipops_on_diff_endpoints_', 'iter_']

    __eq__
    __hash__
    __init__
    __iter__
    __len__
    __repr__
    __reversed__
    get_endpoint_
    ipop_
    ipop_then_ipush_on_same_endpoint_
    ipush_
    ipush_then_ipop_on_diff_endpoints_
    ipushs_then_ipops_on_diff_endpoints_
    iter_

>>> SimpleFingerTree()
SimpleFingerTree()
>>> for sz in range(9):
...     t = SimpleFingerTree(range(sz))
...     print(len(t))
...     print([*iter(t)])
...     print([*reversed(t)])
...     print(repr(t))
0
[]
[]
SimpleFingerTree()
1
[0]
[0]
SimpleFingerTree([0])
2
[0, 1]
[1, 0]
SimpleFingerTree([0, 1])
3
[0, 1, 2]
[2, 1, 0]
SimpleFingerTree([0, 1, 2])
4
[0, 1, 2, 3]
[3, 2, 1, 0]
SimpleFingerTree([0, 1, 2, 3])
5
[0, 1, 2, 3, 4]
[4, 3, 2, 1, 0]
SimpleFingerTree([0, 1, 2, 3, 4])
6
[0, 1, 2, 3, 4, 5]
[5, 4, 3, 2, 1, 0]
SimpleFingerTree([0, 1, 2, 3, 4, 5])
7
[0, 1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1, 0]
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6])
8
[0, 1, 2, 3, 4, 5, 6, 7]
[7, 6, 5, 4, 3, 2, 1, 0]
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6, 7])
>>> for sz in range(9):
...     t = SimpleFingerTree(range(sz), reverse=True)
...     print(len(t))
...     print([*iter(t)])
...     print([*reversed(t)])
...     print(repr(t))
0
[]
[]
SimpleFingerTree()
1
[0]
[0]
SimpleFingerTree([0])
2
[1, 0]
[0, 1]
SimpleFingerTree([1, 0])
3
[2, 1, 0]
[0, 1, 2]
SimpleFingerTree([2, 1, 0])
4
[3, 2, 1, 0]
[0, 1, 2, 3]
SimpleFingerTree([3, 2, 1, 0])
5
[4, 3, 2, 1, 0]
[0, 1, 2, 3, 4]
SimpleFingerTree([4, 3, 2, 1, 0])
6
[5, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 5]
SimpleFingerTree([5, 4, 3, 2, 1, 0])
7
[6, 5, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 5, 6]
SimpleFingerTree([6, 5, 4, 3, 2, 1, 0])
8
[7, 6, 5, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 5, 6, 7]
SimpleFingerTree([7, 6, 5, 4, 3, 2, 1, 0])

>>> def call_(f, /, *args, **kwds):
...     try:
...         return (True, f(*args, **kwds))
...     except Exception as exc:
...         return (False, exc)
>>> for sz in range(9):
...     t = SimpleFingerTree(range(sz))
...     print(t)
...     print(call_(t.get_endpoint_, left_vs_right=False))
...     print(call_(t.get_endpoint_, left_vs_right=True))
...     print(call_(t.ipop_, left_vs_right=False))
...     print(call_(t.ipop_, left_vs_right=True))
...     print(call_(t.ipop_then_ipush_on_same_endpoint_, 999, left_vs_right=False))
...     print(call_(t.ipop_then_ipush_on_same_endpoint_, 999, left_vs_right=True))
SimpleFingerTree()
(False, Error__empty_tree())
(False, Error__empty_tree())
(False, Error__empty_tree())
(False, Error__empty_tree())
(False, Error__empty_tree())
(False, Error__empty_tree())
SimpleFingerTree([0])
(True, 0)
(True, 0)
(True, (SimpleFingerTree(), 0))
(True, (SimpleFingerTree(), 0))
(True, (SimpleFingerTree([999]), 0))
(True, (SimpleFingerTree([999]), 0))
SimpleFingerTree([0, 1])
(True, 0)
(True, 1)
(True, (SimpleFingerTree([1]), 0))
(True, (SimpleFingerTree([0]), 1))
(True, (SimpleFingerTree([999, 1]), 0))
(True, (SimpleFingerTree([0, 999]), 1))
SimpleFingerTree([0, 1, 2])
(True, 0)
(True, 2)
(True, (SimpleFingerTree([1, 2]), 0))
(True, (SimpleFingerTree([0, 1]), 2))
(True, (SimpleFingerTree([999, 1, 2]), 0))
(True, (SimpleFingerTree([0, 1, 999]), 2))
SimpleFingerTree([0, 1, 2, 3])
(True, 0)
(True, 3)
(True, (SimpleFingerTree([1, 2, 3]), 0))
(True, (SimpleFingerTree([0, 1, 2]), 3))
(True, (SimpleFingerTree([999, 1, 2, 3]), 0))
(True, (SimpleFingerTree([0, 1, 2, 999]), 3))
SimpleFingerTree([0, 1, 2, 3, 4])
(True, 0)
(True, 4)
(True, (SimpleFingerTree([1, 2, 3, 4]), 0))
(True, (SimpleFingerTree([0, 1, 2, 3]), 4))
(True, (SimpleFingerTree([999, 1, 2, 3, 4]), 0))
(True, (SimpleFingerTree([0, 1, 2, 3, 999]), 4))
SimpleFingerTree([0, 1, 2, 3, 4, 5])
(True, 0)
(True, 5)
(True, (SimpleFingerTree([1, 2, 3, 4, 5]), 0))
(True, (SimpleFingerTree([0, 1, 2, 3, 4]), 5))
(True, (SimpleFingerTree([999, 1, 2, 3, 4, 5]), 0))
(True, (SimpleFingerTree([0, 1, 2, 3, 4, 999]), 5))
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6])
(True, 0)
(True, 6)
(True, (SimpleFingerTree([1, 2, 3, 4, 5, 6]), 0))
(True, (SimpleFingerTree([0, 1, 2, 3, 4, 5]), 6))
(True, (SimpleFingerTree([999, 1, 2, 3, 4, 5, 6]), 0))
(True, (SimpleFingerTree([0, 1, 2, 3, 4, 5, 999]), 6))
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6, 7])
(True, 0)
(True, 7)
(True, (SimpleFingerTree([1, 2, 3, 4, 5, 6, 7]), 0))
(True, (SimpleFingerTree([0, 1, 2, 3, 4, 5, 6]), 7))
(True, (SimpleFingerTree([999, 1, 2, 3, 4, 5, 6, 7]), 0))
(True, (SimpleFingerTree([0, 1, 2, 3, 4, 5, 6, 999]), 7))


>>> for sz in range(9):
...     t = SimpleFingerTree(range(sz))
...     print(t)
...     print(t.ipush_(999, left_vs_right=False))
...     print(t.ipush_(999, left_vs_right=True))
...     print(t.ipush_then_ipop_on_diff_endpoints_(999, leftward_vs_rightward=False))
...     print(t.ipush_then_ipop_on_diff_endpoints_(999, leftward_vs_rightward=True))
SimpleFingerTree()
SimpleFingerTree([999])
SimpleFingerTree([999])
(SimpleFingerTree(), 999)
(SimpleFingerTree(), 999)
SimpleFingerTree([0])
SimpleFingerTree([999, 0])
SimpleFingerTree([0, 999])
(SimpleFingerTree([999]), 0)
(SimpleFingerTree([999]), 0)
SimpleFingerTree([0, 1])
SimpleFingerTree([999, 0, 1])
SimpleFingerTree([0, 1, 999])
(SimpleFingerTree([1, 999]), 0)
(SimpleFingerTree([999, 0]), 1)
SimpleFingerTree([0, 1, 2])
SimpleFingerTree([999, 0, 1, 2])
SimpleFingerTree([0, 1, 2, 999])
(SimpleFingerTree([1, 2, 999]), 0)
(SimpleFingerTree([999, 0, 1]), 2)
SimpleFingerTree([0, 1, 2, 3])
SimpleFingerTree([999, 0, 1, 2, 3])
SimpleFingerTree([0, 1, 2, 3, 999])
(SimpleFingerTree([1, 2, 3, 999]), 0)
(SimpleFingerTree([999, 0, 1, 2]), 3)
SimpleFingerTree([0, 1, 2, 3, 4])
SimpleFingerTree([999, 0, 1, 2, 3, 4])
SimpleFingerTree([0, 1, 2, 3, 4, 999])
(SimpleFingerTree([1, 2, 3, 4, 999]), 0)
(SimpleFingerTree([999, 0, 1, 2, 3]), 4)
SimpleFingerTree([0, 1, 2, 3, 4, 5])
SimpleFingerTree([999, 0, 1, 2, 3, 4, 5])
SimpleFingerTree([0, 1, 2, 3, 4, 5, 999])
(SimpleFingerTree([1, 2, 3, 4, 5, 999]), 0)
(SimpleFingerTree([999, 0, 1, 2, 3, 4]), 5)
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6])
SimpleFingerTree([999, 0, 1, 2, 3, 4, 5, 6])
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6, 999])
(SimpleFingerTree([1, 2, 3, 4, 5, 6, 999]), 0)
(SimpleFingerTree([999, 0, 1, 2, 3, 4, 5]), 6)
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6, 7])
SimpleFingerTree([999, 0, 1, 2, 3, 4, 5, 6, 7])
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6, 7, 999])
(SimpleFingerTree([1, 2, 3, 4, 5, 6, 7, 999]), 0)
(SimpleFingerTree([999, 0, 1, 2, 3, 4, 5, 6]), 7)




>>> for sz in range(9):
...     t = SimpleFingerTree(range(sz))
...     print(t)
...     print([*t.iter_(reverse=False)])
...     print([*t.iter_(reverse=True)])
...     tt = SimpleFingerTree(reversed(range(sz)), reverse=True)
...     print(hash(t) == hash(tt))
...     print(t == tt)
SimpleFingerTree()
[]
[]
True
True
SimpleFingerTree([0])
[0]
[0]
True
True
SimpleFingerTree([0, 1])
[0, 1]
[1, 0]
True
True
SimpleFingerTree([0, 1, 2])
[0, 1, 2]
[2, 1, 0]
True
True
SimpleFingerTree([0, 1, 2, 3])
[0, 1, 2, 3]
[3, 2, 1, 0]
True
True
SimpleFingerTree([0, 1, 2, 3, 4])
[0, 1, 2, 3, 4]
[4, 3, 2, 1, 0]
True
True
SimpleFingerTree([0, 1, 2, 3, 4, 5])
[0, 1, 2, 3, 4, 5]
[5, 4, 3, 2, 1, 0]
True
True
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6])
[0, 1, 2, 3, 4, 5, 6]
[6, 5, 4, 3, 2, 1, 0]
True
True
SimpleFingerTree([0, 1, 2, 3, 4, 5, 6, 7])
[0, 1, 2, 3, 4, 5, 6, 7]
[7, 6, 5, 4, 3, 2, 1, 0]
True
True



>>> t = SimpleFingerTree(range(3000))
>>> [*t] == [*range(3000)]
True
>>> (tt, ls) = t.ipushs_then_ipops_on_diff_endpoints_(range(3000, 9000), leftward_vs_rightward=False)

#>>> ls[:20], ls[2990:3010], ls[-20:]
>>> ls == [*range(6000)]
True
>>> [*tt] == [*range(6000, 9000)]
True
>>> (tt, ls) = t.ipushs_then_ipops_on_diff_endpoints_(range(3000, 9000), leftward_vs_rightward=True)
>>> ls == [*range(3000)[::-1], *range(3000, 6000)]
True
>>> [*tt] == [*range(6000, 9000)[::-1]]
True




#]]]'''
__all__ = r'''
SimpleFingerTree
展翅树牜带总长
    匞展翅树爫元组爫最小极简




错误牜展翅树相关
    错误牜空树
魖参数配置纟极简展翅树
    乸最小参数配置纟极简展翅树
        最小参数配置纟极简展翅树

魖匞展翅树
    魖匞根深树
    魖匞光杆树
魖匞更深节点
魖匞翅膀
    魖匞左右翼


魖部件容器
魖节点容器
    魖节点容器爫部件即节点

魖展翅树牜基本
    魖展翅树牜带总长
        展翅树牜带总长
    魖展翅树
        魖根深树
        魖光杆树
魖更深节点
魖翅膀
    魖左右翼
        魖左翼
        魖右翼















魖匞展翅树
    魖匞根深树
    魖匞光杆树
        魖匞根深树爫元组
        魖匞光杆树爫元组
魖匞更深节点
    魖匞更深节点爫元组
魖匞翅膀
    魖匞左右翼
        魖匞左右翼爫元组







魖部件容器
    魖部件容器爫元组
魖节点容器
    魖节点容器爫元组

魖展翅树牜基本
    魖展翅树牜带总长
        展翅树牜带总长
    魖展翅树
        魖根深树
            魖根深树爫元组
        魖光杆树
            魖光杆树爫元组
魖更深节点
    魖更深节点爫元组
魖翅膀
    魖左右翼
        魖左翼
            魖左翼爫元组
        魖右翼
            魖右翼爫元组



乸匞根深树爫元组爫最小极简
    匞根深树爫元组爫最小极简
乸匞光杆树爫元组爫最小极简
    匞光杆树爫元组爫最小极简
乸匞更深节点爫元组爫最小极简
    匞更深节点爫元组爫最小极简
乸匞左右翼爫元组爫最小极简
    匞左右翼爫元组爫最小极简

乸匞展翅树爫元组爫最小极简
    匞展翅树爫元组爫最小极简




魖根深树爫元组
    乸根深树爫元组爫最小极简
魖光杆树爫元组
    乸光杆树爫元组爫最小极简
魖更深节点爫元组
    乸更深节点爫元组爫最小极简
魖左翼爫元组
    乸左翼爫元组爫最小极简
魖右翼爫元组
    乸右翼爫元组爫最小极简





Error4FingerTree
    Error__empty_tree
ISimpleFingerTree
    SimpleFingerTree


'''.split()#'''
__all__
from itertools import islice, chain
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge
#from seed.tiny_.class_property import class_property


from seed.data_funcs.finger_tree__errors import 错误牜展翅树相关,错误牜空树

class 魖参数配置纟极简展翅树(ABC):
    '只考虑:单元素 压入/弹出'
    '参数配置纟极简展翅树'
    __slots__ = ()
    @property
    @abstractmethod
    def 节点数纟更深节点(sf, /):
        '-> uint'
        # !! 只考虑:单元素 压入/弹出
    @property
    @abstractmethod
    def 最大节点数纟光杆树(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def 最大节点数纟翅膀(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def 最小节点数纟翅膀(sf, /):
        '-> uint'

    def __init__(sf, /):
        super().__init__()
        sf.verify()

    def verify(sf, /):
        check_int_ge(1, sf.节点数纟更深节点)
        check_int_ge(1, sf.最大节点数纟光杆树)
        check_int_ge(1, sf.最小节点数纟翅膀)
        check_int_ge(1, sf.最大节点数纟翅膀)
        if not 2*sf.最小节点数纟翅膀 <= sf.最大节点数纟光杆树+1 <= 2*sf.最大节点数纟翅膀: raise ValueError
        if not sf.最小节点数纟翅膀 + sf.节点数纟更深节点 <= sf.最大节点数纟翅膀 + 1: raise ValueError

        if not sf.节点数纟更深节点 >= 2: raise ValueError

        ######################
        ######################
        ######################
        # 防震荡:
        if not 2*sf.最小节点数纟翅膀 +2 <= sf.最大节点数纟光杆树+1 <= 2*sf.最大节点数纟翅膀 -2: raise ValueError
        if not sf.最小节点数纟翅膀 + 2 <= sf.最大节点数纟翅膀: raise ValueError
        if not sf.最小节点数纟翅膀 + sf.节点数纟更深节点 <= sf.最大节点数纟翅膀: raise ValueError


        ######################
        ######################
        ######################
        # 简化编程:
        if not sf.最小节点数纟翅膀 + sf.最大节点数纟翅膀 <= sf.最大节点数纟光杆树+1: raise ValueError
            # [:约束牜简化编程牜弹出乊临界缺员乊空心]:here

class 乸最小参数配置纟极简展翅树(魖参数配置纟极简展翅树):
    __slots__ = ()
    节点数纟更深节点 = 2
    最小节点数纟翅膀 = 1
    最大节点数纟翅膀 = 3
    最大节点数纟光杆树 = 3
最小参数配置纟极简展翅树 = 乸最小参数配置纟极简展翅树()

def _调序扌(*args, 左起丷右起):
    if 左起丷右起:
        args = args[::-1]
    return args
class 魖匞展翅树(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 参数配置纟极简展翅树(sf, /):
        '-> 魖参数配置纟极简展翅树'
    @property
    @abstractmethod
    def 匞根深树(sf, /):
        '-> 魖匞根深树'
    @property
    @abstractmethod
    def 匞光杆树(sf, /):
        '-> 魖匞光杆树'
    @property
    @abstractmethod
    def 匞更深节点(sf, /):
        '-> 魖匞更深节点'
    @property
    @abstractmethod
    def 匞翅膀(sf, /):
        '-> 魖匞翅膀'
    def 构造冫空树扌(sf, /):
        '-> 魖展翅树'
        return sf.匞光杆树.构造冫光杆树扌('', 左起丷右起=False)
    def 构造冫展翅树扌(sf, 节点序列, /, *, 左起丷右起):
        '-> 魖展翅树'
        (树, 总长) = sf.构造冫展翅树牜计总长扌(节点序列, 左起丷右起=左起丷右起)
        return 树
    def 构造冫展翅树牜计总长扌(sf, 节点序列, /, *, 左起丷右起):
        '-> (魖展翅树, 总长)'
        check_type_is(bool, 左起丷右起)
        kwds = dict(左端丷右端=not 左起丷右起)
        树 = sf.构造冫空树扌()
        总长 = 0
        for 总长, 节点 in enumerate(节点序列, 1):
            树 = 树.压入扌(节点, **kwds)
        return (树, 总长)
class 魖匞根深树(ABC):
    __slots__ = ()
    @abstractmethod
    def 构造冫根深树爫左右扌(sf, 左翼, 更深树, 右翼, /):
        '-> 根深树{深度;}/魖根深树'
    def 构造冫根深树爫起讫扌(sf, 起翼, 更深树, 讫翼, /, *, 左起丷右起):
        '-> 根深树{深度;}/魖根深树'
        return sf.构造冫根深树爫左右扌(*_调序扌(起翼, 更深树, 讫翼, 左起丷右起=左起丷右起))
class 魖匞光杆树(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 参数配置纟极简展翅树(sf, /):
        '-> 魖参数配置纟极简展翅树'
    @abstractmethod
    def 构造冫光杆树扌(sf, 节点序列, /, *, 左起丷右起):
        '节点序列{深度;左起丷右起}/Iter 节点 -> 光杆树{深度;}/魖光杆树'
    @property
    def 最大节点数纟光杆树(sf, /):
        '-> uint'
        return sf.参数配置纟极简展翅树.最大节点数纟光杆树




class 魖匞更深节点(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 参数配置纟极简展翅树(sf, /):
        '-> 魖参数配置纟极简展翅树'
    @abstractmethod
    def 构造冫更深节点扌(sf, 节点序列, /, *, 左起丷右起):
        '节点序列{深度;左起丷右起}/Iter 节点 -> 更深节点{深度;}/魖更深节点'
    @property
    def 节点数纟更深节点(sf, /):
        '-> uint'
        return sf.参数配置纟极简展翅树.节点数纟更深节点


class 魖匞翅膀(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 参数配置纟极简展翅树(sf, /):
        '-> 魖参数配置纟极简展翅树'
    @abstractmethod
    def 构造冫翅膀扌(sf, 节点序列, /, *, 左翼丷右翼, 左起丷右起):
        '节点序列{深度;左起丷右起}/Iter 节点 -> 翅膀{深度;左翼丷右翼}/魖翅膀'
    @property
    def 最大节点数纟翅膀(sf, /):
        '-> uint'
        return sf.参数配置纟极简展翅树.最大节点数纟翅膀
    @property
    def 最小节点数纟翅膀(sf, /):
        '-> uint'
        return sf.参数配置纟极简展翅树.最小节点数纟翅膀


class 魖匞左右翼(魖匞翅膀):
    '魖左右翼+魖匞左右翼'
    __slots__ = ()
    @property
    @abstractmethod
    def 乸左翼(sf, /):
        '-> 乸左翼{<:魖右翼}'
    @property
    @abstractmethod
    def 乸右翼(sf, /):
        '-> 乸右翼{<:魖右翼}'











class 魖部件容器(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 部件数(sf, /):
        '-> uint'
    @abstractmethod
    def 枚举冫部件扌(sf, /, *, 左起丷右起):
        '-> 部件序列{深度;左起丷右起}/Iter 部件'
class 魖节点容器(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 节点数(sf, /):
        '-> uint'
    @abstractmethod
    def 枚举冫节点扌(sf, /, *, 左起丷右起):
        '-> 节点序列{深度;左起丷右起}/Iter 节点'

class 魖节点容器爫部件即节点(魖部件容器, 魖节点容器):
    __slots__ = ()
    @property
    @override
    def 节点数(sf, /):
        '-> uint'
        return sf.部件数
    @override
    def 枚举冫节点扌(sf, /, *, 左起丷右起):
        '-> 节点序列{深度;左起丷右起}/Iter 节点'
        return sf.枚举冫部件扌(左起丷右起=左起丷右起)



class 魖展翅树牜基本(ABC):
    '展翅树牜极简: [节点{深度=0} =[def]= 元素]'
    __slots__ = ()
    @property
    @abstractmethod
    def 欤光杆(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def 欤空树(sf, /):
        '-> bool'
    @abstractmethod
    def 枚举冫节点扌(sf, /, *, 左起丷右起):
        '-> 节点序列{深度;左起丷右起}/Iter 节点'
    @abstractmethod
    def 压入扌(sf, 节点, /, *, 左端丷右端):
        '-> 展翅树{深度;}/魖展翅树'
    @abstractmethod
    def 弹出扌(sf, /, *, 左端丷右端):
        '-> (展翅树{深度;}/魖展翅树, 节点{深度;}) | ^错误牜空树'
    #@abstractmethod
    def 取冫端点扌(sf, /, *, 左端丷右端):
        '-> 节点{深度;} | ^错误牜空树'
        for 节点 in sf.枚举冫节点扌(左起丷右起=左端丷右端):
            return 节点
        raise 错误牜空树
    #@abstractmethod
    def 同端弹压扌(sf, 节点, /, *, 左端丷右端):
        '-> (展翅树{深度;}/魖展翅树, 节点{深度;}) | ^错误牜空树'
        (树, 节点纟出) = sf.弹出扌(左端丷右端=左端丷右端)
            # ^错误牜空树
        树 = 树.压入扌(节点, 左端丷右端=左端丷右端)
        return (树, 节点纟出)
    def 异端压弹扌(sf, 节点, /, *, 左出丷右出):
        '-> (展翅树{深度;}/魖展翅树, 节点{深度;})'
        return sf.压入扌(节点, 左端丷右端=not 左出丷右出).弹出扌(左端丷右端=左出丷右出)
    def 异端压弹牜序列扌(sf, 节点序列, /, *, 左出丷右出):
        '-> (展翅树{深度;}/魖展翅树, 节点列表{深度;}/[节点])'
        #保长流动:
        #异端压弹牜序列扌
        #ipushs_then_ipops_on_diff_endpoints_
        ls = []
        for 节点 in 节点序列:
            (sf, 节点) = sf.异端压弹扌(节点, 左出丷右出=左出丷右出)
            ls.append(节点)
        return (sf, ls)

class 魖展翅树牜带总长(魖展翅树牜基本):
    __slots__ = ()
    @property
    @abstractmethod
    def 总长(sf, /):
        '-> 总长/总节点数/uint'
    def __len__(sf, /):
        return sf.总长
    def __iter__(sf, /):
        return sf.枚举冫节点扌(左起丷右起=False)
    def __reversed__(sf, /):
        return sf.枚举冫节点扌(左起丷右起=True)
class 展翅树牜带总长(魖展翅树牜带总长):
    ___no_slots_ok___ = True
    def __hash__(sf, /):
        m = sf._mh
        if m is None:
            sf._mh = hash((type(sf), len(sf), tuple(sf)))
            h = hash(sf)
        else:
            h = m
        return h
    def __eq__(sf, ot, /):
        if ot is sf:
            return True
        if not type(ot) is type(sf):
            return False
                # !! __hash__
            return NotImplemented
        if not len(ot) == len(sf):
            return False
        if ot._tr is sf._tr:
            return True
        if not (ot._mh is None or sf._mh is None):
            if not ot._mh == sf._mh:
                return False
        return all(a in [b] for a, b in zip(sf, ot))
    def __str__(sf, /):
        xs = [*sf]
        if not len(xs) == len(sf):raise 000
        if not sf:
            return repr_helper(sf)
        return repr_helper(sf, xs)
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
    @property
    def args(sf, /):
        return (sf._sz, sf._tr)
    def __init__(sf, 节点序列丨总长=(), 鬽展翅树牜无总长丨左起丷右起=None, /):
        if 鬽展翅树牜无总长丨左起丷右起 is None or type(鬽展翅树牜无总长丨左起丷右起) is bool:
            #__str__ => cls(iterable)
            左起丷右起 = bool(鬽展翅树牜无总长丨左起丷右起)
            节点序列 = 节点序列丨总长
            匞展翅树 = 匞展翅树爫元组爫最小极简
            (展翅树牜无总长, 总长) = 匞展翅树.构造冫展翅树牜计总长扌(节点序列, 左起丷右起=左起丷右起)
        else:
            #__repr__ => cls(sz, underlying_finger_tree)
            展翅树牜无总长 = 鬽展翅树牜无总长丨左起丷右起
            总长 = 节点序列丨总长
        (展翅树牜无总长, 总长)
        check_int_ge(0, 总长)
        if 0:
            check_int_ge(0, 总长)
            check_type_le(魖展翅树牜基本, 展翅树牜无总长)
        sf._sz = 总长
        sf._tr = 展翅树牜无总长
        sf._mh = None
    @property
    def 展翅树牜无总长(sf, /):
        '-> 魖展翅树牜基本'
        return sf._tr
    ######################
    ######################
    @property
    @override
    def 总长(sf, /):
        '-> 总长/总节点数/uint'
        return sf._sz
        return len(sf)
    ######################
    @property
    @override
    def 欤光杆(sf, /):
        '-> bool'
        return sf._tr.欤光杆
    @property
    @override
    def 欤空树(sf, /):
        '-> bool'
        return sf._tr.欤空树
    @override
    def 枚举冫节点扌(sf, /, *, 左起丷右起):
        '-> 节点序列{深度;左起丷右起}/Iter 节点'
        return sf._tr.枚举冫节点扌(左起丷右起=左起丷右起)
    @override
    def 压入扌(sf, 节点, /, *, 左端丷右端):
        '-> 展翅树{深度;}/魖展翅树'
        树牜无总长 = sf._tr.压入扌(节点, 左端丷右端=左端丷右端)
        return type(sf)(sf._sz+1, 树牜无总长)
    @override
    def 弹出扌(sf, /, *, 左端丷右端):
        '-> (展翅树{深度;}/魖展翅树, 节点{深度;}) | ^错误牜空树'
        (树牜无总长, 节点) = sf._tr.弹出扌(左端丷右端=左端丷右端)
        return (type(sf)(sf._sz-1, 树牜无总长), 节点)


class 魖展翅树(魖展翅树牜基本):
    '展翅树牜极简: [节点{深度=0} =[def]= 元素]'
    __slots__ = ()
    @property
    @abstractmethod
    def 匞展翅树(sf, /):
        '-> 匞展翅树/魖匞展翅树'
class 魖根深树(魖展翅树, 魖部件容器):
    __slots__ = ()
    欤光杆 = False
    欤空树 = False
    @property
    @abstractmethod
    def 匞根深树(sf, /):
        '-> 魖匞根深树'
    def 拆包冫根深树爫左右扌(sf, /):
        '-> (左翼, 更深树, 右翼)'
        return sf.拆包冫根深树爫起讫扌(左起丷右起=False)
    def 拆包冫根深树爫起讫扌(sf, /, *, 左起丷右起):
        '-> (起翼, 更深树, 讫翼)'
        return sf.枚举冫部件扌(左起丷右起=左起丷右起)
        return _调序扌(*sf.拆包冫根深树爫左右扌(), 左起丷右起=左起丷右起)
    @override
    def 枚举冫节点扌(sf, /, *, 左起丷右起):
        '-> 节点序列{深度;左起丷右起}/Iter 节点'
        for i, 部件 in enumerate(sf.枚举冫部件扌(左起丷右起=左起丷右起)):
            it = 部件.枚举冫节点扌(左起丷右起=左起丷右起)
            if i == 1:
                更深节点序列 = it
                节点序列 = (节点 for 更深节点 in 更深节点序列 for 节点 in 更深节点.枚举冫节点扌(左起丷右起=左起丷右起))
            else:
                节点序列 = it
            yield from 节点序列
        return
    @override
    def 压入扌(sf, 节点, /, *, 左端丷右端):
        '-> 展翅树{深度;}/魖展翅树'
        (起翼, 更深树, 讫翼) = sf.拆包冫根深树爫起讫扌(左起丷右起=左端丷右端)
        (起翼, 鬽更深节点) = 起翼.外端压入扌(节点)
        if not 鬽更深节点 is None:
            更深节点 = 鬽更深节点
            更深树 = 更深树.压入扌(更深节点, 左端丷右端=左端丷右端)
                #recur...
        return sf.匞根深树.构造冫根深树爫起讫扌(起翼, 更深树, 讫翼, 左起丷右起=左端丷右端)
    @abstractmethod
    def 弹出扌(sf, /, *, 左端丷右端):
        '-> (展翅树{深度;}/魖展翅树, 节点{深度;}) | ^错误牜空树'
        (起翼, 更深树, 讫翼) = sf.拆包冫根深树爫起讫扌(左起丷右起=左端丷右端)
        if not 起翼.欤临界缺员:
            (起翼, 节点) = 起翼.外端弹出乊足员扌()
        elif not 更深树.欤空树:
            (更深树, 更深节点) = 更深树.弹出扌(左端丷右端=左端丷右端)
            (起翼, 节点) = 起翼.外端弹出乊临界缺员扌(更深节点)
        else:
            it = sf.枚举冫节点扌(左起丷右起=左端丷右端)
            节点 = next(it)
            匞展翅树 = sf.匞展翅树
            匞光杆树 = 匞展翅树.匞光杆树
            树 = 匞光杆树.构造冫光杆树扌(it, 左起丷右起=左端丷右端)
                # !! [:约束牜简化编程牜弹出乊临界缺员乊空心]:goto
            return (树, 节点)
        树 = sf.匞根深树.构造冫根深树爫起讫扌(起翼, 更深树, 讫翼, 左起丷右起=左端丷右端)
        return (树, 节点)

class 魖光杆树(魖展翅树, 魖节点容器):
    __slots__ = ()
    欤光杆 = True
    @property
    @abstractmethod
    def 匞光杆树(sf, /):
        '-> 魖匞光杆树'
    @property
    @override
    def 欤空树(sf, /):
        '-> bool'
        return sf.节点数==0
    @property
    def 欤满员(sf, /):
        '-> bool'
        return sf.节点数==sf.匞光杆树.最大节点数纟光杆树
    @override
    def 压入扌(sf, 节点, /, *, 左端丷右端):
        '-> 展翅树{深度;}/魖展翅树'
        it = chain([节点], sf.枚举冫节点扌(左起丷右起=左端丷右端))
        匞光杆树 = sf.匞光杆树
        if not sf.欤满员:
            return 匞光杆树.构造冫光杆树扌(it, 左起丷右起=左端丷右端)
        sz = (sf.节点数+1)
        sz0 = sz//2
        sz1 = sz -sz0
        匞展翅树 = sf.匞展翅树
        匞翅膀 = 匞展翅树.匞翅膀
        匞根深树 = 匞展翅树.匞根深树
        起翼 = 匞翅膀.构造冫翅膀扌(islice(it, sz0), 左翼丷右翼=左端丷右端, 左起丷右起=左端丷右端)
        讫翼 = 匞翅膀.构造冫翅膀扌(islice(it, sz1), 左翼丷右翼=not 左端丷右端, 左起丷右起=左端丷右端)
        空更深树 = 匞展翅树.构造冫空树扌()
        空心树 = 匞根深树.构造冫根深树爫起讫扌(起翼, 空更深树, 讫翼, 左起丷右起=左端丷右端)
        return 空心树

    @override
    def 弹出扌(sf, /, *, 左端丷右端):
        '-> (展翅树{深度;}/魖展翅树, 节点{深度;}) | ^错误牜空树'
        it = sf.枚举冫节点扌(左起丷右起=左端丷右端)
        for 节点 in it:
            break
        else:
            raise 错误牜空树
        树 = sf.匞光杆树.构造冫光杆树扌(it, 左起丷右起=左端丷右端)
        return (树, 节点)
class 魖更深节点(魖节点容器):
    __slots__ = ()
    @property
    @abstractmethod
    def 匞更深节点(sf, /):
        '-> 魖匞更深节点'



class 魖翅膀(魖节点容器):
    __slots__ = ()
    @property
    @abstractmethod
    def 匞翅膀(sf, /):
        '-> 魖匞翅膀'
    @property
    @abstractmethod
    def 匞展翅树(sf, /):
        '-> 匞展翅树/魖匞展翅树'
    @property
    @abstractmethod
    def 左翼丷右翼(sf, /):
        '-> bool'
    @property
    def 欤满员(sf, /):
        '-> bool'
        return sf.节点数==sf.匞翅膀.最大节点数纟翅膀
    @property
    def 欤临界缺员(sf, /):
        '-> bool'
        return sf.节点数==sf.匞翅膀.最小节点数纟翅膀

    #@abstractmethod
    def 外端压入扌(sf, 节点, /):
        '-> (翅膀{深度;左翼丷右翼}/魖翅膀, 鬽更深节点/鬽 魖更深节点)'
        左起丷右起 = 左翼丷右翼 = sf.左翼丷右翼
        it = chain([节点], sf.枚举冫节点扌(左起丷右起=左起丷右起))
        匞翅膀 = sf.匞翅膀
        if not sf.欤满员:
            翅膀 = 匞翅膀.构造冫翅膀扌(it, 左翼丷右翼=左翼丷右翼, 左起丷右起=左起丷右起)
            return (翅膀, None)
        匞展翅树 = sf.匞展翅树
        匞更深节点 = 匞展翅树.匞更深节点
        sz = (sf.节点数+1)
        sz1 = 匞更深节点.节点数纟更深节点
        sz0 = sz -sz1
        翅膀 = 匞翅膀.构造冫翅膀扌(islice(it, sz0), 左翼丷右翼=左翼丷右翼, 左起丷右起=左起丷右起)
        更深节点 = 匞更深节点.构造冫更深节点扌(islice(it, sz1), 左起丷右起=左起丷右起)
        return (翅膀, 更深节点)

    #@abstractmethod
    def 外端弹出乊足员扌(sf, /):
        '-> (翅膀{深度;左翼丷右翼}/魖翅膀, 节点)'
        左起丷右起 = 左翼丷右翼 = sf.左翼丷右翼
        it = sf.枚举冫节点扌(左起丷右起=左起丷右起)
        节点 = next(it)
        翅膀 = sf.匞翅膀.构造冫翅膀扌(it, 左翼丷右翼=左翼丷右翼, 左起丷右起=左起丷右起)
        return (翅膀, 节点)
    #@abstractmethod
    def 外端弹出乊临界缺员扌(sf, 更深节点, /):
        '-> (翅膀{深度;左翼丷右翼}/魖翅膀, 节点)'
        左起丷右起 = 左翼丷右翼 = sf.左翼丷右翼
        it0 = sf.枚举冫节点扌(左起丷右起=左起丷右起)
        节点 = next(it0)
        it1 = 更深节点.枚举冫节点扌(左起丷右起=左起丷右起)
        it = chain(it0, it1)
        翅膀 = sf.匞翅膀.构造冫翅膀扌(it, 左翼丷右翼=左翼丷右翼, 左起丷右起=左起丷右起)
        return (翅膀, 节点)

class 魖左右翼(魖翅膀):
    '魖左右翼+魖匞左右翼'
    '魖左右翼爫元组+魖匞左右翼爫元组'
    __slots__ = ()
    @property
    @abstractmethod
    def 匞左右翼(sf, /):
        '-> 魖匞左右翼'
    @property
    @override
    def 匞翅膀(sf, /):
        '-> 魖匞翅膀'
        return sf.匞左右翼

class 魖左翼(魖左右翼):
    __slots__ = ()
    左翼丷右翼 = False
class 魖右翼(魖左右翼):
    __slots__ = ()
    左翼丷右翼 = True










######################
######################
######################
#具现爫元组:
def _构造冫部件容器爫元组扌(cls, 部件序列, /, *, 左起丷右起):
    '部件序列{深度;左起丷右起}/Iter 部件 -> 部件容器{深度;}/魖部件容器'
    check_type_is(bool, 左起丷右起)
    it = _蛮力反向枚举扌(部件序列) if 左起丷右起 else 部件序列
    部件容器 = tuple.__new__(cls, it)
    return 部件容器
def _蛮力反向枚举扌(it, /):
    try:
        return reversed(it)
    except TypeError:
        pass
    ls = list(it)
    return reversed(ls)

class 魖匞根深树爫元组(魖匞根深树):
    __slots__ = ()
    @property
    @abstractmethod
    def 乸根深树(sf, /):
        '-> 乸根深树{<:魖根深树}'
    @override
    def 构造冫根深树爫左右扌(sf, 左翼, 更深树, 右翼, /):
        '-> 根深树{深度;}/魖根深树'
        T = sf.乸根深树
        根深树 = _构造冫部件容器爫元组扌(T, [左翼, 更深树, 右翼], 左起丷右起=False)
        return 根深树


class 魖匞光杆树爫元组(魖匞光杆树):
    __slots__ = ()
    @property
    @abstractmethod
    def 乸光杆树(sf, /):
        '-> 乸光杆树{<:魖光杆树}'
    @override
    def 构造冫光杆树扌(sf, 节点序列, /, *, 左起丷右起):
        '节点序列{深度;左起丷右起}/Iter 节点 -> 光杆树{深度;}/魖光杆树'
        T = sf.乸光杆树
        光杆树 = _构造冫部件容器爫元组扌(T, 节点序列, 左起丷右起=左起丷右起)
        if not 光杆树.节点数 <= sf.最大节点数纟光杆树: raise TypeError
        return 光杆树

class 魖匞更深节点爫元组(魖匞更深节点):
    __slots__ = ()
    @property
    @abstractmethod
    def 乸更深节点(sf, /):
        '-> 乸更深节点{<:魖更深节点}'
    @override
    def 构造冫更深节点扌(sf, 节点序列, /, *, 左起丷右起):
        '节点序列{深度;左起丷右起}/Iter 节点 -> 更深节点{深度;}/魖更深节点'
        T = sf.乸更深节点
        更深节点 = _构造冫部件容器爫元组扌(T, 节点序列, 左起丷右起=左起丷右起)
        if not 更深节点.节点数 == sf.节点数纟更深节点: raise TypeError
        return 更深节点
class 魖匞左右翼爫元组(魖匞左右翼):
    '魖左右翼爫元组+魖匞左右翼爫元组'
    __slots__ = ()
    @override
    def 构造冫翅膀扌(sf, 节点序列, /, *, 左翼丷右翼, 左起丷右起):
        '节点序列{深度;左起丷右起}/Iter 节点 -> 翅膀{深度;左翼丷右翼}/魖翅膀'
        check_type_is(bool, 左翼丷右翼)
        T = sf.乸右翼 if 左翼丷右翼 else sf.乸左翼
        翅膀 = _构造冫部件容器爫元组扌(T, 节点序列, 左起丷右起=左起丷右起)
        if not sf.最小节点数纟翅膀 <= 翅膀.节点数 <= sf.最大节点数纟翅膀: raise TypeError
        return 翅膀



class 魖部件容器爫元组(tuple, 魖部件容器):
    __slots__ = ()
    __iter__ = None
    __reversed__ = None
    __new__ = None
    __init__ = None
    __len__ = None
    __bool__ = None

    def __repr__(sf, /):
        s = repr_helper(sf, *sf.枚举冫部件扌(左起丷右起=False))
        return f'{{<{s!s}>}}'
    __str__ = __repr__

    @property
    @override
    def 部件数(sf, /):
        '-> uint'
        return tuple.__len__(sf)
    @override
    def 枚举冫部件扌(sf, /, *, 左起丷右起):
        '-> 部件序列{深度;左起丷右起}/Iter 部件'
        check_type_is(bool, 左起丷右起)
        if 0:
            f = tuple.__reversed__ if 左起丷右起 else tuple.__iter__
                #AttributeError: type object 'tuple' has no attribute '__reversed__'
        elif 0:
            f = reversed if 左起丷右起 else tuple.__iter__
                #TypeError: '乸光杆树爫元组爫最小极简' object is not reversible
                #   <<== "__reversed__ = None"
        else:
            f = (lambda sf:map(sf.__getitem__, range(sf.部件数)[::-1])) if 左起丷右起 else tuple.__iter__

        return f(sf)
class 魖节点容器爫元组(魖部件容器爫元组, 魖节点容器爫部件即节点):
    __slots__ = ()


class 魖根深树爫元组(魖部件容器爫元组, 魖根深树):
    __slots__ = ()
class 魖光杆树爫元组(魖节点容器爫元组, 魖光杆树):
    __slots__ = ()
class 魖更深节点爫元组(魖节点容器爫元组, 魖更深节点):
    __slots__ = ()
class 魖左翼爫元组(魖节点容器爫元组, 魖左翼):
    __slots__ = ()
class 魖右翼爫元组(魖节点容器爫元组, 魖右翼):
    __slots__ = ()




######################
######################
######################
#具现爫元组爫最小极简:
class 乸匞根深树爫元组爫最小极简(魖匞根深树爫元组):
    __slots__ = ()
    @property
    @override
    def 乸根深树(sf, /):
        '-> 乸根深树{<:魖根深树}'
        return 乸根深树爫元组爫最小极简
匞根深树爫元组爫最小极简 = 乸匞根深树爫元组爫最小极简()
class 乸匞光杆树爫元组爫最小极简(魖匞光杆树爫元组):
    __slots__ = ()
    参数配置纟极简展翅树 = 最小参数配置纟极简展翅树
    @property
    @override
    def 乸光杆树(sf, /):
        '-> 乸光杆树{<:魖光杆树}'
        return 乸光杆树爫元组爫最小极简
匞光杆树爫元组爫最小极简 = 乸匞光杆树爫元组爫最小极简()
class 乸匞更深节点爫元组爫最小极简(魖匞更深节点爫元组):
    __slots__ = ()
    参数配置纟极简展翅树 = 最小参数配置纟极简展翅树
    @property
    @override
    def 乸更深节点(sf, /):
        '-> 乸更深节点{<:魖更深节点}'
        return 乸更深节点爫元组爫最小极简
匞更深节点爫元组爫最小极简 = 乸匞更深节点爫元组爫最小极简()

class 乸匞左右翼爫元组爫最小极简(魖匞左右翼爫元组):
    '魖左右翼爫元组+魖匞左右翼爫元组'
    __slots__ = ()
    参数配置纟极简展翅树 = 最小参数配置纟极简展翅树

    @property
    @override
    def 乸左翼(cls, /):
        '-> 乸左翼{<:魖右翼}'
        return 乸左翼爫元组爫最小极简
    @property
    @override
    def 乸右翼(sf, /):
        '-> 乸右翼{<:魖右翼}'
        return 乸右翼爫元组爫最小极简
匞左右翼爫元组爫最小极简 = 乸匞左右翼爫元组爫最小极简()

class 乸匞展翅树爫元组爫最小极简(魖匞展翅树):
    __slots__ = ()
    参数配置纟极简展翅树 = 最小参数配置纟极简展翅树
    匞根深树 = 匞根深树爫元组爫最小极简
    匞光杆树 = 匞光杆树爫元组爫最小极简
    匞更深节点 = 匞更深节点爫元组爫最小极简
    匞翅膀 = 匞左右翼爫元组爫最小极简
    def __repr__(sf, /):
        return repr_helper(sf)

匞展翅树爫元组爫最小极简 = 乸匞展翅树爫元组爫最小极简()













class 乸根深树爫元组爫最小极简(魖根深树爫元组):
    __slots__ = ()
    匞根深树 = 匞根深树爫元组爫最小极简
    匞展翅树 = 匞展翅树爫元组爫最小极简
乸匞根深树爫元组爫最小极简.乸根深树 = 乸根深树爫元组爫最小极简
匞根深树爫元组爫最小极简.构造冫根深树爫起讫扌(0, 1, 2, 左起丷右起=False)
匞根深树爫元组爫最小极简.构造冫根深树爫起讫扌(0, 1, 2, 左起丷右起=True)

class 乸光杆树爫元组爫最小极简(魖光杆树爫元组):
    __slots__ = ()
    匞光杆树 = 匞光杆树爫元组爫最小极简
    匞展翅树 = 匞展翅树爫元组爫最小极简
乸匞光杆树爫元组爫最小极简.乸光杆树 = 乸光杆树爫元组爫最小极简
匞光杆树爫元组爫最小极简.构造冫光杆树扌([0, 1], 左起丷右起=False)

class 乸更深节点爫元组爫最小极简(魖更深节点爫元组):
    __slots__ = ()
    匞更深节点 = 匞更深节点爫元组爫最小极简
乸匞更深节点爫元组爫最小极简.乸更深节点 = 乸更深节点爫元组爫最小极简
匞更深节点爫元组爫最小极简.构造冫更深节点扌([0, 1], 左起丷右起=True)

class 乸左翼爫元组爫最小极简(魖左翼爫元组):
    __slots__ = ()
    匞左右翼 = 匞左右翼爫元组爫最小极简
    匞展翅树 = 匞展翅树爫元组爫最小极简
class 乸右翼爫元组爫最小极简(魖右翼爫元组):
    __slots__ = ()
    匞左右翼 = 匞左右翼爫元组爫最小极简
    匞展翅树 = 匞展翅树爫元组爫最小极简

乸匞左右翼爫元组爫最小极简.乸左翼 = 乸左翼爫元组爫最小极简
乸匞左右翼爫元组爫最小极简.乸右翼 = 乸右翼爫元组爫最小极简
匞左右翼爫元组爫最小极简.构造冫翅膀扌([0,1], 左翼丷右翼=False, 左起丷右起=False)
匞左右翼爫元组爫最小极简.构造冫翅膀扌([0,1], 左翼丷右翼=True, 左起丷右起=True)









from seed.data_funcs.finger_tree__errors import Error4FingerTree, Error__empty_tree
#展翅树牜极简
#魖展翅树牜基本
#魖展翅树牜带总长
class ISimpleFingerTree(ABC):
    __slots__ = ()
    @abstractmethod
    def __len__(sf, /):
        '-> uint'
    @abstractmethod
    def iter_(sf, /, *, reverse):
        '-> Iter x'

    @abstractmethod
    def ipush_(sf, x, /, *, left_vs_right):
        '-> ISimpleFingerTree'
    @abstractmethod
    def ipop_(sf, /, *, left_vs_right):
        '-> (ISimpleFingerTree, x) | ^Error__empty_tree'


    def __iter__(sf, /):
        '-> Iter x'
        return sf.iter_(reverse=False)
    def __reversed__(sf, /):
        '-> Iter x'
        return sf.iter_(reverse=True)
    #@abstractmethod
    def get_endpoint_(sf, /, *, left_vs_right):
        '-> x | ^Error__empty_tree'
        for x in sf.iter_(reverse=left_vs_right):
            return x
        raise Error__empty_tree

    #@abstractmethod
    def ipop_then_ipush_on_same_endpoint_(sf, x, /, *, left_vs_right):
        '-> (ISimpleFingerTree, x) | ^Error__empty_tree'
        (sf, y) = sf.ipop_(left_vs_right=left_vs_right)
            # ^Error__empty_tree
        sf = sf.ipush_(x, left_vs_right=left_vs_right)
        return (sf, y)
    def ipush_then_ipop_on_diff_endpoints_(sf, x, /, *, leftward_vs_rightward):
        '-> (ISimpleFingerTree, x)'
        sf = sf.ipush_(x, left_vs_right=not leftward_vs_rightward)
        (sf, y) = sf.ipop_(left_vs_right=leftward_vs_rightward)
        return (sf, y)
    def ipushs_then_ipops_on_diff_endpoints_(sf, xs, /, *, leftward_vs_rightward):
        '-> (ISimpleFingerTree, [x])'
        #保长流动:
        #异端压弹牜序列扌
        #ipushs_then_ipops_on_diff_endpoints_
        L = len(sf)
        ls = []
        for x in xs:
            (sf, x) = sf.ipush_then_ipop_on_diff_endpoints_(x, leftward_vs_rightward=leftward_vs_rightward)
            ls.append(x)
        assert L == len(sf)
        return (sf, ls)

#展翅树牜带总长
class SimpleFingerTree(ISimpleFingerTree):
    r'''[[[
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.finger_tree__simple:SimpleFingerTree@T    =T    +exclude_attrs5listed_in_cls_doc
all_methods:
    __eq__
    __hash__
    __init__
    __iter__
    __len__
    __repr__
    __reversed__
    get_endpoint_
    ipop_
    ipop_then_ipush_on_same_endpoint_
    ipush_
    ipush_then_ipop_on_diff_endpoints_
    ipushs_then_ipops_on_diff_endpoints_
    iter_

    #]]]'''#'''
    ___no_slots_ok___ = True
    def __hash__(sf, /):
        return hash((type(sf), sf._t))
    def __eq__(sf, ot, /):
        if ot is sf:
            return True
        if not type(ot) is type(sf):
            return False
                # !! __hash__
            return NotImplemented
        return ot._t == sf._t
    def __repr__(sf, /):
        if not sf:
            return repr_helper(sf)
        xs = [*sf]
        return repr_helper(sf, xs)
    def __init__(sf, xs=(), /, *, reverse=False):
        check_type_is(bool, reverse)
        if not reverse and type(xs) is 展翅树牜带总长:
            tree = xs
        else:
            tree = 展翅树牜带总长(iter(xs), reverse)
        tree
        check_type_is(展翅树牜带总长, tree)
        sf._t = tree
    ######################
    ######################
    ######################
    @override
    def __len__(sf, /):
        '-> uint'
        return len(sf._t)
    @override
    def iter_(sf, /, *, reverse):
        '-> Iter x'
        return sf._t.枚举冫节点扌(左起丷右起=reverse)

    @override
    def ipush_(sf, x, /, *, left_vs_right):
        '-> ISimpleFingerTree'
        tree = sf._t.压入扌(x, 左端丷右端=left_vs_right)
        ot = type(sf)(tree)
        assert ot._t is tree
        return ot
    @override
    def ipop_(sf, /, *, left_vs_right):
        '-> (ISimpleFingerTree, x) | ^Error__empty_tree'
        if not sf:
            raise Error__empty_tree
        (tree, x) = sf._t.弹出扌(左端丷右端=left_vs_right)
        ot = type(sf)(tree)
        assert ot._t is tree
        return (ot, x)
#end-class SimpleFingerTree:


__all__
from seed.data_funcs.finger_tree__simple import 错误牜展翅树相关,错误牜空树
from seed.data_funcs.finger_tree__simple import Error4FingerTree, Error__empty_tree

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

from seed.data_funcs.finger_tree__simple import *
