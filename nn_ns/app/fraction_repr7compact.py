r'''[[[
e ../../python3_src/nn_ns/app/fraction_repr7compact.py

[[
e ../../python3_src/bash_script/app/fraction_repr7compact
fraction_repr7compact encode -- 7777 +233/377
    @Yn1
    @0z.z.z.z.z.z00

]]
py -m nn_ns.app.fraction_repr7compact
[[
fraction_repr7compact encode -- 0 1 -1 999 -999 +11 -11 +7777 -7777  +144/233 -144/233 +233/377 -233/377
    =
    @1
    -x
    @VUD
    -UVl
    @FL
    -jd
    @Yn1
    -RBx
    @0z.z.z.z.z.yy
    -y.z.z.z.z.z00
    @0z.z.z.z.z.z00
    -y.z.z.z.z.z.yy


fraction_repr7compact decode -- = @1 -x @VUD -UVl @FL -jd @Yn1 -RBx @0z.z.z.z.z.yy -y.z.z.z.z.z00 @0z.z.z.z.z.z00 -y.z.z.z.z.z.yy
    0
    1
    -1
    999
    -999
    11
    -11
    7777
    -7777
    144/233
    -144/233
    233/377
    -233/377

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end -3
    (Fraction(-233, 377), 18)

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end 17
    ^EOFError: (1, 0, b'')
fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end -7
    ^EOFError: (1, 0, b'')

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end -6
    (Fraction(-233, 377), 18)
fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end 18
    (Fraction(-233, 377), 18)

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end 18 --strict
    -233/377

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end 19 --strict
    ^seed.int_tools.int_repr7lex_order7base.FormatError: ('5', 18, 19)

]]
]]]'''#'''
if 1:from seed.int_tools.int_repr7compact7lex_order7baseGL import _main4fraction_
if __name__ == '__main__':
    _main4fraction_()

