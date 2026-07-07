#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factorint6PARI_GP_.py

seed.math.factor_pint.factorint6PARI_GP_
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factorint6PARI_GP_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factorint6PARI_GP_:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers.py

echo 'factorint(???)' | gp -q
]]



'#'; __doc__ = r'#'
>>> factorint6PARI_GP_ = mk_factorint6PARI_GP__7fixed_timeout_(1)
>>> factorint6PARI_GP_(0)
Traceback (most recent call last):
    ...
ValueError: ('not positive integer:', 0)
>>> factorint6PARI_GP_(-1)
Traceback (most recent call last):
    ...
ValueError: ('not positive integer:', -1)
>>> factorint6PARI_GP_(1)
{}
>>> factorint6PARI_GP_(2)
{2: 1}
>>> factorint6PARI_GP_(4)
{2: 2}
>>> factorint6PARI_GP_(6)
{2: 1, 3: 1}
>>> factorint6PARI_GP_(12)
{2: 2, 3: 1}
>>> factorint6PARI_GP_('(-1+2^67)')
{193707721: 1, 761838257287: 1}
>>> factorint6PARI_GP_('(-1+2^1207)')
Traceback (most recent call last):
    ...
TimeoutError: ('(-1+2^1207)', TimeoutExpired(['gp', '-q', '-f'], 1))

>>> factorint6PARI_GP_ = mk_factorint6PARI_GP__7fixed_timeout_(0)
>>> factorint6PARI_GP_(0)
Traceback (most recent call last):
    ...
TypeError: 0
>>> factorint6PARI_GP_(-1)
Traceback (most recent call last):
    ...
TypeError: -1
>>> factorint6PARI_GP_(1)
Traceback (most recent call last):
    ...
TimeoutError: 1




[[
py_adhoc_call   seed.math.factor_pint.factorint6PARI_GP_   @_raw_factorint6PARI_GP_ --timeout=1  =1
    'matrix(0,2)\n'
py_adhoc_call   seed.math.factor_pint.factorint6PARI_GP_   @_raw_factorint6PARI_GP_ --timeout=1  =2
    'Mat([2,1])\n'
    '\n[2 1]\n\n'
py_adhoc_call   seed.math.factor_pint.factorint6PARI_GP_   @_raw_factorint6PARI_GP_ --timeout=1  =-1
    'Mat([-1,1])\n'
    '\n[-1 1]\n\n'
py_adhoc_call   seed.math.factor_pint.factorint6PARI_GP_   @_raw_factorint6PARI_GP_ --timeout=1  =0
    'Mat([0,1])\n'
    '\n[0 1]\n\n'
py_adhoc_call   seed.math.factor_pint.factorint6PARI_GP_   @_raw_factorint6PARI_GP_ --timeout=1  =12
    '\n[2 2]\n\n[3 1]\n\n'
py_adhoc_call   seed.math.factor_pint.factorint6PARI_GP_   @_raw_factorint6PARI_GP_ --timeout=1  :'(-1+2^1207)'
    ^subprocess.TimeoutExpired: Command '['gp', '-q', '-f']' timed out after 1 seconds
]]
[[
$ gp -q -f
? default('output,0)
? (factorint(1)~)
[;]
? (factorint(4)~)
[2;2]
? (factorint(12)~)
[2,3;2,1]
? (factorint(30)~)
[2,3,5;1,1,1]



]]



]]]'''#'''
__all__ = r'''
factorint6PARI_GP__7timeout_
    mk_factorint6PARI_GP__7fixed_timeout_

Fail__call_PARI_GP
StackOverflowError__PARI_GP

factor_pint__7timeout_eq0_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from subprocess import TimeoutExpired
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_int_ge
    from functools import partial
    from ast import literal_eval
    #view ../../python3_src/seed/exec/output_of_call.py
    from seed.exec.output_of_call import output_of_call_ex
    #def output_of_call_ex(args, *, stdin=None, input=None, shell=False, timeout=None, encoding=None, errors=None) -> (int, {bytes, str}):

    #view ../../python3_src/seed/lang/input7timeout.py
    #from seed.lang.input7timeout import input7timeout_
    #def input7timeout_(prompt, timeout, raise_if_timeout, default=None):

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

class Fail__call_PARI_GP(Exception):pass
class StackOverflowError__PARI_GP(Exception):pass

def factor_pint__7timeout_eq0_(u,/):
    check_int_ge(1, u)
    raise TimeoutError(u)
def mk_factorint6PARI_GP__7fixed_timeout_(timeout, /, **kwds):
    if not timeout >= 0:raise ValueError(timeout)
    if timeout == 0:
        return factor_pint__7timeout_eq0_
    assert timeout > 0
    return partial(factorint6PARI_GP__7timeout_, timeout=timeout, **kwds)
def factorint6PARI_GP__7timeout_(uint_or_str8expr6gp, /, *, timeout, TimeoutError=TimeoutError, parisizemax=1<<28):
    if not timeout >= 0:raise ValueError(timeout)
    if timeout == 0:
        raise TimeoutError(uint_or_str8expr6gp)
    assert timeout > 0
    try:
        str8output = _raw_factorint6PARI_GP_(uint_or_str8expr6gp, timeout=timeout, parisizemax=parisizemax)
    except TimeoutExpired as exc:
        if TimeoutError is None:
            raise
        #raise TimeoutError(uint_or_str8expr6gp, exc)
        #   TimeoutError: [Errno (-1+2^1207)] Command '['gp', '-q', '-f']' timed out after 1 seconds
        raise TimeoutError((uint_or_str8expr6gp, exc))
        #   TimeoutError: ('(-1+2^1207)', TimeoutExpired(['gp', '-q', '-f'], 1))
    str8output
    p2e = _parse_output__0(str8output)
    if p2e and min(p2e) < 2:raise ValueError('not positive integer:', uint_or_str8expr6gp)
    return p2e
def _parse_output__0(str8output, /):
    #for:default('output,0)
    s = s0 = str8output.strip()
    assert s
    p2e = {}
    if s.startswith('***'):
        #ss = s.split('\n')
        ss = s.split('\n=======')
        _s = ss[-1].strip()
        if not _s == '0':
            #if _s[0] in 'M[(' and _s[-1] in ')]':
            # '***   Warning: new maximum stack size = 268435456 (256.000 Mbytes).\n  *** factorint: Warning: increasing stack size to 16000000.\n\n=======\n[58451,1;88177,1;1767863,1;10063060897082377,1;260551495718621260054268273374657473120059796409,1]'
            r'''[[[
            ***   Warning: new maximum stack size = 268435456 (256.000 Mbytes).
            \n  *** factorint: Warning: increasing stack size to 16000000.
            \n
            \n=======
            \n[58451,1;88177,1;1767863,1;10063060897082377,1;260551495718621260054268273374657473120059796409,1]
            #]]]'''#'''
            s = _s;pass
        else:
            #"***   at top-level: ;factorint(u)\n  ***                  ^------------\n  *** factorint: the PARI stack overflows !\n  current stack size: 8000000 (7.629 Mbytes)\n  [hint] set 'parisizemax' to a nonzero value in your GPRC"
            r'''[[[
            ***   at top-level: ;factorint(u)
            \n  ***                  ^------------
            \n  *** factorint: the PARI stack overflows !
            \n  current stack size: 8000000 (7.629 Mbytes)
            \n  [hint] set 'parisizemax' to a nonzero value in your GPRC
            #]]]'''#'''
            raise StackOverflowError__PARI_GP([s0])
        #testing:raise StackOverflowError__PARI_GP([s0])
    ###########################
    #after:transpose:"~"
    ###########################
    # s == "[...;...]"
    assert s[0] == '[', (s0, s)
    assert s[-1] == ']', (s0, s)
    assert s.count(';') == 1, (s0, s)
    #s[1:-1].split(';')
    # [
    s = s.replace(';', '],[')
    # ]
    (ps, es) = literal_eval(s)
    assert len(ps) == len(es), (s0, s)
    p2e = dict(zip(ps, es))
    return p2e
    ###########################
    #before:transpose:"~"
    ###########################
    r'''[[[
    if s.startswith('matrix'):
        assert s == 'matrix(0,2)'
        p2e;pass
    else:
        if s.startswith('Mat'):
            # Mat([2,1])
            s = s[4:-1]
        assert s[0] == '[', (s0, s)
        assert s[-1] == ']', (s0, s)
        assert s.split() == [s]
        s = s.replace('[', '[(')
        s = s.replace(']', ')]')
        s = s.replace(';', '),(')
        p_e_pairs = literal_eval(s)
        p2e.update(p_e_pairs)
    return p2e
    #]]]'''#'''


def _parse_output__1(str8output, /):
    #for:default('output,1)
    raise 'bug'
    s = str8output.strip()
    assert s
    p2e = {}
    if s.startswith('matrix'):
        assert s == 'matrix(0,2)'
        p2e;pass
    else:
        ss = s.replace(' ', ',').split()
            #bug since alignment:
            #   '[  pp ep]\n[qqqq eq]'
            #   -->:
            #   '[,,pp,ep]\n[qqqq,eq]'
        for s8pair in ss:
            assert s8pair[0] == '['
            assert s8pair[-1] == ']'
            (p, e) = literal_eval(s8pair)
            p2e[p] = e
        p2e
    return p2e
def _raw_factorint6PARI_GP_(uint_or_str8expr6gp, /, *, timeout, parisizemax):
    assert parisizemax >= 0
    if 0:
        str8input = f'factorint({uint_or_str8expr6gp!s})'
    else:
        str8input = f'default(\'parisizemax,{parisizemax});\n;default(\'output,0);\n;f()={{{uint_or_str8expr6gp!s};}};\n;u=f();\n;m=0;m=(factorint(u)~);print();print("=======");m'
    str8input
    args = 'gp -q -f'.split()
    encoding = 'ascii'
    (code6exit, str8output) = output_of_call_ex(args, input=str8input, timeout=timeout, encoding=encoding)
    if 0 == code6exit:
        #ok
        return str8output
    raise Fail__call_PARI_GP(uint_or_str8expr6gp, str8input, code6exit, str8output)

__all__
from seed.math.factor_pint.factorint6PARI_GP_ import factorint6PARI_GP__7timeout_, mk_factorint6PARI_GP__7fixed_timeout_
from seed.math.factor_pint.factorint6PARI_GP_ import Fail__call_PARI_GP, StackOverflowError__PARI_GP
from seed.math.factor_pint.factorint6PARI_GP_ import *
