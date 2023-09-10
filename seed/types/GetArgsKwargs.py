
# e ../../python3_src/seed/types/GetArgsKwargs.py

from seed.helper.repr_input import repr_helper
from seed.tiny import check_callable
from seed.tiny_.funcs import echo_args_kwargs





class GetArgsKwargs:
    def get_args_kwargs(sf, /):
        return (sf.args, sf.kwargs)
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and sf.get_args_kwargs() == ot.get_args_kwargs()
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args, **sf.kwargs)
    def __init__(sf, /, *args, **kwargs):
        sf.args = args
        sf.kwargs = kwargs
    def call_me_then_input_(sf, f, /, *post_args, **ex_kw):
        return f(*sf.args, *post_args, **sf.kwargs, **ex_kw)
    def call_input_then_me_(sf, f, /, *pre_args, **ex_kw):
        return f(*pre_args, *sf.args, **sf.kwargs, **ex_kw)
    def call2_(sf, f, pre_args, post_args, /, **ex_kw):
        return f(*pre_args, *sf.args, *post_args, **sf.kwargs, **ex_kw)


assert GetArgsKwargs(1) == GetArgsKwargs(1)
assert not GetArgsKwargs(1) != GetArgsKwargs(1)
assert repr(GetArgsKwargs(1, 3, b=0, a=2)) == 'GetArgsKwargs(1, 3, a = 2, b = 0)'
assert GetArgsKwargs(1,2).call_me_then_input_(GetArgsKwargs, 3,4) == GetArgsKwargs(1, 2, 3, 4)
assert GetArgsKwargs(1,2).call_input_then_me_(GetArgsKwargs, 3,4) == GetArgsKwargs(3, 4, 1, 2)




class GetFuncArgsKwargs:
    def get_func_args_kwargs(sf, /):
        return (sf.func, sf.args, sf.kwargs)
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and sf.get_func_args_kwargs() == ot.get_func_args_kwargs()
    def __repr__(sf, /):
        return repr_helper(sf, sf.func, *sf.args, **sf.kwargs)
    def __init__(sf, f, /, *args, **kwargs):
        check_callable(f)
        sf.func = f
        sf.args = args
        sf.kwargs = kwargs
    def call0_me_then_input_(sf, /, *post_args, **ex_kw):
        return sf.func(*sf.args, *post_args, **sf.kwargs, **ex_kw)
    def call0_input_then_me_(sf, /, *pre_args, **ex_kw):
        return sf.func(*pre_args, *sf.args, **sf.kwargs, **ex_kw)
    def call02_(sf, pre_args, post_args, /, **ex_kw):
        return sf.func(*pre_args, *sf.args, *post_args, **sf.kwargs, **ex_kw)

assert GetFuncArgsKwargs(echo_args_kwargs, 1) == GetFuncArgsKwargs(echo_args_kwargs, 1)
assert not GetFuncArgsKwargs(echo_args_kwargs, 1) != GetFuncArgsKwargs(echo_args_kwargs, 1)
assert repr(GetFuncArgsKwargs(GetArgsKwargs, 1, 3, b=0, a=2)) == f"GetFuncArgsKwargs(<class '{__name__}.GetArgsKwargs'>, 1, 3, a = 2, b = 0)", repr(GetFuncArgsKwargs(GetArgsKwargs, 1, 3, b=0, a=2))
assert GetFuncArgsKwargs(GetArgsKwargs, 1,2).call0_me_then_input_(3,4) == GetArgsKwargs(1, 2, 3, 4)
assert GetFuncArgsKwargs(GetArgsKwargs, 1,2).call0_input_then_me_(3,4) == GetArgsKwargs(3, 4, 1, 2)




from seed.types.GetArgsKwargs import GetArgsKwargs, GetFuncArgsKwargs

