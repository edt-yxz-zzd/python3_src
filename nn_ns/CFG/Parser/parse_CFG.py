
r'''
>>> from ..CFG import CFG
>>> from ..the_py_terminal_set_ops import the_py_terminal_set_ops
>>> terminal_set_ops = the_py_terminal_set_ops
>>> terminal_set_name2terminal_set = lambda a:{a}
>>> make = lambda *args, **kwargs: CFG.make_CFG__hashable_name__less(
...     *args
...     , explain_ref_symbol_name=explain_ref_symbol_name
...     , terminal_set_ops=terminal_set_ops
...     , terminal_set_name2terminal_set=terminal_set_name2terminal_set
...     , **kwargs)
>>> __pairs = [('S', ['Ts1']), ('Ts1', ['Ts0', 't']), ('Ts0', ['Ts1']), ('Ts0', [])]

#>>> __pairs = [('S', ['t', 't'])]
#>>> __pairs = [('S', ['t'])]
>>> explain_ref_symbol_name = lambda name: (name[0].isupper(), name)
>>> cfg = make(__pairs)

>>> find_terminal_set_idc = lambda terminal_set_idx2terminal_set, terminal_name: [terminal_set_idx2terminal_set.index({terminal_name})]
>>> class t:pass
>>> token2terminal_name = lambda token: token.__name__
>>> start_nonterminal_name = 'S'
>>> start_nonterminal_idx = cfg.nonterminal_name2nonterminal_idx(start_nonterminal_name)

>>> tokens = [t]*4
>>> r = parse_CFG(cfg, iter(tokens), start_nonterminal_idc=[start_nonterminal_idx], token2terminal_name=token2terminal_name, find_terminal_set_idc=find_terminal_set_idc, ambiguous_nonterminal_idc=())

'''

__all__ = '''
    parse_CFG
    ParseTreeNonleafNode
    ParseTreeLeafNode

    ParseFailError
    NotTreeError
    NotExistsError
    ParserMessageClosureExecutor

    '''.split()


from seed.types.namedtuple import namedtuple
#from ..CFG import CFG, the_py_terminal_set_ops
from ..MessageClosureExecutor.MessageClosureExecutor_ABC__using_namedtuple__str import \
    MessageClosureExecutor_ABC__using_namedtuple__str
from ..MessageClosureExecutor.show_MessageClosureExecutor import \
    show_MessageClosureExecutor
from ..MessageClosureExecutor.dynamic_sizes_of_MessageClosureExecutor \
    import dynamic_sizes_of_MessageClosureExecutor

from ..errors import ParseFailError
from ._debug_constant_ import _show_dynamic_sizes_of_MessageClosureExecutor


class NotExistsError(ParseFailError):pass
class NotTreeError(ParseFailError):pass
class NotTreeError__recur(NotTreeError):pass
class NotTreeError__ambiguous(NotTreeError):pass
ParseTreeNonleafNode = namedtuple('ParseTreeNonleafNode', '''
    nonterminal_idx
    production_idx
    nonterminal_name
    production_name
    terminal_position_begin
    terminal_position_end
    children
    '''.split())
ParseTreeLeafNode = namedtuple('ParseTreeLeafNode', '''
    terminal_set_idx
    terminal_set_name
    terminal_position_begin
    terminal_position_end
    terminal_name
    token
    '''.split())

def parse_CFG(__cfg, __iter_tokens, *
    , start_nonterminal_idc
    , token2terminal_name
    , find_terminal_set_idc
    , ambiguous_nonterminal_idc
    #, _show_dynamic_sizes_of_MessageClosureExecutor=False
    ):
    '''

input:
    cfg :: CFG
    start_nonterminal_idc :: {nonterminal_idx}
        nonterminal_idx of the start symbol
    token2terminal_name :: token -> terminal_name
    find_terminal_set_idc :: terminal_set_idx2terminal_set -> terminal_name -> sorted[terminal_set_idx]
    ambiguous_nonterminal_idc :: {nonterminal_idx}
        used in extract_parse_main_tree/extract_parse_local_tree
        for ambiguous nonterminal_idx:
            if match empty: then prefer the empty alternative
            else: try avoid only one child not match empty

output:
    parse_result_tree :: ParseTreeNonleafNode
        parse_result_tree.nonterminal_idx <- start_nonterminal_idc
exception:
    ParseFailError
        NotExistsError
            # parse fail
        NotTreeError
            # more than possibles or recur

'''
    e = ParserMessageClosureExecutor(__cfg
        ,start_nonterminal_idc=start_nonterminal_idc
        ,token2terminal_name=token2terminal_name
        ,find_terminal_set_idc=find_terminal_set_idc
        ,ambiguous_nonterminal_idc=ambiguous_nonterminal_idc
        )
    try:
        e.execute_until_closure()
        if e.max_required_terminal_position != len(e.tokens):
            raise ParseFailError('start_nonterminal is dead')
        for token in __iter_tokens:
            e.feed(token)
            e.execute_until_closure()
            if e.max_required_terminal_position != len(e.tokens):
                fail_position = len(e.tokens) - 1
                assert fail_position >= 0
                raise ParseFailError(f'fail_position={fail_position}; token={token!r}')
        if _show_dynamic_sizes_of_MessageClosureExecutor:
            print('_show_dynamic_sizes_of_MessageClosureExecutor:on')
            d = dynamic_sizes_of_MessageClosureExecutor(e)
            d['tokens'] = len(e.tokens)
            print(f'dynamic_sizes_of_MessageClosureExecutor: {d}')
        return e.extract_parse_main_tree()
    except ParseFailError:
        #show_MessageClosureExecutor(e)
        raise

class ParserMessageClosureExecutor(
    MessageClosureExecutor_ABC__using_namedtuple__str):
    '''
terminal_name = token2terminal_name(tokens[terminal_position])
terminal_set_ops.contains(terminal_set_idx2terminal_set[terminal_set_idx], terminal_name)

find_terminal_set_idc :: terminal_set_idx2terminal_set -> terminal_name -> sorted[terminal_set_idx]

see: parse_CFG
'''
    message_interface_action_definition_str = '''

# downward/forward are used to generate actions

# downward
; IDownwardNonterminal_
    <- MDownwardNonterminal_
    ; MDownwardNonterminal_ nonterminal_idx terminal_position
; IDownwardProduction_
    <- MDownwardProduction_
    ; MDownwardProduction_ production_idx terminal_position
; IDownwardAlternativeTail_
    <- MDownwardAlternativeTail_
    ; MDownwardAlternativeTail_ alternative_tail_idx terminal_position
; IDownwardTerminal_
    <- MDownwardTerminal_
    ; MDownwardTerminal_ terminal_set_idx terminal_position

# forward
; IForwardAlternativeTail_
    <- MForwardAlternativeTail_
    ; MForwardAlternativeTail_ alternative_tail_idx terminal_position_begin terminal_position_middle



# store
# assert store
; IStoreTerminal terminal_set_idx terminal_position
    <- MStoreTerminal
    ; MStoreTerminal terminal_position
; IStoreNonterminal nonterminal_idx terminal_position_begin terminal_position_end
    <- MStoreNonterminal
    ; MStoreNonterminal nonterminal_idx terminal_position_begin terminal_position_end
; IStoreProduction production_idx terminal_position_begin terminal_position_end
    <- MStoreProduction
    ; MStoreProduction production_idx terminal_position_begin terminal_position_end
; IStoreAlternativeTail alternative_tail_idx terminal_position_begin terminal_position_end
    <- MStoreAlternativeTail
    ; MStoreAlternativeTail alternative_tail_idx terminal_position_begin terminal_position_end

# discover store
; IStoreNonterminal_ nonterminal_idx terminal_position_begin
    <- MStoreNonterminal
; IStoreProduction_ production_idx terminal_position_begin
    <- MStoreProduction
; IStoreAlternativeTail_ alternative_tail_idx terminal_position_begin
    <- MStoreAlternativeTail

# choice store
; IStoreNonterminalChoice nonterminal_idx terminal_position_begin terminal_position_end
    <- MStoreProduction
; IStoreNonNullAlternativeTailChoice alternative_tail_idx terminal_position_begin terminal_position_end
    <- MStoreNonNullAlternativeTailChoice
    ; MStoreNonNullAlternativeTailChoice alternative_tail_idx terminal_position_begin terminal_position_middle terminal_position_end


# on XXX should be initial_xmessages
# on downward
; AOnDownwardNonterminal_ iDownwardNonterminal_
    <- @IDownwardNonterminal_
; AOnDownwardProduction_ iDownwardProduction_
    <- @IDownwardProduction_
; AOnDownwardAlternativeTail_ iDownwardAlternativeTail_
    <- @IDownwardAlternativeTail_
; AOnDownwardTerminal_ iDownwardTerminal_
    <- @IDownwardTerminal_

# on forward
; AOnForwardAlternativeTail_ iForwardAlternativeTail_
    <- @IForwardAlternativeTail_



# upward
; AUpwardToProduction production_idx iStoreAlternativeTail_
    <- IStoreAlternativeTail_
; AUpwardToNonterminal iStoreProduction_
    <- IStoreProduction_
; AUpwardFromNonterminal alternative_tail_idx iStoreNonterminal_
    <- IStoreNonterminal_
; AUpwardFromTerminal alternative_tail_idx iStoreTerminal
    <- IStoreTerminal

# backward
; ABackwardTerminal alternative_tail_idx iStoreTerminal iStoreAlternativeTail_
    <- IStoreTerminal IStoreAlternativeTail_
; ABackwardNonterminal alternative_tail_idx iStoreNonterminal iStoreAlternativeTail_
    <- IStoreNonterminal IStoreAlternativeTail_


# on store
#; AOn IStoreNonterminalChoice
; AOnIStoreNonNullAlternativeTailChoice iStoreNonNullAlternativeTailChoice
    <- @IStoreNonNullAlternativeTailChoice
    # maked when IStoreNonNullAlternativeTailChoice occur


# now handled by AOnDownwardAlternativeTail_
# auto generate
#; AAutoNullAlternativeTail alternative_tail_idx iDownwardAlternativeTail_
#    <- IDownwardAlternativeTail_


        '''

    def token2terminal_name(self, token):
        return self.__token2terminal_name(token)
    def find_terminal_set_idc(self, terminal_name):
        may_cache = self.__maybe_cache_for_find_terminal_set_idc
        if may_cache is not None:
            cache = may_cache
            may_idc = cache.get(terminal_name)
            if may_idc is None:
                idc = self.__call_directly__find_terminal_set_idc(terminal_name)
                idc = tuple(idc)
                cache[terminal_name] = idc
            else:
                idc = may_idc
        else:
            idc = self.__call_directly__find_terminal_set_idc(terminal_name)
        return idc

    def __call_directly__find_terminal_set_idc(self, terminal_name):
        terminal_set_idc = self.__find_terminal_set_idc(
            self.cfg.terminal_set_idx2terminal_set
            ,terminal_name
            )
        prev = -1
        for terminal_set_idx in terminal_set_idc:
            if not prev < terminal_set_idx: raise Exception('bad find_terminal_set_idc')
        return terminal_set_idc
    def terminal_position2terminal(self, terminal_position):
        return self.token2terminal_name(self.tokens[terminal_position])

    def MDownwardNonterminal_(self, message):
        #IDownwardNonterminal_
        yield self.mk.IDownwardNonterminal_()
    def MDownwardProduction_(self, message):
        #IDownwardProduction_
        yield self.mk.IDownwardProduction_()
    def MDownwardAlternativeTail_(self, message):
        #IDownwardAlternativeTail_
        yield self.mk.IDownwardAlternativeTail_()
    def MDownwardTerminal_(self, message):
        #IDownwardTerminal_
        yield self.mk.IDownwardTerminal_()
    def MForwardAlternativeTail_(self, message):
        #IForwardAlternativeTail_
        yield self.mk.IForwardAlternativeTail_()




    def MStoreTerminal(self, msgStoreTerminal):
        # MStoreTerminal terminal_position
        terminal_position = msgStoreTerminal.terminal_position
        token = self.tokens[terminal_position]
        terminal_name = self.token2terminal_name(token)
        terminal_set_idc = self.find_terminal_set_idc(terminal_name)
        if len(terminal_set_idc) == 0:
            raise ParseFailError(f'unrecognize: terminal_name={terminal_name!r}, token={token!r}, position={terminal_position}')


        for terminal_set_idx in terminal_set_idc:
            #IStoreTerminal
            yield self.mk.IStoreTerminal(terminal_set_idx, terminal_position)
    def MStoreNonterminal(self, message):
        #IStoreNonterminal
        yield self.mk.IStoreNonterminal(
                message.nonterminal_idx
                ,message.terminal_position_begin
                ,message.terminal_position_end
                )
        #IStoreNonterminal_
        yield self.mk.IStoreNonterminal_(
                message.nonterminal_idx
                ,message.terminal_position_begin
                )
    def MStoreProduction(self, message):
        cfg = self.cfg
        production_idx = message.production_idx
        nonterminal_idx = cfg.production_idx2nonterminal_idx[production_idx]

        #IStoreProduction
        yield self.mk.IStoreProduction(
                message.production_idx
                ,message.terminal_position_begin
                ,message.terminal_position_end
                )
        #IStoreProduction_
        yield self.mk.IStoreProduction_(
                message.production_idx
                ,message.terminal_position_begin
                )
        #IStoreNonterminalChoice
        yield self.mk.IStoreNonterminalChoice(
                nonterminal_idx
                ,message.terminal_position_begin
                ,message.terminal_position_end
                )
    def MStoreAlternativeTail(self, message):
        #IStoreAlternativeTail
        yield self.mk.IStoreAlternativeTail(
                message.alternative_tail_idx
                ,message.terminal_position_begin
                ,message.terminal_position_end
                )
        #IStoreAlternativeTail_
        yield self.mk.IStoreAlternativeTail_(
                message.alternative_tail_idx
                ,message.terminal_position_begin
                )
    def MStoreNonNullAlternativeTailChoice(self, message):
        #IStoreNonNullAlternativeTailChoice
        interface = self.mk.IStoreNonNullAlternativeTailChoice(
                message.alternative_tail_idx
                ,message.terminal_position_begin
                ,message.terminal_position_end
                )
        yield interface





    def AOnDownwardNonterminal_(self, action, msgDownwardNonterminal_):
        cfg = self.cfg
        # MDownwardNonterminal_ nonterminal_idx terminal_position
        nonterminal_idx = msgDownwardNonterminal_.nonterminal_idx
        terminal_position = msgDownwardNonterminal_.terminal_position
        production_idc = cfg.nonterminal_idx2sorted_production_idc[nonterminal_idx]
        for production_idx in production_idc:
            #MDownwardProduction_
            yield self.mk.MDownwardProduction_(production_idx, terminal_position)
            #IStoreProduction_
            iStoreProduction_ = self.mk.IStoreProduction_(production_idx, terminal_position)
            #AUpwardToNonterminal
            yield self.mk.AUpwardToNonterminal(iStoreProduction_)

    def AOnDownwardProduction_(self, action, msgDownwardProduction_):
        cfg = self.cfg
        # MDownwardProduction_ production_idx terminal_position
        production_idx = msgDownwardProduction_.production_idx
        terminal_position = msgDownwardProduction_.terminal_position
        alternative_tail_idx = cfg.production_idx2alternative_tail_idx[production_idx]
        #MDownwardAlternativeTail_
        yield self.mk.MDownwardAlternativeTail_(alternative_tail_idx, terminal_position)
        #IStoreAlternativeTail_
        iStoreAlternativeTail_ = self.mk.IStoreAlternativeTail_(alternative_tail_idx, terminal_position)
        #AUpwardToProduction
        yield self.mk.AUpwardToProduction(production_idx, iStoreAlternativeTail_)


    def AOnDownwardAlternativeTail_(self, action, msgDownwardAlternativeTail_):
        #from seed.tiny import print_err; print_err('AOnDownwardAlternativeTail_!!!!!!!!!!!!')
        cfg = self.cfg
        # MDownwardAlternativeTail_ alternative_tail_idx terminal_position
        alternative_tail_idx = msgDownwardAlternativeTail_.alternative_tail_idx
        terminal_position = msgDownwardAlternativeTail_.terminal_position
        may_pair = cfg.alternative_tail_idx2alternative_idx_maybe_pair[alternative_tail_idx]
        if not may_pair:
            #AAutoNullAlternativeTail
            #MStoreAlternativeTail
            yield self.mk.MStoreAlternativeTail(
                    alternative_tail_idx
                    ,terminal_position
                    ,terminal_position
                    )
            return
        ref_symbol_psidx, rhs_alternative_tail_idx = pair = may_pair
        is_nonterminal, idx = cfg.explain_ref_symbol_psidx(ref_symbol_psidx)
        #from seed.tiny import print_err; print_err(f'AOnDownwardAlternativeTail_: ref_symbol_psidx = {ref_symbol_psidx}!!!!!!!!!!!!')
        if is_nonterminal:
            nonterminal_idx = idx
            #MDownwardNonterminal_
            yield self.mk.MDownwardNonterminal_(nonterminal_idx, terminal_position)
            #IStoreNonterminal_
            iStoreNonterminal_ = self.mk.IStoreNonterminal_(nonterminal_idx, terminal_position)
            # AUpwardFromNonterminal
            yield self.mk.AUpwardFromNonterminal(alternative_tail_idx, iStoreNonterminal_)
        else:
            #from seed.tiny import print_err; print_err(f'AOnDownwardAlternativeTail_: terminal_set_idx = {idx}!!!!!!!!!!!!')
            terminal_set_idx = idx
            #MDownwardTerminal_
            yield self.mk.MDownwardTerminal_(terminal_set_idx, terminal_position)
            #IStoreTerminal
            iStoreTerminal = self.mk.IStoreTerminal(terminal_set_idx, terminal_position)
            #AUpwardFromTerminal
            yield self.mk.AUpwardFromTerminal(alternative_tail_idx, iStoreTerminal)
            #
    def AOnDownwardTerminal_(self, action, msgDownwardTerminal_):
        #from seed.tiny import print_err; print_err('AOnDownwardTerminal_!!!!!!!!!!!!')
        cfg = self.cfg
        # MDownwardTerminal_ terminal_set_idx terminal_position
        terminal_position = msgDownwardTerminal_.terminal_position
        if self.max_required_terminal_position > terminal_position: raise logic-error
        assert terminal_position-1 <= self.max_required_terminal_position <= terminal_position
        self.max_required_terminal_position = terminal_position
        return
        yield # null iter



    def AOnForwardAlternativeTail_(self, action, msgForwardAlternativeTail_):
        cfg = self.cfg
        # MForwardAlternativeTail_ alternative_tail_idx terminal_position_begin terminal_position_middle
        alternative_tail_idx = msgForwardAlternativeTail_.alternative_tail_idx
        terminal_position_begin = msgForwardAlternativeTail_.terminal_position_begin
        terminal_position_middle = msgForwardAlternativeTail_.terminal_position_middle


        #MDownwardAlternativeTail_
        #bug: should use rhs_alternative_tail_idx
        #   yield self.mk.MDownwardAlternativeTail_(alternative_tail_idx, terminal_position_middle)
        #rhs_alternative_tail_idx = ??
        may_pair = cfg.alternative_tail_idx2alternative_idx_maybe_pair[alternative_tail_idx]
        if not may_pair: raise logic-error
        _, rhs_alternative_tail_idx = pair = may_pair
        #MDownwardAlternativeTail_
        yield self.mk.MDownwardAlternativeTail_(rhs_alternative_tail_idx, terminal_position_middle)

        #IStoreAlternativeTail_
        rhs_iStoreAlternativeTail_ = self.mk.IStoreAlternativeTail_(rhs_alternative_tail_idx, terminal_position_middle)

        ref_symbol_psidx, rhs_alternative_tail_idx = pair = may_pair
        is_nonterminal, idx = cfg.explain_ref_symbol_psidx(ref_symbol_psidx)
        if is_nonterminal:
            nonterminal_idx = idx
            #IStoreNonterminal
            iStoreNonterminal = self.mk.IStoreNonterminal(
                nonterminal_idx, terminal_position_begin, terminal_position_middle)
            #ABackwardNonterminal
            yield self.mk.ABackwardNonterminal(alternative_tail_idx, iStoreNonterminal, rhs_iStoreAlternativeTail_)
        else:
            terminal_set_idx = idx
            #IStoreTerminal
            iStoreTerminal = self.mk.IStoreTerminal(terminal_set_idx, terminal_position_begin)
            #ABackwardTerminal
            yield self.mk.ABackwardTerminal(alternative_tail_idx, iStoreTerminal, rhs_iStoreAlternativeTail_)



    def AUpwardToProduction(self, action, msgStoreAlternativeTail):
        cfg = self.cfg
        # MStoreAlternativeTail alternative_tail_idx terminal_position_begin terminal_position_end
        production_idx = action.production_idx
        terminal_position_begin = msgStoreAlternativeTail.terminal_position_begin
        terminal_position_end = msgStoreAlternativeTail.terminal_position_end
        #MStoreProduction
        yield self.mk.MStoreProduction(
            production_idx, terminal_position_begin, terminal_position_end)
    def AUpwardToNonterminal(self, action, msgStoreProduction):
        cfg = self.cfg
        # MStoreProduction production_idx terminal_position_begin terminal_position_end
        production_idx = msgStoreProduction.production_idx
        terminal_position_begin = msgStoreProduction.terminal_position_begin
        terminal_position_end = msgStoreProduction.terminal_position_end
        nonterminal_idx = cfg.production_idx2nonterminal_idx[production_idx]
        #MStoreNonterminal
        yield self.mk.MStoreNonterminal(
            nonterminal_idx, terminal_position_begin, terminal_position_end)
    def AUpwardFromTerminal(self, action, msgStoreTerminal):
        cfg = self.cfg
        # MStoreTerminal terminal_position
        alternative_tail_idx = action.alternative_tail_idx
        terminal_position = msgStoreTerminal.terminal_position
        #MForwardAlternativeTail_
        yield self.mk.MForwardAlternativeTail_(
                alternative_tail_idx
                ,terminal_position
                ,terminal_position+1
                )
    def AUpwardFromNonterminal(self, action, msgStoreNonterminal):
        cfg = self.cfg
        # MStoreNonterminal nonterminal_idx terminal_position_begin terminal_position_end
        alternative_tail_idx = action.alternative_tail_idx
        terminal_position_begin = msgStoreNonterminal.terminal_position_begin
        terminal_position_end = msgStoreNonterminal.terminal_position_end
        #MForwardAlternativeTail_
        yield self.mk.MForwardAlternativeTail_(
                alternative_tail_idx
                ,terminal_position_begin
                ,terminal_position_end
                )
    def ABackwardTerminal(self, action, msgStoreTerminal, msgStoreAlternativeTail):
        cfg = self.cfg
        # MStoreTerminal terminal_position
        # MStoreAlternativeTail alternative_tail_idx terminal_position_begin terminal_position_end
        alternative_tail_idx = action.alternative_tail_idx
        terminal_position_begin = msgStoreTerminal.terminal_position
        terminal_position_middle = msgStoreAlternativeTail.terminal_position_begin
        assert terminal_position_middle == terminal_position_begin+1
        terminal_position_end = msgStoreAlternativeTail.terminal_position_end
        #MStoreNonNullAlternativeTailChoice
        yield self.mk.MStoreNonNullAlternativeTailChoice(
                alternative_tail_idx
                ,terminal_position_begin
                ,terminal_position_middle
                ,terminal_position_end
                )

    def ABackwardNonterminal(self, action, msgStoreNonterminal, msgStoreAlternativeTail):
        cfg = self.cfg
        # MStoreNonterminal nonterminal_idx terminal_position_begin terminal_position_end
        # MStoreAlternativeTail alternative_tail_idx terminal_position_begin terminal_position_end
        alternative_tail_idx = action.alternative_tail_idx
        terminal_position_begin = msgStoreNonterminal.terminal_position_begin
        terminal_position_middle = msgStoreAlternativeTail.terminal_position_begin
        assert terminal_position_middle == msgStoreNonterminal.terminal_position_end
        terminal_position_end = msgStoreAlternativeTail.terminal_position_end
        #MStoreNonNullAlternativeTailChoice
        yield self.mk.MStoreNonNullAlternativeTailChoice(
                alternative_tail_idx
                ,terminal_position_begin
                ,terminal_position_middle
                ,terminal_position_end
                )
    def AOnIStoreNonNullAlternativeTailChoice(self, action, msg):
        #let MStoreNonNullAlternativeTailChoice -> MStoreAlternativeTail
        cfg = self.cfg
        # MStoreNonNullAlternativeTailChoice alternative_tail_idx terminal_position_begin terminal_position_middle terminal_position_end

        #MStoreAlternativeTail
        yield self.mk.MStoreAlternativeTail(
                msg.alternative_tail_idx
                ,msg.terminal_position_begin
                ,msg.terminal_position_end
                )

    #def AAutoNullAlternativeTail(self, action):




    def __init__(self, cfg, *
        , start_nonterminal_idc
        , token2terminal_name
        , find_terminal_set_idc
        , ambiguous_nonterminal_idc
        , to_cache_find_terminal_set_idc:bool = False
        ):
        def check_nonterminal_idx(idx):
            if type(idx) is not int: raise TypeError
            if not 0 <= idx < cfg.num_nonterminals: raise TypeError
            return True
        if not callable(token2terminal_name): raise TypeError
        if not callable(find_terminal_set_idc): raise TypeError

        ambiguous_nonterminal_idc = frozenset(ambiguous_nonterminal_idc)
        start_nonterminal_idc = frozenset(start_nonterminal_idc)
        all(map(check_nonterminal_idx, ambiguous_nonterminal_idc))
        all(map(check_nonterminal_idx, start_nonterminal_idc))


        it = self.__iter_initial_xmessages(start_nonterminal_idc, cfg)
        self.cfg = cfg
        self.start_nonterminal_idc = start_nonterminal_idc
        self.__token2terminal_name = token2terminal_name
        self.__find_terminal_set_idc = find_terminal_set_idc
        self.__restart_init()
        self.__ambiguous_nonterminal_idc = ambiguous_nonterminal_idc
        self.__maybe_cache_for_find_terminal_set_idc = {} if to_cache_find_terminal_set_idc else None
        super().__init__(initial_xmessages = list(it))

    def restart(self):
        self.__restart_init()
        super().restart()
    def __restart_init(self):
        self.tokens = []
        self.max_required_terminal_position = -1

    def feed(self, token):
        terminal_position = len(self.tokens)
        self.tokens.append(token) # before put_message

        #MStoreTerminal
        msgStoreTerminal = self.mk.MStoreTerminal(terminal_position)
        self.put_message(msgStoreTerminal)
        if 0 and __debug__:
            #print_err#toberemove#TODO#
            self._MessageClosureExecutor_ABC__with_data__xmessage_queue.reverse()
        return

    def __iter_initial_xmessages(self, start_nonterminal_idc, cfg):
        terminal_position = 0
        #MDownwardNonterminal_
        for start_nonterminal_idx in start_nonterminal_idc:
            yield self.mk.MDownwardNonterminal_(start_nonterminal_idx, terminal_position)

    def extract_parse_main_tree(self):
        forest = []
        for start_nonterminal_idx in self.start_nonterminal_idc:
            try:
                tree = self.extract_parse_local_tree(
                        start_nonterminal_idx, 0, len(self.tokens))
            except NotExistsError:
                pass
            else:
                forest.append(tree)

        cfg = self.cfg
        def on_err(nonterminal_idc):
            nonterminal_idc = sorted(set(nonterminal_idc))
            nonterminal_names = [
                cfg.nonterminal_idx2nonterminal_name[nonterminal_idx]
                for nonterminal_idx in nonterminal_idc
                ]
            err_msg = f'nonterminal_idc={nonterminal_idc}; nonterminal_names={nonterminal_names}'
            return err_msg
        L = len(forest)
        if L == 1:
            [tree] = forest
            return tree
        elif not L:
            err_msg = on_err(self.start_nonterminal_idc)
            raise NotExistsError(f'no start_nonterminal success: {err_msg}')
        else:
            err_msg = on_err(node.nonterminal_idx for node in forest)
            raise MultiStartNonterminalError(f'too many start_nonterminal success: {err_msg}')


    def extract_parse_local_tree(self, nonterminal_idx, terminal_position_begin, terminal_position_end):
        # if not exist then raise NotExistsError
        # if not a tree then raise NotTreeError

        #IStoreNonterminalChoice
        iStoreNonterminalChoice = self.mk.IStoreNonterminalChoice(nonterminal_idx, terminal_position_begin, terminal_position_end)
        queries = set()
        return self._nonterminal2node(queries, iStoreNonterminalChoice)

    def __to_tree_preprocess(self, queries, interface
        , *, allow_ambiguous
        ):
        if interface in queries:
            # should not go here!!!
            raise logic-error
            raise NotTreeError__recur(interface)
        queries.add(interface)

        messages = self.interface2messages.get(interface, ())
        L = len(messages)
        if not L:
            raise NotExistsError(interface)
        elif L > 1:
            if not allow_ambiguous:
                # _terminal2node should be False
                raise NotTreeError__ambiguous(interface)
            message = self.__handle_ambiguous_nonterminal_idx(messages)
        else:
            #L == 1:
            [message] = messages
        return message

    def __is_empty_production(self, production_idx):
        cfg = self.cfg
        alternative_tail_idx = cfg.production_idx2alternative_tail_idx[production_idx]
        return self.__is_empty_alternative_tail_idx(alternative_tail_idx)
    def __is_empty_alternative_tail_idx(self, alternative_tail_idx):
        cfg = self.cfg
        may_pair = cfg.alternative_tail_idx2alternative_idx_maybe_pair[alternative_tail_idx]
        return not may_pair
    def __handle_ambiguous_nonterminal_idx(self, messages):
        # -> message

        assert len(messages) >= 2
        a_message = messages[0]
        message_constructor = self.message2constructor(a_message)
        cfg = self.cfg

        if message_constructor == 'MStoreProduction':
        #_nonterminal2node#iStoreNonterminalChoice
        # MStoreProduction production_idx terminal_position_begin terminal_position_end
        #
        #_production2children#iStoreProduction
        # MStoreProduction production_idx terminal_position_begin terminal_position_end
        #
            if a_message.terminal_position_begin == a_message.terminal_position_end:
                # empty ==>> try to find empty alternative
                production_idc = set()
                for message in messages:
                    production_idx = message.production_idx
                    if production_idx in production_idc: continue
                    production_idc.add(production_idx)
                    if self.__is_empty_production(production_idx):
                        return message
                else:
                    return a_message # arbitrary
            # not empty ==>> try to find at least two nonemtpy children
            alternative_tail_idc = set()
            for message in messages:
                production_idx = message.production_idx
                alternative_tail_idx = cfg.production_idx2alternative_tail_idx[production_idx]
                if alternative_tail_idx in alternative_tail_idc: continue
                alternative_tail_idc.add(alternative_tail_idx)
                #IStoreNonNullAlternativeTailChoice
                iStoreNonNullAlternativeTailChoice = \
                    self.mk.IStoreNonNullAlternativeTailChoice(
                        alternative_tail_idx
                        ,message.terminal_position_begin
                        ,message.terminal_position_end
                    )
                # MStoreNonNullAlternativeTailChoice alternative_tail_idx terminal_position_begin terminal_position_middle terminal_position_end
                submessages = self.interface2messages.get(iStoreNonNullAlternativeTailChoice, ())
                for submessage in submessages:
                    if submessage.terminal_position_begin < submessage.terminal_position_middle < submessage.terminal_position_end:
                        return message # not submessage
            else:
                return a_message # arbitrary
        elif message_constructor == 'MStoreNonNullAlternativeTailChoice':
        # MStoreNonNullAlternativeTailChoice alternative_tail_idx terminal_position_begin terminal_position_middle terminal_position_end
        #   from _alternative_tail2linked_nodes
        #
            for message in messages:
                if message.terminal_position_begin < message.terminal_position_middle < message.terminal_position_end:
                    return message
            else:
                return a_message # arbitrary

        else:
            raise logic-error --unknown-message_constructor
        #_terminal2node#iStoreTerminal
        # MStoreTerminal terminal_position

    def __is_allowed_ambiguous_production_idx(self, production_idx):
        cfg = self.cfg
        nonterminal_idx = cfg.production_idx2nonterminal_idx[production_idx]
        return self.__is_allowed_ambiguous_nonterminal_idx(nonterminal_idx)
    def __is_allowed_ambiguous_nonterminal_idx(self, nonterminal_idx):
        allow_ambiguous = nonterminal_idx in self.__ambiguous_nonterminal_idc
        return allow_ambiguous
    def _nonterminal2node(self, queries, iStoreNonterminalChoice):
        allow_ambiguous = self.__is_allowed_ambiguous_nonterminal_idx(
            iStoreNonterminalChoice.nonterminal_idx)
        message = self.__to_tree_preprocess(
                        queries, iStoreNonterminalChoice
                        , allow_ambiguous=allow_ambiguous)
        del allow_ambiguous

        # MStoreProduction production_idx terminal_position_begin terminal_position_end

        #IStoreProduction
        iStoreProduction = self.mk.IStoreProduction(
            message.production_idx
            ,message.terminal_position_begin
            ,message.terminal_position_end
            )
        children = self._production2children(queries, iStoreProduction)

        cfg = self.cfg
        nonterminal_idx = iStoreNonterminalChoice.nonterminal_idx
        production_idx = message.production_idx
        nonterminal_name = cfg.nonterminal_idx2nonterminal_name[nonterminal_idx]
        production_name = cfg.production_idx2production_name[production_idx]
        return ParseTreeNonleafNode(
            nonterminal_idx=nonterminal_idx
            ,production_idx=production_idx
            ,nonterminal_name=nonterminal_name
            ,production_name=production_name
            ,terminal_position_begin=message.terminal_position_begin
            ,terminal_position_end=message.terminal_position_end
            ,children=tuple(children)
            )
    def _production2children(self, queries, iStoreProduction):
        # -> [Node]
        allow_ambiguous = self.__is_allowed_ambiguous_production_idx(
                            iStoreProduction.production_idx)
        message = self.__to_tree_preprocess(queries, iStoreProduction
                        , allow_ambiguous=allow_ambiguous)
        #del allow_ambiguous -- used below
        # MStoreProduction production_idx terminal_position_begin terminal_position_end

        cfg = self.cfg
        alternative_tail_idx = cfg.production_idx2alternative_tail_idx[message.production_idx]
        #IStoreAlternativeTail
        iStoreAlternativeTail = self.mk.IStoreAlternativeTail(
            alternative_tail_idx
            ,message.terminal_position_begin
            ,message.terminal_position_end
            )
        linked_list = self._alternative_tail2linked_nodes(
                                queries, iStoreAlternativeTail
                                , allow_ambiguous=allow_ambiguous)

        children = []
        while linked_list:
            child, linked_list = linked_list
            children.append(child)
        return children

    def _alternative_tail2linked_nodes(self
        , queries, iStoreAlternativeTail, *, allow_ambiguous
        ):
        # -> linked_list<Node>
        # -> (Node, linked_list<Node>) | ()
        cfg = self.cfg
        may_pair = cfg.alternative_tail_idx2alternative_idx_maybe_pair[
                        iStoreAlternativeTail.alternative_tail_idx]
        if not may_pair:
            return ()

        #IStoreNonNullAlternativeTailChoice
        iStoreNonNullAlternativeTailChoice = \
            self.mk.IStoreNonNullAlternativeTailChoice(
                **iStoreAlternativeTail._asdict()
            )

        message = self.__to_tree_preprocess(
                        queries, iStoreNonNullAlternativeTailChoice
                        , allow_ambiguous=allow_ambiguous)
        # MStoreNonNullAlternativeTailChoice alternative_tail_idx terminal_position_begin terminal_position_middle terminal_position_end
        #
        terminal_position_begin = message.terminal_position_begin
        terminal_position_middle = message.terminal_position_middle
        terminal_position_end = message.terminal_position_end

        ref_symbol_psidx, rhs_alternative_tail_idx = pair = may_pair
        node = self._ref_symbol_psidx2node(
            queries, ref_symbol_psidx
            , terminal_position_begin, terminal_position_middle
            )

        #IStoreAlternativeTail
        rhs_iStoreAlternativeTail = self.mk.IStoreAlternativeTail(
            rhs_alternative_tail_idx
            ,terminal_position_middle
            ,terminal_position_end
            )
        rhs_linked_list = self._alternative_tail2linked_nodes(
                                    queries, rhs_iStoreAlternativeTail
                                    , allow_ambiguous=allow_ambiguous)
        linked_list = node, rhs_linked_list
        return linked_list


    def _ref_symbol_psidx2node(self
        , queries, ref_symbol_psidx
        , terminal_position_begin, terminal_position_end
        ):
        cfg = self.cfg
        is_nonterminal, idx = cfg.explain_ref_symbol_psidx(ref_symbol_psidx)
        if is_nonterminal:
            nonterminal_idx = idx
            #IStoreNonterminalChoice
            iStoreNonterminalChoice = self.mk.IStoreNonterminalChoice(nonterminal_idx, terminal_position_begin, terminal_position_end)
            return self._nonterminal2node(queries, iStoreNonterminalChoice)
        else:
            terminal_set_idx = idx
            #IStoreTerminal
            iStoreTerminal = self.mk.IStoreTerminal(terminal_set_idx, terminal_position_begin)
            return self._terminal2node(queries, iStoreTerminal)
    def _terminal2node(self, queries, iStoreTerminal):
        cfg = self.cfg
        message = self.__to_tree_preprocess(queries, iStoreTerminal
                        , allow_ambiguous=False)
        # MStoreTerminal terminal_position
        terminal_position = message.terminal_position
        terminal_set_idx = iStoreTerminal.terminal_set_idx
        terminal_set_name = cfg.terminal_set_idx2terminal_set_name[terminal_set_idx]

        token = self.tokens[terminal_position]
        terminal_name = self.token2terminal_name(token)
        return ParseTreeLeafNode(
            terminal_set_idx=terminal_set_idx
            ,terminal_set_name=terminal_set_name
            ,terminal_position_begin=terminal_position
            ,terminal_position_end=terminal_position+1
            ,terminal_name=terminal_name
            ,token=token
            )


if __name__ == "__main__":
    def make_parse_example_result(t):
        pass


def _t():
    from pprint import pprint
    from ..CFG import CFG
    from ..the_py_terminal_set_ops import the_py_terminal_set_ops
    terminal_set_ops = the_py_terminal_set_ops
    terminal_set_name2terminal_set = lambda a:{a}
    make = lambda *args, **kwargs: CFG.make_CFG__hashable_name__less(
        *args
        , explain_ref_symbol_name=explain_ref_symbol_name
        , terminal_set_ops=terminal_set_ops
        , terminal_set_name2terminal_set=terminal_set_name2terminal_set
        , **kwargs)
    __pairs = [('S', ['Ts1']), ('Ts1', ['Ts0', 't']), ('Ts0', ['Ts1']), ('Ts0', [])]
    #__pairs = [('S', ['t', 't'])]
    #__pairs = [('S', ['t'])]
    explain_ref_symbol_name = lambda name: (name[0].isupper(), name)
    cfg = make(__pairs)

    find_terminal_set_idc = lambda terminal_set_idx2terminal_set, terminal_name: [terminal_set_idx2terminal_set.index({terminal_name})]
    class t:pass
    token2terminal_name = lambda token: token.__name__
    start_nonterminal_name = 'S'
    start_nonterminal_idx = cfg.nonterminal_name2nonterminal_idx(start_nonterminal_name)

    tokens = [t]*4
    r = parse_CFG(cfg, iter(tokens), start_nonterminal_idc=[start_nonterminal_idx], token2terminal_name=token2terminal_name, find_terminal_set_idc=find_terminal_set_idc, ambiguous_nonterminal_idc=())
    #pprint(r)#bad#one line!
    from nn_ns.lang.reformat_py_source import easy_print_for_namedtuple
    easy_print_for_namedtuple(r, indent=' '*4, depth=0, file=None)



if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

