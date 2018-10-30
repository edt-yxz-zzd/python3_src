
r'''
usage:
    see: nn_ns.my_fileformat.configuration.MyConfiguration2_lex
    see: ply.lex



states = list(dict(
    State = exclusive
    ,State2 = inclusive
    ...
    ).items())
state_to = StateTo(states)

@state_to('-> AfterNoIndents', BigNewlineNoIndents)
def t_ANY_BigNewlineNoIndents(t):
    #= (ignore_tail0 newline)+ (?![#\s])
    #| ignore_tail1 (\Z)
    t.lexer.lineno += count_newlines(t.value)
    return t
'''

__all__ = '''
    StateTo
    '''.split()

from .lex_error_handle import token_error_handle

import re as _re
from functools import wraps


exclusive = 'exclusive'
inclusive = 'inclusive'
state_transform_regex = _re.compile(r'--|-> (\w+)')
class StateTo:
    def __init__(self, states):
        # states :: Iter (state, (exclusive|inclusive))
        # states :: Iter (str, str)
        #   ply.lex; module.states or globals()['states']
        self.states = set(st for st,_ in states)
    def parse_state_transform_to_may_state(self, state_transform:str):
        # -> None|str
        m = state_transform_regex.fullmatch(state_transform)
        if m is None:
            raise Exception(f'unknown state_transform: {state_transform!r}')
        may_result_state = m.group(1)
        if may_result_state is not None:
            #bug:if may_result_state in ('ANY', 'INITIAL'):
            #   no ANY
            #   ANY is a concept state, union of all states
            result_state = may_result_state
            if result_state == 'INITIAL':
                pass
            elif result_state not in self.states:
                raise Exception(f'unknown state: {result_state!r}')
        return may_result_state

    def __call__(self, state_transform, pattern_cls, *, discard=False):
        return self.state_to(state_transform, pattern_cls, discard=discard)
    def state_to(self, state_transform, pattern_cls, *, discard=False):
        # pattern_cls :: PatternBase
        #   see: .PatternBase.PatternBase/make_Pattern
        # state_transform: '-> {state}' | '--'
        # discard: discard or return token
        #
        may_result_state = self.parse_state_transform_to_may_state(state_transform)
        if may_result_state is not None:
            result_state = may_result_state

        def decorator(f):
            if not f.__name__.endswith(f'_{pattern_cls.__name__}'):
                raise Exception(f'name_error: {f.__name__!r} not endswith {pattern_cls.__name__!r}')

            @wraps(f)
            def __f__(__token):
                lexer = __token.lexer
                source_string = lexer.lexdata
                assert len(source_string) == lexer.lexlen

                begin = __token.lexpos
                end = lexer.lexpos
                assert begin + len(__token.value) == end

                m = pattern_cls.precise_regex.match(source_string, begin)
                may_group0 = None if m is None else m.group(0)
                if m is None or m.end() != end:
                    err_msg = \
    f'''match rough_pattern but not precise_pattern:
        rough_pattern = {pattern_cls.rough_pattern!r}
        precise_pattern = {pattern_cls.precise_pattern!r}
        rough_match_result = {__token.value!r}
        precise_match_result = {may_group0!r}
    '''
                    raise token_error_handle(__token, SyntaxError, err_msg)
                    raise SyntaxError(err_msg)

                r = f(__token)
                if discard:
                    if r is not None:
                        raise Exception('should discard the token')
                else:
                    if r is None:
                        raise Exception('should return a token')

                if may_result_state is not None:
                    lexer.begin(result_state)
                return r

            __f__.__doc__ = pattern_cls.rough_pattern
            return __f__
        return decorator


