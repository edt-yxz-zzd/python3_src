
__all__ = '''
    Vertex2TwoColor__set
    '''.split()



from .IVertex2TwoColor import IVertex2TwoColor
from .abc import override


class Vertex2TwoColor__set(IVertex2TwoColor):
    def __init__(self, underlying_set):
        self.underlying_set = underlying_set
    @override
    def is_vertex_colored_WHITE(self, vertex):
        return vertex in self.underlying_set
    @override
    def set_vertex_color_WHITE(self, vertex):
        self.underlying_set.add(vertex)

