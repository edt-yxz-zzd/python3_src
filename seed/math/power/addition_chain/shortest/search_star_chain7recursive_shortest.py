#__all__:goto
#TODO:goto
#DONE:靶值讠次大数讠首尾加链@枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/search_star_chain7recursive_shortest.py

seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫鬽首条加星链牜递归最短巛靶值灬扌 =10 =100 =300
    (1, 2, 3, 5, 10)
    (1, 2, 3, 6, 12, 13, 25, 50, 100)
    (1, 2, 4, 8, 7, 11, 19, 37, 75, 150, 300)
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫鬽首条加星链牜递归最短巛靶值灬扌 =10 =100 =300  +欤次大数降序
    (1, 2, 4, 8, 10)
    (1, 2, 4, 8, 16, 32, 64, 96, 100)
    (1, 2, 4, 8, 12, 24, 48, 96, 192, 288, 300)
]]

[[
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,1:枚举冫加星链牜递归最短巛靶值扌 =50215
    (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1025, 2050, 3075, 4099, 8198, 11273, 19471, 38942, 50215)
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,1:枚举冫加星链牜递归最短巛靶值扌 =50215  +欤次大数降序
    (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1025, 2050, 3075, 4099, 8198, 11273, 19471, 38942, 50215)
        同上！=>唯一！
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫加星链牜递归最短巛靶值扌 =50215  +欤次大数降序
    (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1025, 2050, 3075, 4099, 8198, 11273, 19471, 38942, 50215)
        唯一！
===
py_adhoc_call   seed.math.power.addition_chain.shortest.rewrite3   @严序加链讠最短缩写文本纟递归婪溟链扌 --fmt_case:dnzw_str  ='(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1025, 2050, 3075, 4099, 8198, 11273, 19471, 38942, 50215)'
    '[-^10-^1-2^10--2-1--2]'
]]
[[
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,1:枚举冫加星链牜递归最短巛靶值扌 =4320  +欤次大数降序
    (1, 2, 4, 8, 16, 32, 64, 96, 192, 384, 480, 960, 1920, 3840, 4320)
        #debug@_put4diff()
]]
[[
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌   --休眠期:auto :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌.out.txt
    @20260225晚九点半:启动
11503:consumed: 184.549589846 seconds
11519:consumed: 152.60545584600004 seconds
12463:consumed: 140.100729279 seconds

view /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌.out.txt
tail -n 1 /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌.out.txt
wc -l /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌.out.txt
du -bh /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌.out.txt
    604K #@[1..=12671]
grep '^-' /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌.out.txt
    -12509
    ... ...
]]
[[
++kw:欤只保留首条加链乊次大数
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫加星链牜递归最短巛靶值扌 +欤只保留首条加链乊次大数 =5
    (1, 2, 3, 5)
    (1, 2, 4, 5)
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫加星链牜递归最短巛靶值扌 +欤只保留首条加链乊次大数 =1
    (1,)
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫加星链牜递归最短巛靶值扌 +欤只保留首条加链乊次大数 =15
    (1, 2, 3, 6, 9, 15)
    (1, 2, 3, 5, 10, 15)
    (1, 2, 3, 6, 12, 15)
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫加星链牜递归最短巛靶值扌 +欤只保留首条加链乊次大数 =15 +欤次大数降序
    (1, 2, 3, 6, 12, 15)
    (1, 2, 4, 5, 10, 15)
    (1, 2, 3, 6, 9, 15)
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举冫加星链牜递归最短巛靶值扌 =15 +欤次大数降序
    (1, 2, 3, 6, 12, 15)
    (1, 2, 4, 5, 10, 15)
    (1, 2, 3, 5, 10, 15)
    (1, 2, 3, 6, 9, 15)

]]
[[
#ver1:py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 --鬽最大靶值=20  --休眠期:auto :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.out.txt
#rm -iv /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-?.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.out.txt


#ver1:py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 --鬽最大靶值=2000  --休眠期:auto :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.out.txt

mv -iv /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.out.txt /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver1.out.txt

py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   @格式转换冫文件冃靶值讠次大数讠首尾加星链牜递归最短扌 +verbose  --verI=1 --verO=2  --ipath:/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver1.out.txt  --opath:/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt

wc -l /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt
#wc -l /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver1.out.txt
wc -l /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt
#du -bh /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver1.out.txt
    2.4M #@le2000
    6.0M #@le3754
du -bh /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt
    4.6M #@le3754
    5.3M #@le4203
    24M #@le12509
    53M #@le23219
du -bh /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt
    104K #@le2000
    235K #@le3754
    269K #@le4203
    1.1M #@le12509
    2.4M #@le23219

prefixAB=/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 --ver=2 --鬽最大靶值=12509  --休眠期:auto :"${prefixAB}".-0.out.txt :"${prefixAB}".-1.ver2.out.txt
    DONE
tail -n 1 /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt
    『[#DDd+B]』 #@le12509
tail -n 1 /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt
    『[#DDd+B]』 #@le12509 同上:因为没有次大数
head -n 16 /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt
#slow:grep '^[^,]*$' -n /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt
grep ',' -v -n /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt
    1:[#B+B]
    12509:[#DDd+B]
    13207:[#DOX+B]
    13705:[#DWJ+B]
    15473:[#Dxx+B]
    16537:[#ECZ+B]
    20753:[#FER+B]
    22955:[#Fmr+B]
    23219:[#Fqz+B]

+欤中止乊靶值牜无加星链牜递归最短
+欤询问中止乊靶值牜无加星链牜递归最短
#py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 +欤询问中止乊靶值牜无加星链牜递归最短  --ver=2 --鬽最大靶值=None  --休眠期:auto :"${prefixAB}".-0.out.txt :"${prefixAB}".-1.ver2.out.txt
    #(1, 0, '[#B+B]')
    #(12509, 0, '[#DDd+B]')
    (13207, 0, '[#DOX+B]')
    (13705, 0, '[#DWJ+B]')
    (15473, 0, '[#Dxx+B]')
    (16537, 0, '[#ECZ+B]')
    (20753, 0, '[#FER+B]')
    (22955, 0, '[#Fmr+B]')
    (23219, 0, '[#Fqz+B]')
    stop
出现间隔越来越短:
>>> 13207 -12509
698
>>> 13705 -13207
498
>>> 15473 -13705
1768

echo $[15473 -13705]
    1768
echo $[16537 -15473]
    1064
echo $[20753 -16537]
    4216
echo $[23219 -20753]
    2466

18815:consumed: 91.17141320300016 seconds
23038:consumed: 41.11697117800031 seconds
23039:consumed: 37.1046361560002 seconds

>>> bin(18815)
'0b100100101111111'

py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 -欤询问中止乊靶值牜无加星链牜递归最短  --ver=2 --鬽最大靶值=None  --休眠期:auto :"${prefixAB}".-0.out.txt :"${prefixAB}".-1.ver2.out.txt
    TODO
]]
[[
修改代码后校验:
#ver1:py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 --鬽最大靶值=1000  --休眠期:auto :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0small.out.txt :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1small.out.txt
file_startswith_ /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1small.out.txt  /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.out.txt
    => same
file_startswith_ /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0small.out.txt  /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt
    => same

]]
[[
修改代码后校验:++ver2:
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 --ver=2 --鬽最大靶值=500  --休眠期:auto :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0small.ver2.out.txt :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1small.ver2.out.txt

file_startswith_ /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1small.ver2.out.txt  /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt
    => same
file_startswith_ /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0small.ver2.out.txt  /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt
    => same
]]
[[
修改代码后校验:++contains7bisect_@put_:
py_adhoc_call   seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest   ,枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌 --ver=2 --鬽最大靶值=500  --休眠期:auto :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0small.put_.ver2.out.txt :/sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1small.put_.ver2.out.txt
file_startswith_ /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1small.put_.ver2.out.txt  /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-1.ver2.out.txt
    => same
file_startswith_ /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0small.put_.ver2.out.txt  /sdcard/0my_files/tmp/out4py/seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest..枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌.-0.out.txt
    => same
]]







]]]'''#'''
__all__ = r'''
枚举冫加星链牜递归最短巛靶值扌
    枚举冫鬽首条加星链牜递归最短巛靶值灬扌

枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌
初始化冫参数扌
    构造冫最小显链长讠升列纟靶值扌
    最小化冫最大靶值扌

枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌
    加载冫靶值讠升列纟次大数牜递归最短扌



FormatError
格式转换冫文件冃靶值讠次大数讠首尾加星链牜递归最短扌


构造冫首尾加链扌

表述冫文本冃鬽首尾加链扌
解读冫文本冃鬽首尾加链扌

升列讠文本扌
升列巛文本扌

表述冫文本冃次大数讠首尾加链扌
解读冫文本冃次大数讠首尾加链扌
    表述冫文本冃升列纟次大数扌
    解读冫文本冃升列纟次大数扌

    表述冫文本冃首尾加链乊次大数扌
    解读冫文本冃首尾加链乊次大数扌
        表述冫文本冃加链乊次大数扌
        解读冫文本冃加链乊次大数扌



'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import islice
    from bisect import bisect_left
    from seed.for_libs.for_bisect import contains7bisect_
    from seed.for_libs.for_time import mk_rest_func_
    from seed.tiny_.check import check_type_in, check_type_is, check_int_ge, check_int_ge_le, check_may_
    from seed.debug.print_err import print_err
    from seed.io.ask import ask_yes_no_
    from seed.math.power.addition_chain.shortest.rewrite3 import 严序加链讠最短缩写文本纟递归婪溟链扌, 严序加链巛最短缩写文本纟递归婪溟链扌
    #.def 严序加链讠最短缩写文本纟递归婪溟链扌(严序加链, /, *, fmt_case):
    #.    '严序加链 -> 最短缩写文本纟递归婪溟链/str | ^Error__addition_chain_has_no_greedy_zpow_recur_shortest_stem # [fmt_case == ("stem_str" | "dnzw_str")]'

    #xxx:from seed.math.power.addition_chain.data.target_uint2may_len_optimal_addition_chain import 靶值讠最小显链长
    #xxx:from seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain import 最小显链长讠靶值列表 # .最大靶值牜可用 .最小靶值牜溢出
    from seed.data_funcs.rngs import make_NonTouchRanges, sorted_ints_to_iter_nontouch_ranges
    from seed.data_funcs.rngs import ranges2delta_txt_, ranges5delta_txt_, uint2base64_, uint5base64_
___end_mark_of_excluded_global_names__0___ = ...

def 初始化冫参数扌(鬽最大靶值=None, 靶值讠最小显链长=None, 最小显链长讠升列纟靶值=None, *, 欤无需冫最小显链长讠升列纟靶值=False):
    '-> (最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值)'
    if 靶值讠最小显链长 is None:
        if not 最小显链长讠升列纟靶值 is None:raise TypeError
        from seed.math.power.addition_chain.data.target_uint2may_len_optimal_addition_chain import 靶值讠最小显链长
    靶值讠最小显链长
    最大靶值 = 最小化冫最大靶值扌(鬽最大靶值, 靶值讠最小显链长)
    if 欤无需冫最小显链长讠升列纟靶值:
        最小显链长讠升列纟靶值 = None
    elif 最小显链长讠升列纟靶值 is None:
        if 最大靶值 <= 10_0000:
            from seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain import 最小显链长讠靶值列表 as 最小显链长讠升列纟靶值 # .最大靶值牜可用 .最小靶值牜溢出
        else:
            最小显链长讠升列纟靶值 = 构造冫最小显链长讠升列纟靶值扌(最大靶值, 靶值讠最小显链长)
        最小显链长讠升列纟靶值
    最小显链长讠升列纟靶值
    return (最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值)
def 构造冫最小显链长讠升列纟靶值扌(最大靶值, 靶值讠最小显链长, /):
    最大靶值 = min(最大靶值, -1+len(靶值讠最小显链长))
    最小显链长讠升列纟靶值 = []
    for 靶值 in range(1, 1+最大靶值):
        最小显链长 = 靶值讠最小显链长[靶值]
        if not 最小显链长 < len(最小显链长讠升列纟靶值):
            最小显链长讠升列纟靶值.extend([] for _ in range(1+最小显链长 - len(最小显链长讠升列纟靶值)))
        最小显链长讠升列纟靶值[最小显链长].append(靶值)
    最小显链长讠升列纟靶值 = tuple(map(tuple, 最小显链长讠升列纟靶值))
    return 最小显链长讠升列纟靶值
def 最小化冫最大靶值扌(鬽最大靶值, 靶值讠最小显链长, /):
    check_may_([check_int_ge, 0], 鬽最大靶值)
    最大靶值 = -1+len(靶值讠最小显链长)
    if not 鬽最大靶值 is None:
        最大靶值 = min(最大靶值, 鬽最大靶值)
    check_int_ge(0, 最大靶值)
    return 最大靶值

def 枚举冫鬽首条加星链牜递归最短巛靶值灬扌(*列表纟靶值, 欤次大数降序=False, 欤带靶值=False):
    for 靶值 in 列表纟靶值:
        it = 枚举冫加星链牜递归最短巛靶值扌(靶值, 欤次大数降序=欤次大数降序)
        鬽首条加链 = next(it, None)
            #鬽首条加星链牜递归最短纟靶值
        yield 鬽首条加链 if not 欤带靶值 else (靶值, 鬽首条加链)
def 枚举冫加星链牜递归最短巛靶值扌(靶值, /, *, 欤次大数降序=False, 欤只保留首条加链乊次大数=False, 靶值讠最小显链长=None, 最小显链长讠升列纟靶值=None, 靶值讠升列纟次大数=None):
    (最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值) = 初始化冫参数扌(鬽最大靶值:=靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值)
    if 靶值讠升列纟次大数 is None:
        靶值讠升列纟次大数 = ()

    iter_ = iter if not 欤次大数降序 else reversed
    最小显链长纟靶值 = 靶值讠最小显链长[靶值]
    最小显链长讠升列纟靶值[最小显链长纟靶值]
    us = [None]*(1+最小显链长纟靶值)
    us[0] = 1
    us[-1] = 靶值
    def _put4diff(_szmm4v, diff, /):
        #可能 最小显链长{diff} 超过 最小显链长{靶值}
        szmm4diff = 靶值讠最小显链长[diff]
        existed = put_(szmm4diff, diff) if szmm4diff <= _szmm4v else -1
        return (szmm4diff, existed)
    def put_(szmm, u, /):
        '-> imay existed'
        try:
            existed = not us[szmm] is None
        except IndexError:
            raise IndexError((us, len(us), (szmm, u, 靶值讠最小显链长[u]), (最小显链长纟靶值, 靶值)))
            #^IndexError: ([1, None, None, None, None, None, None, None, None, None, None, 223, None, 4097, 4320], 15, (15, 2047, 15), (14, 4320))
        # [existed == (0|1)]
        if existed:
            # [existed == (1)]
            if not u == us[szmm]:
                existed = -1
                # [existed == (-1)]
                # [u =!= us[szmm]]
            else:
                # [existed == (1)]
                # [u == us[szmm]]
                pass
            # [existed == (-1|1)]
            # [[existed == (-1)] <-> [u =!= us[szmm]]]
        else:
            # [existed == (0)]
            if u < len(靶值讠升列纟次大数) and szmm > 0 and not None is (prev:=us[szmm-1]) and not contains7bisect_(靶值讠升列纟次大数[u], prev):
                existed = -1
            elif szmm+1 < len(us) and not None is (succ:=us[szmm+1]) and succ < len(靶值讠升列纟次大数) and not contains7bisect_(靶值讠升列纟次大数[succ], u):
                existed = -1
            else:
                # [existed == (0)]
                us[szmm] = u
                # [u == us[szmm]]
                # [[existed == (-1)] <-> [u =!= us[szmm]]]
            # [[existed == (-1)] <-> [u =!= us[szmm]]]
        # [[existed == (-1)] <-> [u =!= us[szmm]]]
        return existed
    def drop__(szmm, existed, u, /):
        if not type(existed) is bool:raise 000
        if not existed:
            us[szmm] = None
        return
    if 欤只保留首条加链乊次大数:
        stop_ = bool
    else:
        def stop_(sz, /):
            return False
    def recur_iter0_(b_toplvl, szmm, u, /):
        # [szmm == 靶值讠最小显链长[u]]
        existed = put_(szmm, u)
        if -1 == existed:
            return 0
        #bug:
        #.it = recur_iter1_(szmm, u)
        #.if not b_toplvl and 欤只保留首条加链乊次大数:
        #.    it = islice(it, 0, 1)
        #.it
        #.yield from it
        sz = yield from recur_iter1_(b_toplvl, szmm, u)
        drop__(szmm, existed, u)
        return sz
    def recur_iter1_(b_toplvl, szmm, u, /):
        if u == 1:
            yield tuple(us)
            return 1
        _szmm = szmm -1
        assert _szmm >= 0
        if not None is (v:=us[_szmm]):
            diff = u - v
            if not 0 < diff <= v:
                return 0
            if u < len(靶值讠升列纟次大数):
                vs = 靶值讠升列纟次大数[u]
                if 0:
                    j = bisect_left(vs, v)
                    if not (j < len(vs) and vs[j] == v):
                        return 0
                if not contains7bisect_(vs, v):
                    return 0
            vs = [v]
            js = [0]
        else:
            (vs, js) = _靶值讠候选次大数信息扌(最小显链长讠升列纟靶值, 靶值讠升列纟次大数, u, _szmm)
        (vs, js)
        sz = 0
        for j in iter_(js):
            v = vs[j]
            diff = u - v
            sz += yield from recur_iter2_(_szmm, v, diff)
            if not b_toplvl and stop_(sz):
                break
        sz
        return sz

    def recur_iter2_(_szmm, v, diff, /):
        assert 0 < diff <= v, (_szmm, v, diff)
        (szmm4diff, existed) = _put4diff(_szmm, diff)
        if -1 == existed:
            return 0
        sz = yield from recur_iter0_(False, _szmm, v)
        drop__(szmm4diff, existed, diff)
        return sz
    def main():
        sz = yield from recur_iter0_(True, 最小显链长纟靶值, 靶值)
        assert all(m is None for m in us[1:-1])
    return main()


def _靶值讠候选次大数信息扌(最小显链长讠升列纟靶值, 靶值讠升列纟次大数, u, _szmm, /):
    if u < len(靶值讠升列纟次大数):
        vs = 靶值讠升列纟次大数[u]
        js = range(len(vs))
    else:
        vs = 最小显链长讠升列纟靶值[_szmm]
        begin = bisect_left(vs, (u+1)//2)
        end = bisect_left(vs, u, begin)
        js = range(begin, end)
    vs, js
    return (vs, js)
def _读冫末行扌(end_addr, ibfile, /):
    if end_addr == 0:
        return b''
    ibfile.seek(end_addr-1)
    bs = ibfile.read()
    if not bs[-1:] == b'\n':raise FormatError
    for j in range(0, end_addr, 128)[::-1]:
        ibfile.seek(j)
        bs = ibfile.read()
        assert bs
        k = 1+bs.rfind(b'\n', 0, len(bs)-1)
        if not k == 0:
            bs = bs[k:]
            break
    else:
        assert j == 0
        bs
    bs
    return bs







def 枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌(文件路径, /, *, 休眠期=0.0, 苏醒期=2.0, 鬽最大靶值=None, 靶值讠最小显链长=None, 最小显链长讠升列纟靶值=None):
    check_type_in([float, str], 休眠期)
    _rest = mk_rest_func_(休眠期, 苏醒期)
    (最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值) = 初始化冫参数扌(鬽最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值)
    kwds = dict(靶值讠最小显链长=靶值讠最小显链长, 最小显链长讠升列纟靶值=最小显链长讠升列纟靶值)

    encoding = 'ascii'
    with open(文件路径, 'ab+') as iobfile:
        end_addr = iobfile.tell()
        bs = _读冫末行扌(end_addr, iobfile)
        assert end_addr == iobfile.tell()
        靶值纟末行 = _解读冫行讠靶值扌(bs.decode(encoding)) if bs else 0
        起始靶值 = 1+靶值纟末行
        #.靶值 = 靶值纟末行
        #.while 靶值 < 最大靶值:
        #.    靶值 += 1
        for 靶值 in range(起始靶值, 1+最大靶值):
            鬽首尾加链 = _靶值讠鬽首尾加链扌(kwds, 靶值)
            s = 表述冫文本冃鬽首尾加链扌(靶值, 鬽首尾加链, validate=True)
            iobfile.write(s.encode(encoding))
            777;iobfile.write(b'\n')
            yield (靶值, s)
            777;_rest()


def _靶值讠鬽首尾加链扌(kwds, 靶值, /):
    it = 枚举冫加星链牜递归最短巛靶值扌(靶值, 欤次大数降序=False, **kwds)
    鬽加链 = next(it, None)
    if None is 鬽加链:
        鬽首尾加链 = None
    else:
        首加链 = 鬽加链
        it = 枚举冫加星链牜递归最短巛靶值扌(靶值, 欤次大数降序=True, **kwds)
        尾加链 = next(it, None)
        首尾加链 = 构造冫首尾加链扌(首加链, 尾加链)
        鬽首尾加链 = 首尾加链
    鬽首尾加链
    return 鬽首尾加链

def 表述冫文本冃鬽首尾加链扌(靶值, 鬽首尾加链, /, *, validate):
    if None is 鬽首尾加链:
        s = f'-{靶值}'
    else:
        首尾加链 = 鬽首尾加链
        assert 1 <= len(首尾加链) <= 2
        s = ','.join(严序加链讠最短缩写文本纟递归婪溟链扌(us, fmt_case='dnzw_str') for us in 首尾加链)
    s
    if validate:
        assert (靶值, 鬽首尾加链) == (__:=解读冫文本冃鬽首尾加链扌(s)), ((靶值, 鬽首尾加链), __, s)
    return s
def 解读冫文本冃鬽首尾加链扌(s, /):
    '-> (靶值, 鬽首尾加链)'
    #'-> (case,x)/((0,负靶值牜失败)|(1,(唯一加链,))|(2,(首加链,尾加链)))'
    if s[0] == '-':
        负靶值牜失败 = int(s)
        #.return (0, 负靶值牜失败)
        靶值 = -负靶值牜失败
        check_int_ge(1, 靶值)
        鬽首尾加链 = None
    else:
        #ss = s.replace('][', ']:[').split(':')
        ss = s.split(',')
        if not len(ss) in (1,2):raise FormatError(s)
        uss = tuple(严序加链巛最短缩写文本纟递归婪溟链扌(t, fmt_case='dnzw_str') for t in ss)
        if len(uss) == 2:
            (us0, us1) = uss
            assert len(us0) == len(us1), uss
            assert us0[::-1] < us1[::-1], uss
            assert us0[-1] == us1[-1], uss
        else:
            (us01,) = uss
        #.return (len(uss), uss)
        首尾加链 = uss
        assert 1 <= len(首尾加链) <= 2
        靶值 = 首尾加链[0][-1]
        鬽首尾加链 = 首尾加链
    return (靶值, 鬽首尾加链)
def _解读冫行冃鬽首尾加链扌(s, /):
    '-> (靶值, 鬽首尾加链)'
    s = s.strip()
    return 解读冫文本冃鬽首尾加链扌(s)
def _解读冫行讠靶值扌(s, /):
    (靶值, 鬽首尾加链) = _解读冫行冃鬽首尾加链扌(s)
    return 靶值
    #.match _解读冫行冃鬽首尾加链扌(s):
    #.    case (0,负靶值牜失败):
    #.        靶值 = -负靶值牜失败
    #.    case (1|2, uss):
    #.        靶值 = uss[0][-1]
    #.    case bad:
    #.        raise FormatError(bad)
    #.return 靶值

def 构造冫首尾加链扌(首加链, 尾加链, /):
    if 首加链 == 尾加链:
        首尾加链 = (首加链,)
    else:
        assert 首加链[::-1] < 尾加链[::-1]
        首尾加链 = (首加链, 尾加链)
    return 首尾加链








class FormatError(Exception):pass
def 格式转换冫文件冃靶值讠次大数讠首尾加星链牜递归最短扌(*, ipath, opath, verI, verO, verbose=False):
    check_int_ge_le(1, _MAX_VERSION4fmt4us, verI)
    check_int_ge_le(1, _MAX_VERSION4fmt4us, verO)
    encoding = 'ascii'
    with open(ipath, 'rt', encoding=encoding) as ifile, open(opath, 'xt', encoding=encoding) as ofile:
        for line in ifile:
            文本 = line.strip()
            (靶值, 次大数讠首尾加链) = 解读冫文本冃次大数讠首尾加链扌(文本, ver=verI)
            verbose and print_err('靶值=', 靶值)
            _s = 表述冫文本冃次大数讠首尾加链扌(靶值, 次大数讠首尾加链, validate=True, ver=verO)
            print(_s, file=ofile)

def 枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌(文件路径冃靶值讠升列纟次大数牜递归最短, 输出文件路径冃靶值讠次大数讠首尾加星链牜递归最短, /, *, ver, 休眠期=0.0, 苏醒期=2.0, 鬽最大靶值=None, 靶值讠最小显链长=None, 最小显链长讠升列纟靶值=None, 欤中止乊靶值牜无加星链牜递归最短=False, 欤询问中止乊靶值牜无加星链牜递归最短=False):
    check_int_ge_le(1, _MAX_VERSION4fmt4us, ver)
    check_type_in([float, str], 休眠期)
    _rest = mk_rest_func_(休眠期, 苏醒期)
    (最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值) = 初始化冫参数扌(鬽最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值)
    encoding = 'ascii'
    with open(文件路径冃靶值讠升列纟次大数牜递归最短, 'at+', encoding=encoding) as iofile, open(输出文件路径冃靶值讠次大数讠首尾加星链牜递归最短, 'at', encoding=encoding) as ofile:
        end_addr = iofile.tell()
        iofile.seek(0)
        靶值讠升列纟次大数 = 加载冫靶值讠升列纟次大数牜递归最短扌(iofile)
        assert end_addr == iofile.tell()
        777;_rest()
        kwds = dict(靶值讠最小显链长=靶值讠最小显链长, 最小显链长讠升列纟靶值=最小显链长讠升列纟靶值, 靶值讠升列纟次大数=靶值讠升列纟次大数, 欤只保留首条加链乊次大数=True)
        起始靶值 = len(靶值讠升列纟次大数)
        for 靶值 in range(起始靶值, 1+最大靶值):
            (升列纟次大数, 次大数讠首尾加链) = _靶值讠升列纟次大数丶次大数讠首尾加链扌(kwds, 靶值)
            #######
            s1 = 表述冫文本冃次大数讠首尾加链扌(靶值, 次大数讠首尾加链, validate=True, ver=ver)
            s0 = 表述冫文本冃升列纟次大数扌(靶值, 升列纟次大数, validate=True)
            #######
            #输出到:细节文件
            print(s1, file=ofile)
                #若是 抛出异常，两文件 依然匹配
            #输出到:摘要文件
            print(s0, file=iofile)
                #若是 抛出异常，细节文件 比 摘要文件 多一行，但是 删除重复行更容易，而且 摘要文件行 总是 细节文件行 的 前缀，更容易定位、摘选、复制
            #######
            yield (靶值, len(升列纟次大数), s0)
            if not 升列纟次大数:
                if 欤中止乊靶值牜无加星链牜递归最短:
                    break
                if 欤询问中止乊靶值牜无加星链牜递归最短:
                    if ask_yes_no_('stop? (y/n):'):
                        break
            777;_rest()

def _靶值讠升列纟次大数丶次大数讠首尾加链扌(kwds, 靶值, /):
    靶值讠升列纟次大数 = kwds['靶值讠升列纟次大数']
    if not 靶值 == len(靶值讠升列纟次大数):raise 000#append

    it = 枚举冫加星链牜递归最短巛靶值扌(靶值, 欤次大数降序=False, **kwds)
    列表纟首加链 = tuple(it)
    次大数讠首加链 = {us[-2]:us for us in 列表纟首加链} if not 靶值 == 1 else {}
    777;升列纟次大数 = tuple(sorted(次大数讠首加链.keys()))
    777;靶值讠升列纟次大数.append(升列纟次大数)#for next step:列表纟尾加链
    if 次大数讠首加链:
        it = 枚举冫加星链牜递归最短巛靶值扌(靶值, 欤次大数降序=True, **kwds)
        列表纟尾加链 = tuple(it)
        assert len(列表纟尾加链) == len(列表纟首加链)
        次大数讠首尾加链 = {us[-2]:构造冫首尾加链扌(次大数讠首加链[us[-2]], us) for us in 列表纟尾加链}
    else:
        assert 靶值 == 1 or not 列表纟首加链#12509
        次大数讠首尾加链 = {}
    return (升列纟次大数, 次大数讠首尾加链)

def _升列讠升区扌(us, /):
    ranges = make_NonTouchRanges(sorted_ints_to_iter_nontouch_ranges(us))
    return ranges
def _升列巛升区扌(ranges, /):
    us = tuple(ranges.iter_ints())
    return us
def 升列讠文本扌(升列, /, *, validate):
    #.return _升列讠升区扌(us).to_delta_txt(validate=False)
    文本 = ranges2delta_txt_(_升列讠升区扌(升列), validate=False)
    if validate:
        assert 升列 == (__:=升列巛文本扌(文本)), (升列, __, 文本)
    return 文本
def 升列巛文本扌(s, /):
    ranges = ranges5delta_txt_(s)
    return _升列巛升区扌(ranges)
def 表述冫文本冃升列纟次大数扌(靶值, 升列纟次大数, /, *, validate):
    check_type_is(tuple, 升列纟次大数)
    升列 = (*升列纟次大数, 靶值)
    文本 = 升列讠文本扌(升列, validate=False)
    if validate:
        assert (靶值, 升列纟次大数) == (__:=解读冫文本冃升列纟次大数扌(文本)), ((靶值, 升列纟次大数), __, 文本)
    return 文本
def 解读冫文本冃升列纟次大数扌(s, /):
    '-> (靶值, 升列纟次大数)'
    升列 = 升列巛文本扌(s)
    #(*升列纟次大数, 靶值) = 升列
    靶值 = 升列[-1]
    升列纟次大数 = 升列[:-1]
    return (靶值, 升列纟次大数)
_MAX_VERSION4fmt4us = 2
def 表述冫文本冃加链乊次大数扌(靶值, 次大数, 加链, /, *, validate, ver):
    '-> str | ^Error__addition_chain_has_no_greedy_zpow_recur_shortest_stem'
    check_int_ge_le(1, _MAX_VERSION4fmt4us, ver)
    match ver:
        case 1:
            #old:
            assert 加链[:2] == (1,2)
            assert 加链[-2:] == (次大数,靶值)
            升列 = 加链[2:-2]
            文本 = 升列讠文本扌(升列, validate=False)
        case 2:
            #new:
            文本 = 严序加链讠最短缩写文本纟递归婪溟链扌(加链, fmt_case='dnzw_str')
                # ^Error__addition_chain_has_no_greedy_zpow_recur_shortest_stem
        case _:
            raise TypeError(ver)
        #case
    if validate:
        assert (加链) == (__:=解读冫文本冃加链乊次大数扌(靶值, 次大数, 文本, ver=ver)), ((靶值, 次大数, 加链), __, 文本)
    return 文本
def 解读冫文本冃加链乊次大数扌(靶值, 次大数, s, /, *, ver):
    '-> 加链'
    check_int_ge_le(1, _MAX_VERSION4fmt4us, ver)
    match ver:
        case 1:
            #old:
            升列 = 升列巛文本扌(s)
            if not 升列 and 次大数 <= 2:
                加链 = (1, 2, 靶值) if 次大数 == 2 else (1, 2)
            else:
                加链 = (1, 2, *升列, 次大数, 靶值)
        case 2:
            #new:
            加链 = 严序加链巛最短缩写文本纟递归婪溟链扌(s, fmt_case='dnzw_str')
        case _:
            raise TypeError(ver)
        #case
    return 加链
def 表述冫文本冃首尾加链乊次大数扌(靶值, 次大数, 首尾加链, /, *, validate, ver):
    check_int_ge_le(1, _MAX_VERSION4fmt4us, ver)
    assert 1 <= len(首尾加链) <= 2
    文本 = ':'.join(表述冫文本冃加链乊次大数扌(靶值, 次大数, 加链, validate=False, ver=ver) for 加链 in 首尾加链)
    if validate:
        assert (首尾加链) == (__:=解读冫文本冃首尾加链乊次大数扌(靶值, 次大数, 文本, ver=ver)), ((靶值, 次大数, 首尾加链), __, 文本)
    return 文本
def 解读冫文本冃首尾加链乊次大数扌(靶值, 次大数, s, /, *, ver):
    '-> 首尾加链'
    check_int_ge_le(1, _MAX_VERSION4fmt4us, ver)
    首尾加链 = tuple(解读冫文本冃加链乊次大数扌(靶值, 次大数, t, ver=ver) for t in s.split(':'))
    assert 1 <= len(首尾加链) <= 2
    return 首尾加链
def 表述冫文本冃次大数讠首尾加链扌(靶值, 次大数讠首尾加链, /, *, validate, ver):
    check_int_ge_le(1, _MAX_VERSION4fmt4us, ver)
    升列纟次大数 = tuple(sorted(次大数讠首尾加链.keys()))
    def __():
        s0 = 表述冫文本冃升列纟次大数扌(靶值, 升列纟次大数, validate=False)
        yield s0
        for 次大数 in 升列纟次大数:
            首尾加链 = 次大数讠首尾加链[次大数]
            yield 表述冫文本冃首尾加链乊次大数扌(靶值, 次大数, 首尾加链, validate=False, ver=ver)
    文本 = ','.join(__())
    if validate:
        assert (靶值, 次大数讠首尾加链) == 解读冫文本冃次大数讠首尾加链扌(文本, ver=ver)
    return 文本
def 解读冫文本冃次大数讠首尾加链扌(s, /, *, ver):
    '-> (靶值, 次大数讠首尾加链)'
    check_int_ge_le(1, _MAX_VERSION4fmt4us, ver)
    [s0, *ss] = s.split(',')
    (靶值, 升列纟次大数) = 解读冫文本冃升列纟次大数扌(s0)
    if not len(ss) == len(升列纟次大数):raise FormatError(s)
    次大数讠首尾加链 = {次大数:解读冫文本冃首尾加链乊次大数扌(靶值, 次大数, t, ver=ver) for 次大数, t in zip(升列纟次大数, ss)}
    return (靶值, 次大数讠首尾加链)
def 加载冫靶值讠升列纟次大数牜递归最短扌(ifile, /):
    assert ifile.tell() == 0
    靶值讠升列纟次大数 = [None]
    for lineno, line in enumerate(ifile, 1):
        if not line[-1:] == '\n':raise FormatError
        s = line.strip()
        (靶值, 升列纟次大数) = 解读冫文本冃升列纟次大数扌(s)
        if not 靶值 == lineno:raise ValueError(lineno, s, 靶值, 升列纟次大数)
        if not 靶值 == len(靶值讠升列纟次大数):raise 000
        靶值讠升列纟次大数.append(升列纟次大数)
    return 靶值讠升列纟次大数


__all__
from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 枚举冫加星链牜递归最短巛靶值扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 枚举冫加星链牜递归最短巛靶值扌, 枚举冫鬽首条加星链牜递归最短巛靶值灬扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 枚举生成冫文件冃靶值讠鬽首尾加星链牜递归最短扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 初始化冫参数扌, 构造冫最小显链长讠升列纟靶值扌, 最小化冫最大靶值扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾加星链牜递归最短扌, 加载冫靶值讠升列纟次大数牜递归最短扌



from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import FormatError, 格式转换冫文件冃靶值讠次大数讠首尾加星链牜递归最短扌


from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 构造冫首尾加链扌
from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 表述冫文本冃鬽首尾加链扌, 解读冫文本冃鬽首尾加链扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 升列讠文本扌, 升列巛文本扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 表述冫文本冃次大数讠首尾加链扌, 解读冫文本冃次大数讠首尾加链扌, 表述冫文本冃升列纟次大数扌, 解读冫文本冃升列纟次大数扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 表述冫文本冃首尾加链乊次大数扌, 解读冫文本冃首尾加链乊次大数扌, 表述冫文本冃加链乊次大数扌, 解读冫文本冃加链乊次大数扌



from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import *
