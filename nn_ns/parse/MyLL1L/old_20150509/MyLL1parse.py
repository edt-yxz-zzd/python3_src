
from MyLL1InfoID import getMatchResultRng, MatchFail
from MyLL1fill_raw_id2info import fill_raw_id2info

'''
from MyLL1_init_raw_id2info import gen_MyLL1_raw_id2info

MyLL1_raw_id2info = gen_MyLL1_raw_id2info()
MyLL1_tIDDict, MyLL1_id2info = fill_raw_id2info(MyLL1_raw_id2info)
del MyLL1_raw_id2info

def parse_MyLL1lang(lang_text):'''

def parse(tokens, info):
    match_result = info.match(tokens, 0, len(tokens))
    begin, end = getMatchResultRng(match_result)
    if end != len(tokens):
        raise MatchFail('match end at pos {}. token:{}'.format(end, tokens[end]))

    return match_result


#tokens, match_result = parse(lang_MyLL1, id2info['MyLL1'])


def test_parse(raw_id2info, tokens, mainID):
    result1_InfoDict = raw_id2info
    tIDDict, id2info = fill_raw_id2info(raw_id2info)
    match_result = parse(tokens, id2info[mainID])
    return tIDDict, id2info, match_result



if __name__ == '__main__':
    from MyLL1InfoID import lang_MyLL1
    from MyLL1_init_raw_id2info import gen_MyLL1_raw_id2info
    from MyLL1tokenize import tokenize
    
    tokens = tokenize(lang_MyLL1)
    MyLL1_raw_id2info = gen_MyLL1_raw_id2info()
    tIDDict, id2info, match_result = \
             test_parse(MyLL1_raw_id2info, tokens, 'MyLL1')

