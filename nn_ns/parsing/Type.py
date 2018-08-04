
import collections # for namedtuple



class RuleType:
    ALT = 'AlternativeRule'
    CON = 'ConcatenateRule'
    ITE = 'IterativeRule'
    TAG = 'TaggedRule'
    all_types = {ALT, CON, ITE, TAG}



RuleBase = collections.namedtuple('RuleBase', 'rule_id, rule_type, rule_data'.split(', '))

class Rule(RuleBase):
    def __new__(cls, rule_id, rule_type, rule_data):
        assert rule_type in RuleType.all_types
        self = super(__class__, cls).__new__(cls, rule_id, rule_type, rule_data)
        hash(self)
        return self
    
##    def __repr__(self):
##        return 'Rule({rule_id!r}, {rule_type!r}, {rule_data!r})'\
##               .format(rule_id   = self.rule_id,
##                       rule_type = self.rule_type,
##                       rule_data = self.rule_data)
##    def __eq__


assert repr(Rule('A', RuleType.ALT, ('a', ''))) == "Rule(rule_id='A', rule_type='AlternativeRule', rule_data=('a', ''))"

def makeAlternativeRule(rule_id, alter_id_ls):
    rule_type = RuleType.ALT
    rule_data = tuple(alter_id_ls)
    return Rule(rule_id, rule_type, rule_data)
def makeConcatenateRule(rule_id, child_id_ls):
    rule_type = RuleType.CON
    rule_data = tuple(child_id_ls)
    return Rule(rule_id, rule_type, rule_data)
def makeIterativeRule(base_rule_id, min, max):
    # max == None stands for infinite
    rule_id = makeIterativeRuleID(base_rule_id, min, max)
    rule_type = RuleType.ITE
    rule_data = base_rule_id, min, max
    return Rule(rule_id, rule_type, rule_data)
def makeTaggedRule(rule_id, base_rule_id, tag):
    rule_type = RuleType.TAG
    rule_data = base_rule_id, tag
    return Rule(rule_id, rule_type, rule_data)
    
def makeCopyRule(rule_id, source_rule_id):
    return makeAlternativeRule(rule_id, [source_rule_id])

##class _MakeTaggedRule:
##    def __init__(self, tag):
##        self.tag = tag
##    def __call__(self, rule_id, base_rule_id):
##        return makeTaggedRule(rule_id, base_rule_id, self.tag)
##makeOptionRule, makeStarRule, makeCrossRule = map(_MakeTaggedRule, '?*+')

class ImplicitRuleIDType:
    U_ITE = 'UserIterative_OrderedTaggedRuleID' # basic_id [min..max]
    B_ITE = 'BuiltinIterative_OrderedTaggedRuleID' # basic_id *
    all_types = {U_ITE, B_ITE}

# (rule_type, base_rule_id, tag_or_data)
def makeIterativeRuleID(base_rule_id, min, max):
    return ImplicitRuleIDType.U_ITE, base_rule_id, (min, max)
def makeOptionRuleID(base_rule_id):
    return ImplicitRuleIDType.B_ITE, base_rule_id, '?'
def isImplicitRuleID(rule_id):
    return type(rule_id) is tuple and len(rule_id) == 3 and\
           rule_id[0] in ImplicitRuleIDType.all_types
def isBuiltinIterRuleID(rule_id):
    return isImplicitRuleID(rule_id) and rule_id[0] == ImplicitRuleIDType.B_ITE
def isOptionRuleID(rule_id):
    return isBuiltinIterRuleID(rule_id) and rule_id[-1] == '?'
def isOptionRule(rule):
    return isRule(rule) and isOptionRuleID(rule.rule_id)
def isRule(rule):
    return isinstance(rule, Rule)


# A -> B?
# B? -> B[0..1]
def makeOptionRule(base_rule_id):
    rule_id = makeOptionRuleID(base_rule_id)
    src_id = makeIterativeRuleID(base_rule_id, 0, 1)
    return makeCopyRule(rule_id, src_id)

class _MakeBuiltinIterRule:
    def __init__(self, min_max):
        self.min, self.max = min_max
    def __call__(self, base_rule_id):
        rule_id = makeOptionRuleID(base_rule_id)
        src_id = makeIterativeRuleID(base_rule_id, self.min, self.max)
        return makeCopyRule(rule_id, src_id)
        return makeTaggedRule(rule_id, base_rule_id, self.tag)
makeOptionRule, makeStarRule, makeCrossRule = map(_MakeBuiltinIterRule,
                                                  [(0, 1), (0, None), (1, None)])

# TODO: fixme, what about being a Rule method??
class RuleFuncs:
    @staticmethod
    def find_direct_depends(rule):
        # yield depended rule_id
        raise NotImplementedError
    
class TaggedRuleFuncs:
    @staticmethod
    def get_tag(tagged_rule):
        base_rule_id, tag = tagged_rule.rule_data
        return tag
    @staticmethod
    def get_base(tagged_rule):
        base_rule_id, tag = tagged_rule.rule_data
        return base_rule_id
    





