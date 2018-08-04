

__all__ = '''

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
from sand.types.ToProcess import UnorderedSetOnce
from .ParseResultAST import ConRuleNode, AltRuleNode, TerminalNode

from .ID_and_Rule_Types import *





# ------------  ExtendedRuleTypes  -----------

##class ExtendedRuleABC(metaclass = ABCMeta):pass
##class ExtendedIterRule(Rule):
##    @property
##    def ref_id(self):
##        return self.unbox()
##    def flip_fmap(self, transform):
##        return type(self)(transform(self.ref_id))
##    
##class QuesRule(ExtendedIterRule):pass
##class StarRule(ExtendedIterRule):pass
##class CrossRule(ExtendedIterRule):pass












    












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


        
        '''

class ExtendedRuleID(ID):pass
class BoxedBasicRuleID(ExtendedRuleID):pass
class ExtendedIterRuleID(ExtendedRuleID):pass
class QuesRuleID(ExtendedIterRuleID):pass
class StarRuleID(ExtendedIterRuleID):pass
class CrossRuleID(ExtendedIterRuleID):pass

''
A -> B C* ;

==>>>
Boxed_A = Boxed_B Star_C  ;
Star_C  { Null    Cross_C }
Cross_C = Boxed_C Star_C  ;
'''
        
def rule2refs(rule):
    if isinstance(rule, ConRule):
        refs = rule.children
    elif isinstance(rule, AltRule):
        refs = rule.alts
    elif isinstance(rule, Terminal):
        refs = ()
    else:
        raise logic-error

    return iter(refs)

    
def inplace_fill_rules_of_SelfDefinedIDs(id2rule):
    to_process = UnorderedSetOnce(id2rule)
    def handle(ID):
        if isinstance(ID, SelfDefinedID):
            rule_should_be = ID.make_rule()
            rule = id2rule.setdefault(ID, rule_should_be)
            
            if rule != rule_should_be:
                raise ValueError('id2rule[self_defined_id] != self_defined_id.make_rule()')

        elif ID in id2rule:
            rule = id2rule[ID]
        else:
            rule = dead_rule # undefined

        return rule2refs(rule)

    to_process.apply(handle)


'''
Join+(Sep, A) = A Con(Sep, A)*
Con(Sep, A) = Sep A
Join*(Sep, A) = Join+(Sep, A)?
'''

def test__inplace_fill_rules_of_SelfDefinedIDs():
    from pprint import pprint
    S = ID('S')
    a = ID('a')
    id2rule = {S: ConRule([a, StarRuleID(S)]), a: ter_rule}
    inplace_fill_rules_of_SelfDefinedIDs(id2rule)
    #pprint(id2rule)

    assert id2rule == { ConRuleID(()): ConRule(()),
                        ID('S'): ConRule((ID('a'), StarRuleID(ID('S')))),
                        ID('a'): Terminal(),
                        StarRuleID(ID('S')): AltRule(frozenset({_StarRuleID(ID('S'))})),
                        _CrossRuleID(ID('S')): ConRule((ID('S'), _StarRuleID(ID('S')))),
                        _StarRuleID(ID('S')): AltRule(frozenset({ConRuleID(()), _CrossRuleID(ID('S'))}))
                      }

    assert all(not isinstance(ID, SelfDefinedID) or
               rule == ID.make_rule()
               for ID, rule in id2rule.items())
    
test__inplace_fill_rules_of_SelfDefinedIDs()




























