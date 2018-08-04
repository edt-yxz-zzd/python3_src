


'''

pattern -> match -> process
for recursion data # assume tuple


pattern_definition:
-------------------
leaf_decl = '-declare' case_id *
# if case_id no pattern, it depends subcases or matchs all
pattern = case_id ':' items 
items = (item ',') *
item = _ | value | case_id | group
group = '(' items ')'

# if case_id with no swith, it's a leaf
switch = case_id '=' case_id ('|' case_id)*
-------------------



'''

pattern_definition_example = '''
-declare syms name items

symbol : 'symbol', syms
symbol_not : 'symbol', 'not', syms
any : 'any',
token = symbol | symbol_not | any


item : atom, count
count = repeat | minmax
repeat : _,
minmax : _, _

atom = group | refID

group : ('group', name, regex)
refID = regex
regex = concat | _and | _or | _not | null | token
concat : ('concat', items)
_and : ('and', items)
_or : ('or', items)
_not : ('not', regex)
null : ('null',)

'''

__doc__ += '\npattern_definition_example:\n{}\n{}\n{}\n'\
           .format('-'*20, pattern_definition_example, '-'*20)

from itertools import chain
from sand import match_case, do_assign, LeftHandConstValue, Counter

__all__ = ('Ignore', 'IGNORED', 'IGNORED_ID',
           'CaseID', 'IgnoredCaseID', 'split_lhID',
           'parse', 'gen_source')

class Ignore:
    def __repr__(self):
        return 'Ignore()'
    def __eq__(self, other):
        return True
    def __ne__(self, other):
        return False
IGNORED = _ignored = Ignore()
IGNORED_ID = _ignored_id = '_'


class CaseID(str):
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.__super_repr())
    def __str__(self):
        return str.__str__(self)
    def __super_repr(self):
        return str.__repr__(self)
    def super_repr(self):
        return self.__super_repr()
    


class IgnoredCaseID(Ignore, CaseID):
    def __repr__(self):
        return CaseID.__repr__(self)
#class DoProcessCaseID(Ignore, CaseID):pass

'''

'''


def strip_lines(lines):
    return [line.strip() for line in lines]

def remove_pure_commentlines(lines):
    r = []
    for line in lines:
        x = line.strip()
        if x and x[0] == '#':
            # pure comment; discard
            continue
        r.append(line)
    return r

def remove_emptylines(lines):
    return [line for line in lines if line]
defaultdict
def separate_list(f, ls):
    d = defaultdict(list)
    for x in ls:
        d[f(x)].append(x)
    return d

def separate_lines_startwith(lines, prefix):
    f = lambda line: str.startswith(line, prefix)
    return separate_list(f, lines)

def find_if_in(string, chars):
    #d = {ch: i for i, ch in enumerate(chars)}
    s = frozenset(chars)
    for i, ch in enumerate(string):
        if ch in s:
            return i
    return -1
def index_if_in(string, chars):
    i = find_if_in(string, chars)
    if i == -1:
        raise ValueError('no char found')
    return i

def find_first_in(string, chars):
    'char in chars with lowest index in string'
    i = index_if_in(string, chars)
    return string[i]

def index_chars_first_in_str(string, chars):
    'index of char in chars with lowest index in string'
    return chars.index(find_first_in(string, chars))

def separate_lines_by_sepchars(line, sepchars):
    f = lambda line: index_chars_first_in_str(line, chars)
    return separate_list(f, lines)


def to_blocks(string, sep = None, strip = None):
    return [s.strip(strip) for s in string.split(sep)]




def preparse_lines_op(lines):
    seps = ':='
    
    lines = strip_lines(lines)
    lines = remove_pure_commentlines(lines)
    lines = remove_emptylines(lines)
    
    d = separate_lines_startwith(lines, '-declare')
    id_declares = d[True]
    define_lines = d[False]
    
    d = separate_lines_by_sepchars(define_lines, seps)
    id_eq_subcases_ls = d[seps.index('=')]
    id_con_pattern_ls = d[seps.index(':')]
    
    return id_declares, id_eq_subcases_ls, id_con_pattern_ls


def parse_id_declares(id_declares):
    ##### -declare ...
    declared_ids = set(chain(to_blocks(decl)[1:] for decl in id_declares))
    return declared_ids

def parse_id_eq_subcases_ls(id_eq_subcases_ls):
    ##### id = subcase | ...
    id2subcases = {id.strip() : to_blocks(subcases, sep='|')
                   for id_eq_subcases in id_eq_subcases_ls
                   for id, subcases in [id_eq_subcases.split('=', 1)]}

    ids = set()
    for id, subcases in id2subcases.items():
        ids.add(id)
        ids.update(subcases)
    return ids, id2subcases

def parse_id_con_pattern_ls(id_con_pattern_ls):
    ##### id : pattern
    id2patternsrc = {id.strip() : pattern
                     for id_con_pattern in id_con_pattern_ls
                     for id, pattern in [id_con_pattern.split(':', 1)]}
    return id2patternsrc
    
def parse_step1(pattern_definition):
    lines = pattern_definition.splitlines()
    id_declares, id_eq_subcases_ls, id_con_pattern_ls = \
                 preparse_lines_op(lines)
    
    ##### -declare ...
    declared_ids = parse_id_declares(id_declares)

    ##### id = subcase | ...
    ids, id2subcases = parse_id_eq_subcases_ls(id_eq_subcases_ls)
    declared_ids.update(ids)

    ##### id : pattern
    id2patternsrc = parse_id_con_pattern_ls(id_con_pattern_ls)
    declared_ids.update(id2patternsrc.keys())

    return declared_ids, id2subcases, id2patternsrc


def parse_step2(declared_ids, id2subcases, id2patternsrc):

    ids = declared_ids
    
    if IGNORED_ID in declared_ids:
        raise ValueError('{!r} cannot be case_id'.format(IGNORED_ID))

    id2ignoredCaseID = {id: IgnoredCaseID(id) for id in ids}
    id2ignoredCaseID[IGNORED_ID] = IGNORED
    
    id2pattern_tuple = {id: eval(patternsrc, id2ignoredCaseID)
                        for id, patternsrc in id2patternsrc.items()}
    for v in id2pattern_tuple.values():
        if type(v) != tuple:
            raise ValueError('pattern should be tuple')

    counter = Counter()
    id2leftsideID = {id: pattern2leftsideID(pattern_tuple, counter)
                     for id, pattern_tuple in id2pattern_tuple.items()}
    
    return id2pattern_tuple, id2leftsideID

def parse(pattern_definition):
    r1 = parse_step1(pattern_definition)
    declared_ids, id2subcases, id2patternsrc = r1
    id2pattern_tuple, id2leftsideID = parse_step2(*r1)
    
    return declared_ids, id2subcases, id2patternsrc, \
           id2pattern_tuple, id2leftsideID


def split_lhID(lhid):
    r'.*_\d+'
    id, num = lhid.rsplit('_', 1)
    if not num.isdigit():
        raise ValueError('ID not in form r".*_\d+"')
    num = int(num)
    return id, num


def pattern2leftsideID(pattern, counter):
    t = type(pattern)
    count = int(counter)
    if t == tuple:
        r = tuple(pattern2leftsideID(x, counter) for x in pattern)
        
    elif issubclass(t, IgnoredCaseID):
        r = '{}_{}'.format(pattern, int(counter))
        counter += 1
        assert isinstance(counter, Counter)
        
    elif issubclass(t, Ignore):
        r = IGNORED_ID
        
    else: # const value
        r = LeftHandConstValue(pattern)
    return r





'''

def split_str_ls(lines, sep, maxsplit = -1):
    return [line.split(sep, maxsplit) for line in lines]
def to_id_items_pairls(nonempty_lines, seps):
    lss = [split_str_ls(nonempty_lines, sep, 1) for sep in seps]
    d = {sep:[] for sep in seps}
    for parts_ls in zip(*lss):
        firsts = [parts[0] for parts in parts_ls]
        lens = [len(first) for first in firsts]
        L = min(lens)
        i = lens.index(L)
        if lens.count(L) != 1 or len(parts_ls[i]) != 2:
            raise ValueError('bad format: {}'.format(seps[0].join(parts_ls[0])))
        d[seps[i]].append(parts_ls[i])

    for ls in d.values():
        for i in range(len(ls)):
            id, items = ls[i]
            id = id.strip()
            ls[i] = id, items

    return d
    





def to_words(string, sep = None, strip = None):
    return [s.strip(strip) for s in string.split(sep)]
def id_declares2ids(id_declares):
    ls = []
    for decl in id_declares:
        words = to_words(decl)
        assert words[0] == '-declare'
        ls.extend(words[1:])
    return ls



def itemsVal2leftsideID(itemsVal, counter):
    t = type(itemsVal)
    count = int(counter)
    if t == tuple:
        r = tuple(itemsVal2leftsideID(x, counter) for x in itemsVal)
##        if count == int(counter):
##            if not all(x == _ignored_id for x in r):
##                print(r)
##                raise logic-error
##            r = _ignored_id
##        else:
##            r = '({})'.format(' '.join(x+',' for x in r))
        
    elif issubclass(t, IgnoredCaseID):
        r = '{}_{}'.format(itemsVal, int(counter))
        counter += 1
        assert isinstance(counter, Counter)
        
    elif issubclass(t, Ignore):
        r = _ignored_id
    else: # const value
        # r = _ignored_id
        r = LeftHandConstValue(itemsVal)
    return r



def parse(s):
    seps = ':='
    nonempty_lines = [line for line in s.splitlines() if line if not line.isspace()]

    id_declares = [line for line in nonempty_lines if line.startswith('-declare')]
    ids = set(id_declares2ids(id_declares))

    
    define_lines = [line for line in nonempty_lines if not line.startswith('-declare')]
    d = to_id_items_pairls(define_lines, seps)


    # id = subcases
    ls = d['=']
    def to_subcase_ids(itemsStr, sep='|'):
        return [s.strip() for s in itemsStr.split(sep)]
    id2subcases = {id : to_subcase_ids(items) for id, items in ls}

    for id, subids in id2subcases.items():
        ids.add(id)
        ids.update(subids)
    

    
    # id : pattern
    ls = d[':']
    id2itemsStr = {id: items for id, items in ls}
    ids.update(id2itemsStr.keys())
    
    if _ignored_id in id2itemsStr:
        raise ValueError('"_" cannot be case_id')
    
    id2ignoredCaseID = {id: IgnoredCaseID(id) for id in ids}
    id2ignoredCaseID[_ignored_id] = _ignored
    
    id2itemsVal = {id: eval(items, id2ignoredCaseID) for id, items in ls}
    for v in id2itemsVal.values():
        if type(v) != tuple:
            raise ValueError('items should be tuple')

    counter = Counter()
    id2leftsideID = {id: itemsVal2leftsideID(itemsVal, counter)
                      for id, itemsVal in id2itemsVal.items()}


    
    return ids, id2subcases, id2itemsStr, id2itemsVal, id2leftsideID
    '''


def test_parse():
    r = parse(s)
    ids, id2subcases, id2itemsStr, id2itemsVal, id2leftsideID = r
    names = 'ids, id2subcases, id2itemsStr, id2itemsVal, id2leftsideID'.split(', ')
    assert len(names) == len(r)

    for name, v in zip(names, r):
        print(name, v)
        print('\n'*2)

#prefix = get_unused_id_prefix(ids)
#def to_is_match_case():pass



def gen_source(classname, pattern_definition):
    r = parse(pattern_definition)
    ids, id2subcases, id2itemsStr, id2itemsVal, id2leftsideID = r
    
    names = 'classname ids id2subcases id2itemsStr id2itemsVal id2leftsideID'
    g = locals()
    d = {name: g[name] for name in names.split()}

    head = '''
from Case import Ignore, IgnoredCaseID, split_lhID
from sand import match_case, do_assign, lh_star_star,\
     LeftHandConstValue, LHID_RHFilter

class {classname}:
    ids = {ids}
    id2subcases = {id2subcases}
    id2itemsStr = {id2itemsStr}
    id2itemsVal = {id2itemsVal}
    id2leftsideID = {id2leftsideID}
'''.format(**d)

    
    protected = '''
    def _preprocess_{case}(self, case, arg, attr):
        return attr
    def _postprocess_{case}(self, case, arg, attr, value):
        return value
'''
    all_protected = ''.join(protected.format(case=case) for case in ids)

    
    public = '''
    def preprocess_{case}(self, case, arg, attr):
        return self._preprocess_{case}(case, arg, attr)
    def postprocess_{case}(self, case, arg, attr, value):
        return self._postprocess_{case}(case, arg, attr)
'''
    all_public = ''.join(public.format(case=case) for case in ids)

    
    rest = '''
    def is_match(self, case, value):
        if case in self.id2itemsVal:
            pattern = self.id2itemsVal[case]
            return pattern == value
        elif case in self.id2subcases:
            return any(self.is_match(sub, value)
                       for sub in id2subcases[case])
        else:
            # leaf match every thing!
            return True


    def process(self, case, arg, attr = None):
        pre = getattr(self, 'preprocess_{case}'.format(case))
        post = getattr(self, 'postprocess_{case}'.format(case))
        attr = pre(case, arg, attr)
        if case in self.id2subcases:
            for sub in self.id2subcases:
                if self.is_match(sub, arg):
                    break
            else:
                raise ValueError('not matched subcase for {}'.format(case))
            value = self.process(case, arg, attr)
        elif case in self.id2itemsVal:
            pattern = self.id2itemsVal[case]
            if not pattern == arg:
                raise ValueError('not match {}'.format(case))
            value = self.assign_and_process(self.id2leftsideID[case], arg, attr)
        else:
            # leaf
            value = None
        return post(case, arg, attr, value)


    def assign_and_process(self, leftsideID, arg, attr):
        #OrderedDict?
        r = match_case([leftsideID], arg)
        if not r:
            raise logic-error
        _, _, id2value = r
        if _ignored_id in id2value:
            id2value.pop(_ignored_id)

        ls = [None] * len(id2value)
        for lhid, value in id2value.items():
            ID, n = split_lhID(lhid)
            if n >= len(ls) or ls[n] is not None:
                raise logic-error
            ls[n] = (ID, value)

        if any(x is None for x in ls):
            raise logic-error

        vs = []
        for case, arg in ls:
            r = self.process(case, arg, attr)
            vs.append(r)
        return vs

    pass
'''

    src = head + all_protected + all_public + rest
    return src


