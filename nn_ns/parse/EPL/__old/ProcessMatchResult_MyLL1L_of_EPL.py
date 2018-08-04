

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

        def get_data(e):
            case = e.define_type
            if case == 'Token':
                raise Exception('get_data() not on Token')
            elif isinstance(e.ID, int):
                #print('ID is int:', tID)
                if 1 == e.info.max == e.info.min:
                    get_data_from_only_child(e)
                else:
                    get_data_from_children(e)
            elif case == 'Block':
                get_data_from_only_child(e)
            elif case == 'List':
                if 1 == len(e):
                    get_data_from_only_child(e)
                else:
                    get_data_from_children(e)
            else:
                raise Exception('unknown case {}'.format(case))
                
            
            
        def get_data_from_only_child(e):
            get_data_from_children(e)
            e.ns.data, = e.ns.data
        def get_data_from_children(e):
            data = e.ns.data = []
            for c in e:
                cns = explain(c).ns
                if not has_data(cns):
                    raise ValueError('no .data: {} @{}'.format(explain(c).tID, e.tID))
                
                data.append(cns.data)
        def has_data(ns):
            #return True
            return 'data' in ns.__dict__

        if case == 'Token':
            assert e.end - e.begin == 1
            t = self.tokens[e.begin]
            ns.data = t.value
            #print('Token', tID, repr(ns.data))

            if ID == 'name':
                last_id, = rID
                if last_id == 'string':
                    ns.data = literal_eval(ns.data)
                elif last_id == 'word':
                    pass
                else:
                    raise Exception('@case=Token: unknown-tID {}'.format(tID))
                assert type(ns.data) == str
            elif ID in {"'['", "']'"}:
                ns.data = literal_eval(ID)
            else:
                raise Exception('@case=Token: unknown-tID {}'.format(tID))
            return

        get_data(e)
        if isinstance(e.ID, int):
            pass
        elif case == 'Block':
            pass
        elif ID == 'names':
            ns.data = tuple(ns.data)
        elif ID == 'nonempty_list':
            assert len(tID) == 2
            last_id, = rID
            if last_id == 'nameless_list':
                ns.data = ((), ns.data)
            elif last_id == 'named_list':
                ns.data = tuple(ns.data)
            else:
                raise Exception('unknown-tID {}'.format(tID))
            list_name, ls = ns.data
        elif ID == 'item':
            assert len(tID) == 1
            (list_name, ls), optional_tag = ns.data

            if optional_tag:
                tag, = optional_tag
                assert tag
            else:
                tag = ()

            ns.data = (list_name, tag, ls)
        elif ID == '[list]':
            assert len(tID) == 1
            _, optional_named_list, _ = ns.data
            
            if optional_named_list:
                named_list, = optional_named_list
                assert named_list
            else:
                named_list = (), []
            ns.data = named_list
        
            
        else:
            pass
            #raise ValueError('else:', tID)
        return
    


        
