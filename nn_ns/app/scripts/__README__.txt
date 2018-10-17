

<path to python3_src>/nn_ns/app/scripts/
    *.exe_py
        # .exe_py instead of .py
        #   "double-click .py" will open it
        #   "double-click .exe_py" will run it
        # see:
        #   "windows_bat/set_path/let_exe_py_file_executable.bat"
        #       assoc .exe_py="executable python script"
        #       ftype "executable python script"=py "%1" %*

add this_folder to %PATH%
    since add to %PATH%, this_folder will occur in sys.path

    # ignore below
    may add this_folder to sys.path by:
    >cat C:/Python33/Lib/site-packages/my_py3src.pth
        E:/my_data/program_source/python3_src
        E:/my_data/program_source/python3_src/nn_ns/app/scripts

may add ".exe_py" to %PATHEXT%
    # hence we can call "XXX ..." instead of "XXX.exe_py ..."
    or use bash:"alias" or dos:"doskey"

# NO!!!
#   it is non-sense to import ".exe_py" file
#   if needed:
#       then move "nn_ns/app/scripts/XXX.exe_py" into "nn_ns/app/XXX.py"
#       then create new XXX.exe_py to call XXX.py
may add ".exe_py" to "importlib.machinery.SOURCE_SUFFIXES"
    # hence we can "import nn_ns.app.scripts.XXX" if exists "XXX.exe_py"
    now add it in "nn_ns.app.scripts.__init__"
    now exec "import nn_ns.app.scripts" at startup
        see: "nn_ns.app.scripts.__startup__register__exe_py__"

may set gvim syntax coloring for ".exe_py"
    C:\Program Files (x86)\Vim\vimfiles\ftdetect\exe_python.vim/
        au BufRead,BufNewFile *.exe_py      set filetype=python


from seed.exec.ShellCmd.GNU_Cmd         import GNU_Cmd
from seed.exec.ShellCmd.CallSetting     import CallSetting
from seed.exec.ShellCmd.CallTheShellCmd import CallTheShellCmd
from seed.exec.ShellCmd.ToCallTheShellCmd import ToCallTheShellCmd
from subprocess import CalledProcessError, CompletedProcess, PIPE, STDOUT, DEVNULL


