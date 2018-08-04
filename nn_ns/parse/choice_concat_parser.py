

r'''
single line comment : # ...
allow emptylines
indent = 4 ascii spaces
no strings
no line joining rules; physical line is logical line
cannot access XX.XXX ; since '.' is part of name
no nongreedy; '? * +' ; no '?? *? +?'

name is '\S+'
keyword is '[=:]'
if name[-1] in '?+*', then ref = name[:-1],
    so, a valid id should not ends with these chars
nonemptyline should be : <indent>* <name> (<keyword> <name>*)? <spaces-comment>? <newline>


NOTE:
    one choice is the same as 'is'
    now, there is no 'is' command, using 'xxx : xxx' instead
'''
__all__ = '''
    ChoiceConcat_TokenizeError
    ChoiceConcat_IndentError
    
    tokenize
    parse_tokens
    parse
'''.split()


import re
from collections import namedtuple
from nn_ns.parse.simple_grammar_parser import \
     simple_grammar_parser, maybe_token_refs
from nn_ns.parse.unger_method import UngerParser, UngerParseFail, \
     parse_tree2info_tree


'''

'''
ChoiceConcat_in_SimpleGrammar = r'''
main = top_def*

top_def* = top_def top_def*
top_def* =

top_def = concat_def
top_def = choice_def



choice_def = choice_head choice_body
concat_def = concat_head concat_body


choice_head = name_def ':'
concat_head = name_def '='


choice_body = newline indent block dedent
choice_body = name_def_and_ref* newline
concat_body = ref_count* newline


name_def_and_ref* = name_def_and_ref name_def_and_ref*
name_def_and_ref* =
ref_count* = ref_count ref_count*
ref_count* =
block = def+

def+ = def def+
def+ = def

def = name_def_and_ref newline
def = top_def

ref_count = real_ref_count
ref_count = ref
name_def = ref
name_def_and_ref = name_def
'''


ChoiceConcat_in_ChoiceConcat = r'''

main = top_def*

top_def :
    concat_def = concat_head concat_body
    choice_def = choice_head choice_body


choice_head = name_def ':'
concat_head = name_def '='


choice_body = newline indent block dedent
choice_body = name_def_and_ref* newline
concat_body = ref_count* newline



block = def+

def :
    same_def = name_def_and_ref newline # as : name_def = <prev name_def>
    top_def

ref_count :
    real_ref_count
    ref
name_def : ref # as : name_def is ref
name_def_and_ref : name_def
'''

if 0:
    print(sorted(maybe_token_refs(
        *simple_gramma_parser(ChoiceConcat_in_SimpleGrammar))))


def _parser():
    nontoken_ref2rule_ids, rule_id2refs = \
                           simple_grammar_parser(ChoiceConcat_in_SimpleGrammar)
    token_refs = maybe_token_refs(nontoken_ref2rule_ids, rule_id2refs)
    main_ref = 'main'

    parser = UngerParser(main_ref, nontoken_ref2rule_ids, rule_id2refs, token_refs)

    return parser

parser = _parser()

r'''
["':'", "'='", 'dedent', 'indent',
    'newline', 'ref', 'real_ref_count']

ref = name_def = r'\S*(?![?*+])\S'
ref_count = r'\S+'

'''

r'''
compile

"""
    A = B C*
    D :
        E = B
        A
        D
"""
===>>>
"""#ntoken   rk     refs  rk_name  rk_type
      A   =>  1  =>  B C   # A        concat
      D   =>  2  =>  B     # D.E      concat
      D   =>  3  =>  A     # D.A      is
      D   =>  4  =>  D     # D.D      is
      C*  =>  5  =>  !C*   # --       times
      !C* =>  6  =>  C !C* # --       impl_times
      !C* =>  7  =>  ''    # --       impl_times
      # children names should be different
      # name_def should not end with '?*+'
      # rename !C* as C**
"""
'''

class ChoiceConcat_TokenizeError(ValueError):
    def __init__(self, *args, pos):
        self.pos = pos
        
class ChoiceConcat_IndentError(ChoiceConcat_TokenizeError):pass
class ChoiceConcat_NameError(ChoiceConcat_TokenizeError):pass
class ChoiceConcat_InvalidRefCountError(ChoiceConcat_NameError):pass


split_by_word = re.compile('(\S+)').split

def tokenize(grammar):
    'tokenize ChoiceConcatLanguage'
    def error(err, Error):
        err += ': lineno {} : {!r}'.format(lineno, line)
        return Error(err, pos=wbegin)
    def IndentError(err):
        return error(err, ChoiceConcat_IndentError)
    def InvalidRefCountError(err):
        return error(err, ChoiceConcat_InvalidRefCountError)
        
    #TokenizeError = ChoiceConcat_TokenizeError
    
    def Token(token_t):
        t = (token_t, wbegin, wend, lineno)
        tokens.append(t)
    def get_substr(token):
        _, wbegin, wend, _ = token
        return grammar[wbegin : wend]
        
    def tokenize_words(sSs):
        #print(sSs)
        nonlocal wbegin, wend

        wend -= L # move back indentspaces
        for i, s_or_S in enumerate(sSs):
            wbegin = wend
            wend += len(s_or_S)
            #print(repr(grammar[wbegin:wend]), repr(s_or_S))
            #assert grammar[wbegin:wend] == s_or_S
            if i % 2 == 0:
                # spaces
                continue


            word = s_or_S
            assert word and len(word.split()) == 1
            assert grammar[wbegin:wend] == word
            
            if word in [choice_t, concat_t]: # : or =
                token_t = "'{}'".format(word)
                Token(token_t)
                continue

            if word[-1] in '?+*':
                name = word[:-1]
                if not name or name[-1] in '?+*':
                    raise InvalidRefCountError(
                        'ref_count should end with "[^?*+][?*+]", not: {!r} '
                        .format(word))
                Token(real_ref_count_t)

            else:
                Token(ref_t)
            
                
    def remove_comment(line):
        i = line.find('#')
        if i >= 0:
            line = line[:i]
        return line
        

    indent_t = 'indent'
    dedent_t = 'dedent'
    choice_t = ':'
    concat_t = '='
    newline_t = 'newline'
    real_ref_count_t = 'real_ref_count'
    ref_t = 'ref'
    
    tokens = []
    prev_depth = 0
    lbegin = lend = 0
    org_line = ''


    for lineno, org_line in enumerate(grammar.splitlines(True)):
        line = org_line
        lbegin = lend
        lend += len(line)
        #print(repr(grammar[lbegin:lend]), repr(line))
        #assert grammar[lbegin:lend] == line
        wbegin = wend = lbegin
        
        line = remove_comment(line)
        if not line or line.isspace():
            continue

        sSs = split_by_word(line)
        assert len(sSs) % 2 == 1
        indentspaces = sSs[0]
        L = len(indentspaces)
        if indentspaces != ' '*L:
            raise IndentError('indentspaces are not all ascii spaces')
        if L % 4 != 0:
            raise IndentError('len(indentspaces) % 4 != 0')

        wend += L
        indent_depth = L // 4
        if prev_depth < indent_depth:
            if indent_depth > prev_depth+1:
                raise IndentError('indent too much')

            prev_depth += 1
            Token(indent_t)
        else:
            while indent_depth < prev_depth:
                prev_depth -= 1
                Token(dedent_t)
        assert prev_depth == indent_depth
        
        tokenize_words(sSs)
        Token(newline_t)
        newline_str = get_substr(tokens[-1])
        assert not newline_str or newline_str.isspace()
    else:
        while prev_depth:
            prev_depth -= 1
            Token(dedent_t)

    assert not prev_depth

    token_types = [t for t, *_ in tokens]
    assert token_types.count(indent_t) == token_types.count(dedent_t)
    return tokens



def parse_tokens(tokens, begin = 0, end = None, *, throw=True):
    'parse ChoiceConcatLanguage; tokens are returned by tokenize'
    token_types = [t[0] for t in tokens]
    return parser.parse(token_types, throw=throw)

def parse(grammar, *, throw=True, print_err=True):
    '''parse ChoiceConcatLanguage

return:
    if tokenize fail and throw=False
        grammar/pos :: int
    if parse_tokens fail and throw=False
        tokens :: [t], grammar/pos :: int
        t = (token_name, grammar/begin, grammar/end, lineno)
    if success
        tokens :: <see above>, parse_tree :: ParseTree ChoiceConcatToken_in_SimpleGrammar

    ParseTree r = () | (r, [ParseTree r])
        () - match one token, so counting the leafs in a subtree gives its range
        r  - rule_id which match the subtree
    since () contains no info of tokens, we need 'tokens'
    
    try parse_tree2info_tree(tokens, parse_tree) to get more infos.
    InfoTree r t = (t, Range) | (r, Range, [InfoTree r t])
        where t is the token type ==>> tokens :: [t]
              Range = (int, int) repr (tokens/begin, tokens/end)
              for leafs, we have : tokens/begin+1 == tokens/end

    since token does not contain grammar string, so, we need 'grammar'
    '''
    if throw:
        tokens = tokenize(grammar)
    else:
        try:
            tokens = tokenize(grammar)
        except ChoiceConcat_TokenizeError as e:
            return e.pos
    if not print_err:
        return parse_tokens(tokens, throw=throw)
    try:
        r = parse_tokens(tokens, throw=throw)
    except UngerParseFail as e:
        import sys
        eprint = lambda *args: print(*args, file=sys.stderr)
        eprint(e)
        pos = e.pos
        lineno = tokens[pos][-1]
        lbegin, lend = lineno-1, lineno+3
        lines = grammar.splitlines()
        eprint('line {} : show [{}:{}]:'.format(lineno, lbegin, lend))
        for line in lines[lbegin:lend]: eprint('\t', line)
        raise e
    
    if type(r) is int:
        # from token-pos to str-pos
        token_pos = r
        if token_pos < len(tokens):
            token_t, wbegin, wend, lineno = tokens[token_pos]
            r = wbegin
        else:
            r = len(grammar)
    return tokens, r


def _test():
    grammar = ChoiceConcat_in_ChoiceConcat
    tokens = tokenize(grammar)
    type_value_ls = [(t, grammar[x:y]) for t, x,y, _ in tokens]
    r = parse(grammar, throw=False)
    if type(r) is int:
        lineno = tokens[r][-1]
        print(grammar.splitlines()[lineno-1:lineno+3])
        print(type_value_ls[r-10:r])
        print(type_value_ls[r:r+10])
        parse(grammar) # fire
    
##r=parse(ChoiceConcat_in_ChoiceConcat, throw=0)
##print(r, ChoiceConcat_in_ChoiceConcat[r:])
parse(ChoiceConcat_in_ChoiceConcat)


example = r"""
A = B C*
D :
    E = B
    A
    D
"""

'''
sorted(rule_id2refs)
['block-0', 'choice_body-0', 'choice_body-1', 'choice_def-0', 'choice_head-0', 'concat_body-0', 'concat_def-0', 'concat_head-0', 'def+-0', 'def+-1', 'def-0', 'def-1', 'main-0', 'name_def-0', 'ref*-0', 'ref*-1', 'ref_count*-0', 'ref_count*-1', 'ref_count-0', 'ref_count-1', 'top_def*-0', 'top_def*-1', 'top_def-0', 'top_def-1']

'''

class CompileError(ValueError):pass

NS_Base = namedtuple('NS_Base', '''
    grammar
    parent_name
    rule_idx2type
    rule_idx2fullname
    rule_idx2ref_counts
    topname2rule_idcs
    fullnames
    partialnames
'''.split())
class Namespace(NS_Base):
    types = concat_t, is_t, times_t, times_impl_t \
            = 'concat_t', 'is_t', 'times_t', 'times_impl_t'
    def __new__(cls, *, grammar):
        self = super(__class__, cls).__new__(
            cls,
            grammar = grammar,
            parent_name = (),
            rule_idx2type = [],
            rule_idx2fullname = [],
            rule_idx2ref_counts = [],
            topname2rule_idcs = {},
            fullnames = set(),
            partialnames = set()
            )
        return self
    def replace(self, **kwargs):
        return self._replace(**kwargs)
    def set_fullname(ns, typ, fullname, ref_counts):
        # xx : yy ==>> xx : yy = yy
        #    ==>> ref_counts = ['yy']; fullname = ('xx', 'yy')
        if typ not in ns.types:
            raise logic-error
        rule_idx = len(ns.fullnames)
        ns.fullnames.add(fullname)
        if rule_idx == len(ns.fullnames):
            raise CompileError('duplicate fullname: {!r}'.format(fullname))
        ns.rule_idx2type.append(typ)
        topname = fullname[0]
        ns.topname2rule_idcs.setdefault(topname, [])
        ns.topname2rule_idcs[topname].append(rule_idx)
        ns.rule_idx2fullname.append(fullname)
        ns.rule_idx2ref_counts.append(ref_counts)
            


def compile(grammar, main_ref):
    # grammar = XL_in_ChoiceConcat
    # parse grammar and compile to a parser which parse XL
    #
    
    tokens, tree = parse(grammar)
    #tokens = [(typ, begin, end, grammar[begin:end]) for typ, begin, end, _ in tokens]
    #print(tokens)
    info_tree = parse_tree2info_tree(tokens, tree)
    ns = Namespace(grammar=grammar)
    _compile(ns, info_tree)
    #return ns
    _compile2(ns)

    nontoken_ref2rule_ids, rule_id2refs, token_refs = \
                           _ns_to_ntoken2rks_rk2refs_token_refs(ns)
    #print(token_refs, main_ref)
    parser = UngerParser(main_ref, nontoken_ref2rule_ids, rule_id2refs, token_refs)
    return parser

def _ns_to_ntoken2rks_rk2refs_token_refs(ns):
    nontoken_ref2rule_ids = ns.topname2rule_idcs
    rule_id2refs = ns.rule_idx2ref_counts

    def ls2dict(ls):
        return dict(enumerate(ls))
    nontoken_ref2rule_ids = nontoken_ref2rule_ids
    rule_id2refs = ls2dict(rule_id2refs)
    token_refs = maybe_token_refs(nontoken_ref2rule_ids, rule_id2refs)
    return nontoken_ref2rule_ids, rule_id2refs, token_refs
    
def _compile2(ns):
    # implement ?*+

    
    # find out real_ref_counts
    # since they arenot ntokens ==>> in maybe_tokens
    _, _, token_refs = _ns_to_ntoken2rks_rk2refs_token_refs(ns)
    real_ref_counts = set(ref for ref in token_refs if ref[-1] in '?*+')
    token_refs -= real_ref_counts


    # insert new rules to implement ?*+
    org_name_idx = 0
    impl_name_idx = org_name_idx + 1
    
    case2idcs_ls = {
        '?': [[org_name_idx], []],
        # xxx? = xxx?**
        # xxx?** = xxx
        # xxx?** =
        '*': [[org_name_idx, impl_name_idx], []],
        # xxx* = xxx***        ==>> id(xxx*):['xxx***']
        # xxx*** = xxx xxx***  ==>> id(xxx***):['xxx', 'xxx***']
        # xxx*** =             ==>> id(xxx***):[]
        '+': [[org_name_idx, impl_name_idx], [org_name_idx]]
        # xxx+ = xxx+**        ==>> id(xxx+):['xxx+**']
        # xxx+** = xxx xxx+**  ==>> id(xxx+**):['xxx', 'xxx+**']
        # xxx+** = xxx         ==>> id(xxx+**):['xxx']
        }

    for real_ref_count in real_ref_counts:
        case = real_ref_count[-1]
        org_name = real_ref_count[:-1]
        impl_name = real_ref_count + '**'
        names = [org_name, impl_name]

        # org_name is xxx
        # real_ref_count is xxx+
        # impl_name is xxx+**
        # xxx+ = xxx+** ==>> real_ref_count = impl_name
        fullname = (real_ref_count,)
        ns.set_fullname(ns.times_t, fullname, [impl_name])

        

        # xxx+** :
        #   0 = xxx xxx+**
        #   1 = xxx
        parent_name = (impl_name,)
        i = -1
        for i, idcs in enumerate(case2idcs_ls[case]):
            fullname = parent_name + (str(i),)
            refs = [names[idx] for idx in idcs]
            ns.set_fullname(ns.times_impl_t, fullname, refs)
            
        
        
    

    

def _compile(ns, info_tree):
    # ns.parent_name = tuple of name # full name
    # ns.grammar = grammar
    # ns.rule_idx2type : type in [concat_t, is_t] #, join_t, join_impl_t]
    # ns.topname2rule_idcs  rule_idx2fullname  rule_idx2ref_counts
    # in concept: ns.rule_idx : begin at 0; increase when concat_t or is_t
    # ns.fullnames, ns.partialnames : to avoid duplicate
    # ns is imutable namespace, using replace to yield a new object
    this_f = _compile
    types = concat_t, is_t = 'concat_t', 'is_t'
    def set_fullname(ns, typ, fullname, ref_counts):
        ns.set_fullname(typ, fullname, ref_counts)
        return
    
        # xx : yy ==>> xx : yy = yy
        #    ==>> ref_counts = ['yy']; fullname = ('xx', 'yy')
        if typ not in types:
            raise logic-error
        rule_idx = len(ns.fullnames)
        ns.fullnames.add(fullname)
        if rule_idx == len(ns.fullnames):
            raise CompileError('duplicate fullname: {!r}'.format(fullname))
        ns.rule_idx2type.append(typ)
        topname = fullname[0]
        ns.topname2rule_idcs.setdefault(topname, [])
        ns.topname2rule_idcs[topname].append(rule_idx)
        ns.rule_idx2fullname.append(fullname)
        ns.rule_idx2ref_counts.append(ref_counts)

    def add_partialname(ns, name):
        this_name = ns.parent_name+(name,)
        if this_name in ns.partialnames:
            raise CompileError('duplicate partialname: {!r}'.format(this_name))
        ns.partialnames.add(this_name)
        return this_name
    
    def is_leaf(node):
        return len(node) == 2
    def slice_rng(rng):
        begin, end = rng
        return ns.grammar[begin: end]
    def is_name(name):
        return name and name[-1] not in '?*+'
    def is_ref_count(ref_count):
        return is_name(ref_count) or is_name(ref_count[:-1])
    if is_leaf(info_tree):
        token, token_rng = info_tree
        token_begin, token_end = token_rng
        assert token_begin + 1 == token_end
        typ, wbegin, wend, _ = token
        substr = slice_rng((wbegin, wend)) # for 'ref' and 'real_ref_count'
        #print(token, repr(substr))
        return substr
    else:
        rule_id, rng, children = info_tree
        parent_name = ns.parent_name
        if rule_id == 'concat_def-0':
            # concat_def = concat_head concat_body
            concat_head, concat_body = children
            name = this_f(ns, concat_head) ############!!!!!!!!!
            this_name = add_partialname(ns, name)
            

            ns_ = ns.replace(parent_name = this_name)
            ref_counts = this_f(ns_, concat_body) ############!!!!!!!!!
            set_fullname(ns, concat_t, this_name, ref_counts)
            return
        elif rule_id == 'choice_def-0':
            # choice_def = choice_head choice_body
            choice_head, choice_body = children
            name = this_f(ns, choice_head) ############!!!!!!!!!
            this_name = add_partialname(ns, name)
            ns = ns.replace(parent_name = this_name)
            this_f(ns, choice_body)
            return 
        elif rule_id == 'name_def_and_ref-0':
            # name_def_and_ref = name_def
            name_def, = children
            name = this_f(ns, name_def) ############!!!!!!!!!
            this_name = add_partialname(ns, name)

            ref_counts = [name]
            set_fullname(ns, is_t, this_name, ref_counts)
            return
        elif rule_id == 'concat_body-0':
            # concat_body = ref_count* newline
            ref_count_star, _ = children
            reversed_ref_counts = this_f(ns, ref_count_star) ############!!!!!!!!!
            reversed_ref_counts.reverse()
            ref_counts = reversed_ref_counts
            return ref_counts
        elif rule_id == 'ref_count*-0':
            # ref_count* = ref_count ref_count*
            ref_count1, ref_count_star = children
            ref_count = this_f(ns, ref_count1)
            reversed_ref_counts = this_f(ns, ref_count_star)
            reversed_ref_counts.append(ref_count)
            return reversed_ref_counts
        elif rule_id == 'ref_count*-1':
            # ref_count* = <>
            assert not children
            return []
        elif rule_id in ['concat_head-0', 'choice_head-0']:
            # concat_head = name_def '='
            # choice_head = name_def ':'
            name_def, _ = children
            #return this_f(ns, name_def)
            name = this_f(ns, name_def)
            #rint(name)
            return name
        elif rule_id[:-2] in {'name_def', 'ref_count'}:
            # this = xxx
            xxx, = children
            return this_f(ns, xxx)
        else:
            r = None
            for tree in children:
                r = this_f(ns, tree)
            return #r


def _t():
    from pprint import pprint
    grammar = example
    tokens, tree = parse(grammar)
    subs = [(typ, begin, end, grammar[begin:end]) for typ, begin, end, _ in tokens]
    #print(subs)
    info_tree = parse_tree2info_tree(subs, tree)
    #pprint(info_tree)
    ns = Namespace(grammar=grammar)
    r = compile(ns, info_tree)
    print(r)

def _t():
    example = r"""
A = B C*
D :
    E = B
    A
    D
    """
    parser = compile(example, 'D')
    parser.parse('B')
    parser.parse('BC')
    return parser.parse('BCC')
    print(parser)
#print(_t())




