'''

usage:
    see: nn_ns.my_fileformat.configuration.MyConfiguration2_lex

def make_token_action_and_inject_globals(
    from_states, to_state, token_name, string
    , *, escaped:bool):
    make_token_action_and_inject_to(
        from_states, to_state, token_name, string
        , escaped=escaped, globals=globals())

'''

__all__ = '''
    make_token_action
    make_token_action_and_inject_to
    '''.split()


import re as _re

def make_token_action(from_states, to_state, token_name, string, *, escaped:bool):
    # (str|Iter str) -> str -> str -> str -> token_action
    #   token_action: def t_XXX(token):...
    def f(__token):
        __token.lexer.begin(to_state)
        return __token
    def iter_func_name_parts():
        #bug:yield 't_'
        yield 't'
        if type(from_states) is str:
            yield from_states
        else:
            yield from from_states
        yield token_name
    func_name = '_'.join(iter_func_name_parts())
    pattern = string if escaped else _re.escape(string)

    f.__name__ = func_name
    f.__doc__ = pattern
    return f

def make_token_action_and_inject_to(
    from_states, to_state, token_name, string
    , *, globals, escaped:bool):
    d = globals; del globals

    token_action = make_token_action(
        from_states, to_state, token_name, string, escaped=escaped)
    func_name = token_action.__name__
    if func_name in d:
        raise Exception(f'{func_name} already exists in globals!!')
    d[func_name] = token_action


