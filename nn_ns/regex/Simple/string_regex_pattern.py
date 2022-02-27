

r'''
simple string regex pattern spec:
    * \< \>
        escaped char_name/char_class_name
        \<0\> ==>> "\0"
        \<x22\> ==>> "\x22"
        \<n\> ==>> "\n"
    * \( \)
        "\(\)" ==>> NullRE
    * \[\^ \- \]
        \[ ... \<char_class_name\> ... \]

        "\[\]" ==>> DeadRE
        "\[\^\]" ==>> SinglePassRE
        "\[ ... \]" ==>> SingleRE
        "\[\^ ... \]" ==>> SingleNotRE
    * \.
        "\." ==>> SinglePassRE
    * \|
        AlternationRE

    * \{ \} \* \+ \?
        CountedRepetitionRE
        MoreRepetitionRE


stream convertor:
    ^ ==>> ns.mkAlter(ns.mkConcat(ns.Beginning
    $ ==>> , end='mkConcat'), end='mkAlter')
    \( ==>> , ns.mkAlter(ns.mkConcat(ns.Beginning
    \) ==>> , end='mkConcat'), end='mkAlter')
    \| ==>> , end='mkConcat'), ns.mkConcat(ns.Beginning
    \? \+ \* ==>> [0:1]  [1:] [0:]
    \{ ==>> [ns.mkMulti(ns.Beginning
    \} ==>> , end='mkMulti')]
    \[ ==>> , ns.mkCharClass(ns.Beginning
    \] ==>> , end='mkCharClass')
    \^ ==>> , ns.InvCharClass
    \- ==>> , ns.CharRangeJointer
    \< ==>> , ns.mkEscapedCharClass(ns.Beginning
    \> ==>> , end='mkEscapedCharClass')
    \. ==>> , ns.mkSinglePass()
    \\ ==>> , ns.mkSingleChar('\\')
    'x' ==>> , ns.mkSingleChar('x')
    \x for x in "abfnrtv" ==>> , ns.mkSingleChar('\x')

    # put back to input and retokenize
        \d ==>> \<digit\>
        \s ==>> \<space\>
        \l ==>> \<lower\>
        \u ==>> \<upper\>
        \w ==>> \<word\>
        \h ==>> \<blank\>


ns is a namespace:
    .Beginning
    .InvCharClass
    .CharRangeJointer
    .mkAlter(*regexes:'expect [ConcatRE]', end) -> 'AlterRE'
    .mkConcat(Beginning, *regexes, end) -> 'ConcatRE'
    .mkMulti(Beginning, *regexes:'expect [SingleRE]', end) -> 'slice|UInt'
    .mkCharClass(Beginning, InvCharClass?, *regexes:'expect [SingleRE|SinglePassRE|CharRangeJointer]', end) -> 'SingleRE|DeadRE|SinglePassRE'
    .mkEscapedCharClass(Beginning, *regexes:'expect [SingleRE]', end) -> 'SingleRE|DeadRE|SinglePassRE'
    .mkSinglePass() -> 'SingleRE'|'SinglePassRE'
    .mkSingleChar(char) -> 'SingleRE'


http://www.regular-expressions.info/posixbrackets.html

POSIX       Shorthand   ASCII
[:alnum:]               [a-zA-Z0-9]
[:alpha:]               [a-zA-Z]
[:ascii:]               [\x00-\x7F]
[:blank:]   \h          [ \t]
[:cntrl:]               [\x00-\x1F\x7F]
[:digit:]   \d          [0-9]
[:graph:]               [\x21-\x7E]
[:lower:]   \l          [a-z]
[:print:]               [\x20-\x7E]
[:punct:]               [!"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]
[:space:]   \s          [ \t\r\n\v\f]
[:upper:]   \u          [A-Z]
[:word:]    \w          [A-Za-z0-9_]
[:xdigit:]              [A-Fa-f0-9]
'''










__all__ =  '''
    parse_string_regex_pattern
    '''.split()


from .ISimpleRE import ISimpleRE
from .SimpleRE import \
    (DeadRE
    ,NullRE
    ,SinglePassRE
    ,SingleNotRE
    ,SingleRE
    ,ConcatenationRE
    ,AlternationRE
    ,CountedRepetitionRE
    ,MoreRepetitionRE
    ,theSinglePassRE
    ,theDeadRE
    ,theNullRE
    )


from seed.abc import not_implemented, override, abstractmethod, ABC
from seed.helper.safe_eval import safe_eval
from seed.seq_tools.split_seq2seq1s import split_seq2seq1s__pred
#from seed.iters.PeekableIterator import PeekableIterator
from ..imports.BlockSet import \
    (IBlockSet
    ,BlockSet
    ,theChar_as_BlockDictKeyOps
    )


def CharBlockSet(iterable=None, *, is_block_keys=False):
    return BlockSet(theChar_as_BlockDictKeyOps, iterable
                    , is_block_keys=is_block_keys)




def is_char(ch):
    return type(ch) is str and len(ch) == 1
def iter_tokens_of_string_regex_pattern(pattern:'Iter Char'):
    # Iter Char -> Iterator token
    #   where token = Char | ("\\" + Char) ; 1 <= len(token) <= 2
    #
    #assert isinstance(pattern, str)

    it = iter(pattern)
    while True:
        c = next(it)
        assert is_char(c)

        if c != '\\':
            yield c
        else:
            try:
                c2 = next(it)
            except StopIteration:
                raise Exception(r'"\\" without char')
            assert is_char(c2)

            token = c + c2
            yield token
    return

'''
def peekable_iter_tokens_of_string_regex_pattern(pattern:str):
    # -> PeekableIterator token
    #   where token = Char | ("\\" + Char) ; 1 <= len(token) <= 2
    #
    return PeekableIterator(iter_tokens_of_string_regex_pattern(pattern))
'''

__retokenize_d = \
    {'d': r'\<digit\>'
    ,'s': r'\<space\>'
    ,'l': r'\<lower\>'
    ,'u': r'\<upper\>'
    ,'w': r'\<word\>'
    ,'h': r'\<blank\>'
    }

__stream_convertor_d =\
    {'(': ", ns.mkAlter(ns.mkConcat(ns.Beginning"
    ,')': ", end='mkConcat'), end='mkAlter')"
    ,'|': ", end='mkConcat'), ns.mkConcat(ns.Beginning"
    ,'?': "[0:1]"
    ,'+': "[1:]"
    ,'*': "[0:]"
    ,'{': "[ns.mkMulti(ns.Beginning"
    ,'}': ", end='mkMulti')]"
    ,'[': ", ns.mkCharClass(ns.Beginning"
    ,']': ", end='mkCharClass')"
    ,'^': ", ns.InvCharClass"
    ,'-': ", ns.CharRangeJointer"
    ,'<': ", ns.mkEscapedCharClass(ns.Beginning"
    ,'>': ", end='mkEscapedCharClass')"
    ,'.': ", ns.mkSinglePass()"
    ,'\\': r", ns.mkSingleChar('\\')"
    #\x for x in "abfnrtv" ==>> , ns.mkSingleChar('\x')
    ,'a': r", ns.mkSingleChar('\a')"
    ,'b': r", ns.mkSingleChar('\b')"
    ,'f': r", ns.mkSingleChar('\f')"
    ,'n': r", ns.mkSingleChar('\n')"
    ,'r': r", ns.mkSingleChar('\r')"
    ,'t': r", ns.mkSingleChar('\t')"
    ,'v': r", ns.mkSingleChar('\v')"
    }
def stream_convertor(tokens):
    # Iter token -> Iter str
    #
    # len(token) == 1 or 2
    #   if 2: token[0] == '\\'
    #

    # ^ ==>> ns.mkAlter(ns.mkConcat(ns.Beginning
    yield 'ns.mkAlter(ns.mkConcat(ns.Beginning'

    tokenss = [iter(tokens)]
    sd = __stream_convertor_d
    td = __retokenize_d
    tokenize = iter_tokens_of_string_regex_pattern
    while tokenss:
        tokens = tokenss[-1]
        for token in tokens:
            L = len(token)
            if L == 1:
                # 'x' ==>> , ns.mkSingleChar('x')
                char = token
                yield f", ns.mkSingleChar({char!r})"
                continue
            elif L != 2 or token[0] != '\\': raise TypeError

            case = token[1]
            s = sd.get(case)
            if s is not None:
                yield s
                continue
            t = td.get(case)
            if t is not None:
                tokens = iter(tokenize(t))
                tokenss.append(tokens)
                break

            raise Exception(f'unknown token: {token!r}')
        else:
            tokenss.pop()

    # $ ==>> , end='mkConcat'), end='mkAlter')
    yield ", end='mkConcat'), end='mkAlter')"


class INameSpace(ABC):
    # ns is a namespace
    __slots__ = ()

    @property
    @not_implemented
    def Beginning(self):
        ...
    @property
    @not_implemented
    def InvCharClass(self):
        ...
    @property
    @not_implemented
    def CharRangeJointer(self):
        ...

    @not_implemented
    def mkAlter(self, *regexes:'expect [ConcatRE]', end):
        # -> 'AlterRE'
        ...
    @not_implemented
    def mkConcat(self, Beginning, *regexes, end):
        # -> 'ConcatRE'
        ...
    @not_implemented
    def mkMulti(self, Beginning, *regexes:'expect [SingleRE]', end):
        # -> 'slice|UInt'
        ...
    @not_implemented
    def mkCharClass(self, Beginning, *regexes:'may leading with InvCharClass, expect [SingleRE|SinglePassRE|CharRangeJointer]', end):
        # -> 'SingleRE|DeadRE|SinglePassRE'
        ...
    @not_implemented
    def mkEscapedCharClass(self, Beginning, *regexes:'expect [SingleRE]', end):
        # -> 'SingleRE|DeadRE|SinglePassRE'
        ...
    @not_implemented
    def mkSinglePass(self):
        # -> 'SingleRE'|'SinglePassRE'
        ...
    @not_implemented
    def mkSingleChar(self, char):
        # -> 'SingleRE'
        ...


def SingleREs2str(regexes):
    # assume using BlockSet
    # and the set contains just one char
    return ''.join(map(SingleRE2char, regexes))
def SingleRE2char(regex):
    # assume using BlockSet
    # and the set contains just one char
    if not isinstance(regex, SingleRE): raise TypeError
    s = regex.terminal_set
    if not isinstance(s, IBlockSet): raise TypeError
    if s.block_dict_key_ops != theChar_as_BlockDictKeyOps: raise TypeError
    if s.get_num_block_keys() != 1: raise TypeError
    block_key = s.get_first_block_key()
    L, R = block_key
    if L != R: raise TypeError
    key_ex_case, ch = L
    return ch
def unionSingleREs(regexes:'SingleRE|DeadRE|SingleNotRE|SinglePassRE'):
    # -> ...
    terminal_set = CharBlockSet()
    for regex in regexes:
        if isinstance(regex, SingleRE):
            terminal_set |= regex.terminal_set
        elif isinstance(regex, SingleNotRE):
            terminal_set |= -regex.terminal_set
        elif isinstance(regex, DeadRE):
            pass
        elif isinstance(regex, SinglePassRE):
            whole_set = terminal_set.self_make_whole_block_set()
            terminal_set = whole_set
            break
            #return SingleRE(whole_set) # instead of theSinglePassRE
            return regex
        else:
            raise Exception('unexpected case: {!r}'.format(type(regex)))
    #if not terminal_set: return theDeadRE
    return SingleRE(terminal_set)


class ISimpleNameSpace(INameSpace):
    __slots__ = ()

    @not_implemented
    def _mkAlter_(self, *regexes:'expect [ConcatRE]'):
        # -> 'AlterRE'
        ...
    @not_implemented
    def _mkConcat_(self, *regexes):
        # -> 'ConcatRE'
        ...

    @not_implemented
    def _mkMulti_(self, *regexes:'expect [SingleRE]'):
        # -> 'slice|UInt'
        ...
    @not_implemented
    def _mkCharClass_(self, *regexes:'may leading with InvCharClass, expect [SingleRE|SinglePassRE|CharRangeJointer]'):
        # -> 'SingleRE|DeadRE|SinglePassRE'
        ...
    @not_implemented
    def _mkEscapedCharClass_(self, *regexes:'expect [SingleRE]'):
        # -> 'SingleRE|DeadRE|SinglePassRE'
        ...
    @not_implemented
    def mkSingleChar(self, char):
        # -> 'SingleRE'
        ...




    Beginning = object()
    InvCharClass = object()
    CharRangeJointer  = object()

    @override
    def mkAlter(self, *regexes:'expect [ConcatRE]', end):
        # -> 'AlterRE'
        if end != 'mkAlter':
            raise Exception('parenthesis mismatched')
        return self._mkAlter_(*regexes)


    @override
    def mkConcat(self, Beginning, *regexes, end):
        # -> 'ConcatRE'
        if Beginning is not self.Beginning:
            raise logic-error
        if end != 'mkConcat':
            raise Exception('parenthesis mismatched')
        return self._mkConcat_(*regexes)

    @override
    def mkMulti(self, Beginning, *regexes:'expect [SingleRE]', end):
        # -> 'slice|UInt'
        if Beginning is not self.Beginning:
            raise logic-error
        if end != 'mkMulti':
            raise Exception('parenthesis mismatched')
        return self._mkMulti_(*regexes)


    @override
    def mkCharClass(self, Beginning, *regexes:'may leading with InvCharClass, expect [SingleRE|SinglePassRE|CharRangeJointer]', end):
        # -> 'SingleRE|DeadRE|SinglePassRE'
        if Beginning is not self.Beginning:
            raise logic-error
        if end != 'mkCharClass':
            raise Exception('parenthesis mismatched')
        return self._mkCharClass_(*regexes)


    @override
    def mkEscapedCharClass(self, Beginning, *regexes:'expect [SingleRE]', end):
        # -> 'SingleRE|DeadRE|SinglePassRE'
        if Beginning is not self.Beginning:
            raise logic-error
        if end != 'mkEscapedCharClass':
            raise Exception('parenthesis mismatched')
        return self._mkEscapedCharClass_(*regexes)

whole_set = CharBlockSet().self_make_whole_block_set()
def make_char_rng(first_char, last_char):
    ops = theChar_as_BlockDictKeyOps
    rng = (ops.mkTheKey(first_char), ops.mkTheKey(last_char))
    return rng
def make_char_rng_block_set(first_char, last_char):
    return CharBlockSet([make_char_rng(first_char, last_char)]
                        , is_block_keys=True)

#[:digit:]   \d          [0-9]
digits = make_char_rng_block_set('0', '9')
#[:lower:]   \l          [a-z]
lower_alphas = make_char_rng_block_set('a', 'z')
lower_alphas_ = lower_alphas.copy()
lower_alphas_.add('_')
#[:upper:]   \u          [A-Z]
upper_alphas = make_char_rng_block_set('A', 'Z')
upper_alphas_ = upper_alphas.copy()
upper_alphas_.add('_')
#[:alpha:]               [a-zA-Z]
alphas = lower_alphas | upper_alphas
alphas_ = lower_alphas_ | upper_alphas_
#[:alnum:]               [a-zA-Z0-9]
alnums = alphas | digits
alnums_ = alphas_ | digits
#[:ascii:]               [\x00-\x7F]
asciis = make_char_rng_block_set('\0', '\x7F')
#[:blank:]   \h          [ \t]
blanks = CharBlockSet(' \t')
#[:cntrl:]               [\x00-\x1F\x7F]
cntrls = make_char_rng_block_set('\0', '\x1F')
cntrls.add('\x7F')
#[:graph:]               [\x21-\x7E]
graphs = make_char_rng_block_set('\x21', '\x7E')
#[:print:]               [\x20-\x7E]
prints = make_char_rng_block_set('\x20', '\x7E')
#[:punct:]               [!"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]
puncts = CharBlockSet(r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
#[:space:]   \s          [ \t\r\n\v\f]
spaces = CharBlockSet(' \t\r\n\v\f')
#[:word:]    \w          [A-Za-z0-9_]
words = alnums_
#[:xdigit:]              [A-Fa-f0-9]
xdigits = (make_char_rng_block_set('A', 'F')
            | make_char_rng_block_set('a', 'f')
            | digits
            )



_EscapedCharClassName2terminal_set = \
    {'digit': digits
    ,'lower': lower_alphas
    ,'lower_': lower_alphas_
    ,'upper': upper_alphas
    ,'upper_': upper_alphas_
    ,'alpha': alphas
    ,'alpha_': alphas_
    ,'alnum': alnums
    ,'alnum_': alnums_
    ,'ascii': asciis
    ,'blank': blanks
    ,'cntrl': cntrls
    ,'graph': graphs
    ,'print': prints
    ,'punct': puncts
    ,'space': spaces
    ,'word': words
    ,'xdigit': xdigits
    }

_char2base = dict(zip(
    'xXoObB'
    , [16, 16, 8, 8, 2, 2]
    ))
class SimpleNameSpace(ISimpleNameSpace):
    __slots__ = ()

    def mkSingle_fromEscapedCharClassName(self, name):
        old_name = name
        name = name.strip()
        if is_char(name) and name in 'abfnrtv':
            ch = eval(f'"\\{name}"')
            return self.mkSingleChar(ch)
        may_terminal_set = _EscapedCharClassName2terminal_set.get(name)
        if may_terminal_set is not None:
            terminal_set = may_terminal_set
            return self.mkSingle(terminal_set)

        try:
            def f(name):
                if len(name) >= 2:
                    base = _char2base.get(name[0])
                    if base is not None:
                        chr_ord = int(name[1:], base=base)
                        return chr_ord
                return None

            may_chr_ord = None
            if name[0:1] == '0':
                # 0x/...
                may_chr_ord = f(name[1:])
            elif name[:2] in ('U+', 'u+'):
                # U+...
                may_chr_ord = int(name[2:], base=16)
            else:
                # x/o/b...
                may_chr_ord = f(name)

            if may_chr_ord is not None:
                chr_ord = may_chr_ord
            else:
                # \d+
                chr_ord = int(name)
        except:
            raise NotImplementedError(f'<{old_name!r}>')
        try:
            ch = chr(chr_ord)
        except ValueError:
            raise Exception(f'bad char ord: <{old_name!r}>')
        return self.mkSingleChar(ch)

    def str2Multi(self, s:str):
        # -> 'slice|UInt'
        # "\s*\d*\s*,\s*\d*\s*"
        # "\s*\d+\s*"
        ls = s.split(',')

        L = len(ls)
        assert L
        if L > 2: raise Exception(f'bad format for Multi: too many ",": {s!r}')
        if L == 2:
            a, b = ls
            a = a.strip()
            b = b.strip()
            m = 0 if not a else int(a)
            M = None if not b else int(b)
            return slice(m, M)
        if L == 1:
            [a] = ls
            m = int(a)
            return m
        raise logic-error


    @override
    def _mkAlter_(self, *regexes:'expect [ConcatRE]'):
        # -> 'AlterRE'
        return AlternationRE(regexes)
    @override
    def _mkConcat_(self, *regexes):
        # -> 'ConcatRE'
        return ConcatenationRE(regexes)


    def mkSingle(self, terminal_set):
        assert isinstance(terminal_set, IBlockSet)
        assert terminal_set.block_dict_key_ops == theChar_as_BlockDictKeyOps
        return SingleRE(terminal_set)
    def mkSingleNot(self, terminal_set):
        assert isinstance(terminal_set, IBlockSet)
        assert terminal_set.block_dict_key_ops == theChar_as_BlockDictKeyOps
        return SingleNotRE(terminal_set)
    @override
    def mkSingleChar(self, char):
        # -> 'SingleRE'
        return SingleRE(CharBlockSet(char))

    @override
    def mkSinglePass(self):
        # -> 'SingleRE'|'SinglePassRE'
        return theSinglePassRE

    @override
    def _mkMulti_(self, *regexes:'expect [SingleRE]'):
        # -> 'slice|UInt'
        s = SingleREs2str(regexes)
        return self.str2Multi(s)

    @override
    def _mkCharClass_(self, *regexes:'may leading with InvCharClass, expect [SingleRE|SinglePassRE|CharRangeJointer]'):
        # -> 'SingleRE|DeadRE|SinglePassRE'
        ops = theChar_as_BlockDictKeyOps
        if regexes[0] is self.InvCharClass:
            f = self.mkSingleNot
            regexes = regexes[1:]
            if not regexes:
                return SingleRE(whole_set)
                #return theSinglePassRE
        else:
            f = self.mkSingle
            if not regexes:
                return theDeadRE

        seqs = split_seq2seq1s__pred(regexes, lambda x:x is self.CharRangeJointer)
        assert seqs
        if not all(seqs):
            # [... \-\- ...] or [\- ...] or [... \-]
            raise Exception('bad format in char class: "-" in "[]" without first/last char')
        if len(seqs) == 1:
            [regexes] = seqs
            # error: s = SingleREs2str(regexes)
            #   may contain SingleRE for escaped char class
            terminal_set = unionSingleREs(regexes).terminal_set
        else:
            regexes = [seqs[0][0], seqs[-1][-1]]
            for seq in seqs:
                assert all(isinstance(x, ISimpleRE) for x in seq)
                regexes.extend(seq[1:-1])

            rngs = []
            for seqL, seqR in zip(seqs, seqs[1:]):
                first_char, last_char = SingleREs2str([seqL[-1], seqR[0]])
                if first_char > last_char:
                    raise Exception('bad format in char class: "-" : first_char > last_char')
                left_bound = ops.mkTheKey(first_char)
                right_bound = ops.mkTheKey(last_char)
                rng = (left_bound, right_bound)
                rngs.append(rng)
            re = self.mkSingle(CharBlockSet(rngs, is_block_keys=True))
            regexes.append(re)
            terminal_set = unionSingleREs(regexes).terminal_set


        return f(terminal_set)

    @override
    def _mkEscapedCharClass_(self, *regexes:'expect [SingleRE]'):
        # -> 'SingleRE|DeadRE|SinglePassRE'
        name = SingleREs2str(regexes)
        return self.mkSingle_fromEscapedCharClassName(name)

theSimpleNameSpace = SimpleNameSpace()

def parse_string_regex_pattern(pattern:str, simplify:bool=True
    , *
    # terminal_set_cmp/is_terminal_block_set used for debug only
    , terminal_set_cmp=None
    , is_terminal_block_set=True
    ):
    # pattern -> ISimpleRE
    tokens = iter_tokens_of_string_regex_pattern(pattern)
    py_expr_str = ''.join(stream_convertor(tokens))
    locals = {'ns': theSimpleNameSpace}
    regex = safe_eval(py_expr_str, locals=locals)
    if simplify:
        regex = regex.simplify(
                terminal_set_cmp=terminal_set_cmp
                , is_terminal_block_set=is_terminal_block_set)
    return regex


def char2regex(ch):
    assert is_char(ch)
    return chars2char_class(ch)
def chars2char_class(s):
    assert type(s) is str
    terminal_set = CharBlockSet(s)
    return SingleRE(terminal_set)
def _t():
    string_regex_pattern = r'a\+\(b\[cd\]\|e\+\)\*'
    regex = parse_string_regex_pattern(string_regex_pattern)
    reA, reB, reC, reD, reE = map(char2regex, 'abcde')
    reCD = chars2char_class('cd')
    r = +reA >> -((reB >> reCD) | +reE)
    assert r.simplify(None, False) == regex.simplify(None, False)

    #rint(regex)
    string_regex_pattern = r'a\+\*\?\{1,2\}\(\[\^\]\)\[a-f14-7\.\]\|'
    regex = parse_string_regex_pattern(string_regex_pattern)
    r = (((-+reA)[0:1][1:2] >> SingleRE(whole_set) >> SingleRE(whole_set))|theNullRE)
    try:
        #assert r.simplify(None, False) == regex.simplify(None, False)
        assert r.simplify(None, True) == regex.simplify(None, True)
    except:
        #print(r.simplify(None, False))
        #print(regex.simplify(None, False))
        print(r.simplify(None, True))
        print(regex.simplify(None, True))
        raise
    return
    ops = theChar_as_BlockDictKeyOps
    rngAF = make_char_rng('a', 'f')
    rng47 = make_char_rng('4', '7')


_t()

'''
'''

