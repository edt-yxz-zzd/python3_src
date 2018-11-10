
class Mapping2Callable:
    def __init__(self, mapping):
        self.mapping = mapping
    def __call__(self, key):
        return self.mapping[key]
    def __repr__(self):
        cls = type(self)
        return f'{cls.__name__!s}({self.mapping!r})'


