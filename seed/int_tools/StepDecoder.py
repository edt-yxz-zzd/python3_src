#__all__:goto
#TODO:goto
#TODO:test:incremental_decode4int_with_inf__alnum__5over8_ : len()? size_eq? size_le? fullmatch? nonnull_remain_ok?
#TODO:test:incremental_decode4rational_with_inf__alnum__5over8_ : len()? size_eq? size_le? fullmatch? nonnull_remain_ok?
#TODO:test: encode4rational_with_inf__alnum__5over8_, decode4rational_with_inf__alnum__5over8_
#64,65:[0-9A-Za-z._-]
r'''[[[
e ../../python3_src/seed/int_tools/StepDecoder.py
    vs:codecs.IncrementalDecoder
view ../../python3_src/seed/int_tools/digits/codecs4int.py
view others/数学/编程/设计/自定义编码纟整数-alnum字母表+5over8效率.txt
    DONE:step_decoder4int_with_inf__alnum__5over8
view others/数学/编程/设计/自定义编码之要点.txt
    TODO:统一:透明数据化硬编码{区间前缀树,况态化解码结果}
        IStepDecoder__hardwired__prefix_tree
            #TODO:分层表{base;radix} #...似乎无必要,因为 整除分阶层 更像是会被参数化的特征
        TODO:阶跃式分阶层、强幂级进分阶层

seed.int_tools.StepDecoder
py -m nn_ns.app.debug_cmd   seed.int_tools.StepDecoder -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.StepDecoder:__doc__ -ht # -ff -df

[[
源起:
    view ../../python3_src/seed/int_tools/digits/codecs4int.py
]]
[[
[radix >= 1][digit :: uint%radix]
内禀:radix_info4digit{body}
输入:radix_info4head, digit8head, digits{stream}
#allow:[radix4head > radix4digit]
    # eg:macro_header vs body_cell
or:
    输入:rxdigit8remain, digits{stream}
    #allow:[radix4remain > radix4digit]
[radix_info4head.radix may be non-zpow]
    #high freq be zpow
[radix_info4digit.radix may be non-zpow]
    #almost be zpow
]]

rename:
    :%s/NormalState\C/LoopState/g
    :%s/normal_st\C/loop_st/g
    :%s/7normal\C/7loop/g
    :%s/\<normal\>\C/loop/g

[[
#[词典序&&变长]=>(动态爻元|动态苞元)
#[变殿后<:语境相关有序对]
DONE:dependent_pair
TODO:dependent_serial#连锁依赖串联
TODO:带多层长度的负载冃自然数#宏头胞 代表 层数; (统一单位:爻元|躯胞，但 线性变换:step{j8layer}*u+offset{j8layer} 或者 非线性变换:f(j8layer,u))
DONE:dynamic_bits-->dynamic_digits
    len_dydigits
    (len_dydigits4head, len_dydigits4body)
DONE:fixed_size_bits-->fixed_size_digits
    (u8head, weight4head, u8digits)
    u8head add1 ???
TODO:dynamic_bits_with_dependent_size_bits-->dynamic_digits_with_dependent_size_digits
    (len_dydigits, u8szdigits)
        u8head add1 ???

]]
[[
头苞另计:因为 头苞 未必是 二幂
躯胞丷爻元:因为 躯胞 未必是 二幂

另计: not counting in; extra
]]
[[
基础:
    IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits
        #覆盖:IStepDecoder__dynamic_bits
        #覆盖:IStepDecoder__dynamic_bibits
    IStepDecoder__fixed_size_xbcells
        #覆盖:IStepDecoder__fixed_size_bits
分叉:
    IStepDecoder__extend_macro_header
        #糅合深入型
        #覆盖:IStepDecoder__skip_macro_header
            #深入型
    IStepDecoder__parallel__partition_space4macro_header
        #并联型
高层:
    IStepDecoder__plugin4finite_uint_interval__fixed_size_layers
        #多凡层插件
        #透明数据化:基于:IStepDecoder__fixed_size_layers__functional
    IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers
        #超凡层插件
树状结构:
    无限区--[分叉]->([有限区],无限区)
        #IStepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header
    无限区--[深入]->糅合深入型{无限区}
        #IStepDecoder__plugin4infinite_uint_interval__extend_macro_header
    无限区--[具现]->超凡层插件
        #IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers

    有限区--[分叉]->[有限区]
        #IStepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header
    有限区--[深入]->糅合深入型{有限区}
        #IStepDecoder__plugin4finite_uint_interval__extend_macro_header
    有限区--[具现]->多凡层插件
        #IStepDecoder__plugin4finite_uint_interval__fixed_size_layers
]]

:%s/\<IStepDecoder__fixed_size_layers__plugin4finite_uint_interval\>/IStepDecoder__plugin4finite_uint_interval__fixed_size_layers/g
:%s/\<IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers__plugin4infinite_uint_interval\>/IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers/g











>>> dr4alnum = gmk_step_decoder4int_with_inf__alnum__5over8_()
>>> from seed.int_tools.DigitReader import SubSeq, DigitReader5seq
>>> from string import digits, ascii_uppercase, ascii_lowercase
>>> _alphabet4alnum = digits+ascii_uppercase
>>> alphabet4alnum6body = _alphabet4alnum[:32]
>>> alphabet4alnum6head = _alphabet4alnum[32:35]
>>> def mk_alnum2digit_(alphabet4alnum, /):
...      alnum2digit = {c:j for j,c in enumerate(alphabet4alnum)}
...      for c in alphabet4alnum:
...          alnum2digit[c.lower()] = alnum2digit[c]
...      return alnum2digit
>>> alnum2digit6head = mk_alnum2digit_(alphabet4alnum6head)
>>> alnum2digit6body = mk_alnum2digit_(alphabet4alnum6body)
>>> def mk_digit_seq4alnum_(alnum2digit, s, /):
...     seq = [*map(alnum2digit.__getitem__, s)] # [alnum2digit[c] for c in s]
...     return seq
>>> radix_info4digit4alnum = dr4alnum.radix_info4digit
>>> radix_info4macro_header4alnum = dr4alnum.radix_info4macro_header
>>> def mk_input4step_decoder4alnum_(s, /):
...     ###
...     c = s[0]
...     digit8H = alnum2digit6head[c]
...     rxdigit8H = RadixedDigit(radix_info4macro_header4alnum, digit8H)
...     ###
...     _s = s[1:]
...     seq = mk_digit_seq4alnum_(alnum2digit6body, _s)
...     digit_subseq = SubSeq(seq, begin:=0, end:=len(seq))
...     digit_reader = DigitReader5seq(radix_info4digit4alnum, digit_subseq)
...     ###
...     input4step_decoder = Input4StepDecoder(rxdigit8H, digit_reader)
...     return input4step_decoder
...     ###

def step_decode__input_(step_decoder, input4step_decoder, /, *, to_full_output=False):
def step_decode__head_(step_decoder, rxdigit8macro_header, digit_reader, /):
>>> def step_decode4alnum_(s, /, *, to_full_output=False):
...     input4step_decoder = mk_input4step_decoder4alnum_(s)
...     return step_decode__input_(dr4alnum, input4step_decoder, to_full_output=to_full_output)


PartialOutput4StepDecoder(oresult, rxdigit8remain)
#>>> step_decode4alnum_('X', to_full_output=False)
>>> step_decode4alnum_('X')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))

>>> step_decode4alnum_('Y0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('Y1')
PartialOutput4StepDecoder(1, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('Y2')
PartialOutput4StepDecoder(2, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('Y3')
PartialOutput4StepDecoder(3, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YA')
PartialOutput4StepDecoder(10, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YF')
PartialOutput4StepDecoder(15, RadixedDigit(ZpowRadixInfo(0), 0))

>>> step_decode4alnum_('YG')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YH') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YN') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...


>>> step_decode4alnum_('YO')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YR') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...


>>> step_decode4alnum_('YS') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...


>>> step_decode4alnum_('YT') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...


>>> step_decode4alnum_('YU')
PartialOutput4StepDecoder((+oo), RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YV')
Traceback (most recent call last):
    ...
seed.int_tools.StepDecoder.ReservedAreaException: (0, RadixedDigit(ZpowRadixInfo(0), 0))




[G-N]:2凡层
>>> step_decode4alnum_('YG')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))

>>> step_decode4alnum_('YH0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YH1')
PartialOutput4StepDecoder(1, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YHF')
PartialOutput4StepDecoder(15, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YHU')
PartialOutput4StepDecoder(30, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YHV')
PartialOutput4StepDecoder(31, RadixedDigit(ZpowRadixInfo(0), 0))


>>> step_decode4alnum_('YI0') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YI00')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YI0V')
PartialOutput4StepDecoder(31, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YI10')
PartialOutput4StepDecoder(32, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YIVV')
PartialOutput4StepDecoder(1023, RadixedDigit(ZpowRadixInfo(0), 0))


>>> step_decode4alnum_('YN000000') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YN0000000')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YN000000V')
PartialOutput4StepDecoder(31, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YN00000VV')
PartialOutput4StepDecoder(1023, RadixedDigit(ZpowRadixInfo(0), 0))



[O-R]:3凡层
>>> step_decode4alnum_('YO')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YP0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP1') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YP10')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP1V')
PartialOutput4StepDecoder(31, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP20') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YP200')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP2VV')
PartialOutput4StepDecoder(1023, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP300') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YP3000')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP30VV')
PartialOutput4StepDecoder(1023, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YP3VVV')
PartialOutput4StepDecoder(32767, RadixedDigit(ZpowRadixInfo(0), 0))

>>> step_decode4alnum_('YR00') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YR000')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YR001') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YR0010')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YR001V')
PartialOutput4StepDecoder(31, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YR0020') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YR00200')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YR002VV')
PartialOutput4StepDecoder(1023, RadixedDigit(ZpowRadixInfo(0), 0))



[S]:4凡层
>>> step_decode4alnum_('YS11') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YS111')
PartialOutput4StepDecoder(1, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YS110')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YS10')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YS0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YS11V')
PartialOutput4StepDecoder(31, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YS13VVV')
PartialOutput4StepDecoder(32767, RadixedDigit(ZpowRadixInfo(0), 0))


[T]:深入
>>> step_decode4alnum_('YT') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YTA') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YTAL') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YTALA') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YTALAL') #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
EOFError: ...
>>> step_decode4alnum_('YT0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YTA0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YTAL0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YTALA0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YTALAL0')
PartialOutput4StepDecoder(0, RadixedDigit(ZpowRadixInfo(0), 0))


[U]:正无穷
[V]:保留区
>>> step_decode4alnum_('YU')
PartialOutput4StepDecoder((+oo), RadixedDigit(ZpowRadixInfo(0), 0))
>>> step_decode4alnum_('YV')
Traceback (most recent call last):
    ...
seed.int_tools.StepDecoder.ReservedAreaException: (0, RadixedDigit(ZpowRadixInfo(0), 0))





encode4int_with_inf__alnum__5over8_
>>> _58_enc = lambda xi:encode4int_with_inf__alnum__5over8_(xi, digits_vs_str=True)
>>> _58_enc(+oo)
'YU'
>>> _58_enc(-oo)
'W1'
>>> _58_enc(0)
'X'
>>> _58_enc(+1)
'Y1'
>>> _58_enc(-15)
'WG'
>>> _58_enc(+15)
'YF'
>>> _58_enc(-16)
'WEF'
>>> _58_enc(+16)
'YHG'

>>> _58_enc(-(2**35-1))
'W80000000'
>>> _58_enc(+(2**35-1)) == ''.join(['YN', 'V'*(2**3-1)])
True
>>> _58_enc(-(2**35))
'W6NUVVVVVVV'
>>> _58_enc(+(2**35)) == ''.join(['YP', '8',     '1','0'*(2**3-1)])
True

>>> _58_enc(-(2**163835-1)) == ''.join(['W4', '0'*(2**2-1), '0'*(2**15-1)])
True
>>> _58_enc(+(2**163835-1)) == ''.join(['YR', 'V'*(2**2-1), 'V'*(2**15-1)])
True
>>> _58_enc(-(2**163835)) == ''.join(['W3', 'R',     'U','V'*(2**2-1),     'U','V'*(2**15-1)])
True
>>> _58_enc(+(2**163835)) == ''.join(['YS', '4',     '1','0'*(2**2-1),     '1','0'*(2**15-1)])
True




decode4int_with_inf__alnum__5over8_
>>> _58_dec = lambda s:decode4int_with_inf__alnum__5over8_(s, fullmatch=True)
>>> _58_dec('YU')
(+oo)
>>> _58_dec('W1')
(-oo)
>>> _58_dec('X')
0
>>> _58_dec('Y1')
1
>>> _58_dec('WG')
-15
>>> _58_dec('YF')
15
>>> _58_dec('WEF')
-16
>>> _58_dec('YHG')
16

>>> _58_dec('W80000000') == -(2**35-1)
True
>>> _58_dec('YNVVVVVVV') == +(2**35-1)
True
>>> _58_dec('W6NUVVVVVVV') == -(2**35)
True
>>> _58_dec('YP810000000') == +(2**35)
True



>>> _58_dec(''.join(['W4', '0'*(2**2-1), '0'*(2**15-1)])) == -(2**163835-1)
True
>>> _58_dec(''.join(['YR', 'V'*(2**2-1), 'V'*(2**15-1)])) == +(2**163835-1)
True
>>> _58_dec(''.join(['W3', 'R',     'U','V'*(2**2-1),     'U','V'*(2**15-1)])) == -(2**163835)
True
>>> _58_dec(''.join(['YS', '4',     '1','0'*(2**2-1),     '1','0'*(2**15-1)])) == +(2**163835)
True

#非标准数据:
>>> _58_dec('YT0')
0
>>> _58_dec('YTA0')
0
>>> _58_dec('YTAL0')
0
>>> _58_dec('YTALA0')
0
>>> _58_dec('YTALAL0')
0


>>> _58_dec('YT0')
0
>>> _58_dec('YT10')
0
>>> _58_dec('YT8')
0
>>> _58_dec('YT90')
0
>>> _58_dec('YTA0')
0
>>> _58_dec('YTA10')
0
>>> _58_dec('YTAG')
0
>>> _58_dec('YTAH0')
0
>>> _58_dec('YTAK0')
0
>>> _58_dec('YTAK10')
0
>>> _58_dec('YTAL0')
0
>>> _58_dec('YTAL10')
0


>>> _58_dec('YTAL0')
0
>>> _58_dec('YTAL10')
0
>>> _58_dec('YTAL8')
0
>>> _58_dec('YTAL90')
0
>>> _58_dec('YTALA0')
0
>>> _58_dec('YTALA10')
0
>>> _58_dec('YTALAG')
0
>>> _58_dec('YTALAH0')
0
>>> _58_dec('YTALAK0')
0
>>> _58_dec('YTALAK10')
0
>>> _58_dec('YTALAL0')
0
>>> _58_dec('YTALAL10')
0


>>> _58_dec('YTALAL111111111111111')
1
>>> _58_dec('YS111')
1
>>> _58_dec('YT11111')
1
>>> _58_dec('YT201111')
1
>>> _58_dec('YT3001111')
1

>>> _58_dec('YT911111')
1
>>> _58_dec('YTA1111111')
1
>>> _58_dec('YTAH1111111')
1
>>> _58_dec('YTAK11111111')
1
>>> _58_dec('YTAL1111111111')
1
>>> _58_dec('YTAL91111111111')
1



py_adhoc_call   seed.int_tools.StepDecoder   @f
from seed.int_tools.StepDecoder import *
]]]'''#'''
__all__ = r'''
incremental_decode__continued_
    incremental_decode__init5head_
    incremental_decode__init5state_
        prepare_step_decoder4incremental_decode_
    incremental_decode__headed_digits_
    incremental_decode__ops4iter_headed_digits_
        mk_incremental_decode5ops4iter_headed_digits_
            Mkr4incremental_decode5ops4iter_headed_digits
    incremental_decode4int_with_inf__alnum__5over8_

    StepDecoder__flatten
    IOps4IterDigitsWithHeadCell
        Ops4IterDigitsWithHeadCell__functional
IWrappedResult7incremental_decode
    WrappedResult7incremental_decode
IWrappedState7incremental_decode
    WrappedState7incremental_decode
IExtendedOutResult7incremental_decode
    ExtendedOutResult7incremental_decode

incremental_decode4int_with_inf__alnum__5over8_
encode4int_with_inf__alnum__5over8_
    iter_encode4int_with_inf__alnum__5over8_
decode4int_with_inf__alnum__5over8_
    gmk_step_decoder4int_with_inf__alnum__5over8_

incremental_decode4rational_with_inf__alnum__5over8_
encode4rational_with_inf__alnum__5over8_
    iter_encode4rational_with_inf__alnum__5over8_
decode4rational_with_inf__alnum__5over8_
    gmk_step_decoder4rational_with_inf__alnum__5over8_

IDecoder__token_seq
    Exception__nonnull_remain
    Exception__not_fullmatch


CallEntry4StepDecoder
Kind4State4StepDecoder
IBaseState4StepDecoder
    ILoopState4StepDecoder
        LoopState4StepDecoder__plain
    ICallState4StepDecoder
        CallState4StepDecoder__plain
            mk_nontail_call_st4step_decoder_
        TailCallState4StepDecoder__plain
            mk_tail_call_st4step_decoder_
        XCallState4StepDecoder__plain
IInput4StepDecoder
    Input4StepDecoder
IPartialOutput4StepDecoder
        PartialOutput4StepDecoder
    IFullOutput4StepDecoder
        FullOutput4StepDecoder

IStepDecoder
    mk_xoutput4step_decoder_
        std_step_decode__call_entry_
        std_step_decode__input_
        std_step_decode__head_
        std_step_decode__state_
    step_decode__input_
    step_decode__head_
    step_decode__state_

IStepDecoder
    IStepDecoder__init_radix_info4digit
    IStepDecoder__recursive_without_nontail_call_and_postprocess
        IStepDecoder__without_subcall
            IStepDecoder__flatten
            IStepDecoder__dynamic_bits
                StepDecoder__dynamic_bits
            IStepDecoder__fixed_size_bits
            IStepDecoder__fixed_size_xbcells
                StepDecoder__fixed_size_xbcells
                IStepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval
                    StepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval
            IStepDecoder__dynamic_bibits
                StepDecoder__dynamic_bibits
    IStepDecoder__wrapper
        IStepDecoder__postprocess_wrapper
        IStepDecoder__flatten
            StepDecoder__flatten
        IStepDecoder__flip_digits
            StepDecoder__flip_digits
    IStepDecoder__dependent_pair
        IStepDecoder__dynamic_bits_with_dependent_size_bits
        IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits
            StepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits
    IStepDecoder__fixed_radix4macro_header
        IStepDecoder__skip_macro_header
        IStepDecoder__extend_macro_header
        IStepDecoder__parallel__partition_space4macro_header
    IStepDecoder__constant_oresult
        StepDecoder__constant_oresult






IUIntCompressor
    IUIntLinearTransform
        UIntLinearTransform
            uint_linear_transform8echo
rxdigit8one
rxdigit8two
IStepDecoder__fixed_size_layers__functional
    Exception__min_layer_idx4end_by_cell_boundary
    IStepDecoder__fixed_size_layers__body4infinite_uint_interval
        StepDecoder__fixed_size_layers__body4infinite_uint_interval
    IStepDecoder__plugin4finite_uint_interval__fixed_size_layers
IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers
    ReservedAreaException
    InfiniteException__nonzero_rxdigit8remain


IStepDecoder__plugin4uint_interval__base
    IStepDecoder__plugin4uint_interval__extend_macro_header
    IStepDecoder__plugin4uint_interval__parallel__partition_space4macro_header

IStepDecoder__plugin4uint_interval__base
    IStepDecoder__plugin4finite_uint_interval
        IStepDecoder__plugin4finite_uint_interval__extend_macro_header
            StepDecoder__plugin4finite_uint_interval__extend_macro_header
        IStepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header
            StepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header
        IStepDecoder__plugin4finite_uint_interval__fixed_size_layers
            StepDecoder__plugin4finite_uint_interval__fixed_size_layers

    IStepDecoder__plugin4infinite_uint_interval
        IStepDecoder__plugin4infinite_uint_interval__extend_macro_header
            StepDecoder__plugin4infinite_uint_interval__extend_macro_header
        IStepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header
            StepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header
        IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers
            StepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers





check_radix_info4macro_header
check_radix_info4digit
check_uint_with_unit
    check_unit
check_uint_linear_transforms4each_layer

IStepDecoder__uint_without_inf__uint_zero_encoded_as_head_digit_zero
IStepDecoder__uint_with_inf
    StepDecoder__uint_with_inf
IStepDecoder__int_with_inf
    StepDecoder__int_with_inf
        gmk_step_decoder4int_with_inf__alnum__5over8_
IStepDecoder__rational_with_inf
    StepDecoder__rational_with_inf





IStepDecoder__hardwired__prefix_tree
    StepDecoder__hardwired__prefix_tree
    fill_prefix_tree_
        PrefixTree4step_decoder
        Target4prefix_tree4step_decoder













max_digit5num_bits_ex_
max_digit5num_bits_
'''.split()#'''
    #IStepDecoder__fixed_size_layers
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from operator import __neg__
from functools import cached_property
from itertools import islice
from itertools import accumulate
#accumulate(iterable, func=None, *, initial=None)
from bisect import bisect_right
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_non_ABC, check_pair, check_callable, check_iterator

from seed.tiny_.oo8inf import oo

from seed.int_tools.RadixInfo import IRadixInfo, RadixInfo


from enum import Enum, auto
from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
#def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
#def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
#    def _check6make_(sf, /):
from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#    def _check6make_(sf, /):


from seed.types.Either import Cased, Either
from seed.types.Either import mk_Left, mk_Right

from seed.int_tools.RadixInfo import IZpowRadixInfo, ZpowRadixInfo# mk_ZpowRadixInfo_
from seed.int_tools.RadixInfo import IRadixInfo, mk_radix_info5or_radix_# RadixInfo, mk_RadixInfo_
from seed.int_tools.RadixInfo import IRadixedDigit, RadixedDigit, rxdigit8no_bits

from seed.helper.ConstantRepr import ConstantRepr
from seed.int_tools.DigitReader import IDigitReader# IDigitReader5iter, IDigitReader5seq, IDigitReader5bytes, IDigitReader5binary_file, IDigitReader5text_file
#from seed.int_tools.DigitReader import DigitReader5seq, DigitReader5iter, DigitReader5bytes, DigitReader5binary_file, DigitReader5text_file
#from seed.int_tools.DigitReader import SubSeq, DigitReader5seq
#from seed.int_tools.count_num_leading1s import count_num_leading1s_, count_num_leading1s_ex_

from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
lazy_import4funcs_('seed.tiny', 'mk_tuple,print_err,fst,snd,MapView:mk_MapView_,echo', __name__)
if 0:from seed.tiny import mk_tuple,print_err,fst,snd,MapView as mk_MapView_,echo
lazy_import4funcs_('seed.int_tools.concat_digits2bytes', 'concat_digits2uint_,concat_digits2bytes_,concat_digits2iter_bytess_', __name__)
if 0:from seed.int_tools.concat_digits2bytes import concat_digits2uint_, concat_digits2bytes_, concat_digits2iter_bytess_

ceil_div = lazy_import4func_('seed.math.floor_ceil', 'ceil_div', __name__)
#from seed.math.floor_ceil import ceil_div

uint5radix_repr_ = lazy_import4func_('seed.int_tools.digits.uint25radix_repr', 'uint5radix_repr_', __name__)
#from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_, uint5radix_repr_

rglnkls2reversed_iterable = lazy_import4func_('seed.data_funcs.lnkls', 'rglnkls2reversed_iterable', __name__)
#from seed.data_funcs.lnkls import rglnkls2reversed_iterable

calc_Fraction5finite_continued_fraction_ = lazy_import4func_('seed.math.continued_fraction.continued_fraction_fold', 'calc_Fraction5finite_continued_fraction_', __name__)
#from seed.math.continued_fraction.continued_fraction_fold import calc_Fraction5finite_continued_fraction_

iter_continued_fraction_digits5ND_ = lazy_import4func_('seed.math.continued_fraction.continued_fraction5ND', 'iter_continued_fraction_digits5ND_', __name__)
#from seed.math.continued_fraction.continued_fraction5ND import iter_continued_fraction_digits5ND_

uintZbase32_ = lazy_import4func_('seed.int_tools.digits.uintZSbase32', 'uintZbase32_', __name__)
#from seed.int_tools.digits.uintZSbase32 import uintZbase32_, uintSbase32_, base32_alplabet see:_58_tbl6body
from numbers import Rational
#Rational.as_integer_ratio
#   AttributeError: type object 'Rational' has no attribute 'as_integer_ratio'
Rational.numerator
Rational.denominator

mk_seq_rng = lazy_import4func_('seed.seq_tools.mk_seq_rng', 'mk_seq_rng', __name__)
#from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len


lazy_import4func_('seed.int_tools.DigitReader', 'DigitReader5iter', __name__, 'mk_DigitReader5iter')
if 0:from seed.int_tools.DigitReader import DigitReader5iter as mk_DigitReader5iter
mk_DigitReader5iter

mk_Rope = lazy_import4func_('seed.types.Rope', 'mk_Rope', __name__)
lazy_import4func_('seed.types.Rope', 'Rope', __name__, '_Rope')
if 0:from seed.types.Rope import mk_Rope, Rope as _Rope
_Rope
#[iter_subseq__opaque_,iter_subseq__transparent_] = lazy_import4funcs_('seed.iters.iter_subseq', 'iter_subseq__opaque_,iter_subseq__transparent_', __name__)

___end_mark_of_excluded_global_names__0___ = ...
__all__

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError


def max_digit5num_bits_ex_(num_bits, imay_max_digit, /):
    'num_bits/uint{>=0} -> imay max_digit -> max_digit/uint{>=0}{==2**num_bits-1}'
    return max_digit5num_bits_(num_bits) if imay_max_digit==-1 else imay_max_digit
def max_digit5num_bits_(num_bits, /):
    'num_bits/uint{>=0} -> max_digit/uint{>=0}{==2**num_bits-1}'
    return (1<<num_bits)-1



_BaseCallEntry4StepDecoder = mk_namedtuple_(__name__, 'BaseCallEntry4StepDecoder', 'step_decoder state')
class CallEntry4StepDecoder(_BaseCallEntry4StepDecoder):
    'call_entry'
    def step_decode_(sf, digit_reader, /, *, to_full_output=False):
        'digit_reader/IDigitReader{digit_reader.radix4digit==sf.radix4digit} -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
        #see:step_decode__state_
        return sf.step_decoder.step_decode__state_(sf.state, digit_reader, to_full_output=to_full_output)
_CallE = CallEntry4StepDecoder
class Kind4State4StepDecoder(Enum):
    'kind4subtype'
    loop = auto()
    call = auto()
_K = Kind4State4StepDecoder
class IBaseState4StepDecoder(ABC):
    r'''[[[
common:
    + kind4subtype =:
        | loop
        | call
    + cased_data/(case, payload)
subtypes:
    * loop_st:
        + rxdigit8remain/(radix_info4remain, digit8remain)
        + num_required_digits
    * call_st:
        + call_entry/(step_decoder4call, state4call)

    #]]]'''#'''
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def kind4subtype(sf, /):
        '-> Kind4State4StepDecoder'
    @property
    @abstractmethod
    def cased_data(sf, /):
        '-> Cased'
    @property
    @abstractmethod
    def is_tail_call_st(sf, /):
        '-> bool # [is_tail_call_st -> is_call_st]'
        #return sf.kind4subtype is _K.call and sf.???
    @property
    def is_final_st(sf, /):
        '-> bool # [is_final_st =[def]= is_loop_st&&(num_required_digits==0)] # [is_final_st -> is_loop_st]'
        return sf.kind4subtype is _K.loop and sf.num_required_digits == 0
    ######################
    ######################
    @property
    def is_loop_st(sf, /):
        '-> bool # [is_loop_st =[def]= kind4subtype is loop]'
        return sf.kind4subtype is _K.loop
    @property
    def is_call_st(sf, /):
        '-> bool # [is_call_st =[def]= kind4subtype is call]'
        return sf.kind4subtype is _K.call
    ######################
    ######################
    @property
    def case(sf, /):
        '-> Hashable'
        return sf.cased_data.case
    @property
    def payload(sf, /):
        '-> object # [[is_final_st] => [payload is oresult]][[is_tail_call_st] => [payload is may_postprocess]]'
        return sf.cased_data.payload
    ######################
class ICallState4StepDecoder(IBaseState4StepDecoder):
    'call_st'
    __slots__ = ()
    ######################
    #@override
    kind4subtype = _K.call
    #@override
    is_final_st = False
    #@override
    is_loop_st = False
    #@override
    is_call_st = True
    ######################
    @property
    @abstractmethod
    def call_entry(sf, /):
        '-> CallEntry4StepDecoder'
    ######################
    @property
    def tmay_may_postprocess(sf, /):
        '-> (tmay may_postprocess){==(payload,) if is_tail_call_st else ()} # [postprocess :: (oresult->oresult)]'
        return (sf.payload,) if sf.is_tail_call_st else ()
    ######################
    ######################
    @property
    def step_decoder4call(sf, /):
        '-> IStepDecoder'
        return sf.call_entry.step_decoder
    @property
    def state4call(sf, /):
        '-> IBaseState4StepDecoder'
        return sf.call_entry.state
    ######################
#end-class ICallState4StepDecoder(IBaseState4StepDecoder):
class ILoopState4StepDecoder(IBaseState4StepDecoder):
    'loop_st'
    __slots__ = ()
    ######################
    #@override
    kind4subtype = _K.loop
    #@override
    is_tail_call_st = False
    #@override
    is_loop_st = True
    #@override
    is_call_st = False
    ######################
    @property
    @abstractmethod
    def rxdigit8remain(sf, /):
        '-> IRadixedDigit # remain{current round} be head{next round}'
    @property
    @abstractmethod
    def num_required_digits(sf, /):
        '-> uint{>=0} # [is_final_st==(0==num_required_digits)]'
    ######################
    @property
    @override
    def is_final_st(sf, /):
        '-> bool'
        return 0 == sf.num_required_digits
        return not sf.num_required_digits
    ######################
    #.######################
    #.@abstractmethod
    #.def ireplace_(sf, case, payload, /):
    #.    '-> ILoopState4StepDecoder'
    #.######################
    ######################
    @property
    def tmay_oresult(sf, /):
        '-> (tmay oresult){==(payload,) if is_final_st else ()}'
        return (sf.payload,) if sf.is_final_st else ()
    ######################
    ######################
    @property
    def radix_info4remain(sf, /):
        '-> IRadixInfo # (.is_zpow_radix|IZpowRadixInfo) => [.radix===2**num_bits4remain] # allow [num_bits4remain > num_bits4digit]'
        return sf.rxdigit8remain.radix_info
    @property
    def digit8remain(sf, /):
        '-> uint%radix4remain # (.is_zpow_radix|IZpowRadixInfo) => uint%2**num_bits4remain'
        return sf.rxdigit8remain.digit
    ######################
    @property
    def num_bits4remain(sf, /):
        '-> (uint{>=0} if (.is_zpow_radix|IZpowRadixInfo) else ^AttributeError) # allow [num_bits4remain > num_bits4digit]'
        return sf.radix_info4remain.num_bits4digit
    @property
    def radix4remain(sf, /):
        '-> uint{>=1}'
        return sf.radix_info4remain.radix
    @property
    def max_digit4remain(sf, /):
        '-> uint{==radix4remain-1}'
        return sf.radix_info4remain.max_digit
    ######################
    #.@property
    #.@abstractmethod
    #.def radix_info4remain8head(sf, /):
    #.    '-> IRadixInfo # (.is_zpow_radix|IZpowRadixInfo) => [.radix===2**num_remain_bits8head] # allow [num_remain_bits8head > num_bits4digit]'
    #.@property
    #.@abstractmethod
    #.def remain_digit8head(sf, /):
    #.    '-> uint%radix # (.is_zpow_radix|IZpowRadixInfo) => uint%2**num_remain_bits8head'
    #.######################
    #.@property
    #.def num_remain_bits8head(sf, /):
    #.    '-> (uint{>=0} if (.is_zpow_radix|IZpowRadixInfo) else ^AttributeError) # allow [num_remain_bits8head > num_bits4digit]'
    #.    return sf.radix_info4remain8head.num_bits4digit
    #.@property
    #.def max_remain_digit8head(sf, /):
    #.    '-> uint{==radix-1}'
    #.    return sf.radix_info4remain8head.max_digit
    ######################
#end-class ILoopState4StepDecoder(IBaseState4StepDecoder):

_BaseLoopState4StepDecoder__plain = mk_namedtuple_(__name__, 'BaseLoopState4StepDecoder__plain', 'cased_data rxdigit8remain num_required_digits')
class LoopState4StepDecoder__plain(_BaseLoopState4StepDecoder__plain, ILoopState4StepDecoder):
    ___no_slots_ok___ = True
    @classmethod
    def mk_loop_st5five_args_(cls, case, payload, radix_info4remain, digit8remain, num_required_digits, /):
        '-> loop_st'
        cased_data = Cased(case, payload)
        rxdigit8remain = RadixedDigit(radix_info4remain, digit8remain)
        return cls(cased_data, rxdigit8remain, num_required_digits)
    ######################
    #.@override
    #.def ireplace_(sf, case, payload, /):
    #.    '-> ILoopState4StepDecoder'
    #.    return __class__(case, payload, *sf._t[2:])
    ######################
    #.def __init__(sf, case, payload, radix_info4remain8head, remain_digit8head, num_required_digits, /):
    #.    sf._t = (case, payload, radix_info4remain8head, remain_digit8head, num_required_digits)
    #.@property
    #.@override
    #.def case(sf, /):
    #.    return sf._t[0]
    #.@property
    #.@override
    #.def payload(sf, /):
    #.    return sf._t[1]
    #.@property
    #.@override
    #.def radix_info4remain8head(sf, /):
    #.    return sf._t[2]
    #.@property
    #.@override
    #.def remain_digit8head(sf, /):
    #.    return sf._t[3]
    #.@property
    #.@override
    #.def num_required_digits(sf, /):
    #.    return sf._t[4]
#end-class LoopState4StepDecoder__plain(ILoopState4StepDecoder):
_LoopST = LoopState4StepDecoder__plain

_BaseCallState4StepDecoder__plain = mk_namedtuple_(__name__, 'BaseCallState4StepDecoder__plain', 'cased_data call_entry')
class CallState4StepDecoder__plain(_BaseCallState4StepDecoder__plain, ICallState4StepDecoder):
    ___no_slots_ok___ = True
    #@override
    is_tail_call_st = False
    @classmethod
    def mk_call_st5four_args_(cls, case, payload, step_decoder4call, state4call__or__rxdigit8macro_header, /, *, state_vs_rxdigit=False):
        '-> call_st # [[cls is CallState4StepDecoder__plain] => [return nontail_call_st]] #subclass may be tail_call_st'
        if not state_vs_rxdigit:
            state4call = state4call__or__rxdigit8macro_header
        else:
            rxdigit8macro_header = state4call__or__rxdigit8macro_header
            state4call = step_decoder4call.start_(rxdigit8macro_header)
        state4call

        cased_data = Cased(case, payload)
        call_entry = _CallE(step_decoder4call, state4call)
        return cls(cased_data, call_entry)
#end-class CallState4StepDecoder__plain(ICallState4StepDecoder):
_CallST = CallState4StepDecoder__plain
class TailCallState4StepDecoder__plain(CallState4StepDecoder__plain):
    ___no_slots_ok___ = True
    #@override
    is_tail_call_st = True
    default_case4tail_call = None
    @classmethod
    def mk_tail_call_st5three_args_(cls, may_postprocess, step_decoder4call, state4call__or__rxdigit8macro_header, /, *, state_vs_rxdigit=False):
        '-> tail_call_st'
        return cls.mk_call_st5four_args_(cls.default_case4tail_call, may_postprocess, step_decoder4call, state4call__or__rxdigit8macro_header, state_vs_rxdigit=state_vs_rxdigit)
#end-class TailCallState4StepDecoder__plain(CallState4StepDecoder__plain):
_TCallST = TailCallState4StepDecoder__plain

def mk_nontail_call_st4step_decoder_(cased_data, call_entry):
    return CallState4StepDecoder__plain(cased_data, call_entry)
mk_nontail_call_st4step_decoder_ = CallState4StepDecoder__plain
def mk_tail_call_st4step_decoder_(cased_data, call_entry):
    return TailCallState4StepDecoder__plain(cased_data, call_entry)
mk_tail_call_st4step_decoder_ = TailCallState4StepDecoder__plain

class XCallState4StepDecoder__plain(CallState4StepDecoder__plain):
    ___no_slots_ok___ = True
    #case4tail_call = ConstantRepr('XCallState4StepDecoder__plain.case4tail_call')
    case4tail_call = ConstantRepr('case4tail_call')
    @property
    @override
    def is_tail_call_st(sf, /):
        '-> bool'
        return sf.case is sf.case4tail_call
    @classmethod
    def mk_tail_call_st5three_args_(cls, may_postprocess, step_decoder4call, state4call__or__rxdigit8macro_header, /, *, state_vs_rxdigit=False):
        '-> tail_call_st'
        return cls.mk_call_st5four_args_(cls.case4tail_call, may_postprocess, step_decoder4call, state4call__or__rxdigit8macro_header, state_vs_rxdigit=state_vs_rxdigit)
#end-class XCallState4StepDecoder__plain(CallState4StepDecoder__plain):
_XCallST = XCallState4StepDecoder__plain



class IInput4StepDecoder(ABC):
    'input4step_decoder'
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def rxdigit8macro_header(sf, /):
        '-> IRadixedDigit'
    @property
    @abstractmethod
    def digit_reader(sf, /):
        '-> IDigitReader'
    ######################
class IPartialOutput4StepDecoder(ABC):
    'partial_output4step_decoder'
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def oresult(sf, /):
        '-> object'
    @property
    @abstractmethod
    def rxdigit8remain(sf, /):
        '-> IRadixedDigit'
    ######################
    def mk_full_output_(sf, digit_reader, /):
        'IDigitReader -> IFullOutput4StepDecoder'
        return FullOutput4StepDecoder(sf.oresult, Input4StepDecoder(sf.rxdigit8remain, digit_reader))
    ######################
class IFullOutput4StepDecoder(IPartialOutput4StepDecoder):
    'full_output4step_decoder'
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def oresult(sf, /):
        '-> object'
    @property
    @abstractmethod
    def remain_input(sf, /):
        '-> IInput4StepDecoder'
    ######################
    @property
    @override
    def rxdigit8remain(sf, /):
        '-> IRadixedDigit'
        return sf.remain_input.rxdigit8macro_header
    @property
    def digit_reader(sf, /):
        '-> IRadixedDigit'
        return sf.remain_input.digit_reader
    ######################
    def to_partial_output_(sf, digit_reader, /):
        'IDigitReader -> IPartialOutput4StepDecoder'
        return PartialOutput4StepDecoder(sf.oresult, sf.rxdigit8remain)
    ######################

_BaseInput4StepDecoder = mk_namedtuple_(__name__, 'BaseInput4StepDecoder', 'rxdigit8macro_header digit_reader')
class Input4StepDecoder(_BaseInput4StepDecoder, IInput4StepDecoder):
    ___no_slots_ok___ = True
_BasePartialOutput4StepDecoder = mk_namedtuple_(__name__, 'BasePartialOutput4StepDecoder', 'oresult rxdigit8remain')
class PartialOutput4StepDecoder(_BasePartialOutput4StepDecoder, IPartialOutput4StepDecoder):
    ___no_slots_ok___ = True
_BaseFullOutput4StepDecoder = mk_namedtuple_(__name__, 'BaseFullOutput4StepDecoder', 'oresult remain_input')
class FullOutput4StepDecoder(_BaseFullOutput4StepDecoder, IFullOutput4StepDecoder):
    ___no_slots_ok___ = True

def check_radix_info4macro_header(radix_info4macro_header, /):
    check_type_le(IRadixInfo, radix_info4macro_header)
    check_int_ge(1, radix_info4macro_header.radix)
def check_radix_info4digit(radix_info4digit, /):
    check_type_le(IRadixInfo, radix_info4digit)
    check_int_ge(2, radix_info4digit.radix)
    assert radix_info4digit.is_zpow_radix
    check_int_ge(1, radix_info4digit.num_bits4digit)

IDigitReader
class IStepDecoder(ABC):
    # 后刹=>LL1,剩余 不足 1躯胞
    __slots__ = ()
    ######################
    forbidden_nontail_call_st = False
    forbidden_tail_call_st = False
    forbidden_call_st = False
    recursive_forbidden_nontail_call_st_and_postprocess = False
    if 0:
        @cached_property
        def forbidden_call_st(sf, /):
            '-> bool # see:IStepDecoder__without_subcall'
            return sf.forbidden_tail_call_st and sf.forbidden_nontail_call_st
        @cached_property
        def recursive_forbidden_nontail_call_st_and_postprocess(sf, /):
            '-> bool # see:IStepDecoder__recursive_without_nontail_call_and_postprocess'
            return sf.forbidden_call_st
    ######################
    #.#forbidden_loop_st = False
    #.forbidden_final_loop_st = False
    #.forbidden_nonfinal_loop_st = False
    #.@cached_property
    #.def forbidden_loop_st(sf, /):
    #.    '-> bool'
    #.    return sf.forbidden_final_loop_st and sf.forbidden_nonfinal_loop_st
    ######################
    @property
    @abstractmethod
    def radix_info4digit(sf, /):
        '-> IRadixInfo{radix>=2}'
    ######################
    @property
    def num_bits4digit(sf, /):
        '-> uint{>=1}|^AttributeError if radix is not zpow'
        return sf.radix_info4digit.num_bits4digit
    @property
    def radix4digit(sf, /):
        '-> uint{>=2} # may be not zpow'
        return sf.radix_info4digit.radix
    @property
    def max_digit(sf, /):
        '-> uint{>=1}'
        return sf.radix_info4digit.max_digit
    ######################
    @abstractmethod
    def start_(sf, rxdigit8macro_header, /):
        'rxdigit8macro_header/IRadixedDigit -> st/IBaseState4StepDecoder # allow [num_bits4macro_header > num_bits4digit]'
    @abstractmethod
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        'loop_st7nonfinal/ILoopState4StepDecoder{not is_final_st} -> required_digits/[uint%2**num_bits4digit]{len==loop_st7nonfinal.num_required_digits} -> st/IBaseState4StepDecoder'
    @abstractmethod
    def feed_oresult_remain_(sf, call_st7nontail, oresult7subcall, rxdigit8remain7subcall, /):
        'call_st7nontail/ICallState4StepDecoder{not is_tail_call_st} -> oresult7subcall{return from subcall} -> rxdigit8remain7subcall{return from subcall} -> st/IBaseState4StepDecoder'
    ######################
    def step_decode__input_(sf, input4step_decoder, /, *, to_full_output=False):
        'input4step_decoder/IInput4StepDecoder -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
        return sf.step_decode__head_(input4step_decoder.rxdigit8macro_header, input4step_decoder.digit_reader, to_full_output=to_full_output)
    def step_decode__head_(sf, rxdigit8macro_header, digit_reader, /, *, to_full_output=False):
        'rxdigit8macro_header/IRadixedDigit -> digit_reader/IDigitReader{digit_reader.radix4digit==sf.radix4digit} -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
        st = sf.start_(rxdigit8macro_header)
        return sf.step_decode__state_(st, digit_reader, to_full_output=to_full_output)
    def step_decode__state_(sf, st, digit_reader, /, *, to_full_output=False):
        'st/IBaseState4StepDecoder -> digit_reader/IDigitReader{digit_reader.radix4digit==sf.radix4digit} -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
        #see:IStepDecoder__without_subcall.step_decode__state_
        #see:CallEntry4StepDecoder.step_decode_
        return std_step_decode__state_(sf, st, digit_reader, to_full_output=to_full_output)
    ######################
    #.@abstractmethod
    #.def start_(sf, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header, /):
    #.    'num_bits4macro_header/uint{>=0} -> imay_max_digit8macro_header/imay uint{==2**num_bits4macro_header-1} -> digit8macro_header/uint%2**num_bits4macro_header -> st/IBaseState4StepDecoder # allow [num_bits4macro_header > num_bits4digit]'
    ######################
def mk_xoutput4step_decoder_(oresult, rxdigit8remain, digit_reader, *, to_full_output:bool):
    xout = PartialOutput4StepDecoder(oresult, rxdigit8remain)
        #partial_output4step_decoder
    if to_full_output:
        xout = xout.mk_full_output_(digit_reader)
            #full_output4step_decoder
    return xout
def std_step_decode__call_entry_(call_entry, digit_reader, /, *, to_full_output=False):
    'call_entry/CallEntry4StepDecoder -> digit_reader/IDigitReader{digit_reader.radix4digit==sf.radix4digit} -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
    return std_step_decode__state_(call_entry.step_decoder, call_entry.state, digit_reader, to_full_output=to_full_output)
def std_step_decode__input_(step_decoder, input4step_decoder, /, *, to_full_output=False):
    'step_decoder/IStepDecoder -> input4step_decoder/IInput4StepDecoder -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
    return std_step_decode__head_(step_decoder, input4step_decoder.rxdigit8macro_header, input4step_decoder.digit_reader, to_full_output=to_full_output)
def std_step_decode__head_(step_decoder, rxdigit8macro_header, digit_reader, /, *, to_full_output=False):
    'step_decoder/IStepDecoder -> rxdigit8macro_header/IRadixedDigit -> digit_reader/IDigitReader{digit_reader.radix4digit==sf.radix4digit} -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
    st = step_decoder.start_(rxdigit8macro_header)
    return std_step_decode__state_(step_decoder, st, digit_reader, to_full_output=to_full_output)
def std_step_decode__state_(step_decoder, st, digit_reader, /, *, to_full_output=False):
    'step_decoder/IStepDecoder -> st/IBaseState4StepDecoder -> digit_reader/IDigitReader{digit_reader.radix4digit==sf.radix4digit} -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
    stack = []
        # :: [Either postprocess call_entry]
    while 1:
        match st.kind4subtype:
            case _K.loop:
                num_required_digits = st.num_required_digits
                if num_required_digits == 0:
                    #if st.is_final_st:
                    oresult = st.payload
                    rxdigit8remain = st.rxdigit8remain
                    while stack:
                        x = stack.pop()
                        if x.is_right:
                            old_call_entry = x.right
                            break
                        postprocess = x.left
                        oresult = postprocess(oresult)
                    else:
                        return mk_xoutput4step_decoder_(oresult, rxdigit8remain, digit_reader, to_full_output=to_full_output)
                    #bug:loss:st.rxdigit8remain => rename:feed_oresult_ --> feed_oresult_remain_
                    (step_decoder, st) = old_call_entry
                    777;oresult7subcall = oresult
                    777;rxdigit8remain7subcall = rxdigit8remain
                    st = step_decoder.feed_oresult_remain_(st, oresult7subcall, rxdigit8remain7subcall)
                    continue
                else:
                    required_digits = digit_reader.read_le(num_required_digits)
                    if not len(required_digits) == num_required_digits:raise EOFError(stack, step_decoder, st, required_digits)
                    st = step_decoder.feed_digits_(st, required_digits)
                    continue
                raise 000
            case _K.call:
                new_call_entry = st.call_entry
                if st.is_tail_call_st:
                    may_postprocess = st.payload
                    if not None is may_postprocess:
                        postprocess = may_postprocess
                        stack.append(mk_Left(postprocess))
                    else:
                        pass
                else:
                    old_call_entry = _CallE(step_decoder, st)
                    stack.append(mk_Right(old_call_entry))
                #updated:stack
                (step_decoder, st) = new_call_entry
                continue
            case _:
                raise 000
        raise 000
    raise 000
#end-def std_step_decode__state_(step_decoder, st, digit_reader, /):
def step_decode__input_(step_decoder, input4step_decoder, /, *, to_full_output=False):
    return step_decoder.step_decode__input_(input4step_decoder, to_full_output=to_full_output)
def step_decode__head_(step_decoder, rxdigit8macro_header, digit_reader, /):
    return step_decoder.step_decode__head_(rxdigit8macro_header, digit_reader)
def step_decode__state_(step_decoder, st, digit_reader, /):
    return step_decoder.step_decode__state_(st, digit_reader)
step_decode__input_.__doc__ = std_step_decode__input_.__doc__
step_decode__head_.__doc__ = std_step_decode__head_.__doc__
step_decode__state_.__doc__ = std_step_decode__state_.__doc__

class _Dead:
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        '... -> ^Exception'
        raise 000
    @override
    def feed_oresult_remain_(sf, call_st7nontail, oresult7subcall, rxdigit8remain7subcall, /):
        '... -> ^Exception'
        raise 000
_Dead.feed_digits_
_Dead.feed_oresult_remain_

class IStepDecoder__recursive_without_nontail_call_and_postprocess(IStepDecoder):
    '[st==(loop_st/ILoopState4StepDecoder|tail_call_st/ICallState4StepDecoder{[.is_tail_call_st==True][.tmay_may_postprocess==(None,)][.payload==None][.step_decoder4call.recursive_forbidden_nontail_call_st_and_postprocess==True]})] # NOTE:no nontail_call_st only'
    __slots__ = ()
    ######################
    #@override
    forbidden_nontail_call_st = True
    #@override
    recursive_forbidden_nontail_call_st_and_postprocess = True
    ######################
    @abstractmethod
    @override#update:__doc__
    def start_(sf, rxdigit8macro_header, /):
        'rxdigit8macro_header/IRadixedDigit -> (loop_st/ILoopState4StepDecoder|tail_call_st/ICallState4StepDecoder{is_tail_call_st==False}) # allow [num_bits4macro_header > num_bits4digit]'
    @abstractmethod
    @override#update:__doc__
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        'loop_st7nonfinal/ILoopState4StepDecoder -> required_digits/[uint%2**num_bits4digit]{len==loop_st7nonfinal.num_required_digits} -> (loop_st/ILoopState4StepDecoder|tail_call_st/ICallState4StepDecoder{is_tail_call_st==False})'
    ######################
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
    ######################
    @override
    def step_decode__state_(sf, loop_st, digit_reader, /, *, to_full_output=False):
        'loop_st/ILoopState4StepDecoder -> digit_reader/IDigitReader{digit_reader.radix4digit==sf.radix4digit} -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
        assert loop_st.is_loop_st
        #need no stack!!!
        dr = sf
        while (num_required_digits := loop_st.num_required_digits):
            # [not loop_st.is_final_st]
            required_digits = digit_reader.read_le(num_required_digits)
            if not len(required_digits) == num_required_digits:raise EOFError([], dr, loop_st, required_digits)
                #EOFError(stack, step_decoder, st, required_digits)
            st = dr.feed_digits_(loop_st, required_digits)
            while st.is_call_st:
                if not st.is_tail_call_st:raise Exception(sf, dr, st)
                tail_call_st = st
                (dr, st) = tail_call_st.call_entry
                if not dr.recursive_forbidden_nontail_call_st_and_postprocess:raise Exception(sf, dr, st)
            loop_st = st
        else:
            # [loop_st.is_final_st]
            oresult = loop_st.payload
            rxdigit8remain = loop_st.rxdigit8remain
            return mk_xoutput4step_decoder_(oresult, rxdigit8remain, digit_reader, to_full_output=to_full_output)
        raise 000
    ######################

class IStepDecoder__without_subcall(IStepDecoder__recursive_without_nontail_call_and_postprocess):
    '[st==loop_st::ILoopState4StepDecoder] # NOTE:no tail_call_st too!'
    __slots__ = ()
    ######################
    #@override
    forbidden_call_st = True
    #@override
    forbidden_nontail_call_st = True
    #@override
    forbidden_tail_call_st = True
    #@override
    recursive_forbidden_nontail_call_st_and_postprocess = True
    ######################
    @abstractmethod
    @override#update:__doc__
    def start_(sf, rxdigit8macro_header, /):
        'rxdigit8macro_header/IRadixedDigit -> loop_st/ILoopState4StepDecoder # allow [num_bits4macro_header > num_bits4digit]'
    @abstractmethod
    @override#update:__doc__
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        'loop_st7nonfinal/ILoopState4StepDecoder -> required_digits/[uint%2**num_bits4digit]{len==loop_st7nonfinal.num_required_digits} -> loop_st/ILoopState4StepDecoder'
    ######################
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
    ######################
    @override
    def step_decode__state_(sf, loop_st, digit_reader, /, *, to_full_output=False):
        'loop_st/ILoopState4StepDecoder -> digit_reader/IDigitReader{digit_reader.radix4digit==sf.radix4digit} -> (IPartialOutput4StepDecoder if not to_full_output else IFullOutput4StepDecoder)'
        #need no stack!!!
        while (num_required_digits := loop_st.num_required_digits):
            required_digits = digit_reader.read_le(num_required_digits)
            if not len(required_digits) == num_required_digits:raise EOFError([], sf, loop_st, required_digits)
                #EOFError(stack, step_decoder, st, required_digits)
            loop_st = sf.feed_digits_(loop_st, required_digits)
            if not loop_st.is_loop_st:raise Exception(sf, loop_st)
        else:
            # [loop_st.is_final_st]
            oresult = loop_st.payload
            rxdigit8remain = loop_st.rxdigit8remain
            return mk_xoutput4step_decoder_(oresult, rxdigit8remain, digit_reader, to_full_output=to_full_output)
        raise 000
    ######################
class IStepDecoder__wrapper(IStepDecoder):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder'
    ######################
    @cached_property
    @override
    def radix_info4digit(sf, /):
        '-> IRadixInfo{radix>=2}'
        return sf.the_wrapped_step_decoder.radix_info4digit
    ######################
class IStepDecoder__postprocess_wrapper(IStepDecoder__wrapper):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def may_postprocess(sf, /):
        '-> may postprocess/(oresult->oresult)'
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        step_decoder = sf.the_wrapped_step_decoder
        st = step_decoder.start_(rxdigit8macro_header)
        tail_call_st = TailCallState4StepDecoder__plain.mk_tail_call_st5three_args_(sf.may_postprocess, step_decoder, st)
        return tail_call_st
    #@override
    feed_digits_ = _Dead.feed_digits_
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_


class IStepDecoder__flatten(IStepDecoder__wrapper, IStepDecoder__without_subcall):
    r'''[[[
    '# reproduce framework{std_step_decode__state_}' for incremental_decode__continued_

    [st =[def]= loop_st =[def]= LoopState4StepDecoder__plain((Either (stk,call_entry) oresult), ...)]
    [stk =[def]= (None|(stk, (Either postprocess call_entry)))]
    #]]]'''#'''
    __slots__ = ()
    ######################
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        step_decoder = sf.the_wrapped_step_decoder
        st = step_decoder.start_(rxdigit8macro_header)
        st4sf = sf.mk_start_state7flatten_(st)
        return st4sf
    ######################
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        st4sf = loop_st7nonfinal
        (stk, call_entry7loop7nonfinal) = st4sf.payload
        (step_decoder, st) = call_entry7loop7nonfinal
        st = step_decoder.feed_digits_(st, required_digits)
        st4sf = sf._mk_st4sf_(stk, step_decoder, st)
        return st4sf
    ######################
    def mk_start_state7flatten_(sf, st, /):
        step_decoder = sf.the_wrapped_step_decoder
        stk = None
            # [stk == (None|(stk, (Either postprocess call_entry)))]
            # stack
        st4sf = sf._mk_st4sf_(stk, step_decoder, st)
        return st4sf
    ######################
    def _mk_st4sf_(sf, stk, step_decoder, st, /):
        call_entry = _CallE(step_decoder, st)
        while 1:
            (stk, call_entry7loop) = sf._pushs_until_loop_st(stk, call_entry)
            st7loop = call_entry7loop.state
            if not 0 == st7loop.num_required_digits:
                call_entry7loop7nonfinal = call_entry7loop
                st7loop7nonfinal = st7loop
                payload = (stk, call_entry7loop7nonfinal)
                #not st4sf.is_final_st
                st4sf = _LoopST(Cased(False,payload),  st7loop7nonfinal.rxdigit8remain, st7loop7nonfinal.num_required_digits)
                break
            call_entry7loop7final = call_entry7loop
            #st7final.is_final_st
            st7final = call_entry7loop7final.state
            (stk, x) = sf._pops_while_postprocess(stk, st7final)
            if x.is_left:
                call_entry = x.left
                continue
            (oresult, rxdigit8remain) = x.right
            assert not stk
            payload = oresult

            #st4sf.is_final_st
            st4sf = _LoopST(Cased(True,payload),  rxdigit8remain, 0)
            break
        st4sf
        return st4sf
    ######################
    def _pops_while_postprocess(sf, stk, st7final, /):
        '-> (stk, (Either call_entry (oresult, rxdigit8remain)))'
        oresult = st7final.payload
        rxdigit8remain = st7final.rxdigit8remain
        while stk:
            (stk, x) = stk #.pop()
            if x.is_right:
                old_call_entry = x.right
                break
            postprocess = x.left
            oresult = postprocess(oresult)
        else:
            return (stk, mk_Right((oresult, rxdigit8remain)))
        #bug:loss:st.rxdigit8remain => rename:feed_oresult_ --> feed_oresult_remain_
        (step_decoder, st) = old_call_entry
        777;oresult7subcall = oresult
        777;rxdigit8remain7subcall = rxdigit8remain
        st = step_decoder.feed_oresult_remain_(st, oresult7subcall, rxdigit8remain7subcall)
        call_entry = _CallE(step_decoder, st)
        return (stk, mk_Left(call_entry))
    ######################
    def _pushs_until_loop_st(sf, stk, call_entry, /):
        '-> (stk, call_entry)'
        while (st:=call_entry.state).is_call_st:
            # [st is call_st]
            new_call_entry = st.call_entry
            if st.is_tail_call_st:
                may_postprocess = st.payload
                if not None is may_postprocess:
                    postprocess = may_postprocess
                    stk = (stk, mk_Left(postprocess))
                else:
                    pass
            else:
                stk = (stk, mk_Right(call_entry))
            #updated:stk
            call_entry = new_call_entry
        #end-while (st:=call_entry.state).is_call_st:
        return (stk, call_entry)
    ######################

#end-class IStepDecoder__flatten(IStepDecoder__wrapper, IStepDecoder__without_subcall):
class StepDecoder__flatten(IStepDecoder__flatten):
    ___no_slots_ok___ = True
    def __init__(sf, step_decoder, /):
        sf._dr = step_decoder
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_wrapped_step_decoder)
    @property
    @override
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder'
        return sf._dr
check_non_ABC(StepDecoder__flatten)
######################
#incremental_decode__continued_:related:begin
######################
#######
class IWrappedResult7incremental_decode(ABC):
    'wresult7inc # for .to_be_continued'
    __slots__ = ()
    ######################
    # [wresult7inc :: ((Either wst7inc ext_oresult), num_digits7read, iter_digits8remain)]
    ######################
    @property
    @abstractmethod
    def either__wst7inc__ext_oresult(sf, /):
        '-> (Either wst7inc ext_oresult)'
    @property
    @abstractmethod
    def num_digits7read(sf, /):
        '-> uint{only for curr call}{besides iter_digits8remain}'
    @property
    @abstractmethod
    def iter_digits8remain(sf, /):
        '-> (Iterator digit)'
    ######################
    @cached_property
    def to_be_continued(sf, /):
        '-> bool{has no oresult yet}'
        x = sf.either__wst7inc__ext_oresult
        return x.is_left and not x.left.to_be_continued
    ######################
class IWrappedState7incremental_decode(ABC):
    'wst7inc # for .to_be_continued'
    __slots__ = ()
    ######################
    # [wst7inc :: (call_entry7flatten, total_num_digits7feed, digit_rope8remain6EOF)]
    # [digit :: uint%wst7inc[0].step_decoder.radix4digit]
    ######################
    @property
    @abstractmethod
    def call_entry7flatten(sf, /):
        '-> CallEntry4StepDecoder{IStepDecoder{.forbidden_call_st==True}}' \
        '   #see:[StepDecoder__flatten <: IStepDecoder__flatten <: IStepDecoder__without_subcall <: IStepDecoder{.forbidden_call_st==True}]'
    @property
    @abstractmethod
    def total_num_digits7feed(sf, /):
        '-> uint{>=1}{accumulated}{included rxdigit8macro_header}{besides digit_rope8remain6EOF,iter_digits8remain}'
    @property
    @abstractmethod
    def digit_rope8remain6EOF(sf, /):
        '-> Rope{digit}' \
        '  # [[len(digit_rope8remain6EOF) > 0] -> [iter_digits8remain is empty]]' \
        '  # [[len(digit_rope8remain6EOF) < wst7inc[0].state.num_required_digits]or[len(digit_rope8remain6EOF) == 0 == wst7inc[0].state.num_required_digits]]' \
        '  # => [[len(digit_rope8remain6EOF) > 0] -> [not wst7inc[0].state.is_final_st]]'
    ######################
    @cached_property
    def to_be_continued(sf, /):
        '-> bool{has no oresult yet}'
        return not sf.call_entry7flatten.state.is_final_st
    ######################
class IExtendedOutResult7incremental_decode(ABC):
    'ext_oresult'
    __slots__ = ()
    ######################
    # [ext_oresult :: (oresult, rxdigit8remain, total_num_digits7feed)]
    ######################
    @property
    @abstractmethod
    def oresult(sf, /):
        '-> object{:=final_st.payload}'
    @property
    @abstractmethod
    def rxdigit8remain(sf, /):
        '-> IRadixedDigit'
    @property
    @abstractmethod
    def total_num_digits7feed(sf, /):
        '-> uint{>=1}{accumulated}{included rxdigit8macro_header}{besides digit_rope8remain6EOF,iter_digits8remain}'
    ######################



mk_named_pseudo_tuple_
_BaseWrappedResult7incremental_decode = mk_named_pseudo_tuple_(__name__, 'BaseWrappedResult7incremental_decode', 'either__wst7inc__ext_oresult num_digits7read iter_digits8remain')
class WrappedResult7incremental_decode(_BaseWrappedResult7incremental_decode, IWrappedResult7incremental_decode):
    ___no_slots_ok___ = True
    def _check6make_(sf, /):
        check_type_is(Either, sf.either__wst7inc__ext_oresult)
        check_int_ge(0, sf.num_digits7read)
        check_iterator(sf.iter_digits8remain)
        #if not iter(it:=sf.iter_digits8remain) is it:raise TypeError(type(it))
check_non_ABC(WrappedResult7incremental_decode)

_BaseWrappedState7incremental_decode = mk_named_pseudo_tuple_(__name__, 'BaseWrappedState7incremental_decode', 'call_entry7flatten total_num_digits7feed digit_rope8remain6EOF')
class WrappedState7incremental_decode(_BaseWrappedState7incremental_decode, IWrappedState7incremental_decode):
    ___no_slots_ok___ = True
    def _check6make_(sf, /):
        check_type_is(CallEntry4StepDecoder, sf.call_entry7flatten)
        check_int_ge(1, sf.total_num_digits7feed)
        _Rope(); check_type_is(_Rope, sf.digit_rope8remain6EOF)
check_non_ABC(WrappedState7incremental_decode)

_BaseExtendedOutResult7incremental_decode = mk_named_pseudo_tuple_(__name__, 'BaseExtendedOutResult7incremental_decode', 'oresult rxdigit8remain total_num_digits7feed')
class ExtendedOutResult7incremental_decode(_BaseExtendedOutResult7incremental_decode, IExtendedOutResult7incremental_decode):
    ___no_slots_ok___ = True
    def _check6make_(sf, /):
        check_type_le(IRadixedDigit, sf.rxdigit8remain)
        check_int_ge(1, sf.total_num_digits7feed)
check_non_ABC(ExtendedOutResult7incremental_decode)
_WRes7inc = WrappedResult7incremental_decode
_WST7inc = WrappedState7incremental_decode
_ExOutRes7inc = ExtendedOutResult7incremental_decode

def incremental_decode__init5head_(step_decoder, rxdigit8macro_header, /, wst7inc_vs_wresult7inc:bool):
    'IStepDecoder -> IRadixedDigit -> (wst7inc if not wst7inc_vs_wresult7inc else wresult7inc) #see:incremental_decode__init5state_,incremental_decode__continued_'
    st = step_decoder.start_(rxdigit8macro_header)
    return incremental_decode__init5state_(step_decoder, st, total_num_digits7feed:=1, wst7inc_vs_wresult7inc=wst7inc_vs_wresult7inc)
#######
def prepare_step_decoder4incremental_decode_(step_decoder, /):
    'IStepDecoder -> IStepDecoder{.forbidden_call_st==True} #see:incremental_decode__init5state_,mk_incremental_decode5ops4iter_headed_digits_'
    #.if not isinstance(step_decoder, IStepDecoder__flatten):
        #why not:IStepDecoder__without_subcall
    #if not step_decoder.recursive_forbidden_nontail_call_st_and_postprocess:
    if not step_decoder.forbidden_call_st:
        #why not:IStepDecoder__recursive_without_nontail_call_and_postprocess
        #   !! complex code
        step_decoder = StepDecoder__flatten(step_decoder)
        st = step_decoder.mk_start_state7flatten_(st)
        # [step_decoder :: IStepDecoder__flatten]
    # [step_decoder :: IStepDecoder{.forbidden_call_st==True}]
    return step_decoder
#######
def incremental_decode__init5state_(step_decoder, st, total_num_digits7feed, /, wst7inc_vs_wresult7inc:bool):
    'IStepDecoder -> IBaseState4StepDecoder -> total_num_digits7feed/uint{>=1} -> (wst7inc if not wst7inc_vs_wresult7inc else wresult7inc) #see:incremental_decode__continued_'
    check_int_ge(1, total_num_digits7feed)
    step_decoder = prepare_step_decoder4incremental_decode_(step_decoder)
    # [step_decoder :: IStepDecoder{.forbidden_call_st==True}]
    if not st.is_loop_st:raise Exception(step_decoder, st)
    loop_st = st
    call_entry7flatten = CallEntry4StepDecoder(step_decoder, loop_st)
    wst7inc = _WST7inc(call_entry7flatten, total_num_digits7feed, digit_rope8remain6EOF:=mk_Rope(''))
    if not wst7inc_vs_wresult7inc:
        return wst7inc
    wresult7inc = incremental_decode__continued_(wst7inc, digits8partial_body:='')
    return wresult7inc
#######
def incremental_decode__continued_(wst7inc, digits8partial_body, /):
    r'''[[[
    wst7inc -> digits8partial_body -> wresult7inc
        #reproduce framework{IStepDecoder__without_subcall.step_decode__state_}

    [wst7inc :: IWrappedState7incremental_decode(call_entry7flatten, total_num_digits7feed, digit_rope8remain6EOF)]
    [wresult7inc :: IWrappedResult7incremental_decode((Either wst7inc ext_oresult), num_digits7read, iter_digits8remain)]
    [ext_oresult :: IExtendedOutResult7incremental_decode(oresult, rxdigit8remain, total_num_digits7feed)]

    [call_entry7flatten :: CallEntry4StepDecoder{IStepDecoder{.forbidden_call_st==True}}]
        #see:[StepDecoder__flatten <: IStepDecoder__flatten <: IStepDecoder__without_subcall <: IStepDecoder{.forbidden_call_st==True}]

    [total_num_digits7feed :: uint{>=1}{accumulated}{included rxdigit8macro_header}{besides digit_rope8remain6EOF,iter_digits8remain}]
    [num_digits7read :: uint{only for curr call}{besides iter_digits8remain}]

    [digits8partial_body :: (Iterable digit)]
    [iter_digits8remain :: (Iterator digit)]
    [digit_rope8remain6EOF :: Rope{digit}]
        [[len(digit_rope8remain6EOF) > 0] -> [iter_digits8remain is empty]]
        [[len(digit_rope8remain6EOF) < wst7inc[0].state.num_required_digits]or[len(digit_rope8remain6EOF) == 0 == wst7inc[0].state.num_required_digits]]
            => [[len(digit_rope8remain6EOF) > 0] -> [not wst7inc[0].state.is_final_st]]
    [digit :: uint%wst7inc[0].step_decoder.radix4digit]


    see:incremental_decode__init5state_,incremental_decode__init5head_
    see:Ops4IterDigitsWithHeadCell__functional
    see:StepDecoder__flatten
    see:IStepDecoder__without_subcall.step_decode__state_
    vs:codecs.IncrementalDecoder

    #]]]'''#'''
    it = iter(digits8partial_body)
    (call_entry7flatten, total_num_digits7feed, digit_rope8remain6prev_EOF) = wst7inc
    loop_st = call_entry7flatten.state
    if not loop_st.is_loop_st:raise Exception(call_entry7flatten)

    def _4final(loop_st7final, /):
        ext_oresult = _ExOutRes7inc(loop_st7final.oresult, loop_st7final.rxdigit8remain, total_num_digits7feed)
        wresult7inc = _WRes7inc(mk_Right(ext_oresult), num_digits7read, iter_digits8remain:=it)
        return wresult7inc

    num_digits7read = 0
    if loop_st.is_final_st:
        loop_st7final = loop_st
        if digit_rope8remain6prev_EOF:raise 000
        return _4final(loop_st7final)
    loop_st7nonfinal = loop_st

    def read(n, /):
        nonlocal num_digits7read
        ds = mk_tuple(islice(it, 0, n))
        num_digits7read += len(ds)
        return ds

    n = loop_st7nonfinal.num_required_digits -len(digit_rope8remain6prev_EOF)
    if not 0 < n:raise 000
    ds = read(n)
    if digit_rope8remain6prev_EOF:
        digit_rope = mk_Rope([digit_rope8remain6prev_EOF, ds])
        digits = digit_rope
    else:
        # [not digit_rope8remain6prev_EOF]
        digits = ds
    777; del digit_rope8remain6prev_EOF
    #loop_st7nonfinal, digits
    # [digits :: (tuple|Rope)]
    # [len(digits) <= loop_st7nonfinal.num_required_digits > 0]


    step_decoder = call_entry7flatten.step_decoder
    feed_digits_ = step_decoder.feed_digits_
    def feed(loop_st7nonfinal, digits, /):
        nonlocal total_num_digits7feed
        # [digits :: (tuple|Rope)]
        ds = mk_tuple(digits)
        # [ds :: tuple{digit}]
        st = feed_digits_(loop_st7nonfinal, ds)
        total_num_digits7feed += len(ds)
        return st

    #loop_st7nonfinal, digits
    # [digits :: (tuple|Rope)]
    # [len(digits) <= loop_st7nonfinal.num_required_digits > 0]
    while len(digits)  == loop_st7nonfinal.num_required_digits:
        #loop_st7nonfinal, digits
        # [len(digits) == loop_st7nonfinal.num_required_digits > 0]
        # [digits :: (tuple|Rope)]
        st = feed(loop_st7nonfinal, digits)
        if not st.is_loop_st:raise Exception(step_decoder, loop_st7nonfinal, st)
        loop_st = st
        if loop_st.is_final_st:
            loop_st7final = loop_st
            return _4final(loop_st7final)
        loop_st7nonfinal = loop_st
        digits = read(loop_st7nonfinal.num_required_digits)
        #loop_st7nonfinal, digits
        # [digits :: (tuple|Rope)]
        # [len(digits) <= loop_st7nonfinal.num_required_digits > 0]
    else:
        #loop_st7nonfinal, digits
        # [digits :: (tuple|Rope)]
        # [len(digits) < loop_st7nonfinal.num_required_digits > 0]
        call_entry7flatten = CallEntry4StepDecoder(step_decoder, loop_st7nonfinal)
        wst7inc = _WST7inc(call_entry7flatten, total_num_digits7feed, digit_rope8remain6EOF:=mk_Rope([digits]))
        wresult7inc = _WRes7inc(mk_Left(wst7inc), num_digits7read, iter_digits8remain:=it)
        return wresult7inc
    raise 000
#end-def incremental_decode__continued_(wst7inc, digits8partial_body, /):
#######
def incremental_decode__headed_digits_(step_decoder, digits_with_rxdigit8macro_header, /):
    'IStepDecoder -> iterable([rxdigit8macro_header/IRadixedDigit;digit8body_cell/uint,...]) -> wresult7inc # see:IOps4IterDigitsWithHeadCell,incremental_decode__continued_'
    it = digits_with_rxdigit8macro_header = iter(digits_with_rxdigit8macro_header)
    for rxdigit8macro_header in it:
        break
    else:
        raise 000
    wst7inc = incremental_decode__init5head_(step_decoder, rxdigit8macro_header, wst7inc_vs_wresult7inc=False)
    wresult7inc = incremental_decode__continued_(wst7inc, digits8partial_body:=it)
    return wresult7inc
#end-def incremental_decode__headed_digits_(step_decoder, digits_with_rxdigit8macro_header, /):
#######
def incremental_decode__ops4iter_headed_digits_(step_decoder, ops4iter_headed_digits, may_wst7inc, tokens, /):
    'IStepDecoder -> IOps4IterDigitsWithHeadCell{token} -> may wst7inc -> Iter token -> wresult7inc # see:Ops4IterDigitsWithHeadCell__functional,incremental_decode__continued_,iter_subseq__opaque_,iter_subseq__transparent_'
    if may_wst7inc is None:
        digits_with_rxdigit8macro_header = ops4iter_headed_digits.iter_(tokens)
        wresult7inc = incremental_decode__headed_digits_(step_decoder, digits_with_rxdigit8macro_header)
    else:
        wst7inc = may_wst7inc
        digits8partial_body = ops4iter_headed_digits.iter4body_only_(tokens)
        wresult7inc = incremental_decode__continued_(wst7inc, digits8partial_body)
    return wresult7inc
#######
def mk_incremental_decode5ops4iter_headed_digits_(step_decoder, ops4iter_headed_digits, /):
    'IStepDecoder -> IOps4IterDigitsWithHeadCell{token} -> incremental_decode__tokens_/(may wst7inc -> Iter token -> wresult7inc) # see:Ops4IterDigitsWithHeadCell__functional,incremental_decode__continued_,iter_subseq__opaque_,iter_subseq__transparent_'
    incremental_decode__tokens_ = Mkr4incremental_decode5ops4iter_headed_digits(step_decoder, ops4iter_headed_digits)
    return incremental_decode__tokens_
    #######old_ver:
    step_decoder = prepare_step_decoder4incremental_decode_(step_decoder)
    # [step_decoder :: IStepDecoder{.forbidden_call_st==True}]
    def incremental_decode__tokens_(may_wst7inc, tokens, /):
        'may wst7inc -> Iter token -> wresult7inc'
        return incremental_decode__ops4iter_headed_digits_(step_decoder, ops4iter_headed_digits, may_wst7inc, tokens)
    return incremental_decode__tokens_
#######
class Mkr4incremental_decode5ops4iter_headed_digits:
    'IStepDecoder -> IOps4IterDigitsWithHeadCell{token} -> incremental_decode__tokens_/(may wst7inc -> Iter token -> wresult7inc) # see:mk_incremental_decode5ops4iter_headed_digits_'
    def __init__(sf, step_decoder, ops4iter_headed_digits, /):
        check_type_le(IStepDecoder, step_decoder)
        check_type_le(IOps4IterDigitsWithHeadCell, ops4iter_headed_digits)
        step_decoder = prepare_step_decoder4incremental_decode_(step_decoder)
        # [step_decoder :: IStepDecoder{.forbidden_call_st==True}]
        sf._dr = step_decoder
        sf._ops = ops4iter_headed_digits
    def __repr__(sf, /):
        return repr_helper(sf, sf.step_decoder, sf.ops4iter_headed_digits)
    @property
    def step_decoder(sf, /):
        return sf._dr
    @property
    def ops4iter_headed_digits(sf, /):
        return sf._ops
    def __call__(sf, may_wst7inc, tokens, /):
        'may wst7inc -> Iter token -> wresult7inc'
        return incremental_decode__ops4iter_headed_digits_(sf.step_decoder, sf.ops4iter_headed_digits, may_wst7inc, tokens)
#end-class Mkr4incremental_decode5ops4iter_headed_digits:


#######
class IOps4IterDigitsWithHeadCell(ABC):
    'ops4iter_headed_digits'
    #see:IDecoder__token_seq
    #see:iter_subseq__transparent_
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def radix_info4macro_header(sf, /):
        '-> IRadixInfo'
    ######################
    #.@abstractmethod
    #.def token2head_digit_(sf, token, /):
    #.    'token -> digit8macro_header'
    #.@abstractmethod
    #.def token2body_digit_(sf, token, /):
    #.    'token -> digit8body_cell'
    ######################
    @property
    @abstractmethod
    def may_token2head_digit_(sf, token, /):
        '-> may (token -> digit8macro_header)'
    @property
    @abstractmethod
    def may_token2body_digit_(sf, token, /):
        '-> may (token -> digit8body_cell)'
    ######################
    @cached_property
    def token2head_digit_(sf, token, /):
        '-> (token -> digit8macro_header)'
        return f if not None is (f:=sf.may_token2head_digit_) else echo(0) or echo
    @cached_property
    def token2body_digit_(sf, token, /):
        '-> (token -> digit8body_cell)'
        return f if not None is (f:=sf.may_token2body_digit_) else echo(0) or echo
    ######################
    def iter4body_only_(sf, tokens, /):
        'Iter token -> Iter digit8body_cell/uint'
        it = tokens = iter(tokens)
        if not None is (f:=sf.may_token2body_digit_):
            it = map(f, it)
        return it
    def iter_(sf, tokens, /):
        'Iter token -> iter([rxdigit8macro_header/IRadixedDigit;digit8body_cell/uint,...])'
        it = tokens = iter(tokens)
        for token in it:
            break
        else:
            raise 000
        digit8H = sf.token2head_digit_(token)
        radix_info4H = sf.radix_info4macro_header
        rxdigit8H = RadixedDigit(radix_info4H, digit8H)
        yield rxdigit8H
        yield from sf.iter4body_only_(it)
        return
    ######################
#end-class IOps4IterDigitsWithHeadCell(ABC):
class Ops4IterDigitsWithHeadCell__functional(IOps4IterDigitsWithHeadCell):
    'ops4iter_headed_digits # functional'
    ___no_slots_ok___ = True
    def __init__(sf, radix_or_radix_info4macro_header, may_token2head_digit_, may_token2body_digit_, /):
        if not None is (token2head_digit_:=may_token2head_digit_):
            check_callable(token2head_digit_)
        if not None is (token2body_digit_:=may_token2body_digit_):
            check_callable(token2body_digit_)
        sf._riH = mk_radix_info5or_radix_(radix_or_radix_info4macro_header)
        sf._mH = may_token2head_digit_
        sf._mB = may_token2body_digit_
    def __repr__(sf, /):
        return repr_helper(sf, sf.radix_info4macro_header, sf.may_token2head_digit_, sf.may_token2body_digit_)
    @property
    @override
    def radix_info4macro_header(sf, /):
        '-> IRadixInfo'
        return sf._riH
    @property
    @override
    def may_token2head_digit_(sf, /):
        '-> may (token -> digit8macro_header)'
        return sf._mH
    @property
    @override
    def may_token2body_digit_(sf, /):
        '-> may (token -> digit8body_cell)'
        return sf._mB
#end-class Ops4IterDigitsWithHeadCell__functional(IOps4IterDigitsWithHeadCell):
check_non_ABC(Ops4IterDigitsWithHeadCell__functional)
#######
######################
#incremental_decode__continued_:related:end
######################







class IStepDecoder__flip_digits(IStepDecoder__wrapper, IStepDecoder__without_subcall):
    __slots__ = ()
    ######################
    @cached_property
    def flatten_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__flatten{.the_wrapped_step_decoder}'
        return StepDecoder__flatten(sf.the_wrapped_step_decoder)
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        loop_st = sf.flatten_wrapped_step_decoder.start_(~rxdigit8macro_header)
            #flip_rxdigit_
        return _mk_loop_st__flipped_rxdigit8remain_(loop_st)
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        loop_st = loop_st7nonfinal.payload
        _required_digits = tuple(sf.radix_info4digit.flip_digits_(required_digits))
        _loop_st = sf.flatten_wrapped_step_decoder.feed_digits_(loop_st, _required_digits)
        return _mk_loop_st__flipped_rxdigit8remain_(_loop_st)
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
    ######################
def _mk_loop_st__flipped_rxdigit8remain_(loop_st, /):
    cased_data = Cased(True, loop_st.payload) if loop_st.is_final_st else Cased(False, loop_st)
    return _LoopST(cased_data, ~loop_st.rxdigit8remain, loop_st.num_required_digits)
#end-class IStepDecoder__flip_digits(IStepDecoder__wrapper, IStepDecoder__without_subcall):
class StepDecoder__flip_digits(IStepDecoder__flip_digits):
    ___no_slots_ok___ = True
    def __init__(sf, step_decoder, /):
        sf._dr = step_decoder
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_wrapped_step_decoder)
    @property
    @override
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder'
        return sf._dr
check_non_ABC(StepDecoder__flip_digits)






class IStepDecoder__dynamic_bits(IStepDecoder__without_subcall):
    r'''[[[
    [dynamic_bits =[def]= regex"1*0"]
    [truncated_dynamic_bits{max_num_bits4read} =[def]= regex"1{0,max_num_bits4read-1}0|1{max_num_bits4read}" if max_num_bits4read > 0 else ""]

    [oresult =[def]= len_dybits/uint]
    [st == LoopState4StepDecoder__plain(b_final,acc_num_leading1s, ...)]
    #]]]'''#'''
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def imay_max_num_bits4read(sf, /):
        '-> imay max_num_bits4read/uint # for truncated_dynamic_bits{max_num_bits4read}'
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        return sf._work(0, *rxdigit8macro_header)
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        st = loop_st7nonfinal
        assert not st.case
        [digit] = required_digits
        return sf._work(st.payload, sf.radix_info4digit, digit)

    def _work(sf, acc_num_leading1s, radix_info4H, digit8H, /):
        if not 0 <= acc_num_leading1s: raise 000
        b_limit = not -1 == (__:=sf.imay_max_num_bits4read)
        if b_limit:
            max_num_bits4read = __
            max_more = max_num_bits4read -acc_num_leading1s
            if max_more == 0:
                return _LoopST.mk_loop_st5five_args_(True,acc_num_leading1s,   radix_info4H,digit8H,   0)
            if not 0 < max_more: raise 000
            # [max_more > 0]
        # b_limit => [max_more > 0]
        (num_leading1s, imay_num_bits4remain) = radix_info4H.count_num_leading1s_ex_(digit8H)
        if b_limit and max_more <= num_leading1s:
            #acc_num_leading1s = max_num_bits4read
            num_leading1s = max_more
            num_bits4remain = radix_info4H.num_bits4digit -num_leading1s
            assert num_leading1s >= 0
                # !! not include end "0"
            #bug:imay_num_bits4remain = num_leading1s
            imay_num_bits4remain = num_bits4remain
        num_leading1s
        imay_num_bits4remain
        acc_num_leading1s += num_leading1s
        if -1 == imay_num_bits4remain:
            return _LoopST(Cased(False,acc_num_leading1s),   rxdigit8no_bits,   1)
        num_bits4remain = imay_num_bits4remain
        radix_info4remain = ZpowRadixInfo(num_bits4remain)
        max_digit4remain = radix_info4remain.max_digit
        digit8remain = max_digit4remain & digit8H
        return _LoopST.mk_loop_st5five_args_(True,acc_num_leading1s,   radix_info4remain,digit8remain,   0)
#end-class IStepDecoder__dynamic_bits(IStepDecoder):

#.from seed.types.BitList import BitList
#.def bitlist5digit_(zpow8radix, digit, /):
#.    payload_uint = zpow8radix | digit
#.    return BitList(payload_uint)
class IStepDecoder__fixed_size_bits(IStepDecoder__without_subcall):
    r'''[[[
    [fixed_size_bits{num_bits4read} =[def]= regex"[01]{num_bits4read}"]

    [oresult =[def]= u8szbits/uint]
    [st == LoopState4StepDecoder__plain(b_final,(rxdigit8macro_header|u8szbits), ...)]
    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def num_bits4read(sf, /):
        '-> uint{>=0}'
        #xxx:'-> uint{>=1} # since always consume at least 1bit instead of lookahead1'
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        return sf._work(sf.num_bits4read, rxdigit8macro_header)
    ######################
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        st = loop_st7nonfinal
        assert not st.case
        assert st.num_required_digits == len(required_digits)
        (radix_info4H,digit8H) = rxdigit8H = st.payload
        num_bits4H = radix_info4H.num_bits4digit
        radix_info4digit = sf.radix_info4digit
        num_bits4digit = radix_info4digit.num_bits4digit
        num_bits4remain = num_bits4H +num_bits4digit*len(required_digits) -sf.num_bits4read
        assert 0 <= num_bits4remain < num_bits4digit
        radix_info4remain = ZpowRadixInfo(num_bits4remain)
        if num_bits4remain:
            digit = required_digits[-1]
            max_digit4remain = radix_info4remain.max_digit
            digit8remain = max_digit4remain & digit
            last_digit = digit >> num_bits4remain
            num_bits4last_digit = num_bits4digit -num_bits4remain
            num_mid_digits = len(required_digits)-1
        else:
            num_mid_digits = len(required_digits)
            last_digit = 0
            num_bits4last_digit = 0
            max_digit4remain = 0
            digit8remain = 0
        #.radix4digit = 1<<num_bits4digit
        #.bs = bitlist5digit_(1<<num_bits4H, digit8H)
        #.for digit in islice(required_digits, 0, num_mid_digits)
        #.    bs += bitlist5digit_(radix4digit, digit)
        #.bs += bitlist5digit_(1<<num_bits4last_digit, last_digit)

        #.oresult = int(bs.to_01str(), 2)
        zri4H = radix_info4H
        zri4digit = radix_info4digit
        zri4last_digit = ZpowRadixInfo(num_bits4last_digit)
        def __(zri4digit):
            yield (zri4H, digit8H)
            for digit in islice(required_digits, 0, num_mid_digits):
                yield (zri4digit, digit)
            yield (zri4last_digit, last_digit)
        oresult = concat_digits2uint_((-sf.num_bits4read)%8, __(zri4digit))
        radix_info4remain
        return _LoopST.mk_loop_st5five_args_(True,oresult,   radix_info4remain,digit8remain,   0)

    ######################
    def _work(sf, num_bits4read, rxdigit8H, /):
        (radix_info4H, digit8H) = rxdigit8H
        num_bits4H = radix_info4H.num_bits4digit
        num_bits4miss = num_bits4read -num_bits4H
        if num_bits4miss > 0:
            num_required_digits = ceil_div(num_bits4miss, sf.num_bits4digit)
            assert num_required_digits > 0
            return _LoopST(Cased(False,rxdigit8H),   rxdigit8no_bits,   num_required_digits)
        num_bits4remain = -num_bits4miss
        radix_info4remain = ZpowRadixInfo(num_bits4remain)
        max_digit4remain = radix_info4remain.max_digit
        digit8remain = max_digit4remain & digit8H
        oresult = digit8H >> num_bits4remain
        return _LoopST.mk_loop_st5five_args_(True,oresult,   radix_info4remain,digit8remain,   0)
    ######################
#end-class IStepDecoder__fixed_size_bits(IStepDecoder):

#_rx_0 = rxdigit8no_bits
class IStepDecoder__fixed_size_xbcells(IStepDecoder__without_subcall):
    r'''[[[
    [fixed_size_xbcells{num_xbcells4read} =[def]= regex"{<xbcell>}{num_xbcells4read}"]
    [xbcell =[def]= (digit8macro_header|bit|digit8body_cell)]

    [oresult =[def]= u8szxbcells/uint]
    [st == LoopState4StepDecoder__plain(b_final,(???|u8szxbcells), ...)]
    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def macro_header_extra(sf, /):
        '-> bool{whether num_xbcells4read not counting in macro_header}'
    @property
    @abstractmethod
    def offset4macro_header(sf, /):
        '-> uint{used when building u8szxbcells}'
    @property
    @abstractmethod
    def num_xbcells4read(sf, /):
        '-> uint{>=0}'
    @property
    @abstractmethod
    def is_xbcell_bit(sf, /):
        '-> bool{whether unit of num_xbcells4read is bit} # [is_xbcell_bit -> sf.radix_info4digit.is_zpow_radix] # [[[is_xbcell_bit][not macro_header_extra]] -> rxdigit8macro_header.radix_info4digit.is_zpow_radix]'
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        _rxH = rxdigit8macro_header
        if sf.macro_header_extra:
            rxH = rxdigit8no_bits
        else:
            rxH = _rxH
            _rxH = rxdigit8no_bits
        _rxH#extra
        rxH#head
        n = sf.num_xbcells4read
        check_int_ge(0, n)
        if sf.is_xbcell_bit:
            num_bits4read = n
            num_bits4H = rxH.radix_info.num_bits4digit
            num_bits4miss = num_bits4read -num_bits4H
            if num_bits4miss <= 0:
                num_bits4remain = -num_bits4miss
                return sf._finish_atH(rxdigit8macro_header, num_bits4remain)
            # [num_bits4miss > 0]
            num_bits4B = sf.num_bits4digit
            #bug:(q, r) = divmod(num_bits4B-1+num_bits4miss, num_bits4B)
            (q, r) = divmod(num_bits4miss, num_bits4B)
            num_required_digits, num_bits4remain = (q, 0) if not r else (q+1, num_bits4B-r)
            return sf._required_atH(rxdigit8macro_header, num_required_digits, num_bits4remain)
        num_xcells4read = n
        num_bits4remain = 0
        num_required_digits = num_xcells4read -(not sf.macro_header_extra)
        if num_required_digits <= 0:
            return sf._finish_atH(rxdigit8macro_header, num_bits4remain)
        return sf._required_atH(rxdigit8macro_header, num_required_digits, num_bits4remain)
    ######################
    def _finish_atH(sf, rxH, num_bits4remain, /):
        assert num_bits4remain >= 0
        # [num_bits4remain == 0] => 苞串
        # [num_bits4remain > 0] => 爻串
        if num_bits4remain==0:
            oresult = u8szxbcells = rxH.digit+sf.offset4macro_header
            return _LoopST(Cased(True,oresult),   rxdigit8no_bits,   0)
        assert not sf.macro_header_extra
        #rxH.radix_info.num_bits4digit
        u = rxH.digit#xxx:+sf.offset4macro_header
            #diff below:feed_digits_()
        (high, rxdigit8remain) = _cut_uint(num_bits4remain, u)
        oresult = u8szxbcells = high+sf.offset4macro_header
        return _LoopST(Cased(True,oresult),   rxdigit8remain,   0)
    ######################
    def _required_atH(sf, rxH, num_required_digits, num_bits4remain, /):
        assert num_required_digits > 0
        assert num_bits4remain >= 0
        # [num_bits4remain == 0] => 苞串
        # [num_bits4remain > 0] => 爻串
        payload = (rxH, num_required_digits, num_bits4remain)
        return _LoopST(Cased(False,payload),   rxdigit8no_bits,   num_required_digits)
    ######################
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        st = loop_st7nonfinal
        assert not st.case
        assert st.num_required_digits == len(required_digits)
        (rxH, num_required_digits, num_bits4remain) = st.payload
        def __():
            yield rxH.digit+sf.offset4macro_header
                #diff above:_finish_atH()
            yield from required_digits
        u = uint5radix_repr_(sf.radix4digit, __(), is_big_endian=True)
        (high, rxdigit8remain) = _cut_uint(num_bits4remain, u)
        oresult = u8szxbcells = high#xxx:+sf.offset4macro_header
        return _LoopST(Cased(True,oresult),   rxdigit8remain,   0)
    ######################
#end-class IStepDecoder__fixed_size_xbcells(IStepDecoder):
def _cut_uint(num_bits4remain, u, /):
    radix_info4remain = ZpowRadixInfo(num_bits4remain)
    digit8remain = u & radix_info4remain.max_digit
    rxdigit8remain = RadixedDigit(radix_info4remain, digit8remain)
    high = u >> num_bits4remain
    return (high, rxdigit8remain)
def _cut_low_uint(num_bits4remain, u, /):
    radix_info4remain = ZpowRadixInfo(num_bits4remain)
    digit8remain = u & radix_info4remain.max_digit
    rxdigit8remain = RadixedDigit(radix_info4remain, digit8remain)
    return rxdigit8remain



class IStepDecoder__dependent_pair(IStepDecoder):
    r'''[[[
    '[dependent_pair =[def]= (fst_part, snd_part{fst_oresult})]'

    [oresult =[def]= (fst_oresult,snd_oresult)]
    [st =[def]= final_st | call_st]
    [final_st == LoopState4StepDecoder__plain(2,(fst_oresult,snd_oresult), ..., 0)]
    [call_st == CallState4StepDecoder__plain((0|1),(None|fst_oresult), ...)]
    #]]]'''#'''
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def step_decoder4fst_part(sf, /):
        '-> IStepDecoder{fst_part}'
    @abstractmethod
    def mk_step_decoder4snd_part_(sf, fst_oresult, /):
        'fst_oresult -> IStepDecoder{snd_part{fst_oresult}}'

    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        dr4fst_part = sf.step_decoder4fst_part
        #.st4fst_part = dr4fst_part.start_(rxdigit8macro_header)
        #.return _CallST.mk_call_st5four_args_(0,None,   dr4fst_part,st4fst_part)
        return _CallST.mk_call_st5four_args_(0,None,   dr4fst_part,rxdigit8macro_header, state_vs_rxdigit=True)
    ######################
    #@override
    feed_digits_ = _Dead.feed_digits_
    ######################
    @override
    def feed_oresult_remain_(sf, call_st7nontail, oresult7subcall, rxdigit8remain7subcall, /):
        st = call_st7nontail
        match st.case:
            case 0:
                fst_oresult = oresult7subcall
                dr4snd_part = sf.mk_step_decoder4snd_part_(fst_oresult)
                #if 0b0001 and isinstance(sf, IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits):raise Exception(len_dybits:=fst_oresult, rxdigit8remain7subcall)
                return _CallST.mk_call_st5four_args_(1,fst_oresult,   dr4snd_part,rxdigit8remain7subcall, state_vs_rxdigit=True)
            case 1:
                fst_oresult = st.payload
                snd_oresult = oresult7subcall
                oresult = (fst_oresult, snd_oresult)
                rxdigit8remain = rxdigit8remain7subcall
                return _LoopST(Cased(2,oresult),   rxdigit8remain,   0)
            case _:
                raise 000
        raise 000
    ######################
#end-class IStepDecoder__dependent_pair(IStepDecoder):


def _mk_step_decoder4fixed_size_bits_(sf, num_bits4read, /):
    'num_bits4read/uint{>=0} -> IStepDecoder__fixed_size_bits{num_bits4read}/IStepDecoder__fixed_size_xbcells'
    return StepDecoder__fixed_size_xbcells(sf.radix_info4digit, offset4macro_header=0, macro_header_extra=False, num_xbcells4read=num_bits4read, is_xbcell_bit=True)


class IStepDecoder__dynamic_bits_with_dependent_size_bits(IStepDecoder__dependent_pair):
    #class IStepDecoder__dynamic_bits_with_dependent_size_bits(IStepDecoder):
    r'''[[[
    '[dynamic_bits_with_dependent_size_bits =[def]= regex"1*0[01]{len:=???}"]'

    [oresult =[def]= (len_dybits,u8szbits)]
    [st =[def]= final_st | call_st]
    [final_st == LoopState4StepDecoder__plain(2,(len_dybits,u8szbits), ..., 0)]
    [call_st == CallState4StepDecoder__plain((0|1),(None|len_dybits), ...)]
    #]]]'''#'''
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def step_decoder4dynamic_bits(sf, /):
        '-> IStepDecoder__dynamic_bits'
    ######################
    #@abstractmethod
    def mk_step_decoder4fixed_size_bits_(sf, num_bits4read, /):
        'num_bits4read/uint{>=0} -> IStepDecoder__fixed_size_bits{num_bits4read}/IStepDecoder__fixed_size_xbcells'
        return _mk_step_decoder4fixed_size_bits_(sf, num_bits4read)
    @abstractmethod
    def num_bits4read5len_dybits_(sf, len_dybits, /):
        'len_dybits/uint{>=0} -> num_bits4read{>=0}'
    ######################

    ######################
    @property
    @override
    def step_decoder4fst_part(sf, /):
        '-> IStepDecoder{fst_part}'
        dr4dybits = sf.step_decoder4dynamic_bits
        return dr4dybits
    @override
    def mk_step_decoder4snd_part_(sf, fst_oresult, /):
        'fst_oresult -> IStepDecoder{snd_part{fst_oresult}}'
        len_dybits = fst_oresult
        num_bits4read = sf.num_bits4read5len_dybits_(len_dybits)
        dr4szbits = sf.mk_step_decoder4fixed_size_bits_(num_bits4read)
        return dr4szbits
    ######################

    ######################
    ###before:IStepDecoder__dependent_pair###
    #.######################
    #.@override
    #.def start_(sf, rxdigit8macro_header, /):
    #.    dr4dybits = sf.step_decoder4dynamic_bits
    #.    return _CallST.mk_call_st5four_args_(0,None,   dr4dybits,rxdigit8macro_header, state_vs_rxdigit=True)
    #.######################
    #.#@override
    #.feed_digits_ = _Dead.feed_digits_
    #.######################
    #.@override
    #.def feed_oresult_remain_(sf, call_st7nontail, oresult7subcall, rxdigit8remain7subcall, /):
    #.    st = call_st7nontail
    #.    match st.case:
    #.        case 0:
    #.            len_dybits = oresult7subcall
    #.            num_bits4read = sf.num_bits4read5len_dybits_(len_dybits)
    #.            dr4szbits = sf.mk_step_decoder4fixed_size_bits_(num_bits4read)
    #.            return _CallST.mk_call_st5four_args_(1,len_dybits,   dr4szbits,rxdigit8remain7subcall, state_vs_rxdigit=True)
    #.        case 1:
    #.            len_dybits = st.payload
    #.            u8szbits = oresult7subcall
    #.            oresult = (len_dybits, u8szbits)
    #.            rxdigit8remain = rxdigit8remain7subcall
    #.            return _LoopST(Cased(2,oresult),   rxdigit8remain,   0)
    #.        case _:
    #.            raise 000
    #.    raise 000
    #.######################
#end-class IStepDecoder__dynamic_bits_with_dependent_size_bits(IStepDecoder):

class IStepDecoder__fixed_radix4macro_header(IStepDecoder):
    __slots__ = ()
    @property
    @abstractmethod
    def radix_info4macro_header(sf, /):
        '-> IRadixInfo # [radix_info4macro_header == start_()::rxdigit8macro_header.radix_info]'
    @property
    def radix4macro_header(sf, /):
        '-> uint{>=1} # [radix4macro_header == start_()::rxdigit8macro_header.radix_info.radix]'
        return sf.radix_info4macro_header.radix
    ######################
    @abstractmethod
    @override#update:__doc__
    def start_(sf, rxdigit8macro_header, /):
        'rxdigit8macro_header/IRadixedDigit{radix==sf.radix4macro_header} -> st/IBaseState4StepDecoder # allow [num_bits4macro_header > num_bits4digit]'
        assert rxdigit8macro_header.radix_info.radix == sf.radix4macro_header
        ...
    ######################

class IStepDecoder__skip_macro_header(IStepDecoder__fixed_radix4macro_header, IStepDecoder__wrapper):
    #深入型
    __slots__ = ()
    #@override
    radix_info4macro_header = rxdigit8no_bits.radix_info
    @override
    def start_(sf, rxdigit8macro_header, /):
        assert rxdigit8macro_header.is_null
        return _LoopST(Cased(False,None),   rxdigit8macro_header,   1)
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        [digit] = required_digits
        step_decoder = sf.the_wrapped_step_decoder
        rxdigit8remain = rxdigit8fst_digit = RadixedDigit(step_decoder.radix_info4digit, digit)
        return _TCallST.mk_tail_call_st5three_args_(None,   step_decoder,rxdigit8remain, state_vs_rxdigit=True)
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
#end-class IStepDecoder__skip_macro_header(IStepDecoder__fixed_radix4macro_header, IStepDecoder__wrapper):
class IStepDecoder__extend_macro_header(IStepDecoder__fixed_radix4macro_header, IStepDecoder__wrapper):
    #糅合深入型
    __slots__ = ()
    @override
    def start_(sf, rxdigit8macro_header, /):
        return _LoopST(Cased(False,None),   rxdigit8macro_header,   1)
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        rxdigit8macro_header = loop_st7nonfinal.rxdigit8remain
        [digit] = required_digits
        step_decoder = sf.the_wrapped_step_decoder
        #rxdigit8fst_digit = RadixedDigit(step_decoder.radix_info4digit, digit)
        radix6high = rxdigit8macro_header.radix_info.radix
        if radix6high == 1:
            rxdigit8remain = RadixedDigit(step_decoder.radix_info4digit, digit)
        else:
            radix6low = step_decoder.radix_info4digit.radix
            radix4remain = radix6high*radix6low
            radix_info4remain = RadixInfo(radix4remain)
            digit8macro_header = rxdigit8macro_header.digit
            digit8remain = digit8macro_header*radix6low + digit
            rxdigit8remain = RadixedDigit(radix_info4remain, digit8remain)
        rxdigit8remain
        return _TCallST.mk_tail_call_st5three_args_(None,   step_decoder,rxdigit8remain, state_vs_rxdigit=True)
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
#end-class IStepDecoder__extend_macro_header(IStepDecoder__fixed_radix4macro_header, IStepDecoder__wrapper):




class IStepDecoder__parallel__partition_space4macro_header(IStepDecoder__fixed_radix4macro_header):
    #并联型
    __slots__ = ()
    @property
    @abstractmethod
    def child_step_decoder_seq(sf, /):
        '-> nonempty [IStepDecoder__fixed_radix4macro_header]{sum(child_step_decoder.radix4macro_header for child_step_decoder in child_step_decoder_seq) == sf.radix4macro_header} #radix_info4digit require nonempty'
    @cached_property
    def accumulated_radix_seq(sf, /):
        return tuple(accumulate(step_decoder.radix4macro_header for step_decoder in sf.child_step_decoder_seq))
    @cached_property
    @override
    def radix_info4macro_header(sf, /):
        return RadixInfo(sf.accumulated_radix_seq[-1])
        #.radix4H = sum(step_decoder.radix4macro_header for step_decoder in sf.child_step_decoder_seq)
        #.radix_info4H = RadixInfo(radix4H)
        #.return radix_info4H
    @cached_property
    @override
    def radix_info4digit(sf, /):
        return sf.child_step_decoder_seq[0].radix_info4digit
    @override
    def start_(sf, rxdigit8macro_header, /):
        assert rxdigit8macro_header.radix_info.radix == sf.radix4macro_header
        digit = rxdigit8macro_header.digit
        check_int_ge(0, digit)
        accumulated_radix_seq = sf.accumulated_radix_seq
        j = bisect_right(accumulated_radix_seq, digit)
        child_step_decoder = sf.child_step_decoder_seq[j]
        #.assert j==0 or digit >= accumulated_radix_seq[j-1]
        #.assert digit < accumulated_radix_seq[j]
        radix4H = child_step_decoder.radix4macro_header
        digit -= accumulated_radix_seq[j-1] if j else 0
        assert 0 <= digit < radix4H
        #.for child_step_decoder in sf.child_step_decoder_seq:
        #.    radix4H = child_step_decoder.radix4macro_header
        #.    if digit < radix4H:
        #.        break
        #.    digit -= radix4H
        #.else:
        #.    raise 000
        child_step_decoder
        digit
        rxdigit8remain = RadixedDigit(child_step_decoder.radix_info4macro_header, digit)
        return _TCallST.mk_tail_call_st5three_args_(None,   child_step_decoder,rxdigit8remain, state_vs_rxdigit=True)
    #@override
    feed_digits_ = _Dead.feed_digits_
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
#end-class IStepDecoder__parallel__partition_space4macro_header(IStepDecoder__fixed_radix4macro_header):

r'''[[[
DONE:IStepDecoder__dynamic_bibits{body_bibit:="10"}
    bibit:two bit
    xxx:regex"(10)*(0|11)"
    regex"(01)*(00|1)"
    IStepDecoder__dynamic_bits.imay_max_num_bits4read
    [imay_max_num_bits4read==-1]:
        regex"1*0"
    [imay_max_num_bits4read==0]:
        regex"(01)*(00|1)"
    [imay_max_num_bits4read>=1]:
        regex"1{0,max_num_bits4read-1}0|1{max_num_bits4read}(01)*(00|1)"

TODO:IStepDecoder__dynamic_nbits{imay_max_num_bits4read,body_nbit}
    nbit:n bit
    [body_nbit:=regex"10{n-1}"]
        regex"(10{n-1})*(0|10{0,n-2}1|1{2,n-1}0|11)"
    =>
    #前缀打断:n种 结束串:
    regex"({<body_nbit>})*({<or:body_nbit[:j]++[~body_nbit[j]] for j in [0..<n]>})"
e ../../python3_src/seed/int_tools/PrefixDecoder.py
#]]]'''#'''


class IStepDecoder__dynamic_bibits(IStepDecoder__without_subcall):
    r'''[[[
    [dynamic_bibits =[def]= regex"(01)*(00|1)"]

    [oresult =[def]= Either u00 u1 ~= (LSB, num_periods)]
    [st == LoopState4StepDecoder__plain(b_final,(acc_num_bits, prev_LSB), ...)]
    #]]]'''#'''

    r'''[[[
view others/数学/编程/设计/自定义编码之要点.txt
    +截断动态爻元串{N}: regex"1{0,N-1}0|1{N}"
    +无限保留区甲型: regex"(01)*(00|1)"
    +[N>=0]截断动态爻元串后继无限保留区{N} == 截断动态爻元串后继无限保留区甲型{N+1}: regex"1{0,N-1}0|1{N}(01)*(00|1)"
        #相当于 在最大截断动态爻元串之后接上无限保留区甲型 #最大 以1结尾  不论是否存在 假设最后一位是1
        ==(截断动态爻元串{N},[全一截断]=>无限保留区甲型)
    #]]]'''#'''
    __slots__ = ()
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        return sf._work(0, 1, *rxdigit8macro_header)
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        st = loop_st7nonfinal
        assert not st.case
        [digit] = required_digits
        assert st.rxdigit8remain is rxdigit8no_bits
        (acc_num_bits, prev_LSB) = st.payload
        return sf._work(acc_num_bits, prev_LSB, sf.radix_info4digit, digit)

    def _work(sf, acc_num_bits, prev_LSB, radix_info4H, digit8H, /):
        if not 0 <= acc_num_bits: raise 000
        assert 0 <= prev_LSB < 2
        assert (1^prev_LSB) == (acc_num_bits&1)
        #######
        def _mk_final_st(acc_num_bits, num_bits4remain, /):
            #nonlocal L, digit8H
            num_bits4consumed = acc_num_bits + (L-num_bits4remain)
            (high, rxdigit8remain) = _cut_uint(num_bits4remain, digit8H)
            LSB = num_bits4consumed&1
            assert LSB == (high&1)
            num_periods = (num_bits4consumed-1) >> 1
            LSB = bool(LSB)
            oresult = Either(LSB, num_periods)
            #if 0b0001:raise Exception(oresult, (acc_num_bits, prev_LSB, radix_info4H, digit8H))
            return _LoopST(Cased(True,oresult),   rxdigit8remain,   0)
        #end-def _mk_final_st(acc_num_bits, num_bits4remain, /):
        #######

        if (L:=radix_info4H.num_bits4digit) == 0:
            return _LoopST(Cased(False,(acc_num_bits,prev_LSB)),   rxdigit8no_bits,   1)

        # [L >= 1]
        MSB = digit8H >> (L-1)
        if MSB == prev_LSB:
            LSB = prev_LSB
            #move into _mk_final_st():acc_num_bits += 1
            return _mk_final_st(acc_num_bits, num_bits4remain:=L-1)

        #MSB=!=prev_LSB
        #drop:prev_LSB
        radix_info4_h = ZpowRadixInfo(L-1)
        u = (digit8H ^ ~(digit8H>>1)) & (radix_info4_h.max_digit)
            # L:=4
            # abcd --> 0abcd --> 1ABC
            # (abcd ^ 1ABC) & 0111 --> (bcd ^ ABC)
        n = u.bit_length()
        if n == 0:
            acc_num_bits += L
            prev_LSB = digit8H&1
            return _LoopST(Cased(False,(acc_num_bits,prev_LSB)),   rxdigit8no_bits,   1)
        #######
        # n:=3
        # (bcd ^ ABC) --> 1zz
        # b=!=A
        # b==a
        # num_bits4remain := n-1 =2
        # delta{acc_num_bits} == 2==4-(3-1)==L-num_bits4remain
        #######

        #move into _mk_final_st():acc_num_bits += L-num_bits4remain
        return _mk_final_st(acc_num_bits, num_bits4remain:=n-1)
#end-class IStepDecoder__dynamic_bibits(IStepDecoder__without_subcall):
class IStepDecoder__init_radix_info4digit(IStepDecoder):
    ___no_slots_ok___ = True
    def __init__(sf, radix_info4digit, /):
        check_radix_info4digit(radix_info4digit)
        sf._ri = radix_info4digit
    def __repr__(sf, /):
        return repr_helper(sf, sf.radix_info4digit)
    ######################
    @property
    @override
    def radix_info4digit(sf, /):
        '-> IRadixInfo{radix>=2}'
        return sf._ri
    ######################
#end-class IStepDecoder__init_radix_info4digit(IStepDecoder):

class StepDecoder__dynamic_bibits(IStepDecoder__init_radix_info4digit, IStepDecoder__dynamic_bibits):
    ___no_slots_ok___ = True
check_non_ABC(StepDecoder__dynamic_bibits)
['radix_info4digit']

class StepDecoder__dynamic_bits(IStepDecoder__dynamic_bits):
    ___no_slots_ok___ = True
    def __init__(sf, radix_info4digit, imay_max_num_bits4read, /):
        check_radix_info4digit(radix_info4digit)
        check_int_ge(-1, imay_max_num_bits4read)
        sf._riB = radix_info4digit
        sf._im = imay_max_num_bits4read
    def __repr__(sf, /):
        return repr_helper(sf, sf.radix_info4digit, sf.imay_max_num_bits4read)
    ######################
    @property
    @override
    def radix_info4digit(sf, /):
        return sf._riB
    @property
    @override
    def imay_max_num_bits4read(sf, /):
        return sf._im
    ######################
check_non_ABC(StepDecoder__dynamic_bits)




class IStepDecoder__constant_oresult(IStepDecoder):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def oresult(sf, /):
        '-> object'
    ######################
    #@override
    feed_digits_ = _Dead.feed_digits_
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
    @override
    def start_(sf, rxdigit8macro_header, /):
        return _LoopST(Cased(True, sf.oresult),   rxdigit8macro_header,   0)
#end-class IStepDecoder__constant_oresult(IStepDecoder):

class StepDecoder__constant_oresult(IStepDecoder__constant_oresult):
    ___no_slots_ok___ = True
    def __init__(sf, radix_info4digit, oresult, /):
        sf._ri = radix_info4digit
        sf._o = oresult
    def __repr__(sf, /):
        return repr_helper(sf, sf.radix_info4digit, sf.oresult)
    ######################
    @property
    @override
    def radix_info4digit(sf, /):
        '-> IRadixInfo{radix>=2}'
        return sf._ri
    @property
    @override
    def oresult(sf, /):
        return sf._o
    ######################
#step_decoder4oresult_be_None = StepDecoder__constant_oresult(???, None)


class IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits(IStepDecoder__dependent_pair):
    r'''[[[
    '[truncated_dynamic_bits_with_may_dynamic_bibits{max_num_bits4read} =[def]= regex"1{0,max_num_bits4read-1}0|1{max_num_bits4read}(01)*(00|1)"]'

    [oresult =[def]= (len_dybits,may either_num_periods/(Either num_periods_00 num_periods_1)){[[len_dybits==max_num_bits4read]<->[may_either_num_periods is not None]]}]
    [st =[def]= final_st | call_st]
    [final_st == LoopState4StepDecoder__plain(2,(len_dybits,may_either_num_periods), ..., 0)]
    [call_st == CallState4StepDecoder__plain((0|1),(None|len_dybits), ...)]
    #]]]'''#'''
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def step_decoder4dynamic_bits(sf, /):
        '-> IStepDecoder__dynamic_bits{imay_max_num_bits4read}'
    @property
    @abstractmethod
    def step_decoder4dynamic_bibits(sf, /):
        '-> IStepDecoder__dynamic_bibits'
    ######################
    @property
    def imay_max_num_bits4read(sf, /):
        '-> (imay max_num_bits4read)/int{>=-1}'
        return sf.step_decoder4dynamic_bits.imay_max_num_bits4read

    ######################
    @property
    @override
    def step_decoder4fst_part(sf, /):
        '-> IStepDecoder{fst_part}'
        dr4dybits = sf.step_decoder4dynamic_bits
        return dr4dybits
    @override
    def mk_step_decoder4snd_part_(sf, fst_oresult, /):
        'fst_oresult -> IStepDecoder{snd_part{fst_oresult}}'
        len_dybits = fst_oresult
        #if 0b0001:raise Exception(len_dybits)
        if len_dybits == sf.step_decoder4dynamic_bits.imay_max_num_bits4read:
            dr4dybibits = sf.step_decoder4dynamic_bibits
            return dr4dybibits
        dr4oresult_be_None = StepDecoder__constant_oresult(sf.radix_info4digit, None)
        return dr4oresult_be_None
    ######################

#end-class IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits(IStepDecoder):

#_BaseStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits = mk_namedtuple__check6make_(__name__, 'BaseStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits', 'radix_info4digit step_decoder4dynamic_bits step_decoder4dynamic_bibits')
class StepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits(IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits):
    ___no_slots_ok___ = True
    def __init__(sf, radix_info4digit, imay_max_num_bits4read, /):
        check_radix_info4digit(radix_info4digit)
        check_int_ge(-1, imay_max_num_bits4read)
        sf._riB = radix_info4digit
        sf._im = imay_max_num_bits4read
    def __repr__(sf, /):
        return repr_helper(sf, sf.radix_info4digit, sf.imay_max_num_bits4read)
    ######################
    @property
    @override
    def radix_info4digit(sf, /):
        return sf._riB
    @property
    @override
    def imay_max_num_bits4read(sf, /):
        return sf._im
    ######################
    ######################
    @cached_property
    @override
    def step_decoder4dynamic_bits(sf, /):
        '-> IStepDecoder__dynamic_bits{imay_max_num_bits4read}'
        return StepDecoder__dynamic_bits(sf.radix_info4digit, sf.imay_max_num_bits4read)
    @cached_property
    @override
    def step_decoder4dynamic_bibits(sf, /):
        '-> IStepDecoder__dynamic_bibits'
        return StepDecoder__dynamic_bibits(sf.radix_info4digit)
    ######################
check_non_ABC(StepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits)
['radix_info4digit', 'step_decoder4dynamic_bibits', 'step_decoder4dynamic_bits']



class IUIntCompressor(ABC):
    r'''[[[
uint_compressor
允许 有损压缩:
    但是:末层(数据负载层)只能用 无损压缩(即:偏移/offset)，不能使用 有损压缩

有损压缩:lossy
    #直接跳过某些串长:eg:非平凡步长
    offset firstly
    then:
        *bisect_left
        *ceil_div
无损压缩:lossless
    offset only

[u,v:<-[0..]]:
    [0 <= compress(u) <= u]
    [uncompress(v) >= v >= 0]
    #允许 有损压缩:不允许解压值小于被压缩值:
    [uncompress(compress(u)) >= u]
        # 『>=』
    #无损压缩:
    [[lossy==False] -> [uncompress(compress(u)) == u]]
    #再压缩不变性:
    [[v == compress(u)] -> [compress(uncompress(v)) == v]]
        # 『==』
    #递增:
    [[u < v] -> [compress(u) <= compress(v)]]
        # 『<=』
    #?严格递增:
    [[u < v] -> [uncompress(u) < uncompress(v)]]
        # 『<』

eg: [offset:<-[0..]][u:<-[offset..]][v:<-[0..]][R:<-[2..]]:
    [uncompress(v) := (v*R+offset)]
    [compress(u) := (u-offset-1)//R+1]
        # == ceil((u-offset)/R)

    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def lossy(sf, /):
        '-> bool'
    #.@property
    #.@abstractmethod
    #.def offset(sf, /):
    #.    '-> uint =?= min_legal_uncompressed_uint'
    @abstractmethod
    def compress(sf, u, /):
        'big_uint -> small_uint #eg:u-offset'
    @abstractmethod
    def uncompress(sf, v, /):
        'small_uint -> big_uint #eg:u+offset'
    @cached_property
    def min_legal_uncompressed_uint(sf, /):
        '-> offset/(min_legal_big_uint{>=0})'
        return sf.uncompress(0)
        return sf.offset
    def min_legal_uncompressed_uint_ge(sf, u, /):
        'u/big_uint -> min_legal_big_uint{>=u}'
        v = sf.compress(u)
        _u = sf.uncompress(v)
        _v = sf.compress(_u)
        if not 0 <= v == _v <= u <= _u:raise Exception((u, v, _u, _v))
        return _u


#class IUIntCompressor__bisect_left(IUIntCompressor):
#class IUIntCompressor__ceil_div(IUIntCompressor):
class IUIntLinearTransform(IUIntCompressor):
    #<==>IUIntCompressor__ceil_div
    'u->(u*scale+offset)'
    __slots__ = ()
    ###########
    @property
    @abstractmethod
    def offset(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def scale(sf, /):
        '-> uint{>=1} # scale/step'
    ###########
    @property
    @override
    def min_legal_uncompressed_uint(sf, /):
        return sf.offset
    @property
    @override
    def lossy(sf, /):
        '-> bool'
        return not sf.scale == 1
    ###########
    def uint_linear_transform(sf, u, /):
        'small_uint -> big_uint # [big_uint==(small_uint*scale+offset)]'
        return sf.uncompress(u)
    ###########
    @override
    def compress(sf, u, /):
        'big_uint -> small_uint # [small_uint == ceil_div(big_uint-offset,scale)]'
        #xxx:'big_uint -> small_uint # [small_uint == (big_uint-offset)//scale]'
        #bug:return (u -sf.offset-1)//sf.scale
        #   !! IUIntLinearTransform <==>IUIntCompressor__ceil_div
        #   !! 不允许解压值小于被压缩值:[uncompress(compress(u)) >= u]

        #return ceil_div(u -sf.offset, sf.scale)
        return 1+(u -sf.offset-1)//sf.scale
    @override
    def uncompress(sf, u, /):
        'small_uint -> big_uint # [big_uint==(small_uint*scale+offset)]'
        #return sf.uint_linear_transform(u)
        return u*sf.scale + sf.offset
#end-class IUIntLinearTransform(IUIntCompressor):

class UIntLinearTransform(IUIntLinearTransform):
    ___no_slots_ok___ = True
    def __init__(sf, scale, offset, /):
        check_int_ge(1, scale)
        check_int_ge(0, offset)
        sf._sc = scale
        sf._off = offset
    def __repr__(sf, /):
        return repr_helper(sf, sf.scale, sf.offset)
    ######################
    @property
    @override
    def scale(sf, /):
        return sf._sc
    @property
    @override
    def offset(sf, /):
        return sf._off
    ######################
#end-class UIntLinearTransform(IUIntLinearTransform):


class Exception__min_layer_idx4end_by_cell_boundary(Exception):pass
rxdigit8one = RadixedDigit(ZpowRadixInfo(1), 1)
rxdigit8two = RadixedDigit(ZpowRadixInfo(2), 2)
class IStepDecoder__fixed_size_layers__functional(IStepDecoder):
    __slots__ = ()
    ######################
    #.class IStepDecoder__fixed_size_layers__functional(IStepDecoder__fixed_radix4macro_header):
    #.@property
    #.@abstractmethod
    #.def radix_info4macro_header(sf, /):
    #.    '-> IRadixInfo{radix>=1} # clipped macro_header'
    ######################
    @property
    @abstractmethod
    def step_decoder4fixed_size_xbcells4zeroth_layer(sf, /):
        '-> IStepDecoder__fixed_size_xbcells'
    @property
    @abstractmethod
    def num_layers(sf, /):
        '-> uint{>=1}'
    @property
    @abstractmethod
    def min_layer_idx4end_by_cell_boundary(sf, /):
        '-> uint%num_layers'
    ######################
    @abstractmethod
    def layer_idx2uint_linear_transform_(sf, layer_idx, /):
        'layer_idx/uint%num_layers -> IUIntLinearTransform # [layer_idx2uint_linear_transform_(num_layers-1).scale==1] # an uniform format instead of seperate the last layer offset'
    #@abstractmethod
    def mk_step_decoder4fixed_size_bits_(sf, num_bits4read, /):
        'num_bits4read/uint -> IStepDecoder__fixed_size_bits{num_bits4read}/IStepDecoder__fixed_size_xbcells'
        return _mk_step_decoder4fixed_size_bits_(sf, num_bits4read)
    ######################
    @property
    def idx4last_layer(sf, /):
        '-> uint%num_layers # [idx4last_layer == num_layers-1]'
        return sf.num_layers-1

    ######################
    @cached_property
    @override
    def radix_info4digit(sf, /):
        return sf.step_decoder4fixed_size_xbcells4zeroth_layer.radix_info4digit
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        'rxdigit8macro_header/IRadixedDigit -> st/IBaseState4StepDecoder # allow [num_bits4macro_header > num_bits4digit]'
        #???:assert rxdigit8macro_header.radix_info.radix == sf.radix_info4macro_header.radix
        #   !! 有限区插件才需要,无限区插件无需
        #######
        #move to:IStepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval
            #.if rxdigit8macro_header.is_null:
            #.    rxdigit8macro_header = rxdigit8one
        #######
        dr4fst_part = sf.step_decoder4fixed_size_xbcells4zeroth_layer
        case = layer_idx = 0
        return _CallST.mk_call_st5four_args_(case,None,   dr4fst_part,rxdigit8macro_header, state_vs_rxdigit=True)
    #@override
    feed_digits_ = _Dead.feed_digits_
    @override
    def feed_oresult_remain_(sf, call_st7nontail, oresult7subcall, rxdigit8remain7subcall, /):
        layer_idx = call_st7nontail.case
        rxdigit8remain = rxdigit8remain7subcall
        #######
        if layer_idx >= sf.min_layer_idx4end_by_cell_boundary:
            # check no remain bits
            if not rxdigit8remain.is_null:raise Exception__min_layer_idx4end_by_cell_boundary(layer_idx, sf.min_layer_idx4end_by_cell_boundary, rxdigit8remain, sf) #raise 000
                #StepDecoder__fixed_size_layers__body4infinite_uint_interval(ZpowRadixInfo(5), 2)
                #   (1, 0, RadixedDigit(ZpowRadixInfo(1), 0), sf)
        #######
        u = oresult7subcall
        v = sf._uncompress_at_(layer_idx, u)
            #if layer_idx == 0 and sf.radix_info4macro_header.is_null: assert u == 0 and v == 1

        #cancel shortcut:case = 1+layer_idx if not v == 0 else sf.num_layers
        #   !! offset may lead to nonzero value
        #   # 只有 无限区/超凡层{超层+多凡层} 才 保证 IUIntLinearTransform(scale:=sf.num_bits4digit, offset:=0)
        #   # 有限区/多凡层 offset 不一定是0
        #######
        case = 1+layer_idx
        if case == sf.num_layers:
            #final
            oresult = v
            return _LoopST(Cased(case,oresult),   rxdigit8remain,   0)
        assert 0 <= case < sf.num_layers
        num_bits4read = v
        #if 0b0001 and not num_bits4read%sf.num_bits4digit==0: raise Exception(num_bits4read, sf.num_bits4digit, sf)
        #if 0b0001 and not rxdigit8remain.radix_info.num_bits4digit==0: raise Exception(rxdigit8remain, sf)
        dr4next_part = sf.mk_step_decoder4fixed_size_bits_(num_bits4read)
        return _CallST.mk_call_st5four_args_(case,None,   dr4next_part,rxdigit8remain, state_vs_rxdigit=True)
    ######################
    def _uncompress_at_(sf, layer_idx, u, /):
        return sf.layer_idx2uint_linear_transform_(layer_idx).uncompress(u)
        #.return sf.layer_idx2uint_linear_transform[layer_idx].uncompress(u)
        #.(j2Tr, offset4last_layer) = sf.uint_linear_transforms4each_layer
        #.if layer_idx == sf.idx4last_layer:
        #.    v = u +offset4last_layer
        #.else:
        #.    v = j2Tr[layer_idx].uncompress(u)
        #.v
        #.return v
    ######################
#end-class IStepDecoder__fixed_size_layers__functional(IStepDecoder):
assert not hasattr(IStepDecoder__fixed_size_layers__functional, 'radix_info4macro_header')

assert not hasattr(IStepDecoder__fixed_size_xbcells, 'radix_info4macro_header')
class IStepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval(IStepDecoder__fixed_size_xbcells):
    '[zeroth_layer==layer0==meta_layer]' ' # layer0 is the fst incomplete xcell/rxdigit8macro_header:[rxdigit8no_bits-->rxdigit8one][[radix4digit==2] -> [offset4zero_layer:=+1]]'
    __slots__ = ()
    #`offset4macro_header

    ######################
    #.#@override
    #.macro_header_extra = False
    #.#@override
    #.num_xbcells4read = 1
    #.#@override
    #.is_xbcell_bit = False
    ######################
    #@override
    macro_header_extra = True
    #@override
    num_xbcells4read = 0
    #@override
    is_xbcell_bit = False
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        #######
        if rxdigit8macro_header.is_null:
            rxdigit8macro_header = rxdigit8one
        #######
        if sf.radix4digit == 2 and rxdigit8macro_header.radix_info.radix < 3:
            rxdigit8macro_header = rxdigit8two
        #######
        return super().start_(rxdigit8macro_header)
    ######################
assert not hasattr(IStepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval, 'radix_info4macro_header')
class StepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval(IStepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval):
    ___no_slots_ok___ = True
    def __init__(sf, radix_info4digit, offset4macro_header, /):
        check_int_ge(0, offset4macro_header)
        sf._ri = radix_info4digit
        sf._off = offset4macro_header
    def __repr__(sf, /):
        return repr_helper(sf, sf.radix_info4digit, sf.offset4macro_header)
    ######################
    @property
    @override
    def radix_info4digit(sf, /):
        return sf._ri
    @property
    @override
    def offset4macro_header(sf, /):
        return sf._off
    ######################
check_non_ABC(StepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval)

_BaseStepDecoder__fixed_size_xbcells = mk_namedtuple__check6make_(__name__, 'BaseStepDecoder__fixed_size_xbcells', 'radix_info4digit offset4macro_header macro_header_extra num_xbcells4read is_xbcell_bit')
class StepDecoder__fixed_size_xbcells(_BaseStepDecoder__fixed_size_xbcells, IStepDecoder__fixed_size_xbcells):
    ___no_slots_ok___ = True
    def _check6make_(sf, /):
        check_radix_info4digit(sf.radix_info4digit)
        check_int_ge(0, sf.offset4macro_header)
        check_type_is(bool, sf.macro_header_extra)
        check_int_ge(0, sf.num_xbcells4read)
        check_type_is(bool, sf.is_xbcell_bit)
check_non_ABC(StepDecoder__fixed_size_xbcells)


uint_linear_transform8echo = UIntLinearTransform(1, 0)
StepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval
class IStepDecoder__fixed_size_layers__body4infinite_uint_interval(IStepDecoder__fixed_size_layers__functional):
    # see:深入型,糅合深入型
    'layer0 is the fst incomplete xcell/rxdigit8macro_header:[rxdigit8no_bits-->rxdigit8one][[radix4digit==2] -> [offset4zero_layer:=+1]]; all IUIntLinearTransform{layer_idx>=1} be {scale=num_bits4digit,offset:=0}'
    __slots__ = ()
    ######################
    @property
    @override
    def step_decoder4fixed_size_xbcells4zeroth_layer(sf, /):
        '-> IStepDecoder__fixed_size_xbcells #IStepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval'
        return StepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval(sf.radix_info4digit, offset4macro_header:=0)
    #@override
    min_layer_idx4end_by_cell_boundary = 0
    ######################
    @override
    def layer_idx2uint_linear_transform_(sf, layer_idx, /):
        #bug:return uint_linear_transform8echo
        #bug:return UIntLinearTransform(sf.num_bits4digit, 0)
        return uint_linear_transform8echo if layer_idx == sf.idx4last_layer else UIntLinearTransform(sf.num_bits4digit, 0)
    #.@override
    #.def mk_step_decoder4fixed_size_bits_(sf, num_bits4read, /):
    #.    'num_bits4read/uint -> IStepDecoder__fixed_size_bits{num_bits4read}/IStepDecoder__fixed_size_xbcells'
    #.    return StepDecoder__fixed_size_xbcells(sf.radix_info4digit, offset4macro_header=0, macro_header_extra=False, num_xbcells4read=num_bits4read, is_xbcell_bit=True)
    ######################
#end-class IStepDecoder__fixed_size_layers__body4infinite_uint_interval(IStepDecoder__fixed_size_layers__functional):
assert not hasattr(IStepDecoder__fixed_size_layers__body4infinite_uint_interval, 'radix_info4macro_header')

_BaseStepDecoder__fixed_size_layers__body4infinite_uint_interval = mk_namedtuple__check6make_(__name__, 'BaseStepDecoder__fixed_size_layers__body4infinite_uint_interval', 'radix_info4digit num_layers')
class StepDecoder__fixed_size_layers__body4infinite_uint_interval(_BaseStepDecoder__fixed_size_layers__body4infinite_uint_interval, IStepDecoder__fixed_size_layers__body4infinite_uint_interval):
    ___no_slots_ok___ = True
    def _check6make_(sf, /):
        check_radix_info4digit(sf.radix_info4digit)
        check_int_ge(1, sf.num_layers)
check_non_ABC(StepDecoder__fixed_size_layers__body4infinite_uint_interval)

def check_uint_with_unit(uint_with_unit, /):
    check_pair(uint_with_unit)
    (u, unit) = uint_with_unit
    check_int_ge(0, u)
    check_unit(unit)
def check_unit(unit, /):
    '[Unit=[def]=uint_vs_bit_vs_xcell/uint%3|num_xcells6layer{neg_idx4layer==1-this}/uint{>=3}]'
    check_int_ge(0, unit)
#class IStepDecoder__plugin4uint_interval__base(IStepDecoder):
class IStepDecoder__plugin4uint_interval__base(IStepDecoder__fixed_radix4macro_header):
    # !! IStepDecoder__parallel__partition_space4macro_header.child_step_decoder_seq require IStepDecoder__fixed_radix4macro_header
    '[Unit=[def]=uint_vs_bit_vs_xcell/uint%3|num_xcells6layer{neg_idx4layer==1-this}/uint{>=3}]'
    __slots__ = ()
    ######################
    @property
    #@abstractmethod
    def is_finite_uint_interval(sf, /):
        '-> bool'
        return type(sf.emay_may_max1_with_unit4finite_uint_interval) is int
    @property
    @abstractmethod
    def min_with_unit4uint_interval(sf, /):
        '-> (uint, Unit)'
    @property
    @abstractmethod
    def emay_may_max1_with_unit4finite_uint_interval(sf, /):
        '-> (...|None|(uint, Unit)) # [...=>include +oo][None=>infinite_uint_interval]'
    ######################
#end-class IStepDecoder__plugin4uint_interval__base(IStepDecoder):
class IStepDecoder__plugin4finite_uint_interval(IStepDecoder__plugin4uint_interval__base):
    __slots__ = ()
    #@override
    is_finite_uint_interval = True
    ######################
    @property
    @abstractmethod
    def max1_with_unit4finite_uint_interval(sf, /):
        '-> (uint, Unit)'
    ######################
    @property
    @override
    def emay_may_max1_with_unit4finite_uint_interval(sf, /):
        return sf.max1_with_unit4finite_uint_interval
    ######################
#end-class IStepDecoder__plugin4finite_uint_interval(IStepDecoder__plugin4uint_interval__base):
class IStepDecoder__plugin4infinite_uint_interval(IStepDecoder__plugin4uint_interval__base):
    __slots__ = ()
    #@override
    is_finite_uint_interval = False
    ######################
    @property
    @abstractmethod
    def included_inf(sf, /):
        '-> bool{include +oo}'
    ######################
    @property
    @override
    def emay_may_max1_with_unit4finite_uint_interval(sf, /):
        return ... if sf.included_inf else None
    ######################
#end-class IStepDecoder__plugin4infinite_uint_interval(IStepDecoder__plugin4uint_interval__base):



class ReservedAreaException(Exception):pass
    #reserved_area{num_periods_1}
class InfiniteException__nonzero_rxdigit8remain(Exception):pass
def _extract_emay_offsetted_num_layers_or_neg1_reserved_area_idx_(included_inf, len_dybits, may_either_num_periods, /):
    '-> emay (offsetted_num_layers/uint|neg1_reserved_area_idx/int{<0}) # [... => split into two half:(+oo | reserved_area{0})] # [neg1_reserved_area_idx==-1-reserved_area_idx]'
    assert len_dybits >= 0
    if may_either_num_periods is None:
        offsetted_num_layers = len_dybits
        r = offsetted_num_layers
    else:
        #(Either num_periods_00 num_periods_1)
        either_num_periods = may_either_num_periods
        if either_num_periods.is_right:
            num_periods_1 = either_num_periods.right
            if included_inf and num_periods_1 == 0:
                # split into two half:(+oo | reserved_area{0})
                r = ...
            else:
                reserved_area_idx = num_periods_1
                neg1_reserved_area_idx = -1 -reserved_area_idx
                assert neg1_reserved_area_idx < 0
                r = neg1_reserved_area_idx
            r
        else:
            num_periods_00 = either_num_periods.left
            assert num_periods_00 >= 0
            offsetted_num_layers = len_dybits + num_periods_00
            r = offsetted_num_layers
        r
    r
    return r
def _extract_imay_offsetted_num_layers_(included_inf, len_dybits, may_either_num_periods, /):
    '-> imay offsetted_num_layers|^ReservedAreaException # [-1 => +oo]'
    if included_inf and not may_either_num_periods is None:
        either_num_periods = may_either_num_periods
        if either_num_periods.is_left:
            num_periods_1 = either_num_periods.left
            if num_periods_1 == 0:
                #+oo | reserved_area{0}
                return -1
    return _extract_offsetted_num_layers_(len_dybits, may_either_num_periods)
        #^ReservedAreaException
def _extract_offsetted_num_layers_(len_dybits, may_either_num_periods, /):
    '-> offsetted_num_layers|^ReservedAreaException'
    if may_either_num_periods is None:
        offsetted_num_layers = len_dybits
    else:
        #(Either num_periods_00 num_periods_1)
        either_num_periods = may_either_num_periods
        if either_num_periods.is_right:
            num_periods_1 = either_num_periods.right
            reserved_area_idx = num_periods_1
            raise ReservedAreaException(reserved_area_idx)
        num_periods_00 = either_num_periods.left
        offsetted_num_layers = len_dybits + num_periods_00
    return offsetted_num_layers
#class IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers(IStepDecoder__plugin4infinite_uint_interval, IStepDecoder__fixed_size_layers__functional, IStepDecoder__fixed_radix4macro_header):
class IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers(IStepDecoder__plugin4infinite_uint_interval, IStepDecoder__fixed_radix4macro_header):
    '(num_layers@meta_layer/IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits, multi_pleb_layers/IStepDecoder__fixed_size_layers__body4infinite_uint_interval{num_layers})'
    __slots__ = ()
    ######################
    #@override
    min_with_unit4uint_interval = (0, 0)
    ######################
    @property
    @abstractmethod
    def offset4meta_layer(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits(sf, /):
        '-> IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits{imay_max_num_bits4read}'
    #@abstractmethod
    def mk_step_decoder4fixed_size_layers__body4infinite_uint_interval_(sf, num_layers, /):
        'num_layers/uint{>=1} -> IStepDecoder__fixed_size_layers__body4infinite_uint_interval{num_layers}'
        assert num_layers >= 1
        return StepDecoder__fixed_size_layers__body4infinite_uint_interval(sf.radix_info4digit, num_layers)
    ######################
    @cached_property
    @override
    def radix_info4digit(sf, /):
        return sf.step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits.radix_info4digit
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        dr4meta_layer = sf.step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits
        return _CallST.mk_call_st5four_args_(0,None,   dr4meta_layer,rxdigit8macro_header, state_vs_rxdigit=True)
    #.#@override
    #.feed_digits_ = _Dead.feed_digits_
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        st = loop_st7nonfinal
        assert st.case == 3
        [digit] = required_digits
        rxdigit8remain = RadixedDigit(sf.radix_info4digit, digit)
        return sf._4inf(rxdigit8remain)
            #^ReservedAreaException
    def on_reserved_area_(sf, reserved_area_idx, rxdigit8remain, /):
        'reserved_area_idx/uint -> rxdigit8remain/RadixedDigit -> (st/IBaseState4StepDecoder|^ReservedAreaException{(reserved_area_idx, rxdigit8remain)})'
        raise ReservedAreaException((reserved_area_idx, rxdigit8remain))
    def on_inf_with_nonzero_remain_digit_(sf, rxdigit8remain, /):
        '[+oo followed by nonzero_remain_digit] => rxdigit8remain/RadixedDigit{digit>0} -> (st/IBaseState4StepDecoder|^InfiniteException__nonzero_rxdigit8remain{rxdigit8remain})'
        raise InfiniteException__nonzero_rxdigit8remain(rxdigit8remain)
    def _4inf(sf, rxdigit8remain, /):
        'precondition:[rxdigit8remain.radix_info.num_bits4digit > 0]'
        #assert rxdigit8remain.radix_info.num_bits4digit > 0
        #MSB = (rxdigit8remain.digit >> (rxdigit8remain.radix_info.num_bits4digit -1))
        _num_bits4remain = rxdigit8remain.radix_info.num_bits4digit -1
        assert _num_bits4remain >= 0
        (MSB, _rxdigit8remain) = _cut_uint(_num_bits4remain, rxdigit8remain.digit)
        if MSB:
            # high_half_interval@[MSB==1]
            reserved_area_idx = 0
            st = sf.on_reserved_area_(reserved_area_idx, _rxdigit8remain)
            return st
            #.raise ReservedAreaException(reserved_area_idx:=0)
        if _rxdigit8remain.digit:
            st = sf.on_inf_with_nonzero_remain_digit_(_rxdigit8remain)
            return st
            #.raise InfiniteException__nonzero_rxdigit8remain(_rxdigit8remain)
        oresult = +oo
        return _LoopST(Cased(4,oresult),   _rxdigit8remain,   0)
    @override
    def feed_oresult_remain_(sf, call_st7nontail, oresult7subcall, rxdigit8remain7subcall, /):
        '# ^InfiniteException__nonzero_rxdigit8remain | ^ReservedAreaException'
        rxdigit8remain = rxdigit8remain7subcall
        match call_st7nontail.case:
            case 0:
                #bug:offsetted_num_layers = oresult7subcall
                (len_dybits, may_either_num_periods) = oresult7subcall
                #if 0b0001:raise Exception((len_dybits, may_either_num_periods), rxdigit8remain)
                #offsetted_num_layers = _extract_offsetted_num_layers_(len_dybits, may_either_num_periods)
                #.imay_offsetted_num_layers = _extract_imay_offsetted_num_layers_(sf.included_inf, len_dybits, may_either_num_periods)
                #.    #^ReservedAreaException
                #.if imay_offsetted_num_layers == -1:
                #.    #+oo | reserved_area{0}
                em = emay_offsetted_num_layers_or_neg1_reserved_area_idx = _extract_emay_offsetted_num_layers_or_neg1_reserved_area_idx_(sf.included_inf, len_dybits, may_either_num_periods)
                if em is ...:
                    # split into two half:(+oo | reserved_area{0})
                    if rxdigit8remain.radix_info.num_bits4digit == 0:
                        # to read next bit
                        return _LoopST(Cased(3,None),   rxdigit8remain,   1)
                    return sf._4inf(rxdigit8remain)
                        #^ReservedAreaException
                elif em < 0:
                    neg1_reserved_area_idx = em
                    reserved_area_idx = -1-neg1_reserved_area_idx
                    assert reserved_area_idx >= 0
                    st = sf.on_reserved_area_(reserved_area_idx, rxdigit8remain)
                    return st
                #offsetted_num_layers = imay_offsetted_num_layers
                offsetted_num_layers = em
                num_layers = offsetted_num_layers +sf.offset4meta_layer
                #if 0b0001:raise Exception((len_dybits, may_either_num_periods), rxdigit8remain, offsetted_num_layers, num_layers)
                #######
                dr4multi_pleb_layers = sf.mk_step_decoder4fixed_size_layers__body4infinite_uint_interval_(num_layers)
                return _CallST.mk_call_st5four_args_(1,None,   dr4multi_pleb_layers,rxdigit8remain, state_vs_rxdigit=True)
            case 1:
                u = oresult7subcall
                oresult = u
                return _LoopST(Cased(2,oresult),   rxdigit8remain,   0)
            case _:
                raise 000
        raise 000

    ######################
#end-class IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers(IStepDecoder__fixed_size_layers__functional, IStepDecoder__fixed_radix4macro_header):

def check_uint_linear_transforms4each_layer(uint_linear_transforms4each_layer, /):
    check_pair(uint_linear_transforms4each_layer)
    (layer_idx2uint_linear_transform__except_last_layer, offset4last_layer) = uint_linear_transforms4each_layer
    check_type_is(tuple, layer_idx2uint_linear_transform__except_last_layer)
    for uint_linear_transform in layer_idx2uint_linear_transform__except_last_layer:
        check_type_le(IUIntLinearTransform, uint_linear_transform)
    check_int_ge(0, offset4last_layer)
class IStepDecoder__plugin4finite_uint_interval__fixed_size_layers(IStepDecoder__plugin4finite_uint_interval, IStepDecoder__fixed_size_layers__functional, IStepDecoder__fixed_radix4macro_header):
    # see:并联型
    #.    __slots__ = ()
    #.class IStepDecoder__fixed_size_layers(IStepDecoder__fixed_size_layers__functional):
    r'''[[[
        [有限区编解码器基础型{基数纟头苞}==基础型{[(占地纟头苞,第零层规模,各层线性变换,整躯胞终末的起始层号,隐藏:囿 带单位值{末层压缩值上尾限})]}]
            #see:IStepDecoder__fixed_size_layers
            #see:IStepDecoder__parallel__partition_space4macro_header
            [囿==惰性数据]
            [带单位值{值名}(无单位值,单位/立即数丷爻元数丷躯胞数)]
            #xxx:[占地纟头苞==(所占用编码空间纟头苞,立即数丷爻元数,欤累计偏移量)]
                # 无用:欤累计偏移量
            [占地纟头苞==(所占用编码空间纟头苞,立即数丷爻元数)]
            [第零层规模==(长度纟第零层,躯胞数丷爻元数,欤头苞另计,头苞偏移量)]
                #多凡层:因为 没有 超层，所以 第零层 是 第零凡层
                # 头苞偏移量:比如:+1则有:([0-8][0-9]*) --> ([1-9][0-9]*)
            [各层线性变换==(非末层层号讠线性变换,末层偏移量)]
                #末层偏移量or累积接力居前末层最大值
                #统统硬编码
            整躯胞终末的起始层号:只用作检查
==>>:
占地纟头苞:
    所占用编码空间纟头苞:radix_info4macro_header(clipped macro_header),单位:立即数
第零层规模:step_decoder4fixed_size_xbcells4zeroth_layer
    #IStepDecoder__fixed_size_xbcells
    #第零层规模==(长度纟第零层,躯胞数丷爻元数,欤头苞另计,头苞偏移量)
    长度纟第零层:num_xbcells4read
    躯胞数丷爻元数:is_xbcell_bit
    欤头苞另计:macro_header_extra
    头苞偏移量:offset4macro_header
各层线性变换:uint_linear_transforms4each_layer or layer_idx2uint_linear_transform
    # [各层线性变换==(非末层层号讠线性变换,末层偏移量)]
    非末层层号讠线性变换:layer_idx2uint_linear_transform__except_last_layer
    末层偏移量:offset4last_layer
整躯胞终末的起始层号:min_layer_idx4end_by_cell_boundary #只用作检查

    #]]]'''#'''
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def uint_linear_transforms4each_layer(sf, /):
        '-> (layer_idx2uint_linear_transform__except_last_layer/[IUIntLinearTransform]{len==num_layers-1}, offset4last_layer)'
    #@property
    #@abstractmethod
    @cached_property
    def layer_idx2uint_linear_transform(sf, /):
        '-> [IUIntLinearTransform]{len==num_layers} # [layer_idx2uint_linear_transform[-1].scale==1] # an uniform format of uint_linear_transforms4each_layer'
        (layer_idx2uint_linear_transform__except_last_layer, offset4last_layer) = sf.uint_linear_transforms4each_layer
        uint_linear_transform4last_layer = UIntLinearTransform(1, offset4last_layer)
        return (*layer_idx2uint_linear_transform__except_last_layer, uint_linear_transform4last_layer)
    ######################
    @property
    @override
    def idx4last_layer(sf, /):
        '-> uint%num_layers'
        return len(sf.uint_linear_transforms4each_layer[0])
    @property
    @override
    def num_layers(sf, /):
        '-> uint{>=1}'
        return len(sf.layer_idx2uint_linear_transform)
        return 1+sf.idx4last_layer
    ######################
    @override
    def layer_idx2uint_linear_transform_(sf, layer_idx, /):
        return sf.layer_idx2uint_linear_transform[layer_idx]
    ######################
#end-class IStepDecoder__fixed_size_layers(IStepDecoder):


class IStepDecoder__plugin4uint_interval__extend_macro_header(IStepDecoder__plugin4uint_interval__base, IStepDecoder__extend_macro_header):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    @override#update:__doc__
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__fixed_radix4macro_header{[radix4macro_header%radix4digit==0]}'
    ######################
    @cached_property
    @override
    def is_finite_uint_interval(sf, /):
        '-> bool'
        return sf.the_wrapped_step_decoder.is_finite_uint_interval
    @cached_property
    @override
    def min_with_unit4uint_interval(sf, /):
        '-> (uint, Unit)'
        return sf.the_wrapped_step_decoder.min_with_unit4uint_interval
    @cached_property
    @override
    def emay_may_max1_with_unit4finite_uint_interval(sf, /):
        return sf.the_wrapped_step_decoder.emay_may_max1_with_unit4finite_uint_interval
    @cached_property
    @override
    def radix_info4macro_header(sf, /):
        dr = sf.the_wrapped_step_decoder
        radix4H = dr.radix_info4macro_header.radix
        radix4B = dr.radix_info4digit.radix
        #bug:radix = radix4H*radix4B
        radix, r = divmod(radix4H, radix4B)
        if not r == 0:raise ValueError((dr, radix4H, radix4B))
        assert radix4H == radix*radix4B
        return RadixInfo(radix)
    ######################
#class IStepDecoder__plugin4finite_uint_interval__extend_macro_header(IStepDecoder__plugin4finite_uint_interval, IStepDecoder__extend_macro_header):
class IStepDecoder__plugin4finite_uint_interval__extend_macro_header(IStepDecoder__plugin4finite_uint_interval, IStepDecoder__plugin4uint_interval__extend_macro_header):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    @override#update:__doc__
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__plugin4finite_uint_interval{[radix4macro_header%radix4digit==0]}'
    ######################
    @cached_property
    @override
    def max1_with_unit4finite_uint_interval(sf, /):
        '-> (uint, Unit)'
        return sf.the_wrapped_step_decoder.max1_with_unit4finite_uint_interval
    ######################
#end-class IStepDecoder__plugin4finite_uint_interval__extend_macro_header(IStepDecoder__plugin4finite_uint_interval, IStepDecoder__extend_macro_header):

class IStepDecoder__plugin4uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4uint_interval__base, IStepDecoder__parallel__partition_space4macro_header):
    __slots__ = ()
    @property
    @abstractmethod
    @override#update:__doc__
    def child_step_decoder_seq(sf, /):
        '-> nonempty [IStepDecoder__plugin4uint_interval__base{<:IStepDecoder__fixed_radix4macro_header}]{sum(child_step_decoder.radix4macro_header for child_step_decoder in child_step_decoder_seq) == sf.radix4macro_header} #radix_info4digit require nonempty # nonlast_child should be finite_uint_interval'
    @cached_property
    @override
    def is_finite_uint_interval(sf, /):
        '-> bool'
        return sf.child_step_decoder_seq[-1].is_finite_uint_interval
    @cached_property
    @override
    def min_with_unit4uint_interval(sf, /):
        '-> (uint, Unit)'
        return sf.child_step_decoder_seq[0].min_with_unit4uint_interval
    @cached_property
    @override
    def emay_may_max1_with_unit4finite_uint_interval(sf, /):
        return sf.child_step_decoder_seq[-1].emay_may_max1_with_unit4finite_uint_interval
#class IStepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4finite_uint_interval, IStepDecoder__parallel__partition_space4macro_header):
class IStepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4finite_uint_interval, IStepDecoder__plugin4uint_interval__parallel__partition_space4macro_header):
    __slots__ = ()
    @property
    @abstractmethod
    @override#update:__doc__
    def child_step_decoder_seq(sf, /):
        '-> nonempty [IStepDecoder__plugin4finite_uint_interval{<:IStepDecoder__fixed_radix4macro_header}]{sum(child_step_decoder.radix4macro_header for child_step_decoder in child_step_decoder_seq) == sf.radix4macro_header} #radix_info4digit require nonempty'
    @property
    @override
    def max1_with_unit4finite_uint_interval(sf, /):
        '-> (uint, Unit)'
        return sf.child_step_decoder_seq[-1].max1_with_unit4finite_uint_interval
#end-class IStepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4finite_uint_interval, IStepDecoder__parallel__partition_space4macro_header):

#class IStepDecoder__plugin4infinite_uint_interval__extend_macro_header(IStepDecoder__plugin4infinite_uint_interval, IStepDecoder__extend_macro_header):
class IStepDecoder__plugin4infinite_uint_interval__extend_macro_header(IStepDecoder__plugin4infinite_uint_interval, IStepDecoder__plugin4uint_interval__extend_macro_header):
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    @override#update:__doc__
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__plugin4infinite_uint_interval{[radix4macro_header%radix4digit==0]}'
    ######################
    @cached_property
    @override
    def included_inf(sf, /):
        '-> bool{include +oo}'
        return sf.the_wrapped_step_decoder.included_inf
    ######################
#end-class IStepDecoder__plugin4infinite_uint_interval__extend_macro_header(IStepDecoder__plugin4infinite_uint_interval, IStepDecoder__extend_macro_header):

#class IStepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4infinite_uint_interval, IStepDecoder__parallel__partition_space4macro_header):
class IStepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4infinite_uint_interval, IStepDecoder__plugin4uint_interval__parallel__partition_space4macro_header):
    __slots__ = ()
    @property
    @abstractmethod
    @override#update:__doc__
    def child_step_decoder_seq(sf, /):
        '-> nonempty [IStepDecoder__plugin4uint_interval__base{<:IStepDecoder__fixed_radix4macro_header}]{sum(child_step_decoder.radix4macro_header for child_step_decoder in child_step_decoder_seq) == sf.radix4macro_header} #radix_info4digit require nonempty # nonlast_child should be finite_uint_interval # last_child should be infinite_uint_interval'
    @cached_property
    @override
    def included_inf(sf, /):
        '-> bool{include +oo}'
        return sf.child_step_decoder_seq[-1].included_inf
#end-class IStepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4infinite_uint_interval, IStepDecoder__parallel__partition_space4macro_header):



class StepDecoder__plugin4finite_uint_interval__extend_macro_header(IStepDecoder__plugin4finite_uint_interval__extend_macro_header):
    ___no_slots_ok___ = True
    def __init__(sf, inner_step_decoder4plugin4finite_uint_interval, /):
        assert inner_step_decoder4plugin4finite_uint_interval.is_finite_uint_interval
        #check_type_le(IStepDecoder__plugin4finite_uint_interval, inner_step_decoder4plugin4finite_uint_interval)
        #assert inner_step_decoder4plugin4finite_uint_interval.radix_info4macro_header.radix % radix_info4macro_header.radix == 0
        assert inner_step_decoder4plugin4finite_uint_interval.radix_info4macro_header.radix % inner_step_decoder4plugin4finite_uint_interval.radix_info4digit.radix == 0
        sf._dr = inner_step_decoder4plugin4finite_uint_interval
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_wrapped_step_decoder)
    ######################
    @property
    @override
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__plugin4finite_uint_interval{[radix4macro_header%radix4digit==0]}'
        return sf._dr
    ######################
check_non_ABC(StepDecoder__plugin4finite_uint_interval__extend_macro_header)
class StepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header):
    ___no_slots_ok___ = True
    def __init__(sf, child_step_decoder_seq, /):
        child_step_decoder_seq = mk_tuple(child_step_decoder_seq)
        assert child_step_decoder_seq
        assert all(dr.is_finite_uint_interval for dr in child_step_decoder_seq)
        sf._xs = child_step_decoder_seq
    def __repr__(sf, /):
        return repr_helper(sf, sf.child_step_decoder_seq)
    @property
    @override
    def child_step_decoder_seq(sf, /):
        return sf._xs
check_non_ABC(StepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header)

_BaseStepDecoder__plugin4finite_uint_interval__fixed_size_layers = mk_named_pseudo_tuple_(__name__, 'BaseStepDecoder__plugin4finite_uint_interval__fixed_size_layers', 'radix_info4macro_header min_with_unit4uint_interval max1_with_unit4finite_uint_interval step_decoder4fixed_size_xbcells4zeroth_layer uint_linear_transforms4each_layer min_layer_idx4end_by_cell_boundary')
class StepDecoder__plugin4finite_uint_interval__fixed_size_layers(_BaseStepDecoder__plugin4finite_uint_interval__fixed_size_layers, IStepDecoder__plugin4finite_uint_interval__fixed_size_layers):
    ___no_slots_ok___ = True
    def _check6make_(sf, /):
        check_radix_info4macro_header(sf.radix_info4macro_header)
        #check_radix_info4digit(sf.radix_info4digit)
        check_uint_with_unit(sf.min_with_unit4uint_interval)
        check_uint_with_unit(sf.max1_with_unit4finite_uint_interval)
        check_type_le(IStepDecoder__fixed_size_xbcells, sf.step_decoder4fixed_size_xbcells4zeroth_layer)
        check_uint_linear_transforms4each_layer(sf.uint_linear_transforms4each_layer)
        check_int_ge(0, sf.min_layer_idx4end_by_cell_boundary)
check_non_ABC(StepDecoder__plugin4finite_uint_interval__fixed_size_layers)

class StepDecoder__plugin4infinite_uint_interval__extend_macro_header(IStepDecoder__plugin4infinite_uint_interval__extend_macro_header):
    ___no_slots_ok___ = True
    def __init__(sf, inner_step_decoder4plugin4infinite_uint_interval, /):
        assert not inner_step_decoder4plugin4infinite_uint_interval.is_finite_uint_interval
        #check_type_le(IStepDecoder__plugin4infinite_uint_interval, inner_step_decoder4plugin4infinite_uint_interval)
        #assert inner_step_decoder4plugin4infinite_uint_interval.radix_info4macro_header.radix % radix_info4macro_header.radix == 0
        assert inner_step_decoder4plugin4infinite_uint_interval.radix_info4macro_header.radix % inner_step_decoder4plugin4infinite_uint_interval.radix_info4digit.radix == 0
        sf._dr = inner_step_decoder4plugin4infinite_uint_interval
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_wrapped_step_decoder)
    ######################
    @property
    @override
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__plugin4infinite_uint_interval{[radix4macro_header%radix4digit==0]}'
        return sf._dr
    ######################
check_non_ABC(StepDecoder__plugin4infinite_uint_interval__extend_macro_header)
class StepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header(IStepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header):
    ___no_slots_ok___ = True
    def __init__(sf, child_step_decoder_seq, /):
        child_step_decoder_seq = mk_tuple(child_step_decoder_seq)
        assert child_step_decoder_seq
        assert not child_step_decoder_seq[-1].is_finite_uint_interval
        assert all(dr.is_finite_uint_interval for dr in child_step_decoder_seq[:-1])
        sf._xs = child_step_decoder_seq
    def __repr__(sf, /):
        return repr_helper(sf, sf.child_step_decoder_seq)
    @property
    @override
    def child_step_decoder_seq(sf, /):
        return sf._xs
check_non_ABC(StepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header)


_BaseStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers = mk_named_pseudo_tuple_(__name__, 'BaseStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers', 'radix_info4macro_header included_inf offset4meta_layer step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits')
class StepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers(_BaseStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers, IStepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers):
    ___no_slots_ok___ = True
    #.#@override
    #.included_inf = True
    #.#@override
    #.emay_may_max1_with_unit4finite_uint_interval = ...
    def _check6make_(sf, /):
        check_radix_info4macro_header(sf.radix_info4macro_header)
        #xxx:assert sf.radix_info4macro_header.is_zpow_radix, sf.radix_info4macro_header
        check_type_is(bool, sf.included_inf)
        check_int_ge(0, sf.offset4meta_layer)
        check_type_le(IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits, sf.step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits)
check_non_ABC(StepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers)






























class IStepDecoder__uint_without_inf__uint_zero_encoded_as_head_digit_zero(IStepDecoder__fixed_radix4macro_header, IStepDecoder__wrapper):
    __slots__ = ()
    ######################
    IStepDecoder__plugin4infinite_uint_interval
    ######################
    @property
    @abstractmethod
    def the_uint8inf_if_shift_out_zero(sf, /):
        '-> uint{>=0}'
    ######################
    @property
    @abstractmethod
    @override#update:__doc__
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__plugin4infinite_uint_interval{[min_with_unit4uint_interval:=(0,0)][included_inf:=False][uint_zero_encoded_as_head_digit_zero]}'
    ######################

class IStepDecoder__uint_with_inf(IStepDecoder__fixed_radix4macro_header, IStepDecoder__wrapper):
    __slots__ = ()
    ######################
    IStepDecoder__plugin4infinite_uint_interval
    ######################
    @property
    @abstractmethod
    @override#update:__doc__
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__plugin4infinite_uint_interval{[min_with_unit4uint_interval:=(0,0)][included_inf:=True]}'
    ######################

class IStepDecoder__int_with_inf(IStepDecoder__fixed_radix4macro_header):
    __slots__ = ()
    ######################
    IStepDecoder__uint_with_inf
    IStepDecoder__uint_without_inf__uint_zero_encoded_as_head_digit_zero
    ######################
    IStepDecoder__flip_digits
    ######################
    @property
    @abstractmethod
    def step_decoder4uint_withxxx_inf(sf, /):
        '-> (IStepDecoder__uint_with_inf | [sf.radix_info4macro_header.radix is odd{>=3}]:IStepDecoder__uint_without_inf__uint_zero_encoded_as_head_digit_zero{uint 0 encoded as head_digit 0}) # [half_int==(positive_int|nonnegative_int)]'
    ######################
    @cached_property
    @override
    def radix_info4digit(sf, /):
        return sf.step_decoder4uint_withxxx_inf.radix_info4digit
    ######################
    @cached_property
    def to_shift_out_zero(sf, /):
        '-> bool'
        dr = sf.step_decoder4uint_withxxx_inf
        if hasattr(dr, 'the_uint8inf_if_shift_out_zero'):
            radix4H = sf.radix_info4macro_header.radix
            rH_odd = bool(radix4H & 1)
            #isolated_0 = (rH_odd and radix4H >= 3) # odd{>=3}
            if not (rH_odd and radix4H >= 3):raise 000
            return True
        return False
    @cached_property
    def _may_to_shift_out_zero(sf, /):
        may_post_ = sf._to_shift_out_zero if sf.to_shift_out_zero else None
        return may_post_
    def _to_shift_out_zero(sf, u, /):
        'uint{>=0} -> (uint{>=1}|+oo)'
        dr = sf.step_decoder4uint_withxxx_inf
        v = dr.the_uint8inf_if_shift_out_zero
        if u <= v:
            if u == v:
                return +oo
            return u+1
        return u

    ######################
    #.@cached_property
    #.def step_decoder4uint_with_inf__may_shift_out_zero(sf, /):
    #.    '-> IStepDecoder__uint_with_inf'
    ######################
    #radix_info4macro_header
    #    1,even{>=2},odd{>=3}
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        radix4H = sf.radix_info4macro_header.radix
        if not rxdigit8macro_header.radix_info.radix == radix4H:raise 000
        return sf._work(rxdigit8macro_header)
    def _work(sf, rxdigit8H, /):
        radix_info4H = rxdigit8H.radix_info
        radix4H = radix_info4H.radix
        digit8H = rxdigit8H.digit
        assert radix4H >= 1
        rH_odd = bool(radix4H & 1)
        half = radix4H>>1
        # [radix4H == rH_odd +2*half]
        # [10 == 0+2*5]
        #   => [0..=4]++[5..=9]
        #   => [[digit8H==half==5] -> [u:=0]]
        # [9 == 1+2*4]
        #   => [0..=3]++[4]++[5..=8]
        #   => [half==4]
        #   => [[digit8H==half==4] -> [u:=0]]
        diff = digit8H -half
        # !! [0 <= digit8H < radix4H == rH_odd+2*half]
        # [-half <= diff == digit8H -half < rH_odd+half]
        if diff < 0:
            flipped_sf = StepDecoder__flip_digits(sf)
            return _TCallST.mk_tail_call_st5three_args_(__neg__,   flipped_sf,rxdigit8H, state_vs_rxdigit=True)
        # [diff >= 0]
        # [0 <= diff < rH_odd+half]
        # [-rH_odd <= diff-rH_odd < half]
        # [not [[diff == 0][rH_odd]]] => [0 <= (diff-rH_odd) < half]

        isolated_0 = (rH_odd and radix4H >= 3) # odd{>=3}
            # 0 as middle digit@macro_header
        #to_flip_digits = diff < 0
        if isolated_0 and diff == 0:
            #final_st
            oresult = u = 0
            return _LoopST(Cased(0x0000,oresult),  rxdigit8no_bits,  0)
        # [not [[diff == 0][isolated_0]]]
        # [not [[diff == 0][rH_odd][radix4H >= 3]]]
        dr = sf.step_decoder4uint_withxxx_inf
        if radix4H == 1:
            # [half == 0]
            if not 2*dr.radix_info4macro_header.radix == dr.radix_info4digit.radix:raise ValueError((radix_info4H, dr.radix_info4macro_header, dr.radix_info4digit))
                # rH_one => 深入:再对半分『头苞』,只剩一半
            assert dr.radix_info4digit.num_bits4digit == 1+dr.radix_info4macro_header.num_bits4digit
            return _LoopST(Cased(0x0001, None),  rxdigit8no_bits,  1)
        # [radix4H >= 2]
        # [half >= 1]
        # [0 <= diff < rH_odd+half]
        _digit8H = diff
        _radix4H = rH_odd + half
        # [_radix4H >= 1]
        _radix_info4H = dr.radix_info4macro_header#RadixInfo(_radix4H)
        if not _radix4H == _radix_info4H.radix:raise ValueError((_radix4H, _radix_info4H))
        _rxdigit8H = RadixedDigit(_radix_info4H, _digit8H)
        may_post_ = sf._may_to_shift_out_zero
        return _TCallST.mk_tail_call_st5three_args_(may_post_,   dr,_rxdigit8H, state_vs_rxdigit=True)
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        st = loop_st7nonfinal
        assert st.case == 0x0001
        [digit8H] = required_digits
        radix_info4H = sf.radix_info4digit
        rxdigit8H = RadixedDigit(radix_info4H, digit8H)
        return sf._work(rxdigit8H)
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
    ######################
#end-class IStepDecoder__int_with_inf(IStepDecoder__fixed_radix4macro_header):
class IStepDecoder__rational_with_inf(IStepDecoder__fixed_radix4macro_header):
    __slots__ = ()
    ######################
    IStepDecoder__int_with_inf#head_int
    IStepDecoder__uint_with_inf#inner_uint/inner_nint
    ######################
    IStepDecoder__flip_digits
    ######################
    @property
    @abstractmethod
    def step_decoder4int_with_inf(sf, /):
        '-> IStepDecoder__int_with_inf # head_int'
    @property
    @abstractmethod
    def step_decoder4uint_with_inf(sf, /):
        '-> IStepDecoder__uint_with_inf # inner_uint'
    @cached_property
    #@abstractmethod
    def step_decoder4nint_with_inf(sf, /):
        '-> IStepDecoder__uint_with_inf # inner_nint #but [oresult::(uint|+oo)]'
        return sf.mk_step_decoder4flip_digits_(sf.step_decoder4uint_with_inf)
    #@abstractmethod
    def mk_step_decoder4flip_digits_(sf, step_decoder, /):
        'IStepDecoder -> IStepDecoder__flip_digits # [inner_uint --> inner_nint]'
        return StepDecoder__flip_digits(step_decoder)
    ######################
    @cached_property
    @override
    def radix_info4macro_header(sf, /):
        return sf.step_decoder4int_with_inf.radix_info4macro_header
    ######################
    @cached_property
    @override
    def radix_info4digit(sf, /):
        return sf.step_decoder4int_with_inf.radix_info4digit
    ######################
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        dr4int = sf.step_decoder4int_with_inf
        lnkls = ()
        return _CallST.mk_call_st5four_args_(0,lnkls,   dr4int,rxdigit8macro_header, state_vs_rxdigit=True)
    #@override
    feed_digits_ = _Dead.feed_digits_
    @override
    def feed_oresult_remain_(sf, call_st7nontail, oresult7subcall, rxdigit8remain7subcall, /):
        st = call_st7nontail
        case = st.case
        lnkls = st.payload
        x = oresult7subcall
        if abs(x) is +oo:
            if not lnkls:
                assert case == 0
                oresult = x
            else:
                assert case
                assert x is +oo
                ls = [*rglnkls2reversed_iterable(lnkls)]
                ls.reverse()
                L = len(ls)
                assert L
                if L >= 2:
                    for j in range(1, L-1):
                        ls[j] += 1
                    ls[-1] += 2
                oresult = calc_Fraction5finite_continued_fraction_(ls)
            oresult
            return _LoopST(Cased(2, oresult),  rxdigit8remain7subcall,  0)
        # [x :: int]
        assert x >= 0 or case == 0
        lnkls = (lnkls, x)
        match case:
            case 0:
                # int
                #i = oresult7subcall
                ###
                dr = dr4nint = sf.step_decoder4nint_with_inf
                #_case = -1
            case -1:
                # nint #but [oresult::(uint|+oo)]
                #u = n = oresult7subcall
                ###
                dr = dr4uint = sf.step_decoder4uint_with_inf
                #_case = +1
            #case +1:
                #^SyntaxError: invalid syntax
            case 1:
                # uint
                #u = oresult7subcall
                ###
                dr = dr4nint = sf.step_decoder4nint_with_inf
                #_case = -1
            case _:
                raise 000
        lnkls
        dr
        _case = +1 if case==-1 else -1
        return _CallST.mk_call_st5four_args_(_case,lnkls,   dr,rxdigit8remain7subcall, state_vs_rxdigit=True)
    ######################
#end-class IStepDecoder__rational_with_inf(IStepDecoder__fixed_radix4macro_header):




#class StepDecoder__uint_with_inf(IStepDecoder__uint_with_inf):
class StepDecoder__uint_with_inf(IStepDecoder__postprocess_wrapper, IStepDecoder__uint_with_inf):
    r'''[[[

    ######################
    [arg4inf =[def]= (0b111, arg4fnt, (arg4gnd4inf|deep1_arg4inf))]
    [arg4gnd4inf =[def]= (0b11, rH, offset4meta_layer,   imay_max_num_bits4read)] # step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits
    [deep1_arg4inf =[def]= (0b10, arg4inf)]
    [arg4fnt =[def]= (0b100, [child])]
    [child =[def]= (arg4gnd4fnt|deep1_arg4fnt)]
    [deep1_arg4fnt =[def]= (0b01, arg4fnt)]
    [arg4gnd4fnt =[def]= (0b00, (rH, min_with_unit4uint_interval, max1_with_unit4finite_uint_interval, uint_linear_transforms4each_layer, min_layer_idx4end_by_cell_boundary),    (offset4macro_header, macro_header_extra, num_xbcells4read, is_xbcell_bit))] # step_decoder4fixed_size_xbcells4zeroth_layer
    ######################



    view others/数学/编程/设计/自定义编码纟整数-alnum字母表+5over8效率.txt
#######
编码扩增自然数{32}:
  直接进入 超凡层:
    超层==第零层==动态爻元
  0_bbbb => 1凡层:16:[0..<2**4]
    # regex"[A-F]"
  1_0bbb => 2凡层:[0..<8]:[0..<2**35]
    # regex"[G-N].*"
  1_10bb => 3凡层:[0..<4]:[0..<2**15]:[0..<2**((2**15-1)*5)==2**163835]
    # regex"[O-R].*"
  #1_111b => 保留区0
    1_1110 => 正无穷
      # 'U'
    1_1111 ... => 保留区0改
      # 'V'
  1_1100 => 4凡层
    # regex"[S].*"
  1_1101 1_bbbb => 保留区1
  1_1101 0_0bbb => 5凡层
  1_1101 0_11bb => 保留区2
  1_1101 0_100b => 6凡层
  1_1101 0_1011 => 保留区3
  1_1101 0_1010 0_bbbb => 7凡层
  1_1101 0_1010 1_1bbb => 保留区4
  <29>   ...
  1_1101 (0_1010 1_0101)*
  <29>   (<10> <21>)*
    # [<31> == 'V']
    # [<29> == 'T']
    # [<10> == 'A']
    # [<21> == 'L']
  regex"T(AL)*"
  ...


#######
    #]]]'''#'''
    ___no_slots_ok___ = True
    ######################
    StepDecoder__fixed_size_xbcells#step_decoder4fixed_size_xbcells4zeroth_layer
        #(radix_info4digit, offset4macro_header, macro_header_extra, num_xbcells4read, is_xbcell_bit)
    StepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits#step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits
        #(radix_info4digit, imay_max_num_bits4read)
    ######################
    StepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers
        #(radix_info4macro_header, included_inf, offset4meta_layer, step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits)
    StepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header
        #child_step_decoder_seq
    StepDecoder__plugin4infinite_uint_interval__extend_macro_header
        #inner_step_decoder4plugin4infinite_uint_interval
    ######################
    StepDecoder__plugin4finite_uint_interval__fixed_size_layers
        #(radix_info4macro_header, min_with_unit4uint_interval, max1_with_unit4finite_uint_interval, step_decoder4fixed_size_xbcells4zeroth_layer, uint_linear_transforms4each_layer, min_layer_idx4end_by_cell_boundary)
    StepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header
        #child_step_decoder_seq
    StepDecoder__plugin4finite_uint_interval__extend_macro_header
        #inner_step_decoder4plugin4finite_uint_interval
    ######################
    def __init__(sf, radix_info4digit, included_inf, arg4inf, /):
        sf._dr = _mk_plugin4step_decoder4uint_with_inf_(radix_info4digit, included_inf, arg4inf)
        sf._args4repr = (radix_info4digit, included_inf, arg4inf)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args4repr)
    #@override
    may_postprocess = None
    @property
    @override
    def the_wrapped_step_decoder(sf, /):
        '-> IStepDecoder__plugin4infinite_uint_interval{[min_with_unit4uint_interval:=(0,0)][included_inf:=True]}'
        return sf._dr
    @cached_property
    @override
    def radix_info4macro_header(sf, /):
        return sf.the_wrapped_step_decoder.radix_info4macro_header
    ######################

def _mk_plugin4step_decoder4uint_with_inf_(radix_info4digit, included_inf, _arg4inf, /):
    def _4arg4fnt(arg4fnt, /):
        '-> child_step_decoder_seq'
        match arg4fnt:
            case (0b100, children):
                pass
            case _:
                raise 000
        children
        child_step_decoder_seq = []
        for x in children:
            match x:
                #(arg4gnd4fnt|deep1_arg4fnt)
                case (0b00, (rH, min_with_unit4uint_interval, max1_with_unit4finite_uint_interval, uint_linear_transforms4each_layer, min_layer_idx4end_by_cell_boundary),    (offset4macro_header, macro_header_extra, num_xbcells4read, is_xbcell_bit)):
                    step_decoder4fixed_size_xbcells4zeroth_layer = StepDecoder__fixed_size_xbcells(radix_info4digit, offset4macro_header, macro_header_extra, num_xbcells4read, is_xbcell_bit)
                    dr = StepDecoder__plugin4finite_uint_interval__fixed_size_layers(radix_info4macro_header:=rH, min_with_unit4uint_interval, max1_with_unit4finite_uint_interval, step_decoder4fixed_size_xbcells4zeroth_layer, uint_linear_transforms4each_layer, min_layer_idx4end_by_cell_boundary)
                case (0b01, arg4fnt):
                    _child_step_decoder_seq = _4arg4fnt(arg4fnt)
                    _dr = StepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header(_child_step_decoder_seq)
                    dr = StepDecoder__plugin4finite_uint_interval__extend_macro_header(_dr)
                case _:
                    raise 000
            dr
            child_step_decoder_seq.append(dr)
        return child_step_decoder_seq
    def _4arg4inf(arg4inf, /):
        match arg4inf:
            case (0b111, arg4fnt, x):
                match x:
                    #(arg4gnd4inf|deep1_arg4inf)
                    case (0b11, rH, offset4meta_layer,   imay_max_num_bits4read):
                        step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits = StepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits(radix_info4digit, imay_max_num_bits4read)
                        dr4last_layer = StepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers(radix_info4macro_header:=rH, included_inf, offset4meta_layer, step_decoder4truncated_dynamic_bits_with_may_dynamic_bibits)
                    case (0b10, arg4inf):
                        _dr = _4arg4inf(arg4inf)
                        dr4last_layer = StepDecoder__plugin4infinite_uint_interval__extend_macro_header(_dr)
                    case _:
                        raise 000
                dr4last_layer
                child_step_decoder_seq = (*_4arg4fnt(arg4fnt), dr4last_layer)
            case _:
                raise 000
        child_step_decoder_seq
        dr = StepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header(child_step_decoder_seq)
        return dr
    return _4arg4inf(_arg4inf)
#end-def _mk_plugin4step_decoder4uint_with_inf_(radix_info4digit, included_inf, _arg4inf, /):
check_non_ABC(StepDecoder__uint_with_inf)
['feed_digits_', 'feed_oresult_remain_', 'radix_info4macro_header', 'start_']
class StepDecoder__int_with_inf(IStepDecoder__int_with_inf):
    r'''[[[
    view others/数学/编程/设计/自定义编码纟整数-alnum字母表+5over8效率.txt

#######
编码扩增整数{3}:
[编码扩增整数{3}.表达{负无穷} =[def]= 取反(编码扩增整数{3}.表达{正无穷})]
[编码扩增整数{3}.表达{负整数} =[def]= 取反(编码扩增整数{3}.表达{取负(负整数)})]
[编码扩增整数{3}.表达{0} =[def]= "X"]
[编码扩增整数{3}.表达{正整数} =[def]= "Y"++头苞减一(编码扩增自然数{32}.表达{正整数})]
  #==>>头苞 最大值 被保留 (用作 正无穷)
[编码扩增整数{3}.表达{正无穷} =[def]= "YV"]

#######
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, radix_info4macro_header, step_decoder4uint_withxxx_inf, /):
        check_radix_info4macro_header(radix_info4macro_header)
        check_type_le((IStepDecoder__uint_with_inf, IStepDecoder__uint_without_inf__uint_zero_encoded_as_head_digit_zero), step_decoder4uint_withxxx_inf)
        #######
        radix4H = radix_info4macro_header.radix
        _radix4H = step_decoder4uint_withxxx_inf.radix_info4macro_header.radix
        radix4B = step_decoder4uint_withxxx_inf.radix_info4digit.radix
        if radix4H == 1:
            assert _radix4H*2 == radix4B
        else:
            assert _radix4H == (radix4H+1)//2
        #######
        sf._riH = radix_info4macro_header
        sf._dr = step_decoder4uint_withxxx_inf
    def __repr__(sf, /):
        return repr_helper(sf, sf.radix_info4macro_header, sf.step_decoder4uint_withxxx_inf)
    @property
    @override
    def radix_info4macro_header(sf, /):
        return sf._riH
    @property
    @override
    def step_decoder4uint_withxxx_inf(sf, /):
        return sf._dr
check_non_ABC(StepDecoder__int_with_inf)
['radix_info4macro_header', 'step_decoder4uint_withxxx_inf']
class StepDecoder__rational_with_inf(IStepDecoder__rational_with_inf):
    r'''[[[
    view others/数学/编程/设计/自定义编码纟整数-alnum字母表+5over8效率.txt


#######
编码扩增有理数{3}:
输入:正负无穷
过程:
  [编码扩增有理数{3}.表达(正负无穷) =[def]= 编码扩增整数{3}.表达(正负无穷)]
输入:有理数
过程:
  [规范连分数:=连分数表达牜最后部分分母大于等于二(有理数)]
  [偏置规范连分数:=部分分母减一并且最后一位再减一(规范连分数)]
  [填充偏置规范连分数:=追附正无穷(偏置规范连分数)]
  [奇负填充偏置规范连分数:=奇位取负(填充偏置规范连分数)]
  [列表纟编码:=各自编码冫头丶躯奇位丶躯偶位(编码扩增整数{3},(取反<<<编码扩增自然数{32}<<<取负),编码扩增自然数{32};奇负填充偏置规范连分数)]
  [最终编码纟有理数:=串接(列表纟编码)]
  [编码扩增有理数{3}.表达(有理数) =[def]= 最终编码纟有理数]

#######
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, step_decoder4int_with_inf, step_decoder4uint_with_inf, /):
        check_type_le(IStepDecoder__int_with_inf, step_decoder4int_with_inf)
        check_type_le(IStepDecoder__uint_with_inf, step_decoder4uint_with_inf)
        assert step_decoder4int_with_inf.radix_info4digit == step_decoder4uint_with_inf.radix_info4digit
        sf._dr4int = step_decoder4int_with_inf
        sf._dr4uint = step_decoder4uint_with_inf
    def __repr__(sf, /):
        return repr_helper(sf, sf.step_decoder4int_with_inf, sf.step_decoder4uint_with_inf)
    @property
    @override
    def step_decoder4int_with_inf(sf, /):
        return sf._dr4int
    @property
    @override
    def step_decoder4uint_with_inf(sf, /):
        return sf._dr4uint

check_non_ABC(StepDecoder__rational_with_inf)
['step_decoder4int_with_inf', 'step_decoder4uint_with_inf']



if 0:
    _58_dr4int = None
    _58_dr4rational = None
def _58_gmk_dr4int_dr4rational():
    '-> (step_decoder4int_with_inf__alnum__5over8, step_decoder4rational_with_inf__alnum__5over8)'
    global _58_dr4int, _58_dr4rational
    try:
        return (_58_dr4int, _58_dr4rational)
    except NameError:
        pass
    (_58_dr4int, _58_dr4rational) = _58_mk_dr4int_dr4rational()
    return _58_gmk_dr4int_dr4rational()
def _58_mk_dr4int_dr4rational():
    '-> (step_decoder4int_with_inf__alnum__5over8, step_decoder4rational_with_inf__alnum__5over8)'
    radix_info4macro_header = RadixInfo(3)
    radix_info4digit = ZpowRadixInfo(5)
    rH32 = radix_info4digit
    ######################
    #bug:rH = radix_info4macro_header
    #rH = RadixInfo(2)
    #   --> rH1+rH1
    rH1 = RadixInfo(1)
    arg4gnd4fnt = (0b00, (rH1, (0,0), (1,0), uint_linear_transforms4each_layer:=((), 0), min_layer_idx4end_by_cell_boundary:=0),    (offset4macro_header:=0, macro_header_extra:=True, num_xbcells4read:=0, is_xbcell_bit:=False))
    child = arg4gnd4fnt
    arg4fnt = (0b100, [child])
    #bug:rH = radix_info4macro_header
    if 0:
        #.rH2 = RadixInfo(2)
        arg4gnd4inf = (0b11, rH1, offset4meta_layer:=1,   imay_max_num_bits4read:=3)
        arg4inf = (0b111, arg4fnt, arg4gnd4inf)
    else:
        rH32
        arg4gnd4inf = (0b11, rH32, offset4meta_layer:=1,   imay_max_num_bits4read:=3)
        _arg4fnt = (0b100, [])
        _arg4inf = (0b111, _arg4fnt, arg4gnd4inf)
        deep1_arg4inf = (0b10, _arg4inf)
        arg4inf = (0b111, arg4fnt, deep1_arg4inf)
    arg4inf
    ######################
    dr4uint = StepDecoder__uint_with_inf(radix_info4digit, included_inf:=True, arg4inf)
    dr4int = StepDecoder__int_with_inf(radix_info4macro_header, step_decoder4uint_withxxx_inf:=dr4uint)
    dr4rational = StepDecoder__rational_with_inf(dr4int, dr4uint)
    ######################
    _58_dr4int = dr4int
    _58_dr4rational = dr4rational
    return (step_decoder4int_with_inf__alnum__5over8:=dr4int, step_decoder4rational_with_inf__alnum__5over8:=dr4rational)

def gmk_step_decoder4int_with_inf__alnum__5over8_():
    '-> IStepDecoder__int_with_inf{radix4macro_header:=3,radix4digit:=32}  # ' \
    'view others/数学/编程/设计/自定义编码纟整数-alnum字母表+5over8效率.txt'
    try:
        return _58_dr4int
    except NameError:
        pass
    _58_gmk_dr4int_dr4rational()
    return gmk_step_decoder4int_with_inf__alnum__5over8_()
def gmk_step_decoder4rational_with_inf__alnum__5over8_():
    '-> IStepDecoder__rational_with_inf{radix4macro_header:=3,radix4digit:=32}  # ' \
    'view others/数学/编程/设计/自定义编码纟整数-alnum字母表+5over8效率.txt'
    try:
        return _58_dr4rational
    except NameError:
        pass
    _58_gmk_dr4int_dr4rational()
    return gmk_step_decoder4rational_with_inf__alnum__5over8_()




def encode4rational_with_inf__alnum__5over8_(xrational, /, *, digits_vs_str:bool):
    '(Rational|-oo|+oo) -> (digits/bytes if digits_vs_str else str/alnum)'
    it = iter_encode4rational_with_inf__alnum__5over8_(xrational, digits_vs_str=digits_vs_str)
    s = '' if digits_vs_str else b''
    r = s.join(it)
    return r
def iter_encode4rational_with_inf__alnum__5over8_(xrational, /, *, digits_vs_str:bool):
    '(Rational|-oo|+oo) -> Iter (digits/bytes if digits_vs_str else str/alnum)'
    if abs(xrational) is +oo:
        xi = xrational
        it = iter_encode4int_with_inf__alnum__5over8_(xi, digits_vs_str=digits_vs_str)
        return it
    rational = xrational
    # [rational :: Rational]
    it = _impl_iter_encode4rational_with_inf__alnum__5over8_(rational)
    if digits_vs_str:
        it = _58_iter_to_str(it)
    return it
def _impl_iter_encode4rational_with_inf__alnum__5over8_(rational, /):
    'Rational -> Iter (digits/bytes)'
    digits_vs_str = False
    #(N, D) = rational.as_integer_ratio()
    (N, D) = (rational.numerator, rational.denominator)
    cf_digits = iter_continued_fraction_digits5ND_(N, D)
    [i, *us] = cf_digits
    to_flip = False
    yield from iter_encode4int_with_inf__alnum__5over8_(i, digits_vs_str=digits_vs_str)
    777;to_flip = not to_flip
    xus = [u-1 for u in us]
    777; del i, us
    if xus:
        xus[-1] -= 1
    assert all(u >= 0 for u in xus)
    xus.append(+oo)
    for xu in xus:
        # [xu :: (uint|+oo)]
        it = _58_iter_encode4uint(xu, head_bytes=b'')
        if to_flip:
            it = _58_flip4body(it)
                #not:_58_iter_flip
                # !! inner body...
        yield from it
        777;to_flip = not to_flip
    return
def encode4int_with_inf__alnum__5over8_(xi, /, *, digits_vs_str:bool):
    '(int|-oo|+oo) -> (digits/bytes if digits_vs_str else str/alnum)'
    it = iter_encode4int_with_inf__alnum__5over8_(xi, digits_vs_str=digits_vs_str)
    s = '' if digits_vs_str else b''
    r = s.join(it)
    return r
def iter_encode4int_with_inf__alnum__5over8_(xi, /, *, digits_vs_str:bool):
    '(int|-oo|+oo) -> Iter (digits/bytes if digits_vs_str else str/alnum)'
    if xi < 0:
        # [xi < 0]
        xu = -xi
        # [xu > 0]
        #head_byte{xi} = b'\x00'
        #head_byte{xu} = b'\x02'
        head_byte = b'\x02'
        it = _58_iter_flip(_58_iter_encode4uint(xu, head_bytes=head_byte))
    elif xi == 0:
        # [xi == 0]
        head_byte = b'\x01'
        it = iter([head_byte])
    else:
        # [xi > 0]
        xu = xi
        # [xu > 0]
        head_byte = b'\x02'
        it = _58_iter_encode4uint(xu, head_bytes=head_byte)
    it
    if digits_vs_str:
        it = _58_iter_to_str(it)
    return it
def _58_flip4body(bs, /):
    '(digits/bytes) -> (digits/bytes)'
    # [31==32-1]
    return bytes(map((31).__sub__, bs))
def _58_iter_flip(it, /):
    'Iter (digits/bytes) -> Iter (digits/bytes)'
    it = iter(it)
    for bs in it:
        if bs:
            break
    else:
        raise 000
    bs
    # [2==3-1]
    yield bytes([2-bs[0]])
    yield _58_flip4body(bs[1:])
    yield from map(_58_flip4body, it)
def _mk_58_tbls():
    from string import digits, ascii_uppercase, ascii_lowercase
    _alphabet4alnum = digits+ascii_uppercase
    alphabet4alnum6body = _alphabet4alnum[:32]
    alphabet4alnum6head = _alphabet4alnum[32:35]
    return (alphabet4alnum6head, alphabet4alnum6body)
(_58_tbl6head, _58_tbl6body) = _mk_58_tbls()
_58_tbl4tr = bytes.maketrans(_58_tbl6body.encode('ascii'), bytes(range(len(_58_tbl6body))))
def _uZdigits_mod32(u, /):
    return uintZbase32_(u).encode('ascii').translate(_58_tbl4tr)

def _58_to_str4body(bs, /):
    '(digits/bytes) -> (str/alnum)'
    return ''.join(map(_58_tbl6body.__getitem__, bs))
def _58_iter_to_str(it, /):
    'Iter (digits/bytes) -> Iter (str/alnum)'
    it = iter(it)
    for bs in it:
        if bs:
            break
    else:
        raise 000
    bs
    yield _58_tbl6head[bs[0]]
    yield _58_to_str4body(bs[1:])
    yield from map(_58_to_str4body, it)
_58_bss = (None, b'\x00', None, b'\x08', None, b'\x00', None, b'\x10', None, b'\x14')
assert len(_58_bss) == 10
def _58_iter_encode4uint(xu, /, *, head_bytes):
    '(uint|+oo) -> Iter (digits/bytes)'
    if head_bytes:
        yield head_bytes
    #######
    #old:uint6int, but now uint6rational
    #.if xu is +oo:
    #.    yield b'\x02\x1E'
    #.elif xu == 0:
    #.    yield b'\x01'
    #.elif xu < 16:
    #.    yield b'\x02'
    #.    yield bytes([xu])
    #.else:
    #.    # [xu >= 16]
    #.    yield b'\x02'
    #.    ...
    #######
    if xu is +oo:
        yield b'\x1E'
    elif xu < 16:
        yield bytes([xu])
    else:
        # [xu >= 16]
        us = []
        u = xu
        # [u >= 16]
        # [u > 1]
        while u > 1:
            # [u > 1]
            us.append(u)
            # [u >= 2]
            nbit = u.bit_length()
            # [nbit >= 2]
            ncell = (nbit+4)//5
            # [ncell >= 1]
            u = ncell
            # [u >= 1]
        assert u == 1
        # [ncell == u == 1]
        assert 2 <= nbit <= 5
        assert us
        assert 2 <= us[-1] <= 31
        us.append(1)
        L = len(us)
        assert L >= 2
        ls = [16, 8, 4, 2]
            # :: [max1{head_cell}]
        if len(ls) > L:
            ls = ls[:L]
        else:
            #ks = (8, 2, 16, 4, 2)
            ks = b'\x08\x02\x10\x04\x02'
            (q,r) = divmod(L-len(ls), len(ks))
            if q:
                ls.extend(ks*q)
            if r:
                ls.extend(ks[:r])
        assert len(ls) == L
        for j, (u, max1) in enumerate(zip(us, ls)):
            if u < max1:break
        else:
            raise 000
        j
        L = j+1
        del us[L:]
        del ls[L:]
        assert L >= 2
        if L > 4:
            # [L >= 5]
            yield b'\x1D' #29
            nbit4prefix = 5+2*(L-4)
            (q, _r) = divmod(nbit4prefix-5-1, 10)
            if q:
                yield b'\x0A\x15'*q # 10,21
            #_58_bss = (b'\x00', b'\x08', b'\x0A\x00', b'\x0A\x10', b'\x0A\x14', b'\x0A\x15\x00')
            #_58_bss = (None, b'\x00', None, b'\x08', None, b'\x0A\x00', None, b'\x0A\x10', None, b'\x0A\x14', None, b'\x0A\x15\x00')
            if _r >= 5:
                yield b'\x0A' # 10
            #_58_bss = (None, b'\x00', None, b'\x08', None, b'\x00', None, b'\x10', None, b'\x14', None, b'\x15\x00')
            if 0:
                _58_bss = (None, b'\x00', None, b'\x08', None, b'\x00', None, b'\x10', None, b'\x14')
                assert len(_58_bss) == 10
            [last_prefix] = _58_bss[_r]
        else:
            # [2 <= L <= 4]
            assert 2 <= L <= 4
            match L:
                case 2:
                    last_prefix = 16 # 32-16
                case 3:
                    last_prefix = 24 # 32-8
                case 4:
                    yield b'\x1C' # 28 # 32-4
                    last_prefix = 0 # next byte
                case _:
                    raise 000
            last_prefix
        last_prefix
        assert last_prefix == 0 or last_prefix >= ls[-1] > us[-1]
        assert last_prefix > 0 or 1 == us[-1]
        u = us.pop()
        if last_prefix == 0:
            if not u == 1:raise 000
            assert us
            pass#skip
        else:
            d = last_prefix | u
            yield bytes([d])
        u
        while us:
            sz = u
            u = us.pop()
            bs = _uZdigits_mod32(u)
            osz = sz -len(bs)
            if osz:
                assert osz > 0
                yield '\x00'*osz
            yield bs
    return
#end-def _58_iter_encode4uint(xu, /):
#end-def iter_encode4int_with_inf__alnum__5over8_(xi, /, *, digits_vs_str:bool):

class _SeqIter:
    #see:iter_subseq__transparent_
    @property
    @override
    def begin(sf, /):
        '#variable'
        return sf._i
    def __init__(sf, seq, /, begin=None, end=None, *, key):
        (begin, end) = mk_seq_rng(seq, begin, end)
        sf._xs = seq
        sf._i = begin
        sf._j = end
        sf._f = key
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        i = sf._i
        if i == sf._j:
            raise StopIteration
        x = sf._xs[i]
        y = sf._f(x)
        sf._i = i+1
        return y

class IDecoder__token_seq(ABC):
    #see:IOps4IterDigitsWithHeadCell
    __slots__ = ()
    @property
    @abstractmethod
    def step_decoder(sf, /):
        '-> IStepDecoder__fixed_radix4macro_header{oresult}'
    @abstractmethod
    def token2head_digit_(sf, token, /):
        'token -> digit8macro_header'
    @abstractmethod
    def token2body_digit_(sf, token, /):
        'token -> digit8body_cell'
    def decode(sf, token_seq, /, begin=None, end=None, *, fullmatch=False, nonnull_remain_ok=False):
        '[token] -> ((((oresult|^Exception__not_fullmatch) if fullmatch else (oresult, new_begin))|^Exception__nonnull_remain) if not nonnull_remain_ok else (oresult, rxdigit8remain/IRadixedDigit, new_begin)) # [not (fullmatch and nonnull_remain_ok)]'
        assert not (fullmatch and nonnull_remain_ok)
        (begin, end) = mk_seq_rng(token_seq, begin, end)
        if not begin < end:
            raise ValueError(token_seq, begin, end)
        digit8H = sf.token2head_digit_(token_seq[begin])
        777;_begin = 1+begin
        digit8H
        dr = sf.step_decoder
        radix_info4H = dr.radix_info4macro_header
        if not 0 <= digit8H < radix_info4H.radix:raise ValueError(digit8H, radix_info4H.radix)
        rxdigit8H = RadixedDigit(radix_info4H, digit8H)
        digit_iter = _SeqIter(token_seq, _begin, end, key=sf.token2body_digit_)
        digit_reader = mk_DigitReader5iter(dr.radix_info4digit, digit_iter)
        ###
        input4step_decoder = Input4StepDecoder(rxdigit8H, digit_reader)
        (oresult, rxdigit8remain) = step_decode__input_(dr, input4step_decoder)
        new_begin = digit_iter.begin
        if nonnull_remain_ok:
            return (oresult, rxdigit8remain, new_begin)
        #not nonnull_remain_ok
        if not rxdigit8remain.is_null:raise Exception__nonnull_remain(rxdigit8remain)
        if not fullmatch:
            return (oresult, new_begin)
        if not new_begin == end:raise Exception__not_fullmatch(new_begin, end)
        #fullmatch
        return oresult
class Exception__nonnull_remain(Exception):pass
class Exception__not_fullmatch(Exception):pass
#end-class IDecoder__token_seq(ABC):
Exception__nonnull_remain
Exception__not_fullmatch

def _mk_alnum2digit_(alphabet4alnum, /):
     alnum2digit = {c:j for j,c in enumerate(alphabet4alnum)}
     for c in alphabet4alnum:
         alnum2digit[c.lower()] = alnum2digit[c]
     return alnum2digit
_58_2digit6head = _mk_alnum2digit_(_58_tbl6head)
_58_2digit6body = _mk_alnum2digit_(_58_tbl6body)
class _58_IDecoder__token_seq(IDecoder__token_seq):
    ___no_slots_ok___ = True
    def __init__(sf, /):
        pass
    @cached_property
    #@override
    def token2head_digit_(sf, /):
        return _58_2digit6head.__getitem__
    @cached_property
    #@override
    def token2body_digit_(sf, /):
        return _58_2digit6body.__getitem__
######################
class _58_4int_Decoder__token_seq(_58_IDecoder__token_seq):
    @cached_property
    @override
    def step_decoder(sf, /):
        return gmk_step_decoder4int_with_inf__alnum__5over8_()
_58_decode4int = _58_4int_Decoder__token_seq().decode
def decode4int_with_inf__alnum__5over8_(_58_alnum_str, /, begin=None, end=None, *, fullmatch=False, nonnull_remain_ok=False):
    'str/alnum -> ((((oresult|^Exception__not_fullmatch) if fullmatch else (oresult, new_begin))|^Exception__nonnull_remain) if not nonnull_remain_ok else (oresult, rxdigit8remain/IRadixedDigit, new_begin)) # [not (fullmatch and nonnull_remain_ok)]'
    return _58_decode4int(_58_alnum_str, begin, end, fullmatch=fullmatch, nonnull_remain_ok=nonnull_remain_ok)
encode4int_with_inf__alnum__5over8_
decode4int_with_inf__alnum__5over8_
######################

######################
class _58_4rational_Decoder__token_seq(_58_IDecoder__token_seq):
    @cached_property
    @override
    def step_decoder(sf, /):
        return gmk_step_decoder4rational_with_inf__alnum__5over8_()
_58_decode4rational = _58_4rational_Decoder__token_seq().decode
def decode4rational_with_inf__alnum__5over8_(_58_alnum_str, /, begin=None, end=None, *, fullmatch=False, nonnull_remain_ok=False):
    'str/alnum -> ((((oresult|^Exception__not_fullmatch) if fullmatch else (oresult, new_begin))|^Exception__nonnull_remain) if not nonnull_remain_ok else (oresult, rxdigit8remain/IRadixedDigit, new_begin)) # [not (fullmatch and nonnull_remain_ok)]'
    return _58_decode4rational(_58_alnum_str, begin, end, fullmatch=fullmatch, nonnull_remain_ok=nonnull_remain_ok)
encode4rational_with_inf__alnum__5over8_
decode4rational_with_inf__alnum__5over8_
######################

_58_4int_Decoder__token_seq
Ops4IterDigitsWithHeadCell__functional
class _58_Ops4IterDigitsWithHeadCell(IOps4IterDigitsWithHeadCell):
    'for both:int,rational'
    ___no_slots_ok___ = True
    def __init__(sf, /):
        pass
    @cached_property
    @override
    def radix_info4macro_header(sf, /):
        return RadixInfo(3)
        return gmk_step_decoder4int_with_inf__alnum__5over8_().radix_info4macro_header
        return gmk_step_decoder4rational_with_inf__alnum__5over8_().radix_info4macro_header
    @cached_property
    #@override
    def may_token2head_digit_(sf, /):
        return _58_2digit6head.__getitem__
    @cached_property
    #@override
    def may_token2body_digit_(sf, /):
        return _58_2digit6body.__getitem__
#end-class _58_Ops4IterDigitsWithHeadCell(IOps4IterDigitsWithHeadCell):

######################
if 0: _58_inc_decode4int = ...
def _gmk_58_inc_decode4int():
    global _58_inc_decode4int
    try:
        return _58_inc_decode4int
    except NameError:
        pass
    _58_inc_decode4int = mk_incremental_decode5ops4iter_headed_digits_(gmk_step_decoder4int_with_inf__alnum__5over8_(), _58_Ops4IterDigitsWithHeadCell())
    return _gmk_58_inc_decode4int()


encode4int_with_inf__alnum__5over8_
decode4int_with_inf__alnum__5over8_
def incremental_decode4int_with_inf__alnum__5over8_(may_wst7inc, s, /):
    'may wst7inc -> str/alnum -> wresult7inc'
    _58_inc_decode4int = _gmk_58_inc_decode4int()
    wresult7inc = _58_inc_decode4int(may_wst7inc, s)
    return wresult7inc
encode4int_with_inf__alnum__5over8_
decode4int_with_inf__alnum__5over8_
incremental_decode4int_with_inf__alnum__5over8_
    #TODO:test
######################




######################
if 0: _58_inc_decode4rational = ...
def _gmk_58_inc_decode4rational():
    global _58_inc_decode4rational
    try:
        return _58_inc_decode4rational
    except NameError:
        pass
    _58_inc_decode4rational = mk_incremental_decode5ops4iter_headed_digits_(gmk_step_decoder4rational_with_inf__alnum__5over8_(), _58_Ops4IterDigitsWithHeadCell())
    return _gmk_58_inc_decode4rational()


encode4rational_with_inf__alnum__5over8_
decode4rational_with_inf__alnum__5over8_
def incremental_decode4rational_with_inf__alnum__5over8_(may_wst7inc, s, /):
    'may wst7inc -> str/alnum -> wresult7inc'
    _58_inc_decode4rational = _gmk_58_inc_decode4rational()
    wresult7inc = _58_inc_decode4rational(may_wst7inc, s)
    return wresult7inc
encode4rational_with_inf__alnum__5over8_
decode4rational_with_inf__alnum__5over8_
incremental_decode4rational_with_inf__alnum__5over8_
    #TODO:test
######################











import builtins as _B
def _prepare_prefix_tree4val(v, /):
    match v:
        #.case ... | None:
            #『case ...:』SyntaxError: invalid syntax
        case _B.Ellipsis | None:
            #None/undefined_interval
            #.../reserved_interval
            r = v
        case (0, x):
            #(0,arg8prefix_tree4step_decoder/extend_macro_header)
            r = PrefixTree4step_decoder.mk_prefix_tree4step_decoder_(x)
        case ((1|2|3) as case, payload):
            #(1,oresult)
            #(2,peculiar_args4step_decoder)
            #(3,step_decoder)
            r = Target4prefix_tree4step_decoder(Cased(case, payload))
        case _:
            raise 000
    r
    return r

def _prepare_prefix_tree(dict_or_pairs, /):
    if hasattr(dict_or_pairs, 'items'):
        d = dict_or_pairs
        pairs = d.items()
    else:
        pairs = dict_or_pairs
    pairs
    ps = sorted(pairs, key=fst)
    f = _prepare_prefix_tree4val
    d = mk_MapView_({k:f(v) for k, v in ps})
    us = tuple(map(fst, ps))
    ts = tuple(map(snd, ps))
    return (d, us, ts)
class PrefixTree4step_decoder:
    'prefix_tree4step_decoder'
    @classmethod
    def mk_prefix_tree4step_decoder_(cls, arg8prefix_tree4step_decoder, /):
        x = arg8prefix_tree4step_decoder
        if isinstance(x, __class__):
            sf = x
        else:
            dict_or_pairs = x
            sf = cls(dict_or_pairs)
    def __init__(sf, dict_or_pairs, /):
        sf._d, sf._us, sf._ts = _prepare_prefix_tree(dict_or_pairs)
        sf._filled = False
            #turn-on by fill_prefix_tree_()
    @property
    def filled(sf, /):
        '-> bool{turn-on by fill_prefix_tree_()}'
        return sf._filled
    @property
    def mapping_view(sf, /):
        '-> {max1:target4prefix_tree}'
        return sf._d
    @property
    def sorted_max1_seq_view(sf, /):
        '-> [max1]'
        return sf._us
    @property
    def ordered_target_seq_view(sf, /):
        '-> [target4prefix_tree]{correspondent with sorted_max1_seq_view}'
        return sf._ts
    def __len__(sf, /):
        return len(sf._d)
    ######################
    def fill_prefix_tree_(sf, dr, /):
        'IStepDecoder__hardwired__prefix_tree -> None{sf.filled}'
        if sf.filled:return
        prefix_tree4step_decoder = dr.prefix_tree4step_decoder
        common_args4step_decoder = dr.common_args4step_decoder
        mkr4step_decoder = dr.mkr4step_decoder
        fill_prefix_tree_(mkr4step_decoder, common_args4step_decoder, prefix_tree4step_decoder, dr.radix_info4digit)
        assert sf.filled
    ######################
class Target4prefix_tree4step_decoder:
    'tgt/target4prefix_tree'
    def __init__(sf, cased_target, may_step_decoder, /):
        check_type_is(Cased, cased_target)
        sf._ct = cased_target
        sf._ms = may_step_decoder
    def __repr__(sf, /):
        return repr_helper(sf, sf.cased_target, sf._ms)
    @property
    def cased_target(sf, /):
        return sf._ct
    @property
    def step_decoder(sf, /):
        m = sf._ms
        if m is None:raise AttributeError('step_decoder')
        return m
    @step_decoder.setter
    def step_decoder(sf, step_decoder, /):
        if not sf._ms is None:raise AttributeError('step_decoder')
        sf._ms = step_decoder


class IStepDecoder__hardwired__prefix_tree(IStepDecoder__fixed_radix4macro_header):
    r'''[[[
    [arg8prefix_tree4step_decoder =[def]= nonempty({max1:arg8target4prefix_tree}|[(max1:arg8target4prefix_tree)]|prefix_tree4step_decoder)]
    [prefix_tree4step_decoder :: PrefixTree4step_decoder]
    [radix4macro_header =[def]= max(prefix_tree4step_decoder)]
    [num_intervals4macro_header =[def]= len(prefix_tree4step_decoder)]
    [arg8target4prefix_tree =[def]= (None/undefined_interval|.../reserved_interval|(0,arg8prefix_tree4step_decoder/extend_macro_header)|(1,oresult)|(2,peculiar_args4step_decoder)|(3,step_decoder))]
    [target4prefix_tree :: (None/undefined_interval|.../reserved_interval|Target4prefix_tree4step_decoder)]
    [mkr4step_decoder :: common_args4step_decoder -> fixed_min_prefix4step_decoder -> fixed_radix_prefix4step_decoder -> whole_head_radix4step_decoder -> peculiar_args4step_decoder -> step_decoder]
    [common_args4step_decoder :: (radix4digit, ...usrdefined...)]
    [begin_size_pair_prefix4step_decoder :: [(begin/min{interval}, size/radix/len{interval})]] =>:
        [fixed_min_prefix4step_decoder :: [uint]]
        [fixed_max_prefix4step_decoder :: [uint]]
        [fixed_radix_prefix4step_decoder :: [uint{>=1}]]
            => [whole_head_radix4step_decoder :: [uint{>=1}]]
        # [fixed_prefix4step_decoder]
        # [radix4macro_header4step_decoder]
    #]]]'''#'''
    #级:grade level class stage step degree cascade
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def mkr4step_decoder(sf, /):
        '-> (common_args4step_decoder -> fixed_min_prefix4step_decoder -> fixed_radix_prefix4step_decoder -> whole_head_radix4step_decoder -> peculiar_args4step_decoder -> step_decoder)'
    @property
    @abstractmethod
    def common_args4step_decoder(sf, /):
        '-> common_args4step_decoder{radix4digit == common_args4step_decoder[0]}'
    @property
    @abstractmethod
    def prefix_tree4step_decoder(sf, /):
        '-> prefix_tree4step_decoder/PrefixTree4step_decoder{Target4prefix_tree4step_decoder}'
    ######################
    @cached_property
    @override
    def radix_info4digit(sf, /):
        radix4digit = sf.common_args4step_decoder[0]
        radix_info4digit = RadixInfo(radix4digit)
        return radix_info4digit
    @cached_property
    @override
    def radix_info4macro_header(sf, /):
        #radix4macro_header = max(sf.prefix_tree4step_decoder.mapping_view)
        radix4macro_header = sf.prefix_tree4step_decoder.sorted_max1_seq_view[-1]
        return RadixInfo(radix4macro_header)
    ######################
    @override
    def start_(sf, rxdigit8macro_header, /):
        tree = sf.prefix_tree4step_decoder
        if not tree.filled:
            tree.fill_prefix_tree_(sf)
        return sf._work(rxdigit8no_bits, rxdigit8macro_header, tree)
    def _work(sf, rxdigit8acc, rxdigit8H, tree, /):
        # [tree.filled]
        assert tree.filled
        digit8H = rxdigit8H.digit
        us = tree.sorted_max1_seq_view
        j = bisect_right(us, digit8H)
        # !! [0 <= digit8H < radix4macro_header == us[-1]]
        # [0 <= j < len(us)]
        offset = 0 if j==0 else us[j-1]
        assert offset <= digit8H < us[j]
        _radix4H = us[j] -offset
        _digit8H = digit8H -offset
        _radix_info4H = RadixInfo(_radix4H)
        _rxdigit8H = RadixedDigit(_radix_info4H, _digit8H)
        _rxdigit8acc = rxdigit8acc.merge_rxdigit_(_rxdigit8H)
        x = tree.ordered_target_seq_view[j]
        if x is ... or x is None:
            raise ReservedAreaException(x)
        if type(x) is Target4prefix_tree4step_decoder:
            tgt = x
            return _TCallST.mk_tail_call_st5three_args_(None,   tgt.step_decoder,_rxdigit8acc, state_vs_rxdigit=True)
        assert type(x) is PrefixTree4step_decoder
        inner_tree = x
        return _LoopST(Cased(False, inner_tree),  _rxdigit8acc,  1)
    @override
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        st = loop_st7nonfinal
        assert st.case is False
        [digit] = required_digits
        rx8low = RadixedDigit(sf.radix_info4digit, digit)
        rx8acc = st.rxdigit8remain
        tree = st.payload
        return sf._work(rx8acc, rx8low, tree)
    #@override
    feed_oresult_remain_ = _Dead.feed_oresult_remain_
    ######################
def fill_prefix_tree_(mkr4step_decoder, common_args4step_decoder, prefix_tree4step_decoder, radix_info4digit=None, /):
    if prefix_tree4step_decoder.filled:return
    if radix_info4digit is None:
        radix4digit = common_args4step_decoder[0]
        radix_info4digit = RadixInfo(radix4digit)
    radix_info4digit
    fixed_min_prefix = []
    fixed_radix_prefix = []
    whole_head_radixes = [1]
    T = Target4prefix_tree4step_decoder
    P = PrefixTree4step_decoder
    def recur_(prefix_tree4step_decoder, /):
        check_type_is(P, prefix_tree4step_decoder)
        if prefix_tree4step_decoder._filled:return
        begin = 0
        for end, x in zip(prefix_tree4step_decoder.sorted_max1_seq_view, prefix_tree4step_decoder.ordered_target_seq_view):
            radix = end-begin
            check_int_ge(1, radix)
            fixed_min_prefix.append(begin)
            fixed_radix_prefix.append(radix)
            whole_head_radixes.append(whole_head_radix4step_decoder:=radix*whole_head_radixes[-1])
            777; begin = end
            if x is ... or x is None:
                pass
            elif type(x) is T:
              if not hasattr(x, 'step_decoder'):
                tgt = x
                match tgt.cased_target:
                    case (1,oresult):
                        step_decoder = StepDecoder__constant_oresult(radix_info4digit, oresult)
                    case (2,peculiar_args4step_decoder):
                        step_decoder = mkr4step_decoder(common_args4step_decoder, tuple(fixed_min_prefix), tuple(fixed_radix_prefix), whole_head_radix4step_decoder, peculiar_args4step_decoder)
                    case (3,step_decoder):
                        step_decoder
                        pass
                    case _:
                        raise 000
                tgt.step_decoder = step_decoder
            else:
                recur_(x)
            fixed_min_prefix.pop()
            fixed_radix_prefix.pop()
            whole_head_radixes.pop()
        #for end, x in zip(prefix_tree4step_decoder.sorted_max1_seq_view, prefix_tree4step_decoder.ordered_target_seq_view):
        prefix_tree4step_decoder._filled = True
    recur_(prefix_tree4step_decoder)
    return

#end-class IStepDecoder__hardwired__prefix_tree(IStepDecoder__fixed_radix4macro_header):

class StepDecoder__hardwired__prefix_tree(IStepDecoder__hardwired__prefix_tree):
    ___no_slots_ok___ = True
    def __init__(sf, mkr4step_decoder, common_args4step_decoder, arg8prefix_tree4step_decoder, /):
        check_callable(mkr4step_decoder)
        check_type_is(tuple, common_args4step_decoder)
        #check_radix_info4digit
        check_int_ge(2, radix4digit:=common_args4step_decoder[0])
        prefix_tree4step_decoder = PrefixTree4step_decoder.mk_prefix_tree4step_decoder_(arg8prefix_tree4step_decoder)
        check_type_is(PrefixTree4step_decoder, prefix_tree4step_decoder)
        sf._mk = mkr4step_decoder
        sf._cs = common_args4step_decoder
        sf._tr = prefix_tree4step_decoder
    def __repr__(sf, /):
        return repr_helper(sf, sf.mkr4step_decoder, sf.common_args4step_decoder, sf.prefix_tree4step_decoder)
    @property
    @override
    def mkr4step_decoder(sf, /):
        return sf._mk
    @property
    @override
    def common_args4step_decoder(sf, /):
        return sf._cs
    @property
    @override
    def prefix_tree4step_decoder(sf, /):
        return sf._tr
check_non_ABC(StepDecoder__hardwired__prefix_tree)
['common_args4step_decoder', 'mkr4step_decoder', 'prefix_tree4step_decoder']











































































__all__
def __():
    if 0:
        #before:mk_namedtuple_-->mk_named_pseudo_tuple_
        x = StepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers
        assert isinstance(x, type)
        assert issubclass(x, tuple)
        assert isinstance(x.radix_info4digit, cached_property)
        assert not "radix_info4digit" in vars(x)
        #assert "radix_info4digit" in vars(x), ','.join(sorted(vars(x)))
            #AssertionError: ___no_slots_ok___,__abstractmethods__,__dict__,__doc__,__module__,_abc_impl
        assert "radix_info4digit" in dir(x), ','.join(sorted(dir(x)))
        #raise 000
    Nothing = object()
    for nm in __all__:
        x = globals()[nm]
        if isinstance(x, type) and issubclass(x, tuple):
            #print_err(f'{nm}<:tuple')
            #for attr, f in vars(x).items():
            for attr in sorted(dir(x)):
                f = getattr(x, attr, Nothing)
                if f is Nothing:continue
                #print_err(f'{nm}.{attr}:={f}')
                if isinstance(f, cached_property):
                    print_err(f'{nm}.{attr}::tuple.cached_property')
                    #raise 000
__()
    #before:mk_namedtuple_-->mk_named_pseudo_tuple_
        #StepDecoder__plugin4finite_uint_interval__fixed_size_layers.layer_idx2uint_linear_transform::tuple.cached_property
        #StepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers.radix_info4digit::tuple.cached_property



__all__
from seed.int_tools.StepDecoder import encode4int_with_inf__alnum__5over8_, iter_encode4int_with_inf__alnum__5over8_, decode4int_with_inf__alnum__5over8_, gmk_step_decoder4int_with_inf__alnum__5over8_
from seed.int_tools.StepDecoder import incremental_decode4int_with_inf__alnum__5over8_


from seed.int_tools.StepDecoder import Exception__nonnull_remain, Exception__not_fullmatch, Exception__min_layer_idx4end_by_cell_boundary, ReservedAreaException, InfiniteException__nonzero_rxdigit8remain

from seed.int_tools.StepDecoder import IDecoder__token_seq, IStepDecoder, step_decode__input_, step_decode__head_, step_decode__state_

from seed.int_tools.StepDecoder import IBaseState4StepDecoder, ILoopState4StepDecoder, ICallState4StepDecoder

from seed.int_tools.StepDecoder import IInput4StepDecoder, IPartialOutput4StepDecoder, IFullOutput4StepDecoder

from seed.int_tools.StepDecoder import IUIntLinearTransform
from seed.int_tools.StepDecoder import IOps4IterDigitsWithHeadCell

from seed.int_tools.StepDecoder import CallEntry4StepDecoder, Kind4State4StepDecoder, LoopState4StepDecoder__plain, CallState4StepDecoder__plain, mk_nontail_call_st4step_decoder_, TailCallState4StepDecoder__plain, mk_tail_call_st4step_decoder_, XCallState4StepDecoder__plain


from seed.int_tools.StepDecoder import Input4StepDecoder, PartialOutput4StepDecoder, FullOutput4StepDecoder


from seed.int_tools.StepDecoder import UIntLinearTransform, uint_linear_transform8echo
from seed.int_tools.StepDecoder import Ops4IterDigitsWithHeadCell__functional

from seed.int_tools.StepDecoder import StepDecoder__dynamic_bits, StepDecoder__fixed_size_xbcells, StepDecoder__fixed_size_xbcells__zeroth_layer4body4infinite_uint_interval, StepDecoder__dynamic_bibits, StepDecoder__flatten, StepDecoder__flip_digits, StepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits, StepDecoder__constant_oresult


from seed.int_tools.StepDecoder import StepDecoder__fixed_size_layers__body4infinite_uint_interval, StepDecoder__plugin4finite_uint_interval__extend_macro_header, StepDecoder__plugin4finite_uint_interval__parallel__partition_space4macro_header, StepDecoder__plugin4finite_uint_interval__fixed_size_layers, StepDecoder__plugin4infinite_uint_interval__extend_macro_header, StepDecoder__plugin4infinite_uint_interval__parallel__partition_space4macro_header, StepDecoder__plugin4infinite_uint_interval__truncated_dynamic_bits_with_may_dynamic_bibits_with_dependent_size_layers



from seed.int_tools.StepDecoder import StepDecoder__uint_with_inf, StepDecoder__int_with_inf, gmk_step_decoder4int_with_inf__alnum__5over8_, StepDecoder__rational_with_inf






from seed.int_tools.StepDecoder import IStepDecoder__hardwired__prefix_tree

from seed.int_tools.StepDecoder import StepDecoder__hardwired__prefix_tree, fill_prefix_tree_, PrefixTree4step_decoder, Target4prefix_tree4step_decoder



from seed.int_tools.StepDecoder import incremental_decode__continued_, incremental_decode__init5head_, incremental_decode__init5state_, prepare_step_decoder4incremental_decode_
from seed.int_tools.StepDecoder import incremental_decode__headed_digits_, Ops4IterDigitsWithHeadCell__functional, incremental_decode__ops4iter_headed_digits_, mk_incremental_decode5ops4iter_headed_digits_, incremental_decode4int_with_inf__alnum__5over8_
if 0:from seed.int_tools.StepDecoder import Mkr4incremental_decode5ops4iter_headed_digits


from seed.int_tools.StepDecoder import *
