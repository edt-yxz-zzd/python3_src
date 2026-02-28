
#########
#usage
#########
#source GUARD4INCLUDE.def.sh
#include7guarded_ echo7safe.def.sh




#########
#defs
#########
#declare -g -x -i -A GUARD4INCLUDE
declare -g -i -A GUARD4INCLUDE
if [[ "${#GUARD4INCLUDE[@]}" -eq 0 ]] ; then

################
GUARD4INCLUDE['GUARD4INCLUDE.def.sh']=1
function include7guarded_
{
  #local _000_fname8cmd
  #for _000_fname8cmd ; do
  #  if [[ ! -n "${GUARD4INCLUDE["${_000_fname8cmd}"]}" ]] ; then
  #    source "${_000_fname8cmd}"
  #    GUARD4INCLUDE["${_000_fname8cmd}"]=1
  #  fi
  #done
  while [ $# -ne 0 ] ; do
    if [[ ! -n "${GUARD4INCLUDE["$1"]}" ]] ; then
      source "$1"
      GUARD4INCLUDE["$1"]=1
    fi
    shift
  done
}
function reload7unguarded_
{
  while [ $# -ne 0 ] ; do
    source "$1"
    GUARD4INCLUDE["$1"]=1
    shift
  done
}
export -f reload7unguarded_

export -f include7guarded_
################

fi
#########
#end:defs
#########
