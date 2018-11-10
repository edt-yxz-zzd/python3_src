
'''
definition:
    see: concrete_CFG_syntax.more_simplified_concrete_CFG_syntax
'''

__all__ = '''
    basic_parse__more_simplified_version
    iter_tokenize__more_simplified_version
    '''.split()


from nn_ns.Tokenizer.ITokenizer import \
    TokenizerBaseError, TokenizerFailError
from nn_ns.Tokenizer.biregex.BiPatternABC__directly import \
    (BiPatternABC__directly
    ,BiPatternABC__directly__same
    )

from ..errors import ParseFailError
from .concrete_CFG_syntax import more_simplified_concrete_CFG_syntax
from .tokenize__simplified_version import (
    tokenize__simplified_version
    ,iter_tokenize__simplified_version
    )
from .abstract_syntax_datatype import (
    OP2
    ,FilteredRefName
    ,OP2_FilteredRefName
    ,Tuple
    )
from .Token import to_splited_source




biregex_dict = {}
class BiPatternHereSame(BiPatternABC__directly__same):
    biregex_dict = globals()['biregex_dict']

class terminal_set_name_decl(BiPatternHereSame):
    pattern_fmt = r'Tn*'
class op2_name(BiPatternHereSame):
    pattern_fmt = r'[-+]n'
class production(BiPatternHereSame):
    pattern_fmt = r'f*n:{op2_name}*'
class stmt(BiPatternHereSame):
    pattern_fmt = r';(?:{terminal_set_name_decl}|{production})'
class cfg(BiPatternHereSame):
    pattern_fmt = r'{stmt}*'
class good_prefix_on_fail(BiPatternHereSame):
    pattern_fmt = r'{cfg}(;f*(n(:[-+]?)?)?)?'
assert biregex_dict

terminal2superchar = dict(
    filter              = 'f'
    ,name                = 'n'
    ,kw_terminal_set     = 'T'
    ,op_semicolon        = ';'
    ,op_colon            = ':'
    ,op_discard          = '-'
    ,op_selected         = '+'
    )



def iter_tokenize__more_simplified_version(source):
    for token in iter_tokenize__simplified_version(source):
        terminal_name = token.terminal
        if terminal_name not in terminal2superchar:
            s = to_splited_source(token)
            raise TokenizerFailError(f'{terminal_name!r} is used in simplified version but not in more_simplified version. {token!r} \n{s!s}')
        yield token

def basic_parse__more_simplified_version(source):
    # -> ([Tuple], {name}, {name}, {name})
    # -> tuple_productions, terminal_set_names, nonterminal_names, undefined_xsymbol_names
    #
    [*tokens] = iter_tokenize__more_simplified_version(source)
    superstring = ''.join(terminal2superchar[t.terminal] for t in tokens)
    m = cfg.precise_regex.fullmatch(superstring)
    if not m:
        m = good_prefix_on_fail.precise_regex.match(superstring)
        if not m:
            print(superstring)
            raise logic-error --regex-error
        L = m.end()
        if L == len(superstring):
            raise ParseFailError('incomplete statement as EOF')
        bad_token = tokens[L]
        s = to_splited_source(bad_token)
        raise ParseFailError(f'bad token: {bad_token!r}; \n{s!s}')

    terminal_set_names = set()
    nonterminal_names = set()
    xsymbol_names = set()
    tuple_productions = []
    def iter_substring_between(begin, end):
        return (token.substring for token in tokens[begin:end])
    prev_end = 0
    for m in stmt.precise_regex.finditer(superstring):
        begin = m.start()
        end = m.end()
        assert begin == prev_end
        prev_end = end
        assert superstring[begin] == ';'
        if superstring[begin+1] == 'T':
            terminal_set_names.update(iter_substring_between(begin+2, end))
            continue

        def_name_pos = superstring.index('n', begin+1, end)
        assert superstring[begin+1:def_name_pos] == 'f'*(def_name_pos-1-begin)
        [*filter_names] = iter_substring_between(begin+1, def_name_pos)
        nonterminal_name = tokens[def_name_pos].substring

        assert superstring[def_name_pos+1] == ':'
        rhs_begin = def_name_pos+2
        assert (end - rhs_begin)&1 == 0

        op2_filtered_ref_names = []
        for i in range(rhs_begin, end, 2):
            op2 = tokens[i].substring
            xsymbol_name = tokens[i+1].substring

            # OP2 is bool
            if op2 == '-':
                op2 = False # OP2.OP_DISCARD
            elif op2 == '+':
                op2 = True # OP2.OP_SELECT
            else:
                raise logic-error
            #no filter in rhs
            filtered_ref_name = FilteredRefName([], xsymbol_name)
            op2_filtered_ref_names.append(
                OP2_FilteredRefName(op2, filtered_ref_name))
            xsymbol_names.add(xsymbol_name)
        tuple_productions.append(Tuple(
            filter_names, nonterminal_name, op2_filtered_ref_names))
        nonterminal_names.add(nonterminal_name)
    assert prev_end == len(superstring)

    both = nonterminal_names&terminal_set_names
    if both:
        raise ParseFailError(f'both nonterminal_names&terminal_set_names: {both}')
    undefined_xsymbol_names = xsymbol_names - nonterminal_names - terminal_set_names
    return (tuple_productions, terminal_set_names
            , nonterminal_names, undefined_xsymbol_names
            )





if __name__ == "__main__":
    r = basic_parse__more_simplified_version(more_simplified_concrete_CFG_syntax)
    (tuple_productions, terminal_set_names
    , nonterminal_names, undefined_xsymbol_names
    ) = r

    print(f'terminal_set_names={terminal_set_names}')
    print(f'tuple_productions={tuple_productions}')
    print(f'nonterminal_names={nonterminal_names}')
    print(f'undefined_xsymbol_names={undefined_xsymbol_names}')
    for tuple_production in tuple_productions:
        print(tuple_production)


