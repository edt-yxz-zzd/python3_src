

from .RegexArg import _RegexArgProcess, to_hashable_regex, _group, _and, _or
from .SerialNFAs2DFA import CONCAT_NFAs_FinalLast
from .NFA import NFA
from .DFA import DFA
from .ParallelFAs2DFA import OR_FAs, AND_FAs

def item_key(item):
    case = item[0]
    if case == _group:
        L = len(item)
        assert 2 <= L <= 3
        name = item[1]
        if name == None:
            name = (0,)
        elif isinstance(name, int):
            name = (1, name)
        elif isinstance(name, str):
            name = (2, name)
        if L == 2:
            key = (1, name)
        else:
            regex = item[-1]
            h = hash(regex)
            key = (1, name, h)
        pass

    else:
        key = (0,)
        pass

    return key

    
class RegexArg2DFA(_RegexArgProcess):
    def __init__(self):
        self.regex_or_atom_or_item = []
        self.regex_or_atom_or_item2DFA = {}
        self.group_name2path = {}

        # path = [count|group_idx]
        # path stands for prev brother
        # when enter an item, path will append the count of it
        self.path = [0]
        pass
    def _process_regex(self, regex):
        case, value = regex
        if case == _not:
            dfa = value
            dfa = value.not_()
            pass
        
        elif len(value) < 2:
            if len(value) == 1:
                dfa, = value
            else:
                dfa = DFA.regex_null()
            pass
        
        elif case == _concat:
            item_dfas = value
            nfas = tuple(NFA.from_dfa(dfa) for dfa in item_dfas)
            dfa = CONCAT_NFAs_FinalLast(nfas)
            pass
        
        elif case in _join:
            item_dfas = value
            item_dfas = sorted(item_dfas, key=item_key)

            join = {_and: AND_FAs, _or: OR_FAs}[case]
            dfa = join(item_dfas)
            pass
        
        else:
            raise never-here


        return dfa
    
    def _process_items(self, items):
        return items
    
    def _process_item(self, item):
        arg = container_map(item)
        return arg
    def _process_count(self, count):
        arg = container_map(count)
        return arg
    
    def _process_group(self, group):
        arg = container_map(group)
        return arg
    def _process_token(self, token):
        arg = container_map(token)
        return arg
    def _process_symbol(self, symbol):
        return symbol
    def _process_symbols(self, symbols):
        return unorder_container_map(symbols)
                
        
