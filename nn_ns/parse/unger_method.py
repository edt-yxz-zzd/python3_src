

r'''offer a CF parser

if ambiguous, then the result parse-tree is implement-defined

term:
    ref                    alias symbol
    token/token_ref        alias terminal
    ntoken/nontoken_ref    alias nonterminal
    token_seq                -   sentence
    main_ref                 -   start symbol
    rk/rule_id               -   name of rule

function:
    UngerMethod          - the parser
    simple_grammar_parser - to parse a CF grammar
    parse_tree2info_tree - to make to parse result more understandable

    calc_rk_ref_minlen   - calc min length of nonterminal and each rule
    find_loop_unit_rules - find out loops formed by unit rules
    get_nullable_ref     - nonterminals with empty production

data-format/type:
    CF grammar    -  lines of: <nonterminal> ' = ' (' ' <symbol>) *
    parse_tree   -  ()             or (rule_id, [parse_tree])
    info_tree    -  (token, range) or (rule_id, range, [info_tree])
    ref/symbol   -  hashable
    rk/rule_id   -  hashable (ref and rk are in different namespace)

'''

from collections import OrderedDict
from itertools import accumulate
import warnings
from nn_ns.graph.directed_graph import strong_connected_components, dedges2u2vtc
from sand import Slist
from nn_ns.parse.simple_grammar_parser import simple_grammar_parser

__all__ = '''
    parse_tree2info_tree
    UngerMethod
    UngerParser
    UngerParseFail

    simple_grammar_parser
    
    calc_rk_ref_minlen
    find_loop_unit_rules
    get_nullable_ref
    '''.split()











def check_ref_rules(nontoken_ref2rule_ids, rule_id2refs, token_refs):
    #assert all(t in token_refs for t in token_seq)
    nontoken_refs = set(nontoken_ref2rule_ids)
    if nontoken_refs & token_refs:
        raise ValueError('token_ref or nontoken_ref?: {}'\
                         .format(nontoken_refs & token_refs))

##    death_refs = {ref for refs in rule_id2refs.values() for ref in refs}
##    death_refs -= nontoken_refs
##    death_refs -= token_refs
##    if death_refs:
##        print('WARN: death_refs: {}'.format(death_refs))
        #raise ValueError('unknown token: {}'.format())
    return True




def gen_ans_dict(d, func, *args):
    old_len = -1
    while old_len < len(d):
        old_len = len(d)
        func(d, *args)
    return d

def get_nullable_ref(nontoken_ref2rule_ids, rule_id2refs, token_refs):
    r'''find out which ref is nullable. -> ref2null_tree

ref2null_tree - {ref : the null parse tree of ref}
'''
    check_ref_rules(nontoken_ref2rule_ids, rule_id2refs, token_refs)
    
    ref2null_tree = {} # nullable_ref to tree
        
    def find_nullable_refs(r):
        for ref, rks in nontoken_ref2rule_ids.items():
            if ref in r: continue
            for rk in rks:
                if all(subref in r for subref in rule_id2refs[rk]):
                    node = (rk, [r[subref] for subref in rule_id2refs[rk]])
                    r[ref] = node
                    break


    gen_ans_dict(ref2null_tree, find_nullable_refs)
    return ref2null_tree



def find_loop_unit_rules(nontoken_ref2rule_ids, rule_id2refs, null_refs):
    r'''->(ref2loop_unit_class, ref_edge2rk)

ref2loop_unit_class -  {ref : [refx]}
                       [refx] is the loop-unit-class which ref is in
                       
ref_edge2rk         -  {(ref1, ref2) : rk}
                       rk is a unit rule of (ref1, ref2)

If "A = <left> B <right>" and <left/right> are nullable,
    then we call this rule a unit-rule of (A, B).
If there exist unit-rules of (A1,A2), (A2,A3)...(AN,A1),
    then we say {Ai} form a loop-unit-class.
Each unit-rule introduce a directed edge (A,B),
    a loop-unit-class form a strong connected component.

If we ask "does A generate some a sentence?" using Unger-Method,
    we may be led to ask the same question again through loop-unit-rules.
We should cut off the same later query to avoid dead-loop.
But now the answer is UNKNOWN instead of YES or NO.

This CUT-OFF action may cause suspicious failures until the
    top-most failure that is failure of the original question.
If the original question answers YES,
    then we should fix those suspicious failures.
'''

    edges = {}
    for ref, rks in nontoken_ref2rule_ids.items():
        for rk in rks:
            refs = rule_id2refs[rk]
            lsn = bytes(r in null_refs for r in refs)
            if sum(lsn) >= len(refs) - 1:
                i = lsn.find(False)
                if i == -1:
                    # all !!
                    pass
                    #edges.extend((ref, r) for r in refs)
                else:
                    refs = [refs[i]] # edges.append((ref, refs[i]))
                for r in refs:
                    if r == ref:
                        continue
                    edge = (ref, r)
                    if edge not in edges:
                        edges[edge] = rk

    vtc = {r for edge in edges for r in edge}
    vtc = list(vtc)
    ref2idx = {r:i for i, r in enumerate(vtc)}
    idx2ref = vtc
    dedges = {tuple(ref2idx[r] for r in edge) for edge in edges}
    u2vtc = dedges2u2vtc(len(vtc), dedges)
    vtc_ls, edges_ls, discarded_edges = strong_connected_components(u2vtc)

    
    loop_unit_classes = [[idx2ref[idx] for idx in vtc]
                         for vtc in vtc_ls if len(vtc) > 1]
    ref2loop_unit_class = {ref: cls for cls in loop_unit_classes for ref in cls}

    ref_edge2rk = edges
    return ref2loop_unit_class, ref_edge2rk



def calc_rk_ref_minlen(nontoken_ref2rule_ids, rule_id2refs, token_refs):
    r'''->(rk2minlen, ref2minlen, rk2lens)

rk2minlen  -  {rule_id : minlen...}
ref2minlen -  {ref     : minlen...}
rk2lens    -  {rule_id : [minlen of this_rule[pos:] for each pos]}
minlen     -  the minimum length of sentences derived by the rule/ref/part-of-rule
'''

    check_ref_rules(nontoken_ref2rule_ids, rule_id2refs, token_refs)
    ref2minlen = {t:1 for t in token_refs} # ref to min length

    inf = float('inf')
    rk2minlen = {rk: inf for rk in rule_id2refs}
    for nt in nontoken_ref2rule_ids:
        assert nt not in ref2minlen
        ref2minlen[nt] = inf
    assert len(ref2minlen) == len(token_refs) + len(nontoken_ref2rule_ids)

    # for non-productive ref
    for refs in rule_id2refs.values():
        for ref in refs:
            if ref not in ref2minlen:
                ref2minlen[ref] = inf

        
    def calc_ref_minlen():
        new = ref2minlen.copy()
        new.update((ref, min(rk2minlen[rk] for rk in rks))
                    for ref, rks in nontoken_ref2rule_ids.items())
        return new


    def calc_rk_minlen():
        return {rk: sum(ref2minlen[ref] for ref in refs)
                for rk, refs in rule_id2refs.items()}


        

    b = 1
    while b:
        b = 0
        r = calc_rk_minlen()
        if r != rk2minlen:
            b += 1
            rk2minlen = r
            
        r = calc_ref_minlen()
        if r != ref2minlen:
            b += 1
            ref2minlen = r

    # calc rk[pos:] minlen
    rk2lens = {}
    for rk, refs in rule_id2refs.items():
        lens = [ref2minlen[ref] for ref in refs]
        lens.reverse()
        lens = list(accumulate(lens))
        lens.reverse()
        rk2lens[rk] = lens
            

    death_refs = {ref for ref in ref2minlen if ref2minlen[ref] == inf}
    if death_refs:
        # print('WARN: death_refs: {}'.format(death_refs))
        warnings.warn('death_refs: {}'.format(death_refs))
    return rk2minlen, ref2minlen, rk2lens
    



    
        

def UngerMethod(main_ref : 'start symbol',
                nontoken_ref2rule_ids : '{ntoken : [rk]}',
                rule_id2refs : '{rk : [ref]}',
                token_refs : '{token}',
                token_seq : '[token]', begin = 0, end = None):
    return UngerParser\
           (main_ref, nontoken_ref2rule_ids, rule_id2refs, token_refs)\
           .parse(token_seq, begin, end)
    
class UngerParseFail(ValueError):
    def __init__(self, *args, pos):
        super().__init__(*args)
        self.pos = pos
    
class UngerParser:
    r'''a CFG parser used Unger Method.

Since middle results are cached, I think it's an Earley Parser.
But only one parse tree are returned, faster than CYK.

1. How to transform a grammar to input?
    grammar:
    S = a S
    S = b

    CALL:
    UngerMethod(main_ref = 'S',
                nontoken_ref2rule_ids = {'S': ['S-1', 'S-2']},
                rule_id2refs = {'S-1': ['a', 'S'], 'S-2': ['b']},
                token_refs = {'a', 'b'},
                token_seq = ['a', 'b', 'a', 'a']
                )

    You can use simple_grammar_parser('S = a S\nS = b') too!

    
2. What's the output format?
    parse_tree = (rule_id, [parse_tree]) or ()
    
    the above call will result:
    IF SET token_seq TO 'aaab', OUTPUT:
        ('S-1', [(), ('S-1', [(), ('S-1', [(), ('S-2', [(), ])])])])
        S-1  =   a    S        |           |            |
                      S-1  =   a    S      |            |
                                    S-1 =  a    S       |
                                                S-2 =   b


3. How to get a better look of the result?
    try this:
        parse_tree2info_tree(token_seq, result)
    see below for the output.


example:
    >>> UngerMethod(main_ref = 'S',
    ...            nontoken_ref2rule_ids = {'S': ['S-1', 'S-2']},
    ...            rule_id2refs = {'S-1': ['a', 'S'], 'S-2': ['b']},
    ...            token_refs = {'a', 'b'},
    ...            token_seq = ['a', 'a', 'a', 'b']
    ...            )
    ('S-1', [(), ('S-1', [(), ('S-1', [(), ('S-2', [()])])])])
    >>> parse_tree2info_tree('aaab', _) == \
    ...     ('S-1', (0, 4), [
    ...         ('a', (0, 1)),
    ...         ('S-1', (1, 4), [
    ...             ('a', (1, 2)),
    ...             ('S-1', (2, 4), [
    ...                 ('a', (2, 3)),
    ...                 ('S-2', (3, 4), [
    ...                     ('b', (3, 4))]
    ...                  )]
    ...              )]
    ...          )]
    ...      )
    True
    >>> UngerMethod(main_ref = 'S',
    ...            nontoken_ref2rule_ids = {'S': [11, 12, 13]},
    ...            rule_id2refs = {11: 'SSSSSS', 12: 'a', 13: ''},
    ...            token_refs = {'a'},
    ...            token_seq = 'aaa'
    ...            ) == \
    ...   (11, [(13, []), (13, []), (13, []), (13, []),
    ...         (12, [()]),
    ...         (11, [(13, []), (13, []), (13, []), (13, []),
    ...               (12, [()]),
    ...               (12, [()])])])
    True
    >>>
    
'''

    def __init__(self,
                main_ref : 'start symbol',
                nontoken_ref2rule_ids : '{ntoken : [rk]}',
                rule_id2refs : '{rk : [ref]}',
                token_refs : '{token}'):
                

        token_refs = frozenset(token_refs)

        if main_ref in token_refs:
            raise ValueError('main_ref in token_refs')
        if main_ref not in nontoken_ref2rule_ids:
            raise ValueError('main_ref not in nontoken_refs')
        
        check_ref_rules(nontoken_ref2rule_ids, rule_id2refs, token_refs)
            
        rk2minlen, ref2minlen, rk2lens = calc_rk_ref_minlen(
            nontoken_ref2rule_ids, rule_id2refs, token_refs)
        ref2null_tree = get_nullable_ref(
            nontoken_ref2rule_ids, rule_id2refs, token_refs)
        assert set(ref for ref in ref2minlen if ref2minlen[ref] == 0) == \
               set(ref2null_tree)

        ref2loop_unit_class, ref_edge2rk = find_loop_unit_rules(
            nontoken_ref2rule_ids, rule_id2refs, ref2null_tree)
        
        (self.main_ref,
         self.nontoken_ref2rule_ids,
         self.rule_id2refs,
         self.token_refs,

         self.ref2minlen,
         self.rk2lens,
         self.ref2null_tree,
         self.ref2loop_unit_class) = \
                     ( main_ref,
                       nontoken_ref2rule_ids,
                       rule_id2refs,
                       token_refs,
                       
                       ref2minlen,
                       rk2lens,
                       ref2null_tree,
                       ref2loop_unit_class)



    def parse(self, token_seq : '[token]', begin = 0, end = None,
              *, throw=True, return_sizes=False):
        'return a failure index or a parse tree'
        if end is None:
            end = len(token_seq)
        if not (0 <= begin <= end <= len(token_seq)):
            raise ValueError('not (0 <= begin <= end <= len(token_seq))')
        
        if not all(t in self.token_refs for t in token_seq[begin:end]):
            raise ValueError('unknown tokens: {}'\
                             .format(set(token_seq[begin:end]) - self.token_refs))
        
        # begin, end = 0, len(token_seq)
        # L = len(token_seq)
        # main = (main_ref, begin, end)
       
        processed_ref_xys = processed_refs = {} # {(ref, x, y):None or reslut} #
        processed_rk_pos_xys = processed_tails = {} # {(rule_id, pos, x,y):}
        processing_ref_xys = processing = OrderedDict() # OrderedDict

        result = _UngerMethod_impl(self.main_ref,
                           self.nontoken_ref2rule_ids,
                           self.rule_id2refs,
                           self.token_refs,
                           
                           self.ref2minlen,
                           self.rk2lens,
                           self.ref2null_tree,
                           self.ref2loop_unit_class,
                           processed_ref_xys,
                           processed_rk_pos_xys,
                           processing_ref_xys,
                           token_seq, begin, end)

        if result is None:
            success_to = list(y for (ref, x, y), v in processed_ref_xys.items()
                              if v is not None)
            farthest_success = begin if not success_to else max(success_to)

            failure_from = list(x for (ref, x, y), v in processed_ref_xys.items()
                             if v is None)
            farthest_failure = begin if not failure_from else max(failure_from)

##            if not farthest_success == farthest_failure:
##                print(farthest_success, farthest_failure)
##                for (ref, x, y), v in processed_ref_xys.items():
##                    if v is not None:
##                        if y > farthest_failure:
##                            print(ref, x, y, token_seq[x:y])
##                            print(v)
            # fire : assert farthest_success == farthest_failure
            # fire : assert farthest_success >= farthest_failure
            # fire : assert farthest_success <= farthest_failure

            result = min(farthest_failure, farthest_success)
            if throw:
                e = UngerParseFail('fail at token_seq[{}]'
                                   .format(result),
                                   pos = result)
                raise e
            
            #raise ValueError('fail at token_seq[{}]'.format(farthest_failure))

        #print(*map(len, [token_seq, processed_ref_xys, processed_rk_pos_xys, processing_ref_xys]))
        # 95 2532 4005 0 ; size = O(len(seq)**2)??
        
        if return_sizes:
            *sizes, = map(len, [token_seq, processed_ref_xys,
                                processed_rk_pos_xys, processing_ref_xys])
            return result, sizes
        return result

def __UngerMethod_impl(main_ref,
                       nontoken_ref2rule_ids,
                       rule_id2refs,
                       token_refs,
                       
                       ref2minlen,
                       rk2lens,
                       ref2null_tree,
                       ref2loop_unit_class,
                       
                       processed_ref_xys,
                       processed_rk_pos_xys,
                       processing_ref_xys,
                       token_seq, begin, end):
    '''

rk/rule_id <<== ref, id
tail_concat_part <<== rk, pos

ref = A B C # rk = ref-0
ref = D E   # rk = ref-1

rk = ref-0 or ref-1
for ref-0, pos = 0, 1, 2, 3
    (ref-0, pos=0) = A B C
    (ref-0, pos=1) = B C
    (ref-0, pos=2) = C
    (ref-0, pos=3) = <null>

tokens[x:y] <<== x,y
rk_pos_xy = (rk, pos, x,y) # means try to match rk[pos:] over tokens[x:y]
ref_xy = (ref, x,y) # means try to match ref[?][0:] over tokens[x:y]
'''

    processing_rk_pos_xys = Slist()
    farthest = -1
    farthest_rk_pos_xy_stack = None
    main = (main_ref, begin, end)

    def to_rule_ids(ref):
        return nontoken_ref2rule_ids.get(ref, [])
    def expand_ref(ref, x,y):
        ls = [(rule_id, 0, x,y) for rule_id in to_rule_ids(ref)]
        return ls


    def _expand(ref_xy):
        return expand_ref(*ref_xy)
    
    def gen_eq_trees_as_processed(ref, tree, x,y):
        ref_xy = ref, x,y
        if processing_ref_xys[ref_xy] != 'cut_off':
            # no by me, even if someone set to failure
            return
        
        if tree is None:
            # I fail, too. hope some ancestor to save me.
            return

        if ref not in ref2loop_unit_class:
            return
        
        for eref in ref2loop_unit_class[ref]:
            if ref == eref: continue
            eref_xy = eref, x,y
            if eref_xy in processed_ref_xys and \
               processed_ref_xys[eref_xy] is None:
                # failure caused by cut off
                # we restore to unknown state
                # since to construct all eq classes
                # is time consuming and not-necessary.
                del processed_ref_xys[eref_xy]
                
                
##                if eref_xy not in processed_ref_xys or \
##                   processed_ref_xys[eref_xy] is None:
##                    processed_ref_xys[eref_xy] = \
##                        make_eq_ref_tree(ref, eref, tree)
##                    #['using loop unit alias', ref_xy]
##    def make_eq_ref_tree(ref, eref, tree):pass
        
    def _ref_xy(ref_xy):
        if ref_xy in processing_ref_xys:
            # cut off
            processing_ref_xys[ref_xy] = 'cut_off'
##            raise NotImplementedError(
##                'TODO: the loop unit rules form a directed-graph of vetices ref. '\
##                'the strong connected components can use to erase the fail caused '\
##                'at this cut off.')
            return None # but may success at the above layer, doesnot set processed

        ref, x, y = ref_xy
        if y-x < ref2minlen[ref]:
            return None
        elif x == y:
            return ref2null_tree[ref]
        elif ref in token_refs:
            if x + 1 == y and token_seq[x] == ref:
                return ()
            else:
                return None
            
        elif ref_xy in processed_ref_xys:
            return processed_ref_xys[ref_xy]
        else:
            processing_ref_xys[ref_xy] = ''

            tree = None
            for rk_pos_xy in _expand(ref_xy):
                rk = rk_pos_xy[0]
                L = len(rk2lens[rk])
                if L == 0:
                    assert x < y
                    continue
                rforest = _rk_pos_xy(rk_pos_xy)
                if rforest is not None:
                    rk, _, x,y = rk_pos_xy
                    forest = list(rforest)
                    forest.reverse()
                    trees = forest
                    tree = (rk, trees)
                    break

            gen_eq_trees_as_processed(ref, tree, x,y)
            this, _ = processing_ref_xys.popitem() # OrderedDict
            assert this == ref_xy


            
            processed_ref_xys[ref_xy] = tree # None indicate fail
        return tree


    def _may_success(rk_pos_xy):
        rk, pos, x, y = rk_pos_xy
        
        if y-x < rk2lens[rk][pos]:
            return False
        if rk_pos_xy in processed_rk_pos_xys:
            if processed_rk_pos_xys[rk_pos_xy] is None:
                return False
        return True

    def _rk_pos_xy(rk_pos_xy):
        nonlocal processing_rk_pos_xys, farthest, farthest_rk_pos_xy_stack

        processing_rk_pos_xys <<= rk_pos_xy
        rk, pos, x, y = rk_pos_xy
        if x > farthest:
            farthest = x
            farthest_rk_pos_xy_stack = processing_rk_pos_xys

        rforest = __rk_pos_xy(rk_pos_xy)
        processing_rk_pos_xys, _ = processing_rk_pos_xys.pop()

        return rforest
            
            
        
        
    def __rk_pos_xy(rk_pos_xy):
        rk, pos, x, y = rk_pos_xy
        assert 0 <= x <= y
        
        refs = rule_id2refs[rk]
        L = len(refs)
        assert pos < L # nullable one is stopped by ref_xy
        
        if not _may_success(rk_pos_xy):
            return None

        if rk_pos_xy in processed_rk_pos_xys:
            return processed_rk_pos_xys[rk_pos_xy]
        
        


        rforest = None
        ref = refs[pos]
        if pos == L-1:
            tree = _ref_xy((ref, x,y))
            if tree is not None:
                rforest = [tree]
        else:
            my_minlen = ref2minlen[ref]
            tail_minlen = rk2lens[rk][pos+1]
            assert my_minlen + tail_minlen == rk2lens[rk][pos]

            for t in range(x+my_minlen, y-tail_minlen  +1): # bug fixed: '+1'
                _tail = (rk, pos+1, t, y)
                if not _may_success(_tail):
                    continue
                
                tree = _ref_xy((ref, x, t))
                if tree is None:
                    continue
                
                rforest = _rk_pos_xy(_tail)
                if rforest is None:
                    continue
                
                rforest.append(tree)
                break
            
        processed_rk_pos_xys[rk_pos_xy] = rforest
        return rforest


    result = _ref_xy(main)
##    print('result', result)
##    print('processed_ref_xys', processed_ref_xys)
##    print('ref2minlen', ref2minlen)
##    print('rk2lens', rk2lens)
    return result

_UngerMethod_impl = __UngerMethod_impl

def parse_tree2info_tree(token_seq, parse_tree, begin = 0, end=None):
    r'''put more information into the parse_tree generated by UngerMethod()

tree nodes are transformed as:
    () -> (token, (pos, pos+1))
    (rule_id, [child]) -> (rule_id, (begin, end), [...])
'''
    if end == None:
        end = len(token_seq)

    tree = parse_tree
    this_f = parse_tree2info_tree
    
    if tree == ():
        assert end > begin
        rng = (begin, begin+1)
        return (token_seq[begin], rng)
    
    rk, ls = tree
    if not ls:
        rng = (begin, begin)
        return (rk, rng, [])

    itrees = []
    _beg = begin
    for subtree in ls:
        itree = this_f(token_seq, subtree, _beg, end)
        itrees.append(itree)
        if len(itree) == 3:
            _, (_, _beg), _ = itree
        else:
            _, (_, _beg) = itree
            

    rng = begin, _beg
    return rk, rng, itrees


def t(to_print=False, *args, **kwargs):
    from pprint import PrettyPrinter
    main_ref = 'm'
    nontoken_ref2rule_ids = {'m':[10,11,12], 'a':[20,21]}
    rule_id2refs = {10: 'mam', 11:'', 12:'a', 20:'m', 21:'T'}
    token_refs = set('T')
    token_seq = 'T' * 3

    r = UngerMethod(main_ref, nontoken_ref2rule_ids, rule_id2refs, token_refs,
                    token_seq)

    s = parse_tree2info_tree(token_seq, r)

    if to_print:
        p = PrettyPrinter(*args, **kwargs)
        p.pprint(r)
        p.pprint(s)


    tree = (10, # m a m
             [(11, []),   # m ==>> ''    # small m
              (21, [()]), # a ==>> 'T'
              (10,        # m ==>> m a m # big m # right biased
               [(11, []),
                (21, [()]),
                (10, # m ==>> m a m
                 [(11, []),
                  (21, [()]),
                  (11, []) # m ==>> ''
                  ])])])

    info = (10, (0, 3),
             [(11, (0, 0), []),
              (21, (0, 1), [('T', (0, 1))]),
              (10, (1, 3),
               [(11, (1, 1), []),
                (21, (1, 2), [('T', (1, 2))]),
                (10, (2, 3),
                 [(11, (2, 2), []),
                  (21, (2, 3), [('T', (2, 3))]),
                  (11, (3, 3), [])
                  ])])])

    assert r == tree
    assert s == info
    return r, s
##    p = PrettyPrinter(4)
##    p.pprint(s)







if __name__ == '__main__':
    t()
    import doctest
    doctest.testmod()


    UngerMethod(main_ref = 'S',
                nontoken_ref2rule_ids = {'S': ['S-1', 'S-2']},
                rule_id2refs = {'S-1': ['a', 'S'], 'S-2': ['b']},
                token_refs = {'a', 'b'},
                token_seq = 'aaab'
                )
    UngerMethod(main_ref = 'S',
                nontoken_ref2rule_ids = {'S': [11, 12, 13]},
                rule_id2refs = {11: 'SSSSSS', 12: 'a', 13: ''},
                token_refs = {'a'},
                token_seq = 'aaa'
                )


