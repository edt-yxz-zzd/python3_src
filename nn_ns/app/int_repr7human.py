r'''[[[
e ../../python3_src/nn_ns/app/int_repr7human.py

[[
e ../../python3_src/bash_script/app/int_repr7human
int_repr7human encode 7777
    YD7777
]]
%s/py -m seed.int_tools.int_repr7human7lex_order7alnum/int_repr7human
py -m nn_ns.app.int_repr7human
[[
int_repr7human encode 0 1 -1 999 -999 +11 -11 +7777 -7777
    W
    X1
    V8
    YC999
    UR000
    YB11
    US88
    YD7777
    UQ2222

int_repr7human decode W X1 V8 YC999 UR000 YB11 US88 YD7777 UQ2222
    0
    1
    -1
    999
    -999
    11
    -11
    7777
    -7777

int_repr7human xdecode  aaaUQ22220000bbb --begin 3 --end -3
    (-7777, 9)

int_repr7human xdecode  aaaUQ22220000bbb --begin 3 --end 8
    ^EOFError: (4, 3, b'\x07\x07\x07')
int_repr7human xdecode  aaaUQ22220000bbb --begin 3 --end 9
    (-7777, 9)

int_repr7human xdecode  aaaUQ22220000bbb --begin 3 --end 9 --strict
    -7777

int_repr7human xdecode  aaaUQ22220000bbb --begin 3 --end 10 --strict
    ^seed.int_tools.int_repr7lex_order7base.FormatError: ('0', 9, 10)

]]
]]]'''#'''
if 1:from seed.int_tools.int_repr7human7lex_order7alnum import _main_
if __name__ == '__main__':
    _main_()

