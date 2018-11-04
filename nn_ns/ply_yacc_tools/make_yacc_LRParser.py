


__all__ = '''
    make_yacc_LRParser
    '''.split()

from .make_pseudo_yacc_module_obj import make_pseudo_yacc_module_obj
import  ply.yacc #.yacc
def make_yacc_LRParser(XXX_yacc__module_or_class_or_dict, **XXX_yacc_kwargs):
    x = XXX_yacc__module_or_class_or_dict
    XXX_pseudo_yacc_module = make_pseudo_yacc_module_obj(x)
    lrparser = ply.yacc.yacc(module=XXX_pseudo_yacc_module, **XXX_yacc_kwargs)
    return lrparser
