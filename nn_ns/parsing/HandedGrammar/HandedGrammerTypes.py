

class Rule:pass
class ExplicitRule(Rule):pass
class ImplicitRule(Rule):pass

class AlternativeRule(ExplicitRule):pass
class ConcatenateRule(ExplicitRule):pass

class Tag:
    def __init__(self, qname, data):
        self.qname = qname
        self.data = data
        
class OrderedTag(Tag):pass
class UnorderedTag(Tag):pass


class IterativeTag(OrderedTag):pass
class FilterTag(OrderedTag):
    def __init__(self, name):
        super().__init__('>>' + name, name)
        
class BuiltinIterativeTag(IterativeTag):pass        
class UserIterativeTag(IterativeTag):
    def __init__(self, min, max):
        if max is None:
            qname = '[{},]'.format(min)
        else:
            qname = '[{},{}]'.format(min, max)

        min_max = (min, max)
        super().__init__(qname, min_max)

class OptionIterTag(BuiltinIterativeTag):
    def __init__(self):
        super().__init__('?', ('option', (0,1)))
class StarIterTag(BuiltinIterativeTag):
    def __init__(self):
        super().__init__('*', ('star', (0,None)))
class CrossIterTag(BuiltinIterativeTag):
    def __init__(self):
        super().__init__('+', ('cross', (1,None)))





class Required_SubtractMe:pass
class UserOptionTag(UnorderedTag):pass
class LocalOptionTag(UserOptionTag, Required_SubtractMe):
    # require: RuleID -self
    def __init__(self, name):
        assert type(name) is str
        assert name
        assert name[0] != '-'
        super().__init__('-' + name, name)
class Neg_GlobalOptionTag(Required_SubtractMe):
    def __init__(self, tag):
        assert isinstance(tag, GlobalOptionTag)
        self.tag = tag
        
class GlobalOptionTag(UserOptionTag):
    # require: RuleID --self
    def __init__(self, name):
        assert type(name) is str
        assert name
        assert name[0] != '-'
        super().__init__('--' + name, name)
    def __neg__(self):
        return Neg_GlobalOptionTag(self)








class OrRuleIDs:
    def __init__(self):
        self.IDs = []
    def __or__(self, rule_id):
        self.IDs.append(rule_id)
        return self
        raise NotImplementedError
class RuleID:
    def __init__(self, ID):
        self.__ID = ID
    @property
    def ID(self):
        return self.__ID
        raise NotImplementedError
    def __or__(self, other):
        return OrRuleIDs() | self | other
        raise NotImplementedError
        

    @property
    def x(self):
        '+'
        raise NotImplementedError
    @property
    def o(self):
        '*'
        raise NotImplementedError
    @property
    def z(self):
        '?'
        raise NotImplementedError

    def __mul__(self, int_or_list_of_len2_int_and_intORNone):
        raise NotImplementedError
    def __rshift__(self, filter):
        raise NotImplementedError
    def __sub__(self, obj_of_Required_SubtractMe):
        raise NotImplementedError
        
        
        
class PrimeRuleID(RuleID):pass
class PrimeNonterminal(PrimeRuleID):
    def define(self, rule_type, data):
        raise NotImplementedError
    def __getitem__(self, tuple_of_RuleID_or_Slice_attr_ID_None_fo_or_elem):
        # ConcatenateRule
        raise NotImplementedError
    def __call__(self, Null_or_RuleID_or_OrRuleIDs=()):
        # AlternativeRule
        raise NotImplementedError
        
        
        
class Terminal(PrimeRuleID):pass


class TaggedRuleID(RuleID):pass


