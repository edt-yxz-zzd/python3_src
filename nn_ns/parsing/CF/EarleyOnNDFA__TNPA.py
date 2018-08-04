

'''
GrammarTNPA:
    TNPA - T:terminal; N:null sequence; P:pair; A:alternative


EarleyOnNDFA(terminals, null_nonterminals, pair_nonterminal2pair, alt_nonterminal2sub_alts)
    # allow multiple start symbols for CFG
    add_start_symbols(start_symbols)

    # allow mutiple initial states for FA since NDFA
    # but donot know all states and final states, e.g. len(tokens) is unknown
    add_initial_states(initial_states)
    
    # since NDFA ==>> null-transition
    # feed(maybe_terminal, begin_state, end_state)
    feed_terminal(terminal, begin_state, end_state)
    feed_null(begin_state, end_state)

    # out_terminals = {(terminal, begin_state, end_state)}
    # out_null_nonterminals = {(null_nonterminal, begin_state, end_state)}
    #     since null-transition:
    #         out_terminals >= those from feed
    #         out_null_nonterminals : end_state may not be begin_state
    # out_alt_nonterminal2sub_alts =
    #       {(alt_nonterminal, begin_state, end_state):
    #          {(sub_symbol, begin_state, end_state)}
    #       }
    # out_pair_nonterminal2middle_alts =
    #       {(pair_nonterminal, begin_state, end_state):
    #          {(pair_nonterminal, begin_state, middle_state, end_state)}
    #       }
    # out_pair_nonterminal_middle2pair =
    #       {(pair_nonterminal, begin_state, middle_state, end_state):
    #          ( (fst_symbol, begin_state, middle_state),
    #            (snd_symbol, middle_state, end_state)
    #          )
    #       }
    # end_state2out_start_symbols = {end_state: {(start_symbol, initial_state, end_state)}}
    get_partial_out_grammar()
    # out_start_symbols = {(start_symbol, initial_state, final_state)}
    get_out_start_symbols(final_states)


BNF to TNPA example:
    S = a B C
    S = Dead
    S = 
    B = S b
    C = c
    ===>> TSA
    S[-1] { S[0] S[1] S[2] }
    B[-1] { B[0] }
    C[-1] { C[0] }
    S[0] = a[-1] B[-1] C[-1]
    S[1] = Dead[-1]
    S[2] = 
    B[0] = S[-1] b[-1]
    C[0] = c[-1]
    
    ===>> TNPA
    T : {a[-1][0], b[-1][0], c[-1][0]}
    N : {S[0][3], S[1][1], S[2][0],
         B[0][2],
         C[0][1]
        }
    P : {S[0][0]: (a[-1][0], S[0][1]),
         S[0][1]: (B[-1][0], S[0][2]),
         S[0][2]: (C[-1][0], S[0][3]),

         S[1][0]: (Dead[-1][0], S[1][1]),

         B[0][0]: (S[-1][0], B[0][1]),
         B[0][1]: (b[-1][0], B[0][2]),
         
         C[0][0]: (c[-1][0], C[0][1]),
         }
    A : {S[-1][0]: {S[0][0], S[1][0], S[2][0]},
         B[-1][0]: {B[0][0]},
         C[-1][0]: {C[0][0]},
         Dead[-1][0]: {},
        }
    
TSA to TNPA example:
    S { a B D }
    B = b C
    C =
    D { }
    ==>>
    T : {a[0], b[0]}
    N : {B[2], C[0]}
    P : {B[0]: (b[0], B[1]),
         B[1]: (C[0], B[2]),
        }
    A : {S[0] : {a[0], B[0], D[0]},
         D[0] : {}
        }

covert back to TSA from TNPA:
    for non_null seq_rule S = ... A :
        S_begin_end = ..._begin_middle A_middle_end' S[L]_end'_end
        total L+2 states!!
        S[L] is in out_null_nonterminals
        assert exists A_middle_end S[L]_end_end
        ==>> eliminate S[L] ==>> L+1 states
        for nonunit S:
            ==>> S_s0_sL {S_s0_s1..sL, ...}
            ==>> S_s0_s1..sL = rule[S][0]_s0_s1 ... rule[S][L]_s(L-1)_sL
        but for unit S:
            ==>> S_s0_s1 = rule[S][0]_s0_s1 or S_s0_s1 { rule[S][0]_s0_s1 }
        to avoid above situation:
            S_s0...sL {S_(s0,...sL), ...}
            now S_s0_s1 is not S_(s0,s1), i.e. (S, s0, s1) != (S, (s0, s1))
    for alt_rule A { B, ...} :
        ==>> A_begin_end { B_begin_end, ...}
    for null seq_rule N:
        ==>> N_begin_end # to avoid S_begin_end = N_begin_begin N_end_end fail...
    for terminal t:
        ==>> t_begin_end

    (symbol, begin, end) ==>> out_alt_symbol/out_terminal
    (symbol, [state]) ==>> out_seq_symbol

'''


__all__ = '''
    EarleyOnNDFA
    feed_tokens
'''.split()



from collections.abc import Set, Sequence
from itertools import chain
# from sand.types.tuple_based_maybe import nothing, just, unjust


def is_pair(pair):
    return isinstance(pair, Sequence) and len(pair) == 2
def is_Set(s):
    return isinstance(s, Set)

def set_defaultfactory(a2bs, a, factory=set):
    if a not in a2bs:
        a2bs[a] = factory()
    return a2bs[a]


def check_EarleyOnNDFA_args(
    terminals, null_nonterminals, pair_nonterminal2pair, alt_nonterminal2sub_alts):
    
    args = (terminals, null_nonterminals,
            pair_nonterminal2pair, alt_nonterminal2sub_alts)
    all_symbols = frozenset().union(*args)
    if not sum(map(len, args)) == len(all_symbols):
        raise ValueError('not disjoint : terminals, null_nonterminals, pair_nonterminals, alt_nonterminals')

    
    if not all(map(is_pair, pair_nonterminal2pair.values())):
        raise ValueError('not all pairs')
    if not all(map(is_Set, alt_nonterminal2sub_alts.values())):
        raise ValueError('not all Sets')

    if not all(map(all_symbols.__contains__,
                   chain.from_iterable(
                       chain(pair_nonterminal2pair.values(),
                             alt_nonterminal2sub_alts.values()
                             )
                       ))):
        raise ValueError('undefined symbol exist')


# wanting types
ROOT_WANTING = 'ROOT_WANTING' # ()
BEGIN = 'BEGIN'
SYMBOL_BEGIN = 'SYMBOL_BEGIN'
SYMBOL_BEGIN_MIDDLE = 'SYMBOL_BEGIN_MIDDLE'

length2wanting_type = ROOT_WANTING, BEGIN, SYMBOL_BEGIN, SYMBOL_BEGIN_MIDDLE
{
    0: ROOT_WANTING,
    1: BEGIN,
    2: SYMBOL_BEGIN,
    3: SYMBOL_BEGIN_MIDDLE,
}

if 0:
        T = self.to_wanting_type(wanting)
        if T == BEGIN:
            begin, = wanting
        elif T == SYMBOL_BEGIN:
            symbol, begin = wanting
        elif T == SYMBOL_BEGIN_MIDDLE:
            # pair_symbol/terminal, begin, middle
            symbol, begin, middle = wanting
        elif T == ROOT_WANTING:
            ...
        else:
            raise logic-error - unknown-case


def dir_show(obj):
    from pprint import pprint
    from inspect import isroutine
    d = {name : getattr(obj, name)
         for name in dir(obj)
         if not name.startswith('_') and not isroutine(getattr(obj, name))
        }
    pprint(d)


class EarleyOnNDFA:
    def __init__(self,
                 terminals, null_nonterminals,
                 pair_nonterminal2pair, alt_nonterminal2sub_alts,
                 *,
                 start_symbols = (),
                 initial_states = ()):
        self.terminals = terminals
        self.null_nonterminals = null_nonterminals
        self.pair_nonterminal2pair = pair_nonterminal2pair
        self.alt_nonterminal2sub_alts = alt_nonterminal2sub_alts
        
        check_EarleyOnNDFA_args(
            terminals, null_nonterminals, pair_nonterminal2pair, alt_nonterminal2sub_alts)

        self.__start_symbols = set(start_symbols)
        self.__initial_states = set(initial_states)
        self.clear()

    def clear(self):
        # wanted/wanting :: () | (begin_state,) | (symbol, begin_state)
        #                 | (pair_symbol, begin_state, middle_state)
        #                 | (terminal, begin_state, end_state) # want null-transition
        # wanted_instance :: (begin_state, end_state) | (symbol, begin_state, end_state) | (symbol, begin_state, middle_state, end_state)
        # wanted -> instance :
        #   () -> (start_symbol, initial_state, end_state)
        #   (begin_state,) -> (begin_state, end_state)
        #   (symbol, begin_state) -> (symbol, begin_state, end_state)
        #   (pair_symbol, begin_state, middle_state) -> (pair_symbol, begin_state, middle_state, end_state)
        #   (terminal, begin_state, end_state) -> (terminal, begin_state, end_state, end_state')
        # wanting -> wanted
        #   () -> (start_symbol, initial_state)
        #   (begin_state,) -> ; (end_state,)
        #   (terminal, begin_state) -> ; (terminal, begin_state, end_state)
        #   (null, begin_state) -> (begin_state,)
        #   (pair, begin_state) -> (fst, begin_state,); (pair, begin_state, middle_state)
        #   (alt, begin_state) -> (sub, begin_state,)
        #   (pair_symbol, begin_state, middle_state) -> (snd, middle)
        #   (terminal, begin_state, end_state) -> (end_state,)

        # from on_new_wanting
        #    not include ()
        #    not include wanted that only from new_wanting_wanted or on_new_instance
        self.wantings = set()

        # wanted from new_wanting_wanted but not include those only from on_new_instance
        self.wanted2wantings = {}  # {wanted:{wanting}}

        # wanted from new_instance but not include those only from new_wanting_wanted
        self.wanted2instances = {} # {wanted:{wanted_instance}}

        # from feed or reduce
        self.instances = set()
        
        self.start_symbols = set()
        self.initial_states = set()

        self.onfunc_args_stack = [] # [(f, args)]


        # output data
        self.out_start_symbols = set()
        self.out_terminals = set()
        self.out_null_nonterminals = set()
        self.out_alt_nonterminal2sub_alts = {}
        self.out_pair_nonterminal2middle_alts = {}
        self.out_pair_nonterminal_middle2pair = {}
        # {end_state:{(start_symbol, initial_state, end_state)}}
        self.end_state2out_start_symbols = {}

        ###
        self.add_start_symbols(self.__start_symbols) 
        self.add_initial_states(self.__initial_states)


    def get_partial_out_grammar(self):
        return (self.out_start_symbols,
                self.out_terminals,
                self.out_null_nonterminals,
                self.out_alt_nonterminal2sub_alts,
                self.out_pair_nonterminal2middle_alts,
                self.out_pair_nonterminal_middle2pair,
                self.end_state2out_start_symbols,
                )
    # out_start_symbols = {(start_symbol, initial_state, final_state)}
    def get_out_start_symbols(self, final_states=None):
        if final_states is None:
            return self.out_start_symbols
        else:
            empty_set = set()
            def get(final):
                return self.end_state2out_start_symbols.get(final, empty_set)
            return set().union(*map(get, set(final_states)))
        
    def __push(self, onfunc, *args):
        self.onfunc_args_stack.append((onfunc, args))
    def __run(self):
        while self.onfunc_args_stack:
            f, args = self.onfunc_args_stack.pop()
            f(*args)

    def to_wanting_type(self, wanting):
        # ROOT_WANTING, BEGIN, SYMBOL_BEGIN, SYMBOL_BEGIN_MIDDLE
        L = len(wanting)
        return length2wanting_type[L]
    def instance2wanted(self, instance):
        return instance[:-1]
    def has_instance(self, instance):
        return instance in self.instances
            
    def add_start_symbols(self, start_symbols):
        news = set(start_symbols) - self.start_symbols
        self.start_symbols |= news
        wanting = () # root
        for start_symbol in news:
            for initial_state in self.initial_states:
                wanted = (start_symbol, initial_state)
                self.__push_wanting_wanted(wanting, wanted)
        self.__run()

    def add_initial_states(self, initial_states):
        news = set(initial_states) - self.initial_states
        self.initial_states |= news
        wanting = () # root
        for initial_state in news:
            self.__push_state(initial_state)
            for start_symbol in self.start_symbols:
                wanted = (start_symbol, initial_state)
                self.__push_wanting_wanted(wanting, wanted)
        self.__run()
        
##    def feed(self, maybe_terminal, begin_state, end_state):
##        if maybe_terminal == nothing:
##            self.feed_null(begin_state, end_state)
##        else:
##            self.feed_terminal(unjust(maybe_terminal), begin_state, end_state)

    def feed_terminal(self, terminal, begin_state, end_state):
        if terminal not in self.terminals:
            raise ValueError('feed unknown terminal')
        self.__feed__instance((terminal, begin_state, end_state))
    def feed_null(self, begin_state, end_state):
        self.__feed__instance((begin_state, end_state))
        if begin_state != end_state:
            wanting = begin_state,
            wanted = end_state,
            self.__push_wanting_wanted(wanting, wanted)

    def __feed__instance(self, instance):
        begin_state, end_state = instance[-2:]
        self.__push_state(begin_state)
        self.__push_state(end_state)
        self.__push_instance(instance)
        self.__run()
        
    def __push_state(self, state):
        self.__push_instance((state, state))
        

    def __push_instance(self, instance):
        if instance in self.instances:
            return
        self.instances.add(instance)
        self.__push(self.__on_new_instance, instance)
    def __on_new_instance(self, instance):
        self.__update_output__on_new_instance(instance)
        
        wanted = self.instance2wanted(instance)
        if wanted not in self.wanted2instances:
            self.wanted2instances[wanted] = set()
            
        assert instance not in self.wanted2instances[wanted]

        self.wanted2instances[wanted].add(instance)
        for wanting in self.wanted2wantings.get(wanted, ()):
            self.__push_new_wanting_wanted_instance(wanting, wanted, instance)

    def __push_new_wanting_wanted_instance(self, wanting, wanted, instance):
        self.__push(self.__on_new_wanting_wanted_instance, wanting, wanted, instance)
    def __push_new_wanting_instance_wanted_instance(
        self, wanting, wanting_instance, wanted, wanted_instance):
        self.__push(self.__on_new_wanting_instance_wanted_instance,
                    wanting, wanting_instance, wanted, wanted_instance)
        
    def __push_wanting_wanted(self, wanting, wanted):
        if wanted in self.wanted2wantings and \
           wanting in self.wanted2wantings[wanted]:
            return
        
        if wanted not in self.wanted2wantings:
            self.wanted2wantings[wanted] = set()
            self.__push_wanting(wanted)
        self.wanted2wantings[wanted].add(wanting)
        self.__push(self.__on_new_wanting_wanted, wanting, wanted)

    def __push_wanting(self, wanting):
        if wanting in self.wantings:
            return
        self.wantings.add(wanting)
        self.__push(self.__on_new_wanting, wanting)
    def __on_new_wanting(self, wanting):
        # wanting -> {wanted}
        T = self.to_wanting_type(wanting)
        if T == BEGIN:
            begin, = wanting
            pass
        elif T == SYMBOL_BEGIN:
            symbol, begin = wanting
            if symbol in self.terminals:
                pass
            elif symbol in self.null_nonterminals:
                wanted = begin,
                self.__push_wanting_wanted(wanting, wanted)
            elif symbol in self.pair_nonterminal2pair:
                fst, snd = self.pair_nonterminal2pair[symbol]
                wanted = fst, begin
                self.__push_wanting_wanted(wanting, wanted)
            elif symbol in self.alt_nonterminal2sub_alts:
                sub_alts = self.alt_nonterminal2sub_alts[symbol]
                for sub in sub_alts:
                    wanted = sub, begin
                    self.__push_wanting_wanted(wanting, wanted)
            else:
                raise logic-error

            
        elif T == SYMBOL_BEGIN_MIDDLE:
            # pair_symbol/terminal, begin, middle/end
            symbol, begin, middle = wanting
            if symbol in self.terminals:
                wanted = middle,
                self.__push_wanting_wanted(wanting, wanted)
            elif symbol in self.pair_nonterminal2pair:
                fst, snd = self.pair_nonterminal2pair[symbol]
                wanted = snd, middle # bug : once "snd, begin"
                self.__push_wanting_wanted(wanting, wanted)
            else:
                raise logic-error
            
        elif T == ROOT_WANTING:
            raise logic-error - root is not new
        else:
            raise logic-error - unknown-case

        
    def __on_new_wanting_wanted(self, wanting, wanted):
        # (wanting, wanted) -> {(wanting, wanted, instance)}
        if wanted in self.wanted2instances:
            for instance in self.wanted2instances[wanted]:
                self.__push_new_wanting_wanted_instance(wanting, wanted, instance)
    

 
    def __on_new_wanting_wanted_instance(self, wanting, wanted, instance):
        'reduce'
        T = self.to_wanting_type(wanting)
        if T == BEGIN:
            begin, = wanting
            assert len(instance) == 2
            wanted_begin, end = instance
            wanting_instance = begin, end
        elif T == SYMBOL_BEGIN:
            symbol, begin = wanting
            if symbol in self.terminals:
                assert len(instance) == 4
                assert wanting[0] == wanted[0]
                _symbol, _begin, _end, end = instance
                wanting_instance = symbol, begin, end
                
            elif symbol in self.null_nonterminals:
                _begin, end = instance
                wanting_instance = symbol, begin, end
            elif symbol in self.pair_nonterminal2pair:
                L = len(instance)
                if L == 3:
                    _fst, _begin, middle = instance
                    middle_wanted = symbol, begin, middle
                    self.__push_wanting_wanted(wanting, middle_wanted)
                    return
                elif L == 4:
                    _pair, _begin, _middle, end = instance
                    wanting_instance = symbol, begin, end
                else:
                    raise logic-error
                    
            elif symbol in self.alt_nonterminal2sub_alts:
                _sub_alt, _begin, end = instance
                wanting_instance = symbol, begin, end
            else:
                raise logic-error

            
        elif T == SYMBOL_BEGIN_MIDDLE:
            # pair_symbol/terminal, begin, middle
            symbol, begin, middle = wanting
            if symbol in self.terminals:
                _middle, end = instance
                wanting_instance = symbol, begin, middle, end
            elif symbol in self.pair_nonterminal2pair:
                _snd, _middle, end = instance
                wanting_instance = symbol, begin, middle, end
            else:
                raise logic-error
            
        elif T == ROOT_WANTING:
            wanting_instance = instance
        else:
            raise logic-error - unknown-case

        if T != ROOT_WANTING:
            assert self.instance2wanted(wanting_instance) == wanting
            self.__push_instance(wanting_instance)
        
        self.__push_new_wanting_instance_wanted_instance(
            wanting, wanting_instance, wanted, instance)
        
        
    def __on_new_wanting_instance_wanted_instance(
        self, wanting, wanting_instance, wanted, wanted_instance):
        self.__update_output__on_new_wanting_instance_wanted_instance(
            wanting, wanting_instance, wanted, wanted_instance)

    def __update_output__on_new_instance(self, instance):
        wanted = self.instance2wanted(instance)
        T = self.to_wanting_type(wanted)
        if T == SYMBOL_BEGIN:
            symbol, begin = wanted
            if symbol in self.terminals:
                self.out_terminals.add(instance)
        
    def __update_output__on_new_wanting_instance_wanted_instance(
        self, wanting, wanting_instance, wanted, wanted_instance):
        # update output data
        
        T = self.to_wanting_type(wanting)
        if T == BEGIN:
            begin, = wanting
            pass
        elif T == SYMBOL_BEGIN:
            symbol, begin = wanting
            if symbol in self.terminals:
                # since not all out_terminals are come from reduce
                # some from feed ==>> move update action to on_new_instance
                pass 
            elif symbol in self.null_nonterminals:
                self.out_null_nonterminals.add(wanting_instance)
            elif symbol in self.pair_nonterminal2pair:
                L = len(wanted_instance)
                assert L == 4
                set_defaultfactory(self.out_pair_nonterminal2middle_alts,
                                   wanting_instance).add(wanted_instance)
                
                _symbol, _begin, middle, end = wanted_instance
                fst, snd = self.pair_nonterminal2pair[symbol]
                out_fst = fst, begin, middle
                out_snd = snd, middle, end
                out_pair = wanted_instance
                set_defaultfactory(self.out_pair_nonterminal_middle2pair,
                                   out_pair).add((out_fst, out_snd))
        
            elif symbol in self.alt_nonterminal2sub_alts:
                set_defaultfactory(self.out_alt_nonterminal2sub_alts,
                                   wanting_instance).add(wanted_instance)
            else:
                raise logic-error

        elif T == SYMBOL_BEGIN_MIDDLE:
            # pair_symbol/terminal, begin, middle
            symbol, begin, middle = wanting
            if symbol in self.terminals:
                pass
            elif symbol in self.pair_nonterminal2pair:
                pass
            else:
                raise logic-error
        elif T == ROOT_WANTING:
            out_start_symbol = wanting_instance
            self.out_start_symbols.add(out_start_symbol)
            assert len(out_start_symbol) == 3
            start_symbol, initial_state, end_state = out_start_symbol
            set_defaultfactory(self.end_state2out_start_symbols,
                               end_state).add(out_start_symbol)
        else:
            raise logic-error - unknown-case




def make_begin_state(parser, begin_state):
    '''
if begin_state is None:
    then begin_state = 0 and is a initial_state
else:
    begin_state may not be a initial_state
'''
    if begin_state is None:
        begin_state = 0
        parser.add_initial_states([begin_state])
    return begin_state

def feed_tokens(parser, tokens, begin_state=None):
    '''
assume NDFA be :
    state_i -> tokens[i] state_(i+1)
    where begin_state <= i < begin_state + len(tokens)
if begin_state is None:
    then begin_state = 0 and is a initial_state
else:
    begin_state may not be a initial_state

return begin_state, begin_state + len(tokens) # begin_state, end_state
'''
    begin_state = make_begin_state(parser, begin_state)
    
    i = begin_state - 1
    for i, t in enumerate(tokens, begin_state):
        parser.feed_terminal(t, i, i+1)
    return begin_state, i + 1
    print(p.get_out_start_symbols())
    print(p.get_partial_out_grammar())
    dir_show(p)




class FeedConst:
    def __init__(self, tokens):
        self.tokens = tuple(tokens)
    def __call__(self, parser, begin_state=None):
        return feed_tokens(parser, self.tokens, begin_state)

class ConcatFeeds:
    def __init__(self, feeds):
        'feeds :: [parser->begin_state->(begin_state, end_state)]'
        self.feeds = tuple(feeds)
    def __call__(self, parser, begin_state=None):
        begin_state = end_state = make_begin_state(parser, begin_state)
        for feed in self.feeds:
            _, end_state = feed(parser, end_state)
        return begin_state, end_state

def feed_star_any(parser, begin_state=None):
    '''feed .* ; productive??

NDFA:
    state_begin -> any_token state_begin
'''
    begin_state = end_state = make_begin_state(parser, begin_state)
    for t in parser.terminals:
        parser.feed_terminal(t, begin_state, begin_state)
    return begin_state, end_state



class Feed_StarAny_Const:
    '''const is a sentence suffix??

NDFA be '.*' + tokens
    state_begin -> any_token state_begin
    state_i -> tokens[i] state_(i+1)

return begin_state, begin_state + len(tokens) # begin_state, end_state

example:
    # assume parser not construct with initial_states
    parser.clear()
    begin_state, end_state = feed_star_any_tokens(parser, tokens)
    if parser.end_state2out_start_symbols.get(end_state):
        print('tokens is a valid suffix')
'''
    def __init__(self, tokens):
        self._f = ConcatFeeds([feed_star_any, FeedConst(tokens)])
    def __call__(self, parser, begin_state=None):
        return self._f(parser, begin_state)

class Feed_Const_StarAny:
    'const is a sentence prefix??'
    def __init__(self, tokens):
        self._f = ConcatFeeds([FeedConst(tokens), feed_star_any])
    def __call__(self, parser, begin_state=None):
        return self._f(parser, begin_state)

'''

const contains a sentence??
    begin, end = FeedConst(tokens)(parser)
    inits = range(begin, end+1)
    finals = range(begin, end+1)
    parser.add_start_symbols(inits)
    if parser.get_out_start_symbols():
        print('const contains a sentence')

const starts with a sentence??
    begin, end = FeedConst(tokens)(parser)
    inits = range(begin, begin+1)
    finals = range(begin, end+1)
    parser.add_start_symbols(inits)
    if parser.get_out_start_symbols():
        print('const starts with a sentence')

const ends with a sentence??
    begin, end = FeedConst(tokens)(parser)
    inits = range(begin, end+1)
    finals = range(end, end+1)
    parser.add_start_symbols(inits)
    if parser.get_out_start_symbols():
        print('const ends with a sentence')
'''



def test_parser():
    terminals = frozenset('abc')
    null_nonterminals = frozenset('Null'.split())
    pair_nonterminal2pair = {
        'A' : ('a', 'S'),
        'B' : ('b', 'Null'),
        'C' : ('S', 'A'),
        }
    alt_nonterminal2sub_alts = {
        'S' : set('ABC'),
        }

    start_symbols = ['S']
    p = EarleyOnNDFA(terminals, null_nonterminals,
                 pair_nonterminal2pair, alt_nonterminal2sub_alts,
                 start_symbols = start_symbols)

    feed_tokens(p, 'b')
    assert p.get_out_start_symbols() == {('S', 0, 1)}
    
    p.clear()
    feed_tokens(p, 'ba')
    assert p.get_out_start_symbols() == {('S', 0, 1)}
    
    p.clear()
    feed_tokens(p, 'bab')
    assert p.get_out_start_symbols() == {('S', 0, 1), ('S', 0, 3)}
    p.add_initial_states([2])
    assert p.get_out_start_symbols() == {('S', 0, 1), ('S', 0, 3), ('S', 2, 3)}
    p.add_initial_states([1])
    assert p.get_out_start_symbols() == {('S', 0, 1), ('S', 0, 3), ('S', 2, 3), ('S', 1, 3)}
    assert p.get_out_start_symbols([1]) == {('S', 0, 1)}

    return
    dir_show(p)
    p.clear()
    
    

test_parser()



def extract_grammar_backto_TSA(parser, final_states=None):
    'assume the original TNPA is from TSA'
    out_start_symbols = parser.get_out_start_symbols(final_states)
    
    (_out_start_symbols, # >= out_start_symbols
    out_terminals,
    out_null_nonterminals,
    out_alt_nonterminal2sub_alts,
    out_pair_nonterminal2middle_alts,
    out_pair_nonterminal_middle2pair,
    end_state2out_start_symbols,
    ) = parser.get_partial_out_grammar()

    def tridotname2triname(tridotname):
        (symbol, _0), begin, end = tridotname
        assert _0 == 0
        return symbol, begin, end
    def dotname_states2name_states(dotname_states):
        dotname_states
    gram_info = {tridotname2triname(t): None
                 for t in out_terminals}
    gram_info.update(tridotname2triname(N): ()
                     for N in out_null_nonterminals)
    gram_info.update(tridotname2triname(A): frozenset(map(tridotname2triname, sub_alts))
                     for A, sub_alts in out_alt_nonterminal2sub_alts.items())



    # flatten pairs into seqs
    out_pairs_with_idx0 = set()
    out_pair2nexts = defaultdict(set) # {out_pair:{out_pair|out_null}}
    for out_pair, middle_alts in out_pair_nonterminal2middle_alts.items():
        (symbol, idx), begin, end = out_pair
        if idx == 0:
            out_pairs_with_idx0.add(out_pair)

        for alt in middle_alts:
            if alt not in out_pair_nonterminal_middle2pair:
                continue
            out_fst, out_snd = out_pair_nonterminal_middle2pair[alt]
            (_symbol, next_idx), middle, _end = out_snd
            assert symbol == _symbol
            assert idx + 1 == next_idx
            assert end == _end
            out_pair2nexts[out_pair].add(out_snd)
    # tree search
    for out_pair in out_pairs_with_idx0:
        triname = tridotname2triname(out_pair)
        states_set = gram_info[triname] = set()
        _, _, END = out_pair
        
        def push(out_pair):
            (symbol, idx), begin, end = out_pair
            path.append(out_pair, iter(out_pair2nexts[out_pair]))
            states.append(begin)
        def pop():
            path.pop()
            states.pop()
        
        path = []
        states = []
        push(out_pair)
        while path:
            _, it = path[-1]
            for out_pair in it:
                break
            else:
                pop()
                continue

            if out_pair not in out_null_nonterminals:
                # nonleaf or undefined leaf
                push(out_pair)
                continue

            # leaf
            out_null = out_pair
            _, begin, end = out_null
            if begin != end:
                # we want to discard S[L], so, require S[L]_begin_begin
                continue
            assert end == END
            states.append(begin)
            states_set.add(tuple(states))
            states.pop()
            
    for out_pair in out_pairs_with_idx0:
        symbol, _, _ = triname = tridotname2triname(out_pair)
        states_set = gram_info[triname]
        gram_info[triname] = frozenset((symbol, states) for states in states_set)

        for states in states_set:
            break
        else:
            continue

        end = states[-1]
        rule = []
        for idx, (begin, middle) in enumerate(zip(states, states[1:])):
            dot_symbol = symbol, idx
            out_pair_middle = dot_symbol, begin, middle, end
            out_fst, _ = out_pair_nonterminal_middle2pair[out_pair_middle]
            dot_fst, _, _ = out_fst
            fst_symbol, _, _ = trifst = tridotname2triname(dot_fst)
            rule.append(fst_symbol)
        assert rule
        assert len(rule) == len(states) - 1
        for states in states_set:
            gram_info[(symbol, states)] = tuple(zip(rule, states, states[1:]))

        
    start_symbols = frozenset(map(tridotname2triname, out_start_symbols))
    return gram_info, start_symbols

        






