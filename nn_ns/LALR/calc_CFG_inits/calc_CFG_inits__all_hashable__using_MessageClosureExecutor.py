

__all__ = '''
    calc_CFG_inits__all_hashable__using_MessageClosureExecutor
    '''.split()



from nn_ns.MessageClosureExecutor\
    .MessageClosureExecutor__mixins__collect_functions import \
    MessageClosureExecutor__mixins__collect_functions
from nn_ns.MessageClosureExecutor\
    .MessageClosureExecutor_ABC__using_namedtuple import \
    MessageClosureExecutor_ABC__using_namedtuple
from nn_ns.MessageClosureExecutor\
    .MessageClosureExecutor__mixins__remove_checks import \
    MessageClosureExecutor__mixins__remove_checks
from nn_ns.MessageClosureExecutor.make_namedtuples import make_namedtuples
from .iter_rule_names_for_calc_CFG_inits import \
    iter_rule_names_for_calc_CFG_inits

namedtuples_in_str = '''
ITerminal terminal_set_name
    MTerminal terminal_set_name
IRuleInit rule_name
    MRuleInit rule_name init
IProductionIdxInit alternative_name idx
    MProductionIdxInit alternative_name idx init

ABackwardT terminal_interface production_interface
ABackwardN rule_interface production_interface
AUpward production_interface
'''
#ABackwardN (IRuleInit rule_name) (IProductionIdxInit alternative_name idx)

interface_constraint = dict(
    IRuleInit = 'MRuleInit'
    ,IProductionIdxInit = 'MProductionIdxInit'
    ,ITerminal = 'MTerminal'
    )
action_constraint = {
    'ABackwardT': ('ITerminal', 'IProductionIdxInit')
    ,'ABackwardN': ('IRuleInit', 'IProductionIdxInit')
    ,'AUpward': ('IProductionIdxInit',)
    }

#type_name2type = make_namedtuples(namedtuples_in_str)
class _MessageClosureExecutor(
    MessageClosureExecutor_ABC__using_namedtuple
    ,MessageClosureExecutor__mixins__collect_functions
    ,MessageClosureExecutor__mixins__remove_checks
    ):
    @classmethod
    def get_namedtuples_in_str(cls):
        return namedtuples_in_str
    #all_message_constructors = 'MRuleInit MProductionIdxInit'.split()
    @classmethod
    def get_interface_constraint(cls):
        return interface_constraint
    @classmethod
    def get_action_constraint(cls):
        return action_constraint

    def __iter_initial_xmessages(self):
        def mkA(type_name, *args):
            return self.action2xmessage(
                self.name2constructor[type_name](*args))
        def mkI(type_name, *args):
            return self.name2constructor[type_name](*args)
        def mkM(type_name, *args):
            return self.message2xmessage(
                self.name2constructor[type_name](*args))
        if self.alternative_name_fullmapping_is_sequence:
            items_of = enumerate
        else:
            def items_of(alternative_name_fullmapping):
                return alternative_name_fullmapping.items()

        '''
        alternative_name_fullmapping_ops = \
            FullMappingOps__mapping__XXX_name_fullmapping_ops(
                frozenset(alternative_name2rule_name)
                , items2mapping=dict, unbox=None, box=None
                )
        it = iter_rule_names_for_calc_CFG_inits(
                alternative_name2rule_name
                ,alternative_name2ixsymbols
                ,alternative_name_fullmapping_ops
                )
        for rule_name in it:
        '''
        for alternative_name, _ in items_of(self.alternative_name2rule_name):
            production_interface = mkI(
                'IProductionIdxInit', alternative_name, 0)
            yield mkA('AUpward', production_interface)

        for alternative_name, ixsymbols in items_of(self.alternative_name2ixsymbols):
            for idx, ixsymbol in enumerate(ixsymbols, 1):
                production_interface = mkI('IProductionIdxInit', alternative_name, idx)

                (is_rule_name, terminal_set_name_or_rule_name) = ixsymbol
                if is_rule_name:
                    rule_name = terminal_set_name_or_rule_name
                    rule_interface = mkI('IRuleInit', rule_name)
                    yield mkA('ABackwardN', rule_interface, production_interface)
                else:
                    terminal_set_name = terminal_set_name_or_rule_name
                    terminal_interface = mkI('ITerminal', terminal_set_name)
                    yield mkA('ABackwardT', terminal_interface, production_interface)
                    yield mkM('MTerminal', terminal_set_name)

        ######### messages
        for alternative_name, ixsymbols in items_of(self.alternative_name2ixsymbols):
            idx = len(ixsymbols)
            yield mkM('MProductionIdxInit', alternative_name, idx, ())

    def __init__(self
        ,max_init_length
        ,alternative_name2rule_name
        ,alternative_name2ixsymbols
        ,*
        ,alternative_name_fullmapping_is_sequence : bool
        ):
        self.max_init_length = max_init_length
        self.alternative_name2rule_name = alternative_name2rule_name
        self.alternative_name2ixsymbols = alternative_name2ixsymbols
        self.alternative_name_fullmapping_is_sequence = bool(
            alternative_name_fullmapping_is_sequence)

        initial_xmessages = frozenset(self.__iter_initial_xmessages())
        super().__init__(initial_xmessages=initial_xmessages)

    def AUpward(self, action, msg_production_idx_init):
        if msg_production_idx_init.idx == 0:
            alternative_name = msg_production_idx_init.alternative_name
            rule_name = self.alternative_name2rule_name[alternative_name]
            init = msg_production_idx_init.init
            yield self.name2constructor['MRuleInit'](rule_name, init)
    def ABackwardT(self, action, msg_terminal, msg_production_idx_init):
        init0 = (msg_terminal.terminal_set_name,)
        return self.__ABackwardX(init0, msg_production_idx_init)
    def ABackwardN(self, action, msg_rule_init, msg_production_idx_init):
        init0 = msg_rule_init.init
        return self.__ABackwardX(init0, msg_production_idx_init)
    def __ABackwardX(self, init0, msg_production_idx_init):
        init1 = msg_production_idx_init.init
        init = init0 + init1[:self.max_init_length-len(init0)]
        idx = msg_production_idx_init.idx
        assert idx > 0
        yield self.message2xmessage(
            msg_production_idx_init._replace(idx=idx-1, init=init))
    def MRuleInit(self, msg_rule_init):
        yield self.name2constructor['IRuleInit'](
            msg_rule_init.rule_name
            )
    def MProductionIdxInit(self, msg_production_idx_init):
        yield self.name2constructor['IProductionIdxInit'](
            msg_production_idx_init.alternative_name
            ,msg_production_idx_init.idx
            )
    def MTerminal(self, msg_terminal):
        yield self.name2constructor['ITerminal'](
            msg_terminal.terminal_set_name
            )

def calc_CFG_inits__all_hashable__using_MessageClosureExecutor(
    max_init_length
    ,alternative_name2rule_name
    ,alternative_name2ixsymbols
    ,*
    ,alternative_name_fullmapping_is_sequence : bool
    ,rule_name_fullmapping_is_sequence : bool
    ):
    '''wrapper for calc_CFG_inits
requires: Hashable: rule_name, alternative_name, terminal_set_name

input:
    max_init_length             :: UInt
    alternative_name2rule_name  :: python.dict if not is_sequence else seq
    alternative_name2ixsymbols  :: python.dict if not is_sequence else seq
    alternative_name_fullmapping_is_sequence    :: bool
    rule_name_fullmapping_is_sequence           :: bool

output:
    rule_name2inits             :: python.dict or list
    alternative_name2initss     :: python.dict or list
        see: ..._is_sequence
see:
    #calc_CFG_inits__all_hashable
'''
    alternative_name_fullmapping_is_sequence = bool(
        alternative_name_fullmapping_is_sequence)

    e = _MessageClosureExecutor(
        max_init_length
        ,alternative_name2rule_name
        ,alternative_name2ixsymbols
        ,alternative_name_fullmapping_is_sequence
            = alternative_name_fullmapping_is_sequence
        )
    e.execute_until_closure()
    if alternative_name_fullmapping_is_sequence:
        keys_of = lambda ls: range(len(ls))
        items_of = enumerate
        L = len(alternative_name2rule_name)
        alternative_name2initss = [[] for _ in range(L)]
    else:
        keys_of = lambda d: iter(d)
        items_of = dict.items
        alternative_name2initss = {k: []for k in alternative_name2rule_name}

    rule_name2inits = {}

    for interface, messages in e.interface2messages.items():
        interface_constructor = e.interface2constructor(interface)
        if 'ITerminal' == interface_constructor:
            pass
        elif 'IRuleInit' == interface_constructor:
            rule_name = interface.rule_name
            rule_name2inits[rule_name] = {
                message.init for message in messages}
        elif 'IProductionIdxInit' == interface_constructor:
            alternative_name = interface.alternative_name
            alternative_name2initss[alternative_name].append(
                (interface.idx, {message.init for message in messages})
                )
        else:
            raise logic-error

    for alternative_name, initss in items_of(alternative_name2initss):
        initss.sort()
        for i in range(len(initss)):
            idx, initss[i] = initss[i]






    def to_list_if_seq(is_sequence, mapping):
        if is_sequence:
            print(mapping)
            L = max(mapping, 0)
            return [mapping.get(i, set()) for i in range(L+1)]
        else:
            return mapping

    rule_name2inits = to_list_if_seq(
        rule_name_fullmapping_is_sequence, rule_name2inits)
    #alternative_name2initss = to_list_if_seq(
        #alternative_name_fullmapping_is_sequence, alternative_name2initss)
    return rule_name2inits, alternative_name2initss


