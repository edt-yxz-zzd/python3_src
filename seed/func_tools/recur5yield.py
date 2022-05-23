#__all__:goto
r'''[[[[[
e ../../python3_src/seed/func_tools/recur5yield.py
py -m seed.func_tools.recur5yield
py -m nn_ns.app.debug_cmd   seed.func_tools.recur5yield

from seed.func_tools.recur5yield import HelperPseudoMeta8Recur5Yield
from seed.func_tools.recur5yield import recur5yield__echo__echo, recur5yield__echo__off, recur5yield__0func__echo, recur5yield__0func__off

from seed.func_tools.recur5yield import recur5yield__eval__main_generator_iterator
from seed.func_tools.recur5yield import recur5yield__decoratorT__all_gi_protocols, child_gi_protocol__echo, child_gi_protocol__0func, tail_recur_gi_protocol__echo, tail_recur_gi_protocol__off

from seed.func_tools.recur5yield import RecurGroupCollector4Recur5Yield
from seed.func_tools.recur5yield import explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff


[[
yield 实现 recur on container-list instead of python-stack

  @recur5yield(caller)
  def f(...):
      x = yield ...
      return x
  互调用递归组:
  @recur5yield(caller, 在互调用递归组中的命名)

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

GeneratorIterator === collections.abc.Generator <: Iterator
generator_iterator :: GeneratorIterator<iter-exprlist5yield, return-return_value5child>
    main_generator_iterator <: generator_iterator
generator :: Callable
    not [generator :: Iterator]
generator(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
    to avoid confuse generator with generator_iterator, below rename generator to generator_func
        # generator?(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
        #   generator =?= generator_func | ?generator_iterator?


generator_func(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
    main_generator_func(*args4main, **kwds4main) -> generator_iterator
    child_gi_protocol(exprlist5yield) -> generator_iterator
        rename history:
            recur_branch_generator_iterator_maker
            recur_branch_gen_iter_protocol
            recur_branch_gi_protocol
            child_gi_protocol
tail_recur_gi_protocol(return_value5child) -> either_tailrecur_result/(is_result5recur, payload)/((False, exprlist5yield)|(True, result5recur))

]]]
==========
==========
[[[

>>> import sys
>>> sys.getrecursionlimit()
1000
>>> sys.setrecursionlimit(500)

>>> collector = RecurGroupCollector4Recur5Yield(None, None)
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
>>> @collector.put_named_generator_func
... def f():    #not same callable => raise
...     yield
Traceback (most recent call last):
    ...
ValueError

>>> def _():
...     @recur5yield__echo__echo
...     def mul(n, m, /):
...         if m > 0:
...             return False, mul_(0, n, m)
...         return True, 0
...         yield
...     def mul_(acc, n, m, /):
...         if m > 1:
...             m = yield dec(m)
...             acc = yield add(acc, n)
...             return False, mul_(acc, n, m)
...         return False, add(acc, n)
...         return True, acc
...     def add(n, m, /):
...         if m > 0:
...             m = yield dec(m)
...             n = yield inc(n)
...             return False, add(n, m)
...         return True, n
...     def inc(n, /):
...         return True, n+1
...         yield
...     def dec(n, /):
...         return True, n-1
...         yield
...     return mul
>>> mul = _()
>>> mul(100, 233)
23300

>>> class main_entry1(metaclass=HelperPseudoMeta8Recur5Yield, tail_recur_gi_protocol_vs_may_echo_vs_turnoff=True):
...     def main_entry1(x, /):
...         return (yield 'main_', x)
...     def main_(x, /):
...         return [x];yield
>>> main_entry1([999])
[[999]]

>>> class main_entry2(metaclass=HelperPseudoMeta8Recur5Yield, may_child_gi_protocol__collector=None):
...     def main_entry2(x, /):
...         return (False, ('main_', x))
...         yield
...         #bug:return (False, (yield 'main_', x))
...     def main_(x, /):
...         return (True, (x,));yield
>>> main_entry2([999])
([999],)

>>> class main_entry3(metaclass=HelperPseudoMeta8Recur5Yield, may_child_gi_protocol__collector=RecurGroupCollector4Recur5Yield._child_gi_protocol_, tail_recur_gi_protocol_vs_may_echo_vs_turnoff=True):
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







]]]
==========
==========
[[[

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

    recur5yield__decoratorT__all_gi_protocols
        explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff
        child_gi_protocol__echo
        child_gi_protocol__0func
        tail_recur_gi_protocol__echo
        tail_recur_gi_protocol__off
            recur5yield__echo__echo
            recur5yield__echo__off
            recur5yield__0func__echo
            recur5yield__0func__off
    recur5yield__eval__main_generator_iterator

    HelperPseudoMeta8Recur5Yield
        RecurGroupCollector4Recur5Yield
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from functools import wraps
from collections.abc import Generator as GeneratorIterator #, Callable
from seed.tiny_.check import check_callable, check_type_is, check_pair #no check_tuple
from seed.tiny_.dict__add_fmap_filter import dict_add__is
from seed.tiny import curry1
___end_mark_of_excluded_global_names__0___ = ...

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
def recur5yield__decoratorT__all_gi_protocols(child_gi_protocol, tail_recur_gi_protocol, /):
    r'''
    (child_gi_protocol, tail_recur_gi_protocol) -> decorator

    decorator :: main_generator_func -> expected_main_recur_func
    expected_main_recur_func :: (*args4main, **kwds4main) -> main_result
    main_result = result5recur<main_generator_iterator>

    main_generator_func(*args4main, **kwds4main) -> main_generator_iterator
    main_generator_iterator :: GeneratorIterator<iter-exprlist5yield, return-return_value5child>

    child_gi_protocol(exprlist5yield) -> generator_iterator
    tail_recur_gi_protocol(return_value5child) -> either_tailrecur_result
    either_tailrecur_result === (is_result5recur, payload) :: ((False, exprlist5yield)|(True, result5recur))
    #'''
    check_callable(child_gi_protocol)
        # child_gi_protocol(exprlist5yield) -> generator_iterator
    check_callable(tail_recur_gi_protocol)
        # tail_recur_gi_protocol(return_value5child) -> either_tailrecur_result/(is_result5recur, payload)/((False, exprlist5yield)|(True, result5recur))

    def recur5yield__decorator__main_generator_func(main_generator_func, /):
        check_callable(main_generator_func)
            # main_generator_func(*args4main, **kwds4main) -> generator_iterator
            # generator_func(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
            # generator?(*args4gi_mkr, **kwds4gi_mkr) -> generator_iterator
            #   generator =?= generator_func | ?generator_iterator?

        @wraps(main_generator_func)
        def wrapper(*args4main, **kwds4main):
            main_generator_iterator = main_generator_func(*args4main, **kwds4main)
            main_result = recur5yield__eval__main_generator_iterator(main_generator_iterator, child_gi_protocol, tail_recur_gi_protocol)
            return main_result
        return wrapper
    return recur5yield__decorator__main_generator_func


def explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff(tail_recur_gi_protocol_vs_may_echo_vs_turnoff, /):
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


#child_gi_protocol
def child_gi_protocol__echo(exprlist5yield, /):
    'exprlist5yield/generator_iterator -> generator_iterator'
    generator_iterator = exprlist5yield
    if not isinstance(generator_iterator, GeneratorIterator): raise TypeError
    return generator_iterator
def child_gi_protocol__0func(exprlist5yield, /):
    'exprlist5yield/(generator_func, *args4gi_mkr) -> generator_iterator'
    check_type_is(tuple, exprlist5yield)
    [generator_func, *args4gi_mkr] = exprlist5yield
    return generator_func(*args4gi_mkr)

#tail_recur_gi_protocol
def tail_recur_gi_protocol__echo(return_value5child, /):
    'return_value5child/either_tailrecur_result -> either_tailrecur_result/(is_result5recur, payload)/((False, exprlist5yield)|(True, result5recur))'
    either_tailrecur_result = return_value5child
    check_pair(either_tailrecur_result)
    (is_result5recur, payload) = either_tailrecur_result
    check_type_is(bool, is_result5recur)
    return either_tailrecur_result
def tail_recur_gi_protocol__off(return_value5child, /):
    'return_value5child/result5recur -> either_tailrecur_result/(is_result5recur, payload)/(True, result5recur)'
    result5recur = return_value5child
    return (True, result5recur)


recur5yield__echo__echo = recur5yield__decoratorT__all_gi_protocols(child_gi_protocol__echo, tail_recur_gi_protocol__echo)
recur5yield__echo__off = recur5yield__decoratorT__all_gi_protocols(child_gi_protocol__echo, tail_recur_gi_protocol__off)
recur5yield__0func__echo = recur5yield__decoratorT__all_gi_protocols(child_gi_protocol__0func, tail_recur_gi_protocol__echo)
recur5yield__0func__off = recur5yield__decoratorT__all_gi_protocols(child_gi_protocol__0func, tail_recur_gi_protocol__off)





def recur5yield__eval__main_generator_iterator(main_generator_iterator, child_gi_protocol, tail_recur_gi_protocol, /):
    r'''
    (main_generator_iterator, child_gi_protocol, tail_recur_gi_protocol) -> main_result/result5recur<main_generator_iterator>

    main_generator_iterator :: GeneratorIterator<iter-exprlist5yield, return-return_value5child>
    child_gi_protocol(exprlist5yield) -> generator_iterator
    tail_recur_gi_protocol(return_value5child) -> either_tailrecur_result/(is_result5recur, payload)/((False, exprlist5yield)|(True, result5recur))
    #'''
    init_value4send = None #const
    def push(exprlist5yield, /):
        it = child_gi_protocol(exprlist5yield)
        push_gi(it)
    def push_gi(generator_iterator, /):
        if not isinstance(generator_iterator, GeneratorIterator): raise TypeError
        if tmay_value4send: raise logic-err
        ls.append(generator_iterator)
        tmay_value4send.append(init_value4send)

    ls = [] # stack<generator_iterator>
    tmay_value4send = []
    def main():
        push_gi(main_generator_iterator)
        while ls:
            try:
                while 1:
                    value4send = tmay_value4send.pop()
                    [] = tmay_value4send
                    exprlist5yield = ls[-1].send(value4send)
                        #raise StopIteration(result5recur)

                    push(exprlist5yield)
            except StopIteration as e:
                return_value5child = e.value
                ls.pop()
                (is_result5recur, payload) = tail_recur_gi_protocol(return_value5child)
                if is_result5recur:
                    result5recur = payload
                    tmay_value4send.append(result5recur)
                else:
                    exprlist5yield = payload
                    push(exprlist5yield)
            #end-try:
        else:
            [main_result] = tmay_value4send
            if not main_result is result5recur:raise logic-err
        #end-while:

        return main_result
    return main()


#class Recur5Yield:
class RecurGroupCollector4Recur5Yield:
    def __init__(sf, may_child_gi_protocol__collector, tail_recur_gi_protocol_vs_may_echo_vs_turnoff, /, *args4update, **kwds4update):
        sf._child_gi_protocol = sf._child_gi_protocol_ if may_child_gi_protocol__collector is None else curry1(may_child_gi_protocol__collector, sf)
        sf._tail_recur_gi_protocol = explain__tail_recur_gi_protocol_vs_may_echo_vs_turnoff(tail_recur_gi_protocol_vs_may_echo_vs_turnoff)
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
        'exprlist5yield/(name, *args4gi_mkr) -> generator_iterator'
        check_type_is(tuple, exprlist5yield)
        #check_tuple(exprlist5yield)
        [nm, *args4gi_mkr] = exprlist5yield
        return sf[nm](*args4gi_mkr)
    def mk_main(sf, main_name, /):
        child_gi_protocol = sf._child_gi_protocol
        tail_recur_gi_protocol = sf._tail_recur_gi_protocol

        main_generator_func = sf[main_name]
        main4recur5yield = recur5yield__decoratorT__all_gi_protocols(child_gi_protocol, tail_recur_gi_protocol)(main_generator_func)
        return main4recur5yield
#pseudo
class HelperPseudoMeta8Recur5Yield(type):
    def __new__(meta, name, bases, namespace, /, **kwds4meta__full):
        if not meta is __class__: raise TypeError
        del meta
        return HelperPseudoMeta8Recur5Yield(name, bases, namespace, **kwds4meta__full)
def HelperPseudoMeta8Recur5Yield(name, bases, namespace, /, may_child_gi_protocol__collector=None, tail_recur_gi_protocol_vs_may_echo_vs_turnoff=None, **kwds4meta__tail):
    if 1:
        if bases: raise TypeError
        if kwds4meta__tail: raise TypeError
        collector = RecurGroupCollector4Recur5Yield(may_child_gi_protocol__collector, tail_recur_gi_protocol_vs_may_echo_vs_turnoff)
    else:
        args4gi_mkr = bases
        kwds4gi_mkr = kwds4meta__tail
        collector = RecurGroupCollector4Recur5Yield(may_child_gi_protocol__collector, tail_recur_gi_protocol_vs_may_echo_vs_turnoff, *args4gi_mkr, **kwds4gi_mkr)
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()


