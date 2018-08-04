
import re
import abc
from abc import abstractmethod, ABCMeta
from MatchResult import MatchResult

__all__ = ['MatchChoices', 'MatchEq', 'MatchMulti', 'MatchOptional',
           'MatchPattern', 'MatchPlus', 'MatchResult', 'MatchRex',
           'MatchSequence', 'MatchStar', 'MatchString']

def match_str(prefix, string, start, end):
    if not string.startswith(prefix, start, end):
        return None
    end = start + len(prefix)
    #print('match_str', repr(prefix), repr(string[start:end]))
    return MatchResult(string, start, end, type=match_str, data=prefix, children=None)

def match_rex(rex, string, start, end):
    m = re.search(rex, string[start : end])
    if (not m) or m.start() != 0:
        return None

    end = start + (m.end() - m.start())
    #print('rex: ', string[start: end])
    return MatchResult(string, start, end, type=match_rex, data=rex, children=None)

skip_follow_chars_by_rex = r'((?=[^\n])\s)*'

class MatchPattern(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def default_factory():
        raise NotImplementedError('default_factory @MatchPattern abstractmethod')
    @abstractmethod
    def _match(self):
        raise NotImplementedError('_match @MatchPattern abstractmethod')

    
    
    def __init__(self, *, name='', follow=skip_follow_chars_by_rex):
        self.name = name
        self.follow = follow
##        if follow is not skip_follow_chars_by_rex:
##            print(name, repr(follow))
        return
    def match(self, string, start, end):
##        print('name = ', self.name)
##        print('type = ', type(self))
##        print('string from ', string[start:start+30])
        r = self._match(string, start, end)

        if r != None:
            r.type = type(self)
            assert not r.name
            r.set_name(self.name)
            
            if (self.follow):
                m = re.search(self.follow, r.string[r.end : end])
##                if m:
##                    print(m.group())
##                print(repr(self.follow), repr(r.string[r.end : end]), r.end, end)
                if m and m.start() == 0:
                    assert not r.follow
                    r.append_follow(r.string[r.end : r.end+m.end()])
##            print('r.follow = {!r}'.format(r.follow))
##            print('r.substring = {!r}'.format(r.string[r.start:r.end]))
##            print('r.type = {!r}'.format(r.type))
##            print('r.data = {!r}'.format(r.data))
##        else:
##            print('r = ', r)
        return r
    def __call__(self, string, start, end):
        return self.match(string, start, end)
    def __repr__(self):
        return '<{type}(name={name})>'.format(type=type(self), name=self.name)

class MatchEq(MatchPattern):
    @staticmethod
    def default_factory():
        return MatchEq(None)
    
    def __init__(self, matchPattern, *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(name=name, follow=follow)
        self.matchPattern = matchPattern
        return
    def _match(self, string, start, end):
        return eq_match(self.matchPattern, string, start, end)
    
class MatchString(MatchPattern):
    @staticmethod
    def default_factory():
        return MatchString('')
    
    def __init__(self, string, *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(name=name, follow=follow)
        self.string = string
        return
    def _match(self, string, start, end):
        return match_str(self.string, string, start, end)

class MatchRex(MatchPattern):
    @staticmethod
    def default_factory():
        return MatchRex('')
    
    def __init__(self, rex, *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(name=name, follow=follow)
        self.rex = rex
        return
    def _match(self, string, start, end):
        return match_rex(self.rex, string, start, end)

class MatchMulti(MatchPattern):
    @staticmethod
    def default_factory():
        return MatchMulti(None, 0)
    
    def __init__(self, matchPattern, min, max=float('inf'), *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(name=name, follow=follow)
        
        assert 0 <= min < min+1 <= max
        assert isinstance(min, int)
        
        self.matchPattern = matchPattern
        self.min = min
        self.max = max
        return
    def _match(self, string, start, end):
        return repeat_match(self.matchPattern, \
                            string, start, end, self.min, self.max)
    
class MatchSequence(MatchPattern):
    @staticmethod
    def default_factory():
        return MatchSequence([])
    
    def __init__(self, matchPatternList, *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(name=name, follow=follow)
        self.matchPatternList = matchPatternList
        #self.match_fs = [p.match for p in matchPatternList]
        return
    def _match(self, string, start, end):
        return sequence_match(self.matchPatternList, string, start, end)
    
 
class MatchChoices(MatchPattern):
    @staticmethod
    def default_factory():
        return MatchChoices([])
    
    def __init__(self, matchPatternList, *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(name=name, follow=follow)
        self.matchPatternList = matchPatternList
        #self.match_fs = [p.match for p in matchPatternList]
        return
    def _match(self, string, start, end):
        return choose_match(self.matchPatternList, string, start, end)
    
class MatchOptional(MatchMulti):
    @staticmethod
    def default_factory():
        return MatchOptional([])
    
    def __init__(self, matchPattern, *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(matchPattern, min=0, max=1, name=name, follow=follow)
        return
    
class MatchStar(MatchMulti):
    @staticmethod
    def default_factory():
        return MatchStar([])
    
    def __init__(self, matchPattern, *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(matchPattern, min=0, name=name, follow=follow)
        return
    
class MatchPlus(MatchMulti):
    @staticmethod
    def default_factory():
        return MatchPlus([])
    
    def __init__(self, matchPattern, *, name='', follow=skip_follow_chars_by_rex):
        super().__init__(matchPattern, min=1, name=name, follow=follow)
        return

def match(match_f, string, start, end):
    if not isinstance(match_f, MatchPattern):
        print(type(match_f), match_f)
    assert isinstance(match_f, MatchPattern)
    return match_f(string, start, end)

def eq_match(match_f, string, start, end):
    r = match(match_f, string, start, end)
    if r == None:
        return None

    rr = MatchResult(string, r.start, r.org_end, type=eq_match, data=None, children=[r])
    rr.append_follow(r.follow)
    return rr
    
def repeat_match(match_f, string, start, end, min, max=float('inf')):
    assert min < max
    
    old_start = start
    ls = []
    for _ in range(min):
        r = match(match_f, string, start, end)
        if r == None:
            return None
        start = r.end
        ls.append(r)

    while len(ls) <= max:
        r = match(match_f, string, start, end)
        if r == None:
            break
        if max == float('inf') and r.start == r.end:
            print(match_f.name)
            print(type(match_f))
            print(string[start:end])
            print(match_f.max)
            raise MemoryError('match empty string infinit times')
        
        start = r.end
        ls.append(r)
        
    return MatchResult(string, old_start, start, type=repeat_match, data=None, children=ls)

def sequence_match(match_fs, string, start, end):
    assert len(match_fs)

    old_start = start
    ls = []
    for match_f in match_fs:
        r = match(match_f, string, start, end)
        if r == None:
            return None
        start = r.end
        ls.append(r)
        
    
    return MatchResult(string, old_start, start, type=sequence_match, data=None, children=ls)

def choose_match(match_fs, string, start, end):
    assert len(match_fs)
    
    ls = []
    for i, match_f in enumerate(match_fs):
        r = match(match_f, string, start, end)
        if r == None:
            continue
        ls.append((i,r))
        
    if not ls:
        return None
    elif len(ls) > 1:
        print('Warning: choose lengthest one from matchs')
        for i, r in ls:
            f = match_fs[i]
            print('\t', f.name)
              
    ir = max(ls, key=lambda ir:ir[-1].length())
    i, r = ir
    
    cs = [None]*len(match_fs)
    cs[i] = r
    return MatchResult(r.string, r.start, r.end, type=choose_match, data=i, children=cs)








#print(sorted(globals().keys()))





