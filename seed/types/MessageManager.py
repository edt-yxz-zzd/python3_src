

r'''

why using events?
    to insert 'code' in special places or on special conditions
    to flatten calls instead of recursion which may overflow call-stack
why using actions?
    to avoid mixing/nesting calls which all try to modify same data


application:
    parse domain:
        closure algorithm
            directed graph
            node's initial state may be 'undefined' or 'non-final'
            inform nodes but final ones about changes of their input nodes
            if a node's state changes, should throw ChangedEvent(node)
            if a node become final, should throw FinalEvent(node)
            different nodes may have different methods to calc it's state
            
'''

__all__ = '''
    BaseMessage
        BoxedMessage
        Event
        Action

    MessageManager
        BoxedMessageManager

'''.split()


import collections

eye_func = lambda x:x

class BaseMessage(BaseException):pass
Base = BaseMessage
class BoxedMessage(Base):
    def __init__(self, msg):
        self.msg = msg
    def unbox(self):
        return msg
    
class Event(Base):pass
class Action(Base):
    def __call__(self):
        raise NotImplementedError
    
# class NoEventError

class MessageManager:
    r'''
deque
    .append
    .popleft
        raise IndexError if empty

may use a priority_queue sorted by msg type
    assume given rules to compare msg types
        rule in form : A < B or A==B; 
        msg_types forms a DAG
        using any topological_ordering of the msg_types DAG to sort msgs
        

'''
    
    def __init__(self, queue=None):
        self.__q = collections.deque() if queue is None else queue

    def throw_boxed_message(self, boxed_msg):
        # unknown type of boxed_msg
        self.__q.append(boxed_msg)
    def catch_boxed_message(self):
        try:
            return self.__q.popleft()
        except IndexError:
            raise StopIteration('no messages@MessageManager::catch_boxed_message')
    def throw_message(self, msg):
        assert isinstance(msg, Base)
        self.throw_boxed_message(msg)
    def catch_message(self):
        # raise StopIteration while no messages
        return self.catch_boxed_message()

    def iter_messages(self):
        while True:
            yield self.catch_message()

    def on_BaseMessage(self, msg):
        assert isinstance(msg, Base)
        raise NotImplementedError
    def on_Action(self, act):
        assert isinstance(act, Action)
        act()
        return None
        raise NotImplementedError
    def _make_message_handler_name(self, MessageT):
        return 'on_{}'.format(MessageT.__name__)
    def find_message_handler(self, MessageT):
        assert issubclass(MessageT, Base)
        
        for T in MessageT.__mro__:
            if issubclass(T, Base):
                attr = self._make_message_handler_name(T)
                h = getattr(self, attr, None)
                if h is not None:
                    return h
        raise logic - error # at least on_BaseMessage
                
    def process_messages(self):
        # until no messages
        for message in self.iter_messages():
            h = self.find_message_handler(type(message))
            h(message)


class BoxedMessageManager(MessageManager):
    # to support priority queue
    def __init__(self, queue=None, *, msg_wrapper=None, msg_unwrapper=None):
        self.__wrap = eye_func if msg_wrapper is None else msg_wrapper
        self.__unwrap = eye_func if msg_unwrapper is None else msg_unwrapper
        super().__init__(queue)
        
    def throw_message(self, msg):
        assert isinstance(msg, Base)
        boxed_msg = self.__wrap(msg)
        self.throw_boxed_message(boxed_msg)
    def catch_message(self):
        # raise StopIteration while no messages
        boxed_msg = self.catch_boxed_message()
        return self.__unwrap(boxed_msg)

def ordered(lt_rules, i_rules=None):
    r'''result :: [obj] -- from left to right: min to max

input:
    lt_rules :: [(obj, obj)]
        [(A, B), (C, D)] ==>> A < B and C < D
    i_rules :: [obj]
        use i_rules to name objs not in lt_rules
            [E] will add E to result even E not present in lt_rules

    
algorithm:
    g = directed_graph(__eq__=__eq__)

    # A < B ==>> A<-B <==> B->A
    for A, B in lt_rules:
        # A < A is not allowed
        if A == B:
            raise ...
        g.add_dedge(A <- B) # make a DAG dedge from B to A
        
    for A in i_rules:
        g.add_node(A)

    nodes = reversed_topological_ordering(g) # may raise if not a DAG
    return list(nodes)
'''
    raise

def make_eq_classes(eq_rules, i_rules=None):
    r'''result :: set (frozenset obj)

type eq_class = frozenset obj

input:
    eq_rules :: [(obj, obj)]
        [(A, B), (C, D)] ==>> A == B and C == D
    i_rules :: [obj]
        use i_rules to name objs not in eq_rules
            [E] will add E to result even E not present in eq_rules

    
algorithm:
    s = union_set()/SetPartition()

    # A == B ==>> [:A:] should be [:B:] ==>> merge [:A:] and [:B:]
    for A, B in eq_rules:
        s.merge(A, B)
    for A in i_rules:
        s.add_elem(A)

    return set(map(frozenset, s.get_eq_classes()))
'''
    raise 

        
    
    
    
def make_ordered_types(lt_rules, eq_rules, i_rules):
    '''rule :: (type, type)
lt_rules :: [(type, type)]
eq_rules :: [(type, type)]

algo:
    eq_clses = make_eq_classes(eq_rules, i_rules)
    build id2eq_cls
    lt_rules = translate_binary_rules(lt_rules, id2eq_cls)
    i_rules = translate_unary_rules(i_rules, id2eq_cls)
    return ordered(lt_rules, i_rules)
    
    
eg:
    lt_rules = [(A, B), (B, C), (D, C)]
    eq_rules = [(B, D)]
    ==>> A < B < C, D<C, B==D

# [:A:] stands for "eq_class of A"
type A ==>> A in [:A:]        # make a eq_class [:A:]
if A == B then [:A:] is [:B:] # merge [:A:] and [:B:]
if A < B then [:A:] <- [:B:]  # make a DAG edge from [:B:] to [:A:]
    [:A:] <- [:A:] is not allowed

return reversed_topological_ordering of all eq_classes :: [[type]]
###### ^^^^^^^^^^^  :: tuple of frozenset of type in pyhon terms

in reversed_topological_ordering
    the first node is not a head of any dedges
    the last node is not a tail of any dedges
    ==>> dedge direction is "left <- right" ==>> min comes first
    so, types are sorted with key="<"
'''
    objs = set(get_objs(lt_rules)) | set(get_objs(eq_rules))
    s = UnionSet(objs)
    s.merge()
    raise
class PrintAction(Action):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        print(*self.args, **self.kwargs)


if __name__ == '__main__':
    MessageManager = BoxedMessageManager
    mm = MessageManager()
    for msg in map(PrintAction, 'hello world'.split()):
        mm.throw_message(msg)
    mm.process_messages()


    


