
r'''
an BidirectedGraph implement example




>>> bgraph = BidirectedGraph(
...     num_vertices = 5
...     ,num_aedges = 6
...     ,num_hedges = 9
...     ,hedge2vertex = (1, 1, 2, 2, 3, 3, 4, 4, 1)
...     ,hedge2is_outgoing = tuple(c == 'T' for c in 'FTFFFTFTT')
...     ,hedge2aedge = (1, 2, 2, 3, 3, 4, 4, 5, 5)
...     )

>>> bgraph
BidirectedGraph(hedge2aedge = (1, 2, 2, 3, 3, 4, 4, 5, 5), hedge2is_outgoing = (False, True, False, False, False, True, False, True, True), hedge2vertex = (1, 1, 2, 2, 3, 3, 4, 4, 1), num_aedges = 6, num_hedges = 9, num_vertices = 5)

>>> bgraph.is_bidirected_graph()
True
>>> bgraph.is_directed_graph()
False
>>> bgraph.is_undirected_graph()
False

>>> bgraph.has_laedges()
True
>>> bgraph.has_haedges()
True
>>> bgraph.has_isolated_vertices()
True

>>> bgraph.get_maybe_min_vertex_degree()
0
>>> bgraph.get_maybe_max_vertex_degree()
3
>>> bgraph.get_maybe_min_aedge_degree()
0
>>> bgraph.get_maybe_max_aedge_degree()
2

>>> isolated_vertices = bgraph.vertex_degree2vertices[0]
>>> isolated_vertices
[0]
>>> loose_aedges = bgraph.aedge_degree2aedges[0]
>>> loose_aedges
[0]
>>> half_aedges = bgraph.aedge_degree2aedges[1]
>>> half_aedges
[1]


>>> bgraph.is_edgeless_graph()
False
>>> bgraph.is_vertexless_graph()
False
>>> bgraph.is_nothing_graph()
False

'''


'''
BidirectedGraph(
    num_vertices = 
    ,num_aedges = 
    ,num_hedges = 
    ,hedge2vertex = ()
    ,hedge2is_outgoing = ()
    ,hedge2aedge = ()
    )
'''


__all__ = '''
    HyperGraph
    BidirectedGraph
    '''.split()

from seed.iters.minmax import minmax_default
from seed.helper.repr_input import repr_helper
from seed.helper.__SpecialMethodGetter__ import (
    theSpecialMethodCaller
    ,SpecialMethodGetter
    )
from types import MappingProxyType
#from collections.abc import Sequence

def is_uint(x):
    return type(x) is int and x >= 0
def is_uint_lt(x, upper):
    return type(x) is int and 0 <= x < upper
def check_uint(x):
    if not is_uint(x): raise TypeError
def is_bool(x):
    return type(x) is bool
def is_tuple(x):
    return type(x) is tuple
def is_tuple_and_len(x, size):
    return type(x) is tuple and len(x) == size
def check_tuple_and_len(x, size):
    if not is_tuple_and_len(x, size): raise TypeError
def check_all(bools):
    if not all(bools): raise TypeError

def tupletuple_of(lsls):
    return tuple(map(tuple, lsls))


class Global:
    input_attrs = '''
        num_vertices
        num_aedges
        num_hedges
        hedge2vertex
        hedge2is_outgoing
        hedge2aedge
        '''.split()
    _init0_attrs = input_attrs + '''
        vertex2hedges
        aedge2hedges
        vertex2outgoing_hedges
        vertex2incoming_hedges

        hedge_to_vertex2hedges_idx
        hedge_to_aedge2hedges_idx
        hedge_to_vertex2incoming_hedges_maybe_idx
        hedge_to_vertex2outgoing_hedges_maybe_idx
        hedge_to_vertex2inout_hedges_fake_idx

        mutable_graph_query_information
        mutable_graph_query_data
        '''.split()
    _init1_attrs = '''
        vertex_degree2vertices
        aedge_degree2aedges
        '''.split()
    all_attrs = '''
        '''.split()

    input_attrs = tuple(input_attrs)
    _init0_attrs = tuple(_init0_attrs)
    _init1_attrs = tuple(_init1_attrs)
    all_attrs = _init0_attrs + _init1_attrs
    assert len(all_attrs) == len(set(all_attrs))

    @staticmethod
    def _get_attr(__self, attr):
        return getattr(__self, '_HyperGraph__'+attr)
    @staticmethod
    def _set_attr(__self, attr, obj):
        return setattr(__self, '_HyperGraph__'+attr, obj)

def make_readonly_property(get, attr):
    def f(__self):
        return get(__self, attr)
    f.__name__ = attr
    return property(f)
def make_readonly_properties(get, attrs):
    return {attr:make_readonly_property(get, attr) for attr in attrs}


class HyperGraph:
    # aedge2hedges
    #   HyperGraph      - 1_to_many
    #   BidirectedGraph - 1_to_[0..2]
    #
    if True: # define properties
        try:
            num_vertices
        except NameError:
            pass
        else:
            raise logic-error

        assert type(locals()) is dict
        locals().update(
            make_readonly_properties(Global._get_attr, Global.all_attrs)
            )
        assert num_vertices is not None


        #########################
        __mutable_graph_query_information = mutable_graph_query_information.fget
        @mutable_graph_query_information.getter # .fget
        def mutable_graph_query_information(__self):
            return MappingProxyType(
                __class__.__mutable_graph_query_information(__self))

        __mutable_graph_query_data = mutable_graph_query_data.fget
        @mutable_graph_query_data.getter # .fget
        def mutable_graph_query_data(__self):
            return MappingProxyType(
                __class__.__mutable_graph_query_data(__self))



    def __init__(__self, *
        , num_vertices          : 'UInt'
        , num_aedges            : 'UInt'
        , num_hedges            : 'UInt'
        , hedge2vertex          : '[Vertex]{num_hedges} where Vertex=UInt{0..num_vertices-1}'
        , hedge2is_outgoing     : '[Bool]{num_hedges}'
            # (vertex->aedge) <==> is_outgoing==True
            # (vertex<-aedge) <==> is_outgoing==False
        , hedge2aedge           : '[AEdge]{num_hedges} where AEdge=UInt{0..num_aedges-1}'
        ):
        check_uint(num_vertices)
        check_uint(num_aedges)
        check_uint(num_hedges)

        check_tuple_and_len(hedge2vertex, num_hedges)
        check_tuple_and_len(hedge2is_outgoing, num_hedges)
        check_tuple_and_len(hedge2aedge, num_hedges)

        check_all(is_uint_lt(v, num_vertices) for v in hedge2vertex)
        check_all(map(is_bool, hedge2is_outgoing))
        #check_all(type(b) is bool for b in hedge2is_outgoing)
        check_all(is_uint_lt(e, num_aedges) for e in hedge2aedge)


        vertex2hedges = [[] for _ in range(num_vertices)]
        aedge2hedges = [[] for _ in range(num_aedges)]
        hedge_to_vertex2hedges_idx = [None]*num_hedges
        hedge_to_aedge2hedges_idx = [None]*num_hedges

        vertex2outgoing_hedges = [[] for _ in range(num_vertices)]
        vertex2incoming_hedges = [[] for _ in range(num_vertices)]
        hedge_to_vertex2incoming_hedges_maybe_idx = [None]*num_hedges
        hedge_to_vertex2outgoing_hedges_maybe_idx = [None]*num_hedges
        hedge_to_vertex2inout_hedges_fake_idx = [None]*num_hedges
            # [NonZeroInteger]
            # [(-incoming_idx-1 | +outgoing_idx+1)]

        for hedge, vertex in enumerate(hedge2vertex):
            hedges = vertex2hedges[vertex]
            idx = len(hedges)
            hedges.append(hedge)
            hedge_to_vertex2hedges_idx[hedge] = idx

        for hedge, aedge in enumerate(hedge2aedge):
            hedges = aedge2hedges[aedge]
            idx = len(hedges)
            hedges.append(hedge)
            hedge_to_aedge2hedges_idx[hedge] = idx

        vertex2inout_hedges = \
            [vertex2incoming_hedges
            ,vertex2outgoing_hedges
            ]
        hedge_to_vertex2inout_hedges_maybe_idx = \
            [hedge_to_vertex2incoming_hedges_maybe_idx
            ,hedge_to_vertex2outgoing_hedges_maybe_idx
            ]
        for hedge, vertex in enumerate(hedge2vertex):
            is_outgoing = hedge2is_outgoing[hedge]
            hedges = vertex2inout_hedges[is_outgoing][vertex]
            idx = len(hedges)
            hedges.append(hedge)
            hedge_to_vertex2inout_hedges_maybe_idx[is_outgoing][hedge] = idx
            fake_idx = len(hedges) # == idx+1
            if not is_outgoing:
                fake_idx = -fake_idx
            hedge_to_vertex2inout_hedges_fake_idx[hedge] = fake_idx

        del vertex2inout_hedges
        del hedge_to_vertex2inout_hedges_maybe_idx




        # make immutable data
        vertex2hedges = tupletuple_of(vertex2hedges)
        aedge2hedges = tupletuple_of(aedge2hedges)
        vertex2outgoing_hedges = tupletuple_of(vertex2outgoing_hedges)
        vertex2incoming_hedges = tupletuple_of(vertex2incoming_hedges)

        hedge_to_vertex2hedges_idx = tuple(hedge_to_vertex2hedges_idx)
        hedge_to_aedge2hedges_idx = tuple(hedge_to_aedge2hedges_idx)
        hedge_to_vertex2incoming_hedges_maybe_idx = tuple(hedge_to_vertex2incoming_hedges_maybe_idx)
        hedge_to_vertex2outgoing_hedges_maybe_idx = tuple(hedge_to_vertex2outgoing_hedges_maybe_idx)
        hedge_to_vertex2inout_hedges_fake_idx = tuple(hedge_to_vertex2inout_hedges_fake_idx)



        mutable_graph_query_information = {}
        mutable_graph_query_data = {}

        __self.__set_attrs_ex(Global._init0_attrs, locals())

        __self.set_graph_query_information(
                __class__, is_bidirected_graph=True)

        __self.__later_init()
    def __set_attrs_ex(__self, attrs, locals):
        d = locals
        d = {attr:d[attr] for attr in attrs}
        __self.__set_attrs(**d)
    def __set_attrs(__self, **kwargs):
        f = Global._set_attr
        for attr, obj in kwargs.items():
            f(__self, attr, obj)
    def set_graph_query_information(__self, who, **kwargs):
        #bug: information = __self.mutable_graph_query_information
        information = __class__.__mutable_graph_query_information(__self)

        information.update(
            (query, (who, information))
            for query, information in kwargs.items()
            )
    def set_graph_query_data(__self, who, **kwargs):
        data = __class__.__mutable_graph_query_data(__self)

        data.update(
            (query, (who, data))
            for query, data in kwargs.items()
            )

    def __repr__(__self):
        kwargs = {attr: getattr(__self, attr) for attr in Global.input_attrs}
        return repr_helper(__self, **kwargs)



    def __later_init(__self):
        ###using get_maybe_max_vertex_degree
        ###using get_maybe_max_aedge_degree
        vertex2hedges = __self.vertex2hedges
        maybe_max_vertex_degree = __self.get_maybe_max_vertex_degree()
        aedge2hedges = __self.aedge2hedges
        maybe_max_aedge_degree = __self.get_maybe_max_aedge_degree()

        def mk(maybe_max_voe_degree, voe2hedges):
            # voe = vertex or aedge
            max_voe_degree = -1 if maybe_max_voe_degree is None else maybe_max_voe_degree
            voe_degree2voes = [[] for _ in range(max_voe_degree+1)]
            for voe, hedges in enumerate(voe2hedges):
                voe_degree = len(hedges)
                voe_degree2voes[voe_degree].append(voe)
            return voe_degree2voes

        vertex_degree2vertices = mk(maybe_max_vertex_degree, vertex2hedges)
        aedge_degree2aedges = mk(maybe_max_aedge_degree, aedge2hedges)
        __self.__set_attrs_ex(Global._init1_attrs, locals())




    #######################################
    # mutable_graph_query_information
    #######################################
    def graph_query_information_ex(__self, __query_key):
        Nothing = object()
        may_result = __self.mutable_graph_query_information.get(__query_key, Nothing)
        if may_result is not Nothing:
            result = may_result
        else:
            tp = type(__self) # __class__
            who = tp # __class__
            method = getattr(tp, f'__{__query_key}__')
            ans = method(__self)
            #result = who, ans
            __self.set_graph_query_information(who, **{__query_key:ans})
            result = __self.mutable_graph_query_information[__query_key]
            if __debug__:
                _who, _ans = result
                assert _who is who
                assert _ans is ans
        return result
    def graph_query_information(__self, __query_key):
        result = __self.graph_query_information_ex(__query_key)
        who, ans = result
        return ans

    def check_query_information(__self, **kwargs:bool):
        if not __self.test_query_information(**kwargs): raise TypeError
    def test_query_information(__self, **kwargs:bool):
        check_all(map(is_bool, kwargs.values()))
        f = __self.graph_query_information
        return all(f(query_key) == ans for query_key, ans in kwargs)

    #######################################

    def is_bidirected_graph(__self):
        return __self.graph_query_information('is_bidirected_graph')
    def is_directed_graph(__self):
        return __self.graph_query_information('is_directed_graph')
    def is_undirected_graph(__self):
        return __self.graph_query_information('is_undirected_graph')
    def __is_directed_graph__(__self):
        if not __self.is_bidirected_graph():  return False
        if __self.has_laedges():              return False
        if __self.has_haedges():              return False
        f = SpecialMethodGetter(__self.hedge2is_outgoing).__getitem__
        return all(f(hedge0) != f(hedge1)
            for aedge, (hedge0, hedge1) in enumerate(__self.aedge2hedges))

    def __is_undirected_graph__(__self):
        if not __self.is_bidirected_graph():  return False
        if __self.has_laedges():              return False
        if __self.has_haedges():              return False
        f = SpecialMethodGetter(__self.hedge2is_outgoing).__getitem__
        return all(f(hedge0) and f(hedge1)
            for aedge, (hedge0, hedge1) in enumerate(__self.aedge2hedges))

    def has_haedges(__self):
        return __self.graph_query_information('has_haedges')
    def has_laedges(__self):
        # loose aedge
        return __self.graph_query_information('has_laedges')
    def has_isolated_vertices(__self):
        return __self.graph_query_information('has_isolated_vertices')

    def __has_haedges__(__self):
        return any(len(hedges) == 1 for hedges in __self.aedge2hedges)
    def __has_laedges__(__self):
        return any(len(hedges) == 0 for hedges in __self.aedge2hedges)
        may_min = __self.get_maybe_min_aedge_degree()
        return may_min is not None and may_min == 0
    def __has_isolated_vertices__(__self):
        return any(len(hedges) == 0 for hedges in __self.vertex2hedges)
        may_min = __self.get_maybe_min_vertex_degree()
        return may_min is not None and may_min == 0
    def __is_bidirected_graph__(__self):
        return any(len(hedges) <= 2 for hedges in __self.aedge2hedges)
        may_max = __self.get_maybe_max_aedge_degree()
        return may_max is None or may_max <= 2


    #######################################
    # mutable_graph_query_data
    #######################################
    def graph_query_data_ex(__self, __query_key):
        Nothing = object()
        may_result = __self.mutable_graph_query_data.get(__query_key, Nothing)
        if may_result is not Nothing:
            result = may_result
        else:
            tp = type(__self) # __class__
            who = tp # __class__
            method = getattr(tp, f'__{__query_key}__')
            ans = method(__self)
            #result = who, ans
            __self.set_graph_query_data(who, **{__query_key:ans})
            result = __self.mutable_graph_query_data[__query_key]
            if __debug__:
                _who, _ans = result
                assert _who is who
                assert _ans is ans
        return result
    def graph_query_data(__self, __query_key):
        result = __self.graph_query_data_ex(__query_key)
        who, ans = result
        return ans

    def check_query_data(__self, **kwargs):
        if not __self.test_query_data(**kwargs): raise TypeError
    def test_query_data(__self, **kwargs):
        def eq(lhs, rhs):
            if lhs is rhs: return True
            return type(lhs) is type(rhs) and lhs == rhs
        f = __self.graph_query_data
        return all(eq(f(query_key), ans) for query_key, ans in kwargs)

    #######################################

    def get_maybe_minmax_vertex_degree(__self):
        return __self.graph_query_data('get_maybe_minmax_vertex_degree')
    def get_maybe_minmax_aedge_degree(__self):
        return __self.graph_query_data('get_maybe_minmax_aedge_degree')
    def __get_maybe_minmax_vertex_degree__(__self):
        # -> None | (min, max)
        return minmax_default(None, map(len, __self.vertex2hedges))
    def __get_maybe_minmax_aedge_degree__(__self):
        return minmax_default(None, map(len, __self.aedge2hedges))

    #######################################
    def __get_may_mM(__self, __query_key, __idx):
        may_mM = getattr(__self, __query_key)()
        if not may_mM: return None
        return may_mM[__idx]
    def get_maybe_min_vertex_degree(__self):
        return __self.__get_may_mM('get_maybe_minmax_vertex_degree', 0)
    def get_maybe_max_vertex_degree(__self):
        return __self.__get_may_mM('get_maybe_minmax_vertex_degree', 1)
    def get_maybe_min_aedge_degree(__self):
        return __self.__get_may_mM('get_maybe_minmax_aedge_degree', 0)
    def get_maybe_max_aedge_degree(__self):
        return __self.__get_may_mM('get_maybe_minmax_aedge_degree', 1)
    #######################################


    #######################################
    #edgeless_graph, vertexless_graph
    #nothing_graph
    #avoid using: order_zero_graph/empty_graph/null_graph
    #######################################
    # A graph is connected when there is a path between every pair of vertices.
    #   edgeless_graph
    #   order_zero_graph |<=| edgeless_graph
    #       # but since thare are maybe loose_aedges
    #       # I define nothing_graph = edgeless order_zero graph
    #   empty_graph = edgeless_graph
    #   null_graph =[ambiguous]= edgeless_graph |ambiguous-or| order_zero_graph
    def is_edgeless_graph(__self):
        return not len(__self.aedge2hedges)
    def is_vertexless_graph(__self):
        return not len(__self.vertex2hedges)
    def is_nothing_graph(__self):
        return __self.is_edgeless_graph() and __self.is_vertexless_graph()

    #######################################
    #undirected/directed:
    #   is_weak_[tree|path|cycle|wheel|star]
    #   is_weak_[forest|paths|cycles|wheels|stars]
    #       num_connected_components_of
    #   is_weak_bipartite_graph
    #   is_weak_complete_graph
    #   is_weak_series_parallel_graph # with 2 terminals
    #directed:
    #   DAG, in_tree, out_tree
    #   series_parallel_graph
    #######################################

    #######################################
    #
    #######################################

    #######################################
    #is_weak_connected
    #   underlying undirected graph
    #is_strong_connected
    #   treat (<-->) as an non-existing aedge
    #   treat (-><-) as two parallel directed aedge
    #num_weak_connected_components_of
    #weak_connected_component_idx2vertices
    #weak_connected_component_idx2aedges
    #vertex2weak_connected_component_idx
    #aedge2weak_connected_component_idx
    #######################################

    #######################################
    #connectivity_of
    #connectivity_ge # is_<k>_connected
    #   #how??
    #######################################

    #######################################
    #should move to BidirectedGraph
    #has_weak_loops # self_loop
    #   is (<-->) an existing aedge???
    #   what if aedge_degree > 2???
    #       aedge incident to a vertex at least twice
    #has_weak_multiedges, has_weak_multiloops
    #   underlying undirected graph
    #has_strong_multiedges, has_strong_multiloops
    #   multiedges distinguish by (->->)|(<-<-)|(-><-)|(<-->)
    #######################################


    #######################################
    #
    #######################################

    #######################################
    #
    #######################################

class BidirectedGraph(HyperGraph):
    def __init__(__self, *
        , num_vertices          : 'UInt'
        , num_aedges            : 'UInt'
        , num_hedges            : 'UInt'
        , hedge2vertex          : '[Vertex]{num_hedges} where Vertex=UInt{0..num_vertices-1}'
        , hedge2is_outgoing     : '[Bool]{num_hedges}'
            # (vertex->aedge) <==> is_outgoing==True
            # (vertex<-aedge) <==> is_outgoing==False
        , hedge2aedge           : '[AEdge]{num_hedges} where AEdge=UInt{0..num_aedges-1}'
        ):

        if True: # make kwargs
            kwargs = dict(locals())
            keys_to_del = [key for key in kwargs if key[0] == '_']
            for k in keys_to_del:
                del kwargs[k]
        HyperGraph.__init__(__self, **kwargs)
        if not __self.is_bidirected_graph():
            # test aedge2hedges
            bad_aedges = [aedge for aedge, hedges in enumerate(aedge2hedges)
                            if len(hedges) > 2]
            if bad_aedges:
                raise ValueError(f'more than two hedges. bad_aedges={bad_aedges}')
            del bad_aedges
            raise logic-error



'''
v0 # isolated
e0 # loose
# e1 # haedge not hedge

e1 --[h0]-> v1 --[h1]-> e2 --[h2]-> v2
            |                       ^
            |                       |
           [h8]                    [h3]
            |                       |
            V                       |
            e5                      e3
            ^                       |
            |                       |
           [h7]                    [h4]
            |                       |
            |                       V
            v4 <-[h6]-- e4 <-[h5]-- v3
'''
def _t():
    bgraph = BidirectedGraph(
        num_vertices = 5
        ,num_aedges = 6
        ,num_hedges = 9
        ,hedge2vertex = (1, 1, 2, 2, 3, 3, 4, 4, 1)
        # FTFFFTFTT
        ,hedge2is_outgoing = tuple(c == 'T' for c in 'FTFFFTFTT')
        ,hedge2aedge = (1, 2, 2, 3, 3, 4, 4, 5, 5)
        )
    #print(bgraph)
    assert repr(bgraph) == '''\
BidirectedGraph(hedge2aedge = (1, 2, 2, 3, 3, 4, 4, 5, 5), hedge2is_outgoing = (False, True, False, False, False, True, False, True, True), hedge2vertex = (1, 1, 2, 2, 3, 3, 4, 4, 1), num_aedges = 6, num_hedges = 9, num_vertices = 5)'''

if __name__ == "__main__":
    _t()

    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #doctest: +NORMALIZE_WHITESPACE
