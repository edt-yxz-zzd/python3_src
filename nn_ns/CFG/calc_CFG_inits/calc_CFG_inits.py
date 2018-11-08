
__all__ = '''
    calc_CFG_inits
    translate_inits
    '''.split()

from ..CFG import CFG, the_py_terminal_set_ops
from ..MessageClosureExecutor.MessageClosureExecutor_ABC__using_namedtuple__str import \
    MessageClosureExecutor_ABC__using_namedtuple__str
#from ...MessageClosureExecutor__mixins__remove_checks import \
#    MessageClosureExecutor__mixins__remove_checks

class _M(MessageClosureExecutor_ABC__using_namedtuple__str):
    message_interface_action_definition_str = '''
; ITerminalInit terminal_set_idx
    <- MTerminalInit
    ; MTerminalInit terminal_set_idx
; INonterminalInit nonterminal_idx
    <- MNonterminalInit
    ; MNonterminalInit nonterminal_idx init
; IAlternativeTailInit alternative_tail_idx
    <- MAlternativeTailInit
    ; MAlternativeTailInit alternative_tail_idx init



; ABackwardT alternative_tail_idx iTerminalInit iAlternativeTailInit
    <- ITerminalInit IAlternativeTailInit
; ABackwardN alternative_tail_idx iNonterminalInit iAlternativeTailInit
    <- INonterminalInit IAlternativeTailInit
; AUpward nonterminal_idx iAlternativeTailInit
    <- IAlternativeTailInit
        '''

    def MTerminalInit(self, message):
        yield self.mkITerminalInit(message.terminal_set_idx)
    def MNonterminalInit(self, message):
        yield self.mkINonterminalInit(message.nonterminal_idx)
    def MAlternativeTailInit(self, message):
        yield self.mkIAlternativeTailInit(message.alternative_tail_idx)
    def ABackwardT(self, action, msg_TerminalInit, msg_AlternativeTailInit):
        try:
            msg_TerminalInit.terminal_set_idx
        except:
            from pprint import pprint
            pprint(self.interface2messages)
            raise

        init0 = (msg_TerminalInit.terminal_set_idx,)
        yield from self.__ABackwardX(action, init0, msg_AlternativeTailInit)
    def ABackwardN(self, action, msg_NonterminalInit, msg_AlternativeTailInit):
        init0 = msg_NonterminalInit.init
        yield from self.__ABackwardX(action, init0, msg_AlternativeTailInit)
    def __ABackwardX(self, action, init0, msg_AlternativeTailInit):
        init1 = msg_AlternativeTailInit.init
        L = self.max_init_length
        init = init0 + init1[:L-len(init0)]
        idx = action.alternative_tail_idx
        yield self.mkMAlternativeTailInit(idx, init)
    def AUpward(self, action, msg_AlternativeTailInit):
        idx = action.nonterminal_idx
        init = msg_AlternativeTailInit.init
        yield self.mkMNonterminalInit(idx, init)

    def __init__(self, max_init_length, cfg):
        assert max_init_length >= 0
        it = self.__iter_initial_xmessages(max_init_length, cfg)
        self.cfg = cfg
        self.max_init_length = max_init_length
        super().__init__(initial_xmessages = list(it))

    def __iter_initial_xmessages(self, max_init_length, cfg):
        for terminal_set_idx in range(cfg.num_terminal_sets):
            yield self.mkMTerminalInit(terminal_set_idx)
        if (max_init_length >= 0
            and len(cfg.alternative_tail_idx2alternative_idx_maybe_pair)
            ):
            idx = cfg.alternative_idx_maybe_pair2alternative_tail_idx(())
            init = ()
            yield self.mkMAlternativeTailInit(idx, init)

        ####### action
        it = zip(cfg.production_idx2nonterminal_idx
                , cfg.production_idx2alternative_tail_idx)
        for nonterminal_idx, alternative_tail_idx in it:
            iAlternativeTailInit = self.mkIAlternativeTailInit(alternative_tail_idx)
            yield self.mkAUpward(nonterminal_idx, iAlternativeTailInit)

        it = enumerate(cfg.alternative_tail_idx2alternative_idx_maybe_pair)
        for lhs_alternative_tail_idx, may_pair in it:
            if not may_pair: continue
            ref_symbol_psidx, rhs_alternative_tail_idx = pair = may_pair
            is_nonterminal, idx = \
                cfg.explain_ref_symbol_psidx(ref_symbol_psidx)
            if is_nonterminal:
                nonterminal_idx = idx
                idx2intf = self.mkINonterminalInit
                mkA = self.mkABackwardN
            else:
                terminal_set_idx = idx
                idx2intf = self.mkITerminalInit
                mkA = self.mkABackwardT

            iAlternativeTailInit = \
                self.mkIAlternativeTailInit(rhs_alternative_tail_idx)
            yield mkA(lhs_alternative_tail_idx
                    , idx2intf(idx)
                    , iAlternativeTailInit
                    )

    def collect(self):
        # -> (nonterminal_idx2inits, alternative_tail_idx2inits)
        self.execute_until_closure()
        cfg = self.cfg

        nonterminal_idx2inits = []
        for nonterminal_idx in range(cfg.num_nonterminals):
            interface = self.mkINonterminalInit(nonterminal_idx)
            messages = self.interface2messages.get(interface, ())
            inits = set(message.init for message in messages)
            nonterminal_idx2inits.append(inits)

        alternative_tail_idx2inits = []
        for alternative_tail_idx in range(cfg.num_alternative_tails):
            interface = self.mkIAlternativeTailInit(alternative_tail_idx)
            messages = self.interface2messages.get(interface, ())
            inits = set(message.init for message in messages)
            alternative_tail_idx2inits.append(inits)
        return nonterminal_idx2inits, alternative_tail_idx2inits

def _t():
    # collections.namedtuple
    # now change to seed.types.namedtuple
    from collections import defaultdict
    IT = _M.mkITerminalInit(terminal_set_idx=0)
    IA = _M.mkIAlternativeTailInit(alternative_tail_idx=0)
    MA = _M.mkMAlternativeTailInit(alternative_tail_idx=0, init=())
    d = defaultdict(list)
    assert hash(IT) == hash(IA)
    assert IT == IA
    d[IT]
    ls = d[IA]
    ls.append(MA)
    print(d)
#_t()

def calc_CFG_inits(__max_init_length, __context_free_grammar):
    '''
see:
    "def - init inits.txt"

input:
    max_init_length :: UInt
    context_free_grammar :: CFG
output:
    nonterminal_idx2inits :: [inits]
    alternative_tail_idx2inits :: [inits]
        where
            inits = {init}
            init = [terminal_set_idx]
'''
    maxL = __max_init_length
    cfg = __context_free_grammar

    executor = _M(maxL, cfg)
    (nonterminal_idx2inits, alternative_tail_idx2inits
    ) = executor.collect()
    return nonterminal_idx2inits, alternative_tail_idx2inits

def translate_inits(cfg, nonterminal_idx2inits, alternative_tail_idx2inits):
    # -> rule_name2inits, alternative_name2initss
    # -> nonterminal_name2inits, production_name2initss
    ls = terminal_set_idx2terminal_set_name = cfg.terminal_set_idx2terminal_set_name
    def idx_inits2name_inits(idx_inits):
        return set(map(idx_init2name_init, idx_inits))
    def idx_init2name_init(idx_init):
        return tuple(map(ls.__getitem__, idx_init))

    nonterminal_name2inits = {
        nonterminal_name : idx_inits2name_inits(idx_inits)
        for nonterminal_name, idx_inits in
            zip(cfg.nonterminal_idx2nonterminal_name
                , nonterminal_idx2inits)
        }
    def handle_alternative_tail_idx(alternative_tail_idx):
        # -> [name_inits]
        ls = []
        may_pair = (None, alternative_tail_idx)
        while may_pair:
            _, alternative_tail_idx = may_pair
            name_inits = idx_inits2name_inits(
                alternative_tail_idx2inits[alternative_tail_idx])
            ls.append(name_inits)
            may_pair = cfg.alternative_tail_idx2alternative_idx_maybe_pair[alternative_tail_idx]
        return ls

    production_name2initss = {
        production_name : handle_alternative_tail_idx(alternative_tail_idx)
        for production_name, alternative_tail_idx in
            zip(cfg.production_idx2production_name
                , cfg.production_idx2alternative_tail_idx)
        }
    return nonterminal_name2inits, production_name2initss




def _test():
    max_init_length = 3
    rule_name_ixsymbols_pairs = \
        [('S', [(True, 'Main')])
        ,('Main', [(True, 'Ts1')])
        ,('Ts1', [(True, 'Ts0'), (False, 'a')])
        ,('Ts0', [(True, 'Ts1')])
        ,('Ts0', [])
        ]
    rule_name2inits = \
        {'Main': {('a',), ('a', 'a'), ('a', 'a', 'a')}
        ,'S': {('a',), ('a', 'a'), ('a', 'a', 'a')}
        ,'Ts0': {(), ('a',), ('a', 'a'), ('a', 'a', 'a')}
        ,'Ts1': {('a',), ('a', 'a'), ('a', 'a', 'a')}
        }
    alternative_name2initss = \
        {('S',0): [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})]
        ,('Main',0): [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})]
        ,('Ts1',0): [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, {('a',)}, frozenset({()})]
        ,('Ts0',0): [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})]
        ,('Ts0',1): [frozenset({()})]
        }


    terminal_set_name2terminal_set = lambda a:{a}
    cfg = CFG.make_CFG__hashable_name__less(
        rule_name_ixsymbols_pairs
        ,explain_ref_symbol_name=lambda x:x
        ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
        ,terminal_set_ops=the_py_terminal_set_ops
        )

    (nonterminal_idx2inits, alternative_tail_idx2inits
    ) = calc_CFG_inits(max_init_length, cfg)

    (nonterminal_name2inits, production_name2initss
    ) = translate_inits(cfg, nonterminal_idx2inits, alternative_tail_idx2inits)

    print(f'nonterminal_name2inits = {nonterminal_name2inits}')
    print(f'rule_name2inits = {rule_name2inits}')
    print(f'production_name2initss = {production_name2initss}')
    print(f'alternative_name2initss = {alternative_name2initss}')
    assert nonterminal_name2inits == rule_name2inits
    assert production_name2initss == alternative_name2initss

if __name__ == "__main__":
    _test()



