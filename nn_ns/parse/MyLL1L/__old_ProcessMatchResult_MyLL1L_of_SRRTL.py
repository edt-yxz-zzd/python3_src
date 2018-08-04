

from .tools_for_id2infoID_SRRTL import *
from .SRRTL_in_MyLL1L import mainID_MyLL1L_of_SRRTL
from .ProcessMatchResult_MyLL1L import ProcessMatchResult_MyLL1L
from .raw_tokenize_SRRTL import RawTokenizer_SRRTL
#from .id2infoID_MyLL1L_of_MyLL1L import tIDDict_MyLL1L_of_MyLL1L




class ProcessMatchResult_MyLL1L_of_SRRTL(ProcessMatchResult_MyLL1L):
    def __init__(self, tIDDict_MyLL1L_of_SRRTL, tokens, pos2rc = None):
        super().__init__(tIDDict_MyLL1L_of_SRRTL, tokens, pos2rc)
        return

    def to_id2infoID(self, match_result):
        info_ls = self.process(match_result)
        id2infoID = {info.ID : info for info in info_ls}
        return id2infoID
        
    def to_raw_tokenizer(self, mainID, match_result):
        id2infoID = self.to_id2infoID(match_result)
        assert mainID in id2infoID
        return RawTokenizer_SRRTL(mainID, id2infoID)
        
    def _pre_process(self, match_result):pass
    def _process_leaf(self, match_result):pass

    
    # match_result2raw_id2info
    def _get_result(self, match_result):
        raw_id2info = {}
        ns = match_result[-1]
        info_ls = ns.data
        return info_ls

            
    def _post_process(self, match_result):
        explain = self.explain
        e = self.explain(match_result)

        tID = e.tID
        ID, *rID = tID
        ns = e.ns
        case = e.define_type

        def has_data(ns):
            #return True
            r = 'data' in ns.__dict__
            if not r:
                print(ID, e.r[:2], ns.__dict__)
            return True
            return r
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
            if ID == 'string':
                ns.data = eval(ns.data)
                assert type(ns.data) == str
            elif ID == 'idstring':
                ns.data = eval(ns.data[2:])
                assert type(ns.data) == str
            elif tID == ('define', 'otherwise'):
                ns.data = None # rex anything
            elif ID == 'state_op':
                assert tID == ('state_op', 'return')
                ns.data = InfoReturn()
                
            #print(ID, repr(ns.data))
        elif ID == 'strings':
            ns.data = ''.join(e[0].ns.data)
        elif ID == 'name':
            ID, = rID
            assert ID == 'idstrings'
            ns.data = ''.join(e[0].ns.data)
            ns.data = repr(ns.data)
        elif ID == 'if_clause':
            assert not rID
            ns.data, = e[1].ns.data
        elif ID == 'state_op':
            ID, = rID
            #print(tID)
            if ID == 'goto':
                state_id, = e[1].ns.data
                ns.data = InfoGoto(state_id)
            elif ID == 'call':
                state_id, = e[1].ns.data
                ns.data = InfoCall(state_id)
            else:
                assert ID == 'error'
                err, = e[1].ns.data
                ns.data = InfoError(err)
        elif ID == 'define':
            ID, = rID
            assert ID == 'rex'
            rex, = e[0].ns.data
            ns.data = rex
            
        elif ID == 'define_body':
            ID, = rID
            if ID == 'normal_define':
                rex, = e[0].ns.data
                children_ls = e[2].ns.data
                if children_ls:
                    children, = children_ls
                else:
                    children = []
                ns.data = InfoNormalDefine(rex, children)
            else:
                assert ID == 'define_if_clause'
                rex_ls = e[0].ns.data
                rex = None
                if rex_ls: rex, = rex_ls
                
                state_op, = e[1].ns.data
                #print(state_op, rex)
                ns.data = InfoDefineIfClause(state_op, rex)
        elif ID == 'name_eq':
            assert not rID
            _id, = e[0].ns.data
            ns.data = _id
            #print(ns.data)
            
        elif ID == 'define_token_type':
            ID, = rID
            _id = None
            if ID == 'named_define':
                _id, = e[0].ns.data
            body, = e[-1].ns.data
            ns.data = InfoDefineTypeID(_id, body)

        elif ID == 'sub_define_block':
            assert not rID
            ns.data, = e[1].ns.data
            #print(ns.data)
        elif ID == 'define_state':
            assert not rID
            _id, = e[0].ns.data
            children, = e[2].ns.data
            
            ns.data = InfoDefineStateID(_id, children)
            #print(ns.data)

        elif ID in {'rex', 'state_id', 'type_id', 'id'}:
            assert not rID
            ns.data, = e[0].ns.data
            #print(ID, ns.data)
        elif ID in {mainID_MyLL1L_of_SRRTL, 'define_block'}:
            assert not rID
            ns.data = e[0].ns.data
            #print(ID, ns.data)
        

#def lang_text2raw_id2info():

def test_ProcessMatchResult_MyLL1L_of_SRRTL():
    from .parser_MyLL1L_of_SRRTL import parser_MyLL1L_of_SRRTL
    from .SRRTL_in_MyLL1L import SRRTL_in_MyLL1L, mainID_MyLL1L_of_SRRTL
    from .raw_tokenize_SRRTL import raw_tokenize_SRRTL
    from .id2infoID_SRRTL_of_SRRTL import id2infoID_SRRTL_of_SRRTL
    from .SRRTL_in_SRRTL import mainID_SRRTL_of_SRRTL, SRRTL_in_SRRTL
    raw_tokens = list(raw_tokenize_SRRTL(SRRTL_in_SRRTL, \
                    mainID_SRRTL_of_SRRTL, id2infoID_SRRTL_of_SRRTL))



    _tokenize = parser_MyLL1L_of_SRRTL.tokenize
    _parse = parser_MyLL1L_of_SRRTL.parse_tokens
    tIDDict = parser_MyLL1L_of_SRRTL.tIDDict

    tokens = _tokenize(SRRTL_in_SRRTL)
    _match_result = _parse(tokens)
    
    raw_tokenizer = ProcessMatchResult_MyLL1L_of_SRRTL(tIDDict, tokens)\
                    .to_raw_tokenizer(mainID_SRRTL_of_SRRTL, _match_result)

    _raw_tokens = list(raw_tokenizer.raw_tokenize(SRRTL_in_SRRTL))

    if not _raw_tokens == raw_tokens:
        assert repr(_raw_tokens) == repr(raw_tokens)
        print(_raw_tokens)
        print(raw_tokens)
    assert _raw_tokens == raw_tokens



if __name__ == '__main__':
    test_ProcessMatchResult_MyLL1L_of_SRRTL()
