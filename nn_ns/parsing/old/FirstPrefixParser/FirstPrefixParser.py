
r'''
FirstPrefixParser<Grammar, {Symbol}>(name, [Symbol], begin, end) -> (end_, SyntaxTree) | Fail

for rule A -> B | C | D
    parse(G, A, [Symbol], begin, end) = parse(G, B, [Symbol], begin, end) if success else ...
for rule A -> B . C . D
    parse(G, A, [Symbol], begin, end) =
        endB, treeB = parse(G, B, [Symbol], begin, end)
        if success then
            parse(G, C, [Symbol], begin = end_, end)

Grammar =
    A -> (. B C D ...)
    A -> (| B C D ...)
    
    # NOTE: greedy
    # A -> B{min, max} 
    A -> B?
    A -> B*
    A -> B+

    
'''


from .FirstPrefixGrammar_FreeStyle import tokenize, std__ranged_sequence\
     _symbols, _tokens
from ..Type import *

rule_type__concat = '.'
rule_type__choose = '|'
rule_type__option = '?'
rule_type__star = '*'
rule_type__cross = '+'

    

class Rule:
    def __init__(self, leftpart, type, rightpart):
        self.leftpart = leftpart # nonterminal
        self.rule_type = type
        self.rightpart = rightpart # [nonterminal]

    def __repr__(self):
        return 'Rule({leftpart}, {type}, {rightpart})'\
               .format(leftpart=self.leftpart,
                       type=self.type,
                       rightpart=self.rightpart)

    def __eq__(self, other):
        return (self.leftpart == other.leftpart and
                self.type == other.type and
                self.rightpart == other.rightpart)
    def __ne__(self, other):
        return not self == other
    
               


class ConcatRule(Rule):
    def __init__(self, leftpart, rightpart):
        super().__init__(leftpart, rule_type__concat, list(rightpart))

        
class ChooseRule(Rule):
    def __init__(self, leftpart, rightpart):
        super().__init__(leftpart, rule_type__choose, list(rightpart))


class TaggedRule(Rule):
    def __init__(self, tagged_name, rule_type__tag, prime_name):
        super().__init__(tagged_name, rule_type__tag, [prime_name])
    

class OptionRule(TaggedRule):
    def __init__(self, tagged_name, prime_name):
        'example: OptionRule("A?", "A")'
        super().__init__(tagged_name, rule_type__option, prime_name)

class StarRule(TaggedRule):
    def __init__(self, tagged_name, prime_name):
        'example: StarRule("A*", "A")'
        super().__init__(tagged_name, rule_type__star, prime_name)

class CrossRule(TaggedRule):
    def __init__(self, tagged_name, prime_name):
        'example: CrossRule("A+", "A")'
        super().__init__(tagged_name, rule_type__cross, prime_name)

class Fail:
    def __init__(self, parsing_args, reason):
        self.parsing_args = parsing_args # name, symbols, begin, end
        self.reason = reason

def _iter_rules():
    _data = [
        'Grammar', ['Rule*'],
        'Rule', ['ConcatRule', 'ChooseRule'],
        'ConcatRule', ('DefiningName', "'='", 'CountedName*', "';'"),
        'ChooseRule', ('DefiningName', "'{'", 'CountedName*', "'}'"),
        'CountedName', ('Name', 'Count'),
        'Count', ["'?'", "'*'", "'+'", 'Null'],
        'Null', (),
        'DefiningName', ["'nonterminal'"],
        'Name', ["'nonterminal'", "'terminal'"],
        ]

    rightpart_type2RuleT = {tuple: ConcatRule, list: ChooseRule}
    for leftpart, rightpart in zip(_data[::2], _data[1::2]):
        RuleT = rightpart_type2RuleT[type(rightpart)]
        rule = RuleT(leftpart, rightpart)
        yield rule

rules__ThisGrammar__FreeStyle = list(_iter_rules())
class FirstPrefixParser:
    def __init__(self, grammar__rules):
        grammar__rules = tuple(grammar__rules)
        self.grammar__rules = grammar__rules
        #self.is_symbol = is_symbol
        self.nonterminal2rule = {rule.leftpart : rule for rule in grammar__rules}


        # if 'A = B* C' then add B* as a new nonterminal using StarRule
        def add_tagged_name(name):
            # tagged_name or prime_name
            tag2TaggedRuleT = {'?': OptionRule, '*': StarRule, '+': CrossRule}
            while self.is_tagged(name) and name not in self.nonterminal2rule:
                tag, prime_name = self.split_tagged_name(name)
                rule = tag2TaggedRuleT[tag](name, prime_name)
                self.nonterminal2rule[rule.leftpart] = rule

                name = prime_name

        for rule in list(self.nonterminal2rule.values()):
            #       ^^^^   since dict will be changed \
             
            for name in rule.rightpart:
                # tagged_name or prime_name
                add_tagged_name(name)

        

    def is_symbol(self, name):
        return len(name) >= 2 and name[0] == name[-1] == "'"
    def is_tagged(self, name):
        return name[-1] in "?*+"
    def split_tagged_name(self, name):
        '''return (tag, prime_name)

note:
    PrimeName??? ==>> (?, PrimeName??)
    PrimeName?? ==>> (?, PrimeName?)'''
        if self.is_tagged(name):
            return name[-1], name[:-1]
        return ('', name)
        
    
    def matched(self, parse_result):
        return not isinstance(parse_result, Fail)
    def parse(self, name, symbols, begin=None, end=None):
        symbols, begin, end = std__ranged_sequence(symbols, begin, end)
        parsing_args = name, symbols, begin, end
        
        if self.is_symbol(name):
            return self._parse_symbol(name, symbols, begin, end)
##        if self.is_tagged(name):
##            return self._parse_tagged_name(name, symbols, begin, end)


        rule = self.nonterminal2rule.get(name, None)
        if rule is None:
            return Fail(parsing_args, 'nonterminal was not defined')

        cls = type(self)
        rule_type2parse = {
            rule_type__concat : cls._parse__concat,
            rule_type__choose : cls._parse__choose,
            rule_type__option : cls._parse__option,
            rule_type__star : cls._parse__star,
            rule_type__cross: cls._parse__cross,}

        parse = rule_type2parse[rule.rule_type]
        r = parse(self, rule, name, symbols, begin, end)

        # is_parse_result
        #    Fail or (end', syntax_tree rooted by name)
        assert isinstance(r, Fail) or \
               (type(r) is tuple and len(r) == 2)

        return r

    def _parse_symbol(self, name, symbols, begin, end):
        parsing_args = name, symbols, begin, end
        if not begin < end:
            return Fail(parsing_args, 'end of stream')

        if symbols[begin] != name:
            return Fail(parsing_args, 'symbol not matched')
        
        return begin + 1, makeSyntaxTree__Symbol(name, symbols[begin])
##    def _parse_tagged_name(self, name, symbols, begin, end):
##        parsing_args = name, symbols, begin, end

        
    def _parse__choose(self, rule, name, symbols, begin, end):
        fails = []
        for alt_name in rule.rightpart:
            r = self.parse(alt_name, symbols, begin, end)
            if self.matched(r):
                end_, alt_tree = r
                return end_, makeSyntaxTree__Choose(name, alt_tree)
            fails.append(r)

        if fails:
            def get_begin(fail):
                name, symbols, begin, end = fail.parsing_args
                return begin
            return first_max(fails, key=get_begin)
        else:
            parsing_args = name, symbols, begin, end
            return Fail(parsing_args, 'no alternatives')
            

    def _parse__concat(self, rule, name, symbols, begin, end):
        subtrees = []
        for sub_name in rule.rightpart:
            r = self.parse(sub_name, symbols, begin, end)
            if not self.matched(r):
                return r
            end_, subtree = r
            subtrees.append(subtree)

            begin = end_

        return begin, makeSyntaxTree__Concat(name, subtrees)
            

    def _parse__option(self, rule, name, symbols, begin, end):
        return self._parse__count_min_max(0, 1,
                                          makeSyntaxTree__Option,
                                          rule, name, symbols, begin, end)

    def _parse__star(self, rule, name, symbols, begin, end):
        return self._parse__count_min_max(0, float('inf'),
                                          makeSyntaxTree__Star,
                                          rule, name, symbols, begin, end)

    def _parse__cross(self, rule, name, symbols, begin, end):
        return self._parse__count_min_max(1, float('inf'),
                                          makeSyntaxTree__Cross,
                                          rule, name, symbols, begin, end)

    def _parse__count_min_max(self, min, max, makeSyntaxTree__XXX,
                              rule, tagged_name, symbols, begin, end):
        org_name, = rule.rightpart
        subtrees = []
        r = None
        while len(subtrees) < max:
            r = self.parse(org_name, symbols, begin, end)
            if not self.matched(r):
                break
            end_, subtree = r
            subtrees.append(subtree)

            begin = end_

        if not min <= len(subtrees) <= max:
            parsing_args = tagged_name, symbols, begin, end
            return Fail(parsing_args, 'count not in range:[min..max]')
            

        return begin, makeSyntaxTree__XXX(tagged_name, org_name, subtrees)
            


free_style_grammar_parser = FirstPrefixParser(rules__ThisGrammar__FreeStyle)

end_, tree = free_style_grammar_parser.parse('Grammar', _symbols)
#print(end_, len(_symbols))
assert end_ == len(_symbols)

##from pprint import pprint
##pprint(tree)

class SyntaxTreeViewer:
    def __init__(self, tree):
        self.tree = tree
    def run(self):
        stack = [self.tree]
        while stack:
            top = stack[-1]
            
def syntax_tree2rules(tree):
    rules = []
    


