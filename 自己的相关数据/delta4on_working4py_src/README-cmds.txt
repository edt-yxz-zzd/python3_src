
e ../../python3_src/自己的相关数据/delta4on_working4py_src/README-cmds.txt


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
]]]
