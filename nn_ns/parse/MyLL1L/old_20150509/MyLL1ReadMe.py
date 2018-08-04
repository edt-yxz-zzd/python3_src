'''
my_LL1 = my_LL1_parse_method
MyLL1L = language_for_my_LL1
MyLL1LS = MyLL1L_specification # abstract concept, will be of type 'text'
MyLL1LS_in_MyLL1L # of type 'text', writing in language MyLL1L


<language_name>_specification
<language_short_name>S_in_MyLL1L = <language_name>_specification_in_MyLL1L

tokenize_for_MyLL1L :: xlanguage_specification_in_MyLL1L -> tokens_of_XLS_for_MyLL1L
parse_for_MyLL1L :: tokens_of_XLS_for_MyLL1L -> match_result_of_XLS_for_MyLL1L
processMatchResult_for_MyLL1L :: match_result_of_XLS_for_MyLL1L -> raw_id2info_of_XLS
make_parser_for_MyLL1L :: (raw_id2info_of_XLS, main_id_of_XLS) -> parser_for_XL
'''

'''
make_tokens
MyLL1tokenize

MyLL1InfoID
MyLL1_init_raw_id2info

MyLL1fill_raw_id2info
MyLL1parse
MyLL1ProcessMatchResult


MyLL1OtherLangParser # I can't offer tokenize !!! It is too complicate to make an general one
'''
