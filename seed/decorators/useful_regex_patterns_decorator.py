
r'''
see:
    decorators.format_docstring
'''


__all__ = '''
    UsefulRegexPatterns
    useful_regex_patterns_decorator

    useful_regex_patterns_dict
    '''.split()

from .format_docstring import format_docstring

class UsefulRegexPatterns:
    #NOTE: (?:...)
    #NOTE: fr'...'
    inline_space = r'(?:(?!\n)\s)'
    not_at_line_begin = r'(?<=[^\n])'
    at_line_begin = r'(?<![^\n])'
    not_at_line_end = r'(?=[^\n])'
    at_line_end = r'(?![^\n])'
    #newline = r'\n'
    ##################
    # not include spaces line
    non_indent_spaces1 = fr'(?:{not_at_line_begin}{inline_space}+)'
    spaces1_line = fr'(?:{at_line_begin}{inline_space}+{at_line_end})'

useful_regex_patterns_dict = UsefulRegexPatterns.__dict__
useful_regex_patterns_dict = {k : v
    for k,v in useful_regex_patterns_dict.items() if type(v) is str}
#assert all(type(v) is str for v in useful_regex_patterns_dict.values())

useful_regex_patterns_decorator = format_docstring(**useful_regex_patterns_dict)



