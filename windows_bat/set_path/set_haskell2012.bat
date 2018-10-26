:sethaskell
rem SHOULD set this file after "set_mingw.bat" 
rem since haskell comes with its mingw

set "haskell_home=D:\software\programming\Haskell Platform\2012.4.0.0\"
set "haskell_admin_home=C:\Program Files (x86)\Haskell\"
set "haskell_prev_path=%haskell_admin_home%\bin;%haskell_home%\lib\extralibs\bin;%haskell_home%\bin;"
set "haskell_succ_path=%haskell_home%\mingw\bin"



set "path=%haskell_prev_path%;%path%;%haskell_succ_path%"




