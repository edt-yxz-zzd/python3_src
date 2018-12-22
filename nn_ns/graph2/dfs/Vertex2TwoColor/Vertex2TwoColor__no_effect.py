
__all__ = '''
    Vertex2TwoColor__no_effect
    the_vertex2two_color__no_effect
    '''.split()

from .IVertex2TwoColor import IVertex2TwoColor
from .abc import override

class Vertex2TwoColor__no_effect(IVertex2TwoColor):
    @override
    def is_vertex_colored_WHITE(self, vertex):
        return False
    @override
    def set_vertex_color_WHITE(self, vertex):
        pass
the_vertex2two_color__no_effect = Vertex2TwoColor__no_effect()


