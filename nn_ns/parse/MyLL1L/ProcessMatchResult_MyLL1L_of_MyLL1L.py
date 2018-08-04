

from .tools_for_raw_id2infoID_MyLL1L import \
     toIDList, toIDBlock, toIDToken
from .tools_for_id2infoID_MyLL1L import fill_raw_id2info
from .MyLL1L_in_MyLL1L import mainID_MyLL1L_of_MyLL1L
from .ProcessMatchResult_MyLL1L import ProcessMatchResult_MyLL1L
from .parse_MyLL1L import Parser_MyLL1L
from .id2infoID_MyLL1L_of_MyLL1L import tIDDict_MyLL1L_of_MyLL1L


class ProcessMatchResult_MyLL1L_of_MyLL1L(ProcessMatchResult_MyLL1L):
    def __init__(self, tokens, pos2rc = None):
        super().__init__(tIDDict_MyLL1L_of_MyLL1L, tokens, pos2rc)
        return

    def to_tIDDict(self, match_result):
        raw_id2info = self.process(match_result)
        tIDDict, id2info = fill_raw_id2info(raw_id2info)
        return tIDDict
        
    def to_parser(self, mainID, match_result):
        tIDDict = self.to_tIDDict(match_result)
        assert (mainID,) in tIDDict
        return Parser_MyLL1L(mainID, tIDDict)

    
    def __raw_processed_match_result2raw_info_list(
        self, raw_processed_match_result):
        ns = raw_processed_match_result[-1]
        info_ls = ns.data
        assert type(info_ls) == list
        return info_ls

    def to_raw_id2info(self, match_result):
        return self.process(match_result)
    def to_raw_info_list(self, match_result):
        self._process(match_result)
        raw_info_list = \
                      self.__raw_processed_match_result2raw_info_list(
                          match_result)
        return raw_info_list

    @staticmethod
    def raw_id2info_to_string(raw_id2info):
        ls = []
        for top_id, raw_info in raw_id2info.items():
            k2x = '{!r}: {!s}'.format(top_id, raw_info.get_raw_init_repr())
            ls.append(k2x)
        s = '{{{}}}'.format(', '.join(ls))
        return s
    @staticmethod
    def raw_info_list2string(raw_info_list):
        s = '[{}]'.format(', '.join(
            raw_info.get_raw_init_repr() for raw_info in raw_info_list))
        return s
        
    def _pre_process(self, match_result):pass
    def _process_leaf(self, match_result):pass

    
    # match_result2raw_id2info
    def _get_result(self, match_result):
        raw_id2info = {}
        info_ls = \
                self.__raw_processed_match_result2raw_info_list(
                    match_result)

        
        for info in info_ls:
            k = info.ID
            if k in raw_id2info:
                raise ValueError('top ID: {!r} are duplicate'.format(k))
            assert k not in raw_id2info
            raw_id2info[k] = info
        return raw_id2info

            
    def _post_process(self, match_result):
        explain = self.explain
        e = self.explain(match_result)

        tID = e.tID
        ID, *rID = tID
        ns = e.ns
        case = e.define_type

        def has_data(ns):
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
                e.ns.data = cns.data
        elif case == 'Token':
            assert e.end - e.begin == 1
            t = self.tokens[e.begin]
            ns.data = t.value
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

        elif ID in {'token', mainID_MyLL1L_of_MyLL1L, 'name', 'n', 'id'}:
            assert not rID
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

def test_ProcessMatchResult_MyLL1L_of_MyLL1L():
    from .Parser_MyLL1L_of_MyLL1L import parser_MyLL1L_of_MyLL1L
    from .MyLL1L_in_MyLL1L import MyLL1L_in_MyLL1L
    
    _tokenize = parser_MyLL1L_of_MyLL1L.tokenize
    _parse = parser_MyLL1L_of_MyLL1L.parse_tokens

    tokens = _tokenize(MyLL1L_in_MyLL1L)
    _match_result = _parse(tokens)
    
    parser = ProcessMatchResult_MyLL1L_of_MyLL1L(tokens)\
             .to_parser(mainID_MyLL1L_of_MyLL1L, _match_result)
    match_result = parser.parse_tokens(tokens)

    _match_result = _parse(tokens)
    assert _match_result == match_result



if __name__ == '__main__':
    test_ProcessMatchResult_MyLL1L_of_MyLL1L()
