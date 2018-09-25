call set_JAVA_SRC_ROOT
call jc_all nn_ns.txt.IncrementalTextEditor -cp %JAVA_SRC_ROOT% -v
set ERRORLEVEL=&&if %ERRORLEVEL% EQU 0 call mk_jar executable -ep nn_ns.txt.IncrementalTextEditor -cp %JAVA_SRC_ROOT% -v

