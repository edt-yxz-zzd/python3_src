
'''
input other language descripted in MyLL1 language
output parser of other language
'''

from MyLL1_init_raw_id2info import gen_MyLL1_raw_id2info
from MyLL1parse import parse
from MyLL1tokenize import tokenize
from MyLL1fill_raw_id2info import fill_raw_id2info
from MyLL1ProcessMatchResult import ProcessMatchResult


MyLL1_raw_id2info = gen_MyLL1_raw_id2info()
MyLL1_tIDDict, MyLL1_id2info = fill_raw_id2info(MyLL1_raw_id2info)
del MyLL1_raw_id2info

MyLL1_main = MyLL1_id2info['MyLL1']


def _to_parser(lang_text, mainID):
    tokens = tokenize(lang_text)
    match_result = parse(tokens, MyLL1_main)

    raw_id2info = ProcessMatchResult(MyLL1_tIDDict, tokens)\
                  .match_result2raw_id2info(match_result)
    
    tIDDict, id2info = fill_raw_id2info(raw_id2info)
    info_main = id2info[mainID]
    return tIDDict, id2info, info_main

class Parser:
    def __init__(self, lang_text, mainID):
        self.tIDDict, self.id2info, self.info_main = _to_parser(lang_text, mainID)
    def parse(self, source_tokens): # user should do the tokenization self.
        return parse(source_tokens, self.info_main)




eval_lang = r'''
# + - * / () call - ,
atom
    group = '(' , expr , ')'
    idnum
        id is t'id'
        num is t'num'

# highest : call
calls = atom , args *
args = '(' , args_tail
args_tail
    withargs = expr , ,expr * , ')'
    noargs = ')'
,expr = ',' , expr

-calls = - * , calls
*/list = calls , */item *
*/item = */ , -calls
-*/list = - * , */list

+-list = -*/list , +-item *
+-item = +- , -*/list

expr = +-list


+-
    '+' is t'+'
    '-' = -
- is t'-'
',' is t','
'(' is t'('
')' is t')'
*/ is t'*/'





'''
Parser(eval_lang, 'expr')
