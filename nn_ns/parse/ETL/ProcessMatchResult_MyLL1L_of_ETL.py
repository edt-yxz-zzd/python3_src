

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

        self.gen_ns_data(e)

        if case == 'Token':
            if tID == ('item', 'string'):
                ns.data = literal_eval(ns.data)
            return

        elif isinstance(e.ID, int):
            pass
        elif case == 'Block':
            pass

        elif ID == 'tuple,':
            assert len(tID) == 1
            ls, _ = ns.data
            ns.data = tuple(ls)
        elif ID == 'ETL_in_MyLL1L':
            assert len(tID) == 1
            ls, _ = ns.data
            ns.data = ls
            
        else:
            pass
            #raise ValueError('else:', tID)
        return
    


        
