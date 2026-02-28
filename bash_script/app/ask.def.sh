
: <<'EOF__USAGE'
USAGE:
# source GUARD4INCLUDE.def.sh
# include7guarded_ ask.def.sh
  # source ask.def.sh

see also:
  man dialog
    dialog - display dialog boxes from shell scripts
      dialog --yesno 'y/n?' 0 0 ; echo $?
        #蓝屏图形对话框 而非 『read -p』
    ===对话框类型:29
    buildlist
    calendar
    checklist
    dselect
    editbox
    form
    fselect
    gauge
    infobox
    inputbox
    inputmenu
    menu
    mixedform
    mixedgauge
    msgbox (message)
    passwordbox
    passwordform
    pause
    prgbox
    programbox
    progressbox
    radiolist
    rangebox
    tailbox
    tailboxbg
    textbox
    timebox
    treeview
    yesno (yes/no)
    ===end:对话框类型
EOF__USAGE



function ask_YN_
{
  [[ $# -eq 1 ]] || { echo "not [num_args==1]" ; return 11 ; }
      # no: 『>&2』

  local ANSWER
  while read -n 1 -r -p "$1" ANSWER ; do
    case "$ANSWER" in
      (y|Y)
        echo YES
        return 0
        ;;
      (n|N)
        echo NO
        return 0
        ;;
    esac
    echo >&2 "bad ANSWER: ${ANSWER@Q}"
  done
  echo EOF
  return 22
}
export -f ask_YN_
