
exit_status=0
for hex ; do
  if [[ "${#hex}" -gt 8 ]] ; then
    echo >&2 "arg too long: ${hex@Q}"
    exit_status=1
  elif ! [[ "${hex}" =~ ^[[:xdigit:]]{0,8}$ ]] ; then
    echo >&2 "arg is not hex: ${hex@Q}"
    exit_status=1
  #.elif ! [[ "${hex}" =~ ^0{0,8}$ ]] ; then
    #echo "$(printf '\x00')"
    #   => bash: warning: command substitution: ignored null byte in input
  else
    #ok:printf "\U$(printf %08s "${hex}")"
    u=\$\'"\U$(printf %08s "${hex}")"\'
    #fail:printf %s ${u}
    eval printf %s "${u}"
    #########
    #no:tailing newline
    # !! when single char...
    #########
  fi
done

exit "${exit_status}"

