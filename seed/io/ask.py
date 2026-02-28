#__all__:goto
r'''[[[
e ../../python3_src/seed/io/ask.py

seed.io.ask
py -m nn_ns.app.debug_cmd   seed.io.ask -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.ask:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   seed.io.ask   @ask_yes_no_ :'...?(y/n)'
py_adhoc_call   seed.io.ask   @ask_yes_no_ :'...?(y/n)' <<<y
    True
py_adhoc_call   seed.io.ask   @ask_yes_no_ :'...?(y/n)' <<<n
    False
py_adhoc_call   seed.io.ask   @ask_yes_no_ :'...?(y/n)' <<<t
    ^EOFError: EOF when reading a line
py_adhoc_call   seed.io.ask   @ask_yes_no_ :'...?(y/n)' <<<Y
    True
]]
[[
py_adhoc_call   seed.io.ask   @ask4idx_ :ny :'...?(y/n)' :'SHOULD INPUT: y/n'  <<<y
    1
py_adhoc_call   seed.io.ask   @ask4idx_ :ny :'...?(y/n)' :'SHOULD INPUT: y/n'  <<<n
    0
py_adhoc_call   seed.io.ask   @ask4idx_ :ny :'...?(y/n)' :'SHOULD INPUT: y/n'  <<<Y
    ^EOFError: EOF when reading a line
py_adhoc_call   seed.io.ask   @ask4idx_ :ny :'...?(y/n)' :'SHOULD INPUT: y/n' +to_lower <<<Y
    1
py_adhoc_call   seed.io.ask   @ask4idx_ :ny :'...?(y/n)' :'SHOULD INPUT: y/n' <<<' y'
    ^EOFError: EOF when reading a line
py_adhoc_call   seed.io.ask   @ask4idx_ :ny :'...?(y/n)' :'SHOULD INPUT: y/n' +to_strip <<<' y'
    1
py_adhoc_call   seed.io.ask   @ask4idx_ :ny :'...?(y/n)' :'SHOULD INPUT: y/n' +to_strip <<<' Y'
    ^EOFError: EOF when reading a line
py_adhoc_call   seed.io.ask   @ask4idx_ :ny :'...?(y/n)' :'SHOULD INPUT: y/n' +to_strip +to_lower <<<' Y'
    1

py_adhoc_call   seed.io.ask   @ask4idx_ :NY :'...?(Y/N)' :'SHOULD INPUT: Y/N' <<<'Y'
    1
py_adhoc_call   seed.io.ask   @ask4idx_ :NY :'...?(Y/N)' :'SHOULD INPUT: Y/N' <<<'y'
    ^EOFError: EOF when reading a line
py_adhoc_call   seed.io.ask   @ask4idx_ :NY :'...?(Y/N)' :'SHOULD INPUT: Y/N' --may_std_=str.upper <<<'y'
    1

]]


]]]'''#'''
__all__ = r'''
ask_yes_no_

std_answer4ask_
ask4result__func_
    ask4answer_
    ask4idx_
    ask4result__dict_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.debug.print_err import print_err
___end_mark_of_excluded_global_names__0___ = ...

def ask_yes_no_(prompt, /):
    while 1:
        c = input(prompt).strip().lower()
            # ^EOFError if ctrl_D
            # ^KeyboardInterrupt if ctrl_C
        match c:
            case 'y':
                return True
            case 'n':
                return False
            case _:
                print_err('SHOULD INPUT: y/n')
                continue
            #case



def std_answer4ask_(answer, /, *, to_strip, to_lower, may_std_):
    if to_strip:
        answer = answer.strip()
    if to_lower:
        answer = answer.lower()
    if not None is may_std_:
        std_ = may_std_
        answer = std_(answer)
    return answer
def ask4result__func_(answer2tmay_result_, prompt, prompt4fail, /, *, to_strip=False, to_lower=False, may_std_=None):
    assert callable(answer2tmay_result_)
    assert type(prompt) is str
    assert type(prompt4fail) is str
    kwds = dict(to_strip=to_strip, to_lower=to_lower, may_std_=may_std_)
    while 1:
        answer = input(prompt)#.strip().lower()
            # ^EOFError if ctrl_D
            # ^KeyboardInterrupt if ctrl_C
        answer = std_answer4ask_(answer, **kwds)
        tmay_result = answer2tmay_result_(answer)
        if tmay_result:
            [result] = tmay_result
            return result
        if prompt4fail:
            print_err(prompt4fail)
def ask4answer_(ok_, prompt, prompt4fail, /, *, to_strip=False, to_lower=False, may_std_=None):
    assert callable(ok_)
    def answer2tmay_result_(answer, /):
        #tmay_result
        if ok_(answer):
            return (answer,)
        return ()
    kwds = dict(to_strip=to_strip, to_lower=to_lower, may_std_=may_std_)
    return ask4result__func_(answer2tmay_result_, prompt, prompt4fail, **kwds)

def ask4idx_(idx2answer, prompt, prompt4fail, /, *, to_strip=False, to_lower=False, may_std_=None):
    assert len(idx2answer)
    assert type(idx2answer[0]) is str
    def answer2tmay_result_(answer, /):
        try:
            j = idx2answer.index(answer)
        except ValueError:
            return ()
        return (j,)
    kwds = dict(to_strip=to_strip, to_lower=to_lower, may_std_=may_std_)
    return ask4result__func_(answer2tmay_result_, prompt, prompt4fail, **kwds)
def ask4result__dict_(answer2result, prompt, prompt4fail, /, *, to_strip=False, to_lower=False, may_std_=None):
    assert len(answer2result)
    assert type(next(iter(answer2result.keys()))) is str
    kwds = dict(to_strip=to_strip, to_lower=to_lower, may_std_=may_std_)
    def answer2tmay_result_(answer, /):
        try:
            result = answer2result[answer]
        except KeyError:
            return ()
        return (result,)
    return ask4result__func_(answer2tmay_result_, prompt, prompt4fail, **kwds)

__all__
from seed.io.ask import ask_yes_no_
from seed.io.ask import ask4result__func_, ask4answer_, ask4idx_, ask4result__dict_
from seed.io.ask import std_answer4ask_
from seed.io.ask import *
