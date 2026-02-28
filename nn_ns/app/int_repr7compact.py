r'''[[[
e ../../python3_src/nn_ns/app/int_repr7compact.py

[[
e ../../python3_src/bash_script/app/int_repr7compact
int_repr7compact encode 7777
    @WtW
]]
py -m nn_ns.app.int_repr7compact
[[
int_repr7compact encode 0 1 -1 999 -999 +11 -11 +7777 -7777
    =
    @0
    -y
    @Ub
    -VN
    @A
    -o
    @WtW
    -T5T

int_repr7compact decode -- = @0 -y @Ub -VN @A -o @WtW -T5T
    0
    1
    -1
    999
    -999
    11
    -11
    7777
    -7777

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end -3
    (-7777, 7)

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end 6
    ^EOFError: (2, 1, b'9')

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end 7
    (-7777, 7)

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end 7 --strict
    -7777

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end 8 --strict
    ^seed.int_tools.int_repr7lex_order7base.FormatError: ('5', 7, 8)

]]
]]]'''#'''
if 1:from seed.int_tools.int_repr7compact7lex_order7baseGL import _main_
if __name__ == '__main__':
    _main_()

