
'''
StdVertexEchoMap(n) == {i:i for i in range(n)}
'''
__all__ = ['StdVertexEchoMap']

from collections.abc import Mapping
class StdVertexEchoMap(Mapping):
    def __init__(self, num_vertices):
        if type(num_vertices) is not int: raise TypeError
        if num_vertices < 0: raise TypeError
        self.__num_vertices = num_vertices
    def __len__(self):
        return self.__num_vertices
    def __getitem__(self, key):
        if type(key) is int and 0 <= key < len(self):
            return key
        raise KeyError

    def __iter__(self):
        return iter(range(len(self)))

if __name__ == '__main__':
    m = StdVertexEchoMap(3)
    assert len(m) == 3
    assert dict(m) == {i:i for i in range(3)}
    assert m[2] == 2
    for k,v in m.items(): print(k,v)

