
'''

lazy module
    what?
        toplevel entity in lazy module will be evaluated on need.
    why?
        define toplevel entities in arbitrary order
        break circular dependency if possible.
        importing module be faster

    how?
        importing a lazy module will parse the module,
            but would not excute its statements.
        each toplevel entity should have no more than one definition.
            toplevel entities include entities in import statements.
            forbid star import statements inside lazy module.
            forbid toplevel for/while
            if-else; else-except; count one position
        from __lazy__.XXX import xxx
        from .__lazy__.XXX import xxx

        def __missing__(lazy_module, name):
            r = lazy_module.globals()[name] = eval(lazy_module.ast[name])
            return r



'''

from collections import defaultdict
def ast_stmts2lazydict(ast_stmts):
    



