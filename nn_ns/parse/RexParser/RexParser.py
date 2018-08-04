
from MatchPattern import *

rex_language = r'''
rex_language = BEGIN line* END
line = id_define? comment_str? NEWLINE
id_define = id FOLLOW? '=' rex

basic_rex = plain_str | rex_str | id | group
item = basic_rex multi?
seq = item+
choices = seq ('|' seq)*
rex = choices

multi = multi_bound | multi_star | multi_plus | multi_optional
multi_bound = '{' num ',' num? '}'
multi_star = '*'
multi_plus = '+'
multi_optional = '?'
group = '(' rex ')'

str = rrex"'(?!'')([^'\\]|\\.)*'" | rrex'"(?!"")([^"\\]|\\.)*"' | rex"\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''" | rex'\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""' 
plain_str = rex'r?(?=[\'"])' str
rex_str = rex'r?rex(?=[\'"])' str
comment_str = rrex'#((?=[^\n]).)*'
id = rex'\\b(?=[^0-9])\\w+\\b(?=[^\'"])'
num = rex'\\b[1-9])\\d*\\b(?=[^\'"])'
NEWLINE = '\n'
BEGIN = rrex'^'
END = rrex'$'
FOLLOW = '_NOSPACES_' | '_SPACES_BUT_NEWLINE_' | '_SPACES_' | rex_str
# _SPACES_BUT_NEWLINE_(default) _SPACES_ _NOSPACES_ are all predefined
'''


class RexParser:
    def __init__(self):
        d = {'_NOSPACES_':MatchString,
             '_SPACES_BUT_NEWLINE_':MatchString,
             '_SPACES_':MatchString,
             'FOLLOW':MatchChoices, 'END':MatchRex, 'BEGIN':MatchRex,
             'NEWLINE':MatchString, 'num':MatchRex,
             'id':MatchRex, 'comment_str':MatchRex, 'rex_str':MatchSequence,
             'plain_str':MatchSequence, 'str':MatchChoices, 'group':MatchSequence,
             'multi_optional':MatchString, 'multi_plus':MatchString,
             'multi_star':MatchString, 'multi_bound':MatchSequence, 
             'multi':MatchChoices,
             'rex':MatchEq, 'choices':MatchSequence,
             'seq':MatchPlus, 'item':MatchSequence,
             'basic_rex':MatchChoices, 'id_define':MatchSequence, 'line':MatchSequence,
             'rex_language':MatchSequence,}

        o = {name:type.default_factory() for name, type in d.items()}

        a = {'_NOSPACES_':(r'_NOSPACES_',),
             '_SPACES_BUT_NEWLINE_':(r'_SPACES_BUT_NEWLINE_',),
             '_SPACES_':(r'_SPACES_',),
             'FOLLOW':([o['_NOSPACES_'], o['_SPACES_BUT_NEWLINE_'], o['_SPACES_'], o['rex_str']],),
             'END':(r'$',), 'BEGIN':(r'^',), 'NEWLINE':('\n',),
             'num':(r'\b[1-9])\d*\b' '(?=[^\'"])',),
             'id':(r'\b(?=[^0-9])\w+\b' '(?=[^\'"])',), 'comment_str':(r'#((?=[^\n]).)*',),
             'rex_str':([MatchRex('r?rex(?=[\'"])'), o['str']],),
             'plain_str':([MatchRex('r?(?=[\'"])'), o['str']],),
             'str':([MatchRex(r"'(?!'')([^'\\]|\\.)*'"), MatchRex(r'"(?!"")([^"\\]|\\.)*"'),
                     MatchRex("\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''"),
                     MatchRex('\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""')],),


             'group':([MatchString('('), o['rex'], MatchString(')'),],), 
             'multi_optional':('?',),

             'multi_plus':('+',),
             'multi_star':('*',),
             'multi_bound':([MatchString('{'), o['num'], MatchString(','),
                       MatchOptional(o['num']), MatchString('}'),],),
             'multi':([o['multi_bound'], o['multi_star'], o['multi_plus'], o['multi_optional']],),


             'rex':(o['choices'],),
             'choices':([o['seq'], MatchStar(MatchSequence([MatchString('|'), o['seq']]))],),
             'seq':(o['item'],),
             'item':([o['basic_rex'], MatchOptional(o['multi'])],),
             'basic_rex':([o['plain_str'], o['rex_str'], o['id'], o['group']],),
             'id_define':([o['id'], MatchOptional(o['FOLLOW']), MatchString('='), o['rex']],),
             
             'line':([MatchOptional(o['id_define']),
                      MatchOptional(o['comment_str']),
                      o['NEWLINE']],),
             'rex_language':([o['BEGIN'], MatchStar(o['line']), o['END']],),}

        assert len(o) == len(a)

        for name, obj in o.items():
            args = a[name]
            obj.__init__(*args, name=name)

        self.lang = o
        return
    def parser(self, string):
        if not string.endswith('\n'):
            string = string + '\n'
        r = self.lang['rex_language'].match(string, 0, len(string))
        return r
    

test_language4 = r'''
a = """a"""
b = \'''b\'''
c = """
"""
'''

test_language3 = r'''
a = 'a'
b = r'\n'
c = rex'\n'
d = rrex'\\'
'''
test_language2 = r'''
#a = 'a'
#b = r'\n'
#c = rex'\n'
#d = rrex'\\'
'''

test_language0 = '''
'''
test_language1 = '''
a = 'a'
'''

def test():
    p = RexParser()
    r = p.parser(test_language3)
    assert r != None
    p.parser(test_language4)
    assert r != None
    #print(r)
    r = p.parser(rex_language)
    assert r != None

        
