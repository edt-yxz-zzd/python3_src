
e ../../python3_src/nn_ns/app/crypt/README_cmds.txt
[[
@20260311
密码丢失:
    view ../../python3_src/nn_ns/app/crypt/psw v4.txt
==>>:
重新加密:
py -m nn_ns.app.crypt encrypt -i {网站注册密码文件} -o ../../python3_src/nn_ns/app/crypt/psw-v4-20260311.txt {加密密码}
    #网站注册密码文件:格式:jsrc.cn hh psw:zs
    #加密密码:格式:regex"[0-9a-f]{9}"
py -m nn_ns.app.crypt decrypt -i ../../python3_src/nn_ns/app/crypt/psw-v4-20260311.txt {加密密码}
view ../../python3_src/nn_ns/app/crypt/psw-v4-20260311.txt
]]


