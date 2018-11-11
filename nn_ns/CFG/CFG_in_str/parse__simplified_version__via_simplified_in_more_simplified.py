
__all__ = '''
    parse__simplified_version__via_simplified_in_more_simplified
    basic_parse__simplified_version__via_simplified_in_more_simplified
    CFG_data__simplified_in_more_simplified
    '''.split()


#from ..errors import ParseFailError

if True:
    #used in make_CFG__simplified_in_more_simplified only
    from .concrete_CFG_syntax import simplified_in_more_simplified
    from ..the_py_terminal_set_ops import the_py_terminal_set_ops
    from .parse__more_simplified_version__ver2 import \
        parse__more_simplified_version__ver2
if True:
    #used in CFG_data__simplified_in_more_simplified only
    from .filters__simplified_in_more_simplified import (
        Filters__simplified_in_more_simplified as _Filters
        )
if True:
    #used in basic_parse__simplified_version__via_simplified_in_more_simplified only
    from .tokenize__simplified_version import \
        iter_tokenize__simplified_version
    from .post_parse import post_parse
if True:
    #used in parse__simplified_version__via_simplified_in_more_simplified only
    from .make_CFG import make_CFG_ex

if True:
    #used in _t2 only
    from .concrete_CFG_syntax import simplified_concrete_CFG_syntax
if True:
    #used in _forTest/_t/_t2 only
    from ..the_py_terminal_set_ops__with_any import (
        TheAnySet
        ,the_py_terminal_set_ops__with_any
        )
    from ..Parser.mk_cached_find_terminal_set_idc import mk_cached_find_terminal_set_idc


def make_CFG__simplified_in_more_simplified():
    # the_py_terminal_set_ops
    # parse__more_simplified_version__ver2
    terminal_set_name2terminal_set=lambda a:{a}
    start_nonterminal_names={'CFG'}

    (cfg, production_name2production
    , filter_names, filter_ex_names
    , start_nonterminal_idc, ambiguous_nonterminal_idc
    ) = r = parse__more_simplified_version__ver2(
            simplified_in_more_simplified
            ,terminal_set_ops=the_py_terminal_set_ops
            ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
            ,start_nonterminal_names=start_nonterminal_names
            ,ambiguous_nonterminal_names=()
            ,maybedead_nonterminal_names=()
            )
    assert start_nonterminal_idc
    return r

class CFG_data__simplified_in_more_simplified:
    (cfg, production_name2production
    , filter_names, filter_ex_names
    , start_nonterminal_idc, ambiguous_nonterminal_idc
    ) = make_CFG__simplified_in_more_simplified()


    token2terminal_name=lambda token:token.terminal
    token2value = lambda token: token.substring
    filter_name2func = _Filters.filter_name2func
    filter_ex_name2func = _Filters.filter_ex_name2func

    def _find_terminal_set_idc(
        terminal_set_idx2terminal_set, terminal_name
        ):
        return [terminal_set_idx2terminal_set.index({terminal_name})]

    find_terminal_set_idc = mk_cached_find_terminal_set_idc(cfg, _find_terminal_set_idc)
    del _find_terminal_set_idc


def parse__simplified_version__via_simplified_in_more_simplified(
    source_or_tokens, *
    ,tokens_directly=False
    ,terminal_set_ops
    ,terminal_set_name2terminal_set
    #,_parse_CFG_kwargs=None
    ):
    (productions
    , terminal_set_names
    , start_nonterminal_names
    , ambiguous_nonterminal_names
    , maybedead_nonterminal_names
    ) = basic_parse__simplified_version__via_simplified_in_more_simplified(
        source_or_tokens, tokens_directly=tokens_directly
        #,_parse_CFG_kwargs=_parse_CFG_kwargs
        )

    (cfg, production_name2production
    , filter_names, filter_ex_names
    , start_nonterminal_idc, ambiguous_nonterminal_idc
    ) = r = make_CFG_ex(
        productions=productions
        ,terminal_set_names=terminal_set_names
        ,start_nonterminal_names=start_nonterminal_names
        ,ambiguous_nonterminal_names=ambiguous_nonterminal_names
        ,maybedead_nonterminal_names=maybedead_nonterminal_names

        ,terminal_set_ops=terminal_set_ops
        ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
        )
    return r
def basic_parse__simplified_version__via_simplified_in_more_simplified(
    source_or_tokens, *, tokens_directly=False
    #, _parse_CFG_kwargs=None
    ):
    '''
input:
    source_or_tokens :: str | [Token]
        source in simplified_version
        or Token<simplified_version>
    tokens_directly :: bool
output:
    productions
    terminal_set_names
    start_nonterminal_names
    ambiguous_nonterminal_names
    maybedead_nonterminal_names
'''
    if tokens_directly:
        tokens = source_or_tokens
    else:
        source = source_or_tokens
        tokens = iter_tokenize__simplified_version(source)
    tokens = iter(tokens)

    Global = CFG_data__simplified_in_more_simplified

    value = post_parse(tokens
        , start_nonterminal_idc=Global.start_nonterminal_idc
        , token2terminal_name=Global.token2terminal_name
        , find_terminal_set_idc=Global.find_terminal_set_idc
        , ambiguous_nonterminal_idc=Global.ambiguous_nonterminal_idc

        , cfg=Global.cfg
        , production_name2production=Global.production_name2production

        , token2value=Global.token2value
        , filter_name2func=Global.filter_name2func
        , filter_ex_name2func=Global.filter_ex_name2func
        #, _parse_CFG_kwargs=_parse_CFG_kwargs
        )

    (productions
    , terminal_set_names
    , start_nonterminal_names
    , ambiguous_nonterminal_names
    , maybedead_nonterminal_names
    ) = value
    return value


class _forTest:
    # assume terminal_set_name is terminal_name
    #outdated:terminal_set_ops = the_py_terminal_set_ops
    #outdated:terminal_set_name2terminal_set=lambda a:{a}
    #outdated:find_terminal_set_idc=lambda ls, t: [ls.index({t})]
    #since now we have @none@ @any@
    terminal_set_ops = the_py_terminal_set_ops__with_any
    def terminal_set_name2terminal_set(terminal_set_name):
        if terminal_set_name == '@none@':
            return {}
        elif terminal_set_name == '@any@':
            return TheAnySet
        else:
            # assume terminal_set_name is terminal_name
            terminal_name = terminal_set_name
            return {terminal_name}

    def _find_terminal_set_idc(
        terminal_set_idx2terminal_set, terminal_name
        ):
        if terminal_name == '@none@':
            return []

        idc = [terminal_set_idx2terminal_set.index(TheAnySet)]
        if terminal_name == '@any@':
            pass
        else:
            # assume terminal_set_name is terminal_name
            terminal_set = {terminal_name}
            idx = terminal_set_idx2terminal_set.index(terminal_set)
            idc.append(idx)
            idc.sort()
        return idc

    @staticmethod
    def cfg2find_terminal_set_idc(cfg, *, find_terminal_set_idc=_find_terminal_set_idc):
        return mk_cached_find_terminal_set_idc(cfg, find_terminal_set_idc)
    del _find_terminal_set_idc


def _t2():
    #from ..debug_tools.position2lineno_columnno import show_splited_text_at
    #show_splited_text_at(simplified_concrete_CFG_syntax, 5145)

    example = simplified_concrete_CFG_syntax
    #terminal_set_ops = the_py_terminal_set_ops
    #terminal_set_name2terminal_set=lambda a:{a}
    terminal_set_ops = _forTest.terminal_set_ops
    terminal_set_name2terminal_set = _forTest.terminal_set_name2terminal_set

    (cfg, production_name2production
    , filter_names, filter_ex_names
    , start_nonterminal_idc, ambiguous_nonterminal_idc
    ) = r = parse__simplified_version__via_simplified_in_more_simplified(
        example
        ,terminal_set_ops=terminal_set_ops
        ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
        #,_show_dynamic_sizes_of_MessageClosureExecutor=True
        )
    print('_t2() finished!!!!!')
    for x in r: print(x)

    find_terminal_set_idc = _forTest.cfg2find_terminal_set_idc(cfg)

def _t():
    example = r'''
    ; @start_nonterminal@
        S
    ; @terminal_set@
        t
    ; S = +t+ @none@*
    '''
    terminal_set_ops = _forTest.terminal_set_ops
    terminal_set_name2terminal_set = _forTest.terminal_set_name2terminal_set


    (cfg, production_name2production
    , filter_names, filter_ex_names
    , start_nonterminal_idc, ambiguous_nonterminal_idc
    ) = r = parse__simplified_version__via_simplified_in_more_simplified(
        example
        ,terminal_set_ops=terminal_set_ops
        ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
        )
    for x in r: print(x)

    find_terminal_set_idc = _forTest.cfg2find_terminal_set_idc(cfg)
    tokens = 't'*6
    token2terminal_name=lambda t:t
    token2value = lambda t: 'o'
    filter_name2func = _Filters.result_cfg_internal_filter_name2func
    filter_ex_name2func = _Filters.result_cfg_internal_filter_ex_name2func

    value = post_parse(tokens
        , start_nonterminal_idc=start_nonterminal_idc
        , token2terminal_name=token2terminal_name
        , find_terminal_set_idc=find_terminal_set_idc
        , ambiguous_nonterminal_idc=ambiguous_nonterminal_idc

        , cfg=cfg
        , production_name2production=production_name2production

        , token2value=token2value
        , filter_name2func=filter_name2func
        , filter_ex_name2func=filter_ex_name2func
        )

    print(value)
    assert value == ['o', 'o', 'o', 'o', 'o', 'o']


if __name__ == "__main__":
    _t()
    _t2()

