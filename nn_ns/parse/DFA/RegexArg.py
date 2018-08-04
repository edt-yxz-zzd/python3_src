
'''
container = list | tuple
unorder_container = set | frozenset

token = container('symbol', unorder_container(symbol...))
      | container('symbol', 'not', unorder_container(symbol...))
      | container('any',)
symbol is any hashable object that would be fed to DFA, usually a string.

item = container(atom, count)
count = container(repeat,) | container(min, max) 
repeat is a positive integer
min is in range(0, inf)
max is None(means inf) or in range(min, inf)
# note : (n,) and (n,n) are different in sense of organizing the match result.

atom = group | refID
group = container('group', name, regex)
name is None or a string or a integer to identify this group.

refID = regex
regex = container('concat', container(item...))
      | container(join, unorder_container(item...))
      | container('not', regex)
      | container('null',)
      | token

join = 'and' | 'or'

'''


from sand import is_main

_concat = 'concat'
_and = 'and'
_or = 'or'
_group = 'group'
_not = 'not'
_join = frozenset([_and, _or])
#_token = 'token'
_any = 'any'
_symbol = 'symbol'

class _RegexArgProcess:
    def _process_regex(self, regex):
        return regex
    def _process_items(self, items):
        return items
    def _process_item(self, item):
        return item
    def _process_count(self, count):
        return count
    def _process_group(self, group):
        return group
    def _process_token(self, token):
        return token
    def _process_symbol(self, symbol):
        return symbol
    def _process_symbols(self, symbols):
        return symbols

    
    def throw(self, err = 'bad format'):
        raise ValueError(err)
    

    
    def process_regex(self, regex):
        case = regex[0]
        d = {_concat: self.process_concat,
             _and: self.process_and,
             _or: self.process_or,
             _not: self.process_and,
             _null: self.process_and,
             }
        f = d.get(case, self.process_token)
        arg = f(regex)

        #arg = type(regex)([case, value])

        return self._process_regex(arg)
    
    def process_items(self, items):
        container = type(items)
        process_item = self.process_item
        arg = container(process_item(item) for item in items)
        return self._process_items(arg)
        
    def process_item(self, item):
        container, (atom, count) = type(item), item
        arg = container([self.process_atom(atom), self.process_count(count)])
        return self._process_item(arg)
    
    def process_atom(self, atom):
        d = {_group: self.process_group,
             _any: self.process_token,
             _symbol: self.process_token}
        case = atom[0]
        return d[case](atom)
    
    def process_count(self, count):
        assert 1 <= len(count) <= 2
        if len(count) == 1:
            n, = count
            assert n > 0
        else:
            min, max = count
            assert min >= 0
            assert max == None or max >= min
        return self._process_count(count)
    
    def process_group(self, group):
        assert 2 <= len(group) <= 3
        container, (case, name, *regex) = type(group), group
        assert case == _group
        
        regex = list(self.process_regex(r) for r in regex)
        arg = container([case, name] + regex)
        return self._process_group(arg)
    
    def process_token(self, token):
        container, (case, *x) = type(token), token
        if case == _any:
            assert len(token) == 1
            arg = token
        elif case == _symbol:
            assert 2 <= len(token) <= 3
            if len(token) == 3:
                assert token[1] == _not
            syms = token[-1]
            syms = type(syms)(self.process_symbol(sym) for sym in syms)
            syms = self.process_symbols(syms)
            
            arg = container(list(token[:-1]) + [syms])
        else:
            self.throw()
        return self._process_token(arg)
    
    def process_symbol(self, symbol):
        return self._process_symbol(symbol)
    def process_symbols(self, symbols):
        return self._process_symbols(symbols)

    pass


class ReverseRegexArg(_RegexArgProcess):
    def _process_regex(self, regex):
        case, value = regex
        if case == _concat:
            value = type(value)(reversed(value))
            regex = type(regex)([case, value])
        elif case in _join:
            pass
        elif case == _not:
            pass
        else:
            raise never-reach-here
        
        return regex
    pass




containers = frozenset([list, tuple])
unorder_containers = frozenset([frozenset, set])
_container_map = {key : v for cs, v in [(containers, tuple), (unorder_containers, frozenset)]
                  for key in cs}
def _change_container(obj, iterable = None):
    if iterable == None:
        iterable = obj
    return _container_map[type(obj)](iterable)

def container_map(obj, iterable = None):
    assert type(obj) in containers
    return _change_container(obj, iterable)
def unorder_container_map(obj, iterable = None):
    assert type(obj) in unorder_containers
    return _change_container(obj, iterable)


class ToHashableRegexArg(_RegexArgProcess):
    def _process_regex(self, regex):
        case, value = regex
        if case == _concat:
            value = container_map(value)
        elif case in _join:
            value = unorder_container_map(value)
        elif case == _not:
            pass
        else:
            raise never-reach-here

        arg = container_map(regex, [case, value])
        return arg
    
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
                
        
    
        
def to_hashable_regex_arg(regex_arg):
    return ToHashableRegexArg().process_regex(regex_arg)

def reverse_regex_arg(regex_arg):
    return ReverseRegexArg().process_regex(regex_arg)



def test_reverse_regex_arg():
    to = ToHashableRegexArg()
    
    try_data = [
        [_not, [_and, {item for item in to.process_items(([[_any,], [1]], [[_symbol, {'a'}], [0,None]]))}]],
        [_concat, [[[_symbol, _not, set()], [0,None]], [[_group, 'name',], [0,None]], ]],
        [_concat, [[[_group, None, [_or, set()]], [1]], ]],
        [_concat, []],
        [_and, set()],
        [_or, set()],
        ]
    result_data = [
        [_not, [_and, {item for item in to.process_items(([[_any,], [1]], [[_symbol, {'a'}], [0,None]]))}]],
        [_concat, [[[_group, 'name',], [0,None]], [[_symbol, _not, set()], [0,None]], ]],
        [_concat, [[[_group, None, [_or, set()]], [1]], ]],
        [_concat, []],
        [_and, set()],
        [_or, set()],
        ]

    for regex, result in zip(try_data, result_data):
        assert result == reverse_regex_arg(regex)
        pass

    return

def test_to_hashable_regex_arg():
    to = ToHashableRegexArg()
    
    try_data = [
        [_not, [_and, {item for item in to.process_items(([[_any,], [1]], [[_symbol, {'a'}], [0,None]]))}]],
        [_concat, [[[_symbol, _not, set()], [0,None]], [[_group, 'name',], [0,None]], ]],
        [_concat, [[[_group, None, [_or, set()]], [1]], ]],
        [_concat, []],
        [_and, set()],
        [_or, set()],
        ]


    result_data = [
        ('not', ('and', frozenset({(('any',), (1,)), (('symbol', frozenset({'a'})), (0, None))}))),
        ('concat', ((('symbol', 'not', frozenset()), (0, None)), (('group', 'name'), (0, None)))),
        ('concat', ((('group', None, ('or', frozenset())), (1,)),)),
        (_concat, ()),
        (_and, frozenset()),
        (_or, frozenset()),
        ]

    for regex, result in zip(try_data, result_data):
        s = {to_hashable_regex_arg(regex)}
        assert result in s
        pass

    return



if is_main(__name__):
    test_to_hashable_regex_arg()
    test_reverse_regex_arg()
    pass




