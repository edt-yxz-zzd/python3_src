
from MyLL1InfoID import MatchResultExplain
from MyLL1_init_raw_id2info import toIDList, toIDBlock, toIDToken
from MyLL1fill_raw_id2info import fill_raw_id2info


class ProcessMatchResult:
    def __init__(self, tIDDict, tokens):
        self.tIDDict, self.tokens = tIDDict, tokens
    def explain(self, match_result):
        return MatchResultExplain(match_result, self.tIDDict, self.tokens)

        
    def match_result2raw_id2info(self, match_result):
        self._process_match_result(match_result)
        raw_id2info = {}
        ns = match_result[-1]
        info_ls = ns.data
        for info in info_ls:
            k = info.ID
            assert k not in raw_id2info
            raw_id2info[k] = info
        return raw_id2info
            
    def _process_match_result(self, match_result):
        this_f = self._process_match_result
        explain = self.explain
        e = self.explain(match_result)
        if e.children != None:
            for c in e.children:
                this_f(c)
        tID = e.tID
        ID, *rID = tID
        ns = e.ns
        case = e.define_type
        def has_data(ns):
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
                e.ns.data = cns.data
        elif case == 'Token':
            assert e.end - e.begin == 1
            t = self.tokens[e.begin]
            ns.data = t.substring
            #print(ID, repr(ns.data))
        elif ID == 'inline_define':
            ID, = rID
            if ID == 'is_token':
                token_str, = e['type'].ns.data
                ns.data = lambda ID:toIDToken(ID, token_str)
            else:
                id_define_ls, = e['ls'].ns.data
                ns.data = lambda ID:toIDList(ID, *id_define_ls)
        elif tID == ('count', "'{}'"):
            min, = e['min'].ns.data
            if e['max'].ns.data:
                max, = e['max'].ns.data
                r = (min, max)
            else:
                r = (min,)
            ns.data = r
            #print(ns.data)
            
        elif ID == 'id_count':
            assert not rID
            _id, = e['id'].ns.data
            if e['count'].ns.data:
                count, = e['count'].ns.data
            else:
                count = ()
            ns.data = (_id, count)
            #print(ns.data)
            
        elif ID == 'item':
            assert not rID
            id_count, = e['id_count'].ns.data
            if e['name'].ns.data:
                name, = e['name'].ns.data
            else:
                name = None
            ns.data = (id_count, name)
            #print(ns.data)
            
        elif ID == ',item':
            assert not rID
            item, = e[1].ns.data
            ns.data = item
            #print(ns.data)
            
            
        elif ID == 'block':
            assert not rID
            id_define_block, = e[1].ns.data
            ns.data = lambda ID: toIDBlock(ID, *id_define_block)
            #print(ns.data)
        elif ID == 'list':
            assert not rID
            item0, = e[0].ns.data
            items = e[1].ns.data
            
            ns.data = [item0]
            ns.data.extend(items)
            #print(ns.data)
        elif ID == 'define':
            ID, = rID
            if ID == 'define_newline':
                ns.data, = e[0].ns.data
            else:
                ns.data, = e[1].ns.data
        elif ID == 'id_define':
            assert not rID
            _id, = e[0].ns.data
            define_f, = e[1].ns.data
            ns.data = define_f(_id)
            
##        elif ID == 'B':
##            assert e.end - e.begin == 1
##            t = self.tokens[e.begin]
##            ns.data = t.substring
##            print(ID, ns.data)
        elif ID in {'token', 'MyLL1', 'name', 'n', 'id'}:
            assert not rID
            if 1:#has_data(e[0].ns) and e[0].ns.data:
                ns.data, = e[0].ns.data
                if ID == 'n':
                    ns.data = int(ns.data)
                #print(ID, ns.data)
        elif ID in {'subrex', 'rex'}:
            assert not rID
            if not rID and has_data(e[0].ns):
                ns.data = e[0].ns.data
                #print(ID, ns.data)
        

#def lang_text2raw_id2info():

def test_ProcessMatchResult():
    from MyLL1_init_raw_id2info import gen_MyLL1_raw_id2info
    from MyLL1InfoID import lang_MyLL1
    from MyLL1parse import parse
    from MyLL1tokenize import tokenize
    
    tokens = tokenize(lang_MyLL1)
    
    MyLL1_raw_id2info = gen_MyLL1_raw_id2info()
    tIDDict, id2info = fill_raw_id2info(MyLL1_raw_id2info)
    match_result = parse(tokens, id2info['MyLL1'])
    del MyLL1_raw_id2info

    
    raw_id2info = ProcessMatchResult(tIDDict, tokens)\
                  .match_result2raw_id2info(match_result)

    _tIDDict, _id2info = fill_raw_id2info(raw_id2info)
    _match_result = parse(tokens, _id2info['MyLL1'])

    match_result = parse(tokens, id2info['MyLL1'])

    #ProcessMatchResult(_tIDDict, tokens).match_result2raw_id2info(_match_result)


    assert _match_result == match_result



if __name__ == '__main__':
    test_ProcessMatchResult()
