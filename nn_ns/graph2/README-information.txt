
# O, graph_information
class XXXOps:
    @O(time=...)
    def f(ops, graph, graph_information, ...):...

# graph_information :: Map query:String (result, who:str)
graph_information =
    {'is_planar': (True, 'Boyer_Myrvold_planarity_test')
    ,'is_connected': (False, '...')
    ,'is_undirected': (False, '...')
    ,'is_simple': (False, '...')
    ,...
    }
