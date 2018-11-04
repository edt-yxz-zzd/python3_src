
from importlib import import_module
from pathlib import Path

def _main(parse__grammar_XXX__name__):
    # parse__grammar_XXX__name__ may be __main__!!!
    m_parse__grammar_XXX = import_module(parse__grammar_XXX__name__)
    parse__grammar_XXX_str = Path(m_parse__grammar_XXX.__file__).stem
    grammar_XXX_str = parse__grammar_XXX_str[len('parse__'):]
    _basic_main(m_parse__grammar_XXX, grammar_XXX_str)
def _basic_main(m_parse__grammar_XXX, grammar_XXX_str):
    # grammar_XXX_str = 'grammar_units' | ......
    # n_ - name
    # f_ - func
    # m_ - module
    #
    n_grammar_XXX = grammar_XXX_str
    parse__grammar_XXX_str = f'parse__{n_grammar_XXX}'

    f_parse__grammar_XXX = getattr(m_parse__grammar_XXX, parse__grammar_XXX_str)
    _grammar_XXX = getattr(m_parse__grammar_XXX, f'_{n_grammar_XXX}')

    tokens = m_parse__grammar_XXX.lex_postprocessor.tokenize(_grammar_XXX)
    for t in tokens:
        print(t)
        del t
    print()
    print()

    r = f_parse__grammar_XXX(_grammar_XXX)
    print(r)
    _grammar_XXX_parse_result = getattr(m_parse__grammar_XXX, f'_{n_grammar_XXX}_parse_result')
    assert r == _grammar_XXX_parse_result

    ####################
    #from .example__grammar_XXX import grammar_XXX
    m_example__grammar_XXX = import_module(
        f'.example__{n_grammar_XXX}', package=__package__)
    s_grammar_XXX = getattr(m_example__grammar_XXX, grammar_XXX_str)
    r = f_parse__grammar_XXX(s_grammar_XXX)
    print(r)

