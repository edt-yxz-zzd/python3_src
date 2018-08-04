

__all__ = '''
    find_top_most_vertices
    find_top_most_classes
    '''.split()

def find_top_most_vertices(big_endian_vertices, __le__):
    # big_endian_vertices s.t. # big-endian
    #   i < j ==>> not(big_endian_vertices[i] < big_endian_vertices[j])
    # return big_endian_vertices2 s.t.
    #   i != j ==>> not(big_endian_vertices2[i] < big_endian_vertices2[j])
    # O(n^2)
    reversed_vertices = list(big_endian_vertices)
    reversed_vertices.reverse() # little-endian

    big_endian_vertices = [] # big-endian
    while reversed_vertices:
        big = reversed_vertices.pop()
        big_endian_vertices.append(big)
        reversed_vertices = [small for small in reversed_vertices
                                    if not __le__(small, big)] # little-endian
    return big_endian_vertices




def find_top_most_classes(big_endian_bases):
    return find_top_most_vertices(big_endian_bases, issubclass)


