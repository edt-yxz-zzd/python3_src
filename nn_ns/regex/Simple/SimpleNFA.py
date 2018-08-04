
__all__ = '''
    DeadNFA
    NullNFA
    SinglePassNFA
    SingleNotNFA
    SingleNFA
    ConcatenationNFA
    AlternationNFA
    OneOrMoreNFA

    '''.split()

from .abc import ABC, abstractmethod, not_implemented, override
from .ISimpleNFA import ISimpleNFA
from .mkSimpleNFA import mkSimpleNFA_ex

the_empty_set = frozenset()
class DeadNFA(ISimpleNFA):
    __slots__ = ()

    @override
    def show(self, show_terminal_set, more=None):
        s = 'DeadNFA'
        if more is not None:
            return more(self, s)
        return s

    @override
    def _feed_astate2nstate_(self, astate, terminal):
        return the_empty_set
    @override
    def _null_transition_of_astate_(self, astate):
        return the_empty_set
    @override
    def is_a_local_dead_astate(self, astate):
        return True
    pass
class NullNFA(ISimpleNFA):
    __slots__ = ()

    @override
    def show(self, show_terminal_set, more=None):
        s = 'NullNFA'
        if more is not None:
            return more(self, s)
        return s
    @override
    def _feed_astate2nstate_(self, astate, terminal):
        return the_empty_set
    @override
    def _null_transition_of_astate_(self, astate):
        if astate == self.initial_astate:
            return frozenset([self.final_astate])
        return the_empty_set
    @override
    def is_a_local_dead_astate(self, astate):
        return True
    pass
class SinglePassNFA(ISimpleNFA):
    __slots__ = ()

    @override
    def show(self, show_terminal_set, more=None):
        s = 'SinglePassNFA'
        if more is not None:
            return more(self, s)
        return s
    @override
    def _feed_astate2nstate_(self, astate, terminal):
        if astate == self.initial_astate:
            return frozenset([self.final_astate])
        return the_empty_set
    @override
    def _null_transition_of_astate_(self, astate):
        return the_empty_set
    @override
    def is_a_local_dead_astate(self, astate):
        return astate != self.initial_astate
    pass
class SingleNotNFA(ISimpleNFA):
    __slots__ = 'terminal_set'.split()

    def __init__(self, make_new_astate, initial_astate, final_astate
                , terminal_set):
        self.terminal_set = terminal_set
        super().__init__(make_new_astate, initial_astate, final_astate)

    @override
    def show(self, show_terminal_set, more=None):
        s = 'SingleNotNFA({})'.format(show_terminal_set(self.terminal_set))
        if more is not None:
            return more(self, s)
        return s
    @override
    def _feed_astate2nstate_(self, astate, terminal):
        if astate == self.initial_astate and terminal not in self.terminal_set:
            return frozenset([self.final_astate])
        return the_empty_set
    @override
    def _null_transition_of_astate_(self, astate):
        return the_empty_set
    @override
    def is_a_local_dead_astate(self, astate):
        return astate != self.initial_astate
    pass

class SingleNFA(ISimpleNFA):
    __slots__ = 'terminal_set'.split()

    def __init__(self, make_new_astate, initial_astate, final_astate
                , terminal_set):
        self.terminal_set = terminal_set
        super().__init__(make_new_astate, initial_astate, final_astate)

    @override
    def show(self, show_terminal_set, more=None):
        s = 'SingleNFA({})'.format(show_terminal_set(self.terminal_set))
        if more is not None:
            return more(self, s)
        return s
    @override
    def _feed_astate2nstate_(self, astate, terminal):
        if astate == self.initial_astate and terminal in self.terminal_set:
            return frozenset([self.final_astate])
        return the_empty_set
    @override
    def _null_transition_of_astate_(self, astate):
        return the_empty_set
    @override
    def is_a_local_dead_astate(self, astate):
        return astate != self.initial_astate
    pass
class ConcatenationNFA(ISimpleNFA):
    __slots__ = 'lNFA rNFA _sep_psudo_astate'.split()

    def __init__(self, NFAs, make_new_astate, final_astate
                , lNFA, regexR):
        L = lNFA
        middle_astate = L.final_astate
        _sep_psudo_astate = make_new_astate.new_astate
        R = mkSimpleNFA_ex(NFAs, regexR, make_new_astate, middle_astate, final_astate)

        self.lNFA = L
        self._sep_psudo_astate = _sep_psudo_astate
        self.rNFA = R
        super().__init__(make_new_astate, L.initial_astate, R.final_astate)

    @override
    def show(self, show_terminal_set, more=None):
        s = '[{} ++ {}]'.format(self.lNFA.show(show_terminal_set, more)
                                , self.rNFA.show(show_terminal_set, more))
        if more is not None:
            return more(self, s)
        return s
    def _whose_astate(self, astate):
        sep = self._sep_psudo_astate
        # middle_astate final_astate must belong to R!!!!
        # initial_astate final_astate must belong to L!!!!
        if astate == self.initial_astate:
            nfa = self.lNFA
        elif astate >= sep or astate in [self.final_astate, self.rNFA.initial_astate]:
            nfa = self.rNFA
        else:
            nfa = self.lNFA
        return nfa
    @override
    def _feed_astate2nstate_(self, astate, terminal):
        nfa = self._whose_astate(astate)
        return nfa._feed_astate2nstate_(astate, terminal)
    @override
    def _null_transition_of_astate_(self, astate):
        nfa = self._whose_astate(astate)
        return nfa._null_transition_of_astate_(astate)
    @override
    def is_a_local_dead_astate(self, astate):
        nfa = self._whose_astate(astate)
        return nfa.is_a_local_dead_astate(astate)
    pass
class AlternationNFA(ISimpleNFA):
    __slots__ = 'uNFA dNFA _sep_psudo_astate'.split()
    def __init__(self, NFAs, make_new_astate
                , uNFA, regexD):
        U = uNFA
        initial_astate = U.initial_astate
        final_astate = U.final_astate
        _sep_psudo_astate = make_new_astate.new_astate
        D = mkSimpleNFA_ex(NFAs, regexD, make_new_astate, initial_astate, final_astate)

        self.uNFA = U
        self._sep_psudo_astate = _sep_psudo_astate
        self.dNFA = D
        super().__init__(make_new_astate, initial_astate, final_astate)

    @override
    def show(self, show_terminal_set, more=None):
        s = '<{} | {}>'.format(self.uNFA.show(show_terminal_set, more)
                                , self.dNFA.show(show_terminal_set, more))
        if more is not None:
            return more(self, s)
        return s
    def _whose_astate(self, astate):
        sep = self._sep_psudo_astate
        # initial_astate belong to both
        # final_astate belong to U or D, donot care
        if astate >= sep:
            nfa = self.dNFA
        else:
            nfa = self.uNFA
        return nfa
    @override
    def _feed_astate2nstate_(self, astate, terminal):
        if astate == self.initial_astate:
            # both
            return (self.uNFA._feed_astate2nstate_(astate, terminal)
                | self.dNFA._feed_astate2nstate_(astate, terminal)
                )
        nfa = self._whose_astate(astate)
        return nfa._feed_astate2nstate_(astate, terminal)
    @override
    def _null_transition_of_astate_(self, astate):
        if astate == self.initial_astate:
            # both
            return (self.uNFA._null_transition_of_astate_(astate)
                | self.dNFA._null_transition_of_astate_(astate)
                )
        nfa = self._whose_astate(astate)
        return nfa._null_transition_of_astate_(astate)
    @override
    def is_a_local_dead_astate(self, astate):
        if astate == self.initial_astate:
            # both
            return (self.uNFA.is_a_local_dead_astate(astate)
                and self.dNFA.is_a_local_dead_astate(astate)
                )
        nfa = self._whose_astate(astate)
        return nfa.is_a_local_dead_astate(astate)
    pass
class OneOrMoreNFA(ISimpleNFA):
    __slots__ = 'refNFA'.split()

    def __init__(self, NFAs, make_new_astate, initial_astate, final_astate
                , regex):
        r = mkSimpleNFA_ex(NFAs, regex, make_new_astate, None, None)
            # must new, to avoid recur
        self.refNFA = r
        super().__init__(make_new_astate, initial_astate, final_astate)

    @override
    def show(self, show_terminal_set, more=None):
        s = '{}+'.format(self.refNFA.show(show_terminal_set, more))
        if more is not None:
            return more(self, s)
        return s

    @override
    def _feed_astate2nstate_(self, astate, terminal):
        if astate in [self.initial_astate, self.final_astate]:
            return the_empty_set
        nfa = self.refNFA
        return nfa._feed_astate2nstate_(astate, terminal)
    @override
    def _null_transition_of_astate_(self, astate):
        if astate == self.initial_astate:
            return frozenset([self.refNFA.initial_astate])
        elif astate == self.refNFA.final_astate:
            return frozenset([self.refNFA.initial_astate, self.final_astate])
        elif astate == self.final_astate:
            return the_empty_set
        nfa = self.refNFA
        return nfa._null_transition_of_astate_(astate)
    @override
    def is_a_local_dead_astate(self, astate):
        if astate in [self.initial_astate, self.final_astate]:
            return True
        nfa = self.refNFA
        return nfa.is_a_local_dead_astate(astate)
    pass





