:set_haskell8
rem SHOULD set this file after "set_mingw.bat" 
rem since haskell comes with its mingw


set "haskell_home=C:\Program Files\Haskell Platform\8.0.2\"
rem set haskell_admin_home=C:\Program Files (x86)\Haskell\
rem set haskell_prev_path=%haskell_admin_home%\bin;%haskell_home%\lib\extralibs\bin;%haskell_home%\bin;
rem set haskell_succ_path=%haskell_home%\mingw\bin
set "haskell_Roaming=C:\Users\Administrator\AppData\Roaming"

goto end_of_comment
    Administrator user var/path
        C:\Users\Administrator\AppData\Roaming\cabal\bin;
        C:\Users\Administrator\AppData\Roaming\local\bin
    system var/path
        C:\Program Files\Haskell\bin;
        C:\Program Files\Haskell Platform\8.0.2\lib\extralibs\bin;
        C:\Program Files\Haskell Platform\8.0.2\bin;
        // original: C:\ProgramData\Oracle\Java\javapath;C:\Program Files\ImageMagick-6.8.9-Q8;C:\Program Files\ImageMagick-6.8.9-Q16;D:\software\programming\library\boost\boost_1_55_0\binary_lib\x86_64_py33\lib;c:\python33;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\Microsoft Windows Performance Toolkit\;C:\Program Files (x86)\Subversion\bin;
        C:\Program Files\Haskell Platform\8.0.2\mingw\bin

    ghci env/path -- exec ":! set" under ghci
        Path=
            C:\Program Files\Haskell\bin;
            C:\Program Files\Haskell Platform\8.0.2\lib\extralibs\bin;
            C:\Program Files\Haskell Platform\8.0.2\bin;
            // original: C:\ProgramData\Oracle\Java\javapath;C:\Program Files\ImageMagick-6.8.9-Q8;C:\Program Files\ImageMagick-6.8.9-Q16;D:\software\programming\library\boost\boost_1_55_0\binary_lib\x86_64_py33\lib;c:\python33;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files\Microsoft Windows Performance Toolkit\;C:\Program Files (x86)\Subversion\bin;
            C:\Program Files\Haskell Platform\8.0.2\mingw\bin;
            C:\Users\Administrator\AppData\Roaming\cabal\bin;
            C:\Users\Administrator\AppData\Roaming\local\bin
:end_of_comment
rem set path=%haskell_prev_path%;%path%;%haskell_succ_path%
rem set haskell_bins=%haskell_home%\bin;%haskell_home%\lib\bin;%haskell_home%\lib\extralibs\bin;%haskell_home%\mingw\bin;%haskell_home%\mingw\x86_64-w64-mingw32\bin;%haskell_home%\msys\usr\bin
set "haskell_bins_prev=%haskell_home%\lib\extralibs\bin;%haskell_home%\bin"

set "haskell_bins_succ=%haskell_home%\mingw\bin;%haskell_Roaming%\cabal\bin;%haskell_Roaming%\local\bin"
set "path=%haskell_bins_prev%;%path%;%haskell_bins_succ%"
rem call "C:\Program Files\Haskell Platform\8.0.2\msys\msys2_shell.cmd"





