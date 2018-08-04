
'''
pp is ppattern (abbr: plain_pattern)
    bytes or str
    not include flags_str


'''

__all__ = '''
    rex_pattern_split
    rex_flags_str2flags
    is_flags_str
    complie_ppattern
    
    backreference
    anchor_ppattern
    if_ppattern
    name_ppattern
    capture_ppattern
    group_ppattern
    
    are_choices
    iter_std_subconcat
    concat_ppatterns
    error_ppattern
    choice_ppatterns
    
    ppattern2iter_choice_rngs
    ppattern2iter_concat_rngs
    isplit_ppattern_as_choice
    isplit_ppattern_as_concat
    split_ppattern_as_choice
    split_ppattern_as_concat
'''.split()

from sand import fixed__package__
fixed__package__(globals())
from sand import top_level_import
assert top_level_import(__name__, 'import_main.forgot_import', args=('logic error',))
assert top_level_import(__name__, 'import_main.collect_globals',
        kwargs=dict(pred=None, include='', exclude='''
    main'''))

import re
from itertools import chain, islice

__flags_rex = re.compile(r'^\s*(\(\?[aiLmsux]+\))') # can match b''??

def is_flags_str(flags_str):
    m = __flags_rex.match(flags_str)
    if m:
        i = 1
        return m.start(i) == 0 and m.end(i) == len(flags_str)
    return False
    
def rex_pattern_split(pattern):
    '''split out flags ==>> (flags_str, plain_pattern);
but it is not the final flags

flags_str can be str or bytes
'''
    # flag_str = '(?aiLmsux)'

    m = __flags_rex.match(pattern)
    if m:
        i = 1
        flags_str = m.group(i)
        plain_pattern = pattern[m.end(i):]
        if m.start(i):
            plain_pattern = pattern[:m.start(i)] + plain_pattern
    else:
        flags_str = pattern[:0] # str or bytes
        plain_pattern = pattern
    return (flags_str, plain_pattern)

def rex_flags_str2flags(flags_str, flags=None):
    assert is_flags_str(flags_str)
    if flags is None:
        flags = 0
    return re.compile(flags_str, flags).flags
def complie_ppattern(flags_str, ppattern, flags=None):
    '''::= compile(flags_str+ppattern, flags)
::= compile(ppattern, rex_flags_str2flags(flags_str, flags))
'''
    return re.compile(ppattern, rex_flags_str2flags(flags_str, flags))
    if flags is None:
        flags = 0
    return re.compile(flags_str+ppattern, flags)

######################## join ############################

def group_ppattern(pp):
    'noncapture'
    return '(?:{})'.format(pp)
def capture_ppattern(pp):
    'anonymous capture'
    return '({})'.format(pp)
def name_ppattern(pp, name):
    'named capture'
    assert name.isidentifier()
    return '(?P<{}>{})'.format(name, pp)
def anchor_ppattern(pp, neg=False, ahead=True):
    if ahead:
        fmt = '(?!{})' if neg else '(?={})'
    else:
        fmt = '(?<!{})' if neg else '(?<={})'
    return fmt.format(pp)
def backreference(name_or_idx):
    if isinstance(name_or_idx, int):
        idx = name_or_idx
        return r'(?:\{})'.format(idx)
    name = name_or_idx
    assert name.isidentifier()
    return '(?P={})'.format(name)

def if_ppattern(name, yes_pp, no_pp):
    'if the named group exists, choose yes_pp otherwise no_pp'
    return '(?({})(?:{})|(?:{}))'.format(name, yes_pp, no_pp)

def iter_std_subconcat(pps):
    'prepare for concat pps'
    for pp in pps:
        if are_choices(pp):
            yield group_ppattern(pp)
        else:
            yield pp
    
def concat_ppatterns(pps):
    return ''.join(iter_std_subconcat(pps))

error_ppattern = r'(?:[^.\s](?!a)a(?#error_ppattern))'
re.compile(error_ppattern)
def choice_ppatterns(pps):
    pps = iter(pps)
    for first in pps:
        break
    else:
        # no choices
        return error_ppattern
    return '|'.join(chain([first], pps))
    
######################## split ###########################

def are_choices(pp):
    *ls, = islice(ppattern2iter_choice_rngs(pp), 2)
    return len(ls) > 1


def ppattern2iter_choice_rngs(ppattern, begin=None, end=None):
    r'split by "|"'
    return __iter_ppattern__choice(ppattern, begin, end).do()
def ppattern2iter_concat_rngs(ppattern, begin=None, end=None):
    r'''yield ranges of () or [] or others

for begin, end in ppattern2iter_choice_rngs(ppattern):
    subppattern = ppattern[begin:end]
    for rng in ppattern2iter_concat_rngs(subppattern):
        ...
'''
    return __iter_ppattern__concat(ppattern, begin, end).do()
def isplit_ppattern_as_choice(ppattern, begin=None, end=None):
    return __iter_ppattern__choice(ppattern, begin, end).isplit()
def isplit_ppattern_as_concat(ppattern, begin=None, end=None):
    return __iter_ppattern__concat(ppattern, begin, end).isplit()

def split_ppattern_as_choice(ppattern, begin=None, end=None):
    return __iter_ppattern__choice(ppattern, begin, end).split()
def split_ppattern_as_concat(ppattern, begin=None, end=None):
    return __iter_ppattern__concat(ppattern, begin, end).split()
    
class __iter_ppattern:
    def __init__(self, ppattern, begin=None, end=None):
        L = len(ppattern)
        begin, end, _ = slice(begin, end).indices(L)
        assert 0 <= begin <= L
        assert 0 <= end <= L
        if end < begin:
            end = begin
            
        self.begin = begin
        self.end = end
        self.ppattern = ppattern
    def __getch_from_str(self, i):
        return self.ppattern[i]
    def __getch_from_bytes(self, i):
        return chr(self.ppattern[i])
        
    def isplit(self):
        ppattern = self.ppattern
        for a, b in self.do():
            yield ppattern[a:b]
    def split(self):
        return list(self.isplit())
    def do(self):
        ppattern = self.ppattern
        L = self.end
        if type(ppattern) is str:
            def getch(i):
                return ppattern[i]
        else:
            def getch(i):
                chr(ppattern[i])

        def skip_escaped(i):
            assert i <= L
            while i < L:
                if getch(i) != '\\':
                    return i
                i += 2
                    
            if i != L:
                raise ValueError('rex ppattern ends with nonescaped \\')
            return i
        def skip_chars_not_in(i, excludes):
            'skip_escaped_and_char_not_in'
            while True:
                i = skip_escaped(i)
                if not i < L:
                    break
                if getch(i) in excludes:
                    return i
                i += 1
            assert i == L
            return i

        def skip_one_bracket(i):
            '[xxx]'
            if not i<L or getch(i) != '[':
                return i

            i += 1
            if i<L and getch(i) == ']': # "[]xxx]" == "[\]xxx]"
                i += 1
            i = skip_chars_not_in(i, ']')
            if i == L:
                raise ValueError('rex "[xxx" : no "]"')
            assert i < L and getch(i) == ']'
            return i+1


        def skip_comment(i):
            '(?#...)'
            if getch(i) != '(':
                return i
            if i+3 <= L and \
               getch(i+2) == '#' and \
               getch(i+1) == '?':
                # it seems a fail pattern: r"(?#\)"
                # so we can escaped ")" in comment
                i = skip_chars_not_in(i+3, ')') 
                if i < L:
                    if not getch(i) == ')':
                        raise logic-error
                else:
                    raise ValueError('rex comment not terminated: "(?#..."')
            return i
            
        def skip_one_group(i):
            '(xxx)'
            if not i<L or getch(i) != '(':
                return i

            depth = 0
            #i += 1
            while True:
                i_ = skip_chars_not_in(i, '()[')
                i = skip_one_bracket(i_)
                if i_ != i:
                    continue
                if not i < L:
                    break
                
                ch = getch(i)
                if ch == '(':
                    depth += 1
                    end = skip_comment(i)
                    if end != i:
                        i = end
                        continue
                elif ch == ')':
                    depth -= 1
                    if not depth:
                        return i+1
                else:
                    raise logic-error
                    
                i += 1
                
            raise ValueError('rex "(xxx" : no ")"')
        return self._do(getch, skip_chars_not_in,
                        skip_one_group, skip_one_bracket)
    def _do(self, getch, skip_chars_not_in,
            skip_one_group, skip_one_bracket):
        raise NotImplementedError

class __iter_ppattern__concat(__iter_ppattern):
    def _do(self, getch, skip_chars_not_in,
            skip_one_group, skip_one_bracket):
        L = self.end
        i = self.begin
        while True:
            end = skip_chars_not_in(i, '([|')
            if i != end:
                yield (i, end)
                i = end

            if not i < L:
                break
            ch = getch(i)
            if ch == '(':
                end = skip_one_group(i)
            elif ch == '[':
                end = skip_one_bracket(i)
            elif ch == '|':
                raise ValueError('rex : not a concat regex; contains toplevel "|"')
                
            yield (i, end)
            i = end
                
        assert i == L
        return

class __iter_ppattern__choice(__iter_ppattern):
    def _do(self, getch, skip_chars_not_in,
            skip_one_group, skip_one_bracket):
        L = self.end
        begin = i = self.begin
        while True:
            i = skip_chars_not_in(i, '([|')
            if not i < L:
                break
            ch = getch(i)
            if ch == '(':
                i = skip_one_group(i)
            elif ch == '[':
                i = skip_one_bracket(i)
            elif ch == '|':
                yield begin, i
                i += 1
                begin = i
                
        assert i == L
        yield begin, i
        return
                
def _test_split_ppattern_as_concat():
    f = split_ppattern_as_concat
    pp = r'(())[]\]]\(\[()'
    assert f(pp) == r'(()) []\]] \(\[ ()'.split()

    pp = r'(?#(([[[\)' # fail to compile???
    pp = r'(?#(([[[)'
    re.compile(pp)
    assert f(pp) == [pp]
_test_split_ppattern_as_concat()
def _test_split_ppattern_as_choice():
    f = split_ppattern_as_choice
    pp = r'(())[]\]]\(\[()'
    assert f(pp) == [pp]

    pp = r'|(|)[|]||\||'
    assert f(pp) == r',(|)[|],,\|,'.split(',')
_test_split_ppattern_as_choice()



















