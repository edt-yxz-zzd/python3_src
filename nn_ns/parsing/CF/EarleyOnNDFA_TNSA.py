

'''
GrammarTNSA:
    TNSA - T:terminal; N:null sequence; S:nonempty sequence; A:alternative
    recommend :
        1) prefer alt rule to unit seq rule
        2) prefer short seq rule, best pair
            why not long seq?
                S = S S... S # assume len(right_part) = L
                S = a
                S =

                parser S over 'a'*N
                ==>> the out_start S_0_N has C(N+L-1, L-1) alternatives
                ==>> since there are C(N, 2) out S_x_y
                ==>> size of out grammar is O(N, L+1)
                that is if used pair only, worst case will be O(N, 3)
    why not merge N into S??
        since null_nonterminal is like a terminal has only one known sentence
        null_nonterminal -->> null transition
        terminal -->> normal transition
    


EarleyOnNDFA(terminals, null_nonterminals, seq_nonterminal2seq, alt_nonterminal2sub_alts)
    # allow multiple start symbols for CFG
    add_start_symbols(start_symbols)

    # allow mutiple initial states for FA since NDFA
    # but donot know all states and final states, e.g. len(tokens) is unknown
    add_initial_states(initial_states)

    # allow to redefined undefined rule (i.e. empty alt rule) to null/seq/alt rule
    # allow use undefined nonterminal which is assgined with undefined rule
    # allow to extend alt rule
    # allow to add new rule, i.e. define new nonterminal
    # not allow to modify exist null/seq rule
    # rules :: [rule]
    # rule = (undefined_nonterminal,) # define new null rule
    #      # define new unit alt/seq rule; # <<==prefer_unit_seq_rule
    #      # or add to exist alt rule;
    #      | (undefined/alt_nonterminal, symbol)
    #      # define new nonempty and nonunit seq rule
    #      | (undefined_nonterminal, symbol, symbol, *symbols) 
    # undefined_nonterminal = nonexist_nonterminal | empty_alt_nonterminal
    add_new_rules(self, rules, prefer_unit_seq_rule = False)
    
    # since NDFA ==>> null-transition
    # feed(maybe_terminal, begin_state, end_state)
    feed_terminal(terminal, begin_state, end_state)
    feed_null(begin_state, end_state)


    # out_alt_symbol/out_terminal/out_null_symbol :: (symbol, begin, end)
    # out_seq_symbol :: (symbol, [state])
    # out_terminals = {(terminal, begin_state, end_state)}
    # out_null_nonterminals = {(null_nonterminal, begin_state, end_state)}
    #     since null-transition:
    #         out_terminals >= those from feed
    #         out_null_nonterminals : end_state may not be begin_state
    # out_altalt_nonterminal2sub_alts =
    #       {(alt_nonterminal, begin_state, end_state):
    #          {(sub_symbol, begin_state, end_state)}
    #       }
    # out_altseq_nonterminal2sub_alts =
    #       {(seq_nonterminal, begin_state, end_state):
    #          {(seq_nonterminal, (begin_state, *middle_states, end_state))}
    #       }
    # out_seq_nonterminal2seq =
    #       {(seq_nonterminal, (begin_state, *middle_states, end_state)):
    #          ( (first_symbol, begin_state, second_state),
    #            ...
    #            (last_symbol, (end-1)_state, end_state)
    #          )
    #       }
    # end_state2out_start_symbols = {end_state: {(start_symbol, initial_state, end_state)}}
    get_partial_out_grammar()
    # out_start_symbols = {(start_symbol, initial_state, final_state)}
    get_out_start_symbols(final_states)


BNF to TNSA example:
    S = a B C
    S = Dead
    S = 
    B = S b
    C = c
    ===>> TSA
    S[0] { S[1] S[2] S[3]}
    B[0] { B[1] }
    C[0] { C[1] }
    S[1] = a[0] B[0] C[0] ;
    S[2] = Dead[0] ;
    S[3] = ;
    B[1] = S[0] b[0] ;
    C[1] = c[0] ;
    ===>> TNSA
    T : {a[0], b[0], c[0]}
    N : {S[3]}
    S : {S[1]: (a[0], B[0], C[0]),
         S[2]: (Dead[0],),
         B[1]: (S[0], b[0]),
         C[1]: (c[0],),
         }
    A : {S[0]: {S[1], S[2], S[3]},
         B[0]: {B[1]},
         C[0]: {C[1]},
         Dead[0]: {},
        }
    






######################### wanting/wanted/instance
# seq == nonempty seq
nonseq_symbol = terminal | null_symbol | alt_symbol
wanting = () | wanted # () is virtual wanting root
wanted  = (begin,) # wanted null-transition by null_nonterminal/out_terminal
        | (symbol, begin)  # wanted symbol at begin
        | (seq_symbol, idx, begin) # wanted rule(symbol)[idx:] at begin, 0 <= idx < L-1

wanting -> instance
    # since not known final_states yet, using any_end_state instead of final_state
    () -> (start_symbol, initial_state, any_end_state)

    # wanted -> instance
    (begin,) -> (begin, end) # auto generate instance (begin, begin)
    (symbol, begin) -> (symbol, begin, end)
    (seq_symbol, idx, begin) -> (seq_symbol, idx, begin, (begin, (...)))
    # where 0 <= idx < L == len(rule(seq_symbol))
    # e.g. (seq_symbol, L-1, begin, (begin, (end, ())))
    # why not (seq_symbol, idx, (begin, (...)))
    #     since I want : wanted == wanted_instance[:-1]
    #        not include () since it belongs to wanting

wanting -> wanted
    () -> (start_symbol, initial_state)
    (begin,) -> (begin', ) if (begin, begin') is a null-transition
    (terminal, begin) -> (end,) if (terminal, begin, end) is a transition
    (null, begin) -> (begin,)
    (alt, begin) -> (sub_alt, begin)
    (seq, begin) -> (seq, 0, begin)
    (seq, i, begin) -> (rule(seq)[i], begin);
                    -> (seq, i+1, middle) if i+1 < L
                                            and (rule(seq)[i], begin, middle) is an instance
    

instance <- ??
    (begin, begin) <- [begin is a state]
    (begin, end) <- [(begin, end) is a null-transition]
    (begin, end) <- [(begin, end',) is an instance]
                and [(begin,) wanted (end',)]
                and [(end', end) is an instance]
    (terminal, begin, end) <- [(terminal, begin, end) is a transition]
    (terminal, begin, end) <- [(terminal, begin, end') is instance]
                          and [(terminal, begin,) wanted (end',)]
                          and [(end', end) is an instance]
    (null, begin, end) <- [(null, begin,) wanted (begin,)]
                      and [(begin, end) is an instance]
    (alt, begin, end) <- [(alt, begin) wanted (sub_alt, begin)]
                     and [(sub_alt, begin, end) is instance]
    (seq, begin, end) <- [(seq, begin) wanted (seq, 0, begin)]
                     and [(seq, 0, begin, (begin, (...(end, ())...))) is an instance]
    (seq, L-1, begin, (begin, (end, ())))
            <- [(seq, L-1, begin) wanted (rule(seq)[-1], begin)]
           and [(rule(seq)[-1], begin, end)] is an instance]
    (seq, i, begin, (begin, tails)) where 0 <= i < L-1
            <- [(seq, i, begin) wanted (rule(seq)[i], begin)]
           and [(rule(seq)[i], begin, middle) is an instance]
           and [(seq, i, begin) wanted (seq, i+1, middle)]
           and [(seq, i+1, middle, tails) is an instance]




actions:
    # add_start_symbols, add_initial_states ->
    on_new_root_wanted(root_wanted):
        # root_wanted == (start_symbol, initial_state)
        push_..._new_wanting_wanted((), root_wanted)
    
    push_maybe_new_wanting_wanted(wanting, wanted):
        push_maybe_new_wanted(wanted)
        ?-> on_new_wanting_wanted...
    on_new_wanting_wanted(wanting, wanted):
        # no : push_maybe_new_wanting(wanting)
        # no : push_maybe_new_wanting(wanted)
        for any wanted_instance:
            push_new_wanting_wanted_instance(wanting, wanted, wanted_instance)

    push_maybe_new_wanted
    on_new_wanted(input_wanted):
        wanting = input_wanted
        for any wanting -> wanted:
            push_..._new_wanting_wanted(wanting, wanted)

    push_maybe_new_instance
    on_new_instance(instance):
        # may not a really wanted, i.e. on_new_wanted(wanted) not happened
        fake_wanted = instance2wanted(instance)
        for any wanting -> fake_wanted:
            push_new_wanting_wanted_instance(wanting, fake_wanted, instance)

    push_new_wanting_wanted_instance
    on_new_wanting_wanted_instance(wanting, wanted, wanted_instance):
        for any wanting_instance:
            push_new_wanting_instance_wanted_instance(wanting, wanting_instance, wanted, wanted_instance)
        for any new_wanted:
            on_new_wanting_wanted(wanting, new_wanted)
    

'''


__all__ = '''
    EarleyOnNDFA
    feed_tokens
'''.split()



from collections.abc import Set, Sequence
from itertools import chain
# from sand.types.tuple_based_maybe import nothing, just, unjust
from seed.types.pair_based_leftward_list import leftward_list2last, leftward_list2list



def is_nonempty_seq(seq):
    return isinstance(seq, Sequence) and seq

def is_Set(s):
    return isinstance(s, Set)

def set_defaultfactory(a2bs, a, factory=set):
    if a not in a2bs:
        a2bs[a] = factory()
    return a2bs[a]


def check_EarleyOnNDFA_args(
    terminals, null_nonterminals, seq_nonterminal2seq, alt_nonterminal2sub_alts,
    *, allow_undefined_nonterminals = False):
    
    args = (terminals, null_nonterminals,
            seq_nonterminal2seq, alt_nonterminal2sub_alts)
    defined_symbols = set().union(*args)
    if not sum(map(len, args)) == len(defined_symbols):
        raise ValueError('not disjoint : terminals, null_nonterminals, seq_nonterminals, alt_nonterminals')

    
    if not all(map(is_nonempty_seq, seq_nonterminal2seq.values())):
        raise ValueError('not all nonempty sequences')
    if not all(map(is_Set, alt_nonterminal2sub_alts.values())):
        raise ValueError('not all Sets')

    used_symbols = set(chain.from_iterable(
                           chain(seq_nonterminal2seq.values(),
                                 alt_nonterminal2sub_alts.values()
                                 )
                       ))

    undefined_symbols = used_symbols - defined_symbols
    if undefined_symbols:
        if not allow_undefined_nonterminals:
            raise ValueError('undefined symbols exist : {}'.format(undefined_symbols))
        # alt_nonterminal2sub_alts.update((dead, set()) for dead in undefined_symbols)
    return defined_symbols, undefined_symbols



    


# wanting types
STR_WANTING_TYPE = False
NUM_WANTING_TYPE = True
if STR_WANTING_TYPE:
    ROOT_WANTING = 'ROOT_WANTING' # ()
    BEGIN = 'BEGIN'
    SYMBOL_BEGIN = 'SYMBOL_BEGIN'
    SEQ_IDX_BEGIN = 'SEQ_IDX_BEGIN'
elif NUM_WANTING_TYPE:
    ROOT_WANTING = 'ROOT_WANTING' # ()
    BEGIN = 'BEGIN'
    SYMBOL_BEGIN = 'SYMBOL_BEGIN'
    SEQ_IDX_BEGIN = 'SEQ_IDX_BEGIN'
else:
    raise logic-error

length2wanting_type = ROOT_WANTING, BEGIN, SYMBOL_BEGIN, SEQ_IDX_BEGIN


def wanting2type(wanting):
    return length2wanting_type[len(wanting)]
def wanted2type(wanted):
    if wanted == ():
        raise ValueError('() is a wanting but not a wanted')
    else:
        wanting = wanted
    return wanting2type(wanting)
    
def instance2wanted_type(instance):
    return length2wanting_type[len(instance)-1]
def instance2wanted(instance):
    # not to wanting!!
    return instance[:-1]

{
    0: ROOT_WANTING,
    1: BEGIN,
    2: SYMBOL_BEGIN,
    3: SEQ_IDX_BEGIN,
}

if 0:
        T = self.to_wanting_type(wanting)
        if T == BEGIN:
            begin, = wanting
        elif T == SYMBOL_BEGIN:
            symbol, begin = wanting
        elif T == SEQ_IDX_BEGIN:
            seq_symbol, idx, begin = wanting
        elif T == ROOT_WANTING:
            assert wanting == ()
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

def copy_to_key2tuple(d):
    return {key: tuple(seq) for key, seq in d.items()}

def copy_to_key2set(d):
    return {key: set(s) for key, s in d.items()}

def _copy_EarleyOnNDFA_args(args):
    (defined_symbols, undefined_symbols,
     terminals, null_nonterminals,
     seq_nonterminal2seq, alt_nonterminal2sub_alts,
     start_symbols, initial_states) = args
    return (set(defined_symbols), set(undefined_symbols),
            set(terminals), set(null_nonterminals),
            copy_to_key2tuple(seq_nonterminal2seq),
            copy_to_key2set(alt_nonterminal2sub_alts),
            set(start_symbols), set(initial_states)
            )
    

class EarleyOnNDFA: # __TNSA:
    def __init__(self,
                 terminals, null_nonterminals,
                 seq_nonterminal2seq, alt_nonterminal2sub_alts,
                 *,
                 start_symbols = (),
                 initial_states = (),
                 allow_undefined_nonterminals = False):
        
        defined_symbols, undefined_symbols = check_EarleyOnNDFA_args(
            terminals, null_nonterminals,
            seq_nonterminal2seq, alt_nonterminal2sub_alts,
            allow_undefined_nonterminals = allow_undefined_nonterminals)
        if undefined_symbols:
            assert allow_undefined_nonterminals

        args = (defined_symbols, undefined_symbols,
                terminals, null_nonterminals,
                seq_nonterminal2seq, alt_nonterminal2sub_alts,
                start_symbols, initial_states)
        self.__args = _copy_EarleyOnNDFA_args(args)
        self.clear()

    def __reset(self):
        args = _copy_EarleyOnNDFA_args(self.__args)
        (defined_symbols, undefined_symbols,
                 terminals, null_nonterminals,
                 seq_nonterminal2seq, alt_nonterminal2sub_alts,
                 start_symbols, initial_states) = args
        
        self.defined_symbols = defined_symbols
        self.undefined_symbols = undefined_symbols
        self.terminals = terminals
        self.null_nonterminals = null_nonterminals
        self.seq_nonterminal2seq = seq_nonterminal2seq
        self.alt_nonterminal2sub_alts = alt_nonterminal2sub_alts
        self.start_symbols = start_symbols
        self.initial_states = initial_states
        
    def add_new_nonterminals(self, undefined_symbols):
        raise TODO - update-wanteds

        undefined_symbols = set(undefined_symbols)
        if not self.defined_symbols.isdisjoint(undefined_symbols):
            existed_symbols = self.defined_symbols & undefined_symbols
            raise ValueError('not all new symbols : {}'.format(existed_symbols))
        self.alt_nonterminal2sub_alts.update((dead, set()) for dead in undefined_symbols)
        self.defined_symbols.update(undefined_symbols)

    def __handle_rules(self, rules):
        for rule in rules:
            self.add_new_nonterminals(set(rule) - self.defined_symbols)
            undefined_nonterminal, *symbols = rule
            assert undefined_nonterminal in self.defined_symbols
            
            if undefined_nonterminal not in self.alt_nonterminal2sub_alts:
                raise ValueError('redefine terminal/null/seq rule')
            yield undefined_nonterminal, symbols
        
    def add_new_rules(self, rules, prefer_unit_seq_rule = False):
        raise TODO - update-wanteds
        for undefined_nonterminal, symbols in self.__handle_rules(rules):
            alt = undefined_nonterminal
            if not prefer_unit_seq_rule and len(symbols) == 1:
                'add to alt rule'
                symbol, = symbols
                self.alt_nonterminal2sub_alts[alt].add(symbol)
                continue

            ## define null/seq rule
            if self.alt_nonterminal2sub_alts[alt]:
                # not undefined rule
                raise ValueError('redefine nonempty alt rule to null/seq rule')
            
            del self.alt_nonterminal2sub_alts[alt]
            if symbols:
                self.seq_nonterminal2seq[undefined_nonterminal] = symbols
            else:
                self.null_nonterminal.add(undefined_nonterminal)

                
        
    def clear(self):
        self.__reset()
        
        if self.undefined_symbols:
            # assert allow_undefined_nonterminals
            # assign default definition
            self.add_new_nonterminals(self.undefined_symbols)
            self.undefined_symbols.clear()

        
        # from on_new_wanting_wanted <- push_maybe_new_wanting_wanted
        #    not include those wanteds only from on_new_instance
        self.wanted2wantings = {}  # {wanted:{wanting}}

        # fake_wanted from on_new_instance + on_new_wanting_wanted
        self.fake_wanted2instances = {} # {wanted:{wanted_instance}}

        # from feed or reduce
        self.instances = set()
        

        # these two should be empty while return to user space
        self.onfunc_args_stack = [] # [(f, args)]
        self.tmp_new_wanting_wanted_pairs = set() # [(wanting, wanted)]


        # output data
        self.out_start_symbols = set()
        self.out_terminals = set()
        self.out_null_nonterminals = set()
        self.out_altalt_nonterminal2sub_alts = {}
        self.out_altseq_nonterminal2sub_alts = {}
        self.out_seq_nonterminal2seq = {}
        # {end_state:{(start_symbol, initial_state, end_state)}}
        self.end_state2out_start_symbols = {}

        ###
        start_symbols = self.start_symbols
        initial_states = self.initial_states
        self.start_symbols = set()
        self.initial_states = set()
        self.add_start_symbols(start_symbols) 
        self.add_initial_states(initial_states)


    def get_partial_out_grammar(self):
        return (self.out_start_symbols,
                self.out_terminals,
                self.out_null_nonterminals,
                self.out_altalt_nonterminal2sub_alts,
                self.out_altseq_nonterminal2sub_alts,
                self.out_seq_nonterminal2seq,
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
            try:
                f(*args)
            except:
                print(self.onfunc_args_stack)
                print(args)
                raise


    def __add_new_main_wanteds(self, start_symbols, initial_states):
        wanting = () # root
        for start_symbol in start_symbols:
            for initial_state in initial_states:
                wanted = (start_symbol, initial_state)
                self.__push_wanting_wanted(wanting, wanted)
        self.__run()
        
    def add_start_symbols(self, start_symbols):
        news = set(start_symbols) - self.start_symbols
        self.start_symbols |= news
        self.__add_new_main_wanteds(news, self.initial_states)

    def add_initial_states(self, initial_states):
        news = set(initial_states) - self.initial_states
        self.initial_states |= news
        self.__add_new_main_wanteds(self.start_symbols, news)


    def feed_terminal(self, terminal, begin_state, end_state):
        if terminal not in self.terminals:
            raise ValueError('feed unknown terminal')

        self.__feed__instance((terminal, begin_state, end_state))

        # below should after __feed__instance
        # now, (terminal, begin_state, end_state) is a known transition
        wanting = terminal, begin_state
        wanted = end_state,
        self.__push_wanting_wanted(wanting, wanted)
        self.__run() # once forgot
        
    def feed_null(self, begin_state, end_state):
        if begin_state != end_state:
            wanting = begin_state,
            wanted = end_state,
            self.__push_wanting_wanted(wanting, wanted)
        self.__feed__instance((begin_state, end_state))
    def feed_state(self, state):
        self.__push_state(state)
        self.__run() # once forgot

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
        
        fake_wanted = instance2wanted(instance)
        if fake_wanted not in self.fake_wanted2instances:
            # now, fake_wanted is not a really wanted
            # here, it is used to collect instances
            self.fake_wanted2instances[fake_wanted] = set()
            
        assert instance not in self.fake_wanted2instances[fake_wanted]

        # follow line cannot move to __push_instance
        #    otherwise, some wantings may visit this instance
        #       before this function called
        self.fake_wanted2instances[fake_wanted].add(instance)

        wanted = fake_wanted        
        for wanting in self.wanted2wantings.get(wanted, ()):
            self.__push_new_wanting_wanted_instance(wanting, wanted, instance)

    def __push_new_wanting_wanted_instance(self, wanting, wanted, instance):
        self.__push(self.__on_new_wanting_wanted_instance, wanting, wanted, instance)
    def __push_new_wanting_instance_wanted_instance(
        self, wanting, wanting_instance, wanted, wanted_instance):
        self.__push(self.__on_new_wanting_instance_wanted_instance,
                    wanting, wanting_instance, wanted, wanted_instance)
        
    def __push_wanting_wanted(self, wanting, wanted):
        self.__push_wanted(wanted)
        if wanting in self.wanted2wantings[wanted] or \
           (wanting, wanted) in self.tmp_new_wanting_wanted_pairs:
            return

        # bug: below line should move to on_new_wanting_wanted
        #      otherwise on_new_instance may visit them
        # self.wanted2wantings[wanted].add(wanting)

        self.tmp_new_wanting_wanted_pairs.add((wanting, wanted))
        self.__push(self.__on_new_wanting_wanted, wanting, wanted)

    def __push_wanted(self, wanted):
        wanted2type(wanted) # xxxxxxxxx
        if wanted in self.wanted2wantings:
            return
        self.wanted2wantings[wanted] = set()
        self.__push(self.__on_new_wanted, wanted)
    def __on_new_wanted(self, wanted):
        T = wanted2type(wanted)
        
        wanting = wanted
        del wanted
        
        # wanting -> {wanted}
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
            elif symbol in self.seq_nonterminal2seq:
                # fst = self.seq_nonterminal2seq[symbol][0]
                wanted = symbol, 0, begin
                self.__push_wanting_wanted(wanting, wanted)
            elif symbol in self.alt_nonterminal2sub_alts:
                sub_alts = self.alt_nonterminal2sub_alts[symbol]
                for sub in sub_alts:
                    wanted = sub, begin
                    self.__push_wanting_wanted(wanting, wanted)
            else:
                raise logic-error

            
        elif T == SEQ_IDX_BEGIN:
            symbol, idx, begin = wanting
            if symbol in self.seq_nonterminal2seq:
                elem = self.seq_nonterminal2seq[symbol][idx]
                wanted = elem, begin
                self.__push_wanting_wanted(wanting, wanted)
            else:
                raise logic-error
            
        elif T == ROOT_WANTING:
            raise logic-error - root is not wanted
        else:
            raise logic-error - unknown-case

        
    def __on_new_wanting_wanted(self, wanting, wanted):
        # (wanting, wanted) -> {(wanting, wanted, instance)}

        assert wanting not in self.wanted2wantings[wanted]
        self.wanted2wantings[wanted].add(wanting)
        self.tmp_new_wanting_wanted_pairs.remove((wanting, wanted))
        
        for instance in self.fake_wanted2instances.get(wanted, ()):
            self.__push_new_wanting_wanted_instance(wanting, wanted, instance)
    

 
    def __on_new_wanting_wanted_instance(self, wanting, wanted, instance):
        'reduce'
        T = wanting2type(wanting)
        if T == BEGIN:
            begin, = wanting
            assert len(instance) == 2
            wanted_begin, end = instance
            wanting_instance = begin, end
        elif T == SYMBOL_BEGIN:
            symbol, begin = wanting
            if symbol in self.terminals:
                assert len(instance) == 2
                _transition_end, end = instance
                wanting_instance = symbol, begin, end
                
            elif symbol in self.null_nonterminals:
                _begin, end = instance
                wanting_instance = symbol, begin, end
            elif symbol in self.seq_nonterminal2seq:
                _symbol, _0, _begin, leftward_list__states = instance
                end = leftward_list2last(leftward_list__states)
                wanting_instance = symbol, begin, end
                    
            elif symbol in self.alt_nonterminal2sub_alts:
                _sub_alt, _begin, end = instance
                wanting_instance = symbol, begin, end
            else:
                raise logic-error

        
        elif T == SEQ_IDX_BEGIN:
            symbol, idx, begin = wanting
            if symbol not in self.seq_nonterminal2seq:
                raise logic - error
        
            L = len(instance)
            if L == 3:
                fst, _begin, middle = instance
                if idx < len(self.seq_nonterminal2seq[symbol]) - 1:
                    new_wanted = symbol, idx+1, middle
                    self.__push_wanting_wanted(wanting, new_wanted)
                    
                    return # since no wanting_instance
                end = middle
                wanting_instance = symbol, idx, begin, (begin, (end, ()))
            elif L == 4:
                _symbol, _inc_idx, _middle, tail_states = instance
                wanting_instance = symbol, idx, begin, (begin, tail_states)
            else:
                raise logic-error
            
        elif T == ROOT_WANTING:
            wanting_instance = instance
        else:
            raise logic-error - unknown-case

        if T != ROOT_WANTING:
            assert instance2wanted(wanting_instance) == wanting
            self.__push_instance(wanting_instance)
        
        self.__push_new_wanting_instance_wanted_instance(
            wanting, wanting_instance, wanted, instance)
        
        
    def __on_new_wanting_instance_wanted_instance(
        self, wanting, wanting_instance, wanted, wanted_instance):
        self.__update_output__on_new_wanting_instance_wanted_instance(
            wanting, wanting_instance, wanted, wanted_instance)

    def __update_output__on_new_instance(self, instance):
        T = instance2wanted_type(instance)
        if T == SYMBOL_BEGIN:
            symbol, begin, end = instance
            if symbol in self.terminals:
                self.out_terminals.add(instance)
        
    def __update_output__on_new_wanting_instance_wanted_instance(
        self, wanting, wanting_instance, wanted, wanted_instance):
        # update output data
        
        T = wanting2type(wanting)
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
            elif symbol in self.seq_nonterminal2seq:
                _symbol, _0, _begin, leftward_list__states = wanted_instance
                rule = self.seq_nonterminal2seq[symbol]
                states = leftward_list2list(leftward_list__states)
                assert len(states) == len(rule) + 1

                states = tuple(states)
                out_seq = (symbol, states)
                out_seq_rule = tuple(zip(rule, states, states[1:]))
                set_defaultfactory(self.out_seq_nonterminal2seq,
                                   out_seq).add(out_seq_rule)

                out_altseq = wanting_instance
                set_defaultfactory(self.out_altseq_nonterminal2sub_alts,
                                   out_altseq).add(out_seq)
        
            elif symbol in self.alt_nonterminal2sub_alts:
                set_defaultfactory(self.out_altalt_nonterminal2sub_alts,
                                   wanting_instance).add(wanted_instance)
            else:
                raise logic-error

        elif T == SEQ_IDX_BEGIN:
            pass
        elif T == ROOT_WANTING:
            out_start_symbol = wanting_instance
            self.out_start_symbols.add(out_start_symbol)
            
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
    
    parser.feed_state(begin_state) # bug: without this line, fire if tokens == []
    
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

def falling(N, e):
    assert e >= 0
##    if 0 <= N < e:
##        return 0
    r = 1
    for x in range(N, N-e, -1):
        r *= x
    return r

assert falling(3, 0) == 1
assert falling(3, 1) == 3
assert falling(3, 2) == 6
assert falling(3, 3) == 6
assert falling(3, 4) == 0


def choose(N, k):
    assert 0 <= k <= N
    if k > N-k:
        k = N - k

    return falling(N, k)//falling(k, k)
ks = [0, 1, 2, 3, 4, 5, 6]
rs = [1, 6, 15, 20, 15, 6, 1]
assert list(map(choose, [6]*7, ks)) == rs


        
def test_parser2():
    for L in range(2, 5):
        minN = 0
        maxN = 6
        rngN = list(range(minN, maxN))
        ls = list(_test_parser2_imple(L, rngN))
        rs = [choose(N+L-1, L-1) for N in rngN]
        assert rs == ls
def _test_parser2_imple(L, rngN):
    terminals = frozenset('a')
    null_nonterminals = frozenset('N'.split())
    seq_nonterminal2seq = {
        'T' : ('S',)*L,
        }
    alt_nonterminal2sub_alts = {
        'S' : set('TAN'),
        'A' : set('a')
        }

    start_symbols = ['S']
    p = EarleyOnNDFA(terminals, null_nonterminals,
                 seq_nonterminal2seq, alt_nonterminal2sub_alts,
                 start_symbols = start_symbols)

    try:
        for N in rngN:
            p.clear()
            feed_tokens(p, 'a'*N)
            # dir_show(p)
            out_T = 'T', 0, N
##            from pprint import pprint
##            if len(p.out_altseq_nonterminal2sub_alts[out_T]) > 40:
##                pprint(p.out_altseq_nonterminal2sub_alts[out_T])
            yield len(p.out_altseq_nonterminal2sub_alts[out_T])
            
    except:
        raise
    


def test_parser():
    terminals = frozenset('abc')
    null_nonterminals = frozenset('Null'.split())
    seq_nonterminal2seq = {
        'A' : ('a', 'S'),
        'B' : ('b', 'Null'),
        'C' : ('S', 'A'),
        }
    alt_nonterminal2sub_alts = {
        'S' : set('ABC'),
        }

    start_symbols = ['S']
    p = EarleyOnNDFA(terminals, null_nonterminals,
                 seq_nonterminal2seq, alt_nonterminal2sub_alts,
                 start_symbols = start_symbols)

    try:
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

    except:
        dir_show(p)
        raise
    return

    
    

test_parser()
test_parser2()

