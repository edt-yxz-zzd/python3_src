


from .parse_EPL import parse_EPL
from .parse_result2EPL import parse_result2indent_EPL




def pretty_format_EPL(src):
    r = parse_EPL(src)
    pretty_src = parse_result2indent_EPL(r)
    assert r == parse_EPL(pretty_src)
    return pretty_src


if True:
    from .EPL_in_MyLL1L import example_EPL
    for src, ans in example_EPL: pretty_format_EPL(src)
