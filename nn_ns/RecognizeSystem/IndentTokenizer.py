

from abc import abstractmethod, ABCMeta
import re

# case for st
Dedent1s = 'Dedent1s'
Continue = 'Continue'
Forbidden = ''
Indent = 'Indent'
New = 'New'
InitialInput__strict = (Forbidden, New, Forbidden)
InitialInput__loose = (Forbidden, New, Indent)
InitialBlock = (Forbidden, Forbidden, Indent)
NextLineEQ_or_Dedents = (Dedent1s, New, Forbidden)
ThisLogicLineWithIndentGT = (Forbidden, Forbidden, Continue)
ThisLogicLineWithIndentGE = (Forbidden, Continue, Continue)
ThisLogicLineWithIndentAny = (Continue, Continue, Continue)
NextLineEQ_or_Dedents_or_ThisLogicLineWithIndentGT = (Dedent1s, New, Continue)
ThisLogicLineContinueNotSkipIndentEmptyLine = ...

class IndentTokenizer(metaclass=ABCMeta):
    '''\
st = ('Dedent1s'|'Continue'|'', 'Continue'|'New'|'', 'Continue'|'Indent'|'')
    # when compare curr_indent prev_indent
    #       LT                  EQ                  GT
    # '' - forbidden
    # 'This
st  = InitialInput   # allow indent? python:NO
        # ('', 'New', '') # not allow indent
        # ('', 'New', 'Indent') # allow indent
    | InitialBlock  # more indent than prev_indent
        # ('', '', 'Indent')
    | NextLineEQ_or_Dedents
        # same indent as prev_indent or any parent_indent
        # ('Dedent1s', 'New', '')
    | ThisLogicLineWithIndentGT # Haskell
        # ('', '', 'Continue')
    | ThisLogicLineWithIndentGE
        # mine LambdaD: [...;...] where '[;]' can be in same indent level
        # ('', 'Continue', 'Continue')
    | ThisLogicLineWithIndentAny # python '\\\n' or (..., ...)
        # ('Continue', 'Continue', 'Continue')
    | NextLineEQ_or_Dedents_or_ThisLogicLineWithIndentGT
        # ('Dedent1s', 'New', 'Continue')
    | ThisLogicLineContinueNotSkipIndentEmptyLine
        # multiline string/comment
        # '...'

prev_indent :: indent # InitialInput ==>> empty_indent
prev_vindent :: virtual_indent # InitialInput ==>> empty_indent
prev_bindent :: (is_virtual, xindent) === (False, indent) | (True, vindent)
virtual_indent
    # i.e. f = let x = do xxx = ...
    #                     ...
    #              y = ....
    #        where ...
    # "f = .... do " is a virtual_indent
    # "f = .... let " is another virtual_indent



# indent maybe str
indent_starts_with :: (indent, indent) -> bool
indent_eq :: (indent, indent) -> bool
mkIndentToken :: (prev_bindent, line, indent, line_tail) -> tk
mkVIndentToken :: (prev_bindent, line, vindent) -> tk
mkDedentToken :: (prev_bindent, line, indent, line_tail) -> tk


reset_tokenizer_state :: () -> ()
get_initial_input__st :: () -> st
new_initial_input__prev_indent :: () -> [tk]
split_to_iter_physical_lines :: file -> [line]
read_indent :: line -> (indent, line_tail)
tokenize_emptyline_without_indent
    :: line_tail -> [tk] | ... | raise Err
    # '...' means not an empty line
tokenize_line_without_indent
    :: line_tail -> ([virtual_indent], [[tk]], st) | raise Err
    # len([[tk]]) == len([virtual_indent]) + 1
tokenize_line_with_indent_emptyline
    :: line -> ([virtual_indent], [[tk]], st) | raise Err
    # to tokenize multiline-string/comment
    # if prev call to tokenize_line_with[out]_indent()
    #   return (_, ThisLogicLineContinueNotSkipIndentEmptyLine)
    #   then call this method
    # line may be empty line

'''
    def tokenize(self, input):
        self.reset_tokenizer_state()
        st = self.get_initial_input__st()
        prev_indent = self.new_initial_input__prev_indent()
        bindents = [(False, prev_indent)]
            # [(is_virtual, prev_xindent)]
            # (False, prev_indent) | (True, prev_vindent)
        del prev_indent
        tokens = []
        def f(vindents_, tokenss, st):
            assert len(vindents_) + 1 == len(tokenss)
            it = iter(tokenss)
            for vindent_, tokens_ in zip(vindent_, it):
                tokens.extend(tokens_)
                tk = self.mkVIndentToken(bindents[-1], line, vindent_)
                tokens.append(tk)
            [tokens_] = it
            tokens.extend(tokens_)

        for line in self.split_to_iter_physical_lines(input):
            if st is ThisLogicLineContinueNotSkipIndentEmptyLine:
                vindents_, tkss, st =\
                    self.tokenize_line_with_indent_emptyline(line)
                f(vindents_, tkss, st)
                continue

            # skip emptyline and indent
            indent, line_tail = self.read_indent(line)
            r = self.tokenize_emptyline_without_indent(line_tail)
            if r is not ...:
                # empty line
                emptyline_tokens = r
                vindents_ = []
                tkss = [emptyline_tokens]
                f(vindents_, tkss, st)
                continue

            # not empty line
            # verify indent with (st, prev_bindent)
            prev_bindent = bindents[-1]
            case = self.handle_nonempty_line_indent(
                            st, prev_bindent, indent)
            del prev_bindent
            block_tokens = self.insert_block_tokens(
                            bindents, case, line, indent, line_tail)
            tokens.extend(block_tokens)
            vindents_, line_tokenss, st = \
                        self.tokenize_line_without_indent(line_tail)
            f(vindents_, line_tokenss, st)

        return tokens
    def insert_block_tokens(
            self, inout_vindents, case, line, indent, line_tail)
        bindents = inout_vindents
        prev_bindent = bindents[-1]
        tokens = []
        if case == Indent:
            indent_tk = self.mkIndentToken(
                            prev_bindent, line, indent, line_tail)
            tokens.append(indent_tk)
            prev_bindent = (False, indent)
            bindents.append(prev_bindent)
        elif case == Dedent1s:
            L = len(bindents)
            tokensL = len(tokens)
            for i in range(L):
                prev_bindent = bindents[L-1-i]
                if not self._bindent_starts_with_indent(
                                prev_bindent, indent):
                    raise TokenizeError('indent error')
                if self._indent_starts_with_bindent(indent, prev_bindent):
                    # prev_bindent == indent
                    break
                # indent + ? == prev_bindent
                dedent_tk = self.mkDedentToken(
                                prev_bindent, line, indent, line_tail)
                tokens.append(dedent_tk)
            else:
                raise logic-error-file-initial-indent-isnot-empty
            delL = i
            del bindents[L-i:]
            assert prev_indent is bindents[-1]
            assert len(tokens) - tokensL == delL
            assert len(bindents) - L == delL
        elif case in (New, Continue):
            pass
        else:
            raise logic-error
        return tokens
    def handle_nonempty_line_indent(self, st, prev_bindent, indent):
        atLT, atEQ, atGT = st
        prev = prev_bindent
        # indent `compare` prev
        # partial ordering!!!!!!!
        GE = self._indent_starts_with_bindent(indent, prev)
            # indent >= prev
        LE = self._bindent_starts_with_indent(prev, indent)
            # indent <= prev
        EQ = GE and LE
        LT = LE and not GE # != not GE!!!
        GT = GE and not LE
        UU = not GE and not LE
        at = None
        if EQ:
            at = atEQ
        elif LT:
            at = atLT
        elif GT:
            at = atGT
        elif UU:
            raise TokenizeError(
                f'not comparable: '
                f'prev_indent: {prev_indent!r}, indent: {indent!r}'
                )
        else:
            raise logic-error
        if at == '':
            raise TokenizeError('indent error')
        elif at not in {Dedent1s, New, Continue, Indent}:
            raise logic-error
        return at



    def indent_eq(self, indentA, indentB):
        return self.indent_starts_with(indentA, indentB) \
            and self.indent_starts_with(indentB, indentA)

    def get_initial_input__st(self):
        # assume not allow indent
        return InitialInput__strict

    #############


    @abstractmethod
    def reset_tokenizer_state(self):pass
    @abstractmethod
    def mkIndentToken(self, prev_vindent, line, indent, line_tail):pass
    @abstractmethod
    def mkVIndentToken(self, prev_vindent, line, vindent):pass
    @abstractmethod
    def mkDedentToken(self, prev_vindent, line, indent, line_tail):pass
    @abstractmethod
    def tokenize_line_without_indent(self, line_tail):pass
    @abstractmethod
    def tokenize_line_with_indent_emptyline(self, line):
        # to tokenize multiline-string/comment
        # if prev call to tokenize_line_with[out]_indent()
        #   return (_, ThisLogicLineWithIndentAny)
        #   then call this method
        pass
    @abstractmethod
    def tokenize_emptyline_without_indent(self, line_tail):pass
    @abstractmethod
    def read_indent(self, line):pass
    @abstractmethod
    def split_to_iter_physical_lines(self, input):pass
    @abstractmethod
    def new_initial_input__prev_indent(self):pass
    @abstractmethod
    def indent_starts_with(self, org_indent, sub_indent):pass
    @abstractmethod
    def is_vindent_prefix_of_indent(self, vindent, indent):pass
    @abstractmethod
    def is_indent_prefix_of_vindent(self, indent, vindent):pass
    def _indent_starts_with_bindent(self, indent, bindent):
        is_virtual, xindent = bindent
        if is_virtual:
            vindent = xindent
            return self.is_vindent_prefix_of_indent(vindent, indent)
        indent_ = xindent
        return self.indent_starts_with(indent, indent_)
    def _bindent_starts_with_indent(self, bindent, indent):
        is_virtual, xindent = bindent
        if is_virtual:
            vindent = xindent
            return self.is_indent_prefix_of_vindent(indent, vindent)
        indent_ = xindent
        return self.indent_starts_with(indent_, indent)

# end IndentTokenizer


class IndentTokenizer__InputIsStr(IndentTokenizer):
    @abstractmethod
    def reset_tokenizer_state(self):pass
    @abstractmethod
    def mkIndentToken(self, prev_indent, line, indent, line_tail):pass
    @abstractmethod
    def mkVIndentToken(self, prev_vindent, line, vindent):pass
    @abstractmethod
    def mkDedentToken(self, prev_indent, line, indent, line_tail):pass
    @abstractmethod
    def tokenize_line_without_indent(self, line_tail):pass
    @abstractmethod
    def tokenize_line_with_indent_emptyline(self, line):pass


    ########

    def indent_starts_with(self, org_indent, sub_indent):
        # assume indent is str
        return org_indent.startswith(sub_indent)
    def new_initial_input__prev_indent(self):
        # assume indent is str
        return ''
    def split_to_iter_physical_lines(self, input):
        # assume input is str
        return iter(input.split('\n'))
    def read_indent(self, line):
        # assume line is str; indent is spaces
        line_tail = line.lstrip()
        indent = line[:len(line)-len(line_tail)]
        return indent, line_tail
    def tokenize_emptyline_without_indent(self, line_tail):
        # assume python line comment
        if not line_tail or line_tail[0] == '#':
            return []
        return ...
# end IndentTokenizer__InputIsStr



def mkStrPattern(quot):
    assert len(quot) == 1
    fmt = r'(?:{quot}(?:\\[^\n]|[^{quot}\\\n])*{quot})'
    return fmt.format(quot)
def mkStrPatternBoth():
    return r'(?:{}|{})'.format(mkStrPattern('"'), mkStrPattern("'")) +
str_pattern_both = mkStrPatternBoth()
class IndentTokenizerGrammarTokenizer(IndentTokenizer__InputIsStr):
    pattern = (r'(?m-s:'
        # keyword block open close str cstr rstr comment id -indent spaces
            # -indent by superclass
        # keyword -block str cstr rstr -comment id -indent spaces
            # -block - alter st
            # -comment - after stmt
        r'(if|otherwise|return|error|call|goto)'
        r'|(:)|(\()|(\))'
        r'|({0})|(c{0})|(r{0})'.format(str_pattern_both)
        r'|(#.*)'
        r'|([\d\w_]+)'
        r'|((?:^|(?<=\n))(?:(?!\n)\S)+)'
        r'|(\n)'
        r'|(\S+)'
        ')')
    rex = re.compile(pattern)
    def __init__(self):pass
    def reset_tokenizer_state(self):pass
    def tokenize_line_with_indent_emptyline(self, line):
        raise logic-error
    def mkIndentToken(self, prev_indent, line, indent, line_tail):
        return ('indent', None)
    def mkVIndentToken(self, prev_vindent, line, vindent):
        raise logic-error
    def mkDedentToken(self, prev_indent, line, indent, line_tail):
        return ('dedent', None)
    def tokenize_line_without_indent(self, line_tail):
        begin = 0
        tokens = []
        for m in self.rex.finditer(line_tail):
            if not m: raise TokenizeError(begin)
            assert m.start() == begin
            begin = m.end()
            [keyword, block, open, close
                , str, cstr, rstr, comment, id, indent, spaces]\
                = m.groups()
            assert indent is None
            d = dict(keyword=keyword, block=block
                , open=open, close=close, id=id
                , spaces=spaces, comment=comment
                , str=str, cstr=cstr, rstr=rstr)
            assert sum(val is not None for val in d.values()) == 1
            for key, val in d.items():
                if val is not None:
                    tokens.append((key, val))
                    break
            else:
                raise logic-error
        if not tokens: raise logic-error
        if tokens[-1][0] == 'comment':
            tokens.pop()
        if not tokens: raise logic-error
        assert tokens[-1][0] != 'comment':
        if tokens[-1][0] == 'block':
            tokens.pop()
            st = InitialBlock
        else:
            st = NextLineEQ_or_Dedents_or_ThisLogicLineWithIndentGT
        if any(case == 'block' for case, _ in tokens):
            raise TokenizeError('":" not at end of stmt')
        return [], tokens, st


IndentTokenizer_tokenize_grammar = r'''

'''



IndentTokenizer_grammar = r'''

IndentTokenizerGrammar = StateDecl*
StateDecl = StateID Block
Block-stmts = indent Stmt* dedent
Block-empty = newline

Stmt = MayNamed StmtBody
StmtBody-def = TokenDef
StmtBody-if = IfClause? Action newline



MayNamed-named = TokenID -eq
MayNamed-unnamed = @pass@
TokenDef = TokenSpec Block

IfClause = kw_if TokenSpec
Action-call = kw_call StateID
Action-goto = kw_goto StateID
Action-return = kw_return
Action-error = kw_error StrCR1s?

TokenSpec-rex = StrL1s
TokenSpec-str = StrCR1s

TokenSpec-otherwise = kw_otherwise


StateID == IDBase
TokenID == IDBase
IDBase-str = StrCR1s
IDBase-id = char_alnum_+
StrCR1s-many1 = open StrCR+ close
StrCR1s-just = StrCR
StrL1s = open StrL+ close
StrL1s-just = StrL


StrCR-str = char_c StrL
StrCR-raw = char_r StrL
StrL-s = -s_wrap $$ StrL_term$s_wrap*
StrL-d = -d_wrap $$ StrL_term$d_wrap*
StrL_term-escape = escape $$ dotted_char
StrL_term-char = dotted_char


dotted_char == any_charNotNewline
escape == char_REVERSE_SOLIDUS
s_wrap == char_APOSTROPHE
d_wrap == char_QUOTATION_MARK
open == char_LEFT_PARENTHESIS
close == char_RIGHT_PARENTHESIS
@token_set@
    char_QUOTATION_MARK char_APOSTROPHE char_REVERSE_SOLIDUS
    char_LEFT_PARENTHESIS char_RIGHT_PARENTHESIS
    char_c char_r
    any_charNotNewline
    char_alnum_
    indent dedent newline
    # ':'   none
@nonnull_recognizer@
    kw_if
    kw_otherwise
    kw_call
    kw_goto
    kw_return
    kw_error
'''

