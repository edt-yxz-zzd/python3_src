

from MyLL1L.ProcessMatchResult_MyLL1L import ProcessMatchResult_MyLL1L
from ast import literal_eval


class ProcessMatchResult_MyLL1L_of_ETL(ProcessMatchResult_MyLL1L):
    
    def _pre_process(self, match_result):pass
    def _process_leaf(self, match_result):pass

    
    def _get_result(self, match_result):
        ns = match_result[-1]
        tuple_ls = ns.data
        assert type(tuple_ls) == list

        return tuple_ls

            
    def _post_process(self, match_result):
        explain = self.explain
        e = self.explain(match_result)

        tID = e.tID
        ID, *rID = tID
        ns = e.ns
        case = e.define_type
        #print('case={} , tID={}'.format(case, tID))

        def has_data(ns):
            return True
            return 'data' in ns.__dict__
        if isinstance(e.ID, int):
            #print('ID is int:', tID)
            data = e.ns.data = []
            for c in e:
                cns = explain(c).ns
                if has_data(cns):
                    data.append(cns.data)
                else:
                    print('no .data: {} @{}'.format(explain(c).tID, tID))
        elif case == 'Block':
            #print('Block', tID)
            c, = e
            cns = explain(c).ns
            if has_data(cns):
                e.ns.data = cns.data
            else:
                print('no .data: {} @{}'.format(explain(c).tID, tID))

        elif case == 'Token':
            assert e.end - e.begin == 1
            t = self.tokens[e.begin]
            ns.data = t.value
            #print('Token', tID, repr(ns.data))

            if ID == 'item':
                last_id, = rID
                if last_id == 'string':
                    ns.data = literal_eval(ns.data)
                elif last_id == 'word':
                    pass
                else:
                    raise Exception('@case=Token: unknown-tID {}'.format(tID))
                assert type(ns.data) == str
            elif ID == "','":
                ns.data = ','
            else:
                raise Exception('@case=Token: unknown-tID {}'.format(tID))
        elif ID == 'tuple,':
            assert len(tID) == 1
            c, _ = e
            e.ns.data = tuple(explain(c).ns.data)
        elif ID == 'ETL_in_MyLL1L':
            assert len(tID) == 1
            c, = e
            e.ns.data = explain(c).ns.data
            
        else:
            raise ValueError('else:', tID)
        return
    


        
