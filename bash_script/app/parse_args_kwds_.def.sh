

#########
: <<'EOF__format'
FORMAT:


input ::= (option | flag | boxed_arg)* ("--" raw_arg*)?

option ::= (-- | \+\+ | [+-]) keyword ((%\+)? boxed_arg | %-)
flag ::= [+-] keyword
  #flag value be 『+』or『-』
keyword ::= [\w.] [\w.+-]*
boxed_arg ::= [:=] raw_arg
raw_arg ::= .*



EOF__format
#########


#########
: <<'EOF__usage'
USAGE:

source GUARD4INCLUDE.def.sh
include7guarded_ parse_args_kwds_.def.sh
unset args kwds
declare -a args=()
declare -A kwds=()
parse_args_kwds_ ':' args kwds "$@"
[[ $? -eq 0 ]] || exit 1

for arg in "${args[@]}" ; do
  if [[ -v kwds["xxx"] ]] ; then
    case ${kwds["xxx"]} in
        (+) : ;;
        (-) : ;;
        (*) : ;;
    esac
  else
    :
  fi
done






see also:
  parse_options_
  parse_args_kwds_
  getopt
  getopts
  ===
  view ../../python3_src/bash_script/app/parse_options_.def.sh

  view ../../python3_src/bash_script/app/parse_args_kwds_.def.sh

  view others/app/termux/help/getopt.man.txt
    less ~/../usr/share/doc/util-linux/getopt-example.bash
    view others/app/termux/help/getopt-example.bash@usr-share-doc-util-linux.txt

  view others/app/termux/help/help.glob-pattern-star.txt
    getopts
    view others/app/termux/help/getopts.help.txt



EOF__usage
#########

#########
: <<'EOF__test'


#########
#setup:
#########
source GUARD4INCLUDE.def.sh
reload7unguarded_ parse_args_kwds_.def.sh

include7guarded_ parse_args_kwds_.def.sh
unset args kwds

#########
parse_args_kwds_
# missing 3 positional parameters: delimiter nm8args nm8kwds
echo $?
# 4

#########
declare -a args=()
declare -A kwds=()
parse_args_kwds_ : args kwds ab
# FormatError:not match regex'^(--|(--|[+][+])${word_pattern}((%[+])?[:=].*|%-)|[+-]${word_pattern}|[:=].*)$': 'ab'
echo $?
# 1


#########
declare -a args=()
declare -A kwds=()
parse_args_kwds_ : args kwds -- a b
echo $? ; declare -p kwds args
# 0
# declare -A kwds=()
# declare -a args=([0]="a" [1]="b")


#########
declare -a args=()
declare -A kwds=( [a]=... )
parse_args_kwds_ : args kwds -ab -- a b
echo $? ; declare -p kwds args
# 0
# declare -A kwds=([ab]="-" [a]="..." )
# declare -a args=([0]="a" [1]="b")

#########
declare -a args=()
declare -A kwds=( [ab]=... )
parse_args_kwds_ : args kwds -ab
echo $? ; declare -p kwds args
# 0
# declare -A kwds=([ab]="-" )
# declare -a args=()

#########
declare -a args=()
declare -A kwds=( [ab]=... )
parse_args_kwds_ : args kwds +ab
echo $? ; declare -p kwds args
# 0
# declare -A kwds=([ab]="+" )
# declare -a args=()

#########
declare -a args=()
declare -A kwds=()
parse_args_kwds_ : args kwds :'\x36' ='\x39'
echo $? ; declare -p kwds args
# 0
# declare -A kwds=()
# declare -a args=([0]="\\x36" [1]="9")


#########
declare -a args=()
declare -A kwds=( [23]=... [ab]=... [xy]=... )
parse_args_kwds_ : args kwds --ab%- ++xy%-
echo $? ; declare -p kwds args
# 0
# declare -A kwds=([23]="..." )
# declare -a args=()

#########
declare -a args=()
declare -A kwds=( [ab]=... [xy]=... )
parse_args_kwds_ : args kwds --ab:'\x36' --xy='\x39'
echo $? ; declare -p kwds args
# 0
# declare -A kwds=([ab]="\\x36" [xy]="9" )
# declare -a args=()

#########
declare -a args=()
declare -A kwds=( [ab]=... [xy]=... )
parse_args_kwds_ : args kwds ++ab:'\x36' ++xy='\x39'
echo $? ; declare -p kwds args
# 0
# declare -A kwds=([ab]="...:\\x36" [xy]="...:9" )
# declare -a args=()

#########
declare -a args=()
declare -A kwds=( [ab]=... [xy]=... )
parse_args_kwds_ : args kwds --ab%+:'\x36' --xy%+='\x39'
echo $? ; declare -p kwds args
# 0
# declare -A kwds=([ab]="...\\x36" [xy]="...9" )
# declare -a args=()

#########
declare -a args=()
declare -A kwds=( [ab]=... [xy]=... )
parse_args_kwds_ : args kwds ++ab%+:'\x36' ++xy%+='\x39'
echo $? ; declare -p kwds args
# 0
# declare -A kwds=([ab]="...\\x36" [xy]="...9" )
# declare -a args=()






#########
unset kk
declare -a kk=()
declare -A kk=()
# bash: kk: cannot convert indexed to associative array
unset kk

#########
declare -a aa=()
declare -A kk=()
parse_args_kwds_ : aa kk   :'a0\n' -x +y  ='b1\t' --z:zz ++a:b ++a:c :c2 --uuu=nnn ++uuu%- --z%+=z -- d3 f4
echo $? ; declare -p aa kk
# 0
# declare -a aa=([0]="a0\\n" [1]=$'b1\t' [2]="c2" [3]="d3" [4]="f4")
# declare -A kk=([z]="zzz" [y]="+" [x]="-" [a]="b:c" )

EOF__test
#########


#########

#################
# move from: echo7safe.def.sh
source GUARD4INCLUDE.def.sh
include7guarded_ echo7safe.def.sh




#################
#debug
#################
#shopt -s extglob
#export -f parse_args_kwds_
    #########
    # bash -c ''
    #########
        # bash: parse_args_kwds_: line 41: syntax error near unexpected token `('
        # bash: parse_args_kwds_: line 41: ` @(--|++)[^%:=+-]*([^%:=])?(%+)[:=]*)'
        # bash: error importing function definition for `parse_args_kwds_'
        #
    #########
    # bash -O extglob  -c '' #ok
    #########
        #   xxx:alias 'bash=bash -O extglob'
        #   xxx:export extglob
        #   xxx:set extglob
        #   xxx:function bash () { bash -O extglob "$@" ; }
        #
#################

function _parse_arg_
{
  case "$1" in
    (:*)
      show7safe "${1:1}"
      ;;
    (=*)
      concat_then_unescape7safe "${1:1}"
      ;;
    (*)
      print_err "not startswith [:=]: ${1@Q}"
      return 1
      ;;
  esac
  return 0
}

#shopt -p | grep ' -s' >&2
#.fff(){
#.  case ++kw%+:vv in
#.    (++|+|-)
#.      echo ...
#.      ;;
#.    (@(--|++)[^%:=+-]*([^%:=])?(%+)[:=]*)
#.      echo ok
#.      ;;&
#.    (@(--|++)[^%:=+-]*([^%:=])%+[:=]*)
#.      echo ok2
#.      ;;
#.  esac
#.}

function parse_args_kwds_
{
  [[ $# -ge 3 ]] || { print_err 'missing 3 positional parameters: delimiter nm8args nm8kwds' ; return 4 ; }
  local delimiter="$1"
  local nm8args="$2"
  local nm8kwds="$3"
      shift 3

  #declare -g -a "$nm8args"  || return 5
  #declare -g -A "$nm8kwds"  || return 5
      #global vars

  [ args == "$nm8args" ] || local -n args="$nm8args"
  [ kwds == "$nm8kwds" ] || local -n kwds="$nm8kwds"
      #nameref

  local arg
  local _key
  local key
  local payload
  local head_char_rng='[:alnum:]_.'
  local body_char_rng="${head_char_rng}+-"
  local word_pattern="[${head_char_rng}][${body_char_rng}]*"
      # bash: d['']: bad array subscript
  local pattern="^(--|(--|[+][+])${word_pattern}((%[+])?[:=].*|%-)|[+-]${word_pattern}|[:=].*)$"
      #view others/app/termux/shell_conditional-string-and_var.txt

  for arg ; do
    shift
    if [[ ! "${arg}" =~ ${pattern} ]] ; then
        #not 『=~ "${pattern}"』
      print_err "FormatError:not match regex${pattern@Q}: ${arg@Q}"
      return 1
    fi
    case "$arg" in
      ([:=]*)
        args[${#args[@]}]="$(_parse_arg_ "${arg}")"
        :   #ok: "$(cmd "${xx}")" since 『$()』
        if [ $? -ne 0 ] ; then
          print_err "LogicError: ${arg@Q}"
          return 1
        fi
        ;;
      #. (-)
      #.   args[${#args[@]}]='-'
      #.       #STDIN
      #.   ;;
      (--)
        break
        ;;
      (++|+|-)
        print_err "LogicError: ${arg@Q}"
        # bash: d['']: bad array subscript
        print_err "NotImplementedError: ${arg@Q}"
        return 1
        ;;
      # (@(--|++)?*[:=]*)
      # (--?*[:=]*|++?*[:=]*)
      (@(--|++)[^%:=+-]*([^%:=])?(%+)[:=]*)
        #bug:[^+-%:=]
        #   fixed: --> [^%:=+-]
        #bug:_key="${arg/[:=]*/}"
        _key="${arg%%[:=]*}"
        ###test err:
        payload="$(_parse_arg_ "${arg:${#_key}}")"
        if [ $? -ne 0 ] ; then
          print_err "LogicError: ${arg@Q}"
          #print_err "FormatError:not match regex'(++|--).*[:=].*': ${arg@Q}"
          return 1
        fi
        #bug:if [[ "${_key:-2:2}" == '%+' ]] ; then
          # !! 『:-』${parameter:-word} Use Default Values.
          # => insert space
        if [[ "${_key: -2}" == '%+' ]] ; then
        #ok:if [[ "${_key:${#_key}-2:2}" == '%+' ]] ; then
          key="${_key:2: -2}"
        else
          key="${_key:2}"
        fi
        ;;&
      (@(--|++)[^%:=+-]*([^%:=])%+[:=]*)
        #xxx:kwds["${key}"]+="${delimiter}${payload}"
        kwds["${key}"]+="${payload}"
        ;;
      (--[^%:=+-]*([^%:=])[:=]*)
      # (--?*[:=]*)
        kwds["${key}"]="${payload}"
        ;;
      (++[^%:=+-]*([^%:=])[:=]*)
      # (++?*[:=]*)
        #useless:${parameter:+word}
        # if [ -n "${kwds["${key}"]@Q}" ] ; then
        if has_key_ "${key}" kwds ; then
          kwds["${key}"]+="${delimiter}${payload}"
        else
          kwds["${key}"]="${payload}"
        fi
        ;;
      (@(--|++)[^%:=+-]*([^%:=])%-)
      # (@(--|++)?*%-)
      # (--?*%-|++?*%-)
        key="${arg:2: -2}"
        unset kwds["${key}"]
        ;;
      #. ([-+]*[^0-9A-Za-z_.+-]*)
      #.   print_err "LogicError: ${arg@Q}"
      #.   return 1
      #.  ;;
      ([+-][^%:=+-]*([^%:=]))
      # ([+-][^+-]*)
        payload="${arg:0:1}"
        key="${arg:1}"
        kwds["${key}"]="${payload}"
        ;;
      (*)
        print_err "LogicError: ${arg@Q}"
        #.print_err "FormatError:not match regex'[-+:=].*': ${arg@Q}"
        return 1
        ;;
    esac
  done

  #come from "(--) break"
  for arg ; do
    shift
    args[${#args[@]}]="${arg}"
  done
  #.local -p args kwds
  #.declare -p "$nm8args"
  #.declare -p "$nm8kwds"
  return 0
}

