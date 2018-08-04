
__all__ = '''

ToProcessQueue
    UnorderedSet
    FILO
    FIFO
    ToProcessQueueOnce
        UnorderedSetOnce
        FILOOnce
        FIFOOnce
'''


import collections

# ToProcessQueue: FILO, FIFO, set

class ToProcessQueue:
    def __bool__(self):
        raise NotImplementedError
    
    def update(self, iterable):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def add(self, e):
        return self.update([e])
        raise NotImplementedError

    def apply(self, handler):
        'exhaustively apply; handler::Elem -> [Elem]'
        while self:
            x = self.pop()
            news = handler(x)
            self.update(news)

    def apply_with(self, handler, *args, **kwargs):
        new_handler = lambda x: handler(x, *args, **kwargs)
        self.apply(new_handler)
        return
    
        while self:
            x = self.pop()
            news = handler(x, *args, **kwargs)
            self.update(news)
        
        
    
class UnorderedSet(ToProcessQueue):
    def __init__(self, iterable=()):
        self.__x = set(iterable)
    def __bool__(self):
        return bool(self.__x)
    
    def update(self, iterable):
        self.__x.update(iterable)

    def pop(self):
        return self.__x.pop()

    def add(self, e):
        self.__x.add(e)
        
class FILO(ToProcessQueue):
    def __init__(self, iterable=()):
        self.__x = list(iterable)
    def __bool__(self):
        return bool(self.__x)
    
    def update(self, iterable):
        self.__x.extend(iterable)

    def pop(self):
        return self.__x.pop()

    def add(self, e):
        self.__x.append(e)

class FIFO(ToProcessQueue):
    def __init__(self, iterable=()):
        self.__x = collections.deque(iterable)
    def __bool__(self):
        return bool(self.__x)
        
    def update(self, iterable):
        self.__x.extend(iterable)

    def pop(self):
        return self.__x.popleft()

    def add(self, e):
        self.__x.append(e)
    
    

class ToProcessQueueOnce(ToProcessQueue):
    '''holds all input processed or to process to avoid duplicate processing

eg:
    queue = XXX_ToProcess(init_values)
    while queue:
        val = queue.pop()
        new_vals = handle(val)
        queue.update(new_vals)


    tree_dfs_visit:
        def visit(node):
            if is_leaf(node):
                ...
                return ()
            else:
                ...
                return get_children(node)
        FILO([root]).apply(visit)

        # if use FILO_ToProcess instead of FILO
        #   may cause bugs:
        #     if the tree allows reusing subtrees to save space...
    dag_visit:
        FILO_ToProcess(roots).apply(visit)
        # actually, we may need to box the node such that:
        #     __hash__(boxed_node) = id(node)
        #     __eq__(boxed_a, boxed_b) = a is b

    undirected_graph_connected_component_visit:
        def visit(vtx):
            ...
            return g.adjacent_vtcs(vtx)

        to_proc = FILO_ToProcess()
        for v in g.vertics():
            to_proc.add(v)
            to_proc.apply(visit)
        


subclassing:
    update = ordered_update | unordered_update
    __ToProcessQueue__ can be FILO, FIFO, set, UnorderedSet
    __ToProcessQueue__ should support:
        __init__()
        __bool__()
        update(iterable)
        pop()
        add(elem)
    
'''
    # __ToProcessQueue__ = ??
        
    
    def unordered_update(self, iterable):
        known = self.known_inputs
        unordered_news = set(iterable) - known
        self.__update(unordered_news)
    def ordered_update(self, iterable):
        known = self.known_inputs
        ordered_news = tuple(x for x in iterable if x not in known)
        self.__update(ordered_news)

    def update(self, iterable):
        'update = ordered_update | unordered_update'
        raise NotImplementedError
    
    def __update(self, disjoint_inputs):
        'disjoint_inputs should be a Container instead of Iterator'

        # known.update should be before _add_to_process
        self.known_inputs.update(disjoint_inputs)
        self.to_process.update(disjoint_inputs)

        
    def __init__(self, iterable):
        self.known_inputs = set()
        self.to_process = type(self).__ToProcessQueue__()
        self.update(iterable)
    def __bool__(self):
        return bool(self.to_process)

    def pop(self):
        '''mark one 'to_process' elem as 'processed'

if x in known_inputs and x not in to_process, then x is processed
'''
        return self.to_process.pop()

    def known(self, elem):
        return elem in self.known_inputs
    


class UnorderedSetOnce(ToProcessQueueOnce):
    __ToProcessQueue__ = set # or UnorderedSet
    update = ToProcessQueueOnce.unordered_update

class FILOOnce(ToProcessQueueOnce):
    __ToProcessQueue__ = FILO
    update = ToProcessQueueOnce.ordered_update
class FIFOOnce(ToProcessQueueOnce):
    __ToProcessQueue__ = FIFO
    update = ToProcessQueueOnce.ordered_update


def test__FILOOnce():
    g = {1: [2, 3], 2:[1, 3], 3:[], 4:[4]}
    ls = []
    def visit(v, g, ls):
        ls.append(v)
        return g[v]
    to = FILOOnce([1])
    assert to
    to.apply_with(visit, g, ls)
    assert not to

    #print(ls)
    assert ls == [1, 3, 2]

test__FILOOnce()

    
