call jc_all nn_ns.txt.IncrementalTextEditor -cp . -v
set ERRORLEVEL=&&if %ERRORLEVEL% EQU 0 call mk_jar executable -ep nn_ns.txt.IncrementalTextEditor -cp . -v

