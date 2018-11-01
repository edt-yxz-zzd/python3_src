
__all__ = '''
    make_rule_inject_to
    '''.split()

from seed.lang.has_no_nonlocals import has_no_nonlocals
import re

_make_rule_inject_to__name_regex = re.compile('(?P<indents>\s*)(?P<name>\w+)')
_make_rule_inject_to__bar_regex = re.compile(r'\|(?![\'"])')
def make_rule_inject_to(locals):
    '''
usage:
    see: PLY_YACC_Helper_YaccRules


    @let_be_all_staticmethod('p_')
    class PLY_YACC_Helper_YaccRules:
        '-> [(RuleName, [(RuleBody, [PythonLine])])]'
        start = 'Main'
        tokens = terminals

        def _(inject_to):
            @inject_to
            def p_(p):
                r'Main : Rules1 | Empty'
                p[0] = list(p[1])
            assert p_ is None
            assert p_Main
            ...
            ...
        _(make_rule_inject_to(locals())); del _

'''
    def decorator(f):
        if not callable(f): raise TypeError
        if not has_no_nonlocals(f): raise ValueError('should have no nonlocals; using kwargs to prevent locals: def f(..., *, a=..., ...)')
        __doc__ = f.__doc__
        m = _make_rule_inject_to__name_regex.match(__doc__)
        if not m: raise Exception('__doc__ should contain a name!!')
        suffix = m.group('name')
        func_name = f.__name__
        if not func_name.startswith('p_'):
            raise ValueError('func_name donot startswith "p_": {func_name}')
        func_name = f'{func_name}{suffix}'

        if func_name in locals:
            raise Exception(f'func_name already exists: {func_name!r}')
        f.__name__ = func_name
        locals[func_name] = f

        # '|' -> '\n    |'
        indents = m.group('indents')
        f.__doc__ = _make_rule_inject_to__bar_regex.sub(fr'\n{indents}    |', __doc__)
        if 0 and '|' in __doc__:
            print(f.__name__)
            print('\t', __doc__)
            print('\t', f.__doc__)

        return None
    return decorator


