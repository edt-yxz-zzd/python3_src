
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

rule_fmap
id2rule_fmap
    box_id2rule
        box_id
        box_rule
    unbox_id2rule
        unbox_id
        unbox_rule

is_unambiguous_result
    classify_FlatOutputIDs_by_IDType_and_RuleType
    collect_undefined_IDs
unambiguous_flat_result2tree
    simplify_unambiguous_flat_result
    maybe_parent2children_to_child2parent

inplace_clean
    cleaned
    find_out_reachables

    calc_id2min_len
        find_out_nullables
        find_out_unproductives

        classify_IDs_by_RuleType
'''.split()
##find_out_keys_to_value
##reserve_keys
##remove_keys

from sand.types.Newtype import Newtype, NewtypeWithMultiArgs
from sand.types.Functor import Functor, fmap

from .ParseResultAST import ConRuleNode, AltRuleNode, TerminalNode


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



##class AllConChildrenInstancesID(NewtypeWithMultiArgs, ID):
##    def __init__(self, con_id, children_begins):
##        assert isinstance(con_id, InputID)
##        children_begins = tuple(children_begins)
##        assert all(isinstance(begin, int) for begin in children_begins)
##        super().__init__(con_id, children_begins)
##
##    @property
##    def parent_input_id(self):
##        return self.unbox()[0]
##    @property
##    def children_begins(self):
##        return self.unbox()[1]



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
    
##class BinConRule(ConRule):
##    def __init__(self, first_ID, second_ID):
##        super().__init__([first_ID, second_ID])
##    @property
##    def fst(self):
##        return self.children[0]
##    @property
##    def snd(self):
##        return self.children[1]
##
##    def __repr__(self):
##        return '{}{}'.format(type(self).__name__, self.children)

class NoArgsRuleTag:
    def __repr__(self):
        return '{}()'.format(type(self).__name__)
class ThisClassRule(NoArgsRuleTag, Rule):
    def __init__(self):
        super().__init__(type(self))
    
##class NullConRule(NoArgsRuleTag, ConRule):
##    def __init__(self):
##        ConRule.__init__(self, [])

# not a real rule, but to mark the rule_id as a terminal
class Terminal(ThisClassRule):
    def flip_fmap(self, transform):
        'immutable'
        return self

#class DeadRule(ThisClassRule):pass

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





# ------------  ExtendedRuleTypes  -----------

class ExtendedRuleABC(metaclass = ABCMeta):pass
class ExtendedIterRule(Rule):
    @property
    def ref_id(self):
        return self.unbox()
    def flip_fmap(self, transform):
        return type(self)(transform(self.ref_id))
    
class QuesRule(ExtendedIterRule):pass
class StarRule(ExtendedIterRule):pass
class CrossRule(ExtendedIterRule):pass












    












################### util ###########################

def rule_fmap(id_transform, rule):
    assert isinstance(rule, Rule)
    return fmap(id_transform, rule)

    if isinstance(rule, AltRule):
        return AltRule(map(id_transform, rule.alts))
    elif isinstance(rule, ConRule):
        return ConRule(map(id_transform, rule.children))
    elif isinstance(rule, Terminal):
        return rule
    else:
        raise logic-error
    

def id2rule_fmap(id_transform, id2rule):
    return {id_transform(ID): rule_fmap(id_transform, rule)
            for ID, rule in id2rule.items()}

default_box_id = InputID
def box_id(unboxed_id):
    return default_box_id(unboxed_id)

def box_rule(self, unboxed_rule, box_id=default_box_id):
    if box_id is None:
        box_id = default_box_id
    return rule_fmap(box_id, unboxed_rule)
def box_id2rule(unboxed_id2rule, box_id=default_box_id):
    if box_id is None:
        box_id = default_box_id
    return id2rule_fmap(box_id, unboxed_id2rule)

def unbox_id(boxed_id):
    assert isinstance(boxed_id, default_box_id)
    return boxed_id.unbox()
default_unbox_id = unbox_id
def unbox_rule(self, boxed_rule, unbox_id=default_unbox_id):
    if unbox_id is None:
        unbox_id = default_unbox_id
    return rule_fmap(unbox_id, boxed_rule)
def unbox_id2rule(boxed_id2rule, unbox_id=default_unbox_id):
    if unbox_id is None:
        unbox_id = default_unbox_id
    return id2rule_fmap(unbox_id, boxed_id2rule)



################### algo ###############################

inf = float('inf')
assert (inf == inf) == True
assert (inf <= inf) == True
assert (inf >= inf) == True
assert (inf != inf) == False
assert (inf < inf) == False
assert (inf > inf) == False


def min0(iterable, *, key=None, start=inf):
    ls = tuple(iterable)
    if not ls:
        return start
    return min(ls, key=key)

def is_unambiguous_result(cleaned_result_id2rule):
    id2rule = cleaned_result_id2rule
    assert all(isinstance(ID, ResultID) for ID in id2rule)
    
    # classify IDs by RuleType
    (_, (non_dead2alts, deads), _),\
           (alls, _, undefineds) = \
           classify_IDs_by_RuleType(id2rule)

    if not all(isinstance(ID, ResultID) for ID in alls):
        raise TypeError('not all ResultID')
    if deads or undefineds:
        raise ValueError('exists deads/undefineds: not cleaned')
    
    for ID, alts in non_dead2alts.items():
        if len(alts) > 1:
            return False
    return True


def maybe_parent2children_to_child2parent(maybe_parent2children):
    '''
maybe_parent2children[x] is None ==>> x is leaf
x in maybe_parent2children and x not in child2parent[x] ==>> x is root

'''
    child2parent = {}
    for maybe_parent, maybe_children in maybe_parent2children.items():
        if maybe_children is None:
            # maybe_parent is not a parent
            continue
        
        parent, children = maybe_parent, maybe_children
        for child in children:
            if child not in maybe_parent2children:
                #print(child)
                raise ValueError('undefined child found, i.e. child not in maybe_parent2children')
            if child in child2parent:
                raise ValueError('multi parents found')
            child2parent[child] = parent
            
    num_roots = len(maybe_parent2children) - len(child2parent)
    if num_roots != 1:
        raise logic-error
    #root, = set(maybe_parent2children) - set(child2parent)
    
    return child2parent

ConRuleNode, AltRuleNode, TerminalNode
def unambiguous_flat_result2tree(unambiguous_cleaned_flat_result_id2rule):
    tree, *_ = unambiguous_flat_result2tree_ex(unambiguous_cleaned_flat_result_id2rule)
    return tree
def unambiguous_flat_result2tree_ex(unambiguous_cleaned_flat_result_id2rule):
    maybe_parent2children = simplify_unambiguous_flat_result(unambiguous_cleaned_flat_result_id2rule)
    child2parent = maybe_parent2children_to_child2parent(maybe_parent2children)
    root, = set(maybe_parent2children) - set(child2parent)

    maybe_parent_stack = [root]
    unvisited_children_stack = []
    id2subtree = {}
        
    while maybe_parent_stack:
        if len(maybe_parent_stack) == len(unvisited_children_stack) + 1:
            maybe_parent = maybe_parent_stack[-1]
            maybe_children = maybe_parent2children[maybe_parent]
            if maybe_children is None:
                leaf = maybe_parent_stack.pop()
                #id2subtree[leaf] = (leaf, None) # children of leaf is None
                id2subtree[leaf] = TerminalNode(leaf)
                continue

            children = maybe_children
            unvisited_children_stack.append(iter(children))
            continue
        elif len(maybe_parent_stack) != len(unvisited_children_stack):
            raise logic-error

        for child in unvisited_children_stack[-1]:
            assert child not in id2subtree
            maybe_parent_stack.append(child)
            break
        else:
            # no child
            unvisited_children_stack.pop()
            parent = maybe_parent_stack.pop()
            children = maybe_parent2children[parent]
            subtrees = type(children)(map(id2subtree.__getitem__, children))
            #id2subtree[parent] = (parent, subtrees)
            Node = ConRuleNode if type(children) is tuple else AltRuleNode
            id2subtree[parent] = Node(parent, subtrees)
            continue

    tree = id2subtree[root]
    return tree, id2subtree, (root, maybe_parent2children, child2parent)

def simplify_unambiguous_flat_result(unambiguous_cleaned_flat_result_id2rule,
                                     alts2rule=frozenset,
                                     children2rule=tuple,
                                     ter_rule=None):
    '''will remove Con2Alt ID;
Placed Con ID will point to con rule instead of copy rule
result should be a tree since unambiguous_cleaned

alt_ID -> frozenset([the_only_alt])
con2alt_ID -> tuple(children)
terminal -> None
'''
    id2rule = unambiguous_cleaned_flat_result_id2rule
    if not is_unambiguous_result(id2rule):
        raise ValueError('ambiguous')

    ((placed_con_ids, placed_alt_ids), con2alt_ids), terminals, (undefineds, deads) = \
                      classify_FlatOutputIDs_by_IDType_and_RuleType(id2rule)
    assert not undefineds
    assert not deads
    

    parent2children = dict.fromkeys(terminals, ter_rule)
    for ID in placed_con_ids:
        rule = id2rule[ID]
        alt, = rule.alts
        if alt not in con2alt_ids:
            raise ValueError("the only alt of Placed Con Rule not in con2alt_ids")

        con_rule = id2rule[alt] # passby Placed Con ID
        parent2children[ID] = children2rule(con_rule.children)

    for ID in placed_alt_ids:
        rule = id2rule[ID]
        alt, = rule.alts
        if alt in con2alt_ids:
            print(ID, alt, id2rule[ID], id2rule[alt])
            raise ValueError("the only alt of Placed Alt Rule in con2alt_ids")
        parent2children[ID] = alts2rule([alt])
        
    return parent2children # maybe_parent2children

    
    
def cleaned(id2rule, *main_ids):
    d = dict(id2rule)
    inplace_clean(d, *main_ids)
    return d

def inplace_clean(id2rule, *main_ids):
    reachables = find_out_reachables(id2rule, *main_ids)
    reserve_keys(id2rule, reachables)
    
    id2min_len = calc_id2min_len(id2rule)
    unproductives = find_out_unproductives(id2min_len)
    remove_keys(id2rule, unproductives)
    remove_unproductive_alts_in_AltRules(id2rule, id2min_len)

def remove_unproductive_alts_in_AltRules(id2rule, id2min_len):
    items = list(id2rule.items())
    for ID, rule in items:
        if isinstance(rule, AltRule):
            new_alts = frozenset(alt for alt in rule.alts if id2min_len[alt] != inf)
            if len(new_alts) < len(rule.alts):
                new_rule = AltRule(new_alts)
                id2rule[ID] = new_rule
    
def reserve_keys(mapping, keys):
    removing = set(mapping)
    removing.difference_update(keys)
    remove_keys(mapping, removing)
    
    
def remove_keys(mapping, keys):
    for key in keys:
        del mapping[key]

def find_out_reachables(id2rule, *main_ids):
    processed = set()
    processing = set(main_ids)
    while processing:
        ID = processing.pop()
        processed.add(ID)

        if ID not in id2rule:
            continue
        rule = id2rule[ID]
        
        if isinstance(rule, ConRule):
            maybe_news = rule.children
        elif isinstance(rule, AltRule):
            maybe_news = rule.alts
        elif isinstance(rule, Terminal):
            continue
        else:
            raise logic-error
        news = set(maybe_news) - processed
        processing.update(news)
    return processed



def classify_FlatOutputIDs_by_IDType_and_RuleType(id2rule):
    '((placed_con_ids, placed_alt_ids), con2alt_ids), terminals, undefineds'
    
    terminals = set()
    placed_ids = set()
    deads = set()
    placed_con_ids = set()
    placed_alt_ids = set()
    con2alt_ids = set()
        
    for ID, rule in id2rule.items():
        if isinstance(ID, PlacedID):
            if isinstance(rule, Terminal):
                updating = terminals
            elif isinstance(rule, AltRule):
                updating = placed_ids
            elif isinstance(rule, ConRule):
                raise logic-error
            else:
                raise logic-error
        elif isinstance(ID, ConToAltID):
            assert isinstance(rule, ConRule)
            updating = con2alt_ids
        else:
            raise logic-error
        updating.add(ID)

    for ID in placed_ids:
        rule = id2rule[ID]
        #assert rule.alts
        if not rule.alts:
            deads.add(ID)
            continue
        
        for alt in rule.alts:
            if alt in con2alt_ids:
                placed_con_ids.add(ID)
            else:
                placed_alt_ids.add(ID)
            break
        
        
    undefineds = collect_undefined_IDs(id2rule)
    deads.update(undefineds)
    return ((placed_con_ids, placed_alt_ids), con2alt_ids), terminals, (undefineds, deads)

def collect_undefined_IDs(id2rule, *main_ids):
    _, (_, _, undefineds) = classify_IDs_by_RuleType(id2rule)
    undefs = set(main_ids) - set(id2rule)
    undefineds |= undefs
    return undefineds

def classify_IDs_by_RuleType(id2rule):
    '((non_null2children, nulls), (non_dead2alts, deads), terminals), (alls, defineds, undefineds)'
    non_null2children = {}
    nulls = set()
    non_dead2alts = {}
    deads = set()
    terminals = set()
    alls = set(id2rule)
    defineds = alls.copy()
    for ID, rule in id2rule.items():
        if isinstance(rule, ConRule):
            if rule.is_null():
                nulls.add(ID)
            else:
                non_null2children[ID] = rule.children
                alls.update(rule.children)
        elif isinstance(rule, AltRule):
            if rule.is_dead():
                deads.add(ID)
            else:
                non_dead2alts[ID] = rule.alts
                alls.update(rule.alts)
        elif isinstance(rule, Terminal):
            terminals.add(ID)
        else:
            raise logic-error

    undefineds = alls - defineds
    deads.update(undefineds)
    return ((non_null2children, nulls), (non_dead2alts, deads), terminals), \
           (alls, defineds, undefineds)
    
def calc_id2min_len(id2rule):
    
    # classify IDs by RuleType
    ((non_null2children, nulls), (non_dead2alts, _), terminals),\
           (alls, _, _) = \
           classify_IDs_by_RuleType(id2rule)

    # init
    id2min_len = dict.fromkeys(alls, float('inf')) # alls instead of keys
    for ID in nulls:
        id2min_len[ID] = 0
    for ID in terminals:
        id2min_len[ID] = 1
    
    # closure
    def update(ID, min_len):
        nonlocal modified
        if min_len < id2min_len[ID]:
            id2min_len[ID] = min_len
            modified = True
    def alts2min(alts):
        return min(id2min_len[ID] for ID in alts)
    def children2min(children):
        return sum(id2min_len[ID] for ID in children)
    
    modified = True
    while modified:
        modified = False
        
        for non_null, children in non_null2children.items():
            m = children2min(children)
            update(non_null, m)
        
        for non_dead, alts in non_dead2alts.items():
            m = alts2min(alts)
            update(non_dead, m)
        
    return id2min_len

def find_out_nullables(id2min_len):
    return find_out_keys_to_value(id2min_len, 0)
def find_out_unproductives(id2min_len):
    return find_out_keys_to_value(id2min_len, float('inf'))

def find_out_keys_to_value(mapping, value):
    for key, val in mapping.items():
        if val == value:
            yield key

class IDKnownRule(ThisClassRule):
    '''id2rule = {..., aSelfDefinedID: aIDKnownRule, ..}

id_transform over SelfDefinedID should fmap to SelfDefinedID.rule

'''
    def flip_fmap(self, transform):
        'immutable'
        return self
id_known_rule = IDKnownRule()


class SelfDefinedID(NewtypeWithMultiArgs, ID):
    '''using rule as ID;

know how to make up rule instead of holding the rule to avoid infinite recur

"A*" holds Star;

if id2rule.get(aSelfDefinedID, id_known_rule) == IDKnownRule():
    then ==>> as-if id2rule[aSelfDefinedID] == aSelfDefinedID.make_rule()

else:
    id2rule[aSelfDefinedID] is not a IDKnownRule
    should hold: id2rule[aSelfDefinedID] == aSelfDefinedID.make_rule()
'''
    def __init__(self, *args):
        'args should be immutable object'
        super().__init__(*args)
    @property
    def rule_args(self):
        return self.unbox()
    def make_rule(self):
        raise NotImplementedError
    


class NullRuleID(SelfDefinedID):
    def __init__(self):
        super().__init__(())
    def make_rule(self):
        'Null = ;'
        return null_rule
class DeadRuleID(SelfDefinedID):
    def __init__(self):
        super().__init__(())
    def make_rule(self):
        'Dead { }'
        return dead_rule

null_rule_id = NullRuleID()
dead_rule_id = DeadRuleID()


class SelfDefinedID_WithOneRefIDArgs(SelfDefinedID):
    def __init__(self, ref_id, *args):
        assert isinstance(ref_id, ID)
        super().__init__(ref_id, *args)
    @property
    def ref_id(self):
        return self.rule_args[0]
    
class SelfDefinedID_WithOneRefIDOnly(SelfDefinedID_WithOneRefIDArgs):
    def __init__(self, ref_id):
        super().__init__(ref_id)
class RepeatRuleID(SelfDefinedID_WithOneRefIDArgs):pass
class RepeatRuleID_WithOneRefIDOnly(RepeatRuleID):pass

class QuesRuleID(SelfDefinedID_WithOneRefIDOnly):
    def make_rule(self):
        'A? { A Null }'
        A = self.ref_id
        return AltRule([A, null_rule_id])
class StarRuleID(SelfDefinedID_WithOneRefIDOnly):
    def make_rule(self):
        'A* { A+ Null }'
        A = self.ref_id
        return AltRule([CrossRuleID(A), null_rule_id])
class CrossRuleID(SelfDefinedID_WithOneRefIDOnly):
    def make_rule(self):
        'A+ = A A* ;'
        A = self.ref_id
        return ConRule([A, StarRuleID(A)])

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

        
        
        

class ExtendedRuleID(ID):pass
class BoxedBasicRuleID(ExtendedRuleID):pass
class ExtendedIterRuleID(ExtendedRuleID):pass
class QuesRuleID(ExtendedIterRuleID):pass
class StarRuleID(ExtendedIterRuleID):pass
class CrossRuleID(ExtendedIterRuleID):pass

'''
A -> B C* ;

==>>>
Boxed_A = Boxed_B Star_C  ;
Star_C  { Null    Cross_C }
Cross_C = Boxed_C Star_C  ;
'''

def id2extended_rule_to_id2basic_rule(id2extended_rule)























