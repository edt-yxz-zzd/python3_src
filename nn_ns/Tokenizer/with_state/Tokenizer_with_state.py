

__all__ = '''
    Tokenizer_with_state
    BadRecognizerError
    '''.split()

from .abc import abstractmethod, override, final
from .TokenizerABC_with_state import TokenizerABC_with_state
from .IRecognizer import IRecognizer
from .errors import BadRecognizerError, TokenizerFailError_with_tail

from itertools import chain


class Tokenizer_with_state(TokenizerABC_with_state):
    '''see: IRecognizer

recognizer:
    .name :: Hashable&Comparable
        e.g. str
    .may_recognize1(state, source, begin, end) -> None|(tokens, succ_state, middle)
        tokens :: Iterable token
            may or may not be iterator
    .allow_empty :: bool
    .precondition_states :: {state} | None
        None - any state

allow_multi_empty :: bool
    mulit recognizers read empty tokens
'''
    def __init__(self, initial_state, recognizers, *, allow_multi_empty=False):
        recognizers = tuple(recognizers)
        name2recognizer = {b.name: b for b in recognizers}
        if len(name2recognizer) != len(recognizers): raise ValueError('name duplicated')
        self.__name2recognizer = name2recognizer
        self.__allow_multi_empty = bool(allow_multi_empty)
        self.__initial_state = initial_state

    @override
    def get_initial_state(self):
        return self.__initial_state

    @override
    def iter_tokens_ex(self, state, source, begin, end):
        # -> Iter token | raise TokenizerFailError|BadRecognizerError
        assert 0 <= begin <= end <= len(source)
        END = end
        BEGIN = begin

        excludes = set() # {(state, name)}
        while True:
            # update state, begin, excludes
            d, emptys = self._recognize1(state, begin, end, excludes, source)

            may_pair = self._handle_emptys(state, begin, emptys)
            if may_pair is not None:
                tokens, succ_state = pair = may_pair
                yield from tokens
                if succ_state != state:
                    # update: state/excludes
                    #   neednot update: begin
                    excludes.update((state, name) for name in emptys)
                    state = succ_state
                    continue
            #may come from succ_state == state
            if not d:
                if begin == END: break
                tail = source[begin:]
                err_msg = f'fail at {begin}: no recognizers success'
                err_position = begin
                raise TokenizerFailError_with_tail(err_msg, err_position, source, BEGIN, END)
            if len(d) != 1:
                names = sorted(d)
                err_msg = f'fail at {begin}: too many recognizers success {names}'
                err_position = begin
                raise TokenizerFailError_with_tail(err_msg, err_position, source, BEGIN, END)

            [(tokens, succ_state, middle)] = d.values()
            assert begin < middle <= END
            yield from tokens
            state = succ_state
            begin = middle
            excludes.clear()
        return state # user may need the final state

    def _recognize1(self, state, begin, end, excludes, source):
        d = {}
        emptys = {}
        for name, recognizer in self.__name2recognizer.items():
            if state not in recognizer.precondition_states:
                continue
            if (state, name) in excludes:
                continue

            r = recognizer.may_recognize1(state, source, begin, end)
            if r is None: continue
            _tokens, _succ_state, middle = r
            if not begin <= middle <= end:
                raise BadRecognizerError(f'middle error: {name!r}: {recognizer!r}')
            if begin == middle:
                if not recognizer.allow_empty:
                    raise BadRecognizerError(f'empty error: {name!r}: {recognizer!r}')
                else:
                    emptys[name] = r
            else:
                d[name] = r
        return d, emptys

    def _handle_emptys(self, state, begin, emptys):
        # -> None|(tokens, succ_state)
        if not emptys:
            return None
        elif len(emptys) != 1:
            names = sorted(emptys)
            succ_states = {succ_state for _tokens, succ_state, _end in emptys.values()}
            if not self.allow_multi_empty:
                err_msg = f'empty error: mulit recognizers at same position={begin} but not allowed; {names}'
                err_position = begin
                raise TokenizerFailError_with_tail(err_msg, err_position, source, BEGIN, END)
            elif len(succ_states) != {state}:
                err_msg = f'empty error: mulit recognizers at same position={begin} with diff succ_states; {names}; succ_states={succ_states}!={{state!r}}'
                err_position = begin
                raise TokenizerFailError_with_tail(err_msg, err_position, source, BEGIN, END)
            succ_state = state
        else:
            [(_, succ_state, _)] = emptys.values()
        tokens = chain.from_iterable(tokens for tokens, _, _ in emptys.values())

        return tokens, succ_state



