#__all__:goto
#[:___main_exports___]:goto
#[:define____std_flattenable]:goto
r'''[[[[[
see also:
    seed.iters.flatten_recur
        view ../../python3_src/seed/iters/flatten_recur.py
    seed.func_tools.recur5yield
        view ../../python3_src/seed/func_tools/recur5yield.py
            without halfway-result/exception
            without boxed-final-exception
    seed.func_tools.recur5yield__halfway
        view ../../python3_src/seed/func_tools/recur5yield__halfway.py
            with halfway-result/exception
            with boxed-final-exception


[[
@20240828:
mv -iv ../../python3_src/seed/func_tools/recur5yield.py ../../python3_src/seed/func_tools/recur5yield__halfway.py
/sdcard/0my_files/git_repos/[20240828]python3_src.zip
cd $my_git_py
git checkout -- seed/func_tools/recur5yield.py
cd $my_git_txt
7z a  ../../python3_src/seed/func_tools/recur5yield-two_versions@20240828.7z  ../../python3_src/seed/func_tools/recur5yield.py  ../../python3_src/seed/func_tools/recur5yield__halfway.py
7z l  ../../python3_src/seed/func_tools/recur5yield-two_versions@20240828.7z

e ../../python3_src/seed/func_tools/recur5yield__halfway.py
%s/\<recur5yield\>\C/recur5yield__halfway/g
]]

e ../../python3_src/seed/func_tools/recur5yield__halfway.py
py -m seed.func_tools.recur5yield__halfway
py -m nn_ns.app.debug_cmd   seed.func_tools.recur5yield__halfway -x
py -m nn_ns.app.doctest_cmd seed.func_tools.recur5yield__halfway:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.func_tools.recur5yield__halfway:__doc__ -ht


[[
fixed_bug____BoxedTailRecur__X__BoxedHalfwayResult:goto
bug:BoxedTailRecur&&BoxedHalfwayResult
    gi0->BoxedTailRecur(gi1)
    gi1->BoxedHalfwayResult(rhr)->...->BoxedFinalResult(rfr)
    ==>>:
    rhr = yield gi0
    assert is_gi_closed(gi0)
        # next(gi0) -> ^StopIteration(None) #not BoxedFinalResult(rfr)
    ==>>:
    fix: replace gi0 by gi1 if not closed
        rhr --> (rhr, gi1)
    ==>>:
        rhr_or_rfr --> rhr_gi_or_rfr
        rhe_or_rfe --> rhe_gi_or_rfe
        ++HalfwayResultAndTailGI
        ++HalfwayExceptionAndTailGI
===
from seed.lang.generator_iterator_ops import is_gi_closed, is_gi_beginning, is_gi_running, is_gi_waiting
]]
[[
[:___main_exports___]:here
from seed.func_tools.recur5yield__halfway import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception, detach_asif_new_gi_wrapper
from seed.func_tools.recur5yield__halfway import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield__halfway import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
from seed.func_tools.recur5yield__halfway import recur5yield__list__echo__echo
### from seed.types.Either import Either


]]
[[
DONE
new:feature__halfway_exception
    counterpart of feature__halfway_result
]]
[[
DONE:multi-phase-output/return
new:feature__halfway_result
required from:
    view ../../python3_src/seed/recognize/recognizer_LLoo.py
        as-if:iter-output:
            + (optional)header_signal
            + (required)xresult4LLoo

]]
[[
typing:def:
### flattenable ~= awaitable
flattenable == customizable_flattenable
customizable_flattenable --[child_gi_protocol]--> std_flattenable
[customizable_flattenable(exprlist5yield,return_value5child;) =[def]=
as-if-IGeneratorIterator<yield-exprlist5yield, return-return_value5child>
]

[not [intermediate_output <: std_flattenable]]:
    [std_flattenable(intermediate_output,final_result;) =[def]= boxed_builtin_gi/IGeneratorIterator
        <yield-(std_flattenable(?t,?r;)|intermediate_output)
        ,return5yield-((?t|?r){distinguished by is_gi_closed/mk_gi4either8xresult} if yield std_flattenable else ???{yield intermediate_output=>feedback is userdefined})
        ,return-Either(tail_gi/tail_recur/std_flattenable(intermediate_output,final_result;), final_result;)
        >
        ++property:to enable is_gi_closed/gi_next__catch/...
        gi.gi_frame
        gi.gi_running
        gi.gi_suspended

++:
    #[fr::final_result(bfr/boxed_final_result|rfr/raw_final_result)]
    #[hr::halfway_result(bhr/boxed_halfway_result|rhr/raw_halfway_result)]
    gi.___666_mk_xresult_999___ :: (rhr_gi_or_rfr, /, *, rhr_vs_rfr) -> xresult
    #xxx:boxed_halfway_result.___666_is_halfway_result_999___
    boxed_halfway_result.unbox() -> raw_halfway_result
    [boxed_halfway_result :: BoxedHalfwayResult]
    [not [BoxedHalfwayResult <: IGeneratorIterator]]

update:
    child_gi_protocol(exprlist5yield) -> generator_iterator
    -->:
    child_gi_protocol(exprlist5yield) -> gi_or_bhr/(generator_iterator|boxed_halfway_result)
    -->:
    child_gi_protocol(exprlist5yield) -> gi_or_bhr_or_bhe/(generator_iterator|boxed_halfway_result|boxed_ halfway_exception)
]
#multi_phase_output/intermediate_output/halfway_result
gi_next__catch(std_flattenable(intermediate_output,final_result;)) -> Either(final_result,intermediate_output;)

view ../../python3_src/seed/lang/generator_iterator_ops.py
from seed.lang.generator_iterator_ops import gi_next__catch, gi_next, gi_start, gi_send, OccasionError
from seed.lang.generator_iterator_ops import  is_gi__builtin, is_gi__ABC, is_gi_maker
from seed.lang.generator_iterator_ops import is_gi_closed, is_gi_beginning, is_gi_runing, is_gi_waiting

]]
[[
[:define____std_flattenable]:here
redefine:std_flattenable

std <<==:
    std_flattenable using tail_recur_gi_protocol__echo
    std_flattenable using child_gi_protocol__echo
    std_flattenable using child_gi_exc_protocol__echo

std_flattenable(raw_halfway_exception,raw_final_exception;raw_halfway_result,raw_final_result;)
[std_flattenable(rhe,rfe;rhr,rfr;) =[def]= IGeneratorIterator
        <return-Either(std_flattenable(rhe,rfe;rhr,rfr;), rfr;)
            # | (False, tail_gi/tail_recur)
            # | (True, raw_final_result)
            #support: BoxedTailRecur|BoxedFinalResult
            #support: Either
            #support: tuple<bool,gi_or_rfr>
        ,yield-std_flattenable(?rhe,?rfe;?rhr,?rfr;)
            =>return5yield-(?rhr|?rfr)[#distinguished<<==mk_gi4either8xresult()#]
            =>raise5yield-(?rhe|?rfe|Escaped)[#except:BoxedException will be Escaped#]
        ,yield-BoxedHalfwayResult(rhr)
            =>return5yield-?userdefined
            =>raise5yield-?userdefined
            [#vivi:normal coroutine:feedback is userdefined#]
        ,yield-BoxedException__halfway(rhe)
            =>return5yield-?userdefined
            =>raise5yield-?userdefined
        ,raise-BoxedException__final(rfe)
        >
]

===
customized_flattenable[tail_recur_gi_protocol,child_gi_protocol,child_gi_exc_protocol;](raw_halfway_exception,raw_final_exception;raw_halfway_result,raw_final_result;input4yield,input4raise,input4return;)
customized_flattenable[tail_recur_gi_protocol,child_gi_protocol,child_gi_exc_protocol;](rhe,rfe;rhr,rfr;i4y,i4e,i4t;)
    [tail_recur_gi_protocol :: i4t -> Either tail_recur rfr]
        [tail_recur :: customized_flattenable[tail_recur_gi_protocol,child_gi_protocol,child_gi_exc_protocol;](rhe,rfe;rhr,rfr;i4y,i4e,i4t;)]
    [child_gi_protocol :: i4y -> (child_gi|BoxedHalfwayResult(rhr)|BoxedException__halfway(rhe))]
        [child_gi :: customized_flattenable[tail_recur_gi_protocol,child_gi_protocol,child_gi_exc_protocol;](?rhe,?rfe;?rhr,?rfr;?i4y,?i4e,?i4t;)]
            #child_gi param choice SHOULD preserve the global settings [tail_recur_gi_protocol,child_gi_protocol,child_gi_exc_protocol;]
    [child_gi_exc_protocol :: (() -> (v|^?i4e)) -> (v|^BoxedException__final(?rfe))]

===
]]
[[
TODO:++child_gi_exc_protocol :: (() -> (v|^i4e)) -> (() -> (v|^BoxedException__final))
new:feature__customizable__boxed_final_exception

API_changed:
    #++child_gi_exc_protocol
    recur5yield__decoratorT__all_gi_protocols
    recur5yield__eval__main_generator_iterator
API_changed:
    #++child_gi_exc_protocol_vs_may_echo_vs_turnoff
    RecurGroupCollector4Recur5Yield.__init__
    HelperPseudoMeta8Recur5Yield

]]






from seed.func_tools.recur5yield__halfway import HelperPseudoMeta8Recur5Yield

xxxxxxx from seed.func_tools.recur5yield__halfway import recur5yield__echo__echo, recur5yield__echo__off, recur5yield__0func__echo, recur5yield__0func__off

from seed.func_tools.recur5yield__halfway import recur5yield__list__echo__echo, recur5yield__list__echo__off, recur5yield__list__0func__echo, recur5yield__list__0func__off

from seed.func_tools.recur5yield__halfway import recur5yield__huge__echo__echo, recur5yield__huge__echo__off, recur5yield__huge__0func__echo, recur5yield__huge__0func__off

from seed.func_tools.recur5yield__halfway import recur5yield__eval__main_generator_iterator
from seed.func_tools.recur5yield__halfway import recur5yield__decoratorT__all_gi_protocols, child_gi_protocol__echo, child_gi_protocol__0func, child_gi_protocolT__0func5ref, tail_recur_gi_protocol__echo, tail_recur_gi_protocol__off

from seed.func_tools.recur5yield__halfway import RecurGroupCollector4Recur5Yield
from seed.func_tools.recur5yield__halfway import explain__child_gi_protocol_vs_may_0ref4func_vs_echo, explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff, explain__emplace_stack_ops_vs_may_ops4list_vs_ops4huge, explain__may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case
from seed.func_tools.recur5yield__halfway import child_gi_protocol6getitemable__0case, child_gi_protocol6getitemable__0func, child_gi_protocol6getitemableT__0func5ref


[[
yield 实现 recur on container-list instead of python-stack

  @recur5yield__halfway(caller)
  def f(...):
      x = yield ...
      return x
  互调用递归组:
  @recur5yield__halfway(caller, 在互调用递归组中的命名)

===
print(sys.getrecursionlimit()) # Prints 1000
print(sys.setrecursionlimit(2000))

https://www.codingem.com/python-maximum-recursion-depth/
What Is the Maximum Recursion Depth in Python?
1000
Python uses a maximum recursion depth of 1000 to ensure no stack overflow errors and infinite recursions are possible. This recursion limit is somewhat conservative, but it is reasonable as stack frames can become big in Python. Stack overflow error is usually caused by too deep (or infinite) recursion.

]]


==========
[[[typing:
exprlist5yield, result5recur, value4send
    result5recur = value4send = yield exprlist5yield
    return return_value5child
    #not: return result5recur

IGeneratorIterator === collections.abc.Generator <: Iterator
generator_iterator :: IGeneratorIterator<yield-exprlist5yield, return-return_value5child>
    main_generator_iterator <: generator_iterator
generator :: Callable
    not [generator :: Iterator]
generator(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
    to avoid confuse generator with generator_iterator, below rename generator to generator_func
        # generator?(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
        #   generator =?= generator_func | ?generator_iterator?


generator_func(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
    main_generator_func(*args4main, **kwds4main) -> generator_iterator
    ###child_gi_protocol(exprlist5yield) -> generator_iterator
    ###child_gi_protocol(exprlist5yield) -> gi_or_bhr/(generator_iterator|boxed_halfway_result)
    child_gi_protocol(exprlist5yield) -> gi_or_bhr_or_bhe/(generator_iterator|boxed_halfway_result|boxed_ halfway_exception)
        rename history:
            recur_branch_generator_iterator_maker
            recur_branch_gen_iter_protocol
            recur_branch_gi_protocol
            child_gi_protocol
    child_gi_protocol6getitemable(getitemable, exprlist5yield) -> generator_iterator
        child_gi_protocol6collector(collector, exprlist5yield) -> generator_iterator
            collector :: RecurGroupCollector4Recur5Yield

tail_recur_gi_protocol(return_value5child) -> either_tailrecur_result/(is_result5recur, payload)/((False, exprlist5yield)|(True, result5recur))

]]]
==========
==========
[[[

>>> import sys
>>> saved_recursion_limit = sys.getrecursionlimit()
>>> saved_recursion_limit
1000
>>> sys.setrecursionlimit(200)

>>> def __():
...     def mul(n, m, /):
...         assert not m < 0
...         assert not n < 0
...         return mul_(0, n, m)
...     def mul_(acc, n, m, /):
...         if m == 0:
...             return acc
...         m = dec(m)
...         acc = add(acc, n)
...         return mul_(acc, n, m)
...     def add(n, m, /):
...         if m == 0:
...             return n
...         m = dec(m)
...         n = inc(n)
...         return add(n, m)
...     def inc(n, /):
...         return n+1
...     def dec(n, /):
...         return n-1
...     return mul
>>> mul = __()
>>> mul(100, 233)
Traceback (most recent call last):
    ...
RecursionError: maximum recursion depth exceeded
>>> mul(100, 60)
6000




>>> collector = RecurGroupCollector4Recur5Yield(None, None, None, None, None)
>>> @collector.put_named_generator_func
... def f():
...     yield
>>> f is None
True
>>> 'f' in collector
True
>>> callable(collector['f'])
True
>>> collector.put_named_generator_func(collector['f']) #same callable is ok
>>> @collector.put_named_generator_func #doctest: +ELLIPSIS
... def f():    #not same callable => raise
...     yield
Traceback (most recent call last):
    ...
ValueError: ('f', <function f at 0x...>, <function f at 0x...>)

>>> def __():
...     @recur5yield__list__echo__echo
...     def mul(n, m, /):
...         assert not m < 0
...         assert not n < 0
...         return False, mul_(0, n, m)
...         yield
...     def mul_(acc, n, m, /):
...         if m == 0:
...             return True, acc
...         m = yield dec(m)
...         acc = yield add(acc, n)
...         return False, mul_(acc, n, m)
...     def add(n, m, /):
...         if m == 0:
...             return True, n
...         m = yield dec(m)
...         n = yield inc(n)
...         return False, add(n, m)
...     def inc(n, /):
...         return True, n+1
...         yield
...     def dec(n, /):
...         return True, n-1
...         yield
...     return mul
>>> mul = __()
>>> mul(100, 233)
23300

>>> class main_entry1(metaclass=HelperPseudoMeta8Recur5Yield, tail_recur_gi_protocol_vs_may_echo_vs_turnoff=True):
...     def main_entry1(x, /):
...         return (yield 'main_', x)
...     def main_(x, /):
...         return [x];yield
>>> main_entry1([999])
[[999]]

>>> class main_entry2(metaclass=HelperPseudoMeta8Recur5Yield, may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case=None):
...     def main_entry2(x, /):
...         return (False, ('main_', x))
...         yield
...         #bug:return (False, (yield 'main_', x))
...     def main_(x, /):
...         return (True, (x,));yield
>>> main_entry2([999])
([999],)

>>> class main_entry3(metaclass=HelperPseudoMeta8Recur5Yield, emplace_stack_ops_vs_may_ops4list_vs_ops4huge=True, may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case=child_gi_protocol6getitemable__0func, tail_recur_gi_protocol_vs_may_echo_vs_turnoff=True):
...     def main_entry3(n, /):
...         num_steps = 0
...         num_steps = yield 'main_', num_steps, n
...         return num_steps
...     def main_(num_steps, n, /):
...         if n > 1:
...             nm = 'on_odd' if n%2 else 'on_even'
...             num_steps = yield nm, num_steps, n
...         return num_steps
...     def on_odd(num_steps, n, /):
...         n = 3*n+1
...         num_steps += 1
...         num_steps = yield 'main_', num_steps, n
...         return num_steps
...     def on_even(num_steps, n, /):
...         n >>= 1
...         num_steps += 1
...         num_steps = yield 'main_', num_steps, n
...         return num_steps

>>> main_entry3(1)
0
>>> main_entry3(7) # 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
16
>>> main_entry3(8) # 8 -> 4 -> 2 -> 1
3
>>> for i in range(1, 100): (i, main_entry3(i))
(1, 0)
(2, 1)
(3, 7)
(4, 2)
(5, 5)
(6, 8)
(7, 16)
(8, 3)
(9, 19)
(10, 6)
(11, 14)
(12, 9)
(13, 9)
(14, 17)
(15, 17)
(16, 4)
(17, 12)
(18, 20)
(19, 20)
(20, 7)
(21, 7)
(22, 15)
(23, 15)
(24, 10)
(25, 23)
(26, 10)
(27, 111)
(28, 18)
(29, 18)
(30, 18)
(31, 106)
(32, 5)
(33, 26)
(34, 13)
(35, 13)
(36, 21)
(37, 21)
(38, 21)
(39, 34)
(40, 8)
(41, 109)
(42, 8)
(43, 29)
(44, 16)
(45, 16)
(46, 16)
(47, 104)
(48, 11)
(49, 24)
(50, 24)
(51, 24)
(52, 11)
(53, 11)
(54, 112)
(55, 112)
(56, 19)
(57, 32)
(58, 19)
(59, 32)
(60, 19)
(61, 19)
(62, 107)
(63, 107)
(64, 6)
(65, 27)
(66, 27)
(67, 27)
(68, 14)
(69, 14)
(70, 14)
(71, 102)
(72, 22)
(73, 115)
(74, 22)
(75, 14)
(76, 22)
(77, 22)
(78, 35)
(79, 35)
(80, 9)
(81, 22)
(82, 110)
(83, 110)
(84, 9)
(85, 9)
(86, 30)
(87, 30)
(88, 17)
(89, 30)
(90, 17)
(91, 92)
(92, 17)
(93, 17)
(94, 105)
(95, 105)
(96, 12)
(97, 118)
(98, 25)
(99, 25)



>>> sys.setrecursionlimit(saved_recursion_limit)



]]]
==========
==========
[[[
new:feature__halfway_result

>>> from seed.types.Either import Either
>>> from seed.func_tools.recur5yield__halfway import BoxedHalfwayResult, mk_gi4either8xresult, bind_gi_with_the_following_first_value4send
>>> from seed.func_tools.recur5yield__halfway import recur5yield__list__echo__echo

>>> def __():
...     @recur5yield__list__echo__echo
...     def main():
...         ls = [*map(as_if_echo, range(990, 995))]
...         gi = mk_gi4either8xresult(as_if_iter(ls))
...         gi = bind_gi_with_the_following_first_value4send(gi)
...         assert gi is bind_gi_with_the_following_first_value4send(gi)
...         while 1:
...             #either_rhr_or_rfr = yield gi
...             either_rhr_gi_or_rfr = yield gi
...             if either_rhr_gi_or_rfr.is_right:break
...             (rhr, _gi) = either_rhr_gi_or_rfr.left
...             print('raw_halfway_result:', rhr)
...             if not _gi is gi:
...                 _gi = mk_gi4xresult_xexception__as_(gi, _gi)
...                 gi = bind_gi_with_the_following_first_value4send(_gi)
...             gi.the_following_first_value4send = rhr
...         return True, either_rhr_gi_or_rfr.right
...         yield
...     def as_if_echo(x, /):
...         return True, x
...         yield
...     def as_if_iter(it, /):
...         sz = 0
...         input_value = None
...         for sz, gi in enumerate(it, 1):
...             x = yield gi
...             input_value = yield BoxedHalfwayResult((input_value, x))
...         return True, sz
...     return main
>>> sz = __()()
raw_halfway_result: (None, 990)
raw_halfway_result: ((None, 990), 991)
raw_halfway_result: (((None, 990), 991), 992)
raw_halfway_result: ((((None, 990), 991), 992), 993)
raw_halfway_result: (((((None, 990), 991), 992), 993), 994)

>>> sz
5


]]]
==========
==========
[[[
new:feature__halfway_exception

>>> from seed.func_tools.recur5yield__halfway import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception, detach_asif_new_gi_wrapper
>>> from seed.func_tools.recur5yield__halfway import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, Escaped, BoxedTailRecur, BoxedFinalResult
>>> from seed.func_tools.recur5yield__halfway import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway

>>> from seed.func_tools.recur5yield__halfway import recur5yield__list__echo__echo
>>> from seed.types.Either import Either

>>> def __():
...     @recur5yield__list__echo__echo
...     def main():
...         ls = [*map(as_if_echo, range(990, 995))]
...         gi = mk_gi4either8xresult(as_if_iter(ls))
...         gi = bind_gi_with_the_following_first_value4send(gi)
...         assert gi is bind_gi_with_the_following_first_value4send(gi)
...         while 1:
...             try:
...                 either_rhr_gi_or_rfr = yield gi
...             except EFinal as e:
...                 [sz] = e.args
...                 print('final_exception_arg:', sz)
...                 return BoxedFinalResult(777)
...                 #return True, 777
...             except HalfwayExceptionAndTailGI as e:
...                 (rhe, _gi) = e
...                 e_vs_r = False
...             else:
...                 e_vs_r = True
...             try:
...                 if not e_vs_r:
...                     raise rhe
...             except EHalfway as e:
...                 halfway_exception_args = e.args
...                 print('halfway_exception_args:', halfway_exception_args)
...                 if not _gi is gi:
...                     _gi = mk_gi4xresult_xexception__as_(gi, _gi)
...                     gi = bind_gi_with_the_following_first_value4send(_gi)
...                 gi.the_following_first_value4send = halfway_exception_args
...                 continue
...             if either_rhr_gi_or_rfr.is_right:break
...             (rhr, _gi) = either_rhr_gi_or_rfr.left
...             print('raw_halfway_result:', rhr)
...             if not _gi is gi:
...                 _gi = mk_gi4xresult_xexception__as_(gi, _gi)
...                 gi = bind_gi_with_the_following_first_value4send(_gi)
...             gi.the_following_first_value4send = rhr
...         raise 000
...         return True, either_rhr_gi_or_rfr.right
...         yield
...     def as_if_echo(x, /):
...         #return True, x
...         return BoxedTailRecur(_as_if_echo(x))
...         yield
...     def _as_if_echo(x, /):
...         return [BoxedFinalResult(x), (True, x), Either.from_right(x)][x%3]
...         yield
...     def as_if_iter(it, /):
...         sz = 0
...         input_value = None
...         for sz, gi in enumerate(it, 1):
...             x = yield gi
...             input_value = yield BoxedHalfwayResult((input_value, x))
...             #input_value = yield BoxedException__halfway(EHalfway(input_value, x))
...             input_value = yield mk_boxed_EHalfway(input_value, x)
...         raise mk_boxed_EFinal(sz)
...         #raise BoxedException__final(EFinal(sz))
...         #return True, sz
...     return main
>>> k = __()()
raw_halfway_result: (None, 990)
halfway_exception_args: ((None, 990), 990)
raw_halfway_result: (((None, 990), 990), 991)
halfway_exception_args: ((((None, 990), 990), 991), 991)
raw_halfway_result: (((((None, 990), 990), 991), 991), 992)
halfway_exception_args: ((((((None, 990), 990), 991), 991), 992), 992)
raw_halfway_result: (((((((None, 990), 990), 991), 991), 992), 992), 993)
halfway_exception_args: ((((((((None, 990), 990), 991), 991), 992), 992), 993), 993)
raw_halfway_result: (((((((((None, 990), 990), 991), 991), 992), 992), 993), 993), 994)
halfway_exception_args: ((((((((((None, 990), 990), 991), 991), 992), 992), 993), 993), 994), 994)
final_exception_arg: 5

>>> k
777


]]]
==========
==========
[[[
new:feature__customizable__boxed_final_exception
++child_gi_exc_protocol/child_gi_exc_protocol_vs_may_echo_vs_turnoff

grep -F 'seed.func_tools.recur5yield__halfway' -r ../../python3_src/seed/ -l | more

>>> from seed.func_tools.recur5yield__halfway import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
>>> def __xxx(eee, /):
...     from seed.func_tools.recur5yield__halfway import BoxedFinalResult, EHalfway
...         #[:hold_ExcTypes_to_fix_main_generator_finialization_failure]:here
...     @recur5yield__list__echo__echo
...     def main():
...         gi = f()
...         while 1:
...             try:
...                 yield gi
...             except GeneratorExit:
...                 #[:skip_GeneratorExit_to_fix_main_generator_finialization_print_GeneratorExit]:here
...                 raise#<--main().close()
...             except HalfwayExceptionAndTailGI as e:
...                 (rhe, _gi) = e
...             except BaseException as e:
...                 print(repr(e))
...                 return BoxedFinalResult(444)
...             else:
...                 raise 000
...             try:
...                 raise rhe
...             except EHalfway as e:
...                 print(repr(e))
...                 continue
...         raise 000
...     def f():
...         yield mk_boxed_EHalfway(eee)
...         raise eee
...     return main
>>> __ = __xxx
>>> __(BoxedException__final(ValueError(999)))()
EHalfway(BoxedException__final(ValueError(999)))
ValueError(999)
444
>>> __(ValueError(999))()
Traceback (most recent call last):
    ...
ValueError: 999
>>> __(BoxedException__through(BoxedException__final(ValueError(999))))()
Traceback (most recent call last):
    ...
seed.func_tools.recur5yield__halfway.BoxedException__final: BoxedException__final(ValueError(999))
>>> __(BoxedException__through(BoxedException__through(ValueError(999))))()
Traceback (most recent call last):
    ...
seed.func_tools.recur5yield__halfway.BoxedException__through: BoxedException__through(ValueError(999))
>>> __(BoxedException__through(BoxedException(ValueError(999))))()
Traceback (most recent call last):
    ...
seed.func_tools.recur5yield__halfway.BoxedException: BoxedException(ValueError(999))
>>> __(BoxedException(ValueError(999)))()
Traceback (most recent call last):
    ...
seed.func_tools.recur5yield__halfway.BoxedException: BoxedException(ValueError(999))
>>> __(BoxedException__halfway(ValueError(999)))()
Traceback (most recent call last):
    ...
seed.func_tools.recur5yield__halfway.BoxedException__halfway: BoxedException__halfway(ValueError(999))
>>> __(Escaped(ValueError(999)))()
Traceback (most recent call last):
    ...
TypeError: <class 'ValueError'>
>>> __(Escaped(BoxedException(ValueError(999))))()
Traceback (most recent call last):
    ...
seed.func_tools.recur5yield__halfway.Escaped: Escaped(BoxedException(ValueError(999)))



######################
why?: generator.__del__():finialize fail??
    [:hold_ExcTypes_to_fix_main_generator_finialization_failure]:goto
    [:skip_GeneratorExit_to_fix_main_generator_finialization_print_GeneratorExit]:goto
    <<==:
$ py -m nn_ns.app.doctest_cmd seed.func_tools.recur5yield__halfway:__doc__ -ht
Exception ignored in: <generator object __xxx.<locals>.main at 0x7465fd45e0>
Traceback (most recent call last):
  File "<doctest seed.func_tools.recur5yield__halfway:__doc__[43]>", line 8, in main
NameError: name 'EHalfway' is not defined
---
NameError: name 'BoxedFinalResult' is not defined
---
GeneratorExit()
######################
]]]
==========
==========
[[[
######################
fixed_bug____BoxedTailRecur__X__BoxedHalfwayResult:here

>>> from seed.lang.generator_iterator_ops import is_gi_closed, is_gi_beginning, is_gi_running, is_gi_waiting
>>> _666 = object()
>>> _999 = object()
>>> def _test__69():
...     yield BoxedHalfwayResult(_666)
...     return BoxedFinalResult(_999)
...     777;    yield
>>> def _test__tail_recur():
...     gi = _test__69()
...     #print_err('69_gi:', hex(id(gi)))
...     return BoxedTailRecur(gi)
...     777;    yield
>>> def _mk_gi4skip(gi, /):
...     #print_err('tail_recur_gi:', hex(id(gi)))
...     gi_ = gi
...     gi = mk_gi4either8xresult(gi)
...     #print_err('xresult_gi:', hex(id(gi)))
...     while 1:
...         assert not is_gi_closed(gi)
...         x = yield gi
...         if x.is_right:
...             break
...         _, gi = x.left#HalfwayResultAndTailGI
...     return BoxedFinalResult(x.right)
>>> @recur5yield__list__echo__echo
... def _test__skip():
...     gi = _test__tail_recur()
...     #gi = mk_gi4skip_header_signal(gi)
...     #print_err('tail_recur_gi:', hex(id(gi)))
...     gi = _mk_gi4skip(gi)
...     #print_err('main_gi:', hex(id(gi)))
...     return gi
>>> _test__skip() is _999
True


######################
]]]
==========
==========
[[[
###rename history:Generator --> GeneratorIterator --> IGeneratorIterator

class collections.abc.Generator


generator

    A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.

    Usually refers to a generator function, but may refer to a generator iterator in some contexts. In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.

generator iterator

    An object created by a generator function.

    Each yield temporarily suspends processing, remembering the location execution state (including local variables and pending try-statements). When the generator iterator resumes, it picks up where it left off (in contrast to functions which start fresh on every invocation).


file:///storage/72A2-151D/000edt/0my_files/unzip/py_doc/python-3.8.1-docs-html/reference/expressions.html#generator.send

When the underlying iterator is complete, the value attribute of the raised StopIteration instance becomes the value of the yield expression. It can be either set explicitly when raising StopIteration, or automatically when the subiterator is a generator (by returning a value from the subgenerator).

    Changed in version 3.3: Added yield from <expr> to delegate control flow to a subiterator.

6.2.9.1. Generator-iterator methods

This subsection describes the methods of a generator iterator. They can be used to control the execution of a generator function.

Note that calling any of the generator methods below when the generator is already executing raises a ValueError exception.

generator.__next__()

    Starts the execution of a generator function or resumes it at the last executed yield expression. When a generator function is resumed with a __next__() method, the current yield expression always evaluates to None. The execution then continues to the next yield expression, where the generator is suspended again, and the value of the expression_list is returned to __next__()’s caller. If the generator exits without yielding another value, a StopIteration exception is raised.

    This method is normally called implicitly, e.g. by a for loop, or by the built-in next() function.

generator.send(value)

    Resumes the execution and “sends” a value into the generator function. The value argument becomes the result of the current yield expression. The send() method returns the next value yielded by the generator, or raises StopIteration if the generator exits without yielding another value. When send() is called to start the generator, it must be called with None as the argument, because there is no yield expression that could receive the value.

generator.throw(type[, value[, traceback]])

    Raises an exception of type type at the point where the generator was paused, and returns the next value yielded by the generator function. If the generator exits without yielding another value, a StopIteration exception is raised. If the generator function does not catch the passed-in exception, or raises a different exception, then that exception propagates to the caller.

generator.close()

    Raises a GeneratorExit at the point where the generator function was paused. If the generator function then exits gracefully, is already closed, or raises GeneratorExit (by not catching the exception), close returns to its caller. If the generator yields a value, a RuntimeError is raised. If the generator raises any other exception, it is propagated to the caller. close() does nothing if the generator has already exited due to an exception or normal exit.

]]]
==========
==========
[[[
]]]
==========

#]]]]]'''

#################################
#HHHHH
__all__ = '''
recur5yield__list__echo__echo
    mk_gi4xresult_xexception__as_
    mk_gi4xresult_xexception
    detach_asif_new_gi_wrapper
    BoxedHalfwayResult
        bind_gi_with_the_following_first_value4send
        mk_gi4either8xresult
    EFlowControl
        EFinal
        EHalfway
            mk_boxed_EFinal
            mk_boxed_EHalfway
                BoxedException__halfway
                BoxedException__final












recur5yield__decoratorT__all_gi_protocols
    explain__child_gi_protocol_vs_may_0ref4func_vs_echo
    explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff
    explain__child_gi_exc_protocol_vs_may_echo_vs_turnoff
    explain__emplace_stack_ops_vs_may_ops4list_vs_ops4huge
    explain__may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case
    child_gi_protocol__echo
    child_gi_protocol__0func
    child_gi_protocolT__0func5ref
    tail_recur_gi_protocol__echo
    tail_recur_gi_protocol__off
    child_gi_exc_protocol__echo
    child_gi_exc_protocol__off
        recur5yield__list__echo__echo
        recur5yield__list__echo__off
        recur5yield__list__0func__echo
        recur5yield__list__0func__off
        recur5yield__huge__echo__echo
        recur5yield__huge__echo__off
        recur5yield__huge__0func__echo
        recur5yield__huge__0func__off
recur5yield__eval__main_generator_iterator


explain__may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case
    child_gi_protocol6getitemable__0case
    child_gi_protocol6getitemable__0func
    child_gi_protocol6getitemableT__0func5ref

HelperPseudoMeta8Recur5Yield
    RecurGroupCollector4Recur5Yield
















is_generator_iterator
mk_gi4return
GeneratorIterator__wrapper
    GeneratorIterator__wrapper__extras_kwds4xexception_xresult
    GeneratorIterator__either8xresult
        mk_gi4either8xresult
    GeneratorIterator__bind_the_following_first_value4send
        bind_gi_with_the_following_first_value4send
    GeneratorIterator__forbid_halfway_result
    GeneratorIterator__forbid_halfway_exception
    GeneratorIterator__boxed8xexception
        mk_gi4xresult_xexception
        detach_asif_new_gi_wrapper



BoxedXxx
    BoxedHalfwayResult
    BoxedTailRecur
    BoxedFinalResult
    BoxedException
        BoxedException__halfway
        BoxedException__final
        BoxedException__through
        Escaped
is_boxed_xxx
    is_boxed_halfway_result
    is_boxed_exception
        is_boxed_halfway_exception
        is_boxed_final_exception

EFlowControl
    EFinal
    EHalfway
        mk_boxed_EFinal
        mk_boxed_EHalfway



mk_xexception
mk_xresult
    is_ok_return5child_gi_protocol
    check_ok_return5child_gi_protocol
std_ok_return5tail_recur_gi_protocol
    check_ok_return5tail_recur_gi_protocol
    is_ok_return5tail_recur_gi_protocol




HalfwayResultAndTailGI
HalfwayExceptionAndTailGI
    '''.split()#'''
    #internal_use_only:_Signal4halfway_result
    #internal_use_only:_Signal4halfway_exception
r'''
xxxxxxx
    recur5yield__echo__echo
    recur5yield__echo__off
    recur5yield__0func__echo
    recur5yield__0func__off
'''#'''
__all__

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)

timer = timer__print_err__thread_wide
_to_show_ = __name__ == "__main__"

with timer(prefix='py:std...', _to_show_=_to_show_):
    from functools import wraps
    from collections.abc import Generator as IGeneratorIterator #, Callable

with timer(prefix='seed:basic...', _to_show_=_to_show_):
    from seed.tiny_.check import check_getitemable, check_callable, check_type_is, check_type_le, check_pair, check_tmay, check_int_ge #no check_tuple
    from seed.tiny_.dict__add_fmap_filter import dict_add__is
    from seed.tiny import curry1, echo, null_tuple, mk_tuple, null_iter
    from seed.tiny import print_err, repr_as_3dot

with timer(prefix='seed.types.ops.IEmplaceStackOps', _to_show_=_to_show_):
    from seed.types.ops.IEmplaceStackOps import IEmplaceStackOps
    from seed.types.ops.IEmplaceStackOps import the_emplace_stack_ops4list, the_emplace_stack_ops4HugeStack

from seed.types.Either import Either
from types import GeneratorType
from seed.helper.repr_input import repr_helper

___end_mark_of_excluded_global_names__0___ = ...

r'''[[[
py -m seed.func_tools.recur5yield__halfway
py:std...:duration: 0.0001646160000000063 *(unit: 0:00:01)
seed:basic...:duration: 0.00011753899999999984 *(unit: 0:00:01)
seed.types.ops.IEmplaceStackOps:duration: 0.01057238299999999 *(unit: 0:00:01)

seed.types.ops.IEmplaceStackOps
e ../../python3_src/seed/types/ops/IEmplaceStackOps.py

py -m seed.types.ops.IEmplaceStackOps
seed:basic...:duration: 0.00015761600000002707 *(unit: 0:00:01)
seed.abc.abc__ver1:duration: 0.004998077999999989 *(unit: 0:00:01)
seed.abc.IHashable:duration: 0.001823384999999983 *(unit: 0:00:01)
seed.types.ops.IEmplaceStackOps:duration: 0.003220001 *(unit: 0:00:01)


#]]]'''#'''







def _t():
    #generator_iterator 并没有保留 返回值
    #   返回值 在 StopIteration.value!!
    def try_to_find_return_value_of_generator_iterator():
        return 233;yield
    it = try_to_find_return_value_of_generator_iterator()
    if 0:
        [*it]
        print(dir(it))
        #print(vars(it))
            #TypeError: vars() argument must have __dict__ attribute
        #help(it)
        print(it.gi_code)
        print(it.gi_frame)
        print(it.gi_running)
        print(it.gi_yieldfrom)
    if 1:
        try:
            it.send(None)
        except StopIteration as e:
            #StopIteration(233)
            #print(repr(e))
            #print(type(e), e.value)
            exc = e
            pass
        except BaseException as e:
            print(repr(e))
            raise
        #assert type(e) is StopIteration
            #UnboundLocalError: local variable 'e' referenced before assignment
        assert type(exc) is StopIteration
        assert (exc.value) == 233
_t()



r'''
def recur5yield__recur_group(name2recur_func, main_name, /):
    f = name2recur_func[main_name]
    return recur5yield__may_recur_group(name2recur_func, f)

def recur5yield__may_recur_group(may_name2recur_func, main_generator_func, /):
    ...
#'''

#old:recur5yield__decoratorT__child_gi_protocol
#API_changed:def recur5yield__decoratorT__all_gi_protocols(emplace_stack_ops, child_gi_protocol, tail_recur_gi_protocol, /):
def recur5yield__decoratorT__all_gi_protocols(emplace_stack_ops, child_gi_protocol, tail_recur_gi_protocol, child_gi_exc_protocol, /):
    r'''
    (emplace_stack_ops, child_gi_protocol, tail_recur_gi_protocol) -> decorator

    decorator :: main_generator_func -> expected_main_recur_func
    expected_main_recur_func :: (*args4main, **kwds4main) -> main_result
    main_result = result5recur<main_generator_iterator>

    main_generator_func(*args4main, **kwds4main) -> main_generator_iterator
    main_generator_iterator :: IGeneratorIterator<yield-exprlist5yield, return-return_value5child>

    emplace_stack_ops :: IEmplaceStackOps
    ###child_gi_protocol(exprlist5yield) -> generator_iterator
    ###child_gi_protocol(exprlist5yield) -> gi_or_bhr/(generator_iterator|boxed_halfway_result)
    child_gi_protocol(exprlist5yield) -> gi_or_bhr_or_bhe/(generator_iterator|boxed_halfway_result|boxed_ halfway_exception)
    tail_recur_gi_protocol(return_value5child) -> either_tailrecur_result
    either_tailrecur_result === (is_result5recur, payload) :: ((False, exprlist5yield)|(True, result5recur))

    child_gi_exc_protocol :: (() -> (v|^i4e)) -> (() -> (v|^BoxedException__final))

    '''#'''
    check_type_le(IEmplaceStackOps, emplace_stack_ops)
    check_callable(child_gi_protocol)
        # old:child_gi_protocol(exprlist5yield) -> generator_iterator
        # old:child_gi_protocol(exprlist5yield) -> gi_or_bhr/(generator_iterator|boxed_halfway_result)
        # child_gi_protocol(exprlist5yield) -> gi_or_bhr_or_bhe/(generator_iterator|boxed_halfway_result|boxed_ halfway_exception)
    check_callable(tail_recur_gi_protocol)
        # tail_recur_gi_protocol(return_value5child) -> either_tailrecur_result/(is_result5recur, payload)/((False, exprlist5yield)|(True, result5recur))
    check_callable(child_gi_exc_protocol)

    def recur5yield__decorator__main_generator_func(main_generator_func, /):
        check_callable(main_generator_func)
            # main_generator_func(*args4main, **kwds4main) -> generator_iterator
            # generator_func(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
            # generator?(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
            #   generator =?= generator_func | ?generator_iterator?

        @wraps(main_generator_func)
        def wrapper(*args4main, **kwds4main):
            main_generator_iterator = main_generator_func(*args4main, **kwds4main)
            main_result = recur5yield__eval__main_generator_iterator(emplace_stack_ops, main_generator_iterator, child_gi_protocol, tail_recur_gi_protocol, child_gi_exc_protocol)
            return main_result
        return wrapper
    return recur5yield__decorator__main_generator_func

def explain__child_gi_protocol_vs_may_0ref4func_vs_echo(child_gi_protocol_vs_may_0ref4func_vs_echo, may_deref4func, /):
    r'''
    -> child_gi_protocol

    child_gi_protocol_vs_may_0ref4func_vs_echo :: (callable | None | bool)
        callable ==>> child_gi_protocol
        True ==>> child_gi_protocol__echo
        default:None/False ==>>:
            may_deref4func :: None | deref4func/callable/(ref4func -> generator_func)
                None ==>> child_gi_protocol__0func
                callable ==>> child_gi_protocol__0ref4func===child_gi_protocolT__0func5ref<deref4func>

    '''#'''
    if callable(child_gi_protocol_vs_may_0ref4func_vs_echo):
        child_gi_protocol = child_gi_protocol_vs_may_0ref4func_vs_echo
    elif child_gi_protocol_vs_may_0ref4func_vs_echo is True:
        _echo = True
        child_gi_protocol = child_gi_protocol__echo
    else:
        may_0ref4func = child_gi_protocol_vs_may_0ref4func_vs_echo
        if not (may_0ref4func is None or may_0ref4func is False):raise TypeError
        if may_deref4func is None:
            child_gi_protocol = child_gi_protocol__0func
        else:
            deref4func = may_deref4func
            check_callable(deref4func)
            child_gi_protocol__0ref4func = child_gi_protocolT__0func5ref(deref4func)
            child_gi_protocol = child_gi_protocol__0ref4func
    return child_gi_protocol
explain__child_gi_protocol_vs_may_0ref4func_vs_echo

def explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff(tail_recur_gi_protocol_vs_may_echo_vs_turnoff, /):
    r'''
    -> tail_recur_gi_protocol

    tail_recur_gi_protocol_vs_may_echo_vs_turnoff :: (callable | None | bool)
        callable ==>> tail_recur_gi_protocol
        True ==>> tail_recur_gi_protocol__off
        default:None/False ==>> tail_recur_gi_protocol__echo

    '''#'''
    if callable(tail_recur_gi_protocol_vs_may_echo_vs_turnoff):
        tail_recur_gi_protocol = tail_recur_gi_protocol_vs_may_echo_vs_turnoff
    elif tail_recur_gi_protocol_vs_may_echo_vs_turnoff is True:
        turnoff = True
        tail_recur_gi_protocol = tail_recur_gi_protocol__off
    else:
        may_echo = tail_recur_gi_protocol_vs_may_echo_vs_turnoff
        if not (may_echo is None or may_echo is False):raise TypeError
        tail_recur_gi_protocol = tail_recur_gi_protocol__echo
    return tail_recur_gi_protocol
explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff
def explain__child_gi_exc_protocol_vs_may_echo_vs_turnoff(child_gi_exc_protocol_vs_may_echo_vs_turnoff, /):
    r'''
    -> child_gi_exc_protocol

    child_gi_exc_protocol_vs_may_echo_vs_turnoff :: (callable | None | bool)
        callable ==>> child_gi_exc_protocol
        True ==>> child_gi_exc_protocol__off
        default:None/False ==>> child_gi_exc_protocol__echo

    '''#'''
    if callable(child_gi_exc_protocol_vs_may_echo_vs_turnoff):
        child_gi_exc_protocol = child_gi_exc_protocol_vs_may_echo_vs_turnoff
    elif child_gi_exc_protocol_vs_may_echo_vs_turnoff is True:
        turnoff = True
        child_gi_exc_protocol = child_gi_exc_protocol__off
    else:
        may_echo = child_gi_exc_protocol_vs_may_echo_vs_turnoff
        if not (may_echo is None or may_echo is False):raise TypeError
        child_gi_exc_protocol = child_gi_exc_protocol__echo
    return child_gi_exc_protocol
explain__child_gi_exc_protocol_vs_may_echo_vs_turnoff

def explain__emplace_stack_ops_vs_may_ops4list_vs_ops4huge(emplace_stack_ops_vs_may_ops4list_vs_ops4huge, /):
    r'''
    -> IEmplaceStackOps

    emplace_stack_ops_vs_may_ops4list_vs_ops4huge :: (IEmplaceStackOps | None | bool)
        IEmplaceStackOps ==>> emplace_stack_ops
        True ==>> the_emplace_stack_ops4HugeStack
        default:None/False ==>> the_emplace_stack_ops4list

    '''#'''
    if isinstance(emplace_stack_ops_vs_may_ops4list_vs_ops4huge, IEmplaceStackOps):
        emplace_stack_ops = emplace_stack_ops_vs_may_ops4list_vs_ops4huge
    else:
        may_ops4list_vs_ops4huge = emplace_stack_ops_vs_may_ops4list_vs_ops4huge
        if may_ops4list_vs_ops4huge is True:
            ops4huge = may_ops4list_vs_ops4huge
            emplace_stack_ops = the_emplace_stack_ops4HugeStack
        else:
            may_ops4list = may_ops4list_vs_ops4huge
            if not (may_ops4list is None or may_ops4list is False):raise TypeError
            emplace_stack_ops = the_emplace_stack_ops4list
    return emplace_stack_ops
explain__emplace_stack_ops_vs_may_ops4list_vs_ops4huge




#tail_recur_gi_protocol
def std_ok_return5tail_recur_gi_protocol(either_tailrecur_result, /):
    check_ok_return5tail_recur_gi_protocol(either_tailrecur_result)
    return mk_tuple(either_tailrecur_result)
def check_ok_return5tail_recur_gi_protocol(x, /):
    if is_ok_return5tail_recur_gi_protocol(x):
        return
    check_pair(x)
    (is_result5recur, payload) = x
    check_type_is(bool, is_result5recur)
    raise 000
def is_ok_return5tail_recur_gi_protocol(x, /):
    typ = type(x)
    if typ is tuple:
        return len(x) == 2 and type(x[0]) is bool
    return typ in _types4return5tail_recur_gi_protocol

#child_gi_protocol
def check_ok_return5child_gi_protocol(x, /):
    'gi_or_bhr_or_bhe'
    if not is_ok_return5child_gi_protocol(x): raise TypeError(type(x))
def is_ok_return5child_gi_protocol(x, /):
    'gi_or_bhr_or_bhe'
    return isinstance(x, IGeneratorIterator) or is_boxed_halfway_result(x) or is_boxed_halfway_exception(x)
    return isinstance(x, IGeneratorIterator) or is_boxed_halfway_result(x)
#child_gi_protocol
def child_gi_protocol__echo(exprlist5yield, /):
    ######################
    #new:feature__halfway_exception
    'exprlist5yield/gi_or_bhr_or_bhe -> gi_or_bhr_or_bhe/(generator_iterator|boxed_halfway_result|boxed_ halfway_exception)' # | ^boxed_final_exception
    gi_or_bhr_or_bhe = echo(exprlist5yield)
    check_ok_return5child_gi_protocol(gi_or_bhr_or_bhe)
    return gi_or_bhr_or_bhe
    ######################
    #new:feature__halfway_result
    'exprlist5yield/gi_or_bhr -> gi_or_bhr/(generator_iterator|boxed_halfway_result)'
    gi_or_bhr = echo(exprlist5yield)
    if not is_ok_return5child_gi_protocol(gi_or_bhr): raise TypeError(type(gi_or_bhr))
    return gi_or_bhr
    ######################
    #old:
    generator_iterator = exprlist5yield
    check_type_le(IGeneratorIterator, generator_iterator)
    return generator_iterator
def child_gi_protocol__0func(exprlist5yield, /):
    'exprlist5yield/(generator_func, *args4gi_mkr) -> generator_iterator'
    check_type_is(tuple, exprlist5yield)
    [generator_func, *args4gi_mkr] = exprlist5yield
    return generator_func(*args4gi_mkr)
def child_gi_protocolT__0func5ref(deref4func, /):
    r'''
    deref4func -> child_gi_protocol__0ref4func

    deref4func(ref4func) -> generator_func
    child_gi_protocol__0ref4func :: exprlist5yield/(ref4func, *args4gi_mkr) -> generator_iterator

    '''#'''
    check_callable(deref4func)
    def child_gi_protocol__0ref4func(exprlist5yield, /):
        'exprlist5yield/(ref4func, *args4gi_mkr) -> generator_iterator'
        check_type_is(tuple, exprlist5yield)
        [ref4func, *args4gi_mkr] = exprlist5yield
        generator_func = deref4func(ref4func)
        return generator_func(*args4gi_mkr)
    return child_gi_protocol__0ref4func

#tail_recur_gi_protocol
def tail_recur_gi_protocol__echo(return_value5child, /):
    'return_value5child/either_tailrecur_result -> either_tailrecur_result/(is_result5recur, payload)/((False, exprlist5yield)|(True, result5recur))'
    either_tailrecur_result = return_value5child
    if 1:
        either_tailrecur_result = std_ok_return5tail_recur_gi_protocol(either_tailrecur_result)
    elif 0:
        check_ok_return5tail_recur_gi_protocol(either_tailrecur_result)
    else:
        check_pair(either_tailrecur_result)
        (is_result5recur, payload) = either_tailrecur_result
        check_type_is(bool, is_result5recur)
    return either_tailrecur_result
def tail_recur_gi_protocol__off(return_value5child, /):
    'return_value5child/result5recur -> either_tailrecur_result/(is_result5recur, payload)/(True, result5recur)'
    result5recur = return_value5child
    return (True, result5recur)

#child_gi_exc_protocol
def child_gi_exc_protocol__echo(lazy, /):
    'child_gi_exc_protocol :: (() -> (v|^i4e)) -> (() -> (v|^BoxedException__final))'
    return lazy
def child_gi_exc_protocol__off(lazy, /):
    'child_gi_exc_protocol :: (() -> (v|^i4e)) -> (() -> (v|^BoxedException__final))'
    def _lazy():
        try:
            return lazy()
        except BoxedException as e:
            raise BoxedException__through(e)
    return _lazy

recur5yield__list__echo__echo = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4list, child_gi_protocol__echo, tail_recur_gi_protocol__echo, child_gi_exc_protocol__echo)
recur5yield__list__echo__off = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4list, child_gi_protocol__echo, tail_recur_gi_protocol__off, child_gi_exc_protocol__echo)
recur5yield__list__0func__echo = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4list, child_gi_protocol__0func, tail_recur_gi_protocol__echo, child_gi_exc_protocol__echo)
recur5yield__list__0func__off = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4list, child_gi_protocol__0func, tail_recur_gi_protocol__off, child_gi_exc_protocol__echo)

recur5yield__huge__echo__echo = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4HugeStack, child_gi_protocol__echo, tail_recur_gi_protocol__echo, child_gi_exc_protocol__echo)
recur5yield__huge__echo__off = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4HugeStack, child_gi_protocol__echo, tail_recur_gi_protocol__off, child_gi_exc_protocol__echo)
recur5yield__huge__0func__echo = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4HugeStack, child_gi_protocol__0func, tail_recur_gi_protocol__echo, child_gi_exc_protocol__echo)
recur5yield__huge__0func__off = recur5yield__decoratorT__all_gi_protocols(the_emplace_stack_ops4HugeStack, child_gi_protocol__0func, tail_recur_gi_protocol__off, child_gi_exc_protocol__echo)



def _no_op():pass
class GeneratorIterator__wrapper(IGeneratorIterator):
    #___666_close_wrapped_gi_999___ = True
    def __del__(sf, /):
        'see:detach_asif_new_gi_wrapper'
        sf.close()
    @property
    def close(sf, /):
        if sf.___666_close_wrapped_gi_999___:
            return sf._gi.close
        return _no_op

    #@class_property
    #_allow_extras_kwds_ = False
    _extras_kwds7allowed_ = frozenset()

    def __init__(sf, generator_iterator, /, *, ___666_close_wrapped_gi_999___, **kwds):
        #if kwds and not type(sf)._allow_extras_kwds_:raise TypeError(','.join(sorted(kwds)))
        if not kwds.keys() <= type(sf)._extras_kwds7allowed_:raise TypeError(','.join(sorted(kwds.keys()-type(sf)._extras_kwds7allowed_)))
        check_type_is(bool, ___666_close_wrapped_gi_999___)
        assert ___666_close_wrapped_gi_999___ is False, '[___666_close_wrapped_gi_999___:=True] is useless'
        check_type_le(IGeneratorIterator, generator_iterator)
        assert '_gi' not in kwds
        sf.__dict__.update(kwds)
        sf.___666_close_wrapped_gi_999___ = ___666_close_wrapped_gi_999___
        sf.___666_close_wrapped_gi_999___
        sf._gi = generator_iterator
        sf._gi
    @property
    def the_wrapped_generator_iterator(sf, /):
        '-> generator_iterator'
        return sf._gi
    @property
    #@override
    def send(sf, /):
        #def send(sf, /, *args, **kwds):
        return sf._gi.send
    @property
    #@override
    def throw(sf, /):
        return sf._gi.throw
    def detach_wrapped_gi(sf, /):
        gi = sf._gi
        sf._gi = null_iter
        return gi
    def __getattr__(sf, nm, /):
        #'del sf --> sf.close() --> sf._gi.close() --> next(sf._gi)->^StopIteration(None)'
        if nm == '___666_close_wrapped_gi_999___':
            #__del__() twice
            return False
        return getattr(sf._gi, nm)

def detach_asif_new_gi_wrapper(old_gi, asif_new_gi, /):
    if not asif_new_gi is old_gi:
        gi = asif_new_gi.detach_wrapped_gi()
        if not gi is old_gi:raise 000
    return old_gi
#class GeneratorIterator__wrapper__allow_extras_kwds(GeneratorIterator__wrapper):
    #@class_property
    #@override
    #_allow_extras_kwds_ = True
class GeneratorIterator__wrapper__extras_kwds4xexception_xresult(GeneratorIterator__wrapper):
    #@class_property
    #@override
    _extras_kwds7allowed_ = frozenset('___666_mk_xresult_999___,___666_mk_xexception_999___,___666_close_wrapped_gi_999___'.split(','))
class GeneratorIterator__forbid_halfway_exception(GeneratorIterator__wrapper):
    'old_mk_xexception:[raise5yield == xexception == rfe/final_exception]'
    ___666_mk_xexception_999___ = False

class GeneratorIterator__boxed8xexception(GeneratorIterator__wrapper):
    'std_mk_xexception:[raise5yield == xexception == bhe_gi_or_bfe/(BoxedException__halfway(rhe,gi)/boxed_halfway_exception|boxed_final_exception)]'
    ___666_mk_xexception_999___ = True



class GeneratorIterator__forbid_halfway_result(GeneratorIterator__wrapper):
    'old_mk_xresult:[return5yield == xresult == rfr/raw_final_result]'
    ___666_mk_xresult_999___ = False

class GeneratorIterator__either8xresult(GeneratorIterator__wrapper):
    #class GeneratorIterator__std_mk_xresult(IGeneratorIterator):
    'std_mk_xresult:[return5yield == xresult == either_rhr_gi_or_rfr/Either(HalfwayResultAndTailGI(raw_halfway_result,gi),raw_final_result;)]'
    ___666_mk_xresult_999___ = True

#class GeneratorIterator__4xresult_xexception(GeneratorIterator__wrapper):
#    r'''[[[
#    [mk_xresult :: None | bool | ((rhr_gi_or_rfr,/,*,rhr_vs_rfr)->xresult)]
#    [mk_xexception :: None | bool | ((rhe_gi_or_rfe,/,*,rhe_vs_rfe)->xexception)]
#    #]]]'''#'''
#    def __init__(sf, /, *, mk_xresult=None, mk_xexception=None):
#        GeneratorIterator__wrapper.__init__(sf, generator_iterator, ___666_mk_xresult_999___=mk_xresult, ___666_mk_xexception_999___=mk_xexception)
#
def mk_gi4return(x, /):
    '-> GeneratorIterator<return-x>'
    return x
    777;    yield
def mk_gi4either8xresult(generator_iterator, /, *, ___666_close_wrapped_gi_999___=False):
    '-> GeneratorIterator__either8xresult # [return5yield == xresult == either_rhr_gi_or_rfr/Either(HalfwayResultAndTailGI(raw_halfway_result,gi),raw_final_result;)]'
    if getattr(generator_iterator, '___666_mk_xresult_999___', None) is True:
        return generator_iterator
    return GeneratorIterator__either8xresult(generator_iterator, ___666_close_wrapped_gi_999___=___666_close_wrapped_gi_999___)

def mk_gi4xresult_xexception__as_(original_gi, tail_gi, /, *, ___666_close_wrapped_gi_999___=False):
    check_type_le(IGeneratorIterator, original_gi)
    check_type_le(IGeneratorIterator, tail_gi)
    return mk_gi4xresult_xexception(tail_gi
    , mk_xresult=getattr(original_gi, '___666_mk_xresult_999___', None)
    , mk_xexception=getattr(original_gi, '___666_mk_xexception_999___', None)
    , ___666_close_wrapped_gi_999___=___666_close_wrapped_gi_999___
    )
_pure_gi_wrapper_types = (
(GeneratorIterator__wrapper
,GeneratorIterator__either8xresult
,GeneratorIterator__boxed8xexception
,GeneratorIterator__forbid_halfway_exception
,GeneratorIterator__forbid_halfway_result
))
def mk_gi4xresult_xexception(generator_iterator, /, *, mk_xresult=None, mk_xexception=None, ___666_close_wrapped_gi_999___=False):
    r'''[[[
    [mk_xresult :: None | bool | ((rhr_gi_or_rfr,/,*,rhr_vs_rfr)->xresult)]
    [mk_xexception :: None | bool | ((rhe_gi_or_rfe,/,*,rhe_vs_rfe)->xexception)]
    #]]]'''#'''
    if getattr(generator_iterator, '___666_mk_xresult_999___', None) is mk_xresult and getattr(generator_iterator, '___666_mk_xexception_999___', None) is mk_xexception:
        return generator_iterator
    #while isinstance(generator_iterator, GeneratorIterator__wrapper) and generator_iterator.___666_close_wrapped_gi_999___ is False:
    while type(generator_iterator) in _pure_gi_wrapper_types and generator_iterator.___666_close_wrapped_gi_999___ is False:
        generator_iterator = generator_iterator.the_wrapped_generator_iterator
    return GeneratorIterator__wrapper__extras_kwds4xexception_xresult(generator_iterator, ___666_mk_xresult_999___=mk_xresult, ___666_mk_xexception_999___=mk_xexception, ___666_close_wrapped_gi_999___=___666_close_wrapped_gi_999___)
    #return GeneratorIterator__wrapper__allow_extras_kwds(generator_iterator, ___666_mk_xresult_999___=mk_xresult, ___666_mk_xexception_999___=mk_xexception, ___666_close_wrapped_gi_999___=___666_close_wrapped_gi_999___)

def __():
    return;yield
assert [*mk_gi4either8xresult(__())] == []

class GeneratorIterator__bind_the_following_first_value4send(GeneratorIterator__wrapper):
    'bind the (following) first value for sf.send()'
    def __init__(sf, gi, /, *tmay_following_first_value4send, ___666_close_wrapped_gi_999___):
        check_tmay(tmay_following_first_value4send)
        sf._tm = tmay_following_first_value4send
        super().__init__(gi, ___666_close_wrapped_gi_999___=___666_close_wrapped_gi_999___)
    @property
    def tmay_following_first_value4send(sf, /):
        '-> tmay v'
        return sf._tm
    @tmay_following_first_value4send.setter
    def tmay_following_first_value4send(sf, tmay_v, /):
        check_tmay(tmay_v)
        if not tmay_v:
            #no op
            return
        [v] = tmay_v
        sf.the_following_first_value4send = v
        return
        if sf._tm:raise ValueError('logic-err')
        sf._tm = tmay_v
    #@override

    @property
    def the_following_first_value4send(sf, /):
        '-> v | ^IndexError'
        return sf._tm[0]
    @the_following_first_value4send.setter
    def the_following_first_value4send(sf, v, /):
        if sf._tm:raise ValueError('logic-err')
        sf._tm = (v,)
    #@override
    def send(sf, v, /):
        if sf._tm:
            if not v is None:raise ValueError('logic-err')
            [v] = sf._tm
            sf._tm = null_tuple
        return sf._gi.send(v)
def bind_gi_with_the_following_first_value4send(gi, /, *tmay_following_first_value4send, ___666_close_wrapped_gi_999___=False):
    'bind the (following) first value for gi.send()'
    check_tmay(tmay_following_first_value4send)
    if type(gi) is GeneratorIterator__bind_the_following_first_value4send:
        gi.tmay_following_first_value4send = tmay_following_first_value4send
    else:
        gi = GeneratorIterator__bind_the_following_first_value4send(gi, *tmay_following_first_value4send, ___666_close_wrapped_gi_999___=___666_close_wrapped_gi_999___)
    check_type_is(GeneratorIterator__bind_the_following_first_value4send, gi)
    return gi



class _BaseException__repr(BaseException):
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
    __str__ = __repr__
class EFlowControl(_BaseException__repr):pass
class EFinal(EFlowControl):pass
class EHalfway(EFlowControl):pass
def mk_boxed_EFinal(*args):
    return BoxedException__final(EFinal(*args))
def mk_boxed_EHalfway(*args):
    return BoxedException__halfway(EHalfway(*args))

class _Signal4xxx(_BaseException__repr):
    def is_ok_value(sf, xxx, /):
        return True
    def __init__(sf, xxx, /):
        assert sf.is_ok_value(xxx)
        sf._v = xxx
    @property
    def _value_(sf, /):
        return sf._v
class _Signal4halfway_exception(_Signal4xxx):
    @property
    def is_ok_value(sf, /):
        return is_boxed_halfway_exception
    boxed_halfway_exception = _Signal4xxx._value_
class _Signal4halfway_result(_Signal4xxx):
    @property
    def is_ok_value(sf, /):
        return is_boxed_halfway_result
    boxed_halfway_result = _Signal4xxx._value_
    #is_ok_value = staticmethod(is_boxed_halfway_result)

    #def __init__(sf, boxed_halfway_result, /):
    #    assert is_boxed_halfway_result(boxed_halfway_result)
    #    sf._bhr = boxed_halfway_result
    #@property
    #def boxed_halfway_result(sf, /):
    #    return sf._bhr

class BoxedXxx:
    def __init__(sf, xxx, /):
        sf._x = xxx
    def unbox(sf, /):
        '-> xxx'
        return sf._x
    def __repr__(sf, /):
        return repr_helper(sf, sf.unbox())


#new:feature__halfway_exception
class BoxedException(_BaseException__repr, BoxedXxx, BaseException):
    r'''[[[
    'boxed_exception:[xxx:=exception]'
    used in two ways:
    def gi_maker1(...):
        ...
        yield BoxedException__halfway(EHalfway()) #halfway_exception/he
        raise BoxedException__final(EFinal()) #final_exception/fe
    def gi_maker2(...):
        try:
            xr = yield gi_maker1(...)
        except EHalfway as e:
            ...
        except EFinal as e:
            ...
        except Escaped as e:
            ...
        #xxx:except BoxedException__final as bf_exc:
            f_exc = bf_exc.final_exception
        #xxx:except BoxedException__halfway as bh_exc:
            h_exc = bf_exc.halfway_exception

    #]]]'''#'''
    def __init__(sf, exc, /):
        check_type_le(BaseException, exc)
        BoxedXxx.__init__(sf, exc)
        BaseException.__init__(sf, exc)
class Escaped(BoxedException):
    'to prevent uncatched:(BoxedException__halfway|BoxedException__final)'
    def __init__(sf, exc, /, *, _lvl_=0):
        check_int_ge(0, _lvl_)
        if type(exc) is Escaped:
            assert _lvl_ == 0
            _lvl_ = 1 + exc._lvl_
            assert _lvl_ > 0
            exc = exc.unbox()
        else:
            pass#[_lvl_ > 0] for repr()
        if type(exc) is Escaped:raise TypeError('logic-err')
        check_type_le(BoxedException, exc)
        sf._lvl_ = _lvl_
        super().__init__(exc)
    def __repr__(sf, /):
        return repr_helper(sf, sf.unbox(), _lvl_=sf._lvl_)

class BoxedException__halfway(BoxedException):
    'boxed_halfway_exception#yield=>will throw into the parent_gi'
    #halfway_vs_final = False
class BoxedException__final(BoxedException):
    'boxed_final_exception#raise=>will throw into the parent_gi'
    #halfway_vs_final = True
class BoxedException__through(BoxedException):
    'boxed_through_exception#raise=>will not throw into the parent_gi'





class _IBoxed8Either(BoxedXxx):
    def __iter__(sf, /):
        yield sf.case
        yield sf.unbox()
class BoxedTailRecur(_IBoxed8Either):
    'boxed_tail_recur:[xxx:=raw_tail_recur]'
    case = False
class BoxedFinalResult(_IBoxed8Either):
    'boxed_final_result:[xxx:=raw_final_result]'
    case = True
_types4return5tail_recur_gi_protocol = (BoxedTailRecur, BoxedFinalResult, Either, tuple)

class BoxedHalfwayResult(BoxedXxx):
    'boxed_halfway_result:[xxx:=raw_halfway_result]'
    #___666_is_halfway_result_999___ = True
    #def __init__(sf, raw_halfway_result, /):
    #    sf._rhr = raw_halfway_result
    #def unbox(sf, /):
    #    '-> raw_halfway_result'
    #    return sf._rhr
assert not issubclass(BoxedHalfwayResult, IGeneratorIterator)
assert not issubclass(BoxedException, IGeneratorIterator)


_known_gi_types = (GeneratorType, GeneratorIterator__forbid_halfway_result, GeneratorIterator__either8xresult, GeneratorIterator__bind_the_following_first_value4send)
_known_gi_type_addrs = tuple(map(id, _known_gi_types))
def is_generator_iterator(x, /):
    return isinstance(x, IGeneratorIterator)
    return id(type(x)) in _known_gi_type_addrs or isinstance(x, IGeneratorIterator)
def is_boxed_xxx(x, /):
    return isinstance(x, BoxedXxx)
def is_boxed_exception(x, /):
    return isinstance(x, BoxedException)
    return type(x) is BoxedException
def is_boxed_halfway_exception(x, /):
    return type(x) is BoxedException__halfway
def is_boxed_final_exception(x, /):
    return type(x) is BoxedException__final

def is_boxed_halfway_result(x, /):
    return type(x) is BoxedHalfwayResult
    return type(x) is BoxedHalfwayResult or getattr(x, '___666_is_halfway_result_999___', False) is True
class HalfwayResultAndTailGI(tuple):
    def __new__(cls, rhr, gi, /):
        check_type_le(IGeneratorIterator, gi)
        return tuple.__new__(cls, [rhr, gi])
    def __repr__(sf, /):
        return repr_helper(sf, *sf)
#class HalfwayExceptionAndTailGI(tuple, Exception):
class HalfwayExceptionAndTailGI(Exception):
    #def __new__(cls, rhe, gi, /):
        #return tuple.__new__(cls, [rhe, gi])
    def __init__(cls, rhe, gi, /):
        check_type_le(BaseException, rhe)
        check_type_le(IGeneratorIterator, gi)
        super().__init__(rhe, gi)
    def __iter__(sf, /):
        #(rhe, gi) = sf.args
        return iter(sf.args)
    def __repr__(sf, /):
        return repr_helper(sf, *sf)
def mk_xresult(gi, bhr_or_rfr, /, *, bhr_vs_rfr):
    '#[fr::final_result(bfr/boxed_final_result|rfr/raw_final_result)][hr::halfway_result(bhr/boxed_halfway_result|rhr/raw_halfway_result)]'
    #rhr_or_rfr = bhr_or_rfr.unbox() if not bhr_vs_rfr else bhr_or_rfr
    rhr_gi_or_rfr = HalfwayResultAndTailGI(bhr_or_rfr.unbox(), gi) if not bhr_vs_rfr else bhr_or_rfr
    rhr_vs_rfr = bhr_vs_rfr
    del bhr_vs_rfr

    if not None is (mk_xr:=getattr(gi, '___666_mk_xresult_999___', None)):
        if type(mk_xr) is bool:
            if mk_xr is True:
                #eg:GeneratorIterator__either8xresult
                #std_mk_xresult:
                xr = either_rhr_gi_or_rfr = Either(rhr_vs_rfr, rhr_gi_or_rfr)
            else:
                #eg:GeneratorIterator__forbid_halfway_result
                #old_mk_xresult:
                if not rhr_vs_rfr:raise TypeError('forbid:halfway_result')
                xr = rfr = rhr_gi_or_rfr
                    #raw_final_result
        else:
            #customized:
            check_callable(mk_xr)
            xr = xresult = mk_xr(rhr_gi_or_rfr, rhr_vs_rfr=rhr_vs_rfr)
        xr
    else:
        #mixed:
        xr = rhr_gi_or_rfr
    xr
    return xr

def mk_xexception(gi, bhe_or_bfe, /, *, bhe_vs_bfe):
    '#[fe::final_exception(bfe/boxed_final_exception|rfe/raw_final_exception)][he::halfway_exception(bhe/boxed_halfway_exception|rhe/raw_halfway_exception)]'
    rhe_or_rfe = bhe_or_bfe.unbox()
    rhe_vs_rfe = bhe_vs_bfe
    rhe_gi_or_rfe = HalfwayExceptionAndTailGI(rhe_or_rfe, gi) if not rhe_vs_rfe else rhe_or_rfe

    if not None is (mk_xe:=getattr(gi, '___666_mk_xexception_999___', None)):
        if type(mk_xe) is bool:
            if mk_xe is True:
                #eg:GeneratorIterator__boxed8xexception
                #std_mk_xexception:
                #boxed:
                #xe = bhe_or_bfe
                bhe_gi_or_bfe = BoxedException__halfway(rhe_gi_or_rfe) if not bhe_vs_bfe else bhe_or_bfe
                xe = bhe_gi_or_bfe
                    #will be Escaped
            else:
                #eg:GeneratorIterator__forbid_halfway_exception
                #old_mk_xexception:
                if not rhe_vs_rfe:raise TypeError('forbid:halfway_exception')
                xe = rfe = rhe_gi_or_rfe
                    #final_exception
        else:
            #customized:
            check_callable(mk_xe)
            xe = xexception = mk_xe(rhe_gi_or_rfe, rhe_vs_rfe=rhe_vs_rfe)
        xe
    else:
        #mixed:
        xe = rhe_gi_or_rfe
    xe
    if is_boxed_exception(xe):
        'to prevent uncatched:(BoxedException__halfway|BoxedException__final)'
        xe = Escaped(xe)
    return xe

_debug_ = True
_debug_ = False
#API_changed:def recur5yield__eval__main_generator_iterator(emplace_stack_ops, main_generator_iterator, child_gi_protocol, tail_recur_gi_protocol, /):
def recur5yield__eval__main_generator_iterator(emplace_stack_ops, main_generator_iterator, child_gi_protocol, tail_recur_gi_protocol, child_gi_exc_protocol, /):
    r'''
    emplace_stack_ops -> (main_generator_iterator, child_gi_protocol, tail_recur_gi_protocol, child_gi_exc_protocol) -> main_result/result5recur<main_generator_iterator>

    emplace_stack_ops :: IEmplaceStackOps

    main_generator_iterator :: IGeneratorIterator<yield-exprlist5yield, return-return_value5child>
    child_gi_protocol(exprlist5yield) -> gi_or_bhr_or_bhe/(generator_iterator|boxed_halfway_result|boxed_ halfway_exception)
    tail_recur_gi_protocol(return_value5child) -> either_tailrecur_result/(is_result5recur, payload)/((False, exprlist5yield)|(True, result5recur))

    child_gi_exc_protocol :: (() -> (v|^i4e)) -> (() -> (v|^BoxedException__final))
    '''#'''
    check_type_le(IEmplaceStackOps, emplace_stack_ops)
    check_callable(child_gi_protocol)
    check_callable(tail_recur_gi_protocol)
    check_callable(child_gi_exc_protocol)

    ops = emplace_stack_ops

    init_value4send = None #const
    def push(exprlist5yield, /):
        ######################
        #new:feature__halfway_exception
        '-> None | ^_Signal4halfway_result(boxed_halfway_result) | ^_Signal4halfway_exception(boxed_halfway_exception)'
        gi_or_bhr_or_bhe = child_gi_protocol(exprlist5yield)
            # [gi_or_bhr_or_bhe == (generator_iterator|boxed_halfway_result|boxed_halfway_exception)]
        if is_boxed_halfway_result(gi_or_bhr_or_bhe):
            boxed_halfway_result = gi_or_bhr_or_bhe
            #assert hasattr(boxed_halfway_result, 'unbox')
            raise _Signal4halfway_result(boxed_halfway_result)
        elif is_boxed_halfway_exception(gi_or_bhr_or_bhe):
            boxed_halfway_exception = gi_or_bhr_or_bhe
            raise _Signal4halfway_exception(boxed_halfway_exception)
        else:
            gi = gi_or_bhr_or_bhe
            push_gi(gi)
            return None
        ######################
        raise 000
        ######################
        #new:feature__halfway_result
        '-> None | ^_Signal4halfway_result(boxed_halfway_result)'
        gi_or_bhr = child_gi_protocol(exprlist5yield)
            # [gi_or_bhr == (generator_iterator|boxed_halfway_result)]
        if is_boxed_halfway_result(gi_or_bhr):
            boxed_halfway_result = gi_or_bhr
            #assert hasattr(boxed_halfway_result, 'unbox')
            raise _Signal4halfway_result(boxed_halfway_result)
        elif is_boxed_halfway_exception(gi_or_bhr):
            boxed_halfway_exception = gi_or_bhr
            raise _Signal4halfway_exception(boxed_halfway_exception)
        else:
            gi = gi_or_bhr
            push_gi(gi)
            return None
        ######################
        raise 000
        ######################
        #old:
        '-> None'
        it = child_gi_protocol(exprlist5yield)
        push_gi(it)
    def push_gi(generator_iterator, /):
        check_type_le(IGeneratorIterator, generator_iterator)
        if tmay_value4send: raise logic-err
        ops.push(stack, generator_iterator) #ls.append(generator_iterator)
        tmay_value4send.append(init_value4send)
        return


    stack = ops.mk_empty_stack() #ls = [] # stack<generator_iterator>
    tmay_value4send = []
    def main():
        if 1:
            #new:feature__halfway_exception
            exc_vs_val = True
        push_gi(main_generator_iterator)
        while not ops.is_empty(stack):#while ls:
            try:
                while 1:
                    value4send = tmay_value4send.pop()
                    [] = tmay_value4send
                    gi = ops.get_top(stack)
                    xsend = gi.send if exc_vs_val else gi.throw
                    exc_vs_val = True
                    if 1:
                        if _debug_:print_err(recur5yield__eval__main_generator_iterator, [repr_as_3dot, *(hex(id(gi)) for gi in stack[-3:])], xsend, type(value4send))
                        exprlist5yield = child_gi_exc_protocol(lambda:xsend(value4send))()
                            # ^StopIteration(result5recur)
                            # ^BoxedException__final(final_exception)/boxed_final_exception
                            # ^BoxedException__through(through_exception)/boxed_through_exception
                    elif 1:
                        lazy_xsend_v = curry1(xsend, value4send)
                        exprlist5yield = child_gi_exc_protocol(lazy_xsend_v)()
                    else:
                        exprlist5yield = xsend(value4send)#ls[-1].send(value4send)
                    exprlist5yield
                    assert exc_vs_val

                    push(exprlist5yield)
                        # ^_Signal4halfway_result(boxed_halfway_result)
                        # ^_Signal4halfway_exception(boxed_halfway_exception)
            except StopIteration as e:
                #BoxedTailRecur|BoxedFinalResult
                return_value5child = e.value
                gi = ops.pop(stack)#ls.pop()
                (is_result5recur, payload) = tail_recur_gi_protocol(return_value5child)
                if is_result5recur:
                    #asif-BoxedFinalResult
                    result5recur = payload
                    #old:tmay_value4send.append(result5recur)
                    xresult4final = mk_xresult(gi, result5recur, bhr_vs_rfr=True)#new:feature__halfway_result
                    777;    bhr_vs_rfr=True
                    #if 0b0001:print_err(gi)
                    #if 0b0001:print_err(gi, '___666_mk_xresult_999___', getattr(gi, '___666_mk_xresult_999___', None))
                    tmay_value4send.append(xresult4final)
                else:
                    #asif-BoxedTailRecur
                    exprlist5yield = payload
                    #bug:push(exprlist5yield)
                        # ^_Signal4halfway_result(boxed_halfway_result)
                        # ^_Signal4halfway_exception(boxed_halfway_exception)
                    _gi = _gi_or_bhr_or_bhe = child_gi_protocol(exprlist5yield)
                    #bug:push_gi(_gi)
                    _gi = mk_gi4xresult_xexception__as_(gi, _gi, ___666_close_wrapped_gi_999___=False)
                        #[_gi/tail_gi SHOULD HAS same outter-shape as original gi]
                        #mk_gi4xresult_xexception
                    push_gi(_gi)
            except _Signal4halfway_result as e:
                #BoxedHalfwayResult
                #new:feature__halfway_result
                boxed_halfway_result = e.boxed_halfway_result
                gi = ops.pop(stack)
                xresult4half = mk_xresult(gi, boxed_halfway_result, bhr_vs_rfr=False)
                777;    bhr_vs_rfr=False
                assert exc_vs_val
                tmay_value4send.append(xresult4half)
            except _Signal4halfway_exception as e:
                #BoxedException__halfway
                #new:feature__halfway_exception
                boxed_halfway_exception = e.boxed_halfway_exception
                gi = ops.pop(stack)
                xexception4half = mk_xexception(gi, boxed_halfway_exception, bhe_vs_bfe=False)
                777;    bhe_vs_bfe=False
                ######
                exc_vs_val = False
                tmay_value4send.append(xexception4half)
            except BoxedException__final as e:
                #BoxedException__final
                #new:feature__halfway_exception
                boxed_final_exception = e#xxx:e.boxed_final_exception
                gi = ops.pop(stack)
                xexception4final = mk_xexception(gi, boxed_final_exception, bhe_vs_bfe=True)
                777;    bhe_vs_bfe=True
                ######
                exc_vs_val = False
                tmay_value4send.append(xexception4final)
            except BoxedException__through as e:
                #BoxedException__through
                boxed_through_exception = e
                through_exception = boxed_through_exception.unbox()
                raise through_exception
            #end-try:
        else:#@outer-while:
            assert ops.is_empty(stack)
            [main_result] = tmay_value4send
            #if not main_result is result5recur:raise logic-err
            if not exc_vs_val:
                if not main_result is (xexception4final if bhe_vs_bfe else xexception4half):raise logic-err
            else:
                if not main_result is (xresult4final if bhr_vs_rfr else xresult4half):raise logic-err
                #if not main_result is xresult4final:raise logic-err
        #end-outer-while:
        if not exc_vs_val:
            raise main_result
        return main_result
    return main()




if 0:
  def check_getitemable(x, /):
    if not hasattr(type(x), '__getitem__'): raise TypeError

#child_gi_protocol6collector <: child_gi_protocol6getitemable
#child_gi_protocol6getitemable
def child_gi_protocol6getitemable__0case(getitemable, exprlist5yield, /):
    'getitemable<k,case> -> exprlist5yield/(key4case, *payload) -> generator_iterator'
    check_getitemable(getitemable)
    check_type_is(tuple, exprlist5yield)
    [key4case, *payload] = exprlist5yield
    case = getitemable[key4case]
    return_value5child = (case, *payload,)
    def generator_func():
        return return_value5child;yield
    return generator_func()
def child_gi_protocol6getitemable__0func(getitemable, exprlist5yield, /):
    'getitemable<k,generator_func> -> exprlist5yield/(generator_func, *args4gi_mkr) -> generator_iterator'
    check_getitemable(getitemable)
    check_type_is(tuple, exprlist5yield)
    [key4func, *args4gi_mkr] = exprlist5yield
    generator_func = getitemable[key4func]
    return generator_func(*args4gi_mkr)
def child_gi_protocol6getitemableT__0func5ref(deref4func, /):
    r'''
    deref4func -> child_gi_protocol6getitemable__0ref4func

    deref4func(ref4func) -> generator_func
    child_gi_protocol6getitemable__0ref4func :: getitemable<k,ref4func> -> exprlist5yield/(ref4func, *args4gi_mkr) -> generator_iterator

    '''#'''
    check_callable(deref4func)
    def child_gi_protocol6getitemable__0ref4func(getitemable, exprlist5yield, /):
        'getitemable<k,ref4func> -> exprlist5yield/(ref4func, *args4gi_mkr) -> generator_iterator'
        check_getitemable(getitemable)
        check_type_is(tuple, exprlist5yield)
        [key4ref4func, *args4gi_mkr] = exprlist5yield
        ref4func = getitemable[key4ref4func]
        generator_func = deref4func(ref4func)
        return generator_func(*args4gi_mkr)
    return child_gi_protocol6getitemable__0ref4func

explain__child_gi_protocol_vs_may_0ref4func_vs_echo
def explain__may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case(may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case, may_deref4func, collector, /):
    r'''
    -> child_gi_protocol

child_gi_protocol := curry1(child_gi_protocol6getitemable, collector)

child_gi_protocol6getitemable <<==:
    collector :: getitemable
    may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case :: (callable | None | bool)
        default:None ==>>:
            collector :: RecurGroupCollector4Recur5Yield
                ==>> type(collector)._child_gi_protocol_
        callable ==>> child_gi_protocol6getitemable
        True ==>> child_gi_protocol6getitemable__0case
        False ==>>:
            may_deref4func :: None | deref4func/callable/(ref4func -> generator_func)
                None ==>> child_gi_protocol6getitemable__0func
                callable ==>> child_gi_protocol6getitemable__0ref4func===child_gi_protocol6getitemableT__0func5ref<deref4func>

    '''#'''
    check_getitemable(collector)
    if may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case is None:
        check_type_le(RecurGroupCollector4Recur5Yield, collector)
        child_gi_protocol6getitemable = type(collector)._child_gi_protocol_
    elif callable(may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case):
        child_gi_protocol6getitemable = may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case
    elif may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case is True:
        _0case = True
        child_gi_protocol6getitemable = child_gi_protocol6getitemable__0case
    else:
        _0ref4func = may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case
        if not (_0ref4func is False):raise TypeError
        if may_deref4func is None:
            child_gi_protocol6getitemable = child_gi_protocol6getitemable__0func
        else:
            deref4func = may_deref4func
            check_callable(deref4func)
            child_gi_protocol6getitemable__0ref4func = child_gi_protocol6getitemableT__0func5ref(deref4func)
            child_gi_protocol6getitemable = child_gi_protocol6getitemable__0ref4func
    child_gi_protocol = curry1(child_gi_protocol6getitemable, collector)
    return child_gi_protocol
explain__may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case



#class Recur5Yield:
class RecurGroupCollector4Recur5Yield:
    #def __init__(sf, emplace_stack_ops_vs_may_ops4list_vs_ops4huge, may_child_gi_protocol__collector, tail_recur_gi_protocol_vs_may_echo_vs_turnoff, /, *args4update, **kwds4update):
    #    sf._child_gi_protocol = sf._child_gi_protocol_ if may_child_gi_protocol__collector is None else curry1(may_child_gi_protocol__collector, sf)
    #API_changed:def __init__(sf, emplace_stack_ops_vs_may_ops4list_vs_ops4huge, may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case, may_deref4func, tail_recur_gi_protocol_vs_may_echo_vs_turnoff, /, *args4update, **kwds4update):
    def __init__(sf, emplace_stack_ops_vs_may_ops4list_vs_ops4huge, may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case, may_deref4func, tail_recur_gi_protocol_vs_may_echo_vs_turnoff, child_gi_exc_protocol_vs_may_echo_vs_turnoff, /, *args4update, **kwds4update):
        sf._child_gi_protocol = explain__may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case(may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case, may_deref4func, sf)
        sf._tail_recur_gi_protocol = explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff(tail_recur_gi_protocol_vs_may_echo_vs_turnoff)
        sf._child_gi_exc_protocol = explain__child_gi_exc_protocol_vs_may_echo_vs_turnoff(child_gi_exc_protocol_vs_may_echo_vs_turnoff)
        sf._emplace_stack_ops = explain__emplace_stack_ops_vs_may_ops4list_vs_ops4huge(emplace_stack_ops_vs_may_ops4list_vs_ops4huge)
        sf._d = {}
        sf.update(*args4update, **kwds4update)
    def update(sf, /, *args4update, **kwds4update):
        d = dict(*args4update, **kwds4update)
        for nm, generator_func in d.items():
            sf[nm] = generator_func
    def __setitem__(sf, nm, generator_func, /):
        if 0:
            check_callable(generator_func)
        else:
            if not callable(generator_func):
                raise TypeError(f'not callable: {nm!r}={generator_func!r}')
        dict_add__is(sf._d, nm, generator_func)
    def __getitem__(sf, nm, /):
        return sf._d[nm]
        raise KeyError
    def __contains__(sf, nm, /):
        return nm in sf._d

    #def __call__(sf, /, *args4main, **kwds4main):
    def __call__(sf, named_generator_func_vs_name, /):
        '(named_generator_func->None)|(name -> decorator/(generator_func->None))'
        if callable(named_generator_func_vs_name):
            named_generator_func = named_generator_func_vs_name
            sf.put_named_generator_func(named_generator_func)
            return None
            return sf
        else:
            name = named_generator_func_vs_name
            decorator = sf.mk_decorator(name)
            return decorator
    def put_named_generator_func(sf, named_generator_func, /):
        name = named_generator_func.__name__
        sf[name] = named_generator_func
        return None

    def mk_decorator(sf, name, /):
        #hash(name)
        if name in sf: raise KeyError(name)
        def decorator(generator_func, /):
            sf[name] = generator_func
            return None
            return sf
        return decorator
    def _child_gi_protocol_(sf, exprlist5yield, /):
        'exprlist5yield/(name4func, *args4gi_mkr) -> generator_iterator'
        return child_gi_protocol6getitemable__0func(sf, exprlist5yield)
        ##old ver:
        check_type_is(tuple, exprlist5yield)
        #check_tuple(exprlist5yield)
        [nm, *args4gi_mkr] = exprlist5yield
        return sf[nm](*args4gi_mkr)
    def mk_main(sf, main_name, /):
        child_gi_protocol = sf._child_gi_protocol
        tail_recur_gi_protocol = sf._tail_recur_gi_protocol
        child_gi_exc_protocol = sf._child_gi_exc_protocol
        emplace_stack_ops = sf._emplace_stack_ops

        main_generator_func = sf[main_name]
        main4recur5yield = recur5yield__decoratorT__all_gi_protocols(emplace_stack_ops, child_gi_protocol, tail_recur_gi_protocol, child_gi_exc_protocol)(main_generator_func)
        return main4recur5yield
#pseudo
class HelperPseudoMeta8Recur5Yield(type):
    def __new__(meta, name, bases, namespace, /, **kwds4meta__full):
        if not meta is __class__: raise TypeError
        del meta
        return HelperPseudoMeta8Recur5Yield(name, bases, namespace, **kwds4meta__full)
#API_changed:def HelperPseudoMeta8Recur5Yield(name, bases, namespace, /, *, emplace_stack_ops_vs_may_ops4list_vs_ops4huge=None, may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case=None, may_deref4func=None, tail_recur_gi_protocol_vs_may_echo_vs_turnoff=None, **kwds4meta__tail):
def HelperPseudoMeta8Recur5Yield(name, bases, namespace, /, *, emplace_stack_ops_vs_may_ops4list_vs_ops4huge=None, may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case=None, may_deref4func=None, tail_recur_gi_protocol_vs_may_echo_vs_turnoff=None, child_gi_exc_protocol_vs_may_echo_vs_turnoff=None, **kwds4meta__tail):
    if 1:
        if bases: raise TypeError
        if kwds4meta__tail: raise TypeError
        collector = RecurGroupCollector4Recur5Yield(emplace_stack_ops_vs_may_ops4list_vs_ops4huge, may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case, may_deref4func, tail_recur_gi_protocol_vs_may_echo_vs_turnoff, child_gi_exc_protocol_vs_may_echo_vs_turnoff)
    else:
        args4gi_mkr = bases
        kwds4gi_mkr = kwds4meta__tail
        collector = RecurGroupCollector4Recur5Yield(emplace_stack_ops_vs_may_ops4list_vs_ops4huge, may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case, may_deref4func, tail_recur_gi_protocol_vs_may_echo_vs_turnoff, child_gi_exc_protocol_vs_may_echo_vs_turnoff, *args4gi_mkr, **kwds4gi_mkr)
    excludes = {
        '__module__'
        ,'__qualname__'
        }
    bads = {k:v for k,v in namespace.items() if not callable(v)}
    if not excludes == bads.keys(): raise logic-err
    pairs = ((k,v) for k,v in namespace.items() if k not in excludes)
    collector.update(pairs)
    main_name = name
    main4recur5yield = collector.mk_main(main_name)
    return main4recur5yield

__all__
from seed.func_tools.recur5yield__halfway import HelperPseudoMeta8Recur5Yield

from seed.func_tools.recur5yield__halfway import recur5yield__list__echo__echo, recur5yield__list__echo__off, recur5yield__list__0func__echo, recur5yield__list__0func__off

from seed.func_tools.recur5yield__halfway import recur5yield__huge__echo__echo, recur5yield__huge__echo__off, recur5yield__huge__0func__echo, recur5yield__huge__0func__off

from seed.func_tools.recur5yield__halfway import recur5yield__eval__main_generator_iterator
from seed.func_tools.recur5yield__halfway import recur5yield__decoratorT__all_gi_protocols, child_gi_protocol__echo, child_gi_protocol__0func, child_gi_protocolT__0func5ref, tail_recur_gi_protocol__echo, tail_recur_gi_protocol__off, child_gi_exc_protocol__echo, child_gi_exc_protocol__off

from seed.func_tools.recur5yield__halfway import RecurGroupCollector4Recur5Yield
from seed.func_tools.recur5yield__halfway import explain__child_gi_protocol_vs_may_0ref4func_vs_echo, explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff, explain__child_gi_exc_protocol_vs_may_echo_vs_turnoff, explain__emplace_stack_ops_vs_may_ops4list_vs_ops4huge, explain__may_child_gi_protocol6getitemable_vs_0ref4func_vs_0case
from seed.func_tools.recur5yield__halfway import child_gi_protocol6getitemable__0case, child_gi_protocol6getitemable__0func, child_gi_protocol6getitemableT__0func5ref


#new:feature__halfway_result
#new:feature__halfway_exception
from seed.func_tools.recur5yield__halfway import bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception__as_, mk_gi4xresult_xexception, detach_asif_new_gi_wrapper
from seed.func_tools.recur5yield__halfway import BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
from seed.func_tools.recur5yield__halfway import EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway

from seed.func_tools.recur5yield__halfway import GeneratorIterator__bind_the_following_first_value4send, GeneratorIterator__either8xresult, GeneratorIterator__boxed8xexception, GeneratorIterator__forbid_halfway_exception, GeneratorIterator__forbid_halfway_result

from seed.func_tools.recur5yield__halfway import GeneratorIterator__wrapper
from seed.func_tools.recur5yield__halfway import BoxedXxx, BoxedException
from seed.func_tools.recur5yield__halfway import is_generator_iterator, is_boxed_xxx, is_boxed_exception
from seed.func_tools.recur5yield__halfway import mk_gi4return
from seed.func_tools.recur5yield__halfway import is_boxed_halfway_result, is_boxed_halfway_exception, is_boxed_final_exception
from seed.func_tools.recur5yield__halfway import mk_xresult, mk_xexception

from seed.func_tools.recur5yield__halfway import check_ok_return5child_gi_protocol, is_ok_return5child_gi_protocol, std_ok_return5tail_recur_gi_protocol, check_ok_return5tail_recur_gi_protocol, is_ok_return5tail_recur_gi_protocol



from seed.func_tools.recur5yield__halfway import HalfwayResultAndTailGI, HalfwayExceptionAndTailGI
from seed.func_tools.recur5yield__halfway import *

if 0:
    #use instead: py -m nn_ns.app.doctest_cmd seed.func_tools.recur5yield__halfway:__doc__ -ff -v
    #
    if __name__ == "__main__":
        import doctest
        doctest.testmod()


