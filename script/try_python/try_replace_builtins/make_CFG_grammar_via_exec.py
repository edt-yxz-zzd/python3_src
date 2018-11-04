
too complicate!!!


'''
make CF grammar via python exec
    avoid f'__{}__' since using __builtins__
    a |= __ | [*b] | +b *b -b | [] | -b +b -b | b
        # tuple
    a *= +b -b -b
        # list
    a @= __ | +b -b -b | b
        # unit
    a -= [b, b, b]
        # discard
'''
from abc import ABC, abstractmethod
from collections import UserDict
from collections.abc import Mapping
class GrammarDict(Mapping):
    def __init__(self):
        self.name2termss = {}
    def __getitem__(self, name):
        if name == '__':
            return RuleBody()
        return Term('', name)
    def __setitem__(self, name, rule_body_or_list_or_sum_or_term):
        if name == '__': raise KeyError
        if name.startswith(...)
        T = type(rule_body_or_list_or_sum_or_term)
        if T is RuleBody:
            body = rule_body_or_list_or_sum_or_term
        else:
            ls_or_sum_or_term = rule_body_or_list_or_sum_or_term
            body = RuleBody() | ls_or_sum_or_term
        self.name2termss(name2termss)


class RuleBodyBase(ABC):
    @abstractmethod
    def to_termss(self):
        raise NotImplementedError
class RuleBody(RuleBodyBase):
    # [Alternative]
    # [[Term]]
    def __init__(self, *, __termss=()):
        self.__termss = __termss
    def __or__(self, ls_or_sum_or_term):
        assert type(ls_or_sum_or_term) in (list, Sum, Term)
        T = type(ls_or_sum_or_term)
        if T is list:
            ls = ls_or_sum_or_term
            assert all(type(x) in (Sum, Term) for x in ls)
            termss = [x.to_terms() for x in ls]
        else:
            sum_or_term = ls_or_sum_or_term
            termss = sum_or_term.to_termss()
        return self.iextendright(termss)
    def iextendright(self, termss):
        for terms in termss:
            self = self.iappendright(terms)
        return self
    def iappendright(self, terms):
        return __class__(_RuleBody__termss=(__termss, terms))
    def to_termss(self):
        reversed_termss = []
        __termss = self.__termss
        while __termss:
            __termss, terms = __termss
            reversed_termss.append(terms)
        reversed_termss.reverse()
        termss = reversed_termss; del reversed_termss
        return termss


'''
class AlternativeBase(ABC):
    @abstractmethod
    def to_alternative(self):
        raise NotImplementedError
class Alternative:
    def __init__(self, terms):
        assert type(terms) is list
        assert all(type(term) is Term for term in terms)
        self.terms = terms
    def to_alternative(self):
        return self
'''
class SumBase(RuleBodyBase):
    def __add__(self, other):
        return Sum('+', self, other)
    def __sub__(self, other):
        return Sum('-', self, other)
    def __mul__(self, other):
        return Sum('*', self, other)
    @abstractmethod
    def iter_terms(self):
        raise NotImplementedError
    def to_terms(self):
        return list(self.iter_terms())
    def to_termss(self):
        return [self.to_terms()]
class Sum(SumBase):
    # Alternative
    # [Term]
    def __init__(self, op, lhs, rhs):
        assert type(lhs) in (Sum, Term)
        assert type(rhs) in (Sum, Term)
        assert type(op) is str
        assert op in ['+', '-', '*']
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
    def iter_terms(self):
        yield from self.lhs.iter_terms()
        it = self.rhs.iter_terms()
        for head in it:
            if head.op != '':
                raise SyntaxError('too many operators! {self.op!r} {head.op!r}')
            yield head.replace(op=self.op)
            break
        else:
            raise logic-error
        yield from it
        return

class Term(SumBase):
    def __init__(self, op, name):
        assert type(name) is str
        assert type(op) is str
        assert not name.startswith('__')
        assert not name.endswith('__')
        assert op in ['', '+', '-', '*']
        self.name = name
    def replace(self, *, op=None, name=None):
        if op is None: op = self.op
        if name is None: name = self.name
        return __class__(op, name)
    def iter_terms(self):
        yield self
    def __iter__(self):
        assert self.op == ''
        yield self.replace(op='*')
    def __pos__(self):
        assert self.op == ''
        return self.replace(op='+')
    def __neg__(self):
        assert self.op == ''
        return self.replace(op='-')


