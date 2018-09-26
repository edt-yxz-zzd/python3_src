goto start

rem query zeng ma
rem grep %* E:\my_data\program_output\py3\nn_ns\char\char2zm\str_char2zm_ls.txt
rem cat E:\my_data\program_output\py3\nn_ns\char\char2zm\str_char2zm_ls.txt | grep %* -

:start
py -m nn_ns.char.query_zm -e gb18030 -d E:\my_data\program_output\py3\nn_ns\char\char2zm\str_char2zm_ls.txt %*
