
'''
-- actually right part of rule
data CFG_Rule id = AltRule [id]
                 | ConRule [id]
                 | Terminal
data BinRule id = AltRule [id]
                | BinRule {fst::id, snd::id}
                | NullRule
                | Terminal

data Extended_Rule id = AltRule [id]
                      | ConRule [id]
                      | Terminal
                      | QuesRule id
                      | StarRule id
                      | CrossRule id

data InputID a = AltID a | ConID a | TerID a
-- 'A -> B C' ==>> 'A -> A[0] A[1]; A[0] -> B; A[1] -> C'
data ExInputID input_id = OrgID input_id
                        | ConChildID {con_id::input_id, child_idx::Integer}


-- 'A -> B | C' ==>> (A, 33, *) -> (B, 33, *) | (C, 33, *)
-- 'A -> B C' ==>> (A, 33, *_2) -> (A, 0, 33, *_1) (A, 1, *_1, *_2)
--                 (A, 0, 33, *_1) -> (B, 33, *_1)
--                 (A, 1, *_1, *_2) -> (C, *_1, *_2)
-- 'A -> ' ==>> '(A, 33, *) -> ' ==>> * == 33 ==>> (A, 33, 33)
-- 'a' ==>> (a, 33, *) -> (a, 33, 34) ==>> ??input[33] == a??
data WantedID input_id = WantedID {ex_id::ExInputID input_id,
                                   begin::TerminalStreamPos}

data OutputID input_id = OutputID {wtid::WantedID input_id, end::TerminalStreamPos}
# def: a output_id is a instance of wanted_id iff wtid output_id == wanted_id.

data FlatOutputID input_id = ConToAltID {input_id::input_id,
                                        child_begins::[TerminalStreamPos] # included last null child's begin
                                        }
                           | PlacedID {input_id::input_id,
                                       begin::TerminalStreamPos,
                                       end::TerminalStreamPos
                                       }

to_aware :: (ID -> ID) -> (ID -> ID)
to_aware unaware_transform (SelfDefinedID args ref_ids) = 
    SelfDefinedID args $ fmap . to_aware unaware_transform $ ref_ids
to_aware unaware_transform id = unaware_transform id

data SelfDefinedID args ref_ids = SelfDefinedID args ref_ids
class Functor ref_ids => Functor (SelfDefinedID args) where
    fmap unaware_transform ID = to_aware unaware_transform ID


input a terminal T
    assert T is a terminal
    if T not in expects: fail

    for wtid in expect2wantings[T]:
        handle(wtid, T)
'''


__all__ = '''
    ID
        InputID
        ExInputID
            OrgID
            ConChildID
        WantedID
        OutputID
        
        FlatOutputID
            ConToAltID
                AllConChildrenInstancesID
            PlacedID
    Rule
        AltRule
        ConRule
        Terminal
        
    null_rule
    ter_rule
    dead_rule

    SelfDefinedIDAwareTransform
    SelfDefinedID
        ConRuleID
        AltRuleID
            null_rule_id
            dead_rule_id
        
        NonExternID
        ExternID
            ExternSelfDefinedID
        
        
        QuesRuleID
        StarRuleID
        CrossRuleID
            _QuesRuleID
            _StarRuleID
            _CrossRuleID

'''.split()

# NullRuleID, DeadRuleID are exported for repr of null_rule_id, dead_rule_id


from sand.types.Newtype import Newtype, NewtypeWithMultiArgs
from sand.types.Functor import Functor



# ------------  IDTypes  -----------
        
class ID(Newtype):pass
class InputID(ID):pass
class ExInputID(ID):pass
class OrgID(ExInputID):
    def __init__(self, input_id):
        assert isinstance(input_id, InputID)
        super().__init__(input_id)
    @property
    def input_id(self):
        return self.unbox()
class ConChildID(NewtypeWithMultiArgs, ExInputID):
    def __init__(self, con_id, child_idx):
        assert isinstance(con_id, InputID)
        assert isinstance(child_idx, int)
        super().__init__(con_id, child_idx)

    @property
    def input_id(self):
        return self.unbox()[0]
    @property
    def child_idx(self):
        return self.unbox()[1]
    def is_first_child(self):
        return self.child_idx == 0

class WantedID(NewtypeWithMultiArgs, ID):
    def __init__(self, ex_id, begin):
        assert isinstance(ex_id, ExInputID)
        assert isinstance(begin, int)
        super().__init__(ex_id, begin)

    @property
    def ex_id(self):
        return self.unbox()[0]
    @property
    def begin(self):
        return self.unbox()[1]

class ResultID(ID):pass

# for wanted instance
class OutputID(NewtypeWithMultiArgs, ResultID):
    # self is a 'instance' of self.wanted_id # not in python meanings
    def __init__(self, wanted_id, end):
        assert isinstance(wanted_id, WantedID)
        assert isinstance(end, int)
        super().__init__(wanted_id, end)

    @property
    def wanted_id(self):
        return self.unbox()[0]
    @property
    def end(self):
        return self.unbox()[1]





# for output grammar
class FlatOutputID(ResultID):pass

class ConToAltID(NewtypeWithMultiArgs, FlatOutputID):
    def __init__(self, input_id, child_begins):
        child_begins = tuple(child_begins)
        assert isinstance(input_id, InputID)
        assert all(isinstance(b, int) for b in child_begins)
        super().__init__(input_id, child_begins)

    @property
    def input_id(self):
        return self.unbox()[0]
    @property
    def child_begins(self):
        return self.unbox()[1]
AllConChildrenInstancesID = ConToAltID

class PlacedID(NewtypeWithMultiArgs, FlatOutputID):
    # self is a 'instance' of self.wanted_id # not in python meanings
    def __init__(self, input_id, begin, end):
        assert isinstance(input_id, InputID)
        assert isinstance(begin, int)
        assert isinstance(end, int)
        super().__init__(input_id, begin, end)

    @property
    def input_id(self):
        return self.unbox()[0]
    @property
    def begin(self):
        return self.unbox()[1]
    @property
    def end(self):
        return self.unbox()[2]
    




# ------------  RuleTypes  -----------

##class Alts(frozenset):pass
##class Children(tuple):pass
##assert repr(Children([]))== '()'
##assert repr(Alts([])) == 'Alts()'
##assert repr(Alts([1])) == 'Alts({1})'
##raise

class Rule(Newtype, Functor):
    'Functor Rule; fmap (id0 -> id1) -> Rule id0 -> Rule id1'
    pass

class AltRule(Rule):
    def __init__(self, IDs):
        super().__init__(frozenset(IDs))
    @property
    def alts(self):
        return self.unbox()

    def is_dead(self):
        return not self.alts
    
    def flip_fmap(self, transform):
        return type(self)(map(transform, self.alts))

class ConRule(Rule):
    def __init__(self, IDs):
        super().__init__(tuple(IDs))
    @property
    def children(self):
        return self.unbox()
    def is_null(self):
        return not self.children
    
    def flip_fmap(self, transform):
        return type(self)(map(transform, self.children))

TupleRule = ConRule
UnionRule = AltRule
    



class NoArgsReprTag:
    def __repr__(self):
        return '{}()'.format(type(self).__name__)
class ThisClassRule(NoArgsReprTag, Rule):
    def __init__(self):
        super().__init__(type(self))
    


# not a real rule, but to mark the rule_id as a terminal
class Terminal(ThisClassRule):
    def flip_fmap(self, transform):
        'immutable'
        return self


def makeNullRule():
    return ConRule([])
def makeDeadRule():
    'for undefined rule or no-alts alt rule'
    return AltRule([])
def makeCopyRule(src_id):
    'for rule in form of "TARGET -> SRC;".'
    return AltRule([src_id])
null_rule = makeNullRule()
ter_rule = Terminal()
dead_rule = makeDeadRule()
assert ter_rule.unbox() is type(ter_rule)







#------------------ SelfDefinedID ----------------

class SelfDefinedIDAwareTransform:
    def __init__(self, unaware_transform):
        self.__t = unaware_transform
    def __call__(self, ID):
        if isinstance(ID, SelfDefinedID):
            return fmap(self, ID)
        else:
            return self.__t(ID)

class SelfDefinedID(NewtypeWithMultiArgs, ID, Functor):
    '''using rule as ID;

know how to make up rule instead of holding the rule to avoid infinite recur

if aSelfDefinedID not in id2rule:
    then ==>> as-if id2rule[aSelfDefinedID] == aSelfDefinedID.make_rule()

else:
    assert id2rule[aSelfDefinedID] == aSelfDefinedID.make_rule()


def id_transform__aware_SelfDefinedID(id):
    if isinstance(id, SelfDefinedID):
        return fmap(id_transform__aware_SelfDefinedID, id)
    else:
        return id_transform__unaware_SelfDefinedID(id)
        
assert fmap(id_transform__aware_SelfDefinedID, self_defined_id).make_rule() ==\
       fmap(id_transform__aware_SelfDefinedID, self_defined_id.make_rule())
'''
    def __init__(self, *args):
        'args should be immutable object'
        super().__init__(*args)
    @property
    def rule_args(self):
        return self.unbox()
    def make_rule(self):
        raise NotImplementedError
    def flip_fmap(self, transform):
        if not isinstance(transform, SelfDefinedIDAwareTransform):
            # raise TypeError('should use SelfDefinedIDAwareTransform')
            transform = SelfDefinedIDAwareTransform(transform)
        return self._flip_fmap(transform)
    def _flip_fmap(self, aware_transform):
        raise NotImplementedError
    

class ConRuleID(SelfDefinedID):
    def __init__(self, IDs):
        super().__init__(tuple(IDs))
    
    def get_children(self):
        return self.rule_args[0]
    def make_rule(self):
        return ConRule(self.get_children())
    def _flip_fmap(self, transform):
        return type(self)(map(transform, self.get_children()))
class AltRuleID(SelfDefinedID):
    def __init__(self, IDs):
        super().__init__(frozenset(IDs))
        
    def get_alts(self):
        return self.rule_args[0]
    def make_rule(self):
        return AltRule(self.get_alts())
    def _flip_fmap(self, transform):
        return type(self)(map(transform, self.get_alts()))

def makeNullRuleID():
    return ConRuleID([])
def makeDeadRuleID():
    return AltRuleID([])
null_rule_id = makeNullRuleID()
dead_rule_id = makeDeadRuleID()

class SelfDefinedID_WithOneRefIDArgs(SelfDefinedID):
    def __init__(self, ref_id, *args):
        assert isinstance(ref_id, ID)
        super().__init__(ref_id, *args)
    @property
    def ref_id(self):
        return self.rule_args[0]
    def _flip_fmap(self, transform):
        'immutable'
        return type(self)(transform(self.ref_id), *self.rule_args[1:])
    
##class SelfDefinedID_WithOneRefIDOnly(SelfDefinedID_WithOneRefIDArgs):
##    def __init__(self, ref_id):
##        super().__init__(ref_id)
class RepeatRuleID(SelfDefinedID_WithOneRefIDArgs):pass
class RepeatRuleID_WithOneRefIDOnly(RepeatRuleID):
    def __init__(self, ref_id):
        super().__init__(ref_id)




class ExternID(ID):
    'exists in final AST'
    pass
class NonExternID(ID):
    'not exists in final AST'
    pass
class ExternSelfDefinedID(SelfDefinedID, ExternID):
    'exists in final AST'
    # __SelfDefinedID_ImplType__ = ??
    def make_rule(self):
        'A_stab { A_impl }'
        args = self.rule_args
        return makeCopyRule(type(self).__SelfDefinedID_ImplType__(*args))
    pass

class _QuesRuleID(RepeatRuleID_WithOneRefIDOnly, NonExternID):
    def make_rule(self):
        'A? { A Null }'
        A = self.ref_id
        return AltRule([A, null_rule_id])
class _StarRuleID(RepeatRuleID_WithOneRefIDOnly, NonExternID):
    def make_rule(self):
        'A* { A+ Null }'
        A = self.ref_id
        return AltRule([_CrossRuleID(A), null_rule_id])
class _CrossRuleID(RepeatRuleID_WithOneRefIDOnly, NonExternID):
    def make_rule(self):
        'A+ = A A* ;'
        A = self.ref_id
        return ConRule([A, _StarRuleID(A)])


class ExternRepeatRuleID_WithOneRefIDOnly(RepeatRuleID_WithOneRefIDOnly, ExternSelfDefinedID):
    # __SelfDefinedID_ImplType__ = ??
    pass
    
class QuesRuleID(ExternRepeatRuleID_WithOneRefIDOnly):
    __SelfDefinedID_ImplType__ = _QuesRuleID
class StarRuleID(ExternRepeatRuleID_WithOneRefIDOnly):
    __SelfDefinedID_ImplType__ = _StarRuleID
class CrossRuleID(ExternRepeatRuleID_WithOneRefIDOnly):
    __SelfDefinedID_ImplType__ = _CrossRuleID

A_plus = CrossRuleID(ID('A'))
#print(A_plus, A_plus.make_rule())
assert A_plus == CrossRuleID(ID('A'))
assert A_plus.make_rule() == AltRule(frozenset({_CrossRuleID(ID('A'))}))
assert repr(A_plus) == "CrossRuleID(ID('A'))"
assert repr(A_plus.make_rule()) == "AltRule(frozenset({_CrossRuleID(ID('A'))}))"




'''
def is_uint(i):
    return isinstance(i, int) and i >= 0
def check_int(i):
    if not isinstance(i, int):
        raise TypeError('not int')
def check_uint(i):
    check_int(i)
    if i < 0:
        raise ValueError('not uint')
    
class ArrayRuleID(SelfDefinedID_WithOneRefIDArgs):
    def __init__(self, ref_id, length):
        check_int(length)
        super().__init__(ref_id, length)
    @property
    def length(self):
        return self.rule_args[1]
    def make_rule(self):
        'A[L+1] = A A[L] ; A[0] { Null }'
        A = self.ref_id
        L = self.length
        if L == 0:
            return null_rule
        elif L > 0:
            return ConRule([A, ArrayRuleID(A, L-1)])
        else:
            return dead_rule

class ArrayMaxRuleID(SelfDefinedID_WithOneRefIDArgs):
    def __init__(self, ref_id, max_length):
        check_int(max_length)
        super().__init__(ref_id, max_length)
    @property
    def max_length(self):
        return self.rule_args[1]
    def make_rule(self):
        'A[0..L+1] { A[L+1] A[0..L]} A[0..0] { Null }'
        A = self.ref_id
        L = self.max_length
        if L == 0:
            return null_rule
        elif L > 0:
            return AltRule([ArrayRuleID(A, L), ArrayMaxRuleID(A, L-1)])
        else:
            return dead_rule
        
class ArrayMinRuleID(SelfDefinedID_WithOneRefIDArgs):
    def __init__(self, ref_id, min_length):
        check_int(min_length)
        super().__init__(ref_id, min_length)
    @property
    def min_length(self):
        return self.rule_args[1]
    def make_rule(self):
        'L>=0: A[L..] = A[L] A* ;'
        A = self.ref_id
        L = max(0, self.min_length)
        return ConRule([ArrayRuleID(A, L), StarRuleID(A)])
        
class ArrayMinMaxRuleID(SelfDefinedID_WithOneRefIDArgs):
    def __init__(self, ref_id, min_length, max_length):
        check_int(min_length)
        check_int(max_length)
##        if min_length > max_length:
##            raise ValueError()
        super().__init__(ref_id, min_length, max_length)
    @property
    def min_length(self):
        return self.rule_args[1]
    @property
    def max_length(self):
        return self.rule_args[2]
    def make_rule(self):
        'L>=0: A[L..U] = A[L] A[0..U-L] ;' # even for L>U
        A = self.ref_id
        L = max(0, self.min_length)
        U = self.max_length
##        if L > U:
##            return dead_rule
        return ConRule([ArrayRuleID(A, L), ArrayMaxRuleID(A, U-L)])

        
'''





    
