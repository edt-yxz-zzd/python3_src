
from MatchPattern import *
class TempParser:
    def __init__(self):
        d = {'_NOSPACES_':MatchString,
             '_SPACES_BUT_NEWLINE_':MatchString,
             '_SPACES_':MatchString,
             'rex_language':MatchSequence,\
            'line':MatchSequence,\
            'id_define':MatchSequence,\
            'basic_rex':MatchChoices,\
            'item':MatchSequence,\
            'seq':MatchPlus,\
            'choices':MatchSequence,\
            'rex':MatchEq,\
            'multi':MatchChoices,\
            'multi_bound':MatchSequence,\
            'multi_star':MatchString,\
            'multi_plus':MatchString,\
            'multi_optional':MatchString,\
            'group':MatchSequence,\
            'str':MatchChoices,\
            'plain_str':MatchSequence,\
            'rex_str':MatchSequence,\
            'comment_str':MatchRex,\
            'id':MatchRex,\
            'num':MatchRex,\
            'NEWLINE':MatchString,\
            'BEGIN':MatchRex,\
            'END':MatchRex,\
            'FOLLOW':MatchChoices
             }

        o = {name:type.default_factory() for name, type in d.items()}

        a = {'_NOSPACES_': ((r'_NOSPACES_',), {'name':'_NOSPACES_'}),
             '_SPACES_BUT_NEWLINE_': ((r'_SPACES_BUT_NEWLINE_',), {'name':'_SPACES_BUT_NEWLINE_'}),
             '_SPACES_': ((r'_SPACES_',), {'name':'_SPACES_'}),
             'rex_language':(([o['BEGIN'], MatchStar(o['line']), o['END']],), {'name': 'rex_language'}),\
            'line':(([MatchOptional(o['id_define']), MatchOptional(o['comment_str']), o['NEWLINE']],), {'name': 'line'}),\
            'id_define':(([o['id'], MatchOptional(o['FOLLOW']), MatchString('='), o['rex']],), {'name': 'id_define'}),\
            'basic_rex':(([o['plain_str'], o['rex_str'], o['id'], o['group']],), {'name': 'basic_rex'}),\
            'item':(([o['basic_rex'], MatchOptional(o['multi'])],), {'name': 'item'}),\
            'seq':((o['item'],), {'name': 'seq'}),\
            'choices':(([o['seq'], MatchStar(MatchSequence([MatchString('|'), o['seq']]))],), {'name': 'choices'}),\
            'rex':((o['choices'],), {'name': 'rex'}),\
            'multi':(([o['multi_bound'], o['multi_star'], o['multi_plus'], o['multi_optional']],), {'name': 'multi'}),\
            'multi_bound':(([MatchString('{'), o['num'], MatchString(','), MatchOptional(o['num']), MatchString('}')],), {'name': 'multi_bound'}),\
            'multi_star':(('*',), {'name': 'multi_star'}),\
            'multi_plus':(('+',), {'name': 'multi_plus'}),\
            'multi_optional':(('?',), {'name': 'multi_optional'}),\
            'group':(([MatchString('('), o['rex'], MatchString(')')],), {'name': 'group'}),\
            'str':(([MatchRex(r"'(?!'')([^'\\]|\\.)*'"), MatchRex(r'"(?!"")([^"\\]|\\.)*"'), MatchRex("\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''"), MatchRex('\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""')],), {'name': 'str'}),\
            'plain_str':(([MatchRex('r?(?=[\'"])'), o['str']],), {'name': 'plain_str'}),\
            'rex_str':(([MatchRex('r?rex(?=[\'"])'), o['str']],), {'name': 'rex_str'}),\
            'comment_str':((r'#((?=[^\n]).)*',), {'name': 'comment_str'}),\
            'id':(('\\b(?=[^0-9])\\w+\\b(?=[^\'"])',), {'name': 'id'}),\
            'num':(('\\b[1-9])\\d*\\b(?=[^\'"])',), {'name': 'num'}),\
            'NEWLINE':(('\n',), {'name': 'NEWLINE'}),\
            'BEGIN':((r'^',), {'name': 'BEGIN'}),\
            'END':((r'$',), {'name': 'END'}),\
            'FOLLOW':(([MatchString('_NOSPACES_'), MatchString('_SPACES_BUT_NEWLINE_'), MatchString('_SPACES_'), o['rex_str']],), {'name': 'FOLLOW'})
             }

        assert len(o) == len(a)

        for name, obj in o.items():
            args, kwargs = a[name]
            obj.__init__(*args, **kwargs)

        self.lang = o
        return
    def parser(self, string):
        if not string.endswith('\n'):
            string = string + '\n'
        r = self.lang['rex_language'].match(string, 0, len(string))
        return r


from RexParser import RexParser, rex_language
from ParserResultWalk import ParserResultWalk

p = TempParser()
def parser2str_parser(parser):
    p = parser
    r = p.parser(rex_language)
    assert r != None
    r = ParserResultWalk().process(r, mainID='rex_language')
    str_parser, parser = r
    return str_parser

str_parser = parser2str_parser(TempParser())
assert str_parser == parser2str_parser(RexParser())
print(str_parser)










