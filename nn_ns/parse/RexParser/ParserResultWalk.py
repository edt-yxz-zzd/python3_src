
from RexParser import RexParser, rex_language
from sand import replace_substrings


class ParserResultWalk:
    class Data:
        def __init__(self, constructor_name, args_str_ls):
            self.constructor_name = constructor_name
            self.args = args_str_ls
            return
        def toConstructStr(self, name=None, follow=None):
            args = self.getStrArgs(name, follow)
            return '{type}({args})'.format(type=self.constructor_name, args=args)
        
        def getStrArgs(self, name=None, follow=None):

            arg_ls = list(self.args)
            
            if name != None:
                last_arg = 'name={!r}'.format(name)
                arg_ls.append(last_arg)
            if follow != None:
                last_arg = 'follow={!r}'.format(follow)
                arg_ls.append(last_arg)
                
            args = ', '.join(arg_ls)
            return args
            
    class IDData(Data):
        def toDictMap(self):
            return 'o[{!r}]'.format(self.ID)
        def __init__(self, ID):
            self.constructor_name = 'MatchEq'
            self.ID = ID
            self.args = (self.toDictMap(),)
            return
        def toConstructStr(self, name=None, follow=None):
            if not name:
                return self.toDictMap()
            return super().toConstructStr(name=name, follow=follow)
        



    def _children2ConstructStrList(self, children):
        args = [c.data.toConstructStr() for c in children]
        arg0 = '[{}]'.format(', '.join(args))
        return arg0





    def process_rex_language(self, subtree):
        assert subtree.name == 'rex_language'

        ls = []
        lines = subtree[1]
        for lineNode in lines:
            self.process_line(lineNode)
            if lineNode.data != None:
                ls.append(lineNode.data)
        subtree.data = ls
        return
    
    def process_line(self, subtree):
        assert subtree.name == 'line'
        #print('here')

        id_defineNodeOpt = subtree[0]
        if len(id_defineNodeOpt.children):
            id_defineNode = id_defineNodeOpt.children[0]
            self.process_id_define(id_defineNode)
            subtree.data = id_defineNode.data
        else:
            subtree.data = None
        return


    def process_FOLLOW(self, subtree):
        assert subtree.name == 'FOLLOW'
        i = subtree.data
        if i == 0: #'_NOSPACES_'
            subtree.data = ''
        elif i == 1: #'_SPACES_BUT_NEWLINE_'
            subtree.data = None
        elif i == 2: #'_SPACES_'
            subtree.data = r'\s*'
        elif i == 3: #rex_str
            self.process_rex_str(subtree[i])
            subtree.data = eval(subtree[i].data)
        else:
            raise
        return
    
    def process_id_define(self, subtree):
        assert subtree.name == 'id_define'

        idNode, followNodeOpt, _, rexNode = subtree
        self.process_id(idNode)
        name = idNode.data.ID

        self.process_rex(rexNode)
        data = rexNode.data

        kwargs = {'name': name}
        if followNodeOpt.children:
            followNode = followNodeOpt[0]
            self.process_FOLLOW(followNode)
            follow = followNode.data
            #follow = eval(follow)
            kwargs['follow'] = follow
            assert type(follow) is str
        else:
            follow = None
            
        subtree.data = data, kwargs
        return

    def process_item(self, subtree):
        assert subtree.name == 'item'

        self.process_basic_rex(subtree[0])

        m = subtree[1].children
        if len(m):
            self.process_multi(m[0])
            data = m[0].data
            arg0 = subtree[0].data.toConstructStr()
            args1_ = data.args
            args = [arg0]
            args.extend(args1_)
            subtree.data = self.Data(data.constructor_name, args)
        else:
            subtree.data = subtree[0].data
        return
    
    def process_seq(self, subtree):
        assert subtree.name == 'seq'

        ls = []
        for child in subtree:
            ls.append(child)

        for c in ls:
            self.process_item(c)

        if 1 == len(ls):
            subtree.data = ls[0].data
        else:
            arg0 = self._children2ConstructStrList(ls)
            args = (arg0,)
            subtree.data = self.Data('MatchSequence', args)

        return
    
    def process_choices(self, subtree):
        assert subtree.name == 'choices'

        ls = [subtree[0]]
        for _, child in subtree[1]:
            ls.append(child)

        for c in ls:
            self.process_seq(c)

        if 1 == len(ls):
            subtree.data = ls[0].data
        else:
            arg0 = self._children2ConstructStrList(ls)
            args = (arg0,)
            subtree.data = self.Data('MatchChoices', args)

        return
    
    def process_rex(self, subtree):
        assert subtree.name == 'rex'
        self.process_choices(subtree[0])
        subtree.data = subtree[0].data
        return

    
    def process_multi_optional(self, subtree):
        assert subtree.name == 'multi_optional'
        subtree.data = self.Data('MatchOptional', ())
        return
    def process_multi_plus(self, subtree):
        assert subtree.name == 'multi_plus'
        subtree.data = self.Data('MatchPlus', ())
        return
    def process_multi_star(self, subtree):
        assert subtree.name == 'multi_star'
        subtree.data = self.Data('MatchStar', ())
        return
    def process_multi_bound(self, subtree):
        assert subtree.name == 'multi_bound'
        self.process_num(subtree[1])
        num1 = subtree[1].data

        args = [num1,]

        num2 = subtree[3].children
        if len(num2):
            self.process_num(num2[0])
            num2 = num2[0].data
            args.append(num2)

        args = tuple(str(n) for n in args)
        subtree.data = self.Data('MatchMulti', args)
        return
    
    def process_multi(self, subtree):
        assert subtree.name == 'multi'
        i = subtree.data
        if i == 0:
            self.process_multi_bound(subtree[i])
        elif i == 1:
            self.process_multi_star(subtree[i])
        elif i == 2:
            self.process_multi_plus(subtree[i])
        elif i == 3:
            self.process_multi_optional(subtree[i])
        else:
            raise
        subtree.data = subtree[i].data
        return


    def process_basic_rex(self, subtree):
        assert subtree.name == 'basic_rex'
        i = subtree.data
        if i == 0:
            self.process_plain_str(subtree[i])
        elif i == 1:
            self.process_rex_str(subtree[i])
        elif i == 2:
            self.process_id(subtree[i])
        elif i == 3:
            self.process_group(subtree[i])
        else:
            raise
        subtree.data = subtree[i].data
        return

    
    def process_group(self, subtree):
        assert subtree.name == 'group'

        self.process_rex(subtree[1])
        subtree.data = subtree[1].data
        return
    
    def process_num(self, subtree):
        assert subtree.name == 'num'

        s = self._getMatchedStr(subtree)
        assert s
        subtree.data = int(s)
        return
    
    def process_id(self, subtree):
        assert subtree.name == 'id'

        s = self._getMatchedStr(subtree)
        assert s
        subtree.data = self.IDData(s)
        return
    
    def process_comment_str(self, subtree):
        assert not 'call me'
        assert subtree.name == 'comment_str'

        s = self._getMatchedStr(subtree)
        assert s[0] == '#'
        subtree.data = s
        return

    def _getMatchedStr(self, subtree):
        strNode = subtree
        s = strNode.string[strNode.start : strNode.org_end]
        return s
    def process_str(self, subtree):
        assert subtree.name == 'str'

        i = subtree.data
        strNode = subtree[i]
        subtree.data = self._getMatchedStr(strNode)
        return
    
    def process_plain_str(self, subtree):
        assert subtree.name == 'plain_str'
        
        prefix = self._getMatchedStr(subtree[0])
        assert prefix in ['', 'r']

        self.process_str(subtree[1])

        s = prefix + subtree[1].data
        subtree.data = self.Data('MatchString', (s,))
        return

    def process_rex_str(self, subtree):
        assert subtree.name == 'rex_str'

        prefix = self._getMatchedStr(subtree[0])
        assert prefix in ['rex', 'rrex']
        prefix = prefix[:-3]

        self.process_str(subtree[1])

        s = prefix + subtree[1].data
        subtree.data = self.Data('MatchRex', (s,))
        return
    

    
    def process(self, parserResult, mainID, parsername='TempParser'):
        self.process_rex_language(parserResult)

        id2type = []
        id2type_tpl = '{!r}:{!s}'
        id2type_join = ',\\\n' + ' '*12
        for data, kwargs in parserResult.data:
            #print(data.toConstructStr(**kwargs))
            typename = data.constructor_name
            idname = kwargs['name']
            id2type.append(id2type_tpl.format(idname, typename))

        id2type = id2type_join.join(id2type)

        id2argskws = []
        id2argskws_tpl = '{idname!r}:(({str_args!s},), {kwargs!r})'
        id2argskws_join = ',\\\n' + ' '*12
        for data, kwargs in parserResult.data:
            str_args = data.getStrArgs()
            typename = data.constructor_name
            idname = kwargs['name']
            if idname == 'NEWLINE':
                #print(idname, repr(str_args))
                # note language = r''' r is important
                pass
            id2argskws.append(id2argskws_tpl.format(idname=idname, str_args=str_args, kwargs=kwargs))

        id2argskws = id2argskws_join.join(id2argskws)

        sub2rpl = {'<<parsername>>': parsername,
                   '<<id2type>>': id2type,
                   '<<id2argskws>>': id2argskws,
                   '<<repr_id_entry>>': repr(mainID),
                   }
        str_parser = replace_substrings(self.tpl, sub2rpl.items())

        #print(str_parser)
        exec(str_parser)
        parser = eval(parsername)
        #print(eval(parsername))
        
        return str_parser, parser

    tpl = r'''
from MatchPattern import *
class <<parsername>>:
    def __init__(self):
        d = {'_NOSPACES_':MatchString,
             '_SPACES_BUT_NEWLINE_':MatchString,
             '_SPACES_':MatchString,
             <<id2type>>
             }

        o = {name:type.default_factory() for name, type in d.items()}

        a = {'_NOSPACES_': ((r'_NOSPACES_',), {'name':'_NOSPACES_'}),
             '_SPACES_BUT_NEWLINE_': ((r'_SPACES_BUT_NEWLINE_',), {'name':'_SPACES_BUT_NEWLINE_'}),
             '_SPACES_': ((r'_SPACES_',), {'name':'_SPACES_'}),
             <<id2argskws>>
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
        r = self.lang[<<repr_id_entry>>].match(string, 0, len(string))
        return r
    
'''

def test():
    p = RexParser()
    r = p.parser(rex_language)
    r = ParserResultWalk().process(r, mainID='rex_language')
    str_parser, parser = r

    print(str_parser)
    newR = parser().parser(rex_language)
    assert newR != None
    newR = ParserResultWalk().process(newR, mainID='rex_language')
    new_str_parser, new_parser = newR

    assert new_str_parser == str_parser





