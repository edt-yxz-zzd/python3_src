
__all__ = '''
    incomplete_u2vtc_to_vertice_set
    incomplete_u2vtc_to_iter_duplicated_vertices
    '''.split()

from itertools import chain

def incomplete_u2vtc_to_iter_duplicated_vertices(u2vtc):
    # all vertices not only keys, and maybe duplicated
    return chain(u2vtc, chain.from_iterable(u2vtc.values()))
def incomplete_u2vtc_to_vertice_set(u2vtc):
    # all vertices not only keys
    return set(incomplete_u2vtc_to_iter_duplicated_vertices(u2vtc))


