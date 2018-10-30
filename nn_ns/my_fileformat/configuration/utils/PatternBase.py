
'''
usage:
    see: nn_ns.my_fileformat.configuration.MyConfiguration2_lex

Pattern = make_Pattern(globals())

'''
__all__ = '''
    PatternBase
    make_Pattern
    Pattern
    '''.split()

from .Flippable import Flippable
import re as _re

regex_flags = _re.MULTILINE | _re.VERBOSE
def regex_compile(pattern):
    # I require re.MULTILINE
    # PLY.lex using re.VERBOSE as flags
    return _re.compile(pattern, flags=regex_flags)



class PatternBase:
    '''

required; if missing, then require pattern_fmt
    rough_pattern :: str
    precise_pattern :: str

optional:
    rough_pattern_fmt :: str
    precise_pattern_fmt :: str
    pattern_fmt :: str
        r = rough_pattern_dict
        p = {pattern_name:~flippable
            for pattern_name, flippable in r.items()}
        rough_pattern = pattern_fmt.format(**r)
        precise_pattern = pattern_fmt.format(**p)
'''
    def __init_subclass__(cls, *, rough_pattern_dict, **kwargs):
        super().__init_subclass__(**kwargs)
        if rough_pattern_dict is None:
            # a base class
            return

        precise_pattern_dict = \
            {pattern_name:~flippable
            for pattern_name, flippable in rough_pattern_dict.items()
            }

        def mayset_x_pattern(x_pattern_attr, x_pattern_dict):
            assert x_pattern_attr in 'rough_pattern precise_pattern'.split()
            if hasattr(cls, x_pattern_attr): return

            x_pattern_fmt_attr = f'{x_pattern_attr}_fmt'
            pattern_fmt_attr = 'pattern_fmt'
            Nothing = object()

            may_pattern_fmt_value = getattr(cls, pattern_fmt_attr, Nothing)
            may_x_pattern_fmt_value = getattr(cls, x_pattern_fmt_attr, may_pattern_fmt_value)
            if may_x_pattern_fmt_value is Nothing:
                raise Exception(f'requires: {x_pattern_attr!r} or {x_pattern_fmt_attr!r} or {pattern_fmt_attr!r}')
            x_pattern_fmt_value = may_x_pattern_fmt_value

            x_pattern_value = x_pattern_fmt_value.format(**x_pattern_dict)
            setattr(cls, x_pattern_attr, x_pattern_value)

        mayset_x_pattern('rough_pattern', rough_pattern_dict)
        mayset_x_pattern('precise_pattern', precise_pattern_dict)

        if not getattr(cls, 'no_wrap', False):
            def wrap(pattern):
                return f'(?:{pattern!s})'
            cls.rough_pattern = wrap(cls.rough_pattern)
            cls.precise_pattern = wrap(cls.precise_pattern)

        # though PLY itself will compile the __doc__
        #   I need precise_regex myself
        cls.rough_regex = regex_compile(cls.rough_pattern)
        cls.precise_regex = regex_compile(cls.precise_pattern)
        return

    @classmethod
    def to_flippable(cls):
        return Flippable(cls.rough_pattern, cls.precise_pattern)

PatternBase.regex_flags = regex_flags
PatternBase.regex_compile = staticmethod(regex_compile)

'''
usage:
Pattern = make_Pattern(globals())
class Pattern(PatternBase, rough_pattern_dict=None):
    def __init_subclass__(cls, **kwargs):
        # Map name Flippable(normal_string=rough_pattern, ...)
        rough_pattern_dict =\
            {pattern_name : pattern_cls.to_flippable()
            for pattern_name, pattern_cls in globals().items()
            if pattern_cls is not __class__
                and isinstance(pattern_cls, type)
                and issubclass(pattern_cls, __class__)
            }

        super().__init_subclass__(
            rough_pattern_dict=rough_pattern_dict
            , **kwargs)
'''
def make_Pattern(globals):
    # globals contain
    class Pattern(PatternBase, rough_pattern_dict=None):
        def __init_subclass__(cls, **kwargs):
            # Map name Flippable(normal_string=rough_pattern, ...)
            rough_pattern_dict =\
                {pattern_name : pattern_cls.to_flippable()
                for pattern_name, pattern_cls in globals.items()
                if pattern_cls is not __class__
                    and isinstance(pattern_cls, type)
                    and issubclass(pattern_cls, __class__)
                }

            super().__init_subclass__(
                rough_pattern_dict=rough_pattern_dict
                , **kwargs)
    return Pattern

class Pattern(PatternBase, rough_pattern_dict=None):
    def __init_subclass__(cls, *, globals, **kwargs):
        # Map name Flippable(normal_string=rough_pattern, ...)
        rough_pattern_dict =\
            {pattern_name : pattern_cls.to_flippable()
            for pattern_name, pattern_cls in globals.items()
            if pattern_cls is not __class__
                and isinstance(pattern_cls, type)
                and issubclass(pattern_cls, __class__)
            }

        super().__init_subclass__(
            rough_pattern_dict=rough_pattern_dict
            , **kwargs)

