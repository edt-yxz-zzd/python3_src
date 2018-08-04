
    ## |  code(argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,
    ## |        constants, names, varnames, filename, name, firstlineno,
    ## |        lnotab[, freevars[, cellvars]])
    # codestring is co_code!!


from .show_excepts import *

STAR_ARGS_FLAG = 0x4
STAR_KWDS_FLAG = 0x8
def code2vars(code):
    return {name : getattr(code, name) for name in dir(code) if name.startswith('co_')}


_pred = lambda name: name.startswith('co_')
code2vars = Obj2Vars(_pred)
show_code = ShowExcepts(code2vars.pred, [])



