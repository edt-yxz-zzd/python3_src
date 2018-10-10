
'''
Artificial Intelligence -- A Modern Approach (3ed)(2010)(Stuart Russell)
3 SOLVING PROBLEMS BY SEARCHING
Section 3.3. Searching for Solutions
page 77
    Figure 3.7
page 79

'''

__all__ = '''
    graph_search__dfs
    graph_search__non_dfs
    IGraphSearchAgent
    '''.split()

from .ISimple_Problem_Solving_Agent__OpenLoop import \
    ISimple_Problem_Solving_Agent__OpenLoop as Agent
from .abc import override, abstractmethod

def graph_search__dfs(problem:Agent.IProblem, state_set_factory):
    # known_states = explored_set + frontier
    initial_state = problem.get_initial_state()
    initial_paired_path = () # path = () | (path, (action, state))
    def make_path(paired_path):
        reversed_path = []
        while paired_path:
            paired_path, (action, state) = paired_path
            reversed_path.append((action, state))
        reversed_path.reverse(); path = reversed_path; del reversed_path
        return path

    #known_states = state_set_factory()
    #known_states.add(initial_state)
    explored_states = state_set_factory()

    frontier = [((), initial_state)]
    while frontier:
        paired_path, state = node = frontier.pop() # how to choose??
        if state in explored_states: continue
        explored_states.add(state)

        if problem.is_goal_state(state):
            return (initial_state, make_path(paired_path))

        actions = problem.get_actions_at(state)
        for action in actions:
            successor = problem.transition_model_result_successor_state_of(state, action)
            if successor in explored_states: continue
            #known_states.add(successor)
            child_paired_path = (paired_path, (action, successor))
            child_node = (child_paired_path, successor)
            frontier.append(child_node) # how to add??
            # frontier may contains duplicate states
    else:
        return Agent.FailureActions

def graph_search__non_dfs(problem:Agent.IProblem, state_set_factory):
    # known_states = explored_set + frontier
    initial_state = problem.get_initial_state()
    initial_paired_path = () # path = () | (path, (action, state))
    def make_path(paired_path):
        reversed_path = []
        while paired_path:
            paired_path, (action, state) = paired_path
            reversed_path.append((action, state))
        reversed_path.reverse(); path = reversed_path; del reversed_path
        return path

    known_states = state_set_factory()
    known_states.add(initial_state)

    frontier = [((), initial_state)]
    while frontier:
        paired_path, state = node = frontier.pop() # how to choose??
        if problem.is_goal_state(state):
            return (initial_state, make_path(paired_path))

        actions = problem.get_actions_at(state)
        for action in actions:
            successor = problem.transition_model_result_successor_state_of(state, action)
            if successor in known_states: continue
            known_states.add(successor)
            child_paired_path = (paired_path, (action, successor))
            child_node = (child_paired_path, successor)
            frontier.append(child_node) # how to add??
    else:
        return Agent.FailureActions

class IGraphSearchAgent(Agent):
    '''

BREADTH-FIRST-SEARCH
page 82 Figure 3.11 Breadth-first search on a graph
    bfs: finite-fanout ==>> complete
    //the memory requirements are a bigger problem for breadth-first search than is the execution time.

    let get_node_queue_ops() -> FIFO_ops
    let is_frontier_unique_filter() -> True

UNIFORM-COST-SEARCH
page 84 Figure 3.14 Uniform-cost search on a graph.
     it will get stuck in an infinite loop if there is a path with an infinite sequence of zero-cost actions—for example, a sequence ofNoOpactions. Completeness is guaranteed provided the cost of every step exceeds some small positive constant.
    let get_node_queue_ops() -> priority_queue_ops
    let is_frontier_unique_filter() -> True #!!!!!! with diff path_cost

'''
    class IQueueOps:
        # Queue = FIFO | LIFO | priority_queue | ...
        @abstractmethod
        def make_new_queue(ops, *, key=None):
            # "key" is used for priority_queue
            raise NotImplementedError
        @abstractmethod
        def is_empty(ops, self):
            raise NotImplementedError
        @abstractmethod
        def pop(ops, self):
            raise NotImplementedError
        @abstractmethod
        def put(ops, self, element):
            raise NotImplementedError
        @abstractmethod
        def update(ops, self, element):
            # assume key(element) changes for priority_queue
            # no-op for LIFO, FIFO
            raise NotImplementedError
    @abstractmethod
    def get_node_queue_ops(self):
        # -> IQueueOps<Node>
        raise NotImplementedError
    @abstractmethod
    def make_new_state_set(self):
        # -> Set<State>
        raise NotImplementedError
    @abstractmethod
    def make_new_state_dict(self):
        # -> Map<State, v>
        raise NotImplementedError
    @abstractmethod
    def is_frontier_unique_filter(self):
        raise NotImplementedError
        queue_ops = self.get_node_queue_ops()
        is_FIFO = queue_ops.is_FIFO()
        is_LIFO = queue_ops.is_LIFO()
        is_priority_queue = queue_ops.is_priority_queue()
        is_frontier_unique_filter = is_FIFO or is_priority_queue
        if is_LIFO:
            assert not is_frontier_unique_filter
        return is_frontier_unique_filter

    @override
    def search(self, problem):
        # -> Iter Action | FailureActions
        # known_state2node.keys() = explored_set + frontier
        # frontier :: IQueue<state>
        is_frontier_unique_filter = self.is_frontier_unique_filter()
        initial_state = problem.get_initial_state()
        initial_node = problem.make_initial_costed_path(initial_state)
        if not is_frontier_unique_filter:
            explored_states = self.make_new_state_set()

        known_state2node = self.make_new_state_dict()
        known_state2node[initial_state] = initial_node

        queue_ops = self.get_node_queue_ops()
        frontier = queue_ops.make_new_queue(
            key=lambda state:known_state2node[state].path_cost)
        frontier_set = self.make_new_state_set()
        def frontier_add_state(state):
            queue_ops.put(frontier, state)
            frontier_set.add(state)
        def frontier_pop():
            state = queue_ops.pop(frontier)
            frontier_set.remove(state)
            return state

        frontier_add_state(initial_state)
        def may_update_known_state2node(node):
            state = node.state
            may_node = known_state2node.get(state)
            if may_node is not None:
                if may_node.path_cost > node.path_cost:
                    known_state2node[state] = node
                    return True
            return False

        while not queue_ops.is_empty(frontier):
            state = frontier_pop()
            node = known_state2node[state]
            if not is_frontier_unique_filter:
                if state in explored_states: continue
                explored_states.add(state)

            if problem.is_goal_state(state):
                return node.to_path()

            actions = problem.get_actions_at(state)
            for action in actions:
                child_node = self.ChildNode(parent_node, action)
                successor = child_node.state

                does_update = True
                if successor in known_state2node:
                    does_update = may_update_known_state2node(child_node)
                else:
                    known_state2node[successor] = child_node

                if successor in frontier_set:
                    if is_frontier_unique_filter:
                        if does_update:
                            queue_ops.update(frontier, successor)
                        continue
                queue_ops.put(frontier, successor)
        else:
            return Agent.FailureActions

