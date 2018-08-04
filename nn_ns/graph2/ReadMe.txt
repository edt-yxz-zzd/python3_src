
1) Graph hierarchy
    IGraph
        NonEmptyGraph # at least one vertex
            WeakConnected
                WeakBiConnected
                    WeakTriConnected
        CyclicGraph # at least one cycle
        Planar
            UPseudoForest # at most one cycle per connected component
                UnicyclicGraph(CyclicGraph) # may not WeakConnected; one cycle
                UForest # AcyclicGraph
                UPseudoTree(WeakConnected)
                    UTree(UForest) # WeakConnected + AcyclicGraph
        Complete
        Bipartition
            UStar(Planar)
        EulerianGraph
    IDGraph(IGraph)
        Connected(WeakConnected)
            BiConnected(WeakBiConnected)
                TriConnected(WeakTriConnected)
        DAG
            DForest(UForest)
                DTree(Connected, UTree)
        DEulerianGraph(EulerianGraph)
2) Graph + Ops + Wrapper__OpsData2Graph(Graph)
3) func
    constructor
    new_mapping, total_new_mapping (free prev alloc)
    with_speed # use ConditionalOverride_Meta to override at same
4) use MRO_Meta to reorder bases
5) use Override_Meta to avoid unstable override caused by reorder bases


#######################

1) ops
2) class
3) ops + data -> class
4) ops for class
5) wrapper with fastest speed


class IClass:
    @abstractmethod
    def f(self, a):pass
    @classmethod
    @abstractmethod
    def cf(cls, a):pass
    @staticmethod
    @abstractmethod
    def sf(a):pass
class IOps:
    @abstractmethod
    def f(self, data, a):pass
    @abstractmethod
    def cf(self, a):pass
    @abstractmethod
    def sf(self, a):pass
class IWrapper(IClass):
    def __init__(self, ops, data):
        self.ops = ops
        self.data = data
    def f(self, a):
        return self.ops.f(self.data, a)
    @classmethod
    def cf(cls, a):
        FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFail!!!!!!!!!!!!!!!!!!!!
        return self.ops.cf(a)
class IWrapper: # not (IClass):
    def __init__(self, ops, data):
        self.ops = ops
        self.data = data
    def f(self, a):
        return self.ops.f(self.data, a)
    # not @classmethod
    def cf(self, a):
        return self.ops.cf(a)
    # not @classmethod
    def sf(self, a):
        return self.ops.sf(a)
def wrapper(ops_or_cls, data_or_obj):
    if issubclass(ops_or_cls, IClass) and isinstance(data_or_obj, ops_or_cls):
        obj = data_or_obj
        return data_or_obj
    ops, data = ops_or_cls, data_or_obj
    return IWrapper(ops, data)
def use(ops_or_cls, data_or_obj, a):
    assert isinstance(ops_or_cls, IOps) or (issubclass(ops_or_cls, IClass) and isinstance(data_or_obj, ops_or_cls))
    ops_or_cls.f(data_or_obj, a)
    ops_or_cls.cf(a)
    ops_or_cls.sf(a)
    obj = wrapper(ops_or_cls, data_or_obj)
    ...using obj...




