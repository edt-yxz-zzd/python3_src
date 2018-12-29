
class make_vertex2degree:
    @classmethod
    def from_hedge2vertex(cls, *, num_vertices, hedge2vertex):
        if not all(0 <= u < num_vertices for u in hedge2vertex): raise ValueError

        vertex2degree = [0]*num_vertices
        for vertex in hedge2vertex:
            vertex2degree[vertex] += 1
        assert sum(vertex2degree) == len(hedge2vertex)
        return tuple(vertex2degree)

