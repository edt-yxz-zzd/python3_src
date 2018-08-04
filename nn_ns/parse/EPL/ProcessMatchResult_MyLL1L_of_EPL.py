

from MyLL1L.ProcessMatchResult_MyLL1L import ProcessMatchResult_MyLL1L
from ast import literal_eval


class ProcessMatchResult_MyLL1L_of_EPL(ProcessMatchResult_MyLL1L):
    
    def _pre_process(self, match_result):pass
    def _process_leaf(self, match_result):pass

    
    def _get_result(self, match_result):
        ns = match_result[-1]
        main_item = ns.data
        assert type(main_item) == tuple
        assert len(main_item) == 3

        return main_item


                
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
            if tID == ('chunk', 'string'):
                #print(tID, ns.data)
                ns.data = literal_eval(ns.data)
        elif isinstance(e.ID, int):
            pass
        elif case == 'Block':
            pass
        elif ID == 'chunks':
            ns.data = tuple(ns.data)
            
        elif ID == 'item':
            assert len(tID) == 1
            _, optional_name, subitems, _, optional_tag = ns.data

            def optional_chunks2tuple(optional_chunks):
                if optional_chunks:
                    chunks, = optional_chunks
                    assert chunks
                else:
                    chunks = ()
                return chunks

            name = optional_chunks2tuple(optional_name)
            tag = optional_chunks2tuple(optional_tag)

            ns.data = (name, tag, subitems)
        
            
        else:
            pass
            #raise ValueError('else:', tID)
        return
    


        
