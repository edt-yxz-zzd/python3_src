
'''
max_init_length
3
------------------------------------------------------------
rule_name_ixsymbols_pairs
[('S', [(True, 'Main')]),
 ('Main', [(True, 'Ts1')]),
 ('Ts1', [(True, 'Ts0'), (False, 'a')]),
 ('Ts0', [(True, 'Ts1')]),
 ('Ts0', [])]
============================================================
============================================================
============================================================
rule_name2inits
{'Main': {('a',), ('a', 'a'), ('a', 'a', 'a')},
 'S': {('a',), ('a', 'a'), ('a', 'a', 'a')},
 'Ts0': {(), ('a',), ('a', 'a'), ('a', 'a', 'a')},
 'Ts1': {('a',), ('a', 'a'), ('a', 'a', 'a')}}
------------------------------------------------------------
alternative_name2initss
[[{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})],
 [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})],
 [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, {('a',)}, frozenset({()})],
 [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})],
 [frozenset({()})]]
'''
from .calc_CFG_inits__all_hashable__pairs import \
    calc_CFG_inits__all_hashable__pairs


def _assert(
        max_init_length, rule_name_ixsymbols_pairs
        , rule_name2inits, alternative_name2initss
        ):
    for naive in [False, True]:
        rule_name2inits, alternative_name2initss = \
            calc_CFG_inits__all_hashable__pairs(
                max_init_length
                ,rule_name_ixsymbols_pairs
                ,rule_name_fullmapping_is_sequence=False
                ,naive=naive
                )
        assert rule_name2inits == rule_name2inits
        assert alternative_name2initss == alternative_name2initss




def _t():
    max_init_length = 3
    rule_name2ixsymbolss_str =dict(
        S = 'Main'
        ,Main = 'Ts1'
        ,Ts1 = 'Ts0 a'
        ,Ts0 = 'Ts1 |'
        )
    def ixsymbolss_str2ixsymbolss(ixsymbolss_str):
        return [[(ixsymbol_str[0].isupper(), ixsymbol_str)
                    for ixsymbol_str in ixsymbols_str.split()
                ] for ixsymbols_str in ixsymbolss_str.split('|')
                ]
    rule_name_ixsymbols_pairs = [(k, ixsymbols)
        for k,s in rule_name2ixsymbolss_str.items()
        for ixsymbols in ixsymbolss_str2ixsymbolss(s)
        ]
    _s(max_init_length, rule_name_ixsymbols_pairs)

def _s(max_init_length, rule_name_ixsymbols_pairs):
    from pprint import pprint

    rule_name2inits, alternative_name2initss = calc_CFG_inits__all_hashable__pairs(
        max_init_length
        ,rule_name_ixsymbols_pairs
        ,rule_name_fullmapping_is_sequence=False
        ,naive=True
        )

    print('max_init_length')
    pprint(max_init_length)
    print('-'*60)
    print('rule_name_ixsymbols_pairs')
    pprint(rule_name_ixsymbols_pairs)
    if 0:
        print('alternative_name2rule_name')
        pprint(alternative_name2rule_name)
        print('-'*60)
        print('alternative_name2ixsymbols')
        pprint(alternative_name2ixsymbols)
    print('='*60)
    print('='*60)
    print('='*60)
    print('rule_name2inits')
    pprint(rule_name2inits)
    print('-'*60)
    print('alternative_name2initss')
    pprint(alternative_name2initss)
    return





###############################################
_t()
_assert(
    max_init_length = 3
    ,rule_name_ixsymbols_pairs =
        [('S', [(True, 'Main')]),
         ('Main', [(True, 'Ts1')]),
         ('Ts1', [(True, 'Ts0'), (False, 'a')]),
         ('Ts0', [(True, 'Ts1')]),
         ('Ts0', [])]
    ,rule_name2inits =
        {'Main': {('a',), ('a', 'a'), ('a', 'a', 'a')},
         'S': {('a',), ('a', 'a'), ('a', 'a', 'a')},
         'Ts0': {(), ('a',), ('a', 'a'), ('a', 'a', 'a')},
         'Ts1': {('a',), ('a', 'a'), ('a', 'a', 'a')}}
    ,alternative_name2initss =
        [[{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})],
         [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})],
         [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, {('a',)}, frozenset({()})],
         [{('a', 'a'), ('a', 'a', 'a'), ('a',)}, frozenset({()})],
         [frozenset({()})]]
    )

