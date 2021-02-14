
r'''

python c-string escape/quote
e ../../python3_src/seed/text/escape_as_c_string.py
py -m seed.text.escape_as_c_string



'"?\abfnrtv
xuU[0-7]
    \0 - 并不一定结束，必须用 \000 或 \x00

https://en.cppreference.com/w/cpp/language/escape
 Escape
sequence 	Description 	Representation
Simple escape sequences
\' 	single quote 	byte 0x27 in ASCII encoding
\" 	double quote 	byte 0x22 in ASCII encoding
\? 	question mark 	byte 0x3f in ASCII encoding
\\ 	backslash 	byte 0x5c in ASCII encoding
\a 	audible bell 	byte 0x07 in ASCII encoding
\b 	backspace 	byte 0x08 in ASCII encoding
\f 	form feed - new page 	byte 0x0c in ASCII encoding
\n 	line feed - new line 	byte 0x0a in ASCII encoding
\r 	carriage return 	byte 0x0d in ASCII encoding
\t 	horizontal tab 	byte 0x09 in ASCII encoding
\v 	vertical tab 	byte 0x0b in ASCII encoding
Numeric escape sequences
\nnn 	arbitrary octal value 	byte nnn
\xnn 	arbitrary hexadecimal value 	byte nn
Conditional escape sequences[1]
\c 	Implementation-defined 	Implementation-defined
Universal character names
\unnnn 	arbitrary Unicode value;
may result in several code units 	code point U+nnnn
\Unnnnnnnn 	arbitrary Unicode value;
may result in several code units 	code point U+nnnnnnnn

    ↑ Conditional escape sequences are conditionally-supported. The character c in each conditional escape sequence is a member of basic source character set that is not the character following the \ in any other escape sequence.



https://en.cppreference.com/w/cpp/language/string_literal
String literal
  Syntax
    "s-char-sequence" 	(1) 	
    L"s-char-sequence" 	(2) 	
    u8"s-char-sequence" 	(3) 	(since C++11)
    u"s-char-sequence" 	(4) 	(since C++11)
    U"s-char-sequence" 	(5) 	(since C++11)
    prefix(optional) R"delimiter(raw_characters)delimiter" 	(6) 	(since C++11)
  Explanation
    s-char-sequence 	- 	A sequence of zero or more s-chars. A s-char is one of

        character from the source character set, except the double-quote ", backslash \, or new-line character
        escape sequence, as defined in escape sequences
        universal character name, as defined in escape sequences 

    prefix 	- 	One of L, u8, u, U
    delimiter 	- 	A character sequence made of any source character but parentheses, backslash and spaces (can be empty, and at most 16 characters long)
    raw_characters 	- 	Any character sequence, except that it must not contain the closing sequence )delimiter"


    1) Narrow multibyte string literal. The type of an unprefixed string literal is const char[N], where N is the size of the string in code units of the execution narrow encoding, including the null terminator.
    2) Wide string literal. The type of a L"..." string literal is const wchar_t[N], where N is the size of the string in code units of the execution wide encoding, including the null terminator.
    3) UTF-8 encoded string literal. The type of a u8"..." string literal is const char[N] (until C++20)const char8_t[N] (since C++20), where N is the size of the string in UTF-8 code units including the null terminator.
    4) UTF-16 encoded string literal. The type of a u"..." string literal is const char16_t[N], where N is the size of the string in UTF-16 code units including the null terminator.
    5) UTF-32 encoded string literal. The type of a U"..." string literal is const char32_t[N], where N is the size of the string in UTF-32 code units including the null terminator.
    6) Raw string literal. Used to avoid escaping of any character. Anything between the delimiters becomes part of the string. prefix, if present, has the same meaning as described above.

    Each s-char initializes the corresponding element(s) in the string literal object. A s-char corresponds to more than one element if and only if it is represented by a sequence of more than one code units in the string literal's associated character encoding.

    If a character lacks representation in the associated character encoding,

        if the string literal is an ordinary string literal or wide string literal, it is conditionally-supported and an implementation-defined code unit sequence is encoded;
        otherwise (the string literal is UTF-encoded), the string literal is ill-formed. 

            (since C++23)

    Each numeric escape sequence corresponds to a single element. If the value specified by the escape sequence fits within the unsigned version of the element type, the element has the specified value (possibly after conversion to the element type); otherwise (the specified value is out of range), the string literal is ill-formed. (since C++23)










https://stackoverflow.com/questions/1675181/get-str-repr-with-double-quotes-python
    1. def string_to_c(...)
    2. json.dumps(...)


def string_to_c(s, max_length = 140, unicode=False):
    ret = []

    # Try to split on whitespace, not in the middle of a word.
    split_at_space_pos = max_length - 10
    if split_at_space_pos < 10:
        split_at_space_pos = None

    position = 0
    if unicode:
        position += 1
        ret.append('L')

    ret.append('"')
    position += 1
    for c in s:
        newline = False
        if c == "\n":
            to_add = "\\\n"
            newline = True
        elif ord(c) < 32 or 0x80 <= ord(c) <= 0xff:
            to_add = "\\x%02x" % ord(c)
        elif ord(c) > 0xff:
            if not unicode:
                raise ValueError, "string contains unicode character but unicode=False"
            to_add = "\\u%04x" % ord(c)
        elif "\\\"".find(c) != -1:
            to_add = "\\%c" % c
        else:
            to_add = c

        ret.append(to_add)
        position += len(to_add)
        if newline:
            position = 0

        if split_at_space_pos is not None and position >= split_at_space_pos and " \t".find(c) != -1:
            ret.append("\\\n")
            position = 0
        elif position >= max_length:
            ret.append("\\\n")
            position = 0

    ret.append('"')

    return "".join(ret)

    print string_to_c("testing testing testing testing testing testing testing testing testing testing testing testing testing testing testing testing testing", max_length = 20)
    print string_to_c("Escapes: \"quote\" \\backslash\\ \x00 \x1f testing \x80 \xff")
    print string_to_c(u"Unicode: \u1234", unicode=True)
    print string_to_c("""New
lines""")



#'''




def escape_as_c_string__narrow(s):
    return ''.join(iter_escape_as_c_string__narrow(s))
def iter_escape_as_c_string__narrow(s):
    '\'\"\?\\\a\b\f\n\r\t\v'
    for c in s:
        if ' ' <= c <= '~':
            if c in '\'\"\\':
                yield fr'\{c}'
            else:
                yield c
        elif c > '\xff':
            raise ValueError(f'{c!r} is not narrow char / byte')
        else:
            i = '\a\b\f\n\r\t\v'.find(c)
            if i < 0:
                #bug:not hex: yield fr'\x{ord(c):0>2}'
                yield fr'\x{ord(c):0>2x}'
            else:
                yield '\\' + 'abfnrtv'[i]



def _t():
    try:
        escape_as_c_string__narrow('\u0100')
        raise logic-error
    except ValueError:
        pass

    s1 = ''.join(map(chr, range(2**8)))
    es = escape_as_c_string__narrow(s1)
    s2 = eval(f'"{es}"')
    #print(f'{s1!r}\n\n{es!s}\n\n{s2!r}\n\n')
    assert s1 == s2

_t()




