
#
#e ../../python3_src/bash_script/app/print_err.def.sh
#   mv -iv $my_git_sh/app/print_err $my_git_sh/app/print_err.def.sh
#fail:how to exit parent shell?: e ../../python3_src/bash_script/app/leave_errmsg_
#   ??using alias??

source echo7safe.def.sh

#.#deprecate:2:『$?』 initial be 『0』
#.echo7safe 1>&2 "$@"
#.exit
#.
#.
#.#deprecate:1:
#.  [[ $# -eq 1 ]] || { print_err 'usage print_err <errmsg>' ; exit 11 ; }
#.
#.  echo 1>&2 '' "$1"
#.  exit 22
#.
