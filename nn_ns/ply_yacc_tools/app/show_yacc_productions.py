

r'''
pym -jq parse__grammar_units.py
pym show_yacc_productions.py M -m nn_ns.my_fileformat.configuration.utils.parses.parse__grammar_units -da .P

pym show_yacc_productions.py S -p nn_ns.my_fileformat.configuration.utils.parses -np parse__grammar_units@E:\my_data\program_source\github\edt-yxz-zzd\python3_src\nn_ns\my_fileformat\configuration\utils\parses\parse__grammar_units.py -da .P

'''

__all__ = '''
    show_extracted_yacc_rules

    extract_rules_from_yacc_productions
    extract_rules_from_yacc_lrparser
    extract_rules_from_lex_postprocessor_with_parser
    show_yacc_productions
    show_yacc_productions_from_yacc_lrparser
    show_yacc_productions_from_lex_postprocessor_with_parser
    '''.split()

from ..make_yacc_LRParser import make_yacc_LRParser
from ..LexPostprocessors.ILexPostprocessorWithParser import \
    ILexPostprocessorWithParser

from seed.pkg_tools.get_python_object import GetPythonObjectHelper
import ply.yacc
from collections import defaultdict

def show_extracted_yacc_rules(rules):
    '''rules :: [(name, [[name]])]

see: extract_rules_from_yacc_productions
'''
    for name, body in rules:
        print(name)
        op = ':'
        for names in body:
            line = ' '.join(names)
            print(f'    {op} {line}')
            op = '|'
    return

def extract_rules_from_yacc_productions(productions):
    '''[production] -> [rule]
[ply.yacc.MiniProduction] -> [(name, [[name]])]


productions :: [ply.yacc.MiniProduction]
rules :: [(name, [[name]])]

body :: [[name]]
rules = name_body_pairs
'''
    d = defaultdict(list)
    for production in productions:
        name = production.name
        name_, _names_ = production.str.split('->')
        names = _names_.split()
        d[name].append(names)
    rules = name_body_pairs = sorted(d.items())
    return rules
def extract_rules_from_yacc_lrparser(lrparser):
    '''ply.yacc.LRParser -> [(name, [[name]])]'''
    productions = lrparser.productions
    return extract_rules_from_yacc_productions(productions)
def extract_rules_from_lex_postprocessor_with_parser(
    lex_postprocessor_with_parser):
    '''LexPostprocessorWithParser -> [(name, [[name]])]'''
    lrparser = lex_postprocessor_with_parser.lrparser
    return extract_rules_from_yacc_lrparser(lrparser)

#############################################
def show_yacc_productions(productions):
    rules = extract_rules_from_yacc_productions(productions)
    show_extracted_yacc_rules(rules)
def show_yacc_productions_from_yacc_lrparser(lrparser):
    rules = extract_rules_from_yacc_lrparser(lrparser)
    show_extracted_yacc_rules(rules)
def show_yacc_productions_from_lex_postprocessor_with_parser(
    lex_postprocessor_with_parser):
    rules = extract_rules_from_lex_postprocessor_with_parser(lex_postprocessor_with_parser)
    show_extracted_yacc_rules(rules)

#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
#############################################
def main(argv=None):
    #seed.io.get_python_object.get_python_object/GetPythonObjectHelper
    '''
    ModuleSystem
        --module x.y.z --dot_attrs .XXX.YYY
    ScriptAsModule # to set the __name__
        --parent x.y [--name_with_path z@path/to/XXX.py]+ --dot_attrs .XXX.YYY

    #from file/stdin/arg
    Exec/Eval
        file
            --input_path path/to/XXX.py --encoding utf8] --dot_attrs .XXX.YYY
        stdin --dot_attrs .XXX.YYY
        arg --python_source --dot_attrs .XXX.YYY
'''
    import argparse
    parser_main = argparse.ArgumentParser(prog='show_yacc_productions')
    subparsers_main = parser_main.add_subparsers(
        dest='sub_command_name__level1'
        #, required=True
        , help='level1 sub-command help'
        )
    subparsers_main.required=True

    parser_ModuleSystem = subparsers_main.add_parser('ModuleSystem'
        , aliases='M'.split()
        , help='via ModuleSystem')
    parser_ScriptAsModule = subparsers_main.add_parser('ScriptAsModule'
        , aliases='S'.split()
        , help='via ScriptAsModule')
    parser_Exec = subparsers_main.add_parser('Exec'
        , aliases='X'.split()
        , help='via Exec')
    parser_Eval = subparsers_main.add_parser('Eval'
        , aliases='V'.split()
        , help='via Eval')

    init_parser_ModuleSystem(parser_ModuleSystem)
    init_parser_ScriptAsModule(parser_ScriptAsModule)
    init_parser_Exec_or_Eval(parser_Exec)
    init_parser_Exec_or_Eval(parser_Eval)
    #init_parser__dot_attrs(parser_main)




    ################
    args = parser_main.parse_args(argv)
    #dot_attrs = args.dot_attrs
    #cmd = parser_main.sub_command_name__level1 # the 'dest'

    x = the_object = args._handler_1_(args)
    if isinstance(x, ILexPostprocessorWithParser):
        rules = extract_rules_from_lex_postprocessor_with_parser(x)
    elif isinstance(x, ply.yacc.LRParser):
        rules = extract_rules_from_yacc_lrparser(x)
    else:
        #assume it is an module/class required by yacc
        lrparser = make_yacc_LRParser(x)
        rules = extract_rules_from_yacc_lrparser(lrparser)
    show_extracted_yacc_rules(rules)


def init_parser__level1(_handler_1_, parser_level1):
    init_parser__dot_attrs(parser_level1)
    init_parser__level1__without_dot_attrs(_handler_1_, parser_level1)
def init_parser__level1__without_dot_attrs(_handler_1_, parser_level1):
    parser_level1.set_defaults(_handler_1_=_handler_1_)
def init_parser__level2(_handler_2_, parser_level2):
    init_parser__dot_attrs(parser_level2)
    parser_level2.set_defaults(_handler_2_=_handler_2_)

def init_parser_ModuleSystem(parser_ModuleSystem):
    parser_ModuleSystem.add_argument('-m', '--module', type=str
        , required=True
        , help='module fullname; qname; x.y.z'
        )
    def _handler_1_(args):
        return GetPythonObjectHelper.ModuleSystem(
            module=args.module
            ,dot_attrs=args.dot_attrs
            )
    init_parser__level1(_handler_1_, parser_ModuleSystem)
def init_parser_ScriptAsModule(parser_ScriptAsModule):
    parser_ScriptAsModule.add_argument('-p', '--parent', type=str
        , required=True
        , help='normal package fullname; qname; x.y.z'
        )
    parser_ScriptAsModule.add_argument('-np', '--name_path_pairs'
        , type=str, action = 'append', default = []
        #not required#, required=True
        , help='bare module name with path to its source file; aaa@path/to/aaa.py'
        )
    def _handler_1_(args):
        return GetPythonObjectHelper.ScriptAsModule(
            parent=args.parent
            ,name_path_pair_strs= args.name_path_pairs
            ,dot_attrs=args.dot_attrs
            )
    init_parser__level1(_handler_1_, parser_ScriptAsModule)
def init_parser_Exec_or_Eval(parser_E):
    Exec_or_Eval = sub_command_name__level1 = parser_E.prog
    subparsers_E = parser_E.add_subparsers(
        dest='Exec_or_Eval_sub_command_name'
        , help='{Exec_or_Eval} sub-command help')

    parser_E_file = subparsers_E.add_parser('file'
        , aliases='f'.split()
        , help='from file')
    parser_E_stdin = subparsers_E.add_parser('stdin'
        , aliases='i'.split()
        , help='from stdin')
    parser_E_arg = subparsers_E.add_parser('arg'
        , aliases='a'.split()
        , help='from arg')

    init_parser_Exec_or_Eval_file(parser_E_file)
    init_parser_Exec_or_Eval_stdin(parser_E_stdin)
    init_parser_Exec_or_Eval_arg(parser_E_arg)
    def _handler_1_(args):
        Exec_or_Eval = args.sub_command_name__level1
        G = GetPythonObjectHelper
        E = G.Exec if Exec_or_Eval == 'Exec' else G.Eval
        return args._handler_2_(E, args)
        # well, we can set _handler_2_ to _handler_1_
    #not!!!: init_parser__level1(_handler_1_, parser_E)
    #   donot: init_parser__dot_attrs
    init_parser__level1__without_dot_attrs(_handler_1_, parser_E)

def init_parser_Exec_or_Eval_file(parser_E_file):
    parser_E_file.add_argument('-i', '--input_path', type=str
        , required=True
        , help='path to input file'
        )
    parser_E_file.add_argument('-e', '--encoding', type=str
        , required=True
        , help='encoding for input file'
        )
    def _handler_2_(E, args):
        return E.file(
            input_path=args.input_path
            ,encoding= args.encoding
            ,dot_attrs=args.dot_attrs
            )
    init_parser__level2(_handler_2_, parser_E_file)

def init_parser_Exec_or_Eval_stdin(parser_E_stdin):
    def _handler_2_(E, args):
        return E.stdin(
            dot_attrs=args.dot_attrs
            )
    init_parser__level2(_handler_2_, parser_E_stdin)
def init_parser_Exec_or_Eval_arg(parser_E_arg):
    parser_E_arg.add_argument('python_source', type=str
        #, required=True
        , help='python source code'
        )
    def _handler_2_(E, args):
        return E.stdin(
            python_source=args.python_source
            ,dot_attrs=args.dot_attrs
            )
    init_parser__level2(_handler_2_, parser_E_arg)


def init_parser__dot_attrs(parser):
    parser.add_argument('-da', '--dot_attrs', type=str
        , required=True
        , help='attrs to object; .XXX.YYY'
        )

if __name__ == "__main__":
    main()
