
import re
import itertools


word_pattern = re.compile(r'\S+')
word_newline_pattern = re.compile(r'\S+|\n')

def word_tokenize(src, word_pattern = word_pattern, *,
                  pycomment_start = None,
                  ccomment_start = None,
                  ccomment_end = None):
    r'''a simple tokenizer.

example:
    >>> word_tokenize('#a (a # \'asf s:"')
    [('#a', (0, 2)), ('(a', (3, 5)), ('#', (6, 7)), ("'asf", (8, 12)), ('s:"', (13, 16))]
    >>> word_tokenize('#a (a # \'asf s:"', pycomment_start=lambda w: w == '#')
    [('#a', (0, 2)), ('(a', (3, 5))]
    >>> word_tokenize('# /** /* */a */ ', ccomment_start=lambda w: w == '/*', ccomment_end=lambda w: w == '*/')
    [('#', (0, 1)), ('/**', (2, 5))]
    '''
    
    if (ccomment_start is None) != (ccomment_end is None):
        raise Exception('(ccomment_start is None) != (ccomment_end is None)')
    
    lines_of_tokens = to_lines_of_tokens(src, word_pattern)
    if pycomment_start is not None:
        lines_of_tokens = remove_pycomment_from_lines_of_tokens(
            lines_of_tokens, pycomment_start)
    tokens = join_lists(lines_of_tokens)

    if ccomment_start is not None:
        tokens = remove_ccomment_from_tokens(tokens, ccomment_start, ccomment_end)

    assert type(tokens) == list
    return tokens


def to_lines_of_tokens(src, word_pattern = word_pattern):
    lines = []
    def get_token(m):
        assert m
        return m.group(), (m.start(), m.end())
    
    for line in src.splitlines(True):
        tokens = [get_token(m) for m in word_pattern.finditer(line)]
        lines.append(tokens)
    return lines

def remove_pycomment_from_lines_of_tokens(lines_of_tokens,
                                         comment_start = lambda w: w == '#'):

    def not_start(token):
        word = token[0]
        return not comment_start(word)
    ls = (itertools.takewhile(not_start, tokens) for tokens in lines_of_tokens)
    return ls

def join_lists(lists, mid = []):
    ilists = iter(lists)
    for first in ilists:
        ls = list(first)
        break
    else:
        return []

    for next_ls in ilists:
        ls.extend(mid)
        ls.extend(next_ls)
    return ls


def remove_ccomment_from_tokens(tokens,
                               comment_start = lambda w: w == '/*',
                               comment_end = lambda w: w == '*/'):
    
    ls = []
    in_comment = False
    for token in tokens:
        w = token[0]
        if in_comment:
            if comment_end(w):
                in_comment = not in_comment
        elif comment_start(w):
            in_comment = not in_comment
        elif comment_end(w):
            raise ValueError('unbalance multiline comment: free end delimiter')
        else:
            ls.append(token)
    if in_comment:
        raise ValueError('unbalance multiline comment: free start delimiter')
    return ls

            

nonspaces_pattern = re.compile(r'\S+')
nonspaces_pattern_with_sharp_line_comment = re.compile(r'\S+|(\s|^)#($|\s.*)')
def split_tokenize(src, pattern=nonspaces_pattern):
    tokens = []
    for m in pattern.finditer(src):
        assert m
        t = m.group(), (m.start(), m.end())
        tokens.append(t)

    return tokens


newline_spaces_word_pattern = re.compile(r'(\n|\s+|\S+)')
def newline_spaces_word_tokenize(src):
    # tokens
    token_or_empty_ls = newline_spaces_word_pattern.split(src)
    L = len(token_or_empty_ls)
    empty_ls = [token_or_empty_ls[i] for i in range(0, L, 2)]
    tokens = [token_or_empty_ls[i] for i in range(1, L, 2)]
    assert not any(empty_ls)
    assert all(tokens)


    # types
    def token2case(token):
        if not token[0].isspace():
            case = 'w'
        elif token[0] == '\n':
            assert len(token) == 1
            case = '\n'
        else:
            case = ' '
        return case
    types = [token2case(t) for t in tokens]

    # positions
    ends = itertools.accumulate(map(len, tokens))
    positions = [(end-len(tokens), end) for end, token in zip(ends, tokens)]
    assert all(src[begin:end] == token for (begin, end), token
               in zip(position, tokens))

    
    return tokens, types, positions
    











if __name__ == "__main__":
    import doctest
    doctest.testmod()
