
'''
Artificial Intelligence -- A Modern Approach (3ed)(2010)(Stuart Russell)
3 SOLVING PROBLEMS BY SEARCHING
Section 3.3. Searching for Solutions
page 77
Figure 3.7
'''

from .ISimple_Problem_Solving_Agent__OpenLoop import \
    ISimple_Problem_Solving_Agent__OpenLoop as Agent

def tree_search(problem:Agent.IProblem):
    initial_state = problem.get_initial_state()
    initial_paired_path = () # path = () | (path, (action, state))
    def make_path(paired_path):
        reversed_path = []
        while paired_path:
            paired_path, (action, state) = paired_path
            reversed_path.append((action, state))
        reversed_path.reverse(); path = reversed_path; del reversed_path
        return path

    frontier = [((), initial_state)]
    while frontier:
        paired_path, state = node = frontier.pop() # how to choose??
        if problem.is_goal_state(state):
            return (initial_state, make_path(paired_path))

        actions = problem.get_actions_at(state)
        for action in actions:
            successor = problem.transition_model_result_successor_state_of(state, action)
            child_paired_path = (paired_path, (action, successor))
            child_node = (child_paired_path, successor)
            frontier.append(child_node) # how to add??
    else:
        return Agent.FailureActions
