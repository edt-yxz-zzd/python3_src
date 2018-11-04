


__all__ = '''
    pythoncoded_rules2python_code_str_ex
    '''.split()

from collections import defaultdict, Counter
class Global:
    the_common_methods_str = """
    def _mayset(p, r):
        if r is None:
            # p[0] may be set internal
            # assume user set p[0] already
            # donot: "p[0] = None" here!!!
            pass
        else:
            p[0] = r


"""
    the_head_str = """
@let_be_all_staticmethod('p_')
class ???:
""" + the_common_methods_str

def pythoncoded_rules2python_code_str_ex(
    pythoncoded_rules
    , *
    , name2count : 'None|defaultdict'
    , the_input_parameter_name : 'e.g. "p"'
    , with_class_keyword : bool
    ):
    '''[(RuleName, [(RuleBody, [PythonLine])])] -> (head_str, tail_str, name2count)
pythoncoded_rules -> python_code_str
#RuleBody = [[name]]

see:
    .example
    .PLY_YACC_Helper_YaccRules

'''
    if name2count is None:
        name2count = defaultdict(int)
    if the_input_parameter_name is None:
        the_input_parameter_name = 'p'

    results = []
    for name, body in pythoncoded_rules:
        for rule_body, python_lines in body:
            #rule_body :: [[name]]
            #python_lines :: [str]
            count = name2count[name]
            name2count[name] += 1
            counted_name = f'{name}__codes_{count}'; del count
            namess = rule_body
            # name, namess, python_lines
            # counted_name

            rule_body_in_str = '\n    | '.join(
                ' '.join(names) for names in namess)
            _rule_body_in_str = ' | '.join(
                ' '.join(names) for names in namess)
            rule_str = f'{name} : {rule_body_in_str}'
            comment_str = f'{name} : {_rule_body_in_str}'
            del rule_body_in_str, _rule_body_in_str
            # name, namess, python_lines
            # counted_name
            # rule_str, comment_str


            common_name_idx_pairs = namess2common_name_idx_pairs(namess)
            sorted_idx_kw_pairs = sorted(
                (i+1, n) for n, i in common_name_idx_pairs)
            del common_name_idx_pairs, namess
            # name, python_lines
            # counted_name
            # rule_str, comment_str
            # sorted_idx_kw_pairs

            pure_kwargs_in_str = ''.join(f', {kw}' for _,kw in sorted_idx_kw_pairs)
            if pure_kwargs_in_str:
                pure_kwargs_in_str = ', *'+pure_kwargs_in_str
            python_lines_in_str = ('\n'+' '*4*2).join(python_lines)
            del python_lines
            # name
            # counted_name
            # rule_str, comment_str
            # sorted_idx_kw_pairs
            # pure_kwargs_in_str, python_lines_in_str



            indents = ' '*(4*4)
            fmt = ', {kw}={p}[{idx}]' # not f''
            fmt = f'\n{indents}{fmt}' # f''
            valued_kwargs_in_str = ''.join(
                fmt.format(idx=idx, kw=kw, p=the_input_parameter_name)
                for idx, kw in sorted_idx_kw_pairs
                )
            if valued_kwargs_in_str:
                valued_kwargs_in_str += f'\n{indents}'
            del fmt, indents, sorted_idx_kw_pairs
            # name
            # counted_name
            # rule_str, comment_str
            # pure_kwargs_in_str, python_lines_in_str
            # valued_kwargs_in_str

            one_result_str = f'''
    def p_{counted_name}({the_input_parameter_name}):
        # {comment_str}
        {rule_str!r}
        __class__._mayset({the_input_parameter_name}
            , __class__._p_{counted_name}({the_input_parameter_name}{valued_kwargs_in_str})
            )
    def _p_{counted_name}({the_input_parameter_name}{pure_kwargs_in_str}):
        {python_lines_in_str}
'''
            results.append(one_result_str)
        #results.append('\n')
    results_in_str = '\n'.join(results)

    head_str = Global.the_head_str if with_class_keyword else Global.the_common_methods_str
    tail_str = results_in_str
    return head_str, tail_str, name2count
def namess2common_name_idx_pairs(namess):
    name_idx_pairss = []
    for names in namess:
        a2idx = find_all_unique_elements_and_indices(names)
        name_idx_pairss.append(set(a2idx.items()))

    common_name_idx_pairs = name_idx_pairss[0].intersection(*name_idx_pairss[1:])
    return common_name_idx_pairs

def find_all_unique_elements_and_indices(iterable):
    # Iter a -> Map a idx
    a2idx = {}
    alls = set()
    for i,a in enumerate(iterable):
        if a in alls:
            a2idx.discard(a)
        else:
            alls.add(a)
            a2idx[a] = i
    #assert set(a2idx) == find_all_unique_elements(iterable)
    return a2idx
def find_all_unique_elements(iterable):
    c = Counter(iter(iterable))
    return {x for x, i in c if i==1}

