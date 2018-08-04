
r'''
' ' SPACE
'!' EXCLAMATION MARK
'"' QUOTATION MARK
'#' NUMBER SIGN
'$' DOLLAR SIGN
'%' PERCENT SIGN
'&' AMPERSAND
"'" APOSTROPHE
'(' LEFT PARENTHESIS
')' RIGHT PARENTHESIS
'*' ASTERISK
'+' PLUS SIGN
',' COMMA
'-' HYPHEN-MINUS
'.' FULL STOP
'/' SOLIDUS
'0' DIGIT ZERO
':' COLON
';' SEMICOLON
'<' LESS-THAN SIGN
'=' EQUALS SIGN
'>' GREATER-THAN SIGN
'?' QUESTION MARK
'@' COMMERCIAL AT
'A' LATIN CAPITAL LETTER A
'[' LEFT SQUARE BRACKET
'\\' REVERSE SOLIDUS
']' RIGHT SQUARE BRACKET
'^' CIRCUMFLEX ACCENT
'_' LOW LINE
'`' GRAVE ACCENT
'a' LATIN SMALL LETTER A
'{' LEFT CURLY BRACKET
'|' VERTICAL LINE
'}' RIGHT CURLY BRACKET
'~' TILDE
'''


__all__ = '''
    RecognizeSystem__TokenIsChar
    CachedRecognizeSystem__TokenIsChar
    Mixin_RecognizeSystem__TokenIsChar
    '''.split()
import unicodedata
# import curses.ascii as ascii # not exists????
from .RecognizeSystem import RecognizeSystem, CachedRecognizeSystem
from .Utils import drop_prefix, snd, end_of


class Ascii(str):
    @staticmethod
    def isxdigit(ch):
        return ch.isdigit() or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'
ascii = Ascii







char2name_dict = {'\n': 'NEWLINE'}
def char2name(ch):
    if ch.isalnum():
        return ch
    name = unicodedata.name(ch, None)
    if not name:
        name = char2name_dict.get(ch)
    return name

def generate_single_char_method():
    # for single_char_method
    fmt = '''\
    def RS_T_char_{char_name}(self, tk):
        ch = self.RS_token2char(tk)
        return ch == {repr_char}\
'''
    for i in range(128):
        ch = chr(i)
        #rint(repr(ch), unicodedata.name(ch, None))
        char_name = char2name(ch)
        if char_name:
            char_name = char_name.replace(' ', '_')
            char_name = char_name.replace('-', '_')
            s = fmt.format(repr_char = repr(ch), char_name=char_name)
            print(s)


def generate_char_set_method():#(name, and_not=None):
    # isXXX()
    fmt = '''\
    def RS_T_{nameM}(self, tk):
        ch = self.RS_token2char(tk)
        return ascii.is{name}(ch)\
'''
    names  = 'digit xdigit   alpha alnum upper       lower      '.split()
    nameMs = 'digit hexdigit alpha alnum upper_alpha lower_alpha'.split()
    for name, nameM in zip(names, nameMs):
        print(fmt.format(name=name, nameM=nameM))

    # XXX_
    nameMs = nameMs + 'digitNot0  hexdigit  hexdigitNot0'.split()
    fmt = '''\
    def RS_T_{nameM}_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_{nameM}(tk) or ch == '_'\
'''
    for nameM in nameMs:
        print(fmt.format(nameM=nameM))

    # XXXNot0
    fmt = '''\
    def RS_T_{nameM}Not0(self, ch):
        ch = self.RS_token2char(tk)
        return self.RS_T_{nameM}(tk) and ch != '0'\
'''
    nameMs = 'digit  hexdigit'.split()
    for nameM in nameMs:
        print(fmt.format(nameM=nameM))
if 0:
    generate_char_set_method()
    print('\n'*2)
    generate_single_char_method()










#################################


class Mixin_RecognizeSystem__TokenIsChar:
    '''\
to offer many usr_token_set_ids, usr_recognizer_ids
    usr_token_set_id:
        # char_set
        space spaceNotNewline any_charNotNewline
        # with or without '_' : [0-9a-zA-Z_]
        digit  digitNot0  hexdigit  hexdigitNot0
        digit_ digitNot0_ hexdigit_ hexdigitNot0_
        alpha  alnum  upper_alpha  lower_alpha
        alpha_ alnum_ upper_alpha_ lower_alpha_

        # single char
        char_0 ...
        char_a ...
        char_A ...
        char_XXX
    usr_recognizer_id:
        many_<char_set>
        many1_<char_set>
        identifier # alpha_ alnum_*

'''

    def __RS_many_char_set(self, char_set_name, char2bool, multi):
        char_recognizer = self.token2bool2recognizer(
                            char_set_name, char2bool)

        #char_recognizer = self.id_recognizer2avoid_empty(
        #                    char_set_name, None, char_recognizer)
        recognizer = self.mkPrimeItemRecognizer(
            char_set_name, char_recognizer, (), '', multi)
        m, M = multi
        def to_char(r):
            tk_case, tk = r
            return self.RS_token2char(tk)
        def many_recognizer(st):
            ls, ts = recognizer(st)
            s = ''.join(map(to_char, ls))
            if 0 and self.RS_have_same_position(st, ts) and m != 0:
                print('char_set_name:{!r}, {{{},{}}}'
                        .format(char_set_name, m, M))
                raise logic-error
            return s, ts
        if 0 and m > 0:
            print(m)
            many_recognizer = self.id_recognizer2avoid_empty(
                'many{}_{}'.format(m, char_set_name), None, many_recognizer)
        return many_recognizer
    def __getattr__(self, attr):
        #rint('__getattr__', attr)
        if attr.startswith('RS_NR_many'):
            suffix = drop_prefix(attr, 'RS_NR_many_')
            if suffix is not None:
                char2bool = getattr(self, 'RS_T_'+suffix, None)
                if char2bool is not None:
                    #rint('got many')
                    return self.__RS_many_char_set(suffix, char2bool, (0,None))
            if attr.startswith('RS_NR_many1_'):
                raise ValueError(
                    'use "RS_NNR_many1_<...>" instead of "RS_NR_many1_<...>"')
        elif attr.startswith('RS_NNR_many1'):
            suffix = drop_prefix(attr, 'RS_NNR_many1_')
            if suffix is not None:
                char2bool = getattr(self, 'RS_T_'+suffix, None)
                if char2bool is not None:
                    #rint('got many1')
                    return self.__RS_many_char_set(suffix, char2bool, (1,None))
        return getattr(super(), attr)



    def RS_R_identifier(self, st):
        alpha_ = self.token2bool2recognizer('alpha_', self.RS_T_alpha_)
        #alnum_ = self.token2bool2recognizer('alnum_', self.RS_T_alnum_)
        many_alnum_ = self.__RS_many_char_set('alnum_', self.RS_T_alnum_, '*')
        def identifier_recognizer(st):
            h, st = alpha_(st)
            s, st = many_alnum_(st)
            return h+s, st
        return identifier_recognizer

    def RS_T_space(self, ch):
        return ch.isspace()
    def RS_T_spaceNotNewline(self, ch):
        return ch.isspace() and ch != '\n'
    def RS_T_any_charNotNewline(self, ch):
        return ch != '\n'



    def RS_token2char(self, tk):
        ch = tk
        assert type(ch) is str and len(ch) == 1
        return ch
    ##########################


    def RS_T_digit(self, tk):
        ch = self.RS_token2char(tk)
        return ascii.isdigit(ch)
    def RS_T_hexdigit(self, tk):
        ch = self.RS_token2char(tk)
        return ascii.isxdigit(ch)
    def RS_T_alpha(self, tk):
        ch = self.RS_token2char(tk)
        return ascii.isalpha(ch)
    def RS_T_alnum(self, tk):
        ch = self.RS_token2char(tk)
        return ascii.isalnum(ch)
    def RS_T_upper_alpha(self, tk):
        ch = self.RS_token2char(tk)
        return ascii.isupper(ch)
    def RS_T_lower_alpha(self, tk):
        ch = self.RS_token2char(tk)
        return ascii.islower(ch)
    def RS_T_digit_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_digit(tk) or ch == '_'
    def RS_T_hexdigit_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_hexdigit(tk) or ch == '_'
    def RS_T_alpha_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_alpha(tk) or ch == '_'
    def RS_T_alnum_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_alnum(tk) or ch == '_'
    def RS_T_upper_alpha_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_upper_alpha(tk) or ch == '_'
    def RS_T_lower_alpha_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_lower_alpha(tk) or ch == '_'
    def RS_T_digitNot0_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_digitNot0(tk) or ch == '_'
    def RS_T_hexdigit_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_hexdigit(tk) or ch == '_'
    def RS_T_hexdigitNot0_(self, tk):
        ch = self.RS_token2char(tk)
        return self.RS_T_hexdigitNot0(tk) or ch == '_'
    def RS_T_digitNot0(self, ch):
        ch = self.RS_token2char(tk)
        return self.RS_T_digit(tk) and ch != '0'
    def RS_T_hexdigitNot0(self, ch):
        ch = self.RS_token2char(tk)
        return self.RS_T_hexdigit(tk) and ch != '0'



    def RS_T_char_NEWLINE(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '\n'
    def RS_T_char_SPACE(self, tk):
        ch = self.RS_token2char(tk)
        return ch == ' '
    def RS_T_char_EXCLAMATION_MARK(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '!'
    def RS_T_char_QUOTATION_MARK(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '"'
    def RS_T_char_NUMBER_SIGN(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '#'
    def RS_T_char_DOLLAR_SIGN(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '$'
    def RS_T_char_PERCENT_SIGN(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '%'
    def RS_T_char_AMPERSAND(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '&'
    def RS_T_char_APOSTROPHE(self, tk):
        ch = self.RS_token2char(tk)
        return ch == "'"
    def RS_T_char_LEFT_PARENTHESIS(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '('
    def RS_T_char_RIGHT_PARENTHESIS(self, tk):
        ch = self.RS_token2char(tk)
        return ch == ')'
    def RS_T_char_ASTERISK(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '*'
    def RS_T_char_PLUS_SIGN(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '+'
    def RS_T_char_COMMA(self, tk):
        ch = self.RS_token2char(tk)
        return ch == ','
    def RS_T_char_HYPHEN_MINUS(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '-'
    def RS_T_char_FULL_STOP(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '.'
    def RS_T_char_SOLIDUS(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '/'
    def RS_T_char_0(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '0'
    def RS_T_char_1(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '1'
    def RS_T_char_2(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '2'
    def RS_T_char_3(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '3'
    def RS_T_char_4(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '4'
    def RS_T_char_5(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '5'
    def RS_T_char_6(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '6'
    def RS_T_char_7(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '7'
    def RS_T_char_8(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '8'
    def RS_T_char_9(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '9'
    def RS_T_char_COLON(self, tk):
        ch = self.RS_token2char(tk)
        return ch == ':'
    def RS_T_char_SEMICOLON(self, tk):
        ch = self.RS_token2char(tk)
        return ch == ';'
    def RS_T_char_LESS_THAN_SIGN(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '<'
    def RS_T_char_EQUALS_SIGN(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '='
    def RS_T_char_GREATER_THAN_SIGN(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '>'
    def RS_T_char_QUESTION_MARK(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '?'
    def RS_T_char_COMMERCIAL_AT(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '@'
    def RS_T_char_A(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'A'
    def RS_T_char_B(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'B'
    def RS_T_char_C(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'C'
    def RS_T_char_D(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'D'
    def RS_T_char_E(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'E'
    def RS_T_char_F(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'F'
    def RS_T_char_G(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'G'
    def RS_T_char_H(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'H'
    def RS_T_char_I(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'I'
    def RS_T_char_J(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'J'
    def RS_T_char_K(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'K'
    def RS_T_char_L(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'L'
    def RS_T_char_M(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'M'
    def RS_T_char_N(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'N'
    def RS_T_char_O(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'O'
    def RS_T_char_P(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'P'
    def RS_T_char_Q(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'Q'
    def RS_T_char_R(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'R'
    def RS_T_char_S(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'S'
    def RS_T_char_T(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'T'
    def RS_T_char_U(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'U'
    def RS_T_char_V(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'V'
    def RS_T_char_W(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'W'
    def RS_T_char_X(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'X'
    def RS_T_char_Y(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'Y'
    def RS_T_char_Z(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'Z'
    def RS_T_char_LEFT_SQUARE_BRACKET(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '['
    def RS_T_char_REVERSE_SOLIDUS(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '\\'
    def RS_T_char_RIGHT_SQUARE_BRACKET(self, tk):
        ch = self.RS_token2char(tk)
        return ch == ']'
    def RS_T_char_CIRCUMFLEX_ACCENT(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '^'
    def RS_T_char_LOW_LINE(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '_'
    def RS_T_char_GRAVE_ACCENT(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '`'
    def RS_T_char_a(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'a'
    def RS_T_char_b(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'b'
    def RS_T_char_c(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'c'
    def RS_T_char_d(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'd'
    def RS_T_char_e(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'e'
    def RS_T_char_f(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'f'
    def RS_T_char_g(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'g'
    def RS_T_char_h(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'h'
    def RS_T_char_i(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'i'
    def RS_T_char_j(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'j'
    def RS_T_char_k(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'k'
    def RS_T_char_l(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'l'
    def RS_T_char_m(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'm'
    def RS_T_char_n(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'n'
    def RS_T_char_o(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'o'
    def RS_T_char_p(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'p'
    def RS_T_char_q(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'q'
    def RS_T_char_r(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'r'
    def RS_T_char_s(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 's'
    def RS_T_char_t(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 't'
    def RS_T_char_u(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'u'
    def RS_T_char_v(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'v'
    def RS_T_char_w(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'w'
    def RS_T_char_x(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'x'
    def RS_T_char_y(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'y'
    def RS_T_char_z(self, tk):
        ch = self.RS_token2char(tk)
        return ch == 'z'
    def RS_T_char_LEFT_CURLY_BRACKET(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '{'
    def RS_T_char_VERTICAL_LINE(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '|'
    def RS_T_char_RIGHT_CURLY_BRACKET(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '}'
    def RS_T_char_TILDE(self, tk):
        ch = self.RS_token2char(tk)
        return ch == '~'

end_of(Mixin_RecognizeSystem__TokenIsChar)


class RecognizeSystem__TokenIsChar(
    Mixin_RecognizeSystem__TokenIsChar, RecognizeSystem):
    pass
class CachedRecognizeSystem__TokenIsChar(
    Mixin_RecognizeSystem__TokenIsChar, CachedRecognizeSystem):
    pass

