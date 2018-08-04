
__all__ = '''
    iter_postfix_dfs_ordering
    iter_prefix_dfs_ordering
    iter_reversed_topological_ordering
'''.split()

from .DAG import iter_reversed_topological_ordering

def iter_postfix_dfs_ordering(g, roots):
    return (path[0] for case, path in dfs(g, roots) if case == EXIT)
def iter_prefix_dfs_ordering(g, roots):
    return (path[0] for case, path in dfs(g, roots) if case == ENTER)




    


