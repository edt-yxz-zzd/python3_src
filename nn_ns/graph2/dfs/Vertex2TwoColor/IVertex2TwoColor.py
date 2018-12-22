

__all__ = '''
    IVertex2TwoColor
    '''.split()

from .abc import ABC, abstractmethod
class IVertex2TwoColor(ABC):
    # like a set
    #   Vertex2TwoColor__set
    @abstractmethod
    def is_vertex_colored_WHITE(self, vertex):
        # vertex -> bool
        pass
    @abstractmethod
    def set_vertex_color_WHITE(self, vertex):
        # vertex -> None
        pass



