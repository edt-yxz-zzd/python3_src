'''
let S be start symbol
assume input was [Terminal]
-> [Maybe Terminal] ended by nothing
recognize "S nothing"

let FIRST(L, A) = {sentence[:L] for any sentence in language(A)}
LL(N) ==>>
    A = B | C | ... ==>> FIRST(N, B + FOLLOW(A)) & FIRST(N, C + FOLLOW(A)) == {}
        ==>> [B is nullable][C is nullable] == False
        ==>> at most one alternative can be nullable
        

if language(S) is prefix code that is S cannot be a proper prefix of S ==>>
    language(S) == {''} or
        S is not nullable (include language(S) == {}) <==>
        S is not ended by nullable Nonterminal
        def. X is not ended by nullable Nonterminal ==>>
            1) X is Terminal
            or 2) X = ... | Y | ... ==>> Y is not ended by nullable Nonterminal
            or 2)' X is dead, i.e. no alternatives
            or 3) X = ... Y ==>> X is not nullable and Y is not ended by nullable Nonterminal
'''


import types
#from sand.types.ToProcess import UnorderedSetOnce

class ParseError(ValueError):pass




def clean_grammar_info(gram_info, start_symbol):
    from sand.types.Grammar import GrammarInfo2MutableGrammar, inplace_clean_grammar
    gram = GrammarInfo2MutableGrammar(gram_info, start_symbol)
    inplace_clean_grammar(gram, [start_symbol])
    return gram.get_grammar_info()



def calc__symbol2maybe_firsts(gram_info, start_symbol):
    return calc__symbol2inits(1, gram_info, start_symbol)

def calc__symbol2inits(k, gram_info, start_symbol):
    from sand.types.Grammar import GrammarInfo2MutableGrammar, calc__dot_INIT, set_union
    gram = GrammarInfo2MutableGrammar(gram_info, start_symbol)
    dot_symbol2len2inits = calc__dot_INIT(k, gram)
    symbol2inits = {}
    for symbol in gram_info:
        dot_symbol = (symbol, 0)
        len2inits = dot_symbol2len2inits[dot_symbol]
        inits = set_union(len2inits)
        symbol2inits[symbol] = inits
    return symbol2inits

def make_DynamicFullLL1(gram_info, start_symbol):
    gram_info = clean_grammar_info(gram_info, start_symbol)
    symbol2maybe_firsts = calc__symbol2maybe_firsts(gram_info, start_symbol)
    return DynamicFullLL1(gram_info, start_symbol, symbol2maybe_firsts)
    

class DynamicFullLL1:
    '''dynamic full LL1

static full LL1
    - rename each nonterminal by (nonterminal, total_terminals)
    - start symbol be (start_symbol, {()})

Total a = Maybe a = () | (a,)
# () in maybe_firsts means nullable
# () in total_firsts/dynamic_follows means end-of-input

see also:
    Parsing Techniques - A Practical Guide (2ed)(by Dick Grune, Ceriel J.H. Jacobs)::8.2.3 LL(1) versus Strong-LL(1)

'''


    def __init__(self, gram_info, start_symbol, symbol2maybe_firsts):
        '''gram_info :: Map Symbol Rule; Rule = None|tuple|frozenset

terminal->None,
seq_nonterminal->tuple<Symbol>,
alt_nonterminal->frozenset<Symbol>
'''
        assert start_symbol in gram_info
        self.gram_info = gram_info
        self.start_symbol = start_symbol
        self.symbol2maybe_firsts = symbol2maybe_firsts # () in maybe_firsts means nullable
        self.clear()
    def clear(self):
        self.to_parse = () # -> (start_symbol, ())
        self.parse_tree = (None, []) # virtual root
        self.parsing_node_stack = [self.parse_tree]
        self.total_firsts_stack = [{()}] # () in total_firsts/dynamic_follows means end-of-input

        self.__append_left_pred_symbol(self.start_symbol)
        
    def _show_details(self):
        attrs = 'gram_info start_symbol symbol2maybe_firsts to_parse parse_tree parsing_node_stack total_firsts_stack'.split()
        for attr in attrs:
            print(attr, getattr(self, attr))


    def is_end_of_input(self, total_terminal):
        return total_terminal == ()
    def is_seq_nonterminal(self, symbol):
        return type(self.gram_info[symbol]) is tuple
    def is_alt_nonterminal(self, symbol):
        return type(self.gram_info[symbol]) is frozenset
    def is_terminal(self, symbol):
        return self.gram_info[symbol] is None
    def __append_left_pred_symbol(self, symbol):
        dynamic_follows = self.total_firsts_stack[-1]
        new_total_firsts = self.__calc_new_total_firsts(symbol, dynamic_follows)
        self.total_firsts_stack.append(new_total_firsts)
        self.to_parse = (symbol, self.to_parse)
    def __pop_left_pred_symbol(self):
        self.total_firsts_stack.pop()
        symbol, self.to_parse = self.to_parse
        return symbol
    def __get_first_pred_symol(self):
        return self.to_parse[0]
    def __get_curr_total_firsts(self):
        return self.total_firsts_stack[-1]
    def __get_second_total_firsts(self):
        return self.total_firsts_stack[-2]
        
    def __calc_new_total_firsts(self, symbol, dynamic_follows):
        total_firsts = set(self.symbol2maybe_firsts[symbol])
        if () in total_firsts:
            total_firsts.remove(())
            total_firsts |= dynamic_follows
        return total_firsts
        
    def __close_nodes(self):
        while len(self.parsing_node_stack) != 1:
            symbol, children = node = self.parsing_node_stack[-1]
            if self.is_terminal(symbol):
                pass
            elif self.is_alt_nonterminal(symbol):
                if len(children) < 1:
                    break
            elif self.is_seq_nonterminal(symbol):
                if len(children) < len(self.gram_info[symbol]):
                    break
            self.parsing_node_stack.pop() # close
            

    def __add_new_node(self, symbol):
        new_node = (symbol, [])
        self.parsing_node_stack[-1][-1].append(new_node)
        self.parsing_node_stack.append(new_node)

        self.__close_nodes()
        return


    def extract_parse_tree_and_clear(self):
        '''tree :: (symbol, [tree]); may not be a complete tree

if complete tree i.e. extract while self.is_finished():
    (symbol, [children]) ==>> len(children)
    (terminal, [])       ==>> 0
    (alt, [one_alt])     ==>> 1
    (seq, [...])         ==>> len(rule(seq))

'''
        tree = self.parse_tree[-1][-1]
        self.clear()
        return tree
    
    def feed_terminals(self, terminals):
        for t in terminals:
            self.feed(t)
            
    def feed(self, terminal):
        return self.feed_total_terminal((terminal,))
    def feed_end_of_input(self):
        return self.feed_total_terminal(())

    def is_endable(self):
        'if return True, we call feed_end_of_input() to finish parsing'
        if self.is_finished():
            return True
        total_firsts = self.__get_curr_total_firsts()
        end_of_input = ()
        return end_of_input in total_firsts
    def is_finished(self):
        #        has finished or not begun yet   &&        has begun
        r = len(self.parsing_node_stack) == 1 and bool(self.parse_tree[-1])
        assert bool(r) == bool(not self.to_parse)
        return r
    def feed_total_terminal(self, total_terminal):
        maybe_terminal = total_terminal
        while True:
            if self.is_finished():
                if self.is_end_of_input(maybe_terminal):
                    return
                raise ParseError('feed terminal while parsing finished')

            #assert self.to_parse
            
            total_firsts = self.__get_curr_total_firsts()
            # print(total_terminal, total_firsts)
            if total_terminal not in total_firsts:
                raise ParseError('mismatch : required {} but input {}'
                                     .format(total_firsts, total_terminal))
            
            wanted_symbol = self.__get_first_pred_symol()
            if self.is_terminal(wanted_symbol):
                assert not self.is_end_of_input(maybe_terminal)
                input_terminal, = maybe_terminal
                assert input_terminal == wanted_symbol
                self.__pop_left_pred_symbol()
                self.__add_new_node(wanted_symbol)
                return
            elif self.is_alt_nonterminal(wanted_symbol):
                # bug : once call __get_curr_total_firsts()
                dynamic_follows = self.__get_second_total_firsts() 
                for sub_alt in self.gram_info[wanted_symbol]:
                    new_total_first = self.__calc_new_total_firsts(sub_alt, dynamic_follows)
                    if total_terminal in new_total_first:
                        break
                else:
                    raise logic-error # total_terminal in FIRST(A...#) but not in any FIRST(A~i...#)

                self.__pop_left_pred_symbol()
                self.__append_left_pred_symbol(sub_alt)
                self.__add_new_node(wanted_symbol)

                
                continue
            elif self.is_seq_nonterminal(wanted_symbol):
                self.__pop_left_pred_symbol()
                for sub_seq in reversed(self.gram_info[wanted_symbol]):
                    self.__append_left_pred_symbol(sub_seq)
                self.__add_new_node(wanted_symbol)

                
                continue
            else:
                raise logic-error # gram_info contains undefined symbol
            
            
                



def test__DynamicFullLL1():
    def end(r):
        assert r.is_endable()
        r.feed_end_of_input()
        assert r.is_finished()
    test_LL1(make_DynamicFullLL1, end)

    
def test_LL1(make_LL1, end):

    gram_info = {
        'S' : frozenset('Nullable a B Dead1 Dead2'.split()),
        'B' : tuple('b Nullable'.split()),
        'Nullable' : frozenset('c Null D'.split()),
        'D' : tuple('d S Null Null'.split()),
        'a' : None,
        'b' : None,
        'c' : None,
        'd' : None,
        'nonreachable' : None,
        'Dead1' : frozenset('Dead2'.split()),
        'Dead2' : tuple('Dead1 a'.split()),
        'Null' : tuple(),
        }
    r = make_LL1(gram_info, 'S')
    for i in range(16):
        # r._show_details()
        r.clear()
        
        if i == 0:
            end(r)
        elif i == 1:
            r.feed('a')
            end(r)
        elif i == 2:
            r.feed('b')
            end(r)
        elif i == 3:
            r.feed('c')
            end(r)
        elif i == 4:
            r.feed_terminals('b c'.split())
            end(r)
        elif i == 5:
            r.feed_terminals('b d'.split())
            end(r)
        elif i == 6:
            r.feed_terminals('d'.split())
            end(r)
        elif i == 7:
            r.feed_terminals('b d a'.split())
            end(r)
            

test__DynamicFullLL1()
































def len2inits_maxlen2follows_to_aheads(len2inits, maxlen2follows):
    'ahead = {sentence}; if len(sentence) < k, means sentence + (end-of-input,) * (k-L)'
    assert len(len2inits) == len(maxlen2follows)
    k = len(len2inits) - 1

    aheads = frozenset(init + follow
                      for inits, follows in zip(len2inits, reversed(maxlen2follows))
                      for init in inits
                      for follow in follows)
    return aheads


def calc__alt_nonterminal2ahead_terminals2subalt_symbol(k, gram_info, start_symbol):
    
    from sand.types.Grammar import GrammarInfo2MutableGrammar, calc__dot_INIT, set_union, calc__dot_FOLLOW, classify_symbols
    gram = GrammarInfo2MutableGrammar(gram_info, start_symbol)
    
    dot_symbol2len2inits = calc__dot_INIT(k, gram)
    dot_symbol2maxlen2follows = calc__dot_FOLLOW(k, gram, dot_symbol2len2inits)
    # print(dot_symbol2maxlen2follows)

    terminals, seq_nonterminals, alt_nonterminals = classify_symbols(gram)
    alt2ahead2subalt = {}
    for alt in alt_nonterminals:
        ahead2subalt = alt2ahead2subalt[alt] = {}
        rule = gram_info[alt]
        partial_aheads = set()

        maxlen2follows = dot_symbol2maxlen2follows[(alt, 1)]
        for subalt in rule:
            len2inits = dot_symbol2len2inits[(subalt, 0)] # bug: once (subalt, 1)
            sub_aheads = len2inits_maxlen2follows_to_aheads(len2inits, maxlen2follows)
##            print(len2inits)
##            print(maxlen2follows)
##            print(sub_aheads)
            if partial_aheads.isdisjoint(sub_aheads):
                partial_aheads |= sub_aheads
                ahead2subalt.update((ahead, subalt) for ahead in sub_aheads)
            else:
                err_subalt = subalt
                err_sub_aheads = sub_aheads
                for subalt in rule:
                    len2inits = dot_symbol2len2inits[(subalt, 1)]
                    sub_aheads = len2inits_maxlen2follows_to_aheads(len2inits, maxlen2follows)
                    if not sub_aheads.isdisjoint(err_sub_aheads):
                        if subalt == err_subalt:
                            raise logic-error
                        raise ValueError('ahead/ahead conflict : {} {{{}, {}}}'.format(alt, subalt, err_subalt))
                    
    return alt2ahead2subalt


    
def make_StrongLL1(gram_info, start_symbol):
    gram_info = clean_grammar_info(gram_info, start_symbol)
    alt2total_ahead2subalt = calc__alt_nonterminal2ahead_terminals2subalt_symbol(1, gram_info, start_symbol)
    return StrongLL1(gram_info, start_symbol, alt2total_ahead2subalt)
    calc__dot_FOLLOW(gram)



class StrongLL1:
    def __init__(self, gram_info, start_symbol, alt_nonterminal2total_ahead_terminal2subalt_symbol):
        self.gram_info = gram_info
        self.start_symbol = start_symbol
        self.alt2ahead2subalt = alt_nonterminal2total_ahead_terminal2subalt_symbol
        self.symbol2rule_len = {symbol : len(gram_info[symbol])
                                    if self.is_seq_nonterminal(symbol)
                                    else 1
                                for symbol in gram_info}
        self.clear()
    def clear(self):
        # self.to_parse = () # -> (start_symbol, ())
        self.parse_tree = (None, []) # virtual root

        # ends with (nonseq, []) or (None, [...])
        # ==>> dot_symbol ends with (nonseq, 0) or empty
        self.parsing_node_stack = [self.parse_tree]

        self.__push_symbol(self.start_symbol)
        
    def _show_details(self):
        attrs = 'gram_info start_symbol alt2ahead2subalt symbol2rule_len parse_tree parsing_node_stack'.split()
        for attr in attrs:
            print(attr, getattr(self, attr))


    def is_end_of_input(self, total_terminal):
        return total_terminal == ()
    def is_seq_nonterminal(self, symbol):
        return type(self.gram_info[symbol]) is tuple
    def is_alt_nonterminal(self, symbol):
        return type(self.gram_info[symbol]) is frozenset
    def is_terminal(self, symbol):
        return self.gram_info[symbol] is None
    def __push_symbol(self, symbol):
        self.__add_new_node(symbol)
        self.__to_dot_nonseq_0()
    def __push_symbol__without_to_dot_nonseq_0(self, symbol):
        self.parsing_dot_symbol_stack.append((symbol, 0))

    def __is_empty__dot_symbol_stack(self):
        return len(self.parsing_node_stack) == 1

    def __get_last_dot_symbol(self):
        if self.__is_empty__dot_symbol_stack():
            raise IndexError
        symbol, children = self.parsing_node_stack[-1]
        return symbol, len(children)
    
    def __add_new_node(self, symbol):
        new_node = (symbol, [])
        self.parsing_node_stack[-1][-1].append(new_node)
        self.parsing_node_stack.append(new_node)
        return
    def __terminal_matched(self):
        assert not self.__is_empty__dot_symbol_stack()
        symbol, idx = self.__get_last_dot_symbol()
        assert idx == 0
        assert self.is_terminal(symbol)
        self.parsing_node_stack[-1][-1].append(None)
        self.__to_dot_nonseq_0()

        
    def __to_dot_nonseq_0(self):
        while not self.__is_empty__dot_symbol_stack():
            symbol, idx = self.__get_last_dot_symbol()
            L = self.symbol2rule_len[symbol]
            if idx == L:
                self.__close_nodes()
                continue
            elif self.is_seq_nonterminal(symbol):
                rule = self.gram_info[symbol]
                new_symbol = rule[idx]
                self.__add_new_node(new_symbol)
                continue
            break

        if not self.__is_empty__dot_symbol_stack():
            symbol, idx = self.__get_last_dot_symbol()
            assert not self.is_seq_nonterminal(symbol)
            assert idx == 0
            
            

    def __close_nodes(self):
        while not self.__is_empty__dot_symbol_stack():
            symbol, idx = self.__get_last_dot_symbol()
            L = self.symbol2rule_len[symbol]
            if idx < L:
                break
            _, children = self.parsing_node_stack.pop() # close
            if children == [None]:
                children.clear()
                
        
    def extract_parse_tree_and_clear(self):
        '''tree :: (symbol, [tree]); may not be a complete tree

if complete tree i.e. extract while self.is_finished():
    (symbol, [children]) ==>> len(children)
    (terminal, [])       ==>> 0
    (alt, [one_alt])     ==>> 1
    (seq, [...])         ==>> len(rule(seq))

'''
        tree = self.parse_tree[-1][-1]
        self.clear()
        return tree
    

    def feed_terminals(self, terminals):
        for t in terminals:
            self.feed(t)
            
    def feed(self, terminal):
        return self.feed_total_terminal((terminal,))
    def feed_end_of_input(self):
        return self.feed_total_terminal(())
    def maybe_endable(self):
        'if return False, we cannot call feed_end_of_input() to finish parsing; otherwise may be endable'
        if self.is_finished():
            return True
        
        end_of_input = ()
        maybe_terminal = total_terminal = end_of_input

        assert not self.__is_empty__dot_symbol_stack()
        wanted_symbol, idx = self.__get_last_dot_symbol()
        assert idx == 0
        
        if self.is_terminal(wanted_symbol):
            return False
        elif self.is_alt_nonterminal(wanted_symbol):
            ahead2subalt = self.alt2ahead2subalt[wanted_symbol]
            return total_terminal in ahead2subalt
        else:
            raise logic-error # should ends with (nonseq, 0)


    def is_finished(self):
        #        has finished or not begun yet   &&        has begun
        return len(self.parsing_node_stack) == 1 and bool(self.parse_tree[-1])
    
    def feed_total_terminal(self, total_terminal):
        maybe_terminal = total_terminal
        while True:
            if self.is_finished():
                if self.is_end_of_input(maybe_terminal):
                    return
                raise ParseError('feed terminal while parsing finished')

            assert not self.__is_empty__dot_symbol_stack()
            wanted_symbol, idx = self.__get_last_dot_symbol()
            assert idx == 0
            
            if self.is_terminal(wanted_symbol):
                if total_terminal != (wanted_symbol,):
                    raise ParseError('mismatch : required {} but input {}'
                                     .format((wanted_symbol,), total_terminal))
                self.__terminal_matched()
                return
            elif self.is_alt_nonterminal(wanted_symbol):
                ahead2subalt = self.alt2ahead2subalt[wanted_symbol]
                if total_terminal not in ahead2subalt:
                    from pprint import pprint as print
                    print(wanted_symbol)
                    print(self.gram_info)
                    print(self.alt2ahead2subalt)
                    raise ParseError('mismatch : required {} but input {}'
                                     .format(set(ahead2subalt), total_terminal))
                subalt = ahead2subalt[total_terminal]
                self.__push_symbol(subalt)

                continue
            else:
                raise logic-error # should ends with (nonseq, 0)

            




def test__StrongLL1():
    def end(r):
        assert r.maybe_endable()
        r.feed_end_of_input()
        assert r.is_finished()
        # print(r.extract_parse_tree_and_clear())
    test_LL1(make_StrongLL1, end)



test__StrongLL1()




    


