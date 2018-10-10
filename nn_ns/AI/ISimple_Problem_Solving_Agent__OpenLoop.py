
'''
Artificial Intelligence -- A Modern Approach (3ed)(2010)(Stuart Russell)
3 SOLVING PROBLEMS BY SEARCHING
Section 3.1. Problem-Solving Agents
page 67
Figure 3.1
'''

from abc import ABC, abstractmethod

class ISimple_Problem_Solving_Agent__OpenLoop(ABC):
    class UnInitActions:pass
    class FailureActions:pass
    class NoAction:pass
    class IProblem(ABC):
        # costed_path = (initial_state,) | (costed_path, (action, state, path_cost))
        # assumption:
        #   path_cost = sum of step_cost
        #   step_cost >= 0
        @abstractmethod
        def get_initial_state(self):
            # -> state
            raise NotImplementedError
        #def get_all_actions(self):
        @abstractmethod
        def get_actions_at(self, state):
            # -> Set Action
            raise NotImplementedError
        @abstractmethod
        def transition_model_result_successor_state_of(self, state, action):
            # -> state
            raise NotImplementedError
        @abstractmethod
        def is_goal_state(self, state):
            # -> Bool
            raise NotImplementedError
        @abstractmethod
        def eval_step_cost(self, begin_state, action, successor_state):
            # -> NonnegativeRealNumber
            raise NotImplementedError
        def eval_path_cost(self, path):
            # path = (begin_state, [(action, successor_state)])
            begin_state, action_successor_state_pairs = path
            cost = 0
            for action, successor_state in action_successor_state_pairs:
                cost += self.eval_step_cost(begin_state, action, successor_state)
                begin_state = successor_state
            return cost
        def is_initial_costed_path(self, costed_path):
            return len(costed_path) == 1
        def make_initial_costed_path(self, initial_state):
            return (initial_state,)
        def make_child_costed_path(self, parent_costed_path, action):
            parent_state = self.costed_path2last_state(parent_costed_path)
            child_state = self.transition_model_result_successor_state_of(parent_state, action)
            step_cost = self.eval_step_cost(parent_state, action, child_state)
            parent_path_cost = self.costed_path2path_cost(parent_costed_path)
            child_path_cost = parent_path_cost + step_cost
            return (parent_costed_path, (action, child_state, child_path_cost))
        def costed_path2path_cost(self, costed_path):
            if self.is_initial_costed_path(costed_path):
                return path_cost
            else:
                (costed_path_, (action_, state_, path_cost)) = costed_path
            return path_cost
        def costed_path2last_state(self, costed_path):
            if self.is_initial_costed_path(costed_path):
                [state] = costed_path
            else:
                (costed_path_, (action_, state, path_cost_)) = costed_path
            return state
    class Node:
        # costed_path = (initial_state,) | (costed_path, (action, state, path_cost))
        # public: state, path_cost
        def __init__(self, problem, costed_path):
            # private
            self.problem = problem
            # protected
            self.costed_path = costed_path
            # public
            self.state = problem.costed_path2last_state(costed_path)
            self.path_cost = problem.costed_path2path_cost(costed_path)
        def to_path(self):
            costed_path = self.costed_path
            reversed_path = []
            while not problem.is_initial_costed_path(costed_path):
                costed_path, (action, state, path_cost) = costed_path
                reversed_path.append((action, state))
            else:
                [initial_state] = costed_path
            reversed_path.reverse(); path = reversed_path; del reversed_path
            return (initial_state, path)


    class ChildNode(Node):
        # public: state, path_cost, parent_node, action
        def __init__(self, problem, parent_node:Node, action):
            parent_state = parent_node.state
            parent_costed_path = parent_node.costed_path
            child_costed_path = problem.make_child_costed_path(parent_costed_path, action)

            super().__init__(child_costed_path, action)
            # public
            self.parent_node = parent_node
            self.action = action


    ###################### Agent #########################
    def __init__(self, initial_state):
        self.__actions = UnInitActions
            # UnInitActions | FailureActions | Iter Action
        self.__state = initial_state
            #self.get_the_problem().get_initial_state()
    @property
    def state(self):
        return self.__state
    '''
    @abstractmethod
    def get_the_problem(self):
        # -> .IProblem
        raise NotImplementedError
    '''
    @abstractmethod
    def update_state(self, state, percept):
        # -> state
        raise NotImplementedError
    @abstractmethod
    def formulate_goal(self, state):
        # -> IGoal
        raise NotImplementedError
    @abstractmethod
    def formulate_problem(self, state, goal):
        # -> IProblem
        raise NotImplementedError
    @abstractmethod
    def search(self, problem):
        # -> Iter Action | FailureActions
        raise NotImplementedError
    def accept(self, percept):
        # -> NoAction | Action
        state = self.__state = self.update_state(self.__state, percept)
        actions = self.__actions
        if actions is FailureActions:
            return NoAction
        elif actions is UnInitActions:
            goal = self.formulate_goal(state)
            problem = self.formulate_problem(state, goal)
            actions = self.__actions = self.search(problem)
            if actions is FailureActions:
                return NoAction
            else:
                assert iter(actions) is actions

        for action in actions:
            return action
        else:
            return NoAction

