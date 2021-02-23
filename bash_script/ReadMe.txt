
=====
普通脚本 放在 python3_src/bash_script/app/

=====
自动化的目的:
由于 /sdcard/ 中的脚本不能直接运行，即『chmod +x xxx.sh』失败
  ，只能在 termux的 $HOME 即『~』文件夹下保存可执行脚本
    $my_git_sh
      脚本-用于同步保存到网络github
      两种：一是 工作脚本，一是 转发调用的脚本
      转发调用的脚本 调用 工作脚本
        ，并 被复制到 $my_sh
        ，对副本执行『chmod +x xxx.sh』
      工作脚本 手写（包括 那些 转发调用python模块的shell脚本）
      转发调用的脚本 自动生成
    $my_sh
      脚本-用于执行，只是转发调用
see: termux/apt_pkg.txt
  set up:
    $my_git_sh
    $my_sh


=====
自动化过程:
  bash $my_git_sh/gss/export/g_sh
  chmod +x $my_sh/*
  #######or########
  bash $my_git_sh/main_sh/ref_sh
      自动生成 转发调用的脚本
  cp -u -i -t $my_sh/ $my_git_sh/my_sh/*
      复制 转发调用的脚本
  chmod +x $my_sh/*
      对副本执行『chmod +x xxx.sh』


###############
###############文件夹结构

python3_src/bash_script/
  my_sh/
    输出文件夹
    用于保存 自动生成的 转发调用的脚本
    来源:
      执行:
        main_sh/ref_sh
      收集:
        main_sh/
        gss/export/
        app/
  main_sh/
    手写的 基础工作脚本 #基础-相对于bash_script/
    use python directly
    other directory can use py
    #####
    py
      python别名
    ref_sh
      自动生成 转发调用的脚本
  gss/export/
    手写的github相关工作脚本，g0~g7
    git helper sh
  app/
    +手写的 工作脚本
    +手写的 转发调用python模块的shell脚本
    普通脚本 直接往这里添加
    nn_ns.app
    ../windows_bat/
  py/
    一些python脚本，被shell工作脚本调用（非转发）
    py scripts
    since "ref_sh" forward all files of some directories, any files other than sh should not mix with sh
    #####
    git_output2utf8.py
      git将中文字符编码成八进制，这里还原之
      used in "g_out"
      convert regex"\\[0-7]{3}" to one byte
      git output path as f(path.encode('utf8'))
      where
        f bs = concat $ map g bs
        g b = chr(b) | fr"\\{b!0>3o}"
    gen_forwarding_sh.py
      生成 转发调用的脚本
      used in "ref_sh"
      since working sh store under /sdcard/... and "chmod +x" fail on them, we have to make forward call sh under ./my_sh/ and copy to $my_sh/

