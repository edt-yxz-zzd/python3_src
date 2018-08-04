

__all__ = '''
    TopMostBases_Meta
    get_top_most_bases
    '''.split()

from .find_top_most_vertices import find_top_most_classes


def get_top_most_bases(cls):
    assert isinstance(cls, TopMostBases_Meta)
    return cls.__top_most_bases__

class TopMostBases_Meta(type):
    # self.__top_most_bases__
    def __new__(meta_cls, name, bases, namespace, **kwargs):
        self = super(__class__, meta_cls).__new__(meta_cls, name, bases, namespace, **kwargs)
        #mro = get_mro(self)
        bases = find_top_most_classes(self.__bases__)
        self.__top_most_bases__ = tuple(bases)
        return self


