

'''
GrammarB:
    B - BNF-like
    recommend :
        prefer short seq rule, best pair
            why not long seq?
                S = S S... S # assume len(right_part) = L
                S = a
                S =

                parser S over 'a'*N
                ==>> the out_start S_0_N has C(N+L-1, L-1) alternatives
                ==>> since there are C(N, 2) out S_x_y at most
                ==>> size of out grammar is O(N, L+1) in worse case
                that is if used pair only, worst case will be O(N, 3)


    


EarleyOnNDFA(terminals, nonterminal2right_parts)
    # allow multiple start symbols for CFG
    add_start_symbols(start_symbols)

    # allow mutiple initial states for FA since NDFA
    # but donot know all states and final states, e.g. len(tokens) is unknown
    add_initial_states(initial_states)


    # add new right_parts
    # rules :: [rule]
    # rule = (nonterminal,) # define new dead rule or add nothing
    #      # add new right_part to nonterminal
    #      | (nonterminal, right_part) # right_part :: [symbol]
    add_new_rules(self, rules)
    
    # since NDFA ==>> null-transition
    # feed(maybe_terminal, begin_state, end_state)
    feed_terminal(terminal, begin_state, end_state)
    feed_null(begin_state, end_state)


    # out_symbol :: (symbol, begin, end)
    # out_terminals = {(terminal, begin_state, end_state)}
    # out_nonterminal2right_parts = 
    #       {(nonterminal, begin_state, end_state):
    #          ( (first_symbol, begin_state, second_state),
    #            ...
    #            (last_symbol, (end-1)_state, end_state)
    #          )
    #       }
    # end_state2out_start_symbols = {end_state: {(start_symbol, initial_state, end_state)}}
    get_partial_out_grammar()
    # out_start_symbols = {(start_symbol, initial_state, final_state)}
    get_out_start_symbols(final_states)





######################### wanting/wanted/instance
# seq == nonempty seq
nonseq_symbol = terminal | null_symbol | alt_symbol
wanting = () | wanted # () is virtual wanting root
wanted  = (begin,) # wanted null-transition by null_nonterminal/out_terminal
        # wanted symbol at begin
        | (symbol, begin)  
        # wanted right_part[idx:] at begin, 0 <= idx < L-1
        | (nonterminal, right_part, idx, begin)

wanting -> instance
    # since not known final_states yet, using any_end_state instead of final_state
    () -> (start_symbol, initial_state, any_end_state)

    # wanted -> instance
    (begin,) -> (begin, end) # auto generate instance (begin, begin)
    (symbol, begin) -> (symbol, begin, end)
    (None, right_part[idx:], begin) -> (None, right_part, begin, (begin, (...)))
    # where 0 <= idx < L == len(right_part)
    # e.g. (nonterminal, right_part, L-1, begin, (begin, (end, ())))
    # why not (nonterminal, right_part, idx, (begin, (...)))
    #     since I want : wanted == wanted_instance[:-1]
    #        not include () since it belongs to wanting

wanting -> wanted
    () -> (start_symbol, initial_state)
    (begin,) -> (begin', ) if (begin, begin') is a null-transition
    (terminal, begin) -> (end,) if (terminal, begin, end) is a transition
    (nonterminal, begin) -> (None, right_part[0:], begin) if RP else (begin,)
    (None, right_part[i:], begin) -> (right_part[i], begin);
                                  -> (None, right_part[i+1:], middle) if i+1 < L
                                 and (right_part[i], begin, middle) is an instance
    
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
    (seq, begin, end) <- [(seq, begin) wanted (None, right_part[0:], begin)]
                     and [(None, right_part[0:], begin, (begin, (...(end, ())...))) is an instance]
    (None, right_part[L-1:], begin, (begin, (end, ())))
            <- [(None, right_part[L-1:], begin) wanted (right_part[-1], begin)]
           and [(right_part[-1], begin, end)] is an instance]
    (None, right_part[i], begin, (begin, tails)) where 0 <= i < L-1
            <- [(None, right_part[i], begin) wanted (right_part[i], begin)]
           and [(right_part[i], begin, middle) is an instance]
           and [(None, right_part[i], begin) wanted (None, right_part[i+1], middle)]
           and [(None, right_part[i+1], middle, tails) is an instance]




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
from seed.types.pair_based_leftward_list import \
     leftward, leftward_list2last, leftward_list2list, seq2leftward_list



def is_seq_set(seq_set):
    return is_Set(seq_set) and all(map(is_seq, seq_set))

def is_seq(seq):
    return isinstance(seq, Sequence)

def is_Set(s):
    return isinstance(s, Set)

def set_defaultfactory(a2bs, a, factory=set):
    if a not in a2bs:
        a2bs[a] = factory()
    return a2bs[a]


def check_EarleyOnNDFA_args(
    terminals, nonterminal2right_parts,
    *, allow_undefined_nonterminals = False):
    
    args = (terminals, nonterminal2right_parts)
    defined_symbols = set().union(*args)
    if not sum(map(len, args)) == len(defined_symbols):
        raise ValueError('not disjoint : terminals, nonterminal2right_parts')

    
    if not all(map(is_seq_set, nonterminal2right_parts.values())):
        raise ValueError('not all set<seq<x>>')

    used_symbols = set(chain.from_iterable(
                           chain.from_iterable(
                               nonterminal2right_parts.values()
                               )
                       ))

    undefined_symbols = used_symbols - defined_symbols
    if undefined_symbols:
        if not allow_undefined_nonterminals:
            raise ValueError('undefined symbols exist : {}'.format(undefined_symbols))
    return defined_symbols, undefined_symbols



    


# wanting types
STR_WANTING_TYPE = False
NUM_WANTING_TYPE = True
if STR_WANTING_TYPE:
    ROOT_WANTING = 'ROOT_WANTING' # ()
    BEGIN = 'BEGIN'
    SYMBOL_BEGIN = 'SYMBOL_BEGIN'
    NONE_RPTAIL_BEGIN = 'NONE_RPTAIL_BEGIN'
elif NUM_WANTING_TYPE:
    ROOT_WANTING = 'ROOT_WANTING' # ()
    BEGIN = 'BEGIN'
    SYMBOL_BEGIN = 'SYMBOL_BEGIN'
    NONE_RPTAIL_BEGIN = 'NONE_RPTAIL_BEGIN'
else:
    raise logic-error

length2wanting_type = ROOT_WANTING, BEGIN, SYMBOL_BEGIN, NONE_RPTAIL_BEGIN


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
    3: NONE_RPTAIL_BEGIN,
}

if 0:
        T = self.to_wanting_type(wanting)
        if T == BEGIN:
            begin, = wanting
        elif T == SYMBOL_BEGIN:
            symbol, begin = wanting
        elif T == NONE_RPTAIL_BEGIN:
            _None, right_part_tail, begin = wanting
            assert _None is None
            assert right_part_tail
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

def copy_to_key2tuple_set(d):
    return {key: set(map(tuple, seq_set)) for key, seq_set in d.items()}
def copy_to_key2set(d):
    return {key: set(s) for key, s in d.items()}



def _copy_EarleyOnNDFA_args(args):
    (defined_symbols, undefined_symbols,
     terminals, nonterminal2right_parts,
     nonterminal2leftward_right_parts,
     start_symbols, initial_states) = args
    return (set(defined_symbols), set(undefined_symbols),
            set(terminals),
            copy_to_key2set(nonterminal2right_parts),
            copy_to_key2set(nonterminal2leftward_right_parts),
            set(start_symbols), set(initial_states)
            )

class EarleyOnNDFA: # __B:
    def __init__(self,
                 terminals, nonterminal2right_parts,
                 *,
                 start_symbols = (),
                 initial_states = (),
                 allow_undefined_nonterminals = False):
        
        defined_symbols, undefined_symbols = check_EarleyOnNDFA_args(
            terminals,
            nonterminal2right_parts,
            allow_undefined_nonterminals = allow_undefined_nonterminals)
        if undefined_symbols:
            assert allow_undefined_nonterminals


        nonterminal2right_parts = copy_to_key2tuple_set(nonterminal2right_parts)
        nonterminal2leftward_right_parts = \
            {n : set(map(seq2leftward_list, RPs))
             for n, RPs in nonterminal2right_parts.items()}
        args = (defined_symbols, undefined_symbols,
                terminals, nonterminal2right_parts,
                nonterminal2leftward_right_parts,
                start_symbols, initial_states)
        self.__args = _copy_EarleyOnNDFA_args(args)
        self.clear()

    def __reset(self):
        args = _copy_EarleyOnNDFA_args(self.__args)
        (defined_symbols, undefined_symbols,
                 terminals, nonterminal2right_parts,
                 nonterminal2leftward_right_parts,
                 start_symbols, initial_states) = args
        
        self.defined_symbols = defined_symbols
        self.undefined_symbols = undefined_symbols
        self.terminals = terminals
        self.nonterminal2right_parts = nonterminal2right_parts
        self.nonterminal2leftward_right_parts = nonterminal2leftward_right_parts
        self.start_symbols = start_symbols
        self.initial_states = initial_states
        
    def add_new_nonterminals(self, undefined_symbols):
        # need not update-wanteds

        undefined_symbols = set(undefined_symbols)
        if not self.defined_symbols.isdisjoint(undefined_symbols):
            existed_symbols = self.defined_symbols & undefined_symbols
            raise ValueError('not all new symbols : {}'.format(existed_symbols))
        for d in [self.nonterminal2right_parts,
                  self.nonterminal2leftward_right_parts]:
            d.update((dead, set()) for dead in undefined_symbols)
        
        self.defined_symbols.update(undefined_symbols)
                
        
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
        self.out_nonterminal2right_parts = {}
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
                self.out_nonterminal2right_parts,
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
            elif symbol in self.nonterminal2right_parts:
                for leftward_right_part in self.nonterminal2leftward_right_parts[symbol]:
                    if not leftward_right_part:
                        # null
                        wanted = begin,
                    else:
                        wanted = None, leftward_right_part, begin
                    self.__push_wanting_wanted(wanting, wanted)
            else:
                raise logic-error

            
        elif T == NONE_RPTAIL_BEGIN:
            _None, right_part_tail, begin = wanting
            assert _None is None
            assert right_part_tail

            elem, _ = right_part_tail
            wanted = elem, begin
            self.__push_wanting_wanted(wanting, wanted)
            
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
                
            elif symbol in self.nonterminal2right_parts:
                L = len(instance)
                if L == 2:
                    # null
                    _begin, end = instance
                elif L == 4:
                    _None, _leftward_right_part, _begin, leftward_states = instance
                    end = leftward_list2last(leftward_states)
                    
                else:
                    raise logic-error
                wanting_instance = symbol, begin, end
                
            else:
                raise logic-error

        
        elif T == NONE_RPTAIL_BEGIN:
            _None, right_part_tail, begin = wanting
            assert _None is None
            assert right_part_tail

            head, tail_tail = right_part_tail

            L = len(instance)
            if L == 3:
                _head, _begin, middle = instance
                assert _head == head
                if tail_tail:
                    new_wanted = None, tail_tail, middle
                    self.__push_wanting_wanted(wanting, new_wanted)
                    
                    return # since no wanting_instance
                end = middle
                tail_states = (end, ())
            elif L == 4:
                _None, _tail_tail, _middle, tail_states = instance
                
            else:
                raise logic-error
            wanting_instance = None, right_part_tail, begin, (begin, tail_states)
            
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
                
            elif symbol in self.nonterminal2right_parts:
                wanted_type = wanted2type(wanted)
                if wanted_type == BEGIN:
                    # null
                    out_right_part = ()
                elif wanted_type == NONE_RPTAIL_BEGIN:
                    _None, _leftward_RP, _begin, leftward_states = wanted_instance
                    right_part = leftward_list2list(_leftward_RP)
                    states = leftward_list2list(leftward_states)
                    assert len(states) == len(right_part) + 1

                    states = tuple(states)
                    out_right_part = tuple(zip(right_part, states, states[1:]))
                else:
                    raise logic-error
                
                out_nonterminal = wanting_instance
                set_defaultfactory(self.out_nonterminal2right_parts,
                                   out_nonterminal).add(out_right_part)

            else:
                raise logic-error

        elif T == NONE_RPTAIL_BEGIN:
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

        #       S=(S,)*L;            S=a;     S=;
        rs = [choose(N+L-1, L-1) + (N==0) + (N==1) for N in rngN]
        try:
            assert ls == rs
        except:
            print(ls)
            print(rs)
            raise
def _test_parser2_imple(L, rngN):
    terminals = frozenset('a')
    nonterminal2RPs = {
        'S' : {('S',)*L, ('a',), ()}
        }

    start_symbols = ['S']
    p = EarleyOnNDFA(terminals, nonterminal2RPs,
                 start_symbols = start_symbols)

    try:
        for N in rngN:
            p.clear()
            feed_tokens(p, 'a'*N)
            # dir_show(p)
            out_S = 'S', 0, N
##            from pprint import pprint
##            if len(p.out_altseq_nonterminal2sub_alts[out_T]) > 40:
##                pprint(p.out_altseq_nonterminal2sub_alts[out_T])
            yield len(p.out_nonterminal2right_parts[out_S])
            
    except:
        raise
    


def test_parser():
    terminals = frozenset('abc')
    nonterminal2RPs = {
        'Null' : {()},
        'A' : {('a', 'S')},
        'S' : {('b', 'Null'), ('S', 'A'), ('A',)}
        }


    start_symbols = ['S']
    p = EarleyOnNDFA(terminals, nonterminal2RPs,
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

