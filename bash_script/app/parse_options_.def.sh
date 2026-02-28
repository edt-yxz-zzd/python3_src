
#e ../../python3_src/bash_script/app/parse_options_.def.sh
#view others/app/termux/shell-nameref.txt
#
#
#########
: <<'EOF__format'
FORMAT:

assume all options before args and terminated by 『--』
『--』is required
defaut value be 『+』or『-』

input ::= option* "--" arg*
option ::= (%%?\w+|(--|\+\+|[+-])\w+(:.*)?)

EOF__format
#########

#########
: <<'EOF__usage'
USAGE:

source GUARD4INCLUDE.def.sh
include7guarded_ parse_options_.def.sh
unset num_args7consumed kwds
declare -i num_args7consumed=0
declare -A kwds=()
parse_options_ num_args7consumed kwds "$@"
[[ $? -eq 0 ]] || exit 1
shift "$num_args7consumed"
for arg ; do
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
reload7unguarded_ parse_options_.def.sh

include7guarded_ parse_options_.def.sh
unset num_args7consumed kwds

#########
parse_options_
# missing 2 positional parameters: nm4num_args7consumed nm4kwds
echo $?
# 4

#########
declare -i num_args7consumed=0
declare -A kwds=( [a]=... )
parse_options_ num_args7consumed kwds ab
# FormatError: not match regex'^(--|%%?[_[:alnum:]]+|(--|\+\+|[+-])[_[:alnum:]]+(:.*)?)$': 'ab'
echo $?
# 1

#########
declare -i num_args7consumed=0
declare -A kwds=( [a]=... )
parse_options_ num_args7consumed kwds -ab
# missing "--"
echo $?
# 1


#########
declare -i num_args7consumed=0
declare -A kwds=( [a]=... )
parse_options_ num_args7consumed kwds -- ab
# 0
# declare -A kwds=([a]="..." )
# declare -i num_args7consumed="1"

#########
declare -i num_args7consumed=0
declare -A kwds=( [a]=... )
parse_options_ num_args7consumed kwds -ab --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([b]="-" [a]="-" )
# declare -i num_args7consumed="2"

#########
declare -i num_args7consumed=0
declare -A kwds=( [a]=... )
parse_options_ num_args7consumed kwds -ab:xxx --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([b]="xxx" [a]="xxx" )
# declare -i num_args7consumed="2"

#########
declare -i num_args7consumed=0
declare -A kwds=( [a]=... )
parse_options_ num_args7consumed kwds +ab --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([b]="+" [a]="+" )
# declare -i num_args7consumed="2"

#########
declare -i num_args7consumed=0
declare -A kwds=( [a]=... )
parse_options_ num_args7consumed kwds +ab:xxx --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([b]="xxx" [a]="...xxx" )
# declare -i num_args7consumed="2"


#########
declare -i num_args7consumed=0
declare -A kwds=( [y]=... [xy]=... )
parse_options_ num_args7consumed kwds %xy --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([xy]="..." )
# declare -i num_args7consumed="2"

#########
declare -i num_args7consumed=0
declare -A kwds=( [y]=... [xy]=... )
parse_options_ num_args7consumed kwds %%xy --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([y]="..." )
# declare -i num_args7consumed="2"

#########
declare -i num_args7consumed=0
declare -A kwds=( [xy]=... )
parse_options_ num_args7consumed kwds --xy --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([xy]="-" )
# declare -i num_args7consumed="2"

#########
declare -i num_args7consumed=0
declare -A kwds=( [xy]=... )
parse_options_ num_args7consumed kwds --xy:aaa --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([xy]="aaa" )
# declare -i num_args7consumed="2"

#########
declare -i num_args7consumed=0
declare -A kwds=( [xy]=... )
parse_options_ num_args7consumed kwds ++xy --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([xy]="+" )
# declare -i num_args7consumed="2"

#########
declare -i num_args7consumed=0
declare -A kwds=( [xy]=... )
parse_options_ num_args7consumed kwds ++xy:aaa --
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([xy]="...aaa" )
# declare -i num_args7consumed="2"







#########
declare -i num_args7consumed=0
declare -A kwds=()
parse_options_ num_args7consumed kwds -abcxyz +uvwxyz %zwc --k0 ++k1 --kx %%kx --k2:... --k2:111 ++k2:,222 +bvy:,/-/ -au:jjj -- xxx '' ' '
echo $? ; declare -p kwds num_args7consumed
# 0
# declare -A kwds=([y]="+,/-/" [x]="+" [v]="+,/-/" [u]="jjj" [b]="-,/-/" [a]="jjj" [k0]="-" [k1]="+" [k2]="111,222" )
# declare -i num_args7consumed="15"



EOF__test
#########


#declare -i PARSE_OPTIONS__CONSUMED_NUM_ARGS
#declare -A PARSE_OPTIONS__OUTPUT_DICT
function parse_options_()
{
  [[ $# -ge 2 ]] || { echo >&2 'missing 2 positional parameters: nm4num_args7consumed nm4kwds' ; return 4 ; }
  local nm8n="$1" #nm4num_args7consumed
  local nm8d="$2" #nm4kwds
      shift 2

  #bug:will be local
    #declare -I -i "$nm8n"  || return 5
    #declare -I -A "$nm8d"  || return 5
        #vars

  #declare
  [ n == "$nm8n" ] || local -n n="$nm8n"
  [ d == "$nm8d" ] || local -n d="$nm8d"
      #nameref


  #.#declare
  #.local -n n=PARSE_OPTIONS__CONSUMED_NUM_ARGS
  #.local -n d=PARSE_OPTIONS__OUTPUT_DICT
      #local -A -n d=PARSE_OPTIONS__OUTPUT_DICT
        #bash: local: d: reference variable cannot be an array
  local -i j
  local arg _key key _payload payload prefix k
  local pattern='^(--|%%?[_[:alnum:]]+|(--|\+\+|[+-])[_[:alnum:]]+(:.*)?)$'
  #let n=0
  #d=()
  for arg ; do
    let n++

    if [[ ! "$arg" =~ ${pattern} ]] ; then
      echo >&2 "FormatError: not match regex${pattern@Q}: ${arg@Q}"
      return 1
    fi

    case "$arg" in
      (--)
        return 0
        ;;
      (%%+([_[:alnum:]]))
        key="${arg:2}"
        unset d["${key}"]
        ;;
      (%+([_[:alnum:]]))
        for (( j=1 ; j < ${#arg} ; ++j )) ; do
          k="${arg:j:1}"
          unset d["${k}"]
        done
        ;;
      (@(--|++|[+-])+([_[:alnum:]])?(:*))
        _key="${arg%%:*}"
          # [+-][+-]?\w+
        _payload="${arg:${#_key}}"
          # (:.*)?
        key="${_key##+([+-])}"
          # \w+
        #prefix="${_key:0: "-${#key}"}"
        prefix="${_key%%+([^+-])}"
          # ++?|--?
        if [[ ${#_payload} -eq 0 ]] ; then
          # (:.*)?
          # $_payload == ''
          payload="${arg:0:1}"
            # [+-]
          prefix="${prefix//+/-}"
            # --?
        else
          # $_payload =~ :.*
          payload="${_payload:1}"
        fi
        # $payload =~ .*
        # $prefix =~ ++?|--?
        # $key =~ \w+
        case "${prefix}" in
          (--)
            d["${key}"]="${payload}"
            ;;
          (++)
            d["${key}"]+="${payload}"
            ;;
          ([+-])
            for (( j=0 ; j < ${#key} ; ++j )) ; do
              k="${key:j:1}"
              if [[ "${prefix}" == '+' ]] ; then
                d["${k}"]+="${payload}"
              else
                d["${k}"]="${payload}"
              fi
            done
            ;;
          (*)
            echo >&2 LOGIC ERROR
            return 9
            ;;
        esac
        ;;
      (*)
        echo >&2 LOGIC ERROR
        return 7
        ;;
    esac
  done
  echo >&2 'missing "--"'
  return 1
}
#export -f parse_options_
#   !! required 『shopt -s extglob』
#   !! required 『bash -O extglob』
