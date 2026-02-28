
: <<'EOF__usage'
USAGE

source GUARD4INCLUDE.def.sh
include7guarded_ echo7safe.def.sh

EOF__usage



: <<'EOF__note'
#################
#import: 『. echo7safe.def.sh』
#import: 『source echo7safe.def.sh』
#################

e ../../python3_src/bash_script/app/echo7safe.def.sh
   mv -iv $my_git_sh/app/echo7safe $my_git_sh/app/echo7safe.def.sh
   rm -iv ../../python3_src/bash_script/my_sh/echo7safe
   rm -iv $my_sh/echo7safe

view ../../python3_src/bash_script/app/echo_result.def.sh
   mv -iv $my_git_sh/app/echo_result $my_git_sh/app/echo_result.def.sh
   rm -iv ../../python3_src/bash_script/my_sh/echo_result
   rm -iv $my_sh/echo_result

view ../../python3_src/bash_script/app/print_err.def.sh
   mv -iv $my_git_sh/app/print_err $my_git_sh/app/print_err.def.sh
   rm -iv ../../python3_src/bash_script/my_sh/print_err
   rm -iv $my_sh/print_err








show_args__via_AT_double_quote a 'b   b' $'\n' '"\\"'   '\n'
    a
    b   b
    <BLANK>
    <BLANK>
    "\\"
    \n
show_args__via_STAR_double_quote a 'b   b' $'\n' '"\\"'   '\n'
    a b   b
     "\\" \n
      #『 "\\"』

show_args__via_AT_without_quote a 'b   b' $'\n' '"\\"'   '\n'
    a
    b
    b
    "\\"
    \n
show_args__via_STAR_without_quote a 'b   b' $'\n' '"\\"'   '\n'
    a
    b
    b
    "\\"
    \n



args2quoted__via_AT_double_quote a 'b   b' $'\n' '"\\"'   '\n'
  'a' 'b   b' $'\n' '"\\"' '\n'
args2quoted__via_STAR_double_quote a 'b   b' $'\n' '"\\"'   '\n'
  $'a b   b \n "\\\\" \\n'

args2quoted__via_AT_without_quote a 'b   b' $'\n' '"\\"'   '\n'
  'a' 'b' 'b' '"\\"' '\n'
args2quoted__via_STAR_without_quote a 'b   b' $'\n' '"\\"'   '\n'
  'a' 'b' 'b' '"\\"' '\n'


EOF__note

function set_result
{
  return "$@"
  #not:return "$1" => err if too many args
}

function echo_result
{
  echo7safe $?
}
#old_ver:
#.function echo_result
#.{
#.  local x=$?
#.  echo $x
#.  return $x
#.  #ok if too many args
#.}



function safe_run
{
  local x=$?
  #bug:eval "${@}"
      #bug:same as above:eval "${*}"
  "${@}" #ok: ';'
  return $x
}
function printf7safe
{
  safe_run printf "$@"
}
#old_ver:
#.function printf7safe
#.{
#.  local x=$?
#.  printf "$@"
#.  return $x
#.}
function show7safe
{
  printf7safe '%s' "$*"
}
function echo7safe
{
  printf7safe '%s\n' "$*"
}
function echo_args__one_by_one7safe
{
  #local IFS=$'\n'
  printf7safe '%s\n' "$@"
}
#old_ver:
#.function echo7safe
#.{
#.  local x=$?
#.  #echo -E '' "$@"
#.  #  output leading spaces
#.  printf '%s\n' "$*"
#.  return $x
#.}



function printf_err7safe
{
  printf7safe 1>&2 "$@"
}
function show_err7safe
{
  show7safe 1>&2 "$@"
}
function echo_err7safe
{
  echo7safe 1>&2 "$@"
}
function leave_errmsg_
{
  echo_err7safe "$@"
  exit
}
function if_err_
{
  #eg: if_err_ leave_errmsg_ 'wrong'
  local x=$?
  if [[ "${x}" -ne 0 ]] ; then
    set_result "${x}"
    "${@}" #ok: ';'
  else
    set_result "${x}"
  fi
  return
  #xxx:return $x
}

#.alias print_err7safe=echo_err7safe
alias print_err=echo_err7safe
#.export -f print_err
  #bash: export: print_err: not a function
function print_err7quoted
{
  print_err "${@@Q}"
}


function concat_then_unescape7safe
{
  #show7safe "${*@E}"
  #<==>:
  printf7safe '%b' "$*"
}
function concat_then_quote7safe
{
  #bug:show7safe "${*@Q}"
  #     <==>show7safe "${@@Q}"
  printf7safe '%q' "$*"
  #vs:args2quoted7safe
}

function args2quoted7safe
{
  echo7safe "${@@Q}"
  #vs:concat_then_quote7safe
  #vs:args2quoted
}
function args2quoted
{
  args2quoted7safe "$@"
  return 0
  #vs:args2quoted7safe
}


function args2quoted__via_AT_double_quote
{
  args2quoted7safe "$@"
  return 0
  #===args2quoted
  #vs:show_args__via_AT_double_quote
}

function args2quoted__via_STAR_double_quote
{
  args2quoted7safe "$*"
  return 0
  #vs:args2quoted__via_AT_double_quote
}

function args2quoted__via_AT_without_quote
{
  args2quoted7safe $@
  return 0
  #vs:args2quoted__via_AT_double_quote
}

function args2quoted__via_STAR_without_quote
{
  args2quoted7safe $*
  return 0
  #vs:args2quoted__via_AT_double_quote
}

function show_args__via_AT_double_quote
{
  echo_args__one_by_one7safe "$@"
  return 0
  #vs:args2quoted
}

function show_args__via_STAR_double_quote
{
  echo_args__one_by_one7safe "$*"
  return 0
  #vs:show_args__via_AT_double_quote
}

function show_args__via_STAR_without_quote
{
  echo_args__one_by_one7safe $*
  return 0
  #vs:show_args__via_STAR_double_quote
}

function show_args__via_AT_without_quote
{
  echo_args__one_by_one7safe $@
  return 0
  #=?=show_args__via_STAR_without_quote
}



function has_key_
{
  local key="$1"
  local nm8kwds="$2"
  [ kwds == "$nm8kwds" ] || local -n kwds="$nm8kwds"
  #ok: [ -n "${kwds["${key}"]@Q}" ]
  [[ -v kwds["${key}"] ]]
}

export -f args2quoted7safe args2quoted
export -f print_err7quoted leave_errmsg_
#.export -f print_err
  #bash: export: print_err: not a function
export -f echo7safe echo_result set_result


#bug:不能继承『$?』
#.  x=$?
#.  echo -E '' "$@"
#.  exit $x

#see: args2quoted, set_result
#see-renamed:print_err.def.sh, echo_result.def.sh
        #bug:『echo_result』/『eval echo_result』/『bash $my_git_sh/app/echo_result』 并不能继承『$?』
        #   必须:『. $my_git_sh/app/echo_result』/『source $my_git_sh/app/echo_result』，但这样一来，就不能用『exit $x』
#leave_errmsg_



#THIS="$my_git_sh/app/echo7safe.def.sh" ; sed -n 's/^function \([[:alpha:]]\w*\)/export -f \1/p' "$THIS" >>  "$THIS"
#.export -f parse_args_kwds_
  # !! 『case』使用的 模板 需要 -O extglob


export -f set_result
export -f echo_result
export -f safe_run
export -f printf7safe
export -f show7safe
export -f echo7safe
export -f printf_err7safe
export -f show_err7safe
export -f echo_err7safe
export -f leave_errmsg_
export -f if_err_
export -f print_err7quoted
export -f concat_then_unescape7safe
export -f concat_then_quote7safe
export -f args2quoted7safe
export -f args2quoted
export -f show_args__via_AT_double_quote
export -f show_args__via_AT_without_quote
export -f show_args__via_STAR_double_quote
export -f show_args__via_STAR_without_quote
export -f args2quoted__via_AT_double_quote
export -f args2quoted__via_AT_without_quote
export -f args2quoted__via_STAR_double_quote
export -f args2quoted__via_STAR_without_quote
export -f has_key_
