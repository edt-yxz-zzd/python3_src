
class Flippable:
    __slots__ = 'normal_string flip_string'.split()
    def __init__(self, normal_string, flip_string):
        if type(normal_string) is not str: raise TypeError
        if type(flip_string) is not str: raise TypeError
        self.normal_string = normal_string
        self.flip_string = flip_string
    @property
    def flip(self):
        return Flippable(self.flip_string, self.normal_string)
    def __invert__(self):
        return self.flip
    def __str__(self):
        return self.normal_string
    def __repr__(self):
        raise NotImplementedError
def _test_Flippable():
    flippable = Flippable('a', 'b')
    assert str(flippable) == 'a'
    assert str(flippable.flip) == 'b'
    assert str(flippable.flip.flip) == 'a'
_test_Flippable()

