
#e ../../python3_src/bash_script/app/chr2hex.sh


declare -i sz j hex_sz
HEX=
succ=
for s ; do
  #bug:if [[ -n succ ]] ; then
  if [[ -n "${succ}" ]] ; then
    #printf "${succ@Q}"
    printf ' , '
  else
    succ=1
  fi
  sz="${#s}"
  for (( j=0 ; j < sz ; ++j )) ; do
    ch="${s:j:1}"
    [[ "${j}" -eq 0 ]] || printf ' : '
    #printf %X "'${ch}"
    printf -v HEX %X "'${ch}"
    hex_sz="${#HEX}"
    if [[ "${hex_sz}" -le 2 ]] ; then
      printf %02s "${HEX}"
    elif [[ "${hex_sz}" -le 4 ]] ; then
      printf %04s "${HEX}"
    elif [[ "${hex_sz}" -le 8 ]] ; then
      printf %08s "${HEX}"
    else
      echo >&2 LOGIC ERROR
      exit 1
    fi
  done
done

echo
exit

#test:
  #chr2hex.sh anc 一丁 $'\x01' $'\U00020000'
  # => 61 : 6E : 63 , 4E00 : 4E01 , 01 , 00020000

