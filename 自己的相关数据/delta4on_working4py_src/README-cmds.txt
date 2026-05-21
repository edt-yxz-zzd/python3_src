
e ../../python3_src/自己的相关数据/delta4on_working4py_src/README-cmds.txt
剪切整合临时文件内容:
  cat5mv__myfiles -f cat5mv__myfiles.conf


2 places:
  /sdcard/0my_files/git_repos/txt_phone/txt/script/delta4on_working4py_src/
  /sdcard/0my_files/git_repos/python3_src/自己的相关数据/delta4on_working4py_src/
2 backup_tools:
  git
    delta4on_working.1.git.txt
  dir_cmp.py
    delta4on_working.1.dir_cmp.txt



[[def__backup_cmds]]
for backup cmd:
  view ../../python3_src/nn_ns/filedir/backup_tools/main.py
  view ../../python3_src/my_convention/backup_cmds.txt
  $ view $tmp/$my_xxx/out__result_of_dir_cmp__relative__extended.txt
  e /sdcard/0my_files/tmp/my_src/out__result_of_dir_cmp__relative__extended.txt

  cp -T /sdcard/0my_files/tmp/my_src/out__result_of_dir_cmp__relative__extended.txt   /sdcard/0my_files/git_repos/txt_phone/txt/script/delta4on_working4py_src/delta4on_working.1.dir_cmp.txt
  e /sdcard/0my_files/git_repos/txt_phone/txt/script/delta4on_working4py_src/delta4on_working.1.dir_cmp.txt

  cp -T /sdcard/0my_files/tmp/my_src/out__result_of_dir_cmp__relative__extended.txt    /sdcard/0my_files/git_repos/python3_src/自己的相关数据/delta4on_working4py_src/delta4on_working.1.dir_cmp.txt
  e /sdcard/0my_files/git_repos/python3_src/自己的相关数据/delta4on_working4py_src/delta4on_working.1.dir_cmp.txt


  ============git
  g0
  cd $my_git_py
  g1
  g3
  mkdir /sdcard/0my_files/git_repos/txt_phone/txt/script/delta4on_working4py_src/
  g3 > /sdcard/0my_files/git_repos/txt_phone/txt/script/delta4on_working4py_src/delta4on_working.1.git.txt
  e /sdcard/0my_files/git_repos/txt_phone/txt/script/delta4on_working4py_src/delta4on_working.1.git.txt
  --
  mkdir /sdcard/0my_files/git_repos/python3_src/自己的相关数据/delta4on_working4py_src/
  cp -t /sdcard/0my_files/git_repos/python3_src/自己的相关数据/delta4on_working4py_src/   /sdcard/0my_files/git_repos/txt_phone/txt/script/delta4on_working4py_src/delta4on_working.1.git.txt
  e /sdcard/0my_files/git_repos/python3_src/自己的相关数据/delta4on_working4py_src/delta4on_working.1.git.txt


[[[
===

:r !date +@\%Y\%m\%d
news:
  @20250409
  gdry_run
    git add -nA
    git add --dry-run --all
  gdry_run


test:
  gdry_run >> /sdcard/0my_files/tmp/0tmp-git_add_nA-$(date +\%Y\%m\%d_\%H\%M\%S).txt
  _nm=txt_phone; cd $my_git_txt; _tm=$(date +\%Y\%m\%d_\%H\%M\%S); _tmp_opath=../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-$_nm-$_tm.txt; echo $_tmp_opath

_nm=txt_phone; cd $my_git_txt; _tm=$(date +\%Y\%m\%d_\%H\%M\%S); _tmp_opath=../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-$_nm-$_tm.txt; echo $_tmp_opath ; echo $_tmp_opath >> $_tmp_opath ; gdry_run >> $_tmp_opath ;
_nm=py_src; cd $my_git_py; _tm=$(date +\%Y\%m\%d_\%H\%M\%S); _tmp_opath=../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-$_nm-$_tm.txt; echo $_tmp_opath ; echo $_tmp_opath >> $_tmp_opath ; gdry_run >> $_tmp_opath ;

view /sdcard/0my_files/git_repos/python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20250409_113637.txt
view /sdcard/0my_files/git_repos/python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20250409_113817.txt
rm -iv '自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20250409_112315.txt'
rm -iv '自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20250409_112429.txt'

===
view ../../python3_src/bash_script/gss/export/gdry_run
view ../../python3_src/bash_script/gss/export/g_both__dry_run
===
view ../.gitignore
===
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20250511_071704.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20250511_071708.txt
===
临时性排除:
xxx:add 'txt/script/对称多项式讠基表达.py'
xxx:add 'txt/script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt.tar.lzma'
  3.3M
xxx:add 'txt/script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt.tar.lzma'
  2.2M

===
临时性排除:
xxx:add 'seed/int_tools/digits/codecs4int.py'
xxx:add 'seed/io/cache_file/README.txt'
xxx:add 'seed/recognize/rgnr/abc/IRecognizer.py'
xxx:add 'seed/recognize/rgnr/abc/utilities4IRecognizer.py'
===


]]]
[[
@20250615
g_both__dry_run
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20250615_130016.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20250615_130012.txt
===
允许:add 'seed/int_tools/digits/codecs4int.py'
临时性排除:py,txt:其余同上
===

]]
[[
@20250703
g_both__dry_run
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20250703_124228.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20250703_124232.txt
===
将允许:add 'seed/recognize/rgnr/abc/IRecognizer.py'
临时性排除:py,txt:其余同上
===
???出错:
  g6_ '我的思考牜大脑机制-灵感泉涌-随机记忘 <= 笔记:《系统方法谈》,《大脑如何思维》'
    导致后台运行并可能有其他毛病...

]]
[[
@20250810
g_both__dry_run
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20250810_102618.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20250810_102622.txt
===
临时性排除:py,txt:同上
xxx:add 'seed/io/cache_file/README.txt'
xxx:add 'seed/recognize/rgnr/abc/utilities4IRecognizer.py'

xxx:add 'txt/script/对称多项式讠基表达.py'
xxx:add 'txt/script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt.tar.lzma'
xxx:add 'txt/script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt.tar.lzma'
===

]]
[[
@20251011
g_both__dry_run
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20251011_075113.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20251011_075117.txt
git add 自己的相关数据/delta4on_working4py_src/README-cmds.txt
===
临时性排除:py,txt:同上

]]
[[
@20251102
g_both__dry_run
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20251102_160203.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20251102_160205.txt
===
临时性排除:py,txt:同上

]]
[[
@20251105
g_both__dry_run
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20251105_092914.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20251105_092918.txt
===
临时性排除:py,txt:同上
]]
[[
@20260228
g_both__dry_run
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20260228_213447.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20260228_213451.txt
===
临时性排除:py,txt:同上
xxx:add 'seed/io/cache_file/README.txt'
xxx:add 'seed/recognize/rgnr/abc/utilities4IRecognizer.py'

xxx:add 'txt/script/对称多项式讠基表达.py'
xxx:add 'txt/script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt.tar.lzma'
xxx:add 'txt/script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt.tar.lzma'
排除许多:add txt/script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..*
xxx:add 'txt/script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.le20.未曾数值校验.out.txt'
===
cat5mv__myfiles -f cat5mv__myfiles.conf
===
'txt/cat5mv__myfiles.conf'
'lots/NOTE/cryptography-book/Introduction to Modern Cryptography(2th)(2015)(Jonathan Katz)(Yehuda Lindell).txt'
'seed/recognize/step_recognizer/IStepRecognizer.py'

===
g6_ 'seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain__doc__py_adhoc_call.py;search_star_chain7recursive_shortest.py;shortest_addition_chain__arbitrary_recur_shortest_stem.py..址距溟次形式纟任意纟递归婪溟链.ge38039.le70070.txt.tar.lzma;对称多项式讠基表达.py;input7timeout.py;finger_tree/ft23_7sized_seq.py;ft23_7sized_ascend_set;txz;int_repr7human;int_repr7compact;'


]]
[[
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20260324_011455.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20260324_011500.txt

g6_ 'seed/helper/lazy_import__func7dict.py;seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py;seed/recognize/text_recognizer/ITextRecognizer.py'
]]
[[
e ../../python3_src/seed/helper/import_stmt_context7collect.py
e ../../python3_src/seed/helper/import_stmt_context7collect.py.excluded_paths.txt
==>>:
添加:__all___;___delta_all___;__this_is_forwarding_module___
==>>:
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20260406_133315.txt
]]
[[
tiny --> tiny_.xxx
floor_ceil --> floor_ceil_tools.xxx
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-txt_phone-20260521_093907.txt
view ../../python3_src/自己的相关数据/delta4on_working4py_src/git_add_nA-py_src-20260521_093912.txt
TODO: 'txt/others/数学/prime/APR_primality_test.txt'
]]


'自己的相关数据/delta4on_working4py_src/README-cmds.txt'



