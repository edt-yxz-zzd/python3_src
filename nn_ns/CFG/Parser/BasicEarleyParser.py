


__all__ = '''
    BasicEarleyParser
    '''.split()

from seed.types.namedtuple import namedtuple
from seed.tiny import print_err
from ..CFG import explain_ref_symbol_psidx
from .errors import (
    ParseFailError
    ,NotExistsError
    ,NotTreeError
    ,NotTreeError__recur
    ,NotTreeError__ambiguous
    )
#from .ParseTreeNode import ParseTreeNonleafNode, ParseTreeLeafNode

EarleyState = namedtuple('EarleyState', '''
    terminal_position_begin_of_production
    production_idx
    dot_idx
    '''.split())


"""deplicated: EarleyResultGrammarXXX
    why?
        some grammar can be very large
            when len(production_rhs) is big and ambiguous
EarleyResultGrammarTerminal = namedtuple(
    'EarleyResultGrammarTerminal', '''
    terminal_name
    terminal_position
    ''')
EarleyResultGrammarNonterminal__cut_nullable = namedtuple(
    'EarleyResultGrammarNonterminal__cut_nullable', '''
    production_idx
    terminal_position_begin
    terminal_position_end
    maybe_children
    ''')
EarleyResultGrammarNode = (EarleyResultGrammarTerminal, EarleyResultGrammarNonterminal__cut_nullable)
    '''
EarleyResultGrammarTerminal
    no token
    why?
        user can get token by:
            BasicEarleyParser.tokens[.terminal_position]
        since I call it EarleyResultGrammarTerminal
            token is not terminal
EarleyResultGrammarNonterminal__cut_nullable:
    if terminal_position_begin == terminal_position_end:
        maybe_children is None
    else:
        len(maybe_children) > 0
    why?
        since I donot want to handle nullable structure
        "None" means "cut directly"
        user can insert nullable structure on its own

    '''
"""

class BasicEarleyParser:
    r'''

methods:
    feed
    extract_parse_main_tree
    #_get_rough_size
    restart


#variables and types
state = (terminal_position_begin_of_production, production_idx, production_rhs_idx)
    finally, if complete, we get:
        (terminal_position_begin_of_production
        ,production_idx
        ,terminal_position_end_of_production
        )

dot_idx - production_rhs_idx
position - terminal_position, token position
terminal_position2state2maybe_prev_positions
    :: [{state: None|{terminal_position_of_prev_dot_idx}}]
    dot_idx = state.production_rhs_idx
    value = terminal_position2state2maybe_prev_positions[position][state]
    if dot_idx == 0:
        value is None
    if dot_idx > 0:
        value :: {terminal_position_of_prev_dot_idx}
        terminal_position2state2maybe_prev_positions[terminal_position_of_prev_dot_idx][state.ireplace(dot_idx-=1)]
terminal_position2nonterminal_idx2states
    :: [{nonterminal_idx: [state]}]
    #:: [{nonterminal_idx: {state}}]
    group states by nonterminal_idx at dot_idx
        # exclude state whose dot_idx is complete or terminal_set_idx

# for extract_parse_main_tree
ambiguous_nonterminal_idc
make_leaf_of_at
    :: terminal_set_idx -> token -> terminal_position_begin -> node
make_nonnull_nonleaf_of_between
    :: production_idx -> [node] -> terminal_position_begin -> terminal_position_end -> node
        terminal_position_begin < terminal_position_end
make_null_nonleaf_of_at
    :: nullable_nonterminal_idx -> terminal_position -> node
        node can be any thing
            e.g. ParseTreeNonleafNode/None/...
terminal_position2nonterminal_idx_begin_pair2complete_states
    :: [{(nonterminal_idx, terminal_position_begin_of_nonterminal):[complete_state]}]
terminal_position2state2maybe_first_prev_position
    #vs. terminal_position2state2maybe_prev_positions
    :: [{state: None|terminal_position_of_prev_dot_idx}]


'''
    def __init__(self, *
        ,production_idx2nonterminal_idx
        ,production_idx2idxalternative
        ,nonterminal_idx2sorted_production_idc
        ,nonterminal_idx2is_nullable
            # from cfg.calc.nonterminal_idx2is_nullable

        ,start_nonterminal_idc
        ,token2terminal_name
        ,terminal_set_ops
        ,terminal_set_idx2terminal_set

        #used in extract_parse_main_tree
        ,nonterminal_idx2nonterminal_name
        ,nonterminal_idx2maybe_one_null_tree
        ):
        self.production_idx2nonterminal_idx = production_idx2nonterminal_idx
        self.production_idx2idxalternative = production_idx2idxalternative
        self.nonterminal_idx2sorted_production_idc = nonterminal_idx2sorted_production_idc
        self.nonterminal_idx2is_nullable = nonterminal_idx2is_nullable

        self.start_nonterminal_idc = frozenset(start_nonterminal_idc)
        self.token2terminal_name = token2terminal_name
        self.terminal_set_ops = terminal_set_ops
        self.terminal_set_idx2terminal_set = terminal_set_idx2terminal_set
        self.nonterminal_idx2nonterminal_name = nonterminal_idx2nonterminal_name
        self.nonterminal_idx2maybe_one_null_tree = nonterminal_idx2maybe_one_null_tree
        self.__running__handle_state_queue = False

        self.restart()

    def __advance_current_terminal_position(self, token):
        if self.state_queue: raise logic-error
        if self.__running__handle_state_queue: raise logic-error
        #self.handle_state_queue()
        #if self.state_queue: raise logic-error
        ############# should be before advance


        self.terminal_position2state2maybe_prev_positions.append({})
        self.terminal_position2nonterminal_idx2states.append({})
        self.tokens.append(token)
        self.terminal_position2nonterminal_idx_begin_pair2complete_states.append({})
        self.terminal_position2state2maybe_first_prev_position.append({})
        self.__curr__terminal_set_idx2states = {}
    def restart(self):
        if self.__running__handle_state_queue: raise logic-error

        self.terminal_position2state2maybe_prev_positions = [{}]
        self.terminal_position2nonterminal_idx2states = [{}]
        self.tokens = [] # to build tree
        self.terminal_position2nonterminal_idx_begin_pair2complete_states = [{}]
        self.terminal_position2state2maybe_first_prev_position = [{}]
        self.state_queue = []
        self.__curr__terminal_set_idx2states = {}

        terminal_position = 0
        for nonterminal_idx in self.start_nonterminal_idc:
            self.put_nonterminal_idx(nonterminal_idx)
        self.__done_at_current_terminal_position()
    def __done_at_current_terminal_position(self):
        self.handle_state_queue()
        return
        # when finish, there are no wanted!!!
        pairs = self.calc_terminal_set_states_pairs()
        if not pairs:
            raise ParseFailError()



    def handle_state_queue(self):
        if self.__running__handle_state_queue: raise logic-error
        if not self.state_queue: return
        self.__running__handle_state_queue = True

        state_queue = self.state_queue
        i = 0
        while i < len(state_queue):
            state = state_queue[i]; i += 1
            (maybe_is_nonterminal, maybe_idx) = self.explain_state(state)
            if maybe_is_nonterminal is None:
                # complete
                self.__handle_complete_dot_idx(state)
            elif maybe_is_nonterminal is False:
                terminal_set_idx = maybe_idx
                self.__handle_terminal_dot_idx(state, terminal_set_idx)
            elif maybe_is_nonterminal is True:
                nonterminal_idx = maybe_idx
                self.__handle_nonterminal_dot_idx(state, nonterminal_idx)
            else:
                raise logic-error
        state_queue.clear()
        self.__running__handle_state_queue = False
    def put_nonterminal_idx(self, nonterminal_idx):
        terminal_position = self.current_terminal_position
        dot_idx = 0
        for production_idx in self.nonterminal_idx2sorted_production_idc[nonterminal_idx]:
            state = EarleyState(terminal_position, production_idx, dot_idx)
            self.put_state(state, None)


    def get_nonterminal_idx2states(self):
        terminal_position = self.current_terminal_position
        return self.terminal_position2nonterminal_idx2states[terminal_position]
    def get_state2maybe_prev_positions(self):
        terminal_position = self.current_terminal_position
        return self.terminal_position2state2maybe_prev_positions[terminal_position]
    def get_nonterminal_idx_begin_pair2complete_states(self):
        terminal_position = self.current_terminal_position
        return self.terminal_position2nonterminal_idx_begin_pair2complete_states[terminal_position]
    def get_state2maybe_first_prev_position(self):
        terminal_position = self.current_terminal_position
        return self.terminal_position2state2maybe_first_prev_position[terminal_position]
    def put_state(self, state, maybe_prev_position):
        # put state to current_terminal_position
        assert state.terminal_position_begin_of_production <= self.current_terminal_position
        assert (state.dot_idx == 0) is (maybe_prev_position is None)
        state2maybe_prev_positions = self.get_state2maybe_prev_positions()

        Nothing = object()
        may_maybe_prev_positions = state2maybe_prev_positions.get(state, Nothing)
        if may_maybe_prev_positions is not Nothing:
            maybe_prev_positions = may_maybe_prev_positions
            if maybe_prev_positions is None:
                if maybe_prev_position is not None: raise ValueError
                if state.dot_idx != 0: raise logic-error
                return
            prev_positions = maybe_prev_positions
            if maybe_prev_position is None: raise ValueError
            if not state.dot_idx > 0: raise logic-error
            prev_position = maybe_prev_position
            prev_positions.add(prev_position)
            return

        state2maybe_first_prev_position = self.get_state2maybe_first_prev_position()
        if state.dot_idx == 0:
            if maybe_prev_position is not None: raise ValueError
            state2maybe_prev_positions[state] = None
            state2maybe_first_prev_position[state] = None
        elif maybe_prev_position is None: raise ValueError
        else:
            first_prev_position = maybe_prev_position
            state2maybe_prev_positions[state] = {first_prev_position}
            state2maybe_first_prev_position[state] = first_prev_position

        self.state_queue.append(state)

    def __handle_terminal_dot_idx(self, state, terminal_set_idx):
        # update __curr__terminal_set_idx2states
        self.__curr__terminal_set_idx2states.setdefault(terminal_set_idx, []).append(state)
    def __handle_nonterminal_dot_idx(self, state, nonterminal_idx):
        # update terminal_position2nonterminal_idx2states
        nonterminal_idx2states = self.get_nonterminal_idx2states()
        states = nonterminal_idx2states.setdefault(nonterminal_idx, [])
        states.append(state)

        #bug: once forgot self.put_nonterminal_idx(nonterminal_idx)
        self.put_nonterminal_idx(nonterminal_idx)

        # forward_state if nullable
        if self.is_nullable_nonterminal_idx(nonterminal_idx):
            terminal_position_of_dot_idx = self.current_terminal_position
            self.put_forward_state(state, terminal_position_of_dot_idx)
        return

    def __handle_complete_dot_idx(self, state):
        assert self.is_complete_state(state)
        #if state.dot_idx == 0:
            # direct nullable production_idx
        #   return
        nonterminal_idx = self.production_idx2nonterminal_idx[state.production_idx]
        begin = state.terminal_position_begin_of_production
        self.get_nonterminal_idx_begin_pair2complete_states(
            ).setdefault((nonterminal_idx, begin), []).append(state)
        ### update first_prev_position should be before other put_state

        if begin == self.current_terminal_position:
            # direct/indirect null
            return
        prev_position = begin
        assert prev_position < self.current_terminal_position
        try:
            prev_states = self.terminal_position2nonterminal_idx2states[prev_position][nonterminal_idx]
        except KeyError:
            if (prev_position == 0
                and nonterminal_idx in self.start_nonterminal_idc
                ):
                # start_nonterminal_idx donot have parent
                return
            print_err(f'prev_position = {prev_position}')
            print_err(f'nonterminal_idx = {nonterminal_idx}')
            print_err(f'terminal_position2nonterminal_idx2states[{prev_position}]={self.terminal_position2nonterminal_idx2states[prev_position]}')
            raise
        for prev_state in prev_states:
            self.put_forward_state(prev_state, prev_position)
        return


    def get_end_dot_idx(self, state):
        return self.get_rhs_size_of_production(state.production_idx)
    def get_rhs_size_of_production(self, production_idx):
        return len(self.production_idx2idxalternative[production_idx])
    def is_complete_state(self, state):
        return state.dot_idx == self.get_end_dot_idx(state)
    def is_nullable_nonterminal_idx(self, nonterminal_idx):
        return self.nonterminal_idx2is_nullable[nonterminal_idx]
    def put_forward_state(self, state, terminal_position_of_dot_idx):
        # dot_idx+=1; stored at current_terminal_position
        assert 0 <= state.dot_idx < self.get_end_dot_idx(state)
        forward_state = state._replace(dot_idx=state.dot_idx+1)
        assert type(forward_state) is type(state)
        terminal_position_of_prev_dot_idx_of_forward_state = terminal_position_of_dot_idx
        self.put_state(forward_state, terminal_position_of_prev_dot_idx_of_forward_state)


    def explain_state(self, state):
        # -> (maybe_is_nonterminal, maybe_idx)
        # -> (None, None) if complete
        # -> (False, terminal_set_idx)
        # -> (True, nonterminal_idx)
        production_idx = state.production_idx
        dot_idx = state.dot_idx
        idxalternative = self.production_idx2idxalternative[production_idx]
        if dot_idx == len(idxalternative):
            return None, None
        else:
            ref_symbol_psidx = idxalternative[dot_idx]
            return explain_ref_symbol_psidx(ref_symbol_psidx)

    @property
    def current_terminal_position(self):
        return len(self.terminal_position2nonterminal_idx2states)-1
    def feed(self, token):
        contains = self.terminal_set_ops.contains
        terminal_name = self.token2terminal_name(token)

        self.handle_state_queue()
        pairs = self.calc_terminal_set_states_pairs()
        curr_position = self.current_terminal_position

        matched_statess = []
        for terminal_set, states in pairs:
            if contains(terminal_set, terminal_name):
                matched_statess.append(states)

        if not any(matched_statess):
            #print_err('matched_statess\n    ', matched_statess)
            raise ParseFailError(f'no match for the given token: at terminal_position={curr_position}; given_token={token!r}')

        #### __advance_current_terminal_position after calc...
        self.__advance_current_terminal_position(token)
        prev_position = curr_position; del curr_position
        for prev_states in matched_statess:
            for prev_state in prev_states:
                self.put_forward_state(prev_state, prev_position)
        self.__done_at_current_terminal_position()
    def calc_terminal_set_states_pairs(self):
        if self.state_queue: raise logic-error
        if self.__running__handle_state_queue: raise logic-error

        terminal_set_idx2states = self.__curr__terminal_set_idx2states
        pairs = []
        for terminal_set_idx, states in terminal_set_idx2states.items():
            terminal_set = self.terminal_set_idx2terminal_set[terminal_set_idx]
            pairs.append((terminal_set, states))
        return pairs































    def _get_rough_size(self):
        # for debug
        return {'tokens': len(self.tokens)
                ,'states': sum(map(len
                    , self.terminal_position2state2maybe_prev_positions
                    ))
                ,'prev_positions': sum(
                    len(maybe_prev_positions)
                    for d in self.terminal_position2state2maybe_prev_positions
                    for maybe_prev_positions in d.values()
                    if maybe_prev_positions # is not None
                    )
                }

    #nonterminal_triple = (begin, nonterminal_idx, end)
    #production_triple = (begin, production_idx, end)
    def extract_parse_main_tree(self, *
        ,ambiguous_nonterminal_idc
        ,make_leaf_of_at
        ,make_nonnull_nonleaf_of_between
        ,make_null_nonleaf_of_at
        ):
        args = _Args(
                frozenset(ambiguous_nonterminal_idc)
                ,make_leaf_of_at
                ,make_nonnull_nonleaf_of_between
                ,make_null_nonleaf_of_at
                )
        terminal_position_begin = 0
        terminal_position_end = self.current_terminal_position
        pair2complete_states = self.terminal_position2nonterminal_idx_begin_pair2complete_states[terminal_position_end]

        nonterminal_idc = []
        for nonterminal_idx in self.start_nonterminal_idc:
            pair = (nonterminal_idx, terminal_position_begin)
            complete_states = pair2complete_states.get(pair, '')
            if complete_states:
                nonterminal_idc.append(nonterminal_idx)

        if not nonterminal_idc:
            raise NotExistsError('no start_nonterminal_idc success')
        if len(nonterminal_idc) >= 2:
            nonterminal_names = [
                self.nonterminal_idx2nonterminal_name[nonterminal_idx]
                for nonterminal_idx in nonterminal_idc
                ]
            raise ParseFailError(f'too many start_nonterminal_idc success: nonterminal_idc={nonterminal_idc}, nonterminal_names={nonterminal_names}')

        [nonterminal_idx] = nonterminal_idc
        nonterminal_triple = _NonterminalTriple(
            terminal_position_begin, nonterminal_idx, terminal_position_end)
        node = self._extract_nonterminal_triple(args, nonterminal_triple)
        return node

    def _extract_nonterminal_triple(self, args, nonterminal_triple):
        def mk_err_msg(nonterminal_triple):
            nonterminal_name = self.nonterminal_idx2nonterminal_name[nonterminal_idx]
            return f'nonterminal_name={nonterminal_name!r}, {nonterminal_triple!r}'

        if nonterminal_triple.terminal_position_begin == nonterminal_triple.terminal_position_end:
            # null
            nullable_nonterminal_idx = nonterminal_triple.nonterminal_idx
            terminal_position = nonterminal_triple.terminal_position_begin
            may = self.nonterminal_idx2maybe_one_null_tree[nullable_nonterminal_idx]
            if not may: raise logic-error
            is_ambiguous_nullable, production_idx = may
            if (is_ambiguous_nullable and nullable_nonterminal_idx
                    not in args.ambiguous_nonterminal_idc
                ):
                raise NotTreeError__ambiguous(
                    'null tree ambiguous: ' + mk_err_msg(nonterminal_triple))

            return args.make_null_nonleaf_of_at(
                nullable_nonterminal_idx, terminal_position
                )



        #nonnull
        begin = nonterminal_triple.terminal_position_begin
        end = nonterminal_triple.terminal_position_end
        nonterminal_idx = nonterminal_triple.nonterminal_idx

        #bug:pair2complete_states = self.get_nonterminal_idx_begin_pair2complete_states()
        pair2complete_states = self.terminal_position2nonterminal_idx_begin_pair2complete_states[end]
        pair = (nonterminal_idx, begin)
        complete_states = pair2complete_states.get(pair, '')

        if not complete_states:
            raise NotExistsError(mk_err_msg(nonterminal_triple))
            raise NotExistsError
        if (len(complete_states) != 1
            and nonterminal_idx not in args.ambiguous_nonterminal_idc
            ):
            raise NotTreeError__ambiguous(mk_err_msg(nonterminal_triple))
            raise NotTreeError__ambiguous
        complete_state = complete_states[0]
        # the first one must exist at least one path to avoid recur
        production_idx = complete_state.production_idx
        end_dot_idx = self.get_rhs_size_of_production(production_idx)
        assert end_dot_idx == complete_state.dot_idx

        nodes = self._extract_state_end_at(args, complete_state, end)
        return args.make_nonnull_nonleaf_of_between(
                        production_idx, nodes, begin, end)
    def _extract_state_end_at(self, args, state, terminal_position_end):
        # -> [node]
        maybe_first_prev_position = self.terminal_position2state2maybe_first_prev_position[terminal_position_end][state]
        if maybe_first_prev_position is None:
            assert state.dot_idx == 0
            return []
        if state.dot_idx == 0: raise logic-error
        first_prev_position = maybe_first_prev_position

        # dot_idx=0
        begin = state.terminal_position_begin_of_production
        # dot_idx=state.dot_idx-1
        middle = first_prev_position
        # dot_idx=state.dot_idx
        end = terminal_position_end
        prev_state = state._replace(dot_idx=state.dot_idx-1)
        nodes = self._extract_state_end_at(args, prev_state, middle)

        #last_node: middle~end
        #bug: self.explain_state(state)
        (maybe_is_nonterminal, maybe_idx) = self.explain_state(prev_state)
        if maybe_is_nonterminal is None: raise logic-error

        is_nonterminal, idx = maybe_is_nonterminal, maybe_idx
        if is_nonterminal:
            nonterminal_idx = idx
            nonterminal_triple = _NonterminalTriple(middle, nonterminal_idx, end)
            last_node = self._extract_nonterminal_triple(args, nonterminal_triple)
        else:
            terminal_set_idx = idx
            assert middle+1 == end
            token = self.tokens[middle]
            last_node = args.make_leaf_of_at(terminal_set_idx, token, middle)
        nodes.append(last_node)
        return nodes



_NonterminalTriple = namedtuple('_NonterminalTriple', '''
    terminal_position_begin
    nonterminal_idx
    terminal_position_end
    ''')
"""
_ProductionTriple = namedtuple('_ProductionTriple', '''
    terminal_position_begin
    production_idx
    terminal_position_end
    ''')
"""
_Args = namedtuple('_Args', '''
    ambiguous_nonterminal_idc
    make_leaf_of_at
    make_nonnull_nonleaf_of_between
    make_null_nonleaf_of_at
    ''')
    # used in extract_parse_main_tree

