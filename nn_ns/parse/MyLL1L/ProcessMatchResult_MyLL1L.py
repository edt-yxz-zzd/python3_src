from .ProcessParseResult import ProcessMatchResult
from .MatchResultExplain_MyLL1L import MatchResultExplain_MyLL1L

class ProcessMatchResult_MyLL1L(ProcessMatchResult):
    # tIDDict : Parser_MyLL1L_of_XL(...).tIDDict
    def __init__(self, tIDDict, tokens, pos2rc = None):
        self.tIDDict, self.tokens = tIDDict, tokens
        self.pos2rc = pos2rc
        
        f = lambda r: MatchResultExplain_MyLL1L(r, self.tIDDict, tokens)
        super().__init__(f)
        return
    
    
    
    def gen_ns_data(self, e):
        case = e.define_type
        if case == 'Token':
            #raise Exception('gen_ns_data() not on Token')
            assert e.end - e.begin == 1
            t = self.tokens[e.begin]
            e.ns.data = t.value
        elif isinstance(e.ID, int):
            #print('ID is int:', tID)
            assert case == 'Item'
            if 1 == e.info.max == e.info.min:
                self.gen_ns_data_from_only_child(e)
            else:
                self.gen_ns_data_from_children(e)
        elif case == 'Block':
            self.gen_ns_data_from_only_child(e)
        elif case == 'List':
            if 1 == len(e):
                self.gen_ns_data_from_only_child(e)
            else:
                self.gen_ns_data_from_children(e)
        else:
            raise Exception('unknown case {}'.format(case))
            
        pass
    def outbox_optional_Item(self, e):
        case = e.define_type
        if case == 'Item':
            if 1 == e.info.max and 0 == e.info.min:
                data = e.ns.data
                if not data:
                    e.ns.data = None
                else:
                    e.ns.data, = data
        return


        
            
        
    def gen_ns_data_from_only_child(self, e):
        self.gen_ns_data_from_children(e)
        e.ns.data, = e.ns.data
    def gen_ns_data_from_children(self, e):
        def has_data(ns):
            #return True
            return 'data' in ns.__dict__

        explain = self.explain
        data = e.ns.data = []
        for c in e:
            cns = explain(c).ns
            if not has_data(cns):
                raise ValueError('no .data: {} @{}'.format(explain(c).tID, e.tID))
            
            data.append(cns.data)
