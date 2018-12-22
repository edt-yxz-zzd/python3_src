

__all__ = '''
    Vertex2TwoColor__seq
    '''.split()



from .IVertex2TwoColor import IVertex2TwoColor
from .abc import override

class Vertex2TwoColor__seq(IVertex2TwoColor):
    def __init__(self, underlying_seq, WHITE):
        self.underlying_seq = underlying_seq
        self.WHITE = WHITE
    @override
    def is_vertex_colored_WHITE(self, vertex):
        return self.underlying_seq[vertex] is self.WHITE
    @override
    def set_vertex_color_WHITE(self, vertex):
        self.underlying_seq[vertex] = self.WHITE



