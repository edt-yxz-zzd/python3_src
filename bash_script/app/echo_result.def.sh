#usage: source echo_result.def.sh

#usage: source $my_git_sh/app/echo_result.def.sh

#e ../../python3_src/bash_script/app/echo_result.def.sh
#   mv -iv $my_git_sh/app/echo_result $my_git_sh/app/echo_result.def.sh
#   rm -iv ../../python3_src/bash_script/my_sh/echo_result
#   rm -iv $my_sh/echo_result


#.declare -p PIPESTATUS
# PIPESTATUS is useless here
#   <<== view others/app/termux/shell_env.txt
if ! : ; then
  : | : ; declare -p PIPESTATUS
  : | : ; echo ${PIPESTATUS[@]@Q}
  : | : ; echo ${PIPESTATUS[@]@A}
  : | : ; echo "${!PIPESTATUS[@]}"
  : | : ; echo ${#PIPESTATUS[@]}
fi

source echo7safe.def.sh
  #.  function echo_result
  #.  {
  #.    x=$?
  #.    echo $x
  #.    return $x
  #.  }




#bug:『echo_result』/『eval echo_result』/『bash $my_git_sh/app/echo_result』 并不能继承『$?』
#   必须:『. $my_git_sh/app/echo_result』/『source $my_git_sh/app/echo_result』，但这样一来，就不能用『exit $x』
#.if false ; then
#.  x=$?
#.  echo $x
#.  exit $x
#.fi

#bug:echo $?
#   leaving $? be 0
#
