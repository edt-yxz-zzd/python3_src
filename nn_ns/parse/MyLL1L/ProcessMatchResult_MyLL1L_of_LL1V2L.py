

from .IDInfoLL1V2L import *
from .LL1V2L_in_MyLL1L import mainID_MyLL1L_of_LL1V2L


from .ProcessMatchResult_MyLL1L import ProcessMatchResult_MyLL1L
from .parse_MyLL1L import Parser_MyLL1L


class ProcessMatchResult_MyLL1L_to_gen_IDInfo_of_LL1V2L(ProcessMatchResult_MyLL1L):
    def __init__(self, tIDDict_MyLL1L_of_LL1V2L, tokens, pos2rc = None):
        super().__init__(tIDDict_MyLL1L_of_LL1V2L, tokens, pos2rc)
        return

    def to_IDInfo_of_LL1V2L(self, match_result):
        filter_actions, defs = self.process(match_result)
        info = IDInfo_top_layer(filter_actions, defs)
        return info
        

        
    def _pre_process(self, match_result):pass
    def _process_leaf(self, match_result):pass

    
    def _get_result(self, match_result):
        ns = match_result[-1]
        #print(match_result[:2])
        filter_actions, defs = ns.data

        return filter_actions, defs

            
    def _post_process(self, match_result):
        explain = self.explain
        e = self.explain(match_result)

        tID = e.tID
        ID, *rID = tID
        ns = e.ns
        case = e.define_type
        #print(tID, case)

        def has_data(ns):
            if not 'data' in ns.__dict__:
                print(e[0].tID)
                print(tID)
            
            return True
            return 'data' in ns.__dict__
        if isinstance(e.ID, int):
            data = e.ns.data = []
            for c in e:
                cns = explain(c).ns
                if has_data(cns):
                    data.append(cns.data)
        elif case == 'Block':
            c, = e
            cns = explain(c).ns
            if has_data(cns):
                ns.data = cns.data
                
        elif case == 'Token':
            assert e.end - e.begin == 1
            t = self.tokens[e.begin]
            ns.data = t.value
            if ID == 'count':
                assert rID
                ID, = rID
                if ID == "'*'": ns.data = (0, float('inf'))
                elif ID == "'+'": ns.data = (1, float('inf'))
                elif ID == "'?'": ns.data = (0, 1)
                else: raise
                
        elif ID == 'num':
            s, = e[0].ns.data
            ns.data = eval(s)

            
        elif ID == 'block':
            actions, defs = e[0].ns.data, e[1].ns.data
            ns.data = actions, defs
        
        elif ID == 'count':
            assert rID
            ID, = rID
            assert ID == "'{}'"
            m, = e[1].ns.data
            M = e[3].ns.data
            if M: M, = M
            else: M = float('inf')
            ns.data = (m, M)
            #print(ns.data)
        elif ID == "', ='":
            assert not rID
            unpack = bool(e[0].ns.data)
            ns.data = unpack
            #print(ns.data)
            
        elif ID == 'names':
            assert not rID
            names = e[0].ns.data
            names.extend(e[1].ns.data)
            ns.data = names
            #print(ns.data)
            
        elif ID == ',name':
            assert not rID
            name, = e[1].ns.data
            ns.data = name
            #print(ns.data)
            
            
        elif ID.endswith('_names}'):
            ID, = rID
            if ID.endswith('_names'):
                ns.data, = e[1].ns.data
            else:
                ns.data, = e[0].ns.data
                
            #print(ns.data)
        elif ID == 'action':
            assert not rID
            what_fix , object_names , action_names , method_names = \
                e[0].ns.data[0], e[1].ns.data[0], e[2].ns.data[0], e[3].ns.data[0]
            
            ns.data = what_fix , object_names , action_names , method_names
            #print(ns.data)
        elif ID == r'filter_action\n':
            ns.data, = e[0].ns.data
        elif ID == r'assign_action\n':
            ns.data, = e[0].ns.data
        elif ID == 'item_count':
            assert not rID
            unpack, refID, count = \
                e[0].ns.data, e[1].ns.data[0], e[2].ns.data
            if not count:
                count = (1,1)
            else:
                count, = count
            ns.data = bool(unpack), refID, count
        elif ID == r'tagged_item':
            tags = e[0].ns.data
            item_count, = e[1].ns.data
            unpack, item, count = item_count
            ns.data = tags, unpack, item, count
        elif ID == r'item_def':
            tagged_item , item_actions = e[0].ns.data[0], e[1].ns.data
            tags, unpack, item, count = tagged_item
            ns.data = tags, unpack, item, count, item_actions
        elif ID == 'list':
            assert not rID
            ns.data = e[0].ns.data
        elif ID == 'assign_body':
            assert not rID
            ns.data = e[1].ns.data
        elif ID == 'filter_body':
            assert not rID
            ns.data, = e[1].ns.data
        elif ID == 'token':
            assert not rID
            token_type , token_value = e[0].ns.data[0], e[1].ns.data
            if len(token_value) == 0:
                token_value = None
            else:
                token_value, = token_value
            ns.data = token_type , token_value
        elif ID == 'def_body':
            ID, = rID
            typ = ID[:-4]
            #print(typ)
            ns.data = [typ]
            if ID == 'assign_def':
                unpack, ls, acts = e[0].ns.data[0], e[1].ns.data[0], e[3].ns.data
                if acts:
                    acts, = acts
                r = (unpack, ls, acts)
            elif ID == 'filter_def':
                r, = e[1].ns.data
            elif ID == 'token_def':
                r, = e[1].ns.data
            else:
                raise
            #print(r)
            ns.data.extend(r)
        elif ID == 'def':
            assert not rID
            ns.data = e[0].ns.data
            ns.data.extend(e[1].ns.data[0])
            #print(ns.data)
        elif ID == 'top_layer':
            ns.data, = e[0].ns.data
            #print(len(ns.data))
        elif ID in {mainID_MyLL1L_of_LL1V2L, 'name', 'refID', \
                    'method_names', 'action_names', 'object_names', \
                    'method_name', 'action_name', 'object_name', \
                    'filter_action', 'assign_action', 'item_action',\
                    'token_type', 'token_value', 'num', 'id', 'attr', \
                    'value', 'string', 'concept_id'}:
            assert not rID
            #print(e.r[:2])
            ns.data, = e[0].ns.data


top_layer_block = filter_action\n * , top_layer_def +
top_layer_def
    object_def = top_layer_id , def_body
    concept_def = 'concept' , top_layer_id , newline
top_layer_id = concept_id , base_concept_decl ?
base_concept_decl = ':' , concept_id +

token = token_type , {token_value} ?

token_type = BTOKEN                         # t'xx'
{token_value} = '{' , attr:value, + , '}'
attr:value, = attr , ':' , value , ','      # ends with ','
action = ?fix , {object_names}{action_names} ? , method_name +

{object_names}{action_names} = {names} { 2 , 2 }
{names} = '{' , name + , '}'


refID = id , .id *
.id = '.' , id



        

#def lang_text2raw_id2info():

def test_ProcessMatchResult_MyLL1L_to_gen_IDInfo_of_LL1V2L():
    from .parser_MyLL1L_of_LL1V2L import parser_MyLL1L_of_LL1V2L as p
    #from .LL1V2L_in_LL1V2L import LL1V2L_in_LL1V2L as text_in_LL1V2L
    from .TryL_in_LL1V2L import TryL_in_LL1V2L as text_in_LL1V2L
    tokens = p.tokenize(text_in_LL1V2L)
    _match_result = p.parse_tokens(tokens)
    
    IDInfo = ProcessMatchResult_MyLL1L_to_gen_IDInfo_of_LL1V2L(p.tIDDict, tokens)\
             .to_IDInfo_of_LL1V2L(_match_result)
    info = eval(str(IDInfo))
    assert str(info) == str(IDInfo)



if __name__ == '__main__':
    test_ProcessMatchResult_MyLL1L_to_gen_IDInfo_of_LL1V2L()
