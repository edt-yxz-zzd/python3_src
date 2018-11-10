
r'''
>>> d = {}
>>> class BiPatternHere(BiPatternABC__directly):
...     biregex_dict = d
>>> class name(BiPatternHere):
...     rough_pattern_fmt = r'(?!\d)\w+'
...     precise_pattern_fmt = rough_pattern_fmt
>>> class inline_char(BiPatternHere):
...     rough_pattern_fmt = r'[ \S]'
...     precise_pattern_fmt = rough_pattern_fmt
>>> class string(BiPatternHere):
...     rough_pattern_fmt = r'"(?:\\[^\n]|(?={inline_char})[^\\\n"])*"'
...     precise_pattern_fmt = r'"(?:\\x\d\d|\\[ntr]|(?={inline_char})[^\\\n"])*"(?:(?=[ ])|(?!{inline_char.flip}))'
>>> print(sorted(d.items())) #doctest: +ELLIPSIS
[('inline_char', <class '....inline_char'>), ('name', <class '....name'>), ('string', <class '....string'>)]
'''

__all__ = '''
    BiPatternABC__directly
    BiPatternABC__directly__same

    init_bipattern_class
    '''.split()

from ..class_property import class_property
from .Flippable import Flippable
from .abc import abstractmethod
from .IBiRegex import IBiRegex
import re
import inspect

def bipattern2flippable(bipattern):
    return Flippable(bipattern.rough_regex.pattern
                    , bipattern.precise_regex.pattern)
class BiPatternABC__directly(IBiRegex):
    '''

# any object has below attrs and s.t. IBiRegex be a BiPatternABC__directly
bipattern:
    .name :: identifier_str
        will be used in some fmt later
        r'(?={name})(?!{name.flip})'
        the named variable is Flippable
    .regex_flags :: re module flags
    .biregex_dict :: {name: biregex}
    .rough_pattern_fmt :: format_str
    .precise_pattern_fmt :: format_str
'''
    __slots__ = ()
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if inspect.isabstract(cls): return
        init_bipattern_class(cls)

    # will be overrided in __init_subclass__
    rough_regex = None
    precise_regex = None

    # may be overrided
    @class_property
    def name(cls):
        return cls.__name__
    @class_property
    def regex_flags(cls):
        return re.MULTILINE | re.VERBOSE


    # mutable dict to inject to
    @class_property
    @abstractmethod
    def biregex_dict(cls):
        # :: Map name IBiRegex
        #   mutable!
        raise NotImplementedError

    @class_property
    @abstractmethod
    def rough_pattern_fmt(cls):
        # :: regex pattern fmt
        raise NotImplementedError
    @class_property
    @abstractmethod
    def precise_pattern_fmt(cls):
        # :: regex pattern fmt
        raise NotImplementedError

class BiPatternABC__directly__same(BiPatternABC__directly):
    __slots__ = ()
    rough_pattern_fmt = None
    precise_pattern_fmt = None
    def __init_subclass__(cls, **kwargs):
        if not inspect.isabstract(cls):
            cls.rough_pattern_fmt = cls.precise_pattern_fmt = cls.pattern_fmt
        super().__init_subclass__(**kwargs)

    @class_property
    @abstractmethod
    def pattern_fmt(cls):
        # :: regex pattern fmt
        raise NotImplementedError
def init_bipattern_class(cls):
    rough_pattern_dict = {
        name: bipattern2flippable(bipattern)
        for name, bipattern in cls.biregex_dict.items()
        }
    precise_pattern_dict = {
        name: flippable.flip
        for name, flippable in rough_pattern_dict.items()
        }
    cls.rough_regex = compile_pattern_fmt(cls
        , cls.rough_pattern_fmt, rough_pattern_dict)
    cls.precise_regex = compile_pattern_fmt(cls
        , cls.precise_pattern_fmt, precise_pattern_dict)
    # inject to biregex_dict
    _cls = cls.biregex_dict.setdefault(cls.name, cls)
    if _cls is not cls:
        raise Exception('{cls.name!r} biregex already defined')

def compile_pattern_fmt(cls, pattern_fmt, pattern_dict):
    pattern = pattern_fmt2pattern(cls, pattern_fmt, pattern_dict)
    return compile_pattern(cls, pattern)
def pattern_fmt2pattern(cls, pattern_fmt, pattern_dict):
    pattern = pattern_fmt.format(**pattern_dict)
    pattern = f'(?:{pattern})'
    return pattern
def compile_pattern(cls, pattern):
    return re.compile(pattern, cls.regex_flags)


def _t():
    d = {}
    class BiPatternHere(BiPatternABC__directly):
        biregex_dict = d
    class name(BiPatternHere):
        rough_pattern_fmt = r'(?!\d)\w+'
        precise_pattern_fmt = rough_pattern_fmt
    class inline_char(BiPatternHere):
        rough_pattern_fmt = r'[ \S]'
        precise_pattern_fmt = rough_pattern_fmt
    class string(BiPatternHere):
        rough_pattern_fmt = r'"(?:\\[^\n]|(?={inline_char})[^\\\n"])*"'
        precise_pattern_fmt = r'"(?:\\x\d\d|\\[ntr]|(?={inline_char})[^\\\n"])*"(?:(?=[ ])|(?!{inline_char.flip}))'
    print(d)


if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):




