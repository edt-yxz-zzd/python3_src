
__all__ = '''
    is_DAG
    iter_reversed_topological_ordering
    find_one_cycle
'''.split()


#from .dfs import *
from seed.graph.dfs import dfs, ENTER, EXIT, BACK, CROSS_OR_FORWARD
from seed.types.pair_based_leftward_list import iter_leftward_list

def is_DAG(g, roots=None):
    return not _find_one_cycle(g, roots) # bug : forgot "not"

def iter_reversed_topological_ordering(g, roots=None):
    for case, path in dfs(g, roots):
        if case == EXIT:
            yield path[0]
        elif case == BACK:
            raise ValueError('Not a DAG : {}'.format(find_one_cycle(dag, roots)))



def find_one_cycle(g, roots=None):
    'return [] or [v1, v2, ...vn] where v1->v2->...->vn->v1'
    path = _find_one_cycle(g, roots)
    ls = []
    if path:
        u, path = path
        for v in iter_leftward_list(path): # bug : forgot "iter_leftward_list"
            ls.append(v)
            if v == u:
                break
        else:
            raise logic-error
        ls.reverse()
        assert ls
    return ls

def _find_one_cycle(g, roots):
    for case, path in dfs(g, roots):
        if case == BACK:
            return path

from seed.graph.DAG import iter_reversed_topological_ordering, is_DAG, find_one_cycle
from seed.graph.DAG import *



