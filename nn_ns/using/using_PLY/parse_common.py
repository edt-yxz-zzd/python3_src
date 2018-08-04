

__all__ = '''
    leftward_list2list
    iter_leftward_list
    set_default_attr
    set_defaultfactory_attr

    
    make_parser
    parse
    
    handle_alt_rule
    p_Null
    p_error

    set_PLY_star_doc
    set_PLY_cross_doc
    set_PLY_option_doc
    set_PLY_optioncross_doc


'''.split()

from .lex_common import nonstr_or___name__2nonstr_or_module, make_lexer, \
     token2lineno_column, token2lexpos_total
from seed.excepts.sand_excepts import ParseError, CompileError
from seed.types.pair_based_leftward_list import iter_leftward_list, leftward_list2list

'LeftwardList a = () | (a, LeftwardList a)'


def set_default_attr(obj, name, default=None):
    '''
if not hasattr:
    setattr
return getattr
'''
    if not hasattr(obj, name):
        setattr(obj, name, default)
    return getattr(obj, name)

def set_defaultfactory_attr(obj, name, factory=None):
    '''
if not hasattr:
    setattr factory()
return getattr
'''
    if not hasattr(obj, name):
        setattr(obj, name, None if factory is None else factory())
    return getattr(obj, name)
    
class ToStarCrossOptionRuleMixin:
    def basic2star_id(self, basic):
        return self.star_id_fmt.format(Basic=basic, Star=self.Star)
    def basic2cross_id(self, basic):
        return self.cross_id_fmt.format(Basic=basic, Cross=self.Cross)
    def basic2option_id(self, basic):
        return self.option_id_fmt.format(Basic=basic, Option=self.Option)

    def basic2star_rule(self, basic):
        return self.star_rule_fmt.format(
            StarBasic = self.basic2star_id(basic),
            OptionCrossBasic = self.basic2option_id(self.basic2cross_id(basic))
            )
    def basic2cross_rule(self, basic):
        return self.cross_rule_fmt.format(
            CrossBasic = self.basic2cross_id(basic),
            Basic = basic,
            StarBasic = self.basic2star_id(basic)
            )
    def basic2option_rule(self, basic):
        return self.option_rule_fmt.format(
            OptionBasic = self.basic2option_id(basic),
            Basic = basic,
            Null = self.Null
            )

    def basic2optioncross_rule(self, basic):
        cross_basic = self.basic2cross_id(basic)
        return self.basic2option_rule(cross_basic)
    def basics2rules(self, basics, basic2rule, joiner='\n'):
        return joiner.join(map(basic2rule, basics))
    def basics2star_rules(self, basics, joiner='\n'):
        return self.basics2rules(basics, self.basic2star_rule, joiner=joiner)
    def basics2cross_rules(self, basics, joiner='\n'):
        return self.basics2rules(basics, self.basic2cross_rule, joiner=joiner)
    def basics2option_rules(self, basics, joiner='\n'):
        return self.basics2rules(basics, self.basic2option_rule, joiner=joiner)
    def basics2optioncross_rules(self, basics, joiner='\n'):
        return self.basics2rules(basics, self.basic2optioncross_rule, joiner=joiner)
        
    

class ToStarCrossOptionRule__PLY(ToStarCrossOptionRuleMixin):
    star_rule_fmt = '{StarBasic} : {OptionCrossBasic}'
    cross_rule_fmt = '{CrossBasic} : {Basic} {StarBasic}'
    option_rule_fmt = '{OptionBasic} : {Basic}\n\t| {Null}'
    star_id_fmt = '{Basic}{Star}'
    cross_id_fmt = '{Basic}{Cross}'
    option_id_fmt = '{Basic}{Option}'
    def __init__(self, Star='Star', Cross='Cross', Option='Option', Null = 'Null'):
        self.Star = Star
        self.Cross = Cross
        self.Option = Option
        self.Null = Null

class SetDoc:
    def __init__(self, doc):
        self.doc = doc
    def __call__(self, func):
        func.__doc__ = self.doc
        return func
class SetDocFrom:
    def __init__(self, to_doc):
        self.to_doc = to_doc
    def __call__(self, x):
        return SetDoc(self.to_doc(x))
    


def make_parser(yacc_module):
    from ply.yacc import yacc
    yacc_module = nonstr_or___name__2nonstr_or_module(yacc_module)
    parser = yacc(module = yacc_module)
    return parser

def parse(lex_module, yacc_module, source):
    lexer = make_lexer(lex_module)
    parser = make_parser(yacc_module)
    return parser.parse(source, lexer=lexer)














def handle_alt_rule(p):
    p[0] = p[1]
def p_Null(p):
    'Null : '
    p[0] = ()
def p_error(token):
    if token is None:
        raise ParseError('end-of-file')

    lineno, column = token2lineno_column(token)
    lexpos, total = token2lexpos_total(token)
    raise ParseError('fail at line:{}, column:{}, lexpos:{}, total:{}, token:{}'
                     .format(lineno, column, lexpos, total, token))



to_SCO = ToStarCrossOptionRule__PLY()
set_PLY_star_doc = SetDocFrom(to_SCO.basics2star_rules)
set_PLY_cross_doc = SetDocFrom(to_SCO.basics2cross_rules)
set_PLY_option_doc = SetDocFrom(to_SCO.basics2option_rules)
set_PLY_optioncross_doc = SetDocFrom(to_SCO.basics2optioncross_rules)





