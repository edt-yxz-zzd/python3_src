
'''
tokenset is NegAbleSet
nstate is frozenset
assume nsize is not None
'''
from abc import ABCMeta, abstractmethod
from NegAbleSet import NegAbleSetABC
from itertools import chain
from functools import reduce
import operator


def pyset_union1(sets):
    return reduce(operator.or_, sets)
    
def nsize_of_union(sets):
    it = iter(sets)
    for s in it:
        break
    else:
        return 0
    s.union(it)
    return s.nsize

def all_disjoint(sets, union_ntotal):
    it = iter(sets)
    exist_neg_set = False
    ntotal = 0
    for s in it:
        if s.nsize < 0:
            if exist_neg_set:
                # two neg sets cannot be disjoint
                return False
            exist_neg_set = True
        ntotal += s.nsize
    if exist_neg_set:
        if ntotal >= 0:
            # one neg set, if all disjoint, ntotal should be < 0
            # note that the underly pos set size = -ntotal-1 >= 0
            return False
    assert union_ntotal <= ntotal
    return union_ntotal == ntotal

def interset_disjoint_setss(disjoint_setss):
    *ls, = reduce(interset_two_disjoint_sets, disjoint_setss, [])
    return ls
def interset_two_disjoint_sets(disjoint_setsA, disjoint_setsB):
    '''interset until all disjoint

input requirement:
    all(setsA), all(setsB)
'''
    *a, = disjoint_setsA
    *b, = disjoint_setsB
    def interset(s,t):
        c = s & t
        return s/c, c, t/c

    ntotal = nsize_of_union(chain(a, b))
    
    ls = []
    for s in a:
        for i in range(len(b)-1, -1, -1):
            if not s: break
            t = b[i]
            s, c, t = interset(s,t)
            if c:
                # c should be disjoint with all others
                ls.append(c)
            if not t:
                # swap out t
                b[i] = b[-1]
                b.pop()
            else:
                # update t
                b[i] = t
        if s:
            ls.append(s)
    ls.extend(b)

    disjoints = ls
    assert all(disjoints)
    # all
    assert ntotal == nsize_of_union(disjoints)
    # disjoint
    assert all_disjoint(disjoints, ntotal)
            
        
            

def sets2disjoint_sets(sets):
    '''interset until all disjoint

input requirement:
    all(sets)
'''
    disjoints = []
    sets = tuple(sets)

    ntotal = nsize_of_union(sets)
        
    for s in sets:
        assert s
        for i in range(len(disjoints)):
            if not s:  # here: why assert s
                break
            t = disjoints[i]
            common = t & s
            if common:
                s -= common
                
                if len(t) > len(common):
                    t -= common
                    disjoints.append(common)
                else:
                    assert len(t) == len(common)
                    # assert t == common
    assert all(disjoints)
    # all
    assert ntotal == nsize_of_union(disjoints)
    # disjoint
    assert all_disjoint(disjoints, ntotal)
    
    return disjoints

            
class RegexABC:
    '''

name is the id to ref this regex;
    name __hash__, __eq__
    if name == None, then not set; otherwise

state is a determine state;
nstate == frozenset<state> is a nondetermine state
'''
    def __init__(self):
        self.__state_table = self.build_state_table()
        self.__nstate_table = self.build_nstate_table()


    @abstractmethod
    def full_tokenset(self):pass
    @abstractmethod
    def _get_init_state(self):pass
    @abstractmethod
    def _is_final_state(self, state):pass
    @abstractmethod
    def _state2states(self, state):
        # null jump
    @abstractmethod
    def _state2jumps(self, state):
        '''return [(tokenset, iter_next_states)];  // raw jumps'''
        pass
##    @abstractmethod
##    def _is_star_true_state(self, state):
##        # '.*'
##        jumps = self.state2jumps(state)
##        return len(jumps) == 1 and jumps[0][0]
##    @abstractmethod
##    def _is_star_false_state(self, state):
##        # '&a' # null language


    ##################### auto #####################
    
    @property
    def regex_id(self):
        'None is not a name, means name not existing'
        return None

##    def __find_out_all_pred2pred(self, pred_source, pred_target):
##        '''final --full_tokenset-->> final; allow self-loop'''
##        for state, jumps in self.__state_table.items():
##            if (len(jumps) == 1 and
##                jumps[0][0].is_full() and
##                pred_source(state)):
##                targets = jumps[0][1]
##                for target in targets:
##                    if self.pred_target(target):
##                        yield (state, target)
##                        
##                
##
##    def __find_out_true_states(self):
##        pred = self._is_final_state
##        iter_edges = self.__find_out_all_pred2pred(self, pred, pred)
##        edges = list(iter_edges)
##        v2outgoings = defaultdict(list)
##        for u, v in edges:
##            v2outgoings[u].append(v)
##            v2outgoings[v]
##        for u, count in v2num_outgoings.items():
##            if 
        
    
    def state2nstate(self, state):
        return frozenset(self._state2states())
    def states2nstate(self, states):
        # null jump
        nstate = frozenset().union(*(
            self.state2nstate(s) for s in set(states)))
        return nstate
    def get_init_nstate(self):
        # return a frozenset of states; hash, ==
        return  self.states2nstate(self._state2states(self._get_init_state()))

    def nstate2final_states(self, nstate):
        return list(filter(self._is_final_state, nstate))
    def is_final_nstate(self, nstate):
        return any(map(self._is_final_state, nstate))
##    def is_star_true_nstate(self, state):
##        return any(map(self._is_star_true_state, nstate))
##    def is_star_false_nstate(self, state):
##        return any(map(self._is_star_false_state, nstate))

    
    def state2jumps(self, state):
        '''return [(tokenset, next_nstate)]; 

all tokensets not empty
diff nstates
disjoint tokensets
union(tokensets) == all_tokens
'''
        return self.__state_table[state]

    def __is_good_std_jumps(self, jumps):
        if not self.__is_good_raw_jumps(jumps):
            return False
        return all(tokenset for tokenset, _ in jumps) and \
               len(set(nstate for _, nstate in jumps)) == len(jumps)
    

    def __is_good_raw_jumps(self, jumps):
        tokensets = [tokenset for tokenset, _ in jumps]
        if not tokensets:
            return False
        alls = tokensets[0].union(tokensets[1:])
        if not alls.is_full():
            return False
        
        ntotal = alls.nsize
        # may not ntotal == -1: since this may be a finite neg able set
        return all_disjoint(tokensets, ntotal)
    
    def __std_jumps(self, jumps):
        '''raw_jumps -> std_jumps

jumps = [(tokenset, next_nstate)] = tokenset_nstate_pairss
raw_jumps:
    may empty tokenset
    may not diff nstates
    disjoint tokensets
    union(tokensets) == all_tokens
std_jumps:
    all tokensets not empty
    diff nstates
    disjoint tokensets
    union(tokensets) == all_tokens
    
'''
        assert self.__is_good_raw_jumps(jumps)
        #jumps = ((tokenset, nstate) for tokenset, nstate in jumps if tokenset)
        next_nstate2input_tokens = {}
        for tokenset, nstate in jumps:
            if tokenset:
                if nstate in nstate2tokenset:
                    next_nstate2input_tokens[nstate] = tokenset
                else:
                    next_nstate2input_tokens[nstate] |= tokenset
        assert all(nstate2tokenset.values())
        jumps = [(tokens, nstate) for nstate, tokens in
                 next_nstate2input_tokens.items()]
        assert self.__is_good_std_jumps(jumps)
        return jumps
    def nstate2jumps(self, nstate):
        '''return [(tokenset, next_nstate)]; 

'''
        return self.__nstate_table[nstate]
    def _nstate2jumps(self, nstate):
        '''return [(tokenset, next_nstate)]; 

'''
        tokenset_nstate_pairss = [[
                [tokenset, next_nstate]
                for tokenset, next_nstate in self.state2jumps(state)
            ]
          for state in nstate]
        
        
        itokensetss = ((tokenset for tokenset, _ in pairs)
                       for pairs in tokenset_nstate_pairss)
        disjoint_tokensets = interset_disjoint_setss(itokensetss)

        #next_nstate2input_tokens = {}
        output = []
        for input_tokens in disjoint_tokensets:
            assert input_tokens
            ls = []
            for pairs in tokenset_nstate_pairss:
                for i, pair in enumerate(pairs):
                    tokenset, next_nstate = pair
                    if not input_tokens.is_disjoint(tokenset):
                        assert input_tokens <= tokenset
                        tokenset /= input_tokens
                        pair[0] = tokenset
                        ls.append(next_nstate)
                        # remains disjoint with input_tokens
                        break
                else:
                    raise logic-error # should intersect one!
                if not tokenset:
                    # del pairs[i]
                    pairs[i] = pairs[-1]
                    pairs.pop()
            
            assert ls
            next_nstate = pyset_union1(ls)
            output.append((input_tokens, next_nstate))
            
        assert not any(tokenset_nstate_pairss)
        return self.__std_jumps(output)

    def __state2jumps(self, state):
        jumps = self._state2jumps(state)
        'jumps = [(tokenset, iter_next_states not nstate)]'
        jumps = [(ts, self.states2nstate(ss)) for ts, ss in jumps]
        return jumps
    def build_state_table(self):
        states = set(self.get_init_nstate())
        def jumps2states(jumps):
            return set().union(nstate for _, nstate in jumps)
        return self.__build_xstate_table(states, self.__state2jumps, jumps2states)
    @staticmethod
    def __build_xstate_table(xstates, xstate2jumps, jumps2xstates):
        table = {}
        olds = set()
        while xstates:
            xstate = xstates.pop()
            if xstate not in table:
                table[xstate] = jumps = self.__std_jumps(xstate2jumps(xstate))
                olds.add(xstate)
                news = jumps2xstates(jumps)
                news -= olds
                xstates.update(news)
        return table
    def build_nstate_table(self):
        nstates = {self.get_init_nstate()}
        def jumps2nstates(jumps):
            return set(nstate for _, nstate in jumps)
        return self.__build_xstate_table(nstates, self._nstate2jumps, jumps2nstates)
            
        

            
            
    
class TokenSetRegex(RegexABC):
    '''i.e. [xxx] or [^...]

three states:
    -1 - fail
    0 - init
    1 - final
'''
    INIT = 0
    FAIL = -1
    FINAL = 1
    def __init__(self, neg_able_set):
        # input a neg_able token set
        self.__set = neg_able_set
        super().__init__()
    def full_tokenset(self):
        return self.set.full_set()
    
    @property
    def set(self):
        return self.__set
    
    def _get_init_state(self):
        return self.INIT
    def _is_final_state(self, state):
        return state == self.FINAL
    def _state2states(self, state):
        # null jump
        yield state
    def _state2jumps(self, state):
        # [neg] self.set may be empty; which should not occur as tokenset in output
        if state == self.INIT:
            return [(self.set, [self.FINAL]), (~self.set, [self.FAIL])]
        else:
            return [(self.set.full_set(), [self.FAIL])]


class ConcatRegexABC(RegexABC):
    '''i.e. "ABC"

state: (idx, subnstate) - hash, iter
    with some other data : i.e. prev final subnstate
final_state : (len(rex_ls), None)
no fail_state : (-1, None)
    
'''

    #FAIL = (-1, None)
    
    def __init__(self, rex_ls):
        rex_ls = tuple(rex_ls)
        assert all(isinstance(rex, RegexABC) for rex in rex_ls)

        self.__rex_ls = rex_ls
        super().__init__()
        
    @property
    def rex_ls(self):
        return self.__rex_ls

    def _state2states(self, state):
        # null jump

        while True:
            yield state
            idx, subnstate = state
            if self._is_final_state(state) or \
               not self.rex_ls[idx].is_final_nstate(subnstate):
                return

            state = self._get_idx_init_1state(idx+1)
        return
    def _get_idx_init_1state(self, idx):
        assert idx >= 0
        if idx == len(self.rex_ls):
            subnstate = None
        else:
            subnstate = self.rex_ls[idx].get_init_nstate()
        state = idx, subnstate
        return state
        
        
    def _get_init_state(self):
        state = self._get_idx_init_1state(0)
        return state

    def _is_final_state(self, state):
        return state == (len(self.rex_ls), None)

    def _state2jumps(self, state):
        '''return [(tokenset, iter_next_states)];  // raw jumps'''
        #if state == self.FAIL:
            
        if self._is_final_state(state):
            yield (self.full_tokenset(), [state])
            return

        idx, subnstate = state
        subjumps = self.rex_ls[idx].nstate2jumps(subnstate)
        for tokenset, next_subnstate in subjumps.items():
            yield tokenset, [(idx, next_subnstate)]
        pass
    

class ChoiceRegexABC(RegexABC):
    '''i.e. "A|B|C"

state: (substate"s"/subnstate, ...) - product of subs - hash, iter
final_state : any sub final
no fail_state : all fail
    
'''

    def __init__(self, rex_ls):
        rex_ls = tuple(rex_ls)
        assert all(isinstance(rex, RegexABC) for rex in rex_ls)

        self.__rex_ls = rex_ls
        super().__init__()
    @property
    def rex_ls(self):
        return self.__rex_ls

    def _state2states(self, state):
        # null jump

        std_state = tuple(subrex.states2nstate(substates)
                          for substates, subrex in zip(state, self.rex_ls))
        yield std_state

        
    def _get_init_state(self):
        return tuple(rex.get_init_nstate() for rex in self.rex_ls)

    def _is_final_state(self, state):
        return any(subrex.is_final_nstate(subnstate)
                   for subnstate, subrex in zip(state, self.rex_ls))

    def _state2jumps(self, state):
        '''return [(tokenset, iter_next_states)];  // raw jumps'''
        #if state == self.FAIL:
            
        idx2subjumps = [list(subrex.nstate2jumps())
                        for subnstate, subrex in zip(state, self.rex_ls)]
        *tokensets, = interset_disjoint_setss(
            (tokens for tokens, _ in subjumps)
            for subjumps in idx2subjumps)

        for input_tokens in tokensets:
            assert input_tokens
            ls = []
            for subjumps in idx2subjumps:
                assert subjumps
                for i in range(len(subjumps)):
                    tokens, nstate = subjumps[i]
                    if not input_tokens.is_disjoint(tokens):
                        assert input_tokens <= tokens
                        tokens = tokens / input_tokens
                        subjumps[i] = tokens
                        ls.append(nstate)
                        break
                else:
                    raise logic-error
                if not tokens:
                    # del subjumps[i]
                    subjumps[i] = subjumps[-1]
                    subjumps.pop()
            assert len(ls) == len(self.rex_ls)
            next_state = tuple(ls)
            yield input_tokens, [next_state]
        assert not any(idx2subjumps)
        return
            

class StarRex(RegexABC):
    '''i.e. "A*"

state:
    (-1,) - fail # init --any_token--> fail
    (0,) - init | final
    (1, subnstate) - mid
'''
    INIT = (0,)
    FINAL = INIT
    FAIL = (-1,)
    def __init__(self, rex):
        self.__rex = rex
        super().__init__()

    @property
    def ref_rex(self):
        return self.__rex
    def __subnstate2midnstate(self, subnstate):
        return (1, subnstate)
    def __midnstate2subnstate(self, midnstate):
        i, subnstate = midnstate
        assert i == 1
        return subnstate

    def full_tokenset(self):
        return self.ref_rex.full_tokenset()
    def _get_init_state(self):
        return self.INIT
    def _is_final_state(self, state):
        return state == self.FINAL
    def _state2states(self, state):
        # null jump
        yield state

        if state == self.FAIL:
            return
        if self._is_final_state(state):
            yield self.__subnstate2midnstate(self.ref_rex.get_init_nstate())
            return

        subnstate = self.__midnstate2subnstate(state)
        if self.ref_rex.is_final_nstate(subnstate):
            yield self.FINAL
        return
    
    def _state2jumps(self, state):
        '''return [(tokenset, iter_next_states)];  // raw jumps'''
        if state == self.FAIL or self._is_final_state(state):
            yield (self.full_tokenset(), self.FAIL)
            return

        subnstate = self.__midnstate2subnstate(state)
        subjumps = self.ref_rex.nstate2jumps(subnstate)
        for input_tokens, subnstate in subjumps:
            yield input_tokens, [self.__subnstate2midnstate(subnstate)]
        return



            
class RegexWrapper:
    '''UserRegex like UserDict'''
    def __init__(self, rex):
        if not isinstance(rex, RegexABC):
            raise TypeError('not isinstance(rex, RegexABC)')
        self.__rex = rex
        #super().__init__()

    @property
    def ref_rex(self):
        return self.__rex
    def __getattr__(self, attr):
        return getattr(self.ref_rex, attr)
        AttributeError
RegexABC.register(RegexWrapper)

class NegRex(RegexWrapper):
    'not rex: i.e. "(?!A)"'
    def _is_final_state(self, state):
        return not self.ref_rex._is_final_state(state)
    def __invert__(self):
        return self.ref_rex

class CaptureRex(RegexWrapper):
    'i.e. "(?P<name>A)"'
    open_type_name = 'capture('
    close_type_name = 'capture)'
    def __init__(self, rex, zero_rex, concat, name):
        open_name = (self.open_type_name, name)
        close_name = (self.close_type_name, name)
        open_named_rex = _NamedRex(zero_rex, open_name)
        close_named_rex = _NamedRex(zero_rex, close_name)
        super().__init__(concat([open_named_rex, rex, close_named_rex]))
        
class _NamedRex(RegexWrapper):
    'i.e. (?P<name>); using at CaptureRex::begin/end(open/close)'
    def __init__(self, rex, name):
        if name is None:
            raise ValueError('name should not be None which means not existing')
        super().__init__(rex)
        self.__name = name
    
    @property
    def regex_id(self):
        return self.__name
    

def full_set2RexType(full_set, RexABC):
    class __RexABC2RexT(RexABC):
        __full_set = full_set
        
        def full_tokenset(self):
            return self.__full_set
    return __RexABC2RexT
##def concat(rex_ls):
##    return ConcatRex(rex_ls)
##def choice(rex_ls):
##    return ChoiceRex(rex_ls)

def rex2zero_rex(rex):
    full_set = rex.full_tokenset()
    

def check_uint(n):
    if type(n) is not int:
        raise TypeError('type(n) is not int')
    if n < 0:
        raise ValueError('n<0')
class FullSetOfferABC:
    @abstractmethod
    def concat(self, rex_ls):pass
    @abstractmethod
    def choice(self, rex_ls):pass
    
    ################# auto ##################
    
    def star(self, rex):
        # x*
        return StarRex(rex)
    def neg_(self, rex):
        # neg x
        if isinstance(rex, NegRex):
            return ~rex
        return NegRex(rex)
    def capture(self, rex, name):
        return CaptureRex(rex, self.zero_rex(), concat, name)

    def zero_rex(self):
        # ''
        return self.concat([])
    def false_rex(self):
        return self.choice([])
    def true_rex(self):
        return self.not_(self.false_rex())
    def optional(self, rex):
        # x?
        return self.count(rex, 0, 1)
        
    def plus(self, rex):
        # x+
        return self.count_inf(rex, 1)

        
    def repeat(self, rex, n):
        check_uint(n)
        return self.concat([rex]*n)

    def count_inf(self, rex, n):
        # {n,+inf}
        check_uint(n)
        return self.concat([self.repeat(rex, n), self.star(rex)])
    def count(self, rex, n, m):
        # {n,m}; n <= L <= m
        check_uint(n)
        check_uint(m)
        if m < n:
            raise ValueError('regex"x{n,m}" : m<n')
        return self.choice([self.repeat(rex, i) for i in range(n,m)])


class FullSetOffer(FullSetOfferABC):
    def __init__(self, full_tokenset):
        #self.__full = full_tokenset
        self.ConcatRexT, self.ChoiceRexT = map(
            lambda ABC: full_set2RexType(full_tokenset, ABC),
            [ConcatRexABC, ChoiceRexABC])

    def concat(self, rex_ls):
        return self.ConcatRexT(rex_ls)
    def choice(self, rex_ls):
        return self.ChoiceRexT(rex_ls)


def rex2jumps(rex):
    '''map nstate to uint_state

new_nstate = ((name,...), nstate) # capture open/close rex final state names
with diff names or diff is_final:
    nstate can not be merged together
    but may be deleted

merge nstates:
    del non-reachable # init --.NoPath.-->> xx
    merge non-success into fail # xx --.NoPath.-->> final
    subgraphs without outgoings:
        NOTE:
            names and is_final is vtx color
            input_tokens is dedge label
        if a such subgraph whose vtcs are of same color, then merge it to one vtx
        if two such subgraphs are color-label-isomorphism:
            they can merge into one subgraph
'''
    raise ...

    
        
