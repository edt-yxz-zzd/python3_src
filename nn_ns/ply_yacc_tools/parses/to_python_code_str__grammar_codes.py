
__all__ = '''
    to_python_code_str__grammar_codes
    '''.split()


from .PutPythonCodeIntoGramma.pythoncoded_rules2python_code_str_ex import \
    pythoncoded_rules2python_code_str_ex

imports_str__grammar_codes = ''
def to_python_code_str__grammar_codes(
    parse_result__grammar_codes
    , the_input_parameter_name : 'e.g. "p"'
    ):
    pythoncoded_rules = parse_result__grammar_codes

    head_str, tail_str, name2count = pythoncoded_rules2python_code_str_ex(
        pythoncoded_rules
        , name2count = None
        , the_input_parameter_name = the_input_parameter_name
        , with_class_keyword = False
        )
    python_code_str__grammar_codes = head_str + tail_str

    return python_code_str__grammar_codes


