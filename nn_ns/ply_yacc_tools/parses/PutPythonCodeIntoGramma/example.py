
r'''
"""
Args
    arg comma Args | arg semicolon Args
        p[0] = put_before(p[1], p[3])
        # or: p[0] = put_before(arg, Args)
        # or: return put_before(arg, Args)
    empty
        pass
empty
    <>
        p[0] = LeftListEmpty
"""
parse(above_string
    , name2count : defaultdict
    , the_input_parameter_name='p'
    ) -> (head_str, tail_str, name2count)
==>>
"""
@let_be_all_staticmethod('p_')
class ???:
    def _mayset(p, r):
        if r is None:
            # p[0] may be set internal
            # assume user set p[0] already
            # donot: "p[0] = None" here!!!
            pass
        else:
            p[0] = r

    def p_Args_0(p):
        'Args : arg comma Args | arg semicolon Args'
        __class__._mayset(p, __class__._p_Args_0(p, arg=p[1], Args=p[3]))
    def _p_Args_0(p, *, arg, Args):
        p[0] = put_before(p[1], p[3])
        # or: p[0] = put_before(arg, Args)
        # or: return put_before(arg, Args)
    def p_Args_1(p):
        'Args : empty'
        __class__._mayset(p, __class__._p_Args_1(p, empty=p[1]))
    def _p_Args_1(p, *, empty):

    def p_empty_0(p):
        'empty :'
        __class__._mayset(p, __class__._p_Args_1(p))
    def _p_empty_0(p):
        p[0] = LeftListEmpty
"""
'''


example = __doc__.split('"""')[1]
assert example.startswith('\nArgs')


